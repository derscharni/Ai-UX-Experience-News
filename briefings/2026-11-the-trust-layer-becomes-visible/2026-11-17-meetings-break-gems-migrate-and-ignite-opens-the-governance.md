# UX Briefing: Meetings Break, Gems Migrate, and Ignite Opens the Governance Reckoning

**November 17, 2026**

Good morning. The 48 hours ending November 17, 2026 are defined by four simultaneous design movements: **Anthropic** suffering a second major reliability event in five days — a **Claude Meetings** capacity incident beginning November 16 at 15:10 UTC that prevented Claude from joining new calls, forced Auto-join offline, and exposed the trust gap at the heart of a beta that asks users to consent to AI presence in live video calls, arriving while the platform ships **Claude Code 2.1.326** with the first-ever intersection of Code Mode and agent teams; **Google** executing the most consequential single-day interaction architecture change in its Gemini history on November 17 — **Gems-to-Skills migration** begins today, retiring the side-panel persona system in favour of a slash-command skill invocation pattern while simultaneously completing the GA of **3-legged OAuth for A2A agents** in Gemini Enterprise, making today the day that both Gemini's conversational persona layer and its agent-to-agent identity layer change permanently; **Microsoft Copilot** opening **Ignite 2026** at Chase Center with Satya Nadella's keynote at 10:00 AM PT, with Agent 365 featured as the enterprise observability layer for the entire agentic stack and the Copilot vibe-coding tool, Autopilot GA timing, and a new Azure agent-cost-reduction system all expected to emerge from the conference floor; and **OpenAI**'s **Responses API MCP write-duplication bug** — documented November 15–16 and reaching broad developer attention this window — establishing a reproducible pattern where approved MCP write tool calls execute twice after a programmatic read, breaking idempotency in multi-step agent programs and making the developer community's trust-design challenge concrete and urgent.

---

## At a Glance: November 17 Highlights

Today's window is defined by the industry arriving simultaneously at the persona-deprecation moment, the live-meeting-agent trust moment, and the agentic idempotency moment — Google retiring its Gems persona layer and replacing it with a session-native skill invocation pattern, Anthropic's Claude Meetings failing under demand on only its fifth day of beta rollout, and OpenAI's Responses API surfacing a double-execution bug in approved MCP writes that reveals a structural trust gap in the agentic approval loop, all on the same day Microsoft opens Ignite as the industry's largest single-stage governance-and-agentic-deployment announcement event of the year.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Meetings (beta) experienced a capacity-driven call-join failure beginning November 16 at 15:10 UTC — Claude unable to join new calls, Auto-join paused, manual call-add also affected; Enterprise customers were re-enabled by 02:02 UTC November 17 though join latency remains elevated; Team customer Auto-join remains paused as of this briefing; Claude Code 2.1.326 (November 17) is the first release to allow Code Mode and agent teams to run simultaneously, streams Remote Control replies live to phone or browser, closes a sandboxed-command path to credentials, and strengthens deny-rule enforcement after restart; Claude Meetings was launched on November 12 for Team and Enterprise plans on Google Meet, with an auto-join setting and an external-participant privacy default** — the Meetings capacity incident is the trust-design event of the window: a feature whose consent design relies on the user actively adding Claude to each call, or trusting an auto-join setting, failed under its first real-world demand spike, surfacing the infrastructure fragility that live-meeting AI agents inherit when they scale. [112-1,112-3,112-5,112-6,112-8,9-4,9-7,69-1,69-3,71-1,116-2,116-5,119-7,119-13] |
| **ChatGPT** | **OpenAI's Responses API MCP write-duplication bug (documented November 15–16) produces a reproducible write→read→write execution sequence when an approved native MCP write is followed by a hosted programmatic read in the same response, executing the write action twice; a second related bug documents the Responses API dropping embedded MCP resources and structuredContent from tool results on November 17; the developer community has circulated an idempotency-key pattern as a defensive server-side mitigation; ChatGPT Images 2.6 (November 4, continuing rollout) adds animated GIF creation from text prompts or photos with per-frame editing and speed control across all plans; Business Hub Shopify integration and claim-your-business flows continue active rollout** — the MCP write-duplication bug is the trust-design event of the OpenAI window: in a system built on the principle that approved actions are executed exactly once, a reproducible double-execution breaks the entire consent contract — the user approved one write, two writes happened. [18-1,18-2,94-3,94-5,95-4,95-6,86-3,86-5,86-6,91-5,17-5,17-6] |
| **Google Gemini** | **Gems-to-Skills migration begins November 17 — all custom, premade, and shared Gems start automatic conversion to Skills today; Skills are invoked via slash command in the prompt box rather than opened from a side panel, require Keep Activity to be on, and are limited to users over 18; multiple Gemini API preview model deprecations also execute on November 17 including gemini-3.1-flash-tts-preview, gemini-3.1-flash-live-preview, and gemini-2.5-flash-preview-tts redirecting to current stable equivalents; Gemini Enterprise GA of 3-legged OAuth for A2A agents (November 13) enables agents to act on behalf of the signed-in user with scoped credentials when calling MCP servers, Cloud services, and third-party APIs; Gemini Workspace Skills are rolling out across Workspace Studio and Workspace apps** — the Gems-to-Skills shift is the interaction-pattern change of the window: Gems lived in a side panel requiring navigation; Skills fire from a slash command inside the conversation, making persona invocation ambient and session-native rather than a separate configuration step. [29-1,29-6,29-7,30-10,30-13,30-14,30-15,38-3,32-2,103-1,103-2,106-3] |
| **Microsoft Copilot** | **Microsoft Ignite 2026 opens November 17 at Chase Center with Satya Nadella and Judson Althoff keynoting at 10:00 AM PT; Agent 365 is featured as the observability layer for agents, models, and assistants across the entire tenant, with sessions on governing and securing agents at scale; Copilot vibe-coding tools — allowing Copilot users to build custom apps within Office and share them with colleagues — are expected to be announced or expanded at the conference; a new Azure agent-cost-reduction system is expected from The Information's pre-Ignite reporting; Autopilot, which has been in private preview since late September, has Ignite as its expected major status update venue** — Agent 365's keynote positioning as the tenant-wide observability layer for all agents is the governance-UX signal of the conference opening: Microsoft is framing the enterprise administrator's view of AI agent activity as a first-class product surface, not an audit afterthought. [125-1,125-2,125-3,125-4,129-3,129-4,129-6,124-6,122-6,122-7,126-7,126-8,43-7,43-8] |
| **Grok (xAI)** | **Grok Build 1.0.75 (most recent in the November window) adds clearer permission warnings, smoother prompt and session controls, stop buttons in the dock that halt a background run while its approval card is open, and fixes for rendering and configuration behaviour; Grok Bot 0.78.1 is the latest tracked version; as of November 16, xAI's release notes contained no Grok 4.8 entry and no confirmed start to the promised soft-rollout to Bot users per multiple trackers; Grok all systems operational as of 04:33 UTC November 17 per status.x.ai; a minor Grok user-reported outage spiked on DownDetector at 10:03 PM Eastern on November 16** — the Grok Build stop-button-during-approval-card fix is the micro-trust-design advance of the xAI window: the ability to halt a background run while its approval card is open means users are not trapped in a consent gate where cancellation was impossible; previously, stopping required answering the card first. [53-4,53-5,56-4,56-5,50-1,50-9,55-1,55-2] |
| **Perplexity** | **Perplexity's Monitor API (shipped November 16) enables developers to watch a topic or page via webhook and receive a notification when something relevant changes — a background monitoring primitive that complements Teammates' foreground work-delegation model; Computer runs fully locally on supported Macs as of November 2026; Teammates continue expanding on web, iOS, and Mac for Max subscribers ($200/month), with each Teammate carrying isolated desktop, browser session, and local cookies, and the ability to spawn parallel sub-agents; Perplexity announced a $1B annual revenue run rate on November 16 per CEO Aravind Srinivas at a live event** — the Monitor API is the temporal-UX infrastructure advance of the Perplexity window: it creates the missing signal layer that allows Teammates to operate reactively rather than on polling schedules, enabling an agent to begin work precisely when a watched condition changes rather than on a fixed timer. [61-1,76-1,76-11,76-12,77-8,78-6,78-9,78-13,78-14,79-5,79-8] |

---

## Product Highlights

### Claude / Anthropic: When Meetings Break — The Live-Agent Consent Design Under Pressure

Anthropic's most consequential interaction-design event in this 48-hour window is not a new surface but a demand-driven failure of its newest one: the **Claude Meetings** capacity incident beginning November 16 at 15:10 UTC — the fifth day of the beta's rolling rollout — which prevented Claude from joining new calls, forced Auto-join offline, and remained unresolved into November 17.



Claude Meetings (beta) saw higher than expected demand, and Claude was unable to join many calls; mitigations were put in place and Claude Meetings was re-enabled for Enterprise customers, though Claude may take longer than usual to join; adding Claude to new calls and Auto-join remain paused for Team customers; and as of 02:02 UTC on November 17, Claude may still be unable to join some calls, with Auto-join still paused.

 The trust-design tension is structural rather than merely operational: Claude Meetings was designed around two consent mechanisms. 

By default, Claude does not join calls that include someone from outside the organisation, and it leaves if an outside participant joins after the meeting has started — an administrator can allow Claude to remain on calls with external guests; and Anthropic says users should ensure that everyone on a call is comfortable being transcribed before Claude is added or set to join automatically.

 Both mechanisms — the external-participant default and the consent-before-auto-join requirement — depend on the platform's ability to reliably execute them. When Auto-join fails under demand, it is not just a reliability issue; it is a consent-design failure, because users who configured Auto-join to trust the platform to manage their meeting consent on their behalf discovered that the trust infrastructure they relied on was unavailable.

The capacity failure also reveals the architecture of Claude Meetings' feature scope. 

The beta expands Claude into live collaboration, giving Team and Enterprise customers notes, transcripts and action items from Google Meet calls at no extra charge.

Organisations on HIPAA or customer-managed encryption cannot use it yet; and because Claude stays out of calls with external people by default, client calls are off the table until an admin changes the setting.

 This design — conservative external-participant defaults, HIPAA exclusion in beta — reflects careful trust-design intent. The demand surge reveals that the rollout assumptions built into the beta's capacity provisioning underestimated actual adoption, and that the gap between intent and execution is a live enterprise trust signal arriving in a week when Anthropic is simultaneously managing its IPO roadshow.

**Claude Code 2.1.326**, shipped November 17, is the agentic coding advance of the window. 

Claude Code 2.1.326 adds Code Mode support for agent teams and delivers stronger sandbox protections, faster responses, and Remote Control streaming; it adds support for turning on Code Mode while agent teams are enabled, with sessions with teams on now starting in Code Mode if already turned on.

Remote Control replies now stream to your phone or browser live as they are written, Code Mode now works with agent teams, and Claude can no longer write to Claude Code's sign-in files like .credentials.json.

 The credential-write restriction is the trust-design substrate of this release: Code Mode running inside an agent team now cannot reach back to modify the sign-in files that authenticate the session, closing a path through which a compromised script inside a Code Mode run could have extended its own access.

---

### Google Gemini: Gems Die, Skills Are Born, and A2A Gets a Delegated Identity

Google's most consequential interaction-design event in this 48-hour window is the execution of the **Gems-to-Skills migration** beginning today — a permanent change to how personalised Gemini configurations are stored, surfaced, and invoked that retires two years of the Gems side-panel architecture in favour of a slash-command skill invocation pattern embedded directly in the conversation prompt box.



Gems will start migrating to skills on November 17, 2026; from this date, custom, premade and shared Gems will be converted to skills automatically; and according to Google, skills require the Keep Activity setting and are limited to users over 18.

 The interaction-architecture shift is from navigation to invocation: 

accessing a saved Gem required opening the side panel in Gemini, locating the Gems manager, and selecting the correct configuration; Skills work differently — users type a slash in the prompt box, and the skill activates directly inside the conversation.

 This is a consequential UX direction change: Gems lived outside the conversation flow, requiring the user to leave the prompt context, navigate a manager, and select a configuration before returning to the prompt. Skills collapse that into a single slash-triggered action within the conversation. The keep-activity dependency is the trust-design tension: 

if you turned Keep Activity off for privacy reasons, check before November 17 whether you will be able to use your converted skills at all.

 Users who disabled Keep Activity for privacy reasons — a legitimate and documented choice — may discover today that their converted skills are inaccessible, with no Skills alternative that preserves their prior privacy posture.

Simultaneously, Google is executing multiple **Gemini API model deprecations** today, redirecting several preview model IDs to current stable equivalents. 

Multiple preview models shut down on November 17, 2026, including gemini-3.1-flash-tts-preview (redirecting to gemini-3.8-flash-tts or gemini-3.8-flash-lite-tts), gemini-3.1-flash-live-preview (redirecting to gemini-3.8-live), and gemini-2.5-flash-preview-tts (redirecting to gemini-3.8-flash-tts or gemini-3.8-flash-lite-tts).

 These are hard shutdowns, not silent redirects — the endpoint goes dark. For developers who deferred migration planning, today's model deprecations are a trust-design event that makes the failure mode visible immediately in production.

The enterprise-tier trust-design advance of this window is the GA of **3-legged OAuth for A2A agents** in Gemini Enterprise. 

Support for 3-legged OAuth authentication with the Agent Identity auth manager for Agent2Agent agents is generally available, enabling configuration of 3-legged OAuth with Agent Identity auth manager for A2A agents and authentication using the auth manager.

When an agent acts on behalf of a specific user — for example, to access a user's Jira tasks or GitHub repositories — the platform uses an OAuth 2.0 three-legged auth provider in the Agent Identity auth manager to manage user consent and tokens.

 This is the identity architecture that makes agent-to-agent delegation safe at enterprise scale: rather than an A2A agent operating under its own identity when calling downstream tools, it now carries the delegated identity of the human user who initiated the work, making the agent's downstream API calls attributable to a specific consenting person with scoped credentials.

---

### Microsoft Copilot: Ignite Opens, Agent 365 Steps Up as the Enterprise Governance Layer

Microsoft's most significant interaction-design and enterprise-governance event of this window is not a released feature but the opening of **Ignite 2026** at Chase Center — the moment when Copilot's most consequential agentic surfaces transition from "announced and upcoming" to "GA or expanded" in front of Microsoft's largest enterprise IT audience of the year.



Microsoft's keynote on November 17 at 10:00 AM PT features Agent 365 as the observability layer for agents, models and assistants; and a session at 2:00–2:15 PM on how Microsoft uses Agent 365 to observe, govern, and secure agents at scale is part of the program.

 The governance-UX signal of Agent 365's keynote positioning is significant: rather than presenting enterprise governance as a constraint on agent capability, Microsoft is positioning it as the central navigation surface of the agentic estate — the tool administrators use to see what every agent is doing across the tenant. 

Live sessions at Ignite through Thursday cover Agent 365 topics including "Bringing agentic defense to secure your agents" and "Agent 365: A year of learning, a future of opportunity," plus a discussion on why FinOps is becoming a core discipline for AI at scale.



The Copilot capability expected to receive its first GA or expanded-preview announcement at Ignite is the **vibe-coding tool** in the Copilot Code tab. 

The Information reported Microsoft will unveil a new Azure system designed to reduce costs for customers running AI agents, and also plans to add features to Copilot that could increase corporate spending, including the vibe-coding tool previewed in September.

Using the vibe-coding tool, Copilot users can build custom apps within Office and share them with colleagues.

 The interaction-design significance of vibe coding landing in a Microsoft Office context is different from its landing in a standalone IDE: when a user's custom app is built inside Office, shared through Copilot Managed Runtime, and accessed through corporate identity, the entire lifecycle of a user-built application becomes an enterprise-governed artefact — a consequential shift from ad-hoc automation scripts to governed, attributable applications.

**Autopilot** remains the most watched Ignite announcement. 

Autopilot is the heir to Scout, the always-on agent Microsoft introduced on June 2, 2026; it runs inside the customer's Microsoft 365 tenant with its own identity managed by Entra, plus a memory and an email address.

Autopilot is a persistent, proactive and personal agent that keeps working even when the user is not present; Home and Code started rolling out in the Frontier programme, and Autopilot is expanding to private preview at the end of the month.

 The governance design detail that matters most for enterprise deployment — how Autopilot's Entra identity is scoped, how its actions are logged in Agent 365, and whether spending thresholds ship alongside capability — is the question today's keynote is expected to begin answering.

---

### OpenAI / ChatGPT: The MCP Write-Duplication Bug and the Approval Loop Integrity Problem

OpenAI's most significant trust-design event reaching broad developer attention in this window is not a new feature but a reproducible API behaviour: the **Responses API MCP write-duplication bug**, documented on November 15–16 and reaching developer community attention on November 16–17, which establishes that an approved MCP write tool call can execute twice when the same response continues with a hosted programmatic read.



A developer community bug report from November 16 documents a reproducible behaviour where an approved, native MCP write sometimes executes twice when the same response continues with a hosted programmatic read; builders that rely on in-response approval flows and MCP writes — for example creating database records, publishing content, or triggering external state changes — can observe duplicate side-effects that break idempotency and data integrity, with that risk increasing for long, multi-step agent programs that mix approval resumption and hosted programmatic continuations.

The actual observed sequence is write → read → write.

 The trust-design failure is precise: an approval flow is designed to give the user one approval for one action. A write→read→write execution means the user's single approval gate was breached — the agent completed the write, read a result, and then re-executed the write without a second approval. For applications like CRM updates, invoice creation, or content publication — the classes of write action that have been the focus of recent agentic trust design — this is not a cosmetic bug but a consent-contract violation.

A second related bug was filed November 17: 

the Responses API drops embedded MCP resources and structuredContent from tool results, observed on 17 November 2026.

 And a third: 

the Responses API ignores replayed mcp_call input items unless they reference a stored response, so in a multi-step agent loop the model never sees an earlier MCP result and either invents values from that result or calls the tool again; an inline mcp_call costs exactly as many input tokens as no item at all, so it is dropped before the prompt is built.

 Together, these three bugs constitute a cluster around MCP protocol handling in multi-step agent loops — the precise interaction pattern that agentic commerce, write actions, and automation workflows depend on. The developer community response has been to recommend defensive server-side idempotency keys as a workaround, which is correct practice but should not substitute for a platform-level fix.

The **ChatGPT Images 2.6** rollout (November 4, continuing this window) is the generative-UX advance of the OpenAI window. 

OpenAI released Images 2.6 with animated GIF output and stored reference pictures for ChatGPT users; a text prompt or still photo can now become a looping animation; and users can change how quickly the GIF plays, tweak frames one by one and post the finished clip to cycle endlessly.

OpenAI says the update is available on every plan, including the free tier.

 The frame-by-frame editing model is the interaction-pattern advance: rather than generating an animation and accepting or discarding it, users can inspect and modify individual frames within the same conversation, making animated content creation a conversational refinement loop rather than a generate-and-redo cycle.

---

### Perplexity: The Monitor API and the Reactive-Agent Primitive

Perplexity's most significant interaction-design and agentic-infrastructure advance reaching active attention in this window is the **Monitor API**, shipped November 16, which establishes a webhook-based change-notification primitive that enables Teammates and developer-built agents to begin work reactively when a watched condition changes rather than operating on polling schedules.



On November 16, Perplexity shipped the Monitor API alongside Computer getting Teammates; the Monitor API lets a developer watch a topic or page and get a webhook when something relevant changes.

 The UX implication is architectural: Perplexity's Teammates, as described, are persistent agents capable of monitoring connected tools and responding to changes. Without a push-notification primitive, that monitoring capability defaults to polling — the agent periodically checks whether something has changed. The Monitor API converts that polling loop into an event-driven trigger, meaning Teammates can now be precisely instantiated at the moment a watched condition fires rather than on arbitrary check intervals. 

Teammates can monitor connected tools, respond to changes and ask for user input when needed; each agent operates on its own computer and carries out its assigned task from start to finish before the results are collected and checked; Teammates can connect to services including Slack, GitHub, Linear and Gmail through Perplexity's plugin system; and users can ask a Teammate to connect a service from within chat, approve the requested permissions and then instruct it to monitor channels, repositories or workflows.



The persistence and isolation model of Teammates continues to be the trust-design detail that distinguishes the architecture. 

Teammates inherit the permissions of installed plugins and project settings; saved credentials are encrypted and entered securely, while each Teammate runs on an isolated computer with its own desktop, browser session and local cookies.

A Teammate breaks a large goal into tasks and starts extra agents in parallel, each with its own computer, then checks the results before returning finished work.

 The isolated-computer-per-Teammate design means credential leakage between agents is architecturally prevented rather than policy-restricted — each agent's browser session, local cookies, and credentials belong to that agent's isolated sandbox and cannot be read by a parallel Teammate. The Monitor API and the isolated-compute model together form the two halves of a reactive-agent trust architecture: the Monitor API tells the agent when to start; the isolated sandbox constrains what it can touch when it does.

---

## The Bigger Picture: Meetings Break, Gems Migrate, and Ignite Opens the Governance Reckoning

The 48 hours ending November 17, 2026 crystallise a single macro movement that the entire November cycle has been building toward: **the moment when the agentic platform's trust design is tested not by adversarial attack or deliberate misuse, but by ordinary scale — real-world demand that reveals the gap between the consent architecture as designed and the consent architecture as deployed.** Anthropic's Claude Meetings capacity incident is the clearest demonstration: a feature whose consent design includes external-participant defaults, opt-in auto-join, and consent-before-recording requirements failed on its fifth day of rollout under demand the beta's infrastructure did not anticipate, temporarily removing every consent mechanism the user was relying on. OpenAI's MCP write-duplication bug is a different manifestation of the same principle: an approval flow designed around the assumption that one approval produces one action produced two actions when the execution layer's interaction between approval resumption and hosted reads was not idempotent. Google's Gems-to-Skills migration is the third form: a platform-initiated persona migration that removes user configurations whose privacy dependency — Keep Activity off — was a legitimate and documented choice, leaving those users with no Skills alternative that preserves their prior posture. What connects all three is that the trust failure is not in the stated policy but in the gap between stated policy and runtime behaviour at scale. Microsoft's Ignite opening is the industry's answer to this gap: Agent 365 is positioned at the keynote as the observability layer for the entire tenant-wide agent estate precisely because the industry has learned that governance cannot be retrofitted after agentic deployment — it has to ship as the first-class administrative surface alongside capability. The platforms that will survive enterprise deployment at scale are the ones that understand the gap between trust-as-designed and trust-as-deployed, and that build their monitoring, audit, and idempotency infrastructure before the demand spike arrives, not after.

---

## References

[1] status.claude.com. (2026). *Claude Status — November 16–17, 2026 Incidents*. [https://status.claude.com/](https://status.claude.com/)

[2] getmaxim.ai. (2026). *Is Claude Down? Anthropic API & Platform Status*. [https://www.getmaxim.ai/bifrost/provider-status/anthropic](https://www.getmaxim.ai/bifrost/provider-status/anthropic)

[3] pulsetic.com. (2026). *Is Claude Down? Claude Status & Outage Tracker*. [https://pulsetic.com/status/claude/](https://pulsetic.com/status/claude/)

[4] technobezz.com. (2026). *Claude Unable to Join Meetings*. [https://www.technobezz.com/news/claude-service-incident-d23a8e7e](https://www.technobezz.com/news/claude-service-incident-d23a8e7e)

[5] dev.to. (2026). *Claude Meetings: Claude Joins Your Google Meet Calls in Beta*. [https://dev.to/paullovelace/claude-meetings-claude-joins-your-google-meet-calls-in-beta-48ff](https://dev.to/paullovelace/claude-meetings-claude-joins-your-google-meet-calls-in-beta-48ff)

[6] itbrief.asia. (2026). *Anthropic launches Claude Meetings for live video calls*. [https://itbrief.asia/story/anthropic-launches-claude-meetings-for-live-video-calls](https://itbrief.asia/story/anthropic-launches-claude-meetings-for-live-video-calls)

[7] mayhemcode.com. (2026). *Claude Meetings Explained: Anthropic's AI That Does the Work During Calls*. [https://www.mayhemcode.com/2026/11/claude-meetings-explained-anthropics-ai.html](https://www.mayhemcode.com/2026/11/claude-meetings-explained-anthropics-ai.html)

[8] releasebot.io. (2026). *Claude Code Updates by Anthropic — November 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[9] github.com. (2026). *Release v2.1.326 · anthropics/claude-code*. [https://github.com/anthropics/claude-code/releases/tag/v2.1.326](https://github.com/anthropics/claude-code/releases/tag/v2.1.326)

[10] ai-tldr.dev. (2026). *Claude Code 2.1.326 — Code Mode works with agent teams*. [https://ai-tldr.dev/releases/anthropic-claude-code-2-1-326/](https://ai-tldr.dev/releases/anthropic-claude-code-2-1-326/)

[11] x.com. (2026). *Alex on X: Claude Code 2.1.326 just dropped*. [https://x.com/alexmichael/status/2122453771905085477](https://x.com/alexmichael/status/2122453771905085477)

[12] notebookcheck.net. (2026). *Google Gemini starts turning your Gems into skills on November 17*. [https://www.notebookcheck.net/Google-Gemini-starts-turning-your-Gems-into-skills-on-November-17.1411044.0.html](https://www.notebookcheck.net/Google-Gemini-starts-turning-your-Gems-into-skills-on-November-17.1411044.0.html)

[13] thestreet.com. (2026). *Google is making a change in November that might catch Gemini users off guard*. [https://www.thestreet.com/technology/google-gemini-gems-skills-change-november](https://www.thestreet.com/technology/google-gemini-gems-skills-change-november)

[14] androidauthority.com. (2026). *Google is officially killing Gemini Gems*. [https://www.androidauthority.com/google-sunset-gemini-gems-november-3716162/](https://www.androidauthority.com/google-sunset-gemini-gems-november-3716162/)

[15] ai.google.dev. (2026). *Gemini deprecations — Gemini API — Google AI for Developers*. [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

[16] docs.cloud.google.com. (2026). *Gemini Enterprise release notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[17] releasebot.io. (2026). *Google Release Notes — November 2026*. [https://releasebot.io/updates/google](https://releasebot.io/updates/google)

[18] docs.cloud.google.com. (2026). *Agent Identity overview — Gemini Enterprise Agent Platform*. [https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)

[19] nhimg.org. (2026). *AI Agent Products Release Tracker: Dated and Sourced*. [https://nhimg.org/ai-agent-products-release-tracker](https://nhimg.org/ai-agent-products-release-tracker)

[20] techcommunity.microsoft.com. (2026). *Plugins at Microsoft Ignite 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/plugins-at-microsoft-ignite-2026/4569951](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/plugins-at-microsoft-ignite-2026/4569951)

[21] techcommunity.microsoft.com. (2026). *Microsoft Ignite 2026: Your Guide to Agent 365*. [https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-ignite-2026-your-guide-to-agent-365/4571750](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-ignite-2026-your-guide-to-agent-365/4571750)

[22] pasqualepillitteri.it. (2026). *Microsoft Launches Autopilot, the Copilot Agent That Works on Its Own*. [https://pasqualepillitteri.it/en/news/18368/microsoft-launches-autopilot-copilot-agent](https://pasqualepillitteri.it/en/news/18368/microsoft-launches-autopilot-copilot-agent)

[23] releasebot.io. (2026). *Microsoft Copilot Updates by Microsoft — November 2026*. [https://releasebot.io/updates/microsoft/microsoft-copilot](https://releasebot.io/updates/microsoft/microsoft-copilot)

[24] digitaltoday.co.kr. (2026). *Microsoft to add system to Azure to cut costs for running AI agents*. [https://www.digitaltoday.co.kr/en/view/126435/microsoft-to-add-system-to-azure-to-cut-costs-for-running-ai-agents](https://www.digitaltoday.co.kr/en/view/126435/microsoft-to-add-system-to-azure-to-cut-costs-for-running-ai-agents)

[25] taskade.com. (2026). *Microsoft Copilot History: Clippy, Cortana, Sydney to Agents*. [https://www.taskade.com/blog/microsoft-copilot-history](https://www.taskade.com/blog/microsoft-copilot-history)

[26] community.openai.com. (2026). *Responses API: approved native MCP write executes twice after a programmatic read*. [https://community.openai.com/t/responses-api-approved-native-mcp-write-executes-twice-after-a-programmatic-read/1416736](https://community.openai.com/t/responses-api-approved-native-mcp-write-executes-twice-after-a-programmatic-read/1416736)

[27] community.openai.com. (2026). *Responses API drops embedded MCP resources and structuredContent*. [https://community.openai.com/t/responses-api-drops-embedded-mcp-resources-and-structuredcontent/1417340](https://community.openai.com/t/responses-api-drops-embedded-mcp-resources-and-structuredcontent/1417340)

[28] community.openai.com. (2026). *Responses API ignores replayed mcp_call input items unless they reference a stored response*. [https://community.openai.com/t/responses-api-ignores-replayed-mcp-call-input-items-unless-they-reference-a-stored-response/1417414](https://community.openai.com/t/responses-api-ignores-replayed-mcp-call-input-items-unless-they-reference-a-stored-response/1417414)

[29] aiagentstore.ai. (2026). *AI Agents News — Week of November 17, 2026*. [https://aiagentstore.ai/ai-agent-news/this-week](https://aiagentstore.ai/ai-agent-news/this-week)

[30] betanews.com. (2026). *ChatGPT Images 2.6 adds GIFs and 50% faster image generation*. [https://betanews.com/article/chatgpt-images-gifs-faster-generation/](https://betanews.com/article/chatgpt-images-gifs-faster-generation/)

[31] notebookcheck.net. (2026). *ChatGPT can now make GIFs and save your photos for later chats*. [https://www.notebookcheck.net/ChatGPT-can-now-make-GIFs-and-save-your-photos-for-later-chats.1445192.0.html](https://www.notebookcheck.net/ChatGPT-can-now-make-GIFs-and-save-your-photos-for-later-chats.1445192.0.html)

[32] latent.space. (2026). *Perplexity hits a $1B revenue run rate, up 4x in 2026*. [https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/](https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/)

[33] itbrief.news. (2026). *Perplexity launches Teammates AI agents for Max users*. [https://itbrief.news/story/perplexity-launches-teammates-ai-agents-for-max-users](https://itbrief.news/story/perplexity-launches-teammates-ai-agents-for-max-users)

[34] cellcog.ai. (2026). *Perplexity Teammates: What They Are and How They Compare*. [https://cellcog.ai/blog/perplexity-teammates/](https://cellcog.ai/blog/perplexity-teammates/)

[35] releasebot.io. (2026). *xAI Release Notes — November 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[36] multichats.ai. (2026). *Grok Status — Real-Time Updates*. [https://www.multichats.ai/status/grok-status](https://www.multichats.ai/status/grok-status)

[37] geotoolbox.ai. (2026). *Grok 5: Release Date, Specs & What's Confirmed (November 2026)*. [https://geotoolbox.ai/blog/grok-5](https://geotoolbox.ai/blog/grok-5)