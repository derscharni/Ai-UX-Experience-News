# Ai-UX-Experience-News

**A News Vault all around Agent2Agent2Human Experience Design**

Welcome to the Ai-UX-Experience-News repository, curated by **Jens Scharnetzki**, Head of Experience Design & Journey Management at EnBW and a thought leader on Agent Experience (AX) and Temporal UX.

This repository serves as a comprehensive collection of daily briefings tracking user experience (UX) developments across the rapidly evolving landscape of AI agents, including Claude, ChatGPT, Gemini, Copilot, Grok, and Perplexity.

> 📰 **[Read the briefings in the web reader →](https://derscharni.github.io/Ai-UX-Experience-News/)**
> A clean, searchable newsletter-style interface. (Enable via *Settings → Pages → Source: `main` / `docs`*.)
>
> 📡 **[Subscribe via RSS →](https://derscharni.github.io/Ai-UX-Experience-News/feed.xml)**
> Pipe new briefings straight into an RSS-ingestion plugin (Obsidian, Logseq, Readwise Reader, Zapier, …).

The briefings are produced **automatically every weekday** by a research agent (`scripts/research_agent.py`) that searches the web for the latest agent-UX developments and writes each briefing in the house style. See [Automation](#automation) below.

## Research Pattern & Our Lens

These briefings are curated through a specific, focused lens: **Agent2Agent2Human Experience Design**. Rather than tracking general AI news or underlying model architectures (like parameter counts or training data), we consistently track the **UX and interaction design** of the leading AI agents (Claude, ChatGPT, Gemini, Copilot, Grok, Perplexity).

Our methodology involves daily monitoring of product updates, interface changes, and industry discourse to identify macro trends in how humans interact with autonomous systems. Key areas of focus include:

*   **Interface Evolution:** Tracking the shift from static chat windows to generative UI, infinite canvases, and specialized workspaces.
*   **Interaction Patterns:** Documenting how users delegate tasks, how agents ask for clarification, and how control is handed back and forth.
*   **Trust and Safety Design:** Analyzing the UX of transparency, such as "Action Audits," "Confidence Signals," and "Intent Previews," which are critical for user acceptance of autonomous actions.
*   **Agentic Workflows:** Observing how agents move from being reactive oracles to proactive coworkers capable of executing multi-step tasks across local files and web applications.
*   **Temporal UX:** Exploring how the dimension of time changes when managing asynchronous, long-running agent tasks versus synchronous chat.

This consistent lens allows us to map the trajectory of Agent Experience (AX) as it matures from a novelty into the primary operating system of our digital lives.

## Repository Structure

The core of this repository is organized chronologically by month in the `briefings/` directory. Each folder contains daily markdown files detailing the latest product updates, interface changes, and broader industry trends related to Agentic UX.

### February 2026 — *The Operationalization of Agentic AI* (`briefings/2026-02-operationalization-of-agentic-ai/`)
*   [2026-02-25 - The Operationalization of Agentic AI](briefings/2026-02-operationalization-of-agentic-ai/2026-02-25-the-operationalization-of-agentic-ai.md)
*   [2026-02-26 - On-Device Agency and Autonomous Workers](briefings/2026-02-operationalization-of-agentic-ai/2026-02-26-on-device-agency-and-autonomous-workers.md)
*   [2026-02-27 - Intent-Centric UX and Creative Tools](briefings/2026-02-operationalization-of-agentic-ai/2026-02-27-intent-centric-ux-and-creative-tools.md)
*   [2026-02-28 - The Agent Designs in Figma](briefings/2026-02-operationalization-of-agentic-ai/2026-02-28-the-agent-designs-in-figma.md)

### March 2026 — *The Agent Becomes the OS* (`briefings/2026-03-the-agent-becomes-the-os/`)
*   [2026-03-01 - The Agent is the New App](briefings/2026-03-the-agent-becomes-the-os/2026-03-01-the-agent-is-the-new-app.md)
*   [2026-03-02 - The Computer-Using Agent Arrives](briefings/2026-03-the-agent-becomes-the-os/2026-03-02-the-computer-using-agent-arrives.md)
*   [2026-03-03 - The Switcher War Heats Up](briefings/2026-03-the-agent-becomes-the-os/2026-03-03-the-switcher-war-heats-up.md)
*   [2026-03-04 - Copilot Tasks and the Personal Agent](briefings/2026-03-the-agent-becomes-the-os/2026-03-04-copilot-tasks-and-the-personal-agent.md)
*   [2026-03-05 - The Five UX Crises of the Agentic Era](briefings/2026-03-the-agent-becomes-the-os/2026-03-05-the-five-ux-crises-of-the-agentic-era.md)
*   [2026-03-06 - GPT-5.4 and the Agentic Arms Race](briefings/2026-03-the-agent-becomes-the-os/2026-03-06-gpt-54-and-the-agentic-arms-race.md)
*   [2026-03-07 - The Agentic War Is Now a Two-Front War](briefings/2026-03-the-agent-becomes-the-os/2026-03-07-the-agentic-war-is-now-a-two-front-war.md)
*   [2026-03-08 - The Agent Is the New IDE](briefings/2026-03-the-agent-becomes-the-os/2026-03-08-the-agent-is-the-new-ide.md)
*   [2026-03-09 - The Dawn of Intentional Agentic UI Design](briefings/2026-03-the-agent-becomes-the-os/2026-03-09-the-dawn-of-intentional-agentic-ui-design.md)
*   [2026-03-10 - The Agent as Coworker](briefings/2026-03-the-agent-becomes-the-os/2026-03-10-the-agent-as-coworker.md)
*   [2026-03-11 - The Agentic Era Meets the Real World](briefings/2026-03-the-agent-becomes-the-os/2026-03-11-the-agentic-era-meets-the-real-world.md)
*   [2026-03-12 - The Great Integration](briefings/2026-03-the-agent-becomes-the-os/2026-03-12-the-great-integration.md)
*   [2026-03-13 - The Agent Is the New OS](briefings/2026-03-the-agent-becomes-the-os/2026-03-13-the-agent-is-the-new-os.md)
*   [2026-03-14 - The Agent Is the New UI](briefings/2026-03-the-agent-becomes-the-os/2026-03-14-the-agent-is-the-new-ui.md)
*   [2026-03-15 - The Consolidation](briefings/2026-03-the-agent-becomes-the-os/2026-03-15-the-consolidation.md)
*   [2026-03-16 - The Agentic Workflow](briefings/2026-03-the-agent-becomes-the-os/2026-03-16-the-agentic-workflow.md)
*   [2026-03-17 - The Agent Comes Home](briefings/2026-03-the-agent-becomes-the-os/2026-03-17-the-agent-comes-home.md)
*   [2026-03-18 - The Great Rebundling](briefings/2026-03-the-agent-becomes-the-os/2026-03-18-the-great-rebundling.md)
*   [2026-03-19 - Intent is the New Interface](briefings/2026-03-the-agent-becomes-the-os/2026-03-19-intent-is-the-new-interface.md)
*   [2026-03-20 - The Great Unification](briefings/2026-03-the-agent-becomes-the-os/2026-03-20-the-great-unification.md)
*   [2026-03-21 - The Agentic Reckoning](briefings/2026-03-the-agent-becomes-the-os/2026-03-21-the-agentic-reckoning.md)
*   [2026-03-22 - The Agent Comes Home](briefings/2026-03-the-agent-becomes-the-os/2026-03-22-the-agent-comes-home.md)
*   [2026-03-23 - The Remote Control](briefings/2026-03-the-agent-becomes-the-os/2026-03-23-the-remote-control.md)
*   [2026-03-24 - The Agent as the Execution Layer](briefings/2026-03-the-agent-becomes-the-os/2026-03-24-the-agent-as-the-execution-layer.md)
*   [2026-03-25 - The Agentic Correction](briefings/2026-03-the-agent-becomes-the-os/2026-03-25-the-agentic-correction.md)
*   [2026-03-26 - The Agentic Ecosystem](briefings/2026-03-the-agent-becomes-the-os/2026-03-26-the-agentic-ecosystem.md)
*   [2026-03-27 - The Great Migration](briefings/2026-03-the-agent-becomes-the-os/2026-03-27-the-great-migration.md)
*   [2026-03-28 - The Agent is the OS](briefings/2026-03-the-agent-becomes-the-os/2026-03-28-the-agent-is-the-os.md)
*   [2026-03-29 - The Great Unbundling and Rebundling](briefings/2026-03-the-agent-becomes-the-os/2026-03-29-the-great-unbundling-and-rebundling.md)
*   [2026-03-31 - The Agent Becomes the OS](briefings/2026-03-the-agent-becomes-the-os/2026-03-31-the-agent-becomes-the-os.md)

### April 2026 — *Formalizing the Agentic Workspace* (`briefings/2026-04-formalizing-the-agentic-workspace/`)
*   [2026-04-02 - The Agentic Integration and Trust](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-02-the-agentic-integration-and-trust.md)
*   [2026-04-03 - The Push for Precision and Desktop Control](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-03-the-push-for-precision-and-desktop-control.md)
*   [2026-04-04 - The Ecosystem Walls Are Closing In](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-04-the-ecosystem-walls-are-closing-in.md)
*   [2026-04-05 - Designing for Trust and Transparency](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-05-designing-for-trust-and-transparency.md)
*   [2026-04-07 - The App Ecosystem Opens Up](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-07-the-app-ecosystem-opens-up.md)
*   [2026-04-08 - Formalizing the Agentic Interface](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-08-formalizing-the-agentic-interface.md)
*   [2026-04-09 - The Agent as the New Revenue Engine](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-09-the-agent-as-the-new-revenue-engine.md)
*   [2026-04-10 - The Agentic Workspace Unifies](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-10-the-agentic-workspace-unifies.md)
*   [2026-04-11 - The UI Retreats, The Agent Advances](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-11-the-ui-retreats-the-agent-advances.md)
*   [2026-04-14 - The Customization Era Begins](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-14-the-customization-era-begins.md)
*   [2026-04-15 - The Agentic Desktop Arrives](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-15-the-agentic-desktop-arrives.md)
*   [2026-04-16 - The UI Fragments into Specialized Workspaces](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-16-the-ui-fragments-into-specialized-workspaces.md)
*   [2026-04-17 - The Multimodal Shift and Agentic Expansion](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-17-the-multimodal-shift-and-agentic-expansion.md)
*   [2026-04-18 - The Agent Becomes the Designer](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-18-the-agent-becomes-the-designer.md)
*   [2026-04-19 - The Visual Execution Layer](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-19-the-visual-execution-layer.md)
*   [2026-04-20 - Desktop Deepening and AEO](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-20-desktop-deepening-and-aeo.md)
*   [2026-04-21 - The Shift to Operator UX](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-21-the-shift-to-operator-ux.md)
*   [2026-04-22 - The Commerce and Car Expansion](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-22-the-commerce-and-car-expansion.md)
*   [2026-04-23 - Autonomous Research and Custom Curation](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-23-autonomous-research-and-custom-curation.md)
*   [2026-04-24 - Multi-Agent Workflows and Model Upgrades](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-24-multi-agent-workflows-and-model-upgrades.md)
*   [2026-04-25 - The Autonomous OS and Multimodal Leaps](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-25-the-autonomous-os-and-multimodal-leaps.md)
*   [2026-04-26 - The UI Bifurcation and Agentic Refinement](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-26-the-ui-bifurcation-and-agentic-refinement.md)
*   [2026-04-27 - The Rise of AI Runtime Layers and Workspace Controls](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-27-the-rise-of-ai-runtime-layers-and-workspace-controls.md)
*   [2026-04-28 - Transparent Workflows and Dashboard Integration](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-28-transparent-workflows-and-dashboard-integration.md)
*   [2026-04-29 - Friction Reduction and Visual Orchestration](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-29-friction-reduction-and-visual-orchestration.md)
*   [2026-04-30 - Desktop Deepening and Cross-Platform Integration](briefings/2026-04-formalizing-the-agentic-workspace/2026-04-30-desktop-deepening-and-cross-platform-integration.md)

### May 2026 — *The Workflow Becomes the Unit of Work* (`briefings/2026-05-the-workflow-as-the-unit-of-work/`)
_Briefings are added automatically as they are generated._

### June 2026 
*   [2026-06-07 - Agents Go Deeper Into Your Stack](briefings/2026-06-the-art-of-the-interrupt/2026-06-07-agents-go-deeper-into-your-stack.md)
*   [2026-06-08 - Trust Surfaces, Session Security, and the Agentic Memory Layer](briefings/2026-06-the-art-of-the-interrupt/2026-06-08-trust-surfaces-session-security-and-the-agentic-memory-layer.md)
*   [2026-06-09 - The Agent-Native Workspace Takes Shape](briefings/2026-06-the-art-of-the-interrupt/2026-06-09-the-agent-native-workspace-takes-shape.md)
*   [2026-06-10 - Guardrails Go Public, Assistants Go Native](briefings/2026-06-the-art-of-the-interrupt/2026-06-10-guardrails-go-public-assistants-go-native.md)
*   [2026-06-11 - Memory, Oversight, and the Agent Safety Layer](briefings/2026-06-the-art-of-the-interrupt/2026-06-11-memory-oversight-and-the-agent-safety-layer.md)
*   [2026-06-12 - Agents Go Deeper, Orchestration Gets Observable](briefings/2026-06-the-art-of-the-interrupt/2026-06-12-agents-go-deeper-orchestration-gets-observable.md)
*   [2026-06-17 - Permission, Delegation, and the Governance of Ambient Agents](briefings/2026-06-the-art-of-the-interrupt/2026-06-17-permission-delegation-and-the-governance-of-ambient-agents.md)
*   [2026-06-23 - Demonstration Teaches, Identity Governs, Research Forks](briefings/2026-06-the-art-of-the-interrupt/2026-06-23-demonstration-teaches-identity-governs-research-forks.md)
*   [2026-06-24 - Design Canvases, Identity Layers, and the Browser as Agent Surface](briefings/2026-06-the-art-of-the-interrupt/2026-06-24-design-canvases-identity-layers-and-the-browser-as-agent-sur.md)
*   [2026-06-25 - Keyless Agents, Generative UI, and the Mobile Approval Surface](briefings/2026-06-the-art-of-the-interrupt/2026-06-25-keyless-agents-generative-ui-and-the-mobile-approval-surface.md)
*   [2026-06-26 - Autopilots, Security Surfaces, and the Canvas Retirement](briefings/2026-06-the-art-of-the-interrupt/2026-06-26-autopilots-security-surfaces-and-the-canvas-retirement.md)
*   [2026-06-29 - Desktop Agents, Scheduled Tasks, and the Session Observatory](briefings/2026-06-the-art-of-the-interrupt/2026-06-29-desktop-agents-scheduled-tasks-and-the-session-observatory.md)
*   [2026-06-30 - Remote Agents, Biometric Gates, and the Desktop Frontier](briefings/2026-06-the-art-of-the-interrupt/2026-06-30-remote-agents-biometric-gates-and-the-desktop-frontier.md)
— *The Art of the Interrupt* (`briefings/2026-06-the-art-of-the-interrupt/`)
_Briefings are added automatically as they are generated._

### July 2026 — *The Visible Safety Layer* (`briefings/2026-07-the-visible-safety-layer/`)
*   [2026-07-01 - Safeguards, Classifiers, and the No-Code Voice Frontier](briefings/2026-07-the-visible-safety-layer/2026-07-01-safeguards-classifiers-and-the-no-code-voice-frontier.md)
*   [2026-07-02 - Agentic Defaults, Dynamic Workflows, and the Fleet Control Layer](briefings/2026-07-the-visible-safety-layer/2026-07-02-agentic-defaults-dynamic-workflows-and-the-fleet-control-lay.md)
*   [2026-07-03 - The Admin Intelligence Layer and the Browser-Native Agent](briefings/2026-07-the-visible-safety-layer/2026-07-03-the-admin-intelligence-layer-and-the-browser-native-agent.md)
*   [2026-07-06 - The Governance Reckoning and the Desktop Agent Race](briefings/2026-07-the-visible-safety-layer/2026-07-06-the-governance-reckoning-and-the-desktop-agent-race.md)
*   [2026-07-07 - Agentic Defaults, Demonstration Learning, and the Gemini UI Pivot](briefings/2026-07-the-visible-safety-layer/2026-07-07-agentic-defaults-demonstration-learning-and-the-gemini-ui-pi.md)
*   [2026-07-08 - The Cross-Device Agent and the Asynchronous Delegation Moment](briefings/2026-07-the-visible-safety-layer/2026-07-08-the-cross-device-agent-and-the-asynchronous-delegation-momen.md)
*   [2026-07-13 - The Unified Agent Desktop and the Workspace Execution Race](briefings/2026-07-the-visible-safety-layer/2026-07-13-the-unified-agent-desktop-and-the-workspace-execution-race.md)
*   [2026-07-14 - Generative UI, Messaging Surfaces, and the Accessibility Turn](briefings/2026-07-the-visible-safety-layer/2026-07-14-generative-ui-messaging-surfaces-and-the-accessibility-turn.md)
*   [2026-07-15 - Voice as Interface, Skills as Memory, and the Browser Expansion](briefings/2026-07-the-visible-safety-layer/2026-07-15-voice-as-interface-skills-as-memory-and-the-browser-expansio.md)
*   [2026-07-16 - Compliance Surfaces, Sandbox Trust, and the Personalisation Layer](briefings/2026-07-the-visible-safety-layer/2026-07-16-compliance-surfaces-sandbox-trust-and-the-personalisation-la.md)
*   [2026-07-17 - Open Source as Trust Signal, Agentic Memory, and the New Tasks Layer](briefings/2026-07-the-visible-safety-layer/2026-07-17-open-source-as-trust-signal-agentic-memory-and-the-new-tasks.md)
*   [2026-07-20 - Demonstration-to-Skill, Agent Memory, and the Automation Layer](briefings/2026-07-the-visible-safety-layer/2026-07-20-demonstration-to-skill-agent-memory-and-the-automation-layer.md)
*   [2026-07-21 - Agent Governance, Desktop Locals, and the Bigger Work Surface](briefings/2026-07-the-visible-safety-layer/2026-07-21-agent-governance-desktop-locals-and-the-bigger-work-surface.md)

## Monthly Management Summaries

To provide a high-level overview of the most significant themes and shifts in the agentic ecosystem, concise management summaries (1-2 pages) are available at the top level of this repository. These documents synthesize the daily briefings to highlight the macro trends shaping the future of human-computer interaction.

*   [**February 2026 Summary**](summary-2026-02.md): Focuses on the operationalization of agentic AI, the shift from chat assistants to active workflow participants, and the emergence of new business models and multi-model orchestration.
*   [**March 2026 Summary**](summary-2026-03.md): Highlights the migration of AI agents to the local desktop ("The Agent Comes Home"), the rise of generative UI ("Intent is the New Interface"), and the industry's response to user pushback against aggressive AI integration.
*   [**April 2026 Summary**](summary-2026-04.md): Details the formalization of Agentic UX patterns, the fragmentation of generic chat windows into specialized workspaces, and the expansion of multimodal, multi-agent workflows.

## Automation

These briefings are generated automatically — no manual research required.

*   **`scripts/research_agent.py`** runs every weekday at 07:00 UTC via [GitHub Actions](.github/workflows/daily_research.yml). It uses the Claude API with web search to research the latest agent-UX developments, writes the briefing in the house style, updates this README, and commits the result.
*   **`scripts/generate_summary.py`** runs at 08:00 UTC on the 1st of each month via [GitHub Actions](.github/workflows/monthly_summary.yml). It synthesizes the previous month's daily briefings into a "Management Summary" (no web search — pure synthesis over already-written content), matching the format of the existing Feb–Apr summaries, and updates this README.
*   **`scripts/generate_index.py`** rebuilds `docs/briefings.json`, the index powering the [web reader](https://derscharni.github.io/Ai-UX-Experience-News/).
*   **`scripts/generate_feed.py`** rebuilds `docs/feed.xml`, an RSS 2.0 feed of every briefing — the "live update into a second brain" channel. Any RSS-ingestion plugin (Obsidian, Logseq, Readwise Reader, Zapier/IFTTT, …) can subscribe directly; no polling or scraping needed. Auto-discoverable via the `<link rel="alternate">` tag on the web reader.
*   **`scripts/sync_to_obsidian.py`** is an optional local tool that mirrors the briefings into an Obsidian vault. Frontmatter follows Google's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (OKF) v0.1 core fields (`type`/`title`/`description`/`resource`/`tags`/`timestamp`), plus our own richer domain fields (`products`, `month-theme`) kept as OKF-permitted extensions — so notes are both Dataview-queryable *and* readable by any OKF-aware tool. Copy `scripts/obsidian_config.example.json` to `obsidian_config.json` and set your `vault_path`.
*   **`scripts/archivist.py`** is the *Archivist* — an optional local tool that cross-links every note in the vault. It scans the synced daily briefings, monthly summaries, and any on-demand research notes (e.g. files saved by the [`/last30days`](https://github.com/mvanhorn/last30days-skill) skill into the configured `research_folder`), computes TF-IDF similarity between them, and appends a `## Related Notes` section of Obsidian `[[wikilinks]]` to each — annotated with the shared products and keywords. It is idempotent, so run it after each sync or research session. Preview with `python scripts/archivist.py --dry-run`.
*   **`scripts/okf_watch.py`** runs weekly via [GitHub Actions](.github/workflows/okf_watch.yml). It diffs Google's upstream OKF spec against the snapshot in `scripts/okf/` and, when it changed, asks Claude to write a short note to [`docs/okf-alignment-log.md`](docs/okf-alignment-log.md) on what changed and whether our schema should track it. It never edits code itself — schema changes stay a reviewed, human decision, so we can mix in our richer fields now and converge further toward the standard as it matures.

**Setup:** add an `ANTHROPIC_API_KEY` repository secret (*Settings → Secrets and variables → Actions*) and enable Pages (*Settings → Pages → Source: `main` / `docs`*).

## About the Author

**Jens Scharnetzki** is the Head of Experience Design & Journey Management at EnBW. He is a recognized thought leader in the emerging fields of Agent Experience (AX) and Temporal UX, exploring how human interaction models must adapt as AI systems become increasingly autonomous, proactive, and deeply integrated into our daily workflows.
