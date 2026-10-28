# UX Briefing: Ambient Delegation, MCP at the OS Layer, and the iCloud Agent Gap

**October 28, 2026**

Good morning. The 48 hours ending October 28, 2026 are defined by a single clarifying question that every major platform is answering in a different way: when an AI agent operates inside personal data — your mail, your documents, your calendar — who controls what it can do, and how does the user know what just happened? **Claude/Anthropic** ships **Claude Code 2.1.312**, whose headlining change is the addition of `oidc.user_id_claim` to the Claude apps gateway, allowing enterprise deployments to identify users by Microsoft Entra ID's `oid` claim rather than the generic `sub` claim — a precision identity-routing fix that closes a critical gap in multi-tenant enterprise deployments — alongside a companion cluster of cloud session reliability fixes and effort-level controls for cloud routines. **ChatGPT/OpenAI** makes its most consequential personal-data delegation move since the Apple Messages plugin in August: the **iCloud Mail and Calendar plugins**, shipping October 27 across all ChatGPT plans, give Dots — OpenAI's proactive background agent — its first live connection to Apple's communication and scheduling data, converting the iCloud ecosystem from a ChatGPT blind spot into a fully agentic surface. **Google Gemini** ships the **Gemini API CLI beta**, a stateless, zero-dependency command-line client released October 27 that gives coding agents running inside Claude Code, Codex, Cursor, and any shell environment a single binary for delegating tasks to Gemini-managed agents without a local integration overhead. **Microsoft Copilot** brings two simultaneous advances to its developer surface: the **Visual Studio GitHub Copilot Chat redesign**, published October 28, extends the Copilot SDK foundation across Ask, Agent, and all chat interactions with longer-running sessions and prompt caching — while the **Copilot Autopilot + Today** private previews, both confirmed active in October, establish the first persistent cloud-hosted Copilot agent with its own identity, memory, and workspace. **Grok (xAI)** ships **Custom Moderation Controls** to the xAI API on October 27, giving developers per-category content guidelines at the request level — and ships **Grok Build 1.0.70**, which completes the dashboard navigation overhaul by adding folder-grouped agent display and cross-folder session resume. **Perplexity** rounds out the window with the **SPACE sandbox open-sourcing** and the ripple effects of **Computer in Email**, which represents the fullest realisation yet of the ambient-delegation pattern: an agent that reads a thread, verifies the sender, uses their established connectors and memory, and replies with finished work — without the user ever opening a browser.

---

## At a Glance: October 28 Highlights

Today's window reveals the industry crossing a threshold from AI agents as explicit, user-initiated tools to AI agents as ambient participants embedded inside personal communication, document, and identity infrastructure — and the trust-design question of how users maintain legible control over agents they can no longer clearly locate.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code 2.1.312 adds flexible OIDC user identification for enterprise gateway routing, effort-level controls in cloud routine model picker, and a Bash editor with syntax highlighting in environment setup scripts; 2.1.311 fixes subagents unable to use late-connecting MCP tools** — the `oidc.user_id_claim` addition lets the Claude apps gateway route by Entra ID's `oid` instead of the generic `sub`; effort selection for cloud routines bridges the gap between interactive and scheduled agentic sessions; MCP tool access for late-connecting servers repairs a class of subagent workflow failures. [1][2][3] |
| **ChatGPT** | **iCloud Mail and Calendar plugins launch October 27 across all ChatGPT plans on web, desktop, and iOS; both plugins unlock Dot (proactive agent) compatibility for the first time; Mail integration supports search, drafts, send, and contact lookup; Calendar supports read, schedule, and event updates** — users connect via app-specific password in Settings > Plugins; Dot can now access Apple scheduling and inbox data; plugins access only iCloud accounts, not Gmail or Outlook accounts visible in Apple Mail. [4][5][6] |
| **Google Gemini** | **Gemini API CLI beta releases October 27: stateless, zero-dependency binary for AI coding agents, shell scripts, and CI pipelines running on the Interactions API; works natively inside Claude Code, Codex, Cursor, and any standard shell; supports text and media generation, file analysis, and Gemini managed agent delegation** — the CLI is explicitly positioned as a companion to Claude Code and Antigravity rather than a replacement; zero-dependency design eliminates local integration overhead for agent-to-agent delegation. [7][8][9] |
| **Microsoft Copilot** | **Visual Studio GitHub Copilot Chat gets a redesigned experience published October 28, extending the Copilot SDK foundation across Ask, Agent, and chat with longer-running sessions and prompt caching; Copilot Autopilot in private preview and Today view entering private preview in October confirm the ambient agent rollout is active** — new VS experience is opt-in via Tools > Options; Autopilot operates with its own identity and memory in the Microsoft 365 tenant; Today is a proactive command centre across mail, calendar, Teams threads, and tasks. [10][11][12] |
| **Grok (xAI)** | **Custom Moderation Controls ship October 27 to the xAI API: per-category content guidelines (nsfw, violence, profanity) added to Chat Completions and Responses API requests; Grok Build 1.0.70 completes dashboard navigation update with blank-line question separation and plugin skill load reporting** — guidelines array lets operators set how Grok handles content categories at the request level; 1.0.69's cross-folder /resume and folder-grouped agent dashboard complete the multi-session navigation surface. [13][14][15] |
| **Perplexity** | **Computer in Email enables ambient task delegation via email thread: forward or cc computer@perplexity.com, Computer reads the thread, verifies sender, uses their connectors and memory, and replies with finished deliverables in the same thread; each session creates a full audit trail reviewable on web or mobile** — deliverables include spreadsheets, PDFs, and presentations; sender verification and permission inheritance are the trust-design primitives; SPACE sandbox platform open-sourced October 15 gives developers the execution isolation layer behind Computer. [16][17][18] |
| **Apple** | **Apple Creator Studio announces beta AI assistants for Keynote, Pages, and Numbers on October 27: assistants built on Apple models and OpenAI understand document context; all three apps gain MCP support enabling external agents to read content, perform edits, and execute actions; shipping November** — MCP support on macOS 27 converts Keynote, Pages, and Numbers into agent-addressable document surfaces; Logic Pro also gets an AI assistant; update is free for existing Creator Studio subscribers. [19][20][21] |

---

## Product Highlights

### Claude / Anthropic: Enterprise Identity Routing and Cloud Routine Precision Mark 2.1.312

Anthropic's most consequential Claude Code advance in this window is not a new agentic capability but the closing of a critical enterprise identity gap: **Claude Code 2.1.312**, which shipped October 27, adds `oidc.user_id_claim` to the Claude apps gateway.



The `oidc.user_id_claim` on the Claude apps gateway identifies people by an id_token claim other than `sub`, such as Microsoft Entra ID's `oid`.

 The interaction-design significance of this change is best understood in the context of large enterprise deployments: when Claude Code is deployed behind a corporate identity provider, the generic `sub` claim is often tenant-specific and not stable across re-authentications in Entra ID — which means audit trails and permission bindings built on `sub` can silently break when users re-authenticate. 

Claude Code 2.1.312 releases updates across its CLI, VS Code, cloud sessions, and integrations, adding flexible OIDC user identification and cloud routine controls while fixing reliability, settings, session, and code review issues.



The second cluster of 2.1.312 changes that warrants practitioner attention lives in the cloud routines surface. 

A banner has been added on a routine's page that says why its last run didn't start, such as the organisation's policy settings

 — and, critically, 

an effort level has been added to the model picker when you create or edit a routine that runs in the cloud, along with a Bash editor with colors, line numbers and a Copy button to the setup script box in cloud environment settings.

 The effort-level addition to the cloud routine model picker is the correct design for scheduled agentic sessions: an operator configuring a nightly code-review routine can now explicitly specify whether that routine runs at a lightweight or extended reasoning effort, rather than inheriting whatever default the session was last configured with interactively. The Bash editor addition completes the environment setup UX — the previous pattern of pasting raw scripts into a plain text box with no syntax validation was a latent error surface for the class of routines that fail silently because a setup script had an invisible character problem.

The companion **Claude Code 2.1.311** fixes that shipped in the same window address the most consequential class of multi-agent reliability failures. 

Claude Code 2.1.311 fixed subagents being unable to use MCP tools from servers that finish connecting after the subagent starts, fixed Claude seeing stale MEMORY.md and CLAUDE.md content right after automatic compaction when those files were edited earlier in the session, and fixed SubagentStop hooks running about twice a minute for each running subagent instead of once when it finishes.

 The MCP tool access fix is the most structurally significant: in multi-agent pipelines where subagents are spawned before all MCP servers have completed their connection handshake, the previous behaviour silently denied those subagents access to tools that were nominally available — producing failures that were difficult to diagnose because the MCP server appeared healthy from the main session's perspective.

---

### ChatGPT / OpenAI: iCloud Plugins Give Dots Its First Apple Ecosystem Data Access

OpenAI's most interaction-design-significant release in this window is not a new model or a reasoning update but a connectivity advance that closes the largest remaining gap in ChatGPT's personal-data agent surface: the **iCloud Mail and Calendar plugins**, which shipped October 27 across all ChatGPT plans.



iCloud users can now connect Mail and Calendar to ChatGPT to find emails, catch up on the inbox, check the schedule, and update calendar events — available to all ChatGPT plans on the web, desktop app, and iOS.

 The trust-design architecture of the plugins is deliberately scoped: 

the Mail integration lets ChatGPT search and read iCloud Mail, manage messages and drafts, send email, and look up iCloud contacts,

 while 

ChatGPT can only see iCloud Mail, not other accounts that are in the iOS Mail app, like Gmail or Outlook.

 This scope restriction is the correct privacy-design posture for a first-launch personal mail integration: rather than requesting broad access to every mail account visible in Apple Mail, the plugin constrains itself to iCloud — which the user has explicitly authorised via an app-specific password — leaving the user in full control of what the agent can and cannot see.

The agentic-UX significance of this launch is in the Dot compatibility it unlocks. 

Both plugins enable ChatGPT Dot compatibility for the first time — a user can even ask a ChatGPT Dot to help set up the iCloud Mail and Calendar plugins.

 Before this release, Dots — OpenAI's always-on proactive background agent — had no access to Apple's communication infrastructure: an iCloud-primary user who relied on ChatGPT Dots for proactive task management had an agent that was blind to their actual inbox and calendar. 

The iCloud plugins give ChatGPT some of the same access that Siri AI has to personal data, expanding what the chatbot can do — iCloud access can also be used for Dots, the proactive AI agent that OpenAI launched last month.

 The framing of Dots as the secondary beneficiary is the correct product-design sequencing: by shipping the plugin as a universal capability across all plans first, OpenAI ensures that the ambient-agent use case (Dot monitoring your iCloud inbox and calendar proactively) is immediately available to Pro subscribers without a separate feature gate.

The connection setup pattern is also well-designed for trust: 

to get started, users open ChatGPT's Settings > Plugins, find iCloud Mail or iCloud Calendar, and follow the connection prompts — a plugin may require connection before it can use its tools; an Apple app-specific password is required to connect either service rather than the regular Apple Account password.

 Requiring an app-specific password rather than an Apple Account password is the correct security choice: it means a user can revoke ChatGPT's access to iCloud without changing their primary Apple Account password or affecting any other Apple service.

---

### Google Gemini: The API CLI Converts Agent Pipelines into First-Class Gemini Delegation Surfaces

Google's most structurally significant Gemini UX advance in this window is not a consumer app redesign but a developer-layer primitive released October 27 that will quietly reshape how multi-agent pipelines interact with Gemini's reasoning and agent infrastructure: the **Gemini API CLI beta**.



Released October 27, the Gemini API CLI (`gemini-api`) is a stateless, zero-dependency command-line client for AI coding agents, scripts, and CI pipelines — use `gemini-api` on the Interactions API to generate text and media, analyze files, and run Gemini managed agents.

 The design philosophy behind the CLI is the correct one for agent-to-agent delegation: 

the Gemini API CLI is a stateless, zero-dependency command-line client built for AI agents with shell access, scripts, and CI pipelines — a coding agent can use it to generate text and media, analyze files, and delegate tasks to Gemini managed agents.

 The "zero-dependency" constraint is what gives this release its leverage: a Claude Code subagent, a Grok Build worktree session, or a Codex sandbox that has shell access can now invoke Gemini's managed agents — including Deep Research — without installing a language SDK, managing OAuth tokens, or maintaining a local server process.



The CLI works with Antigravity, Claude Code, Cursor, and any standard shell environment.

 The explicit acknowledgement of Claude Code and Antigravity as first-class hosts is a significant trust-design statement from Google: rather than positioning the Gemini API CLI as a tool that competes with other coding agents, Google is explicitly designing it as a delegation primitive that plugs into whatever orchestrator the developer is already using. 

The Gemini API CLI is a stateless, zero-dependency CLI binary for terminal exploration, multimodal asset generation, and coding agent execution rails — developers can delegate multi-step research or coding tasks to background Managed Agents such as Deep Research, capture the interaction ID with `--jq`, and poll for structured results.

 The `--jq` output capture combined with async polling is the correct temporal-UX design for long-running agentic sub-tasks: rather than blocking the calling agent's execution thread while Deep Research completes, the CLI returns an interaction ID immediately, and the calling agent can resume its own work and check back on the delegated result at the appropriate point in its workflow.

---

### Microsoft Copilot: Visual Studio Gets a Unified SDK Chat Surface While Autopilot and Today Enter Private Preview

Microsoft's Copilot interaction-design advances in this window arrive on two separate tracks — the developer surface and the enterprise persistent-agent surface — and together they define the two ends of the Microsoft agentic UX spectrum: an IDE chat layer that is more capable and session-persistent, and a cloud-hosted agent that never stops working.

On the developer surface, 

Microsoft has introduced a new GitHub Copilot Chat experience in Visual Studio that extends the Copilot SDK foundation across Ask mode, Agent mode, and chat interactions — the updated experience supports more capable agentic workflows, longer-running sessions, and prompt caching to improve efficiency; developers can enable the new experience by navigating to Tools > Options > GitHub > Copilot > Copilot Chat.

 The significance of unifying Ask, Agent, and chat interactions under the same SDK foundation is the elimination of capability fragmentation: previously, features that worked in Ask mode were not always available in Agent mode, and vice versa — which created a discovery problem for developers who would try a workflow in one mode and find it unexpectedly broken in another. 

Starting in Visual Studio 2026 version 18.11, the new chat experience uses a shared Copilot SDK foundation also used by the Copilot CLI and GitHub Copilot app.

 The cross-tool SDK parity is the most important element: when the same foundation powers both the IDE chat and the CLI agent, prompt patterns, tool invocations, and agent behaviours transfer between surfaces without re-learning.

On the persistent-agent surface, the **Copilot Autopilot** and **Today** private previews entering active rollout this month represent the most consequential temporal-UX advance in the Microsoft ecosystem. 

Autopilot is a cloud-hosted agent inside Microsoft Copilot, previously called Scout, that you set up with a name, a role and a goal — it works across Teams, Outlook and documents in the Microsoft 365 tenant with its own identity, memory, computer and workspace.

 The "own identity" property is the trust-design primitive that makes Autopilot governable: 

it has a dedicated identity, meaning agent actions are distinguishable from human actions and can be assigned specific permissions.

 Meanwhile, 

Today is a "proactive, personalized command center across mail, calendar, Teams threads, meetings and tasks" — Microsoft said Today would enter private preview in October 2026 in Copilot, with Outlook and Teams to follow.

 The combination of Autopilot's background execution and Today's proactive command-centre surface is the correct architecture for an ambient enterprise agent: Today surfaces what requires attention, and Autopilot acts on the delegated objective without requiring the user to re-prompt for each step.

---

### Grok (xAI): Custom Moderation Controls Bring Per-Request Content Governance to the API Surface

xAI's most interaction-design-significant advance in this window is the addition of **Custom Moderation Controls** to the xAI API, published October 27 — a feature that shifts content governance from a platform-level static policy into a per-request developer-configurable contract.



You can now set content guidelines on text API requests — add a `guidelines` array to a Chat Completions or Responses API request to set how Grok handles content in the nsfw, violence, and profanity categories; Grok follows the guidelines as it writes its response.

 The interaction-design implication of per-request rather than per-account moderation is the ability to scope content behaviour to the specific context of each agentic invocation. An enterprise operator building a Grok-powered legal research agent and a creative writing agent in the same pipeline can now configure the appropriate content posture for each without maintaining separate API accounts or applying a blanket policy that would be either too restrictive for one workflow or too permissive for the other.



The diff adds the October 27 product entry with per-category behaviors: nsfw, violence, and profanity accept `decline`; cyber accepts `allow`.

 The category-specific accept/decline mapping is the correct trust-design architecture: rather than a single binary safe/unsafe toggle, operators get granular control that reflects the genuine differences between content risk profiles — a medical information agent might need `violence: decline` but `nsfw: allow` for clinical imagery, a combination that a binary toggle cannot express.

On the Grok Build pipeline side, 

Grok Build 1.0.70, released October 23, introduces blank lines between answered questions except in compact mode, and `/plugins` now counts only the plugin skills that load and says how many were skipped because they link outside the plugin folder.

 The plugin skill load reporting is a meaningful transparency improvement for multi-plugin agent sessions: previously, an operator who had configured several plugins had no easy way to know at session start which skills had successfully loaded and which had been silently skipped due to external link restrictions. 

Grok Build 1.0.69 added `/resume` on the dashboard listing sessions from every folder with the current folder and its checkouts first, and updated the welcome menu to list Resume session above New worktree.

 The cross-folder session resume is the temporal-UX fix that most directly addresses the multi-project developer workflow: an operator running separate agent sessions in multiple project directories can now resume any of them from the dashboard without navigating to each folder individually.

---

### Perplexity: Computer in Email Completes the Ambient Delegation Loop

Perplexity's most structurally significant interaction-design advance reaching practitioner attention in this window is not a new UI surface but the fullest expression yet of the ambient-delegation pattern: **Computer in Email**, which inverts the typical agentic workflow trigger from an in-app prompt to an email thread forward.



Perplexity Computer now works directly through email — users can email, forward a thread, or cc computer@perplexity.com to start a task, with Computer reading the full conversation and any attached files needed to complete it.

 The trust-design architecture of Computer in Email is where the interaction-design work is most clearly visible. 

Users send or forward computer@perplexity.com an email to start a Computer session from email — Computer reads the thread context and replies only to the verified sender in the same thread using that sender's existing connectors, permissions, and Memory.

 The three-part trust contract — verified sender, inherited permissions, existing memory — is the correct design for an ambient agent that operates outside the app: by refusing to reply to anyone other than the verified sender, Perplexity prevents a class of prompt-injection attacks where a forwarded email contains instructions designed to redirect the agent's output to a third party.



Results are returned in the same email thread, including deliverables such as spreadsheets, PDFs, and presentations — each request also creates a full Computer session that can be reviewed on the web or mobile, with the same steps and audit trail as tasks started directly in the app.

 The full audit trail creation for every email-triggered Computer session is the temporal-UX primitive that makes ambient delegation governable: a user who triggered a Computer session by forwarding a vendor email can review the full step-by-step execution — what the agent searched, what it reasoned, what it produced — from the web interface, even if the email thread only shows the final deliverable. This is the correct design for delegated agentic work: the convenience surface (email reply with attachment) and the audit surface (full session log) are separate but linked, satisfying both the user who wants simplicity and the compliance team that needs traceability.

Complementing this, 

Perplexity open-sourced SPACE, the sandbox platform behind Computer, to help developers build safer autonomous AI agents.

 SPACE's open-sourcing is the trust-design multiplier for the entire Computer platform: when the isolation layer that contains Computer's execution — its filesystem access, browser, and tool invocation surface — is publicly inspectable, enterprise security teams can audit the execution boundary directly rather than relying on Perplexity's attestation alone.

---

### Apple: MCP Arrives at the iWork Layer, Turning Pages, Keynote, and Numbers into Agent-Addressable Surfaces

Apple's October 27 announcement of AI assistants for its creative productivity suite deserves attention in this briefing not primarily because of the in-app assistant features, but because of the MCP integration that ships alongside them.



New MCP support, built on this platform, enables external AI agents and tools to read content, perform edits, and execute automated actions directly in Keynote, Pages, and Numbers.

 This is the most significant expansion of the MCP agent-addressable surface in the personal productivity space since Microsoft's Copilot UX components reached GA last week. 

Apple will introduce a beta AI assistant that combines its own models with OpenAI technology into Logic Pro, Keynote, Pages, and Numbers — Keynote, Pages, and Numbers will also support the Model Context Protocol (MCP), allowing them to be operated by external AI agents.



The interaction-design implication is direct: a Claude Code session, a ChatGPT agent, or a Perplexity Computer workflow running on macOS 27 can now programmatically open a Keynote presentation, instruct the Apple-provided MCP server to add a slide, edit a chart, or refine a paragraph in Pages — without requiring the user to switch apps or manually copy content between tools. 

In Keynote, the assistants can help shape slide designs, add animation and polish presentations; Pages users can get help drafting and reorganizing text; in Numbers, the assistant can run calculations, arrange data, recommend charts and create custom tables.

 The MCP support is what converts these from single-app assistant features into cross-agent primitives: the in-app assistant serves the individual user, while the MCP layer serves the orchestrating agent that has been delegated a document-production task.

---

## The Bigger Picture: Ambient Delegation, MCP at the OS Layer, and the iCloud Agent Gap

The 48 hours ending October 28, 2026 reveal a convergence that practitioners should track as its own structural shift: the Agent2Agent2Human trust contract is being renegotiated at the data layer, and the negotiation is happening simultaneously at four levels — personal email (ChatGPT's iCloud plugins and Perplexity's Computer in Email), identity (Claude Code 2.1.312's OIDC routing), document format (Apple's MCP in Keynote, Pages, and Numbers), and content policy (xAI's Custom Moderation Controls). What unites all four is that none of them are new agentic capabilities in the sense of the agent doing something it could not do before — they are all precision expansions of what the agent is permitted to see, touch, and act on, governed by new trust primitives at the boundary. OpenAI's iCloud plugins are the clearest articulation of this: the capability to read and send email existed; the trust-design work was scoping it to iCloud-only, requiring an app-specific password, and ensuring that the Dots proactive agent inherits that scope cleanly rather than expanding it silently. Perplexity's Computer in Email follows the same logic from a different angle: the ambient trigger (an email forward) is simple, but the trust architecture underneath — sender verification, permission inheritance, full audit trail — is the work that makes it safe enough for enterprise use. Apple's MCP addition to Keynote, Pages, and Numbers is the document-layer version of the same pattern: by publishing an MCP interface, Apple is not giving external agents new capabilities but giving them a governed, inspectable boundary through which to exercise the capabilities they already have. And Claude Code 2.1.312's OIDC fix is the identity-layer equivalent: the enterprise deployment was already trusted; the `oidc.user_id_claim` addition makes the trust binding stable across re-authentications rather than brittle. Together, these advances are not moving the frontier of what AI agents can do — they are moving the frontier of what AI agents can be trusted to do at scale, in production, in regulated environments, by users who never open the agent's native interface at all.

---

## References

[1] gradually.ai. (2026). *Claude Code Changelog (October 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[2] releasebot.io. (2026). *Anthropic Release Notes — October 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[3] github.com/anthropics. (2026). *Release v2.1.312 · anthropics/claude-code*. [https://github.com/anthropics/claude-code/releases/tag/v2.1.312](https://github.com/anthropics/claude-code/releases/tag/v2.1.312)

[4] help.openai.com. (2026). *ChatGPT release notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] macrumors.com. (2026). *ChatGPT Can Now Access Your iCloud Mail and Calendar*. [https://www.macrumors.com/2026/10/27/chatgpt-icloud-mail-calendar-plugin/](https://www.macrumors.com/2026/10/27/chatgpt-icloud-mail-calendar-plugin/)

[6] 9to5mac.com. (2026). *iCloud Mail and Calendar plugins now work with ChatGPT*. [https://9to5mac.com/2026/10/27/icloud-mail-and-calendar-plugins-now-work-with-chatgpt/](https://9to5mac.com/2026/10/27/icloud-mail-and-calendar-plugins-now-work-with-chatgpt/)

[7] ai.google.dev. (2026). *Release notes — Gemini API*. [https://ai.google.dev/gemini-api/docs/changelog](https://ai.google.dev/gemini-api/docs/changelog)

[8] aistudio.google.com. (2026). *Introducing the Gemini API CLI*. [https://aistudio.google.com/learn/introducing-the-gemini-api-cli](https://aistudio.google.com/learn/introducing-the-gemini-api-cli)

[9] aistudio.google.com. (2026). *Gemini API CLI — Gemini API Docs*. [https://aistudio.google.com/docs/cli](https://aistudio.google.com/docs/cli)

[10] windowsreport.com. (2026). *Visual Studio October 2026 Update Brings Major Git, Copilot, and Hot Exit Improvements*. [https://windowsreport.com/visual-studio-october-update-brings-major-git-copilot-and-hot-exit-improvements/](https://windowsreport.com/visual-studio-october-update-brings-major-git-copilot-and-hot-exit-improvements/)

[11] blogs.microsoft.com. (2026). *Introducing the new Copilot with Home, Code and Autopilot*. [https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)

[12] cellcog.ai. (2026). *Microsoft Copilot Autopilot: The AI Teammate, Explained*. [https://cellcog.ai/blog/microsoft-copilot-autopilot/](https://cellcog.ai/blog/microsoft-copilot-autopilot/)

[13] docs.x.ai. (2026). *xAI API Release Notes*. [https://docs.x.ai/developers/release-notes](https://docs.x.ai/developers/release-notes)

[14] x.ai. (2026). *Grok Build Changelog*. [https://x.ai/changelog/build](https://x.ai/changelog/build)

[15] releasebot.io. (2026). *xAI Release Notes — October 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[16] alternativeto.net. (2026). *Perplexity launches Computer in Email*. [https://alternativeto.net/news/2026/8/perplexity-launches-computer-in-email-to-give-its-ai-agent-instructions-from-your-inbox/](https://alternativeto.net/news/2026/8/perplexity-launches-computer-in-email-to-give-its-ai-agent-instructions-from-your-inbox/)

[17] releasebot.io. (2026). *Perplexity Release Notes — October 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[18] perplexity.ai. (2026). *Open-sourcing SPACE, the sandbox platform behind Computer*. [https://www.perplexity.ai/hub/blog](https://www.perplexity.ai/hub/blog)

[19] 9to5mac.com. (2026). *Apple Creator Studio gets powerful new AI features using OpenAI models*. [https://9to5mac.com/2026/10/27/apple-creator-studio-gets-powerful-new-ai-features-using-openai-models/](https://9to5mac.com/2026/10/27/apple-creator-studio-gets-powerful-new-ai-features-using-openai-models/)

[20] finance.biggo.com. (2026). *Apple to Update Apple Creator Studio in November With OpenAI-Integrated AI Assistant*. [https://finance.biggo.com/news/3b1fc039-3425-4969-ae20-3f0c577e81a8](https://finance.biggo.com/news/3b1fc039-3425-4969-ae20-3f0c577e81a8)

[21] explainx.ai. (2026). *Apple Keynote, Pages, Numbers Get AI Assistant + MCP (2026)*. [https://explainx.ai/blog/apple-creator-studio-ai-assistants-keynote-pages-numbers-logic-mcp-support-2026](https://explainx.ai/blog/apple-creator-studio-ai-assistants-keynote-pages-numbers-logic-mcp-support-2026)