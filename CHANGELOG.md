# Changelog

All notable changes to the site are recorded here, most recent first.

## 2026-07-29

Published a new skill to the Marketing track: **Build Brand Guidelines**.

- **`skills/build-brand-guidelines/skill.md`** — public-facing skill copy
  (`status: published`, category **Brand**, audience **Marketing Leaders**).
  Give Claude a company URL; it reads the site's real colors, typography,
  logo, and voice and builds an installable brand skill, a written style
  guide, a one-page branded PDF, and an editable PowerPoint deck.
- **`marketing.html`** — added the new **Brand** category to `CATEGORIES` and
  the skill entry to `SKILLS` (listed first).
- **`index.html`** — bumped the "Skills Available" stat 5 → 6.

## 2026-07-23 (2)

Site-wide layout + behavior pass across all three pages (`index.html`,
`marketing.html`, `go-to-market.html`) and shared assets:

- **Global nav.** Replaced the per-page setup (an absolutely-positioned
  `.top-contact` link in the hero + a separate `.page-nav` bar below it) with
  a single `.global-nav` top bar on every page: the three page links
  (Getting Started / Marketing / Go-To-Market) on the left, Contact on the
  right, aligned in one 1040px-wide row above the hero. `setActiveNav` now
  targets `.global-nav a`. Old `.page-nav` CSS left in place (unused, no
  longer referenced).
- **Hero CTA.** Removed the per-card "Open Claude.ai" button from the skill
  card actions (`assets/site.js` `renderSkillsGrid`) and placed one
  `Open Claude.ai ↗` button (`.btn-primary`, inside a new `.hero-cta`) in the
  hero of the two skill pages — below the hero paragraph, above the amber
  bottom border. Not added to `index.html` (no skill cards there).
- **Filter alignment.** Wrapped the Skills filter bar's label + tags in a
  `.filter-inner` (`max-width:1040px; margin:0 auto`) so they left-align with
  the hero copy and the skills grid instead of sitting flush to the viewport
  padding.
- **Sorting.** Skills now render sorted alphabetically by category, then by
  title (`renderSkillsGrid`); category filter chips are sorted alphabetically
  too (`renderTags`).
- **Date order.** Skill card meta and the Read-modal meta now read
  `Updated <date> · Added <date>` (was `Added … · Updated …`) — in both
  `renderSkillsGrid` and `openSkill`.
- **Prompts removed.** Deleted the **Prompts** `.guide-section` (and its
  inline `PROMPTS`/`renderPrompts` JS + `promptStats`) from `marketing.html`
  and `go-to-market.html`. The shared `renderPromptsGrid` / `openPrompt` /
  `copyPrompt` helpers, the prompt-related CSS, and the `prompts/`
  placeholder folder are left in place in case the section is re-enabled
  later; nothing renders them now.
- **Marketing hero copy** updated to: "Skills built for marketing teams —
  persona-based content audits, campaign builders, and more. Read how it
  works, download the file, create as a skill in Claude."

## 2026-07-23 (1)

- Added a new GTM skill: **Basic Discovery**
  (`skills/company-discovery-basic/skill.md`, `status: published`, category
  **Account Intelligence**, audience **GTM Leaders**) — generates an
  executive-level account brief for a target company (overview, ownership,
  funding, products, competitors, revenue-growth opportunities, buying
  reasons, plus optional AI strategy / recent news / talking points /
  executive summary). Promoted from `brain`.
- `go-to-market.html`: added the `company-discovery-basic` entry to the
  `SKILLS` array and added **Account Intelligence** to the `CATEGORIES` array
  (now `["Competitive Intelligence", "Account Intelligence"]`). GTM skill
  count is now 2; hero stats compute from array length, so no manual number
  change on this page.
- `index.html`: bumped the "Skills Available" hero stat from 4 to 5 (total
  across both tracks).

## 2026-07-22 (2)

- Getting Started (`index.html`) copy pass:
  - Hero sub now reads "A library of Claude **prompts and skills** built from
    real GTM workflows. Read how it works, download the **files**, **execute
    in Claude**. Check back often, **updates** are made daily." (was skills-only,
    "drag it into Claude", "skills are added and updated daily").
  - Step 1 (Browse): "Marketing" and "Go-To-Market" are now links to
    `marketing.html` and `go-to-market.html`.
  - Claude Setup Guide: removed the "— New Section" kicker and replaced the
    intro paragraph with "Build a system Claude can rely on with repeatable
    skills, prompts, and more."

## 2026-07-22 (1)

- Added a new **Prompts** section to `marketing.html` and `go-to-market.html`, below the existing Skills grid — its own heading, stats row, filter tags, and grid, wrapped in `.guide-section` (the same amber-top-border/tinted-background "new zone" treatment used for the Claude Setup Guide on `index.html`) so it reads as a distinct content zone rather than more of the Skills grid.
- `assets/site.js`: added `renderPromptsGrid`, `openPrompt`, and `copyPrompt` — mirrors the existing Skills rendering functions but reads from `prompts/<slug>/prompt.md` and swaps the Download button for a Copy button (extracts the first fenced code block in the prompt file and copies it to the clipboard).
- `assets/styles.css`: added `.filter-wrap.static` (non-sticky variant, since the page already has one sticky filter bar for Skills) and `.hero-stats.on-light` (amber-deep instead of amber for stat numbers/border, since this stats row sits on the tinted `--paper-dim` background instead of graphite).
- Shipped with one placeholder card per page (`prompts/placeholder-marketing-prompt/`, `prompts/placeholder-gtm-prompt/`) — `status: draft`, clearly marked `[Placeholder]` in the title. **Replace both before this section should be considered live** — see `CLAUDE.md` → "Adding a new prompt" for the pattern.
- `CLAUDE.md`: documented the Prompts section and the new "Adding a new prompt" recipe alongside the existing "Adding a new skill" one.

## 2026-07-21 (6)

- Rewrote the hero-sub copy on the Getting Started page: dropped the "competitor intelligence, ABM, AEO, and more" list from the intro sentence and added "Check back often, skills are added and updated daily." to signal the library is actively growing.

## 2026-07-21 (5)

- Renamed and expanded **AEO Content Auditor** → **AEO Brand Auditor**
  (`skills/aeo/skill.md` → `skills/aeo-brand-auditor/skill.md`, slug `aeo`
  → `aeo-brand-auditor`). It's a company-wide AEO scan first now, not just a
  single-page content checker — added a company-wide scan mode (AI-answer
  query panel, site audit, competitive teardown) alongside the original
  page-level check, promoted from `brain` after an internal test run.
- Updated the `SKILLS` array entry on `marketing.html` (slug, title,
  summary, perfectFor bullets, and `created`/`updated` dates — `created`
  kept at the original 2026-07-15, `updated` bumped to 2026-07-21) to
  match. No count/category change.

## 2026-07-21 (4)

- Every skill `skill.md` now carries `created` and `updated` dates in front-matter (convention added to `CLAUDE.md` — bump `updated` on any content change). Backfilled all four skills from git history.
- Renamed the **Company Identity Builder** category from "Brand & Messaging" to just **Messaging** (front-matter + `marketing.html`).
- Added a "Generate your LLMS.txt summary" bullet to the Company Identity Builder perfect-for list (skill.md + card).

## 2026-07-21 (3)

- Recategorized **Company Identity Builder** as a brand/messaging skill (it's for understanding a company's external-facing message, not account/market intel). Moved it from the Go-To-Market track to the Marketing track: `audience` → Marketing Leaders, `category` → **Brand & Messaging**, and reframed its copy/perfect-for bullets accordingly.
- `marketing.html` gains the skill and the new **Brand & Messaging** category (Marketing track now 3 skills); `go-to-market.html` reverts to just Competitor Intelligence and its single category. Total site skills unchanged (4), so `index.html` stats stay put.

## 2026-07-21 (2)

- Published new skill: **Company Identity Builder** (`skills/company-identity-builder/skill.md`). Give Claude a company URL and it builds a full identity across six approval-gated questions (brand colors, competitors, categories, sales plays, proof points, beachhead), then outputs a README, a branded HTML deck, and an llms.txt.
- Bumped `index.html` "Skills Available" stat from 3 to 4.

## 2026-07-21 (1)

- Shortened the top-right contact button label from "Contact for Consulting" to "Contact" on all 3 pages (mailto link/subject unchanged).

## 2026-07-20 (8)

- Removed the black `border-bottom` on the "Get Started in 3 Steps" section (`#how`) — it was stacking with the guide-section's amber top border, showing as two lines. Only the amber boundary line remains.
- Updated the AI 101 sub-heading from "The five terms you need before any of this makes sense" to "The terms you need to know before any of this makes sense" (count is no longer five now that LLM and Model were added).

## 2026-07-20 (7)

- Wrapped the Claude Setup Guide content (intro through Best Practices) in a `.guide-section` with a tinted `--paper-dim` background and a 3px amber top border — the same "zone boundary" treatment used at the bottom of the hero/page-header elsewhere on the site — so it reads clearly as a distinct section instead of just a thin divider line.
- Added a small amber "— New Section" eyebrow label above "Claude Setup Guide".

## 2026-07-20 (6)

- Increased `.hstat` left/right padding (0/22px → 24px each side) so the stat numbers have breathing room from the vertical divider lines between cells.
- Rewrote the Claude Setup Guide intro paragraph on the Getting Started page.
- Removed the in-page anchor nav (Getting Started / AI 101 / Best Practices buttons) below the intro — the section titles below still anchor the same IDs, just without the jump-nav.
- Renamed the guide's first section from "Getting Started" to "Know Before You Begin" (avoids clashing with the page-level "Getting Started" nav tab).
- Added "LLM" and "Model" to the AI 101 glossary, with ChatGPT/Claude/Grok as LLM examples; noted a models-comparison graphic is coming later.
- Updated the Best Practices sub-heading with an attribution note (sourced from resources/thought leaders, not original advice).
- Footer link changed from a fully-linked "About GTMAnatomy.AI" to "More about **GTMAnatomy.AI**" — only the name/domain-styled portion is a hyperlink now.

## 2026-07-20 (5)

- Restyled the top page-nav from underlined tabs to bordered box-buttons (matching `rachelwbruce`'s `.section-nav` pattern: `border:1.5px solid #4A5158`, transparent background, amber-filled active state) and moved it below the hero-stats numbers on all 3 pages — mirroring where `rachelwbruce` places its own section nav, right after the hero content.
- Increased `.hstat` top padding (16px → 28px) so the stat numbers no longer sit flush against the amber divider line above them.

## 2026-07-20 (4)

- Removed the hero CTA button row on `index.html` (Marketing Skills / Go-To-Market Skills / How It Works) — the top page-nav already covers this navigation, so the buttons were redundant.
- Folded the standalone `playbook.html` page into `index.html`: its Claude Setup Guide (intro + Getting Started/AI 101/Best Practices sections, with its own in-page anchor nav) now lives directly below the 3-step onboarding on the Getting Started page.
- Removed `playbook.html` and the "Playbook" tab from the shared `page-nav` on all remaining pages (now 3 tabs: Getting Started / Marketing / Go-To-Market).
- Added a `.section-intro` style for the new intro paragraph ahead of the merged guide content.

## 2026-07-20 (3)

- Added a 4th page, `playbook.html` ("Playbook" nav tab) — a Claude setup guide (Getting Started / AI 101 / Best Practices), rebuilt from a first draft that had mistakenly targeted the `rachelwbruce` repo/brand, restyled to `anatomy`'s graphite/amber system and populated with real copy from the underlying research (sources: Ruben Hassid, Kaylee Edmondson, Ruben Dominguez, Anthropic).
- Added new shared `.pb-*` component styles to `assets/styles.css` for the playbook's steps rail, glossary grid, and tiered best-practices cards.
- Added the "Playbook" tab to the shared `page-nav` on all other pages.

## 2026-07-20 (2)

- Split the single-page site into 3 pages sharing `assets/styles.css` and `assets/site.js`: `index.html` (Getting Started/home — hero + 3-step onboarding, skills grid removed), `marketing.html` (ABM Account Snapshot, AEO Content Auditor), `go-to-market.html` (Competitor Intelligence Brief).
- Added a top `page-nav` tab bar (Getting Started / Marketing / Go-To-Market) shared across all 3 pages with active-state highlighting.
- Reclassified Competitor Intelligence Brief's `audience` front-matter from `Marketing Leaders` to `GTM Leaders` to match its new page.
- Added an "About GTMAnatomy.AI" link to the footer on all 3 pages, pointing to the business overview deck (currently unprotected; password-gating to be added later).

## 2026-07-20 (1)

- Added favicon (graphite/amber "A." mark matching the hero wordmark), referenced at 16/32/192px plus a 180px Apple touch icon.
- Added a branded 1200x630 Open Graph / Twitter share image (`assets/og-image.png`).
- Added `og:*` and `twitter:*` meta tags (title, description, image, dimensions, card type) for link previews.
- Tightened the `<meta name="description">` copy.
