---
name: competitor-battlecard
description: Turns a competitor name plus whatever competitive intel you have (their website, G2 reviews, win/loss notes, call transcripts) into a deal-ready battlecard — strengths to acknowledge and pivot away from, weaknesses to exploit carefully, a feature comparison with a talk track for each row, objection-handling scripts, trap-setting questions, landmines to avoid, proof points, and demo differentiation — with every claim framed as Fact, Impact, Act. Use when the user asks to create a battlecard, wants to know how to compete against a named competitor, needs competitive positioning or objection handling, or is prepping a rep or SE for a deal where a specific competitor is in play.
created: 2026-07-30
updated: 2026-08-03
---

# Competitor Battlecard

## What this skill does

Give Claude a competitor and whatever competitive intel you have — their
website, a G2 review, win/loss notes, a call transcript — and it produces a
structured, deal-ready battlecard: strengths to acknowledge and pivot away
from, weaknesses to exploit carefully, a feature comparison with a talk track
for each row, objection-handling scripts, trap-setting questions to plant
doubt early in an evaluation, landmines to avoid, proof points, and demo
differentiation tips.

Every competitive claim follows a **Fact → Impact → Act** framework — the
competitive reality, why it matters, and what to actually say or ask — so the
output reads like something an SE can use live on a call, not a research memo.

## Trigger phrases

- "Create a battlecard for [Competitor]"
- "How do we compete against [Competitor]"
- "Competitor comparison"
- "Competitive positioning against [Competitor]"

## What you say

> "Competitor is Acme Corp. Here's their pricing page, a G2 review
> complaining about their implementation time, and our notes from the last
> two deals we lost to them."

## What Claude delivers

- **Quick-reference header** — win rate, most common deal stage, when you
  win vs. lose, and the one-sentence key differentiator
- **Strengths & weaknesses** — their strengths (how to acknowledge, then
  pivot) and weaknesses (impact + a trap-setting question for each)
- **Feature comparison** — capability-by-capability, with a talk track for
  how to position each row
- **Objection handling** — acknowledge → pivot → proof point scripts for
  the objections that come up most
- **Trap-setting questions** — questions to ask early in an evaluation that
  plant doubt or establish criteria you win on
- **Landmines** — topics to avoid or redirect, and why
- **Proof points** — customer wins, third-party validation, metrics to share
- **Demo differentiation** — what to lead with, always show, and skip unless
  asked

## Perfect for

- Arming reps and SEs to support a competitive deal cycle
- Standardizing how a team talks about a specific competitor
- Turning scattered win/loss notes and call transcripts into something
  reusable across the team

## Scope

⚠️ **This is a structural template, not a source of competitive
intelligence.** Claude can research public information on its own —
competitor sites, G2/Capterra reviews, press — but the sections that actually
win deals (win rate, deal stage, confirmed customer wins/losses, internal
proof points, verified pricing) require real input: sales/CS notes, tracked
deal outcomes, and an accurate ICP. Without that input, a generated
battlecard will surface the placeholder *"Historical opportunity insights and
customer feedback needed here"* throughout, and shouldn't be treated as
deal-ready until a human fills those gaps in.

## Setup required

None to start — prompt-only. Output quality scales directly with how much
real win/loss history and customer intel you feed in.

## Output formats

Markdown by default — the working format for iterating and keeping in
version control. A PowerPoint version is available on request (e.g. "make
this a deck"), built one slide per section rather than dumping tables onto
slides.

## Works great with

- **Competitor Intelligence** — feed a fresh competitor signal in first,
  then turn it into a battlecard update
