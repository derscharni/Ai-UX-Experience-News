# UX Briefing: Gemini Takes the Desktop, Dots Reach Plus, and Brain Rewrites Itself

**November 20, 2026**

Good morning. The 48 hours ending November 20, 2026 are defined by four simultaneous agentic-surface and infrastructure events: **Google** executing the most consequential desktop agentic expansion in Gemini's history on November 19 — **Gemini Computer Use for Mac** launching as the first background-window, full-GUI automation surface in the Gemini app, while simultaneously completing the Gemini 4 model matrix with the launch of **Gemini 4 Neon** on November 18 and **Google AI Mode dropping its Gemini model label** as Carbon rolls to Pro subscribers, abstracting model identity away from the Search interface; **OpenAI** delivering a cluster of four simultaneous UX advances on November 19 — a **redesigned ChatGPT mobile experience** giving dots their own tab with a pinnable feature bar and reaching Plus users for the first time, **ChatGPT Health expanding** to Android, desktop, dots, and Sites with Android Health Connect support and dot-driven proactive suggestions, **GPT-Live-1.1 arriving in the API** with a 60%-cheaper Standby mode that keeps WebRTC sessions open during silence, and **Codex CLI 0.171.0** shipping with cloud thread renaming and improved realtime model and voice defaults; **Anthropic** shipping **Claude Code 2.1.329** on November 19 with a trust dialog that surfaces hook-declaration provenance, MCP reconnection self-healing, and a cluster of VSCode and Code Mode fixes; and **Perplexity** publicly disclosing on November 18–19 the full architecture of **Brain's self-improving skills loop** — a four-stage Evidence-Reflection-Verification-Activation cycle that produced 80,000 skills for 20,000 users in 3.5 months, with a 72.9% skill-adoption rate versus 6.5% manual — alongside its November 19 blog on **context rot in long-running agents** as the theoretical counterpart to that architecture. Microsoft's **Ignite 2026** concludes on November 20, with **Copilot Today** in private preview in Outlook, **Copilot SDK 2.0**'s multi-tenant Rust runtime reaching broad developer attention, and **Grok Build 1.0.89** shipping on November 17 with a `/rename` session command, `/models` server-refresh, and `/hooks` legibility upgrades.

---

## At a Glance: November 20 Highlights

Today's window is defined by the industry arriving simultaneously at the moment when ambient desktop agency — an AI operating native apps in the background while the user keeps working — transitions from a differentiator to a table-stakes capability, with Gemini bringing background computer use to the Mac the same week OpenAI's dots reach Plus users, Perplexity's Brain starts writing its own operating skills, and Microsoft's Copilot Today assembles a proactive daily brief from email, calendar, and Teams.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code 2.1.329 (November 19) adds a trust dialog warning that says where a folder's hooks are declared, adds a warning in conversation, Claude Desktop, and other surfaces when a hook-declaration is detected; fixes background MCP tasks that stalled after a slow reconnect with self-healing HTTP MCP reconnection; fixes /code-review stopping at a permission prompt while searching for a CLAUDE.md that doesn't exist; fixes VSCode proposed-edit diff tabs staying open with a non-functional Accept button after session disconnect; and improves Code Mode subagent guidance consistency** — the hook-declaration provenance warning is the trust-design advance of the window: users can now see not just that a hook is active but precisely where in the folder hierarchy it was declared, giving them the information needed to make an informed decision about whether the hook's origin is trustworthy before granting it authority over tool execution. |
| **ChatGPT** | **ChatGPT mobile redesign (November 19) gives dots their own dedicated tab and adds a pinnable feature grid covering Space, Projects, Images, Scheduled, Codex, Plugins, Finance, Health, and Sites; dots begin testing with a small group of Plus users and roll to all Business Standard users on November 19; ChatGPT Health expands to Android via Health Connect, the Mac desktop app, ChatGPT Sites, and dots, with dots delivering proactive health suggestions; GPT-Live-1.1 arrives in the API on November 20 with Standby mode that pauses inference during silence at $0.02/min while keeping WebRTC open, plus 38 voice IDs including seven new Spanish-language entries; Codex CLI 0.171.0 ships with cloud thread renaming, improved realtime model selection, saved environments for Cloud threads, and native Mermaid flowchart support; ChatGPT Enterprise/Edu adds workspace-level SSO exemptions for external members** — the mobile redesign's dot-tab architecture is the interaction-design advance of the window: a persistent agent that previously required a navigation-bar detour now has a first-class surface at the thumb-reach of the app's primary navigation, normalising continuous engagement with the agent rather than episodic delegation. |
| **Google Gemini** | **Gemini Computer Use launches in the Gemini app for Mac on November 19 — the agent navigates native Mac apps, local files, and websites in an isolated background window with a live preview in chat; users approve key actions and select which apps Gemini can access; available for Google AI Plus, Pro, and Ultra subscribers on Apple Silicon Macs with macOS Sequoia 15.0+, US English only; Gemini 4 Neon launches November 18 as the mid-tier Gemini 4 model with four thinking levels and a 1M-token context window, targeting software engineering, finance, and science at 32% lower cost per task than Carbon; Google AI Mode drops its Gemini model label from the interface header and rolls Gemini 4 Carbon to Pro subscribers; Gemini CLI v0.69.0 ships daily token-usage heatmaps and standalone custom theme configuration** — the background-window isolation architecture in Gemini Computer Use is the trust-design signal of the window: by running the agent in a separate window that leaves the user's screen and cursor untouched, Google has built the same visual-separation trust primitive that the category has converged on, while adding a live preview in chat that keeps the agent's actions legible without requiring the user to watch a background window. |
| **Microsoft Copilot** | **Ignite Day 3 (November 19–20): Copilot Today enters private preview in Outlook and the Copilot app — a daily brief built from email, calendar, and Teams with a morning Brief and a refreshed Feed throughout the day; Copilot SDK 2.0 reaches broad developer attention — the Rust-core multi-tenant runtime lets one process host many isolated agent sessions, with six language SDKs (TypeScript, Python, Go, .NET, Java, Rust) and an empty mode that starts sessions without host shell or file access; Copilot Managed Runtime is generally available for hosting apps built in Code, Cowork, and Copilot Studio; the Dynamics 365 ERP apps plugin goes GA with 39+ finance and operations skills bringing ERP context into Copilot** — Copilot SDK 2.0's empty mode is the trust-design architecture of the developer tooling window: a session that starts without host shell access and without default tools is a session whose capability envelope is explicit from the first instruction rather than inherited from the runtime environment, establishing a least-privilege baseline for every agent session that shares the runtime. |
| **Grok (xAI)** | **Grok Build 1.0.89 (November 17, reaching broad developer attention this window) adds a /rename command on the dashboard for in-place session renaming without opening the session, a /models command to refresh the model list from the server, /hooks rows that now show the hook file name and readable settings instead of raw commands, /mcps now shows hosted sections expanded by default, and Enter on a workflow in the /workflows list opens the file for viewing and searching; grok mcp disable and enable now correctly stop servers inside already-running TUI sessions; grok inspect now reports the correct project config file for project-defined MCP servers; grok update no longer exposes internal experiment IDs or config files** — the /hooks legibility upgrade in 1.0.89 is the trust-design advance of the xAI window: hook configuration rows previously dumped raw commands into the terminal display; they now surface the hook file name and human-readable settings, translating the agent's permission configuration from machine syntax into an auditable, operator-legible format. |
| **Perplexity** | **Perplexity Brain's self-improving skills architecture is publicly disclosed in a research post on November 18, revealing a four-stage loop — Evidence, Reflection, Verification, Activation — that produced 80,000+ personal skills for 20,000+ users between August 1 and November 14, 2026, with 72.9% of Brain-enabled users receiving a new personal skill vs 6.5% of manual controls, and an 11% reduction in tool-call failures; personalization operates on context and instructions, not model weights; personal skills are capped at 10 per user to protect context-window efficiency; shared built-in skills require paired replay testing against historical failure scenarios plus human engineer approval before shipping; a companion November 18 post on context rot in long-running agents addresses how accumulated context degrades agent reliability in multi-step tasks; Perplexity's Orchestrator API restores three previously delisted Gemini Flash model variants to its routing inventory on November 20** — Brain's four-stage self-improvement loop, with its built-in-skill gate of replay testing plus human approval before any shared update ships, is the trust-design architecture that makes self-rewriting agent skills governable at scale. |

---

## Product Highlights

### Google Gemini: Computer Use Lands on the Desktop and Neon Completes the Model Matrix

Google's most consequential interaction-design event in this window is **Gemini Computer Use for Mac** — a background-execution computer agent that navigates native Mac apps, local files, and websites, launched November 19 as the first full GUI-automation surface in the Gemini desktop application.



Google announced on November 19, 2026 that computer use is rolling out in the Gemini app for Mac, allowing the assistant to carry out multi-step work across local files, desktop applications and websites.

 The background-window architecture is the central trust-design decision: 

Gemini operates in an isolated window, allowing the user to continue their own tasks without any screen interruptions, while the user remains in control by approving every action and choosing exactly which apps Gemini can access.

 The isolation model directly addresses the most significant user-trust barrier in computer-use agents: prior approaches that took over the user's primary screen created an adversarial UX where the user could not use their computer while the agent worked. The background-window pattern resolves this by separating the agent's execution environment from the user's working environment — the agent's actions are visible in a live preview within the Gemini chat, but the user's cursor and screen are untouched.



Google's task documentation says Gemini can view only files or directories specifically added to the Connected folders toolbar; users select Task below the text box, optionally add a Mac folder, and can disconnect an item added by mistake.

When Gemini works with computer files, it creates temporary backups.

 The selective-folder-access model and automatic backup creation are the two micro-trust-design decisions that most directly address the data-safety concern in computer-use agents: the agent cannot access the full filesystem unless the user explicitly adds each directory, and every file manipulation is recoverable. These are not incidental safeguards — they are the design decisions that make the difference between an agent a user is willing to let operate on their Documents folder and one they confine to a sandbox.

**Gemini 4 Neon**, launched November 18, completes the Gemini 4 product matrix and introduces an important interaction-architecture signal within the model tier. 

Gemini 4 Neon sits between the top-end Gemini 4 Carbon and the fast, cheap Gemini 4 Hydrogen, bringing "frontier-level intelligence with fast end-to-end task completion" at a lower cost per task.

Google also says Tasks in Gemini, its mode for handing off multi-step jobs, can run on Neon.

 Simultaneously, 

Google no longer shows the Gemini model used in AI Mode in the interface header, and has rolled out Gemini 4 Carbon to Pro subscribers in AI Mode, where it was previously only available to Ultra subscribers.

 The model-label removal from AI Mode is a consequential interaction-design signal in its own right: when the interface stops surfacing which model is running, the design is making a claim about how much model identity should be visible to users — and the answer being communicated is that model selection is an infrastructure concern, not a UI concern.

---

### ChatGPT / OpenAI: Dots Reach Plus, Mobile Gets a Makeover, and Voice Goes to the API

OpenAI's most consequential interaction-design event in this window is a cluster of four simultaneous advances, with the **ChatGPT mobile redesign** and **dots reaching Plus users** as the structural centre of gravity.



OpenAI is rolling out a new experience for the ChatGPT mobile app that makes it easier to get to favourite features and discover more of what users can do; the dot has its own tab, and users can pin favourites like Codex, Projects, and Images to the tab bar; the rollout starts with ChatGPT Pro users who are 18 or older in regions where dots are available.

OpenAI says it's testing dots with a small group of Plus users and bringing them to all Business Standard users, with that rollout set to start November 19.

 The architectural significance of the dot tab is in what it communicates about the agent's intended relationship to the app's information hierarchy: a dot that lived in the navigation bar was a feature among features; a dot that has its own tab is a persistent presence at the same navigational level as the conversation itself, normalising continuous agent engagement rather than episodic task delegation.

**ChatGPT Health's expansion** to multiple new surfaces is the cross-surface integration event of the window. 

Starting November 19, Health is rolling out to more of the places users use ChatGPT, including the desktop app, dots, sites, and Android, with support for Health Connect; users can connect their health and fitness information with Android Health Connect to explore patterns in their sleep, activity, and more; and can get proactive suggestions from their dot, like another time for a workout when a meeting gets in the way, or a reminder about preventive care options based on their connected medical records.

 The dots-plus-Health pairing is the agentic-personalisation advance that merits the most attention: 

from November 19, chats that draw on connected Health data can be used to train OpenAI's models unless the user first switches off "Improve the model for everyone" in Data controls.

 This is the trust-design tension the expansion introduces — a proactively helpful dot drawing on health data is also, by default, contributing that health context to model training, unless the user has taken a deliberate opt-out action that most will not know to take.

**GPT-Live-1.1 arriving in the API** is the voice-infrastructure advance of the window. 

GPT-Live-1.1 improves pronunciation, accent consistency, and transcription in multilingual voice conversations; developers use it in an existing Live session configuration and describe in plain language when to delegate to the backend.

Standby is a new GPT-Live API configuration available for both GPT-Live-1 and GPT-Live-1.1, with an idle timeout between 5 and 60 seconds; after that period of silence, the model temporarily pauses while the WebRTC call stays open, and when someone speaks again, the conversation resumes.

 The Standby interaction pattern is the developer-UX advance that matters most for voice-agent design: a WebRTC session that stays open but pauses inference during silence means the user experience of a persistent voice presence — always available, no reconnection latency — without the billing cost of continuous active inference. 

The API drop also ships 38 voice IDs, with seven new entries including Spanish-language voices.



---

### Claude / Anthropic: Hook Provenance, MCP Self-Healing, and a Cluster of Code Mode Fixes

Anthropic's most consequential interaction-design event in this window is **Claude Code 2.1.329**, shipping November 19 with a trust-design advance that addresses a gap in the existing hook-permission architecture: users can see that hooks are active, but previously could not easily determine from which directory in a potentially deep folder hierarchy a hook was declared.



Claude Code 2.1.329 adds a trust dialog warning that says where a folder's hooks are declared.

The release also adds a warning in the conversation, in Claude Desktop and other surfaces when a hook declaration is detected.

 The hook-provenance design advance addresses a specific attack surface in agentic coding workflows: when a user opens a project directory that contains hooks — particularly a directory shared by a team, cloned from an external repository, or traversed by a background agent — the previous UX presented the hook as an active constraint without surfacing its origin. A hook declared in a deeply nested subdirectory or a connected folder added via `--add-dir` could be exercising authority over tool execution without the user having any visible indication of where that authority was declared. The provenance warning closes this gap.



The release fixes background MCP tasks that stalled after a slow reconnect: Claude Code now reconnects most HTTP MCP servers by itself when one is left on an older protocol version; fixes /code-review stopping at a permission prompt on most models to look for a ~/.claude/CLAUDE.md that doesn't exist; fixes claude mcp login and /mcp saying a service doesn't accept sign-ins from Claude Code when the service's client registration had been retired (HTTP 410 Gone); and fixes a new skills, commands or agents folder being missed when --add-dir names the working directory or Claude Code starts in the home folder.

 The MCP self-healing reconnection is the agentic-reliability advance within this release: a background task that stalls because an MCP server was left on an older protocol version is an invisible failure — the agent appears to be running while making no progress, with no user-visible signal about why. Automatic reconnection at the protocol-mismatch boundary removes a failure mode that previously required user intervention to diagnose and resolve, replacing a silent stall with autonomous recovery.

---

### Microsoft Copilot: Today's Brief, the SDK's Empty Mode, and Ignite Day 3

Microsoft's most consequential interaction-design event completing its Ignite arc in this window is the private preview launch of **Copilot Today** and the broader availability of **Copilot SDK 2.0** — the two advances that together define what Copilot's proactive-surface and developer-infrastructure story looks like after Ignite.



Today, currently rolling out to private preview in Outlook and the Microsoft Copilot app, helps people stay on top of their work by surfacing key priorities and preparing next steps.

Today is a new view, available from the Copilot app's Home page and in Outlook; the Today Brief, the morning summary, is included with a Microsoft 365 Copilot license; the Today Feed, refreshed throughout the day, consumes Copilot Credits.

 The two-track architecture of Today — a licensed Brief for the morning context-load, and a credit-consuming Feed for continuous intra-day updates — is a consequential interaction-design decision about how proactive AI surface access should be priced and how frequently an agent should be allowed to interrupt the user with unsolicited prioritisation.



Microsoft announced Copilot SDK 2.0 at Ignite on November 17, 2026; the SDK, previously the GitHub Copilot SDK, now lets one runtime host many isolated agent sessions in a single process instead of one container each.

The SDK's empty mode starts without a host shell, host file-system access, or default tools.

Application developers can get Copilot SDK 2.0 for TypeScript, Python, Go, .NET, Java and Rust.

 The empty mode's trust-design significance is structural: rather than starting a session with a default capability set that developers then restrict, the empty mode starts with no capabilities at all, requiring developers to explicitly grant each tool and resource access. This reverses the trust direction from "restrict what you don't want" to "grant only what you need" — a least-privilege-by-default architecture that is architecturally sounder for multi-tenant shared runtimes where one session's misconfiguration could affect others in the same process.



Microsoft also announced the updated Sales plugin (generally available) that brings new sales skills into Copilot, so sellers can build account plans, prep for customer meetings, catch up on deals, and prioritise pipeline in their flow of work; new deal insights track progress against the quarterly forecast, map decision makers and engagement gaps, and flag deals and risks that need attention.

 The domain-skills pattern — purpose-built skills for sales, finance, and ERP ops surfaced directly in Copilot's conversation layer — continues the same domain-workspace trajectory that ChatGPT for Sales established on November 17, confirming that the industry has converged on pre-loaded specialist context as the interaction architecture for professional agentic surfaces.

---

### Perplexity: The Four-Stage Self-Improvement Loop and the Context Rot Problem

Perplexity's most significant interaction-design and agentic-architecture publication in this window is not a new surface but a detailed technical disclosure: the **Brain self-improving skills research post** published November 18, which reveals the full architecture of how Brain writes, verifies, and activates new agent skills — and the companion **context rot post** that names the failure mode it is designed to solve.



Perplexity announced on November 18, 2026 that its Brain personalization system can now automatically create and update reusable agent skills from session experience, without altering model weights.

Brain's self-improvement process operates through four sequential stages: Evidence, Reflection, Verification, and Activation.

In an eight-week randomised test, 72.9% of users with Brain got a new personal skill, against 6.5% who added one manually, with tool-call failures down 11%.

 The differential between 72.9% automatic and 6.5% manual adoption is the interaction-design signal that matters most: manual skill creation is a configuration task that requires users to know what they want to configure; Brain-authored skill creation is an observation-and-extraction task that requires only that the user complete work. The gap between the two adoption rates is the gap between "users who understand and engage with the configuration surface" and "users whose work patterns are legible enough for the agent to infer the skill."

The trust-design architecture within Brain's loop is the dual-track approval model: 

while personal skills adapt to individual workflows, shared built-in skills distributed to every Perplexity Computer user must pass paired replay against historical failure scenarios plus human engineer review before any update ships to production.

Because the harness loads an index of all available skills at the start of each session, a large library of skills can clog the context window and make it harder for the agent to find and load relevant skills

 — the reason Brain caps personal skills at 10 per user. 

The Plugins tab shows available skills, identifies those authored by Brain, and lets users choose which skills are enabled.

 The companion **context rot** research published November 18 addresses the structural reason all of this architecture is necessary: 

a guide to what builds up in an AI agent's context, why it hurts accuracy, and how to set up tasks that stay reliable.

 Context rot and self-improving skills are the two sides of the same long-running-agent reliability problem — skills that compress recurring workflows reduce the amount of redundant context that must be carried, while the cap on skill library size prevents the solution from becoming its own context-budget problem.

---

### Grok (xAI): Build 1.0.89 and the Hooks Legibility Upgrade

xAI's most significant interaction-design advance in this window is **Grok Build 1.0.89** — which shipped November 17 and reached broad developer attention in this window — delivering a cluster of terminal legibility and session-management improvements that collectively close the most persistent usability gaps in the agentic coding TUI.



Grok Build 1.0.89 adds a new /rename command on the dashboard that renames the selected session without opening it, a new /models command that refreshes the available model list from the server, and /hooks rows now show the hook file name and list settings in readable fields instead of dumping raw commands.

 The `/hooks` legibility upgrade is the trust-design advance that most directly parallels Claude Code 2.1.329's hook-provenance warning: in both products, the week of November 17–20 sees explicit moves toward making hook configuration human-readable in the terminal — translating agent permission architecture from raw command strings into auditable, operator-legible summaries. When hook configurations are readable, operators can verify that the hooks active in their session are the ones they intended to configure; when they are raw commands, verification requires parsing syntax rather than reading intent.



The release also adds: /mcps now shows hosted sections expanded by default unless they contain more than ten servers; Enter on a workflow in the /workflows list now opens its file for viewing and searching; grok mcp disable (and enable) now correctly stops servers inside already-running TUI sessions; and grok inspect now reports the correct project config file for project-defined MCP servers.

 The in-session MCP disable fix is the agentic-reliability advance within the release: an MCP server that cannot be disabled without restarting the TUI session is an MCP server that cannot be contained in response to an unexpected behaviour during a live agent run. Enabling disable within a running session closes a governance gap that existed between "configuring the agent before a task" and "responding to the agent during a task."



The update also removes internal experiment IDs and config files from grok update output

 — a micro-trust-design detail that matters for enterprise deployments where update logs are part of an audit trail: internal experiment IDs in production update output expose internal instrumentation to operators who have no context for interpreting it, and whose audit logs it clutters.

---

## The Bigger Picture: Gemini Takes the Desktop, Dots Reach Plus, and Brain Rewrites Itself

The 48 hours ending November 20, 2026 crystallise a single macro movement that the week's briefings have been building toward: **the moment when ambient desktop agency — an AI that works in the background while you use your computer — stops being a feature category defined by a single product and becomes a surface that every major platform has shipped, is shipping, or is actively architecting toward.** Google's Gemini Computer Use for Mac is the most explicit expression: an agent that navigates native Mac apps and websites in an isolated background window, with a live preview in chat, selective folder access, and automatic file backups — a trust architecture that replicates, nearly exactly, the same design decisions that Claude Code's terminal-session model and ChatGPT Work's cloud-execution environment have independently converged on. That convergence is the interaction-design signal of the window: the industry has arrived at a stable answer to the question "how should a desktop agent behave?" and that answer is background execution with explicit scope, action-preview transparency, and user-side pause and approval controls. What is not yet converged is the question of what happens when these agents start writing their own operating knowledge: Perplexity's Brain disclosure reveals a four-stage self-improvement loop that produced 72.9% skill adoption versus 6.5% manual, with a dual-track approval gate for personal versus shared skills — the most detailed public architecture for self-rewriting agent behaviour in the category. OpenAI's dots reaching Plus users and getting their own mobile tab, with proactive health suggestions from connected Health data, adds a consumer-tier dimension to the same theme: an agent that knows your calendar, your health metrics, and your sleep patterns, operating persistently in the background, is an agent whose trust architecture is no longer primarily about action-approval gates and is increasingly about data-access scope, training-opt-out defaults, and skill-curation interfaces. The Grok Build 1.0.89 and Claude Code 2.1.329 hook-legibility improvements — both shipping in this window, neither coincidentally — are the developer-infrastructure reflection of the same pressure: as agents run longer, write their own configurations, and operate with less per-action supervision, the ability to read, audit, and constrain the agent's permission layer in plain language becomes the trust primitive that matters most. The industry that spent October building approval gates for individual actions is now building legibility infrastructure for agent configuration itself.

---

## References

[1] blog.google. (2026). *Automate Mac tasks with Gemini computer use*. [https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/](https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/)

[2] techcrunch.com. (2026). *Google gives Gemini the ability to use your Mac for you*. [https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/](https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/)

[3] unite.ai. (2026). *Google Adds Computer Use to Gemini on Mac for Multi-Step Tasks*. [https://www.unite.ai/google-adds-computer-use-to-gemini-on-mac-for-multi-step-tasks/](https://www.unite.ai/google-adds-computer-use-to-gemini-on-mac-for-multi-step-tasks/)

[4] pasqualepillitteri.it. (2026). *Google Launches Computer Use in Gemini for Mac, Running Tasks in the Background*. [https://pasqualepillitteri.it/en/news/35373/google-launches-computer-use-in-gemini-for-mac-running](https://pasqualepillitteri.it/en/news/35373/google-launches-computer-use-in-gemini-for-mac-running)

[5] powerfulai.tools. (2026). *Gemini 4 Neon: Google's New Mid-Tier AI Model (2026)*. [https://www.powerfulai.tools/blog/gemini-4-neon-google-ai-model-launch-2026](https://www.powerfulai.tools/blog/gemini-4-neon-google-ai-model-launch-2026)

[6] seroundtable.com. (2026). *Google AI Mode Drops Gemini Label & Rolls Out Gemini 4 Carbon To Pro Subs*. [https://www.seroundtable.com/google-ai-mode-drops-gemini-label-42540.html](https://www.seroundtable.com/google-ai-mode-drops-gemini-label-42540.html)

[7] help.openai.com. (2026). *ChatGPT release notes — November 19, 2026*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[8] neowin.net. (2026). *OpenAI is giving the ChatGPT mobile app a major redesign*. [https://www.neowin.net/news/openai-is-giving-the-chatgpt-mobile-app-a-major-redesign/](https://www.neowin.net/news/openai-is-giving-the-chatgpt-mobile-app-a-major-redesign/)

[9] digitaltrends.com. (2026). *ChatGPT is getting a new look on your phone, and your dot now has its own tab*. [https://www.digitaltrends.com/computing/chatgpt-new-mobile-design/](https://www.digitaltrends.com/computing/chatgpt-new-mobile-design/)

[10] digg.com. (2026). *ChatGPT dots inch into Plus, with a mobile tab makeover for eligible Pro users*. [https://digg.com/ai/w150f7m9](https://digg.com/ai/w150f7m9)

[11] 9to5mac.com. (2026). *ChatGPT Health feature now works with Mac app, Dots, more*. [https://9to5mac.com/2026/11/19/chatgpt-health-feature-will-soon-work-with-mac-app-dots-more/](https://9to5mac.com/2026/11/19/chatgpt-health-feature-will-soon-work-with-mac-app-dots-more/)

[12] aiweekly.co. (2026). *OpenAI expands ChatGPT Health to Mac, Android, Dots, Sites*. [https://aiweekly.co/alerts/openai-expands-chatgpt-health-to-mac-android-dots-sites](https://aiweekly.co/alerts/openai-expands-chatgpt-health-to-mac-android-dots-sites)

[13] community.openai.com. (2026). *GPT-Live-1.1 has arrived in the API*. [https://community.openai.com/t/gpt-live-1-1-has-arrived-in-the-api/1418537](https://community.openai.com/t/gpt-live-1-1-has-arrived-in-the-api/1418537)

[14] aiweekly.co. (2026). *OpenAI opens GPT-Live-1.1 to API with $0.02/min standby*. [https://aiweekly.co/alerts/openai-opens-gpt-live-11-to-api-with-002min-standby](https://aiweekly.co/alerts/openai-opens-gpt-live-11-to-api-with-002min-standby)

[15] dev.to. (2026). *OpenAI Just Put GPT-Live-1.1 in the API, and Idle Voice Sessions Are Now 60% Cheaper*. [https://dev.to/paullovelace/openai-just-put-gpt-live-11-in-the-api-and-idle-voice-sessions-are-now-60-cheaper-4oik](https://dev.to/paullovelace/openai-just-put-gpt-live-11-in-the-api-and-idle-voice-sessions-are-now-60-cheaper-4oik)

[16] developers.openai.com. (2026). *Changelog — November 2026*. [https://developers.openai.com/api/docs/changelog](https://developers.openai.com/api/docs/changelog)

[17] learn.chatgpt.com. (2026). *ChatGPT & Codex changelog*. [https://learn.chatgpt.com/docs/changelog](https://learn.chatgpt.com/docs/changelog)

[18] github.com/anthropics/claude-code. (2026). *Release v2.1.329*. [https://github.com/anthropics/claude-code/releases/tag/v2.1.329](https://github.com/anthropics/claude-code/releases/tag/v2.1.329)

[19] github.com/715494637. (2026). *Release Claude Code v2.1.329*. [https://github.com/715494637/claude-code-update/releases/tag/2.1.329](https://github.com/715494637/claude-code-update/releases/tag/2.1.329)

[20] claudeupdates.dev. (2026). *Update Claude Code to v2.1.329*. [https://www.claudeupdates.dev/update](https://www.claudeupdates.dev/update)

[21] news.microsoft.com. (2026). *Microsoft Ignite 2026 Live News*. [https://news.microsoft.com/events/ignite/2026/live-news/](https://news.microsoft.com/events/ignite/2026/live-news/)

[22] letsdatascience.com. (2026). *Microsoft Releases Copilot SDK 2.0 With Multi-Tenant Rust Runtime*. [https://letsdatascience.com/news/microsoft-releases-copilot-sdk-20-with-multi-tenant-rust-run-6f4f526d](https://letsdatascience.com/news/microsoft-releases-copilot-sdk-20-with-multi-tenant-rust-run-6f4f526d)

[23] winbuzzer.com. (2026). *Microsoft Copilot SDK 2.0 Enables Shared Use of AI Agents in the Same Environment*. [https://winbuzzer.com/2026/11/19/microsoft-copilot-sdk-2-0-lets-apps-run-ai-agents-in-one-process-xcxwbn/](https://winbuzzer.com/2026/11/19/microsoft-copilot-sdk-2-0-lets-apps-run-ai-agents-in-one-process-xcxwbn/)

[24] witivio.com. (2026). *Microsoft Ignite 2026 Announcements: Full Recap and Analysis*. [https://www.witivio.com/en/blog/microsoft-ignite-2026-announcements/](https://www.witivio.com/en/blog/microsoft-ignite-2026-announcements/)

[25] microsoft.com. (2026). *Microsoft Ignite 2026: Introducing Dynamics 365 in Copilot*. [https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/11/17/microsoft-ignite-2026-introducing-dynamics-365-in-copilot/](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/11/17/microsoft-ignite-2026-introducing-dynamics-365-in-copilot/)

[26] copilot-coaching.de. (2026). *Copilot Managed Runtime Explained: Run Copilot Apps Securely*. [https://www.copilot-coaching.de/en/blog/copilot-managed-runtime-explained/](https://www.copilot-coaching.de/en/blog/copilot-managed-runtime-explained/)

[27] perplexity.ai. (2026). *Self-improving skills*. [https://www.perplexity.ai/hub/blog/self-improving-skills](https://www.perplexity.ai/hub/blog/self-improving-skills)

[28] unite.ai. (2026). *Perplexity Brain Creates and Updates Agent Skills From Experience*. [https://www.unite.ai/perplexity-brain-creates-and-updates-agent-skills-from-experience/](https://www.unite.ai/perplexity-brain-creates-and-updates-agent-skills-from-experience/)

[29] fourweekmba.com. (2026). *Perplexity Brain Writes Skills for 72.9% of Users vs 6.5%*. [https://fourweekmba.com/ai-perplexity-brain-writes-skills-for-72-9-of-users-vs-6-5/](https://fourweekmba.com/ai-perplexity-brain-writes-skills-for-72-9-of-users-vs-6-5/)

[30] futurumgroup.com. (2026). *Perplexity's Brain Learns on the Job: Self-Improving Agent Skills*. [https://futurumgroup.com/insights/perplexitys-brain-learns-on-the-job-self-improving-agent-skills/](https://futurumgroup.com/insights/perplexitys-brain-learns-on-the-job-self-improving-agent-skills/)

[31] ashutoshai.com. (2026). *Google brings Genie 4 to the Gemini API as OpenAI ships GPT-Live-1.1 · AI Compass*. [https://ashutoshai.com/ai-compass/2026/11/19/](https://ashutoshai.com/ai-compass/2026/11/19/)

[32] x.ai. (2026). *Grok Build Changelog*. [https://x.ai/changelog/build](https://x.ai/changelog/build)

[33] releasebot.io. (2026). *xAI Release Notes — November 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[34] releasebot.io. (2026). *OpenAI Release Notes — November 2026*. [https://releasebot.io/updates/openai](https://releasebot.io/updates/openai)