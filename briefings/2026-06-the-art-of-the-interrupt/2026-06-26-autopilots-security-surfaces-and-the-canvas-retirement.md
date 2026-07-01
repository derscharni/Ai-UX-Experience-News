# UX Briefing: Autopilots, Security Surfaces, and the Canvas Retirement

**June 26, 2026**

Good morning. The last 48 hours consolidate around four stories that together mark a new phase in agentic maturity. **Claude/Anthropic** reaches a distribution milestone with the GA of **Claude in Microsoft Foundry**, making Azure the first cloud to host both Claude and GPT frontier models under a single identity and governance layer — with data residency options, Azure-native billing, and a keyless OIDC authentication path that requires zero static Anthropic credentials; the companion **Claude Code dynamic workflows** feature arrives in research preview, enabling Claude to autonomously create and execute multi-step pipeline plans within a single session. **ChatGPT/OpenAI** ships two consequential trust-layer changes: **Canvas** is retired from GPT-5.5 Instant and Thinking in favor of inline **writing blocks and code blocks** embedded directly in the chat thread, and the new **Active Sessions** security panel gives users per-device visibility over every signed-in ChatGPT session. **Google Gemini** launches **Gemini Agent** as a full experimental Labs feature — a generalist multi-step task executor that can plan, confirm, and act across Gmail, Calendar, and the live web under continuous user supervision — and the previously announced **auto browse** for Chrome on Android begins its late-June rollout. **Microsoft Copilot** deepens its always-on agent story with the Frontier preview of **Microsoft Scout**, its first "Autopilot" agent category — a proactive, identity-bearing desktop agent that operates continuously under Entra governance — while the Copilot app itself receives a simplified June UI refresh explicitly targeting adoption clarity over feature density.

---

## At a Glance: June 26 Highlights

The releases this window converge on a single maturing question: as agents grow capable of operating without prompting, what is the right architecture for showing users what is running, proving it ran within bounds, and giving them back control at any moment?

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude in Microsoft Foundry** reaches GA (June 25–26) with two hosting paths — Azure-native (OIDC, Azure billing, US data zone, consolidated invoice) and Anthropic-hosted — plus **Claude Code dynamic workflows** in research preview, enabling Claude to auto-plan and execute multi-step pipelines at `ultracode` effort level. [1][2][3] |
| **ChatGPT** | **Canvas** is retired from GPT-5.5 Instant and Thinking in favour of inline **writing blocks and code blocks** embedded directly in the chat thread; **Active Sessions** security panel (Settings → Security) shows per-device sign-in details across ChatGPT, Codex, and API Platform sessions; GPT-4.5 officially retires from ChatGPT on June 26. [4][5][6] |
| **Google Gemini** | **Gemini Agent** launches as an experimental Labs tool for AI Ultra subscribers — breaking complex tasks into supervised steps with confirmation gates for critical actions, Gmail/Calendar/Canvas integration, and live web browsing; **auto browse** for Chrome on Android begins late-June rollout; **Visual Layout** and **Dynamic View** generative UI Labs features continue rolling out. [7][8][9] |
| **Microsoft Copilot** | **Microsoft Scout** (Frontier preview, announced June 2 at Build) represents a new "Autopilot" agent category — an always-on desktop app operating under its own Entra identity across Teams, Outlook, OneDrive, and browser, with tiered command permissions and Purview enforcement before any write action; the **Copilot app UI refresh** (GA June 2026) redesigns the chat home screen and navigation pane for adoption clarity. [10][11][12] |
| **Grok (xAI)** | Grok Build ships a dense bug-fix and polish wave: OIDC session stability under concurrent API keys, session cycling fixes (Ctrl+[/]), prompt history integrity, model/session routing corrections, and xychart diagram rendering — collectively hardening the agent session management surface introduced in the prior dashboard overhaul. [13][14] |
| **Perplexity** | **Comet Enterprise** is available for MDM-managed deployment with admin-configurable AI action controls and CrowdStrike-integrated security; **Samsung Galaxy S26** ships with Perplexity preloaded as "Hey Plex" at the OS level — Bixby and Samsung Internet both powered by Perplexity APIs — marking the first non-Google company to receive platform-level access on a Samsung device. [15][16] |

---

## Product Highlights

### Claude / Anthropic: Azure Foundry GA and Dynamic Workflows in the Agent Pipeline

Anthropic's most consequential interface and governance release of the 48-hour window is the general availability of **Claude in Microsoft Foundry**, which for the first time places Claude inside the same identity, billing, and governance infrastructure that Azure enterprises already operate. 

Starting June 25–26, Claude models are generally available in Microsoft Foundry, hosted on Azure — running in the customer's Azure environment with the authentication, billing, and governance controls their teams already use, with the option to choose where inference is processed, including a US data zone for teams with data residency requirements.



The trust design architecture matters most here. 

Customers using Claude through Microsoft Foundry are subject to Anthropic's data use terms, and for deployments hosted on Azure, prompts and completions remain within Azure — only usage metadata and content flagged by Anthropic's safety systems egresses to Anthropic.

 The two deployment paths — Azure-hosted and Anthropic-hosted — create an explicit trust choice that prior cloud partnerships did not make visible to developers at provisioning time: 

there are two ways to run Claude in Microsoft Foundry — choose hosted on Azure when running in your Azure environment matters, with Azure authentication, billing, governance, and a US data zone; choose hosted on Anthropic when you need the full set of API features or a model not yet available on Azure.

 The UX implication is a governed multi-model surface: 

Azure is now the only cloud providing access to both Claude and GPT frontier models on one platform, expanding Foundry into a single place to use any model, any framework, and every enterprise control needed to build and run AI apps and agents at scale.



Alongside the Foundry GA, **Claude Code dynamic workflows** arrives in research preview — the most agentic extension of the Claude Code interaction surface to date. 

Dynamic workflows are available in research preview in the Claude Code CLI, Desktop, and VS Code extension for Max, Team, and Enterprise plans; they can consume substantially more tokens than a typical Claude Code session; users can start a workflow by asking Claude directly, or by switching on `ultracode` in the effort menu — which sets effort to `xhigh` and lets Claude decide automatically when to use a workflow to handle the task.

 This shifts the interaction model from *user-directed step sequences* to *outcome delegation with autonomous plan generation* — the agent decides how to decompose the task and when to invoke a multi-agent workflow, and the user reviews the resulting pipeline rather than specifying it.

---

### ChatGPT / OpenAI: Canvas Retires into the Thread, Sessions Become Visible

OpenAI's most structurally significant UX change of the 48-hour window is not a new feature but a deliberate interface consolidation: the retirement of **Canvas** from GPT-5.5 Instant and Thinking in favour of inline **writing blocks and code blocks** embedded directly in the chat thread. 

With this update, canvas is no longer available in GPT-5.5 Instant or GPT-5.5 Thinking; writing and coding functionality is now supported directly in chat responses through writing blocks and code blocks; paid users can continue using canvas for a limited time through legacy models until those models are sunset.

 The design rationale is a consistency argument: 

the stated reasoning is about consistency across surfaces — with ChatGPT running on phones, tablets, web, and desktop apps, maintaining a separate canvas panel that doesn't render the same way everywhere became an engineering burden; writing blocks and code blocks are inline, which means they work the same way whether you're on a laptop or your phone.

 This shifts the UX contract from *side-panel workspace* to *inline structured artifact* — the response surface itself becomes the editing surface, collapsing the distinction between "the conversation" and "the document being worked on." The community reception is mixed: the inline blocks preserve iterability, but the Canvas version history and persistent side-panel — features heavily used for multi-revision document work — do not have clear equivalents in the blocks model yet.

Alongside the canvas retirement, 

OpenAI is rolling out **Active Sessions**, a new security feature in ChatGPT that helps users review sessions associated with their account and sign out of sessions they don't recognize.

Users can review first-party OpenAI sessions from Settings → Security → Active Sessions, with available details such as device, app, approximate location, sign-in time, trusted-device status, and whether it is the current session.

 The UX significance is the pairing of this feature with the previously shipped **Lockdown Mode** (June 6): together they create a two-layer trust surface — Lockdown Mode restricts what the agent can *send out*, while Active Sessions controls who can *reach in*. 

OpenAI has stated that Lockdown Mode "is not intended for everyone" and "is designed for people and organizations that handle sensitive data and want stricter protection from data exfiltration risks related to prompt injection."

 The combination establishes a new pattern for consumer-grade agent trust design: visible session inventory plus selective network isolation, available from a single Settings → Security path, without requiring enterprise enrollment.

---

### Google Gemini: Gemini Agent and the Supervised Multi-Step Execution Model

Google's most interaction-design-significant release of this window is the experimental launch of **Gemini Agent** in the Gemini app — a tool that fundamentally repositions Gemini from a turn-by-turn assistant into a supervised multi-step task executor, with a confirmation-gate architecture at its core. 

Gemini Agent is a new experimental tool that can complete multi-step tasks from start to finish while keeping the user in control; it uses Gemini 3's advanced reasoning and tool calling to break up complex tasks into smaller steps.

If the task requires it, Agent will use apps like Gmail or Calendar, alongside many of the tools in Gemini like deep research capabilities and Canvas, to achieve the end goal; it can also use live web browsing capabilities to research and take action on the web as part of completing a task.



The trust design of Gemini Agent is its most consequential UX element. 

Gemini Agent is designed to get the user's confirmation before taking any critical actions, like sending an email or making a purchase, and users can always pause or take over at any time.

After presenting a plan, each task can be individually declined or confirmed, with options to decline all or confirm all.

 This establishes a *step-level consent architecture* — not a single upfront delegation grant but a per-action approval sequence that keeps the human in the loop at the most consequential moments of the workflow. The Google support documentation is explicit about the prompt-injection risk: 

prompt injection is an attempt to elicit an unintended or harmful response from Gemini Agent, occurring when content like a website, email, document, or multimedia has malicious instructions hidden from the user but visible to the AI agent, which might be tricked into doing unintended things.

 Naming this risk in consumer documentation — not just enterprise governance material — marks a meaningful shift in how Google is framing agentic trust with general users. Meanwhile, 

Gemini in Chrome on Android including auto browse is launching in late June, initially available on devices with 4GB of RAM or more; auto browse for Android lets users automate digital chores from appointment booking to party planning and finding in-stock items, all from an Android phone.



---

### Microsoft Copilot: Scout, the Autopilot Category, and the Always-On Agent Model

Microsoft's most architecturally significant UX development in this window is not an incremental Copilot feature but a new product category: **Microsoft Scout**, unveiled at Build 2026 and now in Frontier private preview, which Microsoft formally designates as its first **Autopilot** agent — a proactive, identity-bearing, background-capable agent that operates without being prompted. 

Scout is described as an "Autopilot" — always on, working in the background on a schedule the user sets, under its own identity, acting on their behalf; it is a desktop app (Windows 11+ and macOS 12+) that can work with files, run commands in a terminal with a tiered permission system so nothing risky runs without approval, drive a browser and navigate pages and fill in forms, and reach into Microsoft 365 — Teams, Outlook, OneDrive, and SharePoint.



The identity and governance architecture is the story Scout is really telling. 

The security design centers on identity: each Scout agent operates under its own governed Entra identity that an organization's directory already recognizes, so the work it performs traces back to a known actor; according to Microsoft, the credentials behind that identity are scoped to the task at hand, redacted from logs and diagnostics, and managed with the same controls applied to first-party Microsoft services.

Sensitive actions can require human sign-off before proceeding; Microsoft Purview data protection policies, including sensitivity labels and loss prevention rules, are enforced in real time before anything is sent or written.

 Scout is powered by OpenClaw, and 

Microsoft is contributing policy conformance upstream to the OpenClaw project, which will let organizations running it validate whether their environment meets security and compliance requirements and produce an audit-ready answer.

 The UX implication is a new interaction paradigm: rather than a user who prompts and waits, Scout models a user who *sets policies and permissions once*, then reviews what the agent completed — a supervision model borrowed from enterprise infrastructure management and brought into knowledge work. Alongside Scout, 

the refreshed Microsoft 365 Copilot app rolling out in June 2026 changes the chat home screen, chat response layout, and navigation pane across Windows, Mac, and the web

 — 

the update represents Microsoft deciding that Copilot's problem is no longer merely capability, but comprehension, trying to make its flagship workplace AI feel less like a bolted-on experiment and more like the front door to Microsoft 365.



---

### Grok (xAI): Session Surface Hardening

xAI's Grok Build activity in this window is a dense wave of session-management correctness fixes following last week's major dashboard overhaul. 

OIDC sessions with `XAI_API_KEY` present no longer lose refresh on idle; session cycling with Ctrl+[/] now switches from the session currently being viewed; prompt history (Up/Ctrl+R) now shows the complete recent list instead of a scrambled partial one; authentication now correctly prefers the session method when both API key and cached token are present.

The `--disable-web-search` flag is now honored in `grok -p` and `grok agent`; auxiliary model routing respects catalog overrides; session last-active timestamps and message counts no longer regress under concurrent writers.

 Individually minor, these fixes collectively address the failure modes that emerge when the agent session surface — newly complex after last week's dashboard overhaul — encounters concurrent credentials, idle timeouts, and rapid mode switching. 

xAI also updated its fair-use policy language to clarify that rate limits apply cumulatively across text, image, voice, and code execution; previously the policy described limits per feature in isolation, but now the total compute consumption across the account triggers a soft cap.

The change also introduced a visible counter in the account dashboard, so users can track Grok message limits, token usage, and media generation in one place

 — a meaningful transparency upgrade for power users running parallel workflows who previously had no consolidated view of aggregate consumption.

---

### Perplexity: Samsung OS Integration and the Comet Enterprise Trust Layer

Perplexity's most strategically significant UX development in this window is the confirmation of its **Samsung Galaxy S26** OS-level integration — the deepest platform embedding Perplexity has yet achieved and the first non-Google company to reach that level of access on a Samsung device. 

The Perplexity app comes preloaded on every Galaxy S26, making Perplexity the first non-Google company to receive OS-level access on a Samsung device; users can say "Hey Plex" or press and hold the side button to launch the assistant instantly, with deep integration across Samsung apps including Notes, Calendar, Gallery, Clock, and Reminders for seamless multi-step workflows.

Samsung's Galaxy S26 is the first smartphone to integrate Perplexity's APIs at the platform level; Bixby now uses Perplexity for real-time web search and advanced reasoning, and Perplexity's capabilities extend to Samsung Internet, bringing agentic browsing capabilities from the Comet browser with Perplexity available as an optional default search engine.

 This is a distribution event with direct UX implications: Perplexity's multi-step agentic workflows are now the default intelligence layer for hundreds of millions of users who have never opened the Perplexity app — making trust and permission design, not feature discovery, the primary UX challenge.

On the enterprise side, 

Comet is now available for Enterprise organizations; Perplexity's AI-native browser comes with Comet Assistant for in-page research, summarization, and autonomous multi-step tasks; enterprise administrators can deploy Comet silently across macOS and Windows devices via MDM, configure hundreds of browser policies, and control exactly which actions the AI agent can take; all activity inherits existing Enterprise settings for data retention, audit logs, and permissions, with no data used to train models.

 The combination of MDM-deployable silent installation and admin-controlled action scope creates a new enterprise control surface for browser-native agentic tasks — a trust primitive that no other major browser currently offers at parity.

---

## The Bigger Picture: Autopilots, Security Surfaces, and the Canvas Retirement

The 48 hours ending June 26, 2026 are defined less by new capabilities than by the industry collectively solving the UX of *ambient agency* — what it looks like to interact with systems that run without being prompted. Microsoft's Scout defines the clearest statement of this paradigm: the Autopilot, an agent that runs continuously under a governed identity, acts within policy-defined boundaries, and requires human sign-off only for actions that cross a risk threshold. Google's Gemini Agent applies the same philosophy at the response level — each individual step in a multi-step plan surfaces a confirmation gate, making the agent's intent legible before it acts rather than auditable after. OpenAI's Canvas retirement tells the same story from the interface direction: by collapsing the separate editing workspace into inline writing blocks within the chat thread, the company is making the response surface itself the agent's working space, removing the boundary between "conversation" and "artifact" that Canvas maintained. And Claude's Foundry GA brings the same logic to the cloud execution layer — every agent workload now has an Azure-managed identity, a data residency choice, and a consolidated governance path, answering the enterprise question of "where did this run and what credential did it use?" across the most pervasive enterprise cloud. What connects all four stories is a shared conviction that the user interface for agentic AI is not the prompt box or the model picker — it is the *permission architecture*: the design of what the agent is authorised to do, what it must ask before doing, and how a human can see, steer, or halt it at any point in the workflow.

---

## References

[1] Anthropic. (2026). *Claude in Microsoft Foundry is now generally available*. [https://claude.com/blog/claude-in-microsoft-foundry](https://claude.com/blog/claude-in-microsoft-foundry)

[2] Anthropic Platform Docs. (2026). *Claude in Microsoft Foundry — Platform Documentation*. [https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)

[3] Releasebot. (2026). *Claude Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[4] OpenAI. (2026). *ChatGPT Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] Releasebot. (2026). *ChatGPT Updates by OpenAI — June 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[6] Medium / Mubashir Burfat. (2026). *I Used ChatGPT's Canvas Feature for Six Months. Then OpenAI Quietly Killed It*. [https://medium.com/@mubashirburfat4/i-used-chatgpts-canvas-feature-for-six-months-then-openai-quietly-killed-it-88c542f1a63f](https://medium.com/@mubashirburfat4/i-used-chatgpts-canvas-feature-for-six-months-then-openai-quietly-killed-it-88c542f1a63f)

[7] Gemini Apps. (2026). *Gemini Apps Release Updates & Improvements*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/)

[8] Google Support. (2026). *Use Gemini Agent for multi-step tasks in Gemini Apps*. [https://support.google.com/gemini/answer/16596215](https://support.google.com/gemini/answer/16596215)

[9] Chrome for Developers. (2026). *15 updates from Google I/O 2026: Powering the agentic web*. [https://developer.chrome.com/blog/chrome-at-io26](https://developer.chrome.com/blog/chrome-at-io26)

[10] Microsoft 365 Blog. (2026). *Introducing Microsoft Scout: Your always-on personal agent*. [https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)

[11] A Guide to Cloud & AI. (2026). *What's New in Microsoft 365 Copilot: June 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-june-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-june-2026-updates/)

[12] Windows Forum. (2026). *Microsoft 365 Copilot UI Refresh June 2026*. [https://windowsforum.com/threads/microsoft-365-copilot-ui-refresh-june-2026-simpler-chat-home-layout-navigation.432228/](https://windowsforum.com/threads/microsoft-365-copilot-ui-refresh-june-2026-simpler-chat-home-layout-navigation.432228/)

[13] Releasebot. (2026). *Grok Build Updates by xAI — June 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[14] Releasebot. (2026). *xAI Release Notes — June 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] Releasebot. (2026). *Perplexity Release Notes — June 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[16] SwitchTools. (2026). *Perplexity Comet Browser Review 2026*. [https://www.switchtools.io/blog/perplexity-comet-ai-agent-browser](https://www.switchtools.io/blog/perplexity-comet-ai-agent-browser)