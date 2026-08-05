---
title: Marketing Audit
status: published
summary: Give Claude a company name or URL and it grades their marketing across owned, earned, paid, and social channels, then hands back a scorecard-style report — good/bad/low-hanging-fruit per channel, a prioritized top-fix list, and HTML + PDF outputs.
category: Marketing Audit
audience: Marketing Leaders
created: 2026-08-05
updated: 2026-08-05
---

# Marketing Audit

## What this skill does

Give Claude nothing but a company name or URL and it runs an outside-in read
of how that company's marketing actually shows up in the world — across the
four channel types that cover the whole surface: **owned** (site, content,
pricing), **earned** (press, analysts, reviews, Wikipedia), **paid** (search,
display, sponsorships), and **social** (LinkedIn, X, YouTube, TikTok,
community, exec personal brand).

Each channel gets researched with live sources, graded A through F, and
broken into concrete good / bad / low-hanging-fruit findings — closing with
a single "if you only fix five things" list ordered by effort-to-impact,
not by channel.

Built for marketers who want a fast, evidence-backed outside view of their
own brand, a client's, or a competitor's — the kind of read a candid outside
consultant would give you, grounded in real sources rather than a vibe.

## Trigger phrases

- "Run a marketing audit on [Company]"
- "Audit [Company]'s marketing"
- "How's [Company] doing across owned, earned, paid, and social?"
- "Review [Company]'s marketing posture"

## What you say

> "Company is Acme Corp, acme.com."

That's enough to run. If you have them, adding your ICP, a messaging or
positioning statement, or a brand identity doc sharpens the read — but none
are required, and the audit runs as a pure outside-in view without them.

## How it works

Claude runs four research passes — one per channel — pulling real sourced
findings (URLs, handles, dates, figures), never fabricated stats. Anything
that can't be verified (a bot-blocked page, a conflicting source, live
paid-search presence that needs a real SERP check) is flagged explicitly as
lower-confidence rather than presented as fact.

Each channel is then graded A through F and written up with:
- **Good** — concrete, sourced strengths
- **Bad** — concrete, sourced weaknesses
- **Low-hanging fruit** — fixes that are cheap relative to their payoff

If a prior audit for the same company already exists, Claude runs it as a
**refresh** instead — re-checking each channel for what changed, what
didn't, and what's being watched for next time, rather than starting over.

## What Claude delivers

- **`report.md`** — the full write-up: composite grade, per-channel grade
  strip, all four channel sections, the priority fix list, and a
  methodology note naming which findings are lower-confidence
- **`report.html`** — a self-contained, responsive report styled to the
  subject rather than a fixed template, with light and dark themes
- **`report.pdf`** — a paginated PDF rendered from the HTML version
- **`README.md`** — a short grades table and method summary

## Perfect for

- A fast, credible outside read on your own brand's marketing posture
- Prepping for a client or prospect conversation with a graded teardown of
  their public marketing
- Competitive teardown — see where a competitor is over- or under-invested
- A recurring health check: re-run later and get a "since the last look"
  refresh instead of a from-scratch report

## Scope

Claude researches from public sources it can reach — the company's own
site, review sites, press, and search results. Live paid-search and display
ad presence can't be confirmed by search tools alone (no incognito SERP, no
ad-transparency access) — the report always names this as its
lowest-confidence section rather than guessing.

## Setup required

Needs live web research and a filesystem — this doesn't run meaningfully in
a plain chat surface with no tools, since it has to check current live
sources rather than reason from memory. Works in Claude Code, or Claude with
web search and file tools enabled.

## Works great with

- Any prior brand-identity/brand-guidelines work for the company — feeds
  the real brand palette and fonts into the HTML report instead of
  inventing one
- **Competitor Intelligence Brief** — turn a "bad" or "low-hanging fruit"
  finding about a named competitor into a battlecard update
- **AEO Brand Auditor** — pairs well when the audit surfaces an
  earned-media or content gap; AEO checks whether that content would get
  cited by an answer engine, this skill checks whether it exists and
  performs at all
