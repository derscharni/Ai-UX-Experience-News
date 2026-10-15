# UX Briefing: The Live Canvas, Voice Identity, and the Composable Workspace Sprint

**October 15, 2026**

Good morning. The 48 hours ending October 15, 2026 are defined by a convergence of three distinct forces: platforms are expanding the Claude/artifact canvas from static documents into live, connected data workspaces; xAI is making its most consequential voice-agent interaction statement of the year with Grok Voice 3.0 shipping on October 14; and Microsoft is completing a two-month Copilot surface consolidation — pushing Copilot in SharePoint and OneDrive to general availability, redesigning Teams and Outlook's Copilot chat interface to match the unified Copilot app, and introducing suggestion chips and quick-access skill triggers in SharePoint's chat surface. **Claude/Anthropic** delivers its most significant generative-UI expansion since the Artifacts launch: **Claude Dashboards and Claude Motion enter beta on October 8**, converting the Claude canvas from a document-and-slide generator into a live data visualisation and code-driven animation environment, while **Docs, Slides, and Design simultaneously exit beta and become available on every plan including Free** — with the Enterprise CMEK and admin template controls turning on by default today, October 15. **Grok (xAI)** ships **Grok Voice 3.0 on October 14**, a speech-to-speech model that already handles millions of daily conversations inside Tesla vehicles, arrives in the API at the same price as Voice 2.0, and introduces MCP tool calling and function calling natively inside voice sessions. **Microsoft Copilot** completes its September/October surface consolidation: **Copilot in SharePoint reaches GA**, the **Copilot Chat interface in Teams and Outlook is redesigned to match the unified Copilot app**, and the **Copilot Notebooks October update ships a UX refresh**, proactive artifact suggestion, and expanded reference types — with Office file editing and scheduled automations confirmed for Frontier. **Google Gemini** continues advancing its Antigravity enterprise governance layer, with **Antigravity v2.23.0 adding a permissions picker, full-screen media viewer, and ZIP/folder attachments** — and October 13 enabling **Gemini 4 Argon by default for licensed Antigravity users in Gemini Enterprise** — while the Workspace Skills rollout delay continues without a new date. **ChatGPT/OpenAI** consolidates its October agentic stack, with the **GPT-6.1 Sol Ultrafast mode rolling out in the API, Codex, and ChatGPT Work**, while Dots' mobile creation, Codex delegation, and Scheduled Tasks editing continue to broaden the ambient-agent surface. **Perplexity** ships the **pplx-embed-v2-late multimodal embedding models** — open-weight 0.6B and 9B late-interaction models that handle text, images, and PDFs without OCR — extending the retrieval architecture underlying Computer and Comet into a developer-available open-weight form.

---

## At a Glance: October 15 Highlights

Today's releases converge on the platform layer's next inflection: the AI canvas is becoming a live, connected workspace that pulls from live data, voice infrastructure is acquiring agentic tool-calling capability at production scale, and enterprise governance is being wired into every new surface before that surface ships rather than after.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Dashboards and Claude Motion enter beta October 8; Docs, Slides, and Design go free; Enterprise artifact controls activate today** — Dashboards connects to BigQuery, Databricks, Snowflake, or Salesforce and builds live query-backed charts; Motion writes editable code animations that export to MP4; Docs/Slides/Design GA on all plans including Free; Artifacts now support CMEK; Enterprise template defaults activate October 15. [1][2][3] |
| **ChatGPT** | **GPT-6.1 Sol Ultrafast rolls out in API, Codex, and ChatGPT Work; Dots mobile creation, Codex delegation, and Scheduled Tasks editing consolidate** — Ultrafast delivers near-Astra intelligence at up to 8x Sol Standard speed; GPT-6.1 Sol is now the default in bundled and Amazon Bedrock catalogs; Dots draw on ChatGPT conversations, Codex threads, and automations; mobile Dot creation live on iOS and Android. [4][5][6] |
| **Google Gemini** | **Antigravity v2.23.0 ships permissions picker and full-screen media; Gemini 4 Argon enabled by default for licensed Antigravity Enterprise users October 13; Workspace Skills delay continues indefinitely** — v2.23.0 adds permissions picker to the message box, full-screen image/video viewer, ZIP and folder attachments; Claude Opus 5.5 and Sonnet 5.5 added to Antigravity AI developer tools in-console October 8; Skills Workspace rollout still on hold, November 17 Gems milestone unchanged. [7][8][9] |
| **Microsoft Copilot** | **Copilot in SharePoint and OneDrive reaches GA; Copilot Chat redesigned in Teams and Outlook; Notebooks UX refresh ships in Frontier** — SharePoint GA adds image generation, site analytics, and automatic document metadata; Teams Copilot chat removes the chat-list entry point and unifies behind left-nav with Chat/Cowork/Work IQ toggle; Notebooks ships grouping/reordering UX and proactive artifact suggestion; Office file editing and scheduled automations rolling out in Frontier. [10][11][12] |
| **Grok (xAI)** | **Grok Voice 3.0 ships October 14 with MCP tool calling, sub-one-second latency, and automatic alias upgrade for grok-voice-latest users** — handles millions of daily Tesla and Starlink conversations; supports Connectors for calendar and email, and Grok Bot for agentic tasks hands-free in-vehicle; grok-voice-2.0 deprecated same day; pricing unchanged at $0.08/min. [13][14][15] |
| **Perplexity** | **pplx-embed-v2-late open-weight multimodal embedding models ship on Hugging Face October 7; older OpenAI model IDs retire October 24 from Agent and Router APIs** — 0.6B and 9B late-interaction models search text, images, and PDFs without OCR; 9B corpus searchable by 0.6B query model at no additional cost; openai/gpt-5.4 through gpt-5 retire October 24 from Agent/Router APIs. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Live Canvas and the GA Generative Workspace

Anthropic's most consequential generative-UI event of the last 48 hours — and arguably of Q4 2026 — is the **Claude Dashboards and Claude Motion beta launch on October 8**, a paired release that collectively converts the Claude artifact canvas from a document-generation surface into a live, connected, animated data workspace. The interaction-design significance is structural: for the first time, an artifact created inside a Claude conversation can represent *current* external state rather than a point-in-time synthesis.



Starting today, Claude can turn your data into a dashboard that stays current, and your ideas into an animated explainer for your next presentation; Claude Dashboards connects to a data platform like BigQuery, Databricks or Snowflake, or a CRM tool like Salesforce, and is in beta on paid plans.

 The UX shift this establishes is from *document* to *instrument*: a Claude Dashboard is not a static chart that reflects data at query time — it is a panel that updates as the underlying data platform updates, converting the conversation from a place where insights are generated to a place where live operational intelligence lives. 

The common thread is inspectability: each chart shows the query behind it, and each animation is built as code you can edit.

 That audit-trail design — every chart revealing the SQL or query that produced it — is the correct trust-design primitive for a live data workspace. Enterprise users reviewing a dashboard can validate its logic without leaving Claude, preventing the opacity problem that has made embedded analytics tools difficult to audit.

**Claude Motion** is the generative-UI advance that deserves separate analysis. 

Motion converts reports, charts, and product walkthroughs into short animated explainers; Claude writes editable code for the text, shapes, images, charts, and timing instead of using a video-generation model, so there is no generated footage or AI-generated people; users can revise the result in the editor or through a prompt, download an MP4, or continue in supported creative tools.

 The no-video-model architecture is the design decision that makes Motion viable for enterprise use: because the output is code rather than generated footage, every frame, word, and timing decision is inspectable and editable by the same Claude conversation that produced it. There is no generative-video black box; the animation is a deterministic artifact with a traceable production history.

The simultaneous GA of Docs, Slides, and Design completes the artifact ecosystem's maturation. 

Docs, Slides, and Design are out of beta and on every Claude plan, including Free.

 Today, October 15, is also a significant enterprise governance date: 

Artifacts now support CMEK, and admins choose which artifact templates their organization uses; Docs, Slides, and Design turn on by default October 15, or you can turn them on today.

 The CMEK support is the enterprise-deployment primitive that closes the data-residency gap that had kept regulated-industry teams from adopting artifact workflows: organisations can now have Claude generate and store artifacts under their own encryption keys, bringing artifact data under the same key-management governance as the rest of their cloud data estate.

---

### ChatGPT / OpenAI: Ultrafast Mode and the Dots Delegation Stack Matures

OpenAI's most UX-significant delivery in this window is the **GPT-6.1 Sol Ultrafast rollout**, which extends the coordination model's speed ceiling in precisely the context where latency matters most: developer pipelines, agentic Codex sessions, and ChatGPT Work automations where a slow model-turn blocks downstream tasks from proceeding.



Ultrafast is rolling out today for GPT-6.1 Sol in the API, Codex, and ChatGPT Work, delivering near-Astra intelligence at up to 8x the speed of Sol Standard.

 The UX significance of this speed ceiling expansion is not just response time — it is the interaction pattern change that Ultrafast enables in multi-step agentic workflows: when the coordinating model responds in a fraction of its previous latency, the compounding delay across a ten-step pipeline is not linear but multiplicative. A pipeline that previously took ninety seconds can now complete in a fundamentally different timescale that changes what "background task" means for the user. 

GPT-6.1 Sol is now the default model in the bundled and Amazon Bedrock catalogs.



The **Dots ambient-agent surface** continues its footprint expansion in this window. 

You can now create your Dot straight from your phone in the ChatGPT app on iOS and Android; delegate work in Codex to your Dot; your Dot can now start work in Codex and follow up on existing threads, drawing on your ChatGPT conversations, Codex threads, and automations.

 The Codex delegation loop is the interaction-design advance that converts Dots from a goal-tracking surface into an active orchestrator of multi-step coding work: the Dot does not just remember a goal — it can initiate and continue Codex sessions on the user's behalf, reducing the user's role in a complex engineering delegation from "initiate and monitor" to "review and approve." 

Your Dot can also review and edit Scheduled Tasks in ChatGPT Work; ask what's scheduled or update a recurring task as plans change.

 The Scheduled Tasks editing capability closes a critical delegation loop: a user who delegated a recurring automation to a Dot previously had to navigate to a separate task management surface to modify it — Dots now surfaces that control inline, keeping modification in the same conversational context where the goal was defined.

---

### Google Gemini: Antigravity Governance, Enterprise Model Controls, and the Persistent Workspace Skills Gap

Google's most significant Gemini interaction-design advances in this window cluster around the **Antigravity enterprise governance layer**, which continues to mature with a dense cluster of permission, media, and attachment capabilities in **v2.23.0**, while the Workspace Skills delay creates an ongoing configuration vacuum for enterprise practitioners that is now in its third day without a confirmed resolution timeline.



Antigravity v2.23.0 adds a permissions picker to the message box, opens images and videos in a full-screen viewer, and lets you attach .zip archives and folders; onboarding now shows what Antigravity can do instead of asking you to pick a theme.

 The permissions picker in the message box is the trust-design advance that matters most here: previously, Antigravity's permission grants were handled at the session or configuration level, meaning a user composing a prompt had no inline visibility into what the agent was currently authorised to do before submitting. Surfacing the permissions picker at the message-composition level converts permission awareness from a settings-menu concern into an ambient, per-prompt decision — the correct design for an agent with file access, terminal execution, and MCP tool calling.

On the enterprise admin surface, 

as of October 13, 2026, AI developer tools are enabled by default for licensed users when Antigravity authorized models uses the default selection; if your organization specifies a custom model list, an administrator must manually select Gemini 4 Argon.

 The default-on posture for Gemini 4 Argon is a meaningful enterprise deployment signal: Google is treating its latest developer-tool model as the expected baseline for Antigravity Enterprise environments, requiring explicit opt-out rather than explicit opt-in. For organisations with custom model lists — where security or compliance teams have already curated the authorised model set — 

administrators can also enable Anthropic Claude Opus 5.5 and Claude Sonnet 5.5 for AI developer tools including Antigravity 2.0, Antigravity CLI, and Antigravity for IDEs, with an in-console Terms of Service consent flow letting administrators opt in directly in the Gemini Enterprise Settings without a separate Anthropic account or onboarding.

 The in-console consent flow without a separate Anthropic account is the enterprise-UX simplification that removes a significant adoption barrier: IT administrators previously had to manage two separate vendor relationships to use Claude models in Antigravity, creating a documentation and legal-review overhead that slowed rollout.

The **Workspace Skills delay** continues without a confirmed new timeline. The composable-persona authoring transition — in which Gem creation ended for Rapid Release users October 13 while Skills remain unavailable in Workspace surfaces — means enterprise Workspace teams are in a period where they cannot create new Gems and cannot yet deploy Skills in Docs, Gmail, or Sheets. 

November 17, 2026 remains the date when Gems move to the Settings panel of the Gemini app, where users can continue to create, edit, and use them.

 Enterprise practitioners should treat this as the working deadline: any configuration work that requires Skills in Workspace cannot be validated until Google confirms a new Workspace rollout date.

---

### Microsoft Copilot: SharePoint GA, the Unified Chat Surface, and Notebooks as a Proactive Workspace

Microsoft's most structurally significant Copilot interaction-design events materialising in this window are a cluster of three related surface consolidations: **Copilot in SharePoint reaching general availability**, the **Copilot Chat interface in Teams and Outlook being redesigned to match the unified Copilot app**, and the **Copilot Notebooks October UX refresh** shipping in Frontier — together comprising the clearest statement yet of Microsoft's agent-surface architecture: one coherent Copilot experience across every surface, with agents and skills discoverable from a single unified interaction layer.



Copilot in SharePoint is now generally available, with features including image generation and editing, site analytics reports, and automatic filling of document metadata.

 The metadata auto-fill is the agentic-workflow capability that matters most for regulated-industry document management: SharePoint libraries that previously relied on manual tagging to make documents discoverable and compliant can now have Copilot apply the correct labels and tags automatically at upload, converting document governance from a user-compliance problem into an agent-managed background task. 

This month also added suggestion chips — after Copilot responds, contextual follow-ups appear right under the answer to help refine the result, dig deeper, or take the next action — and a quick access option for skills, similar to the way you access files, people, and meetings, so you can discover and add the right skill when you need it.



The **Copilot Chat redesign in Teams and Outlook** is the surface-unification event that most directly affects daily interaction patterns for knowledge workers. 

Two updates are rolling out in Teams right now: the Copilot option in the Teams chat list is being removed, intentionally leaving one central place — the left-side navigation — to get to the full Copilot Chat experience.

That experience is getting a new interface that matches the full Copilot Chat interface, with the ability to switch between Chat and Cowork, toggle Work IQ on or off, see pinned agents or open all agents, and find chat history on the left.

 The removal of the chat-list Copilot entry point is the correct consolidation design: the previous dual-entry pattern — Copilot accessible from both the chat list and left-nav — created navigation ambiguity about which Copilot surface had which capabilities, a common source of enterprise user confusion.

The **Copilot Notebooks October 2026 update** advances the workspace toward proactive artifact generation. 

The new UX update brings a refreshed experience to the Microsoft Copilot app and OneNote to help keep notebooks organised and easy to use by grouping and reordering content and artifacts from the navigation pane.

Copilot can also suggest artifacts for your project, proactively recommending relevant Word, Excel, or PowerPoint files based on WorkIQ and your notebook content, then lets you quickly generate them.

 The proactive artifact suggestion is the design move that shifts Notebooks from a *reactive reference container* — where the user asks Copilot questions about stored content — to a *proactive work initiator* that recognises what outputs the project needs and surfaces them before the user explicitly asks. 

Task delegation, scheduled briefings, in-notebook Office editing, interactive reports, and a choice between OpenAI and Anthropic models are all described as rolling out through Microsoft's Frontier preview program in phases, not as a finished release available to every Notebooks user today.



---

### Grok (xAI): Voice 3.0 and the Agentic Voice Identity Leap

xAI's most consequential interaction-design event of this entire window — and arguably the most significant voice-agent UX event in the category so far in October — is **Grok Voice 3.0 shipping on October 14**: a speech-to-speech model release that is not merely a quality upgrade but an architectural expansion of what voice sessions can do, converting Grok's voice surface from a conversation interface into a full agentic runtime.



Grok Voice 3.0 is the world's most intelligent speech-to-speech model; it sets a new record for resolving customer support calls, has class-leading latency at under one second, and costs less than other frontier models; Grok Voice powers millions of conversations a day across Tesla and SpaceX, and is available today in the API at the same price as its predecessor.

 The pricing-unchanged decision is the adoption-design choice that matters most here: xAI has made the capability upgrade zero-friction for developers already running Voice 2.0 integrations. 

Agents configured to use grok-voice-latest have already received the upgrade automatically, without developers needing to make changes.

 The automatic alias upgrade is the correct design for a production voice agent ecosystem: requiring developers to explicitly update model strings to receive improvements creates adoption lag that means enterprise deployments stay on older capability floors.

The agentic-runtime advance is the UX dimension that sets Voice 3.0 apart from prior voice model upgrades. 

Voice 3.0 is a model called over a WebSocket at the speech-to-speech docs endpoint, and functions as an agent runtime because it can search uploaded documents, call your own functions, or reach an MCP server during the call.

 MCP tool calling inside a voice session is the interaction-pattern primitive that converts a voice interface from a conversational channel into a full agentic delegation surface: a user can now speak a goal to Grok Voice and have the voice agent invoke tools, read data, and return structured results — all within the same sub-second-latency voice exchange. 

xAI says Grok Voice 3.0 handles millions of daily conversations inside Tesla vehicles and supplies the voice mode for Grok Bot; drivers can use Connectors to check calendars or answer email, while Grok Bot can handle requests such as dinner reservations.

 The in-vehicle deployment at scale — where the interaction constraint of hands-free and eyes-free is absolute — makes Tesla the highest-stakes proving ground for voice-agent UX in the category, and Grok Voice 3.0's production tenure there is the trust signal that enterprise voice-agent deployments have been waiting for.

---

### Perplexity: Multimodal Retrieval Infrastructure and the Model Retirement Clock

Perplexity's most developer-significant release in this window is the **pplx-embed-v2-late multimodal embedding models**, shipping open-weight on Hugging Face on October 7 — a retrieval architecture advance that extends the search infrastructure underlying Computer and Comet into a developer-available form without an API dependency, and an important signal about the direction of Perplexity's open-weight strategy.



Perplexity AI has released two new embedding models that read pages more like people do — words, pictures, tables and all; the models, called pplx-embed-v2-late, come in 0.6B and 9B parameter versions and are now publicly available on Hugging Face.

 The late-interaction architecture is the retrieval-UX advance that matters here: rather than compressing a document into a single embedding vector, late-interaction models preserve token-level representations that enable more precise relevance matching for complex queries. 

A corpus indexed with the larger 9B model can be searched using the lightweight 0.6B model, with testing showing this cross-model querying worked efficiently at no additional cost.

 The cross-model querying pattern — index at 9B quality, search at 0.6B cost — is the deployment design that makes large-scale document corpora economically viable for enterprise RAG pipelines: organisations can index their full document estate once at high fidelity, then run continuous searches against it at lightweight cost.

The trust-design event that enterprise practitioners must act on before October 24 is the **Perplexity Agent and Router API model retirement**. 

On October 24, 2026 at 00:00 UTC, the Agent API and Router API will retire model IDs including openai/gpt-5.4, openai/gpt-5.4-mini, openai/gpt-5.4-nano, openai/gpt-5.2, openai/gpt-5.1, openai/gpt-5, and openai/gpt-5-mini.

 Any Perplexity Computer Automations, Agent API workflows, or Router configurations that reference these model strings will fail after October 24 — a hard deadline that sits nine days from today and requires explicit migration to currently supported model IDs. The UX significance of this retirement event is the same as GPT-5.5's retirement in ChatGPT last week: automated workflows and Automations tuned to specific model output patterns will now inherit different behaviour from their replacement models, requiring review of any output-format assumptions baked into downstream parsing logic.

---

## The Bigger Picture: The Live Canvas, Voice Identity, and the Composable Workspace Sprint

The 48 hours ending October 15, 2026 reveal a category where the generative-UI layer is undergoing its most consequential architectural evolution since the shift from chat-only to multimodal: platforms are not merely adding features to existing canvases — they are changing what the canvas fundamentally *is*. Anthropic's Claude Dashboards and Motion launch is the clearest statement of this: a dashboard that stays current as the underlying data changes, and an animation built as inspectable, editable code rather than generated video, are both expressions of the same design philosophy — the artifact should be a living, auditable instrument, not a point-in-time snapshot. The CMEK support and admin template controls activating today extend that philosophy into the enterprise governance layer: the canvas is now manageable under the same encryption and compliance controls as everything else in the organisation's data estate. Microsoft's SharePoint GA, Teams/Outlook Copilot redesign, and Notebooks UX refresh are the enterprise-surface equivalent of the same transition: Copilot is no longer a feature accessed from multiple inconsistent entry points — it is a unified workspace that surfaces agents, skills, files, and proactive artifact suggestions from a single coherent interaction layer across every surface the knowledge worker touches. Grok Voice 3.0 is the voice-layer statement of this window: MCP tool calling and function calling inside a sub-one-second-latency speech-to-speech session converts voice from a conversation channel into a full agentic runtime, one that has already been proved at millions-of-calls-per-day scale inside Tesla and Starlink. Google Antigravity's permissions picker and Gemini 4 Argon default activation are the enterprise-governance bookends: every new capability that enters the Antigravity surface is now governed by admin controls from day one, not retrofitted afterward. The throughline is the same as last week but sharper: the canvas is going live, the voice surface is going agentic, and the enterprise governance layer is going ambient — the platforms doing all three simultaneously, and doing them with inspectability built in, are the ones building the enterprise trust position that will matter most as agentic workflows move from pilot to production.

---

## References

[1] claude.com. (2026). *Build live dashboards and animate explainers with Claude*. [https://claude.com/resources/articles/dashboards-and-motion](https://claude.com/resources/articles/dashboards-and-motion)

[2] Testingcatalog. (2026). *Claude launches Dashboards and Motion in beta*. [https://www.testingcatalog.com/claude-launches-dashboards-and-motion-in-beta/](https://www.testingcatalog.com/claude-launches-dashboards-and-motion-in-beta/)

[3] Releasebot. (2026). *Claude Updates by Anthropic — October 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[4] Releasebot. (2026). *OpenAI Release Notes — October 2026*. [https://releasebot.io/updates/openai](https://releasebot.io/updates/openai)

[5] learn.chatgpt.com. (2026). *Fresh Dots updates: Create in the mobile app, delegate to Codex*. [https://learn.chatgpt.com/docs/whats-new](https://learn.chatgpt.com/docs/whats-new)

[6] blog.memoryplugin.com. (2026). *ChatGPT New Features October 2026: GPT-6 & Intelligent UI*. [https://blog.memoryplugin.com/chatgpt-new-features-october-2026/](https://blog.memoryplugin.com/chatgpt-new-features-october-2026/)

[7] Releasebot. (2026). *Antigravity Updates by Google — October 2026*. [https://releasebot.io/updates/google/antigravity](https://releasebot.io/updates/google/antigravity)

[8] Google Cloud Documentation. (2026). *Gemini Enterprise release notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[9] Google Workspace Updates. (2026). *Google Workspace Updates: 2026*. [https://workspaceupdates.googleblog.com/2026/](https://workspaceupdates.googleblog.com/2026/)

[10] m365copilotconnection.substack.com. (2026). *Copilot's biggest October 2026 updates, and when they land*. [https://m365copilotconnection.substack.com/p/copilots-biggest-october-2026-updates](https://m365copilotconnection.substack.com/p/copilots-biggest-october-2026-updates)

[11] Microsoft Tech Community. (2026). *What's New in Notebooks | October 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105)

[12] Techcommunity.microsoft.com. (2026). *What's new in Copilot in SharePoint: October 2026*. [https://techcommunity.microsoft.com/blog/spblog/what%E2%80%99s-new-in-copilot-in-sharepoint-october-2026/4535423](https://techcommunity.microsoft.com/blog/spblog/what%E2%80%99s-new-in-copilot-in-sharepoint-october-2026/4535423)

[13] xAI. (2026). *Introducing Grok Voice 3.0*. [https://x.ai/news/grok-voice-3](https://x.ai/news/grok-voice-3)

[14] eesel.ai. (2026). *Grok Voice 3.0: what it is, what changed, and how to use it*. [https://www.eesel.ai/blog/grok-voice-3](https://www.eesel.ai/blog/grok-voice-3)

[15] technobezz.com. (2026). *xAI Launches Grok Voice 3.0 at $0.08 Per Minute*. [https://www.technobezz.com/news/xai-launches-grok-voice-per-minute](https://www.technobezz.com/news/xai-launches-grok-voice-per-minute)

[16] Perplexity API Docs. (2026). *Changelog*. [https://docs.perplexity.ai/docs/resources/changelog](https://docs.perplexity.ai/docs/resources/changelog)

[17] Cryptobriefing. (2026). *Perplexity AI releases pplx-embed-v2-late models for multimodal search*. [https://cryptobriefing.com/perplexity-pplx-embed-v2-late-multimodal-models/](https://cryptobriefing.com/perplexity-pplx-embed-v2-late-multimodal-models/)

[18] Releasebot. (2026). *Perplexity Release Notes — October 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)