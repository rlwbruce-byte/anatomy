# Getting started with Claude skills — GTM Anatomy

> How to use the free GTM Anatomy Claude skills library: browse, download, and drag the file into Claude. Plus the Claude setup guide for teams.

Source: https://gtmanatomy.ai/getting-started.html

---

_The GTM Anatomy skills library_

# Getting Started.

A library of free Claude skills built from real go-to-market workflows. Read how each one works, download the file, run it in Claude. New skills are added regularly.

**Browse**

Head to the Marketing or Sales page to find the skill built for the workflow you are trying to speed up.

**Download**

Each skill is a single, readable Markdown file — what it does, how to prompt it, what you get back.

**Drag Into Claude**

Drop the file into any Claude conversation, or attach it as a project skill. That's the whole install.

Build a system Claude can rely on with repeatable skills, prompts, and more.

## Claude setup guide

### Know before you begin

Three steps to move off ad-hoc prompting and onto a system Claude can rely on.

1. **Separate knowledge from behavior** Static reference material — brand guidelines, personas, messaging docs — is knowledge. Reusable procedures — voice rules, formatting, workflows — are behavior. They belong in different places: knowledge in a Project's Knowledge Base, behavior packaged as a Skill. _Tags: Knowledge Base, Skills._

2. **Choose your layer** Solo builders start with one Claude Project. Teams split knowledge by function and add Skills on top. Enterprises add governance over both — access control, distribution, review cadence. _Tags: Projects, Cowork, Scale._

3. **Scale access deliberately** Start private, expand sharing on purpose, and reach for a live connector — like GitHub — only when a task genuinely needs live repo access. Don't make a connector your default retrieval path for static knowledge; that's where consistency breaks down. _Tags: Governance, Connectors._

### AI 101

The terms you need to know before any of this makes sense.

- **LLM** Short for Large Language Model — the underlying AI system trained on massive amounts of text to understand and generate language. ChatGPT, Claude, and Grok are all products built on top of an LLM.

- **Model** A specific version of an LLM released under a family name — Claude, GPT, Grok — each with its own size, speed, and capability tradeoffs. A graphic comparing models is coming soon.

- **Prompt** A one-off instruction inside a single conversation. Nothing persists once the chat ends.

- **Project** A persistent workspace with a Knowledge Base and custom instructions that every chat inside it can draw on.

- **Skill** A packaged, reusable procedure — like a brand voice guide — that Claude invokes automatically across chat, Code, and Cowork.

- **Cowork** Claude working directly in a local folder of files — structuring documents and running multi-step tasks.

- **Connector / MCP** A live link to an external tool — GitHub, Drive, Slack — that Claude queries in real time. Powerful, but only as stable as the connection itself.

### Best practices

The right setup depends on how many people need the same answer from Claude.

**Solo Builder (Individual)** One Claude Project holding your personal operating brain — who you are, your voice, your clients, your workflows. Loads automatically at the start of every session.

- One Project, one Knowledge Base

- Custom instructions written once

- Optional local CLAUDE.md mirror for Cowork or Code

Read: Turns out Claude needs a brain: https://demandloops.substack.com/p/turns-out-claude-needs-a-brain (source: Kaylee Edmondson, Looped In)

**Small Team (Team)** Split knowledge into focused Projects by function instead of one mega-project, and turn recurring rules into a Skill so every teammate produces on-brand work without re-explaining the style guide.

- Projects split by function, not one mega-project

- Skills for repeatable voice and format rules

- Shared visibility across the team

Read: Claude Cowork + Project: https://ruben.substack.com/p/claude-cowork-project (source: Ruben Hassid, How to AI)

**Org-Wide Rollout (Enterprise)** Same two layers, plus governance — admin-managed groups and roles, org-wide Skill distribution through a private marketplace, and connectors scoped to specific, live-data tasks only.

- Role-based access by group (SCIM-ready)

- Private Skills marketplace for distribution

- Connectors scoped to live-data tasks

Read: Making Claude Cowork ready for enterprise: https://claude.com/blog/cowork-for-enterprise (source: Anthropic)

