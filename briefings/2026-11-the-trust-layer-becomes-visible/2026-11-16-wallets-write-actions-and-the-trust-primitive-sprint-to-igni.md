# UX Briefing: Wallets, Write Actions, and the Trust-Primitive Sprint to Ignite

**November 16, 2026**

Good morning. The 48 hours ending November 16, 2026 are defined by four simultaneous design movements: **OpenAI** shipping **ChatGPT Wallet** on November 13 as the first native agentic payment surface on any major AI platform — dots agents can now complete purchases on users' behalf through a per-purchase biometric approval gate, a tokenised card architecture, and a confirmation-card UI that surfaces the merchant, items, total, and selected card before every transaction, with a planned future stage allowing pre-authorised spending caps; **Anthropic** delivering **Claude Code 2.1.325** on November 13 as the week's most consequential trust-design update to the agentic coding surface — flipping sandboxed Bash commands from auto-execute to permission-required by default and fixing a zstd decoding security issue, with the same update closing multiple background-session credential-bleed paths and arriving while the Sign in with Apple iOS registration flow remains interrupted; **Perplexity** completing **Teammates'** cross-platform expansion by landing on the Mac app on November 13, completing the web-iOS-macOS triangle in under two weeks and making persistent multi-agent background work accessible from the desktop without a browser tab; and **Microsoft Copilot** entering the final pre-Ignite hours — with connector write actions now GA in Chat and Cowork, the Autopilot timing still uncertain per Message Center, and the opening Ignite keynote by Satya Nadella starting tomorrow at 10:00 AM PT, expected to bring Autopilot GA and Frontier Transformation announcements. **Google**'s continued rollout of **Gemini Omni 1.2 Flash** — with native 15-second video generation, multi-turn conversational editing, and SynthID watermarking — has also been active in background developer and enterprise workflows across this window.

---

## At a Glance: November 16 Highlights

Today's window is defined by the industry arriving simultaneously at the transaction trust moment for agentic systems — the moment when agents move from performing information work to completing financial, destructive, and persistent-write actions on users' behalf, with each platform resolving the resulting trust gap through a different design primitive, from biometric approval gates to per-command permission prompts to connector-level confirmation cards, all in the same 48-hour window, with Microsoft Ignite opening tomorrow as the expected venue for the most consequential agentic-governance announcements of the November cycle.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Code 2.1.325 (November 13) flips the most consequential agentic default in the codebase: sandboxed Bash commands now follow the normal permission flow and stop to ask before executing, closing a path through which the agent could run code without explicit approval; the same update fixes a zstd decoding security issue, closes multiple background-session credential-bleed paths where sign-in tokens could migrate between profiles and billing contexts, and denies rules are now applied to permission approvals arriving after a restart in self-hosted runner and remote-control sessions; a Sign in with Apple failure on the Claude iOS app continues to affect new account registration** — the sandbox permission default-flip is the trust-design event of the week for agentic coding: by making permission-ask the new default for sandboxed Bash, Anthropic establishes that the agent must pause and present its intended action to the human before executing it, rather than the human having to remember to configure a restriction. [97-1,97-3,97-6,101-1,101-3,101-4,101-5,101-10,101-11,96-4,5-4,5-7] |
| **ChatGPT** | **ChatGPT Wallet launches November 13 for US Pro subscribers aged 18+: dots agents can complete purchases on a user's behalf using a tokenised substitute card number so neither the agent nor the merchant sees the real card; every purchase currently requires biometric approval (Face ID or Touch ID) after the user reviews the merchant, items, total, and selected card in a confirmation UI; the approval creates a persistent record of the purchase the user authorised; a future stage will allow spending limits, purchase categories, and time periods so agents can buy within pre-approved parameters without asking each time; Enterprise and Edu Dots admin preview closes November 18 with default-on rollout to follow; Locked Chats continues its phased rollout** — the per-purchase biometric-approval-with-confirmation-card design is the trust-primitive answer to the scariest part of agentic commerce: the agent never holds a real card number, every transaction requires an explicit human authorization signal, and each authorization creates an auditable record. [20-3,20-4,20-5,20-6,20-7,21-10,23-4,23-5,27-6,27-10,27-13,16-7,16-8] |
| **Google Gemini** | **Gemini Omni 1.2 Flash (GA since November 5) continues reaching enterprise workflows and developer pipelines — generating clips up to 15 seconds with synced dialogue, multi-turn conversational editing, and an invisible SynthID provenance watermark on every output; the model is rolling out in Flow, Google Vids, Google Ads, and the Gemini app for Ultra subscribers, with Provisioned Throughput available on Google Cloud; from December 3, requests to the gemini-omni-1.1-flash model ID are silently routed to 1.2 and billed at 1.2 rates** — the silent model-ID redirect on December 3 is the trust-design tension in this rollout: applications built on the 1.1 model ID will switch underlying model and billing rate without any interaction-layer notification, making the redirect deadline a governance event that enterprise developers need to anticipate. [103-4,103-7,103-8,103-9,104-4,104-5,105-9,105-10,105-11,110-5,110-16,110-17] |
| **Microsoft Copilot** | **Connector write actions reach GA in Copilot Chat and Cowork (November 9), enabling Copilot to create, update, and delete data in connected third-party applications including Jira, Notion, and Canva; by default, every write action requires the user's explicit approval via a confirmation card showing what Copilot has been asked to do before it runs; users can approve once or remember approval per tool; Researcher's federated connectors remain read-only; Microsoft Ignite 2026 opens tomorrow November 17 at Moscone Center, San Francisco with Autopilot GA, Work IQ updates, and Frontier Transformation as expected announcement categories** — connector write actions completing their GA rollout on the eve of Ignite establishes the interaction pattern — Copilot proposes a write action, surfaces a confirmation card, waits for human approval — that will govern the most consequential class of Copilot agent actions across the enterprise, arriving just as Ignite is expected to bring Autopilot to GA and dramatically expand the scope of autonomous work. [122-1,122-4,122-5,122-9,122-10,123-3,123-6,124-10,124-11,126-12,39-6,45-8,45-9,45-10] |
| **Grok (xAI)** | **Grok 4.8 remains in its soft rollout to Grok Bot users as of November 16, with no model card, API listing, or formal release note published; Musk described the rollout on November 10 as a limited test to gauge user response while reinforcement learning continues on a rewritten C/C++ stack; the Grok mobile app received updates on November 15 (1.2.56) and November 16 (1.2.57); Grok Bot experienced elevated errors on November 12, now resolved; Grok Build's last published release remains 1.0.74 from early November** — the absence of a formal model page, benchmark table, or API entry for Grok 4.8 as of today means the soft rollout is a capability test rather than a trust-signalling event: Grok Bot users receiving it cannot know what they are running, what it has been evaluated on, or how to compare its behaviour to 4.7. [67-2,67-4,67-6,68-5,68-7,68-9,55-1,52-5,74-3,74-6,74-7] |
| **Perplexity** | **Perplexity Teammates arrives in the Mac app on November 13, completing the web-iOS-macOS triangle in under two weeks since the November 5 web launch; the Mac integration means Teammates can run alongside other desktop workflows without requiring a browser tab to stay open; Teammates remain gated to the $200/month Max plan; Decider v1.3 and Flash v1.3 (November 12) shipped open weights on Hugging Face under Apache 2.0, introducing a locate span extraction output that returns exact matching text positions** — the Mac desktop expansion is a surface-reach advance with a consequential UX implication: Teammates running in a native Mac app means the agent's background work is native to the OS session, not dependent on a browser tab remaining open — establishing the first persistent-agent footprint in Perplexity's desktop presence and removing the browser as a required mediation layer between the user and their standing agents. [116-4,116-5,112-6,120-6,113-3,113-7,113-8,57-1,57-4,63-1,63-3] |

---

## Product Highlights

### ChatGPT / OpenAI: Wallet and the Per-Purchase Biometric Approval Pattern

OpenAI's most consequential interaction-design event in this 48-hour window is the **ChatGPT Wallet** launch on November 13 — the first native agentic payment surface on any major AI platform, and the first time a large-scale AI agent has been given the ability to complete a financial transaction on a user's behalf through a trust architecture designed from first principles rather than bolted onto an existing payment flow.



ChatGPT Wallet is introduced as a secure way for agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections. Users add a card once, then approve each purchase without re-entering payment details. Before each purchase, the user reviews the items, total, and selected card, then approves it with a security check such as Face ID or a fingerprint scan, and each approval creates a clear record of the purchase the user authorised the agent to make.

 The confirmation-card UI — surfacing the merchant, items, total, and card before every transaction — is the central trust-design decision: rather than the agent completing a purchase and notifying the user afterward, the platform inserts a mandatory human review-and-approve gate at the moment of commitment, making every agent-initiated transaction a co-signed act.



When it is time to transact, ChatGPT's Wallet charges the selected card using a payment token, which is a substitute for the user's actual card details, so that information is not shared with either the dot or the merchant.

Once a purchase is approved, the payment network issues a token with a scoped card number, security code, and expiry date tied to that single transaction, so neither the agent nor the merchant receives the real card number. OpenAI plans to let users set spending limits, purchase categories, or time periods later, so their agents can buy within pre-approved rules without asking each time.

 This planned progression — from per-purchase approval to pre-authorised spending envelopes — is the most important trust-design signal in the launch: the current architecture is a trust-building phase, not the end state. The interaction pattern will evolve from every-purchase-requires-approval (maximum human oversight) toward agent-within-approved-envelope (delegated authority with pre-set constraints), and the design of that transition — how users set envelope parameters, how agents communicate when they are approaching envelope limits, and how the approval requirement reasserts itself when an action falls outside the envelope — will be the central UX challenge of agentic commerce.



OpenAI said its dots agents will never actually access a user's card details.

Approval and order confirmation are separate steps — a "Ready to check out" message means the user has approved the purchase, not that the merchant has accepted it.

 This separation of the user's approval from the merchant's confirmation is an important and underappreciated UX boundary: the approval UI creates a record of what the user authorised, but it does not guarantee that the merchant's fulfilment system accepted the same transaction as described. 

OpenAI warns that approving a purchase does not confirm the order, so customers will have to check the merchant's confirmation.



---

### Claude / Anthropic: The Sandbox Permission Default-Flip and the Credential-Bleed Closures

Anthropic's most consequential interaction-design and trust-design event in this window is not a new surface or capability but a default change: **Claude Code 2.1.325**, shipped to npm on November 13, reverses the most consequential implicit permission grant in the agentic coding tool's history by requiring sandboxed Bash commands to go through the normal permission flow before executing.



Starting with version 2.1.325, published to npm on November 13, 2026 at 20:07 UTC, Bash commands that run inside Claude Code's sandbox no longer execute automatically. They now go through the same permission flow as any other command, which means the agent stops and asks before running them unless an allow rule or a permission mode already covers the call.

 The UX implication of this default change is significant: in prior versions, a developer working in a sandboxed environment implicitly trusted the agent to execute Bash commands without interruption. The new default inverts that assumption — the agent is now required to surface its intention before execution, and the developer's explicit approval is the gate. 

Sandboxed Bash commands now follow the normal permission flow by default; sandbox.autoAllowBashIfSandboxed can be set to true to keep the old no-prompt behavior.

 The opt-out path preserves the prior behavior for experienced users who want it, but the burden of configuration is now on the user who wants less oversight, not the user who wants more — a direction of default-travel that is consistent with the direction of enterprise trust-design.



Claude Code v2.1.321 fixes four permission and sandbox gaps; v2.1.325 fixes a security issue in zstd decoding.

The release also fixed a background session sending a conversation under another sign-in when its named Anthropic profile is missing, changed, or overridden — it now stops and says so.

Another fix stops background sessions started on a claude.ai login from using, and billing, an API key or token taken from the shell that launched the background service.

 These credential-bleed closures are the trust-design substrate beneath the sandbox default-flip: the update is not just making individual commands require approval, it is closing the paths through which the agent's access footprint could silently expand across authentication contexts and billing identities. The combined effect — permission-ask for sandboxed execution, credential isolation for background sessions, security fix for compressed-response decoding — makes 2.1.325 the most trust-design-significant Claude Code release of the November cycle.



An investigation continues into an issue with Sign in with Apple on the Claude iOS app, which is mainly affecting new accounts.

New users can sign up with Google or email instead.

 This iOS registration friction arrives in a week when Anthropic's enterprise governance posture — the November 12 policy enforcement, the November 19 Claude Data default-on deadline, and the Claude Code security hardening — is at its most consequential, and the platform's ability to onboard new users is impaired on its mobile surface.

---

### Microsoft Copilot: Connector Write Actions, Confirmation Cards, and the Ignite Eve

Microsoft's most interaction-design-significant event in this window is not an Ignite preview but a capability that has already reached GA: **connector write actions** in Copilot Chat and Cowork, which transform the Copilot connector from a read-only retrieval surface into a bidirectional action surface capable of creating, updating, and deleting data in connected third-party applications.



Connector write actions are now generally available in Copilot Chat and Cowork — depending on the connector, Copilot can create, update, or delete information in the connected application, using the user's permissions in the connected system.

For instance, Copilot can turn a Teams meeting transcript into a CRM activity and follow-up task, or convert Outlook escalations into product issues, complete with summaries and labels.

 This is a significant scope expansion: the same conversation that previously retrieved information from a connected system can now modify it, moving Copilot from information-surface to action-surface within the same interaction context.



A confirmation card is displayed on screen, outlining what Copilot has been told to do — such as "Copilot wants to use [tool name] from [connector]" — along with the details being sent.

Actions are performed using the signed-in user's account and permissions in the third-party service, and by default each create, update, or delete action requires the user's explicit confirmation before it runs.

Users can approve once or remember approval for an individual tool.

 This per-tool, remember-or-approve-each-time model is the correct trust-design pattern for a surface that includes both low-risk write actions (updating a Notion document) and high-risk ones (deleting content in a connected CRM): users can gradually expand their approval trust for tools they have already validated, without being forced into a blanket pre-authorisation.



Microsoft Ignite 2026 takes place November 17–20 at Moscone Center in San Francisco. The opening keynote starts at 10:00 AM PT. Satya Nadella and Judson Althoff share the biggest Microsoft Ignite news, including new releases for Copilot, AI agents, Azure, and security.

Copilot Autopilot's General Availability is a possible Ignite announcement. Microsoft introduced Autopilot — the persistent background agent mode in Microsoft 365 Copilot — in September 2026, and Ignite is a natural moment for a GA announcement or a significant expansion of Autopilot's capabilities.

Autopilot has a timing wrinkle: Microsoft's roundup says Frontier in November, but the updated Message Center notice says rollout timing will follow.

 The gap between the promised Frontier timing and the Message Center's more cautious language is the enterprise governance signal to watch tomorrow: if Ignite brings an Autopilot GA announcement, the question is whether the governance controls — spending caps, task-scope definitions, admin oversight surfaces — ship alongside the capability or follow in a subsequent rollout.

---

### Perplexity: Teammates Reaches the Mac and the Browser-Tab Dependency Falls

Perplexity's most significant interaction-design event in this window is the **Teammates Mac app expansion** on November 13 — completing the web-iOS-macOS surface triangle for persistent agents in under two weeks since launch and removing the browser as a required mediator between the user and their standing agents.



Perplexity expanded its Teammates agentic feature to the macOS app on November 13, 2026, bringing persistent AI agents to desktop users who subscribe to the company's $200-per-month Max plan. The feature officially launched on the web during the first week of November 2026, appeared on iOS shortly after, and arrived on macOS on November 13.

The Mac integration means Teammates can run alongside other desktop workflows without requiring a browser tab to stay open.

 This is the UX implication that matters most: a Teammate running in a native Mac app is a persistent OS-level process, not a browser session that depends on the tab remaining foregrounded, the browser not being closed, or the user not running out of memory. It shifts the agent from an incidental digital presence to a native system participant.



Officially launched on November 13, 2026, the Mac version of Teammates followed the web and iOS releases by less than two weeks. Perplexity introduced Teammates on its web platform in early November, then brought the feature to iOS before expanding to macOS. With the Mac app now supporting Teammates alongside web and iOS, Perplexity has unified the experience for Max subscribers across all major platforms in under a month.

 The speed of this cross-platform expansion — web to iOS to macOS in less than fourteen days — is itself an interaction-design signal: Perplexity is treating Teammates as a platform-level capability that belongs on every surface simultaneously, not a feature to be tested on one surface before cautious expansion.



Perplexity released open-weight pplx-decider-v1.3 and pplx-decider-flash-v1.3 under the Apache 2.0 license on November 13, 2026 on Hugging Face, introducing specialised decision and text-classification models that depart from conventional generative token decoders.

Decision models return probabilities, not chat prose, so routers can threshold yes/no, multi-class, rubric scores, and now text spans in one HTTP contract.

 The UX relevance of Decider v1.3 is indirect but consequential: by open-sourcing the classifier infrastructure that underpins Perplexity's internal routing decisions, the company is making it possible for teams building on Perplexity's agent stack to implement their own decision layers — giving developers the trust primitive of probability-based routing rather than opaque generative decisions.

---

### Google Gemini: Omni 1.2 Flash, the December 3 Silent Redirect, and Video Editing by Conversation

Google's most significant generative-UX development continuing to reach enterprise and developer workflows in this window is **Gemini Omni 1.2 Flash**, generally available since November 5, whose multi-turn conversational editing capability represents the most consequential interaction-pattern advance in the video generation category since the category emerged.



Gemini Omni 1.2 Flash is Google's updated video generation model, now generally available through Google AI Studio, Vertex AI, and the Gemini API. It generates clips up to 15 seconds long, at any length between 3 and 15 seconds, with synced dialogue, sound effects, and multi-speaker voice matching built into the output.

The rollout makes Gemini Omni 1.2 Flash generally available across the Gemini API and Gemini for business, introducing native 15-second video creation and multi-turn conversational editing capabilities.

 The multi-turn editing model is the interaction-pattern advance that matters most: rather than generating a video and exporting it to a separate editing tool, users can describe the edit they want in a follow-up message within the same conversation, and the model refines the clip. This is the same generate-and-refine-in-place shift that defined the generative image category's evolution, now applied to video.



Every video generated through the API carries an invisible SynthID watermark that can be detected programmatically for provenance verification.

The broader rollout covers Flow for scene direction and multi-turn edits, longer clips in Google Vids at no additional cost with a Google account or Workspace subscription, a Gemini app rollout to Google AI Ultra subscribers, and campaign creation in Google Ads.

 The SynthID watermark-on-every-output is the trust primitive embedded in the generation pipeline: it establishes provenance at the moment of creation rather than requiring after-the-fact detection, making model-generated video identifiable across its full distribution lifecycle.



From December 3, requests to the gemini-omni-1.1-flash model ID are routed to 1.2 and billed at 1.2 rates.

 This silent redirect is the trust-design tension in the transition: enterprise applications built on the 1.1 model ID will switch underlying model, output characteristics, and billing rate on December 3 without any interaction-layer notification to end users. The deadline is a governance event that enterprise developers need to anticipate — not because the 1.2 model is worse, but because an undisclosed model substitution in a production workflow removes the ability to reason about which model produced which output.

---

## The Bigger Picture: Wallets, Write Actions, and the Trust-Primitive Sprint to Ignite

The 48 hours ending November 16, 2026 crystallise a single macro movement that has been building across the entire November cycle: **the moment when AI agents move from performing information work to performing consequential real-world actions — financial transactions, data writes in third-party systems, Bash command execution in cloud environments — and the industry's design response is to build a trust primitive specific to each class of consequential action before shipping that action at scale.** ChatGPT Wallet's per-purchase biometric confirmation card, Copilot's connector write-action confirmation card with per-tool approval memory, and Claude Code's sandbox permission-ask flip are three different trust primitives for three different action classes — commercial transactions, enterprise data writes, and local code execution — but they share the same design logic: the agent proposes, the human reviews at the moment of consequence, the approval creates a record. What distinguishes these moves from earlier agentic trust patterns is their specificity: rather than one blanket consent gate at the beginning of an agentic session, each consequential action class gets its own gate, its own review surface, and its own audit trail. This is the correct direction — it allows users to build graduated trust in specific action types while maintaining human authority at the moments that matter most. The tension is in the gaps. Grok 4.8's soft rollout to Bot users without a model card, benchmark table, or API entry means users receiving it cannot know what they are running. Google's December 3 silent redirect from Omni 1.1 to 1.2 means production applications will switch models without notification. Perplexity's Teammates expansion to Mac brings persistent agents to the OS level without a materially new governance surface for enterprise administrators. And Microsoft's Autopilot timing uncertainty — the gap between the promised Frontier timing and the Message Center's "timing will follow" — means enterprise administrators arrive at Ignite tomorrow not knowing whether the most consequential persistent-agent surface in the M365 ecosystem will GA before or after they have completed their governance preparations. Tomorrow's Ignite keynote is therefore the week's most consequential single event not for what it ships, but for which of these gaps it closes — and which it leaves open.

---

## References

[1] status.claude.com. (2026). *Claude Status — November 14–15, 2026 Incidents*. [https://status.claude.com/](https://status.claude.com/)

[2] releasebot.io. (2026). *Claude Code Updates by Anthropic — November 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[3] datastudios.org. (2026). *Claude Code 2.1.325 now asks before running sandboxed Bash commands*. [https://www.datastudios.org/post/claude-code-2-1-325-asks-before-running-sandboxed-bash-commands](https://www.datastudios.org/post/claude-code-2-1-325-asks-before-running-sandboxed-bash-commands)

[4] dev.to. (2026). *Claude Code 2.1.325 Turns Off Auto-Allow for Sandboxed Bash*. [https://dev.to/raxxostudios/claude-code-21325-turns-off-auto-allow-for-sandboxed-bash-2pbo](https://dev.to/raxxostudios/claude-code-21325-turns-off-auto-allow-for-sandboxed-bash-2pbo)

[5] github.com. (2026). *Releases · anthropics/claude-code*. [https://github.com/anthropics/claude-code/releases](https://github.com/anthropics/claude-code/releases)

[6] webcode.tools. (2026). *Claude Code 2.1.325 Fixes A Zstd Decoding Security Issue And Gateway Compaction Errors*. [https://webcode.tools/news/claude-code-2-1-325-fixes-a-zstd-decoding-security-issue-and-gateway-compaction-errors-on-npm/](https://webcode.tools/news/claude-code-2-1-325-fixes-a-zstd-decoding-security-issue-and-gateway-compaction-errors-on-npm/)

[7] dev.to. (2026). *This week in Claude Code, Codex and Gemini CLI (week of November 15, 2026)*. [https://dev.to/aicoding-guide/this-week-in-claude-code-codex-and-gemini-cli-week-of-november-15-2026-4pmm](https://dev.to/aicoding-guide/this-week-in-claude-code-codex-and-gemini-cli-week-of-november-15-2026-4pmm)

[8] openai.com. (2026). *Introducing ChatGPT Wallet*. [https://openai.com/index/introducing-chatgpt-wallet/](https://openai.com/index/introducing-chatgpt-wallet/)

[9] techcrunch.com. (2026). *ChatGPT's new Wallet lets AI agents shop and check out for you*. [https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/](https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/)

[10] cnbc.com. (2026). *OpenAI launches ChatGPT Wallet, allowing its 'dots' AI agents to make purchases for users*. [https://www.cnbc.com/2026/11/13/openai-chatgpt-wallet-dot-purchases.html](https://www.cnbc.com/2026/11/13/openai-chatgpt-wallet-dot-purchases.html)

[11] 9to5mac.com. (2026). *OpenAI launches ChatGPT Wallet, enabling 'dot' agents to make purchases*. [https://9to5mac.com/2026/11/13/openai-launches-chatgpt-wallet-enabling-dot-agents-to-make-purchases/](https://9to5mac.com/2026/11/13/openai-launches-chatgpt-wallet-enabling-dot-agents-to-make-purchases/)

[12] online-tech-tips.com. (2026). *OpenAI introduces ChatGPT Wallet for agent purchases with user approval*. [https://www.online-tech-tips.com/openai-chatgpt-wallet-agent-purchases-user-approval/](https://www.online-tech-tips.com/openai-chatgpt-wallet-agent-purchases-user-approval/)

[13] cxm.world. (2026). *ChatGPT's AI Agents Can Now Shop and Pay for You*. [https://cxm.world/customer-experience/chatgpt-wallet-ai-agents-can-shop-and-pay-for-you/](https://cxm.world/customer-experience/chatgpt-wallet-ai-agents-can-shop-and-pay-for-you/)

[14] basic-tutorials.com. (2026). *ChatGPT Wallet: OpenAI Lets Its "dots" Agents Shop Using Your Credit Card*. [https://basic-tutorials.com/news/chatgpt-wallet-openai-lets-its-dots-agents-shop-using-your-credit-card/](https://basic-tutorials.com/news/chatgpt-wallet-openai-lets-its-dots-agents-shop-using-your-credit-card/)

[15] kingy.ai. (2026). *ChatGPT Wallet Rolls Out in the US. Here's How Checkout Works*. [https://kingy.ai/news/openai-chatgpt-wallet-ai-agent-checkout/](https://kingy.ai/news/openai-chatgpt-wallet-ai-agent-checkout/)

[16] technology.org. (2026). *OpenAI Launches ChatGPT Wallet So Its AI Agents Can Pay for Purchases*. [https://www.technology.org/2026/11/16/openai-chatgpt-wallet-ai-agents-purchases-tokenized-cards/](https://www.technology.org/2026/11/16/openai-chatgpt-wallet-ai-agents-purchases-tokenized-cards/)

[17] help.openai.com. (2026). *ChatGPT Enterprise and Edu release notes*. [https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)

[18] unite.ai. (2026). *Google's Gemini Omni 1.2 Flash Reaches General Availability*. [https://www.unite.ai/googles-gemini-omni-1-2-flash-reaches-general-availability/](https://www.unite.ai/googles-gemini-omni-1-2-flash-reaches-general-availability/)

[19] thenextweb.com. (2026). *Google's Gemini Omni 1.2 Flash makes 15-second AI videos for less*. [https://thenextweb.com/news/google-gemini-omni-1-2-flash-video-15-seconds-price-cut](https://thenextweb.com/news/google-gemini-omni-1-2-flash-video-15-seconds-price-cut)

[20] systemdesign.academy. (2026). *Gemini Omni 1.2 Flash: what's new, pricing and API*. [https://www.systemdesign.academy/explained/gemini-omni-1-2-flash](https://www.systemdesign.academy/explained/gemini-omni-1-2-flash)

[21] mindstudio.ai. (2026). *Gemini Omni 1.2 Flash: Google's Video Model Gets Cheaper and Longer*. [https://www.mindstudio.ai/blog/gemini-omni-1-2-flash-video-generation](https://www.mindstudio.ai/blog/gemini-omni-1-2-flash-video-generation)

[22] aguidetocloud.com. (2026). *What's New in Microsoft 365 Copilot: November 2026*. [https://www.aguidetocloud.com/blog/microsoft-365-copilot-november-2026-updates/](https://www.aguidetocloud.com/blog/microsoft-365-copilot-november-2026-updates/)

[23] techcommunity.microsoft.com. (2026). *Turn Copilot insights into action with connector write capabilities*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/turn-copilot-insights-into-action-with-connector-write-capabilities/4571160](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/turn-copilot-insights-into-action-with-connector-write-capabilities/4571160)

[24] windowsreport.com. (2026). *Microsoft Copilot Can Now Create, Update, and Delete Data Across Connected Apps*. [https://windowsreport.com/microsoft-copilot-can-now-create-update-and-delete-data-across-connected-apps/](https://windowsreport.com/microsoft-copilot-can-now-create-update-and-delete-data-across-connected-apps/)

[25] datastudios.org. (2026). *Microsoft 365 Copilot connector write actions: Jira, Notion, Canva GA*. [https://www.datastudios.org/post/microsoft-365-copilot-connectors-write-actions-jira-notion-canva-user-approval](https://www.datastudios.org/post/microsoft-365-copilot-connectors-write-actions-jira-notion-canva-user-approval)

[26] netcomlearning.com. (2026). *Microsoft Ignite 2026: Dates, Agenda, Keynote & Releases*. [https://www.netcomlearning.com/microsoft-ignite-article](https://www.netcomlearning.com/microsoft-ignite-article)

[27] thelalitblogs.com. (2026). *Microsoft Ignite 2026 Preview: What to Expect for Copilot and Frontier Transformation*. [https://thelalitblogs.com/microsoft-ignite-2026-preview-copilot-frontier-transformation/](https://thelalitblogs.com/microsoft-ignite-2026-preview-copilot-frontier-transformation/)

[28] cellcog.ai. (2026). *Grok 4.8 Release Date: Soft Rollout This Week, Musk Says*. [https://cellcog.ai/blog/grok-4-8-release-date/](https://cellcog.ai/blog/grok-4-8-release-date/)

[29] tokenpost.com. (2026). *xAI Plans Limited Grok 4.8 Rollout for Bot Users This Week*. [https://www.tokenpost.com/news/technology/53847](https://www.tokenpost.com/news/technology/53847)

[30] explainx.ai. (2026). *Grok 4.8 Soft Rollout: RL Done, Bot Test This Week*. [https://explainx.ai/blog/grok-4-8-soft-rollout-rl-cpp-stack-november-2026](https://explainx.ai/blog/grok-4-8-soft-rollout-rl-cpp-stack-november-2026)

[31] aiweekly.co. (2026). *Perplexity Brings Teammates Agents to Mac, $200 Max Plan Only*. [https://aiweekly.co/alerts/perplexity-brings-teammates-agents-to-mac-200-max-plan-only](https://aiweekly.co/alerts/perplexity-brings-teammates-agents-to-mac-200-max-plan-only)

[32] tbreak.com. (2026). *Perplexity Teammates arrive in the Mac app for Max users*. [https://tbreak.com/perplexity-teammates-mac-app/](https://tbreak.com/perplexity-teammates-mac-app/)

[33] emergent.sh. (2026). *Perplexity Teammates Agents Launch on Mac for Max Users*. [https://emergent.sh/news/perplexity-teammates-agents-launch-mac-max](https://emergent.sh/news/perplexity-teammates-agents-launch-mac-max)

[34] opentools.ai. (2026). *Perplexity Teammates AI Agents Arrive on Mac — Behind a $200 Paywall*. [https://opentools.ai/news/perplexity-teammates-agents-mac-desktop-200-dollar-max-plan](https://opentools.ai/news/perplexity-teammates-agents-mac-desktop-200-dollar-max-plan)

[35] casrai.org. (2026). *Perplexity Releases Open-Weight Decider v1.3 and Flash Decision Models*. [https://casrai.org/news/perplexity-pplx-decider-v1-3-open-weights-release-2026](https://casrai.org/news/perplexity-pplx-decider-v1-3-open-weights-release-2026)

[36] explainx.ai. (2026). *pplx-decider v1.3: Locate Extraction API (2026)*. [https://explainx.ai/blog/perplexity-pplx-decider-v1-3-locate-extraction-november-2026](https://explainx.ai/blog/perplexity-pplx-decider-v1-3-locate-extraction-november-2026)