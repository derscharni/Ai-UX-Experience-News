# UX Briefing: Memory, Oversight, and the Agent Safety Layer

**June 11, 2026**

Good morning. Today's briefing is defined by a quiet but consequential pivot: every major platform shipped at least one feature in the last 48 hours that is explicitly designed to tell users more about what their AI knows, what it has done, and what it is permitted to do next. ChatGPT rolls out **Active Sessions** — a new security dashboard surfacing every live ChatGPT, Codex, and API session associated with an account — alongside **Lockdown Mode**, an opt-in prompt-injection defence that limits agent access to the web and external services; Claude's platform continues its verticalization push with a **Foundation Models framework integration** that brings Claude reasoning natively into Apple's Swift development environment, extending its Cowork agent footprint; Microsoft's **Copilot Notebooks** redesign rolls out worldwide, collapsing chats, outputs, and references into a single persistent project surface; and Perplexity's **Comet** browser hits a decisive UX inflection, with the Amazon vs. Perplexity Ninth Circuit oral arguments on agent access rights scheduled for today — a legal ruling that will directly define the boundaries of agentic browsing interaction design. The through-line is trust architecture: not capability expansion, but a hardening of the scaffolding that lets users understand, verify, and constrain agents that are now operating continuously inside their accounts, browsers, and documents.

---

## At a Glance: June 11 Highlights

This week's releases converge on a single design problem: as agents become ambient — running across accounts, browsers, and apps around the clock — the industry urgently needs user-facing mechanisms for understanding what the agent knows, what it has accessed, and where its authority ends.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | Anthropic ships **Foundation Models framework** support for Apple developers via a new Swift package, letting on-device typed outputs hand off to Claude for multi-step reasoning and streaming responses in SwiftUI; Claude's legal MCP rollout continues to establish **Cowork** as the leading vertical agent workspace for knowledge work functions. [1][2] |
| **ChatGPT** | OpenAI rolls out **Active Sessions** — a settings-level dashboard showing every live ChatGPT, Codex, and API session — plus **Lockdown Mode**, an opt-in security setting limiting web and external service access to reduce prompt injection risk. [3][4] |
| **Google Gemini** | The **Antigravity CLI** replaces Gemini CLI for Google AI Pro/Ultra users starting June 18, introducing asynchronous multi-agent orchestration and a unified agent harness shared with the Antigravity desktop app; Gemini **auto browse** for Android remains on track for late-June launch. [5][6] |
| **Microsoft Copilot** | **Copilot Notebooks** redesign begins worldwide rollout, bringing chats, output creations, and references together in a single project-organised workspace; the M365 Copilot app prompt-line redesign continues shipping, transforming the static text box into a task-aware workspace. [7][8] |
| **Grok (xAI)** | Grok Build v0.2.20 remains the current stable release, consolidating the session-state and monitor-visibility changes covered since June 3; xAI's homepage confirms new posts on June 9 and June 10, with Grok 4.3 as the current API flagship and Grok V9-Medium mid-June upgrade on approach. [9][10] |
| **Perplexity** | **Comet** reaches a legal inflection point as Amazon v. Perplexity Ninth Circuit oral arguments are scheduled today, setting the first federal precedent on whether agentic browser access is user-authorized or unauthorized computer access; the Comet trust-transparency model — live blue-frame visual indicators showing exactly what the agent is reading — continues to define the category's UX benchmark. [11][12] |

---

## Product Highlights

### ChatGPT / OpenAI: Session Visibility and the Prompt-Injection Firewall

OpenAI's most interaction-design-significant move in the past 48 hours is not an agent capability but an agent *accountability* feature. 

ChatGPT has introduced **Active Sessions**, a new security feature that lets users review account sessions and sign out of ones they don't recognize, showing session details like device, location, sign-in time, trusted status, and current session info.

 Crucially, 

Active Sessions covers ChatGPT, Codex, and API Platform sessions where available

 — meaning for the first time, users can see a unified view of every surface where their ChatGPT identity is currently active, including coding agents running in the background. This shifts the UX from "assume your session is private and singular" to *a reviewable, revocable inventory of every active agent context.*

The second and arguably more structurally important release is **Lockdown Mode**. 

ChatGPT introduces Lockdown Mode for all logged-in users — an optional opt-in advanced security setting that limits access to the web and external services to help reduce the risk of data exfiltration from prompt injection attacks.

 This is a meaningful trust-design primitive: it gives users a clearly named, zero-friction escape hatch when operating in contexts where they do not want the agent touching the network. The pattern being established is *scoped agent authority* — rather than a global capability toggle, Lockdown Mode creates a defined secure perimeter within which the agent is still useful but cannot be weaponised by malicious prompt content in external documents or web pages. For enterprise users managing sensitive workflows, this is the first genuinely user-operable defence against what is currently the leading class of agentic security failure.

Together, Active Sessions and Lockdown Mode describe a coherent oversight layer: a user can now see every place their AI identity is live (Active Sessions), and selectively reduce what those sessions can do in high-risk moments (Lockdown Mode). This is the clearest expression yet of a *renewable, bounded authority* model applied to consumer AI — the user does not choose once at setup; they review, revoke, and constrain on an ongoing basis.

---

### Claude / Anthropic: The Apple Developer Handoff and Vertical Agent Depth

Anthropic's most noteworthy recent interaction design move is one of platform reach rather than feature addition: 

Claude is adding Foundation Models framework support through a new Swift package that lets Apple developers use Apple's Foundation Models framework to call Claude for more complex workflows.

This works through Apple's Foundation Models framework on iOS 27, iPadOS 27, macOS 27, visionOS 27, and watchOS 27; developers add it to their project, sign in with an Anthropic API key, and pass typed outputs from Apple's on-device pass into a Claude request — the package handles streaming, tool calls, and structured responses back into SwiftUI.



The interaction design implication is an emergent *hybrid agency* pattern: Apple's on-device model handles privacy-sensitive, low-latency tasks locally, then hands off to Claude when the task requires multi-step reasoning, code generation, or extended tool use. This mirrors Perplexity's local-cloud hybrid routing concept but operationalised inside a native development framework at the OS layer. Developers can now build agentic workflows that *automatically* escalate from on-device to cloud inference based on task complexity — without requiring users to understand or manage the routing. The trust dimension is inherited from Apple's platform privacy model: what stays on-device stays on-device, and what goes to Claude is governed by Anthropic's API policy.

On the vertical agent front, 

Anthropic has released 20+ new MCP connectors that link Claude to the software that the legal industry runs on and 12 new plugins tailored to specific legal work and practice areas.

In Claude Cowork, the same connectors and plugins are available for work that spans many documents; scheduled tasks can automate recurring work such as weekly regulatory update sweeps or intake triage; and with Projects, matter teams get a persistent workspace where precedents and prior drafts are retained across every conversation.

 The pattern here — persistent matter workspaces, scheduled sweeps, multi-document orchestration — is what distinguishes a *vertical agent workspace* from a general chat tool with plugins. Anthropic is systematically encoding domain-specific workflow structure into the agent's interaction model, so the agent knows not just what tools exist but in what sequence a legal workflow should invoke them.

---

### Microsoft Copilot: Notebooks as the Agent Project Surface

Microsoft's most operationally significant rollout in the current window is the worldwide expansion of **Copilot Notebooks**. 

The Copilot Notebooks design in the Microsoft 365 Copilot app has been updated to help organize chats and work by project; the new UI brings together chats, output creations, and references in one place so users can more easily collaborate and move work forward; and Copilot Notebooks in the Microsoft 365 Copilot app and in the OneNote app stay in sync, so users can move smoothly between experiences.

 This is Microsoft's answer to the scattered-context problem that has plagued knowledge-work AI since it arrived in the enterprise: conversations happen in one place, outputs appear somewhere else, reference documents live in a third location. Notebooks collapses that into a single persistent project artifact.

The accompanying M365 Copilot app redesign deepens the same principle at the prompt layer. 

The new designs shift Copilot toward a more connected, adaptive system by turning a once-static text box — the prompt line — into a task-aware workspace; within the Copilot app, the prompt line gives users more space to express their needs, while below it Copilot surfaces tools and controls to assist with the task at hand.

 This is a subtle but important interaction shift: from a text input that waits passively for queries to a context-sensitive surface that *proposes* relevant actions based on what the user is working on. The UX implication is a collapse of the distance between stating an intent and acting on it — the agent doesn't wait to be told what tools exist, it surfaces them contextually. On the governance side, 

Microsoft updated the AI disclaimer experience in Microsoft Copilot Chat based on customer feedback, introducing an admin control that allows organisations to customise how the disclaimer appears, improving user awareness and flexibility.

 Admins can now surface a bolded disclaimer with a link to their own AI policy documentation — a small but meaningful step toward organisation-specific trust signalling inside the agent UI.

---

### Google Gemini: The CLI Migration and the Agentic Architecture Unification

Google's most structurally important developer-facing UX event of the week is the formal transition from **Gemini CLI** to **Antigravity CLI**. 

Starting today, Antigravity CLI is available to everyone; on June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will stop serving requests for Google AI Pro and Ultra.

 The reason is architectural, and the UX rationale is explicit: 

Gemini CLI proved the terminal could be an incredible interface for agentic tasks, but user needs shifted — they now require multiple agents communicating with each other to split up the work and solve complex problems, meaning terminal tools need to share a unified backend with the rest of the workflow; listening to feedback made one thing clear: Google can serve users best by pouring energy into a single product built for today's multi-agent reality.



The UX upgrade Antigravity CLI delivers over Gemini CLI is explicit and consequential: 

asynchronous workflows let Antigravity CLI orchestrate multiple agents for complex tasks in the background, letting users run large-scale refactors or research several topics without locking up the terminal session; unified architecture shares the same agent harness as Antigravity 2.0, ensuring that all future improvements to core agents are automatically applied wherever users work.

 This is a terminal-as-async-agent-hub pattern — the user issues a task, the terminal hands it to a background multi-agent harness, and the session stays responsive. This shifts the mental model of the CLI from "command that blocks until done" to "dispatch that returns immediately and notifies on completion." On the consumer side, 

Gemini in Chrome on Android, including Nano Banana and auto browse, will be launching in late June, initially available on devices with 4GB of RAM; already available on desktops, auto browse for Android lets users automate digital chores so they can focus on more important tasks.



---

### Perplexity: Comet's Transparency Model and the Agent Legal Frontier

Perplexity's most consequential UX development today is not a product release but a courtroom: 

oral arguments before the Ninth Circuit in Amazon v. Perplexity are scheduled for June 11, 2026, and that ruling will set the first federal precedent on whether buyer-side AI agents can access third-party platforms at user direction.

 For the interaction design discipline, this is a defining moment. The question is whether the act of a user *delegating* a browser task to an agent constitutes authorised user access or unauthorised automated access — a distinction that will shape what agentic browsers are legally permitted to do on behalf of users and how consent flows must be designed.

The **Comet** browser's own interaction model is directly relevant here. 

One design detail worth noting in Comet: when the AI is reading content from a page, blue frames highlight exactly what it is reading — both a UX feature and a transparency mechanism; users can see in real time where the AI's attention is on the page; it is a small touch that builds a degree of trust that a black-box AI sidebar would not.

 This live-attention-highlighting pattern is the most concrete answer the industry has shipped to the question "how do I know what my agent is doing while it browses?" Meanwhile, 

Comet is also distinct from Perplexity Computer — Perplexity's separate agentic AI product that orchestrates 20+ frontier models and 400+ app connectors for deep workflow automation; Computer is built for backend task orchestration, Comet is the browser users use day to day.

 This two-product architecture — a visible, browsing-level agent and a background orchestration layer — maps cleanly to a *tiered delegation model*: users understand and see what Comet does in the foreground, while Computer handles the workflow automation they may less directly observe. Whether that distinction is legally sufficient is exactly what today's oral arguments will begin to determine.

---

### Grok (xAI): API Openness and the Build Agent's Expanding Footprint

xAI's most UX-relevant move in the extended window remains Grok Build's ongoing expansion of its agent API surface. 

xAI has made Grok Build 0.1, its fastest coding model, available via the xAI API in public beta; developers can now build directly on top of the same model that powers xAI's Grok Build CLI without needing a SuperGrok or X Premium+ subscription.

Grok Build 0.1 is a coding model specifically trained for agentic coding tasks, including web development, debugging, and MCP support; it is designed for multi-step workflows where an AI agent needs to plan, reason, and act — not just generate a block of code in response to a single prompt.



This API opening is a meaningful interaction design event in itself: it transforms Grok Build from an end-user CLI tool into an *orchestration primitive* that other agents and platforms can call programmatically. 

Full Agent Client Protocol (ACP) support means orchestration platforms can call Grok Build as a primitive — the same way they call Claude Code or Codex CLI.

 This establishes Grok Build not as a standalone user-facing coding assistant but as an interchangeable specialist that a higher-level agent orchestrator can route tasks to. The trust and visibility implication is significant: when your primary agent is handing subtasks to a specialist model the user may never directly interact with, the audit-trail question becomes "not just what did the agent do, but which agent did which part?" The v0.2.20 session-state improvements — structured compaction, monitor visibility, collapsible task panels — 

shipped June 3, 2026, making monitors visible and killable to the model and introducing structured compaction with successor-assistant carry-forward

 — remain the strongest answer in the field to exactly that auditability question.

---

## The Bigger Picture: Memory, Oversight, and the Agent Safety Layer

This week's releases, read together, describe the same underlying design challenge arriving from multiple directions simultaneously. ChatGPT's Active Sessions and Lockdown Mode are the most explicit expression of the shift: as AI agents become ambient — running inside accounts, coding agents, and browser sessions continuously — the user needs a *session management* layer analogous to what we built for online banking twenty years ago. Microsoft's Copilot Notebooks redesign answers the same problem from the workspace angle: when an agent works across many documents and conversations over days, the output has to accumulate somewhere reviewable, or it is irrecoverable. Perplexity's Comet live-attention model asks the most granular version of the question: can a user see, in real time, exactly what content the agent is reading in their browser? And the Ninth Circuit hearing today frames the legal boundary of the entire enterprise: at what point does user-delegated agentic action become unauthorised automated access, and who designs the consent flow that distinguishes them? Google's Antigravity CLI migration and Anthropic's Apple Foundation Models handoff both point toward the same architectural destination: agents are not individual tools anymore but layers in a stack, with on-device models escalating to cloud reasoning, cloud agents delegating to specialist subagents, and terminal orchestrators running background tasks across sessions. The design discipline's central question is no longer whether users can talk to an agent — they clearly can — but whether users can *audit, constrain, and recover from* an agent that is permanently, silently, consequentially active. Every product this week shipped one more answer to that question. The full answer is still being written — in product labs, in enterprise governance policies, and now in federal courts.

---

## References

[1] Releasebot. (2026). *Claude Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[2] Claude.com Blog. (2026). *Claude for the legal industry*. [https://claude.com/blog/claude-for-the-legal-industry](https://claude.com/blog/claude-for-the-legal-industry)

[3] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[4] OpenAI. (2026). *Introducing Trusted Contact in ChatGPT*. [https://openai.com/index/introducing-trusted-contact-in-chatgpt/](https://openai.com/index/introducing-trusted-contact-in-chatgpt/)

[5] Google Developers Blog. (2026). *An important update: Transitioning Gemini CLI to Antigravity CLI*. [https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)

[6] Chrome for Developers Blog. (2026). *15 updates from Google I/O 2026: Powering the agentic web*. [https://developer.chrome.com/blog/chrome-at-io26](https://developer.chrome.com/blog/chrome-at-io26)
