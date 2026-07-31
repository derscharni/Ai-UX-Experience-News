# UX Briefing: Infrastructure Outages, Generative UI Canvases, and the Hardware Agent Frontier

**July 31, 2026**

Good morning. The 48 hours ending July 31 are shaped by four stories that each expose a different seam in the agent-to-human interface stack: **Anthropic** is recovering from back-to-back network failures on July 29–30 that produced the industry's most concentrated display yet of how load-bearing agentic infrastructure — specifically Claude Code — has become for daily engineering work, with 155 outages logged since January 2026 raising an urgent trust-design question about status transparency and user recourse during mid-task failures; **xAI** ships the single most consequential generative-UI move of the month with **Grok Build Mode** launching July 28 — a conversational app-creation surface that keeps a live, iterative artifact running inside the chat window and publishes to a `grok.me` domain or custom domain without requiring users to touch code, while simultaneously completing **Tesla's 2026 Summer Update (v2026.26)** which transitions Grok from a screen-bound chatbot to a hardware-control voice agent with access to phone calls, climate, music, and the glovebox; **OpenAI** extends its identity surface into the third-party ecosystem with **Sign in with ChatGPT** entering beta on July 29 across Airtable, GitLab, HubSpot, Notion, Supabase, and Vercel — the first time ChatGPT has operated as an OAuth identity provider at consumer scale — alongside the **ChatGPT for Academic Researchers** workspace; and **Google** ships **Gemini CLI v0.53.0** on July 28 with hardened security, anti-prompt-injection loop mitigations, and workspace trust enforcement in its A2A server, the most security-focused agent CLI release any platform has shipped this month.

---

## At a Glance: July 31 Highlights

The releases in this window collectively surface the three hardest problems in agentic UX design right now: how to maintain user trust and task continuity when always-on infrastructure fails; how to design the interaction model for agents that generate live, editable artifacts inside the conversation itself; and how to safely extend an AI agent's action-boundary from answering questions to controlling physical or third-party systems.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code / claude.ai outage July 29–30** — two separate network failures in 24 hours produce 529 Overloaded errors across claude.ai, API, Claude Code, and Claude Cowork; full recovery by late July 30; Claude for Government stays online throughout; 155 Claude outages logged since January 2026; **legacy Workbench sunset** August 17; **mid-conversation tool-changes** beta live on Fable 5, Opus 5. [1][2][3] |
| **ChatGPT** | **Sign in with ChatGPT** beta rolls out July 29 across Airtable, GitLab, HubSpot, Notion, Supabase, and Vercel — ChatGPT as OAuth identity provider; **ChatGPT for Academic Researchers** launches with 12-month Pro-tier team workspaces; **Atlas** deprecation confirmed August 9 with browser capabilities folding into ChatGPT and Codex. [4][5][6] |
| **Google Gemini** | **Gemini CLI v0.53.0** ships July 28 — fixes infinite ReAct loops and prompt injection vulnerabilities, enforces workspace trust and task isolation in the A2A server, aligns macOS Seatbelt profiles with deny-default model; **Gemini Omni** now live inside Google Vids for in-video generation and text-based edits. [7][8][9] |
| **Microsoft Copilot** | **Copilot Search** shorter, scannable summaries rolling July–August; **Outlook email references** coming to Copilot Notebooks; **Agent Store governed publishing** live — admins review, approve, and publish org-built agents; **MCP agent access** now spanning Word, Excel, PowerPoint, Outlook, and Catalyst; **Edge v149** unified design language aligning with Copilot and Bing visual system. [10][11][12] |
| **Grok (xAI)** | **Grok Build Mode** launches July 28 in Early Beta (SuperGrok Heavy) — conversational app creation with live preview inside chat, publish to grok.me or custom domain; source export to GitHub; interactive dashboards with live data connectors; **Grok Build CLI TUI** improvements: /session-info auth display, in-TUI /doctor fix, 1-hour command timeouts; **Grok 4.6** confirmed ~August 7. [13][14][15] |
| **Perplexity** | **Computer inside Microsoft 365** now live across Word, Excel, PowerPoint, Outlook, and Teams — Deep Research integrated into Computer; **Source Context Panel** and inline citations for mid-task traceable claims; **Samsung Galaxy S26 integration** — Perplexity powers Bixby real-time web search and extends Comet agentic browsing into Samsung Internet. [16][17][18] |
| **Tesla (xAI)** | **Tesla 2026 Summer Update (v2026.26)** rolling out — Grok expands from chatbot to vehicle hardware agent: phone calls, music, climate, glovebox control by voice; Preferred Routes learns driving patterns; first complete hardware-control handoff to Grok; restricted to AMD Ryzen infotainment on current fleet. [19][20][21] |

---

## Product Highlights

### Claude / Anthropic: The Outage Pattern, the Trust-Design Gap, and the Mid-Conversation Tool-Change Beta

Anthropic's most UX-consequential 48 hours are not defined by a product launch but by the absence of one: 

two separate network failures over July 29–30, 2026 cut into Anthropic's capacity to serve Claude, producing elevated errors and reduced availability across claude.ai, the API, Claude Code, and Claude Cowork.

Services were fully recovered by late July 30; Claude for Government stayed online throughout, as it runs on isolated infrastructure separate from the consumer and developer surfaces that took the hit.



The trust-design significance of this incident is not in its severity but in its frequency. 

The disruption triggered more than 2,000 outage reports, with roughly half tied to Claude Code specifically; Anthropic began investigating at 7:49 p.m. UTC and identified the issue by 8:33 p.m. UTC, though the company did not disclose the underlying cause or give a recovery timeline during the incident.

 The pattern that matters is the aggregate: 

according to outage-tracking service StatusGator, Claude has experienced 155 reported outages since January 2026 alone.

2026 has been a rough year for trusting the dashboard; none of these incidents individually is catastrophic, but the frequency is what's notable.

 For users running multi-hour agentic sessions in Claude Code — the kind of long-horizon background work that the platform is explicitly designed for — a mid-task 529 error is not an inconvenience, it is a trust event: it transforms a delegated autonomous workflow into an interrupted state where the user must re-establish context, re-verify what the agent completed, and decide whether to restart or resume. 

Anthropic has attributed earlier outages to demand outpacing compute capacity, driven by enterprise adoption of Claude Code and surging consumer signups.

 The design implication is structural: at the scale Claude is now operating, the status page, the incident response UX, and the session-recovery interaction model for Claude Code are trust-design surfaces as consequential as any feature launch.

On the developer-platform side, the most interaction-design-significant change shipping in this window is the **mid-conversation tool-changes beta**. 

Mid-conversation tool changes are now in beta on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 5 — developers can now add or remove tools between turns of a conversation while preserving the prompt cache, accessed via a beta header.

 This is the per-turn least-privilege primitive that enterprise security teams have been waiting for: rather than binding a full tool-set at session initialisation and leaving it static, the conversation's active tool access can now be narrowed or expanded turn-by-turn based on what the current task actually requires. The combination of that capability with the 

legacy Workbench retirement — access ending August 17, 2026, with users able to export saved prompts, variables, and evals before the updated Workbench replaces the old tools

 — signals that Anthropic is actively rationalising its developer surface at the same time its production infrastructure is under capacity pressure. Both changes point in the same direction: a more minimal, more disciplined developer platform for a product that is now operating at a scale where every unnecessary surface creates both cognitive overhead and a potential failure mode.

---

### ChatGPT / OpenAI: Sign in with ChatGPT and the Identity Layer Expansion

OpenAI's most structurally significant UX release in this 48-hour window is not a capability feature but an identity-layer move that extends ChatGPT's surface far beyond the chat interface: **Sign in with ChatGPT**, entering beta on July 29. 

When users connect a supported app from the plugin directory, they can use Sign in with ChatGPT to create or link an account with that service in fewer steps; on participating partner sites, users can also choose 'Sign in with ChatGPT' to create or access their account.

Sign in with ChatGPT is beginning to roll out in beta across select plugins and partner sites, starting with Airtable, GitLab, HubSpot, Notion, Supabase, and Vercel.

 The interaction-design significance of this launch is the direction of the identity relationship it establishes: rather than ChatGPT being a thing users sign into, it becomes a thing users sign in *with* — flipping the dependency graph so that OpenAI's user identity sits above the third-party app layer, not below it. Apple, Google, and Microsoft have operated this model for years; the UX design question for OpenAI is how the ChatGPT identity maps to the agentic permissions model that Codex and Work are building. 

When users sign in, only their name, email, and profile picture are shared with the partner — users still separately review and approve

 tool and data permissions. That explicit permission separation is the right trust-design pattern: the identity handshake and the capability-delegation handshake are distinct consent events, not bundled in one click.

The second major July 29 release is **ChatGPT for Academic Researchers**, which is a workspace-design story as much as an access story. 

ChatGPT for Academic Researchers gives faculty and postdoctoral researchers the ability to apply for 12 months of complimentary access to a dedicated ChatGPT workspace for a small, verified team; each workspace supports up to five members and includes business data protections and ChatGPT Pro-level usage limits, helping researchers collaborate while keeping team research in its own workspace.

 The workspace-isolation architecture — team research in a bounded, business-data-protected environment — is the pattern that makes the research-assistance use case governable: it mirrors the enterprise workspace design rather than giving researchers raw personal-account access. This is the trust-design choice that allows institutional adoption rather than individual workarounds. Meanwhile, 

Atlas is deprecated as OpenAI brings browser-based agentic capabilities into ChatGPT and Codex, with Atlas scheduled to stop working on August 9, 2026.

 The surface consolidation — one agent-aware desktop application rather than two parallel browser/agent products — is the same interaction-design decision that Perplexity made when folding Computer into Comet, and that Microsoft made when building MCP agent access into Office rather than maintaining a separate agent shell.

---

### Google Gemini: Gemini CLI v0.53.0 and the Security-First Agent Runtime

Google's most UX-consequential release in this window is not a consumer feature but a developer-facing security hardening that addresses the exact failure modes that make autonomous agent loops dangerous in production: **Gemini CLI v0.53.0**, shipping July 28 as the latest stable release, delivers a cluster of fixes that directly address the trust-design problems of always-on, tool-calling agent runtimes.



Gemini CLI ships v0.53.0 with stronger core reliability and security, including fixes for cancelled tool responses, infinite ReAct loops, workspace trust, and credential fallback, plus a new eval coverage report command and updated macOS Seatbelt profiles.

 Each of these is worth examining individually as a trust-design primitive. The infinite ReAct loop fix — 

coalescing consecutive message roles and grouping cancelled tool responses to avoid Bad Request errors, and mitigating infinite ReAct loops and prompt injection vulnerabilities

 — is the most consequential: a CLI agent that can loop indefinitely on a bad tool response is one that can silently consume resources and take unintended actions with no human visible signal that something has gone wrong. Surfacing this as an explicit fix in the stable release changelog, rather than a silent patch, is the right transparency choice. 

The security and sandboxing changes align macOS permissive Seatbelt profiles with the deny-default model, and enforce workspace trust with task isolation in the A2A server

 — moving the default posture from permissive-with-exceptions to deny-with-explicit-allowances, which is the governance pattern that makes agent runtimes auditable rather than emergent. The 

new eval coverage report command introduces a way to generate coverage reports that track agent decision logic and testing

 — the observability primitive that allows developers to understand which parts of an agent's decision graph have been exercised and which remain untested in production.

On the consumer Gemini surface, 

Gemini adds Omni directly in Google Vids, bringing higher-quality video generation and simple text-based video edits; users can improve realism, text rendering, and physics, or ask Gemini to change style, color grading, and even remove background noise.

 The Vids integration is the generative-UI pattern applied to video: rather than requiring users to navigate to a separate generation tool, the model is embedded in the editing surface where the work already lives. The UX shift is from generation-then-import (generate elsewhere, bring it in) to generation-in-context (ask the model to change what you are already looking at), which is the same interaction pattern that Grok Build Mode applies to app creation and that Microsoft Copilot applies to document generation — the emerging consensus that the most trusted generative AI UX is one that never makes users leave the surface they already inhabit.

---

### Microsoft Copilot: Agent Store Governance, MCP Breadth, and the Edge Visual Unification

Microsoft's most UX-consequential structural development in this window is the arrival of the **Agent Store governed publishing** flow, completing the governance architecture that makes enterprise-scale agent discovery safe rather than chaotic. 

Customers can submit agents built in Agent Builder to the Agent Store under the 'Built by your org' section, after admin review and approval in the Microsoft 365 Admin Center; this governed flow enables admins to review, approve, and publish submitted agents so they can be discovered and used by others in the Agent Store, helping organisations share validated agents at scale while maintaining quality and governance.



The interaction-design significance of this flow is the trust architecture it establishes between individual agent builders and the broader organisation. Without a governed publishing layer, an Agent Store becomes a shadow-IT surface: capable users build agents that colleagues find, adopt, and trust without any organisational validation of their safety, accuracy, or data-access scope. The admin-review gate converts the Agent Store from a feature directory into a governed capability catalogue — the same pattern that Apple's App Store Review established for consumer software, applied to enterprise agent workflows. Alongside this, 

Microsoft Copilot adds governed agent publishing, tenant-wide prompt galleries, and broader MCP agent access across Word, Excel, PowerPoint, Outlook, and Catalyst.

 The MCP access breadth across the full Office suite is the infrastructure event that makes every third-party MCP server that developers have been building relevant to enterprise Copilot deployments — a single MCP connection can now surface inside Word, Excel, and Outlook without requiring a separate integration for each surface.



Microsoft Edge will update its look and feel to give customers a unified experience across all Microsoft AI surfaces including Copilot and Bing; Edge version 149 introduces a refreshed interface that aligns with the design language used in Copilot and Bing, with changes including updated spacing, rounded corners, new font styles, and revised default color schemes.

 This visual unification is the design-system event that matters for the broader Copilot estate: as users encounter Copilot in Edge, in the M365 app, in Outlook, and in Teams — with different models and different agent types — a consistent visual system is the baseline legibility layer that makes the multi-surface experience feel coherent rather than assembled from separate products. 

This unified design enhances consistency across Microsoft AI products without affecting browser functionality or security settings, and the update aims to create a cohesive experience across Microsoft AI tools, reducing user confusion and improving visual comfort.



---

### Grok (xAI): Build Mode, the Live-Preview Generative UI Pattern, and What It Changes for Creation UX

xAI's most UX-significant release in this window — and the most consequential generative-UI event of the 48-hour period — is **Grok Build Mode**, launching July 28 in Early Beta and introducing an interaction pattern that the industry has been approaching from multiple directions: the live-artifact canvas embedded inside a conversation, with continuous iterative refinement and instant publication.



On July 28, 2026, Build Mode entered Early Beta for SuperGrok Heavy subscribers on grok.com, iOS, and Android; users tell Grok an idea, and it builds a working version live in the chat, on web or phone; when ready, users can publish it to a link anyone can open.

 The interaction-design novelty is the in-conversation persistence: 

unlike "paste this React," Build Mode keeps the artifact running in the conversation.

Users describe an idea in chat, and Build Mode generates the code while displaying a working preview inside the conversation; the preview updates as users refine layouts, add features, or restyle the interface through additional prompts, with no development tools or technical setup required.

 This is the generative UI loop at the consumer level: prompt, preview, refine, publish — all within a single conversational thread, with the artifact itself as the persistent context object rather than the chat history.



Build Mode supports landing pages, portfolios, business sites, productivity tools such as planners and calculators, arcade and 3D games, and interactive dashboards; the dashboard feature includes connectors that allow Grok to pull in external data and display it as live charts or filterable views.

 The live data connector support is the trust-design boundary worth watching: 

when Build Mode ships connector-backed dashboards that survive a real auth review, that is the moment it stops being a toy and starts competing with hosted app builders on serious internal tools.

 The current state — Early Beta, SuperGrok Heavy gate, no publicly documented data-retention policy for published apps — is the transparency gap that will need closing before enterprise adoption is meaningful. 

Source code can be exported to GitHub, effectively turning Build Mode into a starter generator rather than a walled garden

 — the escape-hatch design that prevents creation-surface lock-in and is the right trust pattern for a developer-adjacent audience.

On the Grok Build CLI side, the TUI improvements shipping alongside Build Mode address the day-to-day reliability of the agent developer experience. 

Users can now run `grok doctor fix` commands directly from inside the TUI instead of only from the CLI; `/session-info` now displays whether the session uses OAuth or an API key and where to manage the account; `!cmd` commands now allow up to one hour before timing out.

 The `/session-info` auth transparency is the trust-design detail that matters most: in a session that can touch repositories, run commands, and access Marketplace connectors, surfacing the authentication type — OAuth vs. API key — and the account management path within the session context is the provenance signal that makes the agent's access model legible to the user who is delegating work to it.

---

### Tesla (xAI): Grok Crosses the Hardware-Control Threshold

The single most interaction-design-consequential event involving Grok in this 48-hour window is not a software feature but a physical-world access expansion: **Tesla's 2026 Summer Update (v2026.26)**, rolling out globally since July 26, completes the transition of Grok from a screen-bound conversational assistant to a vehicle hardware control agent.



Tesla began pushing software version 2026.26 to its global fleet on July 26, and the headline change is one the company's voice assistant has been building toward for a year: Grok can now control the car's hardware by voice.

Drivers can now use voice commands to place phone calls, search and play music, adjust climate settings, open the glovebox, search through the Controls menu, and ask questions about the vehicle or the latest software update.

 The interaction-design significance of this hardware-control handoff cannot be overstated: for the first time, a major frontier AI assistant has been granted direct, OTA-delivered control over physical systems in a deployed consumer product fleet. 

When Tesla first added Grok in July 2025, the assistant couldn't actually control any vehicle functions — it was a chatbot bolted onto the screen; Tesla started closing that gap with the "Hey Grok" wake word in the Spring Update 2026, and now Grok handles calls, media, climate, and the glovebox by voice.



The trust-design architecture of this control expansion reveals both the design intent and its current limits. 

Features restricted to AMD Ryzen vehicles — the expanded Grok Commands, Caraoke scoring, and browser camera and microphone support — are not available on older Intel-based cars.

 The hardware-gate is the access-boundary design that prevents the AI control layer from being deployed to hardware that cannot support the latency and reliability requirements of real-time vehicle command execution — a least-privilege constraint applied at the chip level rather than the software level. 

Grok is no longer just an AI chatbot sitting inside the infotainment system; with this update, Tesla is letting the assistant touch more of the vehicle experience, from media and phone calls to climate settings and the glovebox.

 The deeper design question — what happens when a voice command is ambiguous, misheard, or executed at an unsafe moment — is the interaction pattern that every in-vehicle voice agent will need to resolve explicitly before hardware-control delegation becomes a universal default rather than an opt-in capability.

---

### Perplexity: Computer in Microsoft 365, Samsung Integration, and the Source-Traceability Standard

Perplexity's most significant UX developments in this window consolidate two distribution wins that each address a different dimension of the agentic work pipeline: the full deployment of **Computer inside Microsoft 365** across Word, Excel, PowerPoint, Outlook, and Teams, and the **Samsung Galaxy S26 integration** bringing Perplexity's capabilities into Bixby and Samsung Internet at the platform level.



Perplexity adds Computer inside Microsoft 365 apps, bringing AI workflows to Word, Excel, PowerPoint, Outlook, and Teams; it also adds usage analytics, a new context panel for live task tracking, and answers with sources and inline citations for traceable claims.

 The inline citation pattern — sources surfaced mid-task as the agent works, not delivered as a footnote to the final output — is the trust primitive that makes Computer's output verifiable during the workflow rather than after it. 

Deep Research is now integrated into Computer; faster command panel and inline actions improve workflows; new enterprise controls include analytics APIs and custom credit limits.

 The Deep Research integration is the workflow primitive that closes the research-to-action loop within a single agent surface: a user can ask Computer to run a multi-source research workflow and turn the findings directly into an Excel model or PowerPoint presentation without switching contexts or manually transferring data.



Perplexity APIs now power Bixby and Samsung Internet: Samsung's Galaxy S26 is the first smartphone to integrate Perplexity's APIs at the platform level; Bixby now uses Perplexity for real-time web search and advanced reasoning, delivering accurate, up-to-date answers grounded in the latest information; Perplexity's capabilities also extend to Samsung Internet, bringing agentic browsing capabilities from the Comet browser, with Perplexity available as an optional default search engine.

 The Samsung integration is the distribution pattern worth examining: rather than acquiring users through a standalone app, Perplexity is embedding its agent capabilities into the default AI layer of a billion-device hardware platform. This is the ambient-agent deployment model — the agent capability arrives pre-installed on the device, not as an app the user chooses to download — and it raises the same transparency design questions that all ambient integrations raise: how clearly does the user understand which intelligence is responding, what data it has access to, and how to change or disable it?

---

## The Bigger Picture: Infrastructure Outages, Generative UI Canvases, and the Hardware Agent Frontier

The 48 hours ending July 31, 2026 are defined by a single converging pressure that every platform in this window is confronting from a different angle: the gap between what AI agents are now capable of doing and the trust infrastructure that makes delegating that capability feel safe and recoverable. Anthropic's back-to-back outages are the most visible manifestation — 155 incidents since January, demand outrunning capacity, and a status-page UX that users routinely discover provides less real-time information than community-tracking services — but they are a symptom of an industry-wide condition: agentic AI has become load-bearing infrastructure for engineering teams and knowledge workers before the reliability, observability, and incident-response design that load-bearing infrastructure requires has been built. Grok's Build Mode is the generative-UI answer to that capability-vs-trust gap in the creation layer: by keeping the artifact alive and editable inside the conversation, with a GitHub export escape hatch and a publishable URL, it builds a creation loop that is both more capable than a prompt-to-code generator and more transparent about what was produced, because the output is visible and iterative rather than hidden inside a code editor. Tesla's Summer Update is the most dramatic embodiment of the same underlying design challenge: the moment Grok's action-boundary crosses from answering questions to opening the glovebox, the entire trust architecture of the human-agent relationship must be re-evaluated — who confirms the command, how ambiguity is resolved, what happens when the agent acts on a misheard instruction while the car is in motion. OpenAI's Sign in with ChatGPT, Google's ReAct-loop security hardening, and Microsoft's Agent Store admin-review gate all make the same argument from the identity, security, and governance layers respectively: the UX of agentic AI is now inseparable from the infrastructure of trust that surrounds it, and the platforms that build that infrastructure first — legible failure states, recoverable sessions, auditable actions, transparent identity — are the ones that will earn the delegation that their agents are already technically capable of handling.

---

## References

[1] ExplainX AI. (2026). *Claude Outage July 29–30, 2026 — What Broke, Fixed*. [https://explainx.ai/blog/claude-outage-network-failures-recovery-july-2026](https://explainx.ai/blog/claude-outage-network-failures-recovery-july-2026)

[2] IBTimes UK. (2026). *Another Claude Outage Hits Anthropic: Is This Becoming a Recurring Pattern Throughout 2026?* [https://www.ibtimes.co.uk/claude-ai-faces-repeated-outages-1811601](https://www.ibtimes.co.uk/claude-ai-faces-repeated-outages-1811601)

[3] Releasebot. (2026). *Claude Developer Platform Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-developer-platform](https://releasebot.io/updates/anthropic/claude-developer-platform)

[4] Releasebot. (2026). *ChatGPT Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[5] OpenAI. (2026). *Release Notes — ChatGPT*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[6] OpenAI Help Center. (2026). *ChatGPT Business Release Notes*. [https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes)

[7] Releasebot. (2026). *Gemini CLI Updates by Google — July 2026*. [https://releasebot.io/updates/google/gemini-cli](https://releasebot.io/updates/google/gemini-cli)

[8] Gemini CLI. (2026). *Latest stable release: v0.53.0*. [https://geminicli.com/docs/changelogs/latest/](https://geminicli.com/docs/changelogs/latest/)

[9] Releasebot. (2026). *Gemini Updates by Google — July 2026*. [https://releasebot.io/updates/google/gemini](https://releasebot.io/updates/google/gemini)

[10] Releasebot. (2026). *Microsoft Copilot Updates by Microsoft — July 2026*. [https://releasebot.io/updates/microsoft/microsoft-copilot](https://releasebot.io/updates/microsoft/microsoft-copilot)

[11] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[12] WSU ITS. (2026). *Microsoft 365 Copilot receives interface updates in July 2026*. [https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/](https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/)

[13] xAI. (2026). *Introducing Build Mode*. [https://x.ai/news/grok-build-mode](https://x.ai/news/grok-build-mode)

[14] Releasebot. (2026). *Grok Build Updates by xAI — July 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[15] Basenor. (2026). *Grok Launches Build Mode: One-Prompt App Creation for SuperGrok Heavy*. [https://www.basenor.com/blogs/news/grok-launches-build-mode-one-prompt-app-creation-for-supergrok-heavy](https://www.basenor.com/blogs/news/grok-launches-build-mode-one-prompt-app-creation-for-supergrok-heavy)

[16] Releasebot. (2026). *Perplexity Release Notes — July 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[17] Zentroai. (2026). *Perplexity AI July 2026 Update: New Comet Features*. [https://zentroai.in/perplexity-ai-july-2026-update/](https://zentroai.in/perplexity-ai-july-2026-update/)

[18] AlternativeTo/AndroidHeadlines. (2026). *SpaceXAI Launches Grok's Build Mode: Create Apps, Websites and Games Without Coding*. [https://www.androidheadlines.com/2026/07/spacexai-grok-build-mode-app-creation-launch.html](https://www.androidheadlines.com/2026/07/spacexai-grok-build-mode-app-creation-launch.html)

[19] TechTimes. (2026). *Grok Takes Control: Tesla's Summer Update Unlocks Voice Hardware Access*. [https://www.techtimes.com/articles/322008/20260729/grok-takes-control-teslas-summer-update-unlocks-voice-hardware-access.htm](https://www.techtimes.com/articles/322008/20260729/grok-takes-control-teslas-summer-update-unlocks-voice-hardware-access.htm)

[20] Electrek. (2026). *Tesla's 2026 Summer Update: auto navigation, Grok phone calls, Caraoke scoring, and more*. [https://electrek.co/2026/07/21/tesla-2026-summer-update-release-notes/](https://electrek.co/2026/07/21/tesla-2026-summer-update-release-notes/)

[21] Not a Tesla App. (2026). *Tesla Announces Summer Update: Grok Vehicle Commands, Preferred Routes, Add Vehicle Wraps in App and More*. [https://www.notateslaapp.com/news/4469/tesla-announces-summer-update-grok-vehicle-commands-preferred-routes-add-vehicle-wraps-in-app-and-more](https://www.notateslaapp.com/news/4469/tesla-announces-summer-update-grok-vehicle-commands-preferred-routes-add-vehicle-wraps-in-app-and-more)