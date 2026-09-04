---
name: company-discovery-basic
description: Turns a company name into a sales-ready account brief — overview, ownership, funding, competitors, buying reasons, and revenue-expansion opportunities — sourced from the latest public information, delivered as both a chat brief and a brand-styled HTML artifact. Use when the user asks to research a company, build an account brief, prepare for a discovery call or executive briefing, or identify revenue-expansion opportunities for a target account.
created: 2026-07-23
updated: 2026-09-04
---

# Basic Discovery

## What this skill does

Give Claude a company name and it produces an executive-level account brief for
Enterprise SaaS sales teams. The output is concise, factual, and optimized for
account planning, executive briefings, discovery preparation, and identifying
revenue expansion opportunities — written the way an Enterprise Account
Executive would prep for a customer meeting.

## Every run ships two things

The artifact is not a "if they ask for it" extra — **every run produces both**:

1. **The brief in chat** — the full report, in the sections below.
2. **A self-contained HTML brief** — the same report styled in the company's
   own brand palette and published as a private artifact.

Where the session can also write files, save both to disk as a third output —
see **Save the run**. Where it can't, the first two still both happen.

See **Build the artifact** and **Save the run** at the end of this file.

## Handle with care

Open the brief — in chat and in the artifact — with the soft facts to verify
before a live conversation. This goes first, not in a footnote: a number cited
confidently and wrong is worse than no number.

Flag things like source conflicts on funding totals or headcount, name
collisions with unrelated companies, marquee customers who are also investors,
cumulative figures presented as current, and products announced but not yet GA.
Say what the conflict is and what to do about it — "cite the Series B, not a
total" beats "funding is unclear."

## Company Overview

- Company description
- Founded
- Leadership (CEO and notable executives if relevant)
- Employee count (approximate)
- Industries served
- Primary products/platforms

## Headquarters

- City
- State/Province
- Country

## Ownership

Indicate whether the company is public, private, PE-backed, or a subsidiary.

## Funding

If private, include total funding raised, latest funding round, latest
valuation (if available), and lead investors.

If public, include the ticker and approximate market capitalization.

## Products

Summarize major products and platforms. Group similar offerings together.

## Ideal Customers

- Industries
- Company sizes
- Buying personas
- Geographic focus

## Notable Customers

Include recognizable customer logos where publicly available.

## Competitors

List major competitors in a two-column table — Company and Primary Focus.

## Revenue Growth Opportunities

Assume the audience is speaking with the company about expansion opportunities.
Identify areas where they could generate additional revenue, such as:

- Cross-sell
- Upsell
- New product expansion
- Geographic expansion
- AI initiatives
- Data monetization
- Marketplace opportunities
- Customer success improvements
- Partner ecosystem
- Enterprise expansion
- Government expansion
- Industry-specific offerings

Focus on strategic opportunities rather than speculative ideas.

## Why Customers Buy Them

Summarize the primary buying reasons, such as:

- Cost reduction
- Automation
- Security
- Compliance
- AI capabilities
- Ease of use
- Scalability
- Integrations
- Analytics
- Time savings

## Formatting Guidelines

- Use clear headings.
- Prefer bullet lists over paragraphs.
- Use tables where comparisons improve readability.
- Keep outputs executive-friendly.
- Avoid unnecessary marketing language.

## Research Guidelines

Always use the latest publicly available information.

When possible, verify leadership, funding, valuation, headquarters, and ticker
(if public).

Prioritize sources in this order: company website first, then investor
announcements, SEC filings, press releases, and trusted business publications.

## Response Style

Write like an Enterprise Account Executive preparing for a customer meeting. Be
concise, accurate, business-focused, and strategic. Avoid excessive technical
implementation details unless they directly relate to business value.

## Optional Additions

When relevant, also include the three sections below. They're the only optional
part of the report — everything else above and the Executive Summary below run
every time.

### AI Strategy

Describe AI products, LLM initiatives, generative AI offerings, and AI
partnerships.

### Recent News

Summarize significant announcements from the last 6–12 months.

### Sales Talking Points

Provide several thoughtful discovery questions that could uncover growth
opportunities. For example:

- How are you measuring AI adoption across customers?
- What challenges exist around enterprise expansion?
- How are you approaching monetization of new platform capabilities?

## Executive Summary

End every report with a short summary covering company maturity, growth
trajectory, market position, and the largest strategic opportunity.

## Build the artifact

Every run ends with a self-contained HTML brief, published as a Claude
Artifact. This is what gets forwarded, screen-shared, and read on a phone
before the call — the chat brief is the working text, the artifact is the
deliverable.

### Style it in the company's own brand

Pull the real tokens from the live site rather than guessing — enumerate
`:root` CSS custom properties and the header/nav/CTA computed styles, or fetch
the homepage plus its main stylesheet and grep for `#rrggbb` frequency, CSS
variable definitions, `<meta name="theme-color">`, and SVG fills. Use the
company's real typefaces when they're on Google Fonts; substitute a close match
and say so in the brand table when they aren't.

If a brand-extraction or brand-guidelines skill has already run for this
company, reuse the palette it captured instead of re-extracting. If a
visual-design skill is available in the session, load it for styling guidance
first.

Check contrast before shipping: a brand accent that's safe as a fill is often
not safe as text. Split it into two tokens — the raw brand color for fills and
large display type, a deepened variant clearing 4.5:1 for accent text.

### Build rules

- **Self-contained.** Inline all CSS, embed or omit images, no external requests
  beyond Google Fonts — so it works offline and publishes cleanly under a strict
  CSP.
- **Theme-aware.** Define the light palette on bare `:root`, redefine the tokens
  under both `@media (prefers-color-scheme: dark)` (guarded
  `:root:not([data-theme="light"])`) and `:root[data-theme="dark"]`. Give `body`
  an explicit background token.
- **Responsive.** Verify at 900px and 390px with no horizontal overflow; wide
  tables scroll inside their own `overflow-x: auto` container.
- **Same content as the brief**, in the same order — plus a scan strip of the
  three or four figures that matter (funding, headcount, customers, ticker),
  the competitor table, and the executive summary.
- **Footer:** `Compiled from public sources. Not affiliated with or produced by
  <Company>.`

### Publish it

Publish with the Artifact tool, titled `<Company> Account Brief`. Artifacts are
private by default, so publishing the brief needs no approval — but **don't
share the link outward** (a prospect, a client, a public channel) without
checking first. Account research carries competitive and financial specifics.

Hand back the artifact link in the reply. If the session can't publish
artifacts, hand over the HTML file itself — however this session delivers files
— and say plainly that no hosted link was created. Never let a missing publish
step turn the run back into chat-only output.

## Save the run

Skip this section where the session has no filesystem — the chat brief and the
artifact are still both required. Where files can be written, save under a
per-company folder in your research directory — the slug is lowercase and
hyphenated, domain minus `www.` and the TLD (`datacore.com` →
`datacore`, `kargo.ai` → `kargo-ai`). Account briefs are the standing reference
for a company, so they sit at the folder root and get updated in place rather
than dated into a subfolder.

```
<company-slug>/
  README.md                                  # the canonical brief
  <company-slug>-account-brief.artifact.html # the artifact, on disk
```

`README.md` opens with a metadata blockquote (company, website, context, last
updated, method), then the **Handle with care** list, then the report sections,
a **Brand reference** table, a **Files** table, **Sources**, and the
not-affiliated footer.

**The artifact is the part that gets lost.** An artifact lives in the artifact
store, not on disk — nothing backs it up. Writing the same HTML into the company
folder is what makes it survivable. The same goes for a run in an ephemeral or
cloud session: files that are never saved out are gone when the session ends.

If the research folder is version-controlled, commit the run before the session
ends. If the session can write files but can't commit them — a desktop session
reaching a folder through a filesystem connector usually can't run `git` — write
them anyway, then say plainly that the run is **on disk but not committed** so
someone can finish the job. Never leave a run unsaved silently.
