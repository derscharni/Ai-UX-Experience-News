# UX Briefing: Platform Mergers, Agent Connectors, and the Cutover Moment

**September 01, 2026**

Good morning. The 48 hours ending September 1, 2026 are defined by a single structural force: every major AI product is simultaneously collapsing its seams — merging fragmented surfaces into single unified apps, linking previously isolated identity contexts, and drawing irreversible lines between the old interaction model and the new one. **Claude/Anthropic** enters September with its usage-visibility and governance arc reaching a critical juncture: new Compliance API endpoints for local Claude Code sessions land as the first native audit layer for endpoint agents, while announced interface tooling promises developers direct in-product quota visibility and control — the trust-design answer to the upcoming September 14 limit recalibration. **ChatGPT/OpenAI** ships two high-contact interaction events simultaneously: **multi-account Google plugin support** lands for Gmail, Calendar, and Contacts — ending the forced single-identity constraint that had made agentic scheduling workflows clumsy — while **WebMCP Site Tools** introduce a new agent-to-website interaction primitive in the desktop browser that shifts the model from "simulate a human clicking" to "call the function the site exposes," with a 10-day developer challenge running through September 3 to accelerate adoption. **Google Gemini** crosses the irreversible threshold today: **Google Assistant officially begins its shutdown on Android, Wear OS, and paired headphones** starting September 4, with no rollback path once a device switches — a forced migration of hundreds of millions of users to Gemini's conversational, multi-step interaction model. **Microsoft Copilot** arrives in September mid-rollout of its most consequential UX consolidation in years: the **unified Copilot app** — merging consumer Copilot and Microsoft 365 Copilot into a single surface with a single icon and account-switcher — is active on web and mobile and tracking toward its mid-September Windows/Mac desktop GA, with the **Planner Agent's AI-generated status reports** simultaneously reaching general availability. And **Grok (xAI/SpaceXAI)** delivers the most consequential persistent-agent integration event of its early lifecycle: **Grok Bot's native X account connector** ships on August 29, giving the always-on agent bot authenticated access to post, timeline, and mention tools on the same social platform it lives in.

---

## At a Glance: September 1 Highlights

Today's releases converge on a single architectural signal: the AI industry is forcibly retiring its fragmented, single-context, session-bound interaction models — and the design challenge is now managing the trust implications of unified, persistent, cross-identity agents operating in surfaces users did not originally build for them.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Compliance API adds local Claude Code session endpoints** — first native audit layer for endpoint agents covering text, tool_use, and tool_result blocks; Anthropic teases in-product usage dashboard improvements ahead of September 14 limit recalibration; Claude Code admin console gains value tab with productivity lift and cost-per-commit estimates; web domain allow/blocklists now available for Managed Agents' web_search and web_fetch tools. [1][2][3] |
| **ChatGPT** | **Multi-account Gmail, Calendar, and Contacts plugin support** lands August 28 — single conversation now reaches across personal and work Google identities; **WebMCP Site Tools** ship in desktop browser, letting agents call structured functions on compatible websites instead of scraping UI; WebMCP Challenge open through September 3; DALL·E GPT retired August 30; `Computer History` expands to EEA, Switzerland, and UK for Pro users. [4][5][6] |
| **Google Gemini** | **Google Assistant shutdown begins September 4** — irreversible cutover to Gemini on Android phones, tablets, Wear OS, and Android Auto with no rollback path; Gemini 3.5 Transcribe reaches GA with two dedicated speech-to-text models (high-accuracy and live-streaming); Google Chat Gemini usage metrics now available in admin dashboards; `gemini-omni-flash-preview` endpoint set for September 30 deprecation. [7][8][9] |
| **Microsoft Copilot** | **Unified Copilot app mid-rollout** — consumer and M365 Copilot merged into single app with account switcher and visual identity cues; Windows/Mac desktop GA tracking to mid-September; **Planner Agent AI status reports reach GA in September** — plan data converted to audience-aware stakeholder narratives with audience, tone, and section controls; Copilot mobile proactive notifications arc progressing toward GA. [10][11][12] |
| **Grok (xAI)** | **Grok Bot native X integration lands August 29** — connect X account for post, timeline, and mention tools; paid Grok Bot users receive free X API credits; Grok Bot now included on SuperGrok Plus, Cursor Pro+, and Cursor Teams plans; Grok Build adds `/loop` stop-condition storage for self-terminating recurring tasks; MCP servers now enable/disable from CLI. [13][14][15] |
| **Perplexity** | **Sonar API retirement countdown reaches 26 days** — September 27 deadline passes the two-thirds mark; Agent API now the canonical endpoint combining web search, URL fetch, code execution, MCP, and finance/people search in six configurable presets; Computer in Email remains the temporal UX standout; Perplexity Computer expands to Windows 10/11 with Word, Excel, Outlook, and 400+ app connectors. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Compliance API Gap Closes and the Quota Visibility Arc

Anthropic's most consequential trust-design event entering September is not a new feature — it is the closing of a governance gap that enterprise security teams have been navigating since Claude Code's widespread adoption began. 

On August 11, 2026, Anthropic introduced new endpoints for local Claude Code sessions in the Compliance API; before August 2026, Anthropic's native controls had limited visibility into what endpoint agents were actually doing — with the new local session transcript endpoints, teams can better govern their local agents.

 The interaction-design significance of this is disproportionate to the quiet changelog entry: 

these endpoints give visibility into agents running on endpoints based on their interaction with Anthropic's models, with whatever is communicated to the model logged in three block types — text, tool_use, and tool_result — covering user prompts, bash commands, reads and writes, and MCP commands.

 For enterprise UX practitioners, this is the audit trail that transforms Claude Code from "a developer tool we cannot observe" into "a governed agentic surface we can retrospectively inspect." The three-block taxonomy — input, tool call, tool result — is also the right abstraction level for auditors who are not developers: each block is a legible unit of agent intent and agent action, not a raw log dump.

The second governance-design event entering September is the incoming usage-visibility upgrade Anthropic has signalled ahead of the September 14 limit recalibration. 

To help soften the impact of the upcoming cap change, Anthropic teased that interface updates are in the pipeline, with the engineering team working on new dashboard tools that will give users much clearer visibility and direct control over their remaining weekly quotas.

 The existing admin analytics surface already shows significant depth — 

Claude Code gets richer insights with two tabs focused on value and usage inside the admin console; the Usage tab shows active developers, session counts, and top commands across the org updated daily; the value tab summarises usage and cost data, estimating productivity lift, cost per commit, and annual value, with every formula visible and inputs adjustable.

 What is conspicuously absent from the existing surface — and what the teased new tooling appears intended to supply — is real-time, per-user remaining-quota visibility at the session level. The human-control implication is clear: developers who can see their remaining quota before they start a long agentic session will make qualitatively different decisions about when to delegate versus defer, compared to developers who discover the limit by hitting it.

On the operator-control surface, 

Claude Managed Agents agents' web_search and web_fetch tools now support domain-level allow and blocklists; operators set `allowed_domains` or `blocked_domains` on the tool's entry in the `agent_toolset_20260401` configs array, with web_fetch also accepting `max_content_tokens` and web_search accepting `user_location`.

 This is the web-reach equivalent of the `--restricted` mode that landed in Claude Code last week: rather than governing what the agent can execute locally, domain allow/blocklists govern what the agent can fetch from the web — a trust boundary that enterprise operators can now draw with network-level precision rather than relying on prompt-level instructions.

---

### ChatGPT / OpenAI: Multi-Identity Connectors and the WebMCP Protocol Moment

OpenAI's most immediately impactful interaction-design event in this window is the arrival of **multi-account Google plugin support**, which ships on August 28 and closes a friction point that has constrained agentic scheduling and inbox-management workflows since the plugins launched. 

ChatGPT now accepts several accounts for Gmail, Google Calendar, and Google Contacts at the same time, inside the same conversation — a change that rolled out since August 28.

 The UX significance runs deeper than convenience: 

once linked, the assistant pulls context across connected profiles without merging them behind the scenes — users can search for receipts across a personal archive while simultaneously checking a corporate calendar for open meeting slots, without running two separate searches or switching profiles manually.

 This shifts the identity model of agentic context from "one credential, one world" to "multiple authorized identities, unified query surface" — a pattern that defines how agentic assistants will need to operate for the majority of knowledge workers who live across two or more Google accounts daily. 

Community reports indicate Google Drive multi-account support is arriving next

 — suggesting the multi-identity connector arc is not complete and the same pattern is being extended across the full Google workspace stack.

The second, more structurally significant event is the arrival of **WebMCP Site Tools** in the ChatGPT desktop browser. 

OpenAI added support for WebMCP in the ChatGPT desktop app's built-in browser, giving AI agents a structured way to interact with compatible websites instead of scraping layouts and simulating clicks; when a user visits a WebMCP-enabled site, ChatGPT Work and Codex can automatically discover the tools that site offers and use them to complete tasks.

 The interaction-design shift this establishes is the same one that browser use brought to Claude's computer-use toolset: rather than the agent guessing what a button does by reading HTML and simulating a click, 

a webpage can register JavaScript functions as tools with names, descriptions, and structured input schemas — and instead of leaving agents to guess their way through the UI, developers define exactly how agents can use the app.

 For UX practitioners designing agent-ready web experiences, WebMCP introduces a new design responsibility: the structured action surface that the agent sees is now a first-class design artifact, not just a consequence of the visual interface. 

Millions of Shopify storefronts are already WebMCP-enabled, with Expedia, Instacart, and Target among the companies experimenting with the standard.

 OpenAI is accelerating ecosystem adoption through a competition: 

the OpenAI WebMCP Challenge invites developers to build agent-ready web apps that work with ChatGPT, with submissions due September 3, 2026.

 The trust-design detail worth tracking is the inspection path: 

users can inspect what a page offers by selecting "Site tools" in the browser's address bar

 — a transparency primitive that makes the agent's available action surface legible to the human before any action is taken.

---

### Google Gemini: The Irreversible Cutover and the Transcription Infrastructure

Google's most consequential interaction-design event of the entire September window begins today — not a feature launch but a mandatory migration. 

Google will permanently shut down Google Assistant on Android and Wear OS on September 4, 2026, replacing it with its LLM-powered Gemini across smartphones, tablets, Wear OS, and Android Auto.

 The irreversibility of this cutover is the design detail that separates it from every previous Gemini rollout: 

once Gemini replaces Assistant on a device, there is no option to switch back — the cutover is irreversible on that device.

 The scope of what changes for users is more significant than the switch date alone suggests. 

Gemini, the AI model powering the replacement, handles complex multi-turn queries differently than Assistant did — where Assistant was optimized for single-command tasks, Gemini is built around longer conversations and synthesis.

 This is the largest-scale forced migration of a voice interaction model in the industry's history, and the UX implications are real: habits, Routines, and assistant integrations built around Assistant's single-command, immediate-response model will encounter a fundamentally different interaction contract in Gemini. 

Some Assistant features may lack Gemini equivalents — users should check routines, reminders, Interpreter Mode, and media controls before switching.

 The device-class carve-outs are equally significant: 

built-in car systems, Google TV, smart speakers, and smart displays are exempt from the September 4 cutover scope

 — meaning the transition is not universal, and users with cross-device Assistant integrations face a fragmented transition period where some surfaces switch and others do not.

The companion technical event — the GA launch of **Gemini 3.5 Transcribe** — is the infrastructure investment that makes the assistant replacement credible on the real-time audio surfaces where Assistant competed. 

Gemini 3.5 Transcribe reaches general availability as two dedicated speech-to-text models for high-accuracy transcription and low-latency live streaming, supporting language detection, speaker diarization, word timestamps, custom vocabulary, and Live API streaming.

 The two-model split — 

one for high-accuracy non-streaming transcription with utterance-based language detection across 85+ languages, and one for low-latency bidirectional streaming speech-to-text over WebSockets

 — is the architecture that lets Gemini handle both the real-time voice query (streaming) and the structured meeting transcript (high-accuracy batch) from a single model family. For developers building voice-first Gemini experiences to replace Assistant integrations, this is the toolchain upgrade that removes the latency excuse for not switching. On the admin side, 

admins can now access Google Chat usage metrics in the Gemini reports dashboard across both organisation- and user-level reports; at the organisation level, this allows admins to track active Gemini users in Google Chat, analyse usage trends, and identify who benefits most from Gemini-powered summarisation and generation features.



---

### Microsoft Copilot: The Super App Consolidation and the Planner Agent GA

Microsoft's most structurally significant UX event entering September is the active rollout of the **unified Copilot app**, which formally collapses two previously separate products into a single surface. 

Microsoft is combining its consumer Copilot app and the Microsoft 365 Copilot app into a single application that handles both personal and work accounts, with a worldwide rollout for mobile and web versions beginning in mid-August 2026 — the first structural step toward the "super app" the company has said it plans to launch later in 2026, ending a two-year stretch in which Microsoft shipped two separate Copilot apps that could sit side by side in the same taskbar.

 The trust-design architecture of the unified app is the element that deserves the closest practitioner attention: 

the personal and commercial accounts are separated within the app, meaning data from a work or school account is not shared with a personal account, and vice versa

 — an explicit data-flow boundary that preserves enterprise governance even inside a unified shell. 

The Microsoft 365 Copilot app becomes the new unified app with navigation changes, a new icon, and free Copilot chat access; the worldwide rollout of the unified Copilot desktop apps for Windows and macOS will kick off in mid-September.

 The interaction-design consequence of this consolidation is significant for enterprise IT teams: the copilot.cloud.microsoft URL and unified app mean that the "which Copilot am I in?" confusion — a real source of user support tickets — is addressed through visual identity cues rather than requiring users to track multiple apps.

The companion agentic-workflow event reaching general availability this month is the **Planner Agent AI status report** capability. 

Microsoft is adding AI-generated status reports to Planner Agent, with general availability in September; the feature lets users turn task data into customised, audience-aware narratives, cutting down manual reporting time.

The capability converts Planner task data into a narrative status update; users can ask Planner Agent for a report and tailor it by specifying the intended audience, preferred tone, desired length, and sections to include.

 The interaction design pattern this establishes is the agent-as-reporting-layer: rather than treating status reporting as administrative overhead separate from the task board, 

Microsoft is positioning the plan itself as the reporting source — and Planner Agent as the layer that interprets the data.

The generated status report is created as a Loop component, allowing it to be easily reviewed, edited, and shared across Microsoft 365 surfaces

 — a design choice that makes the agent's output a collaborative artefact rather than a terminal deliverable: the human edits the Loop component, not a static document.

---

### Grok (xAI/SpaceXAI): The Bot-to-Platform Integration and the Loop Self-Termination Pattern

SpaceXAI's most consequential agentic UX event in this window is the arrival of **Grok Bot's native X account connector**, announced August 29. 

Grok Bot now has a tighter integration with X; connect an X account in Grok Bot and xAI will create a developer account if the user does not have one; paid Grok Bot users get free X API credits to start.

 The interaction-design significance of this is architectural rather than additive: 

to get started, users open Grok Bot and sign in with the X connector, then ask a Bot to search posts, read their timeline, check mentions, or pull together what is happening on X.

 Grok Bot is the only major persistent-agent product that runs on the same platform whose live data stream it is now authorised to read, write to, and monitor. This creates a closed-loop agentic architecture — the bot lives on X, accesses the X API through the user's own developer credentials, and can post or respond on the user's behalf — that no other platform in this briefing currently offers. The trust-design question this raises is the one every authenticated-agent integration must answer: 

when a bot needs access to a service, it navigates to the login screen and hands control back to the user with a "sign in, then hand it back" prompt — the user authenticates, and the bot resumes on its own browser instance from where it left off.

 The handoff-at-authentication pattern is the right trust-design primitive for sensitive connector grants — but the X integration, where the bot can now read a live timeline and compose posts, represents the most consequential permission scope Grok Bot has yet acquired.

On the Grok Build agentic-workflow surface, the `/loop` improvement is the temporal UX advancement worth isolating. 

`/loop` now stores prompts that include stop conditions so recurring tasks can terminate themselves when done

 — a design primitive that upgrades the recurring task model from "runs on a schedule until the user manually stops it" to "runs until the specified condition is met and reports completion." This is the agentic equivalent of a loop with a proper exit condition rather than an infinite loop that the human must interrupt. For practitioners designing long-running agentic workflows, self-terminating loops are the temporal UX pattern that prevents the most common class of runaway agent problem — a scheduled task that continues executing past the point of usefulness because no completion criterion was encoded. The CLI-level MCP management improvement — 

MCP servers can now be enabled or disabled from the CLI with `grok mcp enable <name>` and `grok mcp disable <name>`

 — is the operator-control complement: the developer can now scope the tool surface of a running Grok Build session from the command line without modifying configuration files.

---

### Perplexity: Sonar Sunset Midpoint and the Windows Computer Arc

Perplexity's most structurally significant developer-facing event in this window is not a new feature — it is the advancing Sonar retirement clock. 

Sonar endpoints remain fully available today, but on September 27, 2026, the Agent API becomes the main surface for this work and Sonar tiers retire on the same date; Perplexity's Agent API is one programmable endpoint for web search, URL fetching, code execution, MCP, and finance and people search with tunable presets.

 The interaction-design implication for developers who have built agentic workflows on Sonar's chat-completions API is that 

the Perplexity MCP Server v1.0.0 already moves its model-backed tools from the legacy Sonar models to Agent API presets — with `perplexity_ask`, `perplexity_reason`, and `perplexity_research` using fast, medium, and high presets respectively — with tool names and response shapes unchanged, and all three tools faster and cheaper on average than their Sonar predecessors.

 The migration path preserves the existing tool-name contracts, which means the developer-facing interaction model changes minimally even as the underlying infrastructure shifts. The 26 days remaining before the September 27 cutoff is sufficient lead time for teams that are aware; for teams still on Sonar without a migration plan, it is the relevant deadline now crossing into urgent territory.

On the consumer Computer surface, 

Perplexity's agent platform Personal Computer now supports Windows 10 and 11, bringing local file editing, integration with Word, Excel, Outlook, and more, and connections to over 400 apps to Windows users for the first time.

 This completes Perplexity Computer's platform-coverage arc: previously the preserve of Mac and Linux users, the Windows landing puts the multi-step agentic computer platform in front of the majority enterprise desktop demographic. The 400+ app connector library — covering Salesforce, HubSpot, Slack, and category-spanning integrations — means that Windows users arriving at Perplexity Computer for the first time encounter the same broad action surface that has defined Computer's proposition since launch. 

Perplexity has also extended its Model Council feature, which lets users consult multiple AI models at once, to its Computer agent platform

 — bringing the side-by-side multi-model output comparison into the agentic execution context, where users can evaluate which model's plan they want the agent to execute before committing to a run.

---

## The Bigger Picture: Platform Mergers, Agent Connectors, and the Cutover Moment

The 48 hours ending September 1, 2026 mark the moment the AI industry's most deferred structural reckonings arrive simultaneously. Google's Assistant-to-Gemini cutover is the most visible: for the first time in the industry's history, a major AI platform is not asking hundreds of millions of users to adopt a new interaction model — it is removing the option to decline. The transition from Assistant's single-command, immediate-response pattern to Gemini's conversational, multi-step, agentic model is the UX discontinuity that practitioners have been preparing for, and September 4 is when preparation ends and migration begins. Microsoft's unified Copilot app is the enterprise parallel: two separate products with two separate interaction models, collapsed into one surface where the account-switcher is the only visible seam between personal and organisational contexts. ChatGPT's multi-identity Google connector and WebMCP Site Tools represent the same consolidation impulse at the interaction-primitive level — the former collapsing two Google identities into one query context, the latter collapsing the gap between "what the website looks like" and "what the agent is allowed to do on it." What unifies these events is the design problem they all share: when a unified surface inherits the users, habits, and trust expectations from two or more predecessor systems, the governance architecture has to answer one question at every boundary — whose rules apply here? Microsoft's answer is the account-switcher with colour-coded identity cues. Google's answer is irreversibility. OpenAI's answer is the WebMCP action manifest that the website author controls. The platforms that navigate this consolidation well are not the ones that make the merge invisible — they are the ones that make the seam legible, so users understand exactly which context they are operating in, which agent can reach which identity, and what happens when they cross from one into the other.

---

## References

[1] The Hacker News. (2026). *Securing Claude Code: The New Compliance API, Local Visibility, and Identity Governance*. [https://thehackernews.com/2026/08/securing-claude-code-new-compliance-api.html](https://thehackernews.com/2026/08/securing-claude-code-new-compliance-api.html)

[2] Android Headlines. (2026). *Anthropic's Claude Code Usage Cap Update Actually Hides a Quiet Downgrade*. [https://www.androidheadlines.com/2026/08/anthropic-claude-code-weekly-limits-update.html](https://www.androidheadlines.com/2026/08/anthropic-claude-code-weekly-limits-update.html)

[3] Anthropic. (2026). *Claude Platform Release Notes — Overview*. [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview)

[4] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] Releasebot. (2026). *ChatGPT Updates by OpenAI — August 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[6] Search Engine Journal. (2026). *OpenAI Adds WebMCP Site Tools To ChatGPT's Browser*. [https://www.searchenginejournal.com/chatgpt-adds-webmcp-support/587237/](https://www.searchenginejournal.com/chatgpt-adds-webmcp-support/587237/)

[7] AI Weekly. (2026). *Google Sets Sept 4 Cutoff to Replace Assistant With Gemini*. [https://aiweekly.co/alerts/google-sets-sept-4-cutoff-to-replace-assistant-with-gemini](https://aiweekly.co/alerts/google-sets-sept-4-cutoff-to-replace-assistant-with-gemini)

[8] Google Workspace Updates Blog. (2026). *2026 Workspace Update Archive*. [https://workspaceupdates.googleblog.com/2026/](https://workspaceupdates.googleblog.com/2026/)

[9] Releasebot. (2026). *Google Release Notes — August 2026*. [https://releasebot.io/updates/google](https://releasebot.io/updates/google)

[10] Windows Central. (2026). *Microsoft begins unified Copilot app rollout*. [https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding)

[11] Windows News. (2026). *Microsoft Planner's AI Status Reports Come to Life in August: Here's Your Guide*. [https://windowsnews.ai/article/microsoft-planners-ai-status-reports-come-to-life-in-august-heres-your-guide.440790](https://windowsnews.ai/article/microsoft-planners-ai-status-reports-come-to-life-in-august-heres-your-guide.440790)

[12] Microsoft Community Hub. (2026). *What's New in Microsoft Copilot — August 2026*. [https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960)

[13] SpaceXAI. (2026). *Grok Bot now works with X*. [https://x.ai/news/grok-bot-and-x](https://x.ai/news/grok-bot-and-x)

[14] Releasebot. (2026). *xAI Release Notes — August 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Perplexity AI. (2026). *Agent API: Build with LLMs, the Web, and Agents*. [https://www.perplexity.ai/hub/blog/agent-api-one-place-to-build-with-llms-the-web-and-agents](https://www.perplexity.ai/hub/blog/agent-api-one-place-to-build-with-llms-the-web-and-agents)

[17] Perplexity AI. (2026). *Changelog — Perplexity Docs*. [https://docs.perplexity.ai/docs/resources/changelog](https://docs.perplexity.ai/docs/resources/changelog)

[18] AI Watch Station. (2026). *Perplexity Launches Agent API, Will Retire Sonar Endpoints in September*. [https://ai-watch-blog.vercel.app/en/posts/2026-08-13-perplexity-agent-api-launch/](https://ai-watch-blog.vercel.app/en/posts/2026-08-13-perplexity-agent-api-launch/)