# UX Briefing: Policy Guardrails, Persistent Agents, and the Composable Persona Pivot

**October 13, 2026**

Good morning. The 48 hours ending October 13, 2026 are defined by a simultaneous push on two fronts: platforms are hardening the trust and conduct boundaries around agents that already have deep access to user environments, while simultaneously evolving the personalisation layer from fixed configurations into composable, reusable instruction blocks. **Claude/Anthropic** delivers its most consequential trust-design policy event of the year: the **2026 Usage Policy update published October 8** — a consolidated governance document that adds a prohibition on sustained abusive conduct toward models (backed by Claude's trained ability to exit such conversations), consolidates deceptive-campaign rules into a unified section, and tightens surveillance and weapons-software restrictions, effective November 12 — paired with **Claude Code 2.1.296** shipping **per-subagent `autoCompactWindow` controls, the `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` environment variable**, and a new `code` gateway policy key that extends managed enterprise settings into Claude Desktop's Code tab. **ChatGPT/OpenAI** extends the GPT-6 Intelligent UI global rollout (which began October 7) into Enterprise with admin-governed access controls, while shipping **role-based plugin access controls for RBAC-enabled Enterprise workspaces on October 8** — letting admins set per-role plugin availability at Available, Install, or Disabled — and **Dots receiving mobile creation on iOS and Android** alongside expanded Codex handoff and Scheduled Tasks editing in Work. **Google Gemini** reaches its most significant personalisation transition milestone of the year: **Skills begin rolling out in the Gemini app on October 13** — the same day as this briefing — completing the cross-surface Skills deployment that started in Workspace on October 5, while simultaneously ending the ability to create or edit Gems for users on Rapid Release, with the Gems-to-Skills migration now running against a firm November 17 clock. **Microsoft Copilot** advances the **Today proactive command-centre feature into private preview in October** inside the new Home architecture — a persistent inbox/calendar/Teams/tasks synthesis that drafts replies and proposes schedule changes before the user opens their mail — while the **Copilot Notebooks October 2026 update lands Office file editing and interactive reports in Frontier preview**, with recurring scheduled automations confirmed for the following weeks. **Grok (xAI)** ships **Grok Build 1.0.51 and 1.0.52** with a dense cluster of permission-architecture fixes: approval cards for background subagents no longer disappear when the parent turn ends, minimal mode now surfaces the permission prompt rather than hiding it, and worktree deletion is hardened to refuse removing git repositories or directories Grok did not itself create. **Perplexity** continues the post-Automations consolidation with its **Effort Mode now pairing GPT-6.1 Sol with the Light setting** for everyday tasks, while the **HP ZBook Ultra G3a Portable Computer pre-install begins rolling out in October**, making Perplexity the first AI agent stack to ship pre-installed on a major commercial Windows workstation.

---

## At a Glance: October 13 Highlights

Today's releases converge on a maturing-agent category that is simultaneously extending autonomous capability and installing more granular governance — in policy documents, in permission architectures, and in the composable personalisation layers that determine what the agent is allowed to be for each user.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **2026 Usage Policy update published October 8, effective November 12** — prohibits sustained abusive conduct toward models; Claude exits such conversations; deceptive-campaign rules consolidated; surveillance and weapons-software sections rewritten; Claude Code 2.1.296 ships per-subagent `autoCompactWindow`, `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL`, and a `code` gateway-policy key extending enterprise managed settings to Claude Desktop's Code tab. [1][2][3] |
| **ChatGPT** | **Role-based plugin access controls ship for RBAC Enterprise workspaces October 8; Dots get mobile creation and Codex handoff** — admins set per-plugin, per-role access at Available/Install/Disabled in Admin console; GPT-6 Intelligent UI now in Enterprise Chat with admin controls; Dots can be created from iOS/Android apps; plugins now support interactive panels and sidebar views. [4][5][6] |
| **Google Gemini** | **Gemini Skills begin Gemini app rollout today, October 13 — the same day Gem creation/editing ends for Rapid Release users** — Skills now available across Workspace (Rapid Release complete) and Gemini app; multiple Skills can stack per-session; non-sync constraint between app and Workspace surfaces; November 17 is the Gems-move-to-Settings milestone; enterprise Gems survive until no earlier than March 1, 2027. [7][8][9] |
| **Microsoft Copilot** | **Today proactive command centre enters private preview in October inside Copilot Home** — surfaces missed mail, calendar, Teams threads, and tasks with drafts already prepared; Copilot Notebooks October update ships in-notebook Office editing, interactive reports, and PDF creation in Frontier preview; recurring scheduled automations (daily briefs, weekly status) confirmed for coming weeks; SharePoint Plugins now support read/write with human approval on bulk actions. [10][11][12] |
| **Grok (xAI)** | **Grok Build 1.0.51 and 1.0.52 ship subagent approval-card persistence, permission-prompt surface hardening, and safer worktree deletion** — approval cards for background subagents stay visible after parent turn ends; minimal mode shows permission prompt instead of hiding plan/cancel panel; `grok worktree rm` refuses git repos and non-Grok directories; auto-compaction loop capped at three refills; workflow stop targets correct live run. [13][14][15] |
| **Perplexity** | **GPT-6.1 Sol now powers Effort Mode's Light setting; HP ZBook Portable Computer pre-install begins rollout in October** — Effort Mode Light/Standard/High/Ultra slider pairing updated with GPT-6.1 Sol; HP will pre-install Perplexity on the HP ZBook Ultra G3a, expanding to more Windows devices; Claude Opus 5.5 and MiniMax H3/Seedance 2.5 video generation added to Automations; Decisions API pplx-decider v1.1 ships for routing and classification. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Usage Policy as a Trust-Design Artefact

Anthropic's most consequential interaction-design event in this window is not a feature — it is the **2026 Usage Policy update**, published October 8 and effective November 12. Its significance to the Agent2Agent2Human experience layer is structural: it is the first time Anthropic has explicitly encoded the *agent's right to exit an interaction* as a user-facing policy boundary, converting what was previously a model behaviour (Claude stopping a harmful conversation) into a stated contractual rule.



Anthropic published its annual 2026 Usage Policy update on October 8, 2026, consolidating its rules against deceptive campaigns, adding a prohibition on abusive behavior toward its models, and clarifying weapons, surveillance, and high-risk use requirements — the updated policy takes effect November 12, 2026.

 The UX significance of the model-conduct rule runs deeper than its ethics framing: 

since an update in August, Claude has been trained to end conversations with "persistently harmful or abusive user interactions" — but the new policy explicitly bars users from pursuing those conversations.

 This converts a model capability into a policy enforcement point. Where before a user could argue that ending such conversations was Claude's choice, the November 12 policy makes that boundary legible and enforceable at the operator level — a trust-design primitive for platforms deploying Claude in high-volume consumer contexts where sustained adversarial sessions are a real operational risk.



The policy is meant to apply only in extreme cases, where users repeatedly act cruelly toward the models with no discernible purpose — it does not apply to common versions of user frustration, pushback, dark creative themes, or model testing and research.

 The scoping is the correct design choice: a policy broad enough to catch ordinary critical feedback would degrade the utility of every debugging and evaluation workflow Claude supports. By specifying the extreme-case threshold, Anthropic preserves the feedback loops that legitimate users rely on while creating an explicit policy instrument against bad-faith harassment. 

The update also consolidates previously scattered prohibitions into a new section titled "Do Not Engage in Deceptive Campaigns or Artificial Activity," which applies to deceptive activity of any kind, political or commercial.



On the developer surface, 

Claude Code 2.1.296 adds new agent, workflow, and gateway controls, including larger Read support and subagent auto-compact, while improving cloud, VS Code, Slack, Windows, and self-hosted runner reliability with many bug fixes and policy updates.

 The two agentic-workflow advances that matter most for multi-agent enterprise deployments are: 

the new `autoCompactWindow` setting works in subagent frontmatter and `--agents` definitions, letting a subagent auto-compact before the main conversation reaches its own context window threshold

 — preventing one long-running subagent from compacting the entire conversation prematurely — and 

`CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` sets one model for every workflow agent while letting other subagents keep their existing model choices.

 That second control is the enterprise token-predictability primitive that multi-step pipelines have required: operators can now pin every subagent in a defined workflow to one selected model without losing per-subagent flexibility elsewhere in the same session.

---

### ChatGPT / OpenAI: Role-Based Plugin Governance and the Dots Delegation Loop

OpenAI's most trust-design-significant release in this window is the **role-based plugin access controls** reaching RBAC-enabled Enterprise and Edu workspaces on October 8 — a governance primitive that closes the gap between the organisational role directory and the agent's tooling surface, bringing plugin availability under the same role-scoped authority model that governs data access in enterprise environments.



Workspace owners and admins in ChatGPT Enterprise and Edu workspaces with RBAC enabled can now manage plugin access by role — set the workspace default to Available, Install, or Disabled; custom roles can use those settings or Default to inherit the workspace setting.

 The UX significance of this is the completion of a permission hierarchy: previously, plugin availability was a workspace-wide binary that administrators could toggle on or off for all users simultaneously. Role-based access converts that binary into a graduated permission model where a compliance analyst can have access to a legal-research plugin that a junior user cannot, without the administrator having to maintain per-user configurations. 

Review and save plugin access and the corresponding required-app permissions together — app action settings, approval requirements, and provider authorization continue to apply.

 The bundling of plugin access with required-app permissions in a single review-and-save action is the correct UX design for this surface: it prevents the common misconfiguration where an admin grants plugin access but leaves the underlying app permissions misaligned.

The **Dots persistent-agent surface** is also advancing its interaction footprint this window. 

OpenAI adds mobile dot creation in the ChatGPT iOS and Android app and expands Dots with better Codex handoff, thread follow-ups, and Scheduled Tasks editing in ChatGPT Work — you can now create your Dot straight from your phone, and delegate work in Codex to your Dot.

 The mobile creation path is the interaction-design step that makes Dots genuinely ambient rather than desktop-anchored: a user who thinks of a delegation goal during a commute can now instantiate the Dot immediately rather than waiting to be at a workstation. 

Dots are always-on agents in ChatGPT that can take on ongoing work and keep making progress between conversations — give your Dot a goal, connect the apps it needs, and define what it can do on its own.



The **interactive plugin extensions** deserve isolation as a separate interaction-pattern advance: 

plugins can now include interactive panels, sidebar views, and viewers or editors for supported file types.

 This extends the Intelligent UI architecture beyond ChatGPT's own response layer into the plugin ecosystem — third-party tools can now render their own interactive interface components inside the conversation surface, rather than requiring a browser handoff or a modal dialog. The UX implication is that the conversation window is becoming a composable panel host, not just a text stream with embedded interactive elements from OpenAI's own component library.

---

### Google Gemini: Skills Day-One in the Gemini App and the Composable Persona Inflection

Google's most consequential Gemini interaction-design event in this exact window is the **Skills rollout beginning in the Gemini app today, October 13** — the moment the new composable-persona architecture becomes simultaneously available across both the Gemini app and Workspace for Rapid Release domain users, completing the cross-surface deployment that started in Workspace on October 5.



Skills begin rolling out in the Gemini app for all users on October 13, 2026, with rollout completing by mid-November — users can create and use both Gems and skills during the transition window.

 The UX significance of today's date is not just the rollout start: 

starting October 13, 2026, users will no longer be able to create or edit Gems, though they may continue using existing ones until the November 17 automatic migration begins.

 This creates a hard interaction-design milestone for enterprise Workspace teams: the ability to author new Gem configurations has now ended for Rapid Release users, making Skills the only forward path for any new personalisation workflow. 

Multiple Skills can work together, letting Gemini combine specialized instructions for more complex tasks.



The composability advance over Gems is the architectural shift that matters most. 

The older Gems format did not support combining more than one configuration per session

 — a Gem was a single-mode persona switch. Skills are stackable per-session, which shifts the user's relationship with AI personalisation from mode-selection to capability-composition: a user can layer a "tone of voice" Skill with a "data format" Skill and a "domain expertise" Skill in the same prompt, rather than pre-engineering a monolithic Gem that tries to capture all three requirements simultaneously. The architectural consequence is that Skills can be designed and maintained at a more granular level of abstraction — teams can build shared Skills libraries of single-purpose instruction blocks rather than maintaining a proliferating zoo of purpose-built Gems.

The governance constraint that enterprise practitioners must navigate is the **Skills non-sync design**. 

Skills don't currently sync between the Gemini app and Workspace apps — to use a skill across both platforms, or to transition Gems used in Workspace, users must manually recreate them in Google Workspace Studio.

 This means the composable-persona layer is not yet identity-portable in the way that persistent instructions are in competing products. A user who builds a Skills library in the Gemini app must duplicate that configuration in Workspace Studio to get consistent behaviour across both surfaces — creating both maintenance overhead and the risk of divergent AI behaviour between surfaces that the user believes are governed by the same configuration. 

Additionally, GitHub files aren't currently supported in Skills, and Canvas, Deep Research, and several other tools don't yet work with Skills.



---

### Microsoft Copilot: Today's Private Preview, Notebooks as an Agentic Canvas, and the Proactive Work Queue

Microsoft's most structurally significant Copilot UX event materialising in this window is the **Today feature entering private preview in October** — the proactive, pre-synthesised command-centre view inside Copilot Home that converts the start of a user's workday from a reactive inbox-clearing session into a briefed, draft-ready, priority-surfaced delegation act.



Coming soon in Home, Today is a proactive, personalized command center across mail, calendar, Teams threads, meetings and tasks — it shows you what you missed, what needs attention now, and what can wait; Today doesn't just surface the work, it gets work done: the draft is written and ready for you to edit, the schedule change is already proposed, and the forgotten follow-up is waiting for you to send it, complete with context so you can catch up quickly.

 The UX shift this establishes is from *reactive triage* to *pre-delegated action*: the user arrives at the inbox not to process it but to review and approve work that Copilot has already begun on their behalf. This is the correct design for a knowledge worker whose morning context-loading time is a measurable cost — Today externalises the prioritisation and drafting work that previously happened inside the user's head. 

Today enters private preview in October in Copilot, and will be coming to Outlook and Teams as well.



The **Copilot Notebooks October 2026 update** is the agentic-workspace advance that is reshaping what a Notebook is. 

Microsoft is bringing Office editing into Copilot Notebooks through its Frontier preview — users can work on Word, Excel and PowerPoint files alongside their project references, making changes themselves or asking Copilot to handle them.

 The interaction-design implication is a collapse of the boundary between *research context* (the notebook's source references) and *working document* (the Word or Excel file being produced): a user can now review a document, ask Copilot to revise a section, and see the revision applied in the same canvas where the source materials live. 

One of the more interesting additions is scheduled automation — users will be able to schedule recurring tasks, such as daily morning briefs and weekly status presentations, instead of repeatedly prompting Copilot.



The trust-design nuance worth flagging for enterprise practitioners is the **preview-vs-scheduled distinction** in this release. 

Task delegation, scheduled briefings, in-notebook Office editing, interactive reports, and a choice between OpenAI and Anthropic models are all rolling out through Microsoft's Frontier preview program in phases, not as a finished release available to every Notebooks user today.

 On the SharePoint side, 

Plugins let Copilot in SharePoint work with systems such as GitHub, CRM systems, publishing platforms, and internal tools, supporting both read and write scenarios with human approval on bulk actions

 — the human-approval gate on bulk write actions is the correct bounded-autonomy design for a system with write access to an organisation's canonical content store.

---

### Grok (xAI): Subagent Approval Architecture Matures in 1.0.51 and 1.0.52

xAI's most interaction-design-significant releases in this window are a cluster of permission-boundary and approval-surface fixes in **Grok Build 1.0.51 and 1.0.52** that together address the specific failure modes that arise when background subagents operate in parallel with a main session — the approval card disappearance bug, the permission-prompt suppression in minimal mode, and the worktree-deletion safety gap.

The most consequential of these is the approval-card persistence fix. 

Approval cards for background subagents no longer disappear when the parent turn ends.

 This is the failure mode that most directly breaks the human-in-the-loop contract for multi-agent sessions: when a background subagent requires approval for a tool call, the approval card previously disappeared if the main session's turn completed before the user had acted on it — leaving the subagent in an unresolved state with no visible indication that intervention was required. The fix converts approval cards from ephemeral prompts tied to the parent turn's lifecycle into persistent UI elements that remain actionable regardless of what the rest of the session is doing.

The minimal-mode permission-prompt fix addresses a related escape hatch. Previously, minimal mode could hide the permission/cancel panel behind a plan panel when both were present, meaning a user operating in a minimal-mode session could miss a permission prompt entirely. 

Minimal mode now shows the permission prompt instead of a hidden plan or cancel panel when both are present.

 The worktree-deletion safety changes complete this cluster: 

`grok worktree rm` refuses to delete git repositories, `.git` folders, or any directory Grok did not create.

 This prevents a common class of destructive error in multi-session environments where a worktree cleanup operation could silently remove a repository the user intended to keep. 

Auto-compaction also stops after three context refills in a row instead of looping

 — a temporal UX advance that prevents a long-running session from spiralling into continuous compaction without user visibility.

The **Grok Build 1.0.51 goal-control advance** is also worth isolating: 

Ctrl+C on a goal now pauses the goal

 rather than cancelling it. This is the correct interaction primitive for agentic goal management — a user who wants to interrupt an in-progress goal but not discard the accumulated state should be able to pause and resume rather than choosing between full continuation and full cancellation.

---

### Perplexity: Effort Mode Calibrated, HP Hardware Integration, and the Automation Stack Matures

Perplexity's most significant UX development in this window is the **Effort Mode Light setting update**, which now pairs GPT-6.1 Sol with lightweight everyday tasks following the October 5 model addition — converting the effort slider from a reasoning-depth control into a full model-selection-and-reasoning-depth pairing that adjusts automatically as the model roster evolves.



An effort setting selects the model that coordinates the task and how deeply that model reasons; the coordinating model then decides how to approach the work and delegates parts of it to supporting agents — an effort setting does not put a limit on the work itself; it does not cap the number of steps Computer takes, the number of sources it reads, or the tools it uses, and it is not a spending limit.

 This distinction is the critical trust-design clarification that prevents the slider from being misread as a capability fence: Light effort means "use a lighter model and less reasoning depth to coordinate this task," not "Computer will stop after N steps." The design preserves the agent's ability to complete a task fully while giving the user a cost and quality signal without requiring model-selection expertise. 

Perplexity pairs each setting with a model based on evaluation results, and shows that model name in the effort selector — those pairings change as models are added, updated, or retired, so treat the name in the selector as the current answer rather than a permanent one.



The **HP ZBook Ultra G3a Portable Computer pre-install** is the hardware-integration event that deserves editorial attention for what it signals about the agent-surface trajectory. 

HP will pre-install Perplexity on Windows PCs, putting sourced research and Computer a click away on the taskbar — the rollout starts with the HP ZBook Ultra G3a, expected in October 2026, with more HP Windows devices to follow.

 The UX significance of this distribution decision is architectural: a pre-installed agent stack on a commercial workstation removes the onboarding friction that has kept agentic Computer workflows in the early-adopter tier. For regulated-industry knowledge workers who buy standardised hardware configurations managed by IT, pre-installation is the deployment path that actually reaches them — without it, Portable Computer's data-locality guarantees remain available only to users who actively seek the product out. 

The October 5 Automations update also expanded the model roster with Claude Opus 5.5 for Automations, video generation via MiniMax H3 and Seedance 2.5, and Amex-curated business Skills.



---

## The Bigger Picture: Policy Guardrails, Persistent Agents, and the Composable Persona Pivot

The 48 hours ending October 13, 2026 reveal a category navigating a specific maturity inflection: the platforms that spent the last several months expanding agentic surface area and shipping autonomous capability are now doing the harder design work of making those capabilities governable at every layer simultaneously — policy, permission, persona, and hardware. Anthropic's Usage Policy update is the clearest statement of this: codifying the agent's right to exit an abusive session is not a feature, it is a policy-backed interaction boundary that makes Claude deployable in consumer contexts where adversarial sessions are a real operational concern. The Claude Code 2.1.296 workflow-subagent model pinning is the developer-layer equivalent — enterprise teams can now make explicit, auditable decisions about which model runs each subagent in a pipeline, converting token spend from a variable into a governance decision. OpenAI's role-based plugin access controls make the same argument from the enterprise-admin angle: the agent's tooling surface must be governed by the same role hierarchy that governs everything else in the organisation's permission model. Google's Skills rollout — reaching the Gemini app today at the exact moment Gem creation ends for Rapid Release users — is the composable-persona pivot that converts personalisation from a mode-switching problem into a capability-composition problem, though the non-sync constraint between the app and Workspace surfaces is a design debt that will generate configuration drift at scale until it is resolved. Microsoft's Today private preview is the proactive-agent vision statement of the window: not an agent that responds to requests but one that has already reviewed your context, drafted your responses, and is waiting for approval — the correct model for a knowledge worker whose morning bandwidth is the scarcest resource in the workday. Grok Build's approval-card persistence and minimal-mode permission-prompt fixes are the unglamorous infrastructure work that makes multi-agent sessions actually trustworthy: the human approval gate only functions as a trust mechanism if it is consistently visible and actionable regardless of what the rest of the session is doing. Perplexity's HP pre-install is the distribution event that closes the gap between Portable Computer's technical capabilities and the regulated-industry users for whom data-locality matters most. The throughline across all six platforms this window is the same: capability without governance is not product, it is liability — and the platforms investing in the governance layer now are the ones building the enterprise trust that will determine market positions over the next 18 months.

---

## References

[1] TechCrunch. (2026). *Anthropic changes usage policy to ban model abuse and election interference*. [https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/](https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/)

[2] Unite.AI. (2026). *Anthropic Updates Usage Policy, Adding Model Abuse and Deception Rules*. [https://www.unite.ai/anthropic-updates-usage-policy-adding-model-abuse-and-deception-rules/](https://www.unite.ai/anthropic-updates-usage-policy-adding-model-abuse-and-deception-rules/)

[3] Releasebot. (2026). *Claude Code Updates by Anthropic — October 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)

[4] OpenAI Help Center. (2026). *ChatGPT Enterprise and Edu Release Notes*. [https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)

[5] Releasebot. (2026). *ChatGPT Updates by OpenAI — October 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[6] OpenAI Release Notes. (2026). *OpenAI Release Notes — October 2026*. [https://releasebot.io/updates/openai](https://releasebot.io/updates/openai)

[7] Google Workspace Knowledge. (2026). *About the transition from Gems to Skills*. [https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/about-the-transition-to-skills](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/about-the-transition-to-skills)

[8] NQ Brief. (2026). *Google Sets 2026-2027 Timeline to Replace Gemini Gems With Skills*. [https://nqbrief.com/en/tech/google-gemini-gems-skills-timeline/](https://nqbrief.com/en/tech/google-gemini-gems-skills-timeline/)

[9] TechJack Solutions. (2026). *Gemini Skills Replace Gems: Workspace Rollout Starts Now*. [https://techjacksolutions.com/ai-brief/google-workspace-gemini-skills-replace-gems-rollout/](https://techjacksolutions.com/ai-brief/google-workspace-gemini-skills-replace-gems-rollout/)

[10] Microsoft Copilot Release Notes. (2026). *Microsoft Copilot Updates by Microsoft — October 2026*. [https://releasebot.io/updates/microsoft/microsoft-copilot](https://releasebot.io/updates/microsoft/microsoft-copilot)

[11] Windows Report. (2026). *Copilot Notebooks October 2026 Update Adds Office Editing, AI Automations & Interactive Reports*. [https://windowsreport.com/copilot-notebooks-october-2026-update-adds-office-editing-ai-automations-interactive-reports/](https://windowsreport.com/copilot-notebooks-october-2026-update-adds-office-editing-ai-automations-interactive-reports/)

[12] Microsoft Tech Community. (2026). *What's new in Copilot in SharePoint: October 2026*. [https://techcommunity.microsoft.com/blog/spblog/what%E2%80%99s-new-in-copilot-in-sharepoint-october-2026/4535423](https://techcommunity.microsoft.com/blog/spblog/what%E2%80%99s-new-in-copilot-in-sharepoint-october-2026/4535423)

[13] xAI. (2026). *Grok Build Changelog*. [https://x.ai/changelog/build](https://x.ai/changelog/build)

[14] Releasebot. (2026). *Grok Build Updates by xAI — October 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[15] xAI. (2026). *Grok Bot Changelog*. [https://x.ai/changelog/bot](https://x.ai/changelog/bot)

[16] Perplexity. (2026). *Perplexity Changelog*. [https://www.perplexity.ai/changelog](https://www.perplexity.ai/changelog)

[17] Perplexity. (2026). *Effort Mode, GPT-6 Astra, and Skills Marketplace*. [https://www.perplexity.ai/changelog/effort-mode-gpt-6-astra-and-skills-marketplace](https://www.perplexity.ai/changelog/effort-mode-gpt-6-astra-and-skills-marketplace)

[18] Releasebot. (2026). *Perplexity Release Notes — October 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

---