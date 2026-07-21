# UX Briefing: Agent Governance, Desktop Locals, and the Bigger Work Surface

**July 21, 2026**

Good morning. The 48 hours ending July 21 are shaped by a single structural impulse across the entire industry: the race to plant agent surfaces inside every workspace a user already occupies, while simultaneously hardening the governance layer that makes those agents safe to deploy. **Claude/Anthropic** ships the `agent-memory-2026-07-22` beta header for the Developer Platform — a new API contract that standardises how managed agents read and write cross-session memory stores — while **Claude Code** continues its authority-tightening arc with the `/verify` and `/code-review` invocation-governance change landing just inside this window, and **Cowork** begins its mobile and web beta rollout with cross-device session state and server-side scheduled tasks. **ChatGPT/OpenAI** is still living with the structural consequence of the July 9 **ChatGPT Work** launch — the biggest agentic-surface expansion in the product's history — as the updated desktop app's Chat/Work split, unified Recents, and cross-device Work sync consolidate into daily use across all plans, with the **Atlas browser** officially sunset-dated and **custom instructions** expanding to 5,000 characters for enterprise users, tripling the personalisation surface. **Google Gemini** continues rolling out **Gemini in Chrome** to UK Mac and PC users, adds real-time topic monitoring and new third-party MCP integrations to **Gemini Spark** on macOS, and advances the **Dynamic View** and **Visual Layout** generative-UI experiments in Labs that let the assistant generate fully interactive custom interfaces on the fly. **Microsoft Copilot** ships the governed **Agent Store publishing flow** from Agent Builder — introducing admin-review-and-approval before any custom Copilot agent reaches a tenant-wide audience — and extends broader MCP agent access across Word, Excel, PowerPoint, Outlook, and Catalyst. **Perplexity**'s most consequential interaction design work this window is the continued consolidation of the **Computer context panel**, **usage analytics dashboard**, and its deepening position inside Microsoft 365 apps, while the **SPACE sandbox** continues powering all Computer sessions with Firecracker microVM isolation.

---

## At a Glance: July 21 Highlights

The releases this window collectively argue that the agent era's second design challenge — after *can the agent act?* — is *who authorises it, who audits it, and how granularly can those answers be configured?*

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code** `/verify` and `/code-review` now require direct invocation only; `agent-memory-2026-07-22` beta header ships stable memory-listing order and tighter path/cursor semantics for Managed Agents; **Cowork** web and mobile beta begins with cross-device session state and server-side scheduled tasks. [1][2][3] |
| **ChatGPT** | **ChatGPT Work** desktop app Chat/Work split and unified Recents now live on all plans; **custom instructions** expand to 5,000 characters for Plus/Enterprise/Business/Edu; **Atlas browser** deprecated August 9 as browser-agentic capabilities merge into ChatGPT and Codex; unified cross-app **search** across chats, projects, images, and documents rolls out globally. [4][5][6] |
| **Google Gemini** | **Gemini in Chrome** rolls out to UK Mac/PC Pro/Ultra subscribers; **Gemini Spark** adds real-time topic monitoring, Google Tasks/Keep integration, MCP support, and new third-party app integrations (Canva, Dropbox, Instacart, OpenTable); **Visual Layout** and **Dynamic View** generative-UI Labs experiments continue rolling out. [7][8][9] |
| **Microsoft Copilot** | **Agent Store publishing** from Agent Builder ships — governed submit/review/approve flow before custom agents reach tenant-wide discovery; **company-wide Prompt Gallery** publishing lets orgs distribute curated prompt collections; broader **MCP agent access** across Office apps and Catalyst; **Edge 149** design unification with Copilot and Bing. [10][11][12] |
| **Grok (xAI)** | **Grok Automations** continues active rollout — scheduled and email-triggered background jobs with run-history audit threads; **Grok Build** ships managed command defaults via `managed_config.toml`, with user deny rules preserving override authority; terminal and dashboard improvements continue. [13][14][15] |
| **Perplexity** | **Computer context panel** ships — every thread now shows live context the agent is working on; **Computer usage analytics** give admins org-wide credit breakdowns, top connector/skill visibility, and exportable data; **Computer inside Microsoft 365** (Word, Excel, PowerPoint, Outlook, Teams) continues expanding with cited, source-traced outputs. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Invocation Governance, Memory API Stabilisation, and Cowork Goes Cross-Device

Anthropic's most consequential trust-design work in this window arrives in two distinct registers: a developer API stabilisation that tightens how agents interact with memory stores, and an invocation-governance change in Claude Code that converts two previously autonomous skills into explicitly user-triggered actions.



The Claude Developer Platform adds the `agent-memory-2026-07-22` beta header, making memory listing return a stable server-defined order and tightening `depth`, `path_prefix`, and `cursor` behaviour, while also updating SDKs to send the new memory store header by default.

 This is the memory-architecture governance change with the most downstream developer significance: it replaces an ad-hoc, loosely specified listing contract with a stable, deterministic API surface — a prerequisite for production agents that need to reliably traverse, audit, or synchronise memory stores without unpredictable ordering effects. 

Managed agents can hold memory across sessions through the agent-memory beta; each store keeps up to 2,000 memories with individual files capped at 100 kB, and a store can be attached read-only so untrusted external data cannot write into an agent's long-term memory; a consolidation pass Anthropic calls "dreaming" can dedupe and reorganise a store into a cleaner one.

 The read-only mount mode is the trust-design primitive that matters most here: it lets developers expose external data as grounding context without granting that data write access to the agent's persistent memory — a boundary that was previously an application-level responsibility with no platform enforcement.



Claude Code changes `/verify` and `/code-review` to run only when invoked directly — Claude no longer runs these skills on its own; invoke them with `/verify` or `/code-review` when you want them.

 This invocation-governance shift is the daily-developer trust change with the broadest impact: it converts two previously autonomous background skills into explicit user-controlled checkpoints, establishing a clear pattern — skills that make evaluative judgements about code quality run when the user asks, not when the agent decides. The interaction design principle embedded in this change is important: it prioritises predictability and user control over agent proactivity for skills whose outputs carry authority. Meanwhile, 

Claude expands Cowork to mobile and web, letting sessions and files follow users across devices, with background work, scheduled tasks, shared chat and projects, and mobile approvals; beta access is rolling out over the next several weeks starting with Max users; Cowork is where Claude handles tasks across files, calendar, email, messaging, the web, and other connected tools until the job is done.

 The cross-device session-state architecture — where work continues when a laptop closes and scheduled tasks run server-side without any device online — marks the moment Cowork graduates from a desktop tool into a genuinely ambient agentic surface.

---

### ChatGPT / OpenAI: Work's Consolidation, the Atlas Sunset, and the Custom Instructions Expansion

OpenAI's most interaction-design-significant work in this window is not a new launch but a structural consolidation: the **ChatGPT Work** ecosystem introduced on July 9 is now settling into its permanent form across all plans and surfaces, and the deliberate retirement of the Atlas browser makes the agentic capability migration explicit.



ChatGPT Work is an agent that can take action across apps and files, stay with a project for hours if needed, and turn a goal into finished work — gathering information across workflows to create finished materials like sheets, slides, docs, and web apps, and staying with complex projects for hours by breaking them into smaller steps and completing them independently.

 The multi-hour autonomous project duration is the temporal UX milestone that distinguishes Work from prior agentic ChatGPT features: rather than a task completing or timing out in a single session, Work operates with the time horizon of a human knowledge worker — making intermediate progress, returning partial outputs, and resuming. 

Work has Codex technology built in, runs on GPT-5.6, and includes control surfaces like Plan mode (a step-by-step plan the user approves before work starts), configurable check-ins, and action approvals, so users decide how autonomous it gets.

 Plan mode is the interaction-design pattern with the most direct trust implication: it makes the agent's intended workflow visible and revisable *before* execution begins, shifting the approval moment from post-hoc review to pre-run authorisation — the difference between signing off on what the agent did and signing off on what it plans to do.



OpenAI is deprecating Atlas as it brings browser-based agentic capabilities into ChatGPT and Codex; Atlas is scheduled to stop working on August 9, 2026.

 The Atlas deprecation is an important surface-consolidation signal: rather than maintaining a separate browser product alongside the Work agent's in-app browser, OpenAI is collapsing them into one interface — making the agent's browsing behaviour part of the supervised Work session rather than a separate product with its own data and history. 

ChatGPT increases custom instructions to 5,000 characters for Plus, Enterprise, Business, and Education users, up from 1,500, giving them more room to customise ChatGPT's response style and behaviour.

 The tripling of the custom-instructions character limit is the personalisation-layer change with the broadest UX implication: richer standing instructions allow users to encode more nuanced delegation preferences, professional context, and communication style rules — reducing the per-session prompting overhead that makes agentic tools feel high-maintenance for daily work.

---

### Google Gemini: Chrome Integration, Spark's Real-Time Monitoring, and Generative UI in Labs

Google's most UX-relevant work in this window spans three different interaction registers — the browser as a grounded context layer, the desktop agent as a local file operator, and the app itself as a generative-UI canvas — and all three point at the same ambition: making Gemini the ambient intelligence layer of every surface a user occupies.



Gemini in Chrome is starting to roll out to Windows and Mac OS devices to Google AI Pro or Ultra subscribers in the U.S. who have Chrome set to English; the experience is not available to Google Workspace business and education plans.

 The Chrome integration is the browser-grounding pattern with the most significant ambient-agent implications: by embedding Gemini at the browser level rather than requiring users to switch to a separate tab, Google makes every page the user is reading a potential grounding source — closing the context gap between what the user can see and what the agent knows. 

Gemini in Chrome helps users make the most of the web, instantly getting key takeaways and simple explanations for complex subjects, helping them get assistance right on the page they're browsing.

Google launched Gemini Spark for its macOS desktop app on July 1, adding a dedicated Spark tab to the sidebar of the Gemini app, which allows the AI agent to take action on files stored locally on a user's computer rather than just responding to questions in a chat window.

Users control which folders Spark can see by linking them in the sidebar and can revoke that access at any time; Google says a future update will allow users to start tasks on their Mac from a phone.

 This explicit folder-linking model is the local-agent trust design Anthropic's Cowork and Perplexity's Personal Computer also use — and it is becoming the emerging UX standard for desktop agents: the agent's world boundary is visible, explicitly granted, and individually revocable. 

Support for custom Model Context Protocol servers is arriving, and Spark can also monitor events in real time and generate reports based on user-defined instructions.

Google introduces two new experimental Labs features in the Gemini app: visual layout and dynamic view — powered by Gemini 3 and Google Research — where visual layout uses multimodal capabilities to move beyond text, generating a visually immersive response with photos and interactive modules that solicit feedback and help customise Gemini's response across multiple turns.

Dynamic view takes this further using agentic coding capabilities, with Gemini designing and coding a unique experience with a user interface that's perfect for the specific prompt.

 These are the generative-UI experiments with the most long-term interaction-design significance: rather than returning a text answer or a static document, Gemini generates a purpose-built interactive interface matched to the query — establishing the premise that the right output format is not chosen by the user but computed by the agent from the nature of the task.

---

### Microsoft Copilot: Governed Agent Publishing, the Prompt Gallery, and MCP Across Office

Microsoft's most consequential UX and governance addition in this window is the **Agent Store publishing flow** from Agent Builder — a structural change that introduces a formal admin-mediated approval gate between the moment an employee builds a custom Copilot agent and the moment that agent becomes available to the rest of the organisation.



Customers can submit agents built in Agent Builder to the Agent Store under the "Built by your org" section, after admin review and approval in Microsoft 365 Admin Center; this governed flow enables admins to review, approve, and publish submitted agents so they can be discovered and used by others in the Agent Store — helping organisations share validated agents at scale while maintaining quality and governance.

 This is the agent-governance pattern that enterprise IT teams have been waiting for: it moves custom Copilot agents from the *shadow IT* tier — built by individual users, used locally, invisible to administrators — into a *governed discovery* tier where every tenant-wide agent has a documented approval trail. The three-step flow (build → submit for review → publish under "Built by your org") mirrors the app-store governance model that made mobile enterprise apps deployable at scale, applied now to AI agents. 

Organisations can also build their own collections of prompts tailored to their business needs and workflows and distribute these to all users within the tenant through the company-wide Prompt Gallery.

 The Prompt Gallery is the lighter-weight governance companion to agent publishing: rather than requiring every repeated AI workflow to be packaged as an agent, organisations can distribute curated, approved prompts — creating a shared, verified starting-point library that reduces the variance in how different employees approach the same task with Copilot.



Microsoft Copilot adds governed agent publishing, tenant-wide prompt galleries, and broader MCP agent access across Word, Excel, PowerPoint, Outlook, and Catalyst, while also improving connector governance, nested permissions, brand kit creation, and Edge's unified look and feel.

 The MCP agent access expansion across Office apps is the agentic-surface change with the most daily-work significance: it makes Copilot agents that connect to external systems — databases, CRMs, APIs via MCP — available at the point of document creation and email composition, rather than only in the Copilot chat surface. 

Microsoft Edge version 149 introduces a refreshed user interface that aligns with the design language used in Copilot and Bing, changing spacing, corners, fonts, and default colour schemes to give customers a unified experience across all Microsoft AI surfaces.

 The Edge visual unification is the ambient trust-design move: when the browser looks and feels like Copilot, users develop a coherent mental model of where the AI layer begins — reducing the cognitive overhead of working across multiple Microsoft AI surfaces simultaneously.

---

### Grok (xAI): Automations Governance and the Managed Command Defaults Model

xAI's most interaction-design-relevant work in this window is the continued hardening of **Grok Automations'** human-oversight layer and the arrival of **managed command defaults** in Grok Build — two governance primitives that, taken together, advance xAI's agentic products from *capable* to *deployable* in organisational contexts.



xAI's Automations lets users set jobs to run on a schedule or when a matching email arrives, available on grok.com and iOS and Android, supporting templates, run history, and reporting back by email or app notification; users describe a job once and Grok runs it on a schedule or when an email arrives, then reports back.

Scheduled automations are available to everyone; email triggers are included with SuperGrok.

 The tiered access model — free-tier users get scheduled automation, SuperGrok users get the more powerful email-reactive agent — is the trust-design decision with the most commercial architecture significance: it gates the most consequential autonomous capability (acting on external, real-time events that the user did not personally initiate) behind a paid tier, creating a natural adoption ramp where users experience scheduled automations before graduating to event-driven ones.



Grok Build adds managed command defaults — teams can now ship default allowed commands via `managed_config.toml`, and user deny rules still win; mid-turn interjections now appear as normal user prompts instead of a separate cyan block; Rewind now fully removes the selected turn from both scrollback and the model's conversation history.

 The `managed_config.toml` command-default system is the organisational deployment primitive that coding agent teams have needed: it lets an admin define a baseline set of approved commands for an organisation's Grok Build deployments while preserving individual users' ability to deny commands the admin has allowed — a well-ordered permission hierarchy (org default → user deny) that matches how security-conscious teams think about tool access. The Rewind improvement — fully removing a selected turn from both visible scrollback and the model's active context — is a temporal UX fix with meaningful trust implications: it gives users a reliable way to excise a mistaken or sensitive turn from the agent's working context, rather than merely hiding it from the display while the model continues to reference it.

---

### Perplexity: The Context Panel, Usage Analytics, and the M365 Governance Layer

Perplexity's most interaction-design-significant work in this window is a cluster of **Computer** transparency and oversight primitives that, together, represent the most fully developed audit-and-governance stack any agentic product has shipped at the end-user and admin layer simultaneously.



Every Computer thread now has a context panel that shows the context that Computer is working on.

 The context panel is the live-work transparency primitive that makes Computer's multi-step execution legible without requiring users to interrupt the task: rather than inferring what the agent is currently doing from its output tokens, users can see the full context window — files, connectors, previous steps — that is shaping the agent's current action. This is the interaction design equivalent of showing a worker's desk rather than only their output: it makes the agent's reasoning environment visible as work progresses. 

Computer usage analytics are now available, giving admins and individuals visibility into how Computer is being used at both the organisation and individual level; admins can view org-wide analytics to break down credit usage by day across their team, see top users on a usage leaderboard, and understand how Computer is being used org-wide — artifacts generated, top connectors, top skills, top spaces, and average task duration, with data exportable for custom analysis.



The two-tier analytics architecture — admin-level org view and personal-level individual view — is the governance design pattern that matters most for enterprise deployment: it gives IT administrators the signal they need to detect unusual usage patterns (unexpected connectors, anomalous task durations), while giving individual users the self-service accountability layer that makes them more intentional about what they delegate. 

Computer is now available inside Microsoft Word, Excel, PowerPoint, and Outlook, four Microsoft 365 apps used by people at work every day; the integration also extends the earlier Teams launch, giving organisations even deeper ways to use Computer for document creation, data analysis, presentation design, and email management.

Perplexity cites the source of every answer and the provenance of every figure, letting teams validate information before sharing.

 The source-citation requirement at the output layer is the trust design that makes Computer's presence inside regulated document workflows defensible: every claim the agent contributes to a Word document or Excel model links back to a verifiable source, maintaining the evidentiary standard that finance, legal, and compliance teams require before distributing AI-assisted work product.

---

## The Bigger Picture: Agent Governance, Desktop Locals, and the Bigger Work Surface

The 48 hours ending July 21, 2026 reveal a design maturation that is quieter than a major product launch but structurally more significant: the frontier of agentic UX has moved from building agents that can act to building governance layers that make those agents safe to authorise at organisational scale. Microsoft's Agent Store publishing flow is the most explicit statement of this shift — it inserts a human admin review checkpoint between *any employee can build a Copilot agent* and *any employee can find a Copilot agent* — but the same pattern appears across every product in the window. Anthropic's `agent-memory-2026-07-22` beta header gives developers a stable API contract for auditing and scoping what managed agents can write into long-term memory, including a read-only mount mode that isolates untrusted data from the agent's persistent store. Perplexity's context panel makes the agent's live working context visible in real time, and its two-tier usage analytics give administrators the signal they need to detect anomalous delegations before they become incidents. Grok Build's `managed_config.toml` command defaults establish the ordered permission hierarchy that team deployments require. Claude Code's invocation-governance change makes evaluative skills user-triggered rather than agent-autonomous. What all of these share is a common architectural move: the addition of a *legibility layer* between what the agent can do and what the user or administrator has explicitly sanctioned. Google's generative-UI Labs experiments — Visual Layout and Dynamic View — point at where this tension becomes most acute: when the agent generates a custom interactive interface matched to the query, the traditional mental model of *I submitted a prompt, I received a response* dissolves entirely. The governance design challenge of mid-2026 is not only who authorises the agent's actions, but who authorises the interface the agent invents to present them.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] Releasebot. (2026). *Anthropic Release Notes — July 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[3] Claude Platform Docs. (2026). *Claude Platform Release Notes*. [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview)

[4] OpenAI. (2026). *ChatGPT is now a partner for your most ambitious work*. [https://openai.com/index/chatgpt-for-your-most-ambitious-work/](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)

[5] OpenAI Help Center. (2026). *ChatGPT Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[6] Releasebot. (2026). *ChatGPT Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] Gemini Apps. (2026). *Gemini Apps Release Updates & Improvements*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/)

[8] TechCrunch. (2026). *Gemini Spark, Google's agentic assistant, is now available on Mac*. [https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/](https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/)

[9] Releasebot. (2026). *Gemini Updates by Google — July 2026*. [https://releasebot.io/updates/google/gemini](https://releasebot.io/updates/google/gemini)

[10] Releasebot. (2026). *Microsoft Copilot Updates by Microsoft — July 2026*. [https://releasebot.io/updates/microsoft/microsoft-copilot](https://releasebot.io/updates/microsoft/microsoft-copilot)

[11] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[12] SuperSimple365. (2026). *What's New in Microsoft 365 and Copilot? June 2026*. [https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/](https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/)

[13] Releasebot. (2026). *xAI Release Notes — July 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[14] Releasebot. (2026). *Grok Build Updates by xAI — July 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[15] SpaceXAI. (2026). *Automations in Grok*. [https://x.ai/news/grok-automations](https://x.ai/news/grok-automations)

[16] Perplexity AI. (2026). *Computer comes to Word, Excel, PowerPoint, and Outlook*. [https://www.perplexity.ai/hub/blog/computer-comes-to-word-excel-powerpoint-and-outlook](https://www.perplexity.ai/hub/blog/computer-comes-to-word-excel-powerpoint-and-outlook)

[17] Releasebot. (2026). *Perplexity Release Notes — July 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[18] SiliconANGLE. (2026). *Perplexity launches secure sandbox to make its AI agents secure and powerful*. [https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/](https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/)