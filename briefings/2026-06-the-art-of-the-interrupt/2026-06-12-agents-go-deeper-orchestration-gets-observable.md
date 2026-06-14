# UX Briefing: Agents Go Deeper, Orchestration Gets Observable

**June 12, 2026**

Good morning. Today's briefing is defined by a single architectural shift arriving simultaneously on every platform: the agent is no longer a single thread. Claude Code's newly shipped **ultracode** mode and recursive nested sub-agents let one prompt fan out to hundreds of parallel workers, each with its own isolated context window; OpenAI's **Codex** acquires Ona to make those long-running cloud sessions persistent for days, and ships a **Developer Mode** that opens Chrome DevTools Protocol access for agentic browser debugging; **Grok Build** continues maturing its worktree-isolated parallel sub-agent architecture; **Microsoft Copilot** rolls out **Copilot Notebooks** worldwide and ships its **Browsing with Copilot** enterprise preview; and **Perplexity Computer** deepens its Microsoft 365 embedding with a live **context panel** and full inline citation for every agent-generated claim. The through-line is not raw capability but *observability*: as agents spawn sub-agents that spawn their own sub-agents, every platform is simultaneously racing to give users a window into what is running, at what depth, and at what cost.

---

## At a Glance: June 12 Highlights

Today's releases collectively answer the same urgent question: now that agents run multi-level hierarchies of parallel workers autonomously, how does a user — or an enterprise admin — actually see, audit, and interrupt what is happening inside that hierarchy?

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | Claude Code ships **ultracode** — a keyword and `/effort` setting that pairs `xhigh` reasoning with automatic dynamic-workflow orchestration across up to 1,000 parallel sub-agents — and adds recursive nested sub-agents up to five levels deep, each with its own fresh context window, alongside a new **connector observability dashboard** for MCP health monitoring. [1][2][3] |
| **ChatGPT** | Codex ships **Developer Mode** for browser use, granting the agent full Chrome DevTools Protocol access for live JS profiling, DOM inspection, and network traffic analysis; separately, OpenAI acquires **Ona** to enable persistent cloud-hosted Codex sessions that run for days without a local machine; and **Workspace Agents** for Business/Enterprise continue their broad rollout with per-app safeguard controls and admin activity logs. [4][5][6] |
| **Google Gemini** | **Antigravity CLI** (the replacement for Gemini CLI) is now available to all users ahead of the June 18 sunset of Gemini CLI for Pro/Ultra, unifying the terminal agent harness with the Antigravity 2.0 desktop app's multi-agent backend; **Gemini in Chrome** on Android (including auto browse) remains on track for late-June launch. [7][8] |
| **Microsoft Copilot** | **Copilot Notebooks** begins worldwide rollout, collapsing chats, output creations, and references into a single project-organised workspace synced with OneNote; **Browsing with Copilot** in Edge for Business Limited Public Preview is open for enterprise admin signups; and a refreshed AI disclaimer admin control lets organisations surface custom AI policy links inside the agent UI. [9][10][11] |
| **Grok (xAI)** | **Grok Build** continues its worktree-parallel sub-agent architecture, with each sub-agent isolated on its own Git branch and an automated **Arena Mode** evaluation layer scoring competing outputs before human review; the latest changelog also surfaces a consolidated permission-memory system and a visible skills/MCP/hooks origin display via `grok inspect`. [12][13] |
| **Perplexity** | **Perplexity Computer** in Microsoft 365 (Word, Excel, PowerPoint, Outlook, Teams) deepens its trust layer with a live **context panel** showing real-time task progress and artifacts side-by-side with the conversation, plus full inline citations on every agent-generated claim, including financial data. [14][15] |

---

## Product Highlights

### Claude / Anthropic: Ultracode and the Recursive Agent Stack

The most architecturally significant Claude Code development of the past 48 hours is the maturation of the **ultracode** orchestration mode and the arrival of genuinely recursive sub-agent nesting. These are two distinct but complementary features that together redefine the interaction model for long-horizon agentic coding.



**Ultracode** is a Claude Code setting that combines `xhigh` reasoning effort with automatic workflow orchestration; with it on, Claude plans a workflow for each substantive task instead of waiting to be asked, and a single request can turn into several workflows in a row — one to understand the code, one to make the change, and one to verify it.

 The key UX design decision here is the shift from reactive to *anticipatory* orchestration: the agent doesn't ask "should I parallelize?" — it decides, plans, and shows you the plan. 

The approval experience in the Desktop app shows the workflow name, the phase list, and a token-usage caution, with Once, Always, and Deny actions

 — an explicit pre-flight consent gate that keeps the human in the loop before large parallelised runs commence.

Alongside ultracode, 

Claude Code sub-agents can now spawn their own sub-agents, capped at depth 5

, and the design motivation is specifically about context hygiene rather than raw parallelism. 

Each sub-agent gets a fresh context window, so nesting lets a sub-agent offload before its own context fills.

 The UX implication is a new form of *cognitive encapsulation*: noisy intermediate tool calls, web searches, and log greps get pushed into throwaway child windows where they cannot pollute the parent's context, and only distilled signal flows upward. For users, this means longer, more reliable agent runs without the context-drift and goal-deviation that has historically caused agentic sessions to silently go wrong after hour two. Separately, 

Claude adds public beta connector observability and in-app directory submission, letting admins and owners monitor adoption, errors, latency, and usage across Claude products while submitting MCP connectors directly from Claude; published connectors in the directory now have a dashboard showing how they're performing across Claude product surfaces.

 This is a meaningful transparency upgrade for enterprise deployments: rather than discovering a broken MCP connector only when an agent fails, teams can now proactively monitor connector health through a purpose-built observability surface.

---

### ChatGPT / OpenAI: Live Browser Debugging and the Persistent Cloud Agent

OpenAI's most consequential UX development today is a two-part answer to the same problem: how does a coding agent stay useful when the work is long, multi-session, and deeply browser-entangled?



OpenAI announced a **Developer Mode** for browser use in Chrome and the Codex in-app browser; Codex can use the Chrome DevTools Protocol (CDP) to debug browser issues by profiling JavaScript performance and inspecting console output, network traffic, and page state.

 This shifts Codex from a code-generation agent that occasionally opens a browser to a *live browser-native debugging partner*: the agent can observe what a running application is actually doing at the network and DOM layer, not just what its source code says it should be doing. 

Developer Mode gives Codex controlled Chrome DevTools Protocol access so it can profile JavaScript, inspect console output and network traffic, review page state such as the DOM and applied styles, and diagnose live browser issues; the feature is off by default — users can toggle it from Codex app settings.

 The opt-in-by-default design is deliberate: CDP access represents a significant expansion of what the agent can observe and interact with inside the user's browser, and the trust design correctly gates it behind explicit user intent.

The second move is structural: 

OpenAI has agreed to acquire Ona, a company that builds secure cloud execution and orchestration technology for developers; Ona will enable developers to run Codex with persistent and controlled cloud infrastructure for long-running agentic workflows; right now, most Codex execution happens locally on developers' laptops, and through Ona, OpenAI aims to make Codex agents keep working for days without being tied to a user's local machine or an active session.

 The UX implication is a fundamental change to the mental model of a Codex task: from "a session I start and must keep open" to "a delegated job I dispatch and can check back on." This is the *async temporal UX* pattern applied at the infrastructure level — the session outlives the user's attention, with the governance, logging, and review architecture that enterprise contexts require.

---

### Google Gemini: The CLI Consolidation and the Multi-Agent Terminal

Google's most important UX event of the period is the hardening of the **Antigravity CLI** transition ahead of its June 18 deadline. The framing from Google is explicitly architectural, not cosmetic.



Gemini CLI proved the terminal could be an incredible interface for agentic tasks, but user needs shifted — they now require multiple agents communicating with each other to split up the work and solve complex problems; this means terminal tools need to share a unified backend with the rest of the workflow; listening to feedback made one thing clear: Google can serve users best by pouring energy into a single product built for today's multi-agent reality.

 This is a meaningful honesty of design intent: the old CLI was a single-agent tool, and the new one is being built as an async multi-agent dispatch surface from the ground up. 

Asynchronous workflows let Antigravity CLI orchestrate multiple agents for complex tasks in the background, letting users run large-scale refactors or research several topics without locking up the terminal session; Antigravity CLI shares the same agent harness as Antigravity 2.0, the new Antigravity desktop application, ensuring that all future improvements to core agents are automatically applied wherever users work.



This *unified agent harness* design is the structural UX bet: a single orchestration layer governs agents whether they are invoked from the terminal, the desktop app, or Chrome. For users, the practical payoff is that the mental model of "what my agent can do" doesn't need to change based on which surface they're using. The session-level trust and transparency features stay consistent across contexts. On the consumer browser front, 

Gemini in Chrome on Android (including Nano Banana and auto browse) will be launching in late June, initially available on devices with 4GB of RAM or more; already available on desktops, auto browse for Android lets users get the most out of Gemini in Chrome by automating digital chores so they can focus on more important tasks; with auto browse, users can easily complete tasks from appointment booking to party planning, finding in-stock items and more, all from their Android phone.



---

### Microsoft Copilot: Notebooks, Browsing, and the Admin Disclaimer Layer

Microsoft's two most significant UX rollouts this week address opposite ends of the agent experience: the project workspace where outputs accumulate, and the governance surface where enterprise admins signal oversight.



The **Copilot Notebooks** design in the Microsoft 365 Copilot app has been updated to help organise chats and work by project; the new UI brings together chats, output creations, and references in one place, so users can more easily collaborate and move work forward; Copilot Notebooks in the Microsoft 365 Copilot app and in the OneNote app stay in sync, so users can move smoothly between experiences; this feature is rolling out in June.

 This is Microsoft's structural answer to the scattered-context problem that has plagued enterprise AI since it arrived: conversations happen in one place, outputs appear somewhere else, source documents live in a third location. Notebooks collapses that into a single persistent, reviewable project artifact. The OneNote sync is particularly significant for trust: it moves Copilot's working memory into a surface users already audit and share, rather than an opaque proprietary context store.

On the enterprise governance side, 

Microsoft Edge has opened the Limited Public Preview for Browsing with Copilot in Edge for Business for admin signups, introducing agentic browsing to the enterprise — allowing Copilot to navigate websites, fill in information, and complete multi-step tasks on behalf of users.

 The admin-gated rollout pattern is deliberate: capabilities that carry real-world consequence are gated behind explicit, recorded administrative authorisation, establishing the organisation — not the individual user — as the trust boundary. This is reinforced by the AI disclaimer update: 

Microsoft updated the AI disclaimer experience in Copilot Chat based on customer feedback, introducing an admin control that allows organisations to customise how the disclaimer appears; the disclaimer will display bolded text for increased visibility; admins can configure a custom URL pointing to their AI policy documentation.

 This small feature carries a significant trust signal: the AI's output can now be permanently annotated with the organisation's own AI governance policy — a machine-readable pointer to human accountability.

---

### Grok (xAI): Worktree Isolation and the Arena Mode Evaluation Layer

xAI's most UX-relevant ongoing development is the maturation of **Grok Build**'s multi-agent architecture, which makes a distinctive structural bet that sets it apart from Claude Code and Codex: Git-worktree isolation per sub-agent.



Grok Build spawns up to eight parallel sub-agents simultaneously, each working in its own Git worktree; they do not step on each other; an automated evaluation layer called **Arena Mode** scores competing outputs before users ever review them; in practice, larger refactors that would take one agent an hour can be parallelised across several agents working in isolation.

 This is a fundamentally different trust design from Claude Code's ultracode approach: rather than a single orchestration script coordinating specialists, Grok Build frames parallel work as a *competition* where independent agents produce divergent solutions and an automated evaluation layer surfaces the best one before the human sees anything. The UX implication is a shifted review burden — the user inspects a ranked shortlist, not a raw agent output. 

Plan mode reverses the standard failure mode: the model commits to a structure first, users intervene cheaply at the planning layer, and execution becomes deterministic instead of exploratory.



The latest changelog additions deepen observability further. 

The v0.2.16 update fixes stuck session states, shows where external skills, MCP servers, and plugins originate in `grok inspect`, and fixes parent session state leaking into sub-agent conversations.

 The `grok inspect` provenance display is a meaningful transparency primitive: when the agent is using a plugin or MCP server, the user can now see exactly where that capability came from — a direct answer to the auditing question of "what tools is this agent actually calling, and who configured them?" 

The prior v0.2.15 release added permission memory — remembering the last permission choice across tools with a configurable first-prompt default in `config.toml`

 — establishing Grok Build as the first major agentic coding CLI with a *learning permission model* that stops asking questions the developer has already answered.

---

### Perplexity: The Context Panel and Cited Agency Inside Office

Perplexity's most interaction-design-forward recent move is the introduction of the live **context panel** inside Perplexity Computer, which changes how users understand what an agent is doing mid-task — not just what it has done when it finishes.



Every Computer thread now has a context panel that shows the context that Computer is working on; the context panel is a dedicated workspace where live progress, generated artifacts, and credit usage appear side-by-side with the conversation; this helps users quickly track what's happening with their task, access outputs as they're generated, and stay in control from start to finish.

 This shifts the UX from *retrospective inspection* (reviewing what the agent did after it finished) to *concurrent visibility* (watching the agent work in real time, with the ability to intervene). The credit usage display inside the same panel is an underrated trust feature: users can see what an in-progress run is costing before it completes, giving them a meaningful cost-awareness signal during long autonomous tasks. 

All answers contain sources and inline citations directly to the source, including traceable claims for financial data.

Computer is now available inside Microsoft Word, Excel, PowerPoint, and Outlook — four Microsoft 365 apps used by people at work every day; earlier in May, Computer launched in Microsoft Teams, allowing people to kick off projects in the channels where they already communicate.

 The Microsoft 365 integration makes the inline citation design critically important: 

Perplexity cites the source of every answer and the provenance of every figure, letting teams validate information before sharing.

 When an agent is composing an email in Outlook or building a financial model in Excel and pulling from live web sources and connected files simultaneously, the citation layer is not a cosmetic feature — it is the primary mechanism by which a user can distinguish between what the agent generated from enterprise data it owns and what it retrieved from the open web. 

Computer is aimed at something subtly different from a single-document assistant: not just helping inside a document, but coordinating entire multi-step workflows that stretch across many documents, inboxes, and data sources at once.



---

## The Bigger Picture: Agents Go Deeper, Orchestration Gets Observable

This week's releases, read together, describe a single architectural inflection point: the AI agent is no longer a single context window doing one thing at a time, and every platform is simultaneously racing to give users a coherent mental model of what a hierarchy of agents is doing at any given moment. Claude Code's ultracode and five-level nested sub-agents, Grok Build's worktree-isolated parallel execution with Arena Mode evaluation, and Codex's persistent cloud sessions via Ona are all answers to the same engineering challenge — breaking large tasks across many parallel workers without the user losing track of the whole. But the trust and UX challenge that emerges is new and urgent: when an agent spawns sub-agents that spawn their own sub-agents, the interaction design question shifts from "what is the agent doing?" to "how deep is the stack, what is running at each level, who authorised it, and what is it costing?" The answers this week take very different forms: Anthropic surfaces a phase list and token-caution before a workflow launches; xAI shows plugin provenance in `grok inspect` and scores competing outputs with Arena Mode before the human ever sees them; Perplexity puts live progress, artifact outputs, and credit usage side-by-side in its context panel; and Microsoft continues to gate agentic browsing behind explicit admin authorisation and custom policy documentation. What is emerging is not a single standard for agentic observability, but a competition between models: pre-flight consent versus concurrent visibility versus post-task audit versus human-in-the-evaluation-loop. The industry has not yet settled on which combination builds the most durable user trust — and the next few months of enterprise adoption data will force the answer.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[2] Claude Code Docs. (2026). *Orchestrate subagents at scale with dynamic workflows*. [https://code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[3] Releasebot. (2026). *Claude Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[4] Neowin. (2026). *OpenAI is making Codex more useful in Chrome and the cloud*. [https