# UX Briefing: Demonstration-to-Skill, Agent Memory, and the Automation Layer

**July 20, 2026**

Good morning. The 48 hours ending July 20 are defined by the industry's collective bet on a single design premise: agents should be taught by demonstration, not just described by instruction. **Grok (xAI/SpaceXAI)** ships **Automations** on July 16 — a first-party scheduled and email-triggered workflow engine that lets users describe a job once, in plain language, and have Grok execute it autonomously on a recurring schedule or when a matching email lands — completing the ambient-agent loop from one-off conversation to persistent background work. **Perplexity** consolidates its agentic memory architecture with **Brain**, the self-improving context-graph system for Computer that builds a nightly-refreshed LLM wiki from every session, connector, correction, and file the agent has touched — shifting the model of AI memory from remembering the user to remembering the work. **Claude Code (Anthropic)** ships two significant architectural updates: **live MCP connector data in published artifacts**, turning static session snapshots into live-updating dashboards that call external systems every time someone opens them, and a **broad stability and safety update** that tightens permission checks across Bash and PowerShell handling. **Codex (OpenAI)** extends its skill-building surface with continued rollout of **Record & Replay** — the demonstrated-workflow-to-reusable-skill primitive — while the **ChatGPT desktop app** ships a redesigned Chat/Work/Codex layout. **Microsoft Copilot** advances its **Copilot Cowork** general availability and **Copilot Vision** rollout, while **Gemini Enterprise** ships **Gemini Omni in Google Vids** and expands Gemini-powered document creation to 11 new languages.

---

## At a Glance: July 20 Highlights

The releases this window converge on a shared interaction thesis: the next frontier in agentic UX is not what the agent can do in a single session, but what it can learn across sessions — and how users retain meaningful oversight of work they never explicitly initiated.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code** ships live MCP connector data for published artifacts (dashboards update on every view, not just at session time) + broad safety update with tighter Bash/PowerShell permission checks, progress heartbeats for long-running tasks, and the new `EndConversation` tool; **/verify and /code-review** now require direct invocation, removing autonomous skill execution. [1][2][3] |
| **ChatGPT** | **Desktop app redesign** ships globally with Chat/Work split, unified Recents, Projects in-app, and cross-device synced Work conversations; **Record & Replay** continues rollout for macOS Business/Enterprise users — demonstrate once, Codex generates a reusable SKILL.md; **inline visualisations in Codex tasks** and improved task creation from conversations. [4][5][6] |
| **Google Gemini** | **Gemini Omni in Google Vids** ships with higher-quality video generation and text-based edit commands; **Gemini Docs creation** expands to 11 new languages; **Gemini Enterprise Bring Your Own Identity** goes GA for mobile app, enabling third-party IdP integration without an allowlist. [7][8][9] |
| **Microsoft Copilot** | **Copilot Vision** rolling out in July — point-show-ask interactions where users show Copilot a document, dashboard, or physical object and ask questions via voice; **Suggested Edits on Copilot Pages** ships; **Outlook email references in Copilot Notebooks** begins July rollout; Copilot Search summaries get shorter and more scannable with context-preserved handoff to chat. [10][11][12] |
| **Grok (xAI)** | **Grok Automations** launches July 16 on grok.com, iOS, and Android — schedule-based and email-triggered background jobs with run history, connector + skill access, and configurable notifications; Grok Build adds **grouped tool-call display**, cleaner scheduled automation task panels in gateway chat, and improved subagent instruction consistency. [13][14][15] |
| **Perplexity** | **Brain** (self-improving agent memory for Computer) ships in Research Preview to Max/Enterprise Max — nightly context-graph refresh, traceable entries linked to source sessions, user-controlled toggle; Computer also adds mid-task model switching, website publishing from research outputs, and per-model usage analytics. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Live Artifacts, Long-Running Heartbeats, and the Invocation Control Shift

Anthropic's most interaction-design-significant shipping in this window is a cluster of **Claude Code** updates that together advance two distinct trust architectures simultaneously: the transparency of what published artifacts show, and the governance of what the agent does without being asked.



Claude Code adds live MCP connector data for published artifacts, alongside screen reader mode and new sharing and collaboration options for Team and Enterprise. A published artifact can now call MCP connectors each time someone views it, so a dashboard shows live data and can take actions on demand rather than a snapshot from the session that built it.

 This is a fundamental shift in the UX model of Claude Code artifacts: previously, an artifact was a record of what the session produced at a moment in time; now it is an always-current, externally-grounded surface that can query a database, CRM, or internal API every time a colleague opens the URL. The design implication is that Claude Code stops being a one-way document generator and becomes a perpetually live reporting layer — a dashboard factory, not a snapshot tool.



Claude Code also releases a broad stability and safety update with tighter permission checks, safer Bash and PowerShell handling, improved background session cleanup, stronger telemetry, and better remote and plugin reliability. It also adds the `EndConversation` tool and progress heartbeats for long-running tasks.

 The `EndConversation` tool is the temporal UX primitive worth watching most closely: it gives agents a first-class mechanism to signal task completion rather than leaving long-running sessions in an ambiguous "still running?" state that users cannot easily interpret. Progress heartbeats address the same problem from the other direction — making in-flight work legible without requiring user intervention to find out whether the agent is stuck or working.



Claude Code also changes `/verify` and `/code-review` to run only when invoked directly — Claude no longer runs these skills on its own; invoke them with `/verify` or `/code-review` when you want them.

 This is the invocation-governance decision with the most significant day-to-day trust impact: it converts two previously autonomous skills into explicitly user-triggered actions, tightening the user's control over when and whether the agent performs code review. The pattern establishes a principle — autonomous skill execution requires explicit user consent — that is exactly the kind of default-conservative interaction design that makes agentic tools safer to deploy in production environments.

---

### ChatGPT / OpenAI: The Desktop Redesign, Record & Replay, and Cross-Device Work Continuity

OpenAI's most interaction-design-significant shipping in this window is a pairing of a navigation architecture overhaul and a new skill-acquisition primitive that together reframe what the ChatGPT desktop app is for — moving it from a conversation history tool toward a persistent work and automation surface.



ChatGPT updates its desktop app with a clearer Chat and Work layout, unified Recents, Projects in the app, and cloud-synced Work conversations across web, mobile, and desktop for smoother continuity. A global switcher lets you choose between ChatGPT and Codex. In ChatGPT, choose Chat for quick questions and conversational help, or Work to complete tasks end to end. Chat and Work conversations now appear together in Recents, where you can sort, filter, and pin them.

 The Chat/Work split is the conceptual architecture change that matters most: it makes explicit the distinction between asking-the-AI and delegating-to-the-AI that has been implicit in the product for months. The unified Recents surface — where both modes co-exist and are sortable — gives users the first coherent cross-session view of everything they have used the assistant for, conversationally or agentically.



Your existing ChatGPT Projects now appear in the desktop app. You can start a Chat conversation inside a Project or begin a Work thread using Project context. Cloud Work conversations now sync across web, mobile, and desktop, so you can start on one surface and continue on another. Local conversations stay on your computer.

 The cloud-sync boundary here — Work syncs, local conversations stay local — is a deliberate trust-design decision: it acknowledges that users have different privacy expectations for conversational sessions versus agentic tasks that access files and connected apps.



Record & Replay is a new Codex app feature for macOS that lets eligible users demonstrate a workflow once and turn it into a reusable skill. It is useful for repetitive workflows or tasks that are easier to show than describe, such as creating a configured issue, publishing a video, or downloading a recurring report. Record & Replay requires Computer Use to be available and enabled, and initial availability excludes the European Union, UK and Switzerland.

 The UX significance here is profound: rather than requiring users to author a SKILL.md prompt description of a repetitive workflow, Record & Replay shifts the delegation interface from *write-to-delegate* to *show-to-delegate*. 

The recorded skill documents when to use the workflow, the inputs, the steps, and how to verify the result, so it is inspectable and editable rather than an opaque macro. Unlike traditional RPA that replays coordinates and clicks, Record & Replay keeps the intent of the work as text, so it adapts more easily when the screen changes.

 The EU/UK/Switzerland exclusion at launch continues the now-established pattern: the most autonomous Codex features are the last to reach regulated jurisdictions, tracing the contour of EU AI Act Article 50 compliance work in live shipping decisions.

---

### Google Gemini: Omni in Vids, 11-Language Docs Expansion, and Enterprise Identity GA

Google's most UX-relevant work in this window is a pair of generative-workspace expansions that deepen Gemini's integration at the editing layer of existing documents and videos — the surfaces where users spend the most time, rather than at the query layer where they spend the least.



Gemini adds Omni directly in Google Vids, bringing higher-quality video generation and simple text-based video edits. Users can improve realism, text rendering, and physics or ask Gemini to change style, color grading, and even remove background noise. Users now have access to Gemini Omni directly within Google Vids. Omni provides higher quality video generation with significant improvements over previous models. Additionally, Omni's world understanding unlocks simple video edits so you can ask Omni to tweak the video you have to get the video you need.

 This is the generative UI pattern applied to video editing: rather than requiring users to learn a timeline-based edit interface, Gemini Omni accepts plain-language edit instructions against existing video — changing the interaction model from *operate-the-tool* to *describe-the-outcome*. For teams already using Google Vids for work presentations, product demos, or internal briefings, this collapses a multi-step editing workflow into a conversational turn.



Google Docs expands Gemini-powered document creation and editing to 11 more languages, giving users a richer, more centralized way to generate, refine, and format docs with context-aware help from Workspace data. We are now expanding support for these features to 11 more languages, including Mandarin, Dutch, Malay, Hebrew, Polish, Turkish, Czech, Indonesian, Swedish, Danish, and Norwegian. These new additions join previously supported languages: English, Spanish, Portuguese, Japanese, French, Korean, German, and Italian.

 The UX implication of this expansion is often underrated: AI-assisted document creation that operates in a user's native language reduces the cognitive load of the generation-refinement loop dramatically. For multinational Workspace deployments, this is the update that unlocks Gemini document creation for the full team rather than only the English-speaking subset.



Gemini Enterprise adds GA Bring Your Own Identity support for the mobile app, letting organizations connect supported third-party identity providers without an allowlist.

 The removal of the allowlist gate is the trust-architecture change with the most enterprise IT significance: it moves BYOI from a negotiated feature into a self-service GA capability, giving organisations with complex IdP environments (Okta, Ping, Azure AD) a supported path to connect their identity layer to Gemini Enterprise mobile without requiring a Google account relationship per user.

---

### Microsoft Copilot: Vision, Notebook Grounding, and the Cowork Purview Layer

Microsoft's most consequential UX addition in this window is **Copilot Vision** beginning its July rollout — a new multimodal interaction pattern that replaces text-based context-setting with show-and-ask interactions, making any visible object or screen a valid grounding source for a Copilot conversation.



Instead of trying to describe a dashboard, document, image, error message, or real-world object, users can show it to Copilot and ask questions in a voice conversation. Copilot uses that visual context, along with available work and web context, to explain what is in front of them, surface insights, and guide next steps. This feature is rolling out in July.

 This shifts the Copilot interaction model from *describe-your-context-in-words* to *show-your-context-visually* — a meaningful accessibility and efficiency improvement for users working with complex dashboards, physical documents, or error screens where transcribing the context into a prompt is itself a friction point. The voice-paired interaction is the important design detail: combining live visual grounding with voice output makes Copilot usable in hands-occupied, screen-intensive workflows that pure chat interfaces cannot reach.



Users can now get actionable feedback on a Copilot Page by selecting "Suggested edits" in the Copilot Shortcuts menu. Copilot analyzes the page content and offers feedback and suggestions in-line to improve clarity and quality, which users can then apply directly to the page. This helps users quickly polish their work and keep momentum without switching tools.

 Suggested Edits on Copilot Pages establishes an inline revision loop — feedback is surfaced at the point of the content, not in a separate chat thread, and can be applied in-place. This is the interaction pattern that makes AI-assisted document work feel native rather than bolted-on.



Microsoft Purview controls now extend to Cowork, helping organizations manage security and compliance with the same tools they use for Microsoft 365 Copilot. Cowork supports sensitivity label inheritance and display, audit logging, interaction content in Data Security Posture Management Activity Explorer, Insider Risk Management of user risks associated with Cowork interactions, as well as eDiscovery, Data Lifecycle Management, and Communication Compliance of Cowork interactions.

 The Purview integration is the enterprise governance detail that unlocks Cowork for regulated industries: by making every Cowork interaction subject to the same data governance, eDiscovery, and communication compliance machinery that enterprises already use for email and Teams, Microsoft is closing the last gap between "interesting agentic feature" and "IT-approvable production tool."

---

### Grok (xAI): Automations and the Ambient Background-Agent Surface

xAI's most interaction-design-significant shipping in this window is the launch of **Grok Automations** on July 16 — the first-party system that completes Grok's evolution from a conversational assistant into an ambient, always-on background worker that executes instructions on a schedule or in response to real-world events, without the user needing to initiate anything.



Today, xAI is introducing Automations: jobs Grok runs on its own. Describe the work once, choose when it runs, and Grok takes it from there, whether that's research done before you're awake or an important email flagged the moment it lands. Automations are available on grok.com and in the Grok app on iOS and Android.

 This is the ambient-agent paradigm landing in the consumer tier: for the first time, Grok users can delegate a repeating job — a morning briefing, a weekly report, a competitor-monitoring sweep — and have it execute without any further human prompt. The design shift is from *conversation starter* to *standing instruction*, and from *pull interaction* to *push delivery*.



An automation's instructions read like any chat message: describe what you want, attach files for context, add connectors and skills, and pick a mode. Name it, save it, and from then on every run is a fresh request: same instructions, current data.

 The "same instructions, current data" architecture is the UX detail that makes Automations qualitatively different from cron-like task scheduling: the agent does not replay a recorded script — it re-runs the instruction against whatever the current state of the world is, meaning a daily briefing automation automatically reflects today's news, not a cached version of last week's. 

Email triggers watch the inbox instead of a clock: when an incoming email matches the user's filters (sender, recipient, or subject), the automation fires with that email as context, and Grok responds to the actual message.

 This event-driven trigger model is the most consequential trust-design feature in the Automations release: it makes Grok the first major consumer AI product with a first-party, email-reactive agent surface — one where an inbound communication can cause the agent to act.



Users can stay in control by reviewing past runs, pausing and resuming anytime, or kicking off a run on demand with Run now.

 The run-history review surface is the oversight primitive that matters most here: every execution is logged as a full conversation thread that users can open, read, and continue, rather than a binary success/fail badge. This gives Automations an audit trail comparable to what enterprise tools require — though 

the public announcement does not say whether the history includes machine-readable execution traces, connector errors, or exportable audit logs

, which remains the open governance question for enterprise adoption.

---

### Perplexity: Brain and the Agent-Performance Memory Model

Perplexity's most architecturally distinctive work in this window — and one of the most original memory-design contributions the industry has shipped this year — is the continued expansion of **Brain**, the self-improving context-graph system for Computer that fundamentally reframes what AI memory is for.



Brain is a self-improving memory system. It builds a context graph of the work Computer performs. At set intervals, such as overnight, Brain reviews the context graph and teaches itself how to do the work better. The more work you do, the better and more efficient Brain makes your Computer.

 The conceptual distinction that makes Brain unusual in this landscape is its object of memory: 

traditionally, AI memory has been about the user — preferences, tastes, working styles, contacts, and role. Brain pioneers a different model: Brain remembers what the agent did. It remembers what worked and what failed, and what corrections got made to the work. It learns to do better work.

 This is the performance-memory model as opposed to the personalisation-memory model — and the distinction has major implications for how long-running agentic work improves over time.



Computer now learns from every task. Brain builds a private context graph across sessions, connectors, files, and past decisions, then refreshes it overnight so each new task starts already knowing what worked, what failed, and how you like things done. Every memory links back to its source, and you control what it keeps under Customize. In testing, Brain lifted answer correctness 25% and recall 16% while cutting cost 13% on tasks with prior context.

 The trust-design architecture of Brain's transparency layer is also worth noting: 

Brain is built only from the user's own activity and is used only to improve their own answers. Every entry links back to the session, file, or source behind it, so users can open it, check it, and edit or delete anything in Settings → Memory.

 This source-traced, user-editable memory design is the antidote to opaque AI personalisation: rather than learning silently and surfacing changes invisibly, Brain makes every memory entry inspectable and reversible — giving users the audit trail that most AI memory systems lack.

---

## The Bigger Picture: Demonstration-to-Skill, Agent Memory, and the Automation Layer

The 48 hours ending July 20, 2026 reveal a quiet but profound maturation in the interaction design of AI agents: the industry is moving past the phase where users delegate tasks by crafting careful prompts, and into a phase where delegation happens through demonstration, standing instruction, and accumulated work history. Grok Automations makes this shift in the consumer tier — you describe a job once, in plain language, and the agent owns it indefinitely, returning results to your inbox without further prompting. Codex Record & Replay makes it in the developer tier — you perform a workflow on your Mac and the agent converts that demonstration into a reusable, inspectable skill that can be replayed with new inputs. Perplexity Brain makes it at the memory layer — the agent learns not what you prefer, but what it did, building a nightly-refreshed context graph that makes every new task start smarter than the last. Anthropic makes the same shift at the transparency layer: live MCP-connected artifacts mean a Claude Code dashboard is no longer a historical record but a live window into external systems, opened anew on every view. What connects all four moves is that they each require a new trust design to match the new capability: Grok Automations needs run-history audit trails; Codex Record & Replay needs inspectable, editable SKILL.md files rather than opaque macros; Perplexity Brain needs source-traced, user-deletable memory entries; live Claude Code artifacts need connector-scoped permission controls. The pattern that emerges is the defining UX challenge of agentic mid-2026: as agents graduate from responding to anticipating, the interface design must graduate from showing what the agent did to giving users the controls to understand, verify, and, when necessary, undo what the agent has learned.

---

## References

[1] Releasebot. (2026). *Anthropic Release Notes — July 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[2] Releasebot. (2026). *Claude Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[3] Releasebot. (2026). *Claude Code Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[4] Releasebot. (2026). *ChatGPT Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[5] OpenAI. (2026). *Release Notes — OpenAI Products*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[6] OpenAI Developers. (2026). *Codex changelog*. [https://developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

[7] Releasebot. (2026). *Google Release Notes — July 2026*. [https://releasebot.io/updates/google](https://releasebot.io/updates/google)

[8] Releasebot. (2026). *Gemini Updates by Google — July 2026*. [https://releasebot.io/updates/google/gemini](https://releasebot.io/updates/google/gemini)

[9] Google Cloud Documentation. (2026). *Gemini Enterprise release notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[10] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[11] Microsoft Community Hub. (2026). *What's New in Microsoft 365 Copilot — June 2026*. [https://techcommunity.microsoft.com/blog/microsoft365copilotblog/whats-new-in-microsoft-365-copilot--june-2026/4529572](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/whats-new-in-microsoft-365-copilot--june-2026/4529572)

[12] SuperSimple365. (2026). *What's new in Microsoft 365 and Copilot? June 2026*. [https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/](https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/)

[13] SpaceXAI. (2026). *Automations in Grok*. [https://x.ai/news/grok-automations](https://x.ai/news/grok-automations)

[14] Grok. (2026). *Grok Release Notes*. [https://grok.com/release-notes](https://grok.com/release-notes)

[15] Releasebot. (2026). *Grok Build Updates by xAI — July 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Perplexity AI. (2026). *Self-improving Memory for Agents*. [https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents](https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents)

[17] Perplexity Help Center. (2026). *What is Brain?* [https://www.perplexity.ai/help-center/en/articles/19700001-what-is-brain](https://www.perplexity.ai/help-center/en/articles/19700001-what-is-brain)

[18] Releasebot. (2026). *Perplexity Release Notes — July 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

---