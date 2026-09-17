#!/usr/bin/env python3
"""Build a self-contained review copy of a site page, for publishing as an Artifact.

The live pages pull their CSS, JS and fonts from root-relative paths, and an
Artifact is a single file served from a different origin, so everything has to
come inline and every internal link has to become absolute.

One thing genuinely cannot survive the trip: the Calendly embed. The Artifact
CSP admits scripts only from a short allowlist, and assets.calendly.com is not
on it, so the widget would fail silently and read as a broken calendar. It is
replaced by a clearly marked stand-in of the same height that says so.

Usage:
    python3 scripts/make-review-artifact.py contact.html /tmp/contact-review.html
"""

import os
import re
import sys

SITE = "https://gtmanatomy.ai"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CALENDLY_STANDIN = """
  <div class="calendly-wrap">
    <div class="review-standin">
      <div class="review-standin-label">Calendly embed</div>
      <p>The booking widget cannot load in this review copy: an Artifact only
      runs scripts from a short allowlist, and Calendly's host is not on it.
      On the live page this is the inline calendar, themed to the brand tokens
      (<code>faf6f2</code> paper, <code>0b0e12</code> graphite,
      <code>f5a623</code> amber), sitting directly on the page rather than in a
      card.</p>
      <p class="review-standin-note">Everything else on this page is the real
      markup and the real stylesheet.</p>
    </div>
  </div>
"""

STANDIN_CSS = """
/* review copy only: stands in for the Calendly embed, which the Artifact CSP blocks */
.review-standin{ border:1px dashed var(--amber-deep); border-radius:6px; background:var(--paper-dim);
  padding:30px 28px; min-height:340px; display:flex; flex-direction:column; justify-content:center; gap:12px; }
.review-standin-label{ font-family:var(--mono); font-size:10.5px; text-transform:uppercase;
  letter-spacing:.14em; color:var(--amber-deep); }
.review-standin p{ font-size:14px; line-height:1.65; color:var(--ink-soft); max-width:62ch; }
.review-standin code{ font-family:var(--mono); font-size:12.5px; color:var(--ink); }
.review-standin-note{ font-family:var(--mono); font-size:11.5px; }
"""


def build(page, out):
    src = open(os.path.join(ROOT, page), encoding="utf-8").read()
    css = open(os.path.join(ROOT, "assets/styles.css"), encoding="utf-8").read()
    js  = open(os.path.join(ROOT, "assets/site.js"), encoding="utf-8").read()

    body = src[src.index("<body>") + len("<body>"): src.rindex("</body>")]

    # Drop the Calendly widget and its script; leave a marked stand-in.
    body, n = re.subn(r'<div class="calendly-wrap">.*?</script>\s*</div>',
                      CALENDLY_STANDIN.strip() + "\n", body, flags=re.S, count=1)
    assert n == 1, "calendly wrap not matched"
    # The fallback link below the widget is the page's safety net; losing it
    # would make the review copy misrepresent the page.
    assert "Calendar not loading" in body, "fallback link was swallowed"
    body = re.sub(r'<script[^>]*calendly[^>]*>\s*</script>', "", body, flags=re.I)

    # Same rewrite inside the script: it builds links in template literals.
    js = re.sub(r'href="/(?!/)', f'href="{SITE}/', js)

    # site.js goes in exactly where its tag sat: the page's inline calls run
    # after it, and appending it at the end instead leaves setActiveNav
    # undefined at the moment the page calls it.
    assert '<script src="/assets/site.js"></script>' in body, "site.js tag not found"
    body = body.replace('<script src="/assets/site.js"></script>',
                        "<script>\n" + js + "\n</script>")

    # Root-relative links have no meaning off-origin: point them at the live site.
    body = re.sub(r'href="/(?!/)', f'href="{SITE}/', body)
    body = re.sub(r'src="/(?!/)',  f'src="{SITE}/', body)

    title = re.search(r"<title>(.*?)</title>", src, re.S).group(1).strip()

    parts = [
        f"<title>{title}</title>",
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:'
        'wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">',
        "<style>\n" + css + STANDIN_CSS + "\n</style>",
        body.strip(),
    ]
    open(out, "w", encoding="utf-8").write("\n".join(parts) + "\n")
    print(f"{out}  ({os.path.getsize(out)/1024:.0f} KB)  from {page}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
