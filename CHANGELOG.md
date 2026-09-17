# Changelog

All notable changes to the site are recorded here, most recent first.

## 2026-09-17

The six Coming Soon pages come back. Every page on the site is now live.

- **Restored About, the Offerings hub and the four offering pages** from their
  archived versions at `0b5f3a6`. Not a verbatim restore: those versions predate
  several decisions, so each page was reconciled against CLAUDE.md first.
- **The archived nav still carried a Home item**, removed by the nav regroup in
  `01a9da6`. Restoring verbatim would have shipped a nav on six pages that
  disagreed with the other five. All eleven nav blocks now hash identically.
- **The archived footer was missing the LinkedIn link** wired in `4c3be56`. Same
  transplant, same check: all eleven footers now hash identically.
- **`about.html` still sized the ideal customer at "2 to 200."** It was already a
  splash page when the ICP was resized to 1 to 100, so it never got the edit, and
  it was the only file on the site still carrying the old figure.
- **"Full transfer at handover" in four places** did not carry the enablement
  qualifier. Now "Yours at handover, following enablement."
- **"GTM Operating System" in five places**, which the naming decision retired.
  The three meta descriptions and the sequence lead now say Anatomy OS; the
  remaining two describe the product rather than expanding the name.
- **"a AI Sprint" in four places.** Now "an AI Sprint."
- **Every `.placeholder-block` is commented out.** Four dashed amber panels
  reading "PLACEHOLDER, PENDING CLIENT INPUT" would have rendered on public
  offering pages. Commented, not deleted, matching how testimonials are held.
  Verified in a real browser: no page renders any internal marker.

- **Added `CNAME`** containing `gtmanatomy.ai`. The custom domain lived only in
  GitHub Pages repo settings, where a settings reset would have silently dropped
  it and broken every root-relative asset path.

- **Added `scripts/gen-md-twins.py` and `scripts/gen-llms-full.py`.** The twin
  generator lived in the session scratchpad and did not survive it, which is how
  the twins drift. The generator **refuses** `getting-started.html`,
  `marketing.html` and `go-to-market.html`, whose cards are built client-side
  from the `SKILLS` array: a static scrape empties those twins, and did, before
  the guard went in.
- `contact.md` regenerates byte-identical to the committed version, which is what
  establishes the generator matches the existing convention rather than inventing
  a new one.
- **The role-tile fix generalized.** `index.md` now renders every `.spec-item`
  label in bold instead of running the label into its paragraph, the same defect
  that hid the role tiles from answer engines in September.

- **Fixed a horizontal scroll at 320px** on Home and the Offerings hub.
  `.offer-grid` used `minmax(340px,1fr)`, which cannot shrink below 340px, so the
  offer cards pushed the page 40px wider than a small phone. Now
  `minmax(min(340px,100%),1fr)`. Checked at 1440, 1280, 1024, 900, 375 and 320.
- **"Timeline scoped per project" reads "Scoped per project"** in the two
  `.offer-timeline` slots, which carry a "Timeline:" label in the markdown twin
  and were rendering "Timeline: Timeline scoped per project" to answer engines.
- **`llms.txt` Status block** now says every page is complete, and the pricing
  summary says "starting at $5,000" to match the site.
- **`sitemap.xml`** lastmod dates updated for the seven pages that changed.

## 2026-09-14 (17)

- **Dropped "Or try it free if you prefer to build yourself."** from the skills
  band lead. The section now opens on "Sharing is caring:".
- **Role tile labels**: "Founder or CEO" is now "Founder/CEO", and "GTM
  Operations" is now "GTM Ops Teams". The second one also settles the parallelism
  flagged when the tiles were written: every label now names a person or a group
  rather than a function.
- **Fixed a gap in the markdown twins.** The extractor never matched
  `h3.persona-name`, so the five role tiles reached `index.md` and
  `llms-full.txt` as unlabelled paragraphs: an answer engine could read the five
  lines but not tell which role each belonged to. Caught while checking the
  relabel had propagated.

## 2026-09-14 (16)

- **Contact copy**: "Include the company name when you book so we can be better
  prepared for our discussion."
- **Nav wordmark aligns with the hero.** It sat 40px inside it. Cause was two
  competing gutter patterns: the hero puts its 40px gutter on an outer wrapper and
  caps the inner element at 1040px, while the nav carried both the cap and the
  gutter itself, which inset it by the gutter width. Widening the nav cap to
  1120px (1040 plus two gutters) makes the two land on the same line at 1440,
  1280, 900 and 375px. `.subnav-inner` got the same treatment.
- Noted in CLAUDE.md that `.section`, `.how` and `.skills-section` are still the
  inset pattern, so light-ground content sits 40px right of the hero and footer.
  Left as is, pending a decision.

## 2026-09-14 (15)

- **Contact now uses Calendly's own inline widget** rather than a hand-rolled
  iframe, with the client's brand-themed link: background `faf6f2`, text
  `0b0e12`, primary `f5a623`, which are `--paper`, `--graphite` and `--amber`.
  The widget's ground matches the page, so it sits on the page rather than in a
  card.
- **Overrode Calendly's `min-width:320px`** under 420px. Their inline style would
  have forced a sideways scroll on a narrow phone; verified clean at 320px.
- **Removed `initContactForm()` and `initEmbed()` from `assets/site.js`.**
  Calendly replaced both, nothing called them any more, and a mailto-composing
  form helper that no page uses is exactly the kind of thing someone later
  mistakes for live code. 2.2KB out of the shared script.
- **Nav Contact button is "Contact" again.** An earlier instruction to rename a
  contact button was applied to the nav; it meant the contact page heading, which
  is "Let's chat." The nav item is wayfinding and the amber fill already carries
  the emphasis.

## 2026-09-14 (14)

Booking and social go live.

- **"Drop us a DM" now links to the company LinkedIn**, and the line reads "us"
  and "let us know" rather than the first person. That also settles the voice
  wobble flagged earlier: the practice speaks as "we" everywhere on the site.
- **`contact.html` is no longer a splash page.** It carries the Calendly booking
  embed, with email and LinkedIn below it as fallbacks. Calendly collects the
  details at the point of booking, so it serves as the contact form too and no
  separate form is wired.
- **LinkedIn added to the footer** Company column on all eleven pages.
- **Fixed a shipped bug found while testing the embed.** The page's inline script
  carried a literal `\n` instead of a newline, which threw a syntax error and
  silently killed every call in the block, `setActiveNav` included. Caught by
  asserting the iframe actually built rather than trusting the screenshot.

## 2026-09-14 (13)

Home page formatting pass.

- **Nav regrouped.** The wordmark holds the left edge and every button is pushed
  hard right against the call to action.
- **Home removed from the nav.** The wordmark is the home link and already
  carries the right label for screen readers, so the item was a duplicate.
- **Contact is now the nav's call to action**, labelled "Let's Chat" and filled
  amber. The current page dropped from a filled amber chip to a faint amber wash,
  so the solid amber appears exactly once in the bar.
- **"Start here" is now "Getting Started"**, on the home skills band and in the
  Coming Soon cards.
- **Offering cards break before the link.** `.offer-meta` stacks, so price and
  timeline sit above the "See the ..." link rather than beside it.
- **Coming Soon cards are headed "Coming soon."** rather than "Not live yet." The
  status badge came out of the page header at the same time, because the phrase
  was otherwise appearing twice within one screen.

## 2026-09-14 (12)

Merged the skills-library work that landed on `main` while the site restructure
was in progress: Call Summary, Campaign Kit, and the markdown renderer upgrades
(pipe tables, fenced code, deeper headings, `*` bullets, horizontal rules).

- **Skill count corrected to 12.** The Campaign Kit commit added a skill without
  bumping the figure, which had been left at 11. The count now lives on
  `getting-started.html`, not `index.html`, because `index.html` is the new home
  page.
- Both `marketing.html` and `go-to-market.html` merged cleanly: their new skill
  entries and this branch's nav, head and footer changes are all present.

## 2026-09-14 (11)

- **Hero close rewritten** to "so the value of your brand is carried through
  every time", in the client's own words, replacing the brand guide's "the work
  you do once is used every time".
- **Ideal customer is now a GTM team of 1 to 100**, down from 2 to 200, in the
  hero chip, `llms.txt` and the repo guidance.
- **Button rule set and documented.** On light grounds the primary action is the
  graphite fill and the secondary is the outlined ghost; on dark grounds the
  primary is amber. "Learn more about GTM Anatomy" moves from ghost to graphite,
  and the single call to action on every Coming Soon card follows the same rule,
  so amber is spent in one place at a time rather than doubling as a button
  colour on paper.
- **Home contact section simplified.** The "Not ready to talk?" aside is folded
  into the paragraph, and the section now carries two buttons, "Let's strategize"
  and "Explore the skills", instead of a two-column split.
- **Fixed a cascade collision in the footer.** The original `footer` element rule
  carries `text-align:center`, and it was still beating the newer `.site-footer`
  class, so every footer on the site rendered centred instead of in left-aligned
  columns. `.site-footer` now sets alignment, family and size explicitly.
- Added spacing between a `.section-lead` and the `.prose` block after it, which
  previously ran together as one wall of text.

## 2026-09-14 (10)

Home contact section, the last of the client's page pass.

- **Retitled** "Better together. Let's synergize." with new lead copy inviting a
  15 to 30 minute call.
- **Section simplified** to one call to action plus a skills-library aside. The
  "what happens next" list is gone; it duplicated the contact page, which is a
  splash right now anyway.
- Two edits on the supplied copy: "AI-use cases" loses its hyphen, and "15-30
  minutes" becomes "15 to 30 minutes", matching how every other range on the site
  is written.
- **Restored the exclamation mark** in the skills band standing line, which was
  dropped in an earlier pass. The client wrote it in both places and the voice is
  warm by design.

## 2026-09-14 (9)

Role tiles get their real copy.

- **"As a ..." dropped from every tile title.** They now read Founder or CEO,
  CRO, Marketing, GTM Operations, Investors, in the client's own labels.
- **New copy on all five tiles**, each written to the role's own pressure rather
  than restating the offer: deal velocity for the CRO, output and enablement for
  Marketing, data quality and sales administration for GTM Operations, spend and
  sprawl across portfolio companies for Investors.
- **Grid retuned from five columns to three.** The supplied copy runs to two
  sentences, which at five columns set roughly 24 characters a line and turned
  each tile into a narrow ladder. Three across gives the sentences room; the
  remaining two sit in a second row at the same column width.

## 2026-09-14 (8)

Seven pages go to Coming Soon, and the role tiles are rebuilt.

- **About, the Offerings hub, all four offering pages and Contact are now Coming
  Soon splash pages.** Each carries the page name, a status badge, a one-line
  summary of what is coming, and a single call to action. The offering splashes
  keep their price and timeline chips, since those figures are already public on
  Home. Their full versions are in git at `0b5f3a6` and CLAUDE.md records how to
  restore one.
- **Contact's splash carries a `mailto:` rather than a link to itself.** With the
  contact page down, that email is the site's only working conversion path, which
  is why it exists at all: every other splash points at `/contact.html`.
- **Fixed stale footer links** in the shared page template, which still pointed at
  `build-sprint.html` and `fractional-ai-gtm-partner.html` from before the rename.
  These only surfaced now because the splash pages are generated from that
  template. Every internal link on every page resolves.
- **Role tiles rebuilt as compact tiles**: a title and one line each, no bullets.
  Five sit in a single row above 960px, forced to five columns because auto-fit
  stranded the fifth on its own line.
- **Section retitled** "Different roles have different needs." Two edits on the
  supplied lead: "doesn't" spelled out for consistency with the rest of the site,
  and "our needs" changed to "the needs ... across your organization", since "we"
  is the practice and "you" is the client.

## 2026-09-14 (7)

Fourth pass: the skills library band.

- **Retitled** "Try before you buy." and the lead rewritten, opening with "Or"
  so it reads as the fourth door off the offerings section above it.
- **New standing line** replaces the brand guide's "Try it yourself" invitation:
  "The more we build together, the better we become. If you test a skill, drop me
  a DM and let me know what you think."
- **"Drop me a DM" is not yet a link.** No social URL exists in the repo, and a
  DM link that opened the contact form would not do what it says. Marked with a
  placeholder comment in `index.html` until a URL is supplied.
- One edit on the supplied copy: "Sharing is caring and GTM Anatomy publishes"
  joined two independent clauses without punctuation, so it now takes a colon.

## 2026-09-14 (6)

Third pass: the Offerings section.

- **Section retitled** "Work with GTM Anatomy." and the lead rewritten. The four
  verbs are now diagnose, build, operate, and continue to execute. The lead also
  says you can skip the Scan and go straight to an Anatomy OS build, and offers a
  fourth door for teams who just want another set of hands.
- **"Connect with Rachel" links to the contact page**, with a new link treatment
  for `.section-lead` and `.prose` so an inline link reads as one on both grounds.
- **Anatomy OS**: handover now reads "Yours at handover, following enablement."
- **Fractional Partner**: "marketing, go-to-market, and/or GTM engineering", plus
  the extra-set-of-hands sentence.
- **The deeper pages were brought in line** rather than left contradicting Home:
  the Offerings hub lead and heading carry the new four-verb sequence, the hub's
  sequencing paragraph mentions the jump straight to a build, the Anatomy OS page
  ties transfer to enablement in both the deliverable list and the proof points,
  and the Fractional Partner page and hub card carry the new seat wording.

## 2026-09-14 (5)

Second pass: the "What is GTM Anatomy" section.

- **Headings now carry terminal punctuation** across all eight practice pages.
  A full stop is appended as `<span>.</span>` so it picks up the amber, matching
  the wordmark. Headings that already ended in punctuation were left alone.
- **Section retitled** "AI infrastructure, unique to your business."
- **Section copy rewritten** from the client's draft. Three edits on top of what
  was supplied: "today" capitalised at the start of its sentence, a comma splice
  resolved to a colon ("takes a second shape: foundational materials the team
  does not agree on"), and "Oftentimes" dropped as filler with its sentence
  folded into the one before it. Split into three paragraphs, the first set as
  the lede. Go-to-market (GTM) is now defined on first use on this page.
- **Line-drawing icons** on the three specs in the right-hand column, as a new
  `.spec-list.iconic` variant. Base `.spec-item` is untouched, so the plain spec
  lists on About and the four offering pages keep their existing look. Each
  glyph encodes its point: a shared left edge with three rules of differing
  length for alignment, one core feeding three nodes for encoding once, and a
  loop enclosing a rising line for a system that keeps learning.

## 2026-09-14 (4)

Hero and chrome, from the client's first pass over the home page.

- **Wordmark enlarged**: 19px to 27px in the nav, 26px to 36px in the footer.
- **Nav label "Claude Skills" is now "AI Skills"**, in the top bar, the library
  subnav, and the footer column heading. Body copy still says Claude where it
  means Claude, because the skills genuinely run there.
- **Home hero statement is now set in Anton**, mixed case, up from Space Grotesk
  400. It sits directly under the wordmark and now reads as an extension of it.
  This is a deliberate third exception to the Anton rule, recorded in CLAUDE.md.
- **New hero copy**: "Still doing random acts of AI? Turn your context and
  foundational resources into an AI Operating System you own, so the work you do
  once is used every time."
- **Removed** the "Designed and built, not bolted on" support line.
- **Primary call to action is now "Let's strategize"**, replacing "Book a
  strategy call" across all eleven pages. The old phrasing stays in the contact
  page meta description, where it plainly describes the action for search.

## 2026-09-14 (3)

The wordmark lands.

- **`GTMAnatomy.` is now the wordmark** in the nav and the footer of all eleven
  pages: no space, "GTM" and the trailing full stop in amber, "Anatomy" in paper.
  Built as live Anton text rather than an image, so it stays crisp at any size and
  reverses cleanly on the graphite ground, which the supplied black logo file
  cannot do. In prose the company stays "GTM Anatomy", two words.
- **`assets/og-image.png` regenerated** from the same lockup, replacing the old
  "Anatomy, free Claude skills" card that had been wrong since the restructure.
  Rendered at 1200x630 on the graphite ground with the circuit grid, the
  descriptor line, and the tagline.

## 2026-09-14 (2)

Naming, scope and phrasing corrections from the client.

- **Offering 03 is now AI Sprint**, at `offerings/ai-sprint.html`.
- **Offering 04 is now Fractional Partner**, at `offerings/fractional-partner.html`,
  and its scope is explicit: marketing, go-to-market, and GTM engineering, as one
  seat or several. The page now names each of the three and what the seat covers,
  with GTM engineering called out as the one most teams cannot hire for.
- **Timelines read "Typically delivered within …"** rather than a flat duration,
  so delivery speed can evolve without the copy promising a fixed window.
- **The ideal customer is a go-to-market team of 2 to 200, not a company of that
  size.** The company can be far larger. The Home hero chip, the About page, and
  `llms.txt` all say so now, where they previously implied a 20 to 200 person
  company.
- **Removed the "compare all four offerings" button** from Home. The cards link
  through individually and the hub sits in the nav, so the button was a third path
  to the same place.

## 2026-09-14

Pricing, offering sequence, and contact routing, from the client's own figures.

- **Pricing is published.** Anatomy Scan $5,000 for two weeks. Anatomy OS
  $25,000 for three to six weeks, where it lands in that range depending on how
  fast intake comes back and how quickly the sprint sessions run. AI Sprint
  scoped per project, starting at $5,000. Fractional Partner $8,500 per
  month, with hourly rates for project-shaped work. The Scan fee credits into an
  Anatomy OS build. Figures appear on the offering cards, in each page's pill
  row, in a new `.price-table` on the Offerings hub, and in `llms.txt`.
- **`gtm-operating-system.html` is now `anatomy-os.html`.** Anatomy OS is the
  product name; what it is gets described as an AI-native go-to-market operating
  system. Every link, the canonical, the JSON-LD, the sitemap and the markdown
  twin moved with it. Nothing external pointed at the old URL yet, so no redirect
  was needed.
- **Offerings resequenced** to Scan, Anatomy OS, AI Sprint, Fractional. The
  AI Sprint is now scoped project work that follows the build rather than a
  smaller build preceding it, and its copy says so. Kickers, cards, cross-links
  and the footer column all renumbered.
- **The contact form moved off Home.** Home now links to `contact.html` for both
  booking and messaging, so there is one place to change how contact works.
- **Contact page gained two embed slots**, driven by a new `initEmbed()` in
  `assets/site.js`. `#schedulerEmbed` takes any inline booking URL;
  `#formEmbed` takes a hosted form URL and hides the native form when set.
  Both are provider-agnostic one-attribute swaps, because the provider is not
  chosen yet. With neither set the page still works: the scheduler shows a
  visible "not connected" notice and the native form posts by mailto.
- **All `.tbd` timeline chips are gone**, since every timeline is now published.
  The remaining `.placeholder-block` panels are proof points and ROI figures,
  which still need real client outcomes.

## 2026-09-10

Site restructure. The skills library becomes a section of a full GTM Anatomy
marketing site rather than the whole site. Copy across the new pages is drafted
from the Brand + Message Guide v0.4, so voice, vocabulary and mechanics follow
that document.

- **New `index.html`** — Home. Hero on the tagline ("Your brand. Your context.
  Your AI."), what GTM Anatomy is, the four offerings as a sequence, the skills
  library as the self-serve door, five "what it means to you" role tiles, and a
  contact section. Carries Organization JSON-LD and a whitelisted hash redirect
  so the five old root anchors still land on their content.
- **`getting-started.html`** — the previous `index.html`, moved. Content is
  unchanged apart from the nav, the headline, and two copy fixes: Step 1 now
  points at "Sales" rather than a "Go-To-Market tab", and the Best Practices
  standfirst drops first-person voice. Still the only page holding skill counts.
- **New `about.html`** — purpose, the revenue-engine foundations as a numbered
  climb, how we work, who it is for and who it is not, founder, vision and
  mission.
- **New `offerings/`** — a hub plus one page per offering, each covering what it
  is, why it exists, what you get, why you need it, proof points, and a sample.
  Testimonial markup ships commented out on all four, so nothing invented is
  visible. Offering names follow the brand guide: Anatomy Scan, AI Sprint,
  Anatomy OS, Fractional Partner.
- **New `contact.html`** — form plus a "what happens next" aside. The form posts
  to whatever is in `data-endpoint`; left empty, it composes a mailto instead, so
  it works on a static host today.
- **Nav** — one bar across all eleven pages: Home, About, Offerings, Claude
  Skills, Contact. The Claude Skills group is a CSS-only dropdown on pointer
  devices, with a second-row `.subnav` on the three library pages that always
  renders, so the grouping works on touch and without JavaScript.
- **Sales relabel** — the Go-To-Market track is now labelled Sales in the nav,
  the subnav, the title and the H1. `go-to-market.html` keeps its filename,
  because GitHub Pages has no redirects and inbound links should not break.
- **Machine-readable layer** — `llms.txt` as the index, a `.md` twin beside every
  page, `llms-full.txt`, `sitemap.xml` and `robots.txt`. Service JSON-LD on each
  offering page. Any copy change must be mirrored into the page's `.md` twin and
  into `llms-full.txt` in the same commit.
- **`assets/styles.css`** — one appended block for the new components. The only
  changes above it are three nav overrides.
- **Pending client input** is marked in place, never invented: dashed `.tbd`
  chips for the three unpublished timelines, `.placeholder-block` panels for
  pricing and for every proof point or ROI figure, and HTML comments for the
  scheduler URL and the founder biography.

## 2026-09-12

**Campaign Kit** — new skill on the Marketing page, and a markdown renderer
that can show it.

- **`skills/campaign-kit/skill.md`** — new. Give Claude one long-form asset
  plus either a message guide or a statement of what the asset is meant to
  achieve, and it builds the whole campaign around it: the promotion and the
  follow-up. Landing page, confirmation page, five email tracks, newsletter
  module, three LinkedIn post types, SDR cold outreach and post-download
  follow-ups, a blog post, three ads, and an expansion track for companies with
  an installed base. Two things distinguish it from asking for promo copy: it
  reads the asset in full and builds a claims inventory first, so every stat in
  the kit traces to a page and nothing is invented; and it scores the asset
  against the stated goals *before* writing anything, with a hard approval gate
  and the standing option to say the asset doesn't serve the goal and shouldn't
  be promoted as-is.
- **`marketing.html`** — new `Campaign` category, and the skill added to
  `SKILLS`. Eight skills, seven categories.
- **`assets/site.js`** — `mdToHtml()` extended. It previously handled `#`, `##`,
  blockquotes and lists, and dropped everything else into `<p>`. It now renders
  pipe tables, `###`–`#####` headings, fenced code blocks and horizontal rules,
  and pulls fenced content out before parsing so code is never re-interpreted as
  markdown. This was already a live bug rather than a new requirement: Call
  Summary's two tables were rendering as rows of raw pipe characters, and the
  `###` headings in ABM Activation Plan, AEO Brand Auditor, Company Discovery
  and Company Identity Builder were rendering as body paragraphs. All fixed by
  the same change.
- **`assets/styles.css`** — modal styles for the newly-rendered elements:
  tables (in a horizontally scrolling wrapper, so a wide table can't push the
  modal sideways), `h3`–`h5`, `pre`, and `hr`.

## 2026-09-11 (2)

**Call Summary** — category changed and copy revised, same day it shipped.

- **`go-to-market.html`** — category `Call Intelligence` → **`Sales`** in both
  `CATEGORIES` and the skill's `SKILLS` entry, on Rachel's call. Card summary
  and `Perfect for` bullets rewritten in her words: Sales calls, Interviews,
  Meetings, and any call that needs further alignment with other resources.
- **`skills/call-summary/skill.md`** — the new card copy promised a Word doc
  and artifact "that can be pushed directly into CRM," which the skill did not
  do. Rather than soften the claim, the skill now produces it: a **CRM log**
  section, a fenced plain-text block sized to paste into a CRM activity record
  — date, attendees, summary, decisions, next steps as `Owner — action — due`,
  and the page link. It exists because the record itself does not paste: an
  activity field strips markdown, mangles tables, and truncates long text, so a
  document written for a human reader lands there as noise. Where a CRM
  connector is available the skill offers to write the activity directly, and
  it asks first every time — logging to someone's system of record is not a
  step to take unprompted.

## 2026-09-11

New skill on the Go-To-Market track: **Call Summary**, under a new
**Call Intelligence** category.

- **`skills/call-summary/skill.md`** — merges an AI notetaker's summary, the raw
  transcript, and the user's own notes into one call record: participants with
  organization and title, TL;DR, decisions made, open items with named owners, a
  thematic notes summary, and a chronological outline of every topic in the order
  it came up. Two passes are what distinguish it from a summarization prompt. It
  cross-checks the questions the user planned to ask against what the transcript
  shows was actually answered, sorting each into answered, partially answered, or
  never asked. And it flags where the three sources disagree instead of quietly
  picking the confident-sounding one — on the first real run, that caught a
  company name that *both* notetaker outputs had wrong, in two different ways.
- **`go-to-market.html`** — `SKILLS` entry, and `Call Intelligence` added to
  `CATEGORIES`. The track's hero stats read off array length, so they follow.
- **`index.html`** — Skills Available 10 → 11.

Generated with `scripts/promote-skill.py` in the source repo, which was written
for this promotion: it reduces the front-matter to the four keys Claude
validates on upload and strips the `<!-- internal -->` blocks that carry
filesystem paths and private working context. Previously the rule to use that
script existed in `CLAUDE.md` but the script itself did not.

## 2026-09-04 (3)

Heading-level fix in **Basic Discovery**, carried over from the source repo.

- **`skills/company-discovery-basic/skill.md`** — `Optional Additions` was an
  `##` heading followed by four more `##` headings, so AI Strategy, Recent News,
  Sales Talking Points and Executive Summary all read as top-level report
  sections rather than as the optional ones. Executive Summary was the real
  problem: a required section filed under "optional" while its own text says to
  end every report with it. The three genuinely optional sections are now `###`
  under Optional Additions, Executive Summary stays `##` and closes the report
  spec, and the Optional Additions line says which sections it governs. Predates
  the artifact work — the original skill shipped this way.

## 2026-09-04 (2)

Follow-up pass on **Basic Discovery** so the download behaves correctly for
someone who uploads it into Claude > Skills, where there is no filesystem and
no repo.

- **`skills/company-discovery-basic/skill.md`** — the run contract is now
  *two* things (chat brief + published artifact), with saving to disk as a
  conditional third rather than a hard requirement; *Save the run* opens by
  saying to skip it where the session has no filesystem, and no longer assumes
  the research folder is version-controlled. Removed environment-specific tool
  names and the named sibling-skill references, so the styling and delivery
  steps degrade to "if the session has one." Promoted **Handle with care** to
  its own section near the top — it was previously described inside the
  filesystem section, which meant a session that skipped that section also
  lost the instruction to lead the brief with the caveats.

## 2026-09-04

Updated the Go-To-Market track skill **Basic Discovery**: every run now ships
a visual artifact, not just chat output.

- **`skills/company-discovery-basic/skill.md`** — added three sections. *Every
  run ships three things* states the contract up front: the chat brief, a
  markdown copy on disk, and a self-contained HTML brief published as a
  private artifact. *Build the artifact* covers extracting real brand tokens
  from the company's live site (CSS custom properties, computed header/nav/CTA
  styles, hex frequency, `theme-color`, SVG fills), splitting the accent into
  fill and text tokens so accent text clears 4.5:1, and the build rules —
  self-contained, light/dark token blocks, responsive at 900px and 390px, the
  scan strip, the not-affiliated footer. *Save the run* covers the per-company
  folder convention and why the artifact is the thing that gets lost if it
  isn't also written to disk. `updated` → 2026-09-04.
- **`go-to-market.html`** — refreshed the card summary to mention the artifact,
  added a fourth `perfectFor` bullet, and bumped `updated` to match the skill
  file.

Skill and track counts are unchanged, so the stats stay as they are.

## 2026-08-05 (2)

Fixed every skill download on the site. They could not be imported into
Claude, and three of them were the wrong content entirely.

- **All 10 `skills/*/skill.md`** — rewrote the front-matter to the four keys
  Claude and the site actually need: `name`, `description`, `created`,
  `updated`. The files previously carried `title`/`status`/`summary`/
  `category`/`audience` and **no `name` and no `description`**, so every
  download failed on upload with *"missing field 'name' in SKILL.md
  frontmatter and no directory name available for fallback"* — a bare `.md`
  has no directory name to fall back on. `abm-activation-plan` was the only
  one that had been hand-patched and worked. The bug was invisible on the
  site because the Read modal strips front-matter before rendering.
  `created`/`updated` stay because `openSkill()` greps them for the Read
  modal's date line; the card's title, summary and category come from the
  `SKILLS` arrays, not front-matter.
- **`skills/abm-activation-plan`, `skills/aeo-brand-auditor`,
  `skills/company-identity-builder`** — replaced the truncated write-up with
  the skill's real operating procedure. These three shipped as
  descriptions of a skill rather than the skill itself (71, 75 and 95 lines
  against 381, 228 and 227 in source), so importing one gave Claude a
  brochure. Internal repo notes were stripped and references to bundled
  files now degrade gracefully, since a download arrives as a bare `.md`.
- **`marketing.html`, `go-to-market.html`** — corrected the `updated` dates
  for `aeo-brand-auditor` (→ 2026-07-24) and `company-discovery-basic`
  (→ 2026-07-24), which had drifted from the skill files.
- **`CLAUDE.md`** — the "Adding a new skill" recipe still prescribed the old
  front-matter schema and was the root cause. Rewritten to specify the
  four-key contract, the exact failure it prevents, and to generate the file
  with `brain`'s `scripts/promote-skill.py` rather than hand-write it.

## 2026-08-05

Published a new skill to the Marketing track: **Marketing Audit**.

- **`skills/marketing-audit/skill.md`** — public-facing skill copy
  (`status: published`, category **Marketing Audit**, audience **Marketing
  Leaders**). Give Claude a company name or URL; it runs four live research
  passes (owned, earned, paid, social), grades each A–F with sourced
  good/bad/low-hanging-fruit findings, and hands back a prioritized "if you
  only fix five things" list plus `report.md`/`report.html`/`report.pdf`.
  Promoted from `brain` after an internal test run (EasyMetrics), which
  confirmed the grading judgment and report structure.
- **`marketing.html`** — added the new **Marketing Audit** category to
  `CATEGORIES` and the skill entry to `SKILLS` (listed first).
- **`index.html`** — bumped the "Skills Available" stat 9 → 10.

## 2026-08-03 (2)

Published a new skill to the Marketing track: **YouTube Video Kit**.

- **`skills/youtube-video-kit/skill.md`** — public-facing skill copy
  (`status: published`, category **Content**, audience **Marketing &
  Content Teams**). Give Claude a company URL, an unlisted video link, and
  its transcript; it builds a complete YouTube publishing kit — titles,
  description, tags, an A/B thumbnail set, pinned comment, playlist/
  category, and a Shorts/LinkedIn/blog repurposing kit — as a single
  self-contained HTML one-pager, styled in that company's own real brand
  colors and fonts rather than a fixed template. Promoted from `brain`
  after an internal test run (a CloudCover explainer video), which also
  caught and fixed a thumbnail-generator bug (headline text overflow) and
  tightened the strikethrough-emphasis guidance before promotion.
- **`marketing.html`** — added the new **Content** category to `CATEGORIES`
  and the skill entry to `SKILLS` (listed last).
- **`index.html`** — bumped the "Skills Available" stat 8 → 9.

## 2026-08-03

Published a new skill to the Marketing track: **ABM Activation Plan**.

- **`skills/abm-activation-plan/skill.md`** — public-facing skill copy
  (`status: published`, category **ABM**, audience **Marketing & Sales
  Leaders**). Give Claude a company's GTM identity and a campaign objective
  (plus, ideally, a target account list); it builds a full ABM activation
  program — account routing, challenge patterns by segment, persona entry
  points, outreach hooks, a priority account table, and play-based email
  templates — as branded HTML, PDF, and Markdown. Promoted from `brain`
  after an internal test run (SecurityScorecard/TITAN net-new prospecting).
- **`marketing.html`** — added the skill entry to `SKILLS` (listed
  alphabetically after ABM Account Snapshot; no new category needed, ABM
  already existed).
- **`index.html`** — bumped the "Skills Available" stat 6 → 7.

## 2026-07-29

Published a new skill to the Marketing track: **Build Brand Guidelines**.

- **`skills/build-brand-guidelines/skill.md`** — public-facing skill copy
  (`status: published`, category **Brand**, audience **Marketing Leaders**).
  Give Claude a company URL; it reads the site's real colors, typography,
  logo, and voice and builds an installable brand skill, a written style
  guide, a one-page branded PDF, and an editable PowerPoint deck.
- **`marketing.html`** — added the new **Brand** category to `CATEGORIES` and
  the skill entry to `SKILLS` (listed first).
- **`index.html`** — bumped the "Skills Available" stat 5 → 6.

## 2026-07-23 (2)

Site-wide layout + behavior pass across all three pages (`index.html`,
`marketing.html`, `go-to-market.html`) and shared assets:

- **Global nav.** Replaced the per-page setup (an absolutely-positioned
  `.top-contact` link in the hero + a separate `.page-nav` bar below it) with
  a single `.global-nav` top bar on every page: the three page links
  (Getting Started / Marketing / Go-To-Market) on the left, Contact on the
  right, aligned in one 1040px-wide row above the hero. `setActiveNav` now
  targets `.global-nav a`. Old `.page-nav` CSS left in place (unused, no
  longer referenced).
- **Hero CTA.** Removed the per-card "Open Claude.ai" button from the skill
  card actions (`assets/site.js` `renderSkillsGrid`) and placed one
  `Open Claude.ai ↗` button (`.btn-primary`, inside a new `.hero-cta`) in the
  hero of the two skill pages — below the hero paragraph, above the amber
  bottom border. Not added to `index.html` (no skill cards there).
- **Filter alignment.** Wrapped the Skills filter bar's label + tags in a
  `.filter-inner` (`max-width:1040px; margin:0 auto`) so they left-align with
  the hero copy and the skills grid instead of sitting flush to the viewport
  padding.
- **Sorting.** Skills now render sorted alphabetically by category, then by
  title (`renderSkillsGrid`); category filter chips are sorted alphabetically
  too (`renderTags`).
- **Date order.** Skill card meta and the Read-modal meta now read
  `Updated <date> · Added <date>` (was `Added … · Updated …`) — in both
  `renderSkillsGrid` and `openSkill`.
- **Prompts removed.** Deleted the **Prompts** `.guide-section` (and its
  inline `PROMPTS`/`renderPrompts` JS + `promptStats`) from `marketing.html`
  and `go-to-market.html`. The shared `renderPromptsGrid` / `openPrompt` /
  `copyPrompt` helpers, the prompt-related CSS, and the `prompts/`
  placeholder folder are left in place in case the section is re-enabled
  later; nothing renders them now.
- **Marketing hero copy** updated to: "Skills built for marketing teams —
  persona-based content audits, campaign builders, and more. Read how it
  works, download the file, create as a skill in Claude."

## 2026-07-23 (1)

- Added a new GTM skill: **Basic Discovery**
  (`skills/company-discovery-basic/skill.md`, `status: published`, category
  **Account Intelligence**, audience **GTM Leaders**) — generates an
  executive-level account brief for a target company (overview, ownership,
  funding, products, competitors, revenue-growth opportunities, buying
  reasons, plus optional AI strategy / recent news / talking points /
  executive summary). Promoted from `brain`.
- `go-to-market.html`: added the `company-discovery-basic` entry to the
  `SKILLS` array and added **Account Intelligence** to the `CATEGORIES` array
  (now `["Competitive Intelligence", "Account Intelligence"]`). GTM skill
  count is now 2; hero stats compute from array length, so no manual number
  change on this page.
- `index.html`: bumped the "Skills Available" hero stat from 4 to 5 (total
  across both tracks).

## 2026-07-22 (2)

- Getting Started (`index.html`) copy pass:
  - Hero sub now reads "A library of Claude **prompts and skills** built from
    real GTM workflows. Read how it works, download the **files**, **execute
    in Claude**. Check back often, **updates** are made daily." (was skills-only,
    "drag it into Claude", "skills are added and updated daily").
  - Step 1 (Browse): "Marketing" and "Go-To-Market" are now links to
    `marketing.html` and `go-to-market.html`.
  - Claude Setup Guide: removed the "— New Section" kicker and replaced the
    intro paragraph with "Build a system Claude can rely on with repeatable
    skills, prompts, and more."

## 2026-07-22 (1)

- Added a new **Prompts** section to `marketing.html` and `go-to-market.html`, below the existing Skills grid — its own heading, stats row, filter tags, and grid, wrapped in `.guide-section` (the same amber-top-border/tinted-background "new zone" treatment used for the Claude Setup Guide on `index.html`) so it reads as a distinct content zone rather than more of the Skills grid.
- `assets/site.js`: added `renderPromptsGrid`, `openPrompt`, and `copyPrompt` — mirrors the existing Skills rendering functions but reads from `prompts/<slug>/prompt.md` and swaps the Download button for a Copy button (extracts the first fenced code block in the prompt file and copies it to the clipboard).
- `assets/styles.css`: added `.filter-wrap.static` (non-sticky variant, since the page already has one sticky filter bar for Skills) and `.hero-stats.on-light` (amber-deep instead of amber for stat numbers/border, since this stats row sits on the tinted `--paper-dim` background instead of graphite).
- Shipped with one placeholder card per page (`prompts/placeholder-marketing-prompt/`, `prompts/placeholder-gtm-prompt/`) — `status: draft`, clearly marked `[Placeholder]` in the title. **Replace both before this section should be considered live** — see `CLAUDE.md` → "Adding a new prompt" for the pattern.
- `CLAUDE.md`: documented the Prompts section and the new "Adding a new prompt" recipe alongside the existing "Adding a new skill" one.

## 2026-07-21 (6)

- Rewrote the hero-sub copy on the Getting Started page: dropped the "competitor intelligence, ABM, AEO, and more" list from the intro sentence and added "Check back often, skills are added and updated daily." to signal the library is actively growing.

## 2026-07-21 (5)

- Renamed and expanded **AEO Content Auditor** → **AEO Brand Auditor**
  (`skills/aeo/skill.md` → `skills/aeo-brand-auditor/skill.md`, slug `aeo`
  → `aeo-brand-auditor`). It's a company-wide AEO scan first now, not just a
  single-page content checker — added a company-wide scan mode (AI-answer
  query panel, site audit, competitive teardown) alongside the original
  page-level check, promoted from `brain` after an internal test run.
- Updated the `SKILLS` array entry on `marketing.html` (slug, title,
  summary, perfectFor bullets, and `created`/`updated` dates — `created`
  kept at the original 2026-07-15, `updated` bumped to 2026-07-21) to
  match. No count/category change.

## 2026-07-21 (4)

- Every skill `skill.md` now carries `created` and `updated` dates in front-matter (convention added to `CLAUDE.md` — bump `updated` on any content change). Backfilled all four skills from git history.
- Renamed the **Company Identity Builder** category from "Brand & Messaging" to just **Messaging** (front-matter + `marketing.html`).
- Added a "Generate your LLMS.txt summary" bullet to the Company Identity Builder perfect-for list (skill.md + card).

## 2026-07-21 (3)

- Recategorized **Company Identity Builder** as a brand/messaging skill (it's for understanding a company's external-facing message, not account/market intel). Moved it from the Go-To-Market track to the Marketing track: `audience` → Marketing Leaders, `category` → **Brand & Messaging**, and reframed its copy/perfect-for bullets accordingly.
- `marketing.html` gains the skill and the new **Brand & Messaging** category (Marketing track now 3 skills); `go-to-market.html` reverts to just Competitor Intelligence and its single category. Total site skills unchanged (4), so `index.html` stats stay put.

## 2026-07-21 (2)

- Published new skill: **Company Identity Builder** (`skills/company-identity-builder/skill.md`). Give Claude a company URL and it builds a full identity across six approval-gated questions (brand colors, competitors, categories, sales plays, proof points, beachhead), then outputs a README, a branded HTML deck, and an llms.txt.
- Bumped `index.html` "Skills Available" stat from 3 to 4.

## 2026-07-21 (1)

- Shortened the top-right contact button label from "Contact for Consulting" to "Contact" on all 3 pages (mailto link/subject unchanged).

## 2026-07-20 (8)

- Removed the black `border-bottom` on the "Get Started in 3 Steps" section (`#how`) — it was stacking with the guide-section's amber top border, showing as two lines. Only the amber boundary line remains.
- Updated the AI 101 sub-heading from "The five terms you need before any of this makes sense" to "The terms you need to know before any of this makes sense" (count is no longer five now that LLM and Model were added).

## 2026-07-20 (7)

- Wrapped the Claude Setup Guide content (intro through Best Practices) in a `.guide-section` with a tinted `--paper-dim` background and a 3px amber top border — the same "zone boundary" treatment used at the bottom of the hero/page-header elsewhere on the site — so it reads clearly as a distinct section instead of just a thin divider line.
- Added a small amber "— New Section" eyebrow label above "Claude Setup Guide".

## 2026-07-20 (6)

- Increased `.hstat` left/right padding (0/22px → 24px each side) so the stat numbers have breathing room from the vertical divider lines between cells.
- Rewrote the Claude Setup Guide intro paragraph on the Getting Started page.
- Removed the in-page anchor nav (Getting Started / AI 101 / Best Practices buttons) below the intro — the section titles below still anchor the same IDs, just without the jump-nav.
- Renamed the guide's first section from "Getting Started" to "Know Before You Begin" (avoids clashing with the page-level "Getting Started" nav tab).
- Added "LLM" and "Model" to the AI 101 glossary, with ChatGPT/Claude/Grok as LLM examples; noted a models-comparison graphic is coming later.
- Updated the Best Practices sub-heading with an attribution note (sourced from resources/thought leaders, not original advice).
- Footer link changed from a fully-linked "About GTMAnatomy.AI" to "More about **GTMAnatomy.AI**" — only the name/domain-styled portion is a hyperlink now.

## 2026-07-20 (5)

- Restyled the top page-nav from underlined tabs to bordered box-buttons (matching `rachelwbruce`'s `.section-nav` pattern: `border:1.5px solid #4A5158`, transparent background, amber-filled active state) and moved it below the hero-stats numbers on all 3 pages — mirroring where `rachelwbruce` places its own section nav, right after the hero content.
- Increased `.hstat` top padding (16px → 28px) so the stat numbers no longer sit flush against the amber divider line above them.

## 2026-07-20 (4)

- Removed the hero CTA button row on `index.html` (Marketing Skills / Go-To-Market Skills / How It Works) — the top page-nav already covers this navigation, so the buttons were redundant.
- Folded the standalone `playbook.html` page into `index.html`: its Claude Setup Guide (intro + Getting Started/AI 101/Best Practices sections, with its own in-page anchor nav) now lives directly below the 3-step onboarding on the Getting Started page.
- Removed `playbook.html` and the "Playbook" tab from the shared `page-nav` on all remaining pages (now 3 tabs: Getting Started / Marketing / Go-To-Market).
- Added a `.section-intro` style for the new intro paragraph ahead of the merged guide content.

## 2026-07-20 (3)

- Added a 4th page, `playbook.html` ("Playbook" nav tab) — a Claude setup guide (Getting Started / AI 101 / Best Practices), rebuilt from a first draft that had mistakenly targeted the `rachelwbruce` repo/brand, restyled to `anatomy`'s graphite/amber system and populated with real copy from the underlying research (sources: Ruben Hassid, Kaylee Edmondson, Ruben Dominguez, Anthropic).
- Added new shared `.pb-*` component styles to `assets/styles.css` for the playbook's steps rail, glossary grid, and tiered best-practices cards.
- Added the "Playbook" tab to the shared `page-nav` on all other pages.

## 2026-07-20 (2)

- Split the single-page site into 3 pages sharing `assets/styles.css` and `assets/site.js`: `index.html` (Getting Started/home — hero + 3-step onboarding, skills grid removed), `marketing.html` (ABM Account Snapshot, AEO Content Auditor), `go-to-market.html` (Competitor Intelligence Brief).
- Added a top `page-nav` tab bar (Getting Started / Marketing / Go-To-Market) shared across all 3 pages with active-state highlighting.
- Reclassified Competitor Intelligence Brief's `audience` front-matter from `Marketing Leaders` to `GTM Leaders` to match its new page.
- Added an "About GTMAnatomy.AI" link to the footer on all 3 pages, pointing to the business overview deck (currently unprotected; password-gating to be added later).

## 2026-07-20 (1)

- Added favicon (graphite/amber "A." mark matching the hero wordmark), referenced at 16/32/192px plus a 180px Apple touch icon.
- Added a branded 1200x630 Open Graph / Twitter share image (`assets/og-image.png`).
- Added `og:*` and `twitter:*` meta tags (title, description, image, dimensions, card type) for link previews.
- Tightened the `<meta name="description">` copy.
