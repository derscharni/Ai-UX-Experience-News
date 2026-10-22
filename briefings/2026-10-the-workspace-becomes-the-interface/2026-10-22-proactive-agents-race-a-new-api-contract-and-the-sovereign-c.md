# UX Briefing: Proactive Agents Race, a New API Contract, and the Sovereign Compute Frontier

**October 22, 2026**

Good morning. The 48 hours ending October 22, 2026 are dominated by a single strategic declaration that every major platform made simultaneously and independently: the passive, prompt-and-respond interface model is over. **Claude/Anthropic** fires the day's most consequential consumer-UX shot with **Claude Duet, launched October 21 as a research preview** — a standalone proactive agent app that sends a morning brief, monitors connected apps every few hours, works on its own cloud virtual machine, and surfaces human approval gates only for sensitive actions like payments, document signing, and message-sending. On the same day, Anthropic ships **Claude API version 2026-10-21**, the platform's first new versioned API release since 2023, removing temperature, top_p, and top_k from the Messages API across seven new SDK major versions — a platform-contract reset with immediate implications for every agentic pipeline built on the Claude stack. **Google Gemini** delivers its most consequential Workspace interaction-design double-header of the month on October 21: **Docs Live rolls out to Workspace mobile users** on Android and iOS, enabling hands-free document creation that synthesises context from Gmail, Drive, and Chat; and **Gemini Notebook gains a step-by-step Slide Deck and Video Overview creation flow** with an Outline Review toggle that previews the plan before generating the final output. **Microsoft Copilot's** agent governance architecture crystallises further as the **Copilot Credit spending-policy framework** — with Code, Autopilot, and SharePoint advanced capabilities all running on usage-based billing — enters active admin decision territory this week. **Perplexity** closes its privacy-and-sovereignty week with the **Valarian partnership announced October 20**, extending the fully local Mac mode into institutional air-gapped networks and completing the most coherent three-tier compute governance story in the consumer AI category — local device, hybrid cloud, or sovereign institutional infrastructure.

---

## At a Glance: October 22 Highlights

Today's releases converge on a single structural question that the industry has been circling for months and is now answering in product: when an AI agent operates proactively, across connected apps, on its own cloud computer, without the user initiating each task — what does the human approval contract look like, and who decides where the agent's compute runs?

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Duet launches October 21 as a research preview proactive agent; Claude API version 2026-10-21 ships with breaking changes across seven SDK majors; Claude Security goes continuous** — Duet sends a morning brief, monitors connected apps, works on a cloud VM, and requires approval before sending messages, making payments, or deleting files; API 2026-10-21 removes temperature/top_p/top_k (400 error even at default values) and moves auth from X-Api-Key to Authorization: Bearer; Claude Security adds continuous repository scanning, automatic fix tracking, MCP integration, and per-project threat models for Enterprise. [1][2][3][4][5][6] |
| **ChatGPT** | **ChatGPT Locked Chats ship October 20 across all plans; Slides launch October 16 with collaborative Space editing; GPT-6 Pro parallel agents enter rollout** — Locked Chats hide conversations from history, pinned chats, and search behind a 4-digit PIN, Face ID, or Touch ID; Slides lets Pro, Business, and Enterprise users create and co-edit decks in Space; GPT-6 Pro now runs multiple agents on different parts of a task in parallel, with progress visible in the conversation thread. [7][8][9] |
| **Google Gemini** | **Docs Live rolls out to Workspace mobile (Android and iOS) October 21 as a hands-free voice co-writer; Gemini Notebook gains step-by-step Slide Deck and Video Overview creation with Outline Review toggle; Skills delay continues** — Docs Live synthesises context from Gmail, Drive, and Chat without user pasting; Notebook's new guided creation flow shows the outline and producer notes before generating; Workspace Skills remain delayed until further notice while app Skills continue mid-November rollout. [10][11][12] |
| **Microsoft Copilot** | **Copilot Credit spending-policy framework enters active admin territory this week; Agent 365 FinOps expands to Code and Managed Runtime; Notebooks UX refresh in Frontier** — Code, Autopilot, and SharePoint advanced capabilities all run on usage-based billing requiring a spending policy before users can access them; admins set monthly credit caps per user and per service; Notebooks refresh groups and reorders content from the navigation pane, with full Office editing available from within the notebook canvas. [13][14][15] |
| **Grok (xAI)** | **Grok Build v1.0.62 carries forward the CLI pipe-safety and hook-error fixes; Grok's one-subscription model consolidates chat, voice, image, video, and Bot into a single plan** — `grok update` and `grok login` no longer crash when stdout or stderr is closed or unwritable; approval cards for background subagents no longer disappear when the parent turn ends; xAI confirmed that one subscription now covers chat, voice, image/video generation, and Grok Bot for the first time. [16][17] |
| **Perplexity** | **Perplexity–Valarian partnership announced October 20 deploys Computer inside air-gapped institutional networks; Computer in Email launches with GPT-5.6 Terra and Luna as default subagent and automation models** — Valarian's ACRA platform runs Computer on institution-controlled infrastructure under the customer's own policy and data access rules; Computer in Email lets users start and continue Computer sessions from email threads; GPT-5.6 Terra is the default model for complex multi-step Computer subagents, Luna for scheduled automations. [18][19][20] |

---

## Product Highlights

### Claude / Anthropic: Three Simultaneous Bets — Duet, a New API Contract, and a Living Security Scanner

Anthropic's October 21 is the busiest single-day product release in the company's history from a UX architecture standpoint: three distinct product events, each targeting a different layer of the Claude interaction stack — the consumer ambient surface, the developer platform contract, and the enterprise security workflow — all shipped simultaneously.

**Claude Duet** is the most consequential of the three for consumer and professional UX practitioners. 

Anthropic opened a research preview of Claude Duet on October 21, 2026: a standalone app in which Claude works as a proactive agent — instead of waiting for prompts, it sends a short morning brief on what matters across a user's connected apps, checks those apps every few hours, and messages only when something needs attention.

 The interaction-design shift this establishes is fundamental: rather than positioning Claude as a tool the user reaches for, Duet positions it as a presence that monitors on the user's behalf and surfaces work to the user's attention on its own cadence. 

While the agent works on its own, it will get user approval before it takes actions like sending a message, making a payment, signing a document, or deleting a file.

 This selective-approval gate — triggering human review only for irreversible or high-stakes actions — is the correct trust-design architecture for a proactive ambient agent: it preserves automation for routine monitoring while elevating the human at the moments that carry genuine downstream consequences. 

Duet incorporates memory, skills, and connected apps from a Claude account, so there is not much setup involved; interactions happen in one ongoing thread instead of across different conversations.

 The single-thread design is an important UX choice: it converts the agent from a tool you open into a persistent correspondent you have an ongoing relationship with — closer to a colleague's messaging thread than a product modal.

The platform-contract event that will affect the most builders immediately is the **Claude API version 2026-10-21** release. 

Claude API version 2026-10-21 is the first new Claude API version since 2023-06-01; Anthropic released it on 21 October 2026 with new major versions of every SDK. It removes temperature, top_p, and top_k, rejects two odd message shapes, renames fields in the Admin API, and the new SDKs send your key in a different header.

 The temperature removal is the interaction-design implication that practitioners need to understand first: 

removing temperature sounds simple — just delete the parameter. The problem is that many codebases pass it explicitly as a form of documentation, setting temperature=1.0 to make intent clear. On the new API version, that call breaks too.

 The silent proxy-breaker is equally dangerous: 

new SDK versions send credentials as `Authorization: Bearer` instead of the legacy `X-Api-Key` header; any proxy or API gateway reading the key from `X-Api-Key` will receive requests with no visible authentication credential — the failure is silent at the proxy layer.

 This is the governance-surface implication that enterprise teams running Claude through intermediate API gateways — including the many agentic pipeline architectures built this autumn — must audit before upgrading to the new SDKs.

The enterprise security UX advance that deserves equal attention is the **continuous Claude Security update**. 

On October 21, 2026, Anthropic turned Claude Security from a scanner you run into one that keeps watching: it now rescans code as it changes, marks findings fixed when the fix ships, and decides what matters using context your team writes down.

 The MCP connector integration is the in-workflow design advance that closes the most friction: 

Claude Security is also available as an MCP connector in Claude.ai and Claude Code; an engineer can pull up a finding, ask Claude about it, start the fix, and mark it resolved in the same session.

 This is the correct agentic-security workflow pattern — rather than requiring engineers to context-switch between a security dashboard and a code editor, the finding, the question, the fix, and the resolution all live in the same surface.

---

### ChatGPT / OpenAI: Locked Chats Establish a Privacy Primitive, Slides Add a Collaborative Canvas, and Parallel Agents Enter Rollout

OpenAI's most interaction-design-significant event in this window is not a new agentic surface but a privacy-interface primitive that signals a maturing understanding of how ChatGPT is actually being used: **Locked Chats**, shipping October 20 to all plans including Free.



OpenAI announced that users can now lock ChatGPT conversations to keep sensitive chats private when others may have access to their screen or device; users can secure their locked chats with a four-digit PIN, or use Face ID or Touch ID on supported devices.

 The trust-design boundary that OpenAI has drawn honestly is the one that matters for enterprise practitioners: 

the feature does not add end-to-end encryption, does not change data retention, and does not remove anything ChatGPT already remembered.

 This transparency about what the lock does *not* do is the correct disclosure posture — a feature called "Locked Chats" that implied encryption without delivering it would be a more dangerous UX than one that is explicit about operating at the UI layer. 

With Memory enabled, Locked Chats has its own separate memory shared across conversations within the section; new messages sent after locking a chat can update that memory but do not update regular Memory.

 The memory-partitioning design is the feature's most consequential interaction pattern: it means sensitive-context conversations stay in a contained memory space, preventing information from locked sessions from silently leaking into the regular conversation surface.

The second significant ChatGPT UX advance in this window is **ChatGPT Slides**, which launched October 16 and extends the Space collaborative workspace into the presentation format. 

ChatGPT Slides lets users create presentations and keep working on them with their team in Space; users can start from a conversation, files, or an outline, or share an example deck to guide the style and layout.

 The design significance here is the Space integration: rather than creating a presentation in a separate tool and importing it, Slides treats the deck as a first-class Space artefact — meaning team members can iteratively refine the deck inside the same collaborative surface where they are doing the underlying research and conversation.

The third advance — **GPT-6 Pro parallel agents** — is the agentic-workflow development with the longest-term UX implications. 

GPT-6 Pro in the chat tab now offers faster responses, improved use of plugins and tools, and multiple agents that can work on different parts of a task in parallel; users can follow their progress in the conversation and open completed tasks to see what each agent did.

 The "follow their progress in the conversation" design is critical: by surfacing parallel agent activity as an inspectable trace inside the existing conversation thread rather than in a separate orchestration view, OpenAI keeps the user's governance point at the familiar surface rather than requiring them to learn a new multi-agent monitoring interface.

---

### Google Gemini: Voice Enters the Document, and Notebook Gets a Plan-Before-Build Gate

Google's most consequential Workspace interaction-design advances in this window arrive together on October 21 and share a common thesis: the most valuable point at which to insert Gemini into a creative workflow is not after the user has finished drafting, but before they have started — as a voice-driven collaborator that captures unstructured thinking and converts it into structured output.

**Docs Live** is the clearer implementation of this thesis. 

Docs Live is now rolling out to eligible Workspace users of the Google Docs mobile app on Android and iOS; this new feature acts as a hands-free thought partner and co-writer that helps you build structured, context-aware documents on the fly using natural conversation.

 The context-synthesis capability is the trust-design advance that distinguishes Docs Live from simple voice transcription: 

Gemini automatically and securely draws from relevant content in your Gmail, Drive, Chat, and the web, meaning the output is personalised and relevant to what you need.

 This ambient-context pull shifts the mobile document-creation interaction from "user dictates, AI transcribes" to "user describes intent, AI assembles context and drafts" — a meaningfully different delegation contract that positions the mobile Doc session as a briefing to Gemini rather than a dictation to a recorder. 

It is worth noting that Docs Live is not just a fancy name for voice transcription; the feature brings a Gemini Live-like experience inside Google Docs.



**Gemini Notebook's guided Slide Deck and Video Overview creation** is the plan-before-build advance that deserves practitioner attention as a trust-design pattern. 

Gemini Notebook now gives users more creative control over Slide Decks and Video Overviews; instead of jumping straight to a final output, Gemini Notebook can now walk users through a step-by-step creation flow so they can steer the content further and guide the visual style and format.

 The Review toggle is the specific transparency mechanism: 

if you turn on the Review toggle, you can preview the slide deck outline or video producer notes in the Studio panel and give written feedback before generating the final output.

 This plan-then-generate pattern — surfacing the agent's intent before it executes — is the correct human-in-the-loop design for a creative workflow where the cost of an unwanted output is not just compute but the user's creative time spent reviewing something that missed their intent. Meanwhile, 

Skills in Workspace apps remain delayed until further notice

, continuing to widen the planning gap for enterprise teams building Gemini-native workflows.

---

### Microsoft Copilot: The Spending-Policy Gate Is Now the Primary UX Design Decision

Microsoft's most consequential Copilot interaction-design development crystallising in this window is less a feature launch than a governance-architecture reality: the **Copilot Credit spending-policy framework** has become the primary decision gate that determines which users can access which agentic capabilities — and it requires active admin configuration before the new surfaces are accessible at all.



Microsoft has split Copilot into two billing tracks and rebuilt the app around a new Home screen, Code, and an always-on agent called Autopilot, so admins now have spending policies and access defaults to decide on before users see any of it.

 The UX implication is a new class of interaction-design problem: for enterprise users, the experience of Copilot's new agentic surfaces is entirely governed by whether an admin has created a spending policy and what its credit ceiling is. 

A visible Code tab does not establish that the user can open the capability; spending-policy and preview requirements still apply.

 This creates a discoverability-and-disappointment UX pattern: users who see the Code, Autopilot, or SharePoint advanced tabs in the Copilot app may encounter a hard stop at the capability boundary rather than a graceful onboarding flow — unless admins have pre-configured the spending policy that enables access.



Autopilot, previously called Scout, is an always-on personal agent in the Copilot app with persistent context, identity, and memory; it has its own tab and uses usage-based billing, needing a Copilot licence and a spending policy.

 The rename from Scout to Autopilot is itself a significant UX signal: it shifts the interaction frame from "a feature that scouts information for you" to "a mode of operation where the agent pilots your workflow while you are doing other things" — a more ambitious delegation metaphor that sets a higher user expectation for autonomous operation. 

The Notebooks UX refresh brings a refreshed experience to the Microsoft Copilot app and OneNote to help keep notebooks organised and easy to use by grouping and reordering content from the navigation pane; the new UX update is currently available in Frontier.

 For enterprise practitioners, the admin action that matters most this week is configuring spending policies before Copilot's October and November rollouts surface UBB prompts to users unprepared for a credit ceiling.

---

### Grok (xAI): One Subscription, Subagent Approval Cards Fixed, and the Pipeline Safety Sprint Continues

xAI's most interaction-design-relevant development in this window is a consolidation story rather than a launch: the confirmation that 

for the first time, one AI subscription supports the full path from thinking and creating to building and sharing — Grok supports chat, voice, and image and video generation, and Grok Bot gives users AI teammates that get work done.

 The UX significance of single-subscription coverage is the elimination of the capability-tier decision from the user's moment of task initiation: rather than consulting a feature matrix before deciding which Grok surface to invoke, a subscriber can reach for voice, image, video, or Bot without a plan-tier check.

On the Grok Build governance front, the most important fix in this window addresses a critical trust-design failure in multi-agent sessions: 

approval cards for background subagents no longer disappear when the parent turn ends.

 This was the most consequential UX bug in Grok Build's agentic workflow surface — an approval card that disappears before the user can act on it is not a UX inconvenience but a governance failure, as it removes the human's ability to exercise the review authority the system promised them. The pipe-safety fix that arrived with v1.0.62 carries forward into this window: 

`grok update` and `grok login` no longer crash when stdout or stderr is closed or unwritable.

 For enterprise teams running Grok Build in CI/CD pipelines where output streams are frequently redirected or truncated, this prevents a class of silent pipeline failures that were previously invisible at the consuming process layer.

---

### Perplexity: Sovereign Computer, Email Triggers, and the Three-Tier Compute Governance Architecture Completes

Perplexity's most structurally significant advance in this window is the completion of what is now the most coherent multi-tier compute governance architecture in the consumer AI agent category. The **Valarian partnership, announced October 20**, extends the on-device Mac mode into the institutional deployment context. 

Perplexity announced a partnership with UK-based sovereign infrastructure company Valarian on October 20, 2026, to bring Perplexity Computer inside institutions' own servers and systems, including air-gapped networks isolated from the live web and other outside networks.

Deployed through ACRA, Valarian's sovereign execution environment, Perplexity's answer, research, and discovery capabilities run under the customer's own policy, against the customer's own data, on compute the customer chooses; Perplexity provides the experience layer — the harness, tools, and interaction model — while Valarian provides the sovereign execution layer: policy, runtime boundaries, workload orchestration, and compute flexibility.

 The interaction-design significance of this architecture split is the explicit separation of the *experience layer* from the *execution layer*: it means the same Perplexity Computer interface — the same task harness, the same tool invocation model, the same agent orchestration — can run on a consumer's Apple silicon, a hybrid cloud, or an air-gapped government server, with the governance contract determined by where the execution layer sits rather than by which product the user purchased. 

Security teams receive audit records that provide visibility into access decisions and workload activity.



The **Computer in Email** launch in the same window adds a new agentic trigger surface that is significant for temporal UX: 

Perplexity adds Computer in Email, letting users start and continue Computer sessions from email threads, and expands model access with GPT-5.6 Terra and Luna.

 The email-as-agent-trigger pattern converts an existing communication surface into a task-initiation primitive — users can begin a Computer session by forwarding an email thread or replying with a task description, without switching to the Perplexity app. 

GPT-5.6 Terra is now the default model for Computer subagents and is available as an orchestrator model, while GPT-5.6 Luna is the primary model for scheduled automations — use Terra for complex multi-step work and Luna for recurring workflows without choosing a model for every run.

 The default model assignment by task type — rather than requiring users to select a model for each session — is the correct cost-governance design for a platform where the difference between a complex reasoning model and an automation model carries meaningful price and performance implications.

---

## The Bigger Picture: Proactive Agents Race, a New API Contract, and the Sovereign Compute Frontier

The 48 hours ending October 22, 2026 mark the moment the proactive ambient agent became a product category rather than a research concept: Claude Duet, ChatGPT Dots, Meta Muse, and Microsoft Autopilot now coexist as four distinct, commercially available proactive agent surfaces, each expressing a different thesis about the correct human approval architecture for an agent that initiates contact rather than waiting for a prompt. Anthropic's answer — selective approval gates on irreversible actions, a single persistent thread, and a morning brief cadence — is the clearest articulation yet of what "proactive but not presumptuous" looks like in product form: the agent earns the right to work in the background by asking permission only at the moments that genuinely require it. Google's simultaneous Docs Live and Gemini Notebook guided-creation advances express the same underlying conviction from the Workspace layer — that the most trustworthy AI intervention in a creative workflow is the one that shows you its plan before executing it, whether that plan is an outline preview before generating a slide deck or a context-synthesis from your Gmail and Drive before drafting a document. Microsoft's Copilot Credit spending-policy framework makes explicit what every other platform's agentic billing architecture has left implicit: when the agent runs on usage-based compute, the admin's spending policy becomes a first-class UX design decision, and a capability that is visible but inaccessible due to a missing credit policy is a trust failure more damaging than a capability that was never shown. Anthropic's API 2026-10-21 — the first versioned API release in over three years — is the platform-contract event that will determine which agentic pipelines survive the autumn: removing temperature controls and moving auth headers are the kind of breaking changes that only make sense when the model itself has become deterministic enough that sampling parameters are no longer the mechanism of output governance. And Perplexity's three-tier compute story — on-device Mac, hybrid cloud, or sovereign institutional server, all running the same Computer harness under the customer's own policy — is the most honest answer yet to the question that will define enterprise AI adoption for the next two years: not "what can the agent do?" but "where does it run, under whose authority, and can you prove it?"

---

## References

[1] macrumors.com. (2026). *Anthropic Launches Claude Duet, a Proactive AI Agent*. [https://www.macrumors.com/2026/10/21/anthropic-claude-duet/](https://www.macrumors.com/2026/10/21/anthropic-claude-duet/)

[2] 9to5mac.com. (2026). *Anthropic takes on ChatGPT Dots and Meta Muse with Claude Duet*. [https://9to5mac.com/2026/10/21/anthropic-takes-on-chatgpt-dots-and-meta-muse-with-claude-duet/](https://9to5mac.com/2026/10/21/anthropic-takes-on-chatgpt-dots-and-meta-muse-with-claude-duet/)

[3] cellcog.ai. (2026). *Claude Duet: Anthropic's Proactive Agent, Explained*. [https://cellcog.ai/blog/claude-duet/](https://cellcog.ai/blog/claude-duet/)

[4] platform.claude.com. (2026). *Migrating to API version 2026-10-21*. [https://platform.claude.com/docs/en/api/migration-2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21)

[5] byteiota.com. (2026). *Claude API 2026-10-21: Temperature Is Gone, and Even the Default Breaks You*. [https://byteiota.com/claude-api-2026-10-21-breaking-changes/](https://byteiota.com/claude-api-2026-10-21-breaking-changes/)

[6] claude.com. (2026). *Claude Security now scans continuously and tracks fixes*. [https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes](https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes)

[7] techcrunch.com. (2026). *ChatGPT now lets you lock your chats*. [https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/](https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/)

[8] aiweekly.co. (2026). *ChatGPT adds PIN-locked chats, not end-to-end encrypted*. [https://aiweekly.co/alerts/chatgpt-adds-pin-locked-chats-not-end-to-end-encrypted](https://aiweekly.co/alerts/chatgpt-adds-pin-locked-chats-not-end-to-end-encrypted)

[9] releasebot.io. (2026). *ChatGPT Updates by OpenAI — October 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[10] workspaceupdates.googleblog.com. (2026). *Create structured documents using just your voice with Docs Live in Google Docs on mobile*. [https://workspaceupdates.googleblog.com/2026/10/create-structured-documents-using-just-your-voice-with-Docs-Live-in-Google-Docs-on-mobile.html](https://workspaceupdates.googleblog.com/2026/10/create-structured-documents-using-just-your-voice-with-Docs-Live-in-Google-Docs-on-mobile.html)

[11] workspaceupdates.googleblog.com. (2026). *Gain more creative control over Slide Decks and Video Overviews in Gemini Notebook*. [https://workspaceupdates.googleblog.com/2026/10/](https://workspaceupdates.googleblog.com/2026/10/)

[12] workspaceupdates.googleblog.com. (2026). *An update on the launch of skills in the Gemini app and Workspace*. [https://workspaceupdates.googleblog.com/2026/10/an-update-on-launch-of-skills-in-gemini-app-and-workspace.html](https://workspaceupdates.googleblog.com/2026/10/an-update-on-launch-of-skills-in-gemini-app-and-workspace.html)

[13] changepilot.cloud. (2026). *October 2026 Microsoft 365 Updates: Copilot Billing, Home & More*. [https://changepilot.cloud/blog/october-2026-microsoft-365-updates-copilot-billing-home-more](https://changepilot.cloud/blog/october-2026-microsoft-365-updates-copilot-billing-home-more)

[14] aguidetocloud.com. (2026). *What's New in Microsoft 365 Copilot: October 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-october-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-october-2026-updates/)

[15] techcommunity.microsoft.com. (2026). *What's New in Notebooks | October 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105)

[16] releasebot.io. (2026). *Grok Build Updates by xAI — October 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[17] releasebot.io. (2026). *xAI Release Notes — October 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[18] perplexity.ai. (2026). *Perplexity brings Computer to enterprise infrastructure with Valarian*. [https://www.perplexity.ai/hub/blog/perplexity-brings-computer-to-enterprise-infrastructure-with-valarian](https://www.perplexity.ai/hub/blog/perplexity-brings-computer-to-enterprise-infrastructure-with-valarian)

[19] unite.ai. (2026). *Valarian Partnership Puts Perplexity Computer on Institutional Servers*. [https://www.unite.ai/valarian-partnership-puts-perplexity-computer-on-institutional-servers/](https://www.unite.ai/valarian-partnership-puts-perplexity-computer-on-institutional-servers/)

[20] releasebot.io. (2026). *Perplexity Release Notes — October 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)