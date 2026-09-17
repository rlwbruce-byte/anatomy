#!/usr/bin/env python3
"""Generate the markdown twin for an HTML page.

Every HTML page on the site has a markdown twin at the same path with `.md`
instead of `.html`, indexed by llms.txt and concatenated into llms-full.txt.
The twins are scraped from the HTML, so a markup pattern this extractor does
not recognise silently vanishes from the answer-engine surface. That has
happened once already (h3.persona-name reached index.md as unlabelled
paragraphs). After adding a new heading or label class, add it to the maps
below and read the regenerated .md to confirm the label is there.

Usage:
    python3 scripts/gen-md-twins.py about.html offerings/index.html
    python3 scripts/gen-md-twins.py --all
"""

import html
import os
import re
import sys
from html.parser import HTMLParser

SITE = "https://gtmanatomy.ai"

# Never reaches the answer-engine surface: chrome, scripts, and the internal
# placeholder panels that mark content still pending client input.
SKIP_TAGS = {"script", "style", "svg", "noscript", "head"}
SKIP_CLASSES = {"global-nav", "site-footer", "placeholder-block", "gn-drop"}

# Leaf elements whose text becomes one markdown block.
LEAF_TAGS = {"h1", "h2", "h3", "h4", "h5", "p", "li", "blockquote", "cite",
             "td", "th", "figcaption"}

# li variants that wrap block children rather than holding text themselves.
CONTAINER_LI = {"spec-item"}


def classes(attrs):
    return set((dict(attrs).get("class") or "").split())


class Twin(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip_depth = 0
        self.skip_tag = None
        self.leaf = None          # (tag, classes)
        self.buf = []
        self.depth = 0
        self.row = None           # accumulating a table row
        self.table = None         # accumulating a table

    # -- helpers ---------------------------------------------------------
    def emit(self, text):
        if text:
            self.out.append(text)

    def flush(self):
        tag, cls = self.leaf
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.leaf, self.buf = None, []
        if not text:
            return

        if self.row is not None:
            self.row.append(text)
            return

        if tag == "h1":
            self.emit(f"# {text}")
        elif tag == "h2":
            # h2.section-title is the section's headline; the eyebrow above it
            # carries the section name and is emitted as the ## level.
            self.emit(f"### {text}")
        elif tag == "h3":
            # Role tiles and offer cards label a thing, not a section.
            if "persona-name" in cls:
                self.emit(f"**{text}**")
            else:
                self.emit(f"### {text}")
        elif tag in ("h4", "h5"):
            self.emit(f"**{text}**")
        elif tag == "li":
            self.emit(f"- {text}")
        elif tag == "blockquote":
            self.emit(f"> {text}")
        elif tag == "cite":
            self.emit(f"— {text}")
        else:
            self.emit(text)

    # -- parser ----------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        cls = classes(attrs)
        if self.skip_depth:
            if tag == self.skip_tag:
                self.skip_depth += 1
            return
        if tag in SKIP_TAGS or (cls & SKIP_CLASSES):
            self.skip_depth, self.skip_tag = 1, tag
            return

        if tag == "table":
            self.table = []
        elif tag == "tr" and self.table is not None:
            self.row = []

        if self.leaf:
            return  # inline markup inside a leaf; text is collected as-is

        # Labels carried on non-heading elements.
        if tag in ("div", "span", "p"):
            if "kicker" in cls or "pill" in cls:
                self.leaf, self.buf, self.depth = (tag, cls), [], 0
                self._label = ""
                return
            # Commercial terms are labelled, so the figure never reaches an
            # answer engine as a bare number with no idea what it prices.
            if "offer-price" in cls:
                self.leaf, self.buf, self.depth = (tag, cls), [], 0
                self._label = "Investment: "
                return
            if "offer-timeline" in cls:
                self.leaf, self.buf, self.depth = (tag, cls), [], 0
                self._label = "Timeline: "
                return
            if "section-eyebrow" in cls:
                self.leaf, self.buf, self.depth = ("eyebrow", cls), [], 0
                return

        if tag in LEAF_TAGS:
            if tag == "li" and (cls & CONTAINER_LI):
                return
            self.leaf, self.buf, self.depth = (tag, cls), [], 0

    def handle_endtag(self, tag):
        if self.skip_depth:
            if tag == self.skip_tag:
                self.skip_depth -= 1
                if not self.skip_depth:
                    self.skip_tag = None
            return

        if self.leaf:
            ltag = self.leaf[0]
            if tag == ltag or (ltag == "eyebrow" and tag in ("div", "span")):
                if ltag == "eyebrow":
                    text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
                    self.leaf, self.buf = None, []
                    if text:
                        self.emit(f"## {text}")
                    return
                if ltag in ("div", "span", "p") and getattr(self, "_label", None) is not None:
                    text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
                    label = self._label
                    self.leaf, self.buf, self._label = None, [], None
                    if text:
                        self.emit(f"_{label}{text}_")
                    return
                self.flush()
                return

        if tag == "tr" and self.row is not None:
            if self.row:
                self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table is not None:
            if self.table:
                head, *body = self.table
                rows = ["| " + " | ".join(head) + " |",
                        "|" + "|".join(" --- " for _ in head) + "|"]
                for r in body:
                    r = r + [""] * (len(head) - len(r))
                    rows.append("| " + " | ".join(r[:len(head)]) + " |")
                self.emit("\n".join(rows))
            self.table = None

    def handle_data(self, data):
        if self.skip_depth or not self.leaf:
            return
        self.buf.append(data)


def source_url(path):
    if path == "index.html":
        return f"{SITE}/"
    if path.endswith("/index.html"):
        return f"{SITE}/{path[:-len('index.html')]}"
    return f"{SITE}/{path}"


def meta(doc, name):
    m = re.search(rf'<meta name="{name}" content="([^"]*)"', doc)
    return html.unescape(m.group(1)) if m else ""


def generate(path):
    doc = open(path, encoding="utf-8").read()
    if path in CLIENT_RENDERED or "renderSkillsGrid" in doc:
        raise SystemExit(
            f"refusing {path}: its cards are rendered from the SKILLS array at "
            f"runtime, so a static scrape would empty its twin. Edit the .md by "
            f"hand alongside the SKILLS entry.")
    title = html.unescape(re.search(r"<title>(.*?)</title>", doc, re.S).group(1)).strip()
    desc = meta(doc, "description")

    # Body only: everything the reader sees, chrome stripped by the parser.
    body = doc[doc.index("<body"):] if "<body" in doc else doc

    t = Twin()
    t.feed(body)

    head = [f"# {title}", "", f"> {desc}", "", f"Source: {source_url(path)}", "", "---", "", ""]
    md = "\n".join(head) + "\n\n".join(t.out) + "\n"
    md = re.sub(r"\n{3,}", "\n\n", md)
    out = path[:-len(".html")] + ".md"
    open(out, "w", encoding="utf-8").write(md)
    return out, len(t.out)


# The three library pages build their skill cards client-side from the SKILLS
# array, so there is nothing in the static HTML to scrape and this extractor
# would silently empty their twins. They are maintained by hand alongside the
# SKILLS entry (see "Adding a new skill" in CLAUDE.md) and are refused below.
CLIENT_RENDERED = {"getting-started.html", "marketing.html", "go-to-market.html"}

ALL = ["index.html", "about.html", "contact.html", "offerings/index.html",
       "offerings/anatomy-scan.html", "offerings/anatomy-os.html",
       "offerings/ai-sprint.html", "offerings/fractional-partner.html"]

if __name__ == "__main__":
    args = sys.argv[1:]
    targets = ALL if args == ["--all"] else args
    if not targets:
        sys.exit(__doc__)
    for p in targets:
        out, n = generate(p)
        print(f"{out:38s} {n} blocks")
