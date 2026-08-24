---
name: company-identity-builder
description: Given a company URL, builds a complete company identity — brand colors, competitors, category, sales plays, proof points, and beachhead offering — through evidence-backed web research, answering one question at a time with approval gates, then outputs a README.md, a self-contained HTML brand deck, and an llms.txt. Use when the user provides a company URL and wants GTM/brand positioning research, an account/brand identity, or a brand overview deck built from it.
created: 2026-07-21
updated: 2026-07-24
---

# Company Identity Builder

Build a company's identity from its URL by answering six fixed GTM/brand
questions about it, one at a time, using real evidence gathered from the web —
not assumptions. This feeds real GTM/sales work, so treat every answer as
something the user might repeat back to a prospect or use in positioning —
cite where each claim came from.

## How to run this

1. Confirm the URL if not given directly.
2. Research and answer **Question 1 only**, then stop and explicitly ask for
   review/approval (e.g. "Does this look right, or should I adjust
   anything?") before moving to Question 2. This is an approval gate, not
   just a pacing pause — if the user pushes back or corrects something,
   revise and re-present that same question before moving on. Only treat a
   question as locked in once the user approves it. Repeat through
   Question 6.
   - If the user says "just give me all of them" or similar, it's fine to
     collapse the pacing — but default to one-at-a-time-with-approval unless
     told otherwise.
3. Each answer should be evidence-backed: name the specific page, article, or
   review you pulled it from. If you can't find solid evidence for part of an
   answer, say so explicitly rather than guessing — GTM calls made on
   fabricated "facts" are worse than no answer.
4. Keep a running tally of the approved answers (with their sources) as you
   go — you'll need all six, finalized, to build the outputs in the next
   step.

## Research approach

Don't rely on a single homepage fetch. Pull from a mix of:

- **The company's own site**: homepage, about/company page, pricing page,
  product pages, customer stories/case studies section, blog, careers page
  (careers pages often reveal GTM motion and org structure — e.g. a big SDR
  team signals outbound-led, a small team with self-serve signage signals
  PLG).
- **Live CSS extraction for brand colors**: when a browser tool is available,
  read the rendered page's computed styles and CSS custom properties rather
  than eyeballing a screenshot — this is how you get real hex values (see
  Question 1).
- **Review sites**: G2, Capterra, TrustRadius — great source for proof points,
  competitor comparisons ("alternatives to X"), and real buyer language.
- **News/press**: funding announcements, leadership hires (a VP of Sales hire
  vs. a Head of Growth hire signals different GTM motions), partnership
  announcements.
- **Analyst content**: Gartner/Forrester mentions, industry reports, if
  surfaced in search results.
- **LinkedIn**: company page and exec posts often state positioning and ICP
  more plainly than the marketing site does.

Use web search broadly before settling on an answer — the company's own
copy tells you how they want to be seen, but competitor/review/news sources
tell you how the market actually sees them. Both matter for a GTM read.

## The six questions

### 1. Brand colors
Identify the primary and secondary brand colors (hex codes where possible).
Prefer **live extraction**: with a browser tool, read `getComputedStyle` on
the header/nav/body/CTA buttons and enumerate `:root` CSS custom properties
(`--color-*`, `--brand-*`) to capture real hex values and the actual
typeface. Without a browser, fetch the homepage source and look for CSS
custom properties, inline styles, the `<meta name="theme-color">` tag, and
SVG logo fill/stroke attributes. If exact hex values aren't extractable,
describe the palette (e.g. "deep navy primary, coral accent") and name where
you observed it. Note explicitly if you're inferring from visual description
rather than reading an actual hex value. Watch for dual-mode (light + dark)
identities — capture both grounds, not just one.

### 2. Competitors
Who competes for the same buyer? Triangulate from: the company's own
"vs. X" or comparison pages, G2/Capterra "alternatives to [company]" lists,
and how the company categorizes itself (which tells you the comparison set
they're implicitly inviting). List 3-6 core competitors (more if the space is
crowded), note category leader/challenger/niche standing, and flag market
consolidation (acquisitions of former competitors) — it's a useful signal.

### 3. Categories
What category/categories does this company fall into? Check how they
self-describe (homepage tagline, meta description, "what is [product]"
messaging) versus how third parties categorize them (G2 category pages,
analyst reports, press coverage framing). Flag it if there's a mismatch —
e.g. a company positioning itself as a broad "platform" that reviewers still
file under a narrow point-solution category is itself a useful signal. Note
any category the company is actively trying to create or rename.

### 4. Sales plays
What GTM motion(s) are they running? Look for signal on:
- **Motion**: self-serve/PLG (free trial, "start free," instant signup)
  vs. sales-led (demo request, "talk to sales," gated pricing) vs. hybrid
  vs. partner/channel-led. Look for a PLG on-ramp underneath a sales-led
  motion (free tier feeding an enterprise funnel) — it's easy to miss.
- **Buyer personas**: whose pain does the messaging target — economic buyer
  (CFO/VP language, ROI framing) vs. technical buyer (developer docs,
  API-first messaging) vs. end-user (ease-of-use, individual productivity
  framing)? Multiple personas often means multiple entry points.
- **Sales strategy signals**: pricing page structure (per-seat vs.
  usage-based vs. custom/"contact us" only), presence of a partner/reseller
  program, land-and-expand cues (tiered plans, add-ons, usage-based upsell),
  vertical plays (e.g. a dedicated Federal/SLED or industry AE), and job
  postings for sales/CS roles (titles and seniority reveal deal size and
  motion).

### 5. Proof points
Catalog what evidence of value they surface, and where:
- Customer logos and case studies (note if named customers are enterprise
  brand names — enterprise social proof — or if proof leans on volume/reviews
  instead)
- Specific ROI or outcome metrics ("reduced X by Y%," "saved Z hours") — note
  whether these are attributed to a named customer or generic
- Testimonials/quotes, and whether they're from named individuals with
  title+company (stronger signal) or anonymous
- Analyst validation (Gartner Magic Quadrant, Forrester Wave, market guides,
  G2 badges), certifications (SOC 2, HIPAA), and funding as credibility
- Supporting assets referenced or gated (ROI/TCO calculators, whitepapers,
  benchmark reports, webinars)

### 6. Most-adopted entry point
Given the sales play(s) identified in Question 4, which looks like the most
commonly adopted path into the customer base? Answer specifically:
- **Most common customer entry point** — which product, tier, or use case
  shows up most in case studies/testimonials as the "way in"?
- **Which offering lands accounts** — is there one SKU/tier that's clearly
  the wedge (cheapest, most case studies, most reviews mention starting
  there) versus offerings that show up mainly in expansion/upsell context?
- **Beachhead offering** — synthesize the above into a single answer: what
  is the one thing this company gets a new customer to say yes to first,
  before expanding the relationship? Ground this in evidence from case
  studies, pricing structure, and review patterns rather than assumption.

## Per-question presentation format

For each question, lead with a direct answer (2-4 sentences), then a short
bulleted list of the evidence/sources behind it. Keep it scannable — this is
working research for sales strategy, not a report to polish. End every
question's presentation with an explicit ask for approval before moving on
(see step 2 above).

## Final deliverables (once all six are approved)

After the last question is approved, ask where to save the output before
writing anything (don't assume a default location — it varies by project).
Then produce **three** files in that location:

1. **`README.md`** — a company identity readme, structured as one section per
   question, written in finished prose/bullets (not just a copy-paste of the
   chat answers — tighten it up now that the full picture is in front of
   you). Include a short header with company name, URL, and the date
   researched. This is the file the user will reference later without needing
   to re-read the whole conversation, so it should stand alone. If the run
   reconciled against a prior/source document, flag corrections clearly
   (e.g. a "✳ corrected" marker) so verified facts are distinguishable from
   inherited ones.

2. **A brand overview HTML deck** — a single self-contained `.html` file,
   viewable directly in a browser, that presents the same six sections as a
   visual one-pager/deck rather than a document. Use the actual brand colors
   identified in Question 1 as the deck's palette (with enough contrast
   adjustment to stay readable — don't just slap the raw hex codes on text
   over the same hex as background). Structure it as a title section
   (company name + URL) followed by one visual block per question —
   competitors and proof points work well as cards/grids, the sales-play and
   beachhead sections work well as short narrative blocks with a pull-quote
   or stat callout if the research surfaced a strong metric. Keep it to a
   single scrollable page, no external dependencies (inline all CSS), and
   make it presentable enough to screen-share or forward as-is.
   - Before writing this file, if a visual-design skill is available
     (e.g. `canvas-design`, `brand-guidelines`, or `web-artifacts-builder`),
     load it to calibrate the visual treatment. If none is available, apply
     the brand colors from Question 1 directly and proceed.
   - After saving the `.html` file to disk, also deliver it to the user with
     SendUserFile so it's immediately previewable in the session, in addition
     to the saved copy. If the user is on the desktop app and will revisit
     the deck, additionally persist it as an artifact via
     `mcp__remote-devices__create_artifact` using the file_uuid SendUserFile
     returns.

3. **`llms.txt`** — a concise, LLM-friendly plain-markdown summary of the
   company identity, following the llms.txt convention: an H1 with the
   company name, a one-line `>` blockquote summary, then short sections
   distilling the six answers into the most load-bearing facts. This is the
   machine-readable companion to the README — dense, link-rich, no
   decoration. Use this structure:

   ```markdown
   # [Company Name]

   > [One-sentence positioning statement.]

   [1-2 sentence plain description: what they do and who for.]

   ## Categories
   - Primary: [company-defined category]
   - Also: [established market categories]

   ## Brand
   - Colors: [name — #hex], [name — #hex], ...
   - Typeface: [font]

   ## Competitors
   - Direct: [a, b, c]
   - Adjacent: [d, e]

   ## Go-to-market
   - Motion: [sales-led / PLG / hybrid + detail]
   - Buyer personas: [champion, users, economic buyer, approvers]
   - Beachhead: [the first "yes" / land wedge]
   - Expansion: [land-and-expand path]

   ## Proof points
   - [Named metric/customer], [analyst validation], [certifications, funding]

   ## Sources
   - [label](url)
   - [label](url)
   ```

Tell the user all three file paths (and the previewable deck) when done.
