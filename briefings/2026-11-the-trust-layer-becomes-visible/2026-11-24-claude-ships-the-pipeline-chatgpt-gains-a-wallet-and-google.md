# UX Briefing: Claude Ships the Pipeline, ChatGPT Gains a Wallet, and Google Personalises Its Search

**November 24, 2026**

Good morning. The 48 hours ending November 24, 2026 are defined by three simultaneous agentic-authority and trust-design events: **Anthropic** executing a triple-launch on November 23–24 — 

**Claude Ship** launching as a suite of AI agents for automating code reviews, fixes, and approvals of routine code changes

, 

**Skills over MCP** entering public beta so that MCP servers can ship skills alongside their tools

, and 

**Monthly Recap** graduating from beta across Free, Pro, Max, and Ultra plans, now drawing on Claude Code sessions and Cowork tasks in the cloud with recap deletion controls

; **OpenAI** arriving at the same window with **GPT-6.2 Sol reaching the Chat tab** on November 23 — 

the model is optimised for the chat tab for Plus, Pro, Business and Enterprise tiers, is better at knowing when to follow up, and can offer to let users know when a price drops

 — while the previously-launched **ChatGPT Wallet** continues its rollout with 

users adding a card once, then approving each agent-driven checkout with a biometric check such as Face ID, with each approval creating a record of what was authorised

; and **Google** delivering its most consequential personal-data trust-design event of the week on November 23 — 

**AI Mode expanding Personal Intelligence** with integrations for Google Drive, Google Wallet, and the Gemini app

 — following the November 22 iCloud Mail and Calendar plugin addition to ChatGPT. 

**Copilot UX components**, which became generally available with SPFx 1.24, are now supported and available in Copilot Cowork as plugins

, while Perplexity's **Intelligence** platform and **Computer** command panel continue settling into enterprise workflows after their November 22 launches.

---

## At a Glance: November 24 Highlights

Today's window is defined by the category arriving simultaneously at the question of agent authority within workflows: not just whether an agent can perform a task, but how much of the pipeline the agent is permitted to own — from code review to approval, from shopping to checkout, from search context to financial data — and what trust architecture governs each boundary.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Ship launches November 23 in beta for Team and Enterprise GitHub repositories with three agents — Code Review (GA), PR Steward (beta, pushes fixes to failing CI and merge conflicts), and Claude Approvals (beta, applies a team-written YAML policy file and can approve routine PRs without human review); Skills over MCP enters public beta on November 24, letting MCP servers ship domain skills alongside tools, loaded only when Claude needs them, with Intuit and Dropbox as launch partners; Monthly Recap graduates from beta across all plans, adding Claude Code and Cowork activity and deletion controls; Claude Code 2.1.331 ships with Code Mode expanding to Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform** — Claude Approvals' observe-only onboarding mode is the trust-design signal of the window: before any agent is allowed to approve a PR, Anthropic recommends running it in read-only observation mode first, establishing a prove-then-escalate-authority pattern that inverts the default-on assumption. |
| **ChatGPT** | **GPT-6.2 Sol rolls out to the ChatGPT Chat tab on November 23 for Plus, Pro, Business, and Enterprise — tuned for everyday conversation with improved image understanding, instruction following, and proactive follow-up suggestions; ChatGPT Wallet continues its rollout to US Pro subscribers, letting dot agents complete purchases with tokenised payment credentials and mandatory biometric approval for every transaction; iCloud Mail and Calendar plugins connect to ChatGPT for all plans on web, desktop, and iOS** — GPT-6.2 Sol's proactive follow-up pattern — offering a price-drop alert after a shopping conversation — is the most significant interaction-design advance within the Chat tab rollout: a model that knows when to offer a follow-up without being asked is making a claim about the agent's role in the conversation, shifting from reactive responder to anticipatory participant. |
| **Google Gemini** | **AI Mode Personal Intelligence expands on November 23 to Google Wallet (rolling out now), with Google Drive and the Gemini app to follow in coming weeks; Wallet connection is opt-in and read-only — AI Mode can read spending and reward data but cannot move, manage, or invest money; before the Wallet expansion, Personal Intelligence connected Gmail, Calendar, and Google Photos** — the read-only constraint on Wallet access is the trust-design decision that most directly separates Gemini AI Mode's Personal Intelligence from ChatGPT Wallet's agent-payment architecture: Google is building a contextualised understanding of the user's financial life to inform search answers, while OpenAI is building an execution layer where the agent completes transactions. |
| **Microsoft Copilot** | **Copilot UX components reach general availability in Copilot Cowork as plugins on November 24, so declarative agents and their interactive components ship in one SPFx solution; Cowork Projects rolling out in Copilot Chat in November bring related chats, files, and instructions into a persistent shared context; Copilot Notebooks are becoming Copilot Workspaces with live cursors and collaborative file creation** — the Cowork-with-plugins architecture is the developer-UX advance of the Microsoft window: interactive App Blocks — calculators, dashboards, comparisons — that previously required separate deployment now ship with the agent that uses them, collapsing the gap between agent capability and agent interface. |
| **Grok (xAI)** | **Grok Build 1.0.89 (reached broad developer attention this window) remains the latest release, with no new Grok Build release in the November 22–24 window; the Grok Bot 1.2.3 four-tier connector-permission architecture continues its enterprise rollout** — in the absence of new xAI developer tooling in this specific window, the Trust & Safety story for xAI is defined by the ongoing enterprise rollout of Grok Bot 1.2.3's per-action permission model, with its read/write distinction at the connector level establishing the platform's graduated-trust baseline for agentic commerce workflows. |
| **Perplexity** | **Perplexity Intelligence (launched November 22) is settling into enterprise availability combining real-time web retrieval with enhanced multi-step reasoning for finance, legal, healthcare, and academic knowledge workers; Perplexity's Orchestrator API updated its xhigh effort level on November 23 to use GPT-6.2 Sol without a fallback, replacing Claude Opus 5.5; the Computer command panel (accessible via /) and Deep Research in Computer continue rolling out** — the Orchestrator API's model-routing update is the interaction-infrastructure advance that matters most for enterprise workflows built on Perplexity's backend: a change to the xhigh effort level's default model, from Claude Opus 5.5 to GPT-6.2 Sol, is a silent shift in the agent's reasoning substrate that operators who have pinned their workflows to versioned effort configurations must audit. |

---

## Product Highlights

### Claude / Anthropic: Ship Separates Authority from Execution, MCP Gains a Skills Layer

Anthropic's most consequential interaction-design event in this window is **Claude Ship** — a three-agent GitHub workflow suite announced November 23 that moves the agentic-coding category from "AI writes code" to "AI writes, reviews, fixes, and approves code."



Claude Ship separates the power to fix pull requests from the authority to approve them.

It combines Code Review, which is generally available, with two new agents in beta: PR Steward and Claude Approvals.

PR Steward works through failing continuous integration checks, merge conflicts, and review feedback; Claude Approvals can actually approve a PR, applying an approval policy written by the team as a file in the repository.

 The architectural significance of this role separation is structural: PR Steward is explicitly designed never to approve or merge — it can push fixes and comment on what it changed and how to undo it, but the act of approving a merge is reserved for Claude Approvals alone, and Claude Approvals only acts within the bounds of a human-authored YAML policy. 

The company advised caution: "For most customers, we recommend enabling this first in observe-only mode to build confidence before configuring branch protection to require Claude Approvals' green light."



The observe-then-escalate onboarding pattern is the trust-design advance that merits the most attention. 

Admins can enable Code Review and PR Steward for individual repositories, allowing the agents to work on pull requests automatically without developers having to invoke the /ship command; admins can configure the review level, review frequency, and monthly spending limits for Code Review and PR Steward.

Developers can steer or halt PR Steward mid-task using @claude and @claude stop commands.

 This combination — per-repository opt-in, mid-task steering commands, spending caps, and an observe-only approval mode — constitutes the most granular human-in-the-loop architecture for agentic coding workflows that any major platform has shipped, designed for the specific challenge of teams where AI already writes most of the code and the bottleneck has migrated downstream to review and merge.

**Skills over MCP** entering public beta on November 24 is the developer-infrastructure advance that complements Claude Ship. 

With Skills over MCP, servers can publish skills alongside their tools to help Claude take on longer, multi-step work; skills update with the server, so developers can ship tools and guidance together and users have nothing separate to install.

Claude only loads a skill into its context when it actually needs it; Skills over MCP is available in Claude and Claude Code and turned on by default for users on the Pro, Max, and Ultra plans.

Elicitation, now generally available, lets servers pause mid-call to ask users to confirm costly or destructive actions.

 The Elicitation GA is the trust-design detail within the MCP expansion that most directly addresses the agentic-workflow governance problem: a server that can interrupt a long-running task at the moment a consequential action is about to execute — rather than requiring the user to anticipate and pre-approve all such moments in a single upfront consent — establishes a mid-task checkpoint pattern that is architecturally analogous to Claude Approvals' observe mode, applied to the MCP tool layer.

---

### ChatGPT / OpenAI: GPT-6.2 Anticipates the Follow-Up and the Wallet Clears Every Purchase with a Fingerprint

OpenAI's most consequential interaction-design event in this window is a two-track advance: the **GPT-6.2 Sol Chat tab rollout** delivering a new proactive-follow-up interaction pattern to everyday conversation, and **ChatGPT Wallet** establishing the most detailed per-purchase trust architecture in the agent-commerce category.



A version of GPT-6.2, optimised for the chat tab, is rolling out for Plus, Pro, Business and Enterprise tiers.

 The UX significance is in a specific new behaviour: 

compared with GPT-6, GPT-6.2 Sol does a better job detecting fine details in photos, like symbols on a sign or text on a label; it has improved at choosing options online based on the user's priorities, and is smarter about when to offer a follow-up after a conversation, such as an alert about a price drop.

 The proactive follow-up pattern — where the model offers to continue engaging with a task after the user has stopped actively prompting — is the interaction-design shift from reactive assistant to anticipatory agent. A model that knows the conversation about hotels is likely to benefit from a later price check is a model that is beginning to model the user's future intent, not just their current query. 

The model scores higher in teen safety evaluations, with gains in areas like emotional reliance, disordered eating, and dangerous activities; responses met OpenAI's safety policies 91 to 94 percent of the time, up from 77 to 80 percent for GPT-6.

 The safety-compliance improvement is a consequential trust-design signal in its own right: a model that is both more proactively engaged and more reliably policy-compliant is addressing the core tension in conversational AI design — agents that anticipate user needs are more useful but also more capable of overstepping.

**ChatGPT Wallet**, which launched November 13 and is continuing its rollout, is the agentic-commerce trust-design event of the broader two-week window. 

Users add a card once, then ask their dot to help find something to buy; when it is time to check out, they are shown the merchant, the items, the total, and the selected card, and must approve the transaction with a biometric check such as Face ID or a fingerprint scan; each approval creates a record of what the user authorised the agent to buy.

When it is time to transact, ChatGPT's Wallet charges the selected card using a payment token, a substitute for the user's actual card details, so that information is not shared with either the dot or the merchant.

 The tokenisation-plus-biometric architecture is the trust-design pattern that makes agent-driven commerce governable: the agent never sees the real card number, the merchant never sees it either, and each transaction requires an explicit biometric confirmation that creates an auditable record. 

In the future, the company plans to offer users more control by allowing them to set spending limits or configure parameters around purchase categories or time periods, so they can pre-approve purchases that their agent can then handle more autonomously.

 This roadmap disclosure is itself a trust-design signal: by naming the future capability (pre-approved spending envelopes) before it ships, OpenAI is communicating the direction of travel and giving users the opportunity to form expectations about what the agent will eventually be able to do without per-transaction confirmation.

---

### Google Gemini: AI Mode Connects the Wallet, But Only to Read

Google's most consequential interaction-design event in this window is the **AI Mode Personal Intelligence expansion** to Google Wallet, Drive, and the Gemini app — the most significant broadening of the contextual-data layer available to Google's AI search surface since Personal Intelligence launched.



Google announced on Monday that it is expanding Personal Intelligence in Search's AI Mode with integrations for Google Drive, Google Wallet, and the Gemini app; Personal Intelligence is designed to offer users more personalised, context-aware answers by connecting to their Google apps; the feature can already connect to Gmail, Google Calendar, and Google Photos.

Robby Stein, VP of Product for Google Search, wrote on November 23, 2026 that Google Wallet can be connected to Personal Intelligence in AI Mode starting that day.

 The trust-design constraint that Google built into the launch is the read-only boundary: 

AI Mode can only read information from financial accounts and cannot "move, manage, or invest" money.

 This constraint directly distinguishes the Google architecture from ChatGPT Wallet's execution model: Google is using financial data to make search answers more personally relevant, while OpenAI's agents complete transactions. Both are consequential agentic-finance advances; they represent opposite ends of the read/act spectrum on financial data.



Before the November 23 announcement, Personal Intelligence in AI Mode supported Google Photos and Workspace — Gmail and Calendar; the new Google Drive support lets AI Mode take into account Docs, Sheets, and PDFs.

 The Drive integration is the contextual-grounding advance that matters most for knowledge-worker UX: a search surface that can contextualise an answer against a user's own documents — without the user having to attach the document, copy its contents, or switch to a separate AI surface — collapses the gap between "search the web" and "search my work." 

The last integration is the most interesting: users will be able to securely connect the Gemini app to Personal Intelligence in AI Mode, building on the existing ability to have the Gemini app factor Search history into answers.

 The Gemini-app-to-AI-Mode bridge is the cross-surface personalisation advance that the category has been building toward: a user's conversational history with Gemini becoming context for their search results is the beginning of a persistent-agent-informs-search architecture where the agent's accumulated knowledge of the user shapes every query surface, not just the chat interface.

---

### Microsoft Copilot: UX Components Land in Cowork, Workspaces Replace Notebooks

Microsoft's most consequential interaction-design event settling into broad availability in this window is the **Copilot UX components general availability in Cowork with plugins** — the developer-infrastructure advance that closes the gap between agent capability and agent interface in the SharePoint Framework ecosystem.



Copilot UX components are now supported and available in Copilot Cowork as plugins; at GA, a declarative agent and its Copilot UX components ship together in one SPFx solution.

Copilot UX components are now supported and available in Copilot Cowork as plugins, governed centrally with the admin tools you already use.

 The architectural significance is in the bundle: an agent that previously required developers to deploy its conversational layer and its interactive UI components separately now ships them as a single artefact, with admin governance applying to both simultaneously. 

App Blocks are interactive experiences that appear inside a Copilot Chat conversation; Microsoft gives examples including calculators, dashboards, planners, and comparison tools.

 This is the generative-UI pattern — interactive components that appear in the conversation at the moment they are needed, rather than requiring the user to navigate to a separate application — applied to the enterprise Copilot surface at GA scale.



Copilot Notebooks are becoming Copilot Workspaces; a workspace is a shared space where a team and Copilot work on the same ongoing project, with live cursors so users can see who is working where; existing notebooks will convert automatically.

 The live-cursor addition is the collaborative-workspace UX advance: when a human and an agent are working in the same document, and other humans can see both the human edits and the agent's cursor, the agent becomes a legible collaborator rather than an invisible background processor. 

Projects keep related conversations, Cowork tasks, instructions, and files together; instead of explaining the background from the beginning each time, users can start a new piece of work with the project's available context; an Outputs view gathers files produced by its tasks; projects are private to the individual creator.

 The Outputs view is the agentic-workflow management advance within Projects: when all files produced by a multi-step task are collected in a single view, users have a natural audit point for reviewing everything the agent generated without tracing back through individual conversation turns.

---

### Grok (xAI): Bot 1.2.3 Permission Architecture Continues Its Enterprise Rollout

xAI's interaction-design story in this specific 48-hour window is defined not by new releases but by the continued enterprise rollout of **Grok Bot 1.2.3**'s four-tier connector-permission architecture — the most granular per-action governance model in the agent-connector category.



The latest Grok Build release remains version 1.0.89 from November 17, 2026

, with no new Build release in the November 22–24 window. The xAI developer-tooling story this window is therefore the enterprise-adoption phase for the trust-design advances that shipped last week. 

When it is time to check out in an agent commerce scenario, users are shown the merchant, the items, the total, and the selected card, and must approve the transaction with a biometric check such as Face ID or a fingerprint scan

 — a pattern that the Grok Bot 1.2.3 approval-card architecture also implements for irreversible actions in connected apps, establishing that biometric-at-irreversibility is the interaction pattern the whole category is converging on for agentic commerce.

The absence of new xAI releases in this window is itself a signal worth noting in the context of the broader industry movement: on the same day Anthropic ships a three-agent PR-approval workflow and Google expands AI Mode to read financial data, xAI's developer surface is in a consolidation phase after the significant Grok Bot 1.2.3 permission-architecture launch. The industry signal is that the trust-design patterns — per-action tiers, biometric approval at irreversibility boundaries, read-only constraints on financial data — are now shipping faster than any single platform can iterate on them, and the platforms that pause to let adoption catch up with capability are making a deliberate architectural choice.

---

### Perplexity: Intelligence Embeds, the Orchestrator Swaps Its Flagship Model, and Computer Matures

Perplexity's most significant interaction-design event in this window is the continued enterprise embedding of **Intelligence** alongside a consequential **Orchestrator API model-routing update** that operators running versioned workflows must actively audit.



The xhigh effort level now selects xhigh@2026-11-18.0, which uses openai/gpt-6.2-sol without a fallback model, replacing Claude Opus 5.5 and its GPT-6.1 Sol fallback.

 This is the kind of silent infrastructure change that has the largest UX impact on enterprise workflows: a change to the default model at a named effort level is not surfaced to end users, who experience it as a behavioural shift in the agent's reasoning without any interface indication that the underlying model has changed. 

Earlier pinned versions remain unchanged; operators can pin xhigh@2026-11-11.0 to keep the previous model configuration.

 The pinning mechanism is the trust-design affordance that Perplexity offers for this scenario — but it requires operators to know to look for a version change and to understand that the default has moved, placing the audit burden on the operator rather than surfacing the model transition proactively.



Perplexity's Computer update adds Deep Research in Computer, a new command panel, forking, improved inline confirmations, and enterprise controls including a Computer Analytics API and custom credit limits.

The new Computer command panel is a single place to discover and access everything Computer can do; the panel includes built-in modes like Deep Research and Plan Mode, alongside all available skills from the user, their space, and their organisation; to get started, users type / in the search box while in Computer mode.

 The command panel is the navigability-UX advance that most directly addresses the discoverability problem in Computer: an agent surface with 20+ models, multiple built-in modes, custom user skills, space skills, and organisation skills is an agent surface where the breadth of available capability is invisible to users who have not explored the full interface. The / command panel collapses the full capability map into a single keyboard-accessible menu, transforming capability discovery from spatial navigation to search. 

Deep Research can use Computer's tools to browse the web, work with Connectors and skills, and run applications to create files; users can continue working after their research is complete — for example, asking Computer to turn a report into a slide deck in the same session.

 The same-session continuation pattern — research that flows directly into artifact creation without a context switch — is the agentic-workflow advance that most clearly establishes Computer as a workspace rather than a query interface.

---

## The Bigger Picture: Claude Ships the Pipeline, ChatGPT Gains a Wallet, and Google Personalises Its Search

The 48 hours ending November 24, 2026 crystallise a single macro movement that has been building across the month: **the AI agent category is completing its migration from task execution to pipeline ownership, and the trust-design decisions that defined this window are all answers to the same underlying question — at which moment in a consequential workflow should the agent act autonomously, and at which moment should it stop and ask?** Claude Ship's three-agent architecture gives the clearest structural answer: Code Review observes and reports, PR Steward fixes but cannot approve, Claude Approvals authorises but only within a human-written policy, and all three start in the least-privileged mode available before escalating. ChatGPT Wallet applies the same logic to commerce: the agent shops but cannot pay, payment requires a biometric that creates a record, and the roadmap points toward spending-envelope delegation only after per-transaction trust is established. Google AI Mode's read-only Wallet constraint makes the same claim from the opposite direction: financial context can flow into the agent's reasoning layer, but the execution layer — moving money — is explicitly withheld. Anthropic's Skills over MCP Elicitation general availability adds the same pattern at the tool layer: an MCP server can pause mid-task to ask a user to confirm a costly or destructive action, establishing a mid-workflow consent checkpoint that did not previously exist in the protocol. What connects all four advances — Claude Approvals' policy file, ChatGPT Wallet's per-purchase biometric, Google's read-only financial constraint, and MCP Elicitation's mid-task interrupt — is the same design conclusion the industry has been arriving at across this entire month: graduated authority is the trust architecture for the agentic era, where every capability the agent gains is paired with a corresponding constraint on when it may exercise that capability without human confirmation. The platforms that ship graduated authority as a first-class design primitive — not as a safeguard bolted onto an otherwise unrestricted agent — are the platforms whose users will be willing to delegate the most. November 2026 is the month the category learned to stop asking "what can the agent do?" and start asking "what should the agent be allowed to do without asking first?"

---

## References

[1] gradually.ai. (2026). *Claude Code Changelog (November 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[2] samonai.substack.com. (2026). *AI Brief – November 24, 2026*. [https://samonai.substack.com/p/ai-brief-november-24-2026](https://samonai.substack.com/p/ai-brief-november-24-2026)

[3] releasebot.io. (2026). *Claude Updates by Anthropic – November 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[4] releasebot.io. (2026). *Claude Code Updates by Anthropic – November 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[5] support.claude.com. (2026). *Release notes – November 24, 2026*. [https://support.claude.com/en/articles/12138966-release-notes](https://support.claude.com/en/articles/12138966-release-notes)

[6] techcrunch.com. (2026). *Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes*. [https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)

[7] helpnetsecurity.com. (2026). *Claude Ship gives AI a seat on both sides of code review*. [https://www.helpnetsecurity.com/2026/11/24/anthropic-claude-ship-beta/](https://www.helpnetsecurity.com/2026/11/24/anthropic-claude-ship-beta/)

[8] unite.ai. (2026). *Anthropic Launches Claude Ship to Review, Fix and Approve PRs*. [https://www.unite.ai/anthropic-launches-claude-ship-to-review-fix-and-approve-prs/](https://www.unite.ai/anthropic-launches-claude-ship-to-review-fix-and-approve-prs/)

[9] theregister.com. (2026). *Claude Ship puts AI at the helm of pull request approvals*. [https://www.theregister.com/ai-and-ml/2026/11/24/claude-ship-puts-ai-at-the-helm-of-pull-request-approvals/5311883](https://www.theregister.com/ai-and-ml/2026/11/24/claude-ship-puts-ai-at-the-helm-of-pull-request-approvals/5311883)

[10] emergent.sh. (2026). *Claude Ship Launches: Three-Agent PR Review System*. [https://emergent.sh/news/claude-ship-launches-three-agent-pr-review](https://emergent.sh/news/claude-ship-launches-three-agent-pr-review)

[11] munderdiffl.in. (2026). *What is Claude Ship? Anthropic's pull request agents*. [https://munderdiffl.in/blog/what-is-claude-ship/](https://munderdiffl.in/blog/what-is-claude-ship/)

[12] claude.com. (2026). *MCP servers can now ship skills, run tasks, and more with Claude*. [https://claude.com/resources/articles/skills-over-mcp-tasks-and-more](https://claude.com/resources/articles/skills-over-mcp-tasks-and-more)

[13] thenewstack.io. (2026). *As MCP turns two, Claude gets Skills over MCP and better support for long-running tasks*. [https://thenewstack.io/mcp-skills-tasks-claude/](https://thenewstack.io/mcp-skills-tasks-claude/)

[14] unite.ai. (2026). *Anthropic Brings Server-Supplied Skills and Background Tasks to Claude*. [https://www.unite.ai/anthropic-brings-server-supplied-skills-and-background-tasks-to-claude/](https://www.unite.ai/anthropic-brings-server-supplied-skills-and-background-tasks-to-claude/)

[15] alphasignal.ai. (2026). *Anthropic Expands MCP With Skills, Background Tasks, and Direct File Transfers*. [https://alphasignal.ai/news/anthropic-expands-mcp-with-skills-background-tasks-and-direct-file-transfers](https://alphasignal.ai/news/anthropic-expands-mcp-with-skills-background-tasks-and-direct-file-transfers)

[16] help.openai.com. (2026). *ChatGPT release notes – November 23, 2026*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[17] releasebot.io. (2026). *ChatGPT Updates by OpenAI – November 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[18] macrumors.com. (2026). *OpenAI Brings GPT-6.2 Sol to ChatGPT's Chat Tab*. [https://www.macrumors.com/2026/11/23/openai-gpt-6-2-sol-chatgpt/](https://www.macrumors.com/2026/11/23/openai-gpt-6-2-sol-chatgpt/)

[19] gsmarena.com. (2026). *ChatGPT Wallet lets OpenAI's agents buy things for you*. [https://www.gsmarena.com/chatgpt_wallet_lets_openais_agents_buy_things_for_you-news-75481.php](https://www.gsmarena.com/chatgpt_wallet_lets_openais_agents_buy_things_for_you-news-75481.php)

[20] techcrunch.com. (2026). *ChatGPT's new Wallet lets AI agents shop and check out for you*. [https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/](https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/)

[21] cryptobriefing.com. (2026). *OpenAI introduces ChatGPT wallet for Pro subscribers*. [https://cryptobriefing.com/openai-chatgpt-wallet-pro-subscribers/](https://cryptobriefing.com/openai-chatgpt-wallet-pro-subscribers/)

[22] iclarified.com. (2026). *OpenAI Introduces ChatGPT Wallet With Face ID Approval for Agent Purchases*. [https://www.iclarified.com/103506/openai-introduces-chatgpt-wallet-with-face-id-approval-for-agent-purchases](https://www.iclarified.com/103506/openai-introduces-chatgpt-wallet-with-face-id-approval-for-agent-purchases)

[23] techcrunch.com. (2026). *Google Search's AI Mode can now tap into Drive and Wallet for more personalized responses*. [https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/](https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/)

[24] 9to5google.com. (2026). *AI Mode adding Google Drive, Wallet, & Gemini app integration*. [https://9to5google.com/2026/11/23/ai-mode-wallet-gemini/](https://9to5google.com/2026/11/23/ai-mode-wallet-gemini/)

[25] relevantaudience.com. (2026). *Google adds Wallet and Drive to AI Mode personalisation*. [https://www.relevantaudience.com/ai/google-wallet-drive-gemini-personal-intelligence-ai-mode/](https://www.relevantaudience.com/ai/google-wallet-drive-gemini-personal-intelligence-ai-mode/)

[26] fourweekmba.com. (2026). *Google AI Mode Adds Wallet, Its 4th Personal Data Source*. [https://fourweekmba.com/ai-google-ai-mode-adds-wallet-its-4th-personal-data-source/](https://fourweekmba.com/ai-google-ai-mode-adds-wallet-its-4th-personal-data-source/)

[27] etvbharat.com. (2026). *Google AI Mode Can Now Use Drive And Wallet For More Personal Answers*. [https://www.etvbharat.com/en/technology/google-ai-mode-search-google-drive-google-wallet-personal-intelligence-gemini-app-enn26112406804](https://www.etvbharat.com/en/technology/google-ai-mode-search-google-drive-google-wallet-personal-intelligence-gemini-app-enn26112406804)

[28] devblogs.microsoft.com. (2026). *Copilot UX components now available in Cowork with plugins – SPFx roadmap update for November 2026*. [https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-now-available-in-cowork-with-plugins-spfx-roadmap-update-for-november-2026/](https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-now-available-in-cowork-with-plugins-spfx-roadmap-update-for-november-2026/)

[29] changingsocial.com. (2026). *What's new in Microsoft Copilot – November 2026*. [https://www.changingsocial.com/blog/whats-new-in-microsoft-copilot-november-2026/](https://www.changingsocial.com/blog/whats-new-in-microsoft-copilot-november-2026/)

[30] aguidetocloud.com. (2026). *What's New in Microsoft 365 Copilot: November 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-november-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-november-2026-updates/)

[31] x.ai. (2026). *Grok Build Changelog*. [https://x.ai/changelog/build](https://x.ai/changelog/build)

[32] docs.perplexity.ai. (2026). *Changelog – November 2026*. [https://docs.perplexity.ai/changelog/changelog](https://docs.perplexity.ai/changelog/changelog)

[33] releasebot.io. (2026). *Perplexity Release Notes – November 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[34] perplexity.ai. (2026). *Deep Research and Model Council in Computer*. [https://www.perplexity.ai/help-center/en/articles/2026102603-deep-research-and-model-council-in-computer](https://www.perplexity.ai/help-center/en/articles/2026102603-deep-research-and-model-council-in-computer)