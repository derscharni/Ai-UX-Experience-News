# UX Briefing: Demonstration Teaches, Identity Governs, Research Forks

**June 23, 2026**

Good morning. The last 48 hours are defined by four interlocking stories that each advance the same underlying shift: agents are no longer configured by writing instructions — they are *taught, identified, governed, and forked in real time*. **OpenAI Codex** shipped **Record & Replay** on June 18, a programming-by-demonstration feature that lets a user perform a workflow once on their Mac while Codex watches and converts the session into an inspectable, editable, reusable skill — ending the era of prompt-described automation for procedural desktop work; **Anthropic Claude Code** consolidated its multi-session orchestration surface with a broad release that streamlines **Agent Teams**, tightens nested skill handling, and hardens auto mode review; **Google Gemini Enterprise** deepened its agent identity infrastructure, with each deployed agent now receiving a unique SPIFFE-formatted cryptographic ID that flows through IAM, the Agent Gateway, and full audit logging; **Microsoft Copilot** made Claude available as a selectable model in the main Copilot Chat interface across all platforms; and **Perplexity Computer** merged **Deep Research** directly into its agentic Computer workflow, adding forking, inline actions, and analytics APIs. The macro signal: the interaction design frontier has moved from "how do agents get instructions?" to "how do agents get trusted, tracked, and improved without the user having to re-author them from scratch?"

---

## At a Glance: June 23 Highlights

This week's releases collectively describe a maturation layer arriving across the category at once: less about spawning more agents and more about how agents learn workflows, prove identity, and surface progress — the governance and legibility infrastructure that makes autonomous systems safe to actually use at scale.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | Claude Code ships a broad release streamlining **Agent Teams** (implicit team spawn, no setup step), adding `Tool(param:value)` permission syntax for parameterised policy rules, improving nested skill handling in `.claude/skills` directories, and hardening auto mode to evaluate subagent spawns before launch; a new VSCode usage attribution panel now shows cache misses, subagent and per-skill breakdowns over 24h/7d. [1][2][3] |
| **ChatGPT** | Codex ships **Record & Replay** (app v26.616, June 18) — a programming-by-demonstration feature where a user performs a workflow on their Mac once and Codex generates an inspectable, editable SKILL.md file reusable across Computer Use, browser actions, and plugins; thread hand-off between local and remote host also ships in the same release. [4][5][6] |
| **Google Gemini** | Gemini Enterprise deepens its **Agent Identity** infrastructure, assigning each deployed agent a unique SPIFFE-formatted cryptographic ID with auto-provisioned X.509 certificates, IAM integration, and audit logs that attribute every action to the agent's own credential — distinct from shared service accounts; Asana data store integration enters Public Preview, enabling natural-language project and task actions from within Gemini Enterprise. [7][8][9] |
| **Microsoft Copilot** | **Claude is now selectable in Microsoft 365 Copilot Chat** across web, desktop, iOS, and Android (rolling out June 2–16), letting users choose Claude for complex analysis, document understanding, and structured content generation; VS Code 1.125 ships a smarter **integrated browser** for secure browsing over remote connections plus stronger enterprise Copilot management controls. [10][11][12] |
| **Grok (xAI)** | **Grok for Microsoft Word** (and PowerPoint/Excel) launches as a free add-in, bringing web research, X data, and document drafting directly into the Office canvas; xAI also introduces a unified **cumulative usage counter** in the account dashboard tracking tokens, voice, image, and video consumption across the account simultaneously. [13][14][15] |
| **Perplexity** | **Deep Research comes to Perplexity Computer** (June 19), embedding multi-model research directly into the agentic workflow with forking, inline actions, analytics APIs, and custom credit limits — the first major Computer changelog update since the Microsoft 365 integration launched in late May. [16][17] |

---

## Product Highlights

### ChatGPT / OpenAI: Record & Replay and the Demonstration Paradigm

The most significant UX design shift of the 48-hour window is not a new agent architecture or a new interface surface — it is a new *teaching modality*. 

**Record & Replay** lets users demonstrate a workflow on their Mac and turn it into a reusable skill; the guidance is to reach for it when the workflow is repetitive, depends on personal preferences, or is easier to show than to describe in a prompt.

The feature shipped on June 18 as part of Codex app version 26.616, and is available to ChatGPT Plus, Pro, Business, Enterprise, and Edu subscribers outside the European Economic Area, the United Kingdom, and Switzerland.

 The UX design bet here is fundamental: it inverts the standard agent-instruction relationship. Rather than a user constructing a prompt that approximates what they want the agent to do, the user simply *does the thing* while the agent observes. 

By generating a natural-language skill description rather than a mechanical replay log, Codex shifts the generalization work from a rule-based system to a reasoning model — the practical effect is a system that can execute a workflow against a fresh instance of an application, with new input values, rather than one that replays a fixed sequence of clicks valid only on the day the recording was made.



The trust and safety design of Record & Replay is notably careful. 

During recording, Codex observes the actions and window content needed to learn the workflow, and the captured skill can then be replayed with Codex, Computer Use, browser actions, plugins, or a combination of available tools — no re-recording required.

 The output is not an opaque binary — it is an inspectable, editable SKILL.md file a user can read, correct, and share. 

OpenAI's own guidance to keep recordings focused on the workflow and avoid secrets or sensitive data signals that accidentally capturing credentials or PII is a real risk; the release notes do not yet specify how recorded skills are stored at the org level, or what happens when a third-party UI changes.

 This transparency gap will become a governance question as organisations begin sharing skills team-wide. Also shipping in the same v26.616 release: 

bulk actions for the Automations history, plus the ability to hand off threads between a local and remote host to continue tasks on a connected machine.

 The thread hand-off is a quiet but consequential temporal UX improvement — it means an in-flight task started on one machine can be resumed on another without abandoning state.

---

### Claude / Anthropic: Agent Teams Simplified, Permission Policy Deepened

Anthropic's most consequential June 21 release is a comprehensive tightening of the interaction layer governing how Claude Code coordinates multiple agents, decides what they are permitted to do, and surfaces attribution for what they consumed. 

Claude Code adds agent team streamlining, richer permission rules, smarter nested skill and workflow handling, and stronger auto-mode review — also improving `/doctor`, remote control and `/bug`, while fixing many background session, auth, subagent, and Windows issues.



The **Agent Teams** simplification is the most ergonomically visible change. 

With `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` set, every session now has one implicit team — users can spawn teammates directly with the Agent tool's `name` parameter, with no setup step needed; the `team_name` parameter is still accepted but ignored.

 This removes the cognitive overhead that had made agent teams feel like infrastructure work rather than a natural extension of a coding session: the lead-and-team relationship is now implicit rather than requiring explicit creation commands.

The `Tool(param:value)` permission syntax extends Anthropic's governance vocabulary in a meaningful direction. 

The syntax allows permission rules to match a tool's input parameters with `*` wildcard — for example, `Agent(model:opus)` to block Opus subagents; skills in nested `.claude/skills` directories now load when working on files there, and on a name clash, the nested skill appears as `<dir>:<name>` so both remain available.

 The UX implication is a shift from all-or-nothing capability gating to *risk-proportionate policy authoring*: a team can selectively block the most computationally expensive subagent tier while permitting lighter ones to run freely, calibrating governance to actual risk exposure. Finally, 

a new usage attribution panel in VSCode's Account & usage dialog now shows cache misses, long context, subagent, and per-skill/agent/plugin/MCP breakdowns over the last 24 hours or 7 days.

 This is the first in-editor cost-transparency surface Claude Code has shipped — it transforms post-session usage review from a console-level investigation into an ambient, session-adjacent signal.

---

### Google Gemini: SPIFFE Agent Identity and the Trust-by-Default Architecture

Google's most UX-consequential release of the week operates almost entirely below the visible interface layer — yet it defines the trust architecture for everything built on top of the Gemini Enterprise Agent Platform. 

**Agent Identity** provides a strongly attested, cryptographic identity for each agent based on the SPIFFE standard; with Agent Identity, an agent can securely authenticate to MCP servers, cloud resources, endpoints, and other agents, acting either on its own behalf or on behalf of an end user.



The interaction design significance is most visible in what Agent Identity *replaces*: shared service accounts, where multiple agents or workloads share a single credential and audit trail is therefore ambiguous. 

Unlike service accounts, agent identities are not shared by multiple workloads by default, cannot be impersonated, and do not allow developers to generate long-lived service account keys; access tokens generated for Google Cloud are cryptographically bound to the agent's unique X.509 certificates to prevent token theft.

 For users and admins, the practical payoff is a coherent answer to the question that has plagued multi-agent deployments: "which agent took that action?" 

View of agent identity flows through logs across Google Cloud services; for user-delegated flows, logs show both the user identity and the agent identity.

 This dual-identity audit trail — agent *and* user both attributed in every log line — is the trust primitive that makes enterprise delegated-action workflows auditable at the depth compliance teams require. On the data connectivity side, 

the Asana data store is now available in Public Preview in Gemini Enterprise; users can connect an Asana account to search and read projects, workspaces, teams, and tasks using natural language, and can also perform actions such as creating projects and tasks directly from the Gemini Enterprise app.



---

### Microsoft Copilot: Multi-Model Chat and the VS Code Integrated Browser

Microsoft's most structurally significant UX move of this window arrived on June 16: 

Anthropic's Claude is now available in Copilot Chat across Android, Windows, iOS, Mac, and Web; users can now select Claude as a model option for complex analysis, document understanding, and structured content generation; adding Claude gives users more flexibility to choose the model that best fits their needs.



The model-selector interaction is a new UX primitive in its own right. 

Users select the AI model switcher and choose a model from the list; they can also choose Auto and let Copilot automatically select the right model for them.

 This shifts Copilot from a single-model interface to a *model-routing* interface — one where the choice of underlying model is now an explicit, per-session user decision rather than a platform default the user has no visibility into. The governance design is correspondingly layered: 

for enterprise customers, an admin must enable Anthropic as a Microsoft sub-processor in the Microsoft 365 Admin Center before Claude can be used for edits.

 This admin-first gate preserves the organisation as the trust boundary: model capability expands are made available to users only after IT has made an explicit data-governance decision about a non-Microsoft inference provider. Separately, 

Visual Studio Code released version 1.125.1 on June 17, 2026, bringing a smarter integrated browser, more control over extension updates, and stronger enterprise management for Copilot.

 The integrated browser feature — 

search the web and securely browse over remote connections without leaving VS Code

 — is a meaningful workspace consolidation: developers can now perform research and verification without breaking their coding context into a separate browser window, reducing the context-switching friction that has historically made agent-assisted development feel fragmented.

---

### Grok (xAI): In-Document Agents and the Unified Usage Counter

xAI's most interaction-design-relevant release of this window is the arrival of **Grok for Microsoft Word** — and its companion PowerPoint and Excel add-ins — as a free add-in available from the Microsoft Marketplace. 

xAI adds Grok for Microsoft Word, a free Microsoft 365 add-in that turns notes into polished documents, rewrites text for clarity, brings web research and X data into Word, and helps draft content with connectors from email, SharePoint, and Google Drive.

 The UX bet here is workplace-surface depth over standalone app breadth: rather than requiring users to switch to grok.com, xAI is embedding Grok's live-web-search and X-social-context capabilities directly into the document canvas where knowledge workers already draft. 

Users can prompt Grok with an initial set of notes to rewrite into structured, long-form text, or have Grok write initial drafts of proposals and reference materials; the add-in also excels at fixing grammar, rewriting text for clarity, or aligning writing styles across multiple authors.



The other notable Grok UX development this week is the introduction of a visible cumulative usage counter in the account dashboard. 

xAI updated its Grok AI fair use policy language to clarify that rate limits apply cumulatively across text, image, voice, and code execution; previously, the policy described limits per feature in isolation, but now the total compute consumption across the account triggers a soft cap.

The change also introduced a visible counter in the account dashboard, so users can track message limits, token usage, and media generation in one place; this transparency was absent before and represents a meaningful upgrade for power users who rely on planning rather than guessing.

 This is the same *concurrent visibility* design principle that Perplexity has pursued with its context panel and credit usage display — the insight that showing users what their agent usage is *costing in real time* is a trust primitive as important as any output quality signal.

---

### Perplexity: Deep Research Forks Inside Computer

Perplexity's most significant UX event of the window is the June 19 integration of Deep Research into the Computer agentic workflow, a move that merges two previously distinct interaction models — the linear research-and-report pipeline and the multi-step autonomous task executor — into a single composable surface. 

On June 19, 2026, Deep Research came to Computer, with faster command access, forking, inline actions, analytics APIs, and custom credit limits.



The *forking* capability is the most architecturally novel element. It establishes a new temporal UX pattern for long-running research tasks: rather than waiting for a single linear research run to complete before adjusting direction, users can now branch a mid-flight research thread — creating a divergent research path at any step without losing the work accumulated up to that branch point. 

Deep Research in Computer is built on the Agent Search SDK and Search as Code: with one complex question, it builds a research plan automatically, then finds primary sources across hundreds of sites and cites every claim; the model writes code that assembles the search itself, and that code runs thousands of retrieval steps in parallel, tailored to each question.

 The analytics API and custom credit limit additions are the governance surface: 

context and sources are now easier to see in Computer threads, and usage analytics are available for both individuals and teams.

 This shift — making the cost and provenance of a multi-model research run inspectable at the individual thread level — closes the observability gap that has made autonomous deep research workflows feel like black boxes to the users and team admins responsible for reviewing their outputs.

---

## The Bigger Picture: Demonstration Teaches, Identity Governs, Research Forks

This week's releases, read together, describe a quiet but decisive transition in the maturity curve of agentic AI design: the field has largely solved *how to run* agents in parallel, and is now solving *how agents acquire capability, prove trustworthiness, and remain legible as they operate*. Codex's Record & Replay answers the capability acquisition problem through demonstration — the agent learns a workflow by watching, not by being programmed — which dramatically lowers the floor for non-technical users to build real automation without writing a single prompt. Claude Code's simplified Agent Teams and `Tool(param:value)` permission syntax answers the trust configuration problem through composable policy: organisations can now write governance rules that match real workflow risk, rather than toggling blunt capability flags. Google's SPIFFE Agent Identity answers the attribution problem at the infrastructure level: every agent action in a multi-agent mesh is now traceable to a unique, non-spoofable cryptographic identity, making the audit trail that enterprises require for compliance not a bolt-on but a default property of every deployed agent. Microsoft's model selector makes the *which agent* question visible in the user interface for the first time in mainstream enterprise productivity software, establishing model choice as an explicit user and admin decision. And Perplexity's Deep Research forking answers the temporal control problem: users can now redirect a long-running autonomous research run at any mid-point branch, turning what was a fire-and-wait workflow into a steerable, inspectable process. What unites all five is the recognition that the hardest unsolved problem in agentic UX is not raw capability — it is the legibility of *how capabilities were acquired, who authorised them, and what they are currently doing* — and the week's releases each take a different architectural approach to the same underlying answer.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] Claude Code Docs. (2026). *Orchestrate teams of Claude Code sessions*. [https://code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)

[3] Releasebot. (2026). *Anthropic Release Notes — June 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[4] OpenAI Developers. (2026). *Record & Replay – Codex*. [https://developers.openai.com/codex/record-and-replay](https://developers.openai.com/codex/record-and-replay)

[5] The Decoder. (2026). *OpenAI's Codex can now watch you work once and repeat the task forever*. [https://the-decoder.com/openais-codex-can-now-watch-you-work-once-and-repeat-the-task-