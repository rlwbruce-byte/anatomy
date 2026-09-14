---
name: call-summary
description: Build a meeting write-up or call recap from an AI notetaker's summary, a raw transcript, and handwritten or typed notes. Produces a structured record with date, time, participants (including each participant's organization and title), a TL;DR, decisions made, open items with named owners, a thematic notes summary, and a chronological outline of every topic in the order it came up. Cross-checks the questions the user planned to ask against what the transcript shows was actually answered, and flags where the sources disagree rather than inventing facts. Each run ships the markdown record plus a Word copy and a web page rendered from it, so the three cannot drift, and a plain-text CRM log block ready to paste into an activity or call record. Use when asked to write up a call, turn meeting notes into a recap, debrief an interview or discovery call, or summarize a conversation from a transcript.
created: 2026-09-10
updated: 2026-09-11
---

# Call Summary — a notetaker's output plus your own notes, into one record

You are turning the raw output of a call into the single document someone would actually
reread a month later. The inputs are messy and partly contradictory: an AI notetaker's
summary that is well organized but paraphrased and occasionally wrong, a raw transcript that
is accurate on substance and unreliable on proper nouns, and the user's own notes, which are
fragmentary but tell you what they thought mattered.

The job is a merge, not a summary of a summary. **Every fact in the record must trace to one
of the inputs.** When they disagree, say so in the document rather than picking a winner
silently.

One call, one run. Never merge two calls into one document, even with the same person — a
write-up is the record of a conversation, and its date is part of what it records.

## What a run produces

| Output | Role |
|---|---|
| `<file>.md` | **The source of truth.** Everything else is rendered from it. |
| `<file>.docx` | The copy to send, print, or mark up |
| `<file>.html` | A page to publish, for a link that opens anywhere |
| **CRM log** | A plain-text block inside the record, sized and formatted to paste straight into a CRM activity |

All three, every run, and the two rendered files are built from the markdown rather than
written by hand — that is the only thing keeping three copies of one call from disagreeing
with each other later.

## Step 0 — Intake, and the precedence rule

Resolve today's date from the environment rather than from memory, and use it only as a
fallback — never date a record from today when the inputs state a date. Then take inventory,
because each input plays a different role:

| Input | What it's good for | What not to trust it on |
|---|---|---|
| **The user's own notes** | What mattered to them, their questions, their read on people | Completeness — they stop mid-thought |
| **The transcript** | Substance, numbers, quotes, who said what | Proper nouns — names, companies and products are frequently mis-transcribed |
| **The AI summary** | Structure and the next-steps block | Precision — it paraphrases, and sometimes states as fact what was hedged on the call |

**Precedence: the transcript settles what was said; the user's notes settle what was
important; the AI summary is scaffolding, never a source of record.**

Work with whatever you are given, and say in *Sources* what was missing. Three common
partial cases, each with a consequence to state rather than paper over:

- **No personal notes.** There is no pre-call question list, so Step 2 cannot run. Say so —
  *Still open* will hold only threads raised on the call itself.
- **No transcript.** Every fact is now paraphrase, so conflicts cannot be adjudicated. Mark
  the record as summary-derived and keep the *Conflicts* bar low: flag more, not less.
- **No AI summary.** No loss. Work from the transcript and notes.

## Step 1 — Resolve the header facts before writing a word

These are the ones that get fudged, so resolve each deliberately.

**Date.** From the notes header or the meeting record. A notetaker often gives a bare
`Sep 10` — expand to ISO `YYYY-MM-DD` using the meeting's year, not today's.

**Time.** Rarely in either export. Ladder, in order: an explicit time in the notes or
transcript → the calendar event on that date, if a calendar tool is connected →
`not recorded`. Record the timezone when you have one, and note the duration if the
transcript shows the call ran long or ended early. **Do not back-fill a plausible time.**

**Participants.** A notetaker's participants line is unreliable — it commonly lists only the
account holder who recorded. Build the real list from the transcript's speaker turns, the
user's notes, and the calendar invite. The user is always a participant.

**Org and title for each participant.** Resolve in this order, stopping at the first hit:

1. Stated in the transcript or notes ("Lindsay, she covers supply chain").
2. Already recorded in the user's own files — earlier write-ups, account research, a client
   folder.
3. The calendar invite attendee list, or the email domain, if a calendar or mail tool is
   connected.
4. `— (not stated)`.

**Never infer a title from what a person talked about.** Someone discussing budget is not
thereby a VP. A background described loosely ("product marketing background") is a
background, not a title — write what was said and mark the exact title as not stated.

Everyone named on the call but not *on* the call goes in a separate **People mentioned**
table, same discipline. It keeps the participants table honest and builds the org chart the
user is actually assembling.

## Step 2 — Cross-check the pre-call questions

The highest-value pass, and the one most easily skipped. The user's notes usually carry a
question list — sometimes headed `QUESTIONS`, sometimes just lines ending in a question
mark. Walk each against the transcript and sort it:

- **Answered** — record the answer, compressed, in the notes summary.
- **Partially answered** — they asked which tier most customers sit at and got the tiering
  philosophy instead. Partial is not answered. It stays open, marked partial.
- **Not asked** — it becomes a row under *Still open*.

A question they never got to is the most reusable thing in the document. Never drop one
because the conversation went somewhere else.

## Step 3 — Write the document

Sections, in this order, with these exact names. Renderers key on the names, so renaming a
section changes the layout of the Word file and the page.

Front-matter carries `date`, `time`, `duration`, `type`, `company`, `title`, `participants`,
`source`, `artifact` and `status`. Then: an H1 of `YYYY-MM-DD — <meeting title>`, the
**Date / Time / Duration / Platform** header lines, **Participants**, **People mentioned**,
**TL;DR**, **Decisions made**, **Open items** (with `Committed follow-ups` and `Still open`
beneath it), **Notes summary**, **Discussion outline**, **Conflicts and unknowns**, **CRM log**,
and **Sources**.

**TL;DR** — 3 to 6 bullets, full sentences. Lead with the thing that changes what the user
does next, not with what happened first. Someone who reads only this should be able to hold
their end of a conversation about the call.

**Decisions made** — only what was *settled on this call*, and who settled it. Three things
that are not decisions and belong elsewhere: a decision the other side reported having made
earlier (notes summary), an idea someone liked (notes summary), and a commitment to do
something (open items). **"None — nothing was settled on this call" is a legitimate and
common answer**, especially for interviews and first meetings. Write it rather than padding.

**Open items** — two tables. *Committed follow-ups* has columns `#`, `Item`, `Owner`, `Due`,
`Source`, and a named human owner in every row, never "the team"; where the call set no
date, Due reads `not set` rather than an invented one. *Still open* has columns `#`,
`Question or thread`, `Why it matters`, `Status`, and holds unanswered questions and threads
raised without an owner. Status is `Not asked`, `Partially answered`, or `No owner` — those
exact words, since they render as pills on the page.

**Notes summary** — thematic sections, not a chronological replay. Five to nine sections of
three to eight bullets. Preserve every number, name, dollar figure, date and product name
verbatim — the specifics are the whole value. Where a bullet is the user's read rather than
something stated on the call, attribute it to them.

**Discussion outline** — every topic in the order it came up, one line each, no analysis.
Not optional. The notes summary reorganizes the call by theme, and reorganizing is exactly
how a topic goes missing: an aside that fits no theme gets dropped, and nobody notices
because the document still reads complete. The outline is what the user reads against their
own memory to catch what the summary lost. So it covers the whole call including the small
stuff — the scheduling mix-up at the top, the one-line aside near the end — and a topic that
appears nowhere else in the record still appears here. Twenty to thirty lines is normal for
an hour. It goes last, because that is where you reach for it: the document has been read,
and now you are checking whether anything is missing.

**CRM log** — a fenced plain-text block holding the version of this call that belongs in a
CRM activity record. It exists because the record itself does not paste: a CRM activity field
strips markdown, mangles tables, and truncates long text, so a document written for a human
reader arrives there as noise. Keep it to roughly 12 to 18 lines, plain text only, no
markdown syntax, no tables, no bold. Lead with the date and who was on the call, then the
one-paragraph summary, then decisions, then next steps as `Owner — action — due`, then the
page link if there is one. Every line must survive being pasted into a single-line-per-entry
field. This is a compression of what is already in the record, so it introduces no fact that
is not above it.

If the session has a CRM connector, offer to write the activity directly rather than
handing over text to paste — and ask before writing to a CRM, always. Logging to someone's
system of record is not a step to take on your own initiative.

**Conflicts and unknowns** — where the sources disagree, where a proper noun looks
mis-transcribed, where a name in the notes appears nowhere in the transcript. One line each,
stating both readings. Where you resolve one against an outside source, say so and keep the
entry: the resolution is worth more than the silence. Omit the section only if it is truly
empty; never resolve a conflict by picking quietly.

Voice: plain past tense, third person, named people by name. No corporate throat clearing,
no "the meeting commenced." Quote directly only where the exact wording carries something a
paraphrase would lose.

## Step 4 — File it, render it, publish it

Save the markdown where the user keeps call records, named `YYYY-MM-DD-<person-or-topic>.md`
and filed under the company the call belongs to. **If the transcript's rendering of the
company name is at all uncertain, verify it against the live web before creating a folder**
— a mis-transcribed name becomes a permanently wrong directory, and notetakers get company
names wrong often enough that this is a real risk, not a theoretical one. If the call has no
company anchor at all, ask where it goes rather than inventing a location.

Then render the Word copy and the page **from the finished markdown**, so they cannot drift
from the record or from each other. Never hand-build either one: generate them with whatever
document tooling the session has, and keep the tables as real tables — those are what get
read on a phone and pasted into a follow-up email.

Publish the HTML if the session can, and **write the returned URL into the record's
front-matter as `artifact:`**, so a later correction republishes to the same link instead of
minting a second one. If it is already set, publish to that URL. If publishing isn't
available in the session, say so plainly and carry on — a missing link degrades a run, it
doesn't fail it.

Hand the Word file to the user directly rather than only naming a path.

## Step 5 — Save it, and push the follow-ups onward

A record that lives only in the chat window is lost when the session ends. Commit it, or
save it where the user's files actually persist, and say plainly if you could not.

Then close the loop on the open items: every *Committed follow-up* owned by the user belongs
in whatever list they actually track, added in the same session. The record captures them;
the list is what surfaces them again.

## Definition of done

A run is finished when all of these are true. If one isn't, say which.

- [ ] Date is ISO and taken from the inputs, not from today.
- [ ] Every participant has an org, and a title or an explicit `— (not stated)`.
- [ ] Every pre-call question is answered, marked partial, or sitting in *Still open*.
- [ ] Every committed follow-up has a named human owner.
- [ ] The discussion outline covers the call end to end, including the small stuff.
- [ ] Conflicts are flagged, not silently resolved.
- [ ] `.md`, `.docx` and `.html` all exist and were rendered from the same markdown.
- [ ] The CRM log block is plain text and pastes without markdown artifacts.
- [ ] The artifact URL is in the front-matter.
- [ ] The files are saved somewhere that survives the session.
- [ ] The user's follow-ups are on their open-items list.

## Never

- Never invent a time, a title, an org, a last name, or a due date. `not recorded`,
  `— (not stated)` and `not set` are correct answers.
- Never let the AI summary override the transcript on a fact.
- Never drop one of the user's questions because the conversation moved on.
- Never smooth over a name conflict between sources — flag it.
- Never hand-build the `.docx` or the `.html`. Render them, or they drift.
- Never write to a CRM without asking first, even when a connector is available.
- Never put a fact in the CRM log that isn't already in the record above it.

## Works great with

- **Company Identity Builder** — run it on the company before the next call; the questions
  left open in a record make good inputs.
- **Target Account Snapshot** — a prospect call record feeds the stakeholder map directly.
- **Basic Discovery** — pairs with an interview loop or a first discovery call.
