# UX Briefing: Mod Consent Logging, Dots Multi-Model Routing, and the Floating Overlay Wave

**November 04, 2026**

Good morning. The 48 hours ending November 4, 2026 are defined by three simultaneous design movements: an **agent consent and transparency tightening** at the session layer, with Claude Code 2.1.318 introducing persistent records of users' mod-activation answers and the Microsoft Copilot Autopilot governance layer reaching Frontier rollout; a **multi-model routing maturation** inside persistent agents, with OpenAI expanding Dots to include GPT-6.1 Terra alongside Astra so that each Dot can automatically select the best model per sub-task; and a **surface unification wave** that continues to absorb discrete app-entry points into the main chat interface. **Claude/Anthropic** ships **Claude Code 2.1.318** on November 4, adding a session-level consent record for mod activation and fixing a cascade of configuration and IDE-extension edge cases. **ChatGPT/OpenAI** posts a landmark trust-design update to the Dots product page on November 3: **GPT-6.1 Terra joins GPT-6 Astra** as a model powering Dots, enabling each persistent agent to route different sub-tasks to different models automatically — the first native multi-model dispatch inside OpenAI's always-on agent layer. **Google Gemini** surfaces two simultaneous design convergences: the **Gemini-in-Gmail floating panel redesign** spotted in Gmail v2026.10.26, replacing the bottom-sheet with a pill-shaped expandable overlay; and the **Gems-to-Skills migration clock ticking**, with the November 17 cutover now two weeks away and Skills invocable via `/` in the main prompt box. **Microsoft Copilot** brings its **Autopilot always-on agent** into November Frontier rollout while confirming that **Agent 365 provides the governance layer** — governed identity, audit records, and a 30-day inactivity retirement rule — alongside the interactive **Excel canvas** beginning its worldwide rollout. **Grok (SpaceXSI)** continues the stabilisation of the grok-imagine-image-2.0 migration following the November 2 retirement of the grok-imagine-image-quality slug, with nightly builds confirming a scheduler token-boundary fix on November 3–4. **Perplexity** matures its **Orchestrator API** (private preview) as the multi-model access primitive of record, with Gemini 4 Argon now live in the Agent API and the Orchestrator endpoint acting as a drop-in base-URL replacement for both OpenAI and Anthropic SDK integrations.

---

## At a Glance: November 4 Highlights

Today's window is defined by the agent autonomy layer filling in its remaining gaps: consent records, multi-model dispatch, persistent-agent governance, and floating UI surfaces that bring the AI assistant into the host app rather than demanding the user navigate out to it.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code 2.1.318 ships November 4 with a consent record for mod activation answers, plus fixes for plugin validation, non-interactive config corruption, and VS Code sign-in diagnostics; the IDE extension no longer auto-installs when Claude Code starts in an IDE terminal** — the mod-activation record is the most trust-significant change: when Claude Code asks permission to enable a mod it writes in a session, the user's answer is now stored, giving operators an auditable trail of which session-level capabilities a user explicitly authorised. [56-1,56-2,57-1,57-2] |
| **ChatGPT** | **OpenAI updates the Dots product page on November 3 to add GPT-6.1 Terra alongside GPT-6 Astra; Dots will automatically select the best model for each part of a task and can combine multiple models in a single request; GPT-6.1 Terra was already in Codex 0.166.0; Chat and Work tab merge continues expanding to select users** — the multi-model dispatch removes the last remnant of user-managed model selection inside a persistent agent session; a Dot no longer commits to one model for its entire lifecycle. [109-1,109-4,109-5,109-6,114-3,114-4,115-4] |
| **Google Gemini** | **A floating pill-shaped Gemini overlay spotted in Gmail v2026.10.26 on November 3 replaces the bottom-sheet design and can be expanded with a grab handle; the overlay adds voice input and a plus menu with Drive, Gmail, and web source toggles; Gems-to-Skills migration is now 13 days away (November 17)** — the Gmail floating panel brings the Gemini app's interaction model into the host email surface rather than requiring a full-screen context switch; source-scope toggles directly inside the panel give users inline control over what data Gemini searches. [100-5,100-7,100-8,100-9,100-10,22-3,22-13,22-14] |
| **Microsoft Copilot** | **Copilot Autopilot enters November Frontier rollout — the always-on cloud agent (formerly Scout) gives users a name, a role, and a goal, then runs continuously across Teams, Outlook, and documents; each Autopilot instance has its own Microsoft Entra identity, cloud workspace, and audit record; Agent 365 governs permissions, spending, and a 30-day inactivity retirement rule; the interactive Excel canvas (Interactive Canvas) begins worldwide rollout in November** — Autopilot's governed identity model is the correct trust-design architecture for a persistent background agent: actions are attributable to a named, governed agent principal rather than hidden behind whoever initiated the session. [73-3,73-4,118-5,120-10,120-11,120-14,126-3,126-4,126-13,73-6,73-7] |
| **Grok (SpaceXSI)** | **Nightly Grok Build 2026.11.3 (November 3) and 2026.11.4 (November 4) ship a scheduler fix: interval tokens are no longer sliced at a byte boundary, preventing malformed token sequences in scheduled agent tasks; the grok-imagine-image-quality API slug retirement (November 2) is complete — requests are now automatically served by grok-imagine-image-2.0 at low quality with no request shape change** — the scheduler byte-boundary fix is the operational safety patch of the window: a scheduled multi-step Grok Build task that produced malformed tokens at interval edges could silently produce corrupted tool call sequences. [85-4,38-3,38-7,45-4,45-5] |
| **Perplexity** | **The Perplexity Orchestrator API (private preview) provides unified access to open-weight models at api.perplexity.ai/orchestrator/v1 as a drop-in base-URL replacement for both OpenAI Chat Completions and Anthropic Messages SDKs; Gemini 4 Argon is now live in the Agent API; older OpenAI model IDs (GPT-5.4, 5.2, 5.1, 5.0) are retired from both the Agent and Orchestrator APIs from October 24** — the dual-SDK compatibility means a developer can switch from either an OpenAI or Anthropic integration to Perplexity's orchestrated open-weight models with a single base URL change and no client-code modification. [94-2,94-4,94-5,91-1,91-4] |

---

## Product Highlights

### Claude / Anthropic: 2.1.318 Introduces Session-Level Mod Consent Records

Anthropic's most interaction-design-significant Claude Code release in this window is **Claude Code 2.1.318**, which shipped on November 4 and addresses a trust-design gap that has existed since session-level mods were introduced: until now, when Claude Code asked a user whether to activate a mod it had written for the session, the answer was not recorded anywhere accessible to operators or the user themselves.



Claude Code v2.1.318 was built on 2026-11-03T19:21:35Z and added a record of the user's answer when Claude Code asks to turn on the mods it writes in a session.

 This is a targeted consent-trail advance: session-level mods are capabilities Claude Code generates on the fly to extend its own toolset, and the decision to enable them is a meaningful permission grant that now has a durable record. The UX implication for operators building on Claude Code is that they can now retrieve a verifiable log of which session-level capabilities a user explicitly authorised, rather than having to infer capability state from downstream behaviour. This matters most in regulated enterprise environments where the ability to demonstrate that an AI coding agent operated within explicitly user-authorised boundaries — rather than assumed ones — is a governance requirement.



The 2.1.318 changelog also fixed the claude plugin validate command passing a custom-named marketplace file that claude plugin marketplace add rejects, fixed a running Claude Code process owned by another user being treated as dead by version cleanup (which could delete its binary), and fixed non-interactive launches replacing a ~/.claude.json that isn't valid JSON with defaults — the start now fails, says how to restore the file, and leaves it as is.

 These fixes address a cluster of edge cases that caused silent data loss or unexpected process behaviour: the JSON config fix is particularly significant for unattended or CI/CD agent environments where non-interactive launches are the norm, and where a silent config replacement could cause the next session to run with defaults rather than the operator-configured settings the deployment requires. 

Claude Code was also changed to no longer install or update the IDE extension when started in an IDE terminal; users are now directed to use /ide from an outside terminal or the editor's extensions view, and the VS Code sign-in screen was improved to show what Claude Code printed when its sign-in status check fails.

 The IDE extension auto-install removal is a scope-containment decision: decoupling extension installation from the CLI launch prevents the class of unintended extension state changes that can occur when a developer starts Claude Code in an integrated terminal without intending to modify their IDE setup.

---

### ChatGPT / OpenAI: Dots Gains Multi-Model Dispatch as GPT-6.1 Terra Joins the Agent Roster

OpenAI's most consequential interaction-design advance in this window is not a new surface but a fundamental change to how its persistent **Dots** agents select and apply model intelligence: on November 3, OpenAI updated the Dots product page to announce that GPT-6.1 Terra joins GPT-6 Astra as a model powering Dots — and that the two can be combined within a single agent session.



The November 3 update states that the Dots frontier model family is being expanded to include GPT-6.1 Terra, that a Dot can draw on different models for different parts of its work, and that GPT-6.1 Terra builds on the GPT-6 series' alignment improvements and uses safeguards developed for GPT-6 Astra.

Dots will automatically select the model best suited to each task and can combine multiple models to complete a request; GPT-6.1 Terra is designed to provide faster performance and a friendlier personality.

 The UX significance of this change is the removal of the last residual form of model-selection friction inside a Dots session: previously, a Dot was powered by a single model (Astra) for its entire lifetime. With Terra available as an alternative dispatch target, the agent can now route latency-sensitive or cost-sensitive sub-tasks to Terra while reserving Astra for the highest-complexity steps — without the user knowing or caring which model handled which step. This is automatic multi-model routing at the agent-layer, not the prompt layer.



Dots will automatically select a model for each task and can use multiple models to complete a request, removing the need for users to choose a model themselves.

 The trust-design implication is significant: when a Dot's decision about which model to use for a given sub-task is invisible to the user, the audit trail that documents which model produced which output becomes the only mechanism for post-hoc transparency. 

Each Dot works on its own cloud computer while the user's computer and its contents stay separate unless the user chooses to connect it; for signing into supported websites, Dots can use saved passwords without exposing them to the model.

 The credential-isolation design is the correct trust architecture for a persistent background agent that connects to over 4,000 apps: the model's access to passwords is structurally prevented, so a compromised or misbehaving model cannot exfiltrate credentials even if it attempts to.

The Chat and Work tab merge, announced November 2 and continuing its phased rollout, remains the parallel surface-consolidation story. 

OpenAI noted it will test a combined Chat and Work tab experience initially with a small group of users; if selected, users will be able to move from ordinary conversations to more complex tasks without switching modes, as "this will enable you to move from exploring an idea to having ChatGPT carry it through, all in one place."



---

### Google Gemini: The Floating Panel Comes to Gmail and the Skills Migration Clock Ticks

Google's most significant interaction-design development surfacing in this window is not a shipped feature but an APK-teardown discovery that signals the near-term direction of Gemini's presence inside host apps: a **floating panel redesign for Gemini in Gmail** spotted in Gmail version 2026.10.26.1009152371, replacing the existing bottom-sheet model with a design that closely mirrors the standalone Gemini app on Android.



In version 2026.10.26.1009152371 of the Gmail app, a refreshed Ask Gemini interface appears largely identical to the Gemini overlay on Android — a pill-shaped floating overlay replaces the bottom sheet interface and frees up space at the bottom of the screen; the floating overlay can be expanded using a grab handle; the placeholder text changes to "Ask Gemini," matching the standalone Gemini app, while the overlay adds buttons for a plus menu and voice input.

The redesign adds a floating Gemini overlay, voice input, and a plus menu with options to manage sources or add files from Drive.

 The interaction-design implication is a shift from "Gemini as a panel you open" to "Gemini as an overlay that lives within the app" — the floating, expandable window model keeps Gmail's email list visible and contextually present while Gemini is active, rather than the bottom-sheet model that obscures the lower portion of the inbox. 

The Gemini search settings option allows users to choose where Gemini can look for information, with three options: Google Drive, Gmail, and the web.

 Source-scope toggles directly within the floating overlay are the correct inline-control design for an email AI assistant: a user asking Gemini to summarise a supplier's history can immediately constrain the search to Gmail + Drive without navigating to a settings screen.

The parallel Gemini story in this window is the **Gems-to-Skills migration**, now 13 days from the November 17 cutover. 

Going to the Gems manager reveals the notice: "Gems will become skills starting Nov 17, 2026."

Skills are more easily invoked with a `/` in the prompt box, and multiple can be used at the same time — this broader access is better than first having to go to Gems in the side panel and scrolling down for My Gems.

On November 17, Gems move to the Settings panel of the Gemini app, but users can continue to create, edit, and use them; no sooner than March 1, 2027 (business and enterprise only), Gems can no longer be created, edited, or used.

 The two-stage retirement — move-to-settings in November, full removal no earlier than March 2027 — is the correct migration runway design for a feature set that powers custom workflows: it gives enterprise users more than three months to rebuild in the Skills architecture before the old capability disappears.

---

### Microsoft Copilot: Autopilot Enters Frontier Rollout with Governed Identity and the Excel Canvas Goes Worldwide

Microsoft's interaction-design story in this window is the convergence of its two most structurally ambitious Copilot features reaching active rollout simultaneously: **Autopilot** — the always-on background agent (formerly Scout) — entering November Frontier distribution, and the **Excel Interactive Canvas** beginning worldwide availability for Microsoft 365 subscribers.



Microsoft Copilot Autopilot is an always-on AI agent inside Microsoft 365 — users give it a name, a role, and a goal, and it keeps working in the background: watching Teams channels and email threads, chasing people for updates, running recurring work, and picking a project back up days later without a new prompt.

Each Autopilot instance gets its own governed identity in Microsoft Entra ID, dedicated cloud storage, and a workspace; the agent does not wait for a prompt — it keeps monitoring assigned tasks even when the user is offline.

 The trust-design detail that most distinguishes Autopilot from earlier Microsoft agent concepts is the governed identity: 

its own identity means the agent shows up in your directory like a user, so its actions can be attributed and audited rather than hiding behind whoever pressed go.

An agent with no owner or no activity for 30 days is switched off

 — the inactivity retirement rule is the correct dead-agent governance design: it prevents the accumulation of unowned, unmonitored background agents that run against organisational data with no active human accountable for their scope. 

With Agent 365, organisations can understand who is using Autopilot, manage and govern its access, assess risks, and measure business value to guide adoption; Autopilot is rolling out in November to Frontier.



The parallel Copilot advance reaching worldwide rollout in November is the **Excel Interactive Canvas**. 

The Interactive Canvas in Excel uses Copilot to turn workbook data into a polished report of key visualisations, metrics, and insights; the canvas updates automatically as the underlying data changes, and users can change it by chatting with Copilot.

The feature is in Microsoft 365 Frontier Preview in early November, with broader rollout expected in late November or early December.

 The UX significance of the auto-update behaviour is the elimination of the manual refresh cycle that has historically made spreadsheet-based dashboards brittle: a canvas that reflows when the source data changes converts a static AI-generated summary into a live analytical surface that remains current without additional prompting. The natural-language modification model — chatting with Copilot to change the canvas rather than editing chart properties directly — establishes a new interaction pattern for data visualisation in enterprise spreadsheets: the user's intent is expressed conversationally, and the canvas re-renders accordingly.

---

### Grok (SpaceXSI): Scheduler Byte-Boundary Fix and Image API Migration Settles

SpaceXSI's most operationally significant interaction-design development in this 48-hour window is a targeted safety fix in the nightly Grok Build releases: the **scheduler token-boundary correction** shipping in the November 3 nightly build (2026.11.3), which prevents interval tokens from being sliced at a byte boundary during scheduled multi-step agent tasks.



The November 3 nightly build (v2026.11.3) includes a fix to the scheduler: stop slicing interval tokens at a byte boundary.

 This fix addresses a class of silent failure that is particularly difficult to diagnose in scheduled agentic tasks: when a Grok Build scheduler slices a multi-byte token at a byte boundary — rather than at a token boundary — the resulting token sequences are malformed, and the agent step that consumes them may produce unexpected output or fail in ways that surface as content errors rather than execution errors. For practitioners running scheduled Grok Build workflows that fire on calendar intervals or external app events (Slack, Gmail, Outlook, Linear, GitHub), this fix removes a source of intermittent malformed-output risk that could previously survive undetected through several scheduled runs before producing visible failures.

The parallel API surface story completing in this window is the **grok-imagine-image-quality retirement**, which became final on November 2. 

Effective November 2, 2026, the grok-imagine-image-quality model slug was retired from the xAI API; after November 2, requests to grok-imagine-image-quality are served by grok-imagine-image-2.0 with quality set to low.

Requests to the slug are now served by grok-imagine-image-2.0 with quality set to low, with no change to the request or response shape and at a lower per-image price.

 The no-change-to-request-or-response-shape guarantee is the correct migration design for a production API surface: integrations that have not explicitly updated their model slug continue to function, with the only observable difference being the lower output quality of the automatic redirect target — a detectable, recoverable change rather than a hard failure.

---

### Perplexity: Orchestrator API Matures as the Multi-SDK Agent Infrastructure Primitive

Perplexity's most consequential interaction-design advance reaching practitioners in this window is the continued maturation of the **Orchestrator API** — now in private preview — as the platform's answer to the multi-model access problem for agentic developers who have existing OpenAI or Anthropic SDK integrations.



The Perplexity Orchestrator API provides unified access to open-weight models through OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages APIs, with a Perplexity API key.

The Orchestrator API is a drop-in replacement for existing OpenAI or Anthropic integrations — only the base URL and API key need to change; it is designed for direct model access with the user's own prompts and tools.

 The dual-SDK compatibility is the interaction-design primitive that most reduces integration friction: a developer with an existing Anthropic Claude integration can point the Anthropic SDK's base URL at `api.perplexity.ai/orchestrator` and immediately gain access to Perplexity's catalogue of hosted open-weight models — Kimi K3, GLM-5.3, NVIDIA Nemotron 3 Ultra — without rewriting a single line of client code. This converts Perplexity from a destination product into a model-routing infrastructure layer that slots into existing agentic stacks at the dependency level.



The Agent API now supports Google's Gemini 4 Argon, with introductory pricing through November 30, 2026, at $2.00 per million input tokens, $0.10 per million cached input tokens, and $10.00 per million output tokens, including reasoning tokens.

On October 24, 2026 at 00:00 UTC, the Agent API and Orchestrator API retired older OpenAI model IDs: gpt-5.4, gpt-5.4-mini, gpt-5.4-nano, gpt-5.2, gpt-5.1, and gpt-5.

 The model retirement is the housekeeping that clears the namespace for the next generation of routing targets; the Gemini 4 Argon addition is the routing expansion that matters most for agentic pipeline builders needing a 1-million-token context window for extended research or document-analysis tasks without leaving the Perplexity API surface. 

The Perplexity Computer agentic system orchestrates 19 different AI models as sub-agents: users assign a project, Computer splits it, routes each piece to a best-fit model, and returns a synthesised result.

 The Orchestrator API is the developer-layer expression of the same multi-model routing philosophy that powers Consumer Computer — exposing the routing infrastructure as a callable primitive rather than keeping it exclusively inside Perplexity's own UX.

---

## The Bigger Picture: Mod Consent Logging, Dots Multi-Model Routing, and the Floating Overlay Wave

The 48 hours ending November 4, 2026 reveal an industry simultaneously tightening three separate trust-design layers that have each been conspicuously underdeveloped since the first generation of agentic products shipped. The first layer is **consent logging at the session level**: Claude Code 2.1.318's mod-activation record and Microsoft Copilot Autopilot's governed Entra identity and audit trail represent the same design insight arriving from opposite architectural directions — a user's decision to extend an agent's capabilities in-session is a permission grant that must be recorded, attributable, and retrievable, not an ephemeral gesture that disappears when the session closes. The second layer is **model-dispatch transparency inside persistent agents**: OpenAI's Dots update — where GPT-6.1 Terra joins Astra so that Dots can automatically route different sub-tasks to different models — introduces a new transparency gap alongside a genuine UX improvement. Users whose Dots now run on two models rather than one gain efficiency but lose the ability to reason about which model produced which output in a given agent session, unless OpenAI surfaces that routing decision in the audit trail. The third layer is **surface proximity**: the Gemini-in-Gmail floating overlay, the Microsoft Excel Interactive Canvas, and the continuing OpenAI Chat-Work merge all represent the same design commitment — the AI assistant should live inside the work surface where the user is already operating, not require a navigation event to reach. The floating panel replacing the bottom sheet in Gmail is the micro-expression of the same macro-trend that Microsoft's Autopilot and OpenAI's unified chat surface represent at the macro level: the gap between the user's current context and the AI's reach is closing. The challenge that emerges from all three movements together is the same one the industry has not yet solved: when agents act autonomously across multiple models, with session-level capability extensions, inside the host app rather than in a named agent interface, the user's mental model of what the AI is doing, on whose authority, and with what data, becomes harder to maintain — not easier. The consent records, governed identities, and audit trails that are shipping this week are the correct foundation. The user-facing surfaces that make those records legible at the moment of agent action — not just in a compliance log — have not yet arrived.

---

## References

[1] github.com/715494637. (2026). *Release Claude Code v2.1.318*. [https://github.com/715494637/claude-code-update/releases/tag/2.1.318](https://github.com/715494637/claude-code-update/releases/tag/2.1.318)

[2] github.com/ellismosss. (2026). *scout: Claude Code changed to 2.1.318*. [https://github.com/ellismosss/optimizer/issues/15](https://github.com/ellismosss/optimizer/issues/15)

[3] openai.com. (2026). *Introducing dots — Update on November 3, 2026*. [https://openai.com/index/introducing-dots/](https://openai.com/index/introducing-dots/)

[4] dataconomy.com. (2026). *OpenAI adds GPT-6 models to ChatGPT Dots*. [https://dataconomy.com/2026/11/03/openai-adds-gpt-6-models-to-chatgpt-dots/](https://dataconomy.com/2026/11/03/openai-adds-gpt-6-models-to-chatgpt-dots/)

[5] techbriefly.com. (2026). *OpenAI adds GPT-6 models to ChatGPT Dots*. [https://techbriefly.com/2026/11/03/openai-adds-gpt-6-models-to-chatgpt-dots/](https://techbriefly.com/2026/11/03/openai-adds-gpt-6-models-to-chatgpt-dots/)

[6] bleepingcomputer.com. (2026). *OpenAI says it's doubling Pro usage limits and bringing Work features to Chat*. [https://www.bleepingcomputer.com/news/artificial-intelligence/openai-says-its-doubling-pro-usage-limits-and-bringing-work-features-to-chat/](https://www.bleepingcomputer.com/news/artificial-intelligence/openai-says-its-doubling-pro-usage-limits-and-bringing-work-features-to-chat/)

[7] androidauthority.com. (2026). *Ask Gemini in Gmail may finally get a long-overdue design revamp*. [https://www.androidauthority.com/gmail-ask-gemini-redesign-apk-teardown-3731134/](https://www.androidauthority.com/gmail-ask-gemini-redesign-apk-teardown-3731134/)

[8] sammyguru.com. (2026). *Gmail's Gemini Panel Is Getting a Floating Redesign on Android*. [https://sammyguru.com/gmail-gemini-interface-redesign-android/](https://sammyguru.com/gmail-gemini-interface-redesign-android/)

[9] sammyfans.com. (2026). *Gemini in Gmail may soon look more like the Gemini app*. [https://www.sammyfans.com/2026/11/03/gemini-in-gmail-may-soon-look-more-like-the-gemini-app/](https://www.sammyfans.com/2026/11/03/gemini-in-gmail-may-soon-look-more-like-the-gemini-app/)

[10] 9to5google.com. (2026). *Gemini app replacing Gems with skills in November*. [https://9to5google.com/2026/09/27/gemini-gems-skills/](https://9to5google.com/2026/09/27/gemini-gems-skills/)

[11] releasebot.io. (2026). *Gemini Updates by Google*. [https://releasebot.io/updates/google/gemini](https://releasebot.io/updates/google/gemini)

[12] m365admin.handsontek.net. (2026). *Microsoft Copilot app: Updates to Home and navigation*. [https://m365admin.handsontek.net/microsoft-copilot-app-updates-home-navigation/](https://m365admin.handsontek.net/microsoft-copilot-app-updates-home-navigation/)

[13] eesel.ai. (2026). *Microsoft Copilot Autopilot: what the new autonomous agent does*. [https://www.eesel.ai/blog/microsoft-copilot-autopilot](https://www.eesel.ai/blog/microsoft-copilot-autopilot)

[14] aitoolsreview.co.uk. (2026). *Microsoft Copilot Autopilot: Always-On Agent Explained*. [https://aitoolsreview.co.uk/insights/microsoft-copilot-autopilot](https://aitoolsreview.co.uk/insights/microsoft-copilot-autopilot)

[15] usecarly.com. (2026). *Microsoft Copilot Autopilot: What It Is, Pricing, Limits*. [https://www.usecarly.com/blog/microsoft-copilot-autopilot/](https://www.usecarly.com/blog/microsoft-copilot-autopilot/)

[16] techcommunity.microsoft.com. (2026). *What's New in Microsoft Copilot — October 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528)

[17] hubsite365.com. (2026). *Excel Copilot creates interactive dashboards from workbooks*. [https://www.hubsite365.com/en-ww/crm-pages/create-incredible-copilot-dashboards-in-excel-powerpoint-sharepoint-e3af3e05-76ab-4a85-9591-035dc3ac3ed6.htm](https://www.hubsite365.com/en-ww/crm-pages/create-incredible-copilot-dashboards-in-excel-powerpoint-sharepoint-e3af3e05-76ab-4a85-9591-035dc3ac3ed6.htm)

[18] github.com/crayonlu. (2026). *Release Grok nightly 2026-11-03*. [https://github.com/crayonlu/pure-grok-build/releases/tag/v2026.11.3](https://github.com/crayonlu/pure-grok-build/releases/tag/v2026.11.3)

[19] docs.x.ai. (2026). *grok-imagine-image-quality Retirement on November 2, 2026*. [https://docs.x.ai/developers/migration/imagine-image-quality-nov-2](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)

[20] docs.x.ai. (2026). *Release Notes — xAI API*. [https://docs.x.ai/developers/release-notes](https://docs.x.ai/developers/release-notes)

[21] docs.perplexity.ai. (2026). *Perplexity Orchestrator API*. [https://docs.perplexity.ai/docs/router/quickstart](https://docs.perplexity.ai/docs/router/quickstart)

[22] docs.perplexity.ai. (2026). *Changelog — Perplexity*. [https://docs.perplexity.ai/docs/resources/changelog](https://docs.perplexity.ai/docs/resources/changelog)

[23] suprmind.ai. (2026). *Perplexity Pricing 2026: Pro, Max, Comet & Sonar API Costs*. [https://suprmind.ai/hub/perplexity/pricing/](https://suprmind.ai/hub/perplexity/pricing/)

[24] techcrunch.com. (2026). *OpenAI is finally merging ChatGPT's Chat and Work tabs*. [https://techcrunch.com/2026/11/02/openai-is-finally-merging-chatgpts-chat-and-work-tabs/](https://techcrunch.com/2026/11/02/openai-is-finally-merging-chatgpts-chat-and-work-tabs/)

[25] releasebot.io. (2026). *OpenAI Release Notes — November 2026*. [https://releasebot.io/updates/openai](https://releasebot.io/updates/openai)