# UX Briefing: Keyless Agents, Generative UI, and the Mobile Approval Surface

**June 25, 2026**

Good morning. The last 48 hours crystallise around four stories that together define the week's deepest shift in agentic UX infrastructure. **Anthropic Claude** reached a milestone in agentic authentication, making **Workload Identity Federation** generally available on the Claude Platform — replacing static API keys with short-lived, per-workload credentials and pairing the release with a new **Claude Apps Gateway** that brings corporate SSO, role-based access, and per-developer cost attribution to every Claude Code deployment; **OpenAI Codex** brought **Codex Remote** to general availability across all paid ChatGPT plans on June 25, introducing authenticated QR-paired phone-to-desktop control and a new **DigitalOcean Droplet Workspace plugin** that lets agents provision and occupy a persistent cloud VM from within the app; **Google Gemini** activated its most radical interface experiment to date, shipping **Dynamic View** and **Visual Layout** as Labs features powered by Gemini 3's agentic coding capabilities — allowing the app to generate fully interactive, custom-coded micro-app UIs on the fly for any prompt; and **Microsoft Copilot** rounded out its Build-season agentic stack with the GA of **Copilot Cowork** (June 16), a metered, cloud-hosted, long-running task executor that ships with a Cost Management Dashboard, Purview compliance controls, and a toggle-accessed entry point directly in the Copilot app. The macro signal: the field is no longer racing to add agentic capabilities — it is racing to make those capabilities authenticated, observable, and steerable from any surface a user happens to be on.

---

## At a Glance: June 25 Highlights

This window's releases collectively answer the question that follows capability maturity: now that agents can do the work, how do you prove they are who they say they are, see what they spent, steer them from your phone, and trust that what they display is actually suited to what you asked?

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Workload Identity Federation (WIF)** reaches GA on the Claude Platform (June 17), replacing static API keys with short-lived, per-workload OIDC tokens and introducing service accounts with per-workload audit trails; the companion **Claude Apps Gateway** ships for Amazon Bedrock and Google Cloud, adding corporate SSO, managed-settings enforcement, and per-developer cost attribution via a stateless container; Claude Code also ships **Trusted Devices for Remote Control** requiring device verification before remote sessions. [1][2][3] |
| **ChatGPT** | **Codex Remote** reaches general availability across all ChatGPT plans on June 25, enabling mobile-to-desktop task control with **authenticated one-to-one QR pairing**; the new **DigitalOcean Droplet Workspace plugin** lets Codex provision a cloud VM and connect it as a persistent remote workspace; also shipping: a Codex **Sites preview** for deploying hosted web apps and dashboards directly from within the app. [4][5][6] |
| **Google Gemini** | **Dynamic View** and **Visual Layout** launch as experimental Labs features in the Gemini app, powered by Gemini 3's agentic coding capabilities — Dynamic View generates fully coded, single-purpose interactive UIs per prompt; Visual Layout renders magazine-style immersive responses; both are rolling out in **Google Search AI Mode** alongside the Gemini app; Gemini in Chrome on Android (including auto browse) is launching in late June. [7][8][9] |
| **Microsoft Copilot** | **Copilot Cowork** reaches GA worldwide (June 16), bringing metered, cloud-hosted, end-to-end task execution with a toggle entry point in the M365 Copilot app, a **Cost Management Dashboard**, 13 built-in skills, push notifications for long-running tasks on iOS and Android, and full Purview compliance coverage; the **Researcher agent** now lets users choose model and mode per research task inline; **model choice in Word** adds Anthropic models to in-document editing. [10][11][12] |
| **Grok (xAI)** | **Grok Build** ships a major agent dashboard overhaul with per-agent model and mode visibility in the peek panel, mode cycling via Shift+Tab, typed tool-usage cards for search, directory listing and file deletion, `--json-schema` output for `grok -p`, and automatic local plugin refresh at session start; the `/goal` long-running autonomous mode for larger implementation tasks also ships this window. [13][14] |
| **Perplexity** | The **Deep Research in Computer** integration (June 19) continues maturing; the hybrid local-server inference orchestrator announced at Computex — which automatically routes tasks between on-device and cloud models and asks for user permission before sending sensitive data to the cloud — remains on track for July 2026; Perplexity Health rolls out to Pro and Max subscribers with connected medical records and device data. [15][16] |

---

## Product Highlights

### Claude / Anthropic: Keyless Authentication and the Per-Workload Audit Trail

Anthropic's most consequential release of the 48-hour window operates almost entirely below the visible application interface — but it reshapes the trust contract for every agentic workload built on Claude. 

On June 17, Anthropic made Workload Identity Federation (WIF) generally available on the Claude Platform; the short version is that the static API key, the long secret string that gets pasted into scripts and then leaks out of them, is now optional.



**WIF**'s trust design directly addresses the credential sprawl that agentic coding workflows have created. 

WIF replaces static API keys with short-lived, scoped credentials issued at request time — whether you're a two-person startup running GitHub Actions or an enterprise with detailed credential policies, you can now authenticate with the Claude Platform the same way you authenticate with the rest of your stack, with no static Anthropic credentials to create, rotate, or leak.

 The credential topology maps to existing cloud identity infrastructure: 

workloads authenticate with the identity they already have — an AWS IAM role, a GCP or Kubernetes service account, an Azure managed identity, a GitHub Actions token, or other OIDC-compliant providers — and Anthropic is also introducing service accounts to the Claude Platform, so each workload can have its own identity, roles, and audit trail instead of a shared API key.

 The UX implication for operators is significant: for the first time, the question "which Claude workload made that API call?" is answerable in the same audit infrastructure that governs the rest of the cloud stack, without any additional logging instrumentation. 

Every exchange and request is recorded against that service account in audit logs, and the Claude Console has a guided setup flow for configuring workload identities.



Alongside WIF, Anthropic shipped the **Claude Apps Gateway** for Amazon Bedrock and Google Cloud deployments — a companion control plane that solves the org-level management problem WIF leaves open. 

Previously, running Claude Code across a team meant provisioning a cloud credential per developer, manually pushing settings to every laptop, and standing up separate tooling to see per-developer spend; the gateway is a self-hosted control plane that gives you corporate SSO login, centrally enforced policy, role-based access, and per-user cost attribution for Claude Code.

The gateway is built and shipped by Anthropic inside the same `claude` binary developers already install, so it runs in one stateless container; because the gateway and the client are built together, the `/login` flow is gateway-aware, the client applies managed settings automatically at sign-in, and policy is enforced consistently on every request.

 This shifts the governance model from per-developer credential management to IdP-managed membership: 

onboarding a developer means adding them to your Identity Provider; offboarding means removing them.

 Rounding out the security story, 

Claude adds Trusted Devices for Remote Control for admins on Team and Enterprise plans to verify devices before remote Claude Code sessions — admins can now require members to verify their device before viewing or steering local Claude Code sessions remotely.



---

### ChatGPT / OpenAI: Codex Remote GA and the Mobile Approval Surface

OpenAI's most interaction-design-significant release of the window is the June 25 general availability of **Codex Remote**, which fundamentally changes the temporal and spatial contract of a long-running agentic coding session. 

Codex Remote is now generally available on all ChatGPT plans: from the ChatGPT mobile app, users can start or continue work on a connected Mac or Windows host, review progress, and approve actions from their phone; Remote Control now uses authenticated one-to-one QR pairing between each supported mobile device and each host.



The trust design of the QR pairing mechanism is the release's most consequential UX decision. 

The launch replaces the previous remote-shell connection approach with a purpose-built relay architecture designed to keep development machines inaccessible to the public internet while remaining reachable from anywhere a developer happens to be.

 The practical effect is that Codex tasks no longer require the developer to be physically present: 

for the more than 5 million developers who already use Codex each week, approving an agent action, steering a long-running task, or reviewing a set of diffs no longer requires sitting at the machine where the code is running.

 This establishes a new interaction pattern — the *mobile approval surface* — in which the phone becomes not a secondary device for consuming AI output but the primary human-in-the-loop gate for consequential agentic actions running on a more capable host machine.

Alongside Remote GA, 

the new DigitalOcean Droplet Workspace plugin lets Codex provision a DigitalOcean Droplet, configure SSH access, and connect it to the Codex app as a remote workspace.

The plugin addresses a specific friction point: developers who want to hand off heavy or long-duration tasks to a cloud machine without maintaining separate infrastructure can now do it directly from within Codex; tasks running on a Droplet are not affected by host sleep or network interruptions on the developer's local machine.

 The UX implication is a new dimension of temporal persistence: agent sessions are now detached not only from the developer's attention (via mobile review) but from the developer's hardware (via cloud-resident execution). Also shipping in this window: 

Sites is now available in preview in the Codex app, allowing users to create, save, deploy, and inspect websites, dashboards, internal tools, web apps, and games hosted by OpenAI; ChatGPT Business workspaces include Sites by default, and Enterprise admins can enable it through role-based access control.

 This establishes Codex as a deployment target, not merely a development tool — a meaningful expansion of the agentic workspace surface.

---

### Google Gemini: Dynamic View and the On-Demand UI Paradigm

Google's most structurally novel UX release of the window is the rollout of **Dynamic View** and **Visual Layout** as Labs experiments in the Gemini app — a shift that recasts the AI response surface from a text container into a *per-prompt generative interface layer*. 

Generative UI is a powerful capability in which an AI model generates not only content but an entire user experience; Google's implementation dynamically creates immersive visual experiences and interactive interfaces — such as web pages, games, tools, and applications — that are automatically designed and fully customized in response to any question, instruction, or prompt.



The two features occupy distinct positions on the generativity spectrum. 

The experimental feature called Visual Layout generates an immersive, magazine-style view of information, complete with photos and interactive modules; the experimental feature called Dynamic View can use advanced agentic coding capabilities to design and code a unique, single-purpose experience with a user interface that's perfect for a specific prompt — users can then tap, scroll, and learn via this interactive response.

 The distinction is design-consequential: Visual Layout is a *formatting layer* that makes text responses more browsable; Dynamic View is a *fabrication layer* that builds a purpose-built micro-app on request and discards it when the conversation ends. 

When using Dynamic View, Gemini designs and codes a fully customized interactive response for each prompt using Gemini's agentic coding capabilities; Generative UI experiences are also integrated into Google Search starting with AI Mode, unlocking dynamic visual experiences with interactive tools and simulations generated specifically for a user's question.

 The UX implication is a dissolution of the boundary between "AI response" and "application": instead of an AI explaining how to visualise data, the AI builds the visualisation widget inline and hands control to the user. 

Some users can expect to see visual layout or dynamic view in the tool menu of the Gemini app soon; Google believes that the best way to answer a question isn't always a text-based response, and by creating dynamic, interactive interfaces on the fly, users can explore information in a way that is more intuitive and tailored to their specific needs.

 Alongside these interface experiments, 

Gemini in Chrome on Android (including Nano Banana and auto browse) is launching in late June, initially available on devices with 4GB of RAM or more; auto browse for Android lets users automate digital chores such as appointment booking to party planning and finding in-stock items, all from an Android phone.



---

### Microsoft Copilot: Cowork GA and the Metered Delegation Contract

Microsoft's most consequential UX event of the June window is the June 16 general availability of **Copilot Cowork**, which repositions Copilot from a chat-adjacent assistant into a metered, delegated labor platform with its own cost governance infrastructure. 

Copilot Cowork, an agentic system that plans, executes, and delivers real work, is now generally available worldwide; users define the task, and Cowork executes it from start to finish, returning a completed deliverable rather than a draft or recommendation; powered by Work IQ, Cowork grounds every task in the systems a business already runs on; Cowork is enabled via usage-based billing, and administrators can use the new Cost Management Dashboard in the Microsoft 365 admin center to monitor credit usage, manage budgets, and control spend.



The interaction model is a structural shift from the "Copilot as advisor" paradigm to "Copilot as executor." 

Copilot Cowork executes complex, long-running, multi-tool tasks — you define the work and Cowork runs it end-to-end and returns a completed result, not just a draft or a recommendation.

 The entry point design matters: 

the Microsoft 365 Copilot app now includes a toggle that takes you into Cowork's full experience so you can move from chat to action faster than ever before.

 The governance architecture is explicitly consumption-based: 

you are billed on a usage basis, denominated in Copilot Credits, and the price for each task is calculated from four inputs: model use, context retrieval, tool calls, and runtime.

Cowork can automatically choose the best AI model based on the task provided, supports more plugins than before, and enables users to define custom skills for specialized work; other enhancements include the ability to create and edit visuals, leverage the Edge browser, and send push notifications on mobile for long-running tasks on Android and iOS.

 The compliance architecture at GA is comprehensive: 

Cowork supports sensitivity label inheritance and display, audit logging, interaction content in Data Security Posture Management Activity Explorer, Insider Risk Management of user risks associated with Cowork interactions, as well as eDiscovery, Data Lifecycle Management, and Communication Compliance.

 Within the broader Copilot surface, 

when the Researcher agent is added to a Copilot chat, users can now choose from supported Researcher models and modes directly in the conversation — putting control over depth and approach in the user's hands for each research task and giving teams more flexibility to match the model to the job.



---

### Grok (xAI): Agent Dashboard Overhaul and the `/goal` Long-Running Mode

xAI's most interaction-design-significant release of the window is a comprehensive overhaul of the **Grok Build agent dashboard**, which transforms the terminal-adjacent coding agent surface from a flat session list into a structured, observable orchestration interface. 

The agent dashboard now shows each agent's model and mode in the peek panel, lets you cycle modes with Shift+Tab, collapses the Inactive section by default, and hides older idle agents behind a "N more" row; tool usage cards for search, directory listing, file deletion, and glob now render as distinct typed cards instead of generic MCP entries.



The significance of typed tool cards as a UX primitive should not be understated. Until this release, tool calls in Grok Build rendered as undifferentiated MCP entries — offering no visual distinction between a web search, a file deletion, or a directory listing. 

The keyboard shortcuts help now shows richer descriptions and correctly scrolls wrapped text in the detail view; users can now pass `--json-schema` to `grok -p` and receive a validated JSON object instead of free text.

 This shifts the session audit trail from an opaque log into a legible, typed record of what each agent did. Alongside the dashboard, 

xAI introduces `/goal` in Grok Build, a new long-running autonomous mode for handing off larger implementation tasks

 — a direct counterpart to OpenAI's Goal Mode in Codex, establishing that outcome-oriented, persistent task delegation is now a cross-platform pattern rather than a single-vendor bet. 

Local plugins installed from your home directory are now automatically refreshed when you start a session, so new agents or skills added to the source appear immediately

 — a small but meaningful improvement for teams actively building and iterating agent skill libraries, closing the restart-to-reload loop that had slowed iterative plugin development.

---

### Perplexity: Hybrid Inference Routing and the Data-Residency UX

Perplexity's most architecturally significant active development in this window is the **hybrid local-server inference orchestrator** announced at Computex, which introduces a new class of trust UX decision that no other major AI product has yet shipped at scale. 

Perplexity AI announced what it calls the first hybrid local-server inference orchestrator at Computex 2026, designed to automatically route AI tasks between a user's local device and cloud-based frontier models without requiring the user to decide in advance.



The trust design is the central UX story. 

Perplexity describes this local model as deciding "when sensitive data should also be kept locally," and the system is designed to ask for user permission before sending sensitive tasks to the cloud — directly addressing a specific concern enterprises have about agentic AI: data governance and knowing where data goes and who controls that decision; examples of data the system is intended to keep local include financial records, health information, and personal files.

The feature is expected to come to Perplexity Computer in July 2026.

 The interaction design shift is from *user-unaware cloud delegation* to *consent-gated compute routing*: rather than silently sending every subtask to frontier cloud models, the system exposes the routing decision to the user at the moment when personal data is in scope. This establishes a new permission primitive for agentic workflows — not "do you allow this agent to use this tool?" but "do you allow this subtask to leave your device?" Meanwhile, 

Perplexity Computer is now available directly inside Word, Excel, PowerPoint, Outlook, and Teams, bringing AI workflows into the Microsoft 365 apps used by hundreds of millions of people every day; Microsoft 365 users can now use Computer to draft documents, analyze spreadsheets, build presentations, and manage communication using the context already across their files, emails, and workflows.



---

## The Bigger Picture: Keyless Agents, Generative UI, and the Mobile Approval Surface

The 48 hours ending June 25, 2026 describe a single, coherent maturation moment across every major agentic AI platform: the work of building agent capability is substantially complete, and the work now underway is building the *legibility and control infrastructure* that makes those capabilities safe to delegate at scale. Anthropic's WIF and Claude Apps Gateway solve the *identity problem* at the credential layer — every agent workload now has a unique, short-lived, auditable identity rather than sharing a static key, and every developer in an enterprise deployment is governed through the IdP the organisation already operates. OpenAI's Codex Remote GA solves the *temporal control problem* at the hardware layer — a developer can now approve, steer, or halt a long-running agent task from a mobile phone, making the human-in-the-loop gate portable rather than device-bound, while the DigitalOcean Droplet plugin extends the agent's execution surface into always-on cloud infrastructure. Google's Dynamic View and Visual Layout solve the *response legibility problem* at the interface layer — rather than returning undifferentiated text, Gemini now generates custom interactive UIs that are structurally appropriate to what the user asked for, treating the interface itself as a generated artifact rather than a fixed container. And Microsoft's Copilot Cowork GA solves the *delegation economics problem* — by binding agentic task execution to per-task consumption billing, a Cost Management Dashboard, and Purview compliance coverage, it makes delegated multi-step work auditable, budgetable, and governable in the same administrative framework as every other enterprise workload. What connects these four stories is a shared architectural conviction: that the highest-value investment in agentic AI in mid-2026 is not more capability but more *accountability surface* — the design of the systems by which organisations can see what their agents did, who authorised it, what it cost, and how to stop it.

---

## References

[1] Anthropic. (2026). *Workload Identity Federation is now generally available on the Claude Platform*. [https://claude.com/blog/workload-identity-federation](https://claude.com/blog/workload-identity-federation)

[2] Anthropic. (2026). *Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud*. [https://claude.com/blog/introducing-the-claude-apps-gateway](https://claude.com/blog/introducing-the-claude-apps-gateway)

[3] Releasebot. (2026). *Claude Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[4] OpenAI. (2026). *Release Notes — OpenAI Products*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[5] OpenAI Developers. (2026). *Changelog — Codex*. [https://developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

[6] TechTimes. (2026). *OpenAI Codex Remote Goes Live for All Plans: Phone Control Now Secured by QR Relay*. [https://www.techtimes.com/articles/319201/20260627/openai-codex-remote-goes-live-all-plans-phone-control-now-secured-qr-relay.htm](https://www.techtimes.com/articles/319201/20260627/openai-codex-remote-goes-live-all-plans-phone-control-now-secured-qr-relay.htm)

[7] Google Research. (2026). *Generative UI: A rich, custom, visual interactive user experience for any prompt*. [https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)

[8] Gemini Apps Release Notes. (2026). *Gemini Apps release updates & improvements*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/)

[9] Chrome for Developers. (2026). *15 updates from Google I/O 2026: Powering the agentic web*. [https://developer.chrome.com/blog/chrome-at-io26](https://developer.chrome.com/blog/chrome-at-io26)

[10] Microsoft. (2026). *Copilot Cowork is now generally available*. [https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)

[11] Microsoft Community Hub. (2026). *What's New in Microsoft 365 Copilot — June 2026*. [https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what's-new-in-microsoft-365-copilot--june-2026/4529572](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what's-new-in-microsoft-365-copilot--june-2026/4529572)

[12] Neowin. (2026). *Here are all the new features added to Microsoft 365 Copilot in June 2026*. [https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/](https://www.neowin.net/news/here-are-all-the-new-features-added-to-microsoft-365-copilot-in-june-2026/)

[13] Releasebot. (2026). *Grok Build Updates by xAI — June 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[14] Releasebot. (2026). *xAI Release Notes — June 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] Releasebot. (2026). *Perplexity Release Notes — June 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[16] MarkTechPost. (2026). *Perplexity AI Introduces Hybrid Local-Server Inference Orchestrator for Personal Computer*. [https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/](https://www.marktechpost.com/2026/06/05/perplexity-ai-introduces-hybrid-local-server-inference-orchestrator-for-personal-computer-automatic-on-device-and-cloud-task-routing/)