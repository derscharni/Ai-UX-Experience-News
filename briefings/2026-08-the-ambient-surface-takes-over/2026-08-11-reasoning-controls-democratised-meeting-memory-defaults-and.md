# UX Briefing: Reasoning Controls Democratised, Meeting Memory Defaults, and the Government Agent

**August 11, 2026**

Good morning. The 48 hours ending August 11 are shaped by three converging design pressures that touch every layer of the human-agent stack simultaneously: **OpenAI** executes the most consequential free-tier interaction redesign in ChatGPT's history, replacing invisible model routing with a user-controlled reasoning slider for Plus/Pro subscribers and a discrete **Think button** for Free users — collapsing the Instant/reasoning split into one model, one surface, and one explicit control that makes the AI's effort level legible for the first time at scale; **Microsoft** is advancing two default-on data capture decisions simultaneously — **AI meeting archives** (.meeting files generated for every eligible Teams session, stored in tenant SharePoint by default with a five-year retention window arriving late August) and **Copilot Mobile's in-person meeting recording**, both on by default — representing the most consequential pair of opt-out governance decisions Microsoft has shipped in a single wave this year; and **Anthropic** completes the trust-and-governance architecture for its most sensitive deployment surface yet, with **Claude for Government Desktop** in public beta, bringing FedRAMP High-authorized Claude Code and Cowork with tamper-evident audit logs and department-level spend controls to U.S. public sector agencies, while the Claude Code changelog simultaneously ships the workspace trust prompt for untrusted directories and spend-limit transparency in usage warnings. **Grok Build** (xAI) extends its agent observability layer with dashboard turn summaries and client reattachment to running sessions, and **Perplexity's** Bumblebee open-source scanner ships as a developer-facing trust signal for agent pipelines.

---

## At a Glance: August 11 Highlights

The releases in this window collectively describe an industry renegotiating the visibility contract between users and agents: who sees the AI's effort, who owns the memory it creates, and who controls the governance layer that makes autonomous work auditable.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude for Government Desktop in public beta** — FedRAMP High-authorized Claude Code and Cowork for public sector with tamper-evident audit logs and department spend controls; Claude Code ships workspace trust prompt for untrusted directories and gateway spend-limit transparency in usage warnings; MCP 2026-07-28 stateless core rolling across Claude products. [1][2][3] |
| **ChatGPT** | **GPT-5.6 Sol reasoning slider and Think button rolling this week** — Plus/Pro get a continuous effort slider from Instant to High; Free/Go get GPT-5.6 Luna as new default with unlimited text and a discrete Think button for harder questions; o3 retiring from ChatGPT August 26; restaurant reservation booking live across all plans. [4][5][6] |
| **Google Gemini** | **Gemini in Classroom expands to all K-12 students August 10** — admin-gated, guided flashcards, practice quizzes, and study guides tied to class materials; Gemini Deep Research Agent in preview for autonomous multi-step research tasks; Robotics ER 2 adds multi-robot coordination and blocking function calls for physical actions. [7][8][9] |
| **Microsoft Copilot** | **AI meeting archives (.meeting files) arriving late August by default** — AI-generated summaries for every eligible Teams meeting, stored in tenant-owned SharePoint with five-year default retention; Copilot Mobile in-person recording on by default; OpenAI now a subprocessor in M365 Copilot auto-enabled July 24; Cowork available across browser, Outlook, Teams, desktop, and mobile. [10][11][12] |
| **Grok (xAI)** | **Grok Build dashboard turn summaries and client session reattachment** — dashboard rows now show per-turn agent work summaries; clients can reattach to running sessions without replaying transcripts; /undo slash command ships as rewind alias; auto-classifier permission fallback fixed to show prompt instead of silently denying. [13][14][15] |
| **Perplexity** | **Bumblebee open-source scanner releases for dev teams** — MCP Server adds one-click install for Cursor, VS Code, Claude Desktop, and Claude Code; Personal Computer on Mac ships with Personal CFO prebuilt agent; Agent API continues supporting Claude Opus 4.7, GPT-5.5, and Grok 4.20 Reasoning as third-party models. [16][17][18] |

---

## Product Highlights

### ChatGPT / OpenAI: The Reasoning Effort Slider and What Making AI Effort Visible Means for Interaction Design

OpenAI's most interaction-design-significant event in this window is not a new capability but a new control surface: the **GPT-5.6 Sol reasoning effort slider**, rolling this week for Plus and Pro subscribers alongside an unlimited-text upgrade and **Think button** for Free users. The structural change that matters most is the elimination of the hidden router. 

As of August 6, 2026, GPT-5.6 Sol powers both the Instant and reasoning experiences inside the everyday chat surface, replacing the two-model split with one consistent model and interaction pattern.

 The previous architecture invisibly picked a model based on question complexity; the new architecture exposes that tradeoff to the user as an explicit dial.

The slider itself is the trust-design primitive worth examining most closely. 

Plus and Pro users can use the new slider in ChatGPT on web, mobile, and desktop to choose how much thought ChatGPT puts into an answer — keeping it quick for everyday questions, or moving the slider up for planning, research, writing, coding, or decisions that need more thought.

 This shifts the UX from a black-box routing decision to a legible tradeoff: users now see and control how much processing effort the AI applies. The design tension this creates is real — 

model pickers in ChatGPT have historically been ignored by most users, and choosing the right model has generally mattered more than choosing a reasoning depth; the slider does make the trade-off visible rather than leaving it to a router, but it also adds one more setting to get wrong.



For Free users, the equivalent control arrives as a discrete button rather than a continuous slider. 

Plus and Pro users get a slider in ChatGPT on web, mobile, and desktop that sets how much thought the model puts into an answer, from quick everyday replies up to extended effort for planning, research, writing, coding, and decisions; Free users instead get a Think button, which gives GPT-5.6 Luna more time to work through harder questions on a per-message basis.

 The UX implication of this tiered control design is worth naming: the slider encodes effort as a spectrum the user navigates continuously, while the Think button encodes it as a binary toggle. Both patterns make AI reasoning effort legible — they just calibrate the granularity of control to the assumed sophistication of each user tier. What remains unchanged for Free users is access to the stronger reasoning stack: 

the Think button gives the smaller GPT-5.6 Luna more time; it does not route the question to GPT-5.6 Sol or GPT-5.6 Terra — Free users therefore get more volume and a longer-thinking small model, but no access to OpenAI's stronger reasoning models.

 Separately, 

ChatGPT adds restaurant reservation search with OpenTable, Resy, and Yelp, letting users find available times in chat and book a table after narrowing options with follow-up questions, rolling out across ChatGPT plans on mobile, web, and desktop

 — the first native transactional booking action built into the chat surface this year.

---

### Microsoft Copilot: Two Default-On Memory Expansions and the Governance Debt They Create

Microsoft's most trust-design-consequential events in this window are not feature additions but **default-on data capture decisions** arriving in rapid succession. The first is **AI meeting archives** for Teams: 

Microsoft says "Microsoft Teams will generate AI meeting archive files capturing key insights to enhance Microsoft 365 Copilot and Facilitator responses while ensuring privacy — stored in tenant-owned SharePoint, archives are enabled by default with admin controls available before rollout in August 2026; retention is configurable, and access is restricted to meeting participants."

 The governance architecture is important to read carefully: 

the files will contain AI-generated summaries and meeting insights rather than raw transcripts, and they will live in tenant-owned SharePoint rather than an individual employee's storage.

 But the default-on posture is the trust-design decision that requires the most immediate admin attention. 

The AI meeting archives (.meeting files) are an AI-generated summary file for every eligible meeting, stored in tenant-owned SharePoint Embedded and not user-accessible, with a default five-year retention — admins should review this retention default before it lands in September.



Running in parallel, 

Copilot Mobile records in-person meetings on by default, with audio going to the user's OneDrive with transcript and insights, inheriting OneDrive permissions and Purview governance; organisations can disable this org-wide via Intune App Configuration Policy if needed.

 The juxtaposition of these two simultaneous default-on memory features is the design tension that matters most: one creates a tenant-level AI memory layer for every eligible remote meeting without user action, the other extends that capture to in-person conversations via mobile. Together they represent a meaningful expansion of what a Teams meeting leaves behind — and of what Copilot can subsequently know about it. The design implication is that the control architecture for both features places the governance responsibility on admins, not end users, and the default assumption is that persistent AI meeting memory is beneficial unless explicitly refused.

The third significant governance event in this window is one that already landed: 

OpenAI-operated models (from GPT-5.6) now run under OpenAI as a subprocessor in Microsoft 365 Copilot, and the admin toggle auto-enabled on July 24 unless it was already set to "No users" — admins who have any considerations around where and how their data is processed, particularly the EU Data Boundary where the wording is now "except as otherwise disclosed," should check that toggle today.

 The UX implication of this auto-enablement compounds with the meeting archive and mobile recording defaults: three separate Microsoft data-processing expansions have now landed or are imminent in the same August wave, each opt-out rather than opt-in, and their combined governance surface is larger than any one of them individually.

---

### Claude / Anthropic: FedRAMP Cowork, Audit Logs, and the Governance Architecture for Agentic Government Work

Anthropic's most structurally significant development in this window is the completion of its public sector deployment architecture: **Claude for Government Desktop** in public beta, bringing Claude Code and Cowork into a FedRAMP High authorized environment for U.S. federal, state, and local agencies. 

Claude Code and Claude Cowork are now available in public beta in Claude for Government Desktop, built on the same application commercial customers use and delivered through a FedRAMP High authorized environment — with Claude Code, public sector teams can build and modernize the software systems that underpin public services, while Claude Cowork works directly with files on the desktop, allowing agency staff to delegate memo creation, RFP reviews, casework, and decks to Claude.



The governance layer that makes this a meaningfully different deployment than a commercial Cowork session is the audit infrastructure. 

The expanded experience comes with additional governance capabilities: administrators can set configuration defaults and allocate and control spending across departments, while security teams and authorizing officials get tamper-evident audit logs and documentation that supports the agency ATO process — today's launch makes it easier for agencies to acquire, authorize, and allocate AI in pursuit of their missions.

 The UX implication of tamper-evident audit logs at the agentic layer is significant: when Claude Cowork delegates a memo creation task or an RFP review across files, every step of that delegation is now logged in a way that cannot be silently modified. This is the transparency primitive that federal procurement and compliance teams require before they can delegate work to an agent — and it establishes a trust-design pattern that commercial enterprise deployments of Cowork do not yet match.

On the developer side, 

Claude Code's usage warning now names the cap, its reset time, and the operator's message when a gateway spend limit is reached — and Claude Code adds a workspace trust prompt for untrusted directories, matching the behavior of the standard Claude CLI session.

 The workspace trust prompt is the agentic safety primitive that prevents Claude Code from silently operating in directories it has not been explicitly authorised to touch — the same trust boundary that the FedRAMP government deployment formalises at the department level is now arriving in the developer CLI as a per-directory approval gate. 

MCP 2026-07-28 moves the protocol from a bidirectional stateful model to a request/response model, so servers can now deploy on serverless and edge infrastructure, simplifying the experience of building MCP servers for Claude and scaling their usage as they grow in adoption

 — with support rolling across Claude products now.

---

### Grok (xAI): Agent Dashboard Turn Summaries and the Observability Layer for Parallel Coding Sessions

xAI's most interaction-design-consequential release in this window is not a new Grok Imagine capability or a voice model migration but a quiet transparency upgrade to Grok Build's multi-agent dashboard: **per-turn agent work summaries** in dashboard rows. 

Dashboard rows now show a short summary of the agent's work in the previous turn, and the Extensions modal groups items alphabetically with a collapsible Skills section; when a subagent runs in the background, the parent agent is now reminded to keep working on the original task, and clients can reattach to a running session without replaying the transcript, or explicitly close sessions.



This is the ambient observability pattern that multi-agent coding workflows have been missing. When a developer has multiple parallel Grok Build sessions running against different parts of a codebase, the dashboard previously required opening each session to understand its state. Per-turn summaries in the dashboard row surface that state at a glance — the user can audit what each agent did last without context-switching into the session itself. The client reattachment capability is equally significant for long-running agentic tasks: rather than losing session context or replaying an entire transcript to resume work, a client can reattach to an active session mid-execution, which is the continuity primitive that makes Grok Build sessions viable for tasks that outlast a single sitting.

The trust-design fix that warrants specific attention this week is the **auto-classifier permission fallback** correction: 

when the auto-permission classifier times out or fails, Grok now shows a normal permission prompt instead of silently denying.

 Silent denial — where a permission gate fails invisibly and the agent simply stops without telling the user why — is one of the most disorienting failure modes in agentic systems. The fix changes this from a silent stop to an explicit human checkpoint, which is the correct fallback for a classifier failure in an autonomous coding session. 

Grok Build also adds streaming JSON headless output with tool calls, results, and usage, plus a new /undo slash command to restore files and chat to an earlier turn, along with improved slash command handling, login stability, draft history warnings, settings pickers, and deep-linked settings behavior.



---

### Google Gemini: Classroom at K-12 Scale and the Deep Research Agent in Preview

Google's most UX-consequential event in this 48-hour window is the expansion of **Gemini in Classroom** to K-12 students of all ages, which took effect August 10. 

Google launched Gemini in Classroom to help educators save time on planning; starting August 10, 2026, Gemini in Classroom is also being made available to K-12 and higher education students of all ages who have already been granted access by their admin, offering a guided space to interact with these tools — in Classroom, students can access the Gemini tab to transform their class materials into interactive experiences that help them study and learn.

 The trust-design architecture that makes this a materially different deployment than an open chatbot for minors is the admin gate and the content constraint: 

Gemini expands in Google Classroom with new student access and more context-aware study help, including flashcards, practice quizzes, study guides, and guided prompts tied to class materials and assignments; it also brings Learn with Gemini to the Classroom homepage for faster support.

 When the AI's outputs are constrained to materials the teacher has already assigned, the student is interacting with a bounded, contextually appropriate agent — not a general-purpose model that can range freely across topics.

On the developer-platform side, 

Google launched the Gemini Deep Research Agent in preview, which can autonomously plan, execute, and synthesize results for multi-step research tasks.

 This is the agentic pattern that Perplexity has been building toward with its own Deep Research capability — an agent that does not just answer a query but plans the research, executes multiple steps, and synthesises the results into a deliverable. The UX distinction between a search result and a Deep Research output is the difference between a pointer and a product: the agent does the work rather than directing the user toward the work. 

Gemini Robotics ER 2 is also in public preview with two endpoints: the advanced model adds spatial reasoning, agentic code execution, multi-step tool orchestration, video moment finding, progress classification, and multi-robot coordination; the streaming-optimised variant enables low-latency robot agents with bidirectional audio and video input — both endpoints support function calling with blocking behavior for physical robot actions.

 The blocking function-call pattern for physical actions is the trust-design primitive the embodied AI layer requires: a robot agent must be able to pause before executing an irreversible physical outcome, and the blocking call is Gemini's API expression of that contract.

---

### Perplexity: Bumblebee, MCP One-Click Install, and the Personal Computer on Mac

Perplexity's most developer-facing release in this window is **Bumblebee**, an open-source scanner for dev teams, which positions Perplexity in the emerging category of agentic pipeline integrity tooling — 

Perplexity releases Bumblebee as an open-source scanner for dev teams.

 While details on Bumblebee's full capability surface are still emerging, its open-source posture signals a trust-design strategy: releasing inspection tooling as a community asset rather than a proprietary gate is the move that builds credibility with developer teams evaluating whether to deploy Perplexity's agent stack in production.

The MCP integration update is the distribution event that matters most for Perplexity's reach into developer workflows. 

The Perplexity MCP Server now supports one-click installation for Cursor, VS Code, Claude Desktop, and Claude Code, providing four tools: perplexity_search, perplexity_ask, perplexity_research, and perplexity_reason.

 One-click MCP installation into the four dominant agentic development environments means Perplexity's search and research capabilities are now a single click away from any developer building an agentic workflow in those tools — the distribution friction that previously required a manual server configuration step is eliminated. The personal deployment story also advances: 

Perplexity shipped Personal Computer on Mac, with updates including easier control of Computer and improved integration with personal context, including a prebuilt Personal CFO.

The Agent API continues to support Claude Opus 4.7, GPT-5.5, and Grok 4.20 Reasoning as third-party models

 — the multi-model interoperability posture that prevents any single provider's capability ceiling from constraining the entire orchestration pipeline.

---

## The Bigger Picture: Reasoning Controls Democratised, Meeting Memory Defaults, and the Government Agent

The 48 hours ending August 11, 2026 are unified by a single design question that every platform is answering differently: who decides how much the AI does, and who can see what it did? OpenAI's reasoning slider is the most explicit statement of the question at the interaction layer — making effort level a user-controlled dial rather than an invisible routing decision is the moment the "how hard should AI think about this?" tradeoff becomes a UX primitive rather than a backend implementation detail, and shipping a simplified version of that control (the Think button) to over a billion free-tier users simultaneously is the largest single expansion of AI effort-legibility in the industry's history. Microsoft's dual default-on meeting memory decisions answer the same question from the opposite direction: rather than giving users control over the AI's effort, Microsoft is expanding the AI's persistent awareness of work that has already happened — and making that expansion the default, with admin-level opt-out as the only check. The governance debt this creates for IT teams is real and immediate: three separate Microsoft data-processing expansions (OpenAI subprocessor auto-enablement, Copilot Mobile in-person recording, and AI meeting archives) have now landed in a single August wave, each requiring an active administrative decision to constrain rather than a deliberate choice to enable. Anthropic's Claude for Government Desktop answers the question with the most rigorous governance architecture in the window: tamper-evident audit logs, FedRAMP High authorization, and department-level spend controls are the trust primitives that make autonomous agentic work delegatable in the highest-stakes environments that exist. Grok Build's per-turn dashboard summaries and session reattachment, Google's Classroom content constraints, and Perplexity's open-source Bumblebee scanner are all expressions of the same underlying design movement: the industry is building the observation layer that lets humans see what agents did, understand why, and intervene precisely — because the agents are now running long enough and autonomously enough that "watch what it does" is no longer a sufficient oversight strategy.

---

## References

[1] Claude by Anthropic. (2026). *Bringing Claude Code and Claude Cowork to government*. [https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government)

[2] Releasebot. (2026). *Claude Code Updates by Anthropic — August 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] Releasebot. (2026). *Anthropic Release Notes — August 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[4] OpenAI. (2026). *Improving GPT-5.6 Sol in ChatGPT — and expanding access to GPT-5.6 Luna for free users*. [https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)

[5] Unite.AI. (2026). *OpenAI Gives Free ChatGPT Users Unlimited Text Chats on GPT-5.6 Luna*. [https://www.unite.ai/openai-gives-free-chatgpt-users-unlimited-text-chats-on-gpt-5-6-luna/](https://www.unite.ai/openai-gives-free-chatgpt-users-unlimited-text-chats-on-gpt-5-6-luna/)

[6] Releasebot. (2026). *ChatGPT Updates by OpenAI — August 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] Google Workspace Updates. (2026). *Gemini in Classroom expands to K-12 students*. [https://workspaceupdates.googleblog.com/2026/](https://workspaceupdates.googleblog.com/2026/)

[8] Google AI for Developers. (2026). *Release notes — Gemini API*. [https://ai.google.dev/gemini-api/docs/changelog](https://ai.google.dev/gemini-api/docs/changelog)

[9] Releasebot. (2026). *Gemini Updates by Google — August 2026*. [https://releasebot.io/updates/google/gemini](https://releasebot.io/updates/google/gemini)

[10] BetaNews. (2026). *Microsoft Teams will generate AI meeting archives by default*. [https://betanews.com/article/microsoft-teams-will-generate-ai-meeting-archives-by-default/](https://betanews.com/article/microsoft-teams-will-generate-ai-meeting-archives-by-default/)

[11] Empowering.cloud. (2026). *Microsoft 365 Enterprise Update August 2026*. [https://empowering.cloud/microsoft-365-ai-workplace-update-august-2026/](https://empowering.cloud/microsoft-365-ai-workplace-update-august-2026/)

[12] M365 Admin. (2026). *OpenAI models will soon be available as a subprocessor in Microsoft 365 Copilot*. [https://m365admin.handsontek.net/openai-models-will-soon-available-subprocessor-microsoft-365-copilot/](https://m365admin.handsontek.net/openai-models-will-soon-available-subprocessor-microsoft-365-copilot/)

[13] Toolsbase.dev. (2026). *Grok Build (grok) Cheat Sheet 2026 — 204 Commands*. [https://toolsbase.dev/en/reference/grok-build-commands](https://toolsbase.dev/en/reference/grok-build-commands)

[14] xAI. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[15] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Just AI News. (2026). *Perplexity Releases Bumblebee As An Open Source Scanner For Dev Teams*. [https://justainews.com/category/companies/perplexity/](https://justainews.com/category/companies/perplexity/)

[17] Releases.sh. (2026). *Perplexity Release Notes & Changelog — August 2026*. [https://releases.sh/perplexity](https://releases.sh/perplexity)

[18] Releasebot. (2026). *Perplexity Release Notes — August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)