# UX Briefing: Model Upgrades, Generative UI, and the Proactive-Agent Threshold

**September 02, 2026**

Good morning. The 48 hours ending September 2 are defined by a quiet but structurally decisive shift: every major platform simultaneously crossed the line from *reactive agent* — one that waits for a prompt — into *proactive agent* — one that initiates, escalates, or upgrades its own behaviour without a user asking. **Claude/Anthropic** delivers its most consequential agentic-coding upgrade of the September window: **Claude Fable 5.1 becomes the default model in Claude Code**, bringing effort-level session controls, a new `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` environment variable for fleet-wide subagent standardisation, and a new Containment Escape auto-mode rule that blocks cloud metadata credential fetches and cross-tenant network reach from being auto-approved. **ChatGPT/OpenAI** ships three converging UX events that collectively expand the agent's ambient reach: **Live voice surfaces in the iPhone Lock Screen and Dynamic Island** via Live Activities — voice conversations that persist and stay legible while the phone is locked — **Site tools via WebMCP** land in the desktop browser so agents call structured website functions rather than scraping UI, and the **Apple Messages plugin** for Codex and ChatGPT Work on Apple silicon Macs adds read/draft/send access to iMessage, SMS, and RCS, with default send-approval gating. **Google Gemini** advances two distinct agentic UX frontiers simultaneously: the **A2UI (Agent-to-UI) protocol** in Gemini Enterprise reaches a new component catalogue update (v0.9), enabling custom agents to dynamically generate native UI components — forms, pickers, visualisations — inside the Gemini Enterprise chat surface rather than returning text, while **Google Assistant's irreversible Android cutover begins September 4**, putting a deadline on the world's largest forced interaction-model migration. **Microsoft Copilot** enters September with two proactive-design events completing their rollout arcs: **Copilot Notebooks' revamped UX flow** lands with proactive artefact suggestions driven by WorkIQ context, and **proactive push notifications** — "Your Day at a Glance" and "Items waiting for you" — reach general availability on mobile, making Copilot the first major enterprise AI product to push AI-generated organisational summaries to a device lock screen by default. **Grok (xAI)** ships its most interaction-design-significant Grok Build release of the month: **configurable default permission mode** for new interactive sessions lands alongside browsable headless session history and a new auto-mode permission card — a trust-design cluster that fundamentally changes how operators scope what an agentic Grok Build session can do before it starts. And **Perplexity** converts its Bumblebee internal supply-chain scanner — previously used to protect its own Computer and Comet infrastructure — into an open-source trust primitive for the wider agentic developer ecosystem.

---

## At a Glance: September 2 Highlights

Today's releases converge on a single architectural signal: agents are no longer waiting to be invoked — they are initiating, surfacing on lock screens, generating their own UI, and requiring operators to configure their permission posture *before* the session starts rather than after it runs.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Fable 5.1 becomes Claude Code's default Fable model** — 1M context, `/effort` session-level controls, `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` for fleet-wide subagent standardisation, and a new Containment Escape auto-mode rule blocking cloud metadata credential fetches; macOS 12 launch regression fixed; watermark transparency for EU AI Act compliance ships across all post-August 2 models. [1][2][3] |
| **ChatGPT** | **Live voice surfaces on iPhone Lock Screen and Dynamic Island** via Live Activities; **Site tools (WebMCP)** land in desktop browser — agents call structured website functions, address-bar arrow reveals available tool surface; **Apple Messages plugin** for Codex and ChatGPT Work reads/drafts/sends iMessage, SMS, and RCS with default send-approval gate; Computer History expands to EEA, Switzerland, and UK. [4][5][6] |
| **Google Gemini** | **A2UI v0.9 component catalogue update** expands generative UI primitives in Gemini Enterprise — Material 3 styling, reactive validation, new icon/chip properties; **Google Assistant shutdown begins September 4** — irreversible cutover on phones, tablets, Wear OS, and Android Auto with no rollback path; Gemini Chat usage metrics now available in admin dashboards. [7][8][9] |
| **Microsoft Copilot** | **Copilot Notebooks UX revamped** — streamlined navigation flow, proactive artefact suggestions from WorkIQ context recommending Word/Excel/PowerPoint outputs; **proactive push notifications reach GA** — "Your Day at a Glance" and "Items waiting for you" delivered to the mobile lock screen by default for M365 Copilot licence holders; multimodal Notebooks capture (audio + images + notes) rolls out in September on Android and iOS. [10][11][12] |
| **Grok (xAI)** | **Grok Build ships configurable default permission mode** — operators set the session-start permission posture via `[ui] default_selected_permission` or `GROK_DEFAULT_SELECTED_PERMISSION` env var; headless sessions browsable in resume picker; auto mode now shows a permission card when the classifier blocks an action; turn duration and footers appear in session history after `/resume`; `grok clone` reuses linked worktrees for faster session creation. [13][14][15] |
| **Perplexity** | **Bumblebee open-sourced** — read-only Go scanner for macOS/Linux developer endpoints checks packages, editor extensions, browser extensions, and MCP configs against known-compromised releases, connected to Computer for triggered deeper scans; Agent API remains the canonical post-Sonar endpoint with 25 days to September 27 retirement deadline; Computer in Email available to all Computer users. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Fable 5.1 Default, Subagent Fleet Control, and the Containment Escape Rule

Anthropic's most consequential Claude Code UX event entering September is the silent promotion of **Claude Fable 5.1** to the default Fable model in Claude Code. 

Claude Code releases Fable 5.1 as the default Fable model and adds new time, effort, and subagent controls, stronger auto-mode and sandbox protections, plus broad fixes and performance improvements across sessions, Remote Control, and cloud workflows.

 The changelog entry understates the UX significance: 

Claude Code added Claude Fable 5.1 (claude-fable-5-1) as the default Fable model with a 1M context window, new time format and timezone settings, and `/effort` in session to change effort for the current session only, matching `/model`.

 The addition of a per-session `/effort` command — which persists for the duration of the session rather than requiring re-specification per turn — is the developer ergonomics improvement that practitioners running long-horizon agentic coding workflows have needed. 

Fable 5.1 defaults to high-effort mode in Claude Code environments, aiming to maximise task performance rather than minimise cost — inside tools and IDE plug-ins, this can yield higher accuracy and persistence on large, multi-step coding problems.



The second consequential control-design event is the introduction of `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`. 

Anthropic added `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` to apply `CLAUDE_CODE_SUBAGENT_MODEL` (or the main model) to every subagent, ignoring per-spawn and agent-definition model overrides.

This was accompanied by a change to `CLAUDE_CODE_SUBAGENT_MODEL` to set the default subagent model rather than override everything: an agent definition's `model:` and an explicit per-spawn model now take precedence over it.

 For fleet operators running multi-agent Claude Code workflows on shared enterprise infrastructure, these two environment variables are a meaningful governance pair: the force variant locks the model across the entire subagent graph, while the non-force variant sets the default but respects agent-definition-level overrides. This is the subagent model-governance primitive that was previously missing from the Claude Code operator toolkit.

The third safety-design event — and the one most relevant to practitioners running Claude Code in cloud or shared infrastructure environments — is the new Containment Escape rule in auto mode. 

Anthropic added a Containment Escape rule to auto mode so cloud metadata-credential fetches, egress evasion, and cross-tenant reach are no longer auto-approved unless your environment marks them expected.

 The UX significance of this rule is disproportionate to its single-line changelog description: previously, auto mode's permissiveness extended to the class of network actions — metadata endpoint fetches, credential materialisation calls — that are the standard mechanism for cloud privilege escalation. Making these require explicit environmental opt-in rather than implicit auto-approval closes the automated-session attack surface that security teams have most consistently flagged. 

Anthropic also notes that models released after August 2, 2026 now carry an invisible watermark — a numerical signal of the likelihood Claude was involved in writing a text — as part of its EU AI Act Code of Practice commitments, with no practical impact on output quality and no user-identifying information contained in the signal.



---

### ChatGPT / OpenAI: Lock Screen Voice, WebMCP Site Tools, and the Messages-Agent Connector

OpenAI's most ambient-reach-expanding UX event in this window is the arrival of **Live voice on the iPhone Lock Screen and Dynamic Island**. 

Content from a Live voice conversation can now appear on the iPhone Lock Screen and, on iPhones with Dynamic Island, in the Dynamic Island — Live Activities can show content from a voice conversation while the user is in another app or the phone is locked, and continuing a voice conversation outside ChatGPT requires enabling Background conversations in Settings → Voice.

 The interaction-design shift this establishes is significant: the AI voice session is no longer bounded by the app window. A user can lock their phone, put it in their pocket, and the conversation continues — visible on the lock screen as a persistent Live Activity card. This converts ChatGPT Live voice from a "within-app experience" to an "ambient presence on the device surface" model, the same architectural leap that persistent always-on agents have been approaching across every platform.

The second consequential UX event is the formal arrival of **Site tools via WebMCP** in the ChatGPT desktop browser. 

ChatGPT Work and Codex can now use tools that supported websites provide directly in the desktop app's built-in browser — users can work directly with a website's tools, with ChatGPT discovering tools for the task without a separate connection; selecting the arrow in the address bar reveals the tools a page provides; site tools use WebMCP and require a supported account, model, and webpage.

 The trust-design transparency element here is the address-bar arrow: 

existing website-access and sensitive-action confirmations still apply.

 This means the agent's tool discovery is legible before execution — the user can inspect what a site offers before the agent acts on it, which is the correct sequencing for building user trust in a protocol that allows websites to define what agents can do on their behalf.

The third event — the **Apple Messages plugin** — is the interaction-design development with the most sensitive trust surface of the three. 

On Apple silicon Macs, the Apple Messages plugin in the ChatGPT desktop app can read and search iMessage, SMS, and RCS conversations and prepare or send messages through Messages — and by default, ChatGPT asks the user to approve the message and recipients before sending.

The plugin guide notes persistent-approval risks, revocation steps, and a known issue with tasks that disable approval prompts.

 The default-approval-before-send gate is the right trust primitive for a plugin with send access to the user's personal message threads — but the explicit warning about tasks that can disable approval prompts is the safety caveat practitioners need to track: the agent's ability to compose and queue messages is not itself the risk, but agentic task execution that inherits the plugin connection without triggering the approval gate is.

---

### Google Gemini: Generative UI Matures and the Assistant Migration Clock Runs Out

Google's most structurally significant enterprise UX event in this window is the continued maturation of **A2UI (Agent-to-UI)** in Gemini Enterprise. 

With new support for the Agent-to-UI protocol, custom agents can dynamically generate rich, native UI components — like interactive data visualisations and structured forms — directly within the Gemini Enterprise app, moving beyond simple text chat.

 The latest component catalogue update (v0.9) expands the available primitive set: 

the A2UI v0.9 Material catalogue adds Material 3 styling properties, new variants including icon, fab, and mini-fab buttons, and replaces the static required boolean across input components with a reactive validation checks rule array.

 The interaction-design paradigm A2UI establishes is worth isolating: 

instead of returning text or HTML, an agent returns a JSON payload that describes a UI — a tree of components (Card, Text, Button, ChoicePicker, Image) and a separate data model holding the values those components display.

The payload is data, not code — the client only renders components from a pre-approved catalogue, so a remote agent cannot inject arbitrary code or steal credentials through a UI widget.

 This declarative-not-executable constraint is the trust-design property that makes agent-generated UI safe to render in an enterprise context: the rendering boundary is enforced by the catalogue, not by the developer who built the agent.

The companion event — and the one with the largest immediate UX footprint — is the imminent **Google Assistant shutdown beginning September 4**. 

Google's notice to users states that "Google Assistant on your mobile device is being discontinued, and Gemini, our next-generation AI-powered assistant, is now the Assistant experience on Android" — removal starts on September 4, 2026, across phones, tablets, Wear OS, and Android Auto, with cars with Google built-in keeping the classic Assistant beyond that date.

Gemini stops being something a person chooses to install and becomes the assistant that answers when they hold the power button on a device they already own.

 The interaction-contract shift this forces on hundreds of millions of users is not cosmetic: where Assistant was optimised for single-command, immediate-response patterns, Gemini operates around multi-turn conversation, contextual reasoning, and agentic task delegation. 

On the admin side, admins can now access Google Chat usage metrics in the Gemini reports dashboard across organisation- and user-level reports, tracking active Gemini users, usage trends, and identifying who benefits most from Gemini-powered summarisation and generation features.



---

### Microsoft Copilot: Notebooks Become Proactive and the Lock Screen Threshold

Microsoft's most interaction-design-significant September event is the arrival of **proactive push notifications** completing their GA rollout — a shift that makes Copilot the first major enterprise AI product to push AI-generated organisational summaries to the device lock screen by default. 

Microsoft 365 Copilot's mobile app is now proactively summarising a user's emails, Teams activity, and files, then pushing that summary to their phone as a notification before anyone has asked for it — a genuine shift in how Copilot works: instead of waiting for a prompt, it decides on its own what is worth surfacing, somewhere far more visible than an app window.

Users with both a Microsoft 365 Copilot licence and mobile notifications enabled receive notifications built around "Your Day at a Glance" — a personalised summary of emails, Teams activity, and files — and "Items waiting for you" — a summary of open action items.

 The trust-design implication is significant: 

the feature is enabled by default for users who have both a Microsoft 365 Copilot licence and mobile app notifications enabled

 — meaning the opt-out model, not the opt-in model, governs whether AI-generated organisational data reaches the personal device lock screen. This is the consent architecture that enterprise privacy teams will need to evaluate before the rollout completes mid-September.

The companion workspace UX event is the **Copilot Notebooks revamp**, which lands alongside proactive artefact suggestions. 

The Copilot Notebooks user experience has been revamped with a streamlined flow for opening items and navigating the product — previously, users faced a more complex and less cohesive interface.

Copilot Notebooks now proactively lets users generate relevant documents by recommending artefacts based on WorkIQ and their notebook content — selecting a suggestion prompts Copilot to generate a more specific Word, Excel, or PowerPoint artefact based on the notebook's content and current project; this feature rolled out in August.

 The interaction-design pattern this establishes is the agent-as-content-initiator inside the workspace: rather than the user explicitly requesting a document, Notebooks reads the context of what the user is working on and surfaces relevant output formats. This is the same proactive-initiation model as the push notifications, applied to the desktop canvas rather than the mobile lock screen. 

Multimodal capture on Android — capturing audio, images, and notes in one experience, with Copilot automatically generating structured notes for Copilot Notebooks — also rolls out in September, with the same capability available in the OneNote app on iOS and iPad.



---

### Grok (xAI): Configurable Permission Posture and the Session Governance Arc

xAI's most interaction-design-significant Grok Build release in this window is the introduction of **configurable default permission mode** for new interactive sessions — a trust-design primitive that changes the governance model of how a Grok Build session's authority is established at start-up rather than negotiated mid-run. 

Grok Build improves session history, permissions, and terminal behaviour with smarter resume browsing, configurable default permission mode, more reliable prompt handling, and fixes for input, paste, image previews, and tool output, along with better voice capture fallback and background job handling. Key additions include: default permission mode for new interactive sessions is configurable; turn duration appears in session history after resume; turn footers appear after `/resume`; headless sessions can auto-allow permission prompts via a startup hint.



The UX significance of the configurable default permission mode runs deeper than the single changelog line suggests. 

The `GROK_DEFAULT_SELECTED_PERMISSION` environment variable (or `[ui] default_selected_permission` in config.toml) overrides the default, with precedence: env var → config.toml → always_allow_all_sessions.

 This means operators can now pre-configure the permission posture of a Grok Build session — from cautious allow-once defaults appropriate for sensitive repositories to more permissive modes for automated CI pipelines — without modifying the agent definition or interrupting the session mid-run. 

Additionally, auto mode now shows a permission card when the classifier blocks an action on interactive sessions

 — a transparency primitive that makes the agent's blocked-action decisions visible in-line rather than silently suppressing them. The combination of configurable session-start permission posture and in-session blocked-action cards is the governance-layer design that enterprise teams need before they can sanction Grok Build for use on regulated repositories: the authority boundary is declared before the session starts, and any deviation from it is surfaced to the operator during execution.

The session-observability improvements compound this governance arc. 

Turn duration now appears in session history after resume, and turn footers (Worked for, cancelled, failed) appear after `/resume`.

 For practitioners managing long-running or resumed Grok Build sessions, this is the temporal UX information that was previously missing: how long each turn took, and what its final status was — the minimal audit trail that multi-session agentic workflows require. 

Separately, `grok clone` now reuses matching local checkouts as linked worktrees for faster session creation

 — a performance improvement that meaningfully reduces the friction cost of spinning up a new agentic coding session on a large existing codebase.

---

### Perplexity: Bumblebee and the Agent-Endpoint Trust Surface

Perplexity's most consequential trust-design contribution in this window is not a product feature — it is an infrastructure release. 

Perplexity is open-sourcing one of the internal tools it uses to protect the developer systems behind Perplexity, Comet, and Computer — recent threats increasingly target the software packages, developer tools, and local environments that modern engineering teams rely on, and the integrity of products has to begin further up the supply chain than production.

Built for macOS and Linux, Bumblebee operates in read-only mode and scans packages, browser extensions, editor extensions, and AI tool configurations without executing potentially harmful installation scripts — the company says the tool was originally developed internally to protect systems behind Comet and Perplexity Computer.



The interaction-design significance of **Bumblebee** for the agentic ecosystem is its explicit scope extension to MCP configurations. 

Bumblebee answers one question: when an advisory names a compromised package, extension, or version, which developer machines show a match in their on-disk metadata right now? It reads lockfiles, installed package metadata, extension manifests, and MCP configuration files — it never runs npm, pip, or any other package manager, never reads source code, and never makes network calls during the scan.

 As MCP servers become a first-class component of the agentic developer environment — present in Claude Code sessions, Grok Build sessions, Codex sessions, and Gemini Enterprise deployments — a read-only scanner that specifically checks MCP configs for compromised dependencies is the supply-chain trust primitive that the agentic tool ecosystem has needed. 

Connected to Computer, it can trigger deeper scans whenever a new supply-chain risk emerges.

 This Computer integration is the agentic UX layer that makes Bumblebee more than a static CLI tool: the scanning decision itself becomes an agent-triggered workflow, with Computer initiating deeper endpoint scans in response to newly published threat intelligence rather than requiring a human to schedule them manually.

On the API transition front, the Sonar retirement clock continues to advance: with 25 days remaining before the September 27 deadline, teams still running Sonar-backed agentic workflows face an increasingly urgent migration window. 

Users can send or forward an email to `computer@perplexity.ai` to start a Computer session from email — Computer reads the thread context and replies only to the verified sender in the same thread using that sender's existing connectors, permissions, and Memory.

 Computer in Email remains the temporal UX standout of Perplexity's recent release arc: the ability to initiate a multi-step agentic task from the oldest async medium and receive the result back in the same thread — with the agent inheriting scoped permissions from the sender identity — is the interaction pattern that makes agentic delegation genuinely accessible to non-technical users.

---

## The Bigger Picture: Model Upgrades, Generative UI, and the Proactive-Agent Threshold

The 48 hours ending September 2, 2026 mark the moment the agentic AI industry formally crosses what might be called the proactive threshold: agents are no longer primarily reactive surfaces that wait for a user to initiate. They are initiating on their own — pushing summaries to lock screens before a question is asked (Copilot), continuing voice conversations on a locked phone screen (ChatGPT), generating native UI components inside enterprise chat surfaces without a developer writing a line of interface code (Gemini A2UI), and triggering security scans of developer machines when threat intelligence changes (Perplexity Bumblebee + Computer). Each of these events, taken individually, looks like an incremental feature. Taken together, they represent the same architectural shift playing out simultaneously across every surface: the moment of interaction is no longer controlled solely by the user. The trust-design question this raises — who governs whether an agent initiates, how often, on which surface, and with what data — is the one every platform in this window is answering differently. Microsoft's answer is default-on with a licence gate. OpenAI's answer is default-approval-before-action, with a documented path to disable that gate in task contexts. Google's answer on the Assistant cutover is no answer at all, because the option to decline is removed. Grok's answer is the pre-configured permission posture declared at session start. The platforms that will earn sustained enterprise trust are the ones that make the initiation decision legible — where users and administrators can see, at a glance, which agent is initiating, with what authority, and what gate (if any) stands between the agent's decision and its action. The industry is not building proactive agents; it is building proactive agents with governance surfaces, and the quality of those surfaces will determine whether proactivity reads as productivity or as intrusion.

---

## References

[1] Claude Code Docs. (2026). *Claude Code Changelog*. [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

[2] Releasebot. (2026). *Claude Code Updates by Anthropic — September 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] Releasebot. (2026). *Anthropic Release Notes — September 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[4] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] Releasebot. (2026). *ChatGPT Updates by OpenAI — September 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[6] 9to5Mac. (2026). *ChatGPT update adds Apple Messages integration on Mac*. [https://9to5mac.com/2026/08/20/chatgpt-update-adds-apple-messages-integration-on-mac/](https://9to5mac.com/2026/08/20/chatgpt-update-adds-apple-messages-integration-on-mac/)

[7] Google Cloud Documentation. (2026). *Gemini Enterprise Release Notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[8] Keywords Everywhere. (2026). *Gemini Updates 2026: News, Features & Google Assistant Tracker*. [https://keywordseverywhere.com/news/gemini-updates/](https://keywordseverywhere.com/news/gemini-updates/)

[9] Google Workspace Updates Blog. (2026). *2026 Workspace Update Archive*. [https://workspaceupdates.googleblog.com/2026/](https://workspaceupdates.googleblog.com/2026/)

[10] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[11] Vantage 365. (2026). *Microsoft 365 Copilot Push Notifications: What to Know*. [https://vantage365.com/microsoft-365-copilot-proactive-push-notifications/](https://vantage365.com/microsoft-365-copilot-proactive-push-notifications/)

[12] Microsoft Community Hub. (2026). *What's New in Microsoft Copilot — August 2026*. [https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960)

[13] Releasebot. (2026). *Grok Build Updates by xAI — September 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[14] GrokInsider / X. (2026). *Grok Build CLI v1.0.11 Changelog*. [https://x.com/GrokInsider/status/2092733692108067003](https://x.com/GrokInsider/status/2092733692108067003)

[15] Toolsbase. (2026). *Grok Build (grok) Cheat Sheet 2026 — 250 Commands*. [https://toolsbase.dev/en/reference/grok-build-commands](https://toolsbase.dev/en/reference/grok-build-commands)

[16] Perplexity AI. (2026). *Perplexity Is Open-Sourcing Bumblebee*. [https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee](https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee)

[17] Releasebot. (2026). *Perplexity Release Notes — August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[18] Developers Digest. (2026). *Perplexity Bumblebee: Developer Guide to the Open Source Supply Chain Scanner*. [https://www.developersdigest.tech/blog/perplexity-bumblebee-supply-chain-scanner-developer-guide-2026](https://www.developersdigest.tech/blog/perplexity-bumblebee-supply-chain-scanner-developer-guide-2026)