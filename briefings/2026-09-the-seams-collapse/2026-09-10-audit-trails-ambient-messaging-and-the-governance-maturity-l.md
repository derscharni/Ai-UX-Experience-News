# UX Briefing: Audit Trails, Ambient Messaging, and the Governance Maturity Layer

**September 10, 2026**

Good morning. The 48 hours ending September 10, 2026 are defined by a powerful cross-platform theme: as every major agentic product matures from capability demonstration into enterprise deployment, the releases this window are dominated by the observability, audit, and governance primitives that make that deployment durable — not just trusted in theory, but provably inspectable in practice. **Claude/Anthropic** opens the window with its most consequential model-and-tooling week of the year: **Claude Fable 5.1 and Mythos 5.1 launching September 1** as the new default Fable-tier models for Claude Code, the API, and Cursor, bringing a 75% cache-read price cut that makes highly agentic coding workflows 45% cheaper to operate, alongside Claude Code shipping the **fullscreen diff panel** (`/diff`), organisation policy diagnostics in `/status`, and raised inline output limits via `bashOutputMaxChars` and `taskOutputMaxChars`. **ChatGPT/OpenAI**'s defining event is the integration of **GPT-6 Astra into Codex and ChatGPT Work** — a model whose ScreenSpot Pro UI-element targeting score jumped from 76.9% to 92.7% and whose computer-use task time dropped ~47%, materially advancing what delegated automation can accomplish without mid-task human correction — alongside the **Apple Messages plugin** reaching all macOS plans with a default approval gate for every send action. **Google Gemini** ships a governance triple that together completes the full enterprise-readiness cycle for Gemini Notebook: **comprehensive audit logs in the Admin console** rolling out September 3, **custom instructions expanding cross-surface to Drive, Chat, Gmail side panel, Sheets, and Slides**, and the Meet–Teams hardware interoperability reaching Android AOSP devices. **Microsoft Copilot** hits the most structurally consequential moment of its app-consolidation arc as the **unified Copilot app begins its worldwide Windows and Mac desktop rollout in mid-September** — merging consumer Copilot and Microsoft 365 Copilot into a single shell — while Planner task creation rolls live in September and the Excel `=COPILOT()` formula retirement on September 14 forces all users toward the auditable side-pane agent workflow. **Grok (xAI)** delivers the enterprise governance event of its product history: **Grok Bot for Enterprise launches with access, network, and audit controls** — including Action Recording of what Bots actually do and OpenTelemetry Export for streaming audit data into existing monitoring stacks — paired with Grok Build shipping MCP retry improvements, more accurate token counts, and context bar updates on auto-compaction. **Perplexity** continues consolidating Computer in Email as the industry's lowest-friction async delegation entry point while the Bumblebee MCP-config scanner extends the trust surface at the tool-configuration layer.

---

## At a Glance: September 10 Highlights

Today's releases converge on a single maturity signal: every platform is simultaneously shipping the audit trails, governance controls, and trust-design primitives that convert their agentic capabilities from individually impressive features into organisationally deployable systems.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Fable 5.1 and Mythos 5.1 launch September 1 as new default Fable models** — 75% cache-read price cut makes agentic coding workflows up to 45% cheaper; Claude Code ships fullscreen `/diff` panel showing uncommitted changes beside conversation; `bashOutputMaxChars`/`taskOutputMaxChars` settings raise inline output limits to 128K; organisation policy diagnostics added to `/status` and `claude doctor`; `/advisor` text form added for headless and remote-control sessions. [1][2][3] |
| **ChatGPT** | **GPT-6 Astra rolls out to Codex and ChatGPT Work** — ScreenSpot Pro UI-targeting accuracy jumps from 76.9% to 92.7%, OSWorld 2.0 computer-use task time drops ~47%; Apple Messages plugin launches on all macOS plans with default per-send approval gate; Computer History expands to EEA, Switzerland, and UK; read-only Codex chat share links available; pinned Codex chats sync across desktop and iOS. [4][5][6] |
| **Google Gemini** | **Gemini Notebook audit logs reach GA in the Admin console September 3** — full visibility into notebook actions including user identity, IP address, and resource context via security investigation and BigQuery export; Gemini custom instructions expand to Drive, Chat, Gmail, Sheets, and Slides starting September 2; Meet–Teams Android AOSP hardware interoperability enters Early Preview. [7][8][9] |
| **Microsoft Copilot** | **Unified Copilot app begins worldwide Windows/Mac desktop rollout mid-September** — consumer Copilot and Microsoft 365 Copilot merge into single shell with refreshed icon and copilot.cloud.microsoft URL; Excel `=COPILOT()` formula retires September 14 in favour of side-pane agent workflow; Planner task creation and querying goes live in September; Copilot can now query private Viva Engage communities. [10][11][12] |
| **Grok (xAI)** | **Grok Bot for Enterprise launches with access, network, and audit controls** — Action Recording logs what Bots actually do; OpenTelemetry Export streams audit data to existing monitoring stacks; each Bot runs in an isolated cloud environment with no access by default; Grok Build ships MCP retry improvements, accurate token counts after rewind/mode-switch, and immediate context bar updates on auto-compaction. [13][14][15] |
| **Perplexity** | **Computer in Email active for all Computer users; Bumblebee MCP-config scanning active** — forward threads to computer@perplexity.ai to start sessions using existing connectors, permissions, and Memory; enterprise reply-all support coming soon; Search as Code reliability holds at 92.6%; Bumblebee open-sourced for supply-chain MCP-config scanning with human-review-before-propagate workflow. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Fable 5.1, the Diff Panel, and the Cost–Delegation Compact

Anthropic's most consequential Claude Code UX event in this window is not a single feature but a compounding combination: **Claude Fable 5.1 launching September 1** as the new default model for Claude Code, the API, and Cursor, paired with Claude Code's dense September update wave that together make long-running agentic sessions both more capable and more navigable.



Anthropic released Claude Fable 5.1 and Mythos 5.1 — the same underlying model shipped under two different safeguard regimes — with Fable 5.1 generally available and leading on agentic coding, knowledge work, and long-horizon problem solving, while Mythos 5.1 is restricted to vetted cybersecurity and life sciences users.

 The UX implication of the safeguard-regime split is significant: 

for most Claude applications, queries flagged by cybersecurity safeguards automatically route to Opus 4.8, and biology safeguards route to Opus 5

 — a transparent, model-level safety routing system that handles sensitive-domain requests without requiring the user to manage the routing themselves.

The interaction-design event that matters most for enterprise practitioners is the **cache-read pricing restructure**. 

Cached input tokens drop to 25 cents per million — a 75% reduction compared to Fable 5 — bringing typical workload costs down by about 25%, and highly agentic workload costs down by as much as 45%.

 The UX significance of this is not abstract economics: it is the difference between a team that reaches for Fable 5.1 confidently on every long multi-step research or coding session and a team that reserves it for exceptional tasks. When the cost of delegation drops 45% for context-heavy agentic work, the mental model of when to delegate changes — the agent becomes the default tool for long-running tasks, not the expensive exception.

On the tooling side, 

Claude Code adds a diff panel that opens beside the conversation in fullscreen mode and shows uncommitted changes as Claude edits, toggled with `/diff`.

 This is the spatial UX fix that multi-file agentic editing has required: rather than switching between conversation and a diff tool, the developer's uncommitted change state is continuously co-visible with the agent's ongoing narration. The companion output-limit additions — 

`bashOutputMaxChars` and `taskOutputMaxChars` settings to raise how much command and background-task output Claude receives inline before it is saved to a file, up to 128K characters

 — are the configuration primitives that prevent the agent from operating on truncated context during long shell operations. Together, the diff panel and raised output limits address the two most common sources of agentic-session degradation: the agent editing without the developer seeing the full change state, and the agent receiving incomplete output from long-running commands.

---

### ChatGPT / OpenAI: GPT-6 Astra and the Computer-Use Precision Leap

OpenAI's most interaction-design-significant event in this window is the **GPT-6 Astra rollout into Codex and ChatGPT Work** — a model whose agentic computer-use capabilities represent the single largest precision improvement in the category this year, converting delegated computer-use sessions from probabilistic screen-navigation attempts into reliably targeted UI interactions.



OSWorld 2.0 scores rose from roughly 65.7% for GPT-5.6 Sol to 72.6% for Astra, completed tasks in about 40 minutes versus 75 minutes for Sol — and ScreenSpot Pro, which tests whether a model can locate and click the right UI element on a screen, jumped from 76.9% to 92.7%.

 The UX implication of ScreenSpot Pro rising to 92.7% is not incremental: it crosses the threshold at which UI-element targeting is reliable enough that users can reasonably delegate professional-software workflows — design tools, admin dashboards, spreadsheet applications — without expecting the agent to repeatedly misclick and require manual correction. 

Independent testing puts Astra's broad intelligence score roughly level with its predecessor, but on tasks that involve operating a computer over long stretches, using a browser, running terminal commands, or probing software for security flaws, it posts some of the largest jumps seen in a single release — that split between "same intelligence, much better agent" is the core story of this launch.



The **Apple Messages plugin** is the other interaction-design event with immediate UX consequence. 

On Apple silicon Macs, the Apple Messages plugin in the ChatGPT desktop app can read and search iMessage, SMS, and RCS conversations and prepare or send messages through Messages — and by default, ChatGPT asks the user to approve the message and recipients before sending.

 The default-approval gate here is the correct trust-design choice for a messaging action with immediate, irreversible social consequences: the agent prepares the message and surfaces it for human review rather than sending autonomously. 

By default, ChatGPT sends messages only after you approve the message and its recipients — and the plugin guide explicitly documents persistent-approval risks and revocation steps.

 The explicit documentation of persistent-approval risks is the transparency signal that makes this feature enterprise-adjacent: the documentation names the failure mode rather than hiding it in fine print.



Computer History is now available in the EEA, Switzerland, and the United Kingdom for Pro users in the ChatGPT desktop app on macOS — it is off by default and requires Memories.

 The regional expansion of Computer History matters because it brings agentic session recall into regulatory environments where user-data handling carries legal obligations — and the off-by-default posture acknowledges that explicitly, placing the activation decision with the user rather than defaulting to maximum capability.

---

### Google Gemini: Notebook Audit Logs, Cross-Surface Instructions, and the Governance Triple

Google's most consequential enterprise governance event in this window is the **Gemini Notebook audit log launch** — the transparency primitive that converts Gemini Notebook from a productivity surface into an auditable enterprise tool, completing a three-stage governance cycle alongside custom-instruction expansion and Context-Aware Access policies.



Google Workspace administrators can now access comprehensive audit logs for Gemini Notebook in the Admin console, providing greater insights into how the application is used across their organisations — introducing full visibility into Gemini Notebook actions and allowing administrators to track a wide range of user actions across multiple categories, including notebook visibility, user identity, IP address, and resource context.

 The UX significance of this runs deeper than compliance checkbox: before this audit log landed, a Gemini Notebook session was a black box to the admin — the user interacted with AI-grounded content, but the admin had no structured record of which notebooks were accessed, by whom, from which IP, or in what context. 

Gemini Notebook audit logs are available by default in the Workspace Admin console, though exporting audit logs to BigQuery is disabled until turned on.

 The opt-in BigQuery export is the correct default for most organisations — it ensures that sensitive notebook interaction data is not flowing to an external data store unless the admin has explicitly decided it should.

The companion **custom instructions cross-surface expansion** completes the personalization-portability arc. 

Previously limited to Google Docs, you can now set persistent custom instructions for Gemini that apply across a broader range of surfaces — your preferences for tone, formatting, and style are now respected in Ask Gemini in Drive, Ask Gemini in Chat, and the Gemini side panel in Gmail, Sheets, and Slides.

 The interaction-design shift this establishes is from *per-surface personalisation* (the user re-states their preferences in each new Workspace context) to *identity-portable personalisation* (the user's preferences travel with their account, not with the application). 

The expansion moves custom instructions beyond Google Docs and integrates them into major workflow surfaces — cross-app sync means instructions are shared globally across eligible Workspace apps; if you add an instruction while working in Gmail, it automatically carries over to your side panels in Docs, Slides, and Sheets.

Google Vids now allows users to transform static Google Docs, PDFs, and Word files into engaging video summaries, leveraging AI to generate scripts and narration while providing custom visuals to bring documents to life.

 This document-to-video conversion is an agentic document-processing primitive that shifts the role of the agent from *document assistant* (answering questions about a document) to *document transformer* (converting a static artifact into a new format for a new audience). The governance consideration that enterprise deployments will need to address is provenance: AI-narrated video generated from company documents inherits both the document's sensitivity classification and the EU AI Act's emerging watermarking requirements for AI-generated audiovisual content.

---

### Microsoft Copilot: The Unified App Desktop Rollout and the Excel Formula Retirement

Microsoft's most structurally consequential Copilot UX event in this window is the **unified Copilot app beginning its worldwide Windows and Mac desktop rollout in mid-September** — the moment the two-year era of parallel consumer and enterprise Copilot experiences ends and a single product surface begins.



Microsoft is combining its consumer Copilot app and the Microsoft 365 Copilot app into a single application that handles both personal and work accounts — the consolidation is the first structural step toward the "super app" Microsoft has been building, and it ends a two-year stretch in which Microsoft shipped two separate Copilot apps that could sit side by side in the same taskbar.

 The UX significance of this consolidation is primarily about identity coherence: a user who previously managed two separate Copilot identities — one for personal account tasks, one for M365 work tasks — now encounters a single app that surfaces both contexts with 

updated visual cues that help identify whether they are in the Microsoft Entra ID (work or school) experience or the Microsoft account (personal) experience.

 The visual-cue design is the trust-design detail that matters most here: in a unified app, the most important transparency signal is which identity context the user is currently operating in, because the data access and compliance rules differ between them.

The **Excel `=COPILOT()` formula retirement on September 14** is the architectural statement that crystallises the Copilot team's design philosophy. 

Copilot will now support creating Planner tasks and querying Planner task information, letting users manage task work across Copilot and Planner more seamlessly — this feature rolls out in September.

 This closes the delegation gap that has existed since Planner Agent reached GA: a user can now create, query, and track Planner tasks from within a Copilot conversation, making Copilot a full read-write surface for the Planner task graph rather than a read-only window into it. The retirement of `=COPILOT()` reinforces the same design principle: 

the Copilot Notebooks user experience has been revamped with a streamlined flow for opening items and navigating the product — previously, users faced a more complex and less cohesive interface, and the new design simplifies common tasks and enhances consistency across the product.

 Moving AI actions out of volatile cell-level computation and into the side-pane agent workflow — where intent, context, action, and review are separated and inspectable — is the same bounded-autonomy principle that defines every trust-design advance in this window.

---

### Grok (xAI): Grok Bot Enterprise and the Agentic Audit Trail

xAI's most consequential UX event in this window is the **Grok Bot for Enterprise launch on September 3** — the governance-layer release that converts Grok Bot from a capable but ungoverned individual-use tool into an organisationally deployable agentic workforce product with the access controls, network boundaries, and audit primitives that enterprise IT and compliance teams require before authorising persistent autonomous agents.



Grok Bot is described as a team of helpful AI teammates — you delegate real tasks to them and they carry the job through end to end, working autonomously around the clock inside the same tools you use — and enterprises need the ability to govern Bots at scale, with today's release adding access, network, and audit controls that make that possible.

 The UX significance of the audit controls deserves specific attention. 

Grok Bot enterprise audit controls arrived on September 3, 2026, adding audit logs covering admin, security, and authentication events, Action Recording of what Bots actually do, and OpenTelemetry Export for streaming it all into an organisation's own monitoring stack.

 Action Recording is the transparency primitive that the agentic agent category has been missing: previously, the only record of what a persistent Bot had done was whatever it chose to report in the conversation thread. Action Recording creates an independent, machine-readable log of the Bot's actual actions — the audit trail that compliance teams require and that enterprise security teams need for post-incident investigation.

The security-design foundation beneath the audit controls is the **zero-access-by-default architecture**. 

Each user's work in Grok Bot runs in its own secure and isolated environment, separate from every other user — a Bot has no access by default and reaches only the accounts you sign it into.

 This is the correct starting posture for a persistent autonomous agent that retains credentials and state between sessions: the blast radius of a misconfigured or misbehaving Bot is bounded to the specific accounts the user has explicitly connected, not the full surface of the deploying organisation's systems. 

Each user's work runs in its own secure and isolated environment, separate from every other user, and a Bot has no access by default and reaches only the accounts you sign it into.



On the Grok Build side, 

Grok Build fixes context, streaming, and workspace workflows with more accurate token counts, immediate context bar updates, friendlier hook descriptions, faster worktree creation, improved MCP retries, and Linux file monitoring fixes — MCP server connections that fail transiently retry instead of staying unavailable.

 The MCP retry improvement converts transient MCP connection failures from permanent session-level tool unavailability into a recoverable runtime condition — the correct behaviour for any agent that is expected to maintain tool access across long-running sessions that may outlast the network conditions of session initiation.

---

### Perplexity: Computer in Email Consolidates; Bumblebee Deepens the MCP Trust Layer

Perplexity's most significant agentic UX development in this window remains the full-availability consolidation of **Computer in Email** as the ambient delegation on-ramp, now established long enough that its reliability trajectory and trust architecture are the appropriate lens for evaluation rather than its novelty.



Send or forward to computer@perplexity.ai to start a Computer session from email — Computer reads the thread context and replies only to the verified sender in the same thread using that sender's existing connectors, permissions, and Memory; enterprise reply-all support is coming soon; and the feature is available now to all Computer users.

 The interaction-design pattern this consolidates is *inbox-as-delegation surface*: the act of forwarding an email becomes the act of delegating a task, with no interface-switching, no connector reconfiguration, and no context re-establishment required. The thread provides the context; the agent inherits the sender's authorised tool set within it.



Search as Code optimisations are rolling out in Computer, routing search through a unified SDK-backed interface — two update batches raised execution reliability from 81.9% to 92.6%, with real-world workflows also showing higher user satisfaction at 8% lower per-task cost.

 The reliability trajectory from 81.9% to 92.6% is the invisible trust signal that determines whether Computer in Email becomes a workflow habit or remains an experiment: below 90%, users cannot confidently delegate and move on; above 92%, the mental model of "it will handle it" becomes justifiable.

The **Bumblebee MCP-config scanner** continues deepening Computer's trust surface at the tool-configuration layer. 

Perplexity has released Bumblebee as an open-source scanner for developer teams.

 Bumblebee scans the local MCP configuration files that define which external services AI assistants are permitted to connect to — and when a new threat surfaces, Perplexity Computer drafts a catalog entry, a human reviews and approves it, and Bumblebee then scans across developer machines to check for matches. The human-review-before-propagation step is the bounded-autonomy primitive that makes autonomous security tooling credible: the agent surfaces the threat signal, but a human validates the catalog entry before it propagates. This is the same design principle that governs every other trust advance in this window — agentic authority is maximised up to the point of irreversible consequence, and human approval is inserted precisely at that boundary.

---

## The Bigger Picture: Audit Trails, Ambient Messaging, and the Governance Maturity Layer

The 48 hours ending September 10, 2026 mark the moment when the agentic AI industry crosses a threshold from capability maturity to governance maturity — and the two advance simultaneously, not sequentially. Claude Fable 5.1's 45% cost reduction on highly agentic workloads and GPT-6 Astra's ScreenSpot Pro jump to 92.7% represent the capability front moving forward; Google Gemini's Notebook audit logs in the Admin console, Grok Bot's Action Recording and OpenTelemetry Export, Anthropic's policy-diagnostics in `/status`, and Perplexity's Bumblebee human-review-before-propagate workflow represent the governance front moving forward in parallel. The platforms that are winning enterprise trust this week are not winning it by shipping the most impressive autonomous capability — they are winning it by making their agents' actions inspectable after the fact, their access scoped at the point of configuration, and their trust boundaries legible to the humans who must ultimately answer for what their agents did. Microsoft's Excel `=COPILOT()` formula retirement is the clearest architectural statement of this principle: moving AI out of invisible, volatile cell computation and into an auditable side-pane workflow where every action is reviewable is not a capability regression — it is a governance upgrade. The unified Copilot app's mid-September desktop rollout, Grok Bot's zero-access-by-default architecture, and ChatGPT's default per-send approval gate on the Apple Messages plugin all make the same statement from different angles: the agentic era's next design challenge is not building agents that can do more, but building the audit infrastructure that makes it safe to let them.

---

## References

[1] Anthropic. (2026). *Introducing Claude Fable 5.1 and Claude Mythos 5.1*. [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)

[2] Releasebot. (2026). *Claude Code Updates by Anthropic — September 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] Clockedcode. (2026). *Claude Code Changelog: Every Release Explained in Plain English*. [https://clockedcode.com/blog/claude-code-changelog](https://clockedcode.com/blog/claude-code-changelog)

[4] MindStudio. (2026). *GPT-6 Astra's Computer Use Skills: What the Agentic Benchmarks Show*. [https://www.mindstudio.ai/blog/gpt-6-astra-computer-use-agentic](https://www.mindstudio.ai/blog/gpt-6-astra-computer-use-agentic)

[5] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[6] Releasebot. (2026). *Codex Updates by OpenAI — September 2026*. [https://releasebot.io/updates/openai/codex](https://releasebot.io/updates/openai/codex)

[7] Google Workspace Updates Blog. (2026). *Introducing comprehensive audit logs for Gemini Notebook in the Workspace Admin console*. [https://workspaceupdates.googleblog.com/2026/08/introducing-comprehensive-audit-logs-for-Gemini-Notebook-in-the-Workspace-Admin-console.html](https://workspaceupdates.googleblog.com/2026/08/introducing-comprehensive-audit-logs-for-Gemini-Notebook-in-the-Workspace-Admin-console.html)

[8] Google Workspace Updates Blog. (2026). *Custom instructions for Gemini in Workspace now available in more apps*. [https://workspaceupdates.googleblog.com/2026/09/custom-instructions-for-gemini-in-Workspace-now-available-in-more-apps.html](https://workspaceupdates.googleblog.com/2026/09/custom-instructions-for-gemini-in-Workspace-now-available-in-more-apps.html)

[9] Google Workspace Updates Blog. (2026). *Google Workspace Weekly Recap — September 4, 2026*. [https://workspaceupdates.googleblog.com/2026/09/weekly-recap-09-04-2026.html](https://workspaceupdates.googleblog.com/2026/09/weekly-recap-09-04-2026.html)

[10] Windows Central. (2026). *Microsoft begins unified Copilot app rollout*. [https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding)

[11] Microsoft Community Hub. (2026). *What's New in Microsoft Copilot — August 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960)

[12] Releasebot. (2026). *Microsoft Release Notes — September 2026*. [https://releasebot.io/updates/microsoft](https://releasebot.io/updates/microsoft)

[13] xAI. (2026). *Grok Bot for Enterprise*. [https://x.ai/news/grok-bot-for-enterprise](https://x.ai/news/grok-bot-for-enterprise)

[14] AI Success Lab. (2026). *Grok Bot Enterprise Audit Controls: Logs, Recording, Export*. [https://aisuccesslabjuliangoldie.com/blog/grok-bot-enterprise-audit-controls/](https://aisuccesslabjuliangoldie.com/blog/grok-bot-enterprise-audit-controls/)

[15] Releasebot. (2026). *Grok Build Updates by xAI — September 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Releasebot. (2026). *Perplexity Release Notes — August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[17] Perplexity Blog. (2026). *Computer now works in email*. [https://www.perplexity.ai/hub/blog/category/news](https://www.perplexity.ai/hub/blog/category/news)

[18] Just AI News. (2026). *Perplexity Releases Bumblebee As An Open Source Scanner For Dev Teams*. [https://justainews.com/category/companies/perplexity/](https://justainews.com/category/companies/perplexity/)