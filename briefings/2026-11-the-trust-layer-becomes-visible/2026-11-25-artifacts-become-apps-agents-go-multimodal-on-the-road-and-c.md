# UX Briefing: Artifacts Become Apps, Agents Go Multimodal on the Road, and Copilot Learns to Write

**November 25, 2026**

Good morning. The 48 hours ending November 25, 2026 are defined by four simultaneous surface-expansion and agentic-authority events: **Anthropic** executing its most consequential generative-UI advance of the month on November 24–25 —

**Claude's "Install as app" launching in beta, letting any eligible artifact become a standalone Mac or Windows desktop application that opens in its own window, connects to Claude and user connectors, and updates automatically when the underlying artifact changes**

— while simultaneously shipping a **Claude Code** reliability patch addressing background-agent session-restart and gateway routing bugs; **OpenAI** arriving at the same window with a cross-platform health-data expansion — 

**ChatGPT Health reaching Android via Health Connect, the desktop app, Dots, and Sites beginning November 19, extending connected health and fitness data analysis and proactive agent-driven suggestions across all major surfaces for the first time**

— as that expansion continues settling into broad availability today alongside the ongoing **Business Hub** beta (live since November 10) giving brands a claimed-profile interface and Insights dashboard directly inside ChatGPT; **Google Gemini** completing its skills-sharing rollout in the same window — 

**shareable Gemini app skills with View/Edit permissions and Drive, Notebook, and Photos file attachments now broadly reaching Workspace and personal accounts from the November 12 rollout**

— while the **Gemini CLI** shipped v0.71.0 with async PowerShell parsing and MCP OAuth fixes; **Microsoft Copilot** holding its post-Ignite position with **Connector write actions at general availability** in Copilot Chat and Cowork, **Work IQ APIs gaining Copilot connector data beginning its late-November rollout**, and the Cowork Projects November Chat rollout continuing; **Grok (xAI)** generating its most significant in-vehicle agentic-UX moment of the year — 

**Elon Musk publicly endorsing Grok's in-car experience on November 25, spotlighting the Grok Bot + Tesla integration that has been live since September 22, where Grok Bot operates directly within the existing voice interface with Connector-linked task delegation for ordering, scheduling, and email management**

— with Grok 4.8 still in trials and no new Bot release in this window; and **Perplexity** shipping its most significant multi-agent and mobile-interaction advances of the month on November 24 — 

**Multiagent expanding to iOS and Android alongside mobile voice control for Teammates, the Chrome extension for browser-based Computer sessions, Cloud Desktop live-view for watching agents work, and Brain self-improving skills now reaching Max subscribers globally**

.

---

## At a Glance: November 25 Highlights

Today's window is defined by the category simultaneously expanding the agent's output surface (from conversation panel to installed desktop application), the agent's input surface (from iOS health data to Android, desktop, Dots, and Sites), and the agent's execution authority (from read-only connectors to write-capable ones) — while Perplexity completes the mobile-delegation loop for its most capable agent tier.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude "Install as app" launches in beta on November 24 across all plans in Claude Desktop for Mac and Windows, turning eligible artifacts into standalone desktop apps with three permission tiers, auto-update on artifact edit, connector access, and an Enterprise-off-by-default governance gate; Claude Code ships a reliability patch on November 25 fixing background-agent session-restart crashes, gateway routing credential leaks, and cloud-session synchronisation gaps** — the per-version permission prompt on every update is the trust-design signal of the window: each time the underlying artifact changes, the installed app must re-request permissions, operationalising the principle that a capability grant covers exactly one known version of the artifact it authorises. |
| **ChatGPT** | **ChatGPT Health expands from iOS and web to Android (via Health Connect), the desktop app, Dots, and Sites beginning November 19, with Dots agents now able to surface proactive health suggestions; health conversations feed ChatGPT memory when memory is on; the Business Hub beta (live November 10) lets eligible brands claim, verify, and manage their ChatGPT profile, connect product feeds, and view mentions and click-through Insights; the iCloud Mail and Calendar plugin rollout continues across all plans** — Health's Dots integration is the agentic-health trust-design advance of the OpenAI window: a proactive agent that can initiate a health suggestion based on connected data is a materially different interaction pattern than a user manually opening the Health tab, shifting health context from on-demand query to ambient agent awareness. |
| **Google Gemini** | **Shareable Gemini app Skills — with View or Edit permissions, Drive file attachments, Gemini Notebook, and Google Photos integration — are broadly rolling out from the November 12 gradual release; Gemini CLI v0.71.0 ships with async PowerShell parsing to fix frozen UI spinners and scoped MCP server permission fixes; Gemini Vids gains Omni 1.2 Flash for 15-second video generation; and the November 16 Skills-sharing governance (admin-controllable, follows Drive external sharing settings) continues its rollout to all Workspace and personal accounts** — the shareable Skills architecture is the collaborative-customisation advance of the Gemini window: a user can now share a reusable Gemini instruction set with colleagues at View or Edit access, turning a personal prompt configuration into a team-level workflow asset that updates when the owner changes it. |
| **Microsoft Copilot** | **Connector write actions are generally available in Copilot Chat and Cowork, defaulting new write tools to Needs approval, with actions running under the user's permissions in the connected system; Work IQ APIs gaining Copilot connector data begins rolling out in late November; Cowork Projects continues rolling out in Copilot Chat with related conversations, files, instructions, and an Outputs view; and the SharePoint Framework 1.25 roadmap teases single-page apps for Cowork plugins in December/January** — connector write actions' "Needs approval" default is the trust-design decision that most directly governs what Copilot is allowed to change: a new connector tool that defaults to requiring explicit per-action confirmation before creating, updating, or deleting data in a third-party system is Copilot operationalising the same read/write distinction that Grok Bot 1.2.3 established at the connector level two weeks ago. |
| **Grok (xAI)** | **Elon Musk publicly spotlights Grok's in-car experience on November 25; the Grok Bot + Tesla integration live since September 22 operates within the existing "Hey Grok" voice interface on the Tesla center display, with Connectors enabling Gmail, Google Calendar, DoorDash, and OpenTable task delegation hands-free; Grok 4.8 remains in internal trials with no general release; and the Grok Bot 1.2.3 four-tier connector-permission architecture continues its enterprise rollout** — the in-car Grok Bot interaction pattern is the ambient-interface advance of the xAI window: by running task delegation inside the voice session that drivers already use rather than as a separate app on the center display, xAI has established the first production deployment of a trust-governed agentic connector workflow in a vehicle context. |
| **Perplexity** | **Perplexity's November 24 changelog ships Multiagent on iOS and Android (with voice control for Teammates), the Cloud Desktop live-view panel for watching agents work in real time, turn-any-thread-into-a-Teammate conversion, the Perplexity Chrome extension for browser-based Computer sessions, and Brain self-improving skills now available to Max subscribers globally; role-based access controls reach Perplexity Enterprise admin settings; and Grok 4.6 becomes available to all Pro and Max subscribers in Perplexity and Perplexity Computer** — the Cloud Desktop live-view panel is the transparency-UX advance of the Perplexity window: watching a Multiagent team and individual Teammates browse and act in real time on the right-hand panel transforms background execution from an invisible process into an observable one, providing the audit visibility that long-running agentic tasks have consistently lacked. |

---

## Product Highlights

### Claude / Anthropic: Artifacts Graduate to the Desktop and Code Sessions Get Stabler

Anthropic's most consequential interaction-design event in this window is **Claude "Install as app"** — the November 24 beta that completes the arc from conversation-generated artifact to persistent native desktop application, available on all plans in Claude for Mac and Windows.



Announced on November 24, 2026, the feature lets users use Claude artifacts to create, run, and share desktop apps; the "Install as app" feature is rolling out in beta in Claude for Mac and Windows.

 The UX shift is fundamental: until this week, an artifact was a panel alongside a conversation — a tool that existed only inside Claude. 

When you ask Claude to create an artifact, you can now click "Install as app" in the Share menu, after which it launches in its own dedicated app window and appears in the Dock.

Apps can be used with connectors, and they include an option to add a menu bar item; apps also update automatically when the underlying artifact is edited, and each change prompts a new permissions request.

 This auto-update-with-re-permission design is the trust-design detail that most directly separates Claude's artifact-as-app model from a traditional software install: the capability grant is scoped to exactly the version of the artifact the user has seen and approved, not an open-ended delegation to whatever the app becomes after future edits.

The permission architecture is explicitly tiered. 

Users can only give full access to apps they made themselves, or on Team and Enterprise plans, apps made by people in their organisation; every permission covers one version of the app, so Claude asks again after each update, even the user's own edits.

The feature is on by default for Team, with full access off; on Enterprise, it is off until an owner turns it on.

 This sequencing — broad-access default-off, Enterprise owner-gated — mirrors the governance architecture Anthropic established for Computer Use on Team and Enterprise plans five days earlier: the capability is available, but the most consequential permission levels require an organisational decision rather than a user click. 

Anthropic does not review the apps, and only some users can grant the top level of access.

 This disclosure is itself a trust-design signal: by surfacing the absence of Anthropic review directly in product documentation, the company is placing the trust judgment explicitly with the user and the organisation rather than implying a centralised safety gate that does not exist.



Claude Code's November 25 patch fixed background agents saving a slash command it could not deliver to a stopped session and then running it by itself the next time that session restarted, and also fixed cloud sessions not telling Claude about background agents that finished just before a worker restart.

 These two fixes are the agentic-workflow reliability advance of the Claude Code window: a background agent that silently executes a stale command on session restart, and a cloud session that cannot see the results of background work completed before a worker restart, are both failure modes where the agent's behaviour diverges invisibly from the user's expectations — exactly the category of bug that makes long-running agentic tasks difficult to trust at production scale.

---

### ChatGPT / OpenAI: Health Goes Ambient, Business Hub Gives Brands a Home

OpenAI's most consequential interaction-design event in this window is **ChatGPT Health**'s expansion from a single-platform iOS and web feature into a cross-surface ambient health layer — the moment when health data moves from a dedicated tab a user visits to a context available to the agent wherever the user works.



Starting November 19, Health is rolling out to more of the places users use ChatGPT, including the desktop app, Dots, Sites, and Android, with support for Health Connect; to get started, update to the latest ChatGPT app and select Health in the sidebar.

OpenAI has expanded ChatGPT Health to the ChatGPT Android app and desktop version, adding support for Android Health Connect to link selected health and fitness data.

 The significance is in the Dots integration specifically. 

OpenAI also integrated ChatGPT Health into its Dots assistants and Sites service, while some advanced functions involving its autonomous personal agents, called Dots, require a Pro subscription.

The company says it does not sell health information, though conversations involving Health can feed into ChatGPT's memory feature if users keep memory turned on.

 This memory-with-health interaction is the trust-design detail that most requires user awareness: health data that persists into ChatGPT memory is health data that shapes future conversations across all topics, not just the ones where the user has explicitly asked a health question.



Users can select an option to connect information through Android Health Connect and choose the data categories that ChatGPT may sync; Health Connect acts as an intermediary between ChatGPT and compatible fitness applications.

 The granular category-selection model — where users choose which data types to share rather than granting all-or-nothing access — is the consent architecture that makes this expansion governable: a user can share sleep data for workout analysis without sharing medical records, and the selection persists at the data-category level rather than requiring per-session decisions.

**ChatGPT Business Hub**, live in beta since November 10, is the interaction-infrastructure advance that most changes the business-to-AI-search relationship. 

Launched in beta on November 10, 2026 as part of Businesses in ChatGPT, it lets eligible companies claim and verify their profile, update their details, add a product feed and see aggregated Insights.

Business Hub is where you claim your business, verify it, update key details, add product information, and view basic performance data; Business Agents are AI assistants that answer customer questions about your products and policies inside ChatGPT.

 The UX significance is structural: for the first time, a business has a first-party interface to manage how it appears in ChatGPT's answers — equivalent to what Google Business Profile provided for search results, but applied to an AI assistant surface where the agent constructs the answer rather than retrieving a link.

---

### Google Gemini: Skills Become Shareable, Vids Gets Longer, CLI Fixes the Terminal

Google's most consequential interaction-design advance settling into broad availability in this window is the **shareable Gemini app Skills** rollout — the transition from personal prompt configurations to team-level workflow assets that began November 12 and is now reaching the full Workspace and personal account population.



Users can now share any skill from the "Skills" page in the Gemini app with others and choose to grant them View or Edit permissions; Google recently launched skills — reusable, custom instructions that guide Gemini — in the Gemini app, and is now introducing shareable skills alongside Drive file attachment capability.

Drive files and Notebooks update in real time so a skill always works from the latest version.

 The UX shift from Gems (the previous personal-only system) to shareable Skills is from a configuration that lived in one person's account to one that can be distributed across a team, edited collaboratively, and grounded in live Drive content. 

On November 17, 2026, Google made Gems read-only for personal accounts belonging to users age 18 and older in Gemini Apps; Skills replace them in the Gemini app, with file integrations and sharing becoming available as the rollout reaches each account.



The governance architecture of skill sharing reflects the same pattern Google uses for Drive: 

Skill sharing in the Gemini app is on by default for organisations but can be disabled in the Admin console; Skills in the Gemini app follow the organisation's Google Drive sharing settings — if Drive files can be shared outside the organisation, skills in the Gemini app can be shared externally as well.

 This Drive-parity governance model is both the efficiency and the risk of the design: administrators who have already established Drive sharing policies automatically inherit them for Skill sharing, eliminating duplicated configuration, but also meaning that an organisation's external Drive sharing posture now governs its AI workflow asset distribution.



Users now have access to Gemini Omni 1.2 Flash directly within Google Vids, with Omni 1.2 providing longer duration videos up to 15 seconds and improved quality resulting in higher character consistency and vocal realism.

Gemini CLI releases v0.71.0, fixing frozen UI spinners by parsing PowerShell commands asynchronously in its latest release.

 The frozen-spinner fix is a navigability-UX advance in the developer-tool context: a CLI that freezes its UI while parsing shell commands creates an interface state where the user cannot distinguish "agent is working" from "agent is stuck" — the async parsing fix restores the signal that lets developers decide whether to wait or interrupt.

---

### Microsoft Copilot: Connectors Learn to Write, Work IQ Gains External Data

Microsoft's most consequential interaction-design event settling into broad availability in this window is **Copilot Connector write actions at general availability** — the moment when Copilot transitions from a system that reads connected apps to one that can create, update, and delete data in them, with a trust-design architecture that defaults every new write tool to requiring user confirmation.



On November 9, 2026, Microsoft published details about the general availability of write actions for Copilot connectors, allowing employees to perform actions inside connected third-party applications — meaning Copilot can do more than retrieve a CRM record or summarise a support ticket, and with the appropriate connector it can create tasks, update customer information, modify project issues, and delete records.

Connector write actions have reached GA in Chat and Cowork; users can approve once or remember approval for an individual tool, while Researcher's federated connectors remain read-only.

 The trust-design decision embedded in the default is structural: 

new write tools start at "Needs approval."

 This means the transition from read to write does not silently expand the agent's authority — every new connector write capability must receive explicit user confirmation before it executes, establishing an audit checkpoint at exactly the boundary where the agent's actions become consequential to data in systems outside Microsoft 365.



Cowork activity, including adding or sharing a plugin, appears in the Purview unified audit log under Audit (Standard); Purview DLP covers Cowork for sensitive prompts, labeled files and web-search grounding.

 The Purview coverage of Cowork write actions is the enterprise-governance advance that makes the write-action GA meaningful for regulated organisations: an audit trail that captures plugin additions alongside Cowork activity gives security teams the same log-based visibility into AI-driven data modifications that they have for direct user actions in connected systems.



Organisations can use their existing Copilot connector investments to build richer, more context-aware agentic experiences across Microsoft 365 and enterprise systems without requiring separate connector setup or management; Work IQ APIs will be able to use data and tools from connected enterprise systems through Copilot connectors, with rollout beginning late November 2026 and expected completion by late December 2026.

 The Work IQ connector integration is the developer-infrastructure advance that completes the write-action picture: an agent reasoning layer that can now reach connector data without separate setup means that the same connectors administrators have deployed for Copilot Chat can feed directly into the agentic orchestration layer, eliminating the duplication of connector management across surfaces.

---

### Grok (xAI): Bot Proves Its Ambient Vehicle Case

xAI's most significant interaction-design moment in this 48-hour window is not a new release but a product-positioning event: 

Elon Musk took to X on November 25 to endorse Grok's in-car experience firsthand; the comment lands at a moment when Grok's capabilities inside Tesla vehicles have expanded significantly beyond a simple chatbot.



The in-car Grok Bot interaction architecture — which has been live since September 22 — is the ambient-agentic design pattern that the November 25 spotlight brings into focus. 

Grok Bot builds on the growing integration, shifting that functionality from in-car control to actual task delegation; rather than launching a separate application on the center display, the agent runs directly inside the existing Grok interface.

Drivers can rouse it by tapping the Grok app in the App Launcher, holding the steering-wheel microphone button, or saying "Hey Grok"; from there, Tesla says users can trigger a routine coffee run, book appointments and complete purchases over the web.

 The UX significance of running task delegation within the existing voice session — rather than as a distinct "agent mode" requiring a separate launch step — is that it establishes the ambient-always-available pattern for agentic connectors in constrained-interface environments: the agent is simply already there when the user speaks.



Accessing third-party services requires Connectors, secure integrations for external tools like Gmail and Google Calendar that let Grok Bot reach a user's information; they are set up inside the Grok app under a New Connector menu, and once added, Grok Bot uses them automatically.

The bigger shift came in September 2026 with the launch of Grok Bot, which moved the assistant from answering questions to completing multi-step tasks — managing calendars, ordering food, booking reservations; Musk also stated on November 22 that Tesla vehicles will eventually combine Grok with real-time X feed data to surface traffic and destination alerts, though no deployment timeline has been confirmed.

 The X-feed-to-vehicle-alert roadmap is the interaction-design signal that most clearly reveals xAI's ambient-AI vehicle strategy: not a voice assistant that answers questions when asked, but a contextual agent that surfaces relevant information from the user's social and real-world data streams without requiring a prompt.

---

### Perplexity: Multiagent Goes Mobile, Brain Goes Global, and Agents Become Observable

Perplexity's most significant interaction-design event in this window is the November 24 changelog — a broad cluster of Computer advances that simultaneously completes the mobile-delegation loop for Multiagent, adds live observability to background agent execution, and extends Brain's self-improving skills globally.



Perplexity released a broad wave of product updates led by Multiagent teamwork, voice-enabled teammates, browser control, and self-improving skills; Multiagent is a new effort level above Ultra in Perplexity Computer and teammates.

Teammates and Multiagent are now in the Perplexity app on iOS and Android, with voice for Teammates; about a third of the most demanding Computer work already starts on iPhone; users can now control Teammates with voice; available today for Max subscribers.

 The UX significance of voice-controlled Teammates on mobile is temporal: 

long-running Computer jobs execute on Perplexity's servers while the phone acts as a control surface

 — establishing the phone as a delegation and monitoring surface for work that runs in the cloud rather than a device that must stay open and active for the task to proceed.



Cloud Desktop lets users watch Computer and Teammates work live on their own Cloud Desktop in the right-hand panel; the feature also allows users to turn any Computer conversation into a dedicated Teammate without leaving the thread.

 The Cloud Desktop live-view is the transparency-UX advance that most directly addresses the trust problem in long-running multi-agent tasks: a user who can watch the agent browse and act in real time can verify that the agent's approach matches their intent, intervene before an irreversible step, and build the kind of observational confidence in the agent that abstract progress indicators cannot provide.



Brain now creates and refines personal skills automatically from past Computer sessions and memory, turning repeated workflows, formatting preferences, and corrections into reusable instructions that carry into future tasks; self-improving skills are on by default for eligible US Max subscribers.

Perplexity Enterprise now includes role-based access controls in the admin settings.

 The role-based access controls are the enterprise-governance advance within the broader November 24 release: as Perplexity's Computer platform gains Multiagent execution, voice-mobile control, and self-modifying skills, the admin's ability to restrict which roles can access which capabilities becomes the organisational trust-design layer that governs how much autonomous authority any individual user's agent tier is permitted to exercise.

---

## The Bigger Picture: Artifacts Become Apps, Agents Go Multimodal on the Road, and Copilot Learns to Write

The 48 hours ending November 25, 2026 crystallise a single macro movement that the month of November has been building toward: **the AI agent category is completing its migration from embedded conversation surface to native execution environment, and every trust-design decision in this window is an answer to the same underlying question — when the agent's output escapes the conversation and enters the user's native environment, who governs what it can access, change, and remember?** Claude's "Install as app" is the clearest single expression: an artifact that installs as a native desktop application can access the filesystem at the level the user permits, connect to third-party services via connectors, and update itself automatically — but the trust architecture requires a new permission grant on every version change, the full-access tier is restricted by plan and organisational gate, and Enterprise must opt in rather than opt out. Copilot's connector write-action GA answers the same question at the data-modification layer: the agent can now create, update, and delete records in connected systems, but every new write tool defaults to Needs approval and all Cowork write activity lands in the Purview audit log. Perplexity's Cloud Desktop live-view addresses the same question at the execution layer: when a Multiagent team is running 16-model parallel tasks in a cloud desktop, the user's ability to watch the work in real time is the trust mechanism that substitutes for the per-action confirmation model — observable execution as an alternative to interrupt-driven consent. Grok Bot in Tesla is the ambient version of the same pattern: an agent running inside the existing voice interface, with connectors set up once and applied automatically, is an agent whose authority is scoped by the user's upfront connector selections rather than per-task approvals. What connects all four — Claude's per-version permission, Copilot's default-Needs-approval write tools, Perplexity's live execution panel, and Grok's connector-scoped ambient delegation — is the same design conclusion the category has been arriving at across November 2026: as the agent's output surface expands from conversation to installed application to connected-data modification to ambient vehicle task, the trust architecture must expand with it, and the platforms that ship graduated, legible, auditable authority — rather than a single broad consent that covers all future actions — are the ones whose users will delegate the most with the least anxiety.

---

## References

[1] macrumors.com. (2026). *Claude Now Lets You Install Artifacts as Desktop Apps*. [https://www.macrumors.com/2026/11/25/claude-install-artifacts-desktop-apps/](https://www.macrumors.com/2026/11/25/claude-install-artifacts-desktop-apps/)

[2] thenextweb.com. (2026). *Claude can now turn its artifacts into Mac and Windows desktop apps*. [https://thenextweb.com/news/claude-install-as-app-artifacts-mac-windows-desktop](https://thenextweb.com/news/claude-install-as-app-artifacts-mac-windows-desktop)

[3] claude.com. (2026). *Turn artifacts into Mac and Windows apps*. [https://claude.com/resources/articles/install-as-app](https://claude.com/resources/articles/install-as-app)

[4] siliconangle.com. (2026). *Anthropic is trying to kill traditional desktop apps with Claude-generated desktop apps*. [https://siliconangle.com/2026/11/24/anthropic-is-trying-to-kill-traditional-desktop-apps-with-claude-generated-desktop-apps/](https://siliconangle.com/2026/11/24/anthropic-is-trying-to-kill-traditional-desktop-apps-with-claude-generated-desktop-apps/)

[5] testingcatalog.com. (2026). *Anthropic now allows installing artifacts as desktop apps*. [https://www.testingcatalog.com/anthropic-now-allows-installing-artifacts-as-desktop-apps/](https://www.testingcatalog.com/anthropic-now-allows-installing-artifacts-as-desktop-apps/)

[6] inoryva.blogspot.com. (2026). *Claude Artifacts Can Now Install as Desktop Apps — With a Full Access Warning You Must Read*. [https://inoryva.blogspot.com/2026/11/claude-artifacts-can-now-install-as.html](https://inoryva.blogspot.com/2026/11/claude-artifacts-can-now-install-as.html)

[7] code.claude.com. (2026). *Claude Code changelog — November 25, 2026*. [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

[8] help.openai.com. (2026). *ChatGPT release notes — November 19, 2026*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[9] dataconomy.com. (2026). *ChatGPT Health Rolls Out To Android With Health Connect Support*. [https://dataconomy.com/2026/11/25/chatgpt-health-rolls-out-to-android-with-health-connect/](https://dataconomy.com/2026/11/25/chatgpt-health-rolls-out-to-android-with-health-connect/)

[10] androidheadlines.com. (2026). *ChatGPT Can Now Read Your Android Health and Smartwatch Data to Explain Your Daily Habits*. [https://www.androidheadlines.com/2026/11/chatgpt-health-android-health-connect-rollout.html](https://www.androidheadlines.com/2026/11/chatgpt-health-android-health-connect-rollout.html)

[11] distilinfo.com. (2026). *ChatGPT Introduces Proactive Health Reminders*. [https://distilinfo.com/2026/11/24/chatgpt-health-reminders/](https://distilinfo.com/2026/11/24/chatgpt-health-reminders/)

[12] brandlight.ai. (2026). *ChatGPT Business Hub: How It Works and How to Claim (2026)*. [https://brandlight.ai/blog/chatgpt-business-hub](https://brandlight.ai/blog/chatgpt-business-hub)

[13] llmpulse.ai. (2026). *ChatGPT Business Hub explained: how to claim your business and what Insights shows*. [https://llmpulse.ai/blog/chatgpt-business-hub/](https://llmpulse.ai/blog/chatgpt-business-hub/)

[14] workspaceupdates.googleblog.com. (2026). *Share skills and add files from Google Drive, Gemini Notebook and Google Photos to your skills in the Gemini app*. [https://workspaceupdates.googleblog.com/2026/11/share-skills-add-files-from-Drive-Notebook-Photos-to-skills-Gemini-app.html](https://workspaceupdates.googleblog.com/2026/11/share-skills-add-files-from-Drive-Notebook-Photos-to-skills-Gemini-app.html)

[15] online-tech-tips.com. (2026). *Google replaces personal Gemini Gems with Skills and adds attachments and sharing*. [https://www.online-tech-tips.com/google-gemini-gems-to-skills-attachments-sharing/](https://www.online-tech-tips.com/google-gemini-gems-to-skills-attachments-sharing/)

[16] adaptd.ai. (2026). *Gemini app skills can now be shared and use Drive files*. [https://adaptd.ai/updates/gemini-skills-share-with-team/](https://adaptd.ai/updates/gemini-skills-share-with-team/)

[17] workspaceupdates.googleblog.com. (2026). *Gemini Omni 1.2 Flash now in Vids with 15-second generations and improved quality*. [https://workspaceupdates.googleblog.com/2026/11/](https://workspaceupdates.googleblog.com/2026/11/)

[18] releasebot.io. (2026). *Gemini CLI Updates by Google — November 2026*. [https://releasebot.io/updates/google/gemini-cli](https://releasebot.io/updates/google/gemini-cli)

[19] aguidetocloud.com. (2026). *What's New in Microsoft 365 Copilot: November 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-november-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-november-2026-updates/)

[20] dev.to. (2026). *Microsoft Copilot Can Now Write to Connected Apps. What Does That Mean for Data Security?* [https://dev.to/sunychoudhary/microsoft-copilot-can-now-write-to-connected-apps-what-does-that-mean-for-data-security-4pmj](https://dev.to/sunychoudhary/microsoft-copilot-can-now-write-to-connected-apps-what-does-that-mean-for-data-security-4pmj)

[21] windowsforum.com. (2026). *Microsoft Copilot Connector Write Actions Now Available: Approvals and Admin Controls*. [https://windowsforum.com/news/microsoft-copilot-connector-write-actions-now-available-approvals-and-admin-controls.451553/](https://windowsforum.com/news/microsoft-copilot-connector-write-actions-now-available-approvals-and-admin-controls.451553/)

[22] hubsite365.com. (2026). *Copilot connectors can now write to connected apps*. [https://www.hubsite365.com/en-ww/crm-pages/copilot-konnektoren-durfen-jetzt-schreiben-1b3e8fc6-7473-4a5d-a413-eeebfe03f9d5.htm](https://www.hubsite365.com/en-ww/crm-pages/copilot-konnektoren-durfen-jetzt-schreiben-1b3e8fc6-7473-4a5d-a413-eeebfe03f9d5.htm)

[23] m365admin.handsontek.net. (2026). *Microsoft 365 Copilot: Copilot connectors in Work IQ APIs*. [https://m365admin.handsontek.net/microsoft-365-copilot-copilot-connectors-work-iq-apis/](https://m365admin.handsontek.net/microsoft-365-copilot-copilot-connectors-work-iq-apis/)

[24] basenor.com. (2026). *Elon Musk Says Grok Makes Tesla Road Trips More Fun*. [https://www.basenor.com/blogs/news/elon-musk-says-grok-makes-tesla-road-trips-more-fun](https://www.basenor.com/blogs/news/elon-musk-says-grok-makes-tesla-road-trips-more-fun)

[25] notateslaapp.com. (2026). *Tesla Adds Grok Bot to Vehicles for Hands-Free Errands and Tasks*. [https://www.notateslaapp.com/news/4724/tesla-adds-grok-bot-to-vehicles-for-hands-free-errands-and-tasks](https://www.notateslaapp.com/news/4724/tesla-adds-grok-bot-to-vehicles-for-hands-free-errands-and-tasks)

[26] autos.yahoo.com. (2026). *Tesla Integrates Grok Bot to Do Your Tasks For You*. [https://autos.yahoo.com/ev-and-future-tech/articles/tesla-integrates-grok-bot-tasks-231300327.html](https://autos.yahoo.com/ev-and-future-tech/articles/tesla-integrates-grok-bot-tasks-231300327.html)

[27] releasebot.io. (2026). *Perplexity Release Notes — November 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[28] x.com. (2026). *Perplexity on X: Teammates and Multiagent are now in the Perplexity app on iOS and Android*. [https://x.com/perplexity_ai/status/2123126865829515363](https://x.com/perplexity_ai/status/2123126865829515363)

[29] alphasignal.ai. (2026). *Perplexity Brings 16-Agent AI Teams to iPhone and Android*. [https://alphasignal.ai/news/perplexity-brings-16-agent-ai-teams-to-iphone-and-android](https://alphasignal.ai/news/perplexity-brings-16-agent-ai-teams-to-iphone-and-android)

[30] blog.rudrakasturi.com. (2026). *Perplexity Introduces Multiagent: Up to 16 AI Agents Can Work on One Complex Task*. [https://blog.rudrakasturi.com/perplexity-introduces-multiagent-up-to-16-ai-agents-work-together/](https://blog.rudrakasturi.com/perplexity-introduces-multiagent-up-to-16-ai-agents-work-together/)

[31] futurumgroup.com. (2026). *Perplexity's Brain Learns on the Job: Self-Improving Agent Skills*. [https://futurumgroup.com/insights/perplexitys-brain-learns-on-the-job-self-improving-agent-skills/](https://futurumgroup.com/insights/perplexitys-brain-learns-on-the-job-self-improving-agent-skills/)