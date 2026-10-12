# UX Briefing: Generative UI, Workspace Invasion, and the Composable Agent Layer

**October 12, 2026**

Good morning. The 48 hours ending October 12, 2026 are defined by a category-wide push to dissolve the boundary between the AI assistant and the documents, dashboards, and workspaces where work actually lives — every major platform shipping a release that treats the conversation window as a staging area and the user's real files, apps, and workflows as the true execution surface. **Claude/Anthropic** delivers its most structurally ambitious product expansion of the year: **Claude Dashboards and Claude Motion entering beta on October 8**, simultaneously moving Docs, Slides, and Design out of beta onto every plan including Free, paired with **Claude for Google Workspace entering public beta on October 6** — a sidebar add-on for Docs, Sheets, and Slides that applies AI edits in-place with a per-change approval card, and new bidirectional Docs/Sheets/Slides connectors that let users start from Claude and edit live Google files from chat. **ChatGPT/OpenAI** ships the most consequential generative UI advance in the product's four-year history: **GPT-6 with Intelligent UI rolling out globally on October 7**, converting ChatGPT responses from a text-and-markdown stream into a composable runtime that can render calculators, interactive diagrams, comparison tables, bill-splitters, and tappable forms directly inside the conversation — built on a library of native, streamable components with a compiler that progressively renders the interface as the model generates it. **Google Gemini** enters its most significant agent-customisation transition since the product launched: **Gemini Skills beginning their Workspace rollout on October 5**, replacing the Gems paradigm with stackable, reusable custom-instruction blocks that can be combined per-session, while the Gemini Enterprise Federated Query mode allows agents to query live operational databases directly through MCP with user credentials. **Microsoft Copilot** completes the most structurally significant app redesign of the enterprise AI era: **the new Copilot Home, Code, and Autopilot architecture beginning Frontier rollout in October**, merging Chat and Cowork into a single Home surface, adding a Code tab for app creation, and expanding Autopilot — the always-on persistent agent — to private preview, alongside **Copilot in SharePoint and OneDrive reaching general availability**. **Grok (xAI)** ships two trust-design events: **Grok Build 1.0.49 introducing universally scoped hook permission prompts and prompt-policy enforcement** for web searches, fetches, and image generation, with the Grok Bot **Secure Forms mechanism routing sensitive web-form interactions through a contained card instead of a screen handoff**. **Perplexity** delivers the agentic temporal-UX event of the window: **Computer Automations launching on October 5** — replacing one-shot Scheduled Tasks with persistent, memory-carrying, event-triggered agents that run across Slack, Gmail, Outlook, Linear, and GitHub and pause for review before consequential actions.

---

## At a Glance: October 12 Highlights

Today's releases converge on a single structural move: the AI conversation surface is no longer where the work concludes — it is where the work is delegated to live files, live data, live apps, and live recurring workflows.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Dashboards and Motion enter beta October 8; Docs, Slides, Design go Free; Google Workspace add-on enters public beta October 6** — Dashboards builds live, query-traceable charts from BigQuery/Snowflake/Salesforce; Motion turns prompts into editable MP4 animations written as code; Workspace sidebar adds per-edit approval cards in Docs, Sheets, Slides; bidirectional connectors let Claude create and edit Google files from chat; Compliance API now returns unified-experience chats in beta. [1][2][3] |
| **ChatGPT** | **GPT-6 with Intelligent UI rolls out globally October 7–8** — responses can now render calculators, comparison tables, charts, tappable buttons, and interactive diagrams inline; compiler progressively streams the interface while the model generates; Composer predictions in Codex beta let users press Tab to accept next-message suggestions; audio uploads reach all plans. [4][5][6] |
| **Google Gemini** | **Gemini Skills begin Workspace rollout October 5, Gemini app rollout October 13** — stackable reusable instruction blocks replace Gems; multiple Skills can combine per-session; Gems sunset for personal accounts November 17; Gemini Enterprise Federated Query mode reaches Preview, querying live operational data in place via MCP with user credentials and automatic read-only context tools. [7][8][9] |
| **Microsoft Copilot** | **New Copilot Home, Code, and Autopilot begin Frontier rollout in October** — Home merges Chat and Cowork into one surface; Code builds apps in sandboxed GitHub Copilot-backed environment; Autopilot enters private preview as always-on persistent agent; Copilot in SharePoint and OneDrive reach GA with hybrid billing; Copilot Notebooks get creation-by-description, UX refresh, and expanded reference types. [10][11][12] |
| **Grok (xAI)** | **Grok Build 1.0.49 ships universal hook permission prompts and prompt-policy enforcement** — hook permission prompts appear in every approval mode; web searches, fetches, and image generation now follow prompt_policy and rule decisions before they prompt; Allow once scoped to next shell command only; Grok Bot v0.68.1 ships Secure Forms for sensitive web-form interactions and reconnect cards for expired sessions. [13][14][15] |
| **Perplexity** | **Computer Automations launch October 5, replacing Scheduled Tasks** — event-triggered and scheduled agents carry memory of prior runs across Slack, Gmail, Outlook, Linear, and GitHub, building on earlier results without restarting; pause-for-review gate before consequential actions; inline interactive charts and 3D visualizations land in threads; Portable Computer Windows rollout begins with HP ZBook. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Dashboards, Motion, and the Workspace Invasion

Anthropic's defining interaction-design event in this window is a cluster of three simultaneous releases that together complete Claude's transformation from a conversational assistant into a full-document, full-data, full-workspace agent: **Claude Dashboards and Motion entering beta on October 8**, Docs/Slides/Design graduating to every plan, and the Claude for Google Workspace add-on entering public beta on October 6.



Claude Dashboards and Claude Motion are now in beta — Claude can turn data into a dashboard that stays current and ideas into an animated explainer; Claude Dashboards connects to data platforms like BigQuery, Databricks, or Snowflake and is in beta on paid plans; Claude Motion is in beta on Team and Enterprise; Claude Docs, Slides, and Design are out of beta and available on every plan, including Free.

 The UX significance of this triple is architectural: Anthropic is no longer positioning Claude as a tool that helps users *think about* their work but as an agent that *produces and maintains live artifacts* from that work. The most consequential transparency design detail in Dashboards is that 

each chart shows the query behind it, and each animation is built as code that can be edited.

 This is the correct provenance design for AI-generated data artifacts: rather than presenting a chart as a fait accompli, every figure is traceable to its source SQL query, and every animation frame is inspectable as code. The user can verify, modify, and extend rather than simply accept. 

For Enterprise admins, Dashboards and Motion are off by default, while Docs, Slides and Design turn on by default on October 15.

 The opt-in-by-default posture for the two beta features and opt-out-by-default for the GA features is the correct governance gradient: more experimental capabilities require explicit organisational activation, while proven capabilities default to available with admin override.

The **Claude for Google Workspace add-on** is the spatial UX event that matters most for enterprise practitioners. 

Claude for Google Workspace is a new add-on that puts Claude in a sidebar inside Google Docs, Google Sheets, and Google Slides, announced on October 6, 2026, as a public beta on all paid Claude plans — Claude reads the file you have open and edits it in place.

 The interaction-design shift this establishes is from *tab-switching AI assistance* (the user exports content into Claude, gets a result, and pastes it back) to *in-place collaborative editing* (Claude sees the live file, proposes changes in context, and the user approves them without leaving the document). 

The default mode shows each change as an approval card first — Claude can only change files without asking if the user switches to Accept all edits.

 The approval-card-by-default posture is the correct trust-design choice for a workspace agent that has write access to live documents: destructive edits are bounded by a per-change human confirmation gate, and the higher-autonomy mode is an explicit opt-in. 

The announcement also added Docs, Sheets, and Slides connectors that run the other way: Claude creates and edits Google files from the chat — so you can start in the file or start in a Claude chat.

 The bidirectionality is the UX primitive that makes the integration feel genuinely native rather than a one-way export tool — the user's mental model of where to start a task becomes irrelevant because both entry points converge on the same live file.



The Compliance API chat endpoints now also return chats from the unified Claude experience in beta for Claude Enterprise organisations; the Compliance API can now also download Claude Docs documents as Word files in beta.

 This extension of the Compliance API to the unified experience is the governance primitive that makes the Docs/Slides/Design GA graduation enterprise-deployable rather than just individually useful: admin teams now have a structured record of AI-assisted document creation sessions alongside all other Claude interactions, satisfying the audit requirements that enterprise document workflows carry.

---

### ChatGPT / OpenAI: Intelligent UI and the Generative Response Layer

OpenAI's most consequential interaction-design event of this window — and arguably one of the most significant UX architecture decisions in ChatGPT's four-year history — is the **GPT-6 with Intelligent UI global rollout on October 7**, which fundamentally changes what a ChatGPT "response" is: not a stream of text and markdown, but a composable, streamed, interactive interface assembled at query time.



GPT-6 in ChatGPT introduces Intelligent UI, a new capability that allows ChatGPT to answer quickly with fully interactive user interfaces that make everyday answers more visual, make learning complex topics easier, and create a tool to solve a task right in the moment — responses can include graphics, tappable buttons, forms, charts, and interactive experiences used directly in the conversation.

 The UX significance of this is not aesthetic: it is the difference between a system that *describes* how to calculate a bill split and a system that *builds a bill-splitter* in the reply. 

Behind the feature is a library of native, streamable components and a compiler that processes the interface while the model generates it, so the interface appears progressively instead of after the full response is finished.

 The progressive streaming of the interface — rendered as the model thinks rather than after the full response is ready — is the latency design that makes this feel conversational rather than like a loading screen: the user begins interacting with early parts of the interface while the rest is still being generated. 

OpenAI trained GPT-6 to compose responses using text, visuals, and interactive elements, choosing how they fit together based on the question — a comparison might work best side by side, an explanation might be easier to follow through an interactive diagram, and ChatGPT can still give a simple text answer when that is the most useful response.



The rollout posture also reflects a deliberate trust-design choice: 

users do not need to change any setting — GPT-6 with Intelligent UI appears in the Chat tab as the rollout reaches each account, while Enterprise availability depends on workplace admin settings; the update covers only the Chat experience, and the models powering Work and Codex are not changing with this release.

 Scoping Intelligent UI to Chat-only and leaving Work and Codex on their existing model stack is the correct bounded-rollout design: it allows OpenAI to learn how users interact with generative UI at consumer scale without simultaneously changing the model surface in the enterprise and coding-agent contexts where predictability is more tightly required.



ChatGPT adds Composer predictions in Codex beta, suggesting the next message in your thread so users can press Tab to accept, review, or edit before sending.

 This next-message prediction in the Codex conversation is the interaction equivalent of IDE code completion applied to agent delegation: rather than composing the next instruction to the coding agent from scratch, the user is offered a predicted next step they can accept, modify, or discard. The tab-to-accept interaction reduces the cognitive load of managing a multi-step Codex session — particularly for longer agentic threads where the user must decide what to delegate next after each completed subtask.

---

### Google Gemini: Skills, Federated Queries, and the Composable Persona Layer

Google's most consequential Gemini interaction-design event in this window is the **Gemini Skills rollout beginning in Workspace on October 5** — an architectural shift that replaces the Gems paradigm's monolithic custom-assistant model with a composable, stackable system of reusable instruction blocks that can be combined per-session, and that travels with the user across Gemini surfaces and Workspace apps.



Skills roll out October 5 in Workspace and October 13 in the Gemini app, with Gems starting their exit in November — multiple Skills can work together, letting Gemini combine specialized instructions for more complex tasks.

 The UX significance of the *composability* is the critical advance over Gems: where a Gem was a single, fixed persona configuration that the user switched into for an entire session, a Skill is a modular instruction block that can be stacked with other Skills on a per-prompt basis. This shifts the user's relationship with personalisation from *mode-switching* (enter Gem X, exit Gem X) to *capability-composing* (apply Skills A, B, and C to this particular task). 

Google has posted an in-app alert informing users that Gems will be replaced by Skills on November 17, 2026, and that existing Gems will be automatically migrated; starting October 13, users will no longer be able to create or edit Gems, though they may continue using existing ones until the automatic migration begins.

 The in-app alert with a specific migration date and an automatic-migration commitment is the correct transparency design for a breaking change to a personalisation primitive: users are not surprised by a feature disappearing, they are given advance notice and a no-action-required migration path.

The critical UX limitation that enterprise deployments need to account for is the **Skills non-sync constraint**: 

Skills do not sync between the Gemini app and Workspace, so users must create them separately on each platform; additionally, users can no longer create new "Ask a Gem" steps in Workspace Studio.

 This non-sync design means that the composable persona layer is not yet identity-portable the way custom instructions are in Claude or Microsoft Copilot — a user must duplicate their Skill configuration across surfaces, which creates maintenance overhead and the risk of surface-specific drift in AI behaviour.

The **Gemini Enterprise Federated Query mode** is the other agentic UX advance worth isolating in this window. 

Gemini Enterprise adds Preview federated query mode for Data Cloud connectors and Knowledge Catalog integration, helping apps query operational and analytical data in place with user credentials and automatic read-only context tools in the Assistant tab — federated query mode allows Gemini Enterprise to query data in place using MCP and each user's own credentials, without copying or ingesting data into a data store.

 The credential-passthrough design is the correct trust architecture for enterprise data access: the agent queries databases as the authenticated user, meaning access is scoped to what that individual is authorised to see, not to a shared service account with broader permissions. This preserves row-level security and audit trails automatically without requiring special agent-specific access controls.

---

### Microsoft Copilot: Home, Autopilot, and the Work OS Architecture

Microsoft's most structurally consequential Copilot UX event in this window is the **new Copilot Home, Code, and Autopilot architecture entering Frontier rollout in October** — the most fundamental redesign of the Copilot app since its launch, converting it from a conversational assistant with adjacent agentic capabilities into a unified work operating system where conversation, office productivity, app creation, and persistent background agents share a single application shell.



Microsoft is introducing the new Copilot to connect the tools people rely on with the next generation of capabilities — the Copilot app now has three new capabilities: Home is the new starting point where Chat and Cowork come together, and with Office in Copilot, Word, Excel and PowerPoint are built into the experience; Code lets everyone build their own solutions, powered by the same underlying technology as GitHub Copilot; and Autopilot is a persistent, proactive, and personal agent that keeps working even when you're not.

 The UX significance of the Home merger of Chat and Cowork is the same principle that defined the Microsoft 365 Copilot app unification earlier this year: a user should not have to choose between *asking a question* and *delegating a task* at the interface level — both are the same act of directing an AI, differentiated only by the scope and duration of the work. 

The left navigation is changing: Plugins replaces the separate Agents entry point in Chat and the Customise entry point in Cowork — Plugins are add-ons that bundle skills, connectors, and other capabilities in one place.

 The consolidation of Agents and Customise into a single Plugins entry point reduces the cognitive overhead of navigating the agent-extension system from two separate discovery surfaces to one.

The **Copilot Notebooks October update** is the agentic-workspace advance that enterprise users will encounter most immediately. 

Copilot can help get users started by creating a new Copilot Notebook at request — with new expanded references support and a UX refresh, users can simply describe what kind of notebook they want, like "I'm working on pitching to a new customer in [industry]" — and notebook creation with Copilot can put together relevant references across work data and the web.

 The creation-by-description design converts notebook setup from a manual curation task (the user hunts for relevant documents and adds them one by one) into a delegation act (the user describes the project goal and the agent assembles the relevant context). 

The new UX update brings a refreshed experience to the Microsoft Copilot app and OneNote to help keep notebooks organised and easy to use by grouping and reordering content and artifacts from the navigation pane.

The official general availability of Copilot in SharePoint is one of the biggest updates of the month — every user can now create and organise content, ask questions grounded in their SharePoint data, enrich libraries with AI-generated metadata, and build reusable skills; there are also new advanced capabilities including image generation and editing, AI-generated site analytics reports, and near real-time metadata autofill.

 The GA moment for Copilot in SharePoint is significant not just as a feature milestone but as an agent-deployment architecture decision: SharePoint libraries are now live data stores that Copilot agents can read, enrich, and write to as part of automated workflows, completing the content-layer agentic loop that Workspace Studio Flows had opened on the communication side.

---

### Grok (xAI): Permission Architecture Hardens and Secure Forms Ship

xAI's most interaction-design-significant releases in this window are a pair of trust-layer advances in Grok Build and Grok Bot that together harden the permission and credential boundaries around agentic tool use — the infrastructure work that enterprise operators require before deploying agents with persistent web access.

The most consequential trust-design advance in Grok Build this window is **the 1.0.49 permission-prompt universalisation**. 

Hook permission prompts appear in every approval mode; web searches, fetches, and image generation follow the prompt_policy setting and rule decisions before they prompt; Allow once on a permission card applies only to the next shell command.

 The significance of hook prompts appearing in *every* approval mode — including modes that previously bypassed them — is the removal of an escape hatch that allowed agentic sessions to silently acquire capabilities the user had not explicitly reviewed. Previously, a session running in a permissive approval mode could execute hooks without surfacing a prompt; now the hook boundary is enforced regardless of the session's general approval posture. The "Allow once" scope tightening is the complementary advance: a user who approves a single shell command no longer inadvertently grants that approval to the entire class of shell operations for the session.

On the Grok Bot side, 

Secure Forms fill into the page the Bot has open, and checkout card fields get a Secure Form instead of a screen handoff; when X or Vercel needs sign-in again, the Bot shows a reconnect card instead of retrying or giving up.

 The Secure Forms design is the credential-containment advance that the Grok Bot computer-use surface has required: sensitive form inputs — login credentials, payment card fields — are no longer handled by the Bot as visible screen elements but are routed through a contained form interface that the user fills directly, preventing the Bot from intercepting or logging credential data. The reconnect card for expired sessions converts a previously silent failure mode (the Bot retrying or giving up invisibly) into an explicit user-visible state change that invites action rather than abandoning the session.



Grok Build 1.0.50 ships worktree, terminal, and session improvements with safer worktree deletion, compact mode UI tweaks, timestamps, clipboard-friendly branch names, stronger permissions, and many reliability fixes across commands, models, and files.

 The worktree safety improvements are the parallel-session management advance that multi-repository Grok Build workflows have required: safer deletion prevents a worktree removal operation from silently destroying in-progress work in a concurrent session, and clipboard-friendly branch names reduce the manual friction of moving branch references between the terminal and other tools.

---

### Perplexity: Computer Automations and the Event-Triggered Delegation Arc

Perplexity's most significant agentic UX event in this window is the **Computer Automations launch on October 5** — a fundamental redesign of the Computer scheduling model that replaces one-shot, stateless Scheduled Tasks with persistent, memory-carrying, event-triggered agents that build on their own prior work and understand when to pause for human review before taking consequential actions.



Perplexity is launching Automations, which bring Computer's capabilities to long-running agents that work proactively on a schedule or in response to conditional events — each agent uses Computer's connected files, tools, and Projects to carry out its assignment and remembers prior work, picking up where it left off without waiting for a new request.

 The UX shift from Scheduled Tasks to Automations is precisely the shift from *periodic re-execution* to *genuine continuation*: a Scheduled Task restarts from zero on each run, requiring the agent to re-establish context and reconstruct prior state. An Automation carries memory of what it found, decided, and produced in every previous run, enabling the agent to detect changes, escalate anomalies, and progressively refine its outputs over time. 

Triggers work with Slack, Gmail, Outlook, Linear, and GitHub events with conditional filters; each run carries memory of prior runs so agents build on previous work instead of restarting; Automations can watch for missed deadlines or overdue replies and flag them; credits are only spent on actual runs, not while watching for a trigger.



The trust-design advance that makes Automations enterprise-adjacent rather than merely powerful is the **pause-for-review gate before consequential actions**. 

Automations run ongoing work in Computer on the web, on a schedule or when events occur in connected apps — they can use Memory, Skills, and connectors, build on earlier runs, and pause for review before consequential actions; examples include monitoring changes and responding to disruptions like drafting a recovery plan when a supplier emails about a delay.

 The pause gate is the bounded-autonomy primitive that separates Automations from fully autonomous background agents: the agent operates without interruption through all information-gathering, analysis, and draft-preparation steps, and only surfaces for human approval at the boundary where an irreversible action — sending a message, updating a record, publishing a document — is about to be taken. This is the correct design for a persistent agent that the user cannot actively monitor during every run.



Inline charts and interactive 3D explanations appear directly in the Computer thread — users can explore concepts with interactive 3D explanations or chart financial data with TradingView Lightweight Charts for candlesticks, volume, and moving averages.

 The inline visualisation advance is the output-format evolution that makes Computer thread outputs self-contained deliverables rather than text reports that the user must take elsewhere to visualise: a financial monitoring Automation can now deliver its findings as an interactive candlestick chart embedded in the thread, with the data and the visual co-located for immediate review.

---

## The Bigger Picture: Generative UI, Workspace Invasion, and the Composable Agent Layer

The 48 hours ending October 12, 2026 mark the moment the AI product category decisively abandons the chat-as-final-surface model and commits to the work environment — documents, spreadsheets, dashboards, slides, code repositories, recurring workflows — as the true execution layer. Claude's Google Workspace sidebar, Claude Dashboards' live SQL-traceable charts, and Claude Motion's code-backed animations are three facets of the same architectural commitment: the conversation is a delegation interface, not a destination. OpenAI's GPT-6 Intelligent UI makes the same argument from the opposite direction: instead of exporting AI output into other tools, it builds the interactive tool directly inside the response, collapsing the gap between "AI answer" and "usable artifact" to zero. Google's Gemini Skills rollout converts the personalisation layer from a single-Gem mode-switch into a stackable, composable instruction system — closer to a capability palette than a persona selector. Microsoft's Copilot Home, Code, and Autopilot architecture frames the same convergence as a product identity statement: the goal is not an AI assistant that lives beside your work tools but a Work OS where conversation, office productivity, agentic task execution, and persistent background automation share a single shell. The trust-design advances in this window — Grok Build's universal hook permission prompts, Grok Bot's Secure Forms credential containment, Perplexity Automations' pause-for-review gate, Claude's per-edit approval cards in the Google Workspace sidebar — all make the same structural argument from different angles: as agents acquire deeper write access to live work environments, the governance primitives that bound their authority must become correspondingly more granular, not less. Every major platform in this window is simultaneously expanding the surface area of AI action and installing more precise human-approval checkpoints at the boundaries where that action becomes irreversible. The category's next design challenge is not demonstrating that agents can work inside our tools — that proof is now complete — but ensuring that the humans who must answer for what those agents produced can always, clearly, and with minimal friction understand and verify what happened.

---

## References

[1] Anthropic / Claude. (2026). *Build live dashboards and animate explainers with Claude*. [https://www.anthropic.com/news/claude-dashboards-motion](https://www.anthropic.com/news/claude-dashboards-motion)

[2] Powerdrill.ai. (2026). *Claude Dashboards and Motion: What's New, Access, and Alternatives (2026)*. [https://powerdrill.ai/blog/claude-dashboards-and-motion](https://powerdrill.ai/blog/claude-dashboards-and-motion)

[3] CellCog.ai. (2026). *Claude for Google Workspace: Docs, Sheets and Slides*. [https://cellcog.ai/blog/claude-for-google-workspace/](https://cellcog.ai/blog/claude-for-google-workspace/)

[4] OpenAI. (2026). *GPT-6 and Intelligent UI for everyone*. [https://openai.com/index/gpt-6-for-everyone/](https://openai.com/index/gpt-6-for-everyone/)

[5] gHacks Tech News. (2026). *OpenAI Brings GPT-6 to All ChatGPT Users, Adding Intelligent UI With Interactive Answers*. [https://www.ghacks.net/2026/10/08/openai-brings-gpt-6-to-all-chatgpt-users-adding-intelligent-ui-with-interactive-answers/](https://www.ghacks.net/2026/10/08/openai-brings-gpt-6-to-all-chatgpt-users-adding-intelligent-ui-with-interactive-answers/)

[6] OpenAI Help Center. (2026). *ChatGPT release notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[7] Android Authority. (2026). *Google maps out transition plan to replace Gemini Gems with Skills*. [https://news.google.com/read/CBMifEFVX3lxTE5BVERjYmJmV2VhZThTekRwblhpOXRHLXZrLXFHR25PU3R1VU5DcWRNTFc1d1pzdkRKWnVzV2p2Q2dlMlNVRWpYc0V3X05OQ09QbXBBVmFsVWpFenBZcnJHUnREeXBvYldxeENNRllfalNSNlczQ0ZYN05FTXc](https://news.google.com/read/CBMifEFVX3lxTE5BVERjYmJmV2VhZThTekRwblhpOXRHLXZrLXFHR25PU3R1VU5DcWRNTFc1d1pzdkRKWnVzV2p2Q2dlMlNVRWpYc0V3X05OQ09QbXBBVmFsVWpFenBZcnJHUnREeXBvYldxeENNRllfalNSNlczQ0ZYN05FTXc)

[8] NQ Brief. (2026). *Google Sets 2026-2027 Timeline to Replace Gemini Gems With Skills*. [https://nqbrief.com/en/tech/google-gemini-gems-skills-timeline/](https://nqbrief.com/en/tech/google-gemini-gems-skills-timeline/)

[9] Google Cloud Docs. (2026). *Gemini Enterprise release notes — October 2, 2026*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[10] Releasebot. (2026). *Microsoft Copilot Updates by Microsoft — October 2026*. [https://releasebot.io/updates/microsoft/microsoft-copilot](https://releasebot.io/updates/microsoft/microsoft-copilot)

[11] M365 Copilot Connection (Substack). (2026). *Copilot's biggest October 2026 updates, and when they land*. [https://m365copilotconnection.substack.com/p/copilots-biggest-october-2026-updates](https://m365copilotconnection.substack.com/p/copilots-biggest-october-2026-updates)

[12] Microsoft Tech Community. (2026). *What's New in Notebooks — October 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105)

[13] xAI. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[14] xAI. (2026). *Grok Bot Changelog*. [https://x.ai/changelog/bot](https://x.ai/changelog/bot)

[15] Releasebot. (2026). *Grok Build Updates by xAI — October 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Perplexity Blog. (2026). *Computer adds Automations for ongoing work*. [https://www.perplexity.ai/hub/blog/computer-adds-automations-for-ongoing-work](https://www.perplexity.ai/hub/blog/computer-adds-automations-for-ongoing-work)

[17] Releasebot. (2026). *Perplexity Release Notes — October 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[18] The Oxford AI School. (2026). *What Are the New Features of Perplexity? (October 2026)*. [https://www.theoxfordaischool.com/new-features-of-perplexity](https://www.theoxfordaischool.com/new-features-of-perplexity)