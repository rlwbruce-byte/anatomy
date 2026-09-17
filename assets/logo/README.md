# Logo files

The GTM Anatomy mark is the `A.` lockup: a paper `A` on a graphite tile with the
full stop set as an amber square. It is the compact sibling of the `GTMAnatomy.`
wordmark — the wordmark is live Anton text in the page (`.gn-brand`,
`.footer-brand`), the mark is what goes in a favicon, an app tile, or anywhere the
full wordmark will not fit.

**Everything here is generated. Do not hand-edit the SVGs or the PNGs** — change
`build.py` and re-run it, or the sizes drift out of step with each other.

```
python3 assets/logo/build.py             # rewrite the SVGs and the PNGs
python3 assets/logo/build.py --svg-only  # SVGs only, no Chromium needed
```

## The letter is geometry, not type

`build.py` draws the `A` as two tapered strokes plus a crossbar on a 512 grid.
No font is loaded. That is deliberate: this sandbox cannot reach
fonts.googleapis.com from a headless browser, so anything set as live text
silently falls back to a system face and ships in the wrong letterform. Geometry
renders the same everywhere and can be re-cut at any weight.

`letter_a()` takes the apex, the baseline, each stroke's outer edge and width,
and the crossbar. One subtlety worth keeping: both strokes splay as they fall, so
each one's outer edge is narrowest at the **top** of the crossbar. The bar ends
there on both sides, which buries it in the stroke for its whole depth. End it
anywhere lower and a corner pokes out of the silhouette.

## Two optical cuts

| Cut | Used at | Why |
| --- | --- | --- |
| `REGULAR` | 180, 192 | High stroke contrast, 22% corner radius. The display cut. |
| `SMALL` | 16, 32, `favicon.svg` | Bigger `A` in the tile, thicker thins, heavier crossbar, 15% radius, larger dot. |

At 16px the display cut's thin stroke and hairline crossbar fall below one device
pixel and the letter turns to mush. `favicon.svg` takes the small cut as well,
because a browser that supports an SVG favicon uses it at 16px too — which is
exactly where the display cut fails.

## What each file is for

| File | Use |
| --- | --- |
| `mark.svg` | The display cut, rounded tile. Start here for decks, social avatars, anything large. |
| `mark-small.svg` | The small cut, rounded tile. Source for the 16 and 32 PNGs. |
| `mark-square.svg` | Square plate, letter pulled in 8%. For platforms that apply their own corner mask. |
| `mark-clear.svg` | Letter and dot only, no tile. For placing on a graphite ground of its own. |
| `../favicon.svg` | Linked by every page. Small cut. |
| `../favicon-16.png` `../favicon-32.png` | Tab icon fallback for browsers with no SVG favicon support. |
| `../favicon-192.png` | Android home screen, and the `logo` in the Home page's JSON-LD. |
| `../favicon-180.png` | `apple-touch-icon`. Square plate on purpose: iOS rounds it itself, and a pre-rounded tile would leave black corners under its mask. |

Colours come from the site tokens and are repeated at the top of `build.py`:
graphite `#0B0E12`, paper `#FAF6F2`, amber `#F5A623`. Change them in both places
or the mark stops matching the page.

## Replacing a favicon in place

Browsers cache favicons hard, and these filenames never change. The `<link>` tags
on all eleven pages carry a `?v=N` query string for exactly that reason. **Bump
`N` on every page whenever you regenerate the icons**, or returning visitors keep
the old one. `git grep -n 'favicon.*?v='` finds them all.

`og-image.png` is a separate asset built from the Anton wordmark, not from this
mark. It is not regenerated here.
