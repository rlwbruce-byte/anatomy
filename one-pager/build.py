#!/usr/bin/env python3
"""Render the GTM Anatomy one-pager to a print-ready PDF.

The fonts are embedded as base64 @font-face rules in fonts.css, because headless
Chromium in this sandbox cannot reach fonts.googleapis.com and silently falls
back to a system sans, which puts the wordmark in the wrong face.

Usage:  python3 one-pager/build.py
"""
import os, sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "one-pager.html")
OUT  = os.path.join(HERE, "gtm-anatomy-one-pager.pdf")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 816, "height": 1056})
    pg.goto("file://" + SRC, wait_until="load")
    pg.wait_for_timeout(600)          # let the embedded faces settle
    # The sheet is fixed at 8.5x11in. Checking .main alone is not enough: the
    # sheet is a flex column, so an overfull page shrinks the masthead and
    # footer and clips them instead of growing, which once sliced the qualifier
    # line under the masthead clean in half. Measure the sheet, and assert no
    # pinned band is clipping its own content.
    m = pg.evaluate("""() => {
      const sh = document.querySelector('.sheet');
      const clipped = [];
      for (const sel of ['.top', '.foot', '.main']) {
        const e = document.querySelector(sel);
        if (e.scrollHeight > Math.round(e.getBoundingClientRect().height) + 1) clipped.push(sel);
      }
      return {scroll: sh.scrollHeight,
              box: Math.round(sh.getBoundingClientRect().height),
              clipped};
    }""")
    problems = []
    if m["scroll"] > m["box"]:
        problems.append(f"content overflows the sheet by {m['scroll'] - m['box']}px")
    if m["clipped"]:
        problems.append("clipped bands: " + ", ".join(m["clipped"]))
    if problems:
        print("FAILED: " + "; ".join(problems), file=sys.stderr)
        b.close()
        sys.exit(1)
    print(f"fits: {m['scroll']}px of {m['box']}px")
    pg.pdf(path=OUT, width="8.5in", height="11in", print_background=True,
           margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print(f"{OUT}  ({os.path.getsize(OUT)/1024:.0f} KB)")
