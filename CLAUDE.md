# CLAUDE.md

Guidance for Claude Code when working in this repo.

## What this repo is

`anatomy` is the public-facing site hosting free Claude skills for GTM and
marketing teams. It is served via GitHub Pages directly from `main` — no
build step. The site is 3 static pages sharing `assets/styles.css` and
`assets/site.js`:

- `index.html` — Getting Started (home): hero (no CTA buttons — the top
  page-nav is the only navigation), 3-step onboarding, and the Claude Setup
  Guide (its own in-page anchor nav + Getting Started/AI 101/Best Practices
  sections). No skills grid.
- `marketing.html` — skills tagged for the Marketing track.
- `go-to-market.html` — skills tagged for the Go-To-Market (GTM) track.

There is no separate `playbook.html` — that content lives on `index.html`.
Don't re-split it into its own page without the user asking.

## Repo isolation — read before syncing anything

This repo, [`brain`](https://github.com/rlwbruce-byte/brain) (private,
internal), and `rachelwbruce` (Rachel's personal site) are three
independently versioned repos, each with its own git remote. There is no
git submodule, subtree, or automated CI sync between them, and none should
be added without the user explicitly asking for it.

Content moves from `brain` to `anatomy` by deliberate, manual promotion
only: copy the finished skill's files over, adapt as needed for public
consumption (strip internal notes, no proprietary agent internals), commit
and push here as its own step. Never script a bulk sync across repos.

## Adding a new skill

1. Create `skills/<slug>/skill.md` with front-matter: `title`, `status:
   published`, `summary`, `category`, `audience` (`Marketing Leaders` or
   `GTM Leaders` — determines which page it belongs on).
2. Add an entry to the `SKILLS` array in `marketing.html` or
   `go-to-market.html` (whichever matches `audience`) — slug, title,
   category, summary, perfectFor bullets.
3. If it's a new category, add it to that page's `CATEGORIES` array too.
4. Update the stats (`renderStats` call) on both that page and `index.html`
   if the total skill/track counts changed.

## Brand

- Palette: graphite `#0B0E12` / amber `#F5A623` (`#C2760D` deep) — "Amber
  Circuit," chosen deliberately to avoid matching Continuous's navy/violet
  system while keeping a similar tech-forward, dark-ground feel.
- Type: Anton (display, headers only), Space Grotesk (body), IBM Plex Mono
  (labels, kickers, category tags) — carried over from Rachel's personal
  site.
- Voice: confident, specific, no filler. See `brain/CLAUDE.md` for the
  do/don't examples this was built from.
