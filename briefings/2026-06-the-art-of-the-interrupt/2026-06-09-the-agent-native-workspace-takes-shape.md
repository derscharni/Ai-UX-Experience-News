# UX Briefing: The Agent-Native Workspace Takes Shape

**June 09, 2026**

Good morning. Today's briefing is defined by a single structural shift: AI products are stop being add-ons and starting to become the primary workspace. Claude Code ships **Dynamic Workflows** — a research preview that lets a single session orchestrate hundreds of parallel subagents across days-long tasks — redefining what "a coding session" even means; GitHub Copilot debuts its standalone desktop app with **Canvases**, a bidirectional shared work surface between humans and agents; Perplexity **Computer** lands inside Word, Excel, PowerPoint, and Outlook, planting an agent orchestrator inside the world's most-used productivity suite; and Grok Build v0.2.20 continues to harden its agent-visibility layer with collapsible task panels and structured compaction that protects long-running session state. The shift is not incremental. Across every major platform this week, the chat window is being demoted, and purpose-built agent workspaces are taking its place.

---

## At a Glance: June 9 Highlights

This week's releases collectively describe a post-chat paradigm: agents are no longer answering questions inside a conversation box — they are running parallel workflows, updating shared canvases, and operating natively inside enterprise software.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | Claude Code ships **Dynamic Workflows** in research preview — Claude writes its own orchestration scripts and runs tens-to-hundreds of parallel subagents in a single session, with progress saved across interruptions and a `/workflows` management panel. [1][2] |
| **ChatGPT** | OpenAI's **Codex** gains a stable **Goal Mode** across app, IDE extension, and CLI — users define an outcome and let Codex drive autonomously for hours or days — plus locked computer use that keeps agents working after the Mac locks. [3][4] |
| **Google Gemini** | Gemini Enterprise locks in Gemini 3.5 Flash as a mandatory, non-disableable default for all enterprise users as of today, while Gemini in Chrome on Android prepares to ship **auto browse** task automation in late June. [5][6] |
| **Microsoft Copilot** | The **GitHub Copilot app** expands its technical preview to all Pro, Business, and Enterprise subscribers, introducing **Canvases** as bidirectional agent-human work surfaces and a unified **My Work** dashboard for managing parallel agent sessions. [7][8] |
| **Grok (xAI)** | Grok Build v0.2.20 ships structured compaction with successor-assistant carry-forward, collapsible background-task panels grouping monitors and loops, and makes monitors killable by the model — all hardening long-session agent visibility. [9] |
| **Perplexity** | **Perplexity Computer** lands natively inside Microsoft Word, Excel, PowerPoint, and Outlook as a sidebar agent — eliminating the copy-paste loop and turning Office documents into live touchpoints in a multi-model orchestrated workflow. [10][11] |

---

## Product Highlights

### Claude: The Workflow as the New Unit of Work

Anthropic's most consequential UX release of the week — arguably of the month — is **Dynamic Workflows** for Claude Code, now in research preview.



Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you.

 The UX paradigm shift here is profound: 

a dynamic workflow is a JavaScript script that orchestrates subagents at scale — Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive.

 Crucially, 

progress is saved as the run goes, so a job that's interrupted picks up where it left off instead of starting over.



This is more than a capability bump. It represents a new unit of interaction: not the "turn" or the "session," but the *workflow* — a durable, inspectable, resumable artifact. 

A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer — and moving the plan into code lets a workflow apply a repeatable quality pattern, including independent agents that adversarially review each other's findings before they're reported.

 The user-facing control surface — `/workflows` to manage runs, `ultracode` as the keyboard trigger, and the ability to inspect and disable workflows per-organisation — establishes a new class of human oversight interaction: not "what should the agent do next?" but "is the orchestration running as designed, and do I want to stop it?"



The company warns that Dynamic Workflows can consume substantially more tokens than a typical Claude Code session and recommends starting with smaller, well-scoped tasks before using the feature for larger projects.

 This transparency-about-cost pattern is itself a trust design signal worth watching: Anthropic is surfacing the resource implications of agentic autonomy upfront rather than letting users discover them after a runaway billing event. Early real-world validation is striking: 

Jarred Sumner used dynamic workflows to port Bun from Zig to Rust with 99.8% of the existing test suite passing, roughly 750,000 lines of Rust, and eleven days from first commit to merge.



---

### GitHub Copilot: The Agent-Native Desktop Is Here

Microsoft's most structurally important interface release this week is not in Copilot Chat or VS Code — it is a brand-new application category: the **GitHub Copilot app**, now in technical preview for all Pro, Business, and Enterprise subscribers.



While the agentic shift has made development faster, it's also led to disjointed workflows, more context switching, and too much time spent reviewing agent-generated code. If agents are going to be a durable part of how software gets built, they need a real place in the developer workflow. Yet most developer tools were not designed for directing multiple agents in parallel.

 The Copilot app is GitHub's structural answer to that gap. 

The new GitHub Copilot app is the agent-native desktop experience built on GitHub — from a single My Work view, you can see work in motion across connected repositories: active sessions, issues, pull requests, and background automations.



The centrepiece UX innovation is **Canvases**. 

Canvases are bidirectional work surfaces for humans and agents. A canvas might show a plan, pull request, browser session, terminal, deployment, dashboard, or workflow state. Agents update the canvas as they work, and developers can edit, reorder, approve, or redirect that work on the same surface.

 GitHub frames this deliberately as a new interaction paradigm: 

"This is the beginning of agent experience (AX) in the Copilot app: interfaces designed not only for people to use, but for people and agents to operate together. The agent session remains where you instruct, discuss, and reason through ambiguity. Canvases are where that intent becomes visible work you can inspect, steer, and verify."

 This shifts the UX from a chat-transcript-as-output model to a *shared artifact* model — the agent's progress is not buried in a scrollback; it is a live, editable object that both the user and the agent co-own.

Critically, the trust infrastructure underneath the canvas is just as important as the surface. 

Inside any Copilot session, enable sandboxing with `/sandbox enable` — shell command execution runs with restricted access to the filesystem, network, and system capabilities, so developers can experiment with agentic workflows while staying in control of what Copilot can touch on their machine.

 And on permissions: 

the cloud agent asks permission before each write action by default, with an autopilot mode available once teams establish trust.

 This permission-before-action → trust-then-autopilot UX arc is one of the cleaner graduated-autonomy patterns the industry has shipped to date.

---

### Perplexity: The Agent Disappears Into Your Existing Apps

Perplexity's most significant UX move in the current period is the expansion of **Perplexity Computer** into the Microsoft 365 suite.



Computer is now available inside Microsoft Word, Excel, PowerPoint, and Outlook — four Microsoft 365 apps used by people at work every day. Earlier this month, Perplexity launched Computer in Microsoft Teams, allowing people to kick off projects in the channels where they already communicate. Now, Microsoft users have even deeper ways to use Computer. Organisations using Microsoft 365 can use Computer for document creation, data analysis, presentation design, and email management.



The UX implication is a fundamental change in the interaction surface: the agent is no longer a destination you navigate to. 

Perplexity Computer is accessible within Microsoft 365 via the Microsoft AppSource add-in ecosystem — once installed, it appears as a sidebar panel inside Word, Excel, and Outlook, and users can invoke it directly within those applications without switching tabs or copying content to an external tool.

Before this integration, nearly 40% of Computer users had already generated an output in Microsoft formats over the past 30 days — but without a native add-in, they still had to copy and paste content from Computer into tools like Microsoft PowerPoint. This integration removes that copy-paste step. Now teams can use Computer to draft, edit, and deliver work without ever leaving Microsoft 365 apps.



The trust design of the integration is also worth noting: 

Perplexity cites the source of every answer and the provenance of every figure, letting teams validate information before sharing.

 In a world where an agent inside Outlook is composing emails from thread context and web research simultaneously, inline citation is a meaningful safety rail rather than a cosmetic feature. This shifts the agent-in-office UX pattern from "magic black box" to "cited co-author" — and for enterprise adoption, that distinction matters enormously.

---

### Grok (xAI): Long-Session Agent State Gets Visible and Killable

xAI's most UX-relevant week is inside **Grok Build**, where v0.2.20 ships a cluster of changes that together address the hardest problem in agentic coding: what happens to session state during a long run.



Version 0.2.20 ships on June 3, 2026, making monitors visible and killable to the model, adding image-to-video and reference-to-video tools, and introducing structured compaction with a successor-assistant carry-forward and analysis block.

 The monitor-visibility change closes a meaningful transparency gap: a developer running a long Grok Build session can now directly see and terminate background monitoring processes rather than trusting the agent is managing them invisibly. 

A later sub-update groups the background tasks panel into collapsible sections with clearer styling for monitors and loops, and tab navigation now cycles through Prompt → Scrollback → Tasks → Prompt.



The **structured compaction** upgrade deserves particular attention as an agentic UX primitive. As long Grok Build sessions accumulate context and hit token limits, the agent must compress its working memory — a process that can subtly corrupt task state. 

The Context Compaction API shrinks long conversations into a shorter context and reuses it in follow-up requests for lower cost, faster time-to-first-token, and sharper responses on long agent loops.

 The structured compaction in Grok Build goes further: it explicitly neutralises echoed summarisation instructions in the summary seed and adds carry-forward analysis blocks, ensuring the compressed memory passed to the successor session is clean. For users running multi-hour coding agents, this reduces the risk of silent context corruption mid-task — a failure mode that has historically been nearly invisible. The UX principle being operationalised here is: *the agent should not be allowed to accidentally "gaslight" its own future self* via a poorly structured handoff.

---

### ChatGPT/OpenAI: Goal Mode Goes Stable, and Agents Get Trust Safeguards

OpenAI's most consequential interaction design move this week is the graduation of **Goal Mode** from experimental to generally available across the full Codex suite.



Goal mode is no longer an experimental feature and is available in the Codex app, IDE extension, and CLI. With Goal mode, you can have Codex drive toward a specific objective for hours or even days.

 Alongside it, 

remote computer use lets Codex use desktop apps after your Mac locks, including remotely via Codex Mobile — scoped to active, trusted computer use turns with safeguards including short-lived authorization, covered displays, relock on local input, and manual-unlock fallback.



The "locked computer use" safeguards here constitute a notable trust-design taxonomy. Rather than binary "agent can/cannot use computer," OpenAI is building a permission envelope: the agent operates inside a session-scoped trust window, with multiple fallback mechanisms that return control to the user (relock on local input, manual-unlock). This shifts the UX from "trust the agent forever after first authorisation" to a *renewable, bounded authority* model — closer to how OAuth token expiry works, applied to agentic computer control.

On the enterprise side, 

ChatGPT Enterprise/EDU adds default plugin sharing in Codex for eligible workspaces, letting teammates install shared local plugins — users can share local plugins with their workspace so teammates can install and use shared plugins from the Codex plugin directory.

 This shifts Codex from a personal coding agent to a team-level tool infrastructure, with implications for how organisations govern which agents and capabilities are available to whom.

---

### Google Gemini: Forced Standardisation and the Browser Agent Ramp

Google's most operationally significant UX event today is one of subtraction rather than addition. 

Effective June 9, 2026, the feature management toggle for Gemini 3.5 Flash is no longer available — Gemini 3.5 Flash is enabled by default for all users in the Gemini Enterprise app and cannot be disabled, applying to the Global, US, and EU multi-regions.



This is a deliberate reduction of enterprise administrator discretion in service of interaction consistency. When the underlying model can vary per admin policy, the agent's capabilities — and crucially, its behaviours and failure modes — become unpredictable across deployments. Removing the toggle standardises the interaction contract across the install base. The UX rationale is coherent, but the trade-off is real: enterprises that had policy reasons for controlling model version selection lose that capability.

On the browser agent front, Google continues its ramp toward **auto browse** as a persistent delegation layer. 

Already available on desktops, auto browse for Android lets users get the most out of Gemini in Chrome by automating digital chores so they can focus on more important tasks — completing tasks from appointment booking to party planning and finding in-stock items, all from an Android phone.

 The strategic destination is explicit: 

on desktop, Google will be integrating auto browse with Gemini Spark in the coming months, so that the 24/7 personal AI agent can take actions in the browser on the user's behalf.

 This establishes Chrome not as a browser but as an execution environment for a persistent background agent — the tab-as-task-executor pattern that represents the logical endpoint of the agentic browser vision.

---

## The Bigger Picture: The Agent-Native Workspace Takes Shape

This week's releases, read together, describe the same architectural transition from multiple directions. Claude Code's Dynamic Workflows establish the *workflow* as a first-class, durable, inspectable artifact — the agent writes its own harness, runs in the background, and hands you a result rather than a conversation. GitHub's Copilot app introduces **Canvases** as the interaction primitive that finally gives agent progress a surface that is neither a chat transcript nor a code diff — a bidirectional shared work object. Perplexity Computer eliminates the destination-switching problem entirely by planting the agent inside Office itself. Grok Build's monitor panels and structured compaction make the internal state of long-running agents visible and auditable. And Google's forced model standardisation, however administratively contentious, reflects the same underlying pressure: when agents are infrastructure, inconsistency in their behaviour is a governance problem, not a preference. The macro pattern is unmistakable. The UX industry is moving from designing *for* agents — giving them a place to live in the interface — to designing *with* agents, where the interface is a jointly-operated workspace and the agent's work is a live, editable, verifiable artefact alongside the user's. The central design challenge that emerges is human oversight at scale: not "can I talk to the agent?" but "can I see what it has done, understand why, stop it safely, and trust the result?" Every major platform this week shipped at least one answer to that question. None of them have solved it yet.

---

## References

[1] Anthropic Claude Blog. (2026, June 2). *Introducing dynamic workflows in Claude Code*. [https://claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[2] Claude Code Docs. (2026). *Orchestrate subagents at scale with dynamic workflows*. [https://code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[3] Releasebot. (2026). *Codex Updates by OpenAI — June 2026*. [https://releasebot.io/updates/openai/codex](https://releasebot.io/updates/openai/codex) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[4] OpenAI Developers. (2026). *Codex Changelog*. [https://developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[5] Google Cloud Documentation. (2026). *Gemini Enterprise Release Notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[6] Chrome for Developers Blog. (2026). *15 updates from Google I/O 2026: Powering the agentic web*. [https://developer.chrome.com/blog/chrome-at-io26](https://developer.chrome.com/blog/chrome-at-io26) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[7] GitHub Blog. (2026, June 2). *GitHub Copilot app: The agent-native desktop experience*. [https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[8] GitHub Changelog. (2026, June 2). *Expanded technical preview availability for the GitHub Copilot app*. [https://github.blog/changelog/2026-06-02-expanded-technical-preview-availability-for-the-github-copilot-app/](https://github.blog/changelog/2026-06-02-expanded-technical-preview-availability-for-the-github-copilot-app/) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[9] xAI Grok Build Changelog. (2026). *Grok Build Changelog — v0.2.20*. [https://x.ai/build/changelog](https://x.ai/build/changelog) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[10] Perplexity Hub. (2026). *Computer comes to Excel, Word, PowerPoint, and Outlook*. [https://www.perplexity.ai/hub/blog