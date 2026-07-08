# UX Briefing: The Cross-Device Agent and the Asynchronous Delegation Moment

**July 08, 2026**

Good morning. The 48 hours ending July 8 are defined by the industry's decisive shift to **asynchronous, cross-device agent delegation** — the moment when persistent AI agents stopped requiring a device to be online and started running in the cloud, sending approval requests to the human's phone rather than waiting for a keyboard. **Claude/Anthropic** leads the window with two simultaneous and structurally significant moves: **Claude Cowork expands to web and mobile**, breaking the desktop-only constraint and enabling scheduled tasks to run with no device online, while **Claude Code and Claude Cowork launch in public beta in Claude for Government Desktop**, shipping the full agentic stack inside a FedRAMP High authorized environment with tamper-evident audit logs, department-level spending controls, and hash-chained administrative accountability. Simultaneously, Anthropic's **Fable 5 access restriction** — moving the model to credits-only after user backlash forced a deadline extension to July 12 — creates a live, contested UI moment around how subscription transitions should be communicated for frontier-tier capabilities. **ChatGPT/OpenAI** deepens its own cross-device delegation story with **Codex task management added directly inside conversation threads** and the continued active landing of the **Migrate to Codex** onboarding flow that imports Claude Code and Claude Cowork setups — a competitive UX signal as pointed as any feature announcement. **Microsoft Copilot** delivers its most OS-layer-significant trust-surface change of the window: **long-running agent task status icons now live in the Windows taskbar**, making Copilot agent progress visible from the OS shell without requiring the app to be open — the clearest expression yet of Microsoft's "agents as taskbar citizens" architecture. **Grok (xAI)** continues active rollout of **Grok 4.1 Fast now enabled for agent tools** at a 50%-reduced price, alongside the **agent tool pricing drop** to $5 per 1,000 successful calls — a cost-floor signal with direct implications for how builders design multi-step agentic call chains. And **Perplexity** continues the active landing of **Deep Research in Computer** with the `/` command panel, thread forking, and the **hybrid inference orchestrator's Windows arrival** this month, routing sensitive data on-device and compute-heavy tasks to cloud with no manual configuration.

---

## At a Glance: July 8 Highlights

The releases this window converge on a single structural argument: the agentic session is no longer tied to a device — it runs in the cloud, persists across surfaces, delivers approval requests to wherever the human happens to be, and is now beginning to surface its progress indicators at the OS shell level, not just inside the AI app.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Cowork expands to web and mobile** — cross-device session persistence, cloud-based background execution, mobile approval prompts, and shared Chat+Cowork home; **Claude for Government Desktop** launches in public beta with FedRAMP High, tamper-evident audit logs, and department-level spend governance; **Fable 5 access transition** extended to July 12 after backlash, moving flagship model to credits-only. [1][2][3] |
| **ChatGPT** | **Codex task management added directly inside conversations** — create, search, open, fork, and manage Codex tasks from a thread; **Migrate to Codex flows** import Claude Code and Claude Cowork setups during onboarding; **Codex Remote GA on Windows** enables phone-to-PC agent control via QR-paired authentication. [4][5] |
| **Google Gemini** | **Gemini in Chrome begins rolling out** on Windows and Mac for AI Pro/Ultra subscribers in the US — page-level AI assistant connecting to Calendar, Keep, and Gmail; **Gemini Enterprise MCP connector** goes live (off by default, admin-enabled) for custom internal data and tools; **Agent identity page** surfaces SPIFFE IDs for admin trust verification. [6][7][8] |
| **Microsoft Copilot** | **Agent task status icons arrive in the Windows taskbar** — long-running agent progress visible from the OS shell without opening the app; **scheduled agent prompts** and **Copilot Notebook exports** to PowerPoint, Word, and Excel now rolling out; **New Copilot toggle** removal on track for July 15, locking the redesign as default. [9][10][11] |
| **Grok (xAI)** | **Grok 4.1 Fast now available with agent tools** via the xAI API, with agent tool pricing dropping up to 50% to a cap of $5 per 1,000 successful calls; **Grok Build** receives dense session-reliability fixes including OIDC idle refresh, session cycling, and model-dropdown routing corrections; **Grok 4.5** confirmed in private beta with SpaceX and Tesla. [12][13] |
| **Perplexity** | **Deep Research in Computer** with the `/` command panel, thread forking, and inline confirmations continues active landing; **hybrid inference orchestrator** arrives on Windows this month with automatic on-device routing for sensitive data; **Computer in M365** continues rollout across Word, Excel, PowerPoint, Outlook, and Teams with inline citations. [14][15] |

---

## Product Highlights

### Claude / Anthropic: Cowork Goes Cross-Device, Government Gets the Full Agentic Stack, and Fable 5's Subscription Cliff

Anthropic's most consequential UX shift of this window is the breaking of **Claude Cowork**'s single-device constraint — and the trust-design architecture that had to be built to make cross-device delegation feel safe rather than opaque.



Cowork is where you hand Claude a task, and it works across files, calendar, email, messaging app, the web, and the other tools you connect until the job is done. AI agents made their name writing code. But when Anthropic looked at how people actually use Claude Cowork, more than 90% of it wasn't software development — most of it was everyday knowledge work, with business operations and content creation as the largest categories.

 This data point reframes the product's identity: Cowork is not a coding tool that civilians can access — it is a general knowledge-work delegation surface that happens to share infrastructure with Claude Code.



Claude Cowork is now available on web and mobile in addition to desktop, rolling out over the next several weeks starting with the Max plan. Cowork runs sessions remotely in beta, so sessions and files are saved to the user's Claude account and go where they go, on any device. Work continues when the laptop closes, and scheduled tasks run with no device online. Chat and Cowork also share one home now, with one place for projects and artifacts across both.

 The trust-design detail that matters most here is how Anthropic handles the human-in-the-loop requirement across devices: 

the "human in the loop" goes mobile too — when Claude hits a point where only a person can make the call, the agent asks via smartphone, and nothing gets sent without the user reviewing and approving it first.

 This establishes a new *mobile-approval gate* interaction pattern: the agent delegates downward in task complexity but escalates upward to the human's phone for consequential decisions, regardless of which device initiated the session.

The second major Anthropic UX event of the window is the arrival of **Claude for Government Desktop** in public beta — which is less a product launch than the articulation of what a fully auditable, governable agentic deployment looks like when the customer is a regulated institution. 

Claude Code and Claude Cowork are now available in public beta in Claude for Government Desktop, built on the same application commercial customers use and delivered through a FedRAMP High authorized environment.

The expanded experience comes with additional governance capabilities: administrators can set configuration defaults and allocate and control spending across departments, while security teams and authorizing officials get tamper-evident audit logs and documentation that supports the agency ATO process.

 The UX significance is structural: every interaction-design decision Anthropic made for Cowork — the mobile approval gate, the task-delegation model, the background execution — is now packaged inside a compliance envelope that public-sector teams can procure, ATO, and govern without building their own audit infrastructure. This is the most complete picture of what "enterprise-ready agentic UX" actually requires: not just capability, but provenance, accountability, and budget control at every delegation point.

The third story in this window is the live, contested UI moment created by **Fable 5's subscription transition**. 

Following backlash online, Anthropic extended Fable 5 access to existing Claude subscribers until July 12 — unlike the prior suspension, this wasn't on orders of the US government but Anthropic's own decision. Instead of regular Claude subscriptions, Fable 5 will require users to switch to a credit-based payment system.

 The extension itself is a trust-surface event: it reveals that Anthropic read user sentiment as sufficiently negative to delay a pricing-gate transition by several days, suggesting the original communication design for the capability downgrade was insufficient. The interaction design lesson is that moving a frontier model from *subscription-included* to *credits-required* is not a pricing decision — it is an experience-layer decision that requires its own notification architecture, grace period, and explanation surface.

---

### ChatGPT / OpenAI: Task Management Inside Threads, Migrate to Codex, and the Cross-Device Delegation Architecture

OpenAI's most interaction-design-significant additions in this window cluster around the maturing of Codex as a **cross-device, thread-native delegation surface** — closing the UX gap between starting a coding task and managing it wherever the user happens to be.



The July changelog adds support for creating, searching, opening, forking, and managing Codex tasks directly from a conversation, along with filters for staged, unstaged, branch, and last-turn changes, and the ability to add selected transcript text directly to the composer.

 This shift from *Codex-as-separate-app* to *Codex-as-thread-native-task-surface* is the interaction pattern that matters most: a user no longer needs to leave a conversation to inspect the state of a running agentic task — the task management surface lives inside the same thread where the intent was expressed. This collapses the cognitive overhead of switching between "what I asked" and "what the agent is doing."

The most strategically pointed UX addition of the window is the **Migrate to Codex** onboarding flow. 

Codex now adds Migrate to Codex flows for importing supported setup from Claude Code and Claude Cowork, including during onboarding, along with a revamped plugins screen with separate tabs, marketplace and category filters, keyboard navigation, and clearer install actions.

 Positioning this migration path inside the onboarding flow — not buried in settings — is a deliberate UX choice: it frames Codex as the destination for users who are already Claude Code or Cowork users, and lowers the switching friction at exactly the moment Anthropic is transitioning Fable 5 to credits-only. The timing is not coincidental.

On the cross-device front, 

Remote Control now supports Windows devices — users can start Codex work on a Windows device from ChatGPT on iOS or Android, or from a Mac running Codex, and check progress remotely.

Codex also adds usage limits and credit details to the task menu, and improves the task list with consistent task terminology, clearer delegated task titles, and a "Needs input" status indicator.

 The "Needs input" status is the interaction-design detail with the most UX weight: it surfaces the agent's blocked state as a named, visible condition rather than as silence — giving the human a clear signal that their attention is required without requiring them to open the full app to understand why.

---

### Google Gemini: Gemini in Chrome, Enterprise MCP, and the Agent Identity Layer

Google's most structurally significant UX development in this window is the launch of **Gemini in Chrome** — not as a browser extension but as a native, page-level AI assistant with Google app connectivity — alongside the opening of a meaningful enterprise trust surface in Gemini Enterprise: the ability to view an agent's verified identity.



Gemini in Chrome is starting to roll out on Windows and macOS devices to Google AI Pro or Ultra subscribers in the US who have their Chrome language set to English. The experience is not available to Google Workspace business and education plans. Gemini in Chrome helps users make the most of the web — instantly getting key takeaways and simple explanations for complex subjects, helping them do more and get assistance right on the page they're browsing.

It lets users summarize long articles, ask specific questions, and get detailed explanations without having to switch apps. Beyond answering questions, it acts as a versatile productivity tool that connects with Google apps like Calendar, Keep, and Gmail to help complete tasks quickly. With Personal Intelligence, if users choose to connect apps like Gmail and Google Photos, this context-aware browsing assistant can provide tailored responses based on their unique interests.

 This establishes a new *ambient browsing assistant* interaction pattern — Gemini is no longer something the user navigates to, but something that is already present on whatever page they are reading, with the option to escalate into connected-app action.

On the enterprise trust side, 

users can now connect custom Model Context Protocol (MCP) servers with Gemini Enterprise to securely access company private data, custom internal tools, and MCP-compliant third-party systems — though the feature is turned off by default and an Organization Policy Administrator must remove the organization constraint to enable it.

 This *default-off, admin-explicit* design pattern for MCP server connectivity is the trust-design decision that distinguishes responsible enterprise agentic deployment from permissive alternatives. Equally significant is the agent identity surface: 

as a Gemini Enterprise administrator, admins can now view an agent's identity on the Agent details page, typically the agent's SPIFFE ID. This feature is in Public Preview. If the SPIFFE ID is not published by the publisher, the Agent Registry resource ID is displayed as a fallback.

 The UX implication is a new *agent identity disclosure layer* — the first time a major enterprise AI platform surfaces a cryptographically verifiable agent identity to an administrator's console, making the question "which agent did this?" answerable without relying solely on audit log text.

---

### Microsoft Copilot: The Taskbar Agent, the July 15 Redesign Lock, and the OS-Layer Trust Surface

Microsoft's most design-consequential move in this window is the arrival of **long-running agent task status icons in the Windows taskbar** — the moment Copilot's agentic monitoring capability breaks out of the app and into the operating system's shell layer.



Long-running agents now display task status icons and progress indicators in the Windows taskbar. Previously, users had to open the Microsoft 365 Copilot app to monitor these workflows.

This update provides real-time visibility and quick access to task states, improving user awareness and reducing app switching. The change enhances productivity by allowing users to track workflow progress at a glance, minimizing interruptions and improving task management.

 The UX significance is architectural: this is not a new Copilot feature — it is a reclassification of AI agents as *OS-level processes with status representation*, equivalent in treatment to a file download or a software update. 

This is a meaningful shift because it moves AI from a side feature into the operating system's workflow layer, where users can launch, monitor, and return to long-running tasks without losing context — and it signals that Microsoft is trying to make AI feel more selective and useful, rather than scattered across every corner of Windows.



The **July 15 redesign lock** is the second interaction-design milestone in this window. 

The new Copilot experience has been available via a "New Copilot" toggle in the top right of the app, letting users switch between the current and updated experience. On July 15 for standard release, the toggle will be removed and the updated experience will become the default without the option to switch back.

 This is the interaction design moment when the Tasks tab — Microsoft's primary agentic monitoring surface — becomes the *only* Copilot experience for standard release users, not an opt-in. The toggle removal is itself a trust-surface event: it signals that Microsoft considers the new agent-monitoring architecture stable enough to be the default for the entire commercial user base. 

The agents section becomes a simpler flyout — hovering shows pinned and recent agents, or jumps straight to Agent Store and Agent Builder — while a brand-new Tasks tab opens a consolidated view of long-running Copilot activity, including scheduled chats and agent activity, making autonomous Copilot tasks easy to track.



---

### Grok (xAI): Agent Tool Pricing Drop, Grok Build Reliability, and the Agentic Cost Floor

xAI's most interaction-design-relevant moves in this window are focused on the economics and reliability of agentic calling — two factors that directly shape how builders design multi-step agent workflows.



Grok 4.1 Fast models are now available with agent tools, and the price of agent tools drops by up to 50% to no more than $5 per 1,000 successful calls.

 The UX implication of this pricing drop is structural: when agent tool calls are expensive, builders design workflows that minimise the number of tool invocations — which often means fewer intermediate checkpoints, less verification, and less transparency for the human delegating the task. A 50% reduction in the cost floor changes the calculus: builders can now afford to add more confirmation steps, more intermediate verification calls, and more explicit human-check-in points without blowing their unit economics. This is a cost structure that actively enables better trust-design in agentic workflows.



xAI's latest Grok Build updates continue active reliability work. Among them, xAI launches Voice Agent Builder in beta — a no-code platform for creating production voice agents on Grok Voice in minutes, bundling telephony, knowledge retrieval, tools, guardrails, MCPs, observability, voice cloning, SIP, and call review in one place.

 On the Grok Build session-reliability front, the changelog continues its dense sequence of interaction-level fixes: 

OIDC sessions with XAI_API_KEY present no longer lose refresh on idle, model switches no longer leave the prompt queue stuck after a reconnect, and prompt history now shows the complete recent list instead of a scrambled partial one.

 Each of these fixes extends the *trustable delegation horizon* — the length of a session over which a developer can hand off work to `/goal` mode and trust that the session state accurately reflects what they left. 

Elon Musk confirmed on June 28 that Grok 4.5 is running in private beta with teams at SpaceX and Tesla, built on a fresh V9 foundation — but he didn't give a public release date, and no broader rollout plan has been announced.



---

### Perplexity: The Windows Orchestrator Arrival, M365 Inline Citations, and the Data-Residency UX

Perplexity's most consequential active UX development this window is the Windows arrival of the **hybrid inference orchestrator** — which, in the context of Perplexity Computer landing inside M365 apps, creates the most differentiated data-governance UX story in any AI product shipping this month.



Perplexity adds Deep Research in Computer, a new command panel, forking, improved inline confirmations, and enterprise controls like a Computer Analytics API and custom credit limits, making it easier to research, build artifacts, and manage usage. Deep Research is now available inside Computer.

 The command panel is the discoverability architecture that makes the full capability legible: 

instead of remembering commands or navigating between modes, users open the panel by typing `/` and quickly search across available modes and skills before starting a task. The panel includes built-in modes like Deep Research and Plan Mode, alongside all available skills from the user, their space, and their organisation.

Perplexity adds Computer inside Microsoft 365 apps, bringing AI workflows to Word, Excel, PowerPoint, Outlook, and Teams, and adds usage analytics, a new context panel for live task tracking, and answers with sources and inline citations for traceable claims.

 The inline citations in the M365 surface are the trust-design differentiator: every Computer output inside a Word or Excel file carries explicit source attribution, giving compliance teams a verifiable provenance chain for AI-generated content — a meaningful contrast to native Copilot outputs, which carry watermarks at the artifact level but not inline citations at the claim level.

The governance story closes with the Windows arrival of the orchestrator. 

A compact local model acts as the router — classifying each subtask by data sensitivity and compute requirements before dispatching it. Sensitive data (financial records, health files) stays on-device; compute-heavy tasks go to frontier cloud models — no manual configuration required.

The local model decides when sensitive data should also be kept locally, and the system is designed to ask for user permission before sending sensitive tasks to the cloud. That design addresses a specific concern enterprises have about agentic AI: data governance — knowing where data goes and who controls that decision.

 The UX implication is a *permission-gate-at-the-task-level* architecture: rather than a blanket policy set at onboarding, the agent makes and surfaces data-routing decisions at the moment of task execution — which is both more precise and more legible than org-level toggle controls.

---

## The Bigger Picture: The Cross-Device Agent and the Asynchronous Delegation Moment

The 48 hours ending July 8, 2026 mark the moment when the industry stopped debating whether persistent AI agents are the future and started solving the next, harder problem: *what does the UX of a delegated, cross-device, always-running agent actually need to look like for the human to remain in control without remaining at their desk?* Claude Cowork's expansion to web and mobile is the clearest statement of the challenge: the session runs in the cloud, the task executes while the laptop is closed, the agent asks for approval on the user's phone, and the output appears wherever the user opens Claude next — a genuinely cross-device delegation loop that requires a mobile-approval-gate architecture, a cross-surface session model, and a unified home for Chat and Cowork artifacts to work as a coherent experience rather than a collection of disconnected surfaces. Microsoft's taskbar agent status icons encode the same insight from the OS layer: the agent's progress should be visible to the human without requiring the human to open an app, because the whole premise of a long-running agent is that the human has gone off to do something else. OpenAI's "Needs input" task status and its thread-native Codex task management answer the same question from the conversation layer: the agent's blocked state should be a named, visible condition in the same surface where the intent was expressed. Perplexity's task-level data-routing decisions and Gemini Enterprise's SPIFFE ID agent identity page answer it from the governance layer: every delegation event needs a verifiable record of what the agent did, what data it touched, and which entity executed the action. The Fable 5 subscription-cliff backlash — and Anthropic's same-day extension of the deadline — is the live UX failure case that the rest of the window is working to prevent: when a consequential capability change (frontier model moving to credits-only) lacks its own notification architecture, grace period, and in-product disclosure surface, users experience it as a removal rather than a transition. The industry is learning, one cross-device session and one taskbar icon and one mobile approval gate at a time, that asynchronous delegation is only trustworthy when the transparency infrastructure is as persistent as the agent itself.

---

## References

[1] Claude by Anthropic. (2026). *Claude Cowork on web and mobile: hand off work anywhere*. [https://claude.com/blog/cowork-web-mobile](https://claude.com/blog/cowork-web-mobile)

[2] Claude by Anthropic. (2026). *Bringing Claude Code and Claude Cowork to government*. [https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government)

[3] Android Authority. (2026). *Fable 5's second act on Claude ends today, unless you're willing to pay more*. [https://www.androidauthority.com/anthropic-claude-fable-5-credits-usage-july-3684840/](https://www.androidauthority.com/anthropic-claude-fable-5-credits-usage-july-3684840/)

[4] OpenAI Developers. (2026). *Changelog — Codex*. [https://developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

[5] Releasebot. (2026). *Codex Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/codex](https://releasebot.io/updates/openai/codex)

[6] Gemini Apps. (2026). *Gemini Apps Release Updates & Improvements*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/)

[7] Google Cloud Documentation. (2026). *Gemini Enterprise Release Notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[8] Chrome for Developers. (2026). *15 updates from Google I/O 2026: Powering the agentic web*. [https://developer.chrome.com/blog/chrome-at-io26](https://developer.chrome.com/blog/chrome-at-io26)

[9] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[10] SuperSimple365. (2026). *What's new in Microsoft 365 and Copilot? June 2026*. [https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/](https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/)

[11] Releasebot. (2026). *Microsoft Release Notes — July 2026*. [https://releasebot.io/updates/microsoft](https://releasebot.io/updates/microsoft)

[12] xAI Docs. (2026). *Release Notes — SpaceXAI*. [https://docs.x.ai/developers/release-notes](https://docs.x.ai/developers/release-notes)

[13] Grok Build Changelog. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[14] Perplexity. (2026). *Perplexity Changelog*. [https://www.perplexity.ai/changelog](https://www.perplexity.ai/changelog)

[15] MarkTechPost. (2026). *Perplexity AI Introduces Hybrid Local-Server Inference Orchestrator for Personal Computer*. [https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/](https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/)

---