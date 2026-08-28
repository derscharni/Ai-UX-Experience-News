# UX Briefing: Restricted Agents, Portable Compute, and the Cross-Session Frontier

**August 28, 2026**

Good morning. The 48 hours ending August 28 are defined by a single structural force playing out on every platform simultaneously: agents are being hardened at the seams — the points where sessions meet other sessions, where cloud compute meets local hardware, and where one agent hands context to another. **Claude/Anthropic** ships its densest agentic governance bundle of the late-August cycle: **Claude Code gains a `--restricted` mode** that strips command-execution and web-fetch tools to create a sandboxed surface, while **cross-session messaging expands to Bedrock, Vertex, and Foundry** — and the plugin marketplace hardens against invisible-character name injection. **ChatGPT/OpenAI** executes two convergent trust-design moves that redefine what a "temporary" session means: **temporary chat gains full personalisation controls** including memory, plugins, and custom instructions, blurring the line between ephemeral and persistent context, while **webhook-triggered scheduled tasks** land in Work with admin-gated sharing — making agentic automation both more powerful and more auditable. **Google Gemini** extends its AI capture arc into physical space: **Gemini's "Take notes for me" expands to in-person meetings** — audio captured by device microphone, structured into a Google Doc without a video call — while the hardware touch-controller note-taking rollout beginning August 31 establishes direct physical presence controls for meeting-room AI. **Microsoft Copilot** lands its most consequential IDE trust-design event of the year: **VS Code 1.135 ships the Agent Host Protocol and the experimental Rubber Duck feature** — a cross-model second-opinion primitive that uses a different AI model to critique the primary agent's work — alongside cross-app session continuity for Copilot and Claude agent sessions. **Grok (xAI)** completes its four-cloud distribution sweep with **Grok 4.6's arrival on Microsoft Foundry** — adding governance-and-evaluation infrastructure alongside raw model access — while simultaneously **expanding Grok Bot access** to Cursor Pro+, Ultra, and Teams plans, pushing the persistent-credential agent into the developer IDE where it matters most. And **Perplexity** delivers the week's most consequential trust-design event in the agentic compute category: **Portable Computer launches on August 25** — a fully local-first version of Perplexity Computer running on Nvidia RTX GPUs, with data-on-device by default and explicit user consent required before any cloud escalation.

---

## At a Glance: August 28 Highlights

This window's releases converge on a single architecture-level signal: the agentic AI industry is simultaneously hardening its execution boundaries (restricted modes, local-first compute, plugin injection controls), extending its session-coordination primitives (cross-session messaging, cross-app session continuity, webhook triggers), and moving AI presence controls closer to the physical world (hardware touch controllers, in-room audio capture).

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **`--restricted` mode lands in Claude Code** — removes built-in command/code execution and `WebFetch` unless explicitly named in `--tools`, keeps file tools inside the working directory, and ignores user/project/local settings; cross-session messaging (`SendMessage`/`ListAgents`) expands to Bedrock, Vertex, and Foundry; plugin marketplace hardened to reject names with control/invisible characters; Sonnet 5 auto-compact window expanded to full 1M context. [1][2][3] |
| **ChatGPT** | **Temporary chat gains full personalisation controls** — memory, plugins, and custom instructions now available in temporary sessions; temporary chats can be saved to persistent history; webhook-triggered scheduled tasks land in Work with admin-gated sharing; `@mention` task cross-referencing in Codex; New Interrupt hooks for mid-turn command interception; DALL·E GPT retires August 30. [4][5][6] |
| **Google Gemini** | **"Take notes for me" expands to in-person meetings** — device microphone captures audio outside video calls, Gemini compiles structured summary, action items, and transcript to Google Docs; hardware touch-controller note-taking rollout begins August 31, surfacing start/stop/pause controls directly on room hardware without Companion mode. [7][8][9] |
| **Microsoft Copilot** | **VS Code 1.135 ships Agent Host Protocol and Rubber Duck** — experimental cross-model second-opinion feature critiques primary agent work using a different model; external agent sessions let developers continue Copilot or Claude sessions from other apps in VS Code; per-model token breakdown in chat response footer; Python-in-Excel via Edit with Copilot reaches GA for Windows, Mac, and web. [10][11][12] |
| **Grok (xAI)** | **Grok 4.6 arrives on Microsoft Foundry** — public preview with 500K context, configurable reasoning levels, and unified evaluation/governance infrastructure; Grok Bot subscription access expands to Cursor Pro+, Ultra, and Teams plans, placing the persistent-credential agent inside the developer IDE; Grok Build adds `tools report read-only status` for safer restricted-agent workflows. [13][14][15] |
| **Perplexity** | **Portable Computer launches August 25** — fully local-first Perplexity Computer on Nvidia DGX Spark and RTX GPUs; model, files, and workflows stay on-device with zero token costs; cloud escalation requires explicit user consent; `Computer in Email` allows starting Computer sessions from email threads; Search as Code execution reliability raised from 81.9% to 92.6%. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Restricted Mode, Cross-Session Reach, and Marketplace Hardening

Anthropic's most consequential agentic safety UX event in this window is the arrival of **`--restricted` mode** in Claude Code. 

The new `--restricted` flag (or `CLAUDE_CODE_RESTRICTED=1`) removes the built-in tools that run commands or code and `WebFetch` (unless named in `--tools`), keeps file tools inside the working directory, refuses `bypassPermissions`, and ignores user, project, and local settings files.

 The UX significance of this is disproportionate to its single-line description: it creates a formally defined sandboxed Claude Code surface that operators can expose to untrusted environments or less-privileged users without the full execution surface of an unconstrained session. Previously, scoping what Claude Code could do required careful per-project permission configuration; `--restricted` inverts the model — you start from a minimal surface and explicitly add back the tools you trust, rather than starting from a full surface and removing things. This is the operator-governance pattern that enterprise security teams require before they can sanction agentic coding assistance on sensitive repositories.

The cross-session coordination arc continues its expansion in this window. 

Claude Code adds cross-session messaging, usage credits for Enterprise, and better server-managed settings diagnostics, improving agent workflows, remote control, and prompt caching while fixing many session, login, MCP, and terminal bugs.

 Specifically, 

cross-session messaging in Linux user namespaces now limits root-equivalent trust for unmapped owners to canonical system directories

 — a trust-design boundary that governs what a session can reach when it operates in a namespaced container. For practitioners running multi-agent Claude Code workflows on shared infrastructure, this is the namespace-level permission primitive that was previously missing. The SendMessage architecture — where 

only text is shared between sessions; conversation history, files, and operating permissions do not transfer to the other party

 — means the coordination primitive is deliberately narrow, an important containment design choice.

The third hardening event in this window addresses the plugin ecosystem surface. 

Plugin marketplace hardening now rejects names containing control or invisible characters, and marketplace-supplied text in `/plugin` and `claude plugin` output is escape-safe.

 The UX implication of this fix is one that most practitioners will miss unless they are specifically thinking about supply-chain injection vectors: invisible Unicode characters in plugin names are a well-documented technique for smuggling adversarial content past visual inspection. Making marketplace-supplied text escape-safe closes the rendering-layer attack surface — an agent that lists its available plugins cannot be made to display or execute injected content through that listing.

---

### ChatGPT / OpenAI: Temporary Chat Personalisation and the Webhook Task Arc

OpenAI's most interaction-design-significant event in this window is a redesign of what "temporary" means in ChatGPT. The new **temporary chat personalisation controls** fundamentally blur the line between ephemeral and persistent sessions. 

Rolling out now, users can choose to personalise responses in a temporary chat with memory, plugins, and custom instructions from their regular chat settings, and can also choose to save a temporary chat.

Personalised temporary chats can use memories, custom instructions, and plugins to tailor responses; they do not create new memories and remain out of chat history unless saved.

 The trust-design implication is worth examining carefully: a temporary chat that uses your memories is not meaningfully temporary from an information-access perspective — it accesses your accumulated context without adding to it. This shifts temporary chat from "clean room" (no memory access, no history) to a nuanced spectrum of context states, where the user now has to actively reason about which context is flowing in and which record is flowing out. The save-a-temporary-chat path — 

when a conversation becomes useful for the future, it can be added to chat history; saving converts it into a regular chat, so it follows account-level personalisation settings and model-improvement preferences

 — is the escape hatch that makes this design coherent: the user decides the session's archival fate after the conversation, not before.

The second consequential UX development is the arrival of **webhook-triggered scheduled tasks** in ChatGPT Work. 

ChatGPT adds webhook-triggered scheduled tasks in Work, plus shared tasks and flexible limits for Free users; it also expands Work's browser to complete tasks on signed-in websites, with secure logins, password manager support, and confirmation before consequential actions.

 The interaction design significance here is the combination of three elements landing together: webhook triggers (an external system can now initiate an agentic task, not just the user), signed-in website access (the agent can act in the user's authenticated sessions), and confirmation before consequential actions (a minimal approval gate on the highest-stakes operations). 

Eligible members can share scheduled or webhook-triggered tasks with others in the same workspace, who can review and customise the instructions; admins control sharing with the "Share chats and scheduled tasks in the workspace" setting.

 Admin-gated task sharing is the governance primitive that makes webhook-triggered agentic automation viable in enterprise contexts: a shared task is reviewable by peers and controllable by administrators, not just the original author.

In the Codex surface, 

users can now reference other Codex tasks with `@` mentions and ask agents to read, create, or message them from the terminal; new Interrupt hooks run commands or MCP handlers when an active top-level turn is interrupted, and untrusted projects no longer supply project-level AGENTS.md instructions.

 The removal of AGENTS.md trust for untrusted projects is the supply-chain-hardening equivalent of Claude Code's plugin-name injection fix: it prevents a cloned repository from injecting agentic instructions into a Codex session the developer didn't intend to authorise.

---

### Google Gemini: In-Person Note-Taking and the Physical Control Surface

Google's most consequential Workspace UX event in this window is the expansion of **Gemini's "Take notes for me" to in-person meetings**. 

Starting August 11, 2026, Google began rolling out a feature that takes Google Meet's automatic note-taking outside of video calls — the same "Take notes for me" tool can now listen in on a meeting held in a room, around a table, with no video connection active; the phone's or computer's microphone records the conversation, Gemini processes it, and returns a Google Docs file with a summary, a list of action items, and a full transcript.

 This is a meaningful perimeter shift in the AI capture surface: previously, Gemini's note-taking was bounded by the video call — a digital session with a clear start and end. Moving it to ambient room audio, activated from the device's home screen, removes that boundary. 

Gemini captures notes, then creates a structured summary, action items, and transcript in Google Docs and saves it to Drive.



The companion event — arriving August 31 — extends the control surface for this AI capture into the physical environment. 

Google will start rolling out the ability to start, stop, and manage "Take notes for me" directly from the Google Meet Hardware touch controller for eligible meetings, ensuring in-room participants have direct control over Gemini note-taking without being in Companion mode.

Historically, managing AI features during a meeting required a user to join from a laptop in Companion mode; this update surfaces the necessary controls directly on the touchscreen hardware.

 The trust-design implication of this hardware-surface control is significant: it makes the AI presence in a physical room legible and governable by anyone in the room, not just the person who joined digitally. 

Users can easily see if Gemini is taking notes and toggle its state between active and inactive; users can confidently pause note-taking during off-the-record discussions, then resume with the tap of a button.

 The pause-for-off-the-record pattern is the human override design that physical-room AI capture requires — a one-tap way to assert that what follows should not be captured, without ending the session. Together, these two Google events mark the moment that Gemini's AI capture surface formally crosses the threshold from "digital call" to "physical room" — and the control design for that crossing is landing alongside it, not after.

---

### Microsoft Copilot: The Agent Host Protocol and the Rubber Duck Reckoning

Microsoft's most trust-design-significant release in this window is **VS Code 1.135**, which ships on August 26 and introduces two primitives that change the agentic IDE landscape simultaneously. 

The Rubber Duck agent is a built-in critic that provides a constructive second opinion on plans, code, and tests of the primary agent, using a different AI model from the one driving the session; Microsoft's latest update to VS Code, released August 26, features Rubber Duck as well as UX improvements to the Agents window.

 The interaction design pattern Rubber Duck establishes is the cross-model audit loop: an agent's output is reviewed not by a human but by a second model operating from a different perspective. 

The experimental feature enables AI models to review each other's work, closing 74.7% of the performance gap to flagship models on SWE-Bench Pro.

 For UX practitioners, Rubber Duck signals that the next phase of human-agent collaboration is not human-reviews-agent but agent-reviews-agent, with the human inspecting the disagreements between the two reviewers rather than each individual output.

The companion session-continuity event in VS Code 1.135 is equally consequential for agentic workflow design. 

The Sessions list in VS Code can now show recent Copilot or Claude agent sessions created in other applications; by default, VS Code shows up to two recently updated external sessions; users can select a session from the Sessions list to view the conversation and continue it in VS Code with their Copilot subscription.

 This establishes a new interaction pattern: the agent session is no longer anchored to the application in which it was started. A session begun in the Copilot app on mobile can be resumed in VS Code on desktop — the work migrates with the developer, not the other way around. 

To give better insight into chat usage, Microsoft has redesigned the chat response footer; hovering over the footer shows a per-model breakdown of the input, cached input, and output tokens used in the chat turn.

 The per-model token breakdown is a transparency primitive that makes the multi-model routing inside Copilot legible at the turn level — a meaningful step toward making the model-selection decisions that affect the quality and cost of agentic work visible to the people commissioning that work. On the M365 surface, 

Edit with Copilot now helps users work with Python in Excel by executing Python code for advanced analysis, automation, and data transformation with results outputted directly in the workbook.



---

### Grok (xAI): Microsoft Foundry Landing and the Cursor Bot Expansion

xAI's most interaction-design-significant event in this window is the completion of **Grok 4.6's four-cloud governance arc** with its arrival on Microsoft Foundry. 

Grok 4.6 from SpaceXAI is available in Microsoft Foundry Models through public preview, bringing SpaceXAI's latest frontier model to developers through a unified platform for model discovery, evaluation, deployment, and governance.

 The UX distinction between Foundry access and raw API access is the governance layer: 

Foundry gives organisations a single place to evaluate Grok 4.6 against other frontier models, run workload-specific tests, deploy managed endpoints, and operate with enterprise security and governance controls.

 With Grok 4.6 now simultaneously on Amazon Bedrock, Google Vertex AI, GitHub Copilot, and Microsoft Foundry, the model's four-cloud distribution sweep means that enterprise teams can access configurable long-horizon reasoning capacity — 

Grok 4.6 focuses on long-running agents and ambitious interactive and visual work, staying with complex tasks across many steps, whether researching a topic, analyzing information, working across a codebase, or turning an idea into a polished application

 — from inside whichever cloud governance toolkit their security team has already approved.

The companion distribution event is the expansion of **Grok Bot** access to the developer IDE environment. 

xAI expands Grok Bot beyond beta, making the AI teammate available in SuperGrok Plus, SuperGrok Heavy, Cursor Pro+, Cursor Ultra, and Cursor Teams plans, bringing always-on digital coworkers that can handle real work across apps, inboxes, and tools.

 The UX significance of Cursor-plan access is not merely distribution — it is context. Grok Bot's persistent-credential, always-on architecture, in which the agent signs into apps and returns only for approval, is now available to the same developers who are actively writing code in Cursor's agentic environment. This creates a dual-agent surface: Cursor's in-IDE coding agent working on the immediate task, and Grok Bot operating asynchronously across the developer's connected apps and inbox in parallel. On the Grok Build surface, 

tools now report whether they only read data, enabling safer restricted agents and subagents

 — a read-only signal that complements the restricted-mode hardening arc Claude Code is executing in parallel, and suggests an industry-wide emerging convention for action-safety classification at the tool level.

---

### Perplexity: Portable Computer and the Local-First Trust Architecture

Perplexity's most consequential UX event of the week — and arguably the most significant trust-design statement in the agentic compute space this August — is the launch of **Portable Computer** on August 25. 

Portable Computer runs Perplexity Computer entirely on device with NVIDIA, keeping private data local and escalating to the cloud only when a task needs it.

Perplexity is launching Portable Computer, a version of its agentic "Computer" platform that runs entirely on hardware users already own — starting with Nvidia's DGX Spark desktop supercomputer and Linux machines equipped with Nvidia RTX GPUs.

 The trust-design architecture this establishes is the inverse of every other platform in this briefing: rather than governing what a cloud agent can reach, Portable Computer makes the question moot by keeping the model, the files, and the execution loop on the user's own hardware. 

Local tasks incur no token charges and keep data on-device by default, with users asked for permission before the system escalates a step to a cloud model.

 This consent-before-cloud-escalation pattern is the trust primitive that makes Portable Computer usable for the workloads where cloud agents have faced the most enterprise resistance: confidential codebases, financial documents, and regulated data.

The agentic-architecture insight embedded in Portable Computer's design deserves attention. 

Alongside the launch, Perplexity published a research paper arguing that effective local agents require the model and the agent harness to be designed together; the core insight is that general-purpose harnesses assume a frontier model that can absorb enormous contexts, navigate sprawling tool surfaces, and plan over long horizons — small local models buckle under those demands; Perplexity found empirically that although models like Qwen 3.8 27B advertise 260,000-token context windows, they begin to struggle beyond 100,000 tokens.

 This co-design principle — that the harness and model must be matched, not assembled independently — is a meaningful interaction-design contribution to the local-agent conversation: the UX failure mode of a capable-sounding but context-limited local model is not a model failure, it is a harness mismatch. The companion release is equally significant for Perplexity's agentic surface: 

users can send or forward an email to `computer@perplexity.ai` to start a Computer session from email; Computer reads the thread context and replies only to the verified sender in the same thread using that sender's existing connectors, permissions, and Memory.

 **Computer in Email** is the temporal UX pattern applied to the oldest async medium: a user can initiate a multi-step agentic task from their email client and receive the result back in the same thread, with the agent inheriting connectors and permissions scoped to that sender identity. And 

two Search as Code update batches raised execution reliability from 81.9% to 92.6%, with real-world workflows also showing higher user satisfaction at 8% lower per-task cost.



---

## The Bigger Picture: Restricted Agents, Portable Compute, and the Cross-Session Frontier

The 48 hours ending August 28, 2026 crystallise a design moment that the AI agent industry has been approaching all month: the frontier between where an agent runs, what it can reach, and who can see it crossing those two boundaries is now being formally governed at every layer simultaneously. Claude Code's `--restricted` mode defines a minimal trusted surface; Grok Build's tool read-only reporting classifies actions by reversibility; ChatGPT's untrusted-project AGENTS.md suppression blocks instruction injection at the session boundary; and Perplexity Portable Computer moves the entire execution environment on-device so the governance question shifts from "what can the cloud agent reach" to "when does the user consent to cloud involvement at all." What makes this window distinct from previous governance updates is the spatial and temporal breadth of where these boundaries are now being drawn: not just at the toolset layer in an API, but in physical meeting rooms (Google's hardware touch controllers), in the IDE session itself (VS Code's Agent Host Protocol and Rubber Duck cross-model audit), across sessions running in parallel on different machines (Claude Code's cross-session messaging on Bedrock/Vertex/Foundry), and in the inbox of an email thread (Perplexity Computer in Email). The industry is not building a single approval gate — it is building an interconnected mesh of context-scoped trust signals, each encoding a specific answer to the question "at this boundary, who is responsible for what happens next?" The platforms that get this architecture right are the ones where that answer is legible, auditable, and adjustable by the operator at every layer — not just at the top-level prompt.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — August 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] Gradually AI. (2026). *Claude Code Changelog (August 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[3] Releasebot. (2026). *Anthropic Release Notes — August 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[4] Releasebot. (2026). *ChatGPT Updates by OpenAI — August 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[5] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[6] Releases.sh. (2026). *OpenAI Release Notes & Changelog — August 2026*. [https://releases.sh/openai](https://releases.sh/openai)

[7] Pasquale Pillitteri. (2026). *Google Meet Now Takes Notes at In-Person Meetings with Gemini*. [https://pasqualepillitteri.it/en/news/11419/google-meet-take-notes-in-person-meetings](https://pasqualepillitteri.it/en/news/11419/google-meet-take-notes-in-person-meetings)

[8] Releasebot. (2026). *Google Meet Updates by Google — August 2026*. [https://releasebot.io/updates/google/google-meet](https://releasebot.io/updates/google/google-meet)

[9] Google Workspace Updates Blog. (2026). *Control "Take notes for me" directly from Google Meet hardware touch controllers*. [https://workspaceupdates.googleblog.com/2026/08/control-take-notes-for-me-directly-from-Google-Meet-hardware-touch-controllers.html](https://workspaceupdates.googleblog.com/2026/08/control-take-notes-for-me-directly-from-Google-Meet-hardware-touch-controllers.html)

[10] Visual Studio Code. (2026). *Visual Studio Code 1.135*. [https://code.visualstudio.com/updates/v1_135](https://code.visualstudio.com/updates/v1_135)

[11] InfoWorld. (2026). *Visual Studio Code 1.135 introduces Rubber Duck agent*. [https://www.infoworld.com/article/4215053/visual-studio-code-1-135-introduces-rubber-duck-agent.html](https://www.infoworld.com/article/4215053/visual-studio-code-1-135-introduces-rubber-duck-agent.html)

[12] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[13] Microsoft Community Hub. (2026). *Grok 4.6 comes to Microsoft Foundry Models*. [https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/grok-4-6-comes-to-microsoft-foundry-models-built-for-long-horizon-reasoning-and-/4547578](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/grok-4-6-comes-to-microsoft-foundry-models-built-for-long-horizon-reasoning-and-/4547578)

[14] Releasebot. (2026). *xAI Release Notes — August 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Perplexity AI. (2026). *Introducing Portable Computer for local-first AI*. [https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai](https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai)

[17] VentureBeat. (2026). *Perplexity partners with Nvidia to launch Portable Computer, a fully local AI agent with zero token costs*. [https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)

[18] Releasebot. (2026). *Perplexity Release Notes — August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)