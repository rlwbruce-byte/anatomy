#!/usr/bin/env python3
"""Rebuild llms-full.txt by concatenating every markdown twin.

llms-full.txt is the whole site as one document, linked from llms.txt as the
"Full site text" entry. It is the twins joined in nav order, so it goes stale
the moment a twin is regenerated without it. Run this after
scripts/gen-md-twins.py.

Usage:
    python3 scripts/gen-llms-full.py
"""

import datetime
import os

# Nav order: the practice, then the offerings in sequence, then the library,
# then contact. Matches the reading order a person would take through the site.
ORDER = [
    "index.md",
    "about.md",
    "offerings/index.md",
    "offerings/anatomy-scan.md",
    "offerings/anatomy-os.md",
    "offerings/ai-sprint.md",
    "offerings/fractional-partner.md",
    "getting-started.md",
    "marketing.md",
    "go-to-market.md",
    "contact.md",
]

HEADER = ("# GTM Anatomy — full site text\n\n"
          "Every page of GTMAnatomy.ai, concatenated. Generated {date}.\n")

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    missing = [p for p in ORDER if not os.path.exists(p)]
    if missing:
        raise SystemExit("missing twins: " + ", ".join(missing))

    parts = [HEADER.format(date=datetime.date.today().isoformat())]
    for p in ORDER:
        parts.append(open(p, encoding="utf-8").read().strip() + "\n")

    out = "\n---\n\n".join(parts)
    open("llms-full.txt", "w", encoding="utf-8").write(out)
    print(f"llms-full.txt  {len(ORDER)} pages, {len(out.splitlines())} lines")
