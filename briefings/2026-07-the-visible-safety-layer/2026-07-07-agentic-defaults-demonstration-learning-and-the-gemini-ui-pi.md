# UX Briefing: Agentic Defaults, Demonstration Learning, and the Gemini UI Pivot

**July 07, 2026**

Good morning. The 48 hours ending July 7 are defined by a decisive shift in how the industry thinks about the *default agentic experience* — who gets agent-class capability by default, how agents learn new skills without code, and how interfaces must evolve to make the growing toolkit of autonomous capabilities legible and reachable rather than hidden behind menus. **Claude/Anthropic** makes its most structurally significant interaction-design move since Fable 5's return with the consequences of **Claude Sonnet 5 becoming the default model for all Free and Pro users** — a model built from the ground up to make plans, use browsers and terminals, and run multi-step tasks autonomously, simultaneously shipping with real-time cybersecurity safeguards enabled by default (a first for any Sonnet-tier model) and with the `/agents wizard` removed from Claude Code in favour of natural-language subagent management. **ChatGPT/OpenAI** continues the active landing of **Codex Record & Replay** — its most consequential interaction-design bet of the summer — which lets users demonstrate a workflow once on macOS and converts the observation into an inspectable, editable SKILL.md file, alongside **thread handoff between local and remote Codex hosts** and bulk automation run-history management. **Google Gemini** delivers the most significant generative UI redesign of the window with the continued active rollout of its **pill-shaped prompt box and unified + tools menu** across iOS, Android, and web — collapsing the previously scattered tool landscape into a single bottom sheet — while **Drive AI Overviews** lands on Android and iOS as a Gemini-powered ambient search layer. **Microsoft Copilot** continues its July default rollout with the **Tasks tab** and agent-interaction labels now live across enterprise tenants, and the **SharePoint Copilot Apps public preview** opens this month as a new generative UI extensibility surface. And **Grok (xAI)** lands a notable multimodal milestone as **Grok Imagine is declared complete** by xAI on July 5, with the Aurora-powered image and video generation workflow fully integrated across the Grok app and X, while the xAI Speech-to-Text API reaches general availability, surfacing the voice input layer builders need to wire into agentic surfaces.

---

## At a Glance: July 7 Highlights

The releases in this window converge on a single decisive argument: agentic capability is no longer an opt-in premium feature but the new default experience — and the critical design challenge is making that capability surface legible, learnable by demonstration, and safe enough to trust without a confirmation prompt on every step.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Sonnet 5** becomes the default model for all Free and Pro users — the first Sonnet-tier model built for autonomous multi-step tasks, with real-time cyber safeguards on by default and adaptive thinking enabled; **Claude Code** removes the `/agents wizard`, shifting subagent management to natural-language and direct file editing; **Managed Agents** now support cron-based scheduling with vault-stored credentials. [1][2][3] |
| **ChatGPT** | **Codex Record & Replay** continues active landing — users demonstrate a workflow once on macOS, Codex converts the observation into an inspectable, editable SKILL.md skill; **thread handoff** between local and remote Codex hosts ships; **bulk automation run history** actions and **GPT-5.5 Instant Mini** as a new smarter fallback model roll out to all users. [4][5][6] |
| **Google Gemini** | **Pill-shaped prompt box and unified + tools menu** continues active rollout across iOS, Android, and web — collapsing all capabilities (Deep Research, Canvas, Images, Videos, Music, Guided Learning) into a single bottom sheet with descriptions; **Drive AI Overviews** land on Android and iOS; **Dynamic View** and **Visual Layout** Labs features continue rolling out. [7][8][9] |
| **Microsoft Copilot** | July 2026 redesign with the **Tasks tab** and updated agent-interaction labels continues worldwide default rollout across enterprise tenants; **SharePoint Copilot Apps** public preview opens in July with a new generative UI extensibility model; **Copilot Notebooks** now available to all Copilot Chat users with Outlook email references. [10][11][12] |
| **Grok (xAI)** | **Grok Imagine declared complete** on July 5 — Aurora-powered image and video generation fully integrated into Grok app and X; **xAI Speech-to-Text API** reaches general availability with 25-language transcription in batch and streaming modes; **Grok Build** session-reliability fixes and `/goal` long-running autonomous mode continue active landing. [13][14] |
| **Perplexity** | **Deep Research in Computer** with the `/` command panel, thread forking, and inline confirmations continues active landing; **Computer in M365** (Word, Excel, PowerPoint, Outlook, Teams) rollout continues with inline citations and a context panel for live task tracking; **hybrid inference orchestrator** arrives on Windows this month with automatic sensitive-data on-device routing. [15][16] |

---

## Product Highlights

### Claude / Anthropic: Sonnet 5 as the Default Agent, Managed Schedules, and the Wizard Removal

Anthropic's most consequential UX shift in this window is not a new surface or a new governance feature — it is a *default change* that redefines what every Claude Free and Pro user encounters the moment they open the product.



Claude Sonnet 5 is built to be the most agentic Sonnet model yet — it can make plans, use tools like browsers and terminals, and run autonomously at a level that, just a few months ago, required larger and more expensive models.

 The UX significance of Sonnet 5 becoming the *default* is not primarily about capability headroom — it is about the interaction contract the model establishes with every new user. 

Adaptive thinking is on by default for Claude Code and API use, and real-time cybersecurity safeguards are enabled by default — the first time this has been true for a Sonnet-tier model.

 This means every free user who opens Claude today lands in an experience that has autonomous multi-step planning enabled from the first turn, with safety constraints active by default rather than opt-in. The shift from *chat-first default with agentic as an opt-in* to *agentic-first default* is the defining UX transition of this window.



Anthropic's safety assessments found that Sonnet 5 shows an overall lower rate of undesirable behaviors than Sonnet 4.6, and is generally safer to use in agentic contexts.

 The design implication is that the trust architecture of the default model has been deliberately calibrated for ambient, unsupervised execution — the model is safer precisely because it is expected to run with less human oversight than a chat assistant. This is the same logic that drove Claude Code's manual permission mode default, but applied at the model level: the agentic surface is designed from the ground up with the assumption that it will operate autonomously, and the safety layer is built in, not bolted on.

The second structurally significant interaction change in this window arrives in **Claude Code** and is a UI removal rather than an addition. 

The `/agents wizard` has been removed; users now ask Claude to create or manage subagents, or edit `.claude/agents/` directly.

 This is a meaningful shift in the subagent management UX: it eliminates the guided wizard scaffolding and replaces it with either natural-language delegation or direct configuration file editing — moving from a *form-based agent-creation flow* to a *conversational-or-file-based agent-creation flow*. The UX implication is a more expert-oriented interaction model for subagent setup, but one that is also more aligned with how the agent itself operates: by speaking intent, not filling fields. Alongside this, 

Claude Managed Agents can now run on a schedule and securely access CLI tools and other authenticated services — both features are in public beta on the Claude Platform; a scheduled deployment gives an agent a cron schedule, and each time the schedule fires, the agent starts a new session and completes its task, with no scheduler for you to build or host.

 This moves cron-based background automation from infrastructure the developer must build to infrastructure the Claude Platform manages, collapsing a significant operational layer.

---

### ChatGPT / OpenAI: Record & Replay, Thread Handoff, and the Demonstration-Learning Interaction Model

OpenAI's most interaction-design-significant active development in this window is the continued landing of **Codex Record & Replay** — a feature that, more than any other shipped this summer, changes the answer to the question "how do users teach an agent what to do?"



Codex adds Record & Replay on macOS to turn demonstrated workflows into reusable skills, bulk actions in automation run history, and thread handoff between local and remote hosts, while also improving SSH deep links, Browser Use session persistence, and overall performance.

 The interaction model established by Record & Replay is qualitatively different from all prior Codex skill-creation approaches: 

it is exactly what it sounds like — you record yourself doing a task once; Codex watches, learns, and turns your workflow into a reusable skill that it can run again and again on your behalf, with no code, no complex prompts, and no describing every click in painful detail; just show it.

 The resulting artifact is not a script or a macro — 

OpenAI's Record and Replay lets Codex watch you complete a repetitive task on macOS once, then turns those observed steps and window details into a reusable skill stored as an editable SKILL.md file that accepts variable inputs like new dates or files on future runs.

 The *inspectable, editable* nature of the SKILL.md output is the trust-design decision that distinguishes this from black-box RPA: the user can review, modify, and extend the skill before the next run, closing the transparency gap that makes fully automated workflows anxiety-inducing.



The feature shipped on June 18 as part of Codex app version 26.616, and is available to ChatGPT Plus, Pro, Business, Enterprise, and Edu subscribers outside the European Economic Area, the United Kingdom, and Switzerland.

 The geographic carve-out is significant: 

the EU AI Act's Article 50 transparency obligations, which explicitly cover agentic AI systems, are scheduled to take effect on August 2, 2026, and a pattern of staged geographic rollouts across Codex's most autonomous features suggests ongoing compliance work in those jurisdictions.

 This is a product surface where regulatory geography is directly shaping the availability of the most autonomous interaction patterns — a dynamic that is becoming structurally visible across every major agentic platform.

The **thread handoff** feature shipping alongside Record & Replay introduces a new coordination pattern for distributed agentic sessions: 

thread handoff between local and remote hosts lets you move a thread to a matching project on a connected host and continue it there, and Codex can also coordinate the handoff for you.

 This shifts the session model from *agent runs on one device and stays there* to *agent session is portable across hosts*, directly extending the Codex Remote GA architecture into seamless mid-task migration. 

ChatGPT also rolls out GPT-5.5 Instant Mini as a new fallback model — it replaces GPT-5.3 Instant Mini as the model users reach after hitting their GPT-5.5 Instant or Auto rate limits, and because it serves as a fallback, it won't appear in the model picker.

 The invisible-fallback architecture is itself a trust-design decision: the model picker stays clean, the rate-limit experience stays graceful, and the quality floor is raised without exposing the substitution to user anxiety.

---

### Google Gemini: The Unified Tools Menu, Drive AI Overviews, and the Capability-Legibility Problem

Google's most consequential UX story in this window is the continued cross-platform landing of a **full app redesign** that addresses one of the hardest problems in agentic interface design: how do you make an ever-expanding toolkit of specialised capabilities discoverable without overwhelming a first-time user?



According to 9to5Google, the redesign introduces a gradient background, a pill-shaped prompt box, a reorganized tools menu, and a new layout for model selection, with changes appearing aimed at making Gemini's tools easier to access across iOS and Android.

 The structural change is the collapse of the previously scattered capability landscape into a single entry point: 

the "+" button has been reimagined as a central hub — tapping it now opens an organized bottom sheet that consolidates Gemini's wide range of capabilities; users can quickly access images, camera input, music, Canvas, Deep Research, Guided Learning, and file uploads all from one place, eliminating the need to hunt through menus and making complex tasks like initiating a deep research session or attaching a NotebookLM resource as simple as a single tap.

 This is a meaningful capability-legibility design decision: it acknowledges that the existing multi-menu structure had made the tool surface opaque to users who didn't already know what Gemini could do.



While Gemini's core capabilities remain the same, the redesign significantly changes how users access them, shifting from a chat-first layout to a more organized, tool-driven interface.

 The model picker move is also significant: 

Google has gone back to placing the model picker in the top-left corner as a dropdown menu

, freeing space in the prompt box for input rather than model selection. Together these spatial decisions encode a philosophy: the prompt box is for intent, the top-left is for model selection, and the + button is for capability selection — a tripartite information architecture that reduces the cognitive load of knowing *what* Gemini can do before knowing *what you want to do*.

On the Workspace side, 

after announcing the general availability of Drive AI Overviews in Drive on the web in April, Google is now bringing this feature to the Drive Android and iOS apps — instead of searching through endless files and opening dozens of tabs to find the information you need, users can now get instant answers right at the top of their search results, with Gemini doing the heavy lifting by scanning documents to provide clear, reliable summaries.

 This is an ambient search layer rather than an explicit agent interaction — Gemini surfaces answers before the user has finished formulating their query — and its arrival on mobile makes the Drive surface meaningfully more agentic for the hundreds of millions of users who do their primary document work from a phone. 

Dynamic View in Labs takes this further using agentic coding capabilities — Gemini will design and code a unique experience with a user interface that is perfect for the specific prompt.

 The continued rollout of Dynamic View alongside the redesign signals Google's direction: as the tool infrastructure matures, the *output format* of Gemini's work is simultaneously evolving from text to bespoke, task-matched interfaces.

---

### Microsoft Copilot: SharePoint Copilot Apps, Agent Labels, and the Generative UI Extensibility Layer

Microsoft's most forward-looking UX development in this window is not the continued Tasks tab rollout — it is the opening of **SharePoint Copilot Apps** public preview, which for the first time gives developers a structured extensibility model for building generative UI components *inside* the Copilot experience.



Microsoft will be starting public preview of SharePoint Copilot Apps in July 2026 with a target to ship the feature generally available later 2026 — the preview covers building UX components for Copilot agents, including a "My Day" scenario, and goes beyond text in Microsoft 365 Copilot.

 The UX significance is structural: this is Copilot's first explicit generative UI extensibility surface — where developers can build task-matched interface components that surface inside Copilot sessions rather than redirecting users to external apps. This shifts the Copilot interaction model from *AI-assisted navigation to external tools* to *AI-orchestrated embedded experiences* — the same architectural bet that Dynamic View represents in Gemini.



The July update introduces a redesigned layout with revised menus and navigation; a new Tasks tab allows users to monitor activities in progress; and Copilot chat conversations appear in an updated format.

Responses, references, and suggested actions are presented differently, and users who work with Copilot agents will notice updated labels that distinguish agent interactions from standard Copilot chats.

 This agent-labelling distinction — now in active default rollout across enterprise tenants worldwide — is the trust-disclosure detail with the most daily-user significance: it makes the difference between "I am talking to Copilot" and "an autonomous agent is working on my behalf" legible at a glance, without requiring users to understand the underlying architecture. 

Copilot Notebooks is now available to all Copilot Chat users, rather than being locked to only those with a Microsoft 365 Copilot license, and customers can now add Outlook emails as references.

 Expanding Notebooks beyond the M365 Copilot paywall is a meaningful access decision — it makes the long-context, multi-source workspace available to a much broader population of users as a default surface rather than a premium one.

---

### Grok (xAI): Grok Imagine Complete, Speech-to-Text GA, and the Multimodal Agent Input Layer

xAI's most product-significant moment in this window is a declaration rather than a launch: **Grok Imagine** is done, and the xAI Speech-to-Text API has reached general availability — together these signal xAI completing its multimodal I/O stack at both the input and output layers.



Elon Musk posted a two-word update on July 5 — "Done with Grok Imagine" — signalling that development of Grok's image and video generation capability has reached completion, a milestone that moves xAI's flagship AI model firmly into multimodal territory.

 The UX implication is a completed output-modality stack: 

Grok Imagine has also been integrated directly within the X app, giving the feature a distribution channel with hundreds of millions of potential users.

 The X integration is the design detail that matters most — it means generative image and video outputs are now a native interaction primitive within X's social surface, not a separate product the user must navigate to. This changes the interaction model of X from *text social graph* to *multimodal social graph with embedded AI generation* — a shift with significant implications for how users compose and respond within the feed.

On the input side, 

the xAI Speech-to-Text API is now generally available, with transcription of audio to text in 25 languages in batch and streaming modes.

 This follows the native Grok Build voice-dictation integration shipped last window, but the GA of the API layer means builders can now construct voice-input pipelines into their Grok-powered agentic applications without leaving the xAI ecosystem. The UX pattern established by the combination of Speech-to-Text GA and Voice Agent Builder is a *full voice-agent stack* within a single provider — speech-to-text, language model, text-to-speech, telephony, and guardrails in one integrated surface, removing the multi-provider assembly that previously made production voice agents architecturally expensive. 

Grok Build continues receiving dense session-reliability improvements: OIDC sessions with `XAI_API_KEY` no longer lose refresh on idle, clicking a model in the dashboard `/model` dropdown no longer opens the wrong session, and prompt history now shows the complete recent list instead of a scrambled partial one.

 As Grok Build's `/goal` long-running autonomous mode continues its rollout, each of these reliability fixes extends the trustable delegation horizon — a developer can hand off a task to `/goal` and return to a session whose state actually matches what they left.

---

### Perplexity: Deep Research in Computer, the Citation Audit Layer, and the Hybrid Orchestrator's Windows Arrival

Perplexity's most consequential active UX development remains the multi-vector landing of **Deep Research in Computer** and the hybrid inference orchestrator — and the arrival of the orchestrator on Windows this month closes a significant deployment gap for Perplexity's enterprise differentiation argument.



Perplexity has added Deep Research in Computer, a new command panel, forking, improved inline confirmations, and enterprise controls like a Computer Analytics API and custom credit limits, making it easier to research, build artifacts, and manage usage; Deep Research is now available inside Computer.

Start with a complex research question, then keep working from the result by turning findings into a report, spreadsheet, deck, dashboard, website, or follow-up workflow in the same place.

 This *research-as-workflow-initiation* pattern — where the research session's output is the first step of an agentic production chain rather than a terminal document — is the interaction design that most directly competes with Copilot's native research surfaces in M365, where the output is typically a Copilot response inserted into an existing document. The command panel is the discoverability architecture that makes the full capability accessible: 

instead of remembering commands or navigating between modes, users open the panel by typing `/` and quickly search across available modes and skills before starting a task; the panel includes built-in modes like Deep Research and Plan Mode, alongside all available skills from the user, their space, and their organisation.

Perplexity has added Computer inside Microsoft 365 apps, bringing AI workflows to Word, Excel, PowerPoint, Outlook, and Teams; it also adds usage analytics, a new context panel for live task tracking, and answers with sources and inline citations for traceable claims.

 The inline citations in the M365 surface are the trust-design differentiator from Microsoft's native Copilot: every Computer output carries explicit source attribution, giving compliance teams and knowledge workers a verifiable provenance chain for AI-generated content inside the same documents that Microsoft's watermark policy is simultaneously trying to protect. 

A compact local model acts as the router for the hybrid inference orchestrator — classifying each subtask by data sensitivity and compute requirements before dispatching it; sensitive data (financial records, health files) stays on-device, and compute-heavy tasks go to frontier cloud models — no manual configuration required.

The feature arrives in Perplexity Computer in July 2026, initially on Windows.

 The Windows arrival this month lands Perplexity's most differentiated governance capability — explicit, user-invisible but admin-legible data routing — directly in the enterprise market that Microsoft's Tasks tab and Cowork GA are simultaneously contesting.

---

## The Bigger Picture: Agentic Defaults, Demonstration Learning, and the Gemini UI Pivot

The 48 hours ending July 7, 2026 mark the moment when agentic capability stopped being a premium tier and became the default experience — and exposed, in doing so, the next unsolved design problem: how do you make a toolkit that can plan, browse, execute code, generate images, and run on a schedule *feel like a tool the average user can trust and control*, rather than an opaque autonomous system that acts on their behalf without legible structure? Claude Sonnet 5 becoming the default model for every Free and Pro user is the most explicit statement of this shift: Anthropic is betting that a model built for multi-step autonomy, with adaptive thinking and real-time safety constraints on by default, is now appropriate as the *first thing every user encounters*. OpenAI's Codex Record & Replay answers the same challenge from the skill-creation side: if the agent can now learn a workflow by watching you do it once and converting that observation into an inspectable, editable skill file, then the human's role in the agent relationship shifts from *instructor of explicit instructions* to *demonstrator of intent* — a more natural and accessible delegation model that lowers the expertise barrier for autonomous workflow creation. Google's Gemini redesign — pill prompt box, unified + tools menu, descriptions for every tool — answers the challenge from the discovery side: you cannot delegate to an agent capability you didn't know existed, and a single bottom sheet with labelled tools is a fundamentally more honest design than the previous scattered-menu architecture. Microsoft's SharePoint Copilot Apps preview and Perplexity's `/` command panel both address the same legibility problem from the enterprise and research sides respectively: the agentic capability space is now large enough that navigation, discoverability, and progressive disclosure are first-class design problems, not afterthoughts. What the industry is converging on — one default change, one redesigned prompt box, one demonstration-learning feature at a time — is a new interaction contract: the agent is capable of more than the user consciously knows, the interface must surface that capability without overwhelming, and the skill-creation pipeline must be accessible to people who will never write a prompt, let alone a line of code.

---

## References

[1] Anthropic. (2026). *Introducing Claude Sonnet 5*. [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5)

[2] Releasebot. (2026). *Claude Code Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] Releasebot. (2026). *Anthropic Release Notes — July 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[4] OpenAI Developers. (2026). *Record & Replay — Codex*. [https://developers.openai.com/codex/record-and-replay](https://developers.openai.com/codex/record-and-replay)

[5] Releasebot. (2026). *Codex Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/codex](https://releasebot.io/updates/openai/codex)

[6] Releasebot. (2026). *ChatGPT Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] eWeek. (2026). *Google Gemini Gets a New Look: Here's What Changed*. [https://www.eweek.com/news/google-gemini-ui-redesign-tools-menu/](https://www.eweek.com/news/google-gemini-ui-redesign-tools-menu/)

[8] Google Workspace Updates. (2026). *Drive AI Overviews on Android and iOS*. [https://workspaceupdates.googleblog.com/](https://workspaceupdates.googleblog.com/)

[9] Gemini Apps. (2026). *Gemini Apps Release Updates & Improvements*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/)

[10] WSU Insider. (2026). *Microsoft 365 Copilot receives interface updates in July 2026*. [https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/](https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/)

[11] Microsoft 365 Developer Blog. (2026). *SharePoint Framework (SPFx) roadmap update — July 2026*. [https://devblogs.microsoft.com/microsoft365dev/sharepoint-framework-spfx-roadmap-update-july-2026/](https://devblogs.microsoft.com/microsoft365dev/sharepoint-framework-spfx-roadmap-update-july-2026/)

[12] Neowin. (2026). *Here are all the new features added to Microsoft 365 Copilot in June 2026*. [https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/](https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/)

[13] Basenor. (2026). *Grok Imagine Is Done: xAI Completes Image Generation Feature*. [https://www.basenor.com/blogs/news/grok-imagine-is-done-xai-completes-image-generation-feature](https://www.basenor.com/blogs/news/grok-imagine-is-done-xai-completes-image-generation-feature)

[14] xAI Docs. (2026). *Release Notes — xAI*. [https://docs.x.ai/developers/release-notes](https://docs.x.ai/developers/release-notes)

[15] Perplexity. (2026). *Perplexity Changelog*. [https://www.perplexity.ai/changelog](https://www.perplexity.ai/changelog)

[16] MarkTechPost. (2026). *Perplexity AI Introduces Hybrid Local-Server Inference Orchestrator for Personal Computer*. [https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/](https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/)

---