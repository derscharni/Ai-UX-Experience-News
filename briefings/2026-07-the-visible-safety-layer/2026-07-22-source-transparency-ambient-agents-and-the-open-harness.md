# UX Briefing: Source Transparency, Ambient Agents, and the Open Harness

**July 22, 2026**

Good morning. The 48 hours ending July 22 are defined by a simultaneous push on two fronts: making agentic work more transparent to the users who authorise it, and expanding the surfaces where ambient agents operate without being asked. **Claude Code (Anthropic)** ships a dense cluster of filesystem isolation and subagent-boundary fixes — including a new `sandbox.filesystem.disabled` setting and critical repairs to worktree-isolated subagents that were escaping their intended git boundaries — while **Claude's** consumer memory architecture graduates from daily summaries to individual categorised entries that Claude reads and updates in real time. **ChatGPT/OpenAI** continues consolidating the July 9 **ChatGPT Work** and **Sites** launch across all plans, with the desktop's unified Chat/Work layout now live on macOS and Windows for every tier, and the **Atlas browser** closure ticking toward its August 9 deadline. **Grok (xAI/SpaceXAI)** makes the most consequential trust-design move of the window: open-sourcing the entire **Grok Build** harness on GitHub — a direct response to a researcher-documented privacy incident — replacing the company's word about how the agent dispatches tool calls with publicly inspectable Rust source code. **Microsoft Copilot** completes the rollout of its **New Copilot** redesigned interface as the default experience for all users as of July 15, including the new **Tasks tab** for monitoring long-running agent activity, while **Perplexity** deepens **Personal Computer** on Mac with voice orchestration and local Comet browsing, and confirms **Claude Opus 4.7** as the new default orchestrator for Computer. Today is also the day of **Samsung Galaxy Unpacked**, where the company's CEO has framed the Galaxy AI transition into the "agentic age" as the launch's headline theme.

---

## At a Glance: July 22 Highlights

The releases this window converge on a shared inflection point: as ambient and background agents proliferate across every surface users occupy, the industry is being forced — by researchers, regulators, and its own users — to make the agent's internals legible, not just its outputs.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code** ships filesystem isolation controls, critical worktree subagent boundary fixes, and a live elapsed-time counter for long-running tools; consumer **memory** upgrades from daily summaries to real-time individual categorised entries; **HIPAA self-serve configuration** arrives for Enterprise and API orgs. [1][2][3] |
| **ChatGPT** | **ChatGPT Work** desktop Chat/Work split and unified Recents fully live across all plans on macOS/Windows; **Sites** interactive web-app publishing in public beta continues rollout (EEA/UK/Switzerland excluded); **Atlas browser** deprecation countdown to August 9 continues. [4][5][6] |
| **Google Gemini** | **Gemini in Google Search** now powers every global query by default after July 10 full rollout; **Gemini Enterprise Agent Studio** patches an SSRF security vulnerability in auto-generated web app proxies; **Gemini Spark** MCP and real-time topic monitoring continue expanding. [7][8][9] |
| **Microsoft Copilot** | **New Copilot** redesigned app is now the forced-default experience for all users as of July 15, with **Tasks tab**, simplified navigation, and **Work IQ** toggle fully deployed; **Anthropic Claude** model choice now available inside Copilot Word for editing; **Agent Store** governed publishing flow live. [10][11][12] |
| **Grok (xAI)** | **Grok Build goes open source** on July 15 — full Rust harness (agent loop, tools, terminal UI, extension system) published on GitHub under Apache 2.0 in direct response to a repository-upload privacy incident; usage limits reset for all users; **Tesla Summer Update** brings Grok to all of Europe via OTA. [13][14][15] |
| **Perplexity** | **Personal Computer** on Mac deepens with voice orchestration, local file editing, and local Comet browsing; **Claude Opus 4.7** replaces prior model as default Computer orchestrator; **hybrid local-server inference** for Windows in active rollout. [16][17][18] |
| **Samsung** | **Galaxy Unpacked July 22** — CEO TM Roh frames the Z Fold 8 / Z Flip 8 / AI glasses launch explicitly around the shift from answering-AI to acting-AI; **Samsung Health Assistant** beta announced, pulling data across Galaxy phone, watch, and ring. [19][20] |

---

## Product Highlights

### Claude / Anthropic: Subagent Boundary Enforcement, Memory Granularity, and the Isolation Layer

Anthropic's most consequential interaction-design work in this window arrives in the trust-and-safety register rather than the capability register: a systematic tightening of the boundaries between Claude Code subagents and the shared environment they operate within, paired with a consumer-facing memory architecture upgrade that replaces blunt periodic summaries with a fine-grained, always-current entry system.



**Claude Code** ships a broad stability and workflow update with new filesystem isolation controls, faster long-session performance, stronger session resume and background agent handling, and numerous fixes for permissions, worktrees, UI, shell parsing, telemetry, and VS Code text rendering — including a new `sandbox.filesystem.disabled` setting that lets teams skip filesystem isolation while retaining network egress control.

 The most significant trust-design fixes in this release target subagent boundary violations: 

resumed background agent sessions were reverting to the default agent — the agent's prompt and tool restrictions are now restored correctly — and worktree-isolated subagents were redirecting git operations into the shared checkout via `git -C`, `--git-dir`, or `GIT_DIR/GIT_WORK_TREE`, a path by which a scoped subagent could escape its intended isolation and mutate the main repository.

 These are not cosmetic fixes. The worktree escape bug represents exactly the class of subagent boundary failure that makes parallel multi-agent architectures difficult to deploy safely: the promise that a worktree-isolated subagent operates on its own copy of the repository was not enforced at the git invocation layer, meaning the agent's written scope did not match its actual file access. 

Claude Code also adds a live elapsed-time counter to the collapsed tool summary line, so long-running tool calls visibly tick instead of looking stuck.

 This is the temporal transparency primitive that directly addresses one of the most common user complaints about agentic coding sessions: the ambiguity between an agent that is thinking and an agent that is hung.

On the consumer side, 

Claude updates memory to work as a set of individual, categorised entries that Claude reads and updates during conversations, replacing the previous daily memory summary.

 The shift from batch-refreshed summaries to per-conversation, fine-grained entry management is the memory UX change with the most direct impact on how Claude feels to use over time: rather than a weekly digest of what the model inferred about you, users now interact with a living, inspectable set of discrete facts that can be corrected, extended, or deleted entry by entry. 

Claude also adds self-serve HIPAA configuration for Enterprise and API orgs with BAA review, guide download, and one-step enablement — eligible admins can review the Business Associate Agreement, download the implementation guide, and enable the HIPAA configuration in a single flow.

 The one-flow self-serve HIPAA enablement collapses what was previously a multi-step procurement process into a compliance action that an admin can complete without a Google or Microsoft account relationship — the kind of friction reduction that meaningfully expands the set of regulated organisations who can trial the product before committing.

---

### ChatGPT / OpenAI: Sites, Work Consolidation, and the Atlas Countdown

OpenAI's most interaction-design-significant work in this window is not a new launch but the full-surface consolidation of **ChatGPT Work** and **Sites** into the stable everyday product — the moment a major launch stops being a feature announcement and becomes the default environment every paid user operates in.



ChatGPT updates its desktop app with a clearer Chat and Work layout, unified Recents, Projects in the app, and cloud-synced Work conversations across web, mobile, and desktop for smoother continuity — now live for all plans on macOS and Windows.

 The practical UX implication of this consolidation becoming universal is that the Chat/Work split is no longer an opt-in architecture for power users: it is the default mental model every ChatGPT desktop user now operates with. 

Cloud Work conversations sync across web, mobile, and desktop so users can start on one surface and continue on another; local conversations stay on the computer.

 This sync boundary — Work follows the user across devices, local conversations stay private — is the trust-design decision that most directly shapes what users feel comfortable putting into Work mode versus Chat mode.



ChatGPT Sites lets users describe a web app in plain language, generates the code, and immediately hosts it at a shareable URL — all without touching a server, database, or deployment pipeline.

Sites is the successor to the Canvas approach for building web things in ChatGPT: Canvas gave users code in a side panel that they had to host themselves; Sites generates the code, hosts it, versions it, and serves it at a real URL with access controls and optional storage attached.

 This is the generative-UI-to-published-surface pipeline closing its last gap: the friction that remained between generating an app in ChatGPT and sharing it with someone else — environment setup, deployment, hosting — is now eliminated. 

Atlas is being deprecated as browser-based agentic capabilities are integrated into ChatGPT and Codex, with shutdown scheduled for August 9, 2026; Atlas browser data including bookmarks, open tabs, and browser history will not transfer automatically.

 The data-non-transfer policy is the trust-design detail that deserves more attention than it typically receives in coverage of product sunsets: users who have built browsing workflows in Atlas have a hard data cliff rather than a migration path, reinforcing the practical argument for keeping agentic browser state in the main Work product rather than a satellite tool.

---

### Google Gemini: The Default Search Shift, Agent Studio Security, and the Spark Expansion

Google's most structurally significant UX change in this window is not a new feature but a completed rollout: the full replacement of the traditional ranked-link search interface with a Gemini-generated prose response as the default experience for every global user.



Google confirmed on July 10 that Gemini 3.5 Flash now powers every query — not merely the opt-in conversational tab called AI Mode, but all searches across Google's surface, globally.

When you search today, Gemini 3.5 Flash generates a prose answer synthesised from multiple web sources; those sources appear as inline citations within the prose — the way footnotes appear in an essay — rather than as a ranked list below your query.

 The interaction-model implications of this shift are profound: the fundamental UX of web search, unchanged since 1998, is now the AI response surface — and citation inline with prose replaces the ranked-list as the primary trust signal. The mental model users have built over two-plus decades of scanning blue links no longer maps to the primary way Google surfaces information. This is the ambient-agent transition arriving at planetary scale and at the most-used interface in human history.

On the developer-platform trust side, 

the Gemini Enterprise Agent Platform fixes a Server-Side Request Forgery vulnerability in the auto-generated `/api-proxy` backend endpoint for web applications created before July 1, 2026, using Agent Studio; the updated backend code includes strict domain allowlist validation, ensuring destination hostnames for the `/api-proxy` endpoint are limited to allowed Google Cloud domains.

 The significance of this for agentic UX governance is direct: every AI product that lets users generate deployable web apps or agents creates a new attack surface at the auto-generated proxy layer — and the existence of this patch validates that Agent Studio's "describe-to-deploy" workflow required explicit security hardening before being trusted in production environments. Teams who deployed Agent Studio web apps before July 1 need to regenerate and redeploy; the patch is not retroactive.

---

### Microsoft Copilot: The New UX Goes Forced-Default, Claude in Word, and the Tasks Tab

Microsoft's most consequential UX event in this window is the completion of a rollout that has been building since May: 

in July, the New Copilot experience became available by default for all users, and the opt-in toggle was removed.

 This is the forced-default moment that transforms the June opt-in redesign into the permanent product surface every Microsoft 365 Copilot user encounters.



The update introduces a redesigned layout with revised menus and navigation; frequently used features are reorganised, and a new Tasks tab allows users to monitor activities in progress; Copilot chat conversations also appear in an updated format, with responses, references, and suggested actions presented differently, and updated labels that distinguish agent interactions from standard Copilot chats.

 The **Tasks tab** is the temporal UX primitive worth examining most carefully: 

it opens a consolidated view of long-running Copilot activity — scheduled chats and agent activity — so autonomous Copilot tasks are easy to track.

 Before this tab existed, a user who had delegated a long-running Cowork task had no single surface to return to in order to check its status without hunting through conversation history. The Tasks tab makes ambient agent activity legible at the navigation level, not just the conversation level — a structural difference in how users understand what the agent is doing on their behalf.



Model choice is now available in Copilot in Word, giving users the option to choose Anthropic models when editing documents with Copilot.

 The arrival of Anthropic Claude as a selectable model inside a Microsoft 365 application is the enterprise trust-design move with the most long-term significance: it decouples the Copilot interaction layer from a single model provider and gives users the first documented point of model-level choice inside a productivity workspace they already trust. 

The governed Agent Store publishing flow — requiring admin review and approval in Microsoft 365 Admin Center before custom agents reach the "Built by your org" section — also remains actively rolling out.

 Together, the Tasks tab (visibility over running agents), model choice (agency over which AI executes), and governed Agent Store (oversight over what agents are available) constitute a coherent three-layer governance stack that enterprise IT teams have been requesting since Copilot agents were first made available to end users.

---

### Grok (xAI/SpaceXAI): Open Source as Trust Repair and the European Ambient Expansion

xAI's most interaction-design-significant move in this window is also its most unusual: the open-sourcing of **Grok Build** — not as a feature launch but as a trust-repair response to a documented privacy incident, completing a 72-hour arc from researcher disclosure to full source publication.



Grok Build went open source on July 15, 2026 — roughly 72 hours after an AI-safety researcher published wire-level evidence that the CLI had been silently uploading complete Git repositories to a SpaceXAI-controlled cloud bucket.

The source is now available on GitHub; publishing the code is described as the most direct way to build toward a robust and reliable harness — users can read the source to see exactly how it works, from context assembly to tool-call dispatch, and the open source makes the harness easier to explore and extend for skills, plugins, hooks, MCP servers, and subagents.

 The trust-design implication of this move is significant: it establishes a new precedent for how AI agent tool providers can respond to privacy incidents — not with a statement about ZDR policy compliance but with source inspection as the transparency mechanism itself. 

The company published the entire Rust harness under Apache 2.0, covering the agent loop, the tool implementations, the terminal UI, and the extension system — 844,530 lines of Rust by public count.

 However, 

the repository does not accept external pull requests or unsolicited patches; SpaceXAI develops the software internally, and the public tree is published for source transparency and local builds.

 This distinction matters for how the open-sourcing should be understood from a governance perspective: it is *inspection transparency*, not *community governance* — users can read and audit how the agent works, but they cannot commit fixes or improvements, meaning the trust model is "you can verify" rather than "you can contribute."

On the ambient-expansion front, 

Tesla has confirmed that Grok is rolling out across all of Europe as part of the 2026 Summer Update; prior to this update, Grok was unavailable in many European countries, and the Summer Update marks the first time the xAI assistant becomes broadly accessible to Tesla owners continent-wide via OTA update.

 The in-vehicle Grok deployment is the ambient-agent surface change that most directly challenges existing UX assumptions: unlike every other Grok surface, in-car deployment means the agent operates in a context where the user's hands and attention are divided — a fundamentally different interaction register than a desktop or phone session.

---

### Perplexity: Personal Computer Deepens, Orchestrator Upgrade, and the Local-Cloud Routing Layer

Perplexity's most interaction-design-significant work in this window is the continued deepening of **Personal Computer** on Mac — moving it from a capable local agent into a fully integrated ambient workspace that combines on-device file access, local browser sessions, and voice-driven orchestration in a single always-on surface.



Personal Computer is now available on Mac inside Perplexity's upgraded desktop app; it expands the capabilities of Computer to include local file editing, local computer use, local browsing with Comet, voice orchestration, and more.

 The addition of voice orchestration to Personal Computer is the interaction-mode change with the most significant practical implication: it allows users to direct a long-running local agent task without switching context to a keyboard — matching the hands-occupied, ambient-task interaction pattern that Copilot Vision and Gemini in Chrome are targeting simultaneously across different surfaces. 

The hybrid local-server inference system — announced at Computex and now in active rollout for Windows — automatically routes AI tasks between on-device and cloud-based frontier models; a compact local model acts as the router, classifying each subtask by data sensitivity and compute requirements, so sensitive data like financial records and health files stays on-device while compute-heavy tasks go to frontier cloud models — no manual configuration required.

 The no-configuration-required routing model is the trust-design primitive that makes the hybrid architecture usable rather than merely available: asking users to classify their own data sensitivity before each task is itself a friction point that most users would abandon; routing it automatically based on classification removes the decision from the human delegation path entirely.



Claude Opus 4.7 is now the default orchestrator model for Computer, offering higher-quality reasoning, writing, and coding tasks; users can now choose between Claude Opus 4.7, GPT-5.4, and Claude Sonnet 4.6 as the main orchestrator.

 This multi-model orchestrator selection is the most forward-looking interaction pattern in Perplexity's current product surface: rather than locking users into one model for all agentic work, Computer exposes orchestrator choice at the task level — establishing the premise that different classes of multi-step work benefit from different reasoning architectures, and that users should be able to act on that preference without rebuilding their workflow.

---

### Samsung: Galaxy Unpacked and the Agentic Hardware Thesis

Samsung's July 22 Galaxy Unpacked event is the hardware event most directly shaped by agentic AI UX assumptions, and it merits coverage for the interaction-design thesis it makes explicit even before product details land.



Samsung CEO TM Roh has revealed that the company is shifting Galaxy AI into the "agentic age," where the software will take proactive actions on behalf of users rather than just answering questions; ahead of the July 22 Galaxy Unpacked event, Roh explained that this transition requires AI to deeply understand user behaviour by pulling data from an interconnected ecosystem of phones, smartwatches, and home appliances.

Roh argued that as AI takes on more active background tasks, device shapes and sizes matter immensely — thinner, lighter foldables with larger flexible screens give users a much bigger physical canvas to multitask alongside running background agents, while upcoming categories like smart glasses will open up entirely new ways to interact with digital assistants.

 This is the hardware-form-factor argument for agentic UX: if background agents are running tasks while the user is doing something else, the user needs a larger, more capable secondary surface to monitor and intervene — which is the foldable value proposition reframed entirely around agentic oversight rather than media consumption. 

Samsung is also rolling out a new AI-powered Samsung Health Assistant that acts as a virtual health companion, pulling in data from the user's Galaxy smartphone, smartwatch, or smart ring.

 The cross-device Health Assistant is the multi-sensor ambient agent pattern applied to a high-stakes personal domain — and 

the updates will initially launch as a beta test next month and require users to opt in

, a default-conservative trust-design decision that is notable given the sensitivity of health data and the cross-device data scope the agent requires.

---

## The Bigger Picture: Source Transparency, Ambient Agents, and the Open Harness

The 48 hours ending July 22, 2026 reveal a design tension that is becoming the defining challenge of the agentic era's second year: the same week that agents expand to every surface a user occupies — in-car via Tesla's OTA, in-browser via Chrome, in-glasses via Samsung Galaxy, in-ear via voice orchestration in Personal Computer — the industry is being forced to make those agents more inspectable, not less. Grok Build's open-source response to a privacy incident is the starkest expression of this tension: source transparency as the only trust mechanism that survives a researcher with a packet sniffer. The principle it establishes — that for an agent running in your local environment with access to your git repositories, "trust us" is not sufficient and source inspection is the only credible alternative — is one the rest of the industry will need to reckon with as Claude Code subagents, Perplexity Personal Computer, and Microsoft Cowork all expand into similar local-access, file-touching, always-on territory. Anthropic's worktree subagent boundary fixes this window make the same argument from the other direction: even when the scope of an agent's access is declared in a configuration file, that declaration must be enforced at every layer of the tool-call stack, not just at the top. Microsoft's forced-default New Copilot rollout — with its Tasks tab surfacing long-running agent activity as a first-class navigation destination — and Samsung's explicit framing of foldable hardware as the physical canvas for agentic oversight make the same architectural bet: as agents proliferate across surfaces, users need dedicated legibility interfaces to understand what is running, what it has done, and when to intervene. The UX design challenge of late July 2026 is no longer how to make agents more capable — it is how to make the expanding surface area of ambient agent activity comprehensible to the humans who are, nominally, still in charge of it.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] Releasebot. (2026). *Claude Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[3] Gradually AI. (2026). *Claude Code Changelog (July 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[4] OpenAI. (2026). *Release Notes — OpenAI Products*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[5] OpenAI Help Center. (2026). *ChatGPT Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[6] Releases.sh. (2026). *Release Notes — OpenAI — releases.sh*. [https://releases.sh/openai/chatgpt-release-notes](https://releases.sh/openai/chatgpt-release-notes)

[7] TechTimes. (2026). *Google Fully Replaced Search With AI*. [https://www.techtimes.com/articles/320298/20260713/google-replaced-its-default-search-ai-how-get-blue-links-back.htm](https://www.techtimes.com/articles/320298/20260713/google-replaced-its-default-search-ai-how-get-blue-links-back.htm)

[8] Releasebot. (2026). *Google Release Notes — July 2026*. [https://releasebot.io/updates/google](https://releasebot.io/updates/google)

[9] Releasebot. (2026). *Gemini Updates by Google — July 2026*. [https://releasebot.io/updates/google/gemini](https://releasebot.io/updates/google/gemini)

[10] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[11] M365 Admin. (2026). *Microsoft 365 Copilot app: Simplified, chat-centered experience*. [https://m365admin.handsontek.net/microsoft-365-copilot-app-simplified-chat-centered-experience/](https://m365admin.handsontek.net/microsoft-365-copilot-app-simplified-chat-centered-experience/)

[12] Microsoft Community Hub. (2026). *What's New in Microsoft 365 Copilot — June 2026*. [https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-365-copilot--june-2026/4529572](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-365-copilot--june-2026/4529572)

[13] SpaceXAI. (2026). *Grok Build is Now Open Source*. [https://x.ai/news/grok-build-open-source](https://x.ai/news/grok-build-open-source)

[14] Digital Applied. (2026). *Grok Build Goes Open Source: Trust Repair in 72 Hours*. [https://www.digitalapplied.com/blog/grok-build-open-source-72-hours-trust-repair](https://www.digitalapplied.com/blog/grok-build-open-source-72-hours-trust-repair)

[15] Basenor. (2026). *Grok Rolls Out Across All of Europe: xAI Expands Continent-Wide*. [https://www.basenor.com/blogs/news/grok-rolls-out-across-all-of-europe-xai-expands-continent-wide](https://www.basenor.com/blogs/news/grok-rolls-out-across-all-of-europe-xai-expands-continent-wide)

[16] Perplexity AI. (2026). *Personal Computer Is Here*. [https://www.perplexity.ai/hub/blog/personal-computer-is-here](https://www.perplexity.ai/hub/blog/personal-computer-is-here)

[17] Releasebot. (2026). *Perplexity Release Notes — July 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[18] MarkTechPost. (2026). *Perplexity AI Introduces Hybrid Local-Server Inference Orchestrator for Personal Computer*. [https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/](https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/)

[19] Android Headlines. (2026). *Samsung's CEO Wants Your AI to Stop Answering Questions and Start Taking Action*. [https://www.androidheadlines.com/2026/07/samsung-ceo-tm-roh-galaxy-ai-agentic-age-unpacked.html](https://www.androidheadlines.com/2026/07/samsung-ceo-tm-roh-galaxy-ai-agentic-age-unpacked.html)

[20] Bloomberg. (2026). *Samsung Debuts AI-Powered Health Assistant, Joining Packed Market*. [https://www.bloomberg.com/news/articles/2026-07-21/samsung-debuts-ai-powered-health-assistant-joining-packed-market](https://www.bloomberg.com/news/articles/2026-07-21/samsung-debuts-ai-powered-health-assistant-joining-packed-market)

---