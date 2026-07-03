# UX Briefing: The Admin Intelligence Layer and the Browser-Native Agent

**July 03, 2026**

Good morning. The 48 hours ending July 3 are defined by a decisive pivot from agentic capability rollout to agentic fleet governance — every major platform shipping the monitoring, alerting, auditing, and browser-native control surfaces that make large-scale autonomous AI deployable, not just demonstrable. **Claude/Anthropic** makes its most consequential enterprise governance move of the summer with **Claude Enterprise Admin Analytics**, a new control plane that adds per-user cost attribution, model-level entitlements, spend-threshold alerts firing at 75% and 90% of org limits, and an Analytics API that pipes usage data into tools like Datadog and Grafana — while simultaneously shipping **Claude in Chrome GA**, which reaches general availability with background-persistent tab execution and push notifications when the agent needs input or completes a task, and a new **/dataviz skill** in Claude Code that provides chart and dashboard design guidance with a runnable color-palette validator. **ChatGPT/OpenAI** continues active landing of its **Codex Mobile** remote-host experience — now rolling out in preview on iOS and Android across all plans including Business — allowing users to review live Codex progress, approve actions, and redirect work from their phone while the agent continues running on a connected Mac or Windows host; and **Locked Computer Use**, which allows Codex to keep driving Mac apps through the lock screen and be triggered remotely from a phone, continues active rollout for Enterprise and Edu users. **Google Gemini** ships two structurally significant developer-facing events: the **Interactions API** reaches general availability as the primary interface for all Gemini models and agents — adding Managed Agents, background execution, and server-side state — while the consumer-facing **Gemini Agent** experimental tool lands in Labs with explicit confirmation gates before consequential actions. **Microsoft Copilot** extends its July redesign story with the continued worldwide default rollout of the **Tasks tab** and Copilot Cowork now generally available, while the auto-installation of the M365 Copilot app on Windows commercial devices reaches its active deployment window. And **Grok (xAI)** ships dense reliability engineering in **Grok Build** — fixing idle session refresh, model-dropdown session mismatches, and clipboard copy trust-path confirmation — alongside the fully active landing of **Voice Agent Builder** GA, now accessible to all users as a no-code production voice platform.

---

## At a Glance: July 3 Highlights

The releases in this window converge on a single maturation signal: agentic AI has crossed from deployment to operations, and the design challenge is no longer "can the agent do it?" but "can the human see, audit, govern, and redirect what the agent is doing — whether it's running in a browser tab, behind a locked screen, or across a fleet of enterprise seats?"

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Enterprise Admin Analytics** ships per-user cost attribution, model-level entitlements, spend-threshold alerts (75%/90%), and an Analytics API for Datadog/Grafana integration; **Claude in Chrome** reaches GA with background tab persistence and agent-needs-input push notifications; **Claude Code** adds `/dataviz` skill and background agents that auto-commit and open draft PRs when finished. [1][2][3] |
| **ChatGPT** | **Codex Mobile** preview rolls out on iOS and Android across all plans — showing live Codex state (diffs, terminal output, approvals) on phone while the agent runs on a connected Mac or Windows host; **Locked Computer Use** for Enterprise/Edu continues landing, letting Codex drive Mac apps through the lock screen triggered from mobile; **Plugin Management** dashboard remains the freshest governance surface. [4][5][6] |
| **Google Gemini** | **Interactions API** reaches GA as the primary interface for all Gemini models and agents — adding Managed Agents, background execution, and server-side state; **Gemini Agent** launches as an experimental Labs tool with built-in confirmation gates before consequential actions; **Gemini in Chrome** continues active rollout for AI Pro/Ultra subscribers on Windows and macOS. [7][8][9] |
| **Microsoft Copilot** | July 2026 M365 Copilot redesign including the **Tasks tab** continues worldwide default rollout; **Copilot Cowork** reaches general availability with automatic model selection, expanded plugins, and custom skills; auto-installation of the M365 Copilot app on commercial Windows devices completes its active deployment window through mid-July. [10][11][12] |
| **Grok (xAI)** | **Grok Build** ships session-reliability fixes targeting real multi-agent failure modes: idle OIDC refresh loss, wrong-session model-dropdown opens, scrambled prompt history, and clipboard copy silent-success false positives; **Voice Agent Builder** GA continues active landing for all users with no-code production voice agent configuration. [13][14] |
| **Perplexity** | **Deep Research in Computer** with the `/` command panel remains the freshest workflow capability — collapsing research-to-artifact into a single session; **Computer in Microsoft 365** (Word, Excel, PowerPoint, Outlook, Teams) continues active landing with inline citations distinguishing it from native Copilot; **hybrid inference orchestrator** Windows rollout enters its July GA window. [15][16] |

---

## Product Highlights

### Claude / Anthropic: Enterprise Admin Analytics, Claude in Chrome GA, and the Agent-Output Observability Layer

Anthropic's most design-consequential releases in this 48-hour window arrive in two distinct but interlocking layers: an admin-facing observability and governance system for Claude Enterprise, and a browser-native agentic surface that reaches general availability with a new temporal UX pattern around background execution.



**Claude Enterprise Admin Analytics** introduces richer admin analytics, model-level entitlements, and spend alerts for Claude Enterprise — because as Claude takes on increasingly difficult and complex agentic work across the organization, usage and cost patterns look different from a standard chat tool, and admins need the visibility to understand how Claude is being used and the tools to manage costs.

 The design detail that matters most is the alert architecture: 

spend-threshold alerts notify admins at 75% and 90% of an org-level spend limit, giving them time to raise the cap before anyone gets blocked mid-task; users receive in-app notifications at 75% and 95% thresholds and can request a limit increase directly from their admin without leaving Claude.

 This closes a critical gap in agentic fleet UX — the moment a long-running background agent hits a spend wall mid-execution was previously a silent failure; now both the admin and the user are warned in advance with enough runway to act. 

Model defaults and entitlements let admins set which Claude model new conversations start with across chat, Cowork, and Claude Code so routine work doesn't necessarily default to the most expensive option; admins control which models are available to specific roles or across the entire organization.

 This shifts the UX of agentic cost governance from *reactive billing review* to *proactive budget-aware model routing* — a meaningful advance for organisations running Claude at org scale.

The second major release of the window is the general availability of **Claude in Chrome** in Claude Code. 

Claude handles complex, multi-step workflows and keeps working even when you switch tabs (as long as Chrome is open); enable notifications to receive alerts when Claude requires permission or completes a task, allowing you to focus on other work while Claude processes tasks in the background.

 The temporal UX design established here — *background execution with permission-gate notifications* — is a direct application of the async agentic session pattern: the human delegates, focuses elsewhere, and is recalled only when the agent requires input or has finished. 

Once a workflow runs reliably — whether from a recording or a saved shortcut — it can be scheduled to run automatically; when creating or editing a shortcut, toggle on Schedule; choose the frequency, set the date and time, and select which model to use; Claude runs the workflow at the specified time and notifies you when it's done or needs input.

 This establishes a *scheduled, model-selectable browser automation* pattern that is meaningfully more mature than the browser agent as purely interactive surface.

The third design-consequential change in this window is the Claude Code background agent workflow automation. 

Background agents launched from `claude agents` now commit, push, and open a draft PR when they finish code work in a worktree, instead of stopping to ask.

 This shifts the agent's completion handoff from *blocking question* to *actionable artifact* — the human returns to a draft PR rather than an idle agent waiting for permission. 

Claude Code also added a `/dataviz` skill for chart and dashboard design guidance with a runnable color-palette validator.

 This is a narrow but meaningful addition to the agentic output surface: for the first time, Claude Code can not only produce data visualisations but validate their own colour accessibility before presenting them to the user.

---

### ChatGPT / OpenAI: Codex Mobile, Locked Computer Use, and the Persistent-Agent Trust Architecture

OpenAI's most interaction-design-significant active rollouts in this window are the two features that together answer the temporal UX problem of long-running autonomous agents: what happens to the agent when the user is away from their desk?



Teams can now use the ChatGPT mobile app to stay connected to Codex work running on a host Mac, making it easier to answer questions, redirect work, approve actions, review outputs, and keep longer-running tasks moving when away from the host machine; the mobile experience reflects the live state of the connected environment, including project context, approvals, screenshots, terminal output, diffs, and test results.

 This is a foundational shift in the UX of autonomous coding: the agent's working state is no longer siloed to the desktop it runs on, but is mirrored to the phone as a live dashboard. 

Codex also adds access tokens for trusted, non-interactive local workflows, so approved automation can run through scripts, schedulers, or private CI runners with a ChatGPT workspace identity.

 The UX implication is a new *background automation with identity* pattern — scripted and scheduled agent runs now carry the operator's workspace identity rather than a generic API key, making them auditable and revocable through the same account governance layer.

**Locked Computer Use** — the companion capability allowing Codex to continue driving Mac apps through the lock screen — is the trust design centrepiece of this cluster. 

When a Codex task accesses an app via Computer Use after your Mac locks, Codex temporarily unlocks the Mac while blocking local use and preserving the locked screen protections; before unlocking, Codex checks whether the unlock attempt is for an active, trusted computer use turn; outside that short-lived window, Codex denies the unlock and asks you to unlock manually if needed.

 The design philosophy encoded here is *time-scoped, purpose-scoped unlock* — the agent's access to the desktop is constrained to the duration and scope of the active task, not an open-ended persistent privilege. 

The feature is macOS-only (no Windows or Linux support) and is unavailable in the European Economic Area, the United Kingdom, and Switzerland at launch, reflecting regional regulatory constraints on automated desktop access.

 This geographic carve-out is itself a significant interaction design disclosure — it makes the regulatory boundary of the feature explicit in the product surface, rather than burying it in policy documentation. Together, Codex Mobile and Locked Computer Use establish a new *distributed-session agentic architecture*: the agent runs on the desktop, the human supervises from the phone, and the trust model scopes the agent's access to precisely the actions that have been authorised.



Codex also gives Enterprise and Edu users in-app browser annotations for more precise styling feedback for browser-based and frontend work; Appshots (letting users attach an app window to a Codex thread with a hotkey, including a screenshot and available text) are available for ChatGPT Edu accounts today, with support for ChatGPT Enterprise coming soon; Goal Mode is generally available across the Codex app, IDE extension, and CLI, so users can define an outcome and success criteria and let Codex keep working toward it.

 The cumulative effect of these three features is a coding agent with an increasingly rich *ambient context awareness* — it can see the live state of any app window via Appshots, navigate and annotate in-browser interfaces directly, and maintain a defined outcome across session boundaries via Goal Mode GA.

---

### Google Gemini: Interactions API GA and Gemini Agent's Confirmation-Gate Model

Google's most structurally significant UX event in this 48-hour window is actually a developer-infrastructure release that directly shapes how all future Gemini-powered agents will present themselves to users: the **Interactions API** reaching general availability.



The Interactions API has reached general availability and is now the primary API for interacting with Gemini models and agents; launched in public beta in December 2025, it has quickly become developers' favourite way to build applications with Gemini; with this GA release, the API now has a stable schema and added major new capabilities including Managed Agents, background execution, Gemini Omni (soon) and more.

 The UX implication is structural: 

frontier capabilities for long-running models and agents are expected to increasingly land exclusively on the Interactions API because it is designed from the ground up for stateful, agentic workflows.

 This is a consequential API-layer design decision — by declaring the Interactions API as the primary surface and signalling that agentic capabilities will *only* land there, Google is effectively requiring all serious Gemini agent builders to migrate to the stateful, background-execution model rather than the stateless request-response paradigm. The interaction design consequence flows downstream to end users: every Gemini agent built on this API inherits server-side state management, which changes how the agent handles session interruptions, context handoffs, and multi-turn autonomous execution.

On the consumer side, **Gemini Agent** represents Google's most explicit statement yet about the trust design contract for autonomous action. 

Gemini Agent is a new experimental tool that can complete multi-step tasks from start to finish, while keeping users in control; it uses Gemini 3's advanced reasoning and tool calling to break up complex tasks into smaller steps; if the task requires it, it will use apps like Gmail or Calendar, alongside many of the tools in Gemini, like deep research capabilities and Canvas; additionally, it can use live web browsing capabilities to research and take action on the web as part of completing the task.

 The governance model is explicit: the agent is designed to ask for confirmation before taking consequential actions — sending emails, making purchases — and users can pause or take over at any time. This establishes *confirmation-before-consequence* as the standard trust pattern across all new Google agentic surfaces, consistent with the auto browse 2 design in Gemini in Chrome.



Google's two experimental Labs features — Visual Layout and Dynamic View — continue rolling out; powered by Gemini 3 and new advances from Google Research, these features make responses more engaging and interactive; Visual Layout uses multimodal capabilities to move beyond text, generating a visually immersive response with photos and interactive modules; these elements solicit feedback and help users further customise Gemini's response across multiple turns.

Dynamic View takes this further using agentic coding capabilities: Gemini will design and code a unique experience with a user interface that is perfect for the specific prompt.

 The continued rollout of these features alongside the Interactions API GA signals the design direction: as the infrastructure for stateful background agents matures, the *output format* of those agents is simultaneously evolving from text to bespoke, task-matched interactive interfaces.

---

### Microsoft Copilot: Cowork GA, the Tasks Tab Default, and the Auto-Install Moment

Microsoft's most design-consequential July deployment event continues to be the worldwide default rollout of the M365 Copilot app redesign — but this window's specific significance is the combination of that redesign going default with **Copilot Cowork** simultaneously reaching general availability.



Copilot Cowork is now generally available, accessed through a toggle in the Microsoft 365 Copilot app, allowing users to orchestrate complex workflows; Cowork can automatically choose the best AI model based on the task provided, supports more plugins than before, and enables users to define custom skills for specialized work; other enhancements include the ability to create and edit visuals, leverage the Edge browser, and send push notifications on mobile for long-running tasks on Android and iOS.

 The UX significance of the push notification addition is particularly notable: 

push notifications on mobile for long-running tasks on Android and iOS

 establish the same async temporal pattern that Claude in Chrome GA and Codex Mobile are implementing — the agent works in the background while the user is away, and the phone is the alert surface for re-engagement. This is not a coincidence; it is the industry converging on the same interaction model for persistent agentic sessions.



The July 2026 update introduces a redesigned layout with revised menus and navigation; a new Tasks tab allows users to monitor activities in progress; Copilot chat conversations also appear in an updated format.

Responses, references, and suggested actions are presented differently, and users who work with Copilot agents will notice updated labels that distinguish agent interactions from standard Copilot chats.

 The agent labelling change deserves specific attention: it establishes *agent interaction* as a visually distinct category in the Copilot UI, making it immediately legible to users whether they are conversing with the base model or delegating to an agent running autonomously on their behalf. This is a meaningful step in the trust-transparency layer — the same category of disclosure that Anthropic makes when Fable 5's safety classifier blocks a request and names the fallback.

The auto-installation of the M365 Copilot app on Windows commercial devices is the deployment-design story of the window. 

Microsoft is resuming automatic installation of the Microsoft 365 Copilot app on eligible Windows devices with commercial Microsoft 365 desktop apps between mid-June and mid-July 2026, unless administrators opt out through the Microsoft 365 Apps admin center; the move is not a Windows Update in the traditional sense; it is another example of Microsoft treating Copilot not as an optional assistant, but as a default layer of the Microsoft 365 experience.

 This deployment decision is itself a UX statement: by making Copilot an automatic presence on the commercial Windows desktop rather than an opt-in installation, Microsoft is committing to the position that agentic AI is a baseline workplace utility, not an advanced feature.

---

### Grok (xAI): Grok Build Session Reliability and the Trust-Signal Micro-Fixes

xAI's most interaction-design-significant work in this window continues to be the dense session-reliability engineering in **Grok Build** — unglamorous individually but critical in aggregate for making long-running multi-agent sessions trustworthy enough to delegate to without babysitting.



OIDC sessions with XAI_API_KEY present no longer lose refresh on idle; clicking a model in the dashboard /model dropdown no longer opens the wrong session; session cycling with Ctrl+[/] now switches from the session you are currently viewing; prompt history (Up/Ctrl+R) now shows the complete recent list instead of a scrambled partial one; authentication now correctly prefers the session method when both API key and cached token are present.

 Each of these represents a different class of trust failure in a concurrent multi-agent session. The wrong-session model-dropdown open is the most consequential: it means a developer who thought they were configuring one agent was silently configuring another — a subtle but serious trust-surface flaw in a tool that runs autonomous code. Fixing it means the session state visible on screen is the session state that actually exists.



Grok Build also adds a new "Keep text selection highlight" setting that keeps drag selections visible until dismissed; doubled lines after tab switches or focus changes in tmux or editor terminals are now healed; clipboard copy now only shows success when the pasteboard actually received the text via a trusted path.

 The clipboard confirmation fix is the most design-principled of the three: it eliminates a class of *silent success* — where the interface reported a copy had succeeded but the pasteboard had not received it. In an agentic coding session where a developer copies a key token, command, or credential, a false success signal is not a cosmetic bug but a trust-signal failure that can cascade into a broken workflow. 

xAI's `/goal` in Grok Build — a new long-running autonomous mode for handing off larger implementation tasks — continues active rollout

, directly competing with OpenAI's Goal Mode GA on the same terminal surface. Together, the reliability work and `/goal` mode represent the same architectural recognition: as the delegation horizon extends from minutes to hours, the session surface must be reliable enough that developers can trust the state they see between check-ins.

---

### Perplexity: Deep Research in Computer and the Citation-First Enterprise Strategy

Perplexity's most consequential active UX development in this window is the continued landing of **Deep Research in Computer** — and the increasingly clear differentiation strategy it represents against both Copilot and ChatGPT in the enterprise M365 surface.



Perplexity adds Deep Research in Computer, a new command panel, forking, improved inline confirmations, and enterprise controls like a Computer Analytics API and custom credit limits, making it easier to research, build artifacts, and manage usage; Deep Research is now available inside Computer.

Start with a complex research question, then keep working from the result by turning findings into a report, spreadsheet, deck, dashboard, website, or follow-up workflow in the same place.

 This shifts the UX from *research as a reading activity* to *research as the first step of an agentic production workflow* — collapsing the historically multi-tool process of research → synthesis → formatting → delivery into a single session with a single provenance chain.

The command panel is the discoverability surface that makes this capability accessible without syntax expertise. 

Instead of remembering commands or navigating between modes, users open the panel by typing `/` and quickly search across available modes and skills before starting a task; the panel includes built-in modes like Deep Research and Plan Mode, alongside all available skills from the user, their space, and their organisation, making it easier to find and use the right capability at the right time.

 This establishes a *capability-discovery-at-initiation* pattern that is distinct from both the model picker (which selects power) and the tool menu (which selects function): the `/` panel surfaces the full agentic capability space at the moment of task creation, reducing the cognitive cost of knowing what Computer can do.



Perplexity adds Computer inside Microsoft 365 apps, bringing AI workflows to Word, Excel, PowerPoint, Outlook, and Teams; it also adds usage analytics, a new context panel for live task tracking, and answers with sources and inline citations for traceable claims.

 The UX differentiation from Microsoft's native Copilot in the same surface is precise: every Computer output carries explicit source citations — a transparency layer that speaks directly to the audit and compliance requirements of the enterprise market Perplexity is contesting. 

A compact local model acts as the router for the hybrid inference orchestrator — classifying each subtask by data sensitivity and compute requirements before dispatching it; sensitive data (financial records, health files) stays on-device, and compute-heavy tasks go to frontier cloud models — no manual configuration required.

 The Windows arrival of the hybrid inference orchestrator this month lands Perplexity's most differentiated governance capability — explicit, user-visible data routing — in the same enterprise market that Microsoft's Tasks tab and Cowork GA are targeting simultaneously.

---

## The Bigger Picture: The Admin Intelligence Layer and the Browser-Native Agent

The 48 hours ending July 3, 2026 describe the moment the agentic AI industry's investment shifted from the agent itself to the *instrumentation layer around the agent* — the surfaces that make autonomous work observable, attributable, redirectable, and governable after it has been delegated. Anthropic's Enterprise Admin Analytics release is the most explicit statement of this shift: the new analytics dashboard does not make Claude more capable; it makes Claude's activity *legible* to the humans responsible for it, at the exact granularity — per-user, per-model, per-product, with pre-emptive spend alerts — that enterprise governance requires. The Claude in Chrome GA release and the Codex Mobile rollout make the same argument from the human side of the delegation: the background-persistent agent session with push notification re-engagement and the phone-as-supervisor model both solve the same design problem — *how does the human re-enter a session they did not watch?* — from different angles. Google's Interactions API GA answers the same question at the infrastructure layer: by declaring stateful, background-execution APIs as the mandatory home for all frontier agentic capabilities, Google is forcing every Gemini agent builder to design for the *interrupted session* as the default case rather than the edge case. Microsoft's Cowork GA with mobile push notifications for long-running tasks, and Perplexity's context panel for live task tracking in M365, apply the same logic to the enterprise productivity surface: if the agent is now running scheduled, multi-hour workflows inside Word and Excel, the human needs a dedicated monitoring view — not chat history — to understand what it did and why. And Grok Build's clipboard trust-path fix, however small, encodes the same conviction in a different register: in an era of always-on agents, every signal the interface emits about the state of the session is a trust claim, and false signals — silent successes, wrong-session states, scrambled histories — are not cosmetic bugs but failures of the human-agent contract. What the industry is building, one feature at a time, is not just more capable agents but a *governability layer* that matches the autonomy the agents already have.

---

## References

[1] Anthropic. (2026). *New analytics and cost controls are available for Claude Enterprise*. [https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)

[2] Releasebot. (2026). *Claude Code Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] Anthropic. (2026). *Get started with Claude in Chrome*. [https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)

[4] OpenAI. (2026). *ChatGPT Business Release Notes*. [https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes)

[5] OpenAI. (2026). *ChatGPT Enterprise & Edu Release Notes*. [https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes)

[6] OpenTools. (2026). *OpenAI Codex Can Now Control Your Mac Even When Locked*. [https://opentools.ai/news/openai-codex-locked-mac-control](https://opentools.ai/news/openai-codex-locked-mac-control)

[7] Google. (2026). *Interactions API: our primary interface for Gemini models and agents*. [https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/](https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/)

[8] Google. (2026). *Gemini Apps Release Updates & Improvements*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/)

[9] Gemini API. (2026). *Release notes | Gemini API*. [https://ai.google.dev/gemini-api/docs/changelog](https://ai.google.dev/gemini-api/docs/changelog)

[10] Neowin. (2026). *Here are all the new features added to Microsoft 365 Copilot in June 2026*. [https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/](https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/)

[11] WSU Insider. (2026). *Microsoft 365 Copilot receives interface updates in July 2026*. [https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/](https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/)

[12] Windows Forum. (2026). *Microsoft 365 Copilot App Auto-Install (June–July 2026): IT Opt-Out Guide*. [https://windowsforum.com/threads/microsoft-365-copilot-app-auto-install-june-july-2026-it-opt-out-guide.428844/](https://windowsforum.com/threads/microsoft-365-copilot-app-auto-install-june-july-2026-it-opt-out-guide.428844/)

[13] xAI. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[14] Releasebot. (2026). *xAI Release Notes — June/July 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] Perplexity. (2026). *Perplexity Changelog*. [https://www.perplexity.ai/changelog](https://www.perplexity.ai/changelog)

[16] Releasebot. (2026). *Perplexity Release Notes — June 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

---