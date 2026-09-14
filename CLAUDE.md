# CLAUDE.md

Guidance for Claude Code when working in this repo.

## What this repo is

`anatomy` is the public-facing site for **GTM Anatomy**: the marketing site for
the practice, plus the free Claude skills library for GTM and marketing teams.
It is served via GitHub Pages directly from `main` — no build step. Eleven
static pages share `assets/styles.css` and `assets/site.js`:

**The practice**

- `index.html` — Home: hero on the tagline, what GTM Anatomy is, the four
  offerings, the skills library, five role tiles, contact section.
- `about.html` — purpose, the revenue-engine foundations, how we work, who it is
  for, founder, vision and mission.
- `offerings/index.html` — hub, plus one page per offering, in sequence:
  `anatomy-scan.html` (01), `anatomy-os.html` (02), `ai-sprint.html` (03),
  `fractional-partner.html` (04). The sequence is diagnose, build, scoped project
  work, then ongoing partnership, and the numbering encodes it — reorder the cards
  and you must renumber the kickers too.
- `contact.html` — the only page carrying a form. Home links here rather than
  embedding one, so there is a single place to change how contact works.

**The skills library**

- `getting-started.html` — onboarding and the Claude Setup Guide (this was the
  old `index.html` before the 2026-09-10 restructure).
- `marketing.html` — skills tagged for the Marketing track.
- `go-to-market.html` — skills tagged for the **Sales** track. The filename stays
  `go-to-market.html` on purpose: GitHub Pages has no redirects, so renaming it
  would break inbound links. Change the label, never the URL.

### Nav

One `.global-nav` bar on all eleven pages: wordmark, then Home, About,
Offerings, AI Skills, and Contact on the right. Five items, and the offerings are
reached through the hub, never listed individually in the nav. AI Skills is a CSS-only
dropdown (`.gn-group` / `.gn-drop`) on pointer devices, suppressed under
`@media (hover:none)`. The three library pages also carry a `.subnav` second row
that always renders, which is how the grouping works on touch and with
JavaScript off. Call `setActiveNav('home'|'about'|'offerings'|'skills'|'contact')`
at the bottom of each page; the `.subnav` active state is hardcoded per page.

Copy the whole nav block verbatim when adding a page. It is duplicated by design
— there is no include mechanism and no build step.

### Machine-readable layer

`llms.txt` is the index. Every HTML page has a markdown twin at the same path
with `.md` instead of `.html`, and `llms-full.txt` is all of them concatenated.
`sitemap.xml` and `robots.txt` sit at the root.

**Maintenance rule: any copy change to a page must be mirrored into that page's
`.md` twin and into `llms-full.txt` in the same commit.** This is the real cost
of the approach; skip it and the answer-engine surface goes stale silently.

### Offering names and pricing

**Anatomy OS** is the product name. What it *is* gets described as an AI-native
go-to-market operating system — that phrasing carries the meaning, the name
carries the brand. Do not expand the name into "GTM Operating System" or
"Anatomy Operating System" in copy.

Pricing is published, and lives in four places that must stay in step: the
`OFFERS` array in the Home generator output, the `HUB_OFFERS` cards and the
`.price-table` on `offerings/index.html`, the `.pill-row` on each offering page,
and the pricing lines in `llms.txt`. Current figures:

| Offering | Investment | Timeline |
| --- | --- | --- |
| Anatomy Scan | $5,000 | Two weeks |
| Anatomy OS | $25,000 | Three to six weeks |
| AI Sprint | Starting at $5,000 | Scoped per project |
| Fractional Partner | $8,500 per month | Ongoing |

The Anatomy Scan fee credits into an Anatomy OS build. The Fractional Partner
covers marketing, go-to-market, and GTM engineering, as one seat or several, and
hourly rates are available for project-shaped work. Never describe it as
go-to-market only: GTM engineering is the seat most teams cannot hire for, and it
is a deliberate part of the offer. Remember the no-"+"-on-
figures rule: write "starting at $5,000", never "$5,000+".

### Contact form and scheduler embeds

`contact.html` has two `.embed-slot` elements driven by `initEmbed()` in
`assets/site.js`. Each renders an iframe when its `data-embed` attribute holds a
URL, and otherwise leaves the slot alone:

- `#schedulerEmbed` — paste any inline booking URL (Calendly, Cal.com, HubSpot
  meetings, SavvyCal). Until then it shows a visible "not connected" notice.
- `#formEmbed` — paste a hosted form URL (HubSpot, Tally, Typeform, Fillout) and
  it replaces the native form, which `initEmbed` hides automatically. Left empty,
  the slot hides itself and the native form is what renders.

The native form posts to `data-endpoint` on the `<form>` if set, and otherwise
composes a mailto. That is why the page works on a static host with nothing
configured. Provider choice is still open, so do not hard-code one.

### Content that is pending client input

Never invent proof points, ROI figures, metrics, testimonials, prices, or
timelines. Where the layout calls for one we do not have, it is marked in place:
a dashed `.tbd` chip for unpublished figures, a `.placeholder-block` panel for
proof-point and ROI sections, and an HTML comment for the founder biography and
every testimonial. Prices and timelines are no longer pending — they are
published, listed above. Before anything goes to a prospect
audience, run `git grep -n 'class="tbd"\|placeholder-block'` and reconcile each
hit. Filling one of these needs the client's word, not a plausible number.

### Who we size to

The ideal customer is a **go-to-market team of 2 to 200**, not a company of that
size. The company can be far larger. Copy must not conflate the two, and the
Home hero chip says "GTM teams of 2 to 200" for exactly this reason.

### Voice

Copy on the practice pages is drafted from the GTM Anatomy Brand + Message
Guide. The mechanics that matter when editing: sentence case headlines, Oxford
comma, commas and colons rather than dashes, "+" only in titles and "and" inside
sentences, no "+" appended to figures, acronyms defined on first use per page,
"we" for the practice and "you" for the client, AI-slop and AI-native
hyphenated, start-ups and scale-ups as two words.

Anton is reserved for the wordmark, offering names, and the Home hero statement
(`.hero-statement`), which is set in Anton mixed case so it reads as an extension
of the wordmark above it rather than as body copy blown up. Nothing else.

The primary call to action is **"Let's strategize"**, not "Book a strategy call".
The older phrasing survives only in `contact.html` meta descriptions, where it
describes the action plainly for search results and should stay. Avoid: "AI-powered", "revolutionary",
"game-changing", "10x", "unlock", "seamless", "cutting-edge", "solutions" as a
noun, "enterprise" as a customer descriptor.

Skills render sorted alphabetically by category then title, with date meta shown
as `Updated … · Added …`. Skill counts live only in the `renderStats` call on
`getting-started.html`, so adding a skill never means editing Home.

The **Prompts** section that briefly lived below the Skills grid on
`marketing.html` and `go-to-market.html` (added 2026-07-22) was removed on
2026-07-23. The scaffolding is still present but unused: the shared
`renderPromptsGrid` / `openPrompt` / `copyPrompt` helpers in `assets/site.js`,
the `.filter-wrap.static` / `.hero-stats.on-light` CSS, and the `prompts/`
placeholder folder. To bring the section back, re-add the `.guide-section`
markup and the inline `PROMPTS` / `renderPrompts` block to a page — see the
"Adding a new prompt" recipe below, which still applies.

There is no separate `playbook.html` — that content lives on
`getting-started.html`. Don't re-split it into its own page without the user
asking.

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
4. Update the stats (`renderStats` call) on `getting-started.html` if the total
   skill or track counts changed. That is the only page holding counts.
5. Mirror the new card into that page's `.md` twin (`marketing.md` or
   `go-to-market.md`) and regenerate `llms-full.txt`.

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

- **Wordmark.** The lockup is `GTMAnatomy.` — no space, "GTM" and the full stop
  in amber, "Anatomy" in paper on dark grounds. It is live Anton text, not an
  image file: `<span class="wm">` with `.wm-a` / `.wm-b` children, used in
  `.gn-brand` and `.footer-brand`. Live text so it stays crisp at any size and
  reverses cleanly on graphite, where the supplied black logo file cannot go.
  The lockup is the only place the name is written closed up; in prose the
  company is **GTM Anatomy**, two words, and the site is **GTMAnatomy.ai**.
- **Local screenshots do not load Google Fonts.** Headless Chromium in this
  environment cannot reach fonts.googleapis.com, so every local render falls back
  to a system sans and Anton never appears. Do not read a local screenshot as
  evidence that a typeface is wrong. To see the real thing, inject the fonts as
  base64 `@font-face` rules with `page.addStyleTag` before screenshotting. The
  published site and any Artifact render correctly, because the viewer's own
  browser fetches the fonts.
- `assets/og-image.png` is rendered from that same lockup. To regenerate it,
  screenshot a 1200x630 page with the fonts embedded as base64 data URIs —
  linking Google Fonts in headless Chromium silently falls back to a default
  sans and the wordmark comes out in the wrong face.
- Palette: graphite `#0B0E12` / amber `#F5A623` (`#C2760D` deep) — "Amber
  Circuit," chosen deliberately to avoid matching Continuous's navy/violet
  system while keeping a similar tech-forward, dark-ground feel.
- Type: Anton (display, headers only), Space Grotesk (body), IBM Plex Mono
  (labels, kickers, category tags) — carried over from Rachel's personal
  site.
- Voice: confident, specific, no filler. See `brain/CLAUDE.md` for the
  do/don't examples this was built from.
