# Anatomy

Free, downloadable Claude skills for GTM and marketing teams — competitor
intelligence, ABM, AEO, and more. Read what a skill does, download the
`.md` file, drag it into any Claude conversation.

Live site: served via GitHub Pages from this repo's `main` branch.

## Structure

```
index.html              # Getting Started (home) — hero, 3-step onboarding, Claude Setup Guide
marketing.html          # Marketing-track skills
go-to-market.html       # Go-To-Market-track skills
assets/styles.css        # shared styles across all 3 pages
assets/site.js           # shared render/filter/modal logic across all 3 pages
skills/<slug>/skill.md   # one skill per folder; front-matter + full write-up
```

Still no build step — just static HTML/CSS/JS shared via plain `<link>`/`<script>`
tags, no bundler. Each page's `SKILLS`/`CATEGORIES` arrays are inlined per page
since which skills appear on which page differs.

`index.html` also carries the Claude Setup Guide (formerly a standalone
`playbook.html`) — Getting Started / AI 101 / Best Practices sections with
their own in-page anchor nav, appended below the 3-step onboarding.

Each `skill.md` starts with front-matter (`title`, `status`, `summary`,
`category`, `audience`). Only `status: published` skills belong here —
this repo is public.

## Where content comes from

Skills are authored and reviewed in a separate private repo
([`brain`](https://github.com/rlwbruce-byte/brain)) and promoted here
deliberately, one at a time, once finished. This repo has no automated
sync with `brain` or with `rachelwbruce` (Rachel's personal site) — each
is an independently versioned repo with its own git remote. See
`CLAUDE.md` for details.

## Brand

Rachel Bruce's typography and editorial voice (Anton / Space Grotesk /
IBM Plex Mono), paired with an "Amber Circuit" palette — graphite ground
(`#0B0E12`), amber accent (`#F5A623`) — chosen to feel tech-forward
without directly replicating Continuous's brand colors.
