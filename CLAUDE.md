# CLAUDE.md

Guidance for Claude Code when working in this repo.

## What this repo is

`anatomy` is the public-facing site hosting free Claude skills for GTM and
marketing teams. It is served via GitHub Pages directly from `main` — no
build step. The site is 3 static pages sharing `assets/styles.css` and
`assets/site.js`:

- `index.html` — Getting Started (home): hero, 3-step onboarding, and the
  Claude Setup Guide (its own in-page anchor nav + Getting Started/AI 101/
  Best Practices sections). No skills grid.
- `marketing.html` — skills tagged for the Marketing track.
- `go-to-market.html` — skills tagged for the Go-To-Market (GTM) track.

Every page opens with a shared `.global-nav` top bar (the three page links
on the left, Contact on the right, in one 1040px row above the hero) — this
replaced the old per-page `.top-contact` + `.page-nav` pattern on 2026-07-23.
The two skill pages carry an `Open Claude.ai` `.hero-cta` button in the hero
(below the paragraph, above the amber border); `index.html` does not. Skills
render sorted alphabetically by category then title, with date meta shown as
`Updated … · Added …`.

The **Prompts** section that briefly lived below the Skills grid on
`marketing.html` and `go-to-market.html` (added 2026-07-22) was removed on
2026-07-23. The scaffolding is still present but unused: the shared
`renderPromptsGrid` / `openPrompt` / `copyPrompt` helpers in `assets/site.js`,
the `.filter-wrap.static` / `.hero-stats.on-light` CSS, and the `prompts/`
placeholder folder. To bring the section back, re-add the `.guide-section`
markup and the inline `PROMPTS` / `renderPrompts` block to a page — see the
"Adding a new prompt" recipe below, which still applies.

There is no separate `playbook.html` — that content lives on `index.html`.
Don't re-split it into its own page without the user asking.

## Repo isolation — read before syncing anything

This repo, [`brain`](https://github.com/rlwbruce-byte/brain) (private,
internal), and `rachelwbruce` (Rachel's personal site) are three
independently versioned repos, each with its own git remote. There is no
git submodule, subtree, or automated CI sync between them, and none should
be added without the user explicitly asking for it.

Content moves from `brain` to `anatomy` by deliberate, manual promotion
only: generate the public copy there with `scripts/promote-skill.py` (it
strips brain-only front-matter and any `<!-- internal -->` blocks), copy the
result over, commit and push here as its own step. Never hand-write the file,
and never script a bulk sync across repos.

## Adding a new skill

1. Don't hand-write `skills/<slug>/skill.md`. Every file in `skills/` is a
   **download that people upload into Claude > Skills > Upload**, so its
   front-matter is validated by Claude itself. Generate it in the `brain` repo
   with `python3 scripts/promote-skill.py <slug>` and copy the result here.

   The front-matter carries **exactly four keys**, and nothing else:

   ```yaml
   ---
   name: <slug>          # REQUIRED by Claude; must equal the folder name.
                         # ≤64 chars, lowercase letters/numbers/hyphens only,
                         # must not contain "anthropic" or "claude"
   description: <what it does AND when to use it>   # REQUIRED by Claude.
                         # Non-empty, ≤1024 chars, third person, no XML tags
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   ---
   ```

   A missing `name` is fatal: a bare `.md` upload has no directory name to
   fall back on, so Claude rejects it outright with *"missing field 'name' in
   SKILL.md frontmatter and no directory name available for fallback"*. That
   is how every download on this site was broken until 2026-08-05.

   `created`/`updated` are required too — `openSkill()` in `assets/site.js`
   greps them out of the front-matter for the Read modal's
   "Updated … · Added …" line. Bump `updated` on any content change, leave
   `created` fixed, and keep both in sync with the `SKILLS` entry in step 2.

   Do **not** add `title`, `summary`, `category`, `audience`, `status` or
   `aliases` here — those are brain-only, and the site reads the card's title,
   summary and category from the `SKILLS` array (step 2), not front-matter.

   The body must be the skill's real operating procedure, not a description of
   it — someone who uploads this file should get a working skill, not a
   brochure. `brain/skills/<slug>/skill.md` is the source of truth.
2. Add an entry to the `SKILLS` array in `marketing.html` or
   `go-to-market.html` (whichever matches the skill's audience) — slug, title,
   category, summary, perfectFor bullets, created, updated.
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
