# UX Briefing: Computer Use Goes Mainstream, Agent Persistence, and the Unified Surface

**September 04, 2026**

Good morning. The 48 hours ending September 4, 2026 are defined by three simultaneous structural shifts in how agents operate, persist, and surface their authority to users. **ChatGPT/OpenAI** delivers its most consequential interaction-model event of 2026 with the release of **GPT-6 Astra**, whose primary UX story is not a new model — it is a new paradigm for computer-use sessions in Codex: notes that persist across context windows rather than lossy compaction, non-blocking clarification questions, and a computer-use harness running at nearly double the previous speed. **Claude/Anthropic** ships its most meaningful agentic workspace UX improvement of the September window: a **fullscreen diff panel** that opens beside the Claude Code conversation as the agent edits, and a new **Auto mode permission tab** within `/permissions` for inline rule management — a canvas-plus-oversight design that converts agentic coding sessions from terminal streams into structured visual workspaces. **Google Gemini** extends its ambient memory surface to the physical world through the **September Android Drop**: Gemini can now remember where a user placed untracked items and save locations to a new Remembered tab in Find Hub — a voice-first, zero-hardware-required interaction pattern — while **Gemini Live** gains Guided Vision, surfacing real-time spoken scene descriptions for low-vision users. **Microsoft Copilot** crosses a structural platform threshold as **VS Code 1.136 ships the Agent Host** — a dedicated process that decouples agent sessions from editor window lifecycle — alongside the open **Agent Host Protocol (AHP)** and **Agent Merge (Preview)**, a loop-until-done PR resolution agent; in parallel, the **unified Copilot app** for personal and work accounts accelerates toward its mid-September Windows and macOS desktop rollout. **Grok (xAI)** expands **Grok Bot** beyond beta — now available on SuperGrok Plus, SuperGrok Heavy, Cursor Pro+, Cursor Ultra, and Cursor Teams — with a Bot roster UI, presence cues, shared group chats, and routines for work that starts without a prompt, formalising the shift from chat sessions to persistent digital coworkers with their own cloud computers. **Perplexity** advances the connector approval UX in Computer, deepening the granular per-tool trust surface that lets users and admins gate exactly when the agent pauses to ask before it acts.

---

## At a Glance: September 4 Highlights

Today's releases converge on a single inflection point: agents are no longer bounded by a single session, a single window, or a single user prompt — and every platform is simultaneously redesigning its session, memory, and permission surfaces to reflect that new reality.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Fullscreen diff panel ships in Claude Code** — `/diff` opens a live uncommitted-changes view beside the conversation in fullscreen mode; Auto mode tab added to `/permissions` for inline classifier rule editing; prompt-cache miss diagnostics surface in `/cost` and status line; concurrent session state isolation fixed. [1][2][3] |
| **ChatGPT** | **GPT-6 Astra launches** — computer-use harness runs nearly 2× faster; Codex gains cross-context-window note-keeping to replace lossy compaction; non-blocking clarification questions let Codex ask without stalling unrelated work; enterprise rollout begins via Daybreak gated access, with Plus/Pro/Business/Enterprise access arriving in coming days; Google Drive side-by-side canvas now on Android. [4][5][6] |
| **Google Gemini** | **September Android Drop ships** — Gemini remembers untracked item locations via voice command to a new Find Hub Remembered tab (Android 16+); Gemini Live gains Guided Vision for real-time spoken scene descriptions; Google Keep integrates into Messages with inline shared lists; Gemini for Home compound-command voice-control fixes continue rollout from September 2. [7][8][9] |
| **Microsoft Copilot** | **VS Code 1.136 ships Agent Host and Agent Host Protocol (AHP)** — dedicated agent process persists sessions across window closures; open AHP enables third-party SDK integration; Agent Merge (Preview) loops on PR review feedback, failed checks, and merge conflicts until ready; multi-root workspace support for Copilot and Claude sessions; unified Copilot app for personal/work accounts accelerates to mid-September Windows/macOS desktop rollout. [10][11][12] |
| **Grok (xAI)** | **Grok Bot expands beyond beta** — available on SuperGrok Plus, SuperGrok Heavy, Cursor Pro+, Ultra, and Teams; Bot roster UI with avatars and presence cues replaces session-centric design; each Bot has its own persistent cloud computer, browser, filesystem, and terminal; routines enable work that starts without a prompt; X account linking lands with free API credits for paid users. [13][14][15] |
| **Perplexity** | **Connector approval granularity deepens in Computer** — users set any connector tool to Always ask before Computer acts; single-action approval, thread-level grants, and deny options all available; Portable Computer (local on-device runtime with NVIDIA) targets Windows availability in September; Computer in Email active for all Computer users with thread-context reply. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Diff Panel and the Auto Mode Permission Tab

Anthropic's most consequential Claude Code UX event arriving on September 4 is the **fullscreen diff panel** — a workspace-design intervention that converts the fullscreen coding session from a pure conversation stream into a split-surface where the agent's edits and the codebase's current state are simultaneously visible.



Claude Code adds a diff panel that opens beside the conversation in fullscreen mode and shows uncommitted changes as Claude edits; it is toggled with `/diff`.

 The interaction-design shift this establishes is significant: previously, developers running fullscreen Claude Code sessions had to mentally track what the agent was changing, or context-switch to a separate diff tool to inspect edits mid-session. The `/diff` toggle brings the codebase's evolving state into the same visual field as the conversation, establishing a true side-by-side canvas model — the same split-pane approach that ChatGPT's Google Drive canvas and Claude Code's VS Code extension have used, now arriving natively in the fullscreen terminal UI.

The second consequential UX event is the **Auto mode permission tab**. 

Claude Code adds an Auto mode tab to `/permissions` for viewing and editing auto mode classifier rules.

 For practitioners who have built up custom auto-mode rule sets for their repositories — allowing certain Bash commands, blocking certain network patterns — this inline editing surface is the governance-legibility improvement that was previously missing. Rather than editing classifier configuration files outside the session, the auto-mode rule set becomes a first-class UI surface within the running session. This is the right design pattern for the same reason Grok Build's blocked-action permission cards matter: the agent's permission posture should be inspectable and editable from within the interaction, not only from configuration files consulted before the session begins.

The session-reliability fix that compounds both workspace UX improvements is the resolution of a critical multi-session state collision. 

Claude Code fixes concurrent sessions silently reverting each other's `~/.claude.json` changes — workspace trust no longer resets and MCP/project state is no longer lost when running many sessions at once.

 For teams running parallel Claude Code sessions on shared infrastructure — a configuration that becomes more common as agentic coding workflows scale — this fix is the correctness guarantee that makes multi-session fleet operation trustworthy. Additionally, 

Claude Code adds a likely cause for prompt-cache misses — such as tool definitions or system prompt changed, or idling past the TTL — to `/cost` and the status line's `prompt_cache` field.

 This is the diagnostics transparency that practitioners managing cost-controlled agentic sessions have needed: knowing *why* the cache missed, not just that it did.

---

### ChatGPT / OpenAI: GPT-6 Astra and the Computer-Use Threshold

OpenAI's most structurally significant UX event in this window is the release of **GPT-6 Astra** — and the UX story is less about the model than about the interaction architecture it enables for Codex and computer-use sessions.



OpenAI shipped GPT-6 Astra on September 3 with a "computer use" capability that lets the model operate existing software UIs directly instead of requiring custom API integrations.

The enterprise case for Astra rests heavily on computer use: OpenAI says the model can fill out online forms, update CRM records, organize calendars, conduct web research, and draft results into documents or email.

 The interaction-design significance of operating existing UIs rather than structured APIs is the long tail it opens: internal tools, legacy systems, and enterprise applications without clean API surfaces are all now reachable through the same session interface. This shifts the automation bottleneck from "can we build a connector?" to "can we govern the session?"

The Codex-specific UX change is where the most durable interaction pattern improvement lives. 

OpenAI introduces a new way for Codex to preserve and retrieve context when the context window fills — historically, models used compaction to summarize work during long sessions such as when debugging complex issues or tackling large refactors, and each compaction could leave out details about why a fix failed or how a component behaves; in Codex, Astra can keep notes across context windows, preserving accumulated details without repeatedly compressing them into a single summary.

Earlier context windows remain searchable, so Astra can find requirements or test results from previous messages and tool outputs even if that information wasn't captured in its notes; the feature can be enabled in Codex config.toml and will become the default for Astra in the coming weeks.

 This is the temporal UX improvement that long-running agentic coding sessions have needed most: the agent's understanding of *why* previous attempts failed is precisely what compaction has been discarding, and the switch to searchable cross-window notes changes the failure mode from "the agent forgets and repeats mistakes" to "the agent retains and reasons over its own work history."

The companion interaction-design feature is the non-blocking clarification pattern. 

Astra can ask the user a question while continuing work that does not depend on the answer — this removes a common agent failure where one unresolved decision stalls an entire job.

 The UX implication is a materially better delegation experience: rather than the agent pausing and waiting for an answer before resuming, it surfaces the clarification question as an async signal and continues all work it can do independently. This converts clarification from a blocking gate into an ambient notification — the correct design for long-running agentic sessions where the human may not be actively watching. 

Users on Pro, Business, and Enterprise plans also get access to GPT-6 Astra Pro

, and 

enterprise administrators can enable Astra for their workspace, with access off by default at launch.

 The default-off enterprise posture is the right trust-design choice for a model whose computer-use capability operates at the UI level of existing internal systems.

---

### Google Gemini: Physical-World Memory and the Guided Vision Interaction Model

Google's most interaction-design-significant September 4 event is the **September Android Drop**, which extends Gemini's ambient memory and perceptual capabilities into two domains that have previously required hardware: physical item tracking and real-time visual scene description.



Google's September Android Drop introduces an upgrade to Find Hub that allows Gemini to remember where users left important items, even if those items don't have a tracker attached — this plugs a hole in Google's current tracking setup, as while Find Hub is ideal for tagged belongings, there are plenty of things routinely misplaced — such as passports, spare keys, documents, or small essentials — that aren't worth attaching a tracker to; this new feature essentially provides a lightweight memory layer for those items.

Users can tell Gemini where an item was placed and optionally add a photo — for example, "Hey Google, remember in Find Hub that I put my passport in my bedroom drawer" — and later ask Gemini for the item's location or check the Remembered items tab in Find Hub.

 The interaction-design pattern this establishes is the voice-first persistent-memory primitive: the user's spoken command becomes a durable record in the tracking surface, with photo context available as an optional confirmation layer.



Until now, Find Hub's usefulness depended almost entirely on hardware — a Bluetooth tracker, a Google-connected device, or a UWB tag; the September update breaks that hardware dependency.

 The UX significance of eliminating the hardware requirement is that it fundamentally changes the adoption curve for Gemini memory features: previously, only users who had purchased and attached tracker hardware could benefit from location recall; now any Android 16+ user with a voice command can delegate item-location memory to Gemini. This is the same paradigm shift as contact-lens versus glasses for vision correction — the friction cost of using the feature drops to zero.

The Guided Vision addition to Gemini Live represents a different but equally significant interaction model. 

Gemini Live adds Guided Vision to offer verbal "descriptions of what's in front of you" — use cases include reading fine print on a food label, ordering from a menu in a low-lit restaurant, or locating household objects; if the camera isn't lined up, voice feedback guides the user to reframe, pan across a space, or centre an object.

Guided Vision brings Gemini Live spoken camera descriptions to assist blind and low-vision users.

 The interaction design of camera-guidance feedback — spoken instructions to reframe rather than visual overlays — is the correct design for the accessibility use case it serves: users who need Guided Vision are often precisely those for whom visual overlay instructions would be inaccessible.

---

### Microsoft Copilot: Agent Host, AHP, and the VS Code Agent Architecture Shift

Microsoft's most structurally significant UX event in this window is the release of **VS Code 1.136 with the Agent Host** — an architectural shift that repositions AI coding agents from editor features that stop when the window closes into persistent processes that outlive any individual window session.



Visual Studio Code 1.136 ships the Agent Host, a dedicated process that isolates AI agents from the extension host so sessions persist across window closures and multiple windows can sync to a single session; Microsoft is also releasing the open Agent Host Protocol (AHP), enabling third-party harnesses like the Copilot SDK and Claude Agent SDK to integrate with a unified interface.

 The trust-design significance of session persistence across window closures is profound: previously, closing a VS Code window terminated the agent session and any running agentic tasks. With the Agent Host, the agent's execution is decoupled from the UI lifecycle — closing the window is no longer an implicit cancel, which changes both the UX model and the governance question (how does the user know what the agent did while the window was closed?).



Agent Merge (Preview) resolves review feedback, failed checks, and merge conflicts until a pull request is ready to merge; Copilot and Claude agent sessions across all folders in a multi-root workspace are now supported in the editor window Chat view.

Agent Merge asks an agent to address review feedback, fix failed checks and merge conflicts, and rerun workflows, repeating the process until the pull request is ready to merge; it is enabled via the `chat.agentMerge.enabled` setting.

 The interaction-design pattern Agent Merge establishes is the loop-until-done agentic task: rather than the developer manually iterating on CI feedback after each push, the agent takes responsibility for the PR-readiness loop, surfacing only when it reaches a state it cannot resolve autonomously. This is the correct design for a workflow where the human's value is in the initial code decision, not in the mechanical merge-conflict resolution.



Chat sessions now allow users to organize related chats in a session hierarchy and quickly see which ones need attention.

The redesigned new-session input brings the prompt, model selection, workspace selection, and other session controls together in one layout; agents can resolve workspaces by their project name in addition to absolute paths and workspace URIs.

 On the broader Copilot platform, the **unified Copilot app** continues its rollout arc. 

The consolidation ends a two-year stretch in which Microsoft shipped two separate Copilot apps that could sit side by side in the same taskbar; the unified app keeps the Microsoft Copilot name but ships with a new icon, and it folds the consumer assistant's chat and image creation into the same shell as the Microsoft 365 work experience.

The single app now holds both work and personal accounts, which makes pasting company material into a personal chat a much easier mistake to make

 — the data-boundary risk that enterprise privacy teams must evaluate before the mid-September Windows and macOS desktop rollout arrives.

---

### Grok (xAI): Grok Bot Beyond Beta and the Persistent Coworker Design Model

xAI's most consequential UX event in this window is the **expansion of Grok Bot beyond beta** — the moment the persistent-agent design model that Grok Bot introduced in August transitions from a closed preview to a broadly available product tier across SuperGrok and Cursor plans.



xAI expands Grok Bot beyond beta, making the AI teammate available in SuperGrok Plus, SuperGrok Heavy, Cursor Pro+, Cursor Ultra, and Cursor Teams plans; the update brings always-on digital coworkers that can handle real work across apps, inboxes, and tools.

 The design philosophy behind Grok Bot's expansion is the most explicit statement any platform has made about the session-versus-agent distinction. 

Most AI interfaces are organized around a chat session the user operates — each session begins with setup, unfolds as the user looks on, and ends when the conversation stops; so the main objects in Grok Bot are Bots, not conversations: a Bot has a name, an avatar and a title, remembers its conversations with the user, has its own computer and tools, and when the user comes back tomorrow, they are coming back to the same Bot.

 This is the interaction-design paradigm that separates Grok Bot from every other product in this briefing: the primary navigation object is a persistent agent identity, not a session log.



xAI launches Grok Bot with a persistent agent experience built around Bots, chats, prompts, tools, and artifacts; the new design adds a Bot roster, presence cues, computer access, inline cards and widgets, shared group chats, and routines for work that starts without a prompt.

 The presence cues and Bot roster surface are the trust-design primitives that make a multi-Bot environment navigable: the user can see, at a glance, which Bots are active, which are idle, and which have produced output since the last visit — the equivalent of a team room where colleagues signal availability. 

Each Bot has memory, its own computer environment, browser access, files, routines, and can coordinate with other Bots across recurring business tasks.

Skills describe how a task should be performed, while routines can schedule a Bot to perform a workflow; xAI recommends testing workflows before turning them into recurring routines and keeping consequential actions behind approval.

 That last sentence is the governance principle embedded in the product design: the escalation from ad-hoc task to recurring routine should be deliberate, and the consequential-action approval gate should persist even in routine mode.



xAI adds tighter X integration in Grok Bot, with account linking, API credits, and post, timeline, and mention tools; Grok Bot now has a tighter integration with X — connect an X account in Grok Bot and xAI creates a developer account if the user does not have one; paid Grok Bot users get free X API credits to start.

 The X account integration is the connector-trust design event worth tracking: linking a Grok Bot to a live social account with post and timeline access means the Bot's consequential-action surface now extends to public communications — precisely the domain where the approval-gate recommendation matters most.

---

### Perplexity: Connector Approval Granularity and the Portable Computer Arc

Perplexity's most significant agentic UX development in this window is the deepening of **connector approval granularity** in Computer — a trust-design refinement that gives users and enterprise admins precise control over when the agent pauses before acting on any connected tool.



Users can set a connector tool to Always ask when they want Perplexity to pause before it acts, with the ability to approve a single action, allow the tool for the rest of the thread, or deny it; recurring runs inherit thread-level grants.

 The interaction-design significance of the three-level approval model — approve once, allow for thread, deny — is that it matches the natural risk calculus users apply to different tool actions: a one-off calendar lookup warrants a different approval posture than a recurring email-send routine. Thread-level grants reduce approval friction for users who have validated a tool action within a session, while recurring-run inheritance means automation does not constantly re-surface approvals for well-understood tasks.



Admins can control which third-party connectors — such as Gmail, Slack, GitHub, and Salesforce — are available to users; individual connectors can be disabled at the organisation level from Organization settings → Permissions, preventing users from authenticating or using those integrations within Computer tasks; this allows admins to restrict data flow to only approved services.

 The admin-level connector governance surface — disable by connector, not by feature — is the enterprise trust primitive that pairs with the user-level approval controls: administrators define which tools are reachable at all, and users then control the approval posture for the tools they can reach. This two-layer model is the correct architecture for enterprise agentic deployments where data-egress boundaries and user autonomy must coexist.

On the infrastructure side, 

Portable Computer, launched August 25 with NVIDIA, is the local version: the entire runtime — orchestrator model, subagent model, agent harness, tool sandbox, and app connectors — runs on hardware the user owns; local steps carry zero token cost, and escalation to Perplexity's cloud models is opt-in and gated per step; the positioning is explicit — Perplexity is pitching this at people whose most valuable work involves data they'd rather keep on their own machines, including private codebases, confidential financial documents, and sensitive material.

Portable Computer is Linux-only at launch, with Windows targeted for September 2026.

 The per-step cloud escalation gate is the trust-design detail that makes Portable Computer's privacy claim credible rather than aspirational: the user controls exactly which steps leave the local runtime, making the data-boundary explicit and deliberate at every task step rather than implicitly managed by a remote orchestrator.

---

## The Bigger Picture: Computer Use Goes Mainstream, Agent Persistence, and the Unified Surface

The 48 hours ending September 4, 2026 mark the moment computer use, persistent agents, and unified surface consolidation converge from parallel trends into a single coordinated wave. OpenAI's GPT-6 Astra establishes computer use — operating software UIs directly, without APIs — as a first-class agentic interaction model, and the note-keeping architecture it introduces for Codex solves the memory-loss problem that has made long-running coding agents frustrating since their introduction. Microsoft's VS Code Agent Host decouples agent sessions from window lifecycle, making the agent's persistence architectural rather than a UX promise. Grok Bot's expansion beyond beta formalises the Bot-roster design model — persistent named identities rather than disposable sessions — as a mainstream product pattern rather than an experimental one. And Google's September Android Drop extends Gemini's memory surface to physical-world objects without hardware, while Perplexity deepens the per-tool approval granularity that makes agentic delegation trustworthy rather than opaque. These are not five separate features. They are five simultaneous answers to the same design question: once an agent can persist beyond a session, operate external software, remember across context windows, and act autonomously on recurring routines, what design surfaces make its authority legible and its actions governable? The answers emerging in this window — Bot roster presence cues, cross-window searchable notes, Agent Host session persistence, per-tool approval gates, and in-session classifier rule editing — are collectively the trust-design vocabulary of the next era of agentic software. The platforms that ship that vocabulary coherently, where the user always knows what the agent is doing, why it has authority to do it, and what stands between its decision and its action, will define the interaction model of enterprise AI through 2027.

---

## References

[1] GitHub / Anthropic. (2026). *Releases · anthropics/claude-code*. [https://github.com/anthropics/claude-code/releases](https://github.com/anthropics/claude-code/releases)

[2] Releasebot. (2026). *Claude Code Updates by Anthropic — September 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] Gradually AI. (2026). *Claude Code Changelog (September 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[4] OpenAI. (2026). *GPT-6 Astra: A new generation of intelligence*. [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)

[5] 9to5Mac. (2026). *OpenAI releasing major upgrade to ChatGPT and Codex with GPT-6 Astra*. [https://9to5mac.com/2026/09/03/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/](https://9to5mac.com/2026/09/03/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/)

[6] MarketScale. (2026). *OpenAI's GPT-6 Astra Aims to Simplify Software Use*. [https://www.marketscale.com/industries/software-and-technology/openais-gpt-6-astra-pitch-is-to-skip-integrations-and-run-the-software-ui-itself](https://www.marketscale.com/industries/software-and-technology/openais-gpt-6-astra-pitch-is-to-skip-integrations-and-run-the-software-ui-itself)

[7] 9to5Google. (2026). *Sept. 2026 Android Drop: Find Hub Remembered, Motion Assist, Google Messages*. [https://9to5google.com/2026/09/01/september-2026-android-drop/](https://9to5google.com/2026/09/01/september-2026-android-drop/)

[8] Android Central. (2026). *No tracker tag? Gemini can now store item locations right in Find Hub*. [https://www.androidcentral.com/apps-software/no-tracker-tag-gemini-can-now-store-item-locations-right-in-find-hub](https://www.androidcentral.com/apps-software/no-tracker-tag-gemini-can-now-store-item-locations-right-in-find-hub)

[9] Android Authority. (2026). *Google Home gets a smarter Gemini with new upgrades*. [https://www.androidauthority.com/google-home-gemini-upgrades-september-2026-3706505/](https://www.androidauthority.com/google-home-gemini-upgrades-september-2026-3706505/)

[10] Visual Studio Code. (2026). *Visual Studio Code 1.136 Release Notes*. [https://code.visualstudio.com/updates/v1_136](https://code.visualstudio.com/updates/v1_136)

[11] Releasebot. (2026). *Visual Studio Code Updates by Microsoft — September 2026*. [https://releasebot.io/updates/microsoft/visual-studio-code](https://releasebot.io/updates/microsoft/visual-studio-code)

[12] Unite AI. (2026). *Microsoft Merges Copilot and Microsoft 365 Copilot Into a Single App*. [https://www.unite.ai/microsoft-merges-copilot-and-microsoft-365-copilot-into-a-single-app/](https://www.unite.ai/microsoft-merges-copilot-and-microsoft-365-copilot-into-a-single-app/)

[13] Releasebot. (2026). *xAI Release Notes — September 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[14] AIToolsReview. (2026). *Grok Bot: xAI's Always-On AI Agents, Explained (September 2026)*. [https://aitoolsreview.co.uk/insights/grok-bot-agent-launch](https://aitoolsreview.co.uk/insights/grok-bot-agent-launch)

[15] SuperGrok Online. (2026). *Grok Bot Guide: Everything You Need to Know in 2026*. [https://supergrok.online/grok-bot-guide/](https://supergrok.online/grok-bot-guide/)

[16] Releasebot. (2026). *Perplexity Release Notes — August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[17] Perplexity Help Center. (2026). *Computer for Enterprise*. [https://www.perplexity.ai/help-center/en/articles/13901210-computer-for-enterprise](https://www.perplexity.ai/help-center/en/articles/13901210-computer-for-enterprise)

[18] Vellum AI. (2026). *Official Perplexity Computer Breakdown (2026)*. [https://www.vellum.ai/blog/official-perplexity-computer-breakdown](https://www.vellum.ai/blog/official-perplexity-computer-breakdown)

---