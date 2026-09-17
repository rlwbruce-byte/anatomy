#!/usr/bin/env python3
"""Generate the GTM Anatomy 'A.' mark and every favicon rendered from it.

The letter is drawn as geometry, not type: two tapered strokes and a crossbar
on a 512 grid. Nothing here depends on a font being installed or on
fonts.googleapis.com being reachable, which is what broke previous attempts at
rendering brand assets in a headless browser.

    python3 assets/logo/build.py            # rewrite the SVGs and the PNGs
    python3 assets/logo/build.py --svg-only # skip the PNGs (no Chromium needed)

PNG rasterisation shells out to Playwright's Chromium. Every file it writes is
listed in FILES below.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.dirname(HERE)

GRAPHITE = "#0B0E12"   # --graphite
PAPER    = "#FAF6F2"   # --paper
AMBER    = "#F5A623"   # --amber

# The mark at display sizes: high stroke contrast, generous corner radius.
REGULAR = dict(radius=114, T=98, B=420, apex_w=12, a_left=56, a_width=316,
               l_w=28, r_w=56, bar_top=330, bar_h=17, dot=52, gap=28)

# Optically sized for 16 and 32px, where the display cut's thin stroke and
# hairline crossbar fall below one device pixel and the letter turns to mush:
# bigger A in the tile, thicker thins, tighter corner radius, larger dot.
SMALL = dict(radius=76, T=80, B=438, apex_w=16, a_left=40, a_width=344,
             l_w=42, r_w=64, bar_top=336, bar_h=26, dot=66, gap=22)


def letter_a(T, B, apex_c, apex_w, l_out, l_w, r_out, r_w, bar_top, bar_h):
    """Path data for the A: left stroke, right stroke, crossbar.

    T/B        apex top and baseline
    apex_c     x the two strokes converge on; apex_w the width of the flat there
    l_out/l_w  left stroke's outer edge and horizontal width at the baseline
    r_out/r_w  same for the right stroke
    bar_top    top of the crossbar; bar_h its thickness
    """
    a1, a2 = apex_c - apex_w / 2, apex_c + apex_w / 2
    left  = f"M{a1:.1f} {T}L{a2:.1f} {T}L{l_out + l_w:.1f} {B}L{l_out:.1f} {B}Z"
    right = f"M{a1:.1f} {T}L{a2:.1f} {T}L{r_out:.1f} {B}L{r_out - r_w:.1f} {B}Z"

    def edge(x_top, x_base, y):                 # x of a stroke edge at height y
        return x_top + (x_base - x_top) * (y - T) / (B - T)

    # Both strokes splay as they fall, so each one's outer edge is at its
    # narrowest at the bar's TOP. Ending the bar there buries it in the stroke
    # for the bar's whole depth instead of letting a corner poke out.
    x1 = edge(a1, l_out, bar_top)
    x2 = edge(a2, r_out, bar_top)
    bar = (f"M{x1:.1f} {bar_top}L{x2:.1f} {bar_top}"
           f"L{x2:.1f} {bar_top + bar_h}L{x1:.1f} {bar_top + bar_h}Z")
    return [left, right, bar]


def build(size=512, plate=True, scale=1.0, cut=REGULAR):
    """One SVG of the mark.

    plate  draw the graphite tile behind the letter (False leaves it clear, for
           placing the mark on a graphite ground of its own)
    scale  shrink the letter within the tile, for icons a platform re-masks
    """
    c = dict(cut)
    radius = c.pop("radius")
    T, B, dot, gap = c["T"], c["B"], c["dot"], c["gap"]
    l_out  = c["a_left"]
    r_out  = c["a_left"] + c["a_width"]
    apex_c = c["a_left"] + c["a_width"] * 0.495
    paths  = letter_a(T, B, apex_c, c["apex_w"], l_out, c["l_w"], r_out,
                      c["r_w"], c["bar_top"], c["bar_h"])

    dot_x = r_out + gap
    body  = "".join(f'<path d="{d}" fill="{PAPER}"/>' for d in paths)
    body += (f'<rect x="{dot_x:.1f}" y="{B - dot}" width="{dot}" height="{dot}"'
             f' rx="2" fill="{AMBER}"/>')

    # Centre the A and its full stop as one unit, then scale about the middle.
    shift = (512 - ((dot_x + dot) - l_out)) / 2 - l_out
    mid   = (T + B) / 2
    tf    = f"translate({shift:.1f} 0)"
    if scale != 1.0:
        tf = f"translate(256 {mid:.1f}) scale({scale}) translate(-256 {-mid:.1f}) " + tf

    tile = (f'<rect width="512" height="512" rx="{radius}" fill="{GRAPHITE}"/>'
            if plate else "")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
            f'width="{size}" height="{size}" role="img" '
            f'aria-label="GTM Anatomy">{tile}'
            f'<g transform="{tf}">{body}</g></svg>')


# path -> how to draw it. PNG entries carry the pixel size they rasterise at.
FILES = [
    # Vector sources, kept so the mark can be re-cut without this script.
    ("logo/mark.svg",        None, dict()),
    ("logo/mark-small.svg",  None, dict(cut=SMALL)),
    ("logo/mark-square.svg", None, dict(cut=dict(REGULAR, radius=0), scale=0.92)),
    ("logo/mark-clear.svg",  None, dict(plate=False)),

    # What the pages actually link. favicon.svg takes the small cut too: a
    # browser that supports it uses it at 16px as well, which is exactly where
    # the display cut's hairlines fail.
    ("favicon.svg",     None, dict(cut=SMALL)),
    ("favicon-16.png",    16, dict(cut=SMALL)),
    ("favicon-32.png",    32, dict(cut=SMALL)),
    ("favicon-192.png",  192, dict()),
    # iOS rounds the touch icon itself, so hand it a square plate with the
    # letter pulled in far enough that its own mask cannot clip a foot.
    ("favicon-180.png",  180, dict(cut=dict(REGULAR, radius=0), scale=0.92)),
]


def rasterise(jobs):
    """jobs: list of (svg_markup, out_path, px). Screenshots each in Chromium."""
    script = os.path.join(HERE, "_shot.js")
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump([{"svg": s, "out": o, "px": p} for s, o, p in jobs], fh)
        payload = fh.name
    try:
        subprocess.run(["node", script, payload], check=True)
    finally:
        os.unlink(payload)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--svg-only", action="store_true",
                    help="write the SVGs but skip Chromium rasterisation")
    args = ap.parse_args()

    jobs = []
    for name, px, kw in FILES:
        out = os.path.join(ASSETS, name)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if px is None:
            with open(out, "w") as fh:
                fh.write(build(**kw) + "\n")
            print("wrote", os.path.relpath(out, os.path.dirname(ASSETS)))
        else:
            jobs.append((build(size=px, **kw), out, px))

    if args.svg_only or not jobs:
        return
    rasterise(jobs)
    for _, out, _ in jobs:
        print("wrote", os.path.relpath(out, os.path.dirname(ASSETS)))


if __name__ == "__main__":
    sys.exit(main())
