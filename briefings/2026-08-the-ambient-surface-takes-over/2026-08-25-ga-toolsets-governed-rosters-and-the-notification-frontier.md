# UX Briefing: GA Toolsets, Governed Rosters, and the Notification Frontier

**August 25, 2026**

Good morning. The 48 hours ending August 25 are defined by a single escalating platform dynamic: every major AI product simultaneously crossing the threshold from "beta capability" to "production infrastructure" — and the governance, transparency, and human-control primitives scrambling to keep pace. **Claude/Anthropic** ships its most significant developer-platform GA event of the year: **computer use, browser use, the Skills API, and the Files API** all exit beta and land as generally available toolsets on the Claude Platform, with Skills API and Files API simultaneously landing on Microsoft Foundry — an architectural four-way GA that changes the operator control calculus for enterprise agentic deployments overnight. **ChatGPT/OpenAI** executes the heaviest model-transition moment of its August retirement arc: **OpenAI o3 retires tomorrow (August 26)** from ChatGPT, forcing a mass model-picker migration for every paid user with workflows built on o3, while **Codex adds Appshots** — a hotkey-invoked app-window-to-context capture that establishes a new pattern for ambient workspace grounding — and **Goal Mode reaches GA** across the Codex app, IDE extension, and CLI. **Google Gemini** enters a compound UI evolution moment: **Ask Gemini in Google Chat** begins its live August 26 rollout today, while Android Authority has spotted an in-flight app-level overhaul — **separate Pinned and Recents sections, a new Notifications hub, and chat filters** — that signals the app's information architecture is being redesigned for the growing volume of agentic outputs returning to the user. And **Microsoft Copilot** lands **multi-tenant agent management in public preview** in the M365 admin center — a trust-design event that gives MSPs and enterprise admins a single consolidated agent inventory, risk scores, and install/block controls across every tenant they govern, without requiring a separate administrator account in each.

---

## At a Glance: August 25 Highlights

Today's releases share a single structural signal: the industry is graduating its most consequential agentic capabilities from gated beta to production-grade GA — and the trust and governance layer is being built in real time, one control surface at a time.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Computer use, browser use, Skills API, and Files API all reach GA** — `computer_toolset_20260801` adds multi-action turns and a new browser use tool; Skills API lets teams upload/version reusable expertise for agents without separate hosting; Files API closes the loop on artifact handoff; all four now on Claude Platform and Skills API + Files API also on Microsoft Foundry; Grok Build changelog noted Vertex rollout coming soon; Claude Code adds mid-turn `/permissions` editing and auto-compact context behaviour. [1][2][3] |
| **ChatGPT** | **o3 retires August 26** — mass model-picker migration underway for paid users; **Codex Appshots** attaches a live app window to a thread via hotkey; **Goal Mode GA** across Codex app, IDE extension, and CLI; in-app browser annotations for styling feedback; locked computer use keeps Codex running after Mac screen locks; `codex mcp-server` command deprecated in favour of Codex app server. [4][5][6] |
| **Google Gemini** | **Ask Gemini in Google Chat begins live rollout today (August 26)** — unified Workspace command line replaces Chat side panel, keyboard shortcut access, sessions organised by topic; **Gemini app UI overhaul spotted in flight** — separate Pinned/Recents sections, Notifications hub (daily summary, scheduled actions, responses, service tips), chat filters, and option to hide status bar icon; Gemini Chat admin usage metrics now in Gemini reports dashboard. [7][8][9] |
| **Microsoft Copilot** | **Multi-tenant agent management lands in public preview** — consolidated agent inventory, install/block controls, risk and activity insights across connected tenants from a single M365 admin centre view; Copilot agents now support **multiple owners** for collaborative governance; Agent 365 agents set to act as A2A connected agents inside Copilot Chat targeting GA August 2026; Copilot Researcher adds model-and-mode picker (Auto, Model Council, GPT, Claude) inside the conversation. [10][11][12] |
| **Grok (xAI)** | **Grok Build hardening arc continues** — prompt caching for long conversations reduces repeated billing on growing transcripts; faster auto-mode approvals for read-only git commands and harmless file appends; plan previews and question card navigation improvements; model picker now updates status bar and /model menu instantly before first session prompt; Grok Bot enterprise waitlist actively expanding. [13][14][15] |
| **Perplexity** | **Brain: Agentic Memory as a Knowledge Wiki** — structured Markdown filesystem published August 19, 2026, formalising Brain's architecture as a traceable, self-improving offline-compiled knowledge graph that loads into Computer's sandbox before each task; Agent API prompt caching and `last_updated_filter` continue rolling; Sonar endpoint retirement September 27 passes its midpoint. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Four-Way GA and the Browser Use Breakthrough

Anthropic's most consequential platform event of the August cycle lands in this window: 

computer use, the Skills API, and the Files API are generally available on the Claude Platform today — and computer use adds a new browser use tool for agents that work in web applications, with all four working together to let teams build agents that operate software, apply expertise, and return finished files.



The browser use addition is the UX breakthrough worth isolating. 

The August release adds multi-action turns and introduces browser use, which reads page structure and targets fields or buttons directly rather than relying only on screen coordinates — a difference that matters in web-based tools where layouts change.

 This shifts the agentic interaction model from "pixel-coordinate guessing" to "semantic-structure understanding": the agent no longer needs to know where a button is drawn on screen, it needs to know what the button is — a fundamentally more robust and human-legible action model. For UX practitioners designing agentic workflows, this means the browser-use tool's action trace is now intelligible enough to audit: "clicked the Submit button in the Payment form" rather than "clicked at coordinate (412, 887)."

The Skills API GA is the second major trust-design event in this bundle. 

The Claude Skills API is a developer interface for uploading and versioning custom Skills so they run inside Claude's code execution sandbox — no separate hosting required; it became generally available on August 20, 2026; it is not a replacement for the Skills you already use — a user-facing Skill packages a reusable way of working, while the Skills API lets developers upload, version, and attach that same Skill to software or automated agents.

 The interaction design implication of Skills reaching GA is that the gap between "how an expert at your org does this task" and "how the agent does this task" can now be formally encoded, versioned, and governed — not as a prompt in a config file, but as deployable infrastructure with a release lifecycle. 

The Skills API and the Files API are also available through Microsoft Foundry, and the updated computer use and browser use tools are coming soon to Google Cloud's Vertex AI.

 The simultaneous Microsoft Foundry landing means that enterprise teams already deployed on Azure can access Skills and Files as first-class toolchain primitives without a separate Claude Platform account — a distribution reach that makes the GA more consequential than a single-platform release.

On the Claude Code surface, two mid-turn control improvements shipped in the same window deserve notice. 

`/permissions` can now be opened while Claude is working — rule changes apply to the rest of the current turn — and `/add-dir <path>` can now be used while Claude is working, with `/add-dir`, `/autocompact`, `/theme`, `/help`, `/config` and `/advisor` dialogs opening mid-turn in the fullscreen TUI.

 The ability to change permission rules while the agent is mid-execution is a meaningful human-control-handoff improvement: it allows the operator to narrow scope in response to what they observe the agent doing, rather than having to stop, reconfigure, and restart the session. This is the trust-design equivalent of a real-time confidence dial — available precisely when the agent is running and visible behaviour creates the impulse to adjust.

---

### ChatGPT / OpenAI: Appshots, Goal Mode GA, and the o3 Retirement Wall

OpenAI's most interaction-design-significant release in this window is not the model retirement — it is the arrival of **Codex Appshots**, a new ambient context capture primitive that changes how users ground long-running agentic tasks. 

Appshots in the Codex app on macOS let you attach an app window to a Codex thread with a hotkey, including a screenshot and available text, so Codex can understand what you are looking at without a long setup prompt.

 The UX pattern this establishes is significant: rather than the user describing their current context to the agent in natural language — a slow, lossy, and effortful translation — Appshots captures the literal visual state of the application the user is working in and injects it as structured context into the active thread. This shifts the human–agent grounding interaction from "tell me what you see" to "I can see what you see" — a reduction in the cost of task initiation that is likely to meaningfully change the moment at which users decide to delegate rather than do.

The companion agentic-workflow event is the general availability of **Goal Mode**. 

Goal Mode is generally available across the Codex app, IDE extension, and CLI, so users can define an outcome and success criteria and let Codex keep working toward it.

 Goal Mode is a temporal UX primitive: it shifts the interaction contract from "I will watch each step and approve" to "I will define the destination and check in when it matters." 

In-app browser annotations support more precise styling feedback for browser-based and frontend work, and locked computer use lets users keep Codex working remotely and securely after the Mac locks, subject to existing regional constraints.

 The locked computer use addition is the trust-design complement to Goal Mode: if the agent keeps working after the Mac screen locks, the user needs confidence that the scope of what it can do is bounded, and the regional constraint caveat signals that the governance of always-on agentic compute is still being worked out jurisdiction by jurisdiction.

The o3 retirement arrives tomorrow and is the most disruptive model-transition event in the window. 

OpenAI o3 will be retired from ChatGPT on August 26, 2026 following a 90-day sunset period.

 For the interaction-design practitioner community, the o3 retirement is a reminder that the human–agent interaction contract is model-specific: workflows, habits, and user expectations calibrated to o3's specific reasoning style and output characteristics cannot be automatically ported to a successor model, and the 90-day notice window — while substantial — is often shorter than the organisational cycle for revalidating agentic workflows in enterprise contexts. 

The `codex mcp-server` command is now deprecated — developers should use the Codex app server instead, and to use Codex from Claude Code, the Codex plugin for Claude Code should be used.

 The deprecation of `codex mcp-server` in favour of the Codex app server is a quiet but meaningful developer workflow change: it consolidates the MCP integration path and establishes the Codex plugin as the canonical bridge for users building cross-agent workflows between Claude Code and Codex.

---

### Google Gemini: Ask Gemini Goes Live and the Notification Architecture Arrives

Google's most consequential Workspace UX event begins rolling out today. 

Google Chat is the central hub for real-time collaboration in Workspace, and starting August 26, 2026, it becomes the place where you can bring the power of Gemini into your flow of teamwork, with the introduction of Ask Gemini in Google Chat, a unified command line for your work, powered by Workspace Intelligence.

Ask Gemini in Chat helps users navigate their day, stay on top of the flow of collaboration, find what they're looking for, and take action — including finding answers quickly by searching across Workspace data like Gmail, Drive, or Calendar, and creating content or drafting critical updates without leaving the conversation.

 The rollout timeline matters for practitioners: 

Rapid Release and Scheduled Release domains are on a gradual rollout of up to 15 days for feature visibility starting on August 26, 2026,

 meaning full organisational visibility won't arrive uniformly — a temporal UX consideration for IT teams managing the transition.

The second Google UX event emerging in this window is not a shipped feature but an in-progress app-level overhaul that Android Authority spotted on August 24. 

Gemini could soon get a new Notifications section, separate Pinned and Recents sections, and filters to make chats easier to find; Google is also working on a dedicated Customize section for Gemini Spark, where users can discover and manage Skills and Apps.

 The interaction-design significance of separating Pinned from Recents is that it acknowledges a structural shift in how Gemini is being used: as the app accumulates both long-running agentic threads and frequent ad-hoc queries, a flat chronological list stops being a usable navigation model. Pinned conversations are conceptually different from Recent ones — they are ongoing collaborative artefacts, not session history — and giving them separate visual real estate acknowledges that difference. 

A new setting could also let users hide Gemini's status bar icon, giving them more control over how the AI appears on their phone

 — a signal that Google is starting to treat ambient AI presence as something users should be able to modulate, not just accept as always-visible.

The Notifications hub is the temporal UX event to watch. 

In mid-August 2026, a new Notifications setting was added to the iOS version of the Gemini app, allowing users to toggle notifications ON or OFF for four items: Daily summary, Scheduled actions, Responses, and Service updates and tips — allowing for granular control over notifications that were previously sent automatically.

 The four-category notification taxonomy encodes an important distinction: "Responses" — notifications sent when Gemini replies to complex questions that take time to process — is the async agentic return pattern finally becoming a first-class UI concept. This is the Gemini app acknowledging, at the notification-settings level, that it now regularly performs work that does not complete within the user's attention span. The design verdict is that Google is building the async temporal UX layer that long-running agentic tasks require: a structured way for the agent to interrupt the user when the work is done, not whenever the platform feels like it.

---

### Microsoft Copilot: Multi-Tenant Agent Management and the Model Council

Microsoft's most trust-design-significant UX event in this window is the arrival of **multi-tenant agent management** in public preview. 

Now in public preview, multi-tenant agent management in the Microsoft 365 admin center enables administrators to view and manage agents across the tenants they govern from a single experience.

 The governance surface this creates is substantial: 

administrators can view a consolidated agent inventory, add agents, install or block agents across eligible tenants, review tenant-specific risk, and activity insights (Agent 365 license required), and use the tenant switcher to move directly into a connected tenant through delegated access without maintaining a separate administrator account in that tenant.

 For MSPs and enterprise IT teams governing dozens of Copilot-enabled customer tenants, this collapses what was a tab-by-tab, account-by-account audit process into a single governed console. The interaction design implication is structural: agent risk visibility and install/block authority are now available at the fleet level, not the individual tenant level — which is the governance granularity enterprise security teams have been asking for since Copilot agents began proliferating.

The companion governance event is the general availability of **multiple agent owners** for Microsoft 365 Copilot declarative agents. 

Microsoft 365 Copilot agents now support multiple owners, enabling collaborative management and reducing dependency on a single creator; this update, rolling out worldwide in August 2026, allows equal editing permissions for all owners, improved sharing controls, and organisation-wide agent publishing.

 The single-creator ownership model created a quiet but significant governance risk: agents built and deployed by one person became unmanageable if that person left, changed roles, or was unavailable. Multi-owner support is the operational-continuity fix that turns agent authorship from a single point of failure into a team responsibility. And inside the Researcher agent, 

Microsoft's support experience now shows Auto, Critique, Model Council, GPT, and Claude paths in the Copilot conversation — with Auto using GPT responses refined by Claude, Model Council combining GPT and Claude deep reasoning, and the GPT and Claude choices letting the user select one provider's deep-reasoning path directly.

 The in-conversation model picker is the trust-design choice that makes the multi-model orchestration legible to end users rather than hiding it: the user can see which reasoning path their task is taking, and choose accordingly.

---

### Grok (xAI): Build Hardening and the Persistent-Agent Expansion

xAI's most interaction-design-relevant developments in this window are concentrated in the **Grok Build hardening arc**, which continues at a dense cadence. 

Grok Build fixes chat history corruption, redirect loops in embedded previews, and several reliability issues across auth, wake turns, and language servers; it also improves prompt caching for long conversations, helping reduce repeated billing on growing transcripts.

 The prompt-caching improvement is a temporal UX fix: in a long agentic session where the conversation transcript grows significantly, repeatedly re-encoding the full history on each turn generates both latency and cost friction that competes with the developer's focus. Reducing redundant billing on growing transcripts is the same compounding-cost problem that Perplexity addressed at the Agent API preset level — here applied to the interactive TUI session.

The auto-mode approval improvements represent a meaningful shift in how Grok Build handles routine agentic actions. 

Grok Build ships faster auto-mode approvals, better plan previews and question card navigation; auto mode auto-approves more common read-only git commands and harmless file appends, and always-allow for bash commands lets users edit a free-form glob pattern instead of only word-prefix scopes.

 The design logic here is the same one governing every approval-gate system in this window: identifying the actions that are genuinely low-risk and removing the approval friction for those, so the human attention remaining in the approval queue is concentrated on the actions that actually warrant it. Glob-pattern bash allow-lists give developers a precision tool for specifying exactly which commands their agent should be trusted to run without confirmation. 

The model picker now updates the status bar and /model menu immediately, even before the first prompt creates a session.

 This is a perceptual trust signal: a UI that shows the model you selected before you start working, rather than after the first response arrives, reduces the ambiguity about which model is actually handling the task — a micro-moment of transparency that accumulates into confidence over repeated sessions.

---

### Perplexity: Brain as Architecture and the Agentic Memory Design Problem

Perplexity's most conceptually significant UX event in this window is not a changelog entry — it is an architectural clarification. 

On August 19, 2026, Perplexity published "Brain: Agentic Memory as a Knowledge Wiki" — a structured, traceable, self-improving Markdown filesystem, compiled offline and navigated on demand.

 This post formalises what Brain actually is at the system-design level, and the architecture it describes is the interaction-design answer to one of agentic AI's most persistent UX problems: every session starting from scratch. 

Brain builds what the company calls a context graph of completed agent work, logging actions, sessions, and corrections; overnight, a synthesis process converts those logs into reusable lessons stored in an LLM wiki that automatically loads into the agent sandbox on each new run.



The trust-design choices encoded in Brain's architecture are worth examining. 

Perplexity says "with Brain, Computer starts each task with full context of your projects, decisions, and sources instead of from scratch," and "every memory links back to the session, file, or source it came from with full transparency and control."

 The auditability claim — every memory linked back to its source — is the human-legibility primitive that distinguishes Brain from a black-box learning system: users can inspect not just what the agent remembers, but *why* it remembers it and *where* that memory came from. 

The distinction Brain draws between user memory and work memory is worth holding onto: most agent frameworks treat memory as personalization, while Brain treats it as a performance log.

 This is the more consequential design decision: an agent that remembers the user's preferences is building a profile; an agent that remembers what it did wrong last Tuesday and why is building a skill. The interaction design implication for practitioners is that the right mental model for Brain is not a contacts list — it is a structured handoff note that the agent writes to its future self before logging off.

On the Agent API surface, 

Agent API presets now use stable prompt cache keys automatically, allowing independent requests with the same preset to reuse the shared prompt prefix — system prompt and tool definitions.

 And 

Perplexity added shared workspaces with shared files, Personal Computer for Windows, a Model Council comparison mode, and the Kimi K3 model, per the vendor changelog dated August 4, 2026

 — completing Personal Computer's cross-platform arc by bringing the always-on agent to Windows, and adding a Model Council comparison mode that lets users see competing model outputs side-by-side before committing to one path.

---

## The Bigger Picture: GA Toolsets, Governed Rosters, and the Notification Frontier

The 48 hours ending August 25, 2026 mark the week that the AI industry's most consequential agentic capabilities stopped being experiments and started being infrastructure. Claude's four-way GA — computer use, browser use, Skills API, Files API — is not a feature launch; it is a platform declaration that agents operating software, navigating the web, applying reusable expertise, and returning finished files are now production-grade primitives subject to enterprise governance, not beta capabilities requiring a special header. Microsoft's multi-tenant agent management landing in public preview is the governance response at the other end of the stack: as agent rosters proliferate across tenants, the control surface for auditing, blocking, and owning those agents has to scale at the same rate. Codex Goal Mode reaching GA establishes the "define a destination and walk away" pattern as a first-class interaction contract rather than a power-user workaround. And Gemini's emerging Notifications architecture — daily summaries, scheduled action alerts, async response notifications — is the mobile UX layer finally acknowledging that agentic work doesn't complete within the human's attention window. What unifies all of these events is a single design reckoning: when agentic capabilities graduate from beta to production, every trust primitive that was deferred during the beta period — audit trails, multi-owner governance, async return signals, semantic-level action logs, cross-tenant control planes — has to graduate with them. The platforms navigating this moment well are not the ones shipping the most capable agents. They are the ones building the governance surfaces fast enough that enterprise security teams, end users, and regulators can see what the agents are doing, who authorised them to do it, and what they remembered from last time.

---

## References

[1] Claude by Anthropic. (2026). *Build production agents with computer use, the Skills API, and the Files API*. [https://claude.com/blog/computer-use-skills-api-files-api](https://claude.com/blog/computer-use-skills-api-files-api)

[2] Releasebot. (2026). *Claude Developer Platform Updates by Anthropic — August 2026*. [https://releasebot.io/updates/anthropic/claude-developer-platform](https://releasebot.io/updates/anthropic/claude-developer-platform)

[3] Releasebot. (2026). *Claude Code Updates by Anthropic — August 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[4] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] OpenAI Help Center. (2026). *ChatGPT Enterprise & Edu — Release Notes*. [https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes)

[6] ChatGPT Learn. (2026). *ChatGPT & Codex changelog*. [https://learn.chatgpt.com/docs/changelog](https://learn.chatgpt.com/docs/changelog)

[7] Google Workspace Updates. (2026). *Introducing Ask Gemini in Google Chat*. [https://workspaceupdates.googleblog.com/](https://workspaceupdates.googleblog.com/)

[8] Android Authority. (2026). *Gemini is working on a ton of useful UI changes: filters, notifications, and more*. [https://www.androidauthority.com/google-gemini-ui-update-chat-filters-notifications-3702443/](https://www.androidauthority.com/google-gemini-ui-update-chat-filters-notifications-3702443/)

[9] Jetstream Blog. (2026). *New iOS "Gemini" Notification Settings Added*. [https://jetstream.blog/en/ios-gemini-notification-settings/](https://jetstream.blog/en/ios-gemini-notification-settings/)

[10] Microsoft Learn — Partner Center. (2026). *August 2026 announcements*. [https://learn.microsoft.com/en-us/partner-center/announcements/2026-august](https://learn.microsoft.com/en-us/partner-center/announcements/2026-august)

[11] M365 Admin — Hands On Tek. (2026). *Public preview: Manage agents across multiple tenants from the Microsoft 365 admin center*. [https://m365admin.handsontek.net/public-preview-manage-agents-across-multiple-tenants-microsoft-365-admin-center/](https://m365admin.handsontek.net/public-preview-manage-agents-across-multiple-tenants-microsoft-365-admin-center/)

[12] A Guide to Cloud & AI. (2026). *What's New in Microsoft 365 Copilot: August 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-august-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-august-2026-updates/)

[13] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[14] xAI. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[15] Releasebot. (2026). *xAI Release Notes — August 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[16] Perplexity AI. (2026). *Brain: Agentic Memory as a Knowledge Wiki*. [https://www.perplexity.ai/hub/blog](https://www.perplexity.ai/hub/blog)

[17] Perplexity AI. (2026). *Changelog — Perplexity Docs*. [https://docs.perplexity.ai/docs/resources/changelog](https://docs.perplexity.ai/docs/resources/changelog)

[18] AI Weekly. (2026). *Perplexity Brain Adds Self-Improving Work Memory to Its Agent*. [https://aiweekly.co/alerts/perplexity-brain-adds-self-improving-work-memory-to-its-agent](https://aiweekly.co/alerts/perplexity-brain-adds-self-improving-work-memory-to-its-agent)