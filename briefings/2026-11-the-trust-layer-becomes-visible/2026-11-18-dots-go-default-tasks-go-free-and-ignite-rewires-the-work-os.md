# UX Briefing: Dots Go Default, Tasks Go Free, and Ignite Rewires the Work OS

**November 18, 2026**

Good morning. The 48 hours ending November 18, 2026 are defined by four simultaneous design movements: **OpenAI** executing the most consequential enterprise-deployment governance event in dots' short history — the **Dots Enterprise default-on rollout** lands today, November 18, flipping from opt-in to available-by-default for every eligible ChatGPT Enterprise, Edu, and Healthcare workspace, while simultaneously launching **ChatGPT for Sales** on November 17 as the platform's first domain-specialised agentic workspace, integrating Salesforce, HubSpot, and 30+ partner plugins directly into ChatGPT Work through a dedicated Sales plugin; **Google** delivering the most consequential agentic democratisation event of the November cycle on November 17 — **Gemini Tasks goes free** in six countries on the new Gemini 4 Hydrogen model, adding Google Pay checkout via a user-set spending cap, agentic phone calls to US businesses, and SMS/email task-creation entry points, transforming a formerly $19.99/month Pro feature into free infrastructure for hundreds of millions of users; **Microsoft Copilot** completing its **Ignite 2026 Day 1** arc on November 17 — Autopilot and Copilot Workspaces both reach Frontier customers, Copilot Code reaches Frontier with GA targeted for December, and the **Home** surface unifying Chat and Cowork rolls out worldwide, with Agent 365 Cost Management and Business Analytics launching as the financial-governance layer for the agentic estate; and **Anthropic** shipping **Claude Code 2.1.327** on November 17 with a critical permission-prompt visibility fix and a GitHub App installation confirmation gate, while simultaneously publishing its updated coordinated vulnerability disclosure policy cutting the high/critical-severity disclosure window from 90 days to 30 — the fastest AI-driven governance adaptation in the industry's history. **Perplexity** simultaneously launched **Multiagent** on November 17 — a new top effort level for Computer and Teammates in which a lead agent coordinates up to 16 parallel sub-agents across Claude, GPT, and Gemini models, with cross-checking before synthesis — and the **Orchestrator API**, making the multi-model routing infrastructure available to developers on a single billing contract.

---

## At a Glance: November 18 Highlights

Today's window is defined by the industry arriving simultaneously at the mass-deployment moment for persistent agentic systems — dots turning on by default for every ChatGPT Enterprise workspace, Gemini Tasks dropping its paywall across six countries, Autopilot rolling to Frontier, and Perplexity's Multiagent coordinating up to 16 sub-agents — while the design challenge shifts from "how do we build agent trust primitives" to "how do we govern and audit agents already running at scale across millions of enterprise users."

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code 2.1.327 (November 17) adds a confirmation gate before /install-github-app can modify a repository, fixes the VSCode permission-prompt bug where PreToolUse hook denial reasons were invisible to users, and fixes a Code Mode script receiving permission prompts for a second auto-allowed script's actions; Anthropic publishes its updated coordinated vulnerability disclosure policy (November 16), cutting the high/critical-severity window from 90 days to 30 and the non-critical window from the prior 90 to 45, effective January 1, 2027; Claude Code 2.1.328 (November 18) adds SDK fields for startup, handoff, permission, and memory events and an opt-in shell working-directory frame** — the GitHub App confirmation gate in 2.1.327 is the trust-design advance of the window: it inserts a mandatory human-review step at the precise moment an agentic coding session crosses from local file manipulation into repository-level infrastructure changes, enforcing a co-signed-action model at the boundary between ephemeral and persistent consequences. |
| **ChatGPT** | **Dots become available by default in eligible ChatGPT Enterprise, Edu, and Healthcare workspaces today, November 18 — the admin preview ends, every member receives access unless the workspace opts out, and billing for enabled dots begins; ChatGPT for Sales launches November 17 with a dedicated Sales plugin for ChatGPT Work connecting to Salesforce, HubSpot, and 30+ partner tools covering CRM records, meeting intelligence, document creation, and contracts; a minor ChatGPT/OpenAI disruption was reported by some users early morning Eastern time November 18** — the dots default-on flip is the enterprise-governance inflection of the window: agents that required deliberate opt-in for two weeks now require deliberate opt-out, shifting the burden of governance from "enable the agent" to "contain the agent." |
| **Google Gemini** | **Gemini Tasks goes free for hundreds of millions of users in the US, Japan, Korea, Canada, Australia, and India on November 17, running on Gemini 4 Hydrogen; US-only additions include Google Pay checkout within a user-set spending cap with per-purchase tap approval, agentic calls to local businesses, and task creation by forwarding a text message or email; Tasks run inside a hardware-isolated virtual machine; Google also confirms a Gemini Live upgrade coming soon to Home speakers and displays, moving to a speech-to-speech architecture with smart home action support mid-session** — the removal of the paywall from Tasks is the agentic-reach event of the window: an agent capability that required a $19.99/month subscription is now available to free-tier users across six countries, making the spending-cap-and-approval-gate checkout pattern a mass-market interaction design rather than a premium feature. |
| **Microsoft Copilot** | **Ignite Day 1 (November 17): Autopilot and Copilot Workspaces reach Frontier customers — Autopilot is a long-running personal agent with its own Entra Agent ID, memory, tool access, and a named manager, colleague @-mentionable in Teams; Workspaces is the shared canvas for people and agents with persistent context, evolving from Copilot Notebooks; Copilot Code (apps from natural language) is in Frontier now, GA in December; Home merges Chat and Cowork into a single composer and rolls out worldwide; Agent 365 Cost Management and Business Analytics launch as the enterprise spend-and-outcome observability layer; Copilot on Windows gains file find/move/rename and PC troubleshooting from plain-language requests on Copilot+ PCs; Windows gains tighter controls for AI agents and Microsoft Defender now scans local AI coding tools for malicious instructions** — Autopilot's Entra Agent ID architecture is the trust-design signal of Ignite Day 1: by giving the persistent agent its own identity, its own manager, and an audit trail visible in Agent 365, Microsoft is making every Autopilot action attributable and governable before the agent ships broadly, not after. |
| **Grok (xAI)** | **Grok Bot 1.0 (released November 11, reaching broad deployment this window) brings shared Team Bots to Slack and Microsoft Teams and adds Bot participation in Google Meet, Zoom, and Teams video calls; Bots can now proactively recognize and offer work, follow up on unfinished tasks, and anticipate team needs; a Bot learns from every colleague it works with, with new knowledge waiting for owner or Manager approval before changing the Bot for the whole team; Bot analytics and settings pages allow admins to manage what a Team Bot knows and how it is used; Grok Build 1.0.75 and 1.0.77 remain the latest tracked agentic coding releases in this window** — the per-learning-approval governance design in Grok Bot 1.0 is the trust-design detail that makes multiplayer agents tractable: when a Bot learns from individual colleagues, that knowledge cannot propagate to the whole team without explicit manager approval, preventing one person's correction or instruction from silently reshaping a shared agent. |
| **Perplexity** | **Perplexity Multiagent launches November 17 as the new top effort level in Computer and Teammates: a lead agent (default: Claude Fable 5.2) assigns work to up to 16 supporting agents across frontier models including Claude Opus 5.5, GPT 6.1 Sol, and Gemini 4 Carbon, which share findings directly and cross-check each other before the lead synthesises a single output; users select Multiagent from Computer's effort slider and can name their preferred models; Perplexity Orchestrator also launches November 17 as a unified API giving developers access to frontier and open-weight models with single-contract billing and automatic same-model failover; both are available to Max subscribers on the web** — Multiagent's cross-checking-before-synthesis architecture is the trust-design advance in multi-agent coordination: rather than a lead agent accepting sub-agent outputs at face value, sub-agents share findings and flag discrepancies before the lead synthesises, embedding a peer-review step into the agent loop itself. |

---

## Product Highlights

### ChatGPT / OpenAI: Dots Go Default and Sales Gets Its Own Workspace

OpenAI's most consequential interaction-design and governance event in this window is not a new feature but a default change: **Dots Enterprise default-on** taking effect today, November 18 — the moment when the persistent-agent capability that has been in admin preview since November 4 becomes available to every member of every eligible ChatGPT Enterprise, Edu, and Healthcare workspace, unless the workspace administrator has explicitly opted out.



Dots become available by default on November 18, 2026, in eligible ChatGPT Enterprise workspaces unless an admin opts out.

Admin preview ends on November 18, and dots become available by default in eligible ChatGPT Enterprise workspaces unless an admin opts out; dots are free to try until January 13, 2027, but the dot's tier is visible in ChatGPT with comparison across Standard, Advanced, and Expert.

 The governance-design significance of the default-on flip is structural: for the two weeks of the admin preview, dots required deliberate action to enable — an administrator had to opt in on behalf of their workspace. After today, the direction of governance is reversed: a workspace that has taken no action now has persistent agents active for every member, and containment requires deliberate opt-out. 

During admin preview, dots are off by default; the preview runs until November 18, 2026, when dots become available by default unless the workspace admin opts out; workspace admins can enable access during the preview.

The "Use custom rules for dots" setting allows members to add or edit rules that guide their dot's actions and confirmations, and is off by default for Enterprise.

 This layered permission architecture — workspace-level access control, role-based targeting, Slack connectivity as a separate opt-in, custom rules as a separate opt-in — reflects the correct trust-design direction for deploying persistent agents at enterprise scale: each capability that expands the agent's reach or authority requires its own consent gate, independent of the master access toggle.

**ChatGPT for Sales**, launched November 17, is the platform's first domain-specialised agentic workspace — an interaction-architecture decision that has significant UX implications beyond its immediate utility. 

OpenAI launched ChatGPT for Sales on November 17, 2026: a new Sales plugin and more than 30 new and enhanced partner plugins that bring a seller's tools and customer context into ChatGPT.

The Salesforce connection runs through OpenAI's Salesforce plugin, which includes Salesforce's Agentforce Sales app and can read and write records, including reviewing records, summarising pipeline risk, and preparing follow-ups and CRM updates.

ChatGPT Business and Enterprise administrators can enable the Sales plugin and chosen partner plugins from the admin console, through workspace Plugins controls.

 The domain-workspace model — a Sales plugin that surfaces sales-specific tools and CRM context within the ChatGPT Work conversation — is a consequential shift from a generic AI assistant to a contextually pre-loaded specialist: the agent knows the user is in a sales context before they ask, the tools available are pre-scoped to sales workflows, and the data surfaces are pre-connected to the CRM systems the work depends on. This is the specialised-workspace pattern that agentic UX has been moving toward, and ChatGPT for Sales is its most fully realised expression in the OpenAI product family to date.

---

### Google Gemini: Tasks Drops Its Paywall and Checkout Becomes a Mass-Market Pattern

Google's most consequential interaction-design event in this window is the **Gemini Tasks free rollout** on November 17 — the removal of the $19.99/month subscription requirement that had previously gated one of the most capable agentic surfaces in the consumer AI category, making the spend-cap, background-execution, and approval-gate interaction pattern available to hundreds of millions of users.



Google has made Tasks in Gemini free of charge in six countries and given it new powers in the US; Gemini can now call local businesses, pay through Google Pay within a cap the user sets, take texts and act on forwarded emails; Josh Woodward, who leads the Gemini app, announced it at 17:00 UTC on November 17, 2026.

Previously, users needed a Google AI Pro or Ultra subscription to use these features.

 The paywall removal is the interaction-design event that matters: the spend-cap-and-approval checkout pattern that was previously a premium UX primitive is now a mass-market one. Every design decision embedded in that pattern — how users set spending ceilings, how the agent surfaces an itemised review before purchase, how the tap-and-device approval gate works — now becomes interaction infrastructure for free-tier users across six countries.



Shopping tasks now support Google Pay checkout; users can set a spending ceiling and ask Gemini to monitor price reductions or restocked items, or reorder household supplies; Gemini prepares a checkout within that limit and provides an itemised review before purchase; payment requires explicit approval through a tap and device confirmation.

 The two-track approval model — a standing spending cap the user sets in advance, combined with a per-purchase itemised review and tap approval at the moment of commitment — is a nuanced trust architecture: the spending cap is a pre-authorised envelope (the user has decided in advance what category of purchase is acceptable), while the per-purchase review gate is a moment-of-consequence check (the agent cannot transact without an approval at the exact moment it is ready to pay). 

Tasks run in a hardware-isolated virtual machine that keeps credentials and cloud keys outside the guest environment.

Google Messages and iMessage can now serve as entry points for Tasks after phone verification; texting is rolling out in English to US users aged 18 or older who have personal Google accounts, a verified US number and a supported carrier.

 The SMS entry point is the interaction-pattern advance that has the most significant long-term UX implications: a user can initiate an agentic task by forwarding a text message to Gemini, eliminating the requirement to open an app as the task-creation surface. When the entry point is a text message, the agent's presence collapses into the user's existing communication channel — establishing ambient task delegation as a pattern rather than a deliberate app-switching workflow. 

Alongside the broader update, Google also announced a "faster and more natural" Gemini Live upgrade for Home speakers and displays, moving to the latest speech-to-speech architecture with significantly faster response times, and adding support for smart home controls and timer-setting actions without leaving a Live session.



---

### Microsoft Copilot: Autopilot's Entra Identity and the Governance Architecture That Ships With the Agent

Microsoft's most consequential interaction-design and enterprise-governance event in this window is **Ignite Day 1** delivering on the most-watched agentic announcement of the November cycle — **Autopilot** and **Copilot Workspaces** both reaching Frontier customers on November 17, with Copilot Code following in December, and the entire surface being re-framed as "the new OS for work."



At Ignite on November 17, 2026, Satya Nadella introduced a rebuilt Microsoft Copilot with Workspaces, Autopilot and Copilot Code; Workspaces and Autopilot reach Frontier customers now, and Copilot Code is due for general availability in December.

Autopilot is a long-running agent for personal productivity; according to the Book of News, it has its own identity, memory, and tool access inside the tenant; colleagues can @mention a person's Autopilot in Teams; its actions are tied to its own agent ID and visible to admins; it is rolling out through the Frontier program, not general release.

 The Entra Agent ID architecture is the trust-design advance that distinguishes Autopilot from prior agentic features: a persistent agent operating under a named identity that colleagues can address, whose actions are attributable in Agent 365, and whose access is scoped by an assigned manager — this is the identity-and-accountability substrate that enterprise IT teams require before deploying autonomous agents in production workflows.



Copilot Workspaces is a shared space in the Copilot app where people, their agents and other people work toward a common goal with shared context, available now in the Frontier program.

The average worker's day will begin in "Home," the new user interface for Copilot, which merges traditional chat with a portal called Cowork where people can start delegating different tasks to AI agents; Spataro said Home is like a grounding anchor where workers can log in each day to pick up where they left off.

 The Home surface unifying Chat and Cowork is the interaction-architecture change that matters most for everyday Copilot users: the prior separation of a chat interface and a delegation interface forced a context switch between asking and doing; Home collapses them into a single composer, allowing the same session to transition from conversational query to delegated task without changing surfaces.



On the administration side, Microsoft announced Agent 365 Cost Management, a central view of usage-based AI spending with limits and alerts, and Agent 365 Business Analytics, which measures completed work against cost; Agent 365 already manages more than 50 million agents, and nearly 80 percent of Fortune 500 companies use Copilot Cowork.

Windows gets tighter controls for AI agents, and Microsoft Defender now scans local AI coding tools like Claude Code and GitHub Copilot CLI for hidden malicious instructions.

 The pairing of Agent 365 Cost Management and Business Analytics is the governance-UX advance that speaks most directly to enterprise decision-makers: rather than presenting AI agent costs as a line item divorced from outcomes, the two surfaces together ask "what did you spend on agents, and what did those agents complete?" — establishing a bidirectional accountability relationship between agent expenditure and agent output at the tenant level.

---

### Claude / Anthropic: The GitHub App Gate, the VSCode Permission Visibility Fix, and the 30-Day Disclosure Clock

Anthropic's most consequential interaction-design events in this window are a cluster: **Claude Code 2.1.327** ships on November 17 with two trust-design fixes that address different sides of the agentic permission gap, while the new coordinated vulnerability disclosure policy establishes a governance accelerant driven by AI's own discovery speed.



Claude Code 2.1.327 added a confirmation before /install-github-app changes a repository; it also fixed the VSCode permission prompt not showing the reason that a PreToolUse hook gives when it asks for confirmation.

 These two fixes address different trust-design problems. The GitHub App confirmation gate inserts a mandatory review moment at the precise point where an agentic coding session crosses from local file changes into repository-level infrastructure modifications — a consequential boundary because installing a GitHub App can grant an agent persistent access to a repository that survives the current session. 

Claude Code 2.1.327 also fixed a running Code Mode script in auto mode getting permission prompts and denials once Claude started a second script that also ran in auto mode.

 The VSCode hook-reason visibility fix addresses a subtler trust-design failure: a PreToolUse hook that provides a denial reason but whose reason is invisible to the user in the IDE means the user sees a permission refusal without understanding why the safety mechanism fired, removing the ability to make an informed decision about whether to override or accept the denial. 

Claude Code 2.1.328, also reaching developer tooling on November 18, adds the opt-in shell working-directory frame and models additional fields in startup, handoff, permission, and memory events in the SDK.



Anthropic's **updated coordinated vulnerability disclosure policy** is the trust-design governance event of the window for the agentic security ecosystem. 

Anthropic is shortening the disclosure window from 90 days to 30 days for high and critical vulnerabilities; Anthropic stated that traditional disclosure norms, which assumed slow human-paced remediation, are no longer sufficient because AI models can now rapidly identify and rediscover bugs.

Under the new guidelines, non-critical issues will have a 45-day window, and the company will escalate unresponsive reports to external coordinators after 15 days.

 The rationale is a consequential interaction-design signal in its own right: when Claude-class models can rediscover independently reported vulnerabilities, the safety window between private disclosure and public exploit is compressed by AI capability itself. 

The new policy does not apply to AI-discovered findings that have not received human review, such as findings from Anthropic's OSS Scanner; on November 13, 2026, Google Project Zero also scrapped its long-standing "90 + 30" policy and replaced it with a 30-day clock of its own.

 The simultaneous convergence of Anthropic and Google Project Zero to 30-day disclosure windows is not coincidence — it reflects an industry-wide recognition that the AI-accelerated vulnerability-discovery cycle has made the 90-day norm structurally obsolete.

---

### Perplexity: Multiagent and the Cross-Checking Architecture

Perplexity's most significant interaction-design and agentic-architecture event in this window is **Multiagent** — the new top effort level in Computer and Teammates, launched November 17, that introduces a cross-model peer-review step into the agent loop itself before synthesis.



Multiagent is the new effort level above Ultra for Computer's most complex work; the lead agent runs a team of agents on different frontier models that work in parallel, share findings directly with each other, and check each other's work; this lets Computer examine complex problems from multiple angles and find conflicting assumptions before bringing findings together into a single recommendation or output.

When Multiagent is selected in Computer's effort slider, the lead can assign up to 16 agents while taking on part of the work itself; the default team combines Opus 5.5, GPT 6.1 Sol, and Gemini 4 Carbon, bringing different models to the analysis and review.

 The cross-checking-before-synthesis architecture is the trust-design advance that distinguishes Multiagent from simply running more agents in parallel: 

Perplexity says that, unlike Ultra's supporting agents which report only to the lead, Multiagent's agents can exchange findings directly, question assumptions and flag discrepancies for further investigation.

 An agent that flags a discrepancy in a parallel agent's finding before the lead synthesises is a qualitatively different trust primitive than one that accepts sub-agent outputs at face value — it embeds a peer-review step into the multi-agent loop that is architecturally analogous to the human editorial check it is designed to replace.



Users select Multiagent through Computer's effort slider and can name the models they want in their query.

Multiagent is available to all Perplexity Max subscribers on the web.

 Simultaneously, 

Perplexity launched Orchestrator on November 17, allowing developers to connect to open-weight and proprietary AI models through one API with unified billing and automatic same-model failover.

 The Orchestrator API is the developer-infrastructure counterpart to Multiagent's end-user surface: where Multiagent gives Max users a managed multi-model coordination experience through Computer's effort slider, Orchestrator gives developers the same underlying routing and failover infrastructure on a single billing contract — enabling teams building on Perplexity's agent stack to implement their own multi-model workflows without managing separate API keys, billing relationships, or failover logic for each provider.

---

### Grok (xAI): Bot 1.0 and the Per-Team-Learning Approval Gate

xAI's most significant interaction-design event in the window is **Grok Bot 1.0** — which reached broad enterprise deployment this window following its November 11 launch — establishing the first fully multiplayer AI teammate architecture in xAI's product lineup, with a trust-design detail that addresses the core governance challenge of shared agents: how does a Bot that learns from individual team members update its behaviour without one person's input silently reshaping the experience for everyone else?



Bots now work with the whole team, take on work without being asked, and get more done faster; with Grok Bot 1.0, Bots can be shared and brought into Slack, Microsoft Teams, and video calls; Bots learn from everyone they work with and keep improving their understanding of the team's knowledge and preferences.

Proactive teammates can recognize work that needs to be done and offer to take it on; they can follow up on unfinished tasks, anticipate what a team needs next, and bring people in when a decision requires their judgment.

 The proactive-offer architecture — where the Bot recognises work and volunteers for it rather than waiting to be asked — is a consequential shift in the human-agent control handoff pattern: rather than the user delegating a task, the agent surfaces a task-delegation opportunity. This inverts the typical interaction model and places the agent in the position of proposing its own scope, which requires the trust-design answer of when and how the user can decline, redirect, or override a proactive offer.



As more colleagues use the Bot, it builds up knowledge of the team's work, preferences, and decisions; according to xAI's documentation, anything it learns from one teammate waits until the owner or a Manager approves it; that stops one person's correction from quietly changing the Bot for everyone.

 This per-learning approval gate is the micro-trust-design architecture that makes multiplayer shared agents manageable in enterprise contexts: without it, a single team member's interaction could reshape the agent's behaviour for all colleagues — a silent authority transfer at the shared-knowledge level. The approval requirement at the manager layer means the team's shared agent maintains a governed knowledge state rather than a continuously drifting one shaped by whoever interacted most recently.

---

## The Bigger Picture: Dots Go Default, Tasks Go Free, and Ignite Rewires the Work OS

The 48 hours ending November 18, 2026 crystallise a single macro movement that the entire November cycle has been building toward: **the moment when AI agents stop being opt-in features that adventurous users activate and start being the default state of enterprise and consumer platforms — present, running, and billing unless someone explicitly turns them off.** OpenAI's dots default-on flip is the clearest expression: two weeks ago, every ChatGPT Enterprise member who wanted a persistent agent had to ask for one; today, every member has one unless their administrator said no. Google's Gemini Tasks paywall removal is the consumer-side mirror: the agentic task execution and Google Pay checkout pattern that required a paid subscription is now free infrastructure for hundreds of millions of users, with the spending-cap-and-approval UX becoming the de facto interaction pattern for agentic commerce at mass scale. Microsoft's Autopilot rolling to Frontier with its own Entra Agent ID, manager assignment, and Agent 365 audit trail is the enterprise-tier version of the same movement — a persistent agent that knows who it works for, whose actions are attributable, and whose cost can be measured against its output. What connects all three is that they have resolved the trust-primitive question from the previous cycle — confirmation cards, biometric approval, permission gates — and arrived at the deployment-governance question: when agents are on by default, running in the background, learning from colleagues, and completing transactions on behalf of users, what administrative infrastructure exists to know what they are doing, what they cost, and how to constrain them? Perplexity's Multiagent adds a fourth dimension: when agents coordinate other agents, the human is now two levels removed from the execution layer, and the trust architecture has to extend its reach from human-agent boundaries to agent-agent boundaries. Anthropic's 30-day disclosure policy update is the meta-signal of the window — a recognition, embedded in a governance document, that AI capability is now moving faster than the institutional norms designed to contain it, and that the platforms closest to that capability have an obligation to accelerate governance to match. The industry that spent October building trust primitives for individual agentic actions is now building the administrative infrastructure for agentic fleets — and the design challenge has shifted from "how does the user approve one action" to "how does the administrator govern ten thousand agents they did not individually deploy."

---

## References

[1] dataconomy.com. (2026). *OpenAI Launches ChatGPT For Sales With Salesforce, HubSpot Integration*. [https://dataconomy.com/2026/11/18/openai-launches-chatgpt-for-sales-with-salesforce-hubspot/](https://dataconomy.com/2026/11/18/openai-launches-chatgpt-for-sales-with-salesforce-hubspot/)

[2] cellcog.ai. (2026). *ChatGPT for Sales: OpenAI's Sales Plugin and 30+ Partners*. [https://cellcog.ai/blog/chatgpt-for-sales/](https://cellcog.ai/blog/chatgpt-for-sales/)

[3] aiera.blog. (2026). *OpenAI ChatGPT for Sales: CRM Work Inside ChatGPT*. [https://aiera.blog/openai-chatgpt-for-sales/](https://aiera.blog/openai-chatgpt-for-sales/)

[4] help.openai.com. (2026). *Pricing and billing for dots in ChatGPT Enterprise*. [https://help.openai.com/en/articles/20001641-pricing-and-billing-for-dots-in-chatgpt-enterprise](https://help.openai.com/en/articles/20001641-pricing-and-billing-for-dots-in-chatgpt-enterprise)

[5] help.openai.com. (2026). *Managing dots in ChatGPT workspaces*. [https://help.openai.com/en/articles/20001554-managing-dots-in-chatgpt-workspaces](https://help.openai.com/en/articles/20001554-managing-dots-in-chatgpt-workspaces)

[6] help.openai.com. (2026). *Getting started with your dot*. [https://help.openai.com/en/articles/20001530-getting-started-with-your-dot](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)

[7] beri.net. (2026). *Opt Out of ChatGPT Enterprise Dots Before Billing Starts November 18*. [https://www.beri.net/article/openai-brings-dots-persistent-personal-agents-to-chatgpt](https://www.beri.net/article/openai-brings-dots-persistent-personal-agents-to-chatgpt)

[8] memorylake.ai. (2026). *ChatGPT Dot Custom Instructions Explained (2026)*. [https://www.memorylake.ai/en/blogs/chatgpt-dot-custom-instructions](https://www.memorylake.ai/en/blogs/chatgpt-dot-custom-instructions)

[9] technobezz.com. (2026). *Gemini Makes Tasks Free and Adds Google Pay Checkout*. [https://www.technobezz.com/news/gemini-app-update-11-17](https://www.technobezz.com/news/gemini-app-update-11-17)

[10] cellcog.ai. (2026). *Tasks in Gemini Is Now Free: Calls, Payments, Limits*. [https://cellcog.ai/blog/tasks-in-gemini/](https://cellcog.ai/blog/tasks-in-gemini/)

[11] unite.ai. (2026). *Google Makes Tasks in Gemini Free and Adds Calls and Payments*. [https://www.unite.ai/google-makes-tasks-in-gemini-free-and-adds-calls-and-payments/](https://www.unite.ai/google-makes-tasks-in-gemini-free-and-adds-calls-and-payments/)

[12] datastudios.org. (2026). *Gemini Tasks free in 6 countries: calls, Google Pay checkout, text and email in the US*. [https://www.datastudios.org/post/gemini-tasks-free-six-countries-calls-pay-bills-google-pay-instacart](https://www.datastudios.org/post/gemini-tasks-free-six-countries-calls-pay-bills-google-pay-instacart)

[13] xenospectrum.com. (2026). *Google makes Gemini Tasks free in Japan and five other countries*. [https://xenospectrum.com/en/gemini-tasks-free-purchase-approval/](https://xenospectrum.com/en/gemini-tasks-free-purchase-approval/)

[14] 9to5google.com. (2026). *Google Home speakers get a major Gemini upgrade 'soon,' but only for paid subscribers*. [https://9to5google.com/2026/11/18/google-home-gemini-live-update-coming/](https://9to5google.com/2026/11/18/google-home-gemini-live-update-coming/)

[15] i10x.ai. (2026). *Microsoft Ignite: Nadella Unveils Copilot Workspaces, Autopilot and Copilot Code*. [https://i10x.ai/news/microsoft-copilot-workspaces-autopilot-copilot-code-ignite-2026](https://i10x.ai/news/microsoft-copilot-workspaces-autopilot-copilot-code-ignite-2026)

[16] news.microsoft.com. (2026). *Microsoft Ignite 2026 Book of News*. [https://news.microsoft.com/events/ignite/2026/book-of-news/](https://news.microsoft.com/events/ignite/2026/book-of-news/)

[17] datastudios.org. (2026). *Microsoft Copilot at Ignite 2026: Office in Copilot GA, Copilot Code in December, Autopilot*. [https://www.datastudios.org/post/microsoft-copilot-ignite-2026-office-in-copilot-copilot-code-december-autopilot](https://www.datastudios.org/post/microsoft-copilot-ignite-2026-office-in-copilot-copilot-code-december-autopilot)

[18] windowsforum.com. (2026). *Microsoft Ignite 2026 Keynote: Copilot Agents, AI Security and Azure Launches Explained*. [https://windowsforum.com/news/microsoft-ignite-2026-keynote-copilot-agents-ai-security-and-azure-launches-explained.452746/](https://windowsforum.com/news/microsoft-ignite-2026-keynote-copilot-agents-ai-security-and-azure-launches-explained.452746/)

[19] siliconangle.com. (2026). *At Ignite 2026, Microsoft reinvents Copilot as the autonomous engine of enterprise work*. [https://siliconangle.com/2026/11/18/at-ignite-2026-microsoft-reinvents-copilot-as-the-autonomous-engine-of-enterprise-work/](https://siliconangle.com/2026/11/18/at-ignite-2026-microsoft-reinvents-copilot-as-the-autonomous-engine-of-enterprise-work/)

[20] powerplatformengineer.com. (2026). *Microsoft Ignite 2026 Announcements: Complete Guide for Power Platform Teams*. [https://powerplatformengineer.com/microsoft-ignite-2026-announcements-guide/](https://powerplatformengineer.com/microsoft-ignite-2026-announcements-guide/)

[21] github.com/ellismosss. (2026). *scout: Claude Code changed to 2.1.327*. [https://github.com/ellismosss/optimizer/issues/28](https://github.com/ellismosss/optimizer/issues/28)

[22] github.com/e-xode. (2026). *Claude Code drift: 2.1.327*. [https://github.com/e-xode/deadweight/issues/21](https://github.com/e-xode/deadweight/issues/21)

[23] github.com/meawoppl. (2026). *Update claude-codes to 2.1.328*. [https://github.com/meawoppl/agent-portal/pull/2487](https://github.com/meawoppl/agent-portal/pull/2487)

[24] msspalert.com. (2026). *Anthropic updates vulnerability disclosure policy for AI flaws*. [https://msspalert.com/news/anthropic-updates-vulnerability-disclosure-policy-for-ai-discovered-flaws](https://msspalert.com/news/anthropic-updates-vulnerability-disclosure-policy-for-ai-discovered-flaws)

[25] helpnetsecurity.com. (2026). *Anthropic vulnerability disclosure deadline drops to 30 days for serious bugs*. [https://www.helpnetsecurity.com/2026/11/17/anthropic-vulnerability-disclosure-days/](https://www.helpnetsecurity.com/2026/11/17/anthropic-vulnerability-disclosure-days/)

[26] dev.to. (2026). *Anthropic Cut Bug Disclosure to 30 Days. The 90-Day Era Is Over*. [https://dev.to/paullovelace/anthropic-cut-bug-disclosure-to-30-days-the-90-day-era-is-over-37n8](https://dev.to/paullovelace/anthropic-cut-bug-disclosure-to-30-days-the-90-day-era-is-over-37n8)

[27] thenextweb.com. (2026). *Anthropic cuts its bug disclosure window to 30 days as AI finds flaws*. [https://thenextweb.com/news/anthropic-disclosure-window-30-days-ai-vulnerabilities](https://thenextweb.com/news/anthropic-disclosure-window-30-days-ai-vulnerabilities)

[28] perplexity.ai. (2026). *Introducing Multiagent for the most complex work*. [https://www.perplexity.ai/hub/blog/introducing-computer-multiagent](https://www.perplexity.ai/hub/blog/introducing-computer-multiagent)

[29] unite.ai. (2026). *Perplexity Launches Multiagent to Coordinate Frontier AI Models*. [https://www.unite.ai/perplexity-launches-multiagent-to-coordinate-frontier-ai-models/](https://www.unite.ai/perplexity-launches-multiagent-to-coordinate-frontier-ai-models/)

[30] marktechpost.com. (2026). *Perplexity Computer Adds Multiagent: Up to 16 AI Agents That Cross-Check Work*. [https://www.marktechpost.com/2026/11/17/perplexity-computer-multiagent-effort-level/](https://www.marktechpost.com/2026/11/17/perplexity-computer-multiagent-effort-level/)

[31] mlq.ai. (2026). *Perplexity launches Multiagent for Computer and Orchestrator*. [https://mlq.ai/news/perplexity-launches-multiagent-for-computer-and-orchestrator-an-api-for-models-from-openai-anthropic-google-and-xai/](https://mlq.ai/news/perplexity-launches-multiagent-for-computer-and-orchestrator-an-api-for-models-from-openai-anthropic-google-and-xai/)

[32] x.ai. (2026). *Introducing Grok Bot 1.0*. [https://x.ai/news/grok-bot-1-0](https://x.ai/news/grok-bot-1-0)

[33] pasqualepillitteri.it. (2026). *Grok Bot 1.0 launches with shared Bots in Slack, Teams and meetings*. [https://pasqualepillitteri.it/en/news/32587/grok-bot-1-0-shared-bots-slack-teams-meetings](https://pasqualepillitteri.it/en/news/32587/grok-bot-1-0-shared-bots-slack-teams-meetings)

[34] datanorth.ai. (2026). *Grok Bot 1.0: xAI's shared AI teammate for Slack and Teams*. [https://datanorth.ai/news/grok-bot-1-0-slack-teams](https://datanorth.ai/news/grok-bot-1-0-slack-teams)

[35] cellcog.ai. (2026). *Grok Bot 1.0: What Changed Since the Beta*. [https://cellcog.ai/blog/grok-bot-1-0/](https://cellcog.ai/blog/grok-bot-1-0/)

[36] releasebot.io. (2026). *xAI Release Notes — November 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)