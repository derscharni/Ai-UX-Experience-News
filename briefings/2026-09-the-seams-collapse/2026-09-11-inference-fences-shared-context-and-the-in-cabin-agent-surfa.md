# UX Briefing: Inference Fences, Shared Context, and the In-Cabin Agent Surface

**September 11, 2026**

Good morning. The 48 hours ending September 11, 2026 are defined by a cluster of releases that deepen the governance architecture around deployed agents while simultaneously extending the agentic surface into new physical and collaborative environments. **Claude/Anthropic** delivers its most consequential trust-design event since per-tool domain controls shipped: **Inference Hooks entering beta for Claude Enterprise** — a pre-inference allow/deny gate that routes every governed prompt across claude.ai, Claude Code, and Cowork through the organisation's own AI security server before the model ever sees it, paired with the **C2PA Content Credentials and text watermarking** now shipping on all Fable 5.1 and Mythos 5.1 outputs. **ChatGPT/OpenAI** continues consolidating GPT-6 Astra's agentic computer-use surface with **cloud browser sign-in reaching web, iOS, and Android**, the **Codex agents dashboard** for managing parallel sessions, and the **built-in browser site-tool discovery** in ChatGPT Work and Codex that allows agents to auto-discover and invoke website-native tools without a separate connection step. **Google Gemini** ships a dense workflow-automation event with **four new Workspace Studio Flows steps** — Move Drive file, Copy Drive file, Send a Chat reply, and Reply to email — now rolling out through September, alongside **Gemini co-presenter suggestions in Google Meet** and **Google Pics reaching GA** with AI-powered image generation and object-based editing embedded directly in Workspace creative workflows. **Microsoft Copilot** lands the **Session and Response Sharing** feature completing its early-September worldwide rollout — allowing users to share full Copilot chat sessions or individual responses by link, with recipients able to fork the conversation in their own chat — while **Cowork's effort-level controls** now appear directly in the compose box, persisting across tasks. **Grok (xAI)** ships its densest Grok Build terminal-reliability update of September, with **scheduled task in-place updates**, **improved subagent spawning under burst load**, and **quieter hook runs** that silence successful hooks to reduce cognitive noise — and the Tesla **2026 Summer Update OTA** advances Grok's in-vehicle command surface to 116 confirmed voice controls, converting Tesla cabins from a touchscreen-dependent interface to a natural-language-first one.

---

## At a Glance: September 11 Highlights

Today's releases converge on two simultaneous UX movements: governing what agents can process before they act, and extending the environments — collaborative documents, automation flows, vehicle cabins — where those agents are encountered.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Inference Hooks enter beta for Claude Enterprise** — every governed prompt across claude.ai, Cowork, and Claude Code held for org's AI security server allow/deny before inference; denials recorded in Activity Feed; C2PA Content Credentials and text watermarking ship on all Fable 5.1 and Mythos 5.1 outputs; Claude Code `maxEffortLevel` controls and fresh system-prompt rendering land. [1][2][3] |
| **ChatGPT** | **Codex agents dashboard, cloud browser sign-in, and built-in site-tool discovery ship** — interactive agents dashboard for searching and managing sessions; cloud browser sign-in available on web, iOS, and Android for eligible plans; ChatGPT Work and Codex can auto-discover and invoke tools from supported website pages via built-in browser; shared Codex thread snapshots and pinned thread sync across desktop. [4][5][6] |
| **Google Gemini** | **Workspace Studio Flows gets four new automation steps rolling out through September** — Move Drive file, Copy Drive file, Send a Chat reply, and Reply to email with per-step admin controls and end-user approval gates for external data sharing; Gemini Meet co-presenter suggestion reaches GA; Google Pics GA with AI image generation and object-based editing in Workspace; Vids document-to-video AI reaches users. [7][8][9] |
| **Microsoft Copilot** | **Session and Response Sharing completes worldwide rollout in early September** — share full chat sessions or individual responses by link; recipients get read-only view and can fork conversation into their own history; existing org permissions govern data access; Cowork effort levels (Light through Max) now in compose box persisting across tasks; unified Copilot app worldwide Windows/Mac desktop rollout continues. [10][11][12] |
| **Grok (xAI)** | **Grok Build ships scheduled task in-place updates, quieter hook runs, and faster subagent spawning** — one-time tasks retired in favour of background commands; recurring tasks remind agent to stop monitor on completion; silent successful hooks; subagent spawning faster under burst load; Tesla Summer Update OTA ships 116 confirmed Grok voice commands for vehicle controls including climate, navigation, and Settings menu. [13][14][15] |
| **Perplexity** | **Computer in Email active for all Computer users; Portable Computer Windows rollout on track for September** — forward to computer@perplexity.ai for full Computer session from inbox; SPACE sandbox now powering 100% of Computer sessions with 60ms median sandbox creation; Portable Computer on DGX Spark expanding to Windows in September; Bumblebee supply-chain scanning remains active. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Inference Hooks, Watermarking, and the Pre-Inference Trust Gate

Anthropic's most consequential Claude Enterprise UX event in this window is the **Inference Hooks beta** — a trust-design primitive that inserts a mandatory organisational security checkpoint between the user's prompt and the model, for the first time making the act of inference itself subject to enterprise allow/deny governance across every Claude surface simultaneously.



Inference Hooks are now in beta for Claude Enterprise organisations — point Claude at your organisation's AI security server, and each governed prompt across claude.ai, Cowork, and Claude Code is held for the server's allow or deny verdict before inference proceeds; requests are signed, failure handling is configurable, and every denial is recorded in the compliance Activity Feed.

 The UX significance of this design choice runs deeper than its compliance utility: previously, every enterprise control layer in Claude — from domain allowlists on Managed Agents to per-tool web controls — operated *after* the agent had decided to act. Inference Hooks install the control layer *before* the model sees the prompt, converting a reactive governance posture into a proactive one. 

The server returns an allow-or-deny verdict; a denied request never reaches the model, and the hook runs on Anthropic's servers so it covers Claude chat, Claude Code, and Cowork with one organisation-level configuration.



The companion trust-design advance is the **C2PA Content Credentials and text watermarking** now shipping on all Fable 5.1 and Mythos 5.1 outputs — a provenance layer that makes AI-generated content identifiable not just within Claude's own interfaces but across any downstream system that honours the C2PA specification. 

Text generated by Claude Fable 5.1 and Claude Mythos 5.1 carries Anthropic's text watermark, and supported image and video files that Claude produces through the code execution tool carry C2PA Content Credentials when you retrieve them through the Files API on the Claude API — marking requires no changes to your requests or response handling.

 The no-change-required implementation is the correct UX decision: if provenance marking required developers to update their integration, adoption would be fragmented and the signal would only appear on outputs where the developer had opted in. By embedding it transparently, Anthropic ensures the watermark is present on every eligible output whether or not the developer thought to request it — which is precisely the behavioural property that makes a provenance system credible at scale. 

As of September 2, 2026, Anthropic lists Claude Fable 5.1 and Mythos 5.1 as supporting text watermarking and offers detection in private preview to eligible organisations and certain enterprises with EU compliance duties.



On the Claude Code side, 

Claude Code adds `maxEffortLevel` controls and fresh system-prompt rendering, while improving resume, prompt-cache, artifact publishing, and sandbox workflows.

 The `maxEffortLevel` setting is the per-session autonomy dial that enterprise operators have been requesting: it allows operators to cap how much reasoning effort the agent is permitted to apply to a given task, which matters both for cost predictability and for ensuring that high-stakes agentic sessions are not running at maximum autonomy without an explicit decision to permit it.

---

### ChatGPT / OpenAI: Site-Tool Discovery, the Agents Dashboard, and the Cloud Browser Sign-In

OpenAI's most interaction-design-significant releases in this window are a cluster of Codex and ChatGPT Work advances that together shift the agent from a tool that *uses* the web to a tool that *understands* the web as a live surface of invokable capabilities — and simultaneously gives operators the session-management infrastructure needed to govern a multi-agent environment at scale.

The most novel interaction primitive is **built-in browser site-tool discovery**. 

ChatGPT Work and Codex can now use tools that supported websites provide directly in the desktop app's built-in browser; work directly with a website's tools; ChatGPT can discover tools for your task without a separate connection — select the arrow in the address bar to see the tools a page provides.

 The UX significance of this is architectural: it converts the browser from a passive viewing surface into an active tool-discovery layer. Previously, a user who wanted ChatGPT to interact with a web application had to pre-configure a connector or MCP server. Site-tool discovery makes the tool available the moment the relevant page is open, discovered automatically rather than pre-wired. This is the correct model for knowledge workers who routinely encounter new web tools mid-task and do not want to pause to configure an integration before the agent can help.

The **Codex agents dashboard** addresses the session-management gap that has existed since multi-task Codex work became common. 

Codex adds a new agents dashboard, working-directory commands, and `codex queue` for managing sessions, while expanding Vim editing and improving diagnostics, SDK config overrides, and session reliability — the dashboard provides an interactive interface for searching and starting sessions.

 The interaction-design implication is that Codex's multi-session environment now has a canonical management view — users no longer need to maintain a mental model of which sessions are running, queued, or paused; the dashboard externalises that state into an inspectable, searchable interface.



Cloud browser sign-in reaches web, iOS, and Android on eligible plans — ChatGPT Work can ask you to sign in to a supported website through the cloud browser; enter your details in the sign-in flow, not in the chat; cloud browser sessions stay separate from your local browser.

 The trust-design detail worth isolating here is *where* credentials are entered: the sign-in flow, not the chat. This separation prevents credentials from appearing in the conversation transcript — the correct containment design for a system where conversation history may be logged, shared, or reviewed. The cloud browser session staying separate from the local browser is the second containment layer: the agent's authenticated web session cannot bleed into or expose the user's local browsing state.

---

### Google Gemini: Workspace Studio Flows, Meet Co-Presenter, and the No-Code Automation Expansion

Google's most structurally significant interaction-design event in this window is the **Workspace Studio Flows expansion** — four new automation steps that extend Google's no-code agent-workflow builder into the cross-channel document and communication actions that make up the largest share of routine knowledge-work overhead.



To help teams automate everyday work and seamlessly connect tasks across Google Workspace, four new automation steps have been introduced in Workspace Studio Flows: Move Drive file, Copy Drive file, Send a Chat reply, and Reply to email — with the Drive steps beginning full admin-controls rollout September 1 and Gmail steps rolling out admin controls September 8, with features following within days.

 The UX significance of these four steps is not the individual actions — each is simple — but the completion of a cross-channel automation loop: a Workspace Studio flow can now move files in response to emails, reply to Chat threads as a downstream automation step, and reply to email threads without a user being present. Together these make Workspace Studio flows viable for the delegation patterns that previously required Zapier or Apps Script: file intake flows, approval-triggered routing, and notification chains. 

These new steps give end users greater control over document management and cross-channel communications, enabling end-to-end automated flows directly from Workspace Studio — admins will have settings to disable individual steps and to require end-user approval when these actions may share data with audiences outside of their organisation.



The per-step admin disable and the end-user approval gate for external data sharing are the trust-design primitives that make these steps enterprise-deployable rather than just technically available. An admin who wants to allow intra-organisation Chat automation but prevent flows from replying to external email threads can do so at the step level — a scoped permission model rather than an all-or-nothing toggle.

The **Gemini co-presenter suggestion in Google Meet** is the other interaction-design advance worth isolating. 

Previously, adding a co-presenter in Google Meet required multiple manual steps; now, Gemini will intelligently suggest a co-presenter in the Ask Gemini in Meet panel and with just one click a user can allow another user to co-present their Google Slides presentation — the nudge will only appear for the main presenter when another participant uses a trigger phrase such as "Can you please add me as a co-presenter?" or "Next slide please."

 The interaction pattern this introduces is *intent-parsed permission delegation*: Gemini detects a participant's intent from natural language and surfaces a one-click approval action for the presenter, collapsing a multi-step manual workflow into a single gesture. This is the correct model for in-meeting permission actions where the presenter's cognitive load is already high — the agent does the detection work, the human approves. 

Google Pics is also generally available starting this window, bringing advanced AI image generation and precise, object-based image editing directly into the Workspace creative workflow.



---

### Microsoft Copilot: Session Sharing, Cowork Effort Controls, and the Collaborative Context Layer

Microsoft's most consequential Copilot interaction-design event completing this window is the **Session and Response Sharing worldwide rollout** — a collaborative context primitive that converts Copilot conversations from private, ephemeral, per-user work into shareable, forkable team assets, without requiring anyone to switch to a collaborative document format.



Copilot users can now share either a full chat session or an individual response through a simple link; recipients get a read-only view and can continue the chat like it was their own; users can select a sentence, paragraph, or table in a Chat response and ask Copilot to work only on that content, with the selected text previewed in the prompt before sending — this feature rolled out in August.

 The interaction-design shift this establishes is from *private AI session* to *shared AI context*: a user who has built up a research conversation with specific context, constraints, and prior outputs can now hand that context to a colleague as a live starting point rather than copying and pasting fragments into an email. 

Shared conversations and responses are snapshots — people who open the link cannot change the original conversation; if they continue from shared content, Copilot creates a separate copy in their own chat history.

 The snapshot-and-fork design is the correct trust-design choice for this feature: the original session is immutable, and the recipient's continuation is private. This prevents shared sessions from becoming collaborative editing surfaces with complex permission and conflict-resolution requirements.

The **Cowork effort-level controls in the compose box** are the other UX event materialising this window. 

Copilot Cowork now includes effort levels in the model picker, giving users more control over how Cowork responds — users can select Light effort for simpler tasks, keep Medium effort for everyday work, or choose higher effort levels when more complex analysis and reasoning are needed; the enhancement helps users balance response quality, speed, and usage consumption based on the needs of each task.

 The UX implication of effort levels persisting across tasks — 

a user's selected effort level persists across future Cowork tasks until they change it

 — is that the effort choice becomes a declared work posture rather than a per-task configuration. This reduces the cognitive overhead of choosing effort on every delegation, but also creates a risk that users forget they have set a non-default level and are inadvertently running lightweight effort on tasks that warrant deeper analysis. The `/cost` skill companion, which shows estimated credits consumed so far in a session, gives users the feedback signal they need to notice when effort calibration is misaligned with task complexity.

---

### Grok (xAI): Terminal Reliability, Scheduled Task Upgrades, and the Tesla Cabin Voice Surface

xAI's most interaction-design-significant Grok Build events in this window are the **scheduled task in-place update capability** and the **hook-run silencing** — a pair of changes that advance Grok Build's agentic workflow model from a system that requires users to manage task state manually into one that manages its own recurring work lifecycle with minimal interruption.



Scheduled tasks can now be updated in place — one-time tasks are retired in favour of background commands.

 This is the correct lifecycle design for agentic scheduled work: a task that needs to change scope or timing no longer requires deletion and recreation, which breaks any downstream references or monitoring that were pointed at the original task ID. In-place updates preserve continuity of the task object while allowing its parameters to change — the same principle that makes calendar event editing less disruptive than cancelling and re-creating a meeting. 

Grok Build also ships quieter hook runs, better Vim and dashboard navigation, cleaner voice dictation and theme handling, reliable headless timeouts, and improved scheduled tasks — successful hook runs are now silent; only blocking or failing hooks show status.



The hook-silencing change is the UI-noise reduction that long-running agentic sessions have required: in a session with many tool hooks running, every successful hook confirmation adds cognitive load without providing actionable information. Silencing success and surfacing only failure is the correct information-architecture principle — it converts hook output from a stream of confirmations the user must scan into a signal that only fires when intervention is needed.

The Tesla **2026 Summer Update** (OTA firmware 2026.26) represents the most significant expansion of the Grok agentic voice surface to a non-screen environment this year. 

With the 2026 Summer Update rolling out on firmware 2026.26.6.5, the assistant that used to crack jokes and answer trivia now folds mirrors, sets wipers, and adjusts climate on command — say "Hey Grok" and the chatbot stops chatting and starts driving the cabin; it is a shift from voice commands as a novelty to an actual input method that changes how owners touch their cars every day.

 The UX significance of this transition is the change of *commitment model*: a voice assistant that only answers questions has a low error cost — a wrong answer can be ignored. A voice assistant that executes vehicle state changes has a higher error cost and requires the user to develop a new mental model of verification. 

Grok now parses a chained sentence and fires off several actions from one breath — ask it to fold the mirrors, crank the wipers, and drop the temperature five degrees, and it does all three without the user repeating "Hey Grok" between each one.

 The chained command execution is the interaction primitive that makes in-cabin delegation feel genuinely different from prior voice assistants — it handles compound intent rather than requiring each sub-action to be a discrete invocation.

---

### Perplexity: Portable Computer Windows Rollout, SPACE Sandbox Maturity, and Email Delegation Consolidation

Perplexity's most significant agentic UX development in this window is the ongoing consolidation of the **Portable Computer** deployment model — the local-execution variant of Computer that runs the agent harness, orchestrator, and sandbox on dedicated hardware — as Windows availability approaches in September, paired with the SPACE sandbox platform's continued maturation as the universal execution layer beneath all Computer sessions.



Perplexity Portable Computer runs the agent harness, orchestrator, and sandbox locally on NVIDIA DGX Spark with per-step cloud approval — availability is Linux-first for Pro, Max, Enterprise Pro, and Enterprise Max subscribers, with Windows following in September.

 The trust-design advance that Portable Computer introduces is **per-step cloud escalation approval**: 

Portable Computer runs the full agent harness, orchestrator, and sandbox locally on DGX Spark — not just a local LLM; every step starts on-device; escalation to 15+ cloud models requires explicit per-step approval after a PII check.

 This per-step approval on cloud escalation is the bounded-autonomy design that regulated-industry deployments require: the agent can act autonomously on local compute but must pause and seek human approval before any step that crosses the data boundary to cloud inference, precisely at the boundary where sensitive data could leave the controlled environment.



Perplexity SPACE is the sandbox platform that runs agentic workloads for Perplexity Computer — its acronym describes precisely what it does: Sandboxed Platform for Agentic Code Execution; as of July 15, 2026, all Perplexity Computer sessions run on SPACE.

 The temporal UX advance SPACE provides — 

work that lasts over hours, days, and months sometimes requires restarts; to handle this, SPACE wraps sessions that can be paused, resumed, or branched into multiple sandboxes

 — converts the Computer session from a fragile single-thread process into a durable, resumable, branch-capable work unit. The design is significant for the Computer in Email use case specifically: a user who delegates a task by email and then receives a partial result can forward the reply to start a branched continuation, rather than needing to re-establish context from scratch. 

SPACE achieves 60ms median sandbox creation versus 185ms previously, with P90 latency at 89ms versus 447ms — 100% of Perplexity Computer sessions now run on SPACE.



---

## The Bigger Picture: Inference Fences, Shared Context, and the In-Cabin Agent Surface

The 48 hours ending September 11, 2026 reveal a category in simultaneous motion on two axes: the governance layer is moving *earlier* in the action lifecycle, and the agent surface is moving into *more physical and collaborative environments*. Claude's Inference Hooks represent the most decisive step yet in moving enterprise AI governance from post-hoc audit to pre-inference interception — the control gate installs not at the output, not at the tool call, but at the moment of inference itself, before the model has had the chance to act on any input. The C2PA watermarking on Fable 5.1 outputs extends the same principle to the content layer: provenance travels with the artefact into every downstream system, making the audit trail ambient rather than something the administrator must go looking for. At the same time, the agentic surface is expanding outward in every direction: into Tesla cabins via Grok's 116 confirmed voice commands (and the looming FSD planning-stack integration), into Copilot chat sessions that can now be forked and shared as live team context, into Google Meet presentations where Gemini detects participant intent and collapses permission delegation into a single gesture, and into Workspace Studio flows that now close the cross-channel automation loop from file movement to email reply. Perplexity's per-step cloud-escalation approval on Portable Computer, Google's per-step admin disable on Workspace Studio Flows, and OpenAI's credential-containment design in cloud browser sign-in all make the same architectural argument: the correct governance model for a world where agents are everywhere is not a single perimeter fence but a series of approval gates installed at every point where the agent's authority could extend into a new domain. The platforms that win enterprise trust in this era will be those that treat every expansion of the agentic surface as an occasion to install a correspondingly precise authority boundary — not as a constraint on capability, but as the design choice that makes expanded capability trustworthy enough to use.

---

## References

[1] Claude Platform Docs. (2026). *Claude Platform release notes*. [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview)

[2] Waxell.ai. (2026). *Claude Inference Hooks: Inline DLP, Allow or Deny [2026]*. [https://waxell.ai/blog/claude-inference-hooks-inline-dlp](https://waxell.ai/blog/claude-inference-hooks-inline-dlp)

[3] Wavect. (2026). *Does Claude Watermark Text? The 2026 API Answer*. [https://wavect.io/blog/claude-text-watermark-api-2026/](https://wavect.io/blog/claude-text-watermark-api-2026/)

[4] Releasebot. (2026). *Codex Updates by OpenAI — September 2026*. [https://releasebot.io/updates/openai/codex](https://releasebot.io/updates/openai/codex)

[5] Releasebot. (2026). *ChatGPT Updates by OpenAI — September 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[6] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[7] Google Workspace Updates Blog. (2026). *Automate Drive, Gmail, and Google Chat actions with new steps in Workspace Studio*. [https://workspaceupdates.googleblog.com/2026/09/automate-drive-gmail-and-google-chat-actions-with-new-steps-in-Workspace-Studio.html](https://workspaceupdates.googleblog.com/2026/09/automate-drive-gmail-and-google-chat-actions-with-new-steps-in-Workspace-Studio.html)

[8] Google Workspace Updates Blog. (2026). *Add co-presenters in Google Meet with one click*. [https://workspaceupdates.googleblog.com/2026/08/add-co-presenters-in-google-meet-with-one-click.html](https://workspaceupdates.googleblog.com/2026/08/add-co-presenters-in-google-meet-with-one-click.html)

[9] Google Workspace Updates Blog. (2026). *Google Workspace Weekly Recap — September 4, 2026*. [https://workspaceupdates.googleblog.com/2026/09/weekly-recap-09-04-2026.html](https://workspaceupdates.googleblog.com/2026/09/weekly-recap-09-04-2026.html)

[10] M365 Admin. (2026). *Session and Response Sharing in M365 Copilot*. [https://m365admin.handsontek.net/session-response-sharing-m365-copilot/](https://m365admin.handsontek.net/session-response-sharing-m365-copilot/)

[11] M365 Admin. (2026). *Microsoft Copilot: Effort control for models in Cowork*. [https://m365admin.handsontek.net/microsoft-copilot-effort-control-models-cowork/](https://m365admin.handsontek.net/microsoft-copilot-effort-control-models-cowork/)

[12] Microsoft Community Hub. (2026). *What's New in Microsoft Copilot — August 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960)

[13] Releasebot. (2026). *xAI Release Notes — September 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[14] Grok Build Changelog. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[15] Motor1. (2026). *Tesla's Grok AI Now Does 116 Voice Commands, But Many Owners Are Locked Out*. [https://www.motor1.com/news/806866/tesla-grok-summer-update-brings/](https://www.motor1.com/news/806866/tesla-grok-summer-update-brings/)

[16] Perplexity Blog. (2026). *Computer now works in email*. [https://www.perplexity.ai/hub/blog/category/news](https://www.perplexity.ai/hub/blog/category/news)

[17] MarkTechPost. (2026). *Perplexity Ships Portable Computer on NVIDIA DGX Spark: Local Harness, OS-Enforced Sandbox, and Zero Per-Token Cost for Local Steps*. [https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/](https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/)

[18] Perplexity Research. (2026). *Making SPACE: Secure Runtimes for Long-Running Agents*. [https://research.perplexity.ai/articles/making-space-secure-and-efficient-runtimes-for-long-running-agents](https://research.perplexity.ai/articles/making-space-secure-and-efficient-runtimes-for-long-running-agents)