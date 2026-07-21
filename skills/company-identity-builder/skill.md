---
title: Company Identity Builder
status: published
summary: Give Claude a company URL and it builds a full GTM identity — brand colors, competitors, category, sales plays, proof points, and beachhead offering — one question at a time, then hands back a README, a branded HTML deck, and an llms.txt.
category: Messaging
audience: Marketing Leaders
created: 2026-07-21
updated: 2026-07-21
---

# Company Identity Builder

## What this skill does

Paste a company's URL and Claude researches it across the open web — the
company's own site, review sites, news, analyst coverage, and job postings —
to build a complete go-to-market identity. It works through six fixed
questions and pauses after each one for your approval, so you can correct the
research before it hardens into the final output.

When all six are approved, it produces three deliverables: a standalone
`README.md`, a self-contained HTML brand deck styled in the company's real
colors, and an `llms.txt` (a dense, machine-readable summary).

Built for marketing and brand teams who need a company's external-facing
identity laid out clearly — your own, to pressure-test the message you're
putting into market, or another company's, to see how they present
themselves.

## Trigger phrases

- "Build an identity for [company]"
- "Give me the rundown on [url]"
- "What do they sell, and how?"
- "Run a GTM overview / brand teardown on [company]"

## What you say

> "Build a company identity for https://www.example.com — I'm meeting them
> next week and want to understand their positioning and how they land
> accounts."

## The six questions

Claude answers these one at a time, with an approval gate between each:

1. **Brand colors** — primary and secondary palette, extracted from the live
   site's CSS where possible (real hex values, not a guess), including
   dual light/dark identities.
2. **Competitors** — who competes for the same buyer, triangulated from
   comparison pages, "alternatives to" lists, and analyst landscapes, plus
   any market consolidation.
3. **Categories** — how the company describes itself vs. how the market and
   analysts categorize it, and any category it's trying to create.
4. **Sales plays** — GTM motion (PLG, sales-led, hybrid, channel), buyer
   personas, and sales-strategy signals from pricing, verticals, and hiring.
5. **Proof points** — customer logos, quantified ROI metrics, testimonials,
   analyst validation, certifications, and funding.
6. **Beachhead offering** — the most-adopted entry point: which offering
   lands accounts, and the one thing a new customer says yes to first before
   expanding.

Every answer is evidence-backed and cites its source. Where the evidence is
thin, Claude says so rather than guessing.

## What Claude delivers

- **`README.md`** — a standalone company identity, one section per question,
  written as finished prose you can reference later without re-reading the
  research
- **HTML brand deck** — a single self-contained page, styled in the
  company's actual brand colors, presentable enough to screen-share or
  forward as-is
- **`llms.txt`** — a concise, link-rich, machine-readable summary of the
  identity for feeding into other AI workflows

## Perfect for

- Auditing your own external-facing message — is it saying what you think?
- Capturing a company's brand identity (palette, category, positioning) in one place
- Building a positioning or messaging input from scratch
- Onboarding a new marketer onto how a company presents itself
- Generate your LLMS.txt summary

## Scope

Claude researches from public sources it can reach — the company's site,
review sites, news, and search results. It does not access anything behind a
login. Brand-color extraction is most accurate when a browser tool is
available to read the live page's styles; otherwise Claude works from page
source and describes the palette.

## Setup required

None to run the research — this is a prompt-driven skill. The HTML deck and
`llms.txt` are written as files, so a filesystem (Claude Code, or the desktop
app with a Filesystem connector) makes saving the deliverables seamless.

## Works great with

- **Competitor Intelligence Brief** — turn the competitor list this surfaces
  into an ongoing monitoring cadence
- **ABM Account Snapshot** — layer this company identity into an
  account-level plan
