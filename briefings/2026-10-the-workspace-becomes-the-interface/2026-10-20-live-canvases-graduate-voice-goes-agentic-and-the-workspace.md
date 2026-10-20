# UX Briefing: Live Canvases Graduate, Voice Goes Agentic, and the Workspace Persona Wars

**October 20, 2026**

Good morning. The 48 hours ending October 20, 2026 consolidate a month of individual agentic-surface launches into a single, legible structural story: generative canvases are graduating from beta into infrastructure, voice is crossing from conversational novelty into tool-connected agentic backbone, and the race to own the daily workspace is producing the most consequential UX architecture decision of the autumn — how to present a delegated agent's ongoing work to a user who has stopped watching. **Claude/Anthropic** closes the window with **Claude Code v2.1.303 and v2.1.304 shipping October 18–19**, cementing a steady reliability-hardening cadence on top of last week's fork-subagent default and first-token latency cut — while the generative workspace layer matures further as **Claude Dashboards and Claude Motion (launched October 8) continue their beta rollout**, with Docs, Slides, and Design now available on every plan including Free, and Motion's code-backed animation architecture establishing a transparency primitive absent from every competing animation tool. **xAI** delivers the window's most consequential voice-interaction design event: **Grok Voice 3.0, shipped October 14**, which brings full-duplex speech-to-speech with tool calling, 28 built-in voices, server-side interruption handling, and automatic custom voice cloning to the Voice Agent API — a model that already powers voice experiences in Tesla and SpaceX at production scale and that the `grok-voice-latest` alias silently upgraded to, with no code change required from any developer using the alias. **Microsoft Copilot** continues its structural October renovation as the **Home/Code/Autopilot redesign rolls into Frontier**, with **interactive PowerPoint slides** due mid-to-late October and the new **Today** ambient feed entering private preview — a command-centre view that proactively drafts replies, proposes schedule changes, and surfaces forgotten follow-ups across email, calendar, and Teams without any user prompt. **Google Gemini** remains in its most consequential planning gap of the year: **Workspace Skills are still delayed without a confirmed date**, confirmed as of October 19, while the Gemini app Skills rollout continues its mid-November arc — and the practical consequence for enterprise teams is worsening daily as Skills built in the app cannot be synced to Workspace. **Notion** lands the most unexpected platform entrant of the day: **Notion Agents sixth-generation harness ships October 20**, extending single-agent task duration from 5 minutes to more than 24 hours and introducing a model router called Auto that dispatches work to the best-cost model for each step.

---

## At a Glance: October 20 Highlights

Today's releases converge on a single inflection point: the platforms that began this month shipping individual agentic features are now beginning to reveal the governance and transparency architectures that will determine whether those features are trustworthy enough to delegate to completely — the shift from "can the agent do the task" to "can the user verify and audit what the agent did."

| Product | Key UX Developments |
|:---|:---|
| **Claude** | **Claude Code v2.1.303–v2.1.304 ship October 18–19 with reliability fixes; Claude Dashboards and Motion beta continue rollout with code-backed animation transparency** — Claude Code ships two reliability point releases in the 48-hour window; Claude Motion generates animations as editable code with no video-generation model involved, so every word, number, and timing is inspectable and revisable; Claude Dashboards shows the SQL query behind every chart, with a last-refresh timestamp; Docs, Slides, and Design now generally available on every plan including Free. [1][2][3] |
| **ChatGPT** | **Intelligent UI surfaces interactive charts, forms, and tools inline in ChatGPT conversations; Codex Composer Predictions enter beta for Pro users** — GPT-6 with Intelligent UI continues rollout, rendering charts, forms, and micro-tools directly in the conversation without requiring any app switch; Codex Composer predictions suggest the next message in a thread with Tab-to-accept; custom GPT retirement continues on track with Enterprise deadline December 11. [4][5][6] |
| **Google Gemini** | **Workspace Skills delay confirmed ongoing as of October 19; Gemini app Skills continue mid-November arc; sync gap compounds enterprise planning cost** — Skills inside Gmail, Docs, and Drive remain delayed without a new date; Skills in the Gemini app rolling out since October 13; skills don't sync between the two environments, requiring manual recreation; Gems remain available for business accounts until at least March 2027; Google Home Gemini update adds reliable "stop" command disambiguation and friendlier conversation endings. [7][8][9] |
| **Microsoft Copilot** | **Copilot Home/Code/Autopilot redesign rolls into Frontier; interactive PowerPoint slides target mid-to-late October GA; Today ambient feed enters private preview** — new Home screen merges Chat and Cowork with Word, Excel, and PowerPoint embedded; Autopilot is described as a persistent agent that works while the user is offline; Today proactively drafts replies, proposes schedule changes, and surfaces forgotten follow-ups across email, calendar, and Teams; interactive PowerPoint slides create full-slide clickable visuals that any viewer can explore without a Copilot licence. [10][11][12] |
| **Grok (xAI)** | **Grok Voice 3.0 ships October 14 with full-duplex speech, tool calling, 28 built-in voices, and automatic alias upgrade; Grok Build v1.0.61–1.0.62 ship CLI pipe safety and hook error naming** — Voice 3.0 scores 97% on Full Duplex Bench, handles 20 languages with auto-detection, supports server-side interruption and custom voice cloning; `grok-voice-latest` alias upgraded automatically with no code change; Build v1.0.61 names the failing program in hook spawn failures on Windows; Build v1.0.62 fixes CLI commands crashing when output pipe closes early. [13][14][15] |
| **Perplexity** | **Computer Automations (launched September 29, expanded October 5) establish event-driven, memory-carrying agent runs across Slack, Gmail, Outlook, Linear, and GitHub** — Automations replace Scheduled Tasks; each run carries memory of prior runs and builds on previous work; event triggers include conditional filters; Automations pause for review before consequential actions; credits are spent only on actual runs, not while watching for a trigger; inline charts and 3D visualizations now render directly in Computer threads. [16][17][18] |
| **Notion** | **Notion Agents sixth-generation harness ships October 20: 24-hour task duration, Auto model router, two-tier credit system, and BYOK for enterprise** — single-agent tasks now run for more than 24 hours, up from five minutes; Auto delegates each step to the best-cost model without user selection; enterprise customers can bring their own keys; admins gain spending visibility and controls. [19] |

---

## Product Highlights

### Claude / Anthropic: The Transparent Canvas and the Reliability Sprint

Anthropic's most UX-significant delivery across the 48 hours ending October 20 is not a single dramatic feature but a two-track story: a steady reliability-hardening sprint in Claude Code that continues to close the operational gaps in headless and agentic sessions, and the maturing rollout of a generative workspace whose most important trust-design primitive is one that almost no coverage has highlighted — the fact that every artefact Claude generates on the Dashboards and Motion surfaces is backed by inspectable, editable source code rather than opaque generative output.



Claude Code v2.1.303 and v2.1.304 shipped on October 18 and 19

, 

with October 18 delivering bug fixes and reliability improvements, while October 16's v2.1.302 fixed mods staying off for users connecting through a gateway with no Anthropic account, and fixed replies from Claude agents being refused after crashes — they are now retried for up to 12 seconds while the session restarts.

 The pattern across these rapid point releases is consistent: Anthropic is specifically closing the failure modes that appear in unattended, headless, and gateway-routed sessions — exactly the execution contexts that enterprise agentic pipelines depend on.

The generative workspace story is the one with longer-term UX significance. 

Starting October 8, Claude can turn data into a dashboard that stays current; Claude Dashboards connects to a data platform like BigQuery, Databricks, or Snowflake, or a CRM tool like Salesforce, and is in beta on paid plans.

 The trust-design primitive embedded in Dashboards is the per-chart query disclosure: 

each chart shows its query and the time of its last update, so you can check what is being counted.

 This is the correct transparency pattern for a conversational data surface — rather than presenting a chart as an authoritative answer, every Dashboards panel anchors the claim to the query that produced it, giving users an immediate audit path without requiring them to know SQL.



Claude Motion converts reports, charts, and product walkthroughs into short animated explainers; Claude writes editable code for the text, shapes, images, charts, and timing instead of using a video-generation model, so there is no generated footage or AI-generated people; users can revise the result in the editor or through a prompt, download an MP4, or continue in supported creative tools.

 The UX implication of the code-backed architecture is its verifiability: a Motion animation is not a black-box video render — it is a program that the user can inspect, modify, and audit at the level of individual frames. 

For Enterprise, Docs, Slides, and Design turn on by default on October 15, while Dashboards and Motion stay off until an admin turns them on.

 That default-off posture for the data-connected and motion surfaces is the correct enterprise trust-design choice — it ensures that the capabilities with the highest potential for data exposure and content misrepresentation require explicit admin activation rather than arriving silently with a plan upgrade.

---

### ChatGPT / OpenAI: Intelligent UI Matures and the Custom GPT Retirement Clock Ticks

OpenAI's most interaction-design-significant event in this window is not a new launch but the continued maturation of **Intelligent UI** — the generative interface layer that shipped October 7 with GPT-6 and that is now establishing the conversation itself as the primary rendering surface for charts, forms, and micro-tools, rather than a text stream that describes where to find them.



GPT-6 in ChatGPT introduces Intelligent UI, a new capability that allows ChatGPT to answer quickly with fully interactive user interfaces that make everyday answers more visual, make learning complex topics easier, and can quickly create a tool to solve a task right in the moment.

 The UX shift this establishes is a departure from the text-then-export loop that has characterised conversational AI since its inception: rather than producing a written answer that the user must then carry to a spreadsheet, chart tool, or form builder, the model renders the instrument that makes the answer usable inside the same conversational turn. 

Answers can come back as charts, forms, and small tools, and start while the model is still thinking.

 The "starts while thinking" detail is the temporal UX advance that practitioners should pay most attention to: it means the UI element begins populating before the generation is complete, converting the loading experience from a wait into a progressive reveal.

The interaction-design change that warrants equal attention is the **Codex Composer Predictions** beta. 

ChatGPT adds Composer predictions in Codex beta, suggesting the next message in a thread so users can press Tab to accept, review, or edit before sending.

The beta is available to personal ChatGPT Pro users aged 18 and older in all supported regions, in the latest Codex desktop app; it supports local and SSH threads using GPT-6 Astra or GPT-6.1 Sol; predictions are on by default, with an option to turn off Show predictions in General settings.

 The trust-design implication is the Tab-to-accept pattern: by requiring an explicit keypress to accept the suggestion, rather than auto-inserting it, Composer preserves the human author's moment of deliberate choice at every turn — an important signal in a tool where the AI's suggestions may carry significant downstream consequences in the codebase the session is working on.

The background governance story for enterprise ChatGPT practitioners this week is the custom GPT retirement timeline. 

Enterprise accounts can create no new GPTs from October 26, with GPTs retiring on December 11.

 Teams that have built internal workflows on custom GPTs should treat this as the deadline that resets their agent-surface architecture: the capabilities migrate to plugins, but the governance model, permission structure, and invocation patterns change with the migration, requiring deliberate re-review rather than automatic equivalence.

---

### Google Gemini: The Workspace Skills Gap Widens, and Smart Home Voice Learns to Stop

Google's most consequential Gemini interaction-design event in this window is, again, an absence rather than a delivery: 

as of October 19, 2026, Google's Workspace Updates blog says skills in the Gemini app began rolling out on October 13, with completion expected by mid-November — but Skills inside Workspace apps are "Delayed until further notice."



The enterprise cost of this delay is compounding in a specific and underappreciated way: 

Skills do not sync between the Gemini app and Workspace, so users must create them separately on each platform.

 This means every Skills configuration built in the Gemini app since October 13 represents work that will need to be manually recreated in Workspace Studio when the Workspace rollout eventually lands — a compounding investment tax on every hour spent configuring skills during the delay window. 

Some built-in tools don't work with skills yet; Google says most default tools available in Gems do not work with skills, including Create video, Create music, Canvas, Deep Research, and Guided learning.

 The capability gap is not just temporal — the Skills surface is shipping with meaningful functional regression relative to Gems for teams that relied on Canvas or Deep Research integration, and enterprise architects designing Workspace personas need to account for this gap explicitly.

The Gemini UX advance that did ship cleanly in this window is on the ambient smart home layer. 

Google Home is receiving a fresh update with improvements to reordering favourite devices, redesigned controls for third-party smart home devices, and fixes to how Gemini works with the Home app, including more reliable "stop" commands to prevent misinterpretations and easier-to-read answers on smart displays.

 The "stop" disambiguation fix is a meaningful interaction-design improvement: 

the update fixes an issue where saying "stop" used to be misinterpreted as ending a conversation rather than stopping an active alarm, timer, or media playback.

 For ambient voice agents operating in shared home environments, this is the intent-disambiguation failure mode that produces the most user frustration — and resolving it strengthens the trust contract for Gemini's ambient presence in the home as a context where users expect their commands to be interpreted correctly without hedging.

---

### Microsoft Copilot: Home, Autopilot, and the Ambient Architecture Takes Shape

Microsoft's most structurally significant Copilot interaction-design event materialising in this window is the Frontier rollout of the **Home/Code/Autopilot redesign** — a tripartite restructuring of the Copilot app that represents the clearest statement yet of Microsoft's thesis about how enterprise AI assistance should be organised: not as a single chat surface that does everything, but as three distinct delegation modes matched to three distinct work patterns.



Microsoft has announced the new Copilot, bringing more changes to the Copilot app's interface: a new Home screen brings Chat and Cowork together, Word, Excel, and PowerPoint are built right into the app, a new Code tab lets users build simple apps by describing them in plain English, and Autopilot is an always-on agent that works on the user's behalf.

 The UX implication of embedding Office directly into the Copilot Home surface — rather than treating Copilot as an add-in that lives inside Office — is a fundamental inversion of the ambient-agent relationship: the AI workspace becomes the primary environment, with document editing as a capability that lives inside it, rather than a document editor with an AI sidebar.



Coming soon to Home, Today is a command center that proactively supports users across email, calendar, Teams threads, meetings, and tasks; it organises and presents what users missed, what needs immediate attention, and what can be put off; Today not only visualises work but also moves it forward — drafts are already created and just need editing, proposed changes to schedules are already prepared, and forgotten follow-ups are ready to be sent, along with the necessary context to quickly grasp the situation.

 The interaction-design significance of Today is the elimination of the query step: rather than requiring the user to ask "what did I miss?" and then separately ask "what should I respond?", Today pre-generates the answer to both questions and presents the result as a set of pending human-review actions rather than a conversational exchange.

The PowerPoint surface advance approaching GA is equally significant for the generative workspace layer. 

Copilot in PowerPoint can now create interactive slides: full-slide visuals that audiences can click through to reveal steps, context, and data; users start from the new Interactive Slide button on the ribbon or the Create Interactive Slide skill in Copilot; anyone a user shares with can explore them without a Copilot licence.

Interactive slides run in a sandboxed view that doesn't connect to other content or services.

 The "no Copilot licence required to explore" design is the distribution primitive that will drive adoption: a Copilot-created interactive slide becomes a shareable artefact that any viewer can engage with, extending the value of the Copilot licence beyond the creator to every downstream consumer of the presentation.

---

### Grok (xAI): Voice Goes Agentic With Full-Duplex Tool Calling

xAI's most consequential interaction-design event in this window is not a Grok Build fix but the arrival of **Grok Voice 3.0** on October 14 — a voice model that crosses the design threshold separating conversational voice assistants from tool-connected agentic voice agents, and that did so at production scale across Tesla and SpaceX before it was even announced.



Released on October 14, 2026, Grok Voice 3.0 is a real-time speech-to-speech model developed by xAI; available through the Grok Voice Agent API, it combines spoken interaction, conversational reasoning, interruption handling, and tool calling for real-time voice applications.

 The tool-calling capability is the design boundary that matters: it means a Grok Voice session can not only respond to spoken input in natural speech but can invoke external APIs, look up data, or take actions mid-conversation without the user needing to type or switch surfaces. 

It powers voice agents that handle full-duplex conversations in multiple languages and complete multi-step tasks such as verifying customers, troubleshooting hardware, and issuing credits.



The interaction-design details that practitioners building voice-agent workflows should examine most carefully are the interruption model and the language-switching behaviour. 

The model handles 20 languages with automatic detection, so it can switch mid-call without a manual language flag; it ships 28 built-in voices; teams can also clone a custom voice from a reference clip up to 120 seconds long; server-side voice activity detection manages interruptions, letting a caller talk over the agent naturally.

 Server-side interruption handling is the correct architecture for enterprise voice-agent deployments: client-side interruption detection creates latency gaps that make the handoff feel abrupt, while server-side detection can manage the acoustic overlap gracefully without a perceptible seam.

The deployment-design detail that requires the most attention from enterprise teams is the automatic alias upgrade: 

grok-voice-latest now points to grok-voice-3.0, so sessions that use the alias are upgraded automatically; the API is unchanged.

 Teams that built on `grok-voice-latest` for its convenience have already been silently upgraded. 

The conversation flow Full Duplex Bench score improved from 95.1% to 97.0%, but time to first audio rose slightly from 0.70s to 0.81s.

 The 0.11-second latency increase is small enough to be imperceptible in casual conversation but meaningful in time-critical customer-support contexts — teams with latency-sensitive deployments should evaluate whether to pin to `grok-voice-2.0` while testing 3.0's task performance.

On the Grok Build governance front, 

Grok Build v1.0.61 makes hook spawn failures on Windows name the program that failed to start — such as PowerShell or Git Bash — instead of blaming the hook script

, and 

v1.0.62 fixes CLI commands such as grok models, grok sessions, and grok export no longer crashing when their output pipe closes early, such as when piped to head or when the output device is full.

 The pipe-safety fix is operationally significant for enterprise scripting environments where Grok Build output is frequently piped into downstream tools — a crash in that context would silently break the pipeline without surfacing an error in the consuming command.

---

### Perplexity: Computer Automations Establish the Event-Driven Agent Primitive

Perplexity's most significant agentic-workflow advance materialising in this window is the settling of **Computer Automations** — launched September 29 and expanded with inline visualisations on October 5 — into what is becoming the clearest production-grade implementation of event-driven, memory-carrying background agents in the consumer AI category.



Automations bring Computer's capabilities to long-running agents that work proactively on a schedule or in response to conditional events; each agent uses Computer's connected files, tools, and Projects to carry out its assignment; it remembers prior work, picking up where it left off without waiting for a new request.

 The design distinction between Automations and the Scheduled Tasks they replace is not primarily scheduling — it is memory carryover: 

triggers work with Slack, Gmail, Outlook, Linear, and GitHub events with conditional filters; each run carries memory of prior runs, so agents build on previous work instead of restarting; Automations can also watch for missed deadlines or overdue replies and flag them; credits are spent only on actual runs, not while watching for a trigger.



The trust-design gate embedded in Automations is the consequential-action pause: 

Automations can use Memory, Skills, and connectors, build on earlier runs, and pause for review before consequential actions.

 This is the correct human-in-the-loop design for recurring agentic workflows: rather than applying a blanket approval gate to every step (which defeats the purpose of automation) or removing approvals entirely (which removes the trust contract), the system identifies the steps that carry irreversible or high-stakes consequences and gates only those — letting routine steps proceed unattended while surfacing the decisions that genuinely require human judgement.

The inline visualisation capability that shipped October 5 closes an important feedback-loop gap in the agentic workflow surface. 

Perplexity Computer can now create interactive charts and visualisations directly in a Computer thread; users can explore concepts with interactive 3D explanations, or chart financial data with TradingView Lightweight Charts for candlesticks, volume, and moving averages.

 The UX significance of inline visualisations in an agentic thread — rather than exporting results to a separate dashboard — is that the evidence is co-located with the reasoning: a Computer agent that researches market data and then charts it in the same thread makes the entire analytical chain inspectable in one surface, rather than requiring the user to cross-reference outputs across two tools.

---

### Notion: The Unexpected Entrant — 24-Hour Agents and the Auto Router

The most unexpected platform story of the day comes from outside the core five: **Notion's sixth-generation Agents harness**, shipping October 20, which advances a set of temporal-UX and cost-governance design primitives that every enterprise AI platform has been circling but that Notion is the first to ship in combination.



Notion rolled out a sixth-generation agent harness that can run single agent tasks for more than 24 hours (up from five minutes) and added a smarter model router called Auto that delegates work to the best-cost model.

 The 24-hour task duration is the temporal-UX event that matters most: a five-minute ceiling means Notion Agents could only handle tasks that could be chunked into sub-five-minute segments, which excluded almost every meaningful knowledge-work automation. The 24-hour ceiling converts Notion Agents from a task-completion tool into a genuine long-running background agent capable of candidate screening, recursive research, or multi-step content pipelines without the user needing to manage continuity across runs.



Teams using Notion as their workspace can run longer-running, multi-step automations without repeatedly paying for large token windows, and admins get visibility and spending controls to contain agent cost and risk.

 The Auto model router is the cost-governance design primitive that makes 24-hour tasks financially viable for enterprise teams: by delegating each step to the best-cost model rather than running the entire task on the most capable (and expensive) model, Auto converts long-duration agent tasks from a premium-tier luxury into a practical operational tool. The BYOK (bring your own key) option for enterprise customers further extends this cost-control posture, allowing organisations to route agent compute through their own model contracts rather than through Notion's margin.

---

## The Bigger Picture: Live Canvases Graduate, Voice Goes Agentic, and the Workspace Persona Wars

The 48 hours ending October 20, 2026 reveal an industry that has crossed a specific threshold: the generative workspace features that were in beta six weeks ago are now infrastructure, and the question is no longer whether AI can generate a dashboard, animate a report, or run a 24-hour background task — it is whether the user can trust what was generated, inspect how it was done, and govern what the agent is authorised to do next. Claude Dashboards and Motion establish the clearest answer to the first question: every chart shows its query, and every animation is backed by code you can read and edit — transparency primitives that competing tools do not yet offer at this level of granularity. Grok Voice 3.0 establishes the clearest answer to the second question from the voice layer: by shipping full-duplex tool-calling with server-side interruption management and automatic alias upgrades, xAI has converted voice from a conversational novelty into an agentic infrastructure surface — one that already handles millions of real production interactions at Tesla and SpaceX, making it the most battle-tested voice-agent platform in the consumer AI category. Microsoft's Home/Code/Autopilot restructuring, Today's ambient feed, and the interactive PowerPoint slides approaching GA together represent the most ambitious answer to the third question: by proposing a tripartite architecture that separates daily delegated work, app creation, and offline-persistent agency into distinct surfaces, Microsoft is designing the governance architecture of the AI workspace before its users have had time to ask for it. The throughline across all six platforms — including Notion's unexpected arrival with 24-hour agents and an Auto model router — is the same: the era of the demo feature is ending. What is being built now is the layer that makes agentic AI governable, auditable, and safe enough to leave running while no one is watching.

---

## References

[1] github.com/anthropics/claude-code. (2026). *Claude Code Releases — v2.1.303, v2.1.304*. [https://github.com/anthropics/claude-code/releases](https://github.com/anthropics/claude-code/releases)

[2] code.claude.com. (2026). *Claude Code Changelog — October 2026*. [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

[3] testingcatalog.com. (2026). *Claude launches Dashboards and Motion in beta*. [https://www.testingcatalog.com/claude-launches-dashboards-and-motion-in-beta/](https://www.testingcatalog.com/claude-launches-dashboards-and-motion-in-beta/)

[4] openai.com. (2026). *GPT-6 and Intelligent UI for everyone*. [https://openai.com/index/gpt-6-for-everyone/](https://openai.com/index/gpt-6-for-everyone/)

[5] help.openai.com. (2026). *ChatGPT release notes — October 2026*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[6] blog.memoryplugin.com. (2026). *ChatGPT New Features October 2026: GPT-6 & Intelligent UI*. [https://blog.memoryplugin.com/chatgpt-new-features-october-2026/](https://blog.memoryplugin.com/chatgpt-new-features-october-2026/)

[7] workspaceupdates.googleblog.com. (2026). *Introducing skills in the Gemini app and Workspace, plus what's next for Gems*. [https://workspaceupdates.googleblog.com/2026/09/skills-gemini-app-workspace.html](https://workspaceupdates.googleblog.com/2026/09/skills-gemini-app-workspace.html)

[8] dev.to. (2026). *Gemini Gems to Skills: What Changes in November 2026 and How to Move Your Gems Now*. [https://dev.to/crypteasensei/gemini-gems-to-skills-what-changes-in-november-2026-and-how-to-move-your-gems-now-1di1](https://dev.to/crypteasensei/gemini-gems-to-skills-what-changes-in-november-2026-and-how-to-move-your-gems-now-1di1)

[9] 9to5google.com. (2026). *Google Home update rolling out with improved Favorites, more app & Gemini fixes*. [https://9to5google.com/2026/10/14/google-home-update-rolling-out-improved-favorites-gemini-fixes/](https://9to5google.com/2026/10/14/google-home-update-rolling-out-improved-favorites-gemini-fixes/)

[10] supersimple365.com. (2026). *The new Copilot: Home, Code, Autopilot and interface changes*. [https://supersimple365.com/the-new-copilot-home-code-autopilot-and-interface-changes/](https://supersimple365.com/the-new-copilot-home-code-autopilot-and-interface-changes/)

[11] supersimple365.com. (2026). *Create interactive slides in PowerPoint with Copilot*. [https://supersimple365.com/create-interactive-slides-in-powerpoint-with-copilot/](https://supersimple365.com/create-interactive-slides-in-powerpoint-with-copilot/)

[12] note.com. (2026). *Announcing the new Copilot with Home, Code, and Autopilot*. [https://note.com/kazuhiko_kawai/n/n4b8f78a9c9fd](https://note.com/kazuhiko_kawai/n/n4b8f78a9c9fd)

[13] x.ai. (2026). *Grok Voice 3.0 — API Release Notes, October 14, 2026*. [https://docs.x.ai/developers/release-notes](https://docs.x.ai/developers/release-notes)

[14] eesel.ai. (2026). *Grok Voice 3.0: what it is, what changed, and how to use it*. [https://www.eesel.ai/blog/grok-voice-3](https://www.eesel.ai/blog/grok-voice-3)

[15] x.ai. (2026). *Grok Build Changelog — v1.0.61–v1.0.62*. [https://x.ai/changelog/build](https://x.ai/changelog/build)

[16] perplexity.ai. (2026). *Computer adds Automations for ongoing work*. [https://www.perplexity.ai/hub/blog/computer-adds-automations-for-ongoing-work](https://www.perplexity.ai/hub/blog/computer-adds-automations-for-ongoing-work)

[17] alphasignal.ai. (2026). *Perplexity's Computer Agent Now Automates Recurring Work Across Slack, Gmail, and GitHub*. [https://alphasignal.ai/news/perplexity-s-computer-agent-now-automates-recurring-work-across-slack-gmail-and](https://alphasignal.ai/news/perplexity-s-computer-agent-now-automates-recurring-work-across-slack-gmail-and)

[18] releasebot.io. (2026). *Perplexity Release Notes — October 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[19] aiagentstore.ai. (2026). *AI Agent News Today — October 20, 2026: Notion rebuilds Agents for longer work, lower cost*. [https://aiagentstore.ai/ai-agent-news/today](https://aiagentstore.ai/ai-agent-news/today)