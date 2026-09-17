# CLAUDE.md

Guidance for Claude Code when working in this repo.

## What this repo is

`anatomy` is the public-facing site for **GTM Anatomy**: the marketing site for
the practice, plus the free Claude skills library for GTM and marketing teams.
It is served by **Vercel** from `main` — no build step, no `vercel.json`, just
static files. The canonical URL is **https://gtmanatomy.ai**; merging to `main`
publishes. Eleven static pages share `assets/styles.css` and `assets/site.js`:

**The practice**

- `index.html` — Home: hero on the tagline, what GTM Anatomy is, the four
  offerings, the skills library, five role tiles, contact section.
- `about.html` — live, and deliberately short: point of view, why the practice
  exists, how we work, who it is for, founder credibility, call to action. Restructured 2026-09-17 against the rule that an About page answers
  four buyer questions (who are you, do you understand my problem, why trust
  you, what makes you different) in roughly 500 to 800 words. Body copy is ~850
  words including headings, down from ~1270. Two sections were cut and are in
  git at `5c479c2`: the fourteen-step revenue-engine foundations climb
  (`.foundations` / `.foundation-item`, still styled and unused) and the
  Vision + mission dark band. **Do not re-add either without the user asking.**
  The founder section is the page's centrepiece, not an afterthought: it carries
  named employers, real figures, and `assets/rachel-bruce.jpg`. It ends on the
  bio: a personal "outside the work" close was drafted and cut on request, so do
  not add one back without being asked.
  About is the one page whose CTA band is **not** "Let's strategize" into the
  Anatomy Scan. It reads "Not sure where to get started? Let's chat." into
  `/contact.html#book` and `/offerings/`, because a reader who has just met the
  practice is choosing a direction, not an offering.
- `offerings/index.html` — hub, plus one page per offering, in sequence:
  `anatomy-scan.html` (01), `anatomy-os.html` (02), `ai-sprint.html` (03),
  `fractional-partner.html` (04). The sequence is diagnose, build, scoped project
  work, then ongoing partnership, and the numbering encodes it — reorder the cards
  and you must renumber the kickers too.
- `contact.html` — live: a Calendly booking embed, with email and LinkedIn as
  fallbacks. Home links here rather than embedding a form, so there is a single
  place to change how contact works.

**The skills library**

- `getting-started.html` — onboarding and the Claude Setup Guide (this was the
  old `index.html` before the 2026-09-10 restructure).
- `marketing.html` — skills tagged for the Marketing track.
- `go-to-market.html` — skills tagged for the **Sales** track. The filename stays
  `go-to-market.html` on purpose: renaming it would break inbound links. Change
  the label, never the URL. (The old reason given here was "GitHub Pages has no
  redirects." That stopped being true when the site moved to Vercel, which does
  support redirects via `vercel.json`. Keeping the URL is now a choice rather
  than a constraint — but it is still the right one, and anyone changing it owes
  a redirect.)

### Nav

One `.global-nav` bar on all eleven pages: the wordmark on the left, then About,
Offerings, AI Skills and **Contact** grouped hard right. The Contact button keeps
that plain label: it is wayfinding, and the amber fill already carries the
emphasis. "Let's chat" is the heading on the contact page, not the nav item. There
is no Home item: the wordmark is the home link and carries
`aria-label="GTM Anatomy, home"`. Offerings are reached through the hub, never
listed individually in the nav.

`.gn-contact` is the only solid amber in the bar, which is why the current page
reads as a faint amber wash (`.gn-links a.active`) rather than a filled chip.
Keep it that way: two solid amber chips in one bar and neither reads as the
action. AI Skills is a CSS-only
dropdown (`.gn-group` / `.gn-drop`) on pointer devices, suppressed under
`@media (hover:none)`. The three library pages also carry a `.subnav` second row
that always renders, which is how the grouping works on touch and with
JavaScript off. Call `setActiveNav('home'|'about'|'offerings'|'skills'|'contact')`
at the bottom of each page; the `.subnav` active state is hardcoded per page.

**Two gutter patterns exist in the stylesheet, and they do not align.** Where the
40px gutter sits on an outer wrapper and an inner element is capped at 1040px
(`.hero`, `.page-header`, `.cta-band`, `.site-footer`, `.filter-wrap`), content
lands at 120px on a 1280px viewport. Where an element carries both the cap and
the gutter itself (`.section`, `.how`, `.skills-section`), it lands at 160px.
`.global-nav-inner` and `.subnav-inner` are the second kind but are capped at
**1120px** (1040 plus two 40px gutters) so they match the hero exactly at every
width. If you unify the rest, widen their caps the same way rather than
restructuring the markup.

Copy the whole nav block verbatim when adding a page. It is duplicated by design
— there is no include mechanism and no build step.

### Hosting, and the two URLs

**Vercel serves `gtmanatomy.ai` from `main`.** That is the whole deployment: a
push to `main` is a deploy, and pull requests get their own preview URL (which
is behind Vercel's deployment protection, so a sandbox cannot fetch it — verify
against the live site after merge instead).

**GitHub Pages is still switched on, but it no longer serves the site.** Its
source is the `gh-pages` branch, which holds two files and nothing else:
`index.html` and `404.html`, both redirect stubs pointing at gtmanatomy.ai.
Every path under `rlwbruce-byte.github.io/anatomy/` therefore lands on the
canonical domain — the root through `index.html`, everything else through
`404.html`, which GitHub serves with a 404 status and a body that redirects.
That status code is expected and is not a broken link.

`gh-pages` is a **content branch, not a copy of the site.** Never merge `main`
into it or regenerate it from `main`; it would republish the whole site at the
old URL, which is the thing it exists to prevent.

`CNAME` at the repo root is inert. It is a GitHub Pages mechanism, `main` is not
the Pages source, and DNS for gtmanatomy.ai points at Vercel. It is kept because
the repo's records treat it as meaningful; it does nothing.

### Machine-readable layer

`llms.txt` is the index. Every HTML page has a markdown twin at the same path
with `.md` instead of `.html`, and `llms-full.txt` is all of them concatenated.
`sitemap.xml` and `robots.txt` sit at the root.

The twins are generated by scraping the HTML, so **a new markup pattern that the
extractor does not recognise silently vanishes from the answer-engine surface**.
`h3.persona-name` did exactly that: the five role tiles reached `index.md` as
unlabelled paragraphs for several commits. After adding any new heading or label
class, read the regenerated `.md` and check it is there.

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

The four offerings are framed as **diagnose, build, operate, and continue to
execute**. A prospect can start with the Scan or jump straight to an Anatomy OS
build; the sequence is a recommendation, not a gate. Transfer happens **after
enablement**, so write "yours at handover, following enablement", never handover
alone. The Anatomy Scan fee credits into an Anatomy OS build. The Fractional Partner
covers marketing, go-to-market, and GTM engineering, as one seat or several, and
hourly rates are available for project-shaped work. Never describe it as
go-to-market only: GTM engineering is the seat most teams cannot hire for, and it
is a deliberate part of the offer. Remember the no-"+"-on-
figures rule: write "starting at $5,000", never "$5,000+".

### Contact page and booking

`contact.html` is live and doubles as the booking page and the contact form:
Calendly collects the details at the point of booking, so there is no separate
form to wire.

It uses **Calendly's own inline widget**, not a hand-rolled iframe: a
`div.calendly-inline-widget` carrying `data-url`, plus their
`assets.calendly.com/assets/external/widget.js`. Changing the booking link means
changing that one `data-url`.

The link carries brand theming as query params, and they must stay in step with
the tokens: `background_color=faf6f2` is `--paper`, `text_color=0b0e12` is
`--graphite`, `primary_color=f5a623` is `--amber`. Because the widget's ground
matches the page, it sits on the page rather than inside a card.

Calendly's own inline style sets `min-width:320px`, which forces a sideways
scroll on a narrow phone, so `.calendly-inline-widget` is overridden to
`min-width:0` under 420px. That override needs `!important` to beat the inline
style. Keep it.

A "Calendar not loading?" link sits under the widget, and email and LinkedIn sit
below that. Keep them: an embed that fails must not leave the page with no way to
make contact.

**Watch the inline script when regenerating this page.** `close(page, extra_js)`
takes a real newline, not an escaped one. A literal `\n` in that argument lands
in the HTML, throws a syntax error, and silently kills every call in the block,
including `setActiveNav`. That shipped once.

**This sandbox cannot load calendly.com or Google Fonts in a headless browser.**
A blank embed in a local screenshot proves nothing. Assert the widget div and its
script tag are present, then check the rendered calendar on the live site.

`initContactForm()` and `initEmbed()` were removed from `assets/site.js` once
Calendly replaced both. Nothing calls them. They are in git if a hosted form is
ever wanted instead.

### Coming Soon splash pages

`offerings/index.html` and the four offering pages are
currently **Coming Soon splash pages** (`about.html` and `contact.html` are live
again): `.page-header` with a `.soon-badge`, then
a `.soon-card` carrying one call to action. Generated by
`build_soon.py` in the session scratchpad; the markup is plain enough to hand-edit.

Each splash card is headed "Coming soon." and there is no status badge in the
page header: the words appeared twice within one screen, so the badge went.
Every splash points at `/contact.html`, which is a working booking page, so the
conversion path is real from anywhere on the site.

**The full pages are not lost.** Their last complete versions are in git at commit
`0b5f3a6`. Restore one with
`git show 0b5f3a6:offerings/anatomy-scan.html > offerings/anatomy-scan.html`, then regenerate its `.md` twin and
`llms-full.txt`. `llms.txt` carries a Status block saying which pages are splash
pages; update it when any of them goes live.

### Content that is pending client input

Never invent proof points, ROI figures, metrics, testimonials, prices, or
timelines. Where the layout calls for one we do not have, it is marked in place:
a dashed `.tbd` chip for unpublished figures, a `.placeholder-block` panel for
proof-point and ROI sections, and an HTML comment for every testimonial. The
founder biography is no longer pending: every figure in it (fifteen years, the
fourteen-person team, the $3.5M budget, the $9M in sourced pipeline, the nine
agents, the named employers) comes from Rachel's own published career page at
https://rlwbruce-byte.github.io/rachelwbruce/, which is the source to check
before changing any of them. Prices and timelines are no longer pending — they are
published, listed above. Before anything goes to a prospect
audience, run `git grep -n 'class="tbd"\|placeholder-block'` and reconcile each
hit. Filling one of these needs the client's word, not a plausible number.

### Who we size to

The ideal customer is a **go-to-market team of 1 to 100**, not a company of that
size. The company can be far larger. Copy must not conflate the two, and the
Home hero chip says "GTM teams of 1 to 100" for exactly this reason.

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

Headings carry terminal punctuation. The full stop is marked up as
`<span>.</span>` so `.section-title span` and `.page-header h1 span` tint it
amber, echoing the wordmark. A heading that is a question keeps its "?" and gets
nothing appended.

Line-drawing icons use the `.spec-list.iconic` variant, never the base
`.spec-item`. Icons are inline SVG, 24x24 viewBox, `fill="none"`,
`stroke="currentColor"`, stroke-width 1.4, in `--amber-deep`. Each one has to
encode its point; a decorative glyph that could sit on any bullet does not ship.

The primary call to action is **"Let's strategize"**, not "Book a strategy call".
The older phrasing survives only in `contact.html` meta descriptions, where it
describes the action plainly for search results and should stay. `about.html` is
the deliberate exception: its CTA band says "Let's chat", matching the contact
page heading, because that reader is choosing a direction rather than an offering. Avoid: "AI-powered", "revolutionary",
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
- **The mark.** `A.` — a paper A on a graphite tile, the full stop set as an
  amber square — is the compact sibling of the wordmark, used wherever the full
  lockup will not fit. Every file is generated by `assets/logo/build.py`; the
  SVGs and PNGs it writes are **build output, never hand-edited**. Read
  `assets/logo/README.md` before touching any of it. Three things to carry:
  the letter is drawn as geometry rather than set in a font, precisely so it
  does not depend on a webfont this sandbox cannot reach; there are two optical
  cuts, a display cut for 180/192 and a heavier small cut for 16/32 and
  `favicon.svg`, because the display cut's hairlines vanish below one device
  pixel; and `favicon-180.png` is a square plate on purpose, because iOS rounds
  the touch icon itself.
- **Favicons are cached hard and the filenames never change.** Every page links
  them with a `?v=N` query string. Bump `N` on all eleven pages whenever you
  regenerate the icons, or returning visitors keep the old mark.
  `git grep -n 'favicon.*?v='` finds them.
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
- `assets/rachel-bruce.jpg` is the founder headshot on `about.html`, copied from
  Rachel's own career page. It is 896x1088, sits in a 240px `.founder-portrait`
  frame (180px under 720px wide), and is the only photograph on the site: the
  rest of the visual language is line-drawn. Replace the file in place rather
  than adding a second one, and keep the portrait aspect ratio.
- **Buttons.** On a **light** ground the primary action is the graphite fill,
  `.btn-navy`, and the secondary is the outlined `.btn-ghost`. On a **dark**
  ground the primary is the amber fill, `.btn-primary`, and the secondary is
  `.btn-ghost-dark`. Amber is spent in one place at a time, so it does not
  double as a button colour on paper. This applies to the Coming Soon cards too.
- Palette: graphite `#0B0E12` / amber `#F5A623` (`#C2760D` deep) — "Amber
  Circuit," chosen deliberately to avoid matching Continuous's navy/violet
  system while keeping a similar tech-forward, dark-ground feel.
- Type: Anton (display, headers only), Space Grotesk (body), IBM Plex Mono
  (labels, kickers, category tags) — carried over from Rachel's personal
  site.
- Voice: confident, specific, no filler. See `brain/CLAUDE.md` for the
  do/don't examples this was built from.
