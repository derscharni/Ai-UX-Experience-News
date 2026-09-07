# UX Briefing: Astra Floods Production, Governance Scales, Persona Persists

**September 07, 2026**

Good morning. The 48 hours ending September 7, 2026 are defined by four simultaneous pressure fronts that, taken together, represent the most consequential week of agentic product delivery since the category's inception. **ChatGPT/OpenAI** completes the broadest rollout of its lifecycle as **GPT-6 Astra** — whose UX story is not merely a model upgrade but a fundamental redesign of how agents handle ambiguity, authority, and long-running task state — reaches all Plus, Business, Enterprise, and Pro users in Work and Codex by September 6, carrying with it a new **Astra Auto-Review safety monitor** that pauses or stops agentic sessions the moment misinterpretation is detected, and an **async clarification** model that lets Codex ask questions without stalling unrelated work. **Claude/Anthropic** ships its most operationally significant diagnostic release of the year: **Claude Code v2.1.261** lands `/skill-doctor` — a first-class command that shows every loaded skill the session never used and measures its context cost — alongside a new **Organization policy line** in `/status` and `claude doctor` that surfaces *why* an org policy failed to load, ending the silent-failure era for enterprise fleet operators. **Google Gemini** simultaneously advances on two fronts: persistent **cross-surface custom instructions** for Gemini in Workspace begin their gradual rollout to Drive, Chat, Gmail, Sheets, and Slides as of September 2, and four new **Workspace Studio Flows** automation steps — Move Drive file, Copy Drive file, Send a Chat reply, Reply to email — expand the no-code agentic workflow surface with per-step admin approval gates. **Grok (xAI/SpaceXAI)** converts Grok Bot from an individual product into an **enterprise governance platform**, adding audit logs, Action Recording, OpenTelemetry Export, network destination allowlists, and per-user isolated execution environments as of September 3. And **Microsoft Copilot** advances its Cowork agentic surface with the **Automations tab** — a renamed and restructured scheduling surface that gives users a single place to view and manage every scheduled and event-triggered Cowork task — alongside **SharePoint personal skills** that follow users across sites, and the continued September rollout of **multimodal capture** for Notebooks.

---

## At a Glance: September 7 Highlights

Today's releases converge on the moment agentic AI stops being a pilot surface and becomes an organisational operating layer — and every platform is simultaneously redesigning its diagnostic, governance, and transparency surfaces to match.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **`/skill-doctor` and org-policy diagnostics ship in v2.1.261** — new command shows unused loaded skills and their context cost so operators can prune; Organization policy line added to `/status` and `claude doctor` to explain why a policy failed to load; `bashOutputMaxChars`/`taskOutputMaxChars` raised to 128K; Remote Control inbound event-stream fixed behind TLS-inspecting proxies on native Windows. [1][2][3] |
| **ChatGPT** | **GPT-6 Astra reaches all Plus, Business, Enterprise, and Pro users in Work and Codex** — Astra Auto-Review safety monitor pauses sessions when instruction misinterpretation is detected; async clarification lets Codex ask questions without stalling unrelated work; Astra made bundled default in model picker; Codex gets Amazon Bedrock model route; Apple Messages plugin ships for Apple silicon Macs. [4][5][6] |
| **Google Gemini** | **Cross-surface custom instructions begin rollout September 2** — persistent user instructions now apply across Ask Gemini in Drive, Chat, Gmail side panel, Sheets, and Slides; four new Workspace Studio Flows steps (Move Drive file, Copy Drive file, Send a Chat reply, Reply to email) add end-user approval gates for cross-org data actions; Gemini Notebook audit logs land in Admin console. [7][8][9] |
| **Microsoft Copilot** | **Cowork Automations tab restructures agentic task management** — Scheduled tab renamed Automations, unifying scheduled and event-triggered tasks in one view; SharePoint personal skills (Markdown, OneDrive-stored) follow users across sites; Copilot in SharePoint adds skill evaluations; multimodal Notebook capture continues September rollout on Android and OneNote. [10][11][12] |
| **Grok (xAI)** | **Grok Bot enterprise governance layer ships September 3** — audit logs (admin, security, auth events), Action Recording of what Bots actually do, OpenTelemetry Export for streaming into org monitoring stacks, network destination allowlists, SCIM, and per-user isolated execution environments now Enterprise-only; each Bot has no access by default; Grok and Cursor Enterprise customers get two-week free access. [13][14][15] |
| **Perplexity** | **Computer in Email active for all Computer users** — start or continue Computer sessions by forwarding email threads to computer@perplexity.ai; agent reads thread context and replies to verified sender using their existing connectors, permissions, and Memory; Search as Code reliability holds at 92.6%; Bumblebee MCP-config scanning integration with Computer deepens the supply-chain trust surface. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Skill-Doctor Diagnostic and the Silent-Policy-Failure Fix

Anthropic's most consequential Claude Code UX event in this window is the arrival of **`/skill-doctor`** in v2.1.261 — a diagnostic command that surfaces the context cost of skills that are loaded but never used during a session, giving enterprise operators a measured, per-skill pruning signal for the first time.



Published on September 4, 2026, the release adds `/skill-doctor` to show unused loaded skills and their context cost, giving teams a measured pruning candidate list.

 The UX significance of this runs deeper than routine tooling: as Claude Code skill libraries grow across organisations — accumulated through months of team contributions and third-party skill registries — the context cost of skills that are *loaded but idle* becomes a significant, invisible drag on every session's effective window. `/skill-doctor` converts that invisible cost into an actionable, per-skill line item. This is the same trust-design principle as Grok Build's context-usage display: operators cannot govern what they cannot see.

The companion diagnostic event is the **Organization policy line** that now appears in `/status` and `claude doctor`. 

An "Organization policy" line added to `/status` and `claude doctor` explains why your organisation's policy could not be loaded — for example, a proxy not passing the endpoint through.

 Before this release, an organisation policy that silently failed to load could leave a developer operating without the intended governance constraints, with no visible signal that anything was wrong. 

Improved policy helper diagnostics now mean refresh failures show in `/status`, declining the managed-settings dialog prints why Claude Code exited, and helper timeouts are reported as timeouts.

 This is the fleet-operations legibility improvement that enterprise platform engineers have been waiting for: the "is my policy actually applied?" question now has a first-class diagnostic answer that surfaces before the session begins rather than only in retrospect.

The supporting infrastructure improvements compound both diagnostic gains. 

Bedrock model checks behind TLS-inspecting proxies are now fixed, and the setup wizard times out clearly when AWS or a credential helper never responds; Remote Control fixes its inbound event-stream failure behind TLS-inspecting corporate proxies on native Windows.

 These are the deployment-reality fixes that matter most for enterprise fleet operators whose managed-network environments have historically been the primary source of Claude Code rollout friction. The UX implication is that the gap between "works in the developer's home environment" and "works in the corp VPN environment" closes materially in this release.

---

### ChatGPT / OpenAI: Astra Reaches Production and Auto-Review Becomes the Safety Primitive

OpenAI's most structurally significant UX event in this window is not the GPT-6 Astra launch itself — covered in the September 4 briefing — but rather the **completion of Astra's rollout** across all paid tiers and the concurrent hardening of its safety-interaction design for production agentic use.



As of September 6, OpenAI's official rollout announcement confirmed Astra is live in the API and available to all Pro, Enterprise, and Business Premium users in Work and Codex; OpenAI leaders then said the Work and Codex rollout had also reached all Plus and Business users — moving the access label to rollout complete.

 This is the moment Astra transitions from a preview-posture product to a production-posture one, and the trust-design decisions baked into its UX become the daily interaction model for the broadest user base OpenAI has ever deployed a frontier model to.

The **Astra Auto-Review safety monitor** is the trust-design primitive worth isolating. 

Astra includes additional safety monitoring to look for cases where agents may not have interpreted user instructions correctly; if a potential case is detected, the conversation may be paused or stopped as a precaution for the user to review and decide how to proceed.

 The UX pattern this establishes is the mid-task checkpoint: rather than a pre-session approval gate or a post-hoc audit log, Auto-Review inserts a review moment *during* task execution, at the point where the agent's trajectory has diverged from what the user likely intended. 

In an internal evaluation, Astra never attempted to circumvent a Codex Auto-Review denial — this held even when Auto-review was deliberately configured to be evadable and the task was impossible to complete otherwise.

 The willingness-to-stop rather than willingness-to-circumvent quality is the most significant trust signal in Astra's safety profile.

The **async clarification** model and the **Apple Messages plugin** round out the week's interaction-design changes. 

In Codex, Astra can ask asynchronously while continuing work that doesn't depend on your reply; if you don't respond, it proceeds with sensible assumptions where appropriate, but waits for your input on consequential decisions.

On Apple silicon Macs, the Apple Messages plugin in the ChatGPT desktop app can read and search iMessage, SMS, and RCS conversations and prepare or send messages through Messages.

 The Messages integration extends Astra's computer-use surface to the most sensitive communication layer on Apple devices — and the trust-design implication is the same as every connector launch this week: the approval architecture that governs what the agent can read and send needs to be explicit, visible, and revisable.

---

### Google Gemini: Persistent Instructions Across the Workspace Surface and the Studio Flows Consent Architecture

Google's most interaction-design-significant event in this window is the gradual rollout of **persistent cross-surface custom instructions** for Gemini in Workspace — an architectural change that moves user preferences from a per-conversation re-entry ritual into a durable, cross-app personalization layer.



Gemini expands persistent custom instructions across Google Workspace, bringing personalised responses to Ask Gemini in Drive and Chat plus the Gemini side panel in Slides, Sheets, and Gmail; users can save and manage instructions to keep style, tone, and formatting consistent across surfaces.

The feature began its gradual 15-day rollout on 2 September 2026 and is available across various business and enterprise tiers.

 The UX significance of this cross-surface expansion is the shift from a *per-surface* personalisation model — where a user's instruction set existed in Docs but had to be re-established in every other app — to a *per-user* personalisation model where a single instruction set governs Gemini's behaviour regardless of which Workspace surface the user is in. 

The system is designed to provide a consistent experience; currently the instructions are applied globally to ensure a uniform output style across the user's entire Workspace.



The second major UX architecture event is the launch of four new **Workspace Studio Flows** automation steps. 

To help teams automate everyday work and seamlessly connect tasks across Google Workspace, Google is introducing four new automation steps in Workspace Studio Flows: Move Drive file, Copy Drive file, Send a Chat reply, and Reply to email.

 The trust-design detail that matters most for enterprise practitioners is the per-step admin approval gate: 

these new steps give end users greater control over document management and cross-channel communications, enabling end-to-end automated flows directly from Workspace Studio; admins will have settings to disable individual steps and to require end-user approval when these actions may share data with audiences outside of their organisation.

 This is the correct governance pattern for no-code agentic flow builders: the admin defines which steps are permissible at all, and then opts specific steps into a user-approval gate precisely at the moment data might cross an organisational boundary.

The companion admin-transparency event is the arrival of **Gemini Notebook audit logs** in the Workspace Admin console. 

Workspace administrators can now access comprehensive audit logs for Gemini Notebook in the Admin console, providing greater insights into how the application is used across their organisations; the update introduces full visibility into Gemini Notebook actions, allowing administrators to review usage and audit data access in the security investigation tool.

 The UX arc this completes is notable: Gemini Notebook first landed its user-facing revamp in recent months; audit log visibility arriving now brings the admin-observability surface into parity with the user experience maturity — the pattern every enterprise feature needs before it can be considered governance-ready rather than merely available.

---

### Microsoft Copilot: Automations Tab, SharePoint Skills, and the Cowork Agentic Task Surface

Microsoft's most structurally significant Copilot UX event in this window is the renaming and restructuring of Cowork's scheduling surface into the **Automations tab** — a trust-design intervention that converts a feature that had been growing organically (scheduled tasks, event-triggered tasks, Planner integrations) into a unified, legible management surface.



The Scheduled tab in Cowork is now called Automations; the updated section gives users one place to view and manage all of their automated tasks, including both scheduled and event-triggered tasks.

 The interaction-design significance of this renaming-plus-restructuring is the ontological shift it signals to users: "Scheduled" implied a calendar; "Automations" implies agency. A user looking at an Automations tab understands they are looking at work Cowork is doing on their behalf, not simply a reminder queue. That semantic clarity is the first step toward the kind of human-agent relationship legibility that sustained enterprise adoption requires.

The **SharePoint personal skills** surface advances the Copilot personalisation arc that the September Notebooks revamp began. 

This month, reusable skills can follow users across SharePoint and OneDrive, Copilot can measure and improve those skills with evaluations, and new guidance helps AI agents build live, SharePoint-safe experiences.

Users can create a personal skill once and use it across all their SharePoint sites — preferred formats, standards, and repeatable ways of working can travel with the user instead of being tied to one site.

 The UX pattern this establishes is the portable work identity: rather than the user's AI-interaction preferences being site-scoped or session-scoped, they travel with the user's OneDrive identity across the entire Workspace. This is the Copilot equivalent of what Gemini's cross-surface custom instructions deliver in the Google ecosystem — and both platforms landing it in the same week signals deliberate convergence on the user-persistent personalisation primitive as a table-stakes feature.

The **multimodal Notebook capture** September rollout continues in parallel. 

Users can capture audio, images, and notes in one experience, and Copilot automatically generates structured notes for their Copilot Notebooks; multimodal capture is also available in the OneNote app on iOS and iPad; this feature rolls out in September.

Copilot Notebooks now gives users two connected ways to work: a lightweight experience in the Copilot app, and a workspace experience in OneNote; in the Copilot app, users can quickly chat with Copilot, explore references, and create artefacts; in OneNote, users will get a workspace experience for deeper project work, expanded artefact creation, and team collaboration; because notebooks stay in sync across the Copilot app and OneNote, users can move between the two without losing context.



---

### Grok (xAI): Grok Bot Enterprise and the Audit Stack as Governance Infrastructure

SpaceXAI's most consequential agentic UX event in this window is the transformation of Grok Bot from a consumer and teams product into a **governed enterprise platform** — a release that adds the compliance-grade audit and network infrastructure that makes persistent autonomous agents deployable in regulated organisational environments.



Grok Bot enterprise audit controls arrived on 3 September 2026, when xAI opened Grok Bot to enterprises and added access, network, and audit controls for governing autonomous bots at scale — audit logs covering admin, security, and authentication events, Action Recording of what bots actually do, and OpenTelemetry Export for streaming it all into the organisation's own monitoring stack.

 The UX significance of this three-layer audit architecture is that it maps directly onto the three questions a compliance officer asks before approving any autonomous agent for enterprise use: who authorised what access (audit logs), what did the agent actually do (Action Recording), and how does this integrate with our existing SIEM/monitoring infrastructure (OpenTelemetry Export). Shipping all three simultaneously is not accidental; it is the minimum viable governance stack for enterprise deployment.

The network control layer adds the infrastructure boundary that makes the audit trail meaningful. 

Enterprise-only on the Grok Bot dashboard: the organisation-wide enable switch, Network Controls, Team Setup, Action Recording, and computer management for organisation admins; audit logs, OpenTelemetry Export, the MCP allowlist, and SCIM are also Enterprise only.

Admins set a Grok Bot network policy from the Grok Bot page of the Cursor dashboard; it controls which destinations team computers can reach.

 This destination-allowlist model — the same pattern that Anthropic's Inference Hooks and Perplexity's Computer connector governance use — is the trust-design primitive that converts an agent's network reach from "everything the internet allows" to "everything the organisation has approved."

The isolation-by-default access model is the zero-trust design detail worth isolating. 

A Bot has no access by default and reaches only the accounts you sign it into.

For enterprise deployments, SpaceXAI says each user's work runs in a secure isolated environment and that a Bot has no account access by default; the new enterprise release adds controls for access, networking, and audits, which are particularly relevant when agents are allowed to work asynchronously and across multiple business systems.

 This is the governance design that distinguishes a platform ready for enterprise deployment from one that acquired permissions broadly at setup and proceeded without further constraint — the exact design failure mode that the entire industry is working to eliminate.

---

### Perplexity: Computer in Email and the Async-Agent Entry Pattern

Perplexity's most significant agentic UX development in this window is the general availability of **Computer in Email** — an interaction-design primitive that converts email into a first-class Computer session surface, allowing users to delegate agentic tasks through the communications channel they are most likely to be using when they encounter work that needs doing.



Perplexity adds Computer in Email, letting users start and continue Computer sessions from email threads.

Send or forward computer@perplexity.ai an email to start a Computer session from email; Computer reads the thread context and replies only to the verified sender in the same thread using that sender's existing connectors, permissions, and Memory.

 The interaction-design significance of this pattern is the ambient delegation model it enables: the user does not need to navigate to a separate Computer interface, configure connectors, or re-establish context. The email thread *is* the context. The agent inherits the sender's verified connectors and Memory, acts within those boundaries, and replies inline. This is the lowest-friction on-ramp to agentic delegation in any product this week.

The trust-design primitives embedded in Computer in Email's architecture deserve the same scrutiny as the feature itself. The verified-sender check and the existing-connectors-only constraint are not UX conveniences; they are the security design that prevents email-based Computer delegation from becoming a social-engineering vector. 

Enterprise reply-all support is coming soon

 — and when it arrives, the verified-sender check will be the critical control that determines whether reply-all Computer invocations are safe for enterprise use. The trust-design practitioner question for this feature is: does the sender-verification design hold when the email is forwarded, BCC'd, or originates from a mailing list?

On the supply-chain trust surface, the **Bumblebee-Computer integration** deepens the agentic ecosystem security model in a way that directly affects every platform covered in this briefing. 

Bumblebee also scans MCP configuration files — the local files that tell AI assistants like Claude or Cursor which external services they're allowed to connect to; when a new threat surfaces, Perplexity Computer drafts a catalog entry for it, a human reviews and approves it, and Bumblebee runs across all developer machines to check for matches.

 This human-in-the-loop catalog update workflow — Computer identifies, human approves, Bumblebee scans — is the trust-design pattern that makes agentic security tooling credible: the autonomous agent surfaces the threat signal, but a human validates the catalog entry before it propagates to endpoints. The autonomy is bounded at exactly the right point.

---

## The Bigger Picture: Astra Floods Production, Governance Scales, Persona Persists

The 48 hours ending September 7, 2026 mark the moment the agentic AI industry simultaneously crosses three thresholds that have been approaching for the past year. First, Astra completing its production rollout to all ChatGPT paid tiers means computer-use and long-running agentic coding sessions are no longer a preview capability available to a selected cohort — they are the default experience for hundreds of millions of users, and the safety design baked into Auto-Review and async clarification becomes the interaction model at scale. Second, Grok Bot's enterprise governance launch establishes that persistent autonomous agents cannot enter organisations without a compliance-grade audit stack: audit logs, Action Recording, OpenTelemetry Export, network destination allowlists, and per-user execution isolation are the minimum viable governance layer, and they all shipped together. Third, Google and Microsoft simultaneously landing cross-surface persistent instructions and portable personal skills signals that the industry has reached agreement on a previously contested UX primitive: user preferences must follow the user across every surface the agent appears on, not reset with each new app or session. Claude Code's `/skill-doctor` and organisation-policy diagnostic sit at the intersection of all three trends — a single release that makes the agent's loaded capabilities visible, its governance configuration legible, and its failure modes diagnosable before they affect production work. The platforms that will define enterprise AI interaction in 2027 are the ones that treat diagnostic transparency, governance infrastructure, and persistent user identity not as separate features to be shipped on separate roadmaps, but as a single coherent contract between the agent and the organisation that deploys it. This week's releases are the most concrete evidence yet that the industry knows what that contract requires.

---

## References

[1] Updatify. (2026). *Claude Code release notes — Sep 5, 2026*. [https://updatify.io/releases/claude-code](https://updatify.io/releases/claude-code)

[2] CCLeaks. (2026). *Claude Code 2.1.261 adds /skill-doctor diagnostics*. [https://ccleaks.com/news/claude-code-2-1-261-sep-2026](https://ccleaks.com/news/claude-code-2-1-261-sep-2026)

[3] Releasebot. (2026). *Claude Code Updates by Anthropic — September 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[4] OpenAI. (2026). *GPT-6 Astra: A new generation of intelligence*. [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)

[5] Kingy.ai. (2026). *GPT-6 Astra Access: Plans, API, Pricing, Daybreak*. [https://kingy.ai/news/gpt-6-astra-access-chatgpt-api-daybreak/](https://kingy.ai/news/gpt-6-astra-access-chatgpt-api-daybreak/)

[6] Releasebot. (2026). *ChatGPT Updates by OpenAI — September 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] Google Workspace Updates Blog. (2026). *Custom instructions for Gemini in Workspace now available in more apps*. [https://workspaceupdates.googleblog.com/2026/09/custom-instructions-for-gemini-in-Workspace-now-available-in-more-apps.html](https://workspaceupdates.googleblog.com/2026/09/custom-instructions-for-gemini-in-Workspace-now-available-in-more-apps.html)

[8] Google Workspace Updates Blog. (2026). *Automate Drive, Gmail, and Google Chat actions with new steps in Workspace Studio*. [https://workspaceupdates.googleblog.com/2026/09/automate-drive-gmail-and-google-chat-actions-with-new-steps-in-Workspace-Studio.html](https://workspaceupdates.googleblog.com/2026/09/automate-drive-gmail-and-google-chat-actions-with-new-steps-in-Workspace-Studio.html)

[9] Google Workspace Updates Blog. (2026). *Google Workspace Weekly Recap — September 4, 2026*. [https://workspaceupdates.googleblog.com/2026/09/weekly-recap-09-04-2026.html](https://workspaceupdates.googleblog.com/2026/09/weekly-recap-09-04-2026.html)

[10] Microsoft Community Hub. (2026). *What's New in Microsoft Copilot — August 2026*. [https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-copilot--august-2026/4551960](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-copilot--august-2026/4551960)

[11] Microsoft Community Hub. (2026). *What's New in Copilot in SharePoint: September 2026*. [https://techcommunity.microsoft.com/blog/spblog/whats-new-in-copilot-in-sharepoint-september-2026/4535422](https://techcommunity.microsoft.com/blog/spblog/whats-new-in-copilot-in-sharepoint-september-2026/4535422)

[12] Releasebot. (2026). *Microsoft Copilot Updates by Microsoft — September 2026*. [https://releasebot.io/updates/microsoft/microsoft-copilot](https://releasebot.io/updates/microsoft/microsoft-copilot)

[13] SpaceXAI. (2026). *Grok Bot for Enterprise*. [https://x.ai/news/grok-bot-for-enterprise](https://x.ai/news/grok-bot-for-enterprise)

[14] SpaceXAI Docs. (2026). *Grok Bot security*. [https://docs.x.ai/grok-bot/security](https://docs.x.ai/grok-bot/security)

[15] AI Success Lab. (2026). *Grok Bot Enterprise Audit Controls: Logs, Recording, Export*. [https://aisuccesslabjuliangoldie.com/blog/grok-bot-enterprise-audit-controls/](https://aisuccesslabjuliangoldie.com/blog/grok-bot-enterprise-audit-controls/)

[16] Releasebot. (2026). *Perplexity Release Notes — August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[17] Yahoo Tech. (2026). *Perplexity Built a Tool That Checks Your Computer for Infected Software*. [https://tech.yahoo.com/ai/perplexity-ai/articles/perplexity-built-tool-checks-computer-170855184.html](https://tech.yahoo.com/ai/perplexity-ai/articles/perplexity-built-tool-checks-computer-170855184.html)

[18] Perplexity. (2026). *Perplexity is Open-Sourcing Bumblebee*. [https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee](https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee)

---