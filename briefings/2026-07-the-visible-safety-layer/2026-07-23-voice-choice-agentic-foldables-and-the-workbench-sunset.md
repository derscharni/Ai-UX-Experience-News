# UX Briefing: Voice Choice, Agentic Foldables, and the Workbench Sunset

**July 23, 2026**

Good morning. The 48 hours ending July 23 are shaped by three distinct design impulses arriving simultaneously: the expansion of model-level choice into interaction modalities that have historically been locked to a single model, the arrival of agentic AI assumptions into hardware form factors for the first time, and a steady stream of developer-platform housekeeping that quietly removes legacy surfaces before users rely on them too deeply. **Claude/Anthropic** is the most active in this window — the Platform ships a dense July 22 batch that adds effort-level configuration and lifecycle webhooks to **Claude Managed Agents**, the `agent-memory-2026-07-22` beta header stabilises listing semantics across all major SDKs, and a feature flag now routes **Claude Voice Mode** sessions through Opus and Sonnet rather than silently falling back to Haiku, pointing to an imminent public rollout of genuine model choice for voice conversations. **ChatGPT/OpenAI** launches its **ChatGPT for Small Business** programme — an on-ramp initiative pairing the Work agent with in-person academies and workflow templates — while simultaneously disclosing that ChatGPT Work and Codex have already reached 10 million users. **Google Gemini** completes the rollout of **Gemini Omni** conversational video editing inside **Google Vids**, turning a timeline-editing tool into a natural-language-driven video creation and revision surface. **Microsoft Copilot** consolidates the **New Copilot** redesign as the permanent experience for all users, with the **Tasks tab** now the canonical surface for monitoring ambient agent activity, and **Copilot Cowork** continuing its billing-activated enterprise rollout. **Samsung Galaxy Unpacked** (July 22) debuts the **Galaxy Z Fold 8** line with an agentic AI layer — **Now Nudge** proactively opens multi-window contexts — and **Galaxy Glasses**, making this the first major hardware Unpacked explicitly framed around multi-step agent execution rather than chatbot assistance.

---

## At a Glance: July 23 Highlights

The releases in this window converge on a single design question: as agentic AI migrates into every interaction layer — voice, video, hardware, enterprise workflows — what choices do users actually retain about how those agents operate, and on what model?

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Voice Mode** model selector now functionally routes through Opus and Sonnet (previously cosmetic); **Managed Agents** gains effort-level config and lifecycle webhooks for environment/memory stores on July 22; **legacy Workbench** sunset confirmed for August 17; **Claude Code** adds `Needs input` status for paused sessions. [1][2][3] |
| **ChatGPT** | **ChatGPT for Small Business** programme launches — virtual training, in-person AI academies, partner integrations, and workflow templates; Work + Codex milestone: 10M users; **Codex** desktop polish across long chats, sidebar, reviews, and side chats continues. [4][5][6] |
| **Google Gemini** | **Gemini Omni** lands in **Google Vids** — conversational text-based video editing and generation from prompts plus reference images, replacing timeline-based editing; **personal avatars** built from selfie + voice recording; rollout began July 16 for Rapid Release domains. [7][8][9] |
| **Microsoft Copilot** | **New Copilot** forced-default (since July 15) with **Tasks tab** for long-running agent monitoring; **Copilot Cowork** GA (since June 16) continues billing-activated rollout with Cost Management dashboard in M365 admin center; **Claude** now selectable inside **Copilot Chat** as alternative model. [10][11][12] |
| **Grok (xAI)** | **Grok Build** open-source harness (Rust, Apache 2.0, GitHub) remains the primary trust-design reference point for the window; **Automations** continue rolling out — scheduled and email-triggered; **grok-voice-think-fast-1.0** now available on the Voice Agent API. [13][14][15] |
| **Perplexity** | **Brain** self-improving memory system in Research Preview (Max/Enterprise Max) builds a context graph from agent work rather than user preferences, refreshing overnight; Computer now supports **mid-task model switching** and **website publishing** from research outputs. [16][17][18] |
| **Samsung** | **Galaxy Unpacked July 22** — Z Fold 8 Ultra / Z Fold 8 / Z Flip 8 debut with **Now Nudge** agentic multi-window prompting and Gemini-powered background task execution; **Galaxy Glasses** launched as first AI eyewear entry. [19][20] |

---

## Product Highlights

### Claude / Anthropic: Voice Model Choice, Effort Dials, and the Workbench Retirement

Anthropic's most consequential interaction-design work in this window is distributed across three distinct registers — a voice-modality trust change that is still behind a feature flag, a developer-platform control expansion that ships stable today, and a developer-surface retirement that sets a hard deadline.

The voice-mode change is the most user-visible. 

A model selector has sat inside the voice interface for roughly three weeks, but until now the choice was cosmetic — whichever option you picked, the session still ran on Claude Haiku 4.5. That shifted today: selecting Opus or Sonnet now routes voice conversations through those models rather than quietly falling back to Haiku, which points to an imminent public rollout, probably within days (this feature is not yet available to the public and is currently hidden under a feature flag).

 The trust-design implication of this change is significant: for the entire period the selector existed without functional effect, users were operating under a false impression of control — a pattern that is particularly corrosive for voice, where the interaction register is more intimate and the model's character is more viscerally apparent than in text. Resolving that discrepancy — making the selector *actually* select — is the transparency fix that had to happen before the wider rollout.

On the developer platform, 

as of July 22 you can now set an `effort` level on a Claude Managed Agents agent's model configuration, passing `effort` inside the model object when you create the agent; webhooks for Claude Managed Agents now cover the environment and memory store lifecycle, with four `environment.*` event types and three `memory_store.*` event types.

You can react to environment and memory store lifecycle changes without polling.

 The effort-level dial is the agentic resource-management primitive that production deployments have needed: it lets developers express whether a task warrants maximum reasoning depth or speed-optimised processing at agent-creation time, rather than only at the model-call level. The lifecycle webhook expansion — covering both environment and memory-store events — closes the polling gap that previously required developers to periodically query state rather than react to it, a structural improvement for long-running agents where polling latency directly affects responsiveness.

The Workbench retirement is the legacy-surface change with the broadest developer impact. 

The Claude Developer Platform is retiring the legacy Workbench and experimental prompt tools APIs, with access ending on August 17, 2026; users can export saved data before the updated Workbench replaces unsupported legacy prompts, variables, and evals.

Claude Code's agent view now shows sessions waiting on a sandbox, MCP-input, or managed-settings prompt as "Needs input" instead of "Working."

 This status-label correction is a small but meaningful trust-design fix: "Working" implied the agent was making progress; "Needs input" accurately signals that the agent is *blocked*, giving developers the correct mental model for why a session has gone quiet.

---

### ChatGPT / OpenAI: The Small Business On-Ramp and the 10M User Signal

OpenAI's most interaction-design-significant move in this window is not a new product feature but a new adoption architecture: the **ChatGPT for Small Business** programme builds a structured on-ramp — training, academies, templates, and partner integrations — designed to move small business owners from isolated chatbot use into repeatable agentic workflows, anchored around the Work agent.



OpenAI is announcing the launch of its ChatGPT for small businesses program, an initiative to help small businesses be more productive and scale their businesses with ChatGPT. The programme includes hands-on virtual training — product-specific webinars that show how small businesses can use ChatGPT Work in their day-to-day, with demos for specific small business use cases, prompts to try, and automations and workflows across accounting, marketing, ecommerce, and more.

These include access to hands-on virtual training, attending in-person small business AI academies in the U.S., helpful guides for getting started with ChatGPT, and access to new agents and partners specifically made for small businesses.

 The interaction-design significance of this programme is not the features it exposes — those are the same Work agent features that enterprise users already have — but the *delegation vocabulary* it is building. Accounting, marketing, and ecommerce are task domains with specific, learnable delegation patterns, and the webinar-plus-template structure teaches users to express their intent in the agent's language rather than leaving them to discover it by trial and error.



The company simultaneously touts reaching 10M ChatGPT Work and Codex users.

ChatGPT Work is powered by GPT-5.6, the most advanced model available to businesses of any size and all subscription plans.

 The 10M user disclosure is the adoption-signal that gives the Small Business programme its strategic context: Work has already scaled past the early-adopter tier into mainstream professional use, and the programme is designed to accelerate the next tier of adoption — the lean-team owner who does not have an IT department or a product manager to build workflows on their behalf. The UX challenge this programme addresses is real and distinct from enterprise deployment: a solo business owner cannot tolerate a tool that requires multi-session configuration to become useful, which is why the on-ramp is built around templates and guided instruction rather than API documentation.

---

### Google Gemini: Conversational Video Editing and the End of the Timeline

Google's most UX-relevant work in this window — though it landed on July 16 and is still in active rollout — is the arrival of **Gemini Omni** inside **Google Vids**, which represents the most complete implementation yet of the natural-language-to-video-output interaction pattern across any major productivity suite.



Google on July 16, 2026, added two capabilities to Google Vids, its Workspace video creation tool: a generative model called Gemini Omni that produces and edits clips from written prompts, and personal avatars that let a user build a digital stand-in from a single selfie and a short voice recording.

The update arrives three and a half months after Google opened basic video generation inside Vids to every account holder, and it moves the tool further from timeline-based editing toward a workflow driven entirely by natural language. Gemini Omni handles two jobs that previously required separate effort: generating a video from scratch and refining one after the fact.

 This is the generative-video interaction pattern with the most direct workplace-tool significance: rather than a creative-suite capability requiring specialist skill, Vids now accepts intent expressed in natural language — and produces, or modifies, footage from it. 

Users can generate higher-quality AI-generated videos as well as edit existing clips simply by entering text — for example, to make colour corrections, change the style, or remove distracting background noise.

Inside Google Vids, users can begin by describing the clip they want and add reference images for more control over the final result. Once the first version is ready, they can continue chatting with Omni to change the background, improve the lighting, add effects, or adjust individual parts of the scene.

 The conversational editing loop — generate, then refine through follow-up prompts rather than timeline scrubbing — is the interaction pattern that collapses the traditional distinction between creation and editing into a single continuous dialogue. 

Rollout began July 16, 2026 for Rapid Release domains and will begin August 5, 2026 for Scheduled Release domains; in the EEA, Switzerland, the United Kingdom, as well as Texas and Illinois, editing of non-AI-generated videos will not be available initially.

 The regional carve-out is the trust-governance signal worth noting: the editing capability (which applies AI generation to content the user did not originally create with AI) is subject to tighter regulatory scrutiny than pure generation, and Google is shipping regionally rather than globally to navigate that boundary.

---

### Microsoft Copilot: The Tasks Tab Becomes the Agent Dashboard

Microsoft's most interaction-design-significant development in this window is the completion of the **New Copilot** forced-default rollout — a moment that makes the **Tasks tab** for monitoring long-running agent activity the permanent, universal navigation primitive for every Microsoft 365 Copilot user.



The update introduces a redesigned layout with revised menus and navigation; frequently used features are reorganised, and a new Tasks tab allows users to monitor activities in progress. Copilot chat conversations appear in an updated format, with responses, references, and suggested actions presented differently, and users who work with Copilot agents will notice updated labels that distinguish agent interactions from standard Copilot chats.

The updated experience will be on by default, and on July 15 for standard release, the toggle will be removed and the updated experience will be default on without the option for users to switch back to the previous experience.

 The forced-default moment matters because it converts the Tasks tab from an opt-in panel for early adopters into the standard mental model for every Copilot user — including the millions who will encounter Copilot agents for the first time through this interface.

**Copilot Cowork**, which reached general availability on June 16 and is now in active enterprise billing rollout, adds a new administrative governance layer that is directly relevant to daily-use UX. 

Admins can control the discoverability of Copilot Cowork and consumptive features via Copilot Settings, and a new Cost Management dashboard in the Microsoft 365 admin center gives admins visibility and control over billing configuration, spending policies, and usage reporting.

Cowork handles long-running, multi-tool workflows across Microsoft 365 apps, files, and data; admin controls, Copilot Credits billing, and Sentinel agent visibility support enterprise AI governance.

 The Cost Management dashboard is the admin-layer trust primitive that makes Cowork deployable at scale: without visibility into per-task spending, organisations cannot set rational delegation policies — they cannot decide which task types are worth delegating to an agent without knowing what each class of task costs in practice.



Anthropic's Claude is now a selectable model inside Copilot Chat, alongside Microsoft's own models; users can choose Claude for complex analysis, document understanding, and structured content generation, then switch back for everyday tasks. This is a genuine choice, not a marketing label: different models suit different jobs, and giving people the option to pick the right tool for a specific task is a meaningful shift from the single-model Copilot most businesses have used until now.



---

### Grok (xAI): Voice API Expansion and the Open-Source Transparency Arc

xAI's most consequential ongoing UX arc in this window is the Grok Build open-source publication — now stable on GitHub — which continues to function as the industry's clearest example of source transparency as a trust-repair mechanism. The new product surface in this window is the **Voice Agent API**.



The `grok-voice-think-fast-1.0` model is now available via the Voice Agent API, giving developers programmatic access to xAI's fast reasoning voice capability.

 The arrival of a reasoning-capable voice model on the developer API is the interaction pattern with the most forward-looking agentic significance: voice agents that can reason mid-conversation — rather than simply transcribe and route — can handle the ambiguity and clarification loops that make complex task delegation by voice practical rather than frustrating. 

xAI's Automations lets users set jobs to run on a schedule or when a matching email arrives, available on grok.com and iOS and Android, supporting templates, run history, and reports back by email or app notification; users describe a job once and Grok runs it on a schedule or when an email arrives, then reports back.



On the open-source front, 

the Grok Build harness published on GitHub covers the agent loop — how context is assembled, how model responses are parsed, and how tool calls are dispatched — the tools, the terminal UI, and the extension system including skills, plugins, hooks, MCP servers, and subagents.

Grok Build can now also run fully local-first: compile it yourself, point it at your own local inference, and drive everything from your `config.toml`.

 The local-first option is the trust primitive that extends source transparency into operational practice: users who have read the source and verified the agent's behaviour can now run that exact verified harness locally, closing the gap between *inspecting* how the agent works and *controlling* where it runs.

---

### Perplexity: Brain, Mid-Task Switching, and the Agent-Performance Memory Thesis

Perplexity's most architecturally distinctive work in this window is the continued rollout of **Brain** — its self-improving memory system for Computer — which advances a fundamentally different design thesis about what AI memory is *for*.



Brain is a self-improving memory system that builds a working model of your projects, people, and files to give Perplexity Computer the context it needs to move your work forward.

Perplexity said the goal is to move AI memory beyond personalisation. Most memory systems focus on the user — including preferences, contacts, work style, and recurring instructions. Brain is focused on what the agent did, what worked, what failed, and what corrections were made.

 This distinction is the most important design choice in Perplexity's current product surface: user-focused memory makes the agent feel familiar; agent-performance memory makes it *better at the work itself*. The first reduces social friction; the second reduces task friction. 

Brain runs in the background, reviewing recent activity from sessions, connector updates, artifacts, and corrections, and writing what it learns into Computer's memory; each entry links back to its source, so users can check or correct it.

Perplexity adds self-improving memory, faster Opus 4.8 Fast mode, Claude Fable 5 orchestration, mid-task model switching, website publishing, cleaner homepage navigation, per-model usage analytics, Mac account switching, and private company research in Computer. Computer now learns from every task: Brain builds a private context graph across your sessions, connectors, files, and past decisions, then refreshes it overnight so each new task starts already knowing what worked, what failed, and how you like things done; every memory links back to its source, and you control what it keeps under Customize.

 The **mid-task model switching** capability — allowing users to change the orchestrator model partway through a running task — is the interaction pattern with the most direct trust implication in this release: it lets users course-correct the agent's reasoning architecture without abandoning the task, reducing the cost of discovering mid-task that a different model would handle the next step better. 

Users can start with a complex research question, then keep working from the result by turning findings into a report, spreadsheet, deck, dashboard, website, or follow-up workflow in the same place.



---

### Samsung: The Foldable as the Agent Oversight Surface

Samsung's Galaxy Unpacked on July 22 is the most consequential hardware event for agentic UX this window, and it merits analysis for the interaction-design thesis it embeds in physical form factor — not just software.



Samsung Galaxy Unpacked 2026 arrives in London on July 22 with the Flex Titanium foldable display redesign, two simultaneously launched book-style Galaxy Z Fold 8 models, Samsung Galaxy Glasses AI eyewear, and a new agentic AI platform layer.

Agentic AI anticipates when multitasking is needed, using **Now Nudge** to open Multi Window at the right moment — for example, suggesting adding dinner plans from a messaging app to the calendar and opening the Calendar app in Multi Window.

 Now Nudge is the agentic UX primitive that most directly makes the case for the foldable form factor: proactive multi-window suggestions are most useful when there is actually a large enough display to make two concurrent contexts legible. The agent's intervention — *I notice you might need this other app right now* — is only non-disruptive when the user does not have to close one context to open another.



The device also delivers a more advanced agentic AI experience — for example, if a user shares a photo of the Eiffel Tower with Gemini and asks it to book a nearby hotel, the AI agent finds accommodations that match the specified criteria even while they continue using other apps.

 This is the ambient-background-agent pattern applied to the phone's primary interaction surface: the agent works in the background while the user continues interacting in the foreground, with the fold providing the physical space for both to be visible simultaneously. 

Galaxy Z Fold8 Ultra pairs ultra-level performance with an 8-inch main display designed for AI-powered multitasking to elevate productivity; the Galaxy Z Fold8 offers screen ratios optimised for various content types and advanced agentic AI features.

All foldables run One UI 9 based on Android 17 out of the box, and Samsung is positioning AI as a key point of differentiation on its devices with a strong suite of utilities distributed throughout.



---

## The Bigger Picture: Voice Choice, Agentic Foldables, and the Workbench Sunset

The 48 hours ending July 23, 2026 reveal a design maturation that is less about launching new agent capabilities and more about making existing ones honest, governable, and physically embodied. Claude's voice-mode model selector is the clearest expression of this shift: for three weeks, users had a control that looked like choice but delivered none. Fixing it — routing voice sessions through the model the user actually selected — is a small change with a large trust implication, because the gap between a visible control and a functional one is precisely the gap that erodes confidence in AI interfaces. The same principle runs through Anthropic's Managed Agents webhook expansion (replace polling with event-driven reaction) and the Workbench retirement (remove a legacy surface before users anchor workflows to it). OpenAI's Small Business programme makes the same argument from the adoption side: the gap between *an agent that technically works* and *an agent a solo business owner will actually delegate to* is filled by structured delegation vocabulary — templates, academies, worked examples — not by capability alone. Perplexity's Brain makes the most architecturally ambitious bet of the window: that AI memory should be optimised for agent-performance improvement rather than user-preference recall, shifting the memory design question from *what does the user like?* to *what has the agent learned to do better?* And Samsung's Now Nudge at Galaxy Unpacked makes the argument in hardware: if agents are going to proactively interrupt users with suggestions, the physical surface needs to be large enough to absorb that interruption without forcing a context switch. The foldable, reframed as an agentic-oversight canvas, is the hardware response to a software problem that no amount of UX polish can fully solve on a 6-inch screen. What unites all of these is a single structural move: the industry is no longer asking whether agents should be more capable, but how every layer of the stack — model selector, webhook, memory graph, hardware display — can be made worthy of the trust users are being asked to extend.

---

## References

[1] Claude Platform Docs. (2026). *Claude Platform release notes — July 22, 2026*. [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview)

[2] Releasebot. (2026). *Anthropic Release Notes — July 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[3] TestingCatalog. (2026). *Claude Voice Mode to get Opus and Sonnet model options*. [https://www.testingcatalog.com/claude-voice-mode-to-get-opus-and-sonnet-model-options/](https://www.testingcatalog.com/claude-voice-mode-to-get-opus-and-sonnet-model-options/)

[4] OpenAI. (2026). *Introducing the ChatGPT for small business program*. [https://openai.com/index/introducing-chatgpt-small-business-program/](https://openai.com/index/introducing-chatgpt-small-business-program/)

[5] 9to5Mac. (2026). *OpenAI launches small business program as it touts 10M ChatGPT Work and Codex users*. [https://9to5mac.com/2026/07/21/openai-launches-small-business-program-as-it-touts-10m-chatgpt-work-and-codex-users/](https://9to5mac.com/2026/07/21/openai-launches-small-business-program-as-it-touts-10m-chatgpt-work-and-codex-users/)

[6] OpenAI. (2026). *Release Notes — OpenAI Products*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[7] Google Workspace Blog. (2026). *Create, edit and star in videos with two Google Vids updates*. [https://blog.google/products-and-platforms/products/workspace/gemini-omni-personal-avatars/](https://blog.google/products-and-platforms/products/workspace/gemini-omni-personal-avatars/)

[8] TechCrunch. (2026). *Google Vids now lets you star in your own AI videos*. [https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/](https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/)

[9] PPC.Land. (2026). *Google Vids gains Gemini Omni editing and avatars for paid users only*. [https://ppc.land/google-vids-gains-gemini-omni-editing-and-avatars-for-paid-users-only/](https://ppc.land/google-vids-gains-gemini-omni-editing-and-avatars-for-paid-users-only/)

[10] WSU Insider. (2026). *Microsoft 365 Copilot receives interface updates in July 2026*. [https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/](https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/)

[11] Braintree. (2026). *Microsoft 365 Copilot: every update that matters from July 2026*. [https://www.braintree.co.za/microsoft-365-copilot-july-2026-updates/](https://www.braintree.co.za/microsoft-365-copilot-july-2026-updates/)

[12] M365 Admin. (2026). *Copilot Cowork generally available today*. [https://m365admin.handsontek.net/copilot-cowork-generally-available-today/](https://m365admin.handsontek.net/copilot-cowork-generally-available-today/)

[13] SpaceXAI. (2026). *xAI Release Notes — July 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[14] SpaceXAI Docs. (2026). *Release Notes — xAI Docs*. [https://docs.x.ai/developers/release-notes](https://docs.x.ai/developers/release-notes)

[15] SpaceXAI. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[16] Perplexity Help Center. (2026). *What is Brain?*. [https://www.perplexity.ai/help-center/en/articles/19700001-what-is-brain](https://www.perplexity.ai/help-center/en/articles/19700001-what-is-brain)

[17] Releasebot. (2026). *Perplexity Release Notes — July 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[18] CryptoBriefing. (2026). *Perplexity unveils Brain, a self-improving memory system for its AI Computer platform*. [https://cryptobriefing.com/perplexity-brain-memory-system-computer/](https://cryptobriefing.com/perplexity-brain-memory-system-computer/)

[19] Samsung Global Newsroom. (2026). *Galaxy Unpacked July 2026: A First Look at Galaxy Z Fold8 Ultra, Galaxy Z Fold8 and Galaxy Z Flip8*. [https://news.samsung.com/global/galaxy-unpacked-july-2026-a-first-look-at-galaxy-z-fold8-ultra-galaxy-z-fold8-and-galaxy-z-flip8](https://news.samsung.com/global/galaxy-unpacked-july-2026-a-first-look-at-galaxy-z-fold8-ultra-galaxy-z-fold8-and-galaxy-z-flip8)

[20] TechTimes. (2026). *Samsung Galaxy Unpacked 2026: Two Folds, Titanium Fix, and First AI Glasses*. [https://www.techtimes.com/articles/321249/20260722/samsung-galaxy-unpacked-2026-two-folds-titanium-fix-first-ai-glasses.htm](https://www.techtimes.com/articles/321249/20260722/samsung-galaxy-unpacked-2026-two-folds-titanium-fix-first-ai-glasses.htm)