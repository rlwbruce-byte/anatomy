---
name: campaign-kit
title: Campaign Kit
aliases:
  - Asset Activation Kit
  - Content Promotion Kit
  - Asset Launch Kit
  - Content Atomizer
status: ready
version: 2
category: Campaign
audience: Marketing & Sales Leaders
summary: Turns one long-form asset into the whole campaign around it — promotion and follow-up. Reads the asset in full, checks it against the message guide or the asset's stated goals, and builds a gated landing page, confirmation page, five email tracks, newsletter module, three LinkedIn post types, SDR outreach and follow-up, blog post, three LinkedIn ads, and an expansion track where there's an installed base. Runs an alignment brief with an approval gate before writing any copy, and ships markdown plus a browsable HTML page with a rendered preview of every asset.
description: Turns a finished long-form asset into a complete promotion and follow-up campaign. Requires the asset itself plus either a message guide or a clear statement of what the asset is meant to achieve. Reads the asset cover to cover, builds a claims-and-proof inventory so no stat is invented, scores the asset against the stated goals, then produces a gated landing page, confirmation page, confirmation email, promo email, newsletter module, corporate/founder/seller LinkedIn posts, a three-email nurture track, SDR cold outreach, three SDR post-download follow-ups, a blog post, three LinkedIn ads, and an expansion track for existing customers — delivered as markdown, a browsable HTML page with a rendered preview of each asset, and a PDF. Use this whenever someone has an ebook, whitepaper, analyst or research report, guide, case study, or webinar recording and wants a campaign, launch kit, promotional copy, follow-up sequences, help getting more out of a piece of content, or asks how to promote, atomize, relaunch, or "do something with" a report that underperformed — even if they never say the word campaign.
created: 2026-09-10
updated: 2026-09-11
---

# Campaign Kit

*Also known as: Asset Activation Kit, Content Promotion Kit, Asset Launch Kit, Content Atomizer*

## What this skill does

Most long-form assets get a landing page, one email, and one LinkedIn post —
and then die. The promotion is thin and the follow-up doesn't exist, so a piece
that took a quarter to produce converts for a week and then sits there.

This skill takes one finished asset and builds the whole campaign around it in
a single run — **the promotion and the follow-up**: demand capture, demand
nurture, sales activation, paid, and expansion.

Three things make it different from asking Claude to "write some promo copy":

1. **It reads the asset in full first** and builds a Claims & Proof Inventory.
   Every stat, quote, and claim that appears anywhere in the kit traces back to
   a specific page or section. Nothing is invented.
2. **It aligns the asset to the business before it promotes it.** The asset is
   scored against the company's stated priorities, and that check is a visible
   deliverable with an approval gate — including the standing option to
   recommend repositioning the asset, or not promoting it as-is.
3. **It ships something people can actually use.** Markdown as the source of
   truth, plus a browsable HTML page carrying a rendered preview of every
   deliverable, so a marketer can see the landing page as a landing page rather
   than reading a spec of one.

## Trigger phrases

- "Build a campaign around this ebook / whitepaper / report"
- "Turn this asset into a launch kit"
- "Write the promo copy for [asset]"
- "How do we promote this guide?"
- "Atomize this report into channel content"
- "We spent a lot on this report and it went nowhere"
- "Give me the full campaign kit for [asset]"
- "What's the follow-up sequence after someone downloads this?"

## What you say

> "Here's our new research report on [topic] (PDF attached). Our priority this
> half is landing mid-market accounts in [vertical]. Here's our message guide.
> Build the campaign kit."

The asset and the second line are the two things that must be there. The
message guide is better still, but the goals alone are enough to run on.

## What Claude delivers

A campaign folder with one file per channel, plus an alignment brief and an
index:

| # | Deliverable | File |
|---|---|---|
| — | Alignment brief, campaign spine, and Claims & Proof Inventory | `00-alignment-brief.md` |
| 1 | Gated landing page | `01-landing-page.md` |
| 2 | Confirmation / download page | `02-confirmation-page.md` |
| 3 | Confirmation email | `03-confirmation-email.md` |
| 4 | Promo email to house list | `04-promo-email.md` |
| 5 | Newsletter and syndication module | `05-newsletter-module.md` |
| 6 | LinkedIn post — corporate | `06-linkedin-corporate.md` |
| 7 | LinkedIn post — founder / executive | `07-linkedin-founder.md` |
| 8 | LinkedIn posts — sellers and SDRs | `08-linkedin-sellers.md` |
| 9 | Nurture emails (×3) | `09-nurture-emails.md` |
| 10 | SDR cold outreach promoting the asset | `10-sdr-outreach-cold.md` |
| 11 | SDR follow-ups after download (×3) | `11-sdr-followups.md` |
| 12 | Blog post | `12-blog-post.md` |
| 13 | LinkedIn ads (×3) | `13-linkedin-ads.md` |
| 14 | Expansion track — **only if there's an installed base** | `14-expansion-track.md` |
| — | Index, launch sequence, UTM table, measurement, open items | `README.md` |

Plus the generated views: `campaign-kit.html` (every deliverable with a
rendered preview above its copy) and a PDF of the alignment brief.

## Perfect for

- Launching a new research report, ebook, or whitepaper
- Relaunching an asset that underperformed with a sharper message
- Getting value out of a commissioned analyst study, which is usually the most
  expensive asset a company owns and the most underused
- Giving sales something to send that isn't a product one-pager
- Getting a lean team a full campaign in one pass instead of six briefs

## Scope

This skill writes copy and specs, and generates preview pages from them. It
does not design, build, or publish anything — no page builds, no image
generation, no sending, no ad account access. Creative direction is written as
a brief for a designer.

It works from the asset and the context you supply. It does not pull live
performance data, list counts, or CRM records. If you paste in exports, it uses
them; if you don't, it says so rather than guessing.

## Works great with

- **Company Identity Builder** — run first if the company's identity, proof
  points, ICP, and competitors aren't documented. This skill reads its output,
  and without it a client run has to assume all four.
- **Build Brand Guidelines** — supplies the voice and visual system. Without
  it, previews render unbranded and the copy runs under an unvalidated-voice
  flag.
- **AEO Brand Auditor** — the blog post here is written to be citable by answer
  engines; run the auditor after publishing to check whether it is.
- **ABM Activation Plan** — the SDR outreach here is asset-led and horizontal;
  the ABM plan is account-led. Use both when the asset supports a named account
  push.

---

## How to run this

Five steps. Step 3 is a hard gate.

### Step 1 — Intake

Establish **whose asset this is** before anything else, then gather inputs.
That first question decides which voice sources are legitimate, and getting it
wrong means writing a client's campaign in someone else's voice.

**Two things are required. Ask for both by name and don't start without them:**

1. **The long-form asset.** The finished piece — ebook, whitepaper, analyst or
   research report, guide, case study, webinar recording. PDF, DOCX, Markdown,
   a URL, or pasted text. If it doesn't exist yet and only an outline does, say
   so and run **Concept Mode**.
2. **A message guide, or the asset's goals.** Either a positioning and voice
   document, or a clear statement of what this asset is meant to achieve and
   for whom. One or the other — not neither.

The second requirement is the one people try to skip, and it is what separates
a campaign from a pile of copy. Without it there is nothing to align the asset
*to*, the alignment brief has no scale to score against, and every downstream
decision — the hero stat, the CTA ladder, which angle leads — becomes a guess
dressed as a recommendation.

If neither is offered, ask once, plainly: *what is this asset supposed to do,
and who is it for?* A two-sentence answer is enough to run on. Refusing to
guess here costs a minute; guessing costs the whole kit.

Everything else is optional and the run completes without it, behind a
disclaimer naming exactly what was missing.

The full question set, the voice-source precedence rules, and the asset
provenance and rights questions are in **Appendix A**.

### Step 2 — Read the asset in full and build the Claims & Proof Inventory

Read the entire asset before writing a single line of copy. Not the executive
summary, not the first three pages — all of it. Long assets get read anyway;
length is not a reason to skim.

While reading, build the **Claims & Proof Inventory**: every usable stat,
finding, quote, framework, and customer example, each with its location.

**This table is the only sanctioned source of facts for the kit.** If it isn't
in the table, it doesn't appear in the kit. Where a channel needs a number and
none exists, write `[[NEED STAT — none in asset]]` rather than filling the gap.
A loud gap is a task for a human; an invented number is a liability that ships.

The inventory has four required sections — table structures and what belongs in
each are in **Appendix B**:

1. **The claims themselves**, with location, type, strength, and public-use call
2. **Quotes**, with attribution exactly as published
3. **Do not use** — everything the asset contains that must never appear in
   copy, with the reason. This is not optional and it is not a footnote; it is
   the section that stops the most expensive mistakes.
4. **Changes the sales conversation** — anything in the asset that a rep will be
   asked about before they expect it. Disclosed pricing, implementation
   timelines, contract terms, named limitations.

Also capture while reading:

- The **single most surprising or contrarian finding** — this becomes the
  campaign hook and the founder post.
- The **strongest section for each persona** — the SDR emails point each
  recipient at the part that matters to them.
- Anything **outdated, unsupported, or legally risky** — this goes to the
  alignment brief as a flag, not into copy.

### Step 3 — Write the alignment brief, then stop

Write `00-alignment-brief.md` and present it. **Do not generate the
deliverables until the user approves it.** This is the gate, and it is the most
valuable thing the skill does: it is the last moment at which repositioning is
cheap.

The brief's structure, the scoring scales, the campaign spine, and the four
recommendation options are in **Appendix C**.

The recommendation is allowed to be uncomfortable. A skill that always says
"looks great, here's your campaign" is worth nothing at the gate. If the asset
doesn't serve a stated priority, say so and say what would.

**Concept Mode.** If the asset isn't written yet, run the same brief against
the outline, build the full kit, and mark every fact-dependent line
`[[PENDING ASSET]]`. State at the top of every file that the kit is written
against a concept and must be re-run against the finished asset.

### Step 4 — Build the kit

On approval, write the deliverables using the specs in **Appendix D**, then
write `README.md` with the index, launch sequence, UTM table, measurement, and
the collected open items.

Write all of them. A kit missing three files is not a kit — the whole point is
that a lean team gets the entire campaign in one pass, and the missing pieces
are exactly the ones that never get written later.

### Step 5 — Generate the views, save, and file

Markdown is the source of truth. The HTML and PDF are generated from it, so
they cannot drift.

### What ships

| Output | What it is |
|---|---|
| The numbered markdown files and `README.md` | The source of truth. Every edit happens here. |
| `00-alignment-brief.html` and `.pdf` | The brief as a styled page, and a PDF generated from it for anyone who won't open a link. |
| `campaign-kit.html` | Every deliverable in one browsable page, each section opening with a **rendered preview** of the asset, then the copy deck. |

### The previews

A preview renders the **recommended variant** of each deliverable as it would
actually appear — the landing page and blog in browser chrome, emails in a mail
client with from, subject and preheader, LinkedIn posts and ads as post cards
with the truncation point visible, the newsletter module dropped into a greyed
host layout, sequences shown as all their steps side by side.

This matters more than it sounds. A marketer reading a spec of a landing page
is doing translation work; a marketer looking at a landing page is doing
judgement work. The preview is where someone notices that the hook dies at the
truncation point, or that the third email in a sequence asks for too much.

Render previews in the brand's real system when one is available. When one
isn't, render deliberately unbranded — a `[[LOGO]]` placeholder and a neutral
palette — and say so. Previews show layout, hierarchy and length. Presenting an
invented brand as a mockup invites someone to build from it.

### Saving

Save to a folder named for the campaign, with a slug descriptive enough to tell
two campaigns apart a year later. **Commit it.** Files written in a cloud or
scheduled session are destroyed when the container is reclaimed, and a run
that isn't committed is lost.

---

## The rules that govern every run

These apply across every file. Don't restate them in each one; apply them.

**One campaign, one message.** Every deliverable works off the campaign spine
from the alignment brief. Channels reinforce each other; they don't each make a
different argument. If a channel needs a different argument to work, that's a
finding for the brief, not a silent divergence.

**Facts only from the inventory.** `[[NEED STAT]]` beats a plausible
invention, every time. The reason is not pedantry: a single invented number in
a campaign built on a research asset discredits the asset, and the asset is the
only reason the campaign works.

**Placeholders are loud.** Anything a human must supply is written as
`[[LIKE THIS]]` so it cannot ship by accident, and every one is collected in
the README's open items. Never leave a soft blank.

**Respect the voice source, and name it.** Banned words are banned. Word-count
limits are limits. Every file states which voice source was used, and carries
an **unvalidated voice** flag if there wasn't one. If the voice doc conflicts
with a channel best practice, follow the voice doc and note the conflict.

**Attribution discipline.** Attribute to the study or asset and to specific
roles — never to an implied population. With a handful of interviews behind it,
"customers report" and "users say" are not honest. Quote attributions are
copied exactly as published and never enriched with a company name the asset
didn't print.

**Honor the asset's own constraints.** If the asset restricts how it may be
used — an analyst's prohibition on competitive use, an embargo, a
co-branding limit — that restriction binds every file in the kit. Surface it in
the brief and repeat it in the README's standing constraints.

**Disclose a commissioned or sponsored asset** wherever it is promoted. A
skeptical reader finds the commissioning relationship in ten seconds, and
finding it themselves discounts everything above it. Disclosing it first is
what keeps the numbers credible.

**No fabricated social proof.** No invented customer names, logos, review
counts, download numbers, or "trusted by" claims. Where none are cleared, the
asset's own evidence base is usually a better proof point anyway — the size and
shape of the study population is real and citable.

**Every file is copy-paste ready.** Subject lines in a labeled block, body copy
clean, no commentary mixed into the copy. Notes go in a `### Notes` section at
the bottom.

**Every file names its variants and what they test**, and which to lead with.

**UTM every link**, following the convention in the README spec.

---

## Quality bar

Check every one of these before delivering:

- [ ] The asset was read in full, and the Claims & Proof Inventory exists with
      all four sections, including **Do not use**
- [ ] No stat, quote, or customer name appears that isn't in the inventory or
      the cleared proof points
- [ ] The alignment brief was approved before any copy was written
- [ ] Both axes were scored — priorities/motions *and* business outcomes — and
      anything the asset contradicts is marked **Contradicted**, not softened
- [ ] Every deliverable exists, plus the brief and the README
- [ ] The expansion track exists if there's an installed base, and doesn't if
      there isn't
- [ ] Every file works off the same campaign spine
- [ ] Every placeholder is `[[LOUD]]` and collected in the README open items
- [ ] Voice source is named at the top of every file, and flagged if unvalidated
- [ ] The asset's own usage constraints are stated in the README and respected
      in every file
- [ ] Channel length limits respected — LinkedIn hooks, subject lines, ad
      character counts, SEO title and meta lengths
- [ ] Every link carries a UTM
- [ ] The generated HTML page builds, and its previews render the recommended
      variant of each asset
- [ ] Output is written to disk and committed — not just shown in chat

## Disclaimer to carry in the output

When any priority input was missing, put this at the top of the README and the
alignment brief, filled in:

> **Built without: [[list what was missing]].** Every [[stat / customer name /
> claim]] in this kit traces to the source asset, but [[proof point clearance /
> voice validation / ICP confirmation / usage rights]] was not available at
> build time. Treat the copy as a strong first draft, not send-ready, until
> those are confirmed.

---

# Appendix A — Intake in full

Gather this before reading the asset or writing anything. Accept files, pasted
text, or links for any of it.


---

### The first question: whose asset is this?

Ask this before anything else, because it decides which voice sources are
legitimate and there is no way to recover from getting it wrong. A client
campaign written in someone else's voice reads fine in isolation and is
obviously wrong the moment the client sees it.

| Answer | What it means for the run |
|---|---|
| **Ours** — your own company or practice | The operator's own reference library applies: their messaging, ICP, GTM framework, positioning. This is the only case where those documents are the right source. |
| **A client's** | Their message guide, brand guidelines, or identity output. If none exists, run inline voice questions and flag **unvalidated voice**. Your own reference docs are **not** a fallback here. |
| **A prospect's** — building this to win the work | Same as a client's, except nothing has been supplied. Reconstruct voice from their public writing, say plainly that it was reconstructed, and flag **unvalidated voice** in every file. |
| **A partner's or co-branded** | Both parties' constraints apply. Ask which brand leads and whether the other has approval rights over the copy. |

### Voice source precedence

Use the first source that exists **for the answer above**, and name which one
was used in the header of every output file.

**When the asset is ours:**

1. A supplied message guide or brand voice doc
2. A `company-identity-builder` or `build-brand-guidelines` output
3. Your own documented reference library — messaging, ICP, GTM framework
4. Inline voice questions, asked once, with **unvalidated voice** flagged

**When the asset is a client's, a prospect's, or a partner's:**

1. Their supplied message guide or brand voice doc
2. A `company-identity-builder` or `build-brand-guidelines` output **for that
   company**
3. Their public writing — the asset's own register is usually the best
   available signal, since it is finished, reviewed copy they already shipped
4. Inline voice questions, asked once, with **unvalidated voice** flagged

**Your own reference library never appears in this second list.** Those
documents describe a different company. Reaching for them because they are
conveniently present is the single most damaging thing this skill can do.

When running unvalidated, say so in the brief, in the README, and at the top of
every file. An unvalidated run is useful; an unvalidated run that looks
validated is not.

### Required — don't proceed without these

#### 1. The long-form asset

The finished piece: ebook, whitepaper, analyst or research report, guide, case
study, webinar recording or transcript. PDF, DOCX, Markdown, a live URL, or
pasted text.

If it doesn't exist yet and only an outline or concept does, say so plainly and
run **Concept Mode** (see the main skill file). Don't quietly treat an outline
as an asset — every fact-dependent line in the kit changes when the real thing
lands.

#### 2. A message guide, or the asset's goals

**One of these two. Not neither.**

- **A message guide** — positioning statement, messaging pillars, tone, banned
  words, cleared proof points. This is the better input, because it also
  resolves voice.
- **Or the asset's goals** — what this asset is meant to achieve and for whom.
  Two sentences is enough: the audience, and the thing you want them to do or
  believe.

This is the requirement people try to skip, and it is what separates a campaign
from a pile of copy. It is the thing the asset gets aligned *to*. Without it,
the alignment brief has no scale to score against, and every downstream
decision — the hero stat, the lead angle, the CTA ladder, what to drop —
becomes a guess wearing the clothes of a recommendation.

If neither is offered, ask once, plainly: **what is this asset supposed to do,
and who is it for?** Then wait for the answer. Refusing to guess costs a
minute. Guessing costs the kit, and it costs it invisibly, because generic copy
looks fine until someone asks why the campaign leads where it leads.

A good goals answer usually contains **both axes**, and most real answers do:

- **Sales motions** — new logo acquisition, cross-sell, upsell, adoption and
  utilization, renewal defense, a product-led motion
- **Business outcomes** — the things the product is claimed to produce for a
  customer

They score independently in the brief, and an asset can serve one axis well
while contradicting the other. Scoring only the outcomes is how a run misses
that an asset serves expansion better than acquisition.

If the answer names only one axis, that's workable — score what you were given
and say in the brief which axis went unstated.

### Asset provenance and rights

A third-party or commissioned asset carries constraints no first-party asset
does, and they bind every file in the kit. Ask all four:

**1. Is this first-party, third-party, commissioned, or co-branded?**
An analyst report the company paid for is commissioned. One the analyst
published independently is third-party. The disclosure obligations differ.

**2. What are the usage terms?**
Can it be excerpted in paid social? Can charts be reproduced? Is there a
licensed-use window? Unconfirmed rights don't stop the run, but they block
specific deliverables — usually the ads and the blog post, which are the most
expensive things in the kit. Flag it as blocking against those files rather
than discovering it at launch.

**3. Does the asset contain a restriction on its own use?**
Read for this while reading the asset. Analyst studies routinely carry one —
a statement that the study is not to be used as a competitive analysis is
common, and it silently forbids an entire category of copy that a campaign
would otherwise reach for first.

**4. When was it published?**
Capture the date. Age matters differently by asset type: a three-year financial
model survives being two years old, and a trends piece does not. The brief
states the age and judges whether it undermines the asset. Date it visibly in
the copy rather than letting a reader discover it.

### Priority reference materials

Always ask for each of these by name. They separate a send-ready kit from a
first draft.

**1. The message guide, if the goals were supplied instead.** Having both is
better than either. A guide supplied late still improves every file it touches.

**2. Proof points with a cleared / pending split.** Customer names, logos,
metrics, and quotes that are actually allowed in public. Without this, the kit
uses only what's inside the asset and `[[LOGOS]]` placeholders — which is the
correct behavior, not a degraded one.

**3. The offer at the end of the journey.** Demo, assessment, consultation,
trial, event. Every CTA in the kit ladders to this, so an assumed offer means
every CTA is provisional. Say so loudly if it has to be assumed.

### Does the company have an installed base?

Ask directly. If yes, the kit gains the **expansion track** (file 14): plays
aimed at existing customers rather than new logos.

Most assets serve expansion at least as well as acquisition, and nobody asks,
because a campaign brief written by a demand-gen team is acquisition-shaped by
default. An asset whose value scales with deployment, seats, or coverage is an
expansion asset that happens to also work on new logos.

If the company is pre-revenue or has no relevant installed base, skip file 14
rather than padding the kit. A track with no audience is worse than no track.

### Useful if available

- ICP and target persona definitions
- The asset's gating decision and the form fields already in use
- Existing sequences the SDR emails have to slot into
- Prior asset performance — what converted, what didn't
- Competitor assets on the same topic
- The verticals and segments the company actually sells into, which may be
  narrower than the asset's own evidence base supports

---

# Appendix B — The Claims & Proof Inventory

Built while reading the asset, before any copy exists. It is the only
sanctioned source of facts for the kit.

**The rule that governs the whole run: if it is not in this inventory, it does
not appear in the kit.** No invented statistics, no rounded-up numbers, no
borrowed industry stats from memory, no customer names not in the asset or the
cleared proof points.

Where a channel needs a number and none exists, write
`[[NEED STAT — none in asset]]`. A loud gap is a task for a human. An invented
number is a liability that ships, and on a campaign built from a research asset
it discredits the asset — which was the only reason the campaign worked.

### The four required sections

#### 1. Claims

Every usable stat, finding, framework, and customer example.

| Claim / stat | Location | Type | Strength | Safe to use publicly? |
|---|---|---|---|---|
| 68% of teams report X | p.12, fig. 3 | Original research | Strong | Yes |
| Cites a third party on Y | p.6 | Third-party | Medium | Yes, with attribution |
| Composite assumes 7,600 engineers | p.11 | Composite / modeled | Strong | Yes, always labeled composite |
| 50% recapture rate applied | p.18 | Assumption | Medium | Yes — it shows conservatism, use it |

Group into subsections when the asset is large: headline figures, quantified
findings, costs, methodology, population. A reader looking for the one number
they half-remember should find it in seconds.

**Type matters more than it looks.** A modeled composite figure and an observed
one are both true and are not interchangeable in copy. Label composite and
modeled figures as such every time they appear, or the kit quietly claims a
measurement the asset never made.

**Note the conservative choices.** Risk adjustments, haircuts, recapture rates,
and discount rates are credibility assets, not caveats. A study that cut its
own numbers before publishing is more persuasive than one that didn't, and copy
should say so.

#### 2. Quotes

| Quote | Speaker | Location | Best used for |
|---|---|---|---|

Copy attributions **exactly as published**. If the asset attributes a quote to
a role without a company name, it stays that way forever — enriching it is
fabrication, and it is the kind that gets noticed by the person quoted.

Mark the one or two strongest. In most assets there is a single quote that
carries more weight than any statistic, usually because it names a consequence
rather than a benefit. Find it and flag it; it will earn its place on the
landing page and in the highest-stakes ad.

#### 3. Do not use

**Required. Not a footnote.** This is the section that stops the most expensive
mistakes, and the mistakes it stops are the ones a competent writer makes
naturally, because the material looks usable.

| Item | Location | Why |
|---|---|---|
| A quote wishing for future capability | p.23 | It's an aspiration, not a claim. Quoting it implies the product does this. |
| "AI-powered" phrasing in the summary | p.3 | Appears in framing but is evidenced nowhere in the findings. |
| Verticals named but not represented | p.11 | No interviewee from either. Don't target or claim them. |
| Any competitive comparison | p.8 | The asset states it is not to be used as a competitive analysis. |

What to look for while reading:

- **Aspirations dressed as capabilities.** Interview quotes about what someone
  *wants* the product to do read exactly like quotes about what it does.
- **Executive-summary framing not supported by findings.** Summaries are
  written last and often oversell the body. Trust the body.
- **Claims in the asset's own scope statements** that copy would breach — a
  stated non-use, an embargo, a limited licence.
- **Populations the asset names but doesn't evidence.** A composite described
  as serving three industries when only one was studied bounds your targeting,
  whatever the description says.
- **Anything that would need legal or customer clearance** before it ships.

#### 4. Changes the sales conversation

Things in the asset that a rep will be asked about before they expect it.
These aren't copy problems; they're briefing problems, and they cost a deal
when a prospect has read the asset more carefully than the seller.

| Item | Location | What sales needs to know |
|---|---|---|
| Full pricing, itemized | p.25–26 | Public. Anchors before the first call. Also a qualifier — use it. |
| Six-month implementation | p.12 | A prospect who reads closely finds friction. Handle it in the landing page FAQ, not in a call. |
| Consulting fees on top of licence | p.27 | Same. |
| A named limitation or exclusion | — | Better acknowledged than defended. |

Anything landing here gets two consequences: a line in the README's standing
constraints, and an FAQ entry or note in the file where a reader will first hit
it. Disclosed friction handled on your own page is a credibility gain.
Undisclosed friction found by the prospect is a credibility loss.

### Also capture while reading

- **The single most surprising or contrarian finding.** This becomes the
  campaign hook, the founder post, and the blog opener. It is usually a
  finding that inverts the expected ranking of something, and it is usually not
  in the executive summary, because summaries lead with the expected.
- **The strongest section for each persona** the ICP names, by page. The SDR
  follow-ups point each recipient at the part that matters to them, and that
  pointer is only useful if it's specific.
- **Anything outdated, unsupported, or legally risky.** Goes to the alignment
  brief as a flag, never into copy.

---

# Appendix C — The alignment brief

`00-alignment-brief.md`. Written after reading the asset, presented before any
copy exists, and **approved before any copy is written**.

This is the most valuable thing the skill does. It is the last moment at which
repositioning is cheap — after the kit is built, changing the argument means
rewriting fourteen files.

### Structure

#### 1. Asset summary in three sentences

What it argues, who it's for, what it proves. If you can't do it in three, the
asset has no single argument and that is itself the first finding.

#### 2. Priority alignment

Score the asset against what the business said it was trying to accomplish.
**Score both axes separately** — the sales motions and the business outcomes.
An asset can serve one well while contradicting the other, and collapsing them
into one table is how that gets missed.

Use this scale:

| Score | Meaning |
|---|---|
| **Direct** | The asset serves this priority as it stands |
| **Partial** | It serves it, with a caveat that changes how it should be used |
| **Thin** | Touched but not evidenced. Usable once, qualified. Never a headline. |
| **Not at all** | No support in the asset. Drop the priority from this campaign. |
| **Contradicted** | The asset argues *against* this priority |

**Contradicted is a distinct and important result.** "Not at all" means the
asset is silent; "Contradicted" means promoting the asset actively undercuts
the goal. A report describing a long enterprise sales cycle doesn't merely fail
to support a self-serve motion — it is evidence against one, and using it there
damages the motion. Say so.

One sentence of reasoning per row, citing pages. Be honest: a "Partial" is more
useful than a generous "Direct," because a generous Direct produces copy that
overclaims and a reader who feels misled.

#### 3. Audience fit

Who the asset actually speaks to, versus who the ICP says the buyer is. Name
the gap where there is one.

Two failure modes worth checking explicitly:

- **A persona who appears in the asset only as a cost line.** Research assets
  written for buyers often reduce practitioners to an hourly rate. Copy aimed
  at that persona has to be rebuilt around a number that is genuinely theirs,
  not around the ROI that was written about them.
- **An unlisted persona the asset speaks to well.** If the largest finding
  belongs to a function the ICP doesn't name, that is a buyer the company is
  not currently addressing. Recommend adding them.

Also bound the targeting. If the asset's evidence base covers narrower
verticals, segments, or company sizes than the company sells into, say where
the asset travels credibly and where it invites a question it can't answer.

#### 4. Message guide fit

Which messaging pillars the asset reinforces, which it contradicts or ignores,
and any voice or banned-word conflicts.

Where no message guide exists, say so and record what the asset's own language
establishes instead — register, framing, and any topic the asset is weaker on
than the company's usual positioning. An asset's finished copy is evidence
about voice even when no document describes it.

#### 5. The campaign spine

The decisions every other file inherits. Get these right and the kit is
coherent; get them wrong and fourteen files are wrong together.

- **Core claim** — one sentence, the argument the whole campaign makes
- **Hero stat** — the one number that carries the campaign, cited, with an
  executive variant and a practitioner variant where the audiences differ
- **Primary CTA** — the single conversion action everything ladders to
- **CTA ladder** — soft (read more) → medium (assess, benchmark, attend) → hard
  (book time), and which channel uses which
- **Three angles** — the distinct message angles the variants test: typically
  pain-led, outcome-led, and data/curiosity-led
- **Campaign hook** — the most surprising or contrarian finding, stated as a
  sentence someone would repeat
- **The "start here" pointer** — the one section or page a reader should open
  first, and why

That last one looks small and isn't. Everything downstream — the nurture track,
the SDR follow-ups, the whole second half of the funnel — assumes the asset was
actually read. A specific pointer measurably raises the odds of that, and
because it recurs in the confirmation page, the confirmation email, and the
first sales follow-up, it belongs in the spine where it's decided once.

#### 6. Gaps and risks

Missing proof, unsupported claims, thin sections, and anything needing legal or
customer clearance. Include the asset's own usage constraints and its age.

Say which deliverable each risk blocks. "Usage rights unconfirmed" is abstract;
"usage rights unconfirmed, which blocks the three ads and the blog post" is a
task someone can act on.

#### 7. Recommendation

One of four:

| Recommendation | When |
|---|---|
| **Promote as-is** | The asset serves a stated priority and is ready |
| **Promote with repositioning** | Good asset, framed against the wrong priority or audience. Propose the reframe. |
| **Fix before promoting** | Name the specific gaps that must close first |
| **Don't promote** | It doesn't serve any stated priority. Say so directly, and say what would. |

The recommendation is allowed to be uncomfortable. A skill that always says
"looks great, here's your campaign" is worth nothing at the gate, and the
person reading it can tell.

When recommending repositioning, keep it to two or three changes and rank them
by return. A brief proposing nine reframes gets none of them adopted.

### Presenting the brief

Present it and stop. Name the specific decisions that would change what gets
built, so approval is an informed act rather than a nod — typically the offer,
any recommended reframe, and anything you're proposing to drop.

If the user approves without answering them, proceed under stated assumptions
and mark every one `[[LOUD]]`. Blocking a whole kit on a question the user has
already implicitly waved through wastes their time; shipping the assumption
silently wastes their trust.

---

# Appendix D — Deliverable specs

One file per channel. The global rules in the main skill file apply to all of
them; don't restate them, apply them.


---

### 1 — Landing page

**Always written as a gated page with a form.** Ungated is handled by deleting
the form module; don't write a separate version.

Section stack, in order:

1. Eyebrow / asset type label
2. Headline
3. Subhead
4. Three value bullets — what the reader will be able to *do*, not what the
   asset *contains*
5. Form module
6. **What's inside** — the section list, each with a one-line payoff
7. **Who this is for** — 3–4 role or situation lines, so the wrong reader
   self-selects out. Include one disqualifying line; it raises lead quality
   more than any form field.
8. Pull-stat or pull-quote from the asset, cited
9. Social proof strip — logo bar, customer count, or a named quote. Where none
   are cleared, use `[[LOGOS]]` **and** the asset's own evidence base, which is
   real and citable and often the better proof point.
10. Credibility block — author, methodology, sample size, risk adjustments, and
    the commissioning relationship where there is one. Not optional on a
    commissioned asset.
11. FAQ — 3–4 questions handling the real objections to downloading (Is this
    gated? Will I be called? Is this a product pitch? How long is it? Does it
    include pricing?). Where the inventory's "changes the sales conversation"
    section flagged friction, this is where it gets handled.
12. Closing CTA

**Variants to deliver:**

- **Three headline + subhead pairs**, one per campaign angle, with an explicit
  recommendation on which to ship first and why.
- **Two CTA sets** — low-friction ("Get the report") and high-intent ("Get the
  report and the benchmark"), with a note on which pairs with which traffic
  source. Cold paid takes low-friction; house-list and organic can carry the
  high-intent ask.

**Form spec:** exact field list and a recommended count per traffic type, field
labels, button microcopy, the consent line, and which fields are
progressive-profiling candidates on a return visit. Pick one field that routes
the lead, and ask for it second.

**Build notes:** layout direction per module (one or two lines each, enough to
build without a design review); SEO title (≤60), meta description (≤155), URL
slug; OG card title, description and image direction; UTM convention; and the
exact conversion events to fire and where.

Fire at least four events: page view, **form view**, form submit, download
click. Form view is the one teams skip and the one that separates "didn't
scroll" from "saw it and declined" — without it, week one has no diagnosis.

---

### 2 — Confirmation page

Not a dead end. It is the highest-intent moment in the funnel — the visitor has
just raised their hand — and most companies spend it on the word "Thanks."

Section stack:

1. Confirmation headline and one line of reassurance
2. **Primary download button**, plus a line noting a copy is also in their inbox
3. **"Start here" pointer** — the spine's pointer, in two or three lines
4. **Next-step module** — the single highest-intent CTA, with real estate and a
   reason, not a buried link
5. **Related resources row** — three items with one-line descriptions. At least
   one should be the campaign's own blog post, which is the only item
   guaranteed to exist and be on-message.
6. **Share row** — LinkedIn, X and email share links with pre-filled text
   written out in full. Never ship a bare share icon with an empty message.
7. Optional: inline meeting booker, with a note on when to use it

**Variants:** two next-step treatments — **soft** (a related asset or session,
for early-stage traffic) and **hard** (book time, start an assessment, for
high-fit traffic) — plus a routing rule based on a form answer. Tie the rule to
something real from the form, and say why the threshold sits where it does.

**Build notes:** layout per module, download and next-step conversion events,
and `noindex`. A confirmation page in the index leaks the ungated asset and
destroys the form's data.

---

### 3 — Confirmation email

Transactional in feel, expected, and opened at rates nothing else in the kit
will match.

1. **Three subject line options** — plain and literal beats clever; the reader
   is looking for a download, not a headline
2. Preheader
3. Greeting with first-name token
4. One-line confirmation and the **download link, high in the email**
5. The same "start here" pointer as the confirmation page
6. **One** next-step CTA — one, not three
7. A line setting expectations for what arrives next, so the nurture track
   isn't a surprise. This measurably reduces unsubscribes on nurture email one.
8. Signature from a **named person**, not the brand
9. A full **plain-text version**

Single primary CTA, no navigation bar, no promotional footer. Send within
minutes of the form submit, as a transactional or triggered send, never
batched. A confirmation email that arrives the next morning has already been
replaced by the download.

---

### 4 — Promo email

To the house list — people who already know the brand.

1. **Three subject lines and matching preheaders**, one per angle, under 50
   characters
2. An opening line that earns the next line. Lead with the finding, not with
   "We are excited to announce"
3. Two or three short paragraphs, or one paragraph plus three bullets
4. The hero stat, called out visually, cited
5. **Two primary CTA button options**
6. A PS line — read more than the body in many lists; use it for the second
   angle or a timeliness note

**Length:** 120–180 words in the body.

**Variants:** the designed HTML version, plus a **plain-text, person-to-person
variant** written as if a human typed it. Often the higher performer on a warm
list, and worth testing every time. Send the plain-text version from a named
person's address, not a brand alias.

**Notes:** segmentation, suppression (anyone who already downloaded; anyone in
an open opportunity where a rep should send it personally), and a suggested
send day and time with reasoning. Hold back any segment the asset's evidence
base doesn't actually cover.

---

### 5 — Newsletter and syndication module

Written to drop into someone else's layout, where you control words and not
design.

Three lengths:

- **Micro** — one line, ≤15 words, for a quick-links roundup
- **Standard** — headline ≤55 characters, a 25–40 word blurb, CTA link text
- **Featured** — headline, subhead, 60–80 word blurb, two bullets, CTA

**Two versions of each:** an **owned** version, which can sell, and a
**syndicated / partner** version written neutrally — findings-led, brand-light,
no product language.

The partner version is not a formality. A third-party editor will not run "the
number nobody budgets for." They will run a methodology summary. Give them one
and the placement actually happens; send them the owned copy and the slot is
wasted.

**Thumbnail direction:** the visual concept in two or three lines, ≤10 words of
on-image text, the recommended aspect ratio, and the alt text written out.

---

### 6 — LinkedIn post, corporate

**Three posts** on distinct angles — stat-led, problem-led, and
what's-inside-led — staggered across the campaign, not posted together.

Each post:

1. **Hook line** — the first 140–200 characters are all that show before "see
   more." The hook has to work truncated. No throat-clearing.
2. Two to four short body lines, single-line paragraphs with white space
3. One concrete proof element from the inventory
4. CTA and a **link placement recommendation** — in-post or first comment, with
   reasoning for this specific post rather than a blanket rule
5. Three to five hashtags
6. Creative direction — single image, document carousel, or video — plus alt
   text written out

**Length:** 100–180 words each.

**Notes:** posting order and spacing, and one line on what each post tests.
Roughly a week apart; three posts about one asset inside a single week trains
the audience to scroll past the fourth.

---

### 7 — LinkedIn post, founder / executive

First person, opinionated, written like a person. This post fails the moment it
sounds like it went through marketing.

**Two versions:**

- **The POV / take** — leads with a belief about the industry that the asset's
  data supports. Structure: the belief, the moment that formed it, the number
  that confirmed it, what it means for the reader, a soft mention of the asset.
- **The build story** — why we made this, what we expected to find, what
  surprised us, what we're doing about it.

The build story only works from someone who was actually involved in
commissioning or making the asset. Name who should post which.

**Rules:** no corporate boilerplate, no "I'm proud to announce," no
press-release voice. Zero to two hashtags. The CTA is soft — "happy to send it
over" beats a download button, and it generates the comment velocity that
determines reach in the first hour.

**Length:** 150–250 words.

**Include some genuine tension** — a wrong assumption, a surprising number, an
admission. A founder post with no risk in it is a corporate post with a
headshot on it.

**Notes:** four or five suggested replies for common comment types, including
the skeptical one. On a commissioned asset someone will question its
independence, and having a straight answer ready — what was disclosed, what was
haircut, which page to check — converts that comment from a liability into the
most credible thing on the post.

---

### 8 — LinkedIn posts, sellers and SDRs

Built for volume and for people who don't write for a living. The failure mode
is twenty reps posting identical copy on the same morning, which the platform
suppresses and prospects notice.

Deliver:

1. **A fill-in-the-blank template** — a three-to-five line skeleton with clearly
   marked personalization slots
2. **Three ready-to-post variants** by seller persona — AE, SDR, and CSM or SE
   — each with a different opening move
3. **A 30-second personalization guide** — the two things a rep must change
   before posting, and how to pick them. The best opener is the most specific
   thing a real person said to them in the last 30 days, with the company name
   removed.
4. **A "don't do this" list** — no identical posts on the same day, no tagging
   prospects, no comment-bait, don't post it if you haven't read the asset, and
   any constraint the asset itself imposes

**Length:** 60–120 words per variant.

Where there's an installed base, write the CSM/SE variant so it points at
partial-deployment accounts — it does double duty with file 14.

---

### 9 — Nurture emails (×3)

To everyone who downloaded. Marketing automation, from a named person. **One
idea and one CTA per email.**

| # | Timing | Job | CTA level |
|---|---|---|---|
| 1 | Day 3 | Go deep on the single most useful finding | Soft — a section or related asset |
| 2 | Day 8 | Show the finding applied — proof, story, or worked example | Medium — case study or session |
| 3 | Day 15 | Make the offer | Hard — book time or start an assessment |

Each: **two subject line options**, a preheader, 80–140 words, one CTA, and a
named-person signature.

Email 3 should say something honest about the limits of the asset's numbers
before asking for time — where the reader's situation differs from the asset's,
and which figures actually transfer. Naming the limit is what earns the ask.

**Notes:**

- **Branch and exit rules** — a click on email 1 or 2 routes to sales and exits
  the track; any reply exits and hands to a human; anyone who books exits
  immediately; no opens across all three moves to a low-frequency list.
- Suppress the whole track from existing customers where file 14 exists.
- What to do with a contact who reaches the end without converting: leave them
  on the house list and nothing else. A research download is as often a
  research signal as a buying signal.
- Why email 3 doesn't work without 1 and 2 earning it.

---

### 10 — SDR cold outreach

To prospects who have **not** downloaded. The asset is the reason to reach out
and the gift; the meeting is not the ask in version one.

1. **Three subject lines**, five words or fewer, lowercase, no brackets or
   "RE:" tricks
2. **Relevance line** — a trigger or observation about their world, with the
   personalization slot marked
3. **The finding** — the one insight that matters to *this* persona, in one or
   two sentences
4. **The offer** — send it directly, ungated, no form. Making a prospect fill in
   a form from a cold email is how the email gets deleted. The gate exists for
   inbound traffic, not for someone you interrupted.
5. **The ask** — low friction

**Length:** 50–90 words.

**Two versions:** a **pure give** with no meeting ask at all, and a **give plus
soft ask**, with a note on which to lead with by segment.

**Also include:** a LinkedIn DM variant under 400 characters, and a 20-second
voicemail or cold-call opener built on the same finding, so the rep runs one
message across three channels.

**Notes:** bound the target verticals to what the asset's evidence base
actually covers, and brief the rep on anything from the inventory's "changes
the sales conversation" section — especially disclosed pricing, which a
prospect can read before the first call.

---

### 11 — SDR follow-ups after download (×3)

To people who **did** download. Human, one-to-one, referencing a real action.

| # | Timing | Job |
|---|---|---|
| 1 | Day 1 | Point them at the section that matters for their role. Ask a question. No meeting ask. |
| 2 | Day 4 | Bring a second angle or a customer parallel. Soft meeting ask. |
| 3 | Day 10 | Permission to close the loop. Leave something useful either way. |

Each: two subject options, 40–80 words, marked personalization slots, one ask.

Include a **role-routing table** — which page or section to point each persona
at, and why. The pointer is only useful if it's specific.

**Notes:**

- **What not to say.** Don't open with "I saw you downloaded our report." It
  reads as surveillance and it is the most common way this sequence dies. Lead
  with the content; reference the download second, or not at all.
- **Hand-off rule** — the fit signals and reply types that route to an AE
  immediately rather than continuing the sequence.
- **When a download is a research signal rather than a buying signal**, and how
  the tone should change. Most of them are. Be more useful and less directional,
  and stop at follow-up 2. A researcher treated well becomes the internal
  champion later; one who gets chased becomes the reason the next email is
  deleted.

---

### 12 — Blog post

A standalone post that **earns** the download — not a teaser, not a summary.
Give away one real, complete finding. A post that withholds everything converts
worse than one that proves the asset is worth reading.

1. H1 and dek
2. **Intro that states the takeaway in the first 40–60 words.** No windup. This
   is what gets quoted by an answer engine and what keeps a skimmer reading.
3. Three to five H2 sections, each answering one real question a reader would
   type or ask
4. One data callout from the inventory, cited
5. A pull quote
6. Internal links list — which pages to link, with anchor text
7. CTA block mid-post and a closing CTA block

**Length:** 900–1,400 words.

Put the commissioning disclosure in the second section, not at the bottom.

**AEO and SEO spec:**

- SEO title, meta description, URL slug, primary target query
- Three to five related questions the post answers **directly, each in a
  self-contained 40–60 word block**. Each must stand alone if lifted out of the
  page — that is precisely what makes a page quotable by an answer engine.
  Include one that addresses the asset's credibility if it's commissioned;
  "is a vendor-funded study credible" is a real query with a real answer.
- FAQ schema recommendation
- Suggested author and expertise signals worth surfacing. A named person, not
  a team byline.

---

### 13 — LinkedIn ads (×3)

Three ads that isolate different variables, not three rewrites of one. Default
format: single-image sponsored content.

Per ad:

- **Two intro text options**, each front-loading the hook into the first ~150
  characters before truncation
- **Two headline options**, ≤70 characters
- Description line
- **CTA button** chosen from the platform's actual list
- **Creative direction** — the concept, ≤10 words of on-image text, the
  recommended ratio, and written alt text
- **Audience** — the targeting cut this ad is written for

| Ad | Angle | Audience | Isolates |
|---|---|---|---|
| A | Stat / curiosity-led | Cold, ICP-targeted | Whether the data hook pulls |
| B | Pain / problem-led | Cold, ICP-targeted | Whether the problem framing pulls |
| C | Retargeting | Visitors and viewers who didn't convert | Whether familiarity plus a harder CTA converts |

**Also include** a **Thought Leader ad** variant using the founder post from
file 7. These consistently outperform standard sponsored content for research
assets and cost nothing extra to produce here, because the copy already exists.
Note what permission it needs. Where that format isn't available, a Document ad
built from the file 6 carousel is the fallback.

**Notes:** a testing plan — what to read after week one, what a winner looks
like, and the one variable to change next. Read cost per download rather than
cost per click; a cheap click on the wrong audience is how the budget
disappears. Don't run more than three cold variants at once on a modest budget,
or nothing reaches significance.

**Gate these on usage rights.** Ads and the blog are where excerpting a
third-party asset is most exposed. If rights are unconfirmed, say so at the top
of the file.

---

### 14 — Expansion track *(conditional)*

**Only produce this if the company has a relevant installed base.** Skip it for
a pre-revenue company rather than padding the kit.

Most assets serve expansion at least as well as acquisition, and nobody asks,
because campaign briefs are acquisition-shaped by default. The signal to look
for in the asset: **does its value scale with something the customer can have
more of?** Seats, coverage, deployment, volume, breadth of use. If the asset's
own model assumes growth along that axis, it has made the expansion argument
already — and a third-party asset making it is far stronger than a vendor
making it.

Structure:

1. **The argument in one paragraph**, with the evidence from the asset
2. **Segment table** — which customers get which play, and the signal that
   sorts them
3. **Three plays**, each a short email from the right role:
   - **Coverage** — to the economic buyer, where deployment is partial
   - **Adoption** — to the platform owner, where deployment is flat. The ask is
     a service, not a purchase.
   - **Consolidation** — to procurement or the functional lead, where spend is
     still fragmented outside the product
4. **In-life placements** — the QBR slide, the renewal conversation, and which
   seller post from file 8 points here

**Notes:** suppress every existing customer from the acquisition nurture track.
An email explaining the ROI of a product they already own is the fastest way to
look like nobody is talking internally. And only run the coverage play where
coverage is genuinely partial.

---

### Index file (`README.md`)

Write this last, once every deliverable exists.

1. **Campaign spine**, restated at the top, so anyone opening the folder sees
   the message before the copy
2. **File index** — the table from *What Claude delivers*, with a one-line
   description of each
3. **Launch sequence** — a dated table of what publishes when, with owners.
   Respect real dependencies: the blog goes live before the retargeting ad,
   because the retargeting audience is built from its traffic.
4. **UTM convention**, as a table with one filled-in example per channel:
   `?utm_source=<channel>&utm_medium=<type>&utm_campaign=<asset-slug>&utm_content=<file>-<variant>`
5. **Measurement** — the three or four numbers that say whether this worked,
   each with its honest denominator. Landing page conversion against *form
   views*, not page views. Download rate against form submits, which is the only
   number that tests whether the asset was read. Cost per download, not per
   click. Meetings attributed, counted first-touch and last-touch separately
   and never averaged. Say explicitly what not to report: impressions, reach,
   and "engagement" move no decision about this campaign.
6. **Open items** — every `[[PLACEHOLDER]]`, everything needing clearance, and
   every `[[NEED STAT]]` gap, in one list, split into blocking and
   non-blocking, each naming the file it blocks.
7. **Standing constraints** — the rules that bind every file: the asset's own
   usage restrictions, the disclosure obligation, attribution discipline,
   targeting bounds, and anything from the inventory's "changes the sales
   conversation" section that sales must be briefed on before launch.
