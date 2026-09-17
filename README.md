# GTM Anatomy

The public site for GTM Anatomy: AI infrastructure for go-to-market teams.
Marketing pages for the practice (home, about, four offerings, contact), plus
the free Claude skills library — read what a skill does, download the `.md`
file, drag it into any Claude conversation.

Live site: **https://gtmanatomy.ai**, served by Vercel from this repo's `main`
branch. No build step — a push to `main` is a deploy.

The old GitHub Pages URL still resolves but no longer serves the site: the
`gh-pages` branch holds redirect stubs that send every path to gtmanatomy.ai.

## Structure

```
index.html                       # Home — hero, what we do, offerings, roles, contact
about.html                       # About — purpose, the foundations, how we work, who it is for
offerings/index.html             # Offerings hub — the four offerings in sequence
offerings/anatomy-scan.html      # Offering 01
offerings/ai-sprint.html      # Offering 03
offerings/anatomy-os.html        # Offering 03
offerings/fractional-partner.html   # Offering 04
                                 #   (pricing published; see CLAUDE.md)
contact.html                     # Contact — form plus what happens next
getting-started.html             # Claude skills: onboarding + Claude Setup Guide
marketing.html                   # Claude skills: Marketing track
go-to-market.html                # Claude skills: Sales track (URL kept, label is Sales)
assets/styles.css                # shared styles across all 11 pages
assets/site.js                   # shared render/filter/modal/contact-form logic
skills/<slug>/skill.md           # one skill per folder; front-matter + full write-up
llms.txt                         # llms.txt index for answer engines
llms-full.txt                    # every page's markdown, concatenated
<page>.md                        # markdown twin of each HTML page
sitemap.xml, robots.txt          # crawl surface
```

Still no build step — just static HTML/CSS/JS shared via plain `<link>`/`<script>`
tags, no bundler. Each skill page's `SKILLS`/`CATEGORIES` arrays are inlined per
page since which skills appear on which page differs.

`getting-started.html` carries the Claude Setup Guide (formerly a standalone
`playbook.html`) — Getting Started / AI 101 / Best Practices sections appended
below the 3-step onboarding. It is also the only page holding skill counts.

Each `skill.md` starts with the four-key front-matter (`name`, `description`,
`created`, `updated`) that Claude validates on upload. See `CLAUDE.md`.

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
