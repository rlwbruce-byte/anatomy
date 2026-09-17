# One-pager

A print-ready, single-page practice overview for GTM Anatomy: what the practice
does, the four offerings with published pricing, who it is for, and the booking
call to action. Built to be emailed or printed as a leave-behind.

```sh
python3 one-pager/build.py     # -> one-pager/gtm-anatomy-one-pager.pdf
```

- `one-pager.html` is the source. Letter, 8.5x11in, designed as one fixed sheet.
- `fonts.css` carries Anton, Space Grotesk and IBM Plex Mono as base64
  `@font-face` rules. Headless Chromium here cannot reach fonts.googleapis.com
  and silently falls back to a system sans, which puts the wordmark in the wrong
  face, so the fonts are embedded rather than linked.
- `build.py` fails rather than writing a PDF if the content no longer fits. The
  sheet is a flex column, so an overfull page shrinks and clips the masthead and
  footer instead of growing: it once sliced the qualifier line under the
  masthead in half. The check measures the sheet and every pinned band.

The prices here are one of the five places pricing lives. See "Offering names
and pricing" in the repo CLAUDE.md before changing any figure.
