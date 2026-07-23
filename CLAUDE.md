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
- `marketing.html` — skills tagged for the Marketing track, plus its own
  Prompts section below the skills grid.
- `go-to-market.html` — skills tagged for the Go-To-Market (GTM) track, plus
  its own Prompts section below the skills grid.

Both `marketing.html` and `go-to-market.html` carry a **Prompts** section
(added 2026-07-22) below the Skills grid — a separate, self-contained zone
for short copy-paste prompts that don't warrant a full Skill file. It's
wrapped in `.guide-section` (the same amber-top-border + tinted-background
"new zone" treatment used for the Claude Setup Guide on `index.html`), with
its own heading, stats row, filter tags, and grid — structurally identical
to the Skills section but visually distinct. It currently ships with one
placeholder card per page (`status: draft` in front-matter) — replace
before treating the section as live content.

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
   `GTM Leaders` — determines which page it belongs on), `created` and
   `updated` (both `YYYY-MM-DD`). Every skill.md must always carry both
   dates; bump `updated` on any content change to that skill (leave
   `created` fixed).
2. Add an entry to the `SKILLS` array in `marketing.html` or
   `go-to-market.html` (whichever matches `audience`) — slug, title,
   category, summary, perfectFor bullets.
3. If it's a new category, add it to that page's `CATEGORIES` array too.
4. Update the stats (`renderStats` call) on both that page and `index.html`
   if the total skill/track counts changed.

## Adding a new prompt

1. Create `prompts/<slug>/prompt.md` with front-matter: `title`, `status:
   published`, `summary`, `category`, `audience` (`Marketing Leaders` or
   `GTM Leaders`), `created` and `updated` (both `YYYY-MM-DD`). Body should
   include a short "What this prompt does" blurb and a fenced code block
   with the literal copy-paste prompt text — the Copy button on the card
   extracts the first fenced block in the file verbatim.
2. Add an entry to the `PROMPTS` array in `marketing.html` or
   `go-to-market.html` (whichever matches `audience`) — slug, title,
   category, summary, perfectFor bullets, `created`/`updated`.
3. If it's a new category, add it to that page's `PROMPT_CATEGORIES` array.
4. Update the `promptStats` `renderStats` call on that page if the count
   changed.
5. Uses the shared `renderPromptsGrid` / `openPrompt` / `copyPrompt`
   functions in `assets/site.js` — same card markup as Skills
   (`.skill-card`), just a different data source and action set (Read /
   Copy / Open Claude.ai instead of Read / Download / Open Claude.ai).

## Brand

- Palette: graphite `#0B0E12` / amber `#F5A623` (`#C2760D` deep) — "Amber
  Circuit," chosen deliberately to avoid matching Continuous's navy/violet
  system while keeping a similar tech-forward, dark-ground feel.
- Type: Anton (display, headers only), Space Grotesk (body), IBM Plex Mono
  (labels, kickers, category tags) — carried over from Rachel's personal
  site.
- Voice: confident, specific, no filler. See `brain/CLAUDE.md` for the
  do/don't examples this was built from.
