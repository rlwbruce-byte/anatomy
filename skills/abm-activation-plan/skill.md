---
title: ABM Activation Plan
aliases:
  - ABM Activation Ideas
  - ABM Program Builder
status: published
summary: Turns a company's GTM identity plus a campaign objective into a full ABM activation program — account routing, challenge patterns, persona entry points, outreach hooks, a priority account table, and play-based email templates — for sales/marketing alignment.
category: ABM
audience: Marketing & Sales Leaders
created: 2026-08-03
updated: 2026-08-03
---

# ABM Activation Plan

*Also known as: ABM Activation Ideas, ABM Program Builder*

## What this skill does

Give Claude your company's GTM identity, a campaign objective, and (ideally)
a target account list, and it builds a complete ABM activation program: which
accounts to pursue and which to route elsewhere, the operational challenge
patterns that group accounts into playable segments, who to contact first at
each type of account, the specific outreach hooks an SDR can use in a Day 1
email, a priority account table combining all of it, and — for the accounts
selected into a first playable cohort — play-assigned email templates and a
personalization guide.

This is the program-level companion to **ABM Account Snapshot** (single
account, 1:1/1:few) and **Company Identity Builder** (company GTM research) —
it turns company identity plus an account list into a *segment-level*
activation plan the whole sales and marketing team can work from.

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

Two paired documents:

- Account Intelligence & Priority Table — account routing (ICP vs.
  partner vs. disqualify), named challenge patterns by segment, persona-first
  entry points, outreach hooks, and a priority account table combining all of
  it with fit rating, first persona, and entry hook per account.
- Segment to Outreach — the first playable cohort (filtered from the
  priority table), play assignment within that cohort, Day 1/4/9 email
  templates per play angle (two options per touch), and a personalization
  guide (one row per account: trigger slot, personalization notes).

Each delivered as branded HTML (viewable + downloadable), a PDF export, and a
Markdown export — styled in your company's own brand colors.

Before diving in, Claude will ask for the inputs that make the biggest
difference in output quality — your target account or customer list, a proof
points doc, and a brand voice doc. If any of those aren't available, it still
builds the full plan, but flags clearly, up front, exactly which parts are
best-effort and need your validation before anything goes out the door.

## Perfect for

- Kicking off a new ABM program or quarter and needing sales/marketing to work
  from the same account list, segments, and messaging
- Turning a raw target account list into something SDRs can act on without
  guessing who to contact or what to say
- Re-segmenting an existing account list against a new campaign objective
- Auditing whether outreach copy is using only cleared proof points before it
  goes out

## Scope

Works from company identity and account data you provide — it does not pull
live data from HubSpot, intent platforms, or enrichment tools (Apollo/Clay,
G2 intent, 6sense) on its own. If you paste in exports or screenshots from
those tools, it will use them; if none are provided, it says so explicitly
and produces firmographic-only segmentation rather than guessing at intent.

## Setup required

None to start — prompt-only. Higher-fidelity output with:
- A `Company Identity Builder` output, or your own GTM/ICP/sales-play
  reference docs
- A target account list or existing customer list
- A proof points doc with a cleared/pending split
- A brand voice doc (tone, banned terms, word count limits)
- Active sales sequences/cadences, and any intent/behavioral data (HubSpot
  exports, G2 intent, tech stack data, SDR notes, funding/hiring news)

## Works great with

- **Company Identity Builder** — run first if the company identity doesn't
  already exist; this skill reads its output directly.
- **ABM Account Snapshot** — use for a single high-value account that needs a
  deeper 1:1 treatment than a priority-table row provides.
- **Competitor Intelligence Brief** — layer in when a named competitor shows
  up repeatedly across the account list.
