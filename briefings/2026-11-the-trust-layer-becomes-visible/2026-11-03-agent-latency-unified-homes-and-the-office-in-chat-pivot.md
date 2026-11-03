# UX Briefing: Agent Latency, Unified Homes, and the Office-in-Chat Pivot

**November 03, 2026**

Good morning. The 48 hours ending November 3, 2026 are defined by two simultaneous design convergences: the **chat surface swallowing the application layer** — with Microsoft announcing the retirement of standalone Word, Excel, and PowerPoint agents in favour of built-in Copilot Chat capabilities, Google extending Gemini's single-prompt editing to entire Slide decks, and the OpenAI Chat-Work merge continuing its rollout — and a **structural latency breakthrough at the agent infrastructure layer**, with Anthropic's **Message Threads public beta** eliminating the full-conversation resend bottleneck that has constrained long-running agent loops since the Messages API launched. **Claude/Anthropic** delivers the window's deepest agent-infrastructure advance: **Message Threads** in public beta on the Messages API, cutting median time to first token by 35% on long sessions, already live in Claude Code for most users, requiring zero developer setup. **Claude Code 2.1.317** ships today with a critical multi-agent reliability fix: subagents now correctly run with the effort level saved for their specific model, rather than inheriting the orchestrator's setting. Simultaneously, Anthropic's revised **Usage Policy** (effective November 12) introduces new operator-facing constraints on physical hardware, model distillation, and platform abuse. **ChatGPT/OpenAI** continues the rollout of the **Chat and Work tab merge**, with the unified experience expanding beyond its initial test group; the shared ChatGPT-Codex usage pool lands in December. **Google Gemini** completes the most significant Workspace Gemini advance of the quarter: **whole-deck editing from a single Slides prompt**, launched October 29–30, letting Gemini apply a single instruction across every slide in a presentation and list what it changed. **Microsoft Copilot** delivers the biggest structural UX consolidation move in the M365 agent ecosystem in months: the **Notebooks-to-Workspaces rename**, a new **Home navigation surface** bringing Chat, Cowork, Projects, and Workspaces into a single starting point, and the announcement that **standalone Word, Excel, and PowerPoint agents are being retired** in favour of capabilities built directly into Copilot Chat — a triple-convergence of surface consolidation that mirrors what OpenAI is doing with Chat and Work.

---

## At a Glance: November 3 Highlights

Today's window is defined by the chat-native consolidation wave: across Claude, ChatGPT, Gemini, and Copilot, the move is the same — separate application agents, separate tabs, and separate surfaces are being absorbed into a single conversation thread.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Message Threads public beta launches November 2 on the Messages API — agents send only new messages per turn, holding the full conversation server-side for up to 5 minutes, cutting median TTFT 35% in long sessions; Claude Code 2.1.317 ships November 3, fixing subagent effort inheritance and scheduling connector warnings; Usage Policy revision effective November 12 adds operator rules for physical hardware, bans model distillation, and restricts platform abuse including client spoofing** — Message Threads are already live in Claude Code for most accounts with no setup; 2.1.317's subagent effort fix corrects silent mis-execution where agents ran at the wrong reasoning depth; the policy update for physical hardware requires operators to maintain a human-accessible safe state. [101][102][93][96][1][3] |
| **ChatGPT** | **Chat and Work tab merge continues rollout beyond initial test group; ChatGPT and Codex draw from a shared usage pool from December; Unlimited Instant chat is excluded from the shared allowance** — the merge eliminates the pre-task mode-selection decision for users; keeping Codex separate preserves the structured, project-scoped code-agent experience that would not benefit from open-ended conversational context; the shared pool unifies agentic budgeting across coding and general work. [13][15][17][18] |
| **Google Gemini** | **Gemini in Google Slides whole-deck editing launches October 29–30: a single prompt in the Slides side panel can update content, refresh visual styles, combine or expand slides, or align styles across an entire presentation; Gemini determines affected slides and applies edits to native editable slides, listing changes in the side panel; promotional higher limits available through at least December 1, 2026** — this is distinct from the in-chat file editor announced October 29; the Slides update operates on an existing editable Slides deck through the side panel rather than generating a new file in a conversation. [111][112][115] |
| **Microsoft Copilot** | **Copilot Notebooks renamed Copilot Workspaces (rolling out from late October 2026), with Workspaces designed for shared team collaboration; new Copilot Home navigation surface brings Chat, Cowork, Projects, and Workspaces under one starting point (Frontier/standard release late October, deferred late November); standalone Word, Excel, and PowerPoint agents announced for retirement in favour of built-in Copilot Chat document creation (MC1536062, mid-November rollout)** — the Projects/Workspaces split cleanly separates personal task organisation from team collaboration; the agent retirement move is the deepest surface-consolidation signal of the window: separate @-mentionable agents for each Office app are replaced by a single integrated Copilot Chat capability. [83][85][86][122][126] |
| **Grok (SpaceXSI)** | **Grok Build 1.0.74 ships: multi-agent subagent messages now render as left-aligned sender/recipient rows (replacing centered rows); grok --resume now loads large session stores by reading only the resumed session; /new tabs show context window before the new session replies; Grok Build 0.2.111 enables Workflows by default; grok-imagine-image-quality API slug retired today in favour of grok-imagine-image-2.0** — the subagent message rendering fix is the most UX-significant: in multi-agent sessions with several simultaneous subagents, the prior centered layout made it difficult to track who was communicating with whom; the left-aligned sender/recipient row model brings agent conversation clarity closer to a conventional messaging thread. [61][45][40] |
| **Perplexity** | **Perplexity Computer continues to be the platform's dominant update surface — all seven changelogs from June to October 2026 have Computer in the heading or opening; Computer runs asynchronously in a secure cloud sandbox with a persistent filesystem; Remote MCP Server (launched October 30) remains the key recent developer-layer primitive, now a live production endpoint at api.perplexity.ai/mcp** — the Computer-first update cadence signals a product-level bet that task execution, not search response, is the primary value driver going forward; the Remote MCP Server makes Perplexity's search and Computer capabilities a zero-local-infrastructure callable endpoint for any agent in any MCP-compatible pipeline. [70][65][68] |

---

## Product Highlights

### Claude / Anthropic: Message Threads Cut Agent Latency and 2.1.317 Fixes Multi-Agent Effort Inheritance

Anthropic's most structurally significant interaction-design advance in this window is not a UI change but a developer-layer primitive that materially changes the experience of working with long-running Claude agents: the **Message Threads public beta**, which launched November 2 and is already live in Claude Code for most users with no configuration required.



Anthropic introduced Message Threads in public beta on November 2, 2026, allowing Messages API applications on the Claude Platform to send only new messages after an initial full-conversation request — without a thread, each turn uploads the entire conversation again, and the API validates and tokenises all of it again; with a thread, most of that work applies only to the new turn.

 The latency consequence is concrete: 

Anthropic opened the public beta of Message Threads on November 2, 2026, and on Claude Code it is already live for most users, cutting Claude Code's median time to first token by 35% on long sessions.

 The trust-design primitive governing the feature is equally important: 

between turns, Anthropic holds each thread in memory, where it is encrypted and not written to disk; a thread expires 5 minutes after its last request, and the client then resends the full conversation to start a new one.

 This ephemeral, encrypted in-memory storage model is the correct default for a latency-optimisation feature that necessarily holds conversation state server-side — users who are concerned about persistence can trigger a natural expiry by simply waiting; they do not need to opt out of a durable store.

The 35% TTFT reduction has compounding effects on multi-agent agentic pipelines. In a loop where a Claude Code orchestrator calls a subagent ten times in a long session, the prior pattern meant ten full-conversation resends accumulating latency with each turn; Message Threads collapse that to one full send plus nine incremental sends. 

There is no API to list, read, or delete threads; threads do not support Message Batches, token counting, compaction on demand, or most context editing, and they are unavailable to organisations with Inference hooks enabled.

 These constraints are the correct scope for a beta — by launching without thread management surfaces, Anthropic avoids creating new attack surface (enumerable thread stores, deletable conversation histories) before the threat model is fully understood.



Claude Code 2.1.317, shipping November 3, adds a notice in Claude Desktop's Code tab when remote managed settings haven't loaded for the session, fixes a project's effortLevel setting being ignored by sessions that an app starts ahead of time, and fixes Claude saying a working connector needed authorisation when a synced plugin included the same server.

 The effort-level fix is the most operationally significant for multi-agent practitioners: 

2.1.317 changed subagents on a different model to run with that model's saved effort

 — previously, a subagent assigned to a lighter model could silently inherit the orchestrator's higher effort setting, producing unexpected cost and latency profiles mid-pipeline. Separately, 

2.1.317 adds a warning to /schedule when a new cloud scheduled task gets connectors the user did not ask for, with instructions on how to remove them

 — a transparency improvement for the class of agentic scheduling UX failure where background tasks silently acquire more access than the user intended.

On the policy layer, 

Anthropic has published an update to its Usage Policy taking effect November 12, 2026, consolidating rules surrounding influence operations, civic engagement, defence, and surveillance, with a new dedicated section "Do Not Engage in Deceptive Campaigns or Artificial Activity" bringing together previously scattered restrictions regarding fake accounts, fabricated news sites, and coordinated influence infrastructure.

The policy explicitly prohibits unauthorised use of model outputs to train other AI models, including model scraping and distillation, and bans using Claude to conduct malicious cyber attacks, develop malware, or commit fraud.

 The operator-facing addition with the most direct interaction-design implication is the new requirement for physical hardware: 

new operator oversight and safe-state requirements apply to scenarios where Claude is connected to hardware.



---

### ChatGPT / OpenAI: The Chat-Work Merge Expands and the Shared Usage Pool Takes Shape

OpenAI's most consequential interaction-design move in this window is the continued and expanding rollout of the **Chat and Work tab merge** — announced November 2 and now moving beyond its initial test group toward broader general availability. The structural significance of this change is not what it adds but what it removes: the requirement that a user decide, before articulating a task, whether they are about to "chat" or "work."



The ChatGPT desktop app can be a confusing piece of software, given that there are ChatGPT and Codex sections and, within the former, Chat and Work tabs; with so many options, it is sometimes easy to forget where you are working and where exactly your project is; in an apparent effort to address this, OpenAI is now gearing up to merge the Chat and Work tabs within the ChatGPT experience.

OpenAI described the goal in its subscriber email: "This will enable you to move from exploring an idea to having ChatGPT carry it through, all in one place. You can bring in your files and plugins and ask ChatGPT to build a website, create a presentation, or do things for you on the web, while reviewing and guiding its work. Codex will remain a separate experience in the ChatGPT desktop app."



The decision to keep Codex separate is the correct architectural boundary and merits explicit recognition. Codex is a project-scoped, long-running, terminal-adjacent code agent whose interaction model is structurally different from the conversational surface that suits the merged Chat+Work experience; forcing it into an open-ended conversational container would degrade the specialised task clarity that makes it valuable for deep code generation. 

The change also reshapes how usage limits work: OpenAI said that once the switch takes effect, ChatGPT and Codex will both pull tokens from a shared allowance pool; the combined experience will initially reach a select group of users for feedback before a wider rollout, so the single-view layout will not appear for everyone at once.

 The usage-pool unification is the temporal-UX change that most affects power users' planning: 

OpenAI says Unlimited Instant is included in the subscription and won't count towards the shared usage limit

 — preserving the light-query use case from being throttled by heavy agentic Codex sessions. 

OpenAI's Help Centre says that from December, ChatGPT and Codex usage will count toward a shared allowance for Plus, Pro, and Business plans.



---

### Google Gemini: Whole-Deck Editing Completes the Presentation Production Loop

Google's most consequential Workspace Gemini interaction-design advance in this window extends in-document AI editing from the single-slide level to the **whole-deck level in Google Slides** — a capability announced October 29–30 that closes the last major gap in Gemini's presentation production story.



Users can now use Gemini in Google Slides to edit multiple slides or an entire presentation at once; with a single prompt in the Slides side panel, they can update content throughout a deck, refresh visual styles in bulk, or match the style of another presentation; Gemini determines which slides need to change and applies edits directly to native, editable slides, so users stay in full control to make any further adjustments.

 The UX significance of "native, editable slides" is the preservation of the user's ownership over the artifact: Gemini does not export a flattened image or create a new file — it edits the existing slide objects in place, leaving every modified element as a standard editable Slides element the user can continue to adjust manually. 

Once Gemini finishes, a summary of the changes appears in the side panel

 — the correct audit-trail design for a batch multi-slide edit: the user can review exactly what Gemini changed before accepting the result, rather than discovering unexpected changes by scrolling through the deck.

This feature is architecturally distinct from the in-chat file editor announced October 29. 

The Slides update is distinct from the recently announced editor inside the Gemini chat app: the Slides update acts on an existing, editable Google Slides presentation through its side panel; the chat feature lets people create and preview supported files within a conversation before opening or exporting them.

 The two capabilities serve different moments in the presentation workflow — the chat editor is the creation surface, the Slides side-panel editor is the revision surface — and together they cover the complete loop without requiring the user to leave either environment.

The interaction-design patterns enabled by whole-deck editing are precisely the kind of multi-step bulk operations that previously required either manual slide-by-slide repetition or export to a third-party tool: 

examples include refreshing visual styles such as fonts, backgrounds, and colour schemes across the entire deck; combining multiple slides into one or adding new slides to an existing deck; and making styling consistent by aligning title styles or removing page numbers across all slides.



---

### Microsoft Copilot: Notebooks Become Workspaces, a New Home Arrives, and Office Agents Are Retired

Microsoft's interaction-design work in this 48-hour window arrives in three concurrent streams that together represent the most sweeping Copilot surface consolidation since the app launched: a rename that clarifies the collaboration model, a new navigation surface that unifies the starting point, and the retirement of specialised document agents in favour of integrated Chat capabilities.

The first stream is the **Copilot Notebooks → Copilot Workspaces** rename and redesign. 

Copilot Notebooks is now Copilot Workspaces, a shared place for teams to keep project files and information together and work with Copilot; existing notebooks become workspaces automatically, with nothing to move.

 The distinction between Workspaces and the newly introduced **Projects** is the critical UX design detail: 

Projects are for the user's own work, keeping chats, tasks, files, and results in one place, findable on the Home tab and usable with Chat and Cowork; Workspaces are for group work, giving a team a shared place to work with Copilot on a workstream.

 This Projects/Workspaces split is the correct conceptual architecture for an enterprise agent product: a personal Project scoped to one user's task context, versus a shared Workspace scoped to a team's ongoing workstream, are genuinely different interaction primitives with different governance, sharing, and context-accumulation requirements.

The second stream is the **new Copilot Home navigation**. 

Microsoft introduced Home as the new starting point that brings Chat and Cowork together, so users can get chat assistance and delegate multi-step tasks in one view; this announcement adds worldwide rollout timing and the addition of Projects and Workspaces to the Home experience.

In the interface, users open Chat or Cowork from the Home experience instead of separate top-level tabs; Home is the entry point, with Chat and Cowork presented as choices within it rather than as separate top-level tabs.

Projects in Copilot give users one place for related chats, Cowork tasks, and everything they share — files, instructions, and outputs; adding context once means every chat and task in the project builds on it, so users don't have to re-explain their work.



The third and most structurally consequential stream is the **retirement of standalone Word, Excel, and PowerPoint agents**. 

Microsoft 365 Copilot will replace standalone Word, Excel, and PowerPoint agents with integrated document creation and editing in Copilot Chat, with rollout starting mid-November 2026 and completing by late December.

As the change reaches users, the standalone agents will be removed from the left rail and agent discovery, and users will no longer be able to find, pin, @mention, or invoke them as separate agents.

 The interaction-design implication is the same one driving the OpenAI Chat-Work merge and the Gemini in-chat editor: separate, named, invocable agents for each document type are a navigation overhead that a mature agentic chat surface should not require. 

Users will create or refine documents, spreadsheets, and presentations directly in Copilot Chat without selecting a separate agent.



---

### Grok (SpaceXSI): Grok Build 1.0.74 Brings Multi-Agent Conversation Clarity

SpaceXSI's most interaction-design-significant release in this window is **Grok Build 1.0.74**, which addresses a longstanding visual clarity problem in multi-agent sessions and ships a session-resume performance improvement for practitioners working with large session stores.



Grok Build CLI updated with v1.0.74; messages between subagents now appear as left-aligned rows under the bullet that names the sender and recipient, replacing the centred rows.

 This rendering change is the most UX-significant item in the release for practitioners running multi-agent pipelines. In a Grok Build session with several simultaneous subagents — the platform supports up to eight — the prior centred layout made it structurally difficult to follow which subagent was communicating with which, because centred rows gave no visual anchor to the sender's identity. The new left-aligned sender/recipient row model maps onto a conventional messaging thread convention, making agent-to-agent communication legible at a glance. 

The update also makes /new tabs show the context window just switched to before the new session replies

 — a context-awareness signal that prevents the disorientation of landing in a new session with no visible indication of which context scope is active.



grok --resume opens much faster on large session stores, reading only the resumed session instead of every session

 — a temporal-UX improvement for practitioners with long project histories: previously, resuming any session triggered a full scan of the session store, making resume latency proportional to the total number of stored sessions rather than the size of the session being resumed. 

Grok Build 0.2.111 enables Workflows by default

 — the most significant configuration-surface change in the 0.2.x branch, converting Workflows from an opt-in feature to the standard execution model for all Grok Build sessions. 

The grok-imagine-image-quality API slug retires today (November 2) in favour of grok-imagine-image-2.0

, completing the API surface cleanup that eliminates legacy endpoint names that could create silent routing confusion in integrations that had not been updated.

---

### Perplexity: Computer Dominates the Update Cadence as the Platform's Agentic Identity Crystallises

Perplexity's most structurally significant interaction-design development in this briefing window is not a discrete feature release but an observed product trajectory that the window's research makes unambiguously clear: the platform's entire update cadence has pivoted from search to task execution.



Perplexity new feature tracking reveals that since the start of 2026, the feature named Computer has surpassed the search screen in terms of the volume of updates; all seven changelogs from June to October 2026 have "Computer" in either the heading or the beginning of the body text.

 The interaction-design significance of this cadence signal is that Perplexity has, in product terms, repositioned itself from a search interface with an AI layer to an agent interface with a search capability — Computer is the product, and search is a tool Computer calls. 

Computer runs asynchronously in a secure cloud sandbox with a persistent filesystem, meaning it can work on a project for extended periods without requiring user supervision.

Computer is an agent that takes a goal rather than a question, with features including deep research reports run inside Computer, Model Council mode that runs one query across several models and merges the answers, and Personal Computer that lets Computer work with files and apps on the user's own machine.

 The multi-model routing architecture is the UX primitive that most distinguishes Computer from single-model agent competitors: 

Grok 4.6 is available to Pro and Max subscribers in Perplexity Computer, GPT-5.6 Terra is the new default for Computer subagents, and GPT-5.6 Luna powers scheduled automations

 — a pipeline where the orchestrator can select the optimal model for each subagent task rather than committing to a single model for the entire workflow. The Remote MCP Server (announced October 30 and now in production) extends this model-routing architecture beyond Perplexity's own interface: any MCP-compatible agent orchestrator can now call Perplexity's search and Computer capabilities as a zero-local-infrastructure endpoint, converting Perplexity into an on-demand tool for any multi-agent pipeline rather than solely a destination product.

---

## The Bigger Picture: Agent Latency, Unified Homes, and the Office-in-Chat Pivot

The 48 hours ending November 3, 2026 crystallise a structural shift that has been building across the entire Agent2Agent2Human ecosystem for the better part of the year: **the application agent as a navigable destination is being replaced by the chat surface as the universal execution environment**. The evidence is simultaneous across every platform in this window. Microsoft retires three standalone Office agents and builds their capabilities into Copilot Chat. OpenAI removes the tab that separated conversational and agentic work. Google extends Gemini's editing authority to entire Slide decks, eliminating the need to leave the Workspace Slides editor for bulk transformation tasks. Anthropic ships Message Threads to eliminate the latency tax of long-running agent conversations, making the session itself a more viable container for extended agentic work. Perplexity's entire changelog cadence for the second half of 2026 shows Computer — the execution-first, task-oriented surface — absorbing the platform's development attention at the expense of the search interface that defined the product's identity for its first three years. Each of these moves is individually defensible as a UX simplification; together, they constitute a platform-wide bet that the future of the AI agent interface is a single surface that receives any request and routes it to the appropriate execution context without requiring the user to make that routing decision themselves. The design challenge this creates is governance: when a user in a unified chat surface asks Copilot to "fix the presentation and book the follow-up meeting," the system must correctly route document editing to the integrated Office capability and calendar actions to the scheduling integration — without the user ever selecting an agent or specifying a mode. The agent orchestration that happens invisibly between those two tasks is where the real trust-design work now lives, and none of the platforms in this window have yet built a transparency surface that makes that invisible routing legible to the user who initiated it. That gap — between the simplicity of the unified input and the complexity of the multi-agent execution it triggers — is the defining interaction-design problem of the next phase.

---

## References

[1] kucoin.com. (2026). *Anthropic Updates Claude Policy to Prohibit Reselling Subscriptions and Client Spoofing*. [https://www.kucoin.com/news/flash/anthropic-updates-claude-policy-to-prohibit-reselling-subscriptions-and-client-spoofing](https://www.kucoin.com/news/flash/anthropic-updates-claude-policy-to-prohibit-reselling-subscriptions-and-client-spoofing)

[2] cdnping.org. (2026). *Claude Usage Policy Update 2026 (Nov 12): Developer Checklist*. [https://cdnping.org/en/blog/anthropic-usage-policy-update-2026-11](https://cdnping.org/en/blog/anthropic-usage-policy-update-2026-11)

[3] hyperight.com. (2026). *Anthropic Targets Deceptive Campaigns and Consolidates Surveillance Restrictions*. [https://hyperight.com/anthropic-targets-deceptive-campaigns-and-consolidates-surveillance-restrictions/](https://hyperight.com/anthropic-targets-deceptive-campaigns-and-consolidates-surveillance-restrictions/)

[4] techflowpost.com. (2026). *Anthropic Updates Claude Usage Policy, Prohibiting Unauthorized Model Distillation and Malicious Cyber Attacks*. [https://www.techflowpost.com/en-US/newsletter/142484](https://www.techflowpost.com/en-US/newsletter/142484)

[5] unite.ai. (2026). *Anthropic Launches Message Threads Beta for Long-Running Agents*. [https://www.unite.ai/anthropic-launches-message-threads-beta-for-long-running-agents/](https://www.unite.ai/anthropic-launches-message-threads-beta-for-long-running-agents/)

[6] pasqualepillitteri.it. (2026). *Anthropic launches message threads, cutting Claude Code wait time by 35%*. [https://pasqualepillitteri.it/en/news/29685/anthropic-message-threads-claude-code-faster](https://pasqualepillitteri.it/en/news/29685/anthropic-message-threads-claude-code-faster)

[7] claude.com. (2026). *Make long-running agents faster with message threads*. [https://claude.com/resources/articles/message-threads](https://claude.com/resources/articles/message-threads)

[8] gradually.ai. (2026). *Claude Code Changelog (November 2026)*. [https://www.gradually.ai/en/changelogs/claude-code/](https://www.gradually.ai/en/changelogs/claude-code/)

[9] github.com/ellismosss. (2026). *scout: Claude Code changed to 2.1.317*. [https://github.com/ellismosss/optimizer/issues/13](https://github.com/ellismosss/optimizer/issues/13)

[10] dev.classmethod.jp. (2026). *Key Updates in Claude Code v2.1.317*. [https://dev.classmethod.jp/en/articles/20261103-cc-updates-v2-1-317/](https://dev.classmethod.jp/en/articles/20261103-cc-updates-v2-1-317/)

[11] techcrunch.com. (2026). *OpenAI is finally merging ChatGPT's Chat and Work tabs*. [https://techcrunch.com/2026/11/02/openai-is-finally-merging-chatgpts-chat-and-work-tabs/](https://techcrunch.com/2026/11/02/openai-is-finally-merging-chatgpts-chat-and-work-tabs/)

[12] tech.yahoo.com. (2026). *OpenAI Merges ChatGPT's Chat and Work Tabs Into One*. [https://tech.yahoo.com/ai/chatgpt/articles/openai-merges-chatgpts-chat-tabs-203600585.html](https://tech.yahoo.com/ai/chatgpt/articles/openai-merges-chatgpts-chat-tabs-203600585.html)

[13] bleepingcomputer.com. (2026). *OpenAI says it's doubling Pro usage limits and bringing Work features to Chat*. [https://www.bleepingcomputer.com/news/artificial-intelligence/openai-says-its-doubling-pro-usage-limits-and-bringing-work-features-to-chat/](https://www.bleepingcomputer.com/news/artificial-intelligence/openai-says-its-doubling-pro-usage-limits-and-bringing-work-features-to-chat/)

[14] businesstoday.in. (2026). *ChatGPT could soon do much more than answer questions: Here's what OpenAI is changing*. [https://www.businesstoday.in/technology/news/story/chatgpt-could-soon-do-much-more-than-answer-questions-heres-what-openai-is-changing-565295-2026-11-03](https://www.businesstoday.in/technology/news/story/chatgpt-could-soon-do-much-more-than-answer-questions-heres-what-openai-is-changing-565295-2026-11-03)

[15] workspaceupdates.googleblog.com. (2026). *Edit entire presentations with Gemini in Google Slides*. [https://workspaceupdates.googleblog.com/2026/10/edit-entire-presentations-with-gemini-in-Google-Slides.html](https://workspaceupdates.googleblog.com/2026/10/edit-entire-presentations-with-gemini-in-Google-Slides.html)

[16] mixed-news.com. (2026). *Gemini can now edit your entire Google Slides deck from one prompt*. [https://mixed-news.com/en/google-slides-gemini-edit-entire-presentation-one-prompt/](https://mixed-news.com/en/google-slides-gemini-edit-entire-presentation-one-prompt/)

[17] smartscope.blog. (2026). *Gemini in Google Slides: Edit Entire Presentations with a Single Prompt*. [https://smartscope.blog/en/blog/gemini-google-slides-edit-entire-presentations-single-prompt-2026/](https://smartscope.blog/en/blog/gemini-google-slides-edit-entire-presentations-single-prompt-2026/)

[18] m365admin.handsontek.net. (2026). *Microsoft Copilot app: Updates to Home and navigation*. [https://m365admin.handsontek.net/microsoft-copilot-app-updates-home-navigation/](https://m365admin.handsontek.net/microsoft-copilot-app-updates-home-navigation/)

[19] supersimple365.com. (2026). *Copilot Workspaces replaces Notebooks*. [https://supersimple365.com/copilot-notebooks-is-now-copilot-workspaces/](https://supersimple365.com/copilot-notebooks-is-now-copilot-workspaces/)

[20] support.microsoft.com. (2026). *Copilot Notebooks Is Now Copilot Workspaces*. [https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-to-copilot-workspaces](https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-to-copilot-workspaces)

[21] m365admin.handsontek.net. (2026). *Changes to Word, Excel, and PowerPoint agents in Microsoft Copilot*. [https://m365admin.handsontek.net/changes-word-excel-powerpoint-agents-microsoft-copilot/](https://m365admin.handsontek.net/changes-word-excel-powerpoint-agents-microsoft-copilot/)

[22] pupuweb.com. (2026). *MC1536062 Changes to Word, Excel, and PowerPoint agents in Microsoft Copilot*. [https://pupuweb.com/mc1536062-changes-to-word-excel-and-powerpoint-agents-in-microsoft-copilot/](https://pupuweb.com/mc1536062-changes-to-word-excel-and-powerpoint-agents-in-microsoft-copilot/)

[23] mc.ai-news.cz. (2026). *MC1519856: Projects in Copilot*. [https://mc.ai-news.cz/message/MC1519856](https://mc.ai-news.cz/message/MC1519856)

[24] x.com/GrokInsider. (2026). *Grok Build CLI v1.0.74 changelog*. [https://x.com/GrokInsider/status/2117422476128919654](https://x.com/GrokInsider/status/2117422476128919654)

[25] x.ai. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog)

[26] note.com/saishinai. (2026). *Inside Perplexity's New Features*. [https://note.com/saishinai/n/n78271b12b87f?hl=en](https://note.com/saishinai/n/n78271b12b87f?hl=en)

[27] dev.to/kowshik_jallipalli. (2026). *Why Perplexity's New "Computer" Just Changed the AI Agent Game*. [https://dev.to/kowshik_jallipalli_a7e0a5/why-perplexitys-new-computer-just-changed-the-ai-agent-game-4m19](https://dev.to/kowshik_jallipalli_a7e0a5/why-perplexitys-new-computer-just-changed-the-ai-agent-game-4m19)

[28] secondtalent.com. (2026). *Perplexity AI Features and Capabilities in 2026: The Complete Guide*. [https://www.secondtalent.com/resources/perplexity-ai-features-capabilities-2026/](https://www.secondtalent.com/resources/perplexity-ai-features-capabilities-2026/)

---