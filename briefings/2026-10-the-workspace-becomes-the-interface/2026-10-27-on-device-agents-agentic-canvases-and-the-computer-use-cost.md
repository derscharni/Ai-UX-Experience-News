# UX Briefing: On-Device Agents, Agentic Canvases, and the Computer-Use Cost Curve

**October 27, 2026**

Good morning. The 48 hours ending October 27, 2026 are defined by four simultaneous convergences that together mark a new phase of the Agent2Agent2Human design space: platforms are making their agentic workspaces deeper and more persistent, on-device execution is arriving as a first-class trust-design primitive, and a new class of fast, cheap computer-use models is collapsing the cost barrier to continuous background automation. **Claude/Anthropic** ships **Claude Code 2.1.310**, the most significant enterprise admin governance update of the autumn — introducing role-gated permissions for cloud sessions and Remote Control, a file-picker for environment setup scripts, and improved error surfacing in the cloud environment dialog — converting what was an opaque admin toggle into a genuinely governed enterprise capability. **ChatGPT/OpenAI** fires the most consequential agentic compute release of the window with **GPT-6.1 Terra**, a new model purpose-built for visual reasoning and precise computer use, landing simultaneously in ChatGPT Work, Codex, and the Agents API alongside a same-day Agents API expansion that embeds the Artifact SDK and Office-document skills directly into OpenAI-hosted sandboxes. **Google Gemini** completes its most architecturally significant mobile redesign of 2026: the **Gemini for Android side panel and settings consolidation**, arriving through a server-side update on October 24, which collapses a fragmented two-location settings model into a single unified page and surfaces the Spark-to-Task background-agent rename as a prominent Chat/Task toggle — completing parity with the iOS, macOS, and web redesigns that shipped the previous week. **Microsoft Copilot** crosses the threshold from reference-gathering tool to agentic workspace with **Copilot Notebooks' October agentic canvas update**, which adds Frontier-gated Office-on-canvas editing, task delegation from notebook chat, interactive reports, and the upcoming scheduled automations that will let recurring project deliverables run without a human prompt. **Grok (xAI)** establishes the **Grok Voice 3.0** voice interaction frontier for enterprise agent pipelines, delivering a sub-second speech-to-speech model that auto-upgraded every `grok-voice-latest` session without a code change or advance notice — surfacing a significant transparency-design question about silent production model swaps. **Perplexity** ships the most structurally significant trust-and-privacy advance of the window with **fully local Computer execution on Apple silicon**, a local-first architecture that inverts the Hybrid Compute model: the agent and model now start on-device by default, with cloud escalation only upon explicit user approval.

---

## At a Glance: October 27 Highlights

Today's releases converge on a single structural inflection: the platforms that define the next phase of Agent2Agent2Human UX are no longer competing on capability alone — they are competing on where computation runs, who can govern it, and how much trust the user can extend to an agent that may be acting on sensitive files, desktop sessions, or live voice calls without constant supervision.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code 2.1.310 adds role-gated Enterprise permissions for cloud sessions and Remote Control, a file-picker for environment setup scripts, and improved error surfacing in the cloud environment admin dialog** — Owners can now control which custom Enterprise roles have access to cloud sessions and Remote Control independently; the setup-script file picker eliminates manual script entry; failed saves and archives now surface errors inside the dialog rather than silently failing. [1][2][3] |
| **ChatGPT** | **GPT-6.1 Terra launches October 26 for visual reasoning and precise computer use in ChatGPT Work and Codex; Agents API sandboxes gain the Artifact SDK and Office-document skills; Ultrafast mode added to the Agents API** — Terra completes tasks 3× faster than GPT-6 Astra and GPT-6.1 Sol at roughly one-third the cost; Artifact SDK in hosted sandboxes means agents can create and edit spreadsheets, presentations, and Word docs without leaving the sandbox; Ultrafast mode reduces inter-token latency for supported models. [4][5][6][7] |
| **Google Gemini** | **Gemini for Android side panel and settings redesign completes cross-platform rollout on October 24; Spark renamed Task with a Chat/Task toggle above the prompt box; unified Settings page consolidates all preferences** — the redesign that shipped to iOS, macOS, and web with Gemini 4 Argon last week is now server-side updating Android devices without a Play Store download; Task settings replaces the old Spark settings page; chat and task history is now unified with status filters. [8][9][10][11] |
| **Microsoft Copilot** | **Copilot Notebooks October agentic canvas update adds Office-on-canvas editing, task delegation from chat, interactive reports, and PDF creation (Frontier); scheduled recurring automations coming in weeks; model selection per conversation added** — Word, Excel, and PowerPoint files can be opened inline and edited directly on the notebook canvas, with Copilot prompted to add content or restyle; recurring automations will enable daily briefs and weekly decks to run without human re-prompting; users can now scope context to Notebook-only or Work-and-web. [12][13][14] |
| **Grok (xAI)** | **Grok Voice 3.0 ships October 14 as the new default in the Voice Agent API, auto-upgrading all sessions using the `grok-voice-latest` alias without advance notice; Grok Build 1.0.65 improves session-search typo tolerance and worktree file tracking** — Voice 3.0 scores 86.9 on Artificial Analysis's Speech-to-Speech Index, delivers sub-second latency, and is already powering Tesla and Starlink customer support at scale; the silent auto-upgrade is the window's most consequential transparency-design concern for production voice agent operators. [15][16][17] |
| **Perplexity** | **Fully local Computer execution launches October 20 on Apple silicon Macs, running model, agent harness, planning, reasoning, and file operations entirely on-device for Pro/Max/Enterprise subscribers; local tasks do not consume Computer credits** — the architecture inverts Hybrid Compute: work starts locally by default and only escalates to frontier cloud models with explicit user authorization; Qwen 3.6 and PPLX Pro (Perplexity's fine-tuned Qwen 3.6) are the two local model options; 36GB of unified memory recommended. [18][19][20] |

---

## Product Highlights

### Claude / Anthropic: Cloud Session Governance Matures with Role-Gated Enterprise Controls

Anthropic's most consequential interaction-design advance in this window is not a new consumer surface but a precision tightening of the enterprise governance layer that makes cloud-session agentic workflows viable in security-sensitive organisations: **Claude Code 2.1.310**, which shipped October 25 and is the most administratively significant Claude Code release since the introduction of cloud sessions.



Claude Code 2.1.310 adds monitoring support across more platforms and expands cloud session permissions for enterprise roles, while also improving reliability, memory use, sandbox guidance, and VS Code workflows and fixing numerous issues across sessions, tools, and admin pages.

 The two admin-governance changes that warrant the most practitioner attention are the role-gated permission model and the setup-script file picker. 

Cloud sessions and Remote Control permissions have been added to Enterprise custom roles, so Owners can control access to each by role.

 This is the correct trust-design architecture for enterprise agentic deployments: previously, cloud sessions and Remote Control were binary toggles that applied uniformly to a workspace; role-gated access means a security-sensitive organisation can now permit, say, senior engineers to start cloud sessions while restricting that capability from contractor or read-only roles — the same permission granularity that mature enterprise software has long applied to production access.

The companion UX improvement is the **setup script file picker**, which 

adds a Choose File button to load a cloud environment's setup script from a file

, eliminating the previous pattern of manually pasting multi-line scripts into a dialog. 

The admin settings change for turning on Cloud sessions or Remote Control now asks for confirmation and lists the custom roles that have that permission

 — a confirmation-and-disclosure pattern that makes the governance consequence of enabling these capabilities visible at the moment of the decision, rather than buried in documentation. Taken together, the 2.1.310 admin cluster converts the cloud sessions feature from a power-user toggle into a properly governed enterprise capability with role-based access, visible permission disclosure, and reliable error surfacing — the necessary infrastructure for deploying multi-agent cloud coding workflows across large engineering organisations.

---

### ChatGPT / OpenAI: GPT-6.1 Terra Redefines the Computer-Use Cost Curve, Agents API Gains an Artifact Layer

OpenAI's October 26 releases constitute the most consequential single-day advancement in the computer-use interaction design space in the current window: **GPT-6.1 Terra** establishes a new cost-performance frontier for agentic computer use, while the simultaneous Agents API expansion embeds Office-document creation directly inside hosted sandboxes — converting OpenAI's agentic runtime from a task-execution surface into a document-production surface.



OpenAI has launched GPT-6.1 Terra, a new model focused on computer use, visual reasoning, coding, and everyday work. Terra is designed as a faster and cheaper option for tasks such as filling out forms, editing videos, interpreting technical drawings, and automating repetitive desktop work.

 The cost-performance advance is the interaction-design fact that matters most: 

on Agents' Last Exam, OpenAI reports that Terra at medium reasoning scores 15 percentage points above GPT-5.6 Terra at about one-third the cost, while matching GPT-6 Astra at one-tenth the price per token.

GPT-6.1 Terra is available now to Plus, Pro, Enterprise, and Edu users in ChatGPT Work and Codex, as well as through the API as gpt-6.1-terra.

 The UX implication of this cost shift is not incremental — when the economics of computer-use tasks drop to one-third of their previous level, workflows that were previously too expensive to automate continuously become viable as background agents running at ambient frequency, fundamentally changing the interaction model from "invoke for a specific task" to "run persistently as infrastructure."

The equally significant October 26 Agents API expansion ships two primitives that together create a new interaction contract for document-centric agentic workflows. 

OpenAI-hosted sandboxes in the Agents API now include the Artifact SDK and skills for creating and editing spreadsheets, presentations, and Word documents.

Ultrafast mode was also added to the Agents API, and an earlier September update added computer use to the Agents API.

 The Artifact SDK addition is the interaction-design primitive that closes the last major gap in OpenAI's hosted agentic sandbox: previously, an agent running in a hosted sandbox could browse, code, and execute — but any document output required exporting to an external tool. With Office-document creation native to the sandbox, agents can now complete the full research-to-deliverable arc — gather information, reason, write, and produce a formatted document — without leaving the execution environment. 

Terra can vary its reasoning effort before answering, and on Agents' Last Exam, OpenAI reports a 15-percentage-point improvement over GPT-5.6 Terra at medium reasoning effort, at about one-third the measured task cost.

 This variable-reasoning-effort architecture is the correct design for long-running agentic tasks: agents can apply minimal reasoning for routine computer-use steps and escalate to higher reasoning effort for the document-production and decision-making phases within the same pipeline.

---

### Google Gemini: The Spark-to-Task Rename Completes, and the Android Settings Consolidation Closes the Platform Gap

Google's most structurally significant interaction-design advance reaching broad user impact in this window is the completion of a cross-platform UX parity project: the **Gemini for Android side panel and settings redesign**, which arrived through a server-side update on October 24 and requires no app download — completing the same redesign that already reached iOS, macOS, and web the previous week.



The Gemini app on Android now has a tidier side panel and a single Settings page. As 9to5Google reports, the redesign that reached iOS, macOS and the web last week alongside Gemini 4 Argon is now widely available on Android.

 The two structural changes that matter most for agentic UX practitioners are the settings consolidation and the Spark-to-Task surface redesign. 

The Gemini app is revamping settings: instead of having preferences split between the account menu and "Gemini Settings," Google has consolidated everything into one page; the account menu is now just for switching accounts, leaving Feedback, or getting Help.

 The interaction-design implication of settings fragmentation was a discovery problem: a user who wanted to configure Task settings, Skills, and Personal Intelligence had to navigate between two different menus that had no visible relationship to each other. The consolidated single-page settings surface resolves this by making every configuration option — 

Notifications, Personal Intelligence, Avatar, Task settings, Theme, Skills, Voice, Media, Device controls, Cart and orders, and Gemini Notebook

 — visible in a single scrollable hierarchy.

The **Spark-to-Task rename** that this settings redesign completes is the more consequential long-term interaction-architecture shift. 

Google is moving Spark, its background agent, into the main chat as "Task," right alongside Scheduled Actions; in a redesign that's rolling out now, Spark shows up as "Task" in a new Chat and Task switch next to the prompt box, and its settings page is now called Task settings.

The new "Scheduled" page sorts tasks by status — Active, Paused, Completed, or Suggested — making it easier to keep track of what's going on; navigation is simpler now: the old Spark menu is gone, and settings have been renamed to match the new Task feature; chats and tasks are combined in one history view instead of split lists, and there's a filter icon to quickly find what's ready or in progress.

 This is the correct temporal-UX architecture for a background agent surface: by surfacing active, paused, and completed tasks alongside conversation history in a unified, filter-able view, Gemini gives users a single status-management surface for both synchronous conversation and asynchronous background work — eliminating the cognitive overhead of checking two separate histories to understand what the agent is doing.

---

### Microsoft Copilot: Notebooks Becomes an Agentic Canvas with Office-on-Canvas Editing and Scheduled Automations

Microsoft's most consequential Copilot interaction-design advance crystallising in this window is the transformation of Copilot Notebooks from a reference-aggregation and Q&A surface into a genuinely agentic workspace: the **Copilot Notebooks October agentic canvas update**, which adds Frontier-gated Office editing on the canvas, task delegation from chat, interactive reports, and the upcoming scheduled automation capability that will make recurring deliverables run without a human initiating each cycle.



The October 2026 update brings task delegation, recurring automations, direct Office editing, interactive reports, and new ways to turn project information into polished deliverables.

 The Office-on-canvas primitive is the interaction shift that has the broadest long-term implications: 

Notebooks doesn't just start and end with adding references and working with Copilot — now, with the full power of Office, users can create, edit, and collaborate on documents, spreadsheets, and presentations without breaking their flow.

Word, Excel and PowerPoint files can be viewed inline and edited directly on the notebook canvas; users can also ask Copilot to add content, such as an intro paragraph, bullet points or a chart, or to change fonts, colors and layouts; collaborators can be invited to work on the same file with Copilot.

 This establishes Copilot Notebooks as the correct agentic canvas design for knowledge-work workflows: rather than requiring a user to gather information in one tool, generate a draft in a second, and edit a deliverable in a third, the notebook canvas makes information, AI generation, and document editing co-present in a single surface.

The scheduled automations capability that is arriving in the next few weeks is the temporal-UX advance that most directly changes how practitioners will interact with Notebooks day-to-day. 

One of the more interesting additions is scheduled automation: users will be able to schedule recurring tasks, such as daily morning briefs and weekly status presentations, instead of repeatedly prompting Copilot.

Microsoft is also adding model choice, allowing users to select a model for notebook conversations or request deeper reasoning; both task delegation and model selection are currently available through the Frontier program, while scheduled automations are coming in the next few weeks.

 The context-scoping control — 

Copilot does simple work for you, and users can now scope their prompt to just their Notebook only or change to "Work and web" for broader context beyond their references

 — is the trust-design primitive that makes notebook-based agentic work safe for compliance-sensitive use: an agent operating only on the references inside a specific notebook cannot inadvertently pull in data from a user's wider organisational graph that the notebook's intended audience was not meant to see.

---

### Grok (xAI): Grok Voice 3.0's Silent Auto-Upgrade Defines the Window's Sharpest Trust-Design Question

xAI's most interaction-design-significant development in this window is **Grok Voice 3.0**, which shipped October 14 as the new default model in the Voice Agent API — and which surfaced the industry's most consequential trust-and-transparency design question of the autumn: whether a production voice agent's underlying model should be upgradeable automatically, without advance notice, by pointing an alias to a new model ID.



xAI announced Grok Voice 3.0 on October 14, 2026, making the speech-to-speech model available in its Voice Agent API at $0.08 per minute.

Grok Voice 3.0 is a frontier speech-to-speech model, meaning audio goes in and audio comes out without an intermediate text-generation hop.

It scores 86.9 on Artificial Analysis's Speech-to-Speech Index, first ahead of GPT-Live-1 (83.2) and Gemini 3.8 Live (82.6).

 The enterprise deployment story is significant: 

xAI launched Grok Voice 3.0 and immediately plugged it into two of Elon Musk's largest consumer-facing operations — Starlink customer support and in-car voice inside Tesla vehicles.

It achieves sub-second latency and 70% call resolution without human intervention.



The UX-governance concern that warrants the most practitioner attention is the upgrade mechanism. 

The upgrade did not wait for anyone to opt in: xAI pointed the `grok-voice-latest` alias at Grok Voice 3.0 on October 14; any session built on that alias switched versions with no code change on the developer's end; most teams got no deploy to review and no warning email beforehand.

On October 14, `grok-voice-latest` began pointing to `grok-voice-3.0`, and any session that used the alias was upgraded without code changes — that is convenient for a prototype and risky for production, because the agent's behavior changed overnight without a deploy, a code review, or a regression run.

 The trust-design failure this represents is structural: an enterprise voice agent deployed for customer support in a regulated industry has compliance obligations around the model it uses, the voice persona it presents, and the conversational patterns it follows. A silent production model swap — even to a better model — violates the audit-trail contract that those deployments depend on. The correct design is what OpenAI uses for its model aliases: advance notice, a pinned version path that is never auto-upgraded, and a migration window before the alias moves. 

On tau-Voice, a benchmark built from simulated customer-support calls, xAI reported 71.6% for Grok Voice 3.0 and described the result as comparable to GPT-Live-1 at 40% lower latency

 — making the capability advance genuine, but the upgrade pattern one that production operators should be actively auditing right now.

---

### Perplexity: Fully Local Computer Inverts the Cloud-Default Trust Model for On-Device Agentic Work

Perplexity's most structurally significant trust-and-privacy design advance in this window is not an API update or a new research surface but an architectural inversion: **fully local Computer execution on Apple silicon**, announced October 20, which makes the on-device agent the default for sensitive workflows and relegates cloud processing to an explicit opt-in — reversing the trust assumption that has characterised every previous AI agent deployment model.



Some AI agents that handle email, notes, and private documents route that data through a remote server. Perplexity Computer now offers a different path, with the model, agent coordination, planning, reasoning, and task execution running directly on the Mac.

For more complex work, a Hybrid mode can split the task between cloud models and the local model on your Mac, keeping sensitive data private; MacStories notes this flips last month's Hybrid Computer, which started in the cloud — now you start local and only reach cloud frontier models when needed, with the user's approval.

 This architecture inversion is the correct trust-design model for agentic workflows that touch sensitive personal or organisational data: the default state is "nothing leaves this device," and cloud escalation is a deliberate, user-initiated action with a visible approval step — not a silent background behaviour that the user must proactively block.



The new local mode is available to Perplexity Pro, Max, and Enterprise subscribers; it launches with Qwen 3.6 and PPLX Pro as local model options, which users can download and set up through the app.

Local tasks use PPLX Pro, Perplexity's post-trained version of Qwen 3.8, and they don't consume Computer credits.

 The no-credit-consumption for local tasks is the economic incentive that will drive adoption among power users — it converts the local Computer mode from a privacy preference into a cost-optimisation strategy, meaning users who want to run frequent, repetitive local-file workflows have a direct financial reason to prefer the on-device path. 

Users can still authorize Computer to call on one of more than 15 frontier models for assistance, and any code execution or tool use runs in an isolated sandbox environment.

 The hardware constraint is real: 

Perplexity recommends 36GB of unified memory

, which limits the addressable device pool to higher-end Apple silicon configurations — but as Apple's M-series memory headroom expands, this ceiling will rapidly become less restrictive.

---

## The Bigger Picture: On-Device Agents, Agentic Canvases, and the Computer-Use Cost Curve

The 48 hours ending October 27, 2026 reveal an industry moving simultaneously in two complementary directions: toward agentic compute that is faster, cheaper, and more capable (Terra, Grok Voice 3.0), and toward agentic execution that is more local, more governed, and more auditable (Perplexity Computer local mode, Claude Code 2.1.310's role-gated admin controls, Copilot Notebooks' context-scoping). These are not opposing forces — they are the two sides of the same trust contract. When computer-use costs fall by two-thirds in a single model generation, as Terra's economics suggest, the class of workflows that become viable as always-on background agents expands dramatically; that expansion makes the governance and provenance questions — where does this agent run, who authorised it, what data did it touch — more urgent, not less. Anthropic's response is to add role-gated permission architecture to cloud sessions before the adoption curve steepens. Perplexity's response is to make on-device execution the default and require affirmative user action to escalate to the cloud. Google's Spark-to-Task rename and unified history surface is a design response to the same problem: when background tasks and foreground conversations live in separate navigation hierarchies, users lose track of what the agent is doing, and trust erodes. Microsoft's Copilot Notebooks agentic canvas — Office editing, task delegation, scheduled automations — is the enterprise answer to the same inflection: an agent that can draft, edit, and schedule recurring deliverables from within a governed, scoped notebook context is an agent that a compliance team can reason about, because its inputs, outputs, and scheduling parameters are all visible in one place. Grok Voice 3.0's silent auto-upgrade is the counterexample that makes the pattern vivid: a model that performs better is not automatically a model that can be trusted in production, because trust in production depends not only on capability but on auditability, predictability, and the operator's ability to consent to the upgrade before it happens. The frontier of Agent2Agent2Human UX has crossed into a phase where the platforms that earn the deepest enterprise adoption will be the ones that make their agents not just more capable, but more legible — to the users who work with them, to the admins who govern them, and to the compliance teams who have to sign off on deploying them at scale.

---

## References

[1] releasebot.io. (2026). *Claude Code Updates by Anthropic — October 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[2] gradually.ai. (2026). *Claude Code Changelog (October 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[3] code.claude.com. (2026). *Configure cloud environments — Claude Code Docs*. [https://code.claude.com/docs/en/cloud-environments](https://code.claude.com/docs/en/cloud-environments)

[4] developers.openai.com. (2026). *API Changelog — October 2026*. [https://developers.openai.com/api/docs/changelog](https://developers.openai.com/api/docs/changelog)

[5] bleepingcomputer.com. (2026). *OpenAI launches GPT-6.1 Terra with 3x faster AI agents, 50% lower pricing*. [https://www.bleepingcomputer.com/news/artificial-intelligence/openai-launches-gpt-61-terra-with-3x-faster-ai-agents-50-percent-lower-pricing/](https://www.bleepingcomputer.com/news/artificial-intelligence/openai-launches-gpt-61-terra-with-3x-faster-ai-agents-50-percent-lower-pricing/)

[6] testingcatalog.com. (2026). *OpenAI launches GPT-6.1 Terra for precise computer use*. [https://www.testingcatalog.com/openai-launches-gpt-6-1-terra-for-precise-computer-use/](https://www.testingcatalog.com/openai-launches-gpt-6-1-terra-for-precise-computer-use/)

[7] simonwillison.net. (2026). *GPT-6.1 Terra*. [https://simonwillison.net/2026/Oct/26/gpt-61-terra/](https://simonwillison.net/2026/Oct/26/gpt-61-terra/)

[8] 9to5google.com. (2026). *Gemini for Android rolls out side panel and settings redesign*. [https://9to5google.com/2026/10/23/gemini-settings-redesign-android/](https://9to5google.com/2026/10/23/gemini-settings-redesign-android/)

[9] androidpolice.com. (2026). *Google is renaming Gemini again; here's what each feature does now*. [https://www.androidpolice.com/googles-renamed-gemini-features-field-guide/](https://www.androidpolice.com/googles-renamed-gemini-features-field-guide/)

[10] layer3labs.io. (2026). *Gemini Spark Disappeared Because Google Renamed It Task Mode*. [https://www.layer3labs.io/guides/what-happened-to-gemini-spark](https://www.layer3labs.io/guides/what-happened-to-gemini-spark)

[11] chromegeek.com. (2026). *Gemini for Android Gets a New Side Panel and Settings*. [https://www.chromegeek.com/gemini-android-side-panel-settings-redesign/](https://www.chromegeek.com/gemini-android-side-panel-settings-redesign/)

[12] techcommunity.microsoft.com. (2026). *What's New in Notebooks | October 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105)

[13] windowsreport.com. (2026). *Copilot Notebooks October 2026 Update Adds Office Editing, AI Automations & Interactive Reports*. [https://windowsreport.com/copilot-notebooks-october-2026-update-adds-office-editing-ai-automations-interactive-reports/](https://windowsreport.com/copilot-notebooks-october-2026-update-adds-office-editing-ai-automations-interactive-reports/)

[14] aguidetocloud.com. (2026). *What's New in Microsoft 365 Copilot: October 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-october-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-october-2026-updates/)

[15] unite.ai. (2026). *xAI Introduces Grok Voice 3.0 Speech-to-Speech Model for Voice Agents*. [https://www.unite.ai/xai-introduces-grok-voice-3-0-speech-to-speech-model-for-voice-agents/](https://www.unite.ai/xai-introduces-grok-voice-3-0-speech-to-speech-model-for-voice-agents/)

[16] cellcog.ai. (2026). *Grok Voice 3.0: #1 Speech Index, Same $0.08/min Price*. [https://cellcog.ai/blog/grok-voice-3/](https://cellcog.ai/blog/grok-voice-3/)

[17] miraflow.ai. (2026). *Grok Voice 3.0 Explained: Benchmarks, Pricing and Speech-to-Speech (2026)*. [https://miraflow.ai/blog/grok-voice-3-0-explained-benchmarks-pricing-speech-to-speech-2026](https://miraflow.ai/blog/grok-voice-3-0-explained-benchmarks-pricing-speech-to-speech-2026)

[18] 9to5mac.com. (2026). *Perplexity's Computer can now run entirely on your Mac, even offline*. [https://9to5mac.com/2026/10/20/perplexitys-computer-can-now-run-entirely-on-your-mac-even-offline/](https://9to5mac.com/2026/10/20/perplexitys-computer-can-now-run-entirely-on-your-mac-even-offline/)

[19] macdailynews.com. (2026). *Perplexity Computer now runs fully locally, securely, and privately on Mac*. [https://macdailynews.com/2026/10/21/perplexity-computer-now-runs-fully-locally-securely-and-privately-on-mac/](https://macdailynews.com/2026/10/21/perplexity-computer-now-runs-fully-locally-securely-and-privately-on-mac/)

[20] techbriefly.com. (2026). *Perplexity brings fully local AI agents to Mac*. [https://techbriefly.com/2026/10/21/perplexity-brings-fully-local-ai-agents-to-mac/](https://techbriefly.com/2026/10/21/perplexity-brings-fully-local-ai-agents-to-mac/)