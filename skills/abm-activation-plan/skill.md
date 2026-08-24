---
name: abm-activation-plan
description: Given a company's GTM identity/priorities, a campaign objective, and (ideally) a target account list, builds a complete ABM activation program — account tiering, the common challenges that group accounts into playable segments, key contacts or decision makers at each account, outreach hooks, a priority account table, and play-based email templates with a personalization guide. Use when the user wants to build an ABM activation plan, set up or prioritize an ABM program, align sales and marketing on target accounts, turn a raw account list into an outreach plan, or asks for ABM activation ideas tied to a campaign objective or segment.
created: 2026-08-03
updated: 2026-08-03
---

# ABM Activation Plan

*Also known as: ABM Activation Ideas, ABM Program Builder*

## What this skill does

Give Claude a company's GTM priorities, a campaign objective, and (optionally)
a target account list. It builds a complete ABM activation program:

- Common challenges that group accounts into playable segments
- Key contacts or decision makers at each account
- Email templates and a personalization guide to immediately action

This is the program-level companion to ABM Account Snapshot (single account,
1:1/1:few) and Company Identity Builder (company GTM research). This skill
assumes the company identity work is already done or being supplied, and
turns it — plus an account list — into one segment-level activation plan the
whole sales and marketing team can work from.

## Trigger phrases

- "Build an ABM activation plan for [Company]"
- "Set up the ABM program at [Company]"
- "Help me prioritize this target account list for ABM"
- "Turn this account list into an ABM activation plan"
- "Align sales and marketing on our ABM accounts"
- "Give me ABM activation ideas for [objective/segment]"

## What you say

> "Here's our company identity doc from company-identity-builder. Our
> objective this quarter is to expand in mid-market fintech. Here's our
> target account list (40 companies) and a HubSpot export of recent site
> visits and form fills."

## What Claude delivers

Two paired documents (see **Output structure** below), each delivered as
branded HTML (viewable + downloadable), a PDF export, and a Markdown export:

- Account Intelligence & Priority Table — account routing (ICP vs. partner vs. disqualify), challenge patterns by segment, persona-first entry points, outreach hooks, and a priority account table with fit rating, first persona, and entry hook per account
- Segment to Outreach — the first playable cohort (filtered from the priority table), play assignment within that cohort, Day 1/4/9 email templates per play angle, and a personalization guide

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

This skill always runs to completion, even missing every optional input. It
never blocks waiting on materials that aren't available — it asks for them
once, proceeds regardless of the answer, and carries a clear, prominent
disclaimer in the output naming exactly what was missing and what that means
for reliability. See **Priority reference materials** below and Step 1.

## Setup required

None to start — prompt-only. This skill runs a real quality gate, though:
three inputs (target account/customer list, proof points doc, brand voice
doc — see **Priority reference materials** in Step 1) are what separate a
directionally-useful test run from something safe to actually send. Without
them, the plan still gets built, but every account list, stat, and line of
copy in it is a best-effort placeholder that needs validation before it
reaches a prospect.

Full input list:
- A `company-identity-builder` output (README.md/llms.txt) or filled-in brain
  reference docs (GTM approach, ICP, sales plays, proof points, messaging)
- **Priority:** a target account list or existing customer list
- **Priority:** a proof points doc with a cleared/pending split
- **Priority:** a brand voice doc (tone, banned terms, word count limits)
- Active sales sequences/cadences (for sequence matching and email templates)
- Any intent/behavioral data (HubSpot exports, G2 intent, tech stack data,
  SDR notes, funding/hiring news)

## Works great with

- **Company Identity Builder** — run first if the company identity doesn't
  already exist; this skill reads its output directly.
- **ABM Account Snapshot** — use for a single high-value account that needs a
  deeper 1:1 treatment than a priority-table row provides.
- **Competitor Intelligence Brief** — layer in when a named competitor shows
  up repeatedly across the account list.

---

## How to run this

### Step 1 — Intake

Ask for the following up front, before doing any analysis. Accept text,
pasted content, or attached files for any of them, and read every attachment
fully before proceeding — they often answer more than one question at once.

**Required — can't produce a meaningful plan without these. Ask directly and
wait for an answer before proceeding:**

1. **Company identity.** Ask directly: *"Do you have a `company-identity-builder`
   output (README.md or llms.txt) for this company, or should I pull from your
   brain reference docs?"* Read whichever is offered. At minimum you need:
   GTM approach/motion, products & services, category placement, competitors,
   target persona(s) and ICP breakdown, current customer logos, proof points
   cleared for use, messaging & positioning, and active sales plays. If
   neither source exists, don't fabricate any of this — say so, and offer to
   run `company-identity-builder` first, or ask a condensed version of its six
   questions inline if the user wants to keep moving without a full run.
2. **Campaign or current objective.** What is this ABM push actually trying
   to accomplish this cycle? (e.g. "expand in mid-market fintech," "defend
   at-risk renewals," "launch [new product] into an adjacent vertical.") This
   drives which challenge patterns and plays matter — don't proceed without
   it; ask directly if it wasn't given.

**Priority reference materials — always ask for these explicitly, by name,
before starting the analysis.** These three are what separate a high-quality,
send-ready plan from a directional first draft. Don't just mention them in
passing — ask a direct question for each ("Do you have a target account list
or existing customer list to work from? A proof points doc with a
cleared/pending split? A brand voice doc?"). If the user doesn't have one or
more, say plainly, before you proceed, which parts of the plan will carry a
disclaimer as a result — then **run the full pipeline anyway**. Never block
waiting on these; the rule is ask once, proceed regardless, disclaim clearly.

3. **Target account list or existing customer list.** Company names/domains/
   URLs, 10-100 accounts is workable; for expansion motions, an actual
   customer list. Without one, ask if the user wants you to build a candidate
   list (e.g. researched lookalikes of named customers) — say explicitly that
   an AI-researched list is not the same as a real CRM/target list and must be
   verified before use (dedupe against actual customers, confirm firmographic
   claims). If the user declines a candidate list too, produce challenge
   patterns, persona entry points, and hooks at the segment level only, with
   no named priority table.
4. **Proof points doc**, ideally with an explicit cleared/pending split.
   Without one, do not write any stat or customer claim into hooks or email
   copy as if it were cleared — use bracketed placeholders (e.g.
   `[PENDING CLEARANCE: stat needed]`) instead, and carry every claim you did
   pull from company identity or elsewhere into the Proof Point Audit as
   **unverified**, not cleared, until the user confirms otherwise.
5. **Brand voice doc** — tone, banned terms, word count limits. If missing,
   check whatever messaging or brand-voice docs the user has on hand for this
   company; if still nothing, tell the user you'll infer a tone from whatever
   identity/messaging material exists and flag every email template as
   **tone not signed off** until they confirm or correct it.

**Also useful — ask, but these are lower priority and degrade gracefully:**

6. **Active sales sequences/cadences** — touch count, day length, entry
   persona for each. Without these, skip sequence matching (Step 4) and note
   it as a gap rather than inventing a cadence.
7. **Intent/behavioral signals** — HubSpot list exports, G2 intent, tech
   stack data (Apollo/Clay), SDR notes, funding/leadership/hiring news, or
   any other buyer-behavior data. Without this, segmentation runs on
   firmographics and stated ICP fit only — say so in the output rather than
   implying intent signal was used when it wasn't.

**The rule for all of the above:** don't block progress on missing inputs —
proceed and flag every gap. Priority reference material gaps (3-5) get a
**prominent disclaimer banner at the top of both output documents** (see
Output structure), not just a footnote; the lower-priority gaps (6-7) still
get flagged but can stay in the end-of-document "Data gaps" note.

### Step 2 — Account Routing

Using the ICP criteria from company identity, sort the target account list
(if provided) into three buckets:

- **Route to partner team** — the account's business model is implementing,
  reselling, or consulting around a product like this one, not buying it
  (SIs, MSPs, consultancies, implementation firms). Flag these clearly — they
  don't go into SDR sequences.
- **Qualify before rep time** — ICP fit is plausible but something needs
  verification first (recent acquisition, stack unconfirmed, recent IPO/PE
  change that may have altered the buying process).
- **ABM activate** — clear ICP fit, ready for the sequence/persona/hook
  assignment in the steps below.

If no account list was given, skip this step and say so.

### Step 3 — Challenge Pattern Mapping

Group ICP accounts by the operational problem the product actually solves —
not by industry or company size. Ask: what shared trigger (billing model,
tech stack, contract structure, growth stage, org structure — whatever is
load-bearing for *this* product) creates a real, worsening problem for these
accounts? Reference the sales plays and product detail from company identity
so every pattern connects to something the product solves, not a generic
industry trend.

For each pattern (aim for 4-6), produce:
- **Name** — short, memorable
- **Trigger** — what sets it off
- **Why it compounds** — what makes it worse over time
- **Accounts that fit** (if a list was provided)
- Optionally, a concrete "who sees which number/version of this" framing if
  the product's problem shows up differently to different stakeholders (the
  classic version: the same deal produces different numbers for Sales,
  Finance, Revenue Accounting, Procurement, and AP — find the version of this
  that's true for this specific product, don't force-fit it if it doesn't
  apply).

### Step 4 — Sequence Matching

Skip this step entirely if no active sequences were supplied (say so).
Otherwise, map each challenge pattern to whichever existing sequence fits it,
noting entry persona and touch cadence for each match. Don't invent a
custom sequence per account — match to what exists, and flag any pattern with
no matching sequence as a **sequence gap** rather than improvising one.

### Step 5 — Persona Entry Points

Define 2-3 first-contact personas, with entry conditions for each — who gets
contacted first at which type of account, and what account-specific flags
(PE ownership, org structure, buying-process signals) change the entry.
Ground this in the ICP/persona breakdown from company identity, not a generic
seniority ladder. A board/executive-sponsor persona (if relevant) is typically
a late-discovery or multi-thread entry, not a cold-outreach one — say so if it
applies.

### Step 6 — Outreach Hook Development

Develop one outreach hook per challenge pattern (6-10 total), each a
one-sentence, externally observable problem statement an SDR can reference in
a Day 1 email. A good hook: names something specific (not generic), is
verifiable without a conversation (job posting, tech stack, funding news,
public signal), and connects directly to something the product solves. Don't
require the prospect to already recognize they have the problem.

For each hook, give: hook name/ID, when to use it (which accounts/pattern),
which play it belongs to, a one-line pain statement, and a sample opening
line with `[Company]`/`[bracketed]` personalization slots.

### Step 7 — Priority Account Table

Combine routing + pattern + persona + hook into one row per account: company
name, play, fit (High/Medium), key signal (why this account, in one phrase),
first-contact persona, and entry hook(s). Carry forward any flags from
earlier steps (stack unconfirmed, PE/acquisition risk, partner-route risk).

### Step 8 — Proof Point Audit

Before any copy gets written, check the proof points doc (if supplied) and
split into cleared-for-external-use and pending/blocked, with an explicit
"do not use externally" flag on the pending list. If no proof points doc
exists, treat every stat/claim pulled from company identity or elsewhere as
a third **unverified** bucket — distinct from cleared and pending — and use
bracketed placeholders (`[PENDING CLEARANCE: ...]`) in any hook or email copy
rather than presenting it as cleared.

### Step 9 — Segment Filter (first playable cohort)

From the priority table, filter to a first actionable cohort using three
filters: one sales play, one entry persona (not mixed in the same cohort),
and confirmed tech stack/signal only. Target 6-12 accounts — enough to read
signal, few enough to stay personalized. State the filters applied and the
resulting count.

### Step 10 — Play Assignment Within the Cohort

Within the cohort, assign each account a specific play *angle* based on its
challenge pattern — accounts in the same broad play can still need different
openers if their underlying trigger differs.

### Step 11 — Email Template Development

Write two email options per touch, per play angle: Day 1 (trigger + one
specific question, no pitch, under ~100 words), Day 4 (proof point + meeting
ask, under ~110 words), Day 9 (content/insight send, no ask, under ~70
words — "no need to reply"). Follow the brand voice doc's tone, banned terms,
and word count rules — or, if no brand voice doc exists, the inferred tone
from Step 1, clearly labeled as unconfirmed. Use only cleared proof points
from Step 8 — pending and unverified ones stay a bracketed placeholder.
Never name competitors in copy without flagging it for legal/approval review
first.

### Step 12 — Personalization Guide

One row per account: what to reference in the trigger slot, any
product/pricing-model-specific language to use, and any account-specific
context the SDR needs before sending. If the trigger slot can't be filled
with something specific and verifiable for an account, flag it — don't send
until it can be.

---

## Output structure

Produce **two paired documents**, matching the deliverables above. **Every
document this skill produces carries a disclaimer banner** — this isn't
optional cosmetic styling, it's the mechanism that makes it safe to run this
skill without all the priority reference materials in hand.

### Disclaimer banner (mandatory whenever a priority reference material is missing)

Place this immediately after the header, before any analysis content, in
both documents — styled to stand out (a distinct callout color, not buried in
body text). State plainly, by name, which of the three priority reference
materials (target/customer list, proof points doc, brand voice doc) were not
supplied, and what that means concretely: an AI-researched account list needs
deduping against real customers before use; unverified stats need clearance
before appearing in any send; uninferred brand voice needs sign-off before
copy ships. If all three priority materials were supplied, this banner can
shrink to a one-line confirmation ("Built from your supplied account list,
proof points, and brand voice doc") rather than disappearing — the reader
should always be able to tell at a glance what this plan was and wasn't built
from.

### Document 1 — Account Intelligence & Priority Table

1. Header — campaign/play name, date, one-line description, a stat summary
   line (accounts reviewed · routed to partner · priority ABM accounts ·
   hooks developed · sequences mapped)
2. **Disclaimer banner** (see above)
3. Account Routing — three callout blocks (route to partner / qualify first /
   ABM activate)
4. Challenge Patterns by Segment — one block per pattern
5. Sequence Matching — one block per sequence (skip section if none supplied)
6. Persona-First Entry Points — one card per persona
7. Outreach Hooks — one block per hook
8. Priority Account Table — the full table
9. **Data gaps** — plain-language list of every remaining input (including
   the lower-priority ones — sequences, intent data) that was missing and
   what it would have sharpened; the priority-material gaps already called
   out in the banner don't need to repeat here in full, a cross-reference is
   enough

### Document 2 — Segment to Outreach

1. Header matching Document 1's campaign/play name and date
2. **Disclaimer banner** (see above) — restate it here too; a reader may open
   Document 2 without having seen Document 1
3. Segment Filter — the three filters applied and resulting cohort
4. Play Assignment table — account → play angle
5. Proof Point Audit — cleared vs. pending vs. unverified, restated for
   reference — this is where the "no proof points doc" disclaimer becomes
   concrete, line by line
6. Email Templates — grouped by play angle, Day 1/4/9, two options each,
   every unverified stat marked inline (e.g. `[PENDING CLEARANCE: ...]`), not
   just in the audit table
7. Personalization Guide — one row per account

Skip Document 2 entirely (deliver Document 1 only) if the user only wants
account intelligence/prioritization, not outreach copy — ask if it's
ambiguous which they want.

## Building the files

For each document, in a working directory `<company-slug>-abm-activation-<date>/`:

1. Write the Markdown version first (`account-intelligence.md`,
   `segment-to-outreach.md`) — source of truth for the other formats.
2. Build a self-contained HTML version (inline CSS, no external assets,
   responsive, print-friendly) styled in the company's brand colors from
   company identity — reuse the palette/typography extracted by
   `company-identity-builder` if available. If a visual-design skill is
   available (`canvas-design`, `brand-guidelines`, `web-artifacts-builder`),
   load it for styling guidance; otherwise use clean default styling with the
   brand colors applied to headers, callout blocks, and section accents.
   Mirror the visual grammar of a segment-intelligence report: a stat-bar
   header, colored callout cards for routing buckets, bordered segment/pattern
   cards, and a clean data table for the priority list.
3. Render the HTML to PDF:
   ```
   NODE_PATH="$(npm root -g)" node scripts/render-pdf.cjs account-intelligence.html account-intelligence.pdf
   ```
   (repeat for `segment-to-outreach.html` if produced). Uses Playwright +
   Chromium; if unavailable in a given environment, hand over the `.html`
   file in its place and say so rather than blocking the deliverable.
4. Deliver the HTML file(s) with `SendUserFile` so they're previewable
   immediately, in addition to the saved copies. Publish as a Claude Artifact
   only if asked — don't post account-specific competitive or account data to
   a shareable link without checking first.

Don't commit, push, or publish outputs outside the working directory unless
asked.
