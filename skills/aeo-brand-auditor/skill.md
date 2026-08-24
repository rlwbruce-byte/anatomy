---
name: aeo-brand-auditor
description: Runs Answer Engine Optimization (AEO/GEO) audits on a company or URL. Two modes — a quick single-page/post citability check, or a full company-wide AEO/GEO scan from 3-5 intake answers (live AI-answer query panel, site audit, competitive teardown) — producing a markdown report, a browser-viewable HTML version, and an executive-summary PDF. Use when the user asks to run an AEO scan or brand audit on a company, build an AEO plan, check how they show up in ChatGPT/Perplexity/AI Overviews, or whether a page would be cited by an AI answer engine.
created: 2026-07-15
updated: 2026-07-24
---

# AEO Brand Auditor

Answer Engine Optimization is the SEO successor for a world where buyers ask
an LLM instead of typing a search query. This is a **company-wide AEO scan**
first and foremost, not just a content checker — its primary job is Mode 2
below. This skill has two modes — pick whichever the request calls for, or
ask if it's ambiguous:

- **Mode 1 — Quick Page Check**: paste in a page/post/doc, get scored
  against how an answer engine would summarize or cite it. Fast, no research,
  works in any Claude surface.
- **Mode 2 — Full Company AEO Scan** *(primary mode)*: given 3-5 answers about
  a company (plus optional attachments), runs live research and produces a
  full AEO strategy document — current AI-answer visibility, site audit,
  competitive landscape, category positioning, technical fixes, page copy/FAQ
  drafts, net-new page recommendations, a content calendar, an llms.txt
  draft, off-site citation strategy, a roadmap, and a measurement plan. Needs
  web research + a filesystem (Claude Code, or Claude with web search + file
  tools) — this mode can't run meaningfully in a plain chat surface with no
  tools, since it has to actually check live search/answer results rather
  than reason from memory.

## Trigger phrases

- "Run a company-wide AEO scan on [company]" / "Run an AEO brand audit on [company]" *(Mode 2, primary)*
- "Build an AEO plan for [company]" / "Run a full AEO analysis on [company]" *(Mode 2)*
- "How do we show up in ChatGPT/Perplexity/AI Overviews for [company]?" *(Mode 2)*
- "Run an AEO audit on this page" *(Mode 1)*
- "Would an AI answer engine cite this content?" *(Mode 1)*

## What you say

> Mode 2: "Run a company-wide AEO scan for [Company] — [domain]. We sell
> [products]. We want to be cited for [categories/queries]. Our competitors
> are [names]. Our ICP is [persona]. Here's what we know works: [proof
> points]."

> Mode 1: "Here's our product page copy for [Product]. We want to show up
> when someone asks ChatGPT 'what's the best tool for [category].'"

---

## Mode 1 — Quick Content Audit

Evaluate pasted content the way an answer engine would: is the core claim
extractable in one sentence, is it structured so a model can cite it
cleanly, and does it actually answer the question a buyer would ask —
versus talking about itself.

**Deliver:**
- **Extractability score** — can the core claim be lifted as a clean,
  standalone answer, or is it buried in marketing language?
- **Question-fit check** — does the content answer the buyer question, or
  only describe the product?
- **Structure fixes** — specific rewrites (headers, definitional openers,
  comparison framing) that make the page easier for a model to cite
  accurately.
- **Citation risk flags** — claims an answer engine would likely omit or
  soften because they're unverifiable or overly promotional.

**Scope:** works from content pasted in or a URL's copy — does not query
live answer engines to test actual citation behavior. (That live check is
what Mode 2's query panel does, at the company level.)

**Setup required:** none — prompt-only.

---

## Mode 2 — Full Company AEO Plan

This mode is research-heavy — expect 20-40+ tool calls at Full depth. Don't
shortcut it by reasoning from memory instead of checking live sources.

### Step 0 — Pick a run depth

Ask which depth to run, or infer it from how the request is framed:

- **Full** — the deep-dive version, meant to run roughly semi-annually.
  Query panel of 8-15 queries, full site audit across all key pages, full
  competitive teardown of every named competitor, full net-new page
  inventory, full off-site citation strategy. If a worked sample plan is
  bundled with this skill (`reference/sample-plan.md`), it demonstrates this
  depth.
- **Light** — the ad hoc/interim version, for checking in between Full runs.
  Reduced query panel (4-6 queries, top categories only), site audit limited
  to homepage + the 1-2 most important pages + llms.txt, spot-check only the
  top 1-2 competitors, skip or shorten the video/webinar ideas and
  third-party citation sections, roadmap covers 60-90 days instead of 6
  months. Say explicitly in the output that this was a Light run and which
  sections were abbreviated.

Default to **Light** if the user doesn't specify — don't silently run the
full 20-40-call workflow they didn't ask for.

### Step 1 — Intake

Ask for the following. Accept text, pasted content, or attached files
(existing audits, brand/messaging docs, spreadsheets, screenshots) for any
of them — read every attachment fully before proceeding, since they often
answer multiple questions at once and set naming/voice constraints the plan
must respect.

1. **Company + domain(s) in scope** — main site, plus any subdomains,
   landing-page domains, or docs sites to crawl.
2. **Products / business lines** — one line each: what it does, who buys it.
3. **Categories or queries to win** — the "best X," "X vs Y," "X
   alternatives" searches to be cited in (5-15 for Full, 2-4 for Light).
4. **Named competitors** — direct competitors plus 1-2 aspirational/adjacent
   players.
5. **ICP/buyer personas + any verified proof points** — real stats, customer
   names, case studies, or existing brand/naming docs.

**If any question goes unanswered:** say plainly, before starting research,
that the report will be less comprehensive without it — name which
section(s) it weakens (e.g. no named competitors means the competitive
picture and comparison-page recommendations will be thin) — then proceed
anyway. Don't block on completeness; carry the same gap into the report's
final "Open questions" section.

**Never invent stats, customer names, or quotes.** Anything not supplied or
independently verifiable gets marked "needs verification," not fabricated —
the same rule the companion skills (e.g. `company-identity-builder`) run on:
evidence-backed or flagged, never guessed.

### Step 2 — Baseline: AI-answer-engine panel

Build the query panel per the chosen depth, from the categories/competitors
named in intake: a mix of "best X," "X vs Y," "X alternatives," and a couple
of raw definitional queries ("what is X"). For each, use web search to see
who currently shows up — note whether the target company appears, and which
domains/pages are surfaced or cited.

State plainly in the report that this is a **proxy panel via web search
results**, not a literal cross-engine run through ChatGPT/Perplexity/Google
AI Overviews/Claude — unless the user supplies real AI-engine query logs.
Record results as a hit/miss table with source URLs per query.

### Step 3 — Site audit

Use `curl` (not a markdown-converting fetch tool alone — that strips the
markup you need) to pull raw HTML for the pages in scope for the chosen
depth. Check for:

- Organization/Product JSON-LD schema, and whether entity naming is
  consistent site-wide
- FAQPage schema **vs.** visible on-page FAQ content — flag mismatches in
  either direction
- `/llms.txt` — 200, redirect, or 404?
- Comparison/alternatives pages — exist, on the main domain, schema, sitemap
  entry? *(Full only, unless central to the ICP)*
- Category-language coverage — grep page text for each target category
  term; flag zero-mention pages that should own that term
- Meta descriptions and obvious copy problems on any landing pages in scope
- Quantified proof points — in crawlable HTML, or only gated in PDFs/forms?

### Step 4 — Competitive teardown

Full: for every named competitor (plus 1-2 more surfaced by Step 2), pull
their homepage, `/llms.txt`, and a sample comparison/alternatives page;
check their share of voice on the Step 2 panel. Light: spot-check only the
top 1-2 competitors' homepages and `/llms.txt`.

Identify the category's real "kingmaker" third-party citation surfaces —
verify from what Step 2 actually returned, don't assume by default; it
varies by industry.

### Step 5 — Synthesize wedges & strategy

From Steps 2-4, identify wedges (4-6 for Full, 2-3 for Light): queries that
are high-intent, currently thin or unanswered, and credible for this
company specifically. Draft the one target sentence every AI engine should
say about the company. Map each product × category combination to where the
company can credibly win.

Flag any naming/positioning inconsistency (site schema/titles vs. current
brand narrative) as a blocking decision — split entity signals measurably
hurt AI-answer citation.

### Step 6 — Write the report

Follow the section skeleton below, scaled to the chosen depth (if a
`reference/report-template.md` is bundled with this skill, follow that
instead — it is the same skeleton with fuller prompts per section):

1. Where we stand · 2. Strategy · 3. Technical & structural fixes ·
4. Web page copy · 5. Web page FAQs (≤60 words each, self-contained, no
invented stats) · 6. Net-new web page needs · 7. Prioritized question
inventory · 8. Blog topics · 9. Video/webinar ideas *(Light: short or skip)*
· 10. llms.txt draft · 11. Third-party citation strategy *(Light: short or
skip)* · 12. Roadmap · 13. Measurement · 14. Open questions (include every
intake gap flagged in Step 1).

Named-competitor comparison copy gets flagged for legal/approval review.

### Step 7 — Deliver three artifacts

Write to a working output directory (`<company-slug>-aeo-plan-<date>/`):

1. **`plan.md`** — the full report; source of truth for the other two.
2. **`plan.html`** — standalone, self-contained (inline CSS, no external
   assets, responsive, print-friendly). If visual polish matters and a
   visual-design skill is available (e.g. `canvas-design`,
   `brand-guidelines`, or `web-artifacts-builder`), load it for styling
   guidance; otherwise proceed with clean, readable default styling. Only
   publish as a hosted Artifact if asked — don't post client-specific
   competitive/financial content to a shareable link without checking first.
3. **`exec-summary.pdf`** — condensed 1-2 pages (target sentence, baseline
   score, top 3-4 wedges, top priority fixes, headline roadmap). Build
   `exec-summary.html` first, then render:
   ```
   NODE_PATH="$(npm root -g)" node scripts/render-pdf.cjs exec-summary.html exec-summary.pdf
   ```
   Uses Playwright + Chromium; if unavailable in a given environment, don't
   block the deliverable — hand over `exec-summary.html` in its place and
   say so.

Don't commit, push, or publish outputs outside the working directory unless
asked. Confirm before anything hard-to-reverse — publishing an Artifact,
pushing to a repo — especially with competitive/financial specifics in play.
