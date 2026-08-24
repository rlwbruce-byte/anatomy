---
name: build-brand-guidelines
description: Builds brand guidelines from a company or client URL. Extracts the brand identity — colors, typography, logo, and voice — from the live site, then generates an installable brand-guidelines skill for the user's own Claude environment, a human-readable brand-guidelines.md, a one-page branded PDF visual (palette, fonts, and usage rules, with selectable hex codes), and an editable .pptx slide deck. Use when someone asks to build or create brand guidelines from a website, turn a site into a brand style guide, or set up a client's brand as a reusable Claude skill.
created: 2026-07-29
updated: 2026-07-29
---

# Build Brand Guidelines

## What this skill does

Paste a company's URL and Claude reads the live site's real brand identity — the exact hex colors and typefaces from the site's own styles, the logo, and the voice from its headlines and copy. It sorts the colors into roles (backgrounds, primary accent, supporting accents) and the fonts into headings, body, and mono, then generates a full brand guidelines set — everything rendered in the company's own colors and fonts.

It works for both dark-ground brands (a dark canvas with light type) and light-ground brands, adjusting contrast automatically.

## What you get

- An installable brand skill — a single file you drop into your Claude environment so Claude applies the brand to anything it makes (decks, docs, HTML, charts).
- A written style guide — the palette with hex values and usage, typography, logo notes, and voice/tone.
- A one-page branded PDF — swatches, type specimens, and the core rules on a single page, with hex codes you can copy straight out of the PDF.
- An editable PowerPoint deck — a four-slide version (title, palette, typography, application and voice) you can drop into a client or team review.

Send corrections back at any point — a fix to one color or font updates every deliverable at once.

## Trigger phrases

- "Build brand guidelines for [url]"
- "Turn [company's site] into a brand style guide"
- "Set up [company] as a brand skill in Claude"
- "Make me a brand one-pager and deck from [url]"

## What you say

> "Build brand guidelines from https://www.example.com — I want an installable brand skill, a one-pager, and a deck I can share with the team."

## Perfect for

- Standing up brand guidelines for a client or a new brand fast
- Giving Claude a reusable, on-brand look for everything it produces
- Turning a website you admire into a documented palette and type system
- Producing a shareable brand one-pager and deck without a designer

## Good to know

- The guidelines are read from the live site's real styles, not guessed.
- If the site doesn't expose a downloadable logo or exact clear-space rules, the guide flags those to confirm with the brand owner.
- For the PowerPoint to render exactly, install the brand's fonts (all are free Google Fonts); otherwise the app substitutes the nearest match.
