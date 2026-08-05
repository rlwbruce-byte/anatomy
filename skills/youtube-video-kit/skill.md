---
title: YouTube Video Kit
status: published
summary: Give Claude a company URL, an unlisted video link, and its transcript, and it builds a complete, on-brand YouTube publishing kit — titles, description, tags, thumbnails, pinned comment, playlist/category, and cross-channel repurposing — styled in that company's own real brand colors and fonts.
category: VIDEO
audience: Marketing & Content Teams
created: 2026-08-03
updated: 2026-08-03
---

# YouTube Video Kit

## What this skill does

Point Claude at a company's URL and a video (an unlisted link plus its
transcript) and it builds a complete YouTube publishing kit — reading the
company's real brand colors and fonts off their own site rather than
applying a fixed template. You review and paste into YouTube Studio; it
never publishes on its own.

## What you get

- **3 title options**, search-optimized, following a keyword-first,
  product-plus-video-type convention
- **A full description** — hook, summary, chapters with timestamps,
  UTM-tagged links, and hashtags
- **12–20 tags**, mixing exact-match and semantic keywords
- **An A/B thumbnail set** — a designed 1280×720 PNG in the company's real
  brand colors, paired with a video-frame option
- **A pinned comment**, **playlist assignment**, and **category +
  hashtags**
- **A repurposing kit** — Shorts callouts with timestamps, a LinkedIn post,
  and a blog-embed blurb
- **An optional brand & claims check**, run only against real inputs (a
  supplied banned-terms list, or the company's own site voice) — never
  fabricated

Everything lands in a single self-contained, branded HTML one-pager with
one-click copy buttons.

## Trigger phrases

- "Prep this video for YouTube: `<unlisted link>`"
- "Build me a YouTube kit for [company]"
- "Optimize this video for our channel"
- "Turn this webinar recording into YouTube titles/description/tags/thumbnail"

## What you say

> "Prep this video for YouTube: `<unlisted link>`. The company is
> `https://example.com`, this is for [persona], and the CTA should point to
> [page]." Then paste the transcript when asked.

## Perfect for

- Any company or client publishing a webinar, demo, interview, or explainer
  to YouTube
- Turning a raw recording into paste-ready metadata plus repurposed social
  content in one pass
- Agencies and consultants managing YouTube channels across multiple
  client brands, where every kit needs to look native to that client

## Good to know

- Brand colors and fonts are read live from the company's own site — if
  the site doesn't expose clean brand signal, the kit says so and asks you
  to confirm a palette rather than guessing one.
- The brand & claims check only runs against something real (a supplied
  list, or the site's own voice) — it's skipped, visibly, if there's
  nothing to check against.
- Designed thumbnails are generated with Python + Pillow; without the
  brand's exact font installed, it falls back to a clean system sans-serif
  and says so.
