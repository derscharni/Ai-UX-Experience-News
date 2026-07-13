# UX Briefing: The Unified Agent Desktop and the Workspace Execution Race

**July 13, 2026**

Good morning. The 48 hours ending July 13 are defined by the industry's convergent bet on a single, unified agent desktop — a surface where chat, autonomous execution, and browser control collapse into one app — and by the parallel race to make long-horizon, multi-step work the *default* interaction mode rather than a premium feature. **Claude/Anthropic** leads with two simultaneous desktop UX shifts: the **Claude Code built-in sandboxed browser** landing this week as the most structurally significant agentic tool integration since Computer Use, alongside a dense wave of **auto mode safety hardening and agent view improvements** that make background task state legible at a glance; and the **Microsoft 365 write tools** expanding Claude's Cowork connector from search to full action — drafting, sending, and filing. **ChatGPT/OpenAI** delivers its most significant product restructuring in years with the **ChatGPT Work launch on July 9** — a named agent tab powered by GPT-5.6 and Codex technology that produces *finished outputs* rather than chat, accompanied by the physical **merger of the Codex desktop app into the ChatGPT desktop app**, the **Atlas browser deprecation**, and **ChatGPT Sites** in public beta, which turns Work outputs into shareable, updatable web apps. **Google Gemini** continues the active rollout of **Gemini Spark for macOS** — a cloud-based personal agent that works on local files and Workspace workflows while the Mac is locked — alongside **AlphaEvolve reaching GA** on Gemini Enterprise as a code-optimization discovery agent. **Microsoft Copilot** enters the fully billed phase of **Copilot Cowork's general availability**, with the new July redesign's **Tasks tab and July 15 toggle removal** now locking the agentic monitoring layout as the permanent default for all standard-release users. **Grok (xAI)** ships **Grok 4.5** publicly on July 8 as its first Cursor-co-trained agentic coding model, now live in Grok Build and the xAI API console, alongside **21 new multilingual Grok Voice voices** and dense Grok Build UX reliability improvements. And **Perplexity** continues the active landing of its **Computer Analytics dashboard** and **Grok 4.5 support in Computer**, expanding the model-choice surface inside its M365-integrated agentic workspace.

---

## At a Glance: July 13 Highlights

The releases this window converge on a single decisive argument: the AI agent workspace is not a separate product the user navigates to — it is the default desktop, with browser access, background execution, and finished-output generation built into the same window where users have always started their day.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code built-in sandboxed browser** lands on desktop — Claude opens docs, designs, or any site, reads, clicks, and interacts inside a configurable sandboxed pane with per-action approval gates; **agent view rows** now show colored state labels and classifier-written headlines; **Microsoft 365 write tools** enable Claude to draft, send, and file across Outlook, OneDrive, and SharePoint. [1][2][3] |
| **ChatGPT** | **ChatGPT Work** launches July 9 — a named agent powered by GPT-5.6 and Codex that produces finished sheets, slides, docs, and Sites from connected apps; **Codex app merges into the unified ChatGPT desktop app**; **Atlas browser deprecated** as browser-based agentic capability moves into Work; **ChatGPT Sites** launches in public beta. [4][5][6] |
| **Google Gemini** | **Gemini Spark for macOS** continues rollout to AI Ultra subscribers — cloud-based personal agent that organizes folders, drives local files, and runs Workspace workflows autonomously while the Mac is locked; **AlphaEvolve** reaches GA on Gemini Enterprise as a code-optimization discovery agent combining LLM exploration with secure client-side execution. [7][8] |
| **Microsoft Copilot** | **Copilot Cowork** now fully billed across all Microsoft 365 Copilot tenants, with dedicated Cowork tab, browser automation, and personal skills; **July 15 redesign lock** removes the "New Copilot" toggle, making the Tasks tab the permanent default for all standard-release users; **AI content watermarks** rolling out across video and audio. [9][10][11] |
| **Grok (xAI)** | **Grok 4.5** publicly released July 8 via Grok Build, Cursor, and xAI API console — first model co-trained with Cursor's developer data, with 500K context and agentic coding focus; **21 new multilingual Grok Voice voices** ship with voice cloning and speech tags across Voice Agent API, TTS API, and Voice Agent Builder. [12][13] |
| **Perplexity** | **Computer Analytics dashboard** launches tracking credit usage by model across Perplexity Computer; **Grok 4.5 and GPT-5.6 family** added to Agent API model roster; **hybrid inference orchestrator** continues Windows rollout with on-device routing for sensitive data. [14][15] |

---

## Product Highlights

### Claude / Anthropic: The Built-In Browser, Agent View Legibility, and the M365 Write Expansion

Anthropic's most consequential UX move in this window is a surface addition that changes the nature of what Claude Code can *see* during an agentic task — and fundamentally closes the context-switching loop that has been the persistent friction point of AI-assisted development.



**Claude Code on desktop now has a built-in browser.** Claude can pull up docs, designs, or any other site and read, click through, and interact with pages the same way it does with local dev server previews; the browser is sandboxed and configurable, with users choosing whether browsing sessions persist, and safety classifiers reviewing actions on external sites.

 The trust-design architecture here is worth unpacking in detail: 

the first time Claude attempts to act on a particular website, users are asked whether to Allow once, Always allow, or Deny that action.

 This per-site, per-action consent gate is more granular than the blanket permission modes that govern most agentic browsing — it makes the delegation boundary explicit at the moment of action rather than at setup, which is the interaction design that reduces both accidental over-permission and the anxiety of never knowing what the agent just clicked. 

Anthropic distinguishes this in-app approach from its existing Chrome extension, noting that the sandboxed profile excels at anonymous testing and local work, while the extension leverages real user sessions when Claude needs to act on behalf of the user with authenticated access.

 This is a deliberate two-surface UX: clean isolated browsing for development and research; personal-session browsing via extension when the task requires authenticated identity. The combined effect is that the *loop of coding, previewing, researching, and refining* — 

previously requiring the developer to switch windows and manage multiple browser tabs

 — now closes inside a single application.

The second UX cluster of this window arrives in **Claude Code's agent view and auto mode safety hardening**. 

Agent view rows now show a colored state word and a classifier-written headline instead of raw tool call text, and sessions that edit, merge, comment on, or push to an existing PR link it in Claude Agents.

 This is a meaningful disclosure shift: replacing opaque tool-call text with a human-readable, classifier-generated summary collapses the comprehension gap between "what the agent is doing" and "what I understand it to be doing" — a gap that has been the primary trust bottleneck in agentic coding sessions. 

Auto mode now blocks tampering with session transcript files, and asks before running `rm -rf` on a variable it can't resolve from context.

 This is the safety-design pattern that matters most in background execution: the agent does not ask permission for every operation, but it *does* pause at the specific class of irreversible, high-consequence actions where a wrong guess is catastrophic.

On the enterprise connector side, 

the Microsoft 365 connector now goes beyond search: with write tools enabled, Claude can draft, send, and organize email, manage calendar events, update mailbox settings, and create and update files in OneDrive and SharePoint; read and search tools work as before, and Teams remains read-only.

 The UX significance is the shift from *Claude as a read-only research layer inside M365* to *Claude as an execution layer that takes consequential action inside M365* — a permission boundary expansion that also requires explicit admin consent: 

before members can use write tools, a Microsoft Entra administrator needs to consent to the updated permission set and an admin needs to enable them for the organization.

 This admin-gate design correctly treats write-action enablement as an organizational policy decision rather than a per-user toggle — the right trust-architecture for a tool that can now send email on behalf of employees.

---

### ChatGPT / OpenAI: Work Launches, the Desktop Merger, and the Atlas Deprecation as UX Signal

OpenAI's most structurally significant move in this window is a product *architecture* decision, not a feature addition: the **merger of the Codex desktop app into a unified ChatGPT desktop app**, with Chat, Work, and Codex as co-equal tabs — a reorganization that encodes a clear philosophy about what the primary AI interaction surface should be.



**ChatGPT Work** is an agent inside ChatGPT: it takes an outcome, gathers information across your connected apps and workflows, breaks the job into smaller steps, and completes them independently — staying with complex projects for hours; the output is finished material rather than chat — spreadsheets, slides, documents, and interactive web apps — with Codex technology built in, running on GPT-5.6, and including control surfaces like Plan mode (a step-by-step plan you approve before work starts), configurable check-ins, and action approvals.

 The interaction model that matters most here is the **Plan mode approval gate**: before the agent begins executing a multi-step workflow, it presents a step-by-step plan for the user's review and approval. This is the UX decision that separates *autonomous execution you can trust* from *autonomous execution you are anxious about* — it shifts the agent's relationship with the user from "I'll surprise you with the result" to "I'll tell you what I'm about to do and wait for your go-ahead." 

ChatGPT Work is designed to move between devices: a user can start a task from a phone, review a draft on the go, check the status of a longer-running workflow between meetings, then pick the same work back up on the web at their desk.

On July 9, 2026, OpenAI merged ChatGPT and Codex into a single desktop application — not a new model page, not a research preview, not a benchmark chart, but a product merger.

 The UX implication is a reclassification: Codex's agentic infrastructure — browser, computer use, plugins, remote control — becomes the substrate for the entire ChatGPT desktop experience, not a separate tool for developers. 

OpenAI is deprecating Atlas as it brings browser-based agentic capabilities into ChatGPT and Codex; Atlas is scheduled to stop working on August 9, 2026.

 The Atlas deprecation is an unusually legible UX signal: it confirms that the fragmented-surface era (one app for chat, one for agentic browsing, one for coding) is over, and that OpenAI's bet is a single surface where all of those capabilities are accessible from the same prompt box. 

**ChatGPT Sites** lets you turn work or ideas into an interactive website or lightweight app without leaving ChatGPT — creating dashboards, project trackers, launch calendars, prototypes, internal portals, and reports, then previewing and refining the result with ChatGPT before sharing it.

 Sites is the generative UI output layer that completes the Work loop: the agent doesn't just produce a document, it produces a *living, shareable, updatable interface* — moving the output format from static artifact to dynamic web app.

---

### Google Gemini: Gemini Spark for macOS and AlphaEvolve's Code Discovery Agent

Google's most interaction-design-significant development in this window is the continued rollout of **Gemini Spark for macOS** — a product that, more than any other Gemini surface, answers the question of what a *proactive, always-on, cross-context personal agent* looks like when it runs on your device.



**Gemini Spark**, your personal AI agent, is coming to the Gemini app for macOS; it helps you navigate your digital life by working on tasks on your behalf, operating autonomously and under your direction — organizing folders, using local files to build documents, and handling complex workflows across Google Workspace; coming soon, you will be able to command Gemini Spark to run tasks or access local files on your Mac directly from the web or mobile app, ensuring your desktop workflows remain at your fingertips wherever you go.

 The UX architecture of Spark is worth distinguishing from browser-based agent surfaces: it runs *on* the Mac, accesses *local* files, and operates *across* native apps — not inside a browser tab or an iframe. 

Spark transforms Gemini from an assistant into an active partner that does real work on your behalf; since it's a cloud-based agent, Spark keeps working in the background even when you lock your phone.

 The combination of local file access and cloud-based persistence is the design detail that makes Spark architecturally distinct: it is neither a purely cloud agent (which can only access what is connected) nor a purely on-device model (which requires the device to be running) — it is a hybrid that reads local context and executes in the cloud.



Starting today, Gemini Spark is available in English in the Gemini macOS app to Google AI Ultra subscribers aged 18 and over in supported countries.

 The tier restriction — Ultra only at launch — is itself a trust-design signal: Spark's local file access and autonomous background execution warrant the most carefully managed rollout in Google's consumer AI lineup.

On the enterprise side, 

**Gemini Enterprise** adds the AlphaEvolve algorithm optimization agent in GA, bringing a code optimization and discovery service for harder business and research problems with secure client-side code execution and server-side LLM exploration; AlphaEvolve is a code optimization and discovery agent built on Gemini that helps solve the hardest algorithmic problems, combining creative, server-side LLM exploration with secure client-side code execution to autonomously discover new, optimized solutions that surpass human-designed baselines.

 The interaction pattern AlphaEvolve establishes is meaningfully different from standard agentic coding: this is not a model that executes the developer's instructions, but one that *autonomously discovers solutions* and returns them to the human — shifting the UX from *delegation of known tasks* to *exploration of unknown solution spaces*. That is a fundamentally different trust relationship, and it requires its own disclosure architecture. 

Separately, users can now create, import, update, and use skills in the Gemini Enterprise web app — skills are reusable custom instructions that help the assistant perform specific tasks, available as GA with allowlist.

 The skills system is the enterprise-side analogue of OpenAI's SKILL.md model: capturing reusable task instructions in a persistent, shareable form that individual users can teach the agent and organizations can standardize across teams.

---

### Microsoft Copilot: Cowork Billing Goes Live, the July 15 Lock, and the Watermark Layer

Microsoft's most consequential UX moment in this window is not a new feature — it is the **arrival of full Copilot Cowork billing**, which transforms the agentic workspace from a free-preview capability into a metered enterprise product with explicit cost surfaces, and the **July 15 toggle removal** that makes the Tasks-tab-first layout permanent.



**Copilot Cowork** is now generally available to all Microsoft 365 Copilot tenants, bringing new models, image generation, browser use, the Customize page, and consumption billing.

 The governance architecture at GA is the trust-design story: 

administrators can control when Cowork is enabled, who can access it, and how much can be spent; Cowork is "off by default," with admins able to set spending limits at the tenant, group, and user levels.

 This *off-by-default, granular-spend-control* architecture is the enterprise trust pattern that distinguishes responsible agentic deployment from permissive alternatives — the admin must actively choose to turn on the capability, not opt out of it. 

Skills teach Cowork domain expertise, and at GA users can build their own personal ones — the demo's best example is an "email voice" skill that captures how a user writes, so drafted emails sound like them, getting more tailored with use.

 This *learnable personal style* pattern — where the agent internalizes how a specific user works and applies it autonomously — is the most personalization-intensive trust decision in the GA release: it requires the user to accept that the agent will imitate them, which is a meaningfully different consent moment than "the agent will execute this task."



On July 15 for standard release, the toggle will be removed and the updated experience will be default on without the option for users to switch back to the previous experience; on August 22, the updated experience will start rolling out worldwide for deferred release.

 The toggle removal is the administrative act of declaring the agentic monitoring architecture *finished and stable enough to be the only experience* — a meaningful signal that Microsoft considers the Tasks tab, the agent-interaction labels, and the reorganized navigation ready for every standard-release user. 

Additionally, to help provide additional transparency about what content has been generated or altered by using AI in Microsoft 365, **watermarks** can be added to videos and audio content; a policy setting controls the organization's ability to add a visual or audio watermark to video and audio content that users generate or alter using AI in Microsoft 365, with adding watermarks increasing transparency and helping prevent misuse or misattribution of AI-generated content.

 The watermark layer is the trust-disclosure feature with the broadest daily-user significance: it makes AI-generated content visibly attributable at the artifact level — a provenance signal that Perplexity's inline citations address at the claim level, but that Copilot now addresses at the media level.

---

### Grok (xAI): Grok 4.5 in Grok Build, 21 New Voices, and the Multilingual Voice Agent Stack

xAI's most interaction-design-relevant events in this window are the public arrival of **Grok 4.5 inside Grok Build** and the expansion of the **Grok Voice roster** to 21 new multilingual voices — two moves that together complete xAI's full-stack agentic surface for builders who want to wire together coding agents and voice agents from a single provider.



**Grok 4.5** was publicly released on July 8, 2026, initially through Grok Build, the Cursor editor, and the xAI API console; it was not made available in the European Union at launch, with xAI targeting mid-July 2026 for EU availability.

Grok 4.5 is xAI's smartest model built to excel at coding, agentic tasks, and knowledge work — it's their strongest model ever and was trained alongside Cursor.

 The Cursor co-training detail is the UX-relevant signal: a model trained on a coding tool's actual developer workflows has a qualitatively different capability profile for agentic coding tasks than a model trained on general code corpora — it has seen the patterns of real iterative development, not just the patterns of code as text. 

Grok 4.5 is not yet available in the EU in any SpaceXAI products or the API console, with EU availability expected in mid-July.

 This staged geographic rollout — now a recurring pattern across xAI's most autonomous features — continues to trace the contour of EU AI Act compliance work in product shipping decisions.

On the voice side, 

xAI adds 21 multilingual Grok Voice voices with improved naturalness for the original five, plus speech tags, voice cloning, and support across the Voice Agent API, Text to Speech API, and the Grok Voice Agent Builder; all of the new voices are multilingual and available in the realtime Voice Agent API, the TTS API, and the new Grok Voice Agent Builder.

 The UX significance of a 21-voice expansion is not breadth for its own sake — 

each voice was cast for a specific job: support, characters, commentary, advertising, education

 — which means builders now have a voice-identity selection layer with task-appropriate defaults, rather than a generic voice they must customize from scratch. On the Grok Build reliability front, 

Grok Build adds managed command defaults, smoother prompt and tool UI, stronger clipboard and input handling, better rewind and queue behavior, and worktree file links support; teams can now ship default allowed commands via `managed_config.toml`, with user deny rules still winning.

 The `managed_config.toml` default-command management is the enterprise trust-design detail with the most governance significance: it allows teams to pre-approve a set of safe operations while preserving the user's ability to override, encoding a *policy-first, user-controlled* permission model for terminal-level agentic actions.

---

### Perplexity: Computer Analytics, Model Expansion, and the Research-to-Dashboard Pipeline

Perplexity's most consequential UX additions in this window focus on making the internals of its agentic Computer product *legible* to both administrators and users — closing the accountability gap that has been the persistent enterprise adoption friction for agent-as-a-service products.



Perplexity launches **Computer Analytics**, a dashboard for tracking credit usage by model in Perplexity Computer: total credits, active members, average per member, breakdown by model (Claude Opus 4.8 Fast/4.8/4.7, Claude Sonnet 4.6, GPT-5.5, others), and member ranking.

 This is the administrative trust surface that enterprise AI deployments have been missing: a model-level cost breakdown that tells an admin not just *how much was spent* but *which model spent it* — a provenance layer that makes the agent's resource decisions accountable and contestable. The UX implication is that enterprise administrators can now audit agentic spending at the same granularity they would audit cloud infrastructure — shifting AI from a line-item expense to a managed resource with per-model accountability.



In July 2026, the Agent API added support for several new models, including the GPT-5.6 family (Sol, Terra, and Luna) and Grok 4.5, all with direct first-party token pricing.

 The model-roster expansion inside Computer is the flexibility-design decision that matters most for enterprise adoption: an organization whose compliance team requires specific model provenance can now select Claude Opus for regulated document workflows and GPT-5.6 Luna for high-volume summarization within the *same* Perplexity Computer session, without switching products. 

The Deep Research in Computer feature, a new command panel, forking, and improved inline confirmations continue active landing, making it easier to research, build artifacts, and manage usage; Deep Research is now available inside Computer.

 The *research-as-workflow-initiation* pattern — 

start with a complex research question, then keep working from the result by turning findings into a report, spreadsheet, deck, dashboard, website, or follow-up workflow in the same place

 — is the interaction design that most directly competes with ChatGPT Work's *finished output* model, with the key differentiator being that Perplexity's outputs carry inline source attribution at every claim.

---

## The Bigger Picture: The Unified Agent Desktop and the Workspace Execution Race

The 48 hours ending July 13, 2026 mark the week when the fragmented AI tool landscape — one app for chat, one for agentic browsing, one for coding, one for research — collapsed into a single architectural bet that every major platform is now making simultaneously: *the agent desktop*, a unified surface where intent, execution, browser access, and finished-output generation live in one window. OpenAI's merger of Codex into the ChatGPT desktop app, with Chat, Work, and Codex as co-equal tabs, is the most explicit structural statement of this bet; ChatGPT Work's Plan mode approval gate and cross-device session continuity answer the trust question that unified agentic surfaces require. Claude Code's built-in sandboxed browser with per-site, per-action consent gates answers the same question from the safety-first angle: the agent can now see and act on the live web, but the human controls exactly which sites earn trust and which actions require explicit go-ahead. Microsoft's Copilot Cowork entering full billing with a dedicated Cowork tab, admin-level spend controls, and personal skills that learn how a user writes answers the enterprise governance version: the agentic workspace needs a metered, auditable, policy-enforced trust layer before organizations will delegate consequential work to it. Gemini Spark for macOS answers the local-file version of the same challenge: a cloud-based agent that reads your laptop's folders and Workspace calendar and keeps working when the lid closes requires the deepest delegation trust of anything shipping this week — which is precisely why it is restricted to Ultra subscribers at launch. Perplexity's Computer Analytics dashboard answers the accountability version: when an agent can choose between Claude Opus 4.8, GPT-5.6 Sol, and Grok 4.5 for different subtasks in the same session, the enterprise administrator needs a model-level cost and usage breakdown to maintain meaningful oversight of what the system spent and why. What the industry is converging on — one app merger, one in-app browser, one agent tab, one metered billing unlock, one per-site consent gate at a time — is the recognition that the hardest problem in agentic UX is not the *capability* of the agent but the *legibility of its intentions*, *accountability of its costs*, and *reversibility of its actions* — and that no amount of raw capability will produce durable adoption without all three.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] 9to5Mac. (2026). *Anthropic highlights Claude Code's in-app browser on the desktop*. [https://9to5mac.com/2026/07/10/anthropic-highlights-claude-codes-in-app-browser-on-the-desktop/](https://9to5mac.com/2026/07/10/anthropic-highlights-claude-codes-in-app-browser-on-the-desktop/)

[3] Releasebot. (2026). *Claude Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[4] OpenAI Help Center. (2026). *ChatGPT Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] The Next Web. (2026). *OpenAI launches ChatGPT Work, an agent built to finish the job*. [https://thenextweb.com/news/openai-chatgpt-work-agent-launch](https://thenextweb.com/news/openai-chatgpt-work-agent-launch)

[6] Releasebot. (2026). *ChatGPT Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] Gemini Apps. (2026). *Gemini Apps Release Updates & Improvements*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/)

[8] Releasebot. (2026). *Google Release Notes — July 2026*. [https://releasebot.io/updates/google](https://releasebot.io/updates/google)

[9] Microsoft Learn. (2026). *What's new in Copilot Cowork*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new)

[10] SuperSimple365. (2026). *What's new in Microsoft 365 and Copilot? June 2026*. [https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/](https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/)

[11] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[12] xAI. (2026). *Introducing Grok 4.5*. [https://x.ai/news/grok-4-5](https://x.ai/news/grok-4-5)

[13] Releasebot. (2026). *xAI Release Notes — July 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[14] jls42.org. (2026). *Claude Code Desktop adds a browser and moves to v2.1.206*. [https://jls42.org/en/news/ia-actualites-10-jul-2026](https://jls42.org/en/news/ia-actualites-10-jul-2026)

[15] Perplexity. (2026). *Perplexity API Changelog*. [https://docs.perplexity.ai/changelog/changelog](https://docs.perplexity.ai/changelog/changelog)

---