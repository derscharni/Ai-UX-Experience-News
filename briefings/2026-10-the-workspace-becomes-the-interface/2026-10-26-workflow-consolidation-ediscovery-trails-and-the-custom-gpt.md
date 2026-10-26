# UX Briefing: Workflow Consolidation, eDiscovery Trails, and the Custom GPT Sunset

**October 26, 2026**

Good morning. The 48 hours ending October 26, 2026 are defined by four simultaneous convergences in the Agent2Agent2Human design space: platforms are absorbing their standalone surfaces into unified workflow canvases, governments and enterprises are demanding auditable AI conversation trails, and the oldest class of user-configured AI customisation — the Custom GPT — reaches its Enterprise creation deadline today. **Claude/Anthropic's** dominant UX story of this window is the **Claude Code Desktop parallel-session architecture**, which converts a single-agent IDE experience into a multi-agent coordination surface: nested sessions now report back to a single readable main thread, saved environments remember your cloud-or-SSH context, and the **Claude Code Projects redesign** delegates work from one coordinating conversation to parallel cloud sessions with shared memory. **ChatGPT/OpenAI** fires its most consequential interaction-design deadline of the autumn today, October 26: **Custom GPT creation ends for Enterprise workspaces**, marking the hard cutoff before December's full retirement — and the replacement plugin architecture, which combines reusable skills, reference files, connected apps, and optional MCP tools, rewrites the fundamental interaction contract for every GPT-based workflow. **Google Gemini** delivers the compliance-and-audit advance that enterprise teams have been waiting for: **Google Vault's filtered eDiscovery exports for Gemini in Workspace**, announced October 22, enable admins to export Gemini conversations from across Gmail, Drive, Docs, Sheets, Slides, and Meet — turning Gemini interactions from ephemeral AI sessions into governed, discoverable organisational records. **Microsoft Copilot** consolidates its interaction surface in Teams and Outlook this week with the **new Copilot Chat experience** — removing the Copilot entry from the Teams chat list and centralising Chat, Cowork, and Work IQ in left-side navigation — while **Copilot in SharePoint reaches general availability**, bringing AI content creation, metadata autofill, and plugin-connected external systems to every SharePoint site without special opt-in. **Grok (xAI)** publishes a live reference architecture for enterprise agentic operations: **IncidentWatch and IncidentSweep**, two Grok Bot teammates that monitor support queues, detect ticket spikes before internal alerts fire, and clear related backlogs in human-approved batches. **Perplexity** quietly ships the infrastructure advance with the widest long-term reach: a **hosted Remote MCP Server** at `api.perplexity.ai/mcp` with no local installation, and an **xhigh preset** upgrade that replaces GPT-5.6 Sol with Claude Opus 5.5 and raises the output budget to 512,000 tokens — a fourfold increase in the ceiling for the longest-running Computer agentic tasks.

---

## At a Glance: October 26 Highlights

Today's releases converge on a single structural realisation that the industry's product teams have been building toward all autumn: the next frontier of Agent2Agent2Human experience design is not launching new surfaces but making existing surfaces governable — auditable, cancellable, delegatable, and consolidatable — because agents that can't be inspected, proven, and handed off between humans aren't yet enterprise-safe.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code Desktop parallel-session architecture ships nested sessions and saved environments; Claude Code Projects beta delegates to parallel cloud sessions with shared memory; Claude Frontier Academy announced October 26** — nested sessions report results back to a single readable main thread; saved environments preserve cloud, SSH, or local folder setups for one-click session starts; Projects gives one coordinating conversation the ability to fan work out to parallel cloud threads. [1][2][3] |
| **ChatGPT** | **Custom GPT creation ends for Enterprise workspaces today (October 26) as the plugin migration deadline hits; workspace analytics in Admin Console reorganised with Workplace health tracking and 7-day personal migration grace period shipping October 23** — Custom GPTs retire entirely December 11 with GPT instructions migrating as Skills, knowledge files as reference files, and custom actions requiring MCP rebuilds; the new UI already prompts users to create a plugin instead of a GPT. [4][5][6] |
| **Google Gemini** | **Google Vault gains filtered eDiscovery exports for Gemini in Workspace, announced October 22; Gemini in Sheets arrives on iOS October 23; Gemini app interactive apps now publish directly to Google Sites** — Vault exports cover Gemini conversations across Gmail, Drive, Docs, Sheets, Slides, and Meet, filterable by user, OU, and date; iOS Sheets brings AI data analysis on mobile; one-click Sites export converts Gemini app builds to fully interactive, shareable pages. [7][8][9] |
| **Microsoft Copilot** | **Copilot Chat gets a redesigned unified interface in Teams and Outlook removing the chat-list entry; Copilot in SharePoint reaches general availability; Copilot UX components (SPFx 1.24) reach GA** — the consolidated Chat/Cowork/Work IQ interface centralises all Copilot access at left-side navigation; SharePoint GA brings metadata autofill, plugin-connected external systems, site analytics, and suggestion chips to every site; UX components enable rich interactive cards rendered directly inside the Copilot canvas. [10][11][12] |
| **Grok (xAI)** | **IncidentWatch and IncidentSweep Grok Bot teammates published as a live enterprise reference architecture; Grok Build 1.0.67–1.0.70 ships headless exit fixes, worktree approval improvements, and theme-picker reliability** — IncidentWatch reviews 15 minutes of ticket history every 5 minutes and alerts on-call engineers with spike data; IncidentSweep clears the matching backlog in one human-approved batch; 1.0.67 fixes headless mode hanging after background task completion. [13][14][15] |
| **Perplexity** | **Remote MCP Server launches at api.perplexity.ai/mcp with no local install; xhigh Agent API preset upgraded from GPT-5.6 Sol to Claude Opus 5.5 with output budget raised to 512,000 tokens** — any MCP client supporting Streamable HTTP can connect with an API key bearer token; the xhigh model swap targets complex long-horizon Computer tasks; the 4× token budget increase lifts the ceiling on the deepest agentic research runs. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Multi-Session Orchestration Becomes a Native Desktop Interaction Pattern

The most consequential Claude interaction-design advance crystallising in this window is not a single feature launch but the completion of a multi-part architectural shift: the **Claude Code Desktop parallel-session architecture** that Anthropic shipped October 14 and that practitioners are now actively evaluating against the week's other parallel-agent surfaces.



The desktop app has been rebuilt for people who run several sessions at once: when you ask Claude to run tasks in parallel, it starts a nested session for each one, and each nested session reports its result back into the main session when it finishes, so the main thread stays readable.

 The interaction-design significance of the "readable main thread" constraint is the correct one for multi-agent developer workflows: rather than requiring the practitioner to monitor N separate terminal windows or a separate orchestration dashboard, the coordination surface stays in the familiar single-thread chat model while the agent network runs in the background.



Parallel tasks now open as nested sessions that report back to the main one, a setup of folders, an SSH host or the cloud can be saved as an environment, and the sidebar shows which session is waiting for you.

 The saved environments primitive is the low-friction element that will drive adoption: rather than re-specifying a project's context at the start of every session, practitioners save a configuration once — local folder, SSH host, or cloud — and instantiate it in one click. 

You can also save a setup as an environment, such as a few folders, an SSH host, or the cloud, and start sessions there; if you work in git projects, you can also give each folder its own worktree, so parallel sessions each edit their own copy of the files.

 The worktree isolation per parallel session prevents the class of conflicts where multiple coding agents simultaneously edit the same file — a fundamental safety property for autonomous multi-agent coding workflows.

The **Claude Code Projects redesign** extending this architecture into the cloud is the temporal-UX advance that practitioners should track most closely. 

Anthropic's redesigned Projects beta gives Claude Code one coordinating conversation that delegates work to parallel threads — threads that are usually cloud sessions, which Anthropic's docs now list as available, no longer in research preview, on Pro, Max, and Team and for eligible Enterprise seats.

You can run multiple sessions in parallel, branch off side chats, let Claude check on and message your other sessions, send work to the cloud, or let Dispatch start sessions for you from your phone.

 The Dispatch trigger — starting sessions from a phone — is the temporal-UX primitive that closes the last gap in the cloud-session model: a practitioner can initiate a long-running cloud coding task during a commute, receive the nested session results in the main thread, and review the outcome without ever opening a laptop. 

On October 26, Anthropic also announced a $100 million investment in the Claude Frontier Academy to train 10,000 Frontier Deployed Engineers by the end of 2027.



---

### ChatGPT / OpenAI: The Custom GPT Sunset Creates the Most Significant Interaction-Architecture Migration in ChatGPT's History

OpenAI's most consequential interaction-design event in this window is not a new surface but a hard deadline that closes an era: **October 26, 2026** — today — is the date when creation of new Custom GPTs ends for affected Enterprise workspaces, beginning the final migration sprint toward December's full retirement.



Custom GPTs are scheduled to retire on December 11, 2026; for affected Enterprise workspaces with an approved deferral, the retirement date is February 11, 2027.

 The magnitude of this migration is best understood through what does and does not transfer. 

Under the planned migration workflow, the GPT's instructions become a skill within the new plugin, connected apps are added to the plugin as apps, the GPT's knowledge files are copied into the plugin's reference files, but the GPT's selected model does not carry over.

 The model-selection gap is the trust-design implication that enterprise teams must audit explicitly: any Custom GPT that was configured with a specific model for deterministic output behaviour will, after migration, inherit the workspace's Enterprise defaults — a silent behaviour change that will not be visible in the migration summary.



The replacement plugin architecture combines reusable skills with reference files, connected apps and optional MCP-based tools; organisations will need to test migrated workflows because sharing settings, existing conversations and Custom Actions do not automatically transfer.

OpenAI has changed its UI to make GPTs less prominent, and when users choose to try creating a new Custom GPT, they are now prompted with an option to create a plugin instead.

 The prompt-to-create-plugin interaction is the correct progressive-disclosure design for a deprecation: rather than surfacing a hard error at the creation boundary, OpenAI redirects the user's intent toward the migration path at the moment of creation intent — a more instructive UX than a gated refusal.

The second significant OpenAI interaction-design advance in this window is the **Admin Console workspace analytics reorganisation** shipping October 23. 

Workspace analytics for ChatGPT Enterprise and Edu now spans Usage and Insights in Admin Console; Benchmarks and User surveys are under Insights, with User surveys replacing the Impact tab; Usage > Overview now includes Workplace health to track workspace adoption, and the usage export flow also supports a by-user report.

 The Workplace health signal is the governance primitive that was missing from the previous analytics surface: it gives admins a single metric for whether the organisation is actually using the Copilot investment rather than requiring them to infer adoption from per-feature usage counts. 

The update also adds a fixed seven-day grace period for verified-domain users migrating personal workspaces, while access remains blocked until migration or deactivation.



---

### Google Gemini: Vault eDiscovery Turns Gemini Conversations into Governed Organisational Records

Google's most structurally significant interaction-design advance in this window — and the one with the greatest long-term enterprise adoption implication — is not a new input modality or a new generation surface, but a compliance primitive: **Google Vault's filtered eDiscovery exports for Gemini in Workspace**, announced October 22.



Google Vault now supports eDiscovery filtered exports for Gemini in Workspace, adding a new data source to AI compliance capabilities, allowing administrators to filter and export users' Gemini in Workspace conversations across apps like Gmail, Drive, Docs, Sheets, Slides and Meet in line with the security controls and privacy provisions of Vault.

 The interaction-design significance of this advance is the reclassification of Gemini sessions: before this release, a Gemini conversation in Gmail or Docs was ephemeral AI assistance — present in the session, absent from the compliance record. After this release, 

exports include user prompts, AI responses, generated attachments such as images, and links to referenced Workspace files such as Drive documents or Gmail threads and citations.

 This makes the full Agent2Human interaction — question, reasoning, output, and the source documents the agent cited — auditable in a single export, which is the correct trust-design architecture for regulated industries operating under eDiscovery obligations.

The filtering granularity is the practitioner-facing design choice that matters most. 

Admins can define export scopes by specific user accounts or organisational units up to 5,000 users in size, and filter by a specific date range with time zone selection.

Admins can use OU-level conversation history and deletion settings in the Admin console to govern data retention, such as preventing manual conversation deletion by users or configuring automatic deletion after a period of inactivity.

Additional information governance features for Gemini in Workspace, such as retention rules and litigation holds, will follow in future releases.

 The explicit roadmap disclosure of what is *not yet available* — retention rules and litigation holds — is the correct transparency posture: it tells legal and compliance teams precisely which workflows they cannot yet rely on Vault for, preventing over-reliance on a partial compliance surface.

The two additional Workspace advances this week extend the Gemini interaction surface in complementary directions. 

Building upon Gemini in Sheets on the web and its recent launch on Android, Gemini in Google Sheets is now available on iOS devices to quickly analyze and understand data while on the go.

Users can now export interactive apps built in the Gemini app directly to Google Sites — with one click, the app is added to a new, private site draft, fully interactive and ready to customize, from where users can add more content, publish the site, and share it just like any other Google Site.

 The Sites export pattern is the correct agentic-output design for collaborative distribution: rather than requiring the recipient to have Gemini app access to view a generated interactive tool, the export converts it into a standard Google Site artefact that any Workspace user can access and interact with.

---

### Microsoft Copilot: Copilot in Teams Consolidates, SharePoint Reaches GA, and UX Components Unlock Generative Canvases

Microsoft's Copilot interaction-design story in this window has three simultaneous components that, together, represent the most comprehensive Copilot surface consolidation since the product's original launch: a **navigation redesign in Teams and Outlook**, **Copilot in SharePoint reaching general availability**, and **Copilot UX components reaching GA with SharePoint Framework 1.24**.

The navigation redesign is the interaction-design change that affects the largest number of daily Microsoft 365 users immediately. 

Two updates are rolling out in Teams right now: a small popup lets users know the Copilot option in the Teams chat list is being removed — that's intentional, as it leaves one central place, the left-side navigation, to get to the full Copilot Chat experience.

The experience is getting a new interface that now matches the full Copilot Chat interface, with the ability to switch between Chat and Cowork, toggle Work IQ on or off, see pinned agents or open all agents, and find chat history on the left.

 The UX implication of removing the chat-list entry is the elimination of an ambiguous entry point: users who previously navigated to Copilot via the Teams chat list encountered a subset of the capability; the consolidated left-nav surface delivers the full Chat/Cowork/Work IQ interface as the only path, removing the capability-tier discovery problem.



Copilot in SharePoint is now generally available — every user can now create and organize content, ask questions grounded in their SharePoint data, enrich libraries with AI-generated metadata, and build reusable skills; advanced capabilities include image generation and editing, AI-generated site analytics reports, and near real-time metadata autofill.

 The **suggestion chips** that shipped alongside the GA are the in-context interaction design advance most likely to change how users experience Copilot in SharePoint day-to-day: 

after Copilot responds, users see contextual follow-ups right under the answer, helping to refine the result, dig deeper, or take the next action — so users never have to stare at an empty prompt box wondering what to ask next.



The developer-platform advance with the deepest long-term UX implications is **Copilot UX components reaching general availability with SharePoint Framework 1.24**. 

Copilot UX components — rich, interactive experiences rendered directly in Microsoft 365 Copilot — are on track for general availability in October 2026 for all customers worldwide, together with SharePoint Framework 1.24.

This makes it possible to approve an expense, check remaining leave, or book a desk without ever leaving the chat to hunt for the right tool — and this is now possible with the UX components in the Copilot canvas using the MCP apps model.

 This is the correct generative-UI design primitive for enterprise Copilot: rather than Copilot's responses being limited to text and citations, UX components let developers render transactional, interactive forms inside the Copilot conversation — converting the chat canvas from a read-only output surface into a first-class action surface.

---

### Grok (xAI): IncidentWatch and IncidentSweep Publish the Operational Blueprint for Human-Approved Agent Collaboration

xAI's most interaction-design-significant contribution in this window is not a CLI fix or a subscription change but a published reference architecture for enterprise Grok Bot deployment: **IncidentWatch and IncidentSweep**, two production Grok Bot teammates that xAI's own engineering team built and now operates publicly as an open design pattern.



xAI adds IncidentWatch and IncidentSweep to Grok Bot, giving support teams AI teammates that spot ticket spikes, flag potential incidents, and clear related backlogs with engineer approval — the tools help teams manage customer responses from early reports through resolution.

 The temporal-UX design of IncidentWatch is the correct pattern for proactive agentic monitoring: 

IncidentWatch monitors the support queue for spikes in similar tickets and alerts the team when it sees one; when several customers report the same issue at once, those tickets can be an early signal of an incident; IncidentWatch detects that signal by reviewing the previous 15 minutes of tickets for spikes around the same problem every five minutes.

 The five-minute polling cadence with a 15-minute lookback window is a deliberate temporal-UX decision: it balances early detection against false-positive fatigue, surfacing the agent's attention to a human only when the pattern is statistically meaningful — not at every ticket arrival.



IncidentSweep clears the related backlog in an approved batch

 — and the "approved batch" framing is precisely the correct trust-design architecture for a high-stakes, customer-facing action. An agent that could clear hundreds of support tickets individually without human review would be a governance failure; an agent that assembles the batch, presents it for a single approval decision, and executes in one confirmed action gives the engineer both oversight and efficiency. 

When a product incident hit and hundreds of customers were waiting for an answer, a Grok Bot called IncidentSweep cleared the backlog in one approved batch.



On the Grok Build pipeline reliability front, 

Grok Build 1.0.67 fixes headless `grok -p` runs that would hang when a background task or subagent finished and its output was read in the same turn, and the theme picker in Settings now correctly restores the previous theme when the user leaves it without confirming.

Grok Build 1.0.66 restores themes when leaving the picker, keeps selected rows readable across themes, and speeds up file completion results; a worktree name that is already taken is now refused instead of silently getting a numbered suffix.

 The worktree naming fix is the most consequential of these: in multi-agent workflows where parallel sessions each work in their own worktree, a silent auto-suffix renaming was a source of session confusion — agents working in `feature-branch-1` and `feature-branch-2` without the operator having specified two branches.

---

### Perplexity: Remote MCP and the xhigh Model Swap Define the Next Architecture of Long-Horizon Computer Tasks

Perplexity's most significant interaction-design advances in this window are API-layer changes whose surface implications will take weeks to propagate through consumer and enterprise Computer workflows — but their design logic deserves attention now because they establish the template for how Perplexity is thinking about the architecture of its deepest agentic tasks.

The **Remote MCP Server** is the simpler of the two advances but the one with broader reach: 

the Perplexity MCP Server is now available as a remote server hosted by Perplexity at `https://api.perplexity.ai/mcp`.

Any MCP client that supports Streamable HTTP can connect using an API key as a bearer token, with no local installation and nothing to update.

 The interaction-design significance of the "nothing to install or update" constraint is the elimination of the local dependency management friction that has made MCP adoption slower than the standard's technical quality warrants: a developer integrating Perplexity search into a Claude Code session, a Grok Build pipeline, or a Copilot plugin can now point to a URL rather than maintaining a local server process, version, and credential store.

The **xhigh Agent API preset** change is the deeper architectural signal. 

The Agent API xhigh preset now allows up to 512,000 output tokens, up from 128,000; the xhigh preset has used Fast Search since the October update that moved low, medium, and high to Fast Search.

The xhigh preset model has also been upgraded from `openai/gpt-5.6-sol` to `anthropic/claude-opus-5-5` — prompts, reasoning effort, tools, token budgets, and step limits are otherwise unchanged.

 The model swap is a governance choice with direct UX consequences: GPT-5.6 Sol and Claude Opus 5.5 behave differently at extended context lengths, have different tool-call patterns, and produce different citation styles — any Computer workflow running at xhigh that has been tuned to Sol's output shape will need to be re-evaluated against Opus 5.5's behaviour. The fourfold token budget increase is the temporal-UX advance that matters for the class of research workflows that previously hit the 128K ceiling mid-task: rather than a graceful truncation or an abrupt task failure, those workflows can now complete their full reasoning arc inside a single xhigh run.

---

## The Bigger Picture: Workflow Consolidation, eDiscovery Trails, and the Custom GPT Sunset

The 48 hours ending October 26, 2026 mark the moment the industry moved from building new agentic surfaces to governing the ones it already shipped — and three of today's most consequential UX advances are not launches but endings and consolidations. OpenAI's Custom GPT creation deadline is the clearest statement: the four years of GPT-as-customisation-primitive are over, and the plugin architecture that replaces it is not a GPT with a new name but a fundamentally different interaction model — one where reusable instructions, knowledge files, connected apps, and MCP tools are explicitly separated, composable objects rather than a single opaque configuration. Google Vault's Gemini eDiscovery exports make the same architectural argument from the compliance layer: an AI agent that produces work inside Gmail, Docs, and Meet but whose outputs are not discoverable is not enterprise-safe, and the conversation trail that Vault now captures — prompt, response, generated attachment, source link, citation — is the minimum viable audit record for regulated industries. Microsoft's simultaneous moves — Teams navigation consolidation, SharePoint GA, and Copilot UX components reaching GA — are the enterprise equivalent of the same consolidation thesis: Copilot is most valuable when it is one surface that the user never has to leave, not three adjacent tools with overlapping scope. Anthropic's parallel-session architecture for Claude Code applies the same principle to the developer workflow: a multi-agent coding environment that requires the developer to monitor N terminals is not a productivity gain but a cognitive load increase; nested sessions that report to a single readable main thread are the correct delegation contract. xAI's IncidentWatch and IncidentSweep reference architecture is the most honest articulation yet of what "human-approved batch action" should look like in production: the agent monitors continuously, assembles work at scale, and brings it to a human at the single moment of maximum leverage — not as a per-action approval gate, and not as an autonomous execution that bypasses review. Perplexity's xhigh model swap and Remote MCP Server are the quiet infrastructure moves that complete the picture: when the deepest agentic tasks run on the best available reasoning model and the search grounding layer is a zero-install URL rather than a local process, the floor for production-quality Computer workflows rises for every developer who plugs in — whether their orchestrator is Claude, Grok, Copilot, or a custom pipeline.

---

## References

[1] aimaker.substack.com. (2026). *Claude Code Desktop Now Runs in the Cloud, in Parallel, and From Your Phone*. [https://aimaker.substack.com/p/claude-code-updates-october-2026](https://aimaker.substack.com/p/claude-code-updates-october-2026)

[2] prompthackers.co. (2026). *Claude Code Desktop Update: Nested Sessions, Environments and /btw*. [https://www.prompthackers.co/ai-news/claude-code-desktop-parallel-sessions](https://www.prompthackers.co/ai-news/claude-code-desktop-parallel-sessions)

[3] aicatchup.com. (2026). *Claude Code Projects: Parallel Cloud Sessions, Shared Memory, and Project Limits*. [https://aicatchup.com/news/claude-code-projects-parallel-cloud-sessions](https://aicatchup.com/news/claude-code-projects-parallel-cloud-sessions)

[4] help.openai.com. (2026). *Custom GPT retirement and migration FAQ*. [https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq)

[5] virtualizationreview.com. (2026). *OpenAI to Retire Custom GPTs, Replace Them with Plugins*. [https://virtualizationreview.com/articles/2026/09/28/openai-to-retire-custom-gpts-replace-them-with-plugins.aspx](https://virtualizationreview.com/articles/2026/09/28/openai-to-retire-custom-gpts-replace-them-with-plugins.aspx)

[6] help.openai.com. (2026). *ChatGPT Enterprise and Edu release notes*. [https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)

[7] workspaceupdates.googleblog.com. (2026). *Google Vault now supports filtered exports for Gemini in Workspace*. [https://workspaceupdates.googleblog.com/2026/10/google-vault-now-supports-filtered-exports-for-Gemini-in-Workspace.html](https://workspaceupdates.googleblog.com/2026/10/google-vault-now-supports-filtered-exports-for-Gemini-in-Workspace.html)

[8] workspaceupdates.googleblog.com. (2026). *Google Workspace Weekly Recap - October 23, 2026*. [https://workspaceupdates.googleblog.com/2026/](https://workspaceupdates.googleblog.com/2026/)

[9] workspaceupdates.googleblog.com. (2026). *Publish interactive apps from the Gemini app to Google Sites*. [https://workspaceupdates.googleblog.com/](https://workspaceupdates.googleblog.com/)

[10] m365copilotconnection.substack.com. (2026). *Copilot's biggest October 2026 updates, and when they land*. [https://m365copilotconnection.substack.com/p/copilots-biggest-october-2026-updates](https://m365copilotconnection.substack.com/p/copilots-biggest-october-2026-updates)

[11] techcommunity.microsoft.com. (2026). *What's new in Copilot in SharePoint: October 2026*. [https://techcommunity.microsoft.com/blog/spblog/what%E2%80%99s-new-in-copilot-in-sharepoint-october-2026/4535423](https://techcommunity.microsoft.com/blog/spblog/what%E2%80%99s-new-in-copilot-in-sharepoint-october-2026/4535423)

[12] devblogs.microsoft.com. (2026). *Going beyond text in Microsoft 365 Copilot — Introducing SharePoint Copilot Apps*. [https://devblogs.microsoft.com/microsoft365dev/going-beyond-text-in-microsoft-365-copilot-introducing-sharepoint-copilot-apps/](https://devblogs.microsoft.com/microsoft365dev/going-beyond-text-in-microsoft-365-copilot-introducing-sharepoint-copilot-apps/)

[13] x.ai. (2026). *Using Grok Bot to detect and respond to incidents*. [https://x.ai/news/incident-sweep](https://x.ai/news/incident-sweep)

[14] releasebot.io. (2026). *xAI Release Notes — October 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] x.ai. (2026). *Grok Build Changelog*. [https://x.ai/changelog/build](https://x.ai/changelog/build)

[16] docs.perplexity.ai. (2026). *Changelog — Perplexity*. [https://docs.perplexity.ai/docs/resources/changelog](https://docs.perplexity.ai/docs/resources/changelog)

[17] github.com/perplexityai. (2026). *Perplexity API Platform MCP Server*. [https://github.com/perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)

[18] releasebot.io. (2026). *Perplexity Release Notes — October 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)