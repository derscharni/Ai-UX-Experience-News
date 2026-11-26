# UX Briefing: Workspaces Arrive, Prompts Go Private, and Agents Get a Time Machine

**November 26, 2026**

Good morning. The 48 hours ending November 26, 2026 are defined by four simultaneous surface-expansion and trust-design events: **Anthropic** completing its November workspace suite with **Claude Meetings** entering broader availability alongside **Claude Data** graduating from beta on all paid plans — both continuations of the November 10 Sheets and Whiteboards beta launch that is now settling into enterprise workflows — while simultaneously revealing a **Python-to-Rust API migration** that cut median time to first token by roughly 20% for Claude Code requests; **OpenAI** arriving at the same window with a two-track enterprise trust-design advance —

**Private Inference entering alpha testing on November 25–26, running model inference inside confidential computing environments so OpenAI itself cannot read prompts or responses while they are processed, alongside the unified Chat-and-Work usage meter beginning its rollout to a small group of Pro subscribers, merging the previously separate ChatGPT and Codex allowances into a single pool**

— as **ChatGPT Space** continues its global rollout to Plus subscribers following its November 20 launch, bringing collaborative auto-updating pages and presentations to the main chat product; **Google Gemini** completing its most consequential privacy-design event of the month — 

**the Gemini app's "Keep Activity" toggle splitting into two separate controls — History and AI training — rolling out globally from November 16, decoupling the user's choice to save conversations from their choice to contribute to model training, while Gemini for Home ships performance updates enabling smart appliance control mid-chat and faster voice interaction**

— and **Perplexity** shipping its most significant developer-infrastructure advance of the window on November 25 —

**Time Machine launching for the Search and Context APIs, letting developers and AI agents retrieve web pages as they existed on any chosen date up to 365 days back via a snapshot_as_of parameter, transforming retrieval infrastructure into temporal infrastructure for agentic evaluation, forecasting, and compliance workflows**

— while **Microsoft Copilot**'s **Today** experience continues its Frontier private preview and **Grok (xAI)**'s Build 1.0.89 remains the latest developer release, with Grok 4.8 still in multi-variant beta trials.

---

## At a Glance: November 26 Highlights

Today's window is defined by the category simultaneously hardening its trust architecture at the data layer — separating history from training, sealing prompts from the provider, and anchoring agent retrieval to verified historical snapshots — while the workspace expansion of the month settles into production.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Data (formerly Dashboards) now GA on all paid plans with certified queries and live sharing; Claude Meetings in broader availability with auto-join restored for Enterprise and some Team accounts; the Python-to-Rust API migration cuts median time to first token ~20% for Claude Code and reduces CPU usage ~70%; an active incident causes the Claude add-in to disappear from Excel, Word, and PowerPoint on Mac for personal Microsoft account holders** — the Rust migration's 20% first-token latency reduction is the agentic-workflow performance advance of the Anthropic window: for background agents executing long Claude Code sessions, shaving 20% from the moment the first token arrives collapses the perceptual gap between "agent is starting" and "agent is responding," directly improving the temporal UX of multi-step tasks. |
| **ChatGPT** | **OpenAI Private Inference enters alpha on November 25–26, running inference inside confidential computing environments with verifiable controls so OpenAI cannot access plaintext prompts or responses; the unified Chat-and-Work meter begins rolling out to a small group of Pro subscribers, with Instant model conversations staying unlimited and sitting outside the shared pool; ChatGPT Space continues its global rollout to Plus subscribers from November 20, with collaborative pages and presentations that auto-update from connected apps and tools, Dots invitation, and paid-plan-only sharing** — Private Inference is the trust-design event of the OpenAI window: for the first time, enterprise customers have a pathway to run prompts through OpenAI's models without OpenAI being architecturally capable of reading them, establishing a qualitatively new tier of data-custody that changes the trust conversation for regulated industries. |
| **Google Gemini** | **Gemini's "Keep Activity" privacy setting splits into two separate controls — History (chat retention) and AI training — rolling out globally from November 16; the update decouples the user's choice to save conversations from contributing data to model training; Gemini for Home ships its November 25 update with mid-chat smart appliance control, faster voice response, better device memory in follow-up commands, and source citations on smart displays** — the History/training split is the consent-architecture advance of the Gemini window: users who previously turned off "Keep Activity" to avoid training data contribution — and thereby lost their entire conversation history — can now preserve history while opting out of training, eliminating a coercive bundling that had made privacy a binary choice. |
| **Microsoft Copilot** | **Copilot Today remains in Frontier private preview in the Copilot app and Outlook, surfacing prioritized mail, calendar, Teams, and meeting signals with prefilled drafts; Copilot Autopilot is rolling out to Frontier customers as a persistent background agent with its own identity and memory; Agent 365 Business Analytics (Frontier Public) measures spend in work completed rather than tokens; Copilot usage-based billing models including GPT-6 Astra and Claude Fable 5.1 continue their November rollout to the model selector in Chat and Office apps** — Copilot Today's prefilled-draft pattern is the proactive-assistance design advance of the Microsoft window: an agent that reads the user's mail, calendar, and meetings, then prepares draft actions before a prompt is typed, inverts the standard interaction model from reactive query to ambient anticipation. |
| **Grok (xAI)** | **Grok Build 1.0.89 (released November 17) remains the latest Build release in this window, with improved dashboard commands, MCP server management, and session recovery, plus a /rename command and /resume confirmation dialogs; Grok 4.8 remains in multi-variant internal beta with no general availability date; Grok Bot's enterprise connector-permission architecture continues its rollout** — the session-recovery improvements in Build 1.0.89 are the agentic-reliability trust-design signal for xAI's developer surface: a /resume that opens a session in the directory it was recorded in, a prompt that is refused rather than silently dropped when session restoration fails, and a /resume picker that searches session contents as you type are all fixes to the class of failures where the agent's state diverges invisibly from the user's expectation. |
| **Perplexity** | **Perplexity Time Machine launches November 25 for the Search and Context APIs via a snapshot_as_of parameter, letting agents retrieve web pages as they existed up to 365 days ago; the Gemini 4 Hydrogen model is added to the Agent API; the Perplexity Chrome extension, Cloud Desktop live-view, Multiagent on mobile, and Brain self-improving skills from the November 24 changelog continue settling into broad availability** — Time Machine is the temporal-UX infrastructure advance of the Perplexity window: by allowing an agent to query the web as it existed at a specific historical moment, Perplexity is addressing the core evaluation problem of agentic workflows — an agent that can look up the outcome of a past event cannot be meaningfully tested on its ability to reason toward that outcome, and Time Machine removes that contamination by design. |

---

## Product Highlights

### Claude / Anthropic: The Workspace Suite Settles In, and the API Goes Faster

Anthropic's most consequential interaction-design story settling into broad availability in this window is the maturation of its November workspace suite — specifically **Claude Data** reaching full general availability across all paid plans alongside **Claude Meetings** restoring its auto-join capability — while simultaneously, a backend infrastructure change is delivering a measurable latency improvement to Claude Code's agentic workflows.



Claude Sheets and Claude Whiteboards launched in beta on 10 November 2026, and Claude Dashboards became generally available as Claude Data, on all paid Claude plans.

Claude Data "adds data stories, certified queries, and live sharing."

 The UX significance of Claude Data's GA status — particularly certified queries — is the trust-design layer it adds to agentic data workflows: when an agent answers "how are we doing?" from a company data warehouse, certified queries establish a governance checkpoint that distinguishes authoritative metrics from ad hoc calculations, giving the humans reviewing agent-generated dashboards a legibility signal about which numbers have been validated.



Anthropic paused automatic attendance after call-joining problems in November, then reported normal joining operations on November 19 and restored automatic attendance to all Enterprise customers and some Team customers.

Claude Data is out of beta on every paid plan and creates interactive dashboards from connected data sources.

 The Meetings restoration is the temporal-UX advance within the Anthropic window: an auto-join agent that disappears mid-deployment and then reappears is a background-agent whose reliability the user has had to actively monitor — the return to normal operation restores the ambient trust that background agents require to remain truly delegated rather than manually supervised.

The infrastructure advance that most directly affects agentic-workflow UX is the **Python-to-Rust API migration** disclosed this window. 

Anthropic has migrated its Messages API from Python to Rust, resulting in around 70% lower CPU usage per request and more than 80% lower memory consumption per request.

The migration also reduced the median time to first token by around 20% for the measured Claude Code requests.

 This latency reduction is not visible in Claude's interface but is the most consequential background-agent UX improvement of the week: for multi-step Claude Code tasks where the user is watching a progress surface, shaving 20% from first-token latency collapses the perceptual gap between task initiation and visible agent activity — the interval most likely to prompt a user to wonder whether the agent has started at all. 

An active incident from November 24–26 is causing the Claude add-in to disappear from Excel, Word, and PowerPoint on Mac for users signed in with a personal Microsoft account, with Anthropic recommending the web versions of Office at office.com as an interim measure.



---

### ChatGPT / OpenAI: Private Inference Seals the Prompt, Space Extends the Canvas, and the Meter Unifies

OpenAI's most consequential trust-design event in this window is **Private Inference** — an alpha feature announced November 25–26 that for the first time makes it architecturally impossible for OpenAI itself to read the prompts or responses of enterprise customers while their queries are being processed.



OpenAI is testing Private Inference, an alpha feature that encrypts prompts and model responses during processing, with a small group of selected API customers.

Private Inference keeps prompts and responses encrypted inside attested confidential environments, which verify the software running within the computing environment before data enters it.

OpenAI began alpha testing a Private Inference feature with a small group of customers, CEO Sam Altman announced on X on November 25, 2026, running model inference inside confidential-computing environments so OpenAI cannot access prompts or responses while they are processed.

 The UX implication is structural: the trust conversation for regulated enterprise customers — healthcare, legal, financial services — has previously been anchored in contractual commitments and zero-data-retention policies. Private Inference is the first architecture where the trust claim is verifiable rather than contractual: attested confidential environments prove that the software processing the prompt matches the software the customer has approved, before data enters it. 

OpenAI has not disclosed which models support the service, its performance overhead, or its pricing.

An OpenAI team member called the test "the first step towards private intelligence for everyone" and said the company is getting access to confidential compute capacity to scale it up substantially.



**ChatGPT Space**, which began rolling out to Plus subscribers on November 20 and continues settling into broad availability this window, is the generative-workspace advance that most directly expands the agent's output surface beyond the conversation panel. 

ChatGPT Space is rolling out globally to Plus users ages 18 and older; in Space, users can create interactive pages and presentations with ChatGPT, then invite other people with Space access to build on them; pages and slides can also be set to automatically update based on connected apps and tools.

If a user has a Dot, they can invite it to collaborate, too.

 The auto-updating page pattern — where a Space page connected to a live data source refreshes without the user requesting a manual update — is the ambient-data-surface design that moves generative content from a snapshot into a live artifact, shifting the agent's role from one-time generator to continuous maintainer. 

Shared pages can be opened only by recipients with an eligible paid ChatGPT account, limiting collaboration beyond Plus users.

 This access constraint is itself a trust-design decision: by restricting shared pages to paid accounts, OpenAI ensures that every collaborator on a connected, auto-updating page is an authenticated user under a known subscription relationship.

The **unified Chat-and-Work usage meter** beginning its Pro subscriber rollout on November 25 is the interaction-infrastructure advance that most changes how heavy agentic users experience their ChatGPT subscription. 

OpenAI began merging ChatGPT Chat and Work into one shared usage meter for a small group of Pro subscribers on November 25, 2026, marking a significant shift in how the company allocates compute resources.

Conversations with the Instant model remain unlimited and do not count toward the shared meter; users who exhaust their allowance can continue using Instant.

As agents take on longer, work-shaped tasks inside the same window as casual conversation, the subscription is no longer a bundle of separate allowances but one budget with a single drain.

 This is the resource-governance advance that makes the Chat-Work merger legible: by keeping Instant outside the meter, OpenAI preserves an always-available conversational baseline while applying quota pressure specifically to the high-compute agentic use cases — a design that communicates clearly which category of work is expensive.

---

### Google Gemini: History Splits from Training, and the Home Agent Gets Smarter

Google's most consequential trust-design event settling into broad availability in this window is the **Gemini privacy settings split** — the decoupling of chat history retention from AI training data contribution that the category has needed since conversational AI products first implemented activity controls.



Google is splitting the main privacy control of the Gemini app into two separate settings; in an announcement dated November 16, 2026, the company said Gemini users will be able to keep their chat history while opting out of having those chats used to train generative AI models, a combination the app's single activity switch did not allow.

The old Keep Activity switch handled both jobs at once, and it is now being split into a History setting and a separate Gemini AI training control, rolling out to users over the coming weeks; this matters because many people turned Keep Activity off just to keep their chats out of AI training, and lost their saved conversations in the process.

 The UX significance is in the coercive bundling that this update dismantles: when history and training are coupled in a single toggle, users who want privacy must pay for it with utility — losing the ability to reference past conversations, build consistent context, and benefit from memory features. The split resolves this by making two independent decisions independently governable. 

On the updated settings page, in addition to the option to turn History on or off and set the automatic deletion period, a new section titled "Help train generative AI models" has been added, with two options — "Chat content" and "Audio, Gemini Live videos, and screen sharing" — provided as checkboxes, allowing users to individually enable or disable the use of each type of content for training.



**Gemini for Home** shipping its November 25 update is the ambient-agent UX advance of the Google window. 

The update makes Gemini faster and allows users to control Google-compatible smart appliances during a chat; Gemini tells stories more expressively and adapts when asked to change a plot; it responds to smart home commands faster; it better remembers devices, so it can tell which one the user is referring to in follow-up commands; and it fixes a bug that could make Gemini say "nothing is playing" when asked to stop music or other media.

 The mid-chat smart appliance control is the interaction-pattern advance: an agent that can execute a smart home command — pause the TV, adjust the thermostat — without breaking out of an ongoing conversation establishes the ambient-always-available pattern for home automation, where control is a natural extension of dialogue rather than a mode switch. 

The update also restores "Hey Google, tell me a story," with expressive voices and dynamic pacing, and users can guide the story as it unfolds, changing details such as a character's abilities.

 The story-steering interaction — where the user shapes a generative narrative in real time — is the conversational-agency pattern applied to ambient home media: not a command to play content, but a collaborative authoring loop with the agent.

---

### Microsoft Copilot: Today Prioritises Before You Prompt, Autopilot Runs Behind the Scenes

Microsoft's most consequential interaction-design event in this window is **Copilot Today** settling into Frontier private preview — the proactive-briefing surface that inverts the standard Copilot interaction by preparing prioritised work and prefilled drafts before the user types a single prompt.



Inside Home is a new experience called Today; it's a command center across mail, calendar, Teams threads, meetings, and tasks; it proactively shows the user what they missed, what needs attention now, and what can wait; Today doesn't just surface the work, it helps get it done.

Its licensing is worth reading closely: the Today Brief is included with a Microsoft 365 Copilot license, while the Today Feed draws on Copilot credits.

 This licensing split is itself an interaction-design signal: the boundary between the proactive briefing (included) and the continuous priority feed (credit-drawing) is the line between the agent reading and summarising, and the agent actively maintaining an ongoing, refreshing attention surface. The Brief/Feed distinction operationalises the same read/act spectrum that has defined every other agentic trust-design event in November 2026 — passive context is bundled; active execution carries a marginal cost.



Autopilot is now accessible from Home and rolling out in Frontier; Autopilot is a personal, proactive agent with its own identity, memory, and tools that keeps work moving in the background.

 The Autopilot-from-Home architecture is the agentic-delegation design advance of the Microsoft window: by surfacing Autopilot's background tasks in the same view where Today surfaces today's priorities, Microsoft is creating a single visual surface where the user can see both what the agent has identified as urgent and what the agent is autonomously handling — collapsing the gap between agent-as-advisor and agent-as-worker into one management layer. 

Microsoft is also expanding identity and access governance through Entra Agent ID, adding new controls for agent tools, including MCP servers, plugins, and skills, and strengthening security and containment for local agents running on devices through deeper integration with Intune, Defender, and Windows with Microsoft Execution Containers.

 The Entra Agent ID expansion is the enterprise-governance layer that makes Autopilot deployable at scale: when every background agent has an identity in the same directory that governs human users, administrators can apply the same access policies, audit logs, and revocation mechanisms to agents that they apply to employees.

---

### Grok (xAI): Build Consolidates Session Recovery

xAI's interaction-design story in this window is defined by the continued developer-adoption phase of **Grok Build 1.0.89** — a release focused on the class of session-state failures that most erode trust in long-running agentic coding workflows.



Grok Build 1.0.89 improves dashboard commands, workflow and MCP server management, and session recovery, while fixing keyboard input, search, links, timers, sign-in messaging, and hangs when providers fail to respond.

New features include a /rename command on the dashboard that renames the selected session without opening it, and /resume in minimal mode now shows "y confirm delete · n cancel" before deleting a session.

 The /resume confirmation dialog is the trust-design detail that merits most attention: a session deletion that previously had no confirmation gate now surfaces an explicit y/n prompt before proceeding, establishing the same irreversibility checkpoint at the session layer that the broader category has been establishing at the action layer — a pattern that recognises that deleting a session's accumulated context is a consequential, hard-to-reverse action. 

Additional improvements include a /resume picker that now searches session contents as the user types and lets them open a match; stop buttons in the dock stop a background run while its approval card is open instead of doing nothing; and rejecting a change keeps edits the user saved to the file, even when Grok missed the save.

As of November 24, 2026, Grok 4.8 is not generally available; Musk wrote on November 17 that it has had only trials behind the scenes, and on November 19 that it has several model variants in beta with no pick yet for wide release.

 The absence of a Grok 4.8 general release in this window — while the developer tool continues to consolidate session-state reliability — is itself a trust-design signal: xAI's current developer-surface investment is in the infrastructure that makes existing agentic capabilities trustworthy enough to delegate to, rather than adding new capabilities that would require a new trust architecture to govern them.

---

### Perplexity: Time Machine Anchors Agents to the Historical Web

Perplexity's most significant interaction-design event in this window is **Time Machine** — a November 25 launch that transforms the platform's retrieval APIs into temporal infrastructure, giving developers and AI agents the ability to query the web as it existed on any chosen date.



Perplexity announced Time Machine on November 25, 2026 for its Search API and Context API, allowing developers and agents to search and read the web through copies saved at or before a chosen timestamp.

Developers activate Time Machine by adding snapshot_as_of to an existing API request; Perplexity saves a timestamped copy whenever it crawls a page, then uses the latest stored copy from at or before the requested cutoff.

Time Machine is available to existing Perplexity API customers with no new endpoint or setup.

 The zero-new-endpoint adoption model is the interaction-infrastructure advance that matters most for enterprise operators: a temporal constraint that activates via a single parameter addition — rather than requiring a new API integration, new credentials, or a new service — means that existing agentic workflows can retroactively gain temporal grounding without architectural changes. This shifts Time Machine from a research feature to a production-operations tool.

The trust-design implication is significant for agentic evaluation workflows. 

A team can present an agent with a question as it stood at an earlier point, grade the answer against the subsequent outcome, and test whether a model, prompt, or retrieval setup improved performance.

Time Machine lets developers test AI forecasting without hindsight contamination, since an agent can no longer simply look up the outcome of a past event.

 This is the agent-evaluation trust problem in its clearest form: an agent that can retrieve current web pages when asked about a past event is an agent that cannot be meaningfully evaluated on its reasoning, because it always has access to the answer. Time Machine removes that contamination, making it possible to build evaluations where the agent's retrieval and reasoning capabilities are genuinely tested rather than bypassed. 

For finance and compliance, point-in-time reads anchor analysis to the information set available when decisions were made.

 The compliance application is the production deployment that most clearly justifies Time Machine as a trust-design feature: an AI agent whose retrieval is pinned to the information available at a decision point can produce analysis that is auditable against the same information constraints that governed the original human decision.

---

## The Bigger Picture: Workspaces Arrive, Prompts Go Private, and Agents Get a Time Machine

The 48 hours ending November 26, 2026 crystallise a single macro movement that has been building across the month: **the AI agent category is completing its migration from a trust architecture built on contractual commitments and UI-level controls to one built on verifiable technical guarantees — and every significant trust-design event in this window is an answer to the same underlying question: how does the user know that the agent is operating within the boundaries they intended, and how does the enterprise know that its data is protected by something stronger than a promise?** OpenAI's Private Inference is the clearest single expression: for the first time, enterprise trust in an AI provider's data handling is not anchored in terms of service or audit rights, but in attested confidential environments that verify the software before data enters it — a move from "trust us" to "verify this." Google's Gemini history/training split answers the same question at the user layer: by decoupling two previously bundled privacy decisions, Google is replacing a coercive all-or-nothing consent with two independently governable choices, each of which users can inspect, adjust, and understand without sacrificing the other. Perplexity's Time Machine answers it at the retrieval layer: by allowing operators to pin an agent's web access to a historical snapshot, Perplexity is giving developers a verifiable guarantee that the agent's knowledge base at evaluation time matches the knowledge base that existed when a past decision was made — making agentic analysis auditable against the same information constraints that governed human decisions. Claude Data's certified queries answer it at the data layer: when an agent-generated dashboard carries a certification signal, the humans reviewing it have a legibility marker that distinguishes governance-approved metrics from ad hoc calculations. And Microsoft's Copilot Today and Autopilot, arriving in the same window, answer the same question at the workflow layer: a background agent that proactively prepares drafts before being asked, and runs ongoing tasks under an Entra identity that can be audited and revoked, is an agent whose authority is bounded by the same identity and access governance that covers every other actor in the enterprise. What connects all five — Private Inference's sealed chips, Gemini's split toggles, Perplexity's historical snapshots, Claude Data's certified queries, and Copilot's Entra-scoped Autopilot — is the same design conclusion November 2026 has been building toward: the category's trust architecture is graduating from policy to proof, from UI controls to verifiable constraints, from "the agent won't" to "the agent structurally cannot," and the platforms that build that proof into their interaction primitives — rather than layering it onto already-deployed agents as a marketing claim — are the ones whose enterprise users will delegate the most.

---

## References

[1] kellyabbott1.substack.com. (2026). *AI Frontier Daily — November 26, 2026*. [https://kellyabbott1.substack.com/p/ai-frontier-daily-2026-11-26](https://kellyabbott1.substack.com/p/ai-frontier-daily-2026-11-26)

[2] geeky-gadgets.com. (2026). *Anthropic Claude November 2026 Feature Updates Explored*. [https://www.geeky-gadgets.com/anthropic-claude-november-2026-features/](https://www.geeky-gadgets.com/anthropic-claude-november-2026-features/)

[3] status.claude.com. (2026). *Claude Status — November 26, 2026*. [https://status.claude.com/](https://status.claude.com/)

[4] pcguide.com. (2026). *Anthropic moves Claude backend from Python to Rust to deliver massive CPU and memory savings*. [https://www.pcguide.com/pro/news-pro/anthropic-moves-claude-backend-from-python-to-rust-to-deliver-massive-cpu-and-memory-savings/](https://www.pcguide.com/pro/news-pro/anthropic-moves-claude-backend-from-python-to-rust-to-deliver-massive-cpu-and-memory-savings/)

[5] powerdrill.ai. (2026). *Claude Sheets and Claude Data: What's New, Access, and Alternatives (2026)*. [https://powerdrill.ai/blog/claude-sheets-and-claude-data](https://powerdrill.ai/blog/claude-sheets-and-claude-data)

[6] cryptobriefing.com. (2026). *Anthropic launches Claude Sheets and Claude Whiteboards in beta*. [https://cryptobriefing.com/anthropic-launches-claude-sheets-whiteboards-beta/](https://cryptobriefing.com/anthropic-launches-claude-sheets-whiteboards-beta/)

[7] munderdiffl.in. (2026). *Claude Sheets, Whiteboards and Data: What Launched, Who Gets It*. [https://munderdiffl.in/blog/claude-sheets-whiteboards-data/](https://munderdiffl.in/blog/claude-sheets-whiteboards-data/)

[8] samonai.substack.com. (2026). *AI Brief — November 26, 2026*. [https://samonai.substack.com/p/ai-brief-november-26-2026](https://samonai.substack.com/p/ai-brief-november-26-2026)

[9] dev.to. (2026). *AI Daily Digest, November 26, 2026: One Meter for ChatGPT and Codex*. [https://dev.to/hiroki-ii-ai/ai-daily-digest-november-26-2026-one-meter-for-chatgpt-and-codex-cognition-doubles-down-europe-2j0o](https://dev.to/hiroki-ii-ai/ai-daily-digest-november-26-2026-one-meter-for-chatgpt-and-codex-cognition-doubles-down-europe-2j0o)

[10] dataconomy.com. (2026). *OpenAI tests encrypted Private Inference with select customers*. [https://dataconomy.com/2026/11/26/openai-tests-encrypted-private-inference-with-select/](https://dataconomy.com/2026/11/26/openai-tests-encrypted-private-inference-with-select/)

[11] news.sulat.com. (2026). *OpenAI tests Private Inference, a sealed prompt while the model runs*. [https://news.sulat.com/2026/11/26/openai-private-inference/](https://news.sulat.com/2026/11/26/openai-private-inference/)

[12] cryptopolitan.com. (2026). *OpenAI lines up confidential compute to scale Private Inference*. [https://www.cryptopolitan.com/openai-compute-scale-private-inference/](https://www.cryptopolitan.com/openai-compute-scale-private-inference/)

[13] emergent.sh. (2026). *OpenAI Merges ChatGPT Chat and Work into One Usage Meter*. [https://emergent.sh/news/openai-merges-chatgpt-chat-work-into-one](https://emergent.sh/news/openai-merges-chatgpt-chat-work-into-one)

[14] news.lavx.hu. (2026). *OpenAI merges ChatGPT Chat and Work under one usage meter*. [https://news.lavx.hu/article/openai-merges-chatgpt-chat-and-work-under-one-usage-meter](https://news.lavx.hu/article/openai-merges-chatgpt-chat-and-work-under-one-usage-meter)

[15] releasebot.io. (2026). *ChatGPT Updates by OpenAI — November 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[16] dataconomy.com. (2026). *ChatGPT Rolls Out Space Workspace For Plus Users*. [https://dataconomy.com/2026/11/25/chatgpt-rolls-out-space-workspace-for-plus-users/](https://dataconomy.com/2026/11/25/chatgpt-rolls-out-space-workspace-for-plus-users/)

[17] zeniteq.com. (2026). *OpenAI Rolls ChatGPT Space Out to Plus Worldwide*. [https://www.zeniteq.com/news/openai-rolls-chatgpt-space-out-to-plus-worldwide-dp1bnt](https://www.zeniteq.com/news/openai-rolls-chatgpt-space-out-to-plus-worldwide-dp1bnt)

[18] uctoday.com. (2026). *ChatGPT Space Comes to Plus Users for Shared Pages, Slides and Sites*. [https://uctoday.com/in-brief/chatgpt-space-comes-to-plus-users-for-shared-pages-slides-and-sites](https://uctoday.com/in-brief/chatgpt-space-comes-to-plus-users-for-shared-pages-slides-and-sites)

[19] kucoin.com. (2026). *Google Introduces New Privacy Controls for Gemini: Chat History and AI Training Separated*. [https://www.kucoin.com/news/flash/google-adds-new-privacy-controls-for-gemini-chat-history-and-ai-training-separated](https://www.kucoin.com/news/flash/google-adds-new-privacy-controls-for-gemini-chat-history-and-ai-training-separated)

[20] newsbytesapp.com. (2026). *Google's Gemini app adds chat history and training controls*. [https://www.newsbytesapp.com/news/science/googles-gemini-app-adds-chat-history-and-training-controls/tldr](https://www.newsbytesapp.com/news/science/googles-gemini-app-adds-chat-history-and-training-controls/tldr)

[21] jetstream.blog. (2026). *Gemini "My Activity" Updated: Now Supports Individual Learning Settings*. [https://jetstream.blog/en/gemini-myactivity-renewal-november-2026/](https://jetstream.blog/en/gemini-myactivity-renewal-november-2026/)

[22] datastudios.org. (2026). *Gemini lets you keep chat history and turn off AI training: new settings explained*. [https://www.datastudios.org/post/gemini-app-separate-history-and-ai-training-settings-two-month-retention](https://www.datastudios.org/post/gemini-app-separate-history-and-ai-training-settings-two-month-retention)

[23] howtogeek.com. (2026). *Google Home's latest update brings 19 changes, including performance upgrades*. [https://www.howtogeek.com/google-home-latest-update-changes-speed-upgrade/](https://www.howtogeek.com/google-home-latest-update-changes-speed-upgrade/)

[24] analyticsinsight.net. (2026). *Google Home Update Brings Gemini Improvements, Nest Cam Features and Thermostat Controls*. [https://www.analyticsinsight.net/news/google-home-update-brings-gemini-improvements-nest-cam-features-and-thermostat-controls](https://www.analyticsinsight.net/news/google-home-update-brings-gemini-improvements-nest-cam-features-and-thermostat-controls)

[25] microsoft.com. (2026). *Copilot at Microsoft Ignite: Expanding what's possible with intelligence built for work*. [https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/](https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/)

[26] techcommunity.microsoft.com. (2026). *Home: Your starting place for work in the Microsoft Copilot app*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/home-your-starting-place-for-work-in-the-microsoft-copilot-app/4573945](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/home-your-starting-place-for-work-in-the-microsoft-copilot-app/4573945)

[27] hubsite365.com. (2026). *Microsoft Copilot Today prioritizes your workday*. [https://www.hubsite365.com/en-ww/crm-pages/microsoft-copilot-today-prioritizes-your-workday.htm](https://www.hubsite365.com/en-ww/crm-pages/microsoft-copilot-today-prioritizes-your-workday.htm)

[28] epcgroup.net. (2026). *Microsoft Ignite 2026 Day 1 Announcements*. [https://www.epcgroup.net/insights/microsoft-ignite-2026-day-1-announcements](https://www.epcgroup.net/insights/microsoft-ignite-2026-day-1-announcements)

[29] releasebot.io. (2026). *Grok Build Updates by xAI — November 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[30] cellcog.ai. (2026). *Grok 4.8 Release Date: Several Variants in Beta, Musk Says*. [https://cellcog.ai/blog/grok-4-8-release-date/](https://cellcog.ai/blog/grok-4-8-release-date/)

[31] unite.ai. (2026). *Perplexity Launches Time Machine for Point-in-Time Web Retrieval*. [https://www.unite.ai/perplexity-launches-time-machine-for-point-in-time-web-retrieval/](https://www.unite.ai/perplexity-launches-time-machine-for-point-in-time-web-retrieval/)

[32] emergent.sh. (2026). *Perplexity Time Machine API Launches Point-in-Time Search*. [https://emergent.sh/news/perplexity-time-machine-api-launches-point](https://emergent.sh/news/perplexity-time-machine-api-launches-point)

[33] wisevoter.com. (2026). *Perplexity Launches Time Machine for Dated Web Search*. [https://wisevoter.com/world/2026/11/25/perplexity-time-machine-dated-web-search](https://wisevoter.com/world/2026/11/25/perplexity-time-machine-dated-web-search)

[34] computing.net. (2026). *Perplexity Time Machine Lets AI Agents Search the Web as It Was*. [https://computing.net/perplexity-time-machine-lets-ai-agents-search-the-web-as-it-was/](https://computing.net/perplexity-time-machine-lets-ai-agents-search-the-web-as-it-was/)

[35] docs.perplexity.ai. (2026). *Changelog — November 2026*. [https://docs.perplexity.ai/docs/resources/changelog/rss.xml](https://docs.perplexity.ai/docs/resources/changelog/rss.xml)