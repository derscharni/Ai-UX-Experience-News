# UX Briefing: Voice as an Agentic Control Surface, Copilot UX Components, and the Notebook Integration Wave

**October 29, 2026**

Good morning. The 48 hours ending October 29, 2026 are marked by a convergence across five products on a single structural question: what happens when the voice layer becomes the primary orchestration surface for multi-agent, multi-session agentic workflows — and what new trust and governance primitives does that require? **Perplexity** ships the window's most consequential interaction-design advance: **Voice Mode on GPT-Live-1**, announced October 28, which converts voice from a Q&A shortcut into a full agentic orchestration layer — a single spoken session can now drive multiple Computer sessions simultaneously, spawn new tasks mid-conversation, and create and manage Projects without touching a keyboard. **Microsoft Copilot** delivers what the SharePoint Framework community has been tracking since September: **Copilot UX Components reach general availability on October 28 with SPFx 1.24**, shipping interactive dashboards, forms, and business actions directly into the Copilot conversation thread — converting the chat reply from a text response into a live, actionable enterprise UI surface. **Google Gemini** closes the navigation gap between its AI chat surface and its research-and-knowledge tool with the **Gemini Notebook Connected App**, rolling out October 23–24, which makes Gemini Notebook addressable by `@mention` from any Gemini chat and allows Gemini to invoke it autonomously on relevant prompts — the deepest integration yet between Google's conversational and knowledge-management layers. **Claude/Anthropic** continues the weekly cadence of Claude Code reliability and UX improvements, with the current release cluster adding the **Claude Mods plugin system**, prompt recovery, and a suite of cloud session and MCP fixes that collectively improve multi-agent session resilience. **Grok (xAI)** ships a dashboard navigation and session continuity cluster through **Grok Build 1.0.69**, establishing folder-based agent grouping and cross-folder session resume as the correct architecture for multi-project coding agent workflows.

---

## At a Glance: October 29 Highlights

Today's window is defined by two simultaneous movements: the voice modality is being elevated from a convenience shortcut to a full agentic control surface, while enterprise platforms are shipping the developer primitives — Copilot UX components, Gemini Notebook as a Connected App — that will determine how rich, interactive, and trusted the AI conversation surface becomes inside business workflows.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code October cluster ships the Mods plugin system with session-state hooks, prompt recovery, name-based session filtering, and a suite of cloud session and MCP reliability fixes — including a critical fix for subagents unable to use late-connecting MCP tools** — Claude Mods introduces plugin hooks for customizing behavior and accessing session state; pressing Up on an empty prompt now restores cleared drafts including pasted text and images; the fix for MCP tools from late-connecting servers repairs an entire class of multi-agent pipeline failures. [1][2][3] |
| **ChatGPT** | **Codex 0.165.0 ships the Google Cloud Vertex AI built-in provider, GPT-6.1 Terra as the new default model, memory v2 enabled for fresh profiles, and experimental attached thread forks; Codex 0.164.0 added reusable /presets slots and inline /model and /permissions arguments** — the Vertex AI provider adds GCP-native routing without external configuration; memory v2 default plus external-agent memory import enables persistent context across sessions; /presets gives terminal users reusable prompt-and-model configurations without re-typing. [4][5][6] |
| **Google Gemini** | **Gemini Notebook becomes a Connected App in the Gemini app (October 23–24), enabling @Gemini Notebook mentions in chat, autonomous invocation on relevant prompts, and full CRUD operations on notebooks and sources via natural language; rolls out by default globally except EEA** — users can create, edit, delete notebooks and manage sources directly from a chat prompt; Gemini auto-detects when Notebook is relevant and invokes it without an @mention; admin governance available via Settings > Connected Apps. [7][8][9] |
| **Microsoft Copilot** | **Copilot UX components reach general availability on October 28 with SharePoint Framework 1.24 — interactive dashboards, forms, and business actions rendered directly inside the Copilot conversation, built with React/TypeScript, hosted by Microsoft 365, with built-in SSO and no separate auth server required** — components follow the MCP Apps model and can surface line-of-business data, approvals, employee service tasks, and KPI cards inline; deployment uses the existing SharePoint App Catalog; mobile, Cowork, and the new plug-in model are planned follow-on. [10][11][12] |
| **Grok (xAI)** | **Grok Build 1.0.69 adds folder-based agent dashboard grouping, cross-folder /resume for session continuity across projects, and worktree reliability improvements; Grok Voice 3.0 now listed on the xAI API release notes as available with the same deprecation notice for Voice 2.0** — dashboard directory grouping surfaces a folder-path header and agent count above each folder; /resume now finds sessions from every folder with the current folder's sessions listed first; branch and folder location labels move to the dispatch box border for cleaner layout. [13][14][15] |
| **Perplexity** | **Voice Mode upgrades to GPT-Live-1 on October 28 for Pro and Max subscribers on Mac and web: a single voice session can now orchestrate multiple Computer sessions simultaneously, start new tasks mid-conversation, and create and manage Projects without a keyboard; full-duplex voice means the model keeps listening while speaking** — this converts voice from a Q&A shortcut into a multi-agent orchestration surface; GPT-Live-1's full-duplex architecture eliminates the turn-taking constraint that previously broke voice-to-Computer continuity; the update complements the October 20 fully local Computer launch. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Mods, Prompt Recovery, and MCP Reliability Close the Multi-Agent Session Gap

Anthropic's most structurally significant Claude Code interaction-design work in this window is not a single headline feature but a coherent cluster of improvements that together address the three failure modes most frequently cited by practitioners running complex multi-agent pipelines: plugin customisation, session continuity under disruption, and MCP tool availability at subagent spawn time.

The headline addition is the **Claude Mods plugin system**. 

October brought a Claude Mods system with plugin hooks for customising behavior and accessing session state.

 The interaction-design significance of Mods is that it converts Claude Code from a product with fixed session behaviour into a platform where operators can define their own hooks for permission decisions, output routing, and session-state inspection — the same extensibility model that makes mature developer tools governable at enterprise scale. 

The built-in You Should Know mod watches for potential issues during sessions,

 establishing a precedent for proactive in-session safety signals that operate without a separate monitoring pipeline.

The companion UX recovery improvements are the session-continuity fixes that matter most to practitioners running long or interrupted sessions. 

Prompt recovery allows pressing Up on an empty prompt to restore cleared drafts including pasted text and images.

Name-based session filtering with `n:<text>` in the agents view and session search with Ctrl+F

 converts the session management surface from a scroll-and-recognise model to a search-by-intent model — critical when an operator is running multiple named agent sessions across projects. 

The Program Status Protocol (OSC 7501) support shows Claude's working state in compatible terminals,

 giving operators an ambient status signal for long-running sessions without requiring them to stay focused on the terminal output.

The reliability fix that has the highest structural impact on production multi-agent deployments is the MCP tool access repair. 

The fix for subagents being unable to use MCP tools from servers that finish connecting after the subagent starts

 closes a class of failures that were particularly difficult to diagnose: from the main session's perspective, the MCP server appeared healthy, but subagents spawned before the connection completed silently lost access to the tools they were expected to use. This is the correct design: subagent tool availability should be determined by the server's connected state at the time of the tool invocation, not at the moment of subagent spawn — and the fix brings Claude Code's subagent MCP behaviour into alignment with that principle.

---

### ChatGPT / OpenAI: Codex 0.165.0 Brings Vertex AI, Memory V2 Defaults, and the /Presets Surface

OpenAI's interaction-design work reaching practitioners in this window arrives through two Codex releases — 0.164.0 and 0.165.0 — that together make significant advances on three agentic-UX fronts: multi-provider routing, persistent session memory, and reusable configuration management.



Codex 0.165.0 released a broad update with a built-in Google Cloud Vertex AI provider, GPT-6.1 Terra, improved session navigation, and memory v2 enabled for fresh profiles.

 The Vertex AI addition is the routing-design change with the broadest enterprise reach: 

the built-in Google Cloud Vertex AI provider is configured with `model_provider = "gcp"`,

 meaning enterprise operators who run their workloads inside GCP can now route Codex sessions to Vertex-hosted models without building or maintaining a separate provider integration. This is the correct design for enterprise agentic deployments that have data-residency or governance obligations tied to their cloud provider.

The memory advance in 0.165.0 changes the default interaction contract for new users. 

Memory v2 is now enabled by default for fresh profiles, with support added for importing external-agent memories into it.

 The external-agent memory import is the UX primitive that will matter most to practitioners running heterogeneous pipelines: a developer who has built up useful context in Claude Code or another agent surface can now import that memory into a Codex session, rather than starting from a blank context that requires re-establishing project state from scratch. 

The release also added experimental attached thread forks to the app-server API, and enabled reasoning effort changes during a conversation by default for supported models.

 In-conversation reasoning effort changes are the correct temporal-UX design for long Codex sessions: a developer can escalate from fast-mode reasoning to deeper reasoning mid-task, at the point where the agent encounters an ambiguous architectural decision, without starting a new session.

On the reusable-configuration front, **Codex 0.164.0's /presets surface** is the practitioner-facing UX advance with the most immediate workflow impact. 

New features include saving reusable prompts and slash commands in ten numbered /presets slots with a keyboard menu for quick access, and setting model, reasoning effort, speed, and permission profiles directly with inline /model and /permissions arguments.

 The /presets design is the correct solution to a friction point that affects every practitioner who runs different project types with different configuration requirements: rather than reconfiguring model, effort level, and permission profile at the start of each session, the developer stores the configuration for each project type in a preset and invokes it with a single keypress.

---

### Google Gemini: Gemini Notebook as a Connected App Collapses the Research-to-Conversation Gap

Google's most structurally significant Gemini interaction-design advance in this window is the integration that closes the navigation gap between its conversational AI surface and its knowledge-management tool: the **Gemini Notebook Connected App**, which began rolling out October 23–24.



Gemini Notebook is now also available as a Connected App in the Gemini app, and this new integration allows users to manage and query notebooks directly within their chats using natural language.

 The interaction-design shift this enables is the elimination of context-switching between surfaces: previously, a user who wanted to save a finding from a Gemini conversation into a research notebook had to navigate to a separate app, open the relevant notebook, and manually paste the content. 

Users can type `@Gemini Notebook` in a Gemini chat to quickly create new notebooks, add sources, save key notes, or retrieve information from existing notebooks — and Gemini can also automatically detect when to use the Gemini Notebook Connected App for relevant prompts.



The automatic invocation behaviour is the trust-design detail that warrants the most practitioner attention. 

Gemini can call on the Notebook Connected App by itself when it judges a prompt to be relevant, and if users don't want that, they can turn it off in Settings > Connected Apps.

 This is the correct governance architecture for an autonomously-invoked tool: the default state is proactive assistance (Gemini calls Notebook when it seems relevant), but the user retains a clear, accessible opt-out path in a named settings location rather than needing to hunt for a buried toggle. 

The integration is enabled by default for users globally, except in the European Economic Area, where it is off by default,

 — a jurisdiction-aware default that reflects the EEA's stricter consent requirements for data-sharing between services, and sets the correct precedent for how ambient AI integrations should handle regulatory geography.

The range of operations the Notebook Connected App supports covers the full notebook lifecycle: 

users can create, edit, or delete a notebook; add, update, or delete sources; list notebooks and their sources; and answer questions using context from their notebooks.

 This is the correct interaction-design scope for a first-party Connected App — not just read-only retrieval (which would cover the lookup use case but leave the capture use case unsatisfied), but full CRUD, making the integration a genuine bidirectional bridge between conversation and knowledge base.

---

### Microsoft Copilot: Copilot UX Components Reach GA, Converting Chat Replies into Live Enterprise UI Surfaces

Microsoft's most consequential Copilot interaction-design release in this window is not a new agent feature or a canvas update but a developer primitive that will reshape what a Copilot chat reply can contain: **Copilot UX Components GA with SharePoint Framework 1.24**, which shipped October 28 and is the most significant expansion of the Copilot conversation rendering surface since Copilot launched.



Copilot UX components are generally available with SharePoint Framework (SPFx) 1.24, bringing interactive dashboards, forms, and business actions directly into the Copilot conversation.

 The interaction-design implication is fundamental: a Copilot response no longer has to be a block of text followed by links. 

Developers can now embed interactive dashboards, forms, and business actions directly inside the Microsoft Copilot conversation, built with React, TypeScript, or plain JavaScript — and Microsoft 365 hosts and routes the components automatically inside the customer's tenant, with built-in single sign-on, so teams skip building separate web servers or auth flows.

 The automatic hosting with built-in SSO is the trust-design primitive that makes Copilot UX components safe for enterprise deployment: the component runs inside the tenant's own Microsoft 365 infrastructure, subject to the same governance policies as any other SharePoint solution, rather than calling out to a third-party endpoint that the security team has to independently evaluate.



The October 28 announcement says components follow the Model Context Protocol (MCP) Apps model and can be built using React, TypeScript, or other JavaScript frameworks; an SPFx solution packages a declarative agent and its components together, while Microsoft 365 handles component hosting and routing inside the tenant.

 The MCP Apps model alignment is the architectural detail that will matter most for long-term interoperability: by building Copilot UX components on MCP, Microsoft is ensuring that the same component a developer builds for Copilot can, in principle, be addressed by any external agent that supports MCP — not just Microsoft's own. 

Scenario samples include line-of-business data, sales dashboards, customer 360 views, stock levels, expenses and pay slips, employee services, time off, help desk, travel booking, onboarding tasks, and recognition.

Availability has important boundaries: users need a Microsoft Copilot add-on license, and supported clients are the browser, desktop, and Microsoft Teams desktop/browser experiences.

Mobile support, the new plug-in model, Cowork, and additional Copilot surfaces are planned as follow-on work.

 The phased availability is the correct rollout design: ship the governed, desktop-first surface to establish the platform contract, and extend to mobile and additional surfaces once the deployment and governance patterns are established in production.

---

### Grok (xAI): Grok Build 1.0.69 Completes the Multi-Project Dashboard Navigation Architecture

SpaceXSI's Grok Build interaction-design advance in this window is the completion of a navigation architecture overhaul that has been building across the 1.0.65–1.0.70 release cluster: **Grok Build 1.0.69**, which establishes folder-based agent grouping and cross-folder session resume as the standard multi-project navigation model for the terminal-based coding agent.



Grok Build 1.0.69 improves dashboard navigation with folder-based agent grouping, clearer branch and folder labels, and session resume across folders; it also updates welcome-menu shortcuts, retires an unused setting, improves config diagnostics, and returns users to the shell faster when quitting.

 The folder-based grouping design solves the most common multi-project operator complaint about previous Grok Build versions: when running agent sessions across multiple repositories, the dashboard presented a flat list ordered by recency, which made it difficult to locate a specific session without scrolling through unrelated projects. 

The dashboard directory grouping now shows a header with the folder path and agent count above each folder of agents, and the dashboard location (branch and folder) now sits on the dispatch box top border instead of its own header row.



The cross-folder `/resume` capability is the temporal-UX advance that most directly changes the multi-project developer workflow pattern. Previously, resuming a session in a different project directory required the operator to `cd` to that directory first — a small friction that, multiplied across multiple daily context-switches, added meaningful overhead to operators managing several parallel agentic workstreams. The new `/resume` command finds sessions across all folders, with the current folder's sessions listed first — the correct priority ordering for the common case where the operator wants to resume a session in their current project, while preserving access to all other sessions without navigation. 

Grok Build 1.0.65 established the foundation: `/resume` search finds sessions from other folders, tolerates typos, and also matches the commands, file paths, and replies in a session.

 1.0.69 completes this by surfacing the capability at the dashboard level, not just through a search command.

The companion worktree reliability fixes in this cluster address a class of failures that affect operators who use worktrees heavily for parallel branch development. 

A worktree name that is already taken is now refused instead of getting a numbered suffix, and a name whose folder was deleted by hand can be used again.

 These are the correct failure-mode designs: a silent rename (adding a numeric suffix) produces a session that the operator didn't name intentionally, which breaks the name-based session filtering that 1.0.65 introduced; refusing the duplicate and prompting for a new name keeps the session namespace clean and searchable.

---

### Perplexity: Voice Mode on GPT-Live-1 Makes Voice the Primary Agentic Orchestration Interface

Perplexity's most structurally significant interaction-design release in this window is not a new agent capability but a fundamental reconfiguration of the voice modality's role in the Computer product: the **Voice Mode upgrade to GPT-Live-1**, announced October 28, which converts voice from a single-session Q&A shortcut into a multi-agent orchestration surface.



Perplexity's voice mode now runs on OpenAI's gpt-live-1 model, with it users can run multiple sessions at once and manage tasks and projects through conversation, and the upgrade covers both the Mac app and the web interface.

 The agentic-UX significance is precisely what the model swap enables: 

a single spoken session can drive several Perplexity Computer sessions at once, start new tasks mid-sentence, and create or manage Projects without touching a keyboard.

 This is the correct interaction model for a voice-orchestrated agentic workflow: the voice layer becomes the dispatcher that routes work to background Computer sessions, rather than a separate modality that the user has to exit in order to start agentic tasks.

The full-duplex architecture of GPT-Live-1 is the technical primitive that makes this orchestration pattern viable. 

The headline capability of gpt-live-1 is full-duplex voice — the system can keep listening while it is still speaking.

 In the context of multi-session Computer orchestration, this is not an incremental improvement but a qualitative change: with half-duplex voice, a user who wanted to interrupt a running Computer session to redirect it had to wait for the agent to finish speaking before their input was registered. Full-duplex eliminates that latency, making the voice-to-Computer control loop feel like a natural conversation rather than a transactional turn-taking protocol. 

On the Mac, Perplexity's Personal Computer can read and write files in folders you connect, operate native apps such as Mail and Messages, and ask for on-device authorisation before sensitive steps — and a voice session now manages all of it.



The trust-design question that this release surfaces — and that practitioners should be actively assessing — is the dependency chain it creates. 

Perplexity says its voice mode runs on GPT-Live-1; in ChatGPT Voice, OpenAI began rolling out GPT-Live-1.1 on 15 October 2026, two weeks before this switch.

Perplexity's voice leg is now rented from OpenAI and cannot be substituted — GPT-Live-1 exposes exactly one endpoint, `v1/live/sessions`, and is explicitly not a drop-in for the Realtime API.

 This is a meaningful architectural constraint: if OpenAI changes the GPT-Live-1 endpoint, updates the model silently, or introduces latency, it directly affects the voice-to-Computer orchestration experience in Perplexity — a dependency that Perplexity's enterprise users should factor into their SLA expectations and that Perplexity's design team will eventually need to resolve with either model redundancy or an alternative voice path.

---

## The Bigger Picture: Voice as an Agentic Control Surface, Copilot UX Components, and the Notebook Integration Wave

The 48 hours ending October 29, 2026 reveal a maturing phase of the Agent2Agent2Human design space in which the frontier has shifted from "what can the agent do" to "through which surface can the human most naturally direct multiple agents at once." Perplexity's Voice Mode on GPT-Live-1 is the clearest articulation of the new question: by making a single spoken session the dispatcher for multiple parallel Computer sessions, Perplexity has proposed that voice — not a chat box, not a canvas, not a dashboard — is the correct interaction surface for human-to-multi-agent orchestration at ambient frequency. This is a significant bet, and it is only viable because full-duplex voice eliminates the turn-taking constraint that made voice feel like a second-class interface. Microsoft's Copilot UX Components GA is the enterprise-layer answer to the same question from a different angle: when the Copilot conversation can render an interactive sales dashboard, an approval form, or an employee onboarding checklist inline, the conversation becomes the primary work surface — not a gateway that routes the user to a separate application. Google's Gemini Notebook Connected App makes the same move at the knowledge-management layer: by collapsing the boundary between conversation and notebook, Google ensures that the agent's research surface and the user's knowledge-capture surface are co-present in the same conversation thread, with autonomous invocation and a clear opt-out governance path. Claude Code's Mods system and MCP reliability fixes represent Anthropic's contribution to the same trend from the infrastructure layer: if voice-orchestrated, multi-session, multi-agent workflows are to be trusted in production, the underlying agent platform must be customisable enough for operators to define their own permission and safety hooks, and reliable enough that subagent tool access doesn't silently degrade when MCP servers connect late. The window's Grok Build dashboard overhaul completes the picture from the developer-tools layer: a coding agent platform that makes it easy to find, resume, and manage sessions across multiple projects is one that practitioners will actually trust with continuous, multi-project background work. Taken together, these advances define the design agenda for the next phase: the platforms that capture the deepest user trust will be the ones that make multi-agent work feel as natural through a voice session or a conversation thread as it currently feels through a purpose-built dashboard — while preserving the governance, auditability, and opt-out controls that enterprise adoption requires.

---

## References

[1] releasebot.io. (2026). *Anthropic Release Notes — October 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[2] releasebot.io. (2026). *Claude Code Updates by Anthropic — October 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] agentgid.com. (2026). *Claude Code Changelog: What's New in October 2026*. [https://agentgid.com/agents/claude-code/changelog/](https://agentgid.com/agents/claude-code/changelog/)

[4] releasebot.io. (2026). *Codex Updates by OpenAI — October 2026*. [https://releasebot.io/updates/openai/codex](https://releasebot.io/updates/openai/codex)

[5] releasebot.io. (2026). *OpenAI Release Notes — October 2026*. [https://releasebot.io/updates/openai](https://releasebot.io/updates/openai)

[6] developers.openai.com. (2026). *ChatGPT & Codex Changelog — October 2026*. [https://developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

[7] workspaceupdates.googleblog.com. (2026). *Take actions on your notebooks from Gemini Notebook directly in the Gemini app*. [https://workspaceupdates.googleblog.com/2026/10/take-actions-on-your-notebooks-from-Gemini-Notebook-directly-in-the-Gemini-app.html](https://workspaceupdates.googleblog.com/2026/10/take-actions-on-your-notebooks-from-Gemini-Notebook-directly-in-the-Gemini-app.html)

[8] 9to5google.com. (2026). *Gemini Notebook now available as Connected App for deeper integration*. [https://9to5google.com/2026/10/23/gemini-notebook-connected-app/](https://9to5google.com/2026/10/23/gemini-notebook-connected-app/)

[9] androidpure.com. (2026). *Gemini Turns On Its Notebook Connected App by Default Outside the EEA*. [https://www.androidpure.com/gemini-notebook-connected-app/](https://www.androidpure.com/gemini-notebook-connected-app/)

[10] devblogs.microsoft.com. (2026). *Copilot UX components are generally available: bring interactive experiences into Copilot*. [https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-are-generally-available-bring-interactive-experiences-into-copilot/](https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-are-generally-available-bring-interactive-experiences-into-copilot/)

[11] visualstudiomagazine.com. (2026). *Copilot UX Components Reach GA with SharePoint Framework 1.24*. [https://visualstudiomagazine.com/articles/2026/10/28/copilot-ux-components-reach-ga-with-sharepoint-framework-1-24.aspx](https://visualstudiomagazine.com/articles/2026/10/28/copilot-ux-components-reach-ga-with-sharepoint-framework-1-24.aspx)

[12] learn.microsoft.com. (2026). *Overview of the SharePoint Framework (SPFx)*. [https://learn.microsoft.com/en-us/sharepoint/dev/spfx/sharepoint-framework-overview](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/sharepoint-framework-overview)

[13] x.ai. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[14] releasebot.io. (2026). *Grok Build Updates by xAI — October 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[15] releasebot.io. (2026). *xAI Release Notes — October 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[16] 9to5mac.com. (2026). *Perplexity upgrades Mac app with ChatGPT-powered voice mode*. [https://9to5mac.com/2026/10/28/perplexity-upgrades-mac-app-with-chatgpt-powered-voice-mode/](https://9to5mac.com/2026/10/28/perplexity-upgrades-mac-app-with-chatgpt-powered-voice-mode/)

[17] ithinkdiff.com. (2026). *Perplexity Voice Mode on Mac Gets OpenAI's GPT-Live-1*. [https://www.ithinkdiff.com/perplexity-voice-mode-gpt-live-1-mac/](https://www.ithinkdiff.com/perplexity-voice-mode-gpt-live-1-mac/)

[18] orcarouter.ai. (2026). *Perplexity Voice Mode Now Runs on GPT-Live-1: What Changed*. [https://www.orcarouter.ai/blog/perplexity-voice-mode-gpt-live-1](https://www.orcarouter.ai/blog/perplexity-voice-mode-gpt-live-1)