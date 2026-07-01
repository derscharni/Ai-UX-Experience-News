# UX Briefing: Desktop Agents, Scheduled Tasks, and the Session Observatory

**June 29, 2026**

Good morning. The last 48 hours land on four stories that together describe a single shift in agentic UX: the locus of agent control is moving from cloud tab to local desktop and phone, and the interfaces that manage that expansion are maturing fast. **Google Gemini** shipped its most consequential desktop release of the year on June 30, bringing **Gemini Spark** to the macOS app for the first time — giving Ultra subscribers a local file agent that runs in the background, connects to Canva, Dropbox, Google Tasks, Keep, and custom MCP servers, and will soon accept remote task dispatch from a mobile phone; **ChatGPT/OpenAI** retired its **Pulse** proactive briefing feature and replaced it with a full **Scheduled Tasks** management hub — a sidebar observatory where users can view, pause, edit, and delete every recurring automation in one place — while simultaneously previewing **GPT-5.6 Sol/Terra/Luna** to approximately 20 government-approved partner organisations; **Claude/Anthropic** shipped a dense wave of **Claude Code** quality and session-management improvements that collectively close the gap between running one agent and supervising many — including org-level default model governance, readable session names, and a hardened agents view — alongside the access-control story of the window: the US government lifted export controls on Fable 5, restoring global access on July 1; and **Grok (xAI)** published its most navigable agent dashboard release yet with v0.2.70, adding `grok wrap` for universal clipboard support, dashboard directory and branch context, collapsible `/recap` blocks, and a full wave of session-reliability fixes.

---

## At a Glance: June 29 Highlights

The releases this window converge on a shared question of agent oversight: as background and scheduled agents multiply across desktop, cloud, and mobile, every platform is racing to build the session observatory that lets users see what is running, what it did last, and how to pause or redirect it.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code** ships org-level default model governance (admins set in console, shows as "Org default" in `/model`), readable session names, clickable file attachments, a hardened agents view (single `←` to open), a streaming idle **watchdog** on by default, and a security fix preventing untrusted `.mcp.json` servers from auto-spawning; export controls on Fable 5 lifted June 30, restoring global access July 1. [1][2][3] |
| **ChatGPT** | **Pulse** is being sunset as proactive updates consolidate into a new **Scheduled Tasks** hub — a sidebar page where users can view every active recurring task, see its next run time, pause, edit, or delete it; **GPT-5.6** (Sol, Terra, Luna) previews to ~20 government-approved organisations via API and Codex only, with no ChatGPT rollout announced; **personal finance** expands to Plus users on web, iOS, and Android. [4][5][6] |
| **Google Gemini** | **Gemini Spark** launches on macOS (beta, Google AI Ultra only) on June 30 — a local file agent with a new "Spark" sidebar tab, connected-folder permission controls, Canva/Dropbox/Instacart/OpenTable/Zillow integrations, Google Tasks and Keep support, custom **MCP** connections, and real-time topic tracking; remote phone-to-desktop task dispatch confirmed "coming soon." [7][8][9] |
| **Microsoft Copilot** | **Copilot Catchup** ships as a content card surfacing document change recaps since last open; **Copilot in Word for iOS** reaches GA, bringing agentic editing and image insertion to iPhone and iPad; the **Planner Agent** delivers interactive task cards across Planner plans in Copilot; Word now preserves Copilot Chat conversation history across sessions. [10][11][12] |
| **Grok (xAI)** | Grok Build v0.2.70 (June 27) ships `grok wrap` for any-command clipboard support, Ctrl+4 prompt-queue toggle in VS Code, full **session recaps** (`/recap` and return-from-away), dashboard **directory and branch display** with Ctrl+W to dispatch agents into fresh git worktrees, and collapsible recap blocks with loading spinners; also: startup browser-login loop fixed for API-key-only sessions. [13][14] |
| **Perplexity** | **Comet** reaches all iOS users (now available on iOS, Android, Mac, and Windows); **inline editing** ships for any Computer-generated asset — draw a selection box and type a short instruction; **Deep Research** now outputs presentations, spreadsheets, dashboards, and websites directly in the same workflow; enterprise **Computer Analytics API** and custom credit limits GA. [15][16] |

---

## Product Highlights

### Claude / Anthropic: Session Legibility and the Org-Governed Agent Fleet

Anthropic's most interaction-design-significant release of this 48-hour window is not a headline feature but a cluster of session-management and governance improvements to **Claude Code** that, taken together, transform it from a tool that runs one agent at a time into a surface that can supervise an organisational fleet.



The update adds support for organisation default models — admins set it in the org console; it shows as "Org default" (or "Role default") in `/model` when a developer hasn't picked one themselves — and adds readable default names for sessions at start, making them easier to identify and message.

 The UX implication is significant: for the first time, an org administrator can define the model policy once and have every Claude Code session in the organisation reflect it automatically, without relying on individual developers to pick the right model. 

The streaming idle watchdog is now on by default for all providers, aborting and retrying when a response stream produces no events for five minutes, and Remote Control is now correctly disabled when `ANTHROPIC_BASE_URL` points at a non-Anthropic host.



The security hardening in this wave is equally notable. 

A security fix means `claude mcp list/get` no longer auto-spawns `.mcp.json` servers that a repo self-approved via committed settings; untrusted workspaces now show a `⏸ Pending approval` indicator instead.

 This shifts the trust model from *implicit auto-approval* to *explicit human gate* — a repo can no longer silently escalate its own MCP server permissions through committed configuration files. The agents view also receives a UX polish pass: 

opening the agents view from a foreground session now requires a single `←` press instead of two, matching the behavior in background sessions.

 Alongside these improvements, 

Anthropic confirmed on June 30 that the U.S. Department of Commerce lifted export controls on Claude Fable 5 and Mythos 5, with Fable 5 available again to global users on the Claude platform, Claude.AI, and Claude Code starting July 1.

 The practical UX effect is the restoration of the full model roster for organisations whose agentic workflows had been blocked for over two weeks.

---

### ChatGPT / OpenAI: Pulse Retires, the Scheduled Tasks Observatory Arrives

OpenAI's most consequential UX event of this window is the sunset of **Pulse** and its replacement with a dedicated **Scheduled Tasks** management hub — a structural shift in how ChatGPT handles its growing surface area of autonomous, recurring work.



Pulse is being sunset as proactive updates move into scheduled tasks; Pro users will continue to have access for 14 days; to keep receiving daily updates, users can ask ChatGPT to schedule a daily briefing based on their interests and past chats.

 The framing matters: Pulse was a push feature — ChatGPT decided when and what to surface. 

The new Scheduled Tasks page gives users a place to view, pause, edit, and delete active tasks in one place; monitoring tasks scan the web and connected apps, alerting users only when something changes; tasks run no more than once an hour, and users can pause, resume, edit, or delete any request without rebuilding it.

 This is a meaningful interaction-model shift: from *agent-as-broadcaster* to *agent-as-scheduled-worker with a visible task ledger*. The user now has an audit surface for every recurring commitment the agent has made — what it runs, when it next fires, and how to cancel it.

The GPT-5.6 preview landing in this window is notable not for its capability but for its access model. 

GPT-5.6 went live as a limited preview to about 20 pre-approved organisations, at the request of the U.S. government; it is not in ChatGPT; individuals cannot get it.

There was an executive order on June 2, 2026 asking federal agencies to set up a process for evaluating powerful new AI models before wide release, and GPT-5.6 is the first major model to ship under that framework.

 The UX implication for the general ChatGPT user population is zero today, but the pattern it establishes is significant: government-gated model access is now a live variable in how frontier AI products roll out to users. Also shipping this window: 

the personal finance experience in ChatGPT is rolling out to Plus users in the U.S. on web and iOS, and is now also available on Android for Pro and Plus users, with eligible users able to securely connect supported financial accounts and view a dashboard of their finances grounded in their financial context.



---

### Google Gemini: Spark Lands on macOS and the Local-Remote Agent Loop Closes

Google's most structurally novel UX release of the window is the June 30 launch of **Gemini Spark** on macOS — the first time the personal AI agent, announced at Google I/O 2026, has been available as a local desktop surface capable of working directly with a user's files without uploading them to the cloud.



Google is bringing Spark to the Gemini macOS app to help automate time-consuming tasks across the desktop; Gemini Spark can now move beyond the chat window and tackle heavy lifting across desktop files and apps — for example, turning hours of manual file sorting into an instant action; it also connects the desktop and Google Workspace; to keep information secure, Gemini Spark only has access to the files users give it permission to use.

 The new "Spark" tab in the macOS sidebar, and the explicit connected-folder permission UI, establish a *consent-layered file access* model — users explicitly grant access to folders, and can unlink them at any time. 

Google's official product description states Spark "is designed to check with you before taking major actions" — but Gemini Spark's own onboarding text has previously warned it "may do things like share your info or make purchases without asking," a disclosure that was already the central open question about Spark before today's desktop expansion; extending the agent's reach into local Mac file systems expands the surface area of that unresolved trust question rather than resolving it.



The third-party app expansion is the release's other design-consequential moment. 

Spark now works with Google Tasks and Google Keep; new integrations launch with Canva, Dropbox, Instacart, OpenTable, and Zillow Rentals; these are rolling out over the next week on Gemini Spark on web and mobile and will roll out to the macOS app in the coming weeks; Google is also rolling out support for custom Model Context Protocol (MCP), giving users the ability to connect their favorite apps directly into Spark.

 This shifts Spark from a Google-ecosystem agent to an MCP-open one — a material expansion of the delegation surface. The remote dispatch capability is confirmed but not yet shipping: 

coming soon, users will be able to run tasks remotely — assigning a multi-step task to Gemini Spark from their phone, like finding a specific sales report on a Mac, pulling the total revenue number, and emailing it; Gemini Spark for macOS is available in Beta to Google AI Ultra subscribers aged 18 and over, starting in the US.



---

### Microsoft Copilot: Document Continuity, Mobile Agentic Editing, and the Planner Agent

Microsoft's most interaction-design-significant releases of this window are a cluster of in-document agent improvements that collectively solve the *session continuity problem* — the fact that agentic editing work across a long document review was previously reset each time a user reopened a file or switched contexts.



**Copilot Catchup** is now available as a content card that surfaces a quick recap of what's changed in a document since a user last opened it; instead of rereading a document to find updates, users get a quick recap up front; it is a fast way to get back up to speed on shared and evolving files.

 This establishes a new *ambient awareness* pattern: the agent anticipates re-entry friction and resolves it proactively at the moment of document open, before the user has composed a single prompt. 

Word now preserves Copilot Chat conversation history from chat to the apps, so users can pick up where they left off without losing the thread of their Copilot session, keeping complex, multi-step document work continuous.

 Together, Catchup and session persistence close the cognitive gap that had made agentic document work feel episodic rather than cumulative.

The mobile surface also advances materially this window. 

Copilot in Word agentic capabilities are now available for iOS, so users can edit and add content to documents from their iPhone or iPad; users can make quick updates, draft new content, and refine existing text directly on their mobile device, while also performing more advanced actions like image insertion and tracked changes in the full Word experience.

 This establishes parity between desktop and mobile for Word's core agentic editing loop — an important expansion of where consequential agent actions can be approved and applied. 

The **Planner Agent** delivers interactive task cards and actionable insights in Microsoft 365 Copilot, so users can easily prioritize tasks across Planner plans and focus on what matters; via natural language prompts, users can also create and update tasks or ask the agent to create structured plans with goals and buckets.

 This shifts task management from a separate application navigation step to an inline natural-language interaction directly within Copilot, collapsing the context switch that had made task capture a friction point in mid-document or mid-meeting work.

---

### Grok (xAI): Dashboard Context, `grok wrap`, and the Recap as First-Class UX Primitive

xAI's most interaction-design-significant releases of the window are in Grok Build v0.2.70 (June 27), which addresses two distinct usability gaps: the agent session not showing *where* it is, and the developer not knowing *what happened* when they come back to a long-running session.



v0.2.70 adds `grok wrap` to run any command with local clipboard support, makes Ctrl+4 toggle the prompt queue on local macOS VS Code terminals, and makes session recaps (`/recap` and return-from-away) now show the full summary instead of being cut off mid-sentence.

 The `grok wrap` addition is a small but structurally meaningful UX primitive — it means any terminal command can now feed output directly into the Grok clipboard context without requiring a separate copy step, reducing the friction of incorporating external tool output into an agent turn. 

The dashboard was also updated so `grok -w --ref` now creates worktrees based on the specified ref instead of HEAD; Esc in the dashboard input now moves focus to the list without clearing a typed draft; copying a tool header now copies just the path or command without the Read/Run label; headless and stdio sessions no longer start unnecessary filesystem watchers, saving CPU and IO.



The collapsible `/recap` block, shipping in the same release window, is the most consequential UX primitive introduced: 

`/recap` now appears as a collapsible tool-style block with a loading spinner while generating; dashboard arrow keys open agent details and exit overlays; closing an agent now selects the neighboring row; the dashboard now displays the current directory and branch with a click or Ctrl+L to change location, or Ctrl+W to dispatch new agents into fresh git worktrees.

 This shifts the agent session from a *linear transcript* into a *structured log with navigable context* — the developer can jump to the recap, see the current working directory, and dispatch a parallel worktree agent, all without leaving the dashboard. The pattern connects to a cross-platform trend: every major agent surface is converging on a *session observatory* — a single panel where the state, location, and recent actions of running agents are legible at a glance.

---

### Perplexity: Comet Reaches All Platforms and Inline Editing Ships

Perplexity's most consequential UX releases of the window are the completion of **Comet's** cross-platform rollout and the arrival of **inline editing** for Computer-generated assets — a feature that closes a significant friction loop in the agent-to-artifact workflow.



This week, Perplexity launched Comet to all iOS users; with this release, Comet is now available on all major platforms: iOS, Android, Mac, and Windows; users can now ask Comet for research or work help from anywhere in the world; for the best experience, users can pair their mobile and desktop browsers with Comet device sync to teleport to Comet iOS seamlessly.

 The completion of cross-platform availability is a distribution milestone with direct UX implications: the trust and permission design of Comet's agentic browsing capabilities — MDM deployment, admin-controlled action scope, enterprise data retention — now reaches users on every major surface. 

Inline editing for any Computer-generated asset lets users draw a selection box over any part of a document, presentation, spreadsheet, web app, or PDF that Computer created, type a short instruction, and have Computer edit just that region in place.

 This shifts the post-generation workflow from *regenerate the whole artifact* to *surgically correct a region* — a material improvement in the precision of the human-agent collaboration loop for document-class outputs.



Perplexity Deep Research and Pro Search now support creating presentations, spreadsheets, dashboards, websites, and other structured outputs directly within the product, bringing research and creation into a single workflow; with multi-step reasoning across hundreds of sources, Perplexity already helps users synthesize complex topics in depth; now, that same research can be turned into usable deliverables users can immediately put to work; this is the next milestone for deep research agents: not just generating insight, but turning that insight into something tangible and actionable in the same flow.

 On the enterprise control surface, 

Perplexity also adds a Computer Analytics API and custom credit limits, making it easier to research, build artifacts, and manage usage.

 The combination of cross-platform availability, inline editing precision, research-to-artifact pipelines, and enterprise analytics makes this the most complete Perplexity Computer release since the product launched.

---

## The Bigger Picture: Desktop Agents, Scheduled Tasks, and the Session Observatory

The 48 hours ending June 29, 2026 describe a single, coherent maturation moment: the agent paradigm has decisively moved from the cloud browser tab onto the local desktop, the phone screen, and the recurring task schedule — and the industry is now racing to build the *session observatory* infrastructure that makes this expanded surface governable. Google's Gemini Spark macOS launch answers the question of what a personal AI agent looks like when it lives on your machine rather than in a cloud iframe — it looks like a sidebar tab with explicit folder permissions, MCP-open connectivity, real-time topic tracking, and a future phone-triggered remote dispatch. OpenAI's Pulse retirement and Scheduled Tasks hub answer the question of what proactive agency looks like when it's user-legible rather than opaque — it looks like a sidebar ledger where every recurring commitment the agent has made is visible, pauseable, and editable without rebuilding it from scratch. Claude Code's org-default-model governance and hardened agents view answer the question of what fleet-scale agent management looks like when individual developers should not all be configuring their own stacks — it looks like an IdP-governed model policy that propagates automatically to every session, with a session dashboard that lets a developer supervise a roster of parallel agents from a single keyboard shortcut. And Grok Build's dashboard context display, `grok wrap`, and collapsible `/recap` blocks answer the question of what re-entry into a long-running agent session looks like when the developer was away — it looks like a structured summary block, a visible working-directory breadcrumb, and a one-command clipboard bridge. The common architectural conviction across all four stories is identical: the highest-value interaction design work in agentic AI right now is not building the agent, but building the *cockpit from which a human can see, steer, and stop it* at any point in its running life.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] Gradually AI. (2026). *Claude Code Changelog (June 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[3] CNBC. (2026). *Anthropic says Trump admin has lifted export controls on Claude Fable 5 and Mythos 5*. [https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)

[4] OpenAI. (2026). *ChatGPT Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] Releasebot. (2026). *ChatGPT Updates by OpenAI — June 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[6] FindSkill.ai. (2026). *GPT-5.6 Is Here: Sol, Terra & Luna (and When You Can Use It)*. [https://findskill.ai/blog/gpt-5-6-release-date-what-to-expect/](https://findskill.ai/blog/gpt-5-6-release-date-what-to-expect/)

[7] Google. (2026). *Gemini Spark updates: macOS launch, connected apps and more*. [https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/)

[8] 9to5Google. (2026). *Gemini Spark rolling out to macOS app for local tasks, automation*. [https://9to5google.com/2026/06/30/gemini-spark-mac-app/](https://9to5google.com/2026/06/30/gemini-spark-mac-app/)

[9] TechGenyz. (2026). *Gemini Spark Can Now Control Your Mac From Your Phone — Here's Everything in Today's Update*. [https://techgenyz.com/gemini-spark-macos-launch-trust-risks/](https://techgenyz.com/gemini-spark-macos-launch-trust-risks/)

[10] Microsoft Community Hub. (2026). *What's New in Microsoft 365 Copilot — June 2026*. [https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what's-new-in-microsoft-365-copilot--june-2026/4529572](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what's-new-in-microsoft-365-copilot--june-2026/4529572)

[11] Neowin. (2026). *Here are all the new features added to Microsoft 365 Copilot in June 2026*. [https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/](https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/)

[12] A Guide to Cloud & AI. (2026). *What's New in Microsoft 365 Copilot: June 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-june-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-june-2026-updates/)

[13] xAI. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[14] Releasebot. (2026). *Grok Build Updates by xAI — June 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[15] Releasebot. (2026). *Perplexity Release Notes — June 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[16] Perplexity. (2026). *Perplexity Changelog: Deep Research, command panel, forking, inline actions and enterprise controls — June 19, 2026*. [https://www.perplexity.ai/changelog/deep-research-command-panel-forking-inline-actions-and-enterprise-controls](https://www.perplexity.ai/changelog/deep-research-command-panel-forking-inline-actions-and-enterprise-controls)

---