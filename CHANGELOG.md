# Changelog

All notable changes to the site are recorded here, most recent first.

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
