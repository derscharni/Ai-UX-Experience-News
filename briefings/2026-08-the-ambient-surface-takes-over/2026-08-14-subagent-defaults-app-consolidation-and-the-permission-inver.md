# UX Briefing: Subagent Defaults, App Consolidation, and the Permission Inversion

**August 14, 2026**

Good morning. The 48 hours ending August 14 are defined by three interlocking design bets about where the human-agent permission boundary should sit — and one platform consolidation that surgically removes the features that failed to find their place on either side of it. **Anthropic** simultaneously executes two of the most consequential Claude Code architecture changes of the year: auto mode goes live as the default permission mode for Pro, Max, and Team plans today, and a sweeping changelog ships default subagent forking, new per-session @ cross-session mentions, expanded worktree-based parallel development, runaway-loop caps, and a battery of permission-bypass security patches — together representing the fullest expression yet of Claude Code as a multi-agent orchestration platform rather than a single-session coding assistant. **Microsoft** executes the most significant Copilot surface consolidation since the product launched, beginning the rollout of a unified consumer-and-business Copilot app on August 13 while simultaneously confirming that Group Chats, AI-generated Podcasts, Copilot Labs, and consumer Deep Research are being retired as of August 18 — an admission, confirmed in an internal memo obtained by The Information, that the app must earn the right to exist in users' lives. **ChatGPT/OpenAI** completes its individual-user sync deprecation today, centralising all data access to admin-managed connectors in Enterprise and Edu workspaces, while the **GPT-Live** voice model adds file uploads and Project context to voice conversations — connecting spoken interaction to the full agentic workspace for the first time. And **Google** advances the Gemini Deep Research Agent in Enterprise platform preview with a mandatory async API pattern, while the **Gemini Enterprise Agent Platform** ships Agent Observability to preview — the instrumentation layer that makes multi-agent pipelines inspectable in production.

---

## At a Glance: August 14 Highlights

Today's releases collectively answer the question of what gets promoted, what gets deprecated, and what gets locked behind a classifier when an AI platform decides which of its interaction experiments have earned permanent status in the workflow stack.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Auto mode goes live as the default today; default subagent forking and @ cross-session mentions ship in the same changelog wave** — per-session caps on web searches and subagent spawns added; permission-bypass security patches close Bash and Unicode hiding vulnerabilities; /fork now creates a separate worktree for parallel development; background sessions auto-commit, push, and open draft PRs; MCP calls over 2 min auto-background. [1][2][3] |
| **ChatGPT** | **Individual-user sync connections disabled today in all Enterprise/Edu workspaces** — deletion of associated synced data begins; GPT-Live voice now supports file uploads and Projects, connecting spoken interaction to full agentic workspace context; Codex ships portable Agent Plugins and --approve-for-me CLI auto-approval flag; DALL·E GPT retirement set for August 30. [4][5][6] |
| **Google Gemini** | **Gemini Enterprise Agent Platform ships Agent Observability to preview** — comprehensive visibility into agent performance, behaviour, and MCP server health via tracing and key metrics; Gemini Deep Research Agent advances in Enterprise preview with mandatory async/background API execution pattern; Gemini in Classroom expands to all K-12 students under admin grant. [7][8][9] |
| **Microsoft Copilot** | **Unified Copilot app begins rollout August 13** — consumer and business apps merging into a single experience; Group Chats, Podcasts, Copilot Labs, and consumer Deep Research retiring August 18 with no full migration path; Researcher (Premium only) survives as the enterprise replacement for Deep Research; SharePoint Copilot ships live List-connected HTML dashboards and contextual page buttons. [10][11][12] |
| **Grok (xAI)** | **Grok 4.6 enters second day of real-world testing in Grok Build and Cursor** — autonomous 22-minute single-prompt project completions reported in the wild; Grok Build auto mode approves more common read-only git commands and harmless file appends; plan preview and question card navigation improvements; always-allow bash glob editing ships. [13][14][15] |
| **Perplexity** | **Personal Computer on Mac rolling out to all Pro subscribers** — local file editing, Comet browser use, and voice orchestration available on any Mac running macOS 15; Personal CFO expands to 30 linked accounts and 500 assets per account; Computer notifications now intelligent about when to surface approval-needed interrupts; MCP server one-click install available for Claude Code and Cursor. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Default Subagent Forking, the Permission-Bypass Patches, and Auto Mode Goes Live

Anthropic's August 14 changelog wave is the largest single architectural expansion of Claude Code's multi-agent surface since the product launched, and it arrives on the same day that auto mode becomes the default permission mode. 

Starting August 14, auto mode is the default permission mode for new sessions on Pro, Max, and Team plans.

If you set a default mode yourself, it stays in place unless you accept the one-time switch prompt, and a default your organisation manages doesn't change.

 The interaction-design consequence of pairing this with the subagent expansion is significant: agents running in auto mode can now fork and spawn parallel subagents without triggering per-step approval prompts for the majority of their tool calls, which means the human-oversight surface shifts decisively from the tool-call level to the session boundary.

The most consequential of the new subagent primitives is **default subagent forking**. 

Subagent forking is now on by default: a subagent_type: "fork" subagent inherits the full conversation and prompt cache, and non-teammate agent spawns in interactive sessions now run in the background by default; type @ in the prompt to mention another Claude session by name, and Claude then uses SendMessage to reach that session directly.

 The prompt-cache inheritance is the economic and UX detail that matters most here: previously, each fork rebuilt the full conversation history from scratch, making parallel subagents expensive enough to discourage in practice. 

A session you copy with /fork now makes its code changes in a worktree of its own instead of the original session's checkout; background sessions that changed code in a worktree now commit and push before finishing, open a draft pull request only when the task calls for one, and follow the git instructions in your CLAUDE.md — and the 200-subagent-per-session cap is removed, so long-running sessions no longer refuse new subagents.

 The removal of the subagent cap combined with automatic worktree isolation is the architectural choice that promotes Claude Code from a parallel-task tool to a genuinely concurrent development environment.

The trust-design events that deserve equal scrutiny are the permission-bypass security patches, which land in the same changelog. 

Anthropic fixed a Bash permission bypass where a crafted command could hide parts of itself from permission checks, and fixed permission prompts so commands padded with tabs or invisible Unicode can no longer hide part of the command from the approval dialog.

Anthropic also fixed workflow scripts being able to use dynamic import() to run code outside the workflow sandbox, and fixed a permission gap where an agent definition's bypassPermissions mode ignored the org bypass-permissions disable policy.

 These patches are the safety infrastructure that makes the auto mode default viable: if the classifier-as-gatekeeper paradigm is to hold, the permission surface it governs must be tamper-resistant. The fact that Unicode-hidden commands could previously bypass approval dialogs is a reminder that the approval dialog was not a reliable safety primitive even before auto mode made it less frequent — which is the most honest argument for moving the safety gate to the classifier layer. Additionally, 

MCP tool calls running longer than 2 minutes now move to the background automatically so the session stays usable, with the threshold configurable or disableable via CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS.

 This is the temporal UX fix that makes long-running MCP integrations usable without blocking the interactive session — the agent offloads the slow tool call rather than freezing the prompt.

The **Claude Tag** update shipping in the same window is the proactive-context design event worth noting for ambient AI practitioners. 

Claude adds smarter Slack collaboration with Claude Tag, using full channel context, memory, and standing instructions to decide when to jump in or stay quiet — it now responds more accurately and faster, with proactive replies available today at no extra cost.

Before, Claude only saw one message at a time, so it made decisions to act proactively based on what was in front of it, but not the wider context of what was around it; now, Claude uses context from across the channel, as well as its memory and the standing instructions you have given it, to determine when to contribute to the conversation.

 This is the shift from reactive @-mention to context-aware ambient contribution — the agent reads the room, not just the direct address.

---

### Microsoft Copilot: The Unified App, the Retirement Wave, and the Permission Audit

Microsoft's most consequential UX event in this 48-hour window is not a feature launch but a consolidation: the beginning of a unified Copilot app rollout that simultaneously confirms the retirement of four consumer features. 

Microsoft is beginning to roll out a new Copilot app that merges Copilot and Microsoft 365 Copilot under one experience — until now, Copilot and Microsoft 365 Copilot have been targeted at different users, but starting today those apps are being merged into one.

 The surface implication is a single app with account-switching between personal and work contexts, but the governance implication is more significant: 

work and personal experiences remain separated by design, and data does not flow between them.



The retirement events that accompany the launch are the most editorially significant design admissions Microsoft has made about the consumer AI experiment. 

According to Microsoft, consumers will lose access to Group Chats, AI-generated podcasts in Copilot, Copilot Labs experimental features, and Deep Research by August 18, 2026 — for paying professional users, Researcher will offer a replacement for the latter, at least.

 The design verdict on each retired feature is worth reading carefully. 

Group Chats, which allowed multiple users to collaborate within Copilot, will be completely wiped on August 18, 2026, along with all shared messages and images; Microsoft recommends users manually copy any content they want to preserve into separate documents, as there is no automated migration path.

 The complete data wipe — not a migration, a deletion — is the harshest possible signal about a feature's status. For **consumer Deep Research**, the treatment is more nuanced: 

Microsoft 365 Premium subscribers can continue creating detailed reports and analyses using Researcher in Copilot, and existing saved research content will remain available — but if you are an individual using Copilot but not paying, or if you have any subscription other than Microsoft 365 Premium, this feature is going away.

 This gates the research agent behind the premium tier, migrating it from a consumer experiment to an enterprise product — a governance decision that mirrors the trust-and-accountability posture of the wider August Copilot wave.



In July 2026, The Information reported that Microsoft EVP Jacob Andreou, who oversees Copilot, wrote in an internal memo that the app needed to earn "the right to exist" in customers' lives, which meant moving on from features that didn't deliver value.

 The UX implication for practitioners is that the surviving surface — chat, image creation, file uploads, Office artifact creation, and the M365 Researcher — is the minimum viable agentic footprint Microsoft believes users will pay for, and the design team is now free to instrument and improve that surface without maintaining four additional interaction paradigms alongside it. On the SharePoint side, 

SharePoint can now generate HTML dashboards and apps that stay connected to the underlying list data — including project status dashboards that turn a list of projects into a live executive view showing what's on track, at risk, or blocked, with filters for owner, priority, due date, or status.

 This is the live-grounding primitive applied to the SharePoint surface: the dashboard does not go stale because it reads from the list on demand rather than from a snapshot at generation time.

---

### ChatGPT / OpenAI: Sync Centralisation, Voice Context Expansion, and the --approve-for-me Flag

OpenAI's most governance-significant event today is the completion of its individual-sync deprecation. 

On August 14, existing individual-user sync connections are being disabled, and deletion of associated synced data begins — administrator-managed sync is unaffected.

 The interaction-design consequence of this centralisation is that the workspace AI's data access is now fully defined at the admin layer — individual workers can no longer extend the assistant's memory by connecting their personal cloud storage. This is the same admin-layer data-governance posture that Microsoft has operated under from the start, and its arrival at OpenAI completes a convergence: enterprise AI assistants across both major productivity stacks now require IT authorisation to access organisational data, not just individual user consent.

The feature launch that matters most for understanding where OpenAI is expanding the agentic footprint is **GPT-Live with file uploads and Projects**. 

GPT-Live in ChatGPT Voice now supports file uploads and Projects — you can now upload files in a voice conversation and analyse its contents or ask questions.

You can also use voice in Projects, referencing recent project chats, sources, and project instructions.

 The UX shift this represents is voice as a full agentic modality rather than a conversational shortcut: the spoken session now has access to the same file and project context that structured chat has always had, which means a user can hand off a document analysis task in voice and have it execute inside an existing project workspace. This is the interaction pattern that makes voice a serious agentic entry point rather than a convenience mode. 

OpenAI says GPT-Live handles the live voice interaction while deeper work can be passed to another model — at launch, GPT-Live uses GPT-5.5 in the background; for questions that require web search, deeper reasoning, or more complex work, GPT-Live can delegate to OpenAI's latest frontier model behind the scenes, and brings the result back into the conversation when it's ready.



On the Codex CLI side, 

Codex introduces portable Agent Plugins, richer conversation organisation, and smarter approval workflows, while adding MCP 2026-07-28 support, Amazon Bedrock caching, and cleaner imports, tightening security, and expanding bug fixes across platforms.

 The most interaction-design-significant addition is the **--approve-for-me flag**: 

Codex enables automatically reviewed approvals with the new --approve-for-me CLI flag.

 This is Codex's version of the same classifier-default bet that Claude Code's auto mode represents — a command-line primitive that removes the per-approval prompt from the developer's workflow and routes it to an automated review layer.

---

### Google Gemini: Agent Observability Preview and the Async Research Agent Pattern

Google's most trust-design-significant event in this window is the arrival of **Agent Observability** in Gemini Enterprise Agent Platform preview. 

Agent Observability in Gemini Enterprise Agent Platform provides comprehensive visibility into the performance, behaviour, and health of deployed agents and MCP servers — by monitoring key metrics, tracing execution paths, and observing multi-agent systems as a whole, operators can diagnose issues, optimise resource consumption, and improve the reliability of their agents.

 The UX significance of Agent Observability is that it is the enterprise accountability primitive that makes multi-agent Gemini deployments governable in production: without execution traces and health metrics, a multi-agent pipeline is a black box whose failures surface only at the output layer. Tracing makes failure visible at the step level.

The **Gemini Deep Research Agent** on the Enterprise Agent Platform is the async interaction pattern that warrants close attention for temporal UX practitioners. 

The Gemini Deep Research Agent is a managed AI agent that plans, executes, and synthesises complex, multi-step research workflows across the public web and private enterprise data to generate comprehensive, cited reports.

 The mandatory execution model is what distinguishes it architecturally: 

you must run the Gemini Deep Research Agent asynchronously — you must use background execution and streaming mode.

The API returns a partial Interaction object immediately; you can use the id property to retrieve an interaction for polling; the interaction state will transition from in_progress to completed or failed.

 This poll-and-retrieve pattern is the temporal UX contract that long-running research agents require — the developer gets immediate confirmation of task acceptance, the task executes in background, and the UI polls for completion rather than blocking. It is the async design primitive that every agentic research workflow needs but few have shipped as a first-class API constraint. 

Memory profiles in Memory Bank have also reached general availability — memory profiles allow generation of structured profiles with static schemas populated and updated using LLMs, and by defining a fixed schema, agents have immediate, low-latency access to evolving information without expensive search operations during a session.

 This is the structured-memory primitive that allows enterprise agents to maintain fast access to evolving organisational context without paying the latency cost of a retrieval call at every turn.

---

### Grok (xAI / SpaceXAI): Grok 4.6 in Production and the Auto-Approval Expansion

SpaceXAI's UX story in this window is the translation of Grok 4.6's August 12 launch into real-world agentic performance data. 

Real-world testing is reinforcing Grok 4.6's capabilities beyond benchmark numbers — tech creator @DirtyTesLa shared a demonstration where Grok 4.6, working autonomously from a single prompt for 22 minutes, produced a project complete with custom shaders, a minimap, and a time-change feature.

 The 22-minute single-prompt autonomous execution is the agentic UX data point that matters most: it validates that the long-running agent architecture Grok 4.6 was designed for is delivering end-to-end task completion in the wild, not just in controlled benchmarks. 

Rather than positioning the release strictly around raw intelligence scores, SpaceXAI designed Grok 4.6 to solve operational drift in long-running AI workloads.



The Grok Build changelog running alongside the 4.6 launch continues to refine the agentic developer experience. 

Grok Build ships a smoother developer workflow with more flexible bash allow-lists, faster auto mode approvals, better plan previews and question card navigation, and fixes for resume, auth, task logs, plan viewing, and startup performance — always-allow for bash commands lets you edit a free-form glob pattern instead of only word-prefix scopes, and auto mode auto-approves more common read-only git commands and harmless file appends.

 The expansion of auto-approval to cover read-only git commands and harmless file appends is the interaction-design counterpart to Claude Code's classifier approach: rather than routing every command through a classifier, Grok Build expands the static allow-list for the subset of operations that are provably safe by category. Both approaches reduce approval-prompt fatigue; they distribute the safety work differently — one at inference time, one at configuration time. 

According to OrcaRouter, Grok 4.7 — a larger model — is expected within weeks of the 4.6 release.

 For UX practitioners building on Grok Build, the cadence signal matters: the agentic backbone is actively changing beneath the interaction layer, which makes stable interface contracts on top of it the design constraint worth investing in now.

---

### Perplexity: Personal Computer Rolls to All Pro, Intelligent Notifications, and the Finance Context Expansion

Perplexity's most UX-significant event in this window is the completion of **Personal Computer on Mac's** rollout to all Pro subscribers, representing the broadest distribution yet of a local-desktop agentic agent from any major AI platform. 

Personal Computer is now available on Mac for everyone — Personal Computer securely connects local files, apps, and Comet browser to Computer so Computer can work with the context that already lives on the local desktop; users stay in control for what Personal Computer can and cannot access; Personal Computer works on any Mac: desktop, laptop, or Mac Mini.

 The trust-design architecture that makes local file access viable for a broad rollout is the explicit consent model: the user grants access per-source rather than granting a blanket desktop permission, which keeps the permission surface narrow enough to be meaningful.

The notification design update that ships alongside is the interaction primitive that distinguishes a background agent from a background process. 

Computer is now smarter about sending notifications, including completed tasks and moments where Computer needs user input — this helps long-running work continue in the background without losing the user's attention when approval, auth, or clarification is needed; Computer decides intelligently when and where to send notifications.

 This is the temporal UX primitive that makes long-running background tasks feel supervised rather than abandoned: the agent does not notify on every step, but it does notify when a human decision is required or a task completes. The UX inversion of always-on notification to on-demand interruption is the attention-management design that makes ambient AI agents acceptable for professional use.

The **Personal CFO** expansion in the same wave extends the structured finance context significantly: 

Personal CFO now supports more personal finance context — users can connect up to 30 accounts, up from 5, and Computer now fetches up to 500 assets per account, up from 200.

 The jump from 5 to 30 accounts is the threshold that transforms Personal CFO from a demonstration of agentic finance capability into a tool that can model a real household or small-business financial picture in full. 

The Perplexity MCP Server now supports one-click installation for Cursor, VS Code, Claude Desktop, and Claude Code, providing four tools: perplexity_search, perplexity_ask, perplexity_research, and perplexity_reason.

 One-click MCP installation lowers the integration friction that has historically made Perplexity's search infrastructure a back-end capability rather than a front-line tool in developer agentic stacks — making Perplexity's cited research pipeline accessible as a first-class tool inside Claude Code and Cursor sessions.

---

## The Bigger Picture: Subagent Defaults, App Consolidation, and the Permission Inversion

The 48 hours ending August 14, 2026 are defined by a permission renegotiation that is happening simultaneously across every major AI platform — and by a consolidation event that clarifies which interaction experiments survived long enough to join the new permission architecture. Anthropic's auto-mode default and default subagent forking, arriving together, represent the most complete expression of the classifier-as-gatekeeper paradigm: the human is removed from the tool-call approval chain, the session can now fork parallel agents that inherit full conversation context and commit their own code changes in isolated worktrees, and the safety layer moves from the UI to the model. The permission-bypass patches that ship in the same changelog are not incidental — they are the precondition that makes the classifier paradigm credible, because a permission dialog that can be bypassed by invisible Unicode is not a safety gate; it is a UI ritual. OpenAI's Codex --approve-for-me flag and Grok Build's expanded auto-approve allow-list are the same bet expressed in different implementation philosophies: both ask whether per-step approval prompts have ever been the right trust primitive, and both answer no. Microsoft's unified Copilot app consolidation answers a different version of the same question from the consumer direction: which interaction patterns earned the right to survive the permission renegotiation, and which ones didn't? Group Chats, Podcasts, Copilot Labs, and consumer Deep Research — all experiments in what a general-purpose AI surface could do — are being retired, while Researcher, Office artifact creation, and admin-managed data sync survive. The survivors are all features where the governance contract is clear, the output is auditable, and the human remains in a defined review role. Google's Agent Observability preview and the mandatory async pattern of the Deep Research Agent answer the same question from the infrastructure layer: if agents are going to run in background and return results asynchronously, the platform must provide the instrumentation to make their execution paths inspectable and their failures diagnosable before they reach the user. Perplexity's intelligent notification system, which fires only when approval is needed or a task completes, is the ambient-agent design pattern that all of these platforms are converging toward — not agents that pause every step to ask permission, but agents that run to completion and surface the human only at the boundaries where human judgment is genuinely required.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — August 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] Gradually.ai. (2026). *Claude Code Changelog (August 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[3] Releasebot. (2026). *Anthropic Release Notes — August 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[4] OpenAI. (2026). *Release Notes — OpenAI*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[5] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[6] Releasebot. (2026). *ChatGPT Updates by OpenAI — August 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] Google Cloud Documentation. (2026). *Gemini Enterprise Agent Platform release notes*. [https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes)

[8] Google AI for Developers. (2026). *Gemini Deep Research agent*. [https://ai.google.dev/gemini-api/docs/deep-research](https://ai.google.dev/gemini-api/docs/deep-research)

[9] Google Cloud Documentation. (2026). *Use the Gemini Deep Research Agent*. [https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/use-deep-research](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/use-deep-research)

[10] TechCrunch. (2026). *Microsoft kills off unsuccessful AI features while merging its separate Copilot apps*. [https://techcrunch.com/2026/08/13/microsoft-kills-off-unsuccessful-ai-features-while-merging-its-separate-copilot-apps/](https://techcrunch.com/2026/08/13/microsoft-kills-off-unsuccessful-ai-features-while-merging-its-separate-copilot-apps/)

[11] Windows Central. (2026). *Microsoft begins unified Copilot app rollout*. [https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding)

[12] Microsoft Community Hub. (2026). *What's New in Copilot in SharePoint: August 2026*. [https://techcommunity.microsoft.com/blog/spblog/whats-new-in-copilot-in-sharepoint-august-2026/4535421](https://techcommunity.microsoft.com/blog/spblog/whats-new-in-copilot-in-sharepoint-august-2026/4535421)

[13] Basenor. (2026). *xAI Launches Grok 4.6*. [https://www.basenor.com/blogs/news/xai-launches-grok-4-6-1753-elo-half-the-price-of-rival-frontier-models](https://www.basenor.com/blogs/news/xai-launches-grok-4-6-1753-elo-half-the-price-of-rival-frontier-models)

[14] American Bazaar Online. (2026). *SpaceXAI debuts Grok 4.6 model to challenge rival frontier systems*. [https://americanbazaaronline.com/2026/08/13/spacexai-debuts-grok-4-6-model-to-challenge-rival-frontier-systems-486355/](https://americanbazaaronline.com/2026/08/13/spacexai-debuts-grok-4-6-model-to-challenge-rival-frontier-systems-486355/)

[15] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Perplexity. (2026). *Personal Computer on Mac for all — May 11, 2026 (extended rollout to Pro)*. [https://www.perplexity.ai/changelog/personal-computer-for-all-users-on-mac](https://www.perplexity.ai/changelog/personal-computer-for-all-users-on-mac)

[17] Releasebot. (2026). *Perplexity Release Notes — July/August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[18] Releases.sh. (2026). *Perplexity Release Notes & Changelog — August 2026*. [https://releases.sh/perplexity](https://releases.sh/perplexity)