---
title: ABM Activation Plan
aliases:
  - ABM Activation Ideas
  - ABM Program Builder
status: published
summary: Leverages a company's GTM approach along with a campaign objective into a complete ABM program including account tiering, target account entry points, outreach hooks, and play-based email templates.
category: ABM
audience: Marketing & Sales Leaders
created: 2026-08-03
updated: 2026-08-03
---

# ABM Activation Plan

Also known as: ABM Activation Ideas, ABM Program Builder

## What this skill does

Give Claude your company's GTM priorities, a campaign objective, and (ideally) a target account list. It builds a complete ABM activation program:

- Common challenges that group accounts into playable segments
- Key contacts or decision makers at each account
- Email templates and a personalization guide to immediately action

This is the program-level companion to ABM Account Snapshot (built for a single account) and Company Identity Builder (company GTM research) — together they turn your company identity and account list into one activation plan sales and marketing can work from.

## Trigger phrases

- "Build an ABM activation plan for [Company]"
- "Set up the ABM program at [Company]"
- "Help me prioritize this target account list for ABM"
- "Turn this account list into an ABM activation plan"
- "Align sales and marketing on our ABM accounts"
- "Give me ABM activation ideas for [objective/segment]"

## What you say

> "Here's our company identity doc from Company Identity Builder. Our
> objective this quarter is to expand in mid-market fintech. Here's our
> target account list (40 companies) and a HubSpot export of recent site
> visits and form fills."

## What Claude delivers

Two paired documents, each delivered as branded HTML, a PDF export, and a Markdown export, styled in your company's own brand colors:

- Account Intelligence & Priority Table — account routing, challenge patterns by segment, persona entry points, outreach hooks, and a priority account table with fit rating, first persona, and entry hook per account
- Segment to Outreach — the first playable cohort, play assignment, Day 1/4/9 email templates by play angle, and a personalization guide

Before diving in, Claude will ask for the inputs that make the biggest difference in output quality — your target account or customer list, a proof points doc, and a brand voice doc. If any of those aren't available, it still builds the full plan, but flags clearly, up front, exactly which parts are best-effort and need your validation before anything goes out the door.

## Perfect for

- Kicking off a new ABM program
- Aligning sales and marketing on target account approaches
- Turning a raw target account list into SDRs outreach plans
- Re-segmenting an account list against a new campaign objective

## Scope

Works from company identity and account data you provide — it does not pull
live data from HubSpot, intent platforms, or enrichment tools (Apollo/Clay,
G2 intent, 6sense) on its own. If you paste in exports or screenshots from
those tools, it will use them; if none are provided, it says so explicitly
and produces firmographic-only segmentation rather than guessing at intent.

## Setup required

None to start — prompt-only. Higher-fidelity output with:

- A Company Identity Builder output, or your own GTM/ICP/sales-play reference docs
- A target account list or existing customer list
- A proof points doc with a cleared/pending split
- A brand voice doc (tone, banned terms, word count limits)
- Active sales sequences/cadences
- Any intent/behavioral data (HubSpot exports, G2 intent, tech stack data, SDR notes, funding/hiring news)

## Works great with

- Company Identity Builder — run first if the company identity doesn't already exist; this skill reads its output directly
- ABM Account Snapshot — use for a single high-value account that needs a deeper 1:1 treatment than a priority-table row provides
- Competitor Intelligence Brief — layer in when a named competitor shows up repeatedly across the account list
