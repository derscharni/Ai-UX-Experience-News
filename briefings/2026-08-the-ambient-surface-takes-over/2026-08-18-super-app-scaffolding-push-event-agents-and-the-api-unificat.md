# UX Briefing: Super App Scaffolding, Push-Event Agents, and the API Unification Wave

**August 18, 2026**

Good morning. The 48 hours ending August 18 are shaped by four overlapping design bets about where platforms draw the line between what an agent does invisibly and what it surfaces to a human — and by one retirement day that lands exactly on schedule. **Microsoft Copilot** executes the feature retirement wave it announced August 13: Group Chats, Podcasts, consumer Deep Research, and Mico all go dark today as account updates roll, completing the structural foundation for the Copilot Super App — a confirmed Q3 launch that will fold chat, coding, Cowork, and a new class of background agents called **Autopilots** into a single surface, with Entra Agent ID as the identity-governance backbone threading all of it together. **Claude/Anthropic** ships two significant interaction-layer changes in the same changelog window: a **Remote Control effort-level sync** that makes reasoning depth adjustable from any device without touching the terminal, and a major expansion of the **--channels** primitive that turns bidirectional MCP push events into a first-class ambient notification path for CI, monitoring, and messaging platforms feeding into live coding sessions. **Perplexity** crosses a platform consolidation threshold of its own: the **Sonar API officially becomes the Agent API** as of August 13, a unified programmable endpoint for web search, code execution, and MCP — with Sonar retiring September 27 — while the existing Computer-in-Teams integration deepens its workflow surface. And **Google Gemini Enterprise** extends its observability story with end-to-end tracing across data connector workflows, adding `execute_tool` and `invoke_connector` spans that make the full agent-to-third-party-API execution path inspectable for the first time in production.

---

## At a Glance: August 18 Highlights

Today's releases ask a shared design question from four directions: when an agent acts across a long workflow, on what terms does the human stay informed — and what infrastructure must the platform build to make that governable at scale?

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Remote Control effort-level sync ships** — effort picks on claude.ai/code or mobile now apply to terminal- and VS Code-hosted sessions; /code-review at high/xhigh/max now runs in a background agent; --channels push-event preview expands documentation and bidirectional MCP capability; gateway spend-limit naming in usage warnings; workspace trust prompts for `claude agents` in untrusted directories; /plugin install now refreshes marketplace before installing. [1][2][3] |
| **ChatGPT** | **ChatGPT Health reaches full rollout for all U.S. users 18+ on Free, Go, Plus, and Pro** — opt-in Apple Health, Epic, and medical records integration; per-user data-sharing granularity; health conversations siloed in dedicated tab; Computer History (macOS, admin-gated) enters broader enterprise rollout; Sign in with ChatGPT beta expands to Airtable, GitLab, HubSpot, Notion, Supabase, and Vercel. [4][5][6] |
| **Google Gemini** | **Gemini Enterprise extends end-to-end tracing to data connector workflows** — two new trace spans (execute_tool, invoke_connector) visualise the full assistant-prompt-to-third-party-API call chain in Trace Explorer; custom MCP server data stores enter public preview; Gemini Enterprise mobile app reaches GA for third-party identity providers; Gemini 3.6 Flash available in Agent Designer workflow agents. [7][8][9] |
| **Microsoft Copilot** | **Retirement wave lands August 18** — Group Chats, Podcasts, consumer Deep Research, and Mico all retire today; unified app URL transitions from m365.cloud.microsoft to copilot.cloud.microsoft; Autopilot background agents confirmed for Super App (Q3 2026 target); Entra Agent ID governs agent lifecycle and access across Copilot Studio and Power Platform; Microsoft 365 Copilot community call today demos Copilot + Entra ID management agent and SPFx secure document handoff. [10][11][12] |
| **Grok (xAI)** | **Grok Build fixes history corruption and improves prompt caching for long sessions** — chat history corruption that duplicated tool results patched; prompt caching improved to reduce repeated billing on growing transcripts; embedded preview redirect loops fixed; language server crash fixes for Roslyn/C#; Grok 4.6 remains the CLI default after August 12 model upgrade; 2x usage promo in Grok Build and Cursor closes August 19. [13][14][15] |
| **Perplexity** | **Sonar API officially becomes the Agent API as of August 13** — one programmable endpoint for web search, URL fetching, code execution, MCP, finance and people search with tunable presets; Sonar tiers retire September 27; Computer-in-Teams workflow surface continues deepening; Numb at open-source agent security suite available on macOS, Linux, and Windows. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Remote Control Effort Sync and the Push-Event MCP Layer

Anthropic's most interaction-design-significant changelog update in this window is the **Remote Control effort-level sync**, a small change with outsized implications for multi-device agentic workflows. 

Effort picks made on a phone or on claude.ai/code now apply to terminal- and Desktop/VS Code-hosted sessions, and the session publishes its effort level to connected clients.

 Previously, a user monitoring a long-running Claude Code session from their phone could send messages but could not change how hard the underlying session was reasoning — the effort slider existed only where the session was launched. This closes the control gap between Remote Control as a monitor and Remote Control as a genuine remote-management surface: a user can now escalate a session from medium to max effort mid-task from a mobile device without returning to the terminal. The interaction pattern this enables is supervision-without-presence — the human is not glued to the machine, but retains meaningful steering control over the session's reasoning behaviour.

The second major interaction change in the same changelog is the expansion of the **--channels** push-event primitive into a more robust bidirectional messaging layer. 

Channels let users push messages, alerts, and webhooks into a Claude Code session from an MCP server — forwarding CI results, chat messages, and monitoring events so Claude can react while you're away.

2.1.80 opened the reverse channel: --channels (research preview) lets MCP servers push messages into your running session.

 The UX significance of this inversion is profound: previously, MCP was a one-way tool-calling protocol — the agent asked, the server answered. Channels make MCP bidirectional: a CI failure, a deployment alert, or a Telegram message from the developer can arrive in the session without the agent having to poll. 

The direction is clear: MCP is becoming a bidirectional messaging layer, not just a tool-calling protocol.

 The practical consequence for temporal UX is that long-running agentic sessions no longer require the developer to manually check progress — the session receives events and reacts, while the developer receives replies through the same messaging channel they used to invoke the task.

The reliability and governance updates landing alongside deserve attention for enterprise deployments. 

Claude Code adds gateway spend-limit support to usage warnings; the limit-reached message now names the cap, its reset time, and the operator's message. A workspace trust prompt for `claude agents` was added for untrusted directories, matching the behaviour of `claude`.

 The spend-limit naming change is the transparency improvement that makes usage warnings actionable rather than opaque — instead of a generic rate-limit message, the user now sees exactly which cap they have hit and when it resets. The workspace trust prompt for `claude agents` closes a governance gap where the agents sub-command was less cautious than the root command in unfamiliar directories.

---

### Microsoft Copilot: The Retirement Completes and the Super App Architecture Becomes Visible

Today is the day Microsoft's August 13 retirement announcements become real. 

Account updates begin on August 18, 2026; before your account updates, download any media shared by other participants that you want to keep.

Three features are being retired on August 18, 2026: Copilot Podcasts (which auto-generated audio discussions from websites and documents), Group Chat (including all threads, messages, and images in group conversations), and Deep Research (which generated long, cited reports from web sources).

Mico, the animated voice-mode companion, is also being retired from the core consumer experience.

 For practitioners tracking the Copilot product arc, the retirement is not the story — the structural signal beneath it is. 

The Super App is Microsoft's planned consolidation of Copilot chat, AI coding tools, the Cowork research platform, and AutoPilot background agents into a single unified product serving both consumer and business users. The current August 13 rollout — which merges the consumer and Microsoft 365 apps into one unified experience — is the structural foundation for the Super App but is not the Super App itself.



The interaction-design consequence of the Super App architecture is most legible through the **Autopilot** agent design. 

The full Super App will bring together Copilot's chat, AI coding capability, the Cowork research tool, and new AutoPilot agents — background AI agents that can execute tasks autonomously across Outlook, Teams, and OneDrive — into a single product.

A conventional Copilot chat query requires one model call. An AutoPilot agent running a background task — monitoring email, coordinating calendars, managing a recurring document workflow — may require 10 to 20 separate model calls per action, because each call must transmit a full context window back to the model.

 This multi-call architecture is the reason Autopilots will carry a separate cost layer — and the reason the Entra Agent ID governance infrastructure matters so much as its precondition. The UX implication is that the human-agent control handoff for Autopilots is not a prompt; it is an identity policy: which agents have which permissions, governed at the Entra layer, not negotiated in the chat interface.



Starting August 18, 2026, Microsoft is introducing updates to the Microsoft Copilot web, desktop, and mobile app experiences to make it easier for users to distinguish between their work and personal accounts — including clearer account indicators, a simplified app name and icon, and a transition of the web app URL from m365.cloud.microsoft to copilot.cloud.microsoft.

 The URL change is the surface signal of the deeper identity-architecture shift: the app now lives at a Copilot-native address rather than a Microsoft 365 address, which is the branding expression of the move from productivity-suite-with-AI to AI-surface-with-productivity-capabilities. 

The August 18 community call session includes a demonstration of how to create a Copilot agent for Entra ID management — highlighting Microsoft's broader push toward AI-powered agents that can help simplify administrative and identity-related tasks.



---

### ChatGPT / OpenAI: Health as a Structured Consent Surface and Sign In With ChatGPT

OpenAI's most UX-consequential rollout completing in this window is **ChatGPT Health** reaching full availability for all eligible U.S. users. 

OpenAI is making ChatGPT Health, a feature that helps users with health-related queries, available to all U.S.-based users over 18 across all plans.

Users can choose to securely connect Apple Health and supported medical records so ChatGPT can help them understand their information in context, keep track of what has changed, and have more informed, personalized conversations.

 The trust-design architecture of ChatGPT Health is the most consequential aspect of the launch from a UX-practitioner perspective: 

this feature allows users to decide how much data and what data they want to share, and when they want to share.

 This is granular, per-session consent rather than a blanket integration toggle — the user is not granting ChatGPT ongoing access to their medical profile; they are choosing, before each relevant conversation, what context to surface. 

Over 70% of health-related conversations occurred outside the dedicated Health space, prompting the ability to reference health information across all conversations.

 The UX shift this represents is from a siloed health tab to ambient health context — the agent carries the user's health profile across the interface, not just within a dedicated mode.

The second trust-design event completing in this window is the broader rollout of **Sign in with ChatGPT**, which extends the platform's identity surface beyond the chat interface itself. 

ChatGPT adds Sign in with ChatGPT beta across select plugins and partner sites, including Airtable, GitLab, HubSpot, Notion, Supabase, and Vercel, making account setup faster and access simpler from ChatGPT and Codex.

 The interaction-design significance of this is less about login convenience and more about what it establishes: a ChatGPT identity that can authenticate with external tools, which is the prerequisite for an agent that can take actions on external platforms without requiring per-platform credential management. For enterprise practitioners, this is the early-stage plumbing for a future where agentic ChatGPT tasks on third-party platforms inherit the user's ChatGPT identity rather than requiring separate OAuth flows. 

ChatGPT has also launched a new Health experience for U.S. users 18+ on web and iOS, with secure connections to health records and Apple Health data and a dashboard for labs, medications, activity, sleep, and grounded questions; ChatGPT Voice has also come to Work and Codex on desktop.



---

### Google Gemini: Connector Tracing and the Enterprise Observability Deepening

Google's most trust-design-significant event in this window is the extension of end-to-end tracing to the **data connector workflow** in Gemini Enterprise — an expansion of the observability surface that makes the full agent-to-external-API execution path inspectable, not just the agent layer. 

Tracing support is extended end-to-end across the data connector workflow, introducing two new trace spans for better observability: `execute_tool` (representing the execution of a tool on the agent orchestration layer) and `invoke_connector` (representing the request logic and execution on the connector execution layer).

These spans help you visualise end-to-end parent-child relationship workflows from the assistant prompt to the third-party API.

 The UX implication for enterprise teams is that connector failures — which previously surfaced only as silent gaps or opaque error messages at the output layer — are now traceable to the exact execution point where they occurred. This is the difference between debugging by inference and debugging by inspection.

The **custom MCP server data store** entering public preview in the same window is the extensibility event that makes the connector tracing story more consequential. 

Creating a custom MCP server data store is in Public Preview.

 Previously, Gemini Enterprise's connector layer was limited to Google-approved integrations; the custom MCP server path opens it to any third-party data source an enterprise team can express as an MCP server. The combination — arbitrary MCP connectors plus full end-to-end tracing into their execution — is the enterprise data-grounding architecture that makes Gemini Enterprise deployable for organisations whose critical data lives in bespoke internal systems rather than standard SaaS connectors. 

Gemini 3.6 Flash is available in the global region and in Agent Designer workflow agents — administrators must turn on the Gemini 3.6 Flash feature toggle to make it available to users in the Gemini Enterprise app.

 The admin-toggle model for model availability is the governance pattern that distinguishes Gemini Enterprise from consumer Gemini: new model capabilities do not appear automatically; they require explicit IT authorisation before reaching users.

---

### Grok (xAI): Long-Session Reliability Hardening and the Prompt-Caching Fix

SpaceXAI's UX story in this window is quieter than the Grok 4.6 launch week — this is the hardening cycle that follows a major model upgrade. The most interaction-design-significant fix in the current Grok Build changelog is the **prompt-caching improvement for long conversations**. 

Grok Build fixes chat history corruption, redirect loops in embedded previews, and several reliability issues across auth, wake turns, and language servers, and improves prompt caching for long conversations, helping reduce repeated billing on growing transcripts.

 The UX significance of the caching fix is not immediately visible in the interface — but it matters enormously for long-running agentic sessions. 

Cached input rose 67% from $0.30 → $0.50 per million tokens; an agent loop re-sends its accumulated context every turn, so that is the line item that moves.

 The prompt-caching improvement reduces the effective cost of multi-turn agentic loops that re-transmit accumulated context on every step — which is the cost profile of any long-horizon development task in Grok Build.

The specific reliability fixes landing in this cycle address failure modes that only surface in production agentic use. 

Fixed chat history corruption that could duplicate tool results or cause later 400 errors after repeated identical tool calls; fixed infinite redirect loops in embedded previews when the browser blocks the required cookie; fixed language server crashes (e.g. Roslyn on every edit) and missing C# diagnostics, with improved diagnostics reliability for other servers.

 The Roslyn/C# crash fix is the enterprise-developer-experience detail that matters most here: language server crashes during agentic editing sessions are the kind of failure that breaks trust in a coding agent more durably than any benchmark gap. A session that corrupts its own history or crashes its language server mid-task signals that the agent is not safe to leave unattended — precisely the opposite of the long-running agentic posture Grok 4.6 was designed to enable. 

Grok Build is running a 2x usage promo that expires around August 19, 2026

 — making today the final day of the adoption-incentive window that xAI used to drive initial Grok 4.6 workflow integration.

---

### Perplexity: Sonar Becomes the Agent API and the Unified Developer Surface

Perplexity's most architecturally significant event in the last 48 hours is the formal announcement that the **Sonar API is becoming the Agent API** — a consolidation that eliminates the distinction between Perplexity's search product and its orchestration platform. 

Sonar is now the Agent API: one programmable endpoint for web search, code execution, and MCP, with presets that benchmark higher at lower cost.

On September 27, 2026, the Agent API becomes the main surface for this work, and Sonar tiers retire on the same date; every existing tier maps to a preset that benchmarks higher at lower cost, so the move consolidates workloads onto one programmable stack without giving anything up.

 The UX implication for developers building on Perplexity is a platform identity shift: Perplexity is no longer a search API that also has an agent layer; it is an agent platform that includes search as a built-in capability. 

Perplexity is building the infrastructure for work that depends on language models, the public web, and agents running against both — the Agent API is how developers plug into that infrastructure; it is a single programmable endpoint for web search, URL fetching, code execution, MCP connections, and finance and people search.



The governance and security infrastructure Perplexity is building alongside the API consolidation is worth tracking for enterprise practitioners. 

Numbat is Perplexity's open-source agent security suite for client endpoints — it detects, prevents, and investigates risky AI agent behaviour on macOS, Linux, and Windows.

 Numbat is Perplexity's answer to the same agent-security problem Microsoft is solving with Entra Agent ID: as Computer agents run autonomously on user machines and inside enterprise platforms, the ability to detect and investigate anomalous agent behaviour becomes a precondition for enterprise trust. The open-source release strategy is a deliberate contrast to Microsoft's identity-governance approach — instead of a managed platform, Perplexity ships auditable tooling that security teams can run and inspect themselves. 

Perplexity automates coding, deploying, monitoring, and growth reporting for solo founders and small engineering teams through its Computer for builders capability.

 The developer-facing Computer surface and the enterprise Agent API are converging on a shared infrastructure — the same orchestration layer that routes search, code, and MCP calls in the API is the same layer that Computer uses to complete multi-step tasks on the user's behalf.

---

## The Bigger Picture: Super App Scaffolding, Push-Event Agents, and the API Unification Wave

The 48 hours ending August 18, 2026 are defined by three simultaneous consolidation moves — one in the consumer app layer, one in the developer API layer, and one in the agent governance layer — that are each, independently, the most consequential simplification their platform has executed this year. Microsoft's retirement wave and unified-app launch is the consumer consolidation: the platform is shedding the interaction experiments that didn't earn enterprise-grade governance contracts and building the scaffold for Autopilot agents that will operate as identity-managed background workers rather than chat-session tools. Perplexity's Sonar-to-Agent-API migration is the developer consolidation: a search endpoint is becoming an orchestration endpoint, which is the product identity shift that positions Perplexity as infrastructure for the agentic stack rather than a consumer search alternative. And Anthropic's --channels push-event expansion is the interaction-model consolidation that matters most for the day-to-day agentic workflow: MCP is becoming bidirectional, which means the event model for long-running agents shifts from polling-by-the-human to push-by-the-environment — a more accurate reflection of how production software systems actually notify humans of state changes. The governance thread connecting all three is visible in what each platform builds to make its consolidation trustworthy: Microsoft builds Entra Agent ID so every Autopilot has a governable identity; Perplexity ships Numbat so security teams can inspect agent behaviour on endpoints; Anthropic adds workspace trust prompts and spend-limit naming so the enterprise operator retains meaningful oversight of what sessions cost and where they execute. Google's connector tracing deepening and Grok Build's history-corruption patches are the same answer at the infrastructure layer: agents that leave legible execution trails and clean session state are agents that enterprise teams can actually operate in production.

---

## References

[1] Gradually.ai. (2026). *Claude Code Changelog (August 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[2] Releasebot. (2026). *Claude Code Updates by Anthropic — August 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] ClaudeFa.st. (2026). *Claude Code Changelog: All Release Notes (2026)*. [https://claudefa.st/blog/guide/changelog](https://claudefa.st/blog/guide/changelog)

[4] OpenAI. (2026). *Launching Health in ChatGPT*. [https://openai.com/index/health-in-chatgpt/](https://openai.com/index/health-in-chatgpt/)

[5] Releasebot. (2026). *ChatGPT Updates by OpenAI — August 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[6] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[7] Google Cloud Documentation. (2026). *Gemini Enterprise release notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[8] Google Cloud Documentation. (2026). *Gemini Enterprise Agent Platform release notes*. [https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes)

[9] Google Cloud Documentation. (2026). *Observability overview — Gemini Enterprise Agent Platform*. [https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview)

[10] Microsoft Support. (2026). *Updates to Copilot and the Microsoft Copilot app*. [https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app](https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app)

[11] TechTimes. (2026). *Microsoft Copilot Rollout Starts: Free Deep Research Retired in Four Days*. [https://www.techtimes.com/articles/324537/20260814/microsoft-copilot-rollout-starts-free-deep-research-retired-four-days.htm](https://www.techtimes.com/articles/324537/20260814/microsoft-copilot-rollout-starts-free-deep-research-retired-four-days.htm)

[12] WinCentral. (2026). *Microsoft's August 18 Copilot and Microsoft 365 update call*. [https://thewincentral.com/microsoft-365-copilot-power-platform-updates-august-18/](https://thewincentral.com/microsoft-365-copilot-power-platform-updates-august-18/)

[13] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[14] Releasebot. (2026). *xAI Release Notes — August 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] Codersera. (2026). *Grok Build, Grok Skills + Connectors: xAI Dev Stack 2026*. [https://codersera.com/blog/xai-grok-build-skills-connectors-guide-2026/](https://codersera.com/blog/xai-grok-build-skills-connectors-guide-2026/)

[16] Perplexity AI Hub. (2026). *Agent API: One Place to Build with LLMs, the Web, and Agents*. [https://www.perplexity.ai/hub/blog/agent-api-one-place-to-build-with-llms-the-web-and-agents](https://www.perplexity.ai/hub/blog/agent-api-one-place-to-build-with-llms-the-web-and-agents)

[17] Releases.sh. (2026). *Perplexity Release Notes & Changelog — August 2026*. [https://releases.sh/perplexity](https://releases.sh/perplexity)

[18] Perplexity AI Hub. (2026). *Securing agents across Perplexity's client endpoints with Numbat*. [https://www.perplexity.ai/hub/blog](https://www.perplexity.ai/hub/blog)