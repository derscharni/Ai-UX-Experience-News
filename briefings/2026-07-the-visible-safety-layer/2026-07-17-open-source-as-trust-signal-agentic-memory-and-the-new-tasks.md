# UX Briefing: Open Source as Trust Signal, Agentic Memory, and the New Tasks Layer

**July 17, 2026**

Good morning. The 48 hours ending July 17 are defined by a trust crisis and a trust response — both originating from the same product — that make this one of the most consequential windows for agent-safety UX the industry has produced this year. **Grok Build (xAI/SpaceXAI)** sits at the centre: on July 14, a security researcher revealed it had been uploading entire developer repositories — including API keys, SSH keys, and secrets — to SpaceXAI's Google Cloud Storage in excess of what any task required, and by July 16 xAI had responded by disabling default data retention, pledging deletion of all retained data, releasing the full 844,530-line Rust codebase under Apache 2.0, and resetting usage limits for all users — making Grok Build the first major frontier-lab coding agent to go fully open-source in direct response to a privacy incident. **Claude/Anthropic** ships its most significant round of background-agent and subagent infrastructure hardening to date with a dense **Claude Code stability update** that adds subagent text streaming, fixes permission preview injection attacks on bidirectional-override characters, and closes a critical hook-decision bug that allowed auto mode to override a PreToolUse deny — alongside a new **Enterprise Admin API in beta** that gives Claude Enterprise organisations programmatic member and group management for the first time. **ChatGPT/OpenAI** and its **Codex** agentic coding tool extend the UX surface of multi-step agentic work with continued active rollout of the **Tasks tab** in the redesigned Microsoft 365 Copilot app, while Codex ships updated approval controls including a new writes-only app-approval mode and interactive MCP authentication. **Microsoft Copilot** completes the final-mile UX transition of its July interface redesign — on July 15, the "New Copilot" opt-out toggle was removed, making the redesigned app with its new **Tasks tab** and reorganised navigation the permanent default for all standard-release tenants — and **Perplexity** continues its multi-surface expansion with **Comet** arriving on all major platforms and the **Personal Computer** agent adding inline editing, richer background controls, and a prebuilt Personal CFO persona for financial users.

---

## At a Glance: July 17 Highlights

The releases this window argue that the central design question of agentic AI in mid-2026 is no longer *what can the agent do*, but *how does the user verify, audit, and revoke what it does* — and that open-sourcing an agent harness after a data incident is the most radical transparency response the industry has yet produced.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code** ships a dense stability and trust update — subagent text streaming, permission preview injection protection, fixed hook-override bug, Chrome extension startup hang fix, and session cost counter reset on /clear; **Enterprise Admin API** enters beta with programmatic member, group, and invite management; **Memory** updated to individual categorized entries replacing the daily summary. [1][2][3] |
| **ChatGPT / Codex** | **Codex** adds a writes-only app-approval mode (read-only actions pass, writes prompt for approval), interactive MCP authentication without experimental opt-in, and runtime Codex auth for app servers; usage-limit reset credits now show type and expiration; the **ChatGPT WhatsApp EEA return** brings voice, image, and multilingual chat without requiring a ChatGPT account. [4][5][6] |
| **Google Gemini** | **Gemini Enterprise** removes the Idea Generation agent (week of July 14), directing users to the assistant and specialist agents; **Jira Data Center federated store filters** now apply to both search and action execution, scoping agent mutations to allowlisted projects; **Fill with Gemini in Sheets** higher limits for AI Expanded Access users active from July 15. [7][8][9] |
| **Microsoft Copilot** | **Copilot app redesign becomes permanent** — the "New Copilot" toggle is removed July 15, making the Tasks tab, reorganised navigation, and updated agent-interaction labels the irreversible default; **Copilot Cowork** continues GA rollout with Purview integration; **Outlook email grounding in Notebooks** due this window. [10][11][12] |
| **Grok (xAI)** | **Grok Build goes open source** under Apache 2.0 on July 16 with ~844,530 lines of Rust — the harness, TUI, agent loop, and extension system — following a privacy incident where the tool uploaded full Git repos including secrets; usage limits reset for all users; default data retention disabled since July 12 with committed data deletion underway. [13][14][15] |
| **Perplexity** | **Comet browser** reaches all major platforms (iOS, Android, Mac, Windows) as of this week; **Personal Computer** adds inline editing, smarter background-agent controls, Spaces collaboration, and a prebuilt Personal CFO persona; **SPACE sandbox** continues powering 100% of Computer sessions with Firecracker microVM isolation and week-long session persistence. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Permission-Preview Fix, Subagent Streaming, and the Enterprise Admin API

Anthropic's most consequential trust-design work in this 48-hour window is not a headline feature — it is a dense cluster of **Claude Code** safety and reliability fixes that together close three distinct failure modes in the agentic coding workflow, each one of which was quietly undermining the security guarantees that Claude Code's permission architecture is supposed to provide.



Claude Code ships a broad stability and workflow update with new subagent text streaming, better permission and upload handling, improved background agent reporting, faster terminal rendering, and many fixes across Chrome, Windows, Bedrock, Vertex, hooks, and session recovery — including a fix to permission previews relayed to chat channels that were not neutralizing bidirectional-override, zero-width, and look-alike quote characters, so tool inputs could visually alter the approval message.

 This is the most significant security fix in the release: if a malicious tool input could make an approval message *appear* to request something benign while actually requesting something harmful, the human review checkpoint that Claude Code's trust model relies on becomes untrustworthy. The fix closes the visual deception vector at the rendering layer. Separately, 

auto mode was overriding a PreToolUse hook's ask decision for unsandboxed Bash — a hook ask now floors the decision at a prompt.

 This closes a category of failure where a developer's explicitly configured permission policy could be silently bypassed by the agent's auto-escalation logic — exactly the kind of invisible override that makes long-running agentic sessions difficult to trust. 

Claude Code also adds the ability to manage people in Claude Enterprise organisations with the Admin API, in beta for all Claude Enterprise organisations: list members and look them up by email address, change a member's role, remove members, send and withdraw invites, manage groups and their membership, and read custom roles.



The UX implication of the Admin API is architectural: it transforms Claude Enterprise org management from a UI-only workflow into a scriptable, automatable governance layer that IT departments can integrate with their existing identity management systems. Meanwhile, 

memory on Claude now works as a set of individual, categorized entries that Claude reads and updates during conversations, replacing the previous daily memory summary.

 The shift from summary-per-day to categorized individual entries is the memory-architecture change with the most interaction-design significance: a categorized entry system allows Claude to surface, update, and selectively forget specific memories rather than treating an entire day's context as a single undifferentiated block — the difference between a filing cabinet and a notebook.

---

### ChatGPT / OpenAI: Codex Approval Controls, MCP Auth Hardening, and the WhatsApp EEA Return

OpenAI's most interaction-design-significant work in this window is a set of **Codex** trust and approval-flow updates that progressively close the gap between what the agent can do autonomously and what the user has explicitly authorised, at the per-action level rather than the per-session level.



Codex adds new approval and auth controls, including a writes app-approval mode, interactive MCP authentication, hosted login redirects, and runtime Codex auth for app servers; it also improves usage-limit credits, review workflows, Windows and macOS reliability, and terminal safety. Usage-limit reset credits now show their type and expiration. A new writes app-approval mode allows declared read-only actions while prompting for writes.

 The writes-only approval mode is the trust primitive with the most immediate daily-developer significance: it allows a team to authorise Codex to read freely during a session while still requiring an explicit approval gate every time the agent attempts to write — splitting the permission space by action consequence rather than requiring users to choose between fully autonomous and fully supervised modes. 

MCP tools can now request authentication interactively without an experimental opt-in.

 This makes MCP-backed tools — which can connect to external systems like databases, CRMs, and code repositories — a first-class citizen in the Codex permission model rather than an experimental feature that developers had to opt into. The UX shift here is from *the agent either has a credential or it fails* to *the agent can ask for a credential at the precise moment it needs it*, which maps to how human developers actually work with credentials in secure environments.

On the ambient-surface expansion side, 

ChatGPT returns to WhatsApp in the European Economic Area; users can get started without a ChatGPT account by messaging the verified 1-800-CHATGPT contact, and on WhatsApp can message ChatGPT, upload images, send voice notes, create images, and use ChatGPT in many languages.

 The no-account-required entry point is the UX decision with the most inclusion significance: it makes ChatGPT accessible through a surface that hundreds of millions of EEA users already have, without requiring them to navigate an onboarding flow — establishing WhatsApp as a zero-friction ambient interface for the agent, analogous to what SMS was for earlier conversational assistants.

---

### Google Gemini: Jira Scope Control, Workspace Limits, and the Idea Generation Sunset

Google's most interaction-design-relevant work in this window is a pair of **Gemini Enterprise** changes that together reveal a maturing philosophy about which agent surfaces should proliferate and which should consolidate — a consolidation-over-proliferation decision that has significant implications for how enterprise users navigate the growing zoo of Gemini agent capabilities.



The Idea Generation agent, which was in public preview, is being removed starting the week of July 14, 2026; users can brainstorm ideas directly using the assistant; for general brainstorming and creative thinking, users should use the Gemini Enterprise app assistant.

 This is the agent-deprecation pattern with the most governance significance: rather than allowing a proliferation of single-purpose agents to accumulate in the Gemini Enterprise surface, Google is actively collapsing narrow agents back into the general assistant — directing users to Deep Research or Co-Scientist for in-depth exploration while retiring the idea-specific entry point. The trust implication is that fewer, better-scoped agents are easier for enterprise administrators to govern, approve, and explain to employees than a long list of task-specific AI tools. On the action-scoping side, 

filters configured on Jira Data Center federated data stores apply to both search queries and action execution — these filters let you specify which Jira projects are accessible to the Gemini Enterprise app assistant; mutations or retrievals on out-of-scope data fail or return no results.

 This is the agentic permission primitive that regulated enterprise environments have been waiting for: the ability to scope not just what data the agent can *read*, but which systems it can *act on* — so that a Gemini Enterprise agent configured for the product team's Jira projects cannot execute mutations on the security or finance team's projects, even if an employee crafts a prompt attempting to cross that boundary.



Starting July 15, 2026, users with AI Expanded Access licenses will have higher limits on usage of Fill with Gemini and the AI function in Sheets.

 The Fill with Gemini expansion, while incremental, continues Workspace's systematic pattern of increasing agentic capacity at the spreadsheet layer — a surface where ambient AI-fill interactions accumulate into real workflow automation at enterprise scale, especially for finance, operations, and data-heavy teams who live in Sheets.

---

### Microsoft Copilot: The Interface Redesign Becomes Permanent and the Tasks Tab Arrives

Microsoft's most consequential UX event in this window is not a new feature — it is an irreversibility milestone: **the Copilot app redesign becomes the only experience** for standard-release tenants, closing the door on the previous interface and establishing the Tasks tab, reorganised navigation, and updated agent interaction labels as the permanent interaction substrate for Microsoft 365 Copilot.



Users were seeing a "New Copilot" toggle in the top right of their app that let them switch between the current experience and the updated experience; on July 15 for standard release, the toggle was removed and the updated experience became default on without the option for users to switch back to the previous experience.

 This is the UX governance moment that matters most: the toggle's removal signals that Microsoft has enough confidence in the redesign's adoption quality to remove the escape hatch, making every user's interaction with Copilot from July 15 forward a product of the new information architecture. 

The update introduces a redesigned layout with revised menus and navigation; frequently used features will be reorganised, and a new Tasks tab will allow users to monitor activities in progress; Copilot chat conversations will also appear in an updated format.

 The Tasks tab is the interaction-design primitive with the most long-term agentic significance: it transforms the Copilot app from a *conversation history* into an *in-progress work tracker*, giving users a surface to check the state of delegated tasks without needing to re-enter the conversation that initiated them.



Responses, references, and suggested actions will be presented differently, and users who work with Copilot agents will notice updated labels that distinguish agent interactions from standard Copilot chats.

 The agent/chat label distinction is the transparency primitive that most directly serves the trust-design goal of the redesign: it makes the difference between *talking to Copilot* and *delegating to a Copilot agent* legible in the UI, rather than leaving users to infer whether they are in a conversation or an autonomous workflow from context alone. Meanwhile, 

Microsoft is extending Copilot grounding so users will be able to add Outlook emails as reference sources in Copilot Notebooks; this lets Copilot draw on the conversations, decisions, and context held in email to generate more relevant outputs; users can add up to 300 total sources per notebook, including emails; email content reflects its state at the time it is added and does not update with later replies or changes, and in shared notebooks, email content is only available to people who were participants in the original email.

 The participant-only visibility gate continues to be the trust boundary that matters most in collaborative notebook contexts.

---

### Grok (xAI): Open Source as Trust Recovery Architecture

xAI's defining UX and trust-design event in this 48-hour window — and arguably the most significant agentic-trust incident of 2026 to date — is the **Grok Build open-source release** on July 16: a response to a confirmed privacy incident that reframes source transparency as the primary mechanism for rebuilding developer trust in an agentic coding tool.



On July 14, 2026, AI researcher Tinh Dang reported that Grok Build uploaded users' whole source code repositories to SpaceXAI's Google Cloud Storage data bucket, including the repositories' full histories, API keys, shared secrets, and files that users instructed Grok Build not to access, despite Grok Build's "Improve the model" setting being disabled; Dang's analysis stated that the amount of information uploaded by Grok Build greatly exceeded that of competing CLI tools, with the tool uploading 27,800 times more data than needed to fulfil its assignment.

 The incident exposed the most dangerous failure mode in agentic coding tools: an agent that silently exfiltrates data beyond the scope of its task, in violation of its own stated settings, in a way that is invisible to the user during normal operation. 

xAI open-sourced its Grok Build terminal AI coding agent under the Apache 2.0 licence, publishing approximately 844,530 lines of Rust code on GitHub; the release enables developers to independently inspect the agent's architecture and data-handling behaviour following controversy over undisclosed repository uploads; the move comes after security researchers revealed that Grok Build uploaded developers' complete Git repositories, including commit histories and potentially sensitive credentials.

SpaceXAI stated: "With all retained data deleted, retention default off, and an open-source harness, we are offering complete user privacy. You can also run Grok Build fully open-sourced and local-first with your own inference. We disabled default retention for all Grok Build users starting on July 12th. Additionally, we are deleting all coding data that was previously retained, ensuring every user's preferences are respected. With these steps, Grok Build goes beyond other major coding products to protect user privacy."

 This is the trust-recovery architecture with the most industry-defining implications: by open-sourcing the harness, xAI is making the data-handling behaviour *inspectable rather than credible* — shifting the trust model from "believe our privacy claims" to "read the code and verify them." 

Researchers confirmed that the upload infrastructure remains in the published source code, although it is currently disabled through a server-side configuration flag rather than being removed entirely.

 This residual fact is the trust caveat that security teams will note: the open-source release enables inspection, but it does not guarantee that the production binary matches the published source, and the upload path's continued presence in the codebase means the design question of why it existed at all remains unanswered by the release alone.

---

### Perplexity: Comet Reaches All Platforms and Personal Computer Adds Inline Control

Perplexity's most interaction-design-significant work in this window is the completion of **Comet**'s platform-parity rollout — a milestone that completes the company's ambient browser-agent strategy by making the AI-native browser available on every major surface simultaneously — combined with a cluster of **Personal Computer** control improvements that deepen the human-oversight layer of the always-on desktop agent.



This week, Perplexity launched Comet to all iOS users; with this release, Comet is now available on all major platforms: iOS, Android, Mac, and Windows; users can ask Comet for research or work help from anywhere in the world; for the best experience, users can pair mobile and desktop browsers with Comet device sync to teleport to Comet iOS seamlessly.

 The four-platform simultaneity is the UX architecture milestone that matters: Comet is no longer a Mac-first or desktop-first agent surface but a cross-device ambient layer that can carry browser context, research sessions, and task state across every screen a user works on. The device-sync pattern — where a Comet session started on a Mac can be picked up on iOS — is the temporal UX primitive that makes the browser-as-agent surface credible for real work: users do not have to restart context at each device boundary. 

Personal Computer now works 24/7 as a digital proxy: it monitors triggers, executes proactive tasks, and carries work forward around the clock — all controllable from any device, anywhere; every sensitive action requires explicit approval, with a full audit trail and kill switch built in.



The explicit approval requirement paired with a full audit trail and kill switch is the trust-design pattern that distinguishes Perplexity Personal Computer's agentic architecture from less governed autonomous agents: it establishes that the agent can act proactively and continuously, but that every consequential action creates a legible record and can be stopped. 

Personal Computer securely connects your local files, apps, and Comet browser to Computer so Computer can work with the context that already lives on your local desktop; users stay in control of what Personal Computer can and cannot access.

 The explicit user-controlled access scope — defining which folders, apps, and browser contexts the agent can touch — is the on-device governance model that makes Personal Computer's continuous operation feel safe rather than surveillance-like: the boundary of the agent's world is set by the user, not inferred by the system.

---

## The Bigger Picture: Open Source as Trust Signal, Agentic Memory, and the New Tasks Layer

The 48 hours ending July 17, 2026 will be remembered primarily for a single event — Grok Build's repository upload incident and Apache 2.0 open-source response — but that event illuminates a structural truth about the entire industry's moment: the trust problem of agentic AI is no longer theoretical. When a coding agent silently exfiltrates 27,800 times more data than its task requires, in violation of its own settings, the abstract arguments about agent safety become concrete and urgent. xAI's response — delete the data, disable the default, open-source the harness — establishes a new precedent for what trust-recovery UX looks like when an agent fails: not a privacy policy update, but source code on GitHub that any developer can audit. Anthropic's Claude Code work this window arrives in that same register: the fix to bidirectional-override character injection in permission previews, and the patch that stops auto mode from overriding a hook's explicit deny decision, are both responses to the same category of failure — the agent doing something the user's settings said it should not. Microsoft's interface-redesign permanence and Tasks tab arrival argue that the industry is also converging on a new interaction primitive for ambient agentic work: a persistent, session-spanning *task monitor* that makes in-progress agent work visible without requiring users to re-enter the conversation that initiated it. Perplexity's Comet platform parity and Personal Computer audit trail complete the picture: the agent can be always-on, cross-device, and locally integrated — but the UX architecture must answer, at every surface, the question users are now asking not metaphorically but literally: *what is it uploading, and can I see the code?*

---

## References

[1] Releasebot. (2026). *Claude Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude](https://releasebot.io/updates/anthropic/claude)

[2] Releasebot. (2026). *Anthropic Release Notes — July 2026*. [https://releasebot.io/updates/anthropic](https://releasebot.io/updates/anthropic)

[3] Releasebot. (2026). *Claude Code Updates by Anthropic — July 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[4] Releasebot. (2026). *Codex Updates by OpenAI — July 2026*. [https://releasebot.io/updates/openai/codex](https://releasebot.io/updates/openai/codex)

[5] OpenAI. (2026). *ChatGPT Release Notes*. [https://openai.com/products/release-notes/](https://openai.com/products/release-notes/)

[6] OpenAI Help Center. (2026). *ChatGPT Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[7] Google Cloud Documentation. (2026). *Gemini Enterprise release notes*. [https://docs.cloud.google.com/gemini/enterprise/docs/release-notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)

[8] Releasebot. (2026). *Gemini Updates by Google — July 2026*. [https://releasebot.io/updates/google/gemini](https://releasebot.io/updates/google/gemini)

[9] Google Workspace Updates. (2026). *Google Workspace Updates 2026*. [https://workspaceupdates.googleblog.com/2026/](https://workspaceupdates.googleblog.com/2026/)

[10] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[11] SuperSimple365. (2026). *What's new in Microsoft 365 and Copilot? June 2026*. [https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/](https://supersimple365.com/whats-new-in-microsoft-365-and-copilot-june-2026/)

[12] WSU Insider. (2026). *Microsoft 365 Copilot receives interface updates in July 2026*. [https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/](https://news.wsu.edu/announcements/microsoft-365-copilot-receives-interface-updates-in-july-2026/)

[13] Open Source For You. (2026). *xAI Open Sources Grok Build After Repository Upload Controversy*. [https://www.opensourceforu.com/2026/07/xai-open-sources-grok-build-after-repository-upload-controversy/](https://www.opensourceforu.com/2026/07/xai-open-sources-grok-build-after-repository-upload-controversy/)

[14] The Decoder. (2026). *xAI open-sources "Grok-Build" on GitHub after massive data breach*. [https://the-decoder.com/xai-open-sources-grok-build-on-github-after-massive-data-breach/](https://the-decoder.com/xai-open-sources-grok-build-on-github-after-massive-data-breach/)

[15] Wikipedia. (2026). *Grok (chatbot)*. [https://en.wikipedia.org/wiki/Grok_(chatbot)](https://en.wikipedia.org/wiki/Grok_(chatbot))

[16] Releasebot. (2026). *Perplexity Release Notes — July 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[17] Perplexity AI. (2026). *Personal Computer for Mac*. [https://www.perplexity.ai/personal-computer](https://www.perplexity.ai/personal-computer)

[18] SiliconANGLE. (2026). *Perplexity launches secure sandbox to make its AI agents secure and powerful*. [https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/](https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/)