# UX Briefing: Persistent Agents, Watermark Proliferation, and the Office Agent Collapse

**November 06, 2026**

Good morning. The 48 hours ending November 6, 2026 are defined by three simultaneous design movements: a **persistent-agent proliferation surge**, with Perplexity launching **Teammates** on November 5 as the most fully-realised multi-agent workspace yet shipped to consumers — agents that own ongoing roles, recruit other agents, and surface human decisions only when escalation is required — arriving on the same day the **Perplexity Agent API** gains a new `ultra` effort level and a near-90% cost reduction on `medium`; a **provenance signal convergence**, with Anthropic completing the retroactive text-watermarking of its four remaining production Claude models (Mythos 5, Opus 4.7, Opus 4.6, Sonnet 4.6) from November 3, making sixteen Claude models watermarked in total and closing the namespace gap that allowed operators to escape provenance signals by pinning older slugs; and a **Microsoft surface-consolidation acceleration**, with the November 3 announcement that standalone Word, Excel, and PowerPoint agents will be retired from the left rail entirely in mid-November and their capabilities absorbed directly into Copilot Chat, completing the app-agent-to-chat-agent pipeline Microsoft has been building since October — alongside the Copilot Home unification (Chat + Cowork + Projects + Workspaces) and Skills-in-Chat rolling worldwide this month. **Google Gemini** ships **Gemini Omni 1.2 Flash** on November 5 as a GA video-generation model in Google Vids, the Gemini app, and the API, introducing multi-turn conversational editing — a paradigm shift for agentic video creation — alongside a refreshed Gemini Forms insight surface rolling out to Workspace. **Grok (SpaceXSI)** navigates a minor Grok Bot computer-use degradation on November 5–6 (resolved within 14 minutes on November 6) while the Grok Build 155 changelog advances voice dictation, memory indexing, and subagent session visibility.

---

## At a Glance: November 6 Highlights

Today's window is defined by the agent-layer maturing from single-session assistants into persistent, role-bearing workers — and by the trust infrastructure that must accompany that shift arriving in parallel: watermarks expanding to cover the full Claude production stack, Copilot collapsing discrete agent surfaces into one accountable Chat entry point, and Perplexity surfacing human decision gates only at the moments that genuinely require them.

| Product | Key UX Developments |
|:---|:---|
| **Claude** | **Anthropic retroactively extends its invisible text watermark to Claude Mythos 5, Opus 4.7, Opus 4.6, and Sonnet 4.6 from November 3, covering sixteen Claude models in total; the watermark adds no tokens, does not alter quality or readability, requires no request changes, and is applied globally because Anthropic cannot yet scope it by region; there is no opt-out documented for operators** — the retroactive expansion closes the production escape hatch: organisations that had pinned older model slugs to avoid watermarking now find that the November 3 update closes the gap, leaving no current-generation Claude model unmarked. [66-1,66-4,70-7,74-5,74-6,72-6,72-7] |
| **ChatGPT** | **ChatGPT Images 2.6 (shipped November 4) continues worldwide rollout to all tiers: one-step animated GIF creation, saved reference images for reuse across chats, 50% faster generation, and two new API variants (GPT-Image-2.6 Flare for speed, GPT-Image-2.6 Sunburst for quality and SVG export); Dots for Enterprise enters its admin preview window, closing November 18, with per-role access controls and UAE residency exclusion** — weekly image output at OpenAI topping 4 billion is the usage signal that contextualises why the reference-image library matters: the persistent creative library converts a stateless per-session activity into a durable workflow asset. [15-2,19-3,19-5,19-6,17-3,17-7,12-1,12-3,12-5] |
| **Google Gemini** | **Gemini Omni 1.2 Flash goes GA on November 5 in Google Vids, the Gemini app, and the API: native 15-second video generation (up from 10 seconds), multi-turn conversational editing where the model carries context from earlier exchanges across refinements, up to 10 reference images for consistent character styling, and a 30% price reduction; Gemini in Forms begins rolling out actionable insights to Workspace on November 2** — multi-turn conversational editing is the defining interaction advance: a user no longer must restart generation from scratch to refine a clip, establishing an iterative creative dialogue with the model across multiple exchanges. [96-2,96-4,99-6,99-7,99-8,99-10,99-13,100-4,100-5,20-2,20-3] |
| **Microsoft Copilot** | **Microsoft announces standalone Word, Excel, and PowerPoint agents will be retired from the Copilot left rail mid-November through late December 2026, with document creation and editing absorbed directly into Copilot Chat; users can no longer pin, @mention, or invoke the standalone agents; Skills-in-Chat and the unified Home (Chat + Cowork + Projects + Workspaces) continue worldwide rollout this month** — the agent-to-Chat collapse is the most consequential surface unification Microsoft has shipped this year: the named, invocable agent disappears as a distinct interaction object and becomes an invisible capability embedded in the chat flow. [86-2,86-10,86-11,91-4,91-5,38-4,38-5,38-10,38-11,38-12] |
| **Grok (SpaceXSI)** | **Grok Bot computer-use degradation on November 5 (resolved in 1h 14m) and a regional computer-use failure on November 6 (resolved in 14 minutes) are consistent with the Grok Bot egress-proxy tunnel vulnerability documented in community forums; Grok Build 155 ships voice dictation preview that grows the prompt live as you speak, memory indexing via a concise MEMORY.md topic index with per-topic read-frequency ranking, and Rex terminal support that exposes each running subagent as its own status record** — the per-subagent Rex status record is the most trust-significant addition: operators running parallel Grok Build workflows can now observe what each sub-agent is doing in real time, rather than inferring state from aggregate output. [128-6,129-7,129-8,103-8,103-9,103-10] |
| **Perplexity** | **Perplexity launches Teammates on November 5 for Max subscribers on the web: persistent agents that own ongoing roles, run on their own Computer instances, recruit additional Teammates as work grows, notify users only when decisions are needed, and integrate with Slack; simultaneously, the Agent API gains a new `ultra` effort level (four parallel agents, 85.9% WANDR score) and the `medium` tier's BrowseComp score rises from 55% to 77% while cost falls nearly 90%** — Teammates' recruit-to-scale design is the most structurally ambitious agentic interaction pattern shipped by any platform this week: rather than requiring the user to provision each agent manually, the system dynamically adds capacity as work grows. [53-5,58-4,58-6,58-7,58-8,64-9,64-12,112-1,112-5,112-6,117-4,117-5] |

---

## Product Highlights

### Claude / Anthropic: Retroactive Watermarking Closes the Production Escape Hatch

Anthropic's most consequential interaction-design and trust-design development reaching operators in this window is not a new feature but the closure of a structural gap in its provenance infrastructure: the **retroactive text watermarking** of the four remaining production Claude models that had not yet been covered, effective November 3, 2026.



Starting November 3, 2026, Anthropic will apply its text watermark to the output of Claude Mythos 5, Opus 4.7, Opus 4.6 and Sonnet 4.6 on the Claude Platform — the company's API — while the rollout on Amazon Bedrock may take a few extra days.

 The scope is now comprehensive: 

every Claude model launched since August 2, 2026 watermarks its text, among them Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1 and Mythos 5.1, plus the ones updated later.

 The UX implication for operators is that the previous strategy of avoiding watermarking by pinning a pre-August 2026 model slug is now closed: sixteen Claude models carry the mark, and the four that formed the last remaining gap are now covered. The technical design of the watermark preserves operator experience intact: 

the developer documentation states that marking requires no changes to requests or response handling.



The governance design raises a trust question that Anthropic has resolved in a specific way: 

the help center says marking applies "wherever Claude is offered, worldwide," and Anthropic's explainer gives the reason that it cannot yet scope it by region; the help center and the developer documentation describe no opt-out.

 The comparison with SpaceXSI's approach — which defaults watermarking on but preserves a per-model admin opt-out — is the design choice that most differentiates the two platforms' trust architectures. 

The method is a version of SynthID-Text, published by Google DeepMind, and Anthropic says it adds no characters or extra tokens, leaves quality and readability unchanged, and costs nothing more to run; the company also says the watermark carries no information that could trace text back to a user, an organization, or a conversation, and it is being introduced to comply with the EU AI Act, applied worldwide because Anthropic cannot yet scope it by region.

 The no-user-attribution guarantee is the correct privacy architecture for a provenance signal: the mark identifies that Claude produced the text, not who asked Claude to produce it — a distinction that matters significantly in regulated or legally sensitive deployment contexts.

---

### ChatGPT / OpenAI: Images 2.6 Establishes the Persistent Creative Library Pattern

OpenAI's dominant interaction-design story continuing into this window is the worldwide rollout of **ChatGPT Images 2.6**, which shipped on November 4 and is now reaching all subscription tiers and platforms as this briefing goes to press. The headline feature — animated GIF creation — has received the most coverage, but the more structurally significant interaction advance is the persistent reference-image library.



ChatGPT introduces Images 2.6, a faster image generation model that better preserves details during edits, plus GIF creation and saved reference images for reuse across chats.

OpenAI has made Images 2.6 available worldwide in ChatGPT and Codex; the model reaches every subscription tier, from free users to paying ones, on web, desktop, and mobile.

 The GIF surface is the interaction pattern that closes the gap left by Sora's discontinuation: 

the headline feature is animated GIFs, generated in a single step.

 But the reference-image library is the advance that changes the structural nature of image generation as a workflow. Previously, every image session in ChatGPT began stateless — the user's established characters, faces, and brand assets existed only in the files they re-uploaded. With saved references, those assets become persistent objects in the user's ChatGPT workspace, invokable by name rather than by file path.

On the API side, 

the company highlighted new features such as faster generation speeds, improved consistency during editing, markup-based editing, and SVG output.

GPT-Image-2.6 Flare is optimized for speed; GPT-Image-2.6 Sunburst is focused on output quality.

 The parallel Dots for Enterprise story — now in its admin preview window through November 18 — remains the governance story of the window: 

Dots are generally available to eligible ChatGPT Enterprise, Edu, and Healthcare workspaces, with an admin preview until November 18, 2026; during the preview, workspace owners and admins can enable access or opt out before Dots become available by default.

Dots are not available for workspaces with UAE data or inference residency.

 The November 18 default-on date is the trust-design deadline that matters most for enterprise administrators this week: Dots that were previously opt-in become opt-out, and organisations that have not reviewed their governance posture before that date will find background agents active in their workspaces without an explicit enabling decision.

---

### Google Gemini: Omni 1.2 Flash Introduces Conversational Video Editing and Vids GA

Google's most significant interaction-design advance in this 48-hour window is the **Gemini Omni 1.2 Flash** general availability release on November 5 — a video-generation model update that introduces an interaction paradigm that has not previously existed in a production AI video tool: **multi-turn conversational editing**, where the model carries context from earlier refinement exchanges across subsequent edits, eliminating the restart-from-scratch cycle that has historically defined AI video generation workflows.



Google announced Gemini Omni 1.2 Flash on November 5, 2026, making the video-generation and editing model generally available; the update raises native clip length to 15 seconds, adds multi-turn conversational editing, and cuts 720p pricing by 30% to approximately $0.07 per second.

 The conversational editing pattern is the UX advance that most distinguishes 1.2 from its predecessor: 

multi-turn conversational editing means a user can refine a clip through back-and-forth prompts instead of starting over each time; the model draws on context from earlier exchanges to keep scenes consistent across edits.

 This shifts video generation from a generate-and-discard interaction model to an iterative creative dialogue — the same pattern that made text generation workflows dramatically more productive once conversational context became persistent. 

Reference following also gets a boost; users can now feed in 7 to 10 reference images within a single generation process.



The provenance design is notably consistent with the industry-wide watermarking wave of this window: 

every generated video carries Google's built-in SynthID watermark.

 Inside Google Workspace, 

users now have access to Gemini Omni 1.2 Flash directly within Google Vids; Omni 1.2 provides longer duration videos up to 15 seconds and improved quality resulting in higher character consistency and vocal realism.

 The integration into Google Vids — a Workspace tool used by organisations rather than individual creative consumers — is the deployment decision that most expands the enterprise reach of the new conversational editing pattern: a marketing team member composing a campaign video inside Vids can now refine a 15-second clip through natural-language conversation without leaving Workspace or switching to a separate generation tool.

---

### Microsoft Copilot: The Agent-to-Chat Collapse and the November Skills Rollout

Microsoft's most consequential interaction-design announcement in this window is not an addition but a planned removal: the **retirement of standalone Word, Excel, and PowerPoint agents** from the Copilot left rail, announced November 3 and scheduled to complete by late December 2026. This is the most structural surface-unification decision Microsoft has taken in the Copilot era — it eliminates a category of AI interaction object (the named, invocable document agent) and absorbs its capabilities into the undifferentiated Chat entry point.



Microsoft 365 Copilot will replace standalone Word, Excel, and PowerPoint agents with integrated document creation and editing in Copilot Chat.

 The user-impact is significant and deliberate: 

as the change reaches users, the standalone agents will be removed from the left rail and agent discovery; users will no longer be able to find, pin, @mention, or invoke them as separate agents.

Users will create or refine documents, spreadsheets, and presentations directly in Copilot Chat without selecting a separate agent; the standalone agents will disappear from the left rail and agent discovery, and users will no longer be able to pin, @mention, or invoke them separately.

 The UX implication is a loss of discoverability in exchange for a gain in flow continuity: a user who previously selected the Word agent explicitly as a signal of their intent now expresses that intent conversationally, and Copilot applies the appropriate integrated capability without the user choosing an agent. The design risk is that the named agent gave users a legible mental model of "what AI is handling this" — removing it increases flow but reduces transparency about which capability is active at any given moment.

The parallel positive story is **Skills-in-Chat**, which continues worldwide rollout this month. 

Skills are coming to Copilot Chat; a skill is a reusable set of instructions, so if you find yourself typing the same prompt every week, you can save it once and share it with your team, and you can create one just by describing it in plain English.

 The creation model is the critical interaction-design detail: natural-language skill authoring converts a power-user feature (formal prompt templates) into a broadly accessible one. 

Microsoft Copilot app updates include a new Home integrating Chat, Cowork, Projects, and Workspaces; Projects organize related tasks and files without storing content, while Workspaces replace Notebooks for team collaboration.

 The November Home rollout — alongside 

Projects keeping related chats, files, meetings, and instructions in one place, with Chat and Cowork sharing a single searchable history

 — is the unified context persistence layer that makes the agent-to-Chat collapse viable: users can find the work Copilot did without having to remember which agent did it.

---

### Grok (SpaceXSI): Grok Bot Computer-Use Degradations and Build 155's Subagent Visibility

SpaceXSI's most interaction-design-significant developments in this 48-hour window are split between a trust-eroding availability story and a trust-building observability advance. On the availability side, 

resolved incidents on November 5 include degraded Grok Bot performance (starting 12:34 AM, resolved 1:49 AM) and issues with source control integrations.

 On November 6, 

computer use in Grok Bot fails for users in a few regions, with the minor incident starting November 6 at 11:49 AM and resolving by 12:03 PM.

 The browser egress-tunnel pattern — 

the bot's computer has completely lost browser internet access, with every website returning ERR_TUNNEL_CONNECTION_FAILED and the proxy at 127.0.0.1:8791 not responding

 — is a recurring failure mode in Grok Bot's computer-use layer that cuts the bot off from the web browsing its agentic tasks depend on. For users running Grok Bot as an always-on background agent for delegated research or web tasks, a tunnel failure that silently prevents the bot from reaching any website is precisely the class of invisible failure that makes persistent agents difficult to trust: the bot appears active but is operating in a degraded state that produces no output without surfacing a legible error to the user.

The offsetting observability advance is in **Grok Build 155**, which improves the legibility of running agentic sessions in the terminal. 

Voice dictation preview grows the prompt as you speak and keeps the newest words in view

 — a real-time dictation feedback pattern that reduces the blind input friction of terminal-based agent commands. More significantly for multi-agent observability, 

memory always uses the concise MEMORY.md index of topic titles and paths, and /memory lists topics by how often Grok reads them; Rex terminal support reports each open session and each running subagent as its own record, so Rex shows what each one is doing.

 The per-subagent Rex record is the trust-design advance that matters most for practitioners running parallel Grok Build workflows: previously, the status of each sub-agent in a multi-agent build was inferred from aggregate output; now it is directly observable as a named, real-time record. This is the kind of agent transparency primitive that makes the difference between an operator who can confidently leave a multi-agent coding task running overnight and one who cannot.

---

### Perplexity: Teammates Launches the Role-Based Persistent Agent and Agent API Gets Its `ultra` Tier

Perplexity's most consequential interaction-design advance in this 48-hour window is the launch of **Perplexity Teammates** on November 5 — the most fully-specified persistent-agent product any platform has shipped to consumers in this briefing window, and the one that most directly names the interaction paradigm shift it represents.



CEO Aravind Srinivas described Teammates as "personal agents for work" that "change the paradigm from writing prompts in a session to giving high-level goals."

The agents work inside Perplexity Computer, the company's cloud-based agentic assistant that can perform multi-step tasks, and Perplexity explains that the new agents build on top of Computer and come with "additional capabilities for ongoing, large-scale work."

 The multi-agent orchestration pattern is the structural advance: 

Teammates work together, and they can even manage other teammates to make sure tasks are getting done; they can also bring in more teammates and plan the newcomers' tasks accordingly, the more work you give them.

 This recruit-to-scale design means the user does not provision agents manually as workload grows — the system dynamically adds Teammate capacity as the scope of an assigned project expands. The notification design is the correct trust-pattern for a background agent: 

Teammates work 24/7 in the background and will notify you when you have to make decisions.

Users can also interact with agents through Slack, where coworkers can contribute instructions or review ongoing tasks.

 Critically, 

Perplexity also describes the ability to take over an agent's desktop session when direct intervention is needed

 — the take-over primitive is the correct escape-hatch design for a persistent agent that runs into a situation it cannot navigate autonomously.

Simultaneously, Perplexity shipped a major **Agent API** restructuring that will determine whether Teammates is a standalone consumer product or the tip of a developer ecosystem. 

Effort levels in the Perplexity Agent API let developers choose the balance of cost, speed, and research depth for each task; today, every effort level now costs less per query, with research quality that is higher or unchanged; a new ultra level is available for the most wide-reaching and comprehensive research.

Medium improved from 55% to 77% on BrowseComp and DSQA while its cost fell almost 90%, and a new ultra level is available for broad research.

Ultra assigns the same research problem to three agents running in parallel, allowing each to assemble evidence independently.

 The parallel-agent architecture at the API level mirrors the Teammates product architecture at the consumer level — in both cases, Perplexity's answer to deep research is not a larger model but a broader deployment of coordinated agents.

---

## The Bigger Picture: Persistent Agents, Watermark Proliferation, and the Office Agent Collapse

The 48 hours ending November 6, 2026 crystallise a design tension that the AI industry has been approaching since the first background agents shipped: the more capable and persistent an agent becomes, the harder it is for users to maintain a coherent mental model of what it is doing, on whose authority, and with what data — and yet this window shows the industry simultaneously making agents more capable and less legible at the surface level. Perplexity's Teammates recruits its own sub-agents without the user's explicit instruction; Microsoft is removing the named document agents that gave users a legible "which AI is handling this" signal; Grok Bot's computer-use layer can fail silently in a way the user cannot observe without monitoring infrastructure. At the same time, the provenance layer is tightening independently of the interaction layer: Anthropic's retroactive watermarking of sixteen Claude models and Google embedding SynthID in every Omni video represent a world in which AI-generated content is universally marked for downstream detection, but the in-session experience of delegating to an agent remains largely opaque. The platforms that are winning the trust-design race this week — Perplexity with its notification-on-decision-only gate, Grok Build with its per-subagent Rex status records, Copilot with its skill-attribution in Chat — are the ones that are building legibility into the agent's real-time behaviour, not just into the audit log that becomes accessible after the fact. The challenge is that the same week's most significant surface changes (Microsoft collapsing agents into Chat, Perplexity's Teammates auto-scaling without user provisioning) are moving in the opposite direction: reducing the number of explicit, named interaction objects the user can point to as the locus of AI action. The industry has not yet produced a satisfying design answer for how a user maintains a trustworthy mental model of a background agent fleet they did not explicitly assemble — and that is the question that will define the next phase of agent interface design.

---

## References

[1] pasqualepillitteri.it. (2026). *Claude Text Watermark Arrives on Opus 4.7, 4.6 and Sonnet 4.6 on November 3*. [https://pasqualepillitteri.it/en/news/27785/claude-watermark-november-3-opus-4-7-sonnet-4-6](https://pasqualepillitteri.it/en/news/27785/claude-watermark-november-3-opus-4-7-sonnet-4-6)

[2] digitalapplied.com. (2026). *Claude Adds Text Watermarks: Which Models, and Why Now*. [https://www.digitalapplied.com/blog/claude-text-watermark-mythos-opus-sonnet](https://www.digitalapplied.com/blog/claude-text-watermark-mythos-opus-sonnet)

[3] beri.net. (2026). *Claude's Text Watermark Now Covers Mythos 5, Opus 4.7 and Sonnet 4.6*. [https://www.beri.net/article/claude-text-watermark-mythos-5-opus-4-7-sonnet-4-6-november-3-no-opt-out-article-50-detection-api-vs-openai-textgrain](https://www.beri.net/article/claude-text-watermark-mythos-5-opus-4-7-sonnet-4-6-november-3-no-opt-out-article-50-detection-api-vs-openai-textgrain)

[4] techweez.com. (2026). *Anthropic is Bringing Text Watermarking to More Claude Models*. [https://techweez.com/2026/11/02/anthropic-is-bringing-text-watermarking-to-more-claude-models/](https://techweez.com/2026/11/02/anthropic-is-bringing-text-watermarking-to-more-claude-models/)

[5] cellcog.ai. (2026). *Claude's Text Watermark: Older Models Join Nov 3*. [https://cellcog.ai/blog/claude-watermark-older-models/](https://cellcog.ai/blog/claude-watermark-older-models/)

[6] releasebot.io. (2026). *Anthropic Release Notes — November 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[7] help.openai.com. (2026). *ChatGPT release notes — November 4, 2026*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[8] openai.com. (2026). *Release notes — November 4, 2026*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[9] cryptobriefing.com. (2026). *OpenAI rolls out Images 2.6 globally across ChatGPT and Codex*. [https://cryptobriefing.com/openai-images-2-6-global-rollout-chatgpt-codex/](https://cryptobriefing.com/openai-images-2-6-global-rollout-chatgpt-codex/)

[10] note.com/caged. (2026). *OpenAI Announces Images 2.6 with GIF Generation*. [https://note.com/caged/n/n75db7fe25dc4](https://note.com/caged/n/n75db7fe25dc4)

[11] releasebot.io. (2026). *ChatGPT Updates by OpenAI — November 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[12] workspaceupdates.googleblog.com. (2026). *Gemini Omni 1.2 Flash now in Vids with 15-second generations and improved quality*. [https://workspaceupdates.googleblog.com/2026/11/gemini-omni-12-flash-now-in-vids-with-15second-generations-and-improved-quality.html](https://workspaceupdates.googleblog.com/2026/11/gemini-omni-12-flash-now-in-vids-with-15second-generations-and-improved-quality.html)

[13] unite.ai. (2026). *Google's Gemini Omni 1.2 Flash Reaches General Availability*. [https://www.unite.ai/googles-gemini-omni-1-2-flash-reaches-general-availability/](https://www.unite.ai/googles-gemini-omni-1-2-flash-reaches-general-availability/)

[14] cryptobriefing.com. (2026). *Google rolls out Gemini Omni 1.2 Flash with 15-second AI video generation*. [https://cryptobriefing.com/google-gemini-omni-12-flash-video/](https://cryptobriefing.com/google-gemini-omni-12-flash-video/)

[15] tech-insider.org. (2026). *Gemini Omni 1.2 Flash: 15s AI Video, 30% Cheaper*. [https://tech-insider.org/gemini-omni-1-2-flash-15-second-video-30-percent-price-cut-2026/](https://tech-insider.org/gemini-omni-1-2-flash-15-second-video-30-percent-price-cut-2026/)

[16] m365admin.handsontek.net. (2026). *Changes to Word, Excel, and PowerPoint agents in Microsoft Copilot*. [https://m365admin.handsontek.net/changes-word-excel-powerpoint-agents-microsoft-copilot/](https://m365admin.handsontek.net/changes-word-excel-powerpoint-agents-microsoft-copilot/)

[17] m365admin.handsontek.net. (2026). *Microsoft Copilot app: Updates to Home and navigation*. [https://m365admin.handsontek.net/microsoft-copilot-app-updates-home-navigation/](https://m365admin.handsontek.net/microsoft-copilot-app-updates-home-navigation/)

[18] changingsocial.com. (2026). *What's new in Microsoft Copilot — November 2026*. [https://www.changingsocial.com/blog/whats-new-in-microsoft-copilot-november-2026/](https://www.changingsocial.com/blog/whats-new-in-microsoft-copilot-november-2026/)

[19] pupuweb.com. (2026). *MC1536062 Changes to Word, Excel, and PowerPoint agents in Microsoft Copilot*. [https://pupuweb.com/mc1536062-changes-to-word-excel-and-powerpoint-agents-in-microsoft-copilot/](https://pupuweb.com/mc1536062-changes-to-word-excel-and-powerpoint-agents-in-microsoft-copilot/)

[20] openstatus.dev. (2026). *Is Cursor Grok Bot Down? Cursor Grok Bot Status & History*. [https://www.openstatus.dev/status/cursor/grok-bot](https://www.openstatus.dev/status/cursor/grok-bot)

[21] multichats.ai. (2026). *Grok Status — Real-Time Updates*. [https://www.multichats.ai/status/grok-status](https://www.multichats.ai/status/grok-status)

[22] releasebot.io. (2026). *xAI Release Notes — November 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[23] shiftdelete.net. (2026). *Perplexity Teammates Bring Always-On AI Agents to Max*. [https://shiftdelete.net/en/perplexity-teammates-ai-agents](https://shiftdelete.net/en/perplexity-teammates-ai-agents)

[24] digitaltrends.com. (2026). *Perplexity's new AI coworkers can take over your workload*. [https://www.digitaltrends.com/cool-tech/perplexitys-new-ai-coworkers-can-take-over-your-workload-but-they-dont-come-cheap/](https://www.digitaltrends.com/cool-tech/perplexitys-new-ai-coworkers-can-take-over-your-workload-but-they-dont-come-cheap/)

[25] engadget.com. (2026). *Perplexity's 'teammates' are the company's AI agents for daily work tasks*. [https://www.engadget.com/2308870/perplexity-teammates-ai-agents-for-ongoing-work/](https://www.engadget.com/2308870/perplexity-teammates-ai-agents-for-ongoing-work/)

[26] fourweekmba.com. (2026). *Perplexity Launches Teammates for $167-a-Month Max Users*. [https://fourweekmba.com/ai-perplexity-launches-teammates-for-167-a-month-max-users/](https://fourweekmba.com/ai-perplexity-launches-teammates-for-167-a-month-max-users/)

[27] perplexity.ai. (2026). *Improvements to every Agent API effort level*. [https://www.perplexity.ai/hub/blog/improvements-to-every-agent-api-effort-level](https://www.perplexity.ai/hub/blog/improvements-to-every-agent-api-effort-level)

[28] unite.ai. (2026). *Perplexity Cuts Agent API Research Costs and Adds Ultra Effort*. [https://www.unite.ai/perplexity-cuts-agent-api-research-costs-and-adds-ultra-effort/](https://www.unite.ai/perplexity-cuts-agent-api-research-costs-and-adds-ultra-effort/)

[29] pressnewsagency.org. (2026). *Perplexity Teammates: How the $200 AI Agents Work*. [https://pressnewsagency.org/perplexity-teammates-how-the-200-ai-agents-work-techrepublic/](https://pressnewsagency.org/perplexity-teammates-how-the-200-ai-agents-work-techrepublic/)

[30] forum.cursor.com. (2026). *Grok Bot: box browser can't open any site — ERR_TUNNEL_CONNECTION_FAILED*. [https://forum.cursor.com/t/grok-bot-box-browser-cant-open-any-site-err-tunnel-connection-failed-egress-proxy-127-0-0-1-8791-down/177505](https://forum.cursor.com/t/grok-bot-box-browser-cant-open-any-site-err-tunnel-connection-failed-egress-proxy-127-0-0-1-8791-down/177505)