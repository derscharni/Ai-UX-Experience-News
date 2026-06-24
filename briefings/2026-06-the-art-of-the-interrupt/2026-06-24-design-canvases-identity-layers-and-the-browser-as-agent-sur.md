# UX Briefing: Design Canvases, Identity Layers, and the Browser as Agent Surface

**June 24, 2026**

Good morning. The last 48 hours resolve into four interlocking design fronts. **Claude Design** shipped a major June 17 overhaul that turns the conversational canvas into a brand-governed, two-way workspace: imported design systems, direct WYSIWYG canvas editing, and a new `/design-sync` command that creates a live bidirectional bridge between design and code for the first time. **ChatGPT/Codex** continues to refine the long-running task surface with improved subagent progress visibility, per-host personality settings, and a Slack connector that promotes ChatGPT Enterprise from a chat tool to an action-taking workspace agent. **Google Gemini** is this week's most consequential distribution event: **Gemini in Chrome with auto browse** begins rolling out to Android this week — the first time that the browser itself, on the world's dominant mobile OS, becomes a native agentic execution surface, with confirmation gates before sensitive actions and integration into **Gemini Spark** on desktop for a continuous cloud-plus-browser delegation loop. And **Microsoft Copilot Studio** deepens its agent identity story through **Entra Agent ID** auto-provisioning, with each new Copilot Studio agent receiving a unique Microsoft Entra identity scoped to its connector permissions, Conditional Access policies, and DLP governance — closing the shared-service-account attribution gap that has haunted enterprise multi-agent deployments.

---

## At a Glance: June 24 Highlights

This week's releases are unified by a single maturing conviction: the design surface, the browser, and the identity layer are no longer separate concerns — they are the new frontier of agent governance and experience design, each in the process of becoming accountable infrastructure rather than user-facing novelty.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Design** receives its major June 17 overhaul with importable design systems, direct WYSIWYG canvas editing, two-way `/design-sync` with Claude Code, a new sidebar home in the desktop app, expanded tool connectors (Adobe, Canva, Vercel, Miro, and more), and an admin role that can lock the approved design system for brand governance across the enterprise. [1][2][3] |
| **ChatGPT** | Codex ships improved progress visibility for subagents, tasks, and worktree creation, per-host personality settings, forked-conversation links back to their original thread, and improved composer autocomplete; ChatGPT Enterprise adds Slack connector **actions** — not just search, but joining channels, creating reminders, uploading files, and updating profiles — with admin-managed Action control. [4][5][6] |
| **Google Gemini** | **Gemini in Chrome with auto browse** begins rolling out to Android in late June for US AI Pro/Ultra subscribers, bringing Gemini 3.1-powered multi-step task automation, confirmation gates on sensitive actions, and Google app integration (Calendar, Keep, Gmail) directly into the browser toolbar; desktop auto browse is confirmed to integrate with **Gemini Spark** in coming months. [7][8][9] |
| **Microsoft Copilot** | **Copilot Studio** auto-provisions a **Microsoft Entra Agent ID** for every new agent, scoping connector permissions, Conditional Access policies, and DLP governance to individual agent identities instead of shared service principals; audit and sign-in logs attribute every action to the specific agent identity, not a generic app registration. [10][11][12] |
| **Grok (xAI)** | xAI's most recent Codex/tool release window is largely consolidated from prior weeks; the cumulative usage counter and the Grok for Microsoft Word add-in remain the primary active UX stories from June 18 onward; Grok models expand to Databricks Agent Bricks with zero-data-retention guarantees for enterprise agentic pipelines. [13][14] |
| **Perplexity** | The **Deep Research in Computer** integration (June 19) continues maturing with the new `/`-triggered **command panel** unifying modes and skills discovery, forking for mid-flight research branching, and enterprise-grade Computer Analytics API and custom credit limits; the hybrid local-cloud inference orchestrator announced at Computex remains on track for July 2026. [15][16][17] |

---

## Product Highlights

### Claude / Anthropic: The Design Canvas Becomes Brand-Governed Infrastructure

The most consequential Anthropic interface release of the past 48 hours is not a change to Claude Code or the API — it is the June 17 overhaul of **Claude Design**, which moves the product from a rapid prototyping toy into a brand-governed, production-adjacent workspace. 

Claude Design now sticks to your design system across projects, works fluidly with Claude Code, lets you edit directly on the canvas, and connects to more tools you already use, with a new home in the sidebar on the Claude desktop app.

 The shift matters precisely because the prior version's failure mode was well-documented: 

AI-generated screens used approximated colors, invented component names, and spacing that matched no token in the real system, meaning the first implementation session corrected drift rather than built features.



The June update addresses the root cause directly with importable design systems. 

Anthropic rebuilt the design system import to give more flexibility and precision: users can bring in one or several design systems from a GitHub repo, design files, or raw uploads, and Claude builds with those components, checking its output against the design system and making corrections before the user sees it.

 The **`/design-sync`** command is the structural innovation: 

the command runs inside Claude Code and has two directions — pulling imports the local codebase's design system into Claude Design so every generated screen uses real components; pushing, after implementing a design in code, sends the current state back into Claude Design, keeping the canvas in sync with what has actually been built.

 This transforms the handoff from a one-way throw into a live sync loop, eliminating the "translate to code, hope it matches" gap that has made every prior AI design tool production-adjacent but never production-ready.

The trust and governance layer is where the enterprise design story sharpens. 

A new admin role can approve one standard design system and lock down edits, so work always matches company guidelines.

Claude Design is in beta on Claude Pro, Max, Team, and Enterprise plans; it's turned off by default for Enterprise users, and work is shareable only within the organisation.

 The UX implication is that Anthropic is not positioning Claude Design as a replacement for design professionals but as the enforcement layer for the systems those designers already created — making the design governance problem identical in structure to the permission-policy problem Claude Code has been solving: the agent operates only within the envelope the organisation has explicitly defined.

---

### Google Gemini: The Browser Becomes an Agentic Execution Surface

Google's most UX-consequential event of this window is not a Gemini app update — it is a browser update: **Gemini in Chrome with auto browse** is beginning its Android rollout this week, and with it, the browser itself becomes a native agent execution surface for the first time on the world's largest mobile OS. 

Chrome for Android is introducing Gemini-powered features to help users summarise articles, manage tasks, and customise images directly from the browser, including the new auto browse tool to automate errands like booking parking or updating orders, with built-in security to confirm sensitive actions — arriving in late June for US users on Android 12 or higher with at least 4GB of RAM.



The trust design of auto browse is deliberate and consequential. 

Auto browse is designed to ask for confirmation before completing sensitive tasks, like making purchases or posting on social media, and the same security protections that defend against prompt injection on desktop apply.

 This is a meaningfully different interaction contract from Gemini Spark's always-on cloud delegation: auto browse is *reactive* (user-initiated, per task) rather than proactive, and its confirmation gate is the primary mechanism keeping human intent in the loop on consequential actions. The desktop integration announced for the coming months raises the design stakes further: 

on desktop, Google will be integrating auto browse with Gemini Spark, so that the 24/7 personal AI agent can take actions in the browser on behalf of the user.

 This proposed Spark-plus-auto-browse combination is the most ambitious ambient UX arc in the current product landscape — a background cloud agent that can not only manage files and emails but now execute multi-step browser workflows while the user is away from their screen entirely.

The Antigravity CLI transition, which completed its hard cutover on June 18, is the parallel developer-side architecture story. 

Antigravity CLI orchestrates multiple agents for complex tasks in the background, letting users run large-scale refactors or research several topics without locking up their terminal session, and it shares the same agent harness as Antigravity 2.0, ensuring that all future improvements to core agents are automatically applied wherever it is used.

 The UX significance is unified state: a developer who delegates to the Antigravity CLI and a user whose Spark agent takes browser actions are now operating on the same underlying harness, meaning Anthropic-style subagent governance improvements will propagate automatically to both surfaces.

---

### Microsoft Copilot: Entra Agent ID and the Per-Agent Identity Primitive

Microsoft's most structurally important UX development of the week arrives almost entirely beneath the visible interface — but it is the trust primitive that makes everything built on top of Copilot Studio auditable at the depth enterprise compliance teams require. 

Copilot Studio now offers in preview the ability to automatically create Microsoft Entra agent identities for each agent, to scope connector permissions, Conditional Access policies, and DLP governance to individual agents.



The interaction design significance is most visible in what **Entra Agent ID** replaces. 

Some agents created in Microsoft Copilot Studio previously authenticated using platform-managed service principals, and these agents could have been created before Copilot Studio began automatically creating agent identities for all new agents, which happened on March 18, 2026.

 The governance gap that shared service principals created — multiple agents sharing one credential, making audit trails ambiguous — is now closed for every new agent by default. 

Audit and sign-in logs attribute agent actions and the resources they access to the specific agent identity, not a generic app registration, making investigation and attribution straightforward.

When a maker publishes an agent, Copilot Studio attaches API permissions to the agent's Entra Agent ID for each Power Platform connector the agent is configured to use, letting Microsoft Entra ID and Microsoft 365 admins see which connectors an agent can call without leaving the Microsoft Entra admin center.



The governance layer is layerable in ways that matter for real enterprise deployment. 

Because the scopes are first-class API permissions on the agent's Entra Agent ID, admins can target them with Microsoft Entra Conditional Access policies, including requiring network location, device compliance, or risk-based conditions before tokens are issued for a specific connector resource.

 This is the Microsoft answer to the same attribution problem Google solved with SPIFFE in Gemini Enterprise last week: every delegated action is now traceable to a unique, scoped credential, and that credential can be subject to the same policy infrastructure that governs human identities. The practical UX payoff for admins is a coherent answer to the question that has haunted every multi-agent enterprise deployment: *which agent took that action, and what was it authorised to do?*

---

### ChatGPT / OpenAI: Slack Actions and the Workspace Agent as Task Executor

OpenAI's most meaningful UX development of the 48-hour window is the promotion of Codex/ChatGPT Enterprise from a *search-in-Slack* surface to an *action-taking* surface. 

ChatGPT Enterprise/EDU has added Slack connector actions, letting workspaces enable supported tasks like joining channels, creating reminders, uploading files, and updating Slack profiles alongside search; admins can review Slack under Apps in ChatGPT and use Action control to manage which actions are available.

 The governance design is precise: the Action control layer means workspace administrators explicitly select which write actions to expose, preserving the organisation as the trust boundary for agent-initiated changes in a communication platform.

Within the Codex app itself, the most user-facing progress this week is improved supervision clarity. 

Improved progress visibility for subagents, tasks, and worktree creation ships alongside fixes for long threads loading and improvements to workspace file search, code review drafts, steering, and host setup and recovery.

 The addition of 

per-host personality settings with Friendly and Pragmatic options, support for editing goals directly in the composer, and a link from forked conversations back to the original thread

 are small but coherent: they establish that a long-running Codex session has a *character* (personality setting), a *direction* (editable goal in the composer), and a *history* (forked thread lineage traceable to its origin). Together these move the Codex session from an anonymous execution context toward a legible, steerable working relationship — which is precisely the interaction design problem that multi-day Goal Mode tasks expose most clearly.

---

### Perplexity: The Command Panel and the Forking Research Model

Perplexity's most interaction-design-significant development this week is the continued maturation of **Deep Research in Computer**, specifically the new **command panel** and forking capability that together transform the Computer interface from a mode-switching surface into a unified, discoverable skill directory. 

The new Computer command panel is a single place to discover and access everything Computer can do; instead of remembering commands or navigating between modes, users open the panel by typing `/` and searching across available modes and skills before starting a task, with the panel including built-in modes like Deep Research and Plan Mode alongside all available skills from the user, their space, and their organisation.



The forking capability is the more architecturally novel element. 

Forking lets users ask a follow-up question or explore a new iteration in a fresh thread, while keeping full access to the previous thread's context and generated assets.

 This shifts the temporal UX of deep research from a linear pipeline — fire, wait, receive — to a *tree* that the user can branch at any node without abandoning accumulated work. The UX implication is a new control pattern for long-running autonomous tasks: rather than cancelling and restarting when direction changes mid-run, users can preserve the work-to-date as a branch point and explore a divergent path from it. 

Starting with a complex research question, users can keep working from the result by turning findings into a report, spreadsheet, deck, dashboard, website, or follow-up workflow in the same place.

 The enterprise controls shipping alongside — 

a Computer Analytics API and custom credit limits

 — mean the observability and cost-governance layer is now matched to the capability layer, closing the gap between what Computer can do autonomously and what an enterprise admin can see it doing.

---

### Grok (xAI): Databricks Integration and the Enterprise Data Pipeline

xAI's most UX-relevant development in the June 22–24 window is the extension of Grok's agentic reach into enterprise data infrastructure. 

As of June 18, 2026, Grok models are natively available on Databricks Agent Bricks, announced live at the Databricks 2026 Data + AI Summit; for enterprise teams already running data pipelines on Databricks' Lakehouse architecture, this means Grok is now one selection away from powering production AI agents.

 The trust design detail is the most important part of this story: 

the Grok integration connects xAI's models directly to context stored in the Lakehouse — meaning agents can reason over a company's own structured and unstructured data without routing it through external pipelines — and Databricks has confirmed that model partners, including xAI, do not retain data submitted through these features.

 Non-retention as a default is a trust primitive that changes the agentic workflow calculus for regulated industries: it makes Grok an option inside data architectures that previously required zero-egress guarantees as a precondition.

---

## The Bigger Picture: Design Canvases, Identity Layers, and the Browser as Agent Surface

The week ending June 24, 2026 marks the moment when three previously separate design disciplines — generative UI, agent identity governance, and browser-native task execution — converged into a single coherent layer of agentic infrastructure. Claude Design's `/design-sync` and importable design system establish that the canvas is no longer a prototyping toy but a *governed workspace* where the agent operates only within the organisation's defined component vocabulary — the same parameterised-policy logic that Claude Code's `Tool(param:value)` syntax applies to tool permissions, now applied to visual output. Microsoft Copilot Studio's Entra Agent ID auto-provisioning applies exactly the same logic at the identity layer: every agent gets a unique, scopeable, auditable credential that can be targeted by Conditional Access policies, making the question "what is this agent authorised to do, and can I prove it?" answerable in the same admin centre where human identities are governed. Google's Gemini in Chrome auto browse applies the same accountability logic to the browser surface: agentic task execution now requires an explicit confirmation gate before sensitive actions, and the roadmap integration with Gemini Spark signals a coming architecture where a 24/7 cloud agent can take browser actions on behalf of users who have explicitly delegated that scope. What connects all three is the same underlying design insight: agentic systems earn trust not through capability announcements but through *constraint surfaces* — the design of who can authorise what, where the audit trail lives, and how a human can see, steer, or reverse what the agent did. The field has largely solved how to run agents in parallel. It is now solving, in earnest, how to prove they ran within bounds.

---

## References

[1] Claude Blog. (2026). *Claude Design stays on brand for daily work*. [https://claude.com/blog/claude-design-stays-on-brand-for-daily-work](https://claude.com/blog/claude-design-stays-on-brand-for-daily-work)

[2] arte.itlibra.com. (2026). *What Is Claude Design? /design-sync and June Overhaul*. [https://arte.itlibra.com/en/articles/what-is-claude-design-design-sync](https://arte.itlibra.com/en/articles/what-is-claude-design-design-sync)

[3] Vibe Coder Blog. (2026). *Claude Design Learns Your Brand and Hands Off to Claude Code*. [https://blog.vibecoder.me/claude-design-system-sync-code-handoff](https://blog.vibecoder.me/claude-design-system-sync-code-handoff)

[4] OpenAI Developers. (2026). *Codex Changelog — June 2026*. [https://developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

[5] Releasebot. (2026). *OpenAI Release Notes — June 2026*. [https://releasebot.io/updates/openai](https://releasebot.io/updates/openai)

[6] OpenAI Help Center. (2026). *ChatGPT Enterprise/EDU Release Notes*. [https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes](https://help.openai.com/en/