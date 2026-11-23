# UX Briefing: Computer Use Goes Corporate, Space Opens to All, and Gemini Separates Its Signals

**November 23, 2026**

Good morning. The 48 hours ending November 23, 2026 are defined by four simultaneous surface-expansion and trust-design events: **Anthropic** executing its most consequential enterprise computer-use governance event of the year on November 20 — 

**Claude Computer Use reaching Team and Enterprise plans in beta**, letting Claude see a user's screen and work in the desktop apps they allow, in the new Claude Desktop experience and from the web and Claude Mobile where Computer access is on, rolling out to organisations gradually

 — while simultaneously 

**rolling out a refreshed look for Claude Mobile**, starting with iOS, with chats, projects, and plan unchanged

; **OpenAI** completing a week-long collaborative-workspace and domain-workflow expansion cluster — 

**ChatGPT Space reaching Plus users globally on November 20**, replacing Library in the sidebar with a surface for creating interactive pages and presentations that can automatically update from connected apps

, alongside the **Accounting plugin** and **Live Dictation** upgrades shipping on November 18; **Google Gemini** arriving at the same 48-hour window with two simultaneous interaction-design events — 

**a thorough camera redesign for the Gemini Android app** that widely rolled out in both beta and stable (version 17.76+)

 and 

the launch of GIF creation, powered by Gemini Omni 1.2 Flash

 — following the November 16 disclosure that 

Google is **giving users more control over when Gemini chat history is used to train generative AI models**, with new settings to keep history while opting out of training

; and **xAI** shipping **Grok Bot 1.2.3** on November 18 with a granular four-tier connector-permission architecture, while Perplexity launched **Intelligence** on November 22 as an enterprise research workspace combining real-time retrieval with multi-step reasoning workflows for finance, legal, and healthcare professionals.

---

## At a Glance: November 23 Highlights

Today's window is defined by the industry's simultaneous convergence on a single structural shift: expanding the AI agent's execution surface — from individual screens to enterprise desktops, from Pro-tier workspaces to Plus-tier collaborative pages, from single-action connector permissions to per-action granular controls — while in parallel tightening the trust and consent architecture that governs what agents can do with what they access.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Computer Use launches in beta on Team and Enterprise plans on November 20, 2026 — off by default, admin-gated, running in Claude Desktop and from the web and Claude Mobile where Computer access is on, rolling out to organisations gradually; a refreshed Claude Mobile look begins rolling out on iOS; and the November 17 release-channel toggle (Stable vs. Latest, ~daily) in Claude Desktop gives both users and IT teams explicit control over how rapidly desktop builds deploy** — the admin-off-by-default governance architecture is the trust-design signal of the window: unlike the individual-plan computer-use feature, the Team and Enterprise rollout requires an explicit Owner decision to activate, shifting the consent model from user-opt-in to organisational-authorisation. |
| **ChatGPT** | **ChatGPT Space reaches Plus users globally on November 20, replacing Library with a collaborative workspace for interactive pages and presentations that auto-update from connected apps — Dots cannot join Plus Spaces at rollout; ChatGPT for Accounting launches November 18 with the Accounting plugin (QuickBooks, Xero, NetSuite, BILL, FreshBooks, and others) for Work and Business plans; Live Dictation goes unlimited-duration across all plans on November 18 with real-time transcription and an opt-in showable/hideable text display** — Space's global Plus rollout is the collaborative-workspace democratisation event of the window: a feature previously limited to Pro, Business, and Enterprise users has descended to the $20-per-month tier, redefining the shared-page and presentation surface as standard ChatGPT infrastructure rather than an enterprise upsell. |
| **Google Gemini** | **Gemini's Android in-app camera redesigns from a fullscreen viewfinder to an inline bottom sheet draggable up from the prompt box, landing in both beta and stable (version 17.76+) on November 21 and aligning with the iOS version already live; GIF creation launches November 20 powered by Gemini Omni 1.2 Flash, selectable from the Format menu or via "Create a GIF" in a prompt; and the November 16 chat history/training split — giving users separate toggles for history retention and model-training consent — enters global rollout** — the history-training decoupling is the trust-design event of the Gemini window: Google was previously the only major AI assistant that forced an all-or-nothing trade-off between keeping conversation history and opting out of training data, and the new split resolves a gap that ChatGPT and Claude had addressed long before. |
| **Microsoft Copilot** | **Copilot Home (Chat and Cowork unified), Office in Copilot, and Copilot Managed Runtime reach general availability post-Ignite; Autopilot — the always-on personal agent with its own Microsoft Entra Agent ID, named manager, and audit-logged sign-ins — begins rolling out to Frontier customers; Agent Accounts in Copilot Studio enter public preview in December; Agent 365 Business Analytics connects spend, guardrails, adoption, and ROI; MCP server governance lands under Agent 365 in preview; and Copilot Cowork in GCC begins rolling out** — Autopilot's Entra Agent ID architecture is the trust-design event of the Microsoft window: an agent that authenticates and logs under its own named identity, scopeable and blockable by IT at any time, establishes the first broadly available enterprise AI agent with an audit trail that is fully separable from the acting human. |
| **Grok (xAI)** | **Grok Bot 1.2.3 (November 18) introduces a four-tier connector-permission system — Always allow, Auto-review, Needs approval, Blocked — letting users set per-action rules for each connected app rather than granting all-or-nothing access; before irreversible actions (sending, posting, buying, deleting) a Bot checks for explicit approval; browser approval cards describe actions in plain language; in Slack, Team Bots gain message-editing rights; and team admins can restrict Bot sharing to admins only** — the per-action four-tier permission architecture is the trust-design advance of the xAI window: a user can allow a Bot to search and list items in a connected app while requiring Needs approval for any create, change, or delete action — operationalising the read/write distinction at the connector level for the first time. |
| **Perplexity** | **Perplexity Intelligence launches November 22, 2026, with immediate enterprise availability — combining real-time web retrieval with enhanced multi-step reasoning for finance, legal, healthcare, and academic knowledge workers; the platform integrates with Perplexity's existing API infrastructure for embedding into custom workflows; Computer's Deep Research feature is now available inside Computer alongside a new command panel as a single access point; and the Search as Code optimisations routing through a unified SDK-backed interface continue rolling out** — Intelligence's positioning as an enterprise research workspace rather than a search alternative is the product-definition signal of the Perplexity window: by combining real-time retrieval with structured multi-step reasoning workflows for specific professional domains, Perplexity is completing its transition from answer engine to governed research infrastructure. |

---

## Product Highlights

### Claude / Anthropic: Computer Use Enters the Enterprise and Mobile Gets a New Face

Anthropic's most consequential interaction-design event in this window is not an individual-user feature but an enterprise governance expansion: 

**Claude Computer Use** in beta for Claude Team and Enterprise plans, with the capability functioning within the Claude Desktop experience and extending to Claude on the web and Claude Mobile wherever an administrator has enabled Computer access.



The governance architecture of the Team and Enterprise rollout is structurally different from the individual-plan computer-use model in a critical way. 

Computer Use is off by default for every Team and Enterprise organisation, and only an Owner or Primary Owner can switch it on under Organisation settings.

Until this week, Computer Use was available only to individuals on the Pro, Max, and Ultra plans; Team and Enterprise organisations did not have access.

 This sequencing — individual access first, organisational access second, with an explicit admin gate — is a deliberate trust-design choice: it prevents the capability from being activated by individual employees before an organisation's security and IT review has considered whether the agent should have screen access in a managed environment. The UX implication for enterprise administrators is a decision that has arrived this week: 

on November 17, Anthropic also added a release-channel toggle inside Claude Desktop so users can choose between Stable updates and a Latest track that ships about once a day, and IT and security leads should decide where the Computer access toggle lives in their change-management process before a team flips it on ahead of them.

The computer use approval dialog was also improved: it now shows each app's level of access and plainer warnings.

 This micro-trust-design detail matters precisely because computer use is not just a task-execution surface — it is a capability where the specificity of what the agent can access determines whether a user can make an informed decision about whether to grant it. An approval dialog that surfaces each app's access level, rather than a single blanket confirmation, gives users the information needed to make differentiated decisions about which applications to include and which to exclude.

The **release-channel toggle**, shipped November 17, is the developer-and-IT trust-design advance that pairs with the computer-use rollout: 

users can now use a release channel to set which version of Claude Desktop they receive when the app updates — Stable stays the default and gets new versions less often after more testing, while Latest gets a new version about once a day so fixes and new features reach users sooner.

Administrators can set the release channel for managed devices through the admin console's Telemetry and updates page, preventing users from overriding the organisation's choice.

 The governance-UX significance of this pairing is structural: an organisation that enables Computer Use on a managed fleet now has explicit control over how rapidly those builds update, ensuring that computer-use behaviour does not change beneath a team mid-deployment.

---

### ChatGPT / OpenAI: Space Reaches Plus, Accounting Lands, and Dictation Goes Unlimited

OpenAI's most consequential interaction-design event in this window is the **ChatGPT Space global Plus rollout** — the moment when the collaborative-workspace surface that debuted at September's developer conference for Pro, Business, and Enterprise accounts descends to the $20-per-month tier.



Starting November 20, ChatGPT Space is rolling out globally to Plus users ages 18 and older; in Space, users can create interactive pages and presentations with ChatGPT, invite other people with Space access to build on them collaboratively, and set pages and slides to automatically update based on connected apps and tools.

Space replaces Library and is available on web, desktop, iOS, and Android.

 The architectural significance is in what Space does to the relationship between conversation and artifact: Library stored outputs after conversations; Space is a persistent shared environment where outputs live alongside future conversations, can be co-authored, and can stay in sync with connected data sources. 

November 20, 2026, is the day OpenAI stopped treating collaboration as an enterprise upsell and declared it part of the default ChatGPT experience for anyone paying twenty dollars a month.

Dots cannot currently be invited to collaborate in Plus Spaces, though OpenAI began testing Dots with a select group of Plus subscribers outside the European Economic Area, the United Kingdom, and Switzerland on November 19.

 This staged rollout creates a consequential interaction gap: Plus users now have a collaborative workspace but do not yet have the persistent agent that can join it — the architecture exists, but the agent-in-workspace pattern is not yet available at this tier.

**ChatGPT for Accounting**, launched November 18, is the domain-workspace advance of the OpenAI window. 

OpenAI officially launched ChatGPT for Accounting on November 18, 2026, packaging a native accounting plugin with eight third-party integrations designed for finance teams, targeting invoice processing, bank reconciliation, month-end close workflows, data entry, and audit preparation.

The named integrations include Intuit's QuickBooks, Xero, and Oracle's NetSuite, with BILL, FreshBooks, Rillet, and Campfire also listed among the launch partners.

 The human-oversight interaction pattern is explicit in the design: 

the model drafts the output — whether that is a match between bank statements and ledger entries, a batch of journal entries, an invoice queue, or the documentation set an external audit requires — and the person using the tool reviews the draft.

 This draft-then-review model is the agentic-accounting pattern that balances automation with the auditability requirement that financial workflows impose.

**Live Dictation** is the cross-platform input-design advance of the window. 

OpenAI launched Live Dictation for ChatGPT across all plans on November 18, 2026, with the feature transcribing speech in real-time on web, desktop, iOS, and Android, and removing the previous 10-minute recording limit.

For private accounts, OpenAI uses dictation audio for model training only if audio sharing has been explicitly enabled in data controls; business accounts are excluded from training by default.

 The trust-design detail here is the data-use differentiation: a consumer user who dictates without reviewing data controls is by default contributing audio to training, while a business user is not — an asymmetry that places the consent burden on individual users rather than the enterprise tier.

---

### Google Gemini: Camera Becomes Conversational, Training Opts Out, and GIFs Arrive

Google's most consequential trust-design event in this window is not the camera redesign or GIF creation — both significant interaction-design advances — but the **separation of Gemini's chat history and training controls**, announced November 16, which closes the most visible privacy-UX gap between Gemini and its main competitors.



In an announcement dated November 16, 2026, Google said Gemini users will be able to keep their chat history while opting out of having those chats used to train generative AI models — a combination the app's single activity switch did not allow.

Previously, users who wanted to keep conversations out of training had to turn off chat history, which also stopped the history feature from preserving threads for later access; the new design separates those choices, letting users leave history enabled while turning off the model-training control.

Chat history is enabled by default for adults, while training is disabled.

 The trust-design significance is competitive and structural: 

ChatGPT and Claude have let people keep history without training for a long time, and Gemini was the odd one out

 — but the more important point is that the previous coupling of the two settings was a design choice that made privacy protection incompatible with conversational continuity, forcing users to choose between the two rather than exercising them independently.

The **Gemini Android camera redesign** is the input-UX advance of the window. 

The new camera appears inline on the Gemini homepage or inside a conversation, as a nearly edge-to-edge redesign that extends behind the system navigation bar.

The inline design, which launched on November 20 for GIF creation alongside the camera update on November 21, keeps the camera within the conversation rather than jumping to an isolated screen, maintaining conversational continuity.

 The UX shift is from camera-as-detour to camera-as-inline-input: when attaching an image launches a bottom sheet within the conversation rather than navigating away, the friction of multimodal prompting decreases — the camera becomes an extension of the prompt box rather than an interruption of the conversation flow.



GIF creation is powered by Gemini Omni 1.2 Flash, selectable from the Format menu or specifiable with "Create a GIF" in a prompt.

Neowin noted the addition follows OpenAI introducing similar GIF generation to ChatGPT earlier in November

 — placing both products in direct competition on a creative output format used daily in messaging and social contexts, and confirming that animated-GIF generation has converged from differentiator to table-stakes in this product cycle.

---

### Microsoft Copilot: Autopilot's Identity, Cowork's GCC Reach, and Agent Governance Expands

Microsoft's most consequential trust-design event settling into broad availability in this window is **Copilot Autopilot** beginning its Frontier rollout — the first enterprise-grade always-on personal agent in the Copilot ecosystem to authenticate under its own identity rather than acting as a proxy for the human user.



Autopilot is a trusted autonomous agent that is personal to you, always on, and working for you — it lives in your tenant and has its own identity, memory, and tools, showing up where people already work, like Teams, Outlook, chats, channels, and documents, so you can @mention it like a colleague.

 The trust-design architecture is explicit: 

each Autopilot has its own Microsoft Entra Agent ID and a named manager, IT can scope its access and block it anytime, its sign-ins and actions are logged under its own name so security teams have a clear audit trail, and powered by Work IQ it understands how the organisation works within existing permissions.

 The UX implication of a named agent identity is a fundamental shift in accountability: when an agent acts under its own Entra ID rather than as the user, the audit trail separates human decisions from agent decisions — an enterprise security requirement that prior AI assistant architectures, which delegated everything under the user's own permissions, could not satisfy.



Home, where Chat and Cowork come together, and Office in Copilot are now generally available.

 The **Copilot Home** general availability is the interaction-architecture event of the post-Ignite window: 

Ignite confirms Chat and Cowork together at GA and adds the useful handover where Auto can recommend Cowork when a question becomes a larger task.

 This mode-switching recommendation is a consequential interaction-design decision: rather than requiring users to decide whether a task belongs in Chat or Cowork, the system now recommends escalating when it detects that a question has become a task — shifting the routing decision from user judgment to agent inference.



Microsoft is also expanding identity and access governance through Entra Agent ID, adding new controls for agent tools including MCP servers, plugins, and skills, and strengthening security and containment for local agents running on devices through deeper integration with Intune, Defender, and Windows with Microsoft Execution Containers.

 The MCP governance addition is the developer-infrastructure trust-design advance: centralised management of MCP servers through Agent 365 means enterprise administrators can govern which model context protocol servers any agent in the tenant can connect to, applying the same policy-and-approval model to the agent tool layer that already governs the app and plugin layer.

---

### Grok (xAI): Bot 1.2.3 Builds Per-Action Permission Architecture

xAI's most significant interaction-design and trust-design event in this window is **Grok Bot 1.2.3**'s introduction of a four-tier connector-permission system — an architecture that operationalises the read/write distinction at the action level for the first time in the Grok Bot surface.



Connector pages now let users set each tool to Always allow, Auto-review, Needs approval, or Blocked.

For connected apps, users can set permissions for individual actions rather than giving the bot the same access to everything — for example, letting it search or list items while requiring approval before it creates, changes, or deletes anything, with the November 18 update listing the four settings: Always allow, Auto-review, Needs approval, and Blocked.

 The UX significance of this granularity is structural: a connector-level permission model that cannot distinguish read from write forces users to choose between "agent can do nothing" and "agent can do everything" — a binary that makes it rational to either over-grant or refuse access entirely. The four-tier model enables a middle path where the agent's read access is trusted and its write access is supervised.



Before an action it cannot undo — such as sending, posting, buying, or deleting — a Bot checks the user's own messages for approval; browser approval cards describe actions in plain words, such as "Open a new tab in Grok Bot's browser," and a saved Allow rule applies the same way on every tool.

 This is the trust-design pattern that the category needs at scale: rather than a single pre-task permission grant that covers all subsequent actions, the Bot interrupts specifically at irreversibility boundaries, narrows the approval request to plain-language descriptions of the specific action, and lets users save an Allow rule that applies consistently going forward — building trust through predictable, legible checkpoints rather than a single broad consent.



In the Slack-side governance improvements, Team Bot admins can limit Bot sharing to admins, and share controls then say "Your admin has disabled Bot sharing."

In Team Bot Slack setup, Connect goes straight to Slack, Awaiting admin approval offers Resubmit, and a denied request shows when it was denied.

 The admin-sharing restriction is the enterprise-governance advance within the Slack surface: a team administrator who restricts Bot sharing to admins prevents the proliferation of team-shared Bots before governance processes for evaluating what those Bots can access have been established.

---

### Perplexity: Intelligence Launches as a Professional Research Workspace

Perplexity's most significant interaction-design event in this window is the November 22 launch of **Perplexity Intelligence** — a product that marks the clearest statement yet of what Perplexity is becoming at the enterprise layer.



Perplexity has officially launched Intelligence, a next-generation AI research platform that combines real-time web search with advanced reasoning capabilities, building on existing search infrastructure while introducing enhanced reasoning layers designed for multi-step research workflows.

Perplexity designed Intelligence for knowledge workers in sectors including finance, legal research, healthcare, and academia.

 The interaction-design significance is in the workflow structure: Intelligence is not a faster search box but a workspace that takes a complex professional query, executes multi-step retrieval and reasoning across live web sources, and delivers a structured output appropriate to the professional domain — bridging the gap between "search with citations" and "agent-executed research workflow."



Perplexity also adds Deep Research in Computer, a new command panel, forking, improved inline confirmations, and enterprise controls including a Computer Analytics API and custom credit limits, making it easier to research, build artifacts, and manage usage.

 The command panel is the navigability-UX advance that pairs with Deep Research: 

the new Computer command panel is a single place to discover and access everything Computer can do

 — addressing a discoverability gap that has persisted in Computer since its launch, where the breadth of available actions was not visible to users who had not explored the full surface.

The Intelligence launch follows Perplexity's November 16 shipping of its Monitor API — which 

watches a topic or page and delivers a webhook when something relevant changes

 — establishing a monitoring-plus-reasoning loop where Computer can initiate work reactively in response to world-state changes rather than only in response to explicit user prompts. Together, Intelligence and the Monitor API define the two ends of Perplexity's enterprise research architecture: a synchronous deep-research surface for high-stakes professional queries, and an asynchronous monitoring layer for persistent topic tracking.

---

## The Bigger Picture: Computer Use Goes Corporate, Space Opens to All, and Gemini Separates Its Signals

The 48 hours ending November 23, 2026 crystallise a single macro movement that has been building across the month: **the AI agent category is completing its migration from consumer-permissive to enterprise-governed, and the trust-design decisions that defined this window are all expressions of the same underlying question — who authorises the agent, at what granularity, and with what audit trail?** Claude Computer Use reaching Team and Enterprise plans is the clearest single expression: a capability that individual Pro users could already access arrives at the organisational level not as a uniform rollout but as an admin-gated default-off feature, requiring an Owner's decision before any team member can expose their screen to the agent — the same capability, with an entirely different governance architecture appended. Microsoft Autopilot's Entra Agent ID takes the same principle further: the agent does not inherit the user's permissions and act invisibly on their behalf; it authenticates under its own named identity, with its own audit trail, scopeable and blockable by IT independently of the human it serves. Grok Bot 1.2.3's four-tier connector-permission architecture brings the same logic to the action level: rather than a single connector permission that covers read and write equally, users now set per-action rules that distinguish information retrieval from irreversible execution, and the Bot interrupts at the specific boundary of actions it cannot undo. What connects these three advances — Claude's admin gate, Autopilot's agent identity, and Grok Bot's per-action tiers — is a convergence on the same design conclusion: the binary consent model, where a user either trusts the agent or does not, is insufficient for the range of actions that enterprise agents now execute. The industry is converging on graduated trust architectures where the depth of authorisation tracks the irreversibility of the action, the scope of access is independently governable from the act of use, and every agent action leaves a named, auditable record. ChatGPT Space's global Plus expansion and Gemini's history-training split are the user-facing complement: as agents become more capable and more present in professional environments, users simultaneously need more collaborative workspace infrastructure and more granular control over what their agent interactions contribute — to their own history, to model training, and to shared organisational contexts. The industry that began October asking how to build agents is finishing November asking how to govern them.

---

## References

[1] support.claude.com. (2026). *Claude release notes — November 20, 2026*. [https://support.claude.com/en/articles/12138966-release-notes](https://support.claude.com/en/articles/12138966-release-notes)

[2] aiweekly.co. (2026). *Claude Computer Use Beta Lands on Team and Enterprise Plans*. [https://aiweekly.co/alerts/claude-computer-use-beta-lands-on-team-and-enterprise-plans](https://aiweekly.co/alerts/claude-computer-use-beta-lands-on-team-and-enterprise-plans)

[3] cellcog.ai. (2026). *Claude Computer Use Comes to Team and Enterprise Plans*. [https://cellcog.ai/blog/claude-computer-use-team-enterprise/](https://cellcog.ai/blog/claude-computer-use-team-enterprise/)

[4] inoryva.blogspot.com. (2026). *Claude Can Now See Your Work Computer's Screen — If Your Boss Allows It*. [https://inoryva.blogspot.com/2026/11/claude-can-now-see-your-work-computers.html](https://inoryva.blogspot.com/2026/11/claude-can-now-see-your-work-computers.html)

[5] emergent.sh. (2026). *Claude Computer Use Opens to Team and Enterprise Plans*. [https://emergent.sh/news/claude-computer-use-opens-team-enterprise](https://emergent.sh/news/claude-computer-use-opens-team-enterprise)

[6] alphasignal.ai. (2026). *Anthropic Gives Claude Desktop Users Early Access to Fixes Before Stable Rollout*. [https://alphasignal.ai/news/anthropic-gives-claude-desktop-users-early-access-to-fixes-before-stable-rollout](https://alphasignal.ai/news/anthropic-gives-claude-desktop-users-early-access-to-fixes-before-stable-rollout)

[7] support.claude.com. (2026). *Install Claude Desktop — Choose a release channel*. [https://support.claude.com/en/articles/10065433-install-claude-desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)

[8] releasebot.io. (2026). *Claude Updates by Anthropic — November 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[9] help.openai.com. (2026). *ChatGPT release notes — November 2026*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[10] releasebot.io. (2026). *ChatGPT Updates by OpenAI — November 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[11] zeniteq.com. (2026). *OpenAI Rolls ChatGPT Space Out to Plus Worldwide*. [https://www.zeniteq.com/news/openai-rolls-chatgpt-space-out-to-plus-worldwide-dp1bnt](https://www.zeniteq.com/news/openai-rolls-chatgpt-space-out-to-plus-worldwide-dp1bnt)

[12] ctrlmag.com. (2026). *OpenAI Brings ChatGPT Space to Plus Subscribers, Replacing Library With Collaborative AI Pages*. [https://ctrlmag.com/blog/openai-brings-chatgpt-space-to-plus-subscribers-replacing-library-with-collaborative-ai-pages](https://ctrlmag.com/blog/openai-brings-chatgpt-space-to-plus-subscribers-replacing-library-with-collaborative-ai-pages)

[13] emergent.sh. (2026). *ChatGPT for Accounting Launches with Eight Finance Plugins*. [https://emergent.sh/news/chatgpt-accounting-launches-eight-finance](https://emergent.sh/news/chatgpt-accounting-launches-eight-finance)

[14] coinotag.com. (2026). *OpenAI Launches ChatGPT for Accounting With Eight Plugins*. [https://en.coinotag.com/openai-launches-chatgpt-for-accounting](https://en.coinotag.com/openai-launches-chatgpt-for-accounting)

[15] kucoin.com. (2026). *OpenAI Launches Live Dictation for ChatGPT Across All Plans*. [https://www.kucoin.com/news/flash/openai-launches-live-dictation-for-chatgpt-across-all-plans](https://www.kucoin.com/news/flash/openai-launches-live-dictation-for-chatgpt-across-all-plans)

[16] world-today-news.com. (2026). *OpenAI Launches Live Dictation in ChatGPT Removing Ten-Minute Time Limit for All Users*. [https://www.world-today-news.com/openai-launches-live-dictation-in-chatgpt-removing-ten-minute-time-limit-for-all-users/](https://www.world-today-news.com/openai-launches-live-dictation-in-chatgpt-removing-ten-minute-time-limit-for-all-users/)

[17] 9to5google.com. (2026). *Gemini app rolls out very slick camera redesign on Android*. [https://9to5google.com/2026/11/21/gemini-camera-redesign/](https://9to5google.com/2026/11/21/gemini-camera-redesign/)

[18] world-today-news.com. (2026). *Google Introduces New Gemini Camera UI and GIF Creation Feature*. [https://www.world-today-news.com/google-introduces-new-gemini-camera-ui-and-gif-creation-feature/](https://www.world-today-news.com/google-introduces-new-gemini-camera-ui-and-gif-creation-feature/)

[19] blog.google. (2026). *Gemini app updates: New chat history and training controls*. [https://blog.google/innovation-and-ai/products/gemini-app/updated-controls/](https://blog.google/innovation-and-ai/products/gemini-app/updated-controls/)

[20] 9to5google.com. (2026). *New Gemini setting lets you keep chat history, but turn off AI training*. [https://9to5google.com/2026/11/16/gemini-history-ai-training/](https://9to5google.com/2026/11/16/gemini-history-ai-training/)

[21] datastudios.org. (2026). *Gemini lets you keep chat history and turn off AI training*. [https://www.datastudios.org/post/gemini-app-separate-history-and-ai-training-settings-two-month-retention](https://www.datastudios.org/post/gemini-app-separate-history-and-ai-training-settings-two-month-retention)

[22] microsoft.com. (2026). *Copilot at Microsoft Ignite: Expanding what's possible with intelligence built for work*. [https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/](https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/)

[23] emergent.sh. (2026). *Microsoft Copilot Autopilot Launches With Agent Identity*. [https://emergent.sh/news/microsoft-copilot-autopilot-launches-agent](https://emergent.sh/news/microsoft-copilot-autopilot-launches-agent)

[24] openaimaster.ai. (2026). *Copilot Autopilot Explained: Microsoft's Always-On Agent*. [https://openaimaster.ai/copilot-autopilot-explained-microsoft-ignite-2026/](https://openaimaster.ai/copilot-autopilot-explained-microsoft-ignite-2026/)

[25] windowsforum.com. (2026). *Microsoft Copilot Studio Ignite 2026: Agent Accounts, Shared Memory Risks and Governance*. [https://windowsforum.com/news/microsoft-copilot-studio-ignite-2026-agent-accounts-shared-memory-risks-and-governance.453078/](https://windowsforum.com/news/microsoft-copilot-studio-ignite-2026-agent-accounts-shared-memory-risks-and-governance.453078/)

[26] aguidetocloud.com. (2026). *Microsoft Ignite 2026: AI Updates, Explained*. [https://www.aguidetocloud.com/blog/microsoft-ignite-2026-ai-updates/](https://www.aguidetocloud.com/blog/microsoft-ignite-2026-ai-updates/)

[27] releasebot.io. (2026). *Microsoft Copilot Updates — November 2026*. [https://releasebot.io/updates/microsoft/microsoft-copilot](https://releasebot.io/updates/microsoft/microsoft-copilot)

[28] x.ai. (2026). *Grok Bot Changelog v1.2.3*. [https://x.ai/changelog/bot](https://x.ai/changelog/bot)

[29] teslanorth.com. (2026). *Grok Bot Shows How It Can Book Flights and Hotels*. [https://teslanorth.com/2026/11/23/grok-bot-flights-hotels-connector-permissions/](https://teslanorth.com/2026/11/23/grok-bot-flights-hotels-connector-permissions/)

[30] gradually.ai. (2026). *Grok Bot Changelog — November 2026*. [https://www.gradually.ai/en/changelogs/grok-bot/](https://www.gradually.ai/en/changelogs/grok-bot/)

[31] emergent.sh. (2026). *Perplexity Intelligence: New AI Research Platform Launches*. [https://emergent.sh/news/perplexity-intelligence-new-ai-research](https://emergent.sh/news/perplexity-intelligence-new-ai-research)

[32] releasebot.io. (2026). *Perplexity Release Notes — November 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[33] latent.space. (2026). *Perplexity hits a $1B revenue run rate, up 4x in 2026*. [https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/](https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/)