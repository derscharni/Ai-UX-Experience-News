# UX Briefing: Supply Chain Trust, In-Chat Document Editing, and the Agentic Shopping Surface

**October 30, 2026**

Good morning. The 48 hours ending October 30, 2026 are marked by a simultaneous challenge on two fronts: the **trust and safety layer of the agent-tool delivery pipeline**, exposed overnight by the Cursor marketplace trojanization incident affecting the Claude Code extension, and a surge of new interaction-surface advances that together push the frontier of what a chat conversation can contain — a file canvas, a shopping carousel, a task-delegation workspace. **Claude/Anthropic** faces the most consequential trust-design incident of this window: a trojanized **Claude Code 2.1.313** extension circulated in the Cursor marketplace for approximately eleven hours on October 29, exposing up to 5,000 developer machines to a persistent SSH backdoor — triggering Cursor to shutter its entire marketplace, neutralize the malware, and restore access; Anthropic has published the clean **Claude Code 2.1.314** to both Open VSX and the Microsoft VS Code Marketplace. Separately, **Claude Code's October 30 changelog** ships a tightly focused cluster of gateway and multi-agent reliability fixes. **ChatGPT/OpenAI** ships **GPT-6.1 Terra** into ChatGPT Work and Codex as the new mid-tier default for visual reasoning and computer-use tasks, and doubles Work and Codex usage allowances for Pro and Business Premium plans — two changes that together reshape how power users manage agentic workload budgets. **Google Gemini** makes its most significant conversational-surface advance in months: **in-chat file preview and editing**, announced October 29, which eliminates the generate-download-edit-re-upload loop across documents, PDFs, presentations, spreadsheets, and code — all within the chat thread. **Microsoft Copilot** advances the **Copilot Notebooks** workspace in Frontier, adding task delegation, model choice, Office file editing on canvas, and interactive reports, converting Notebooks from a source-grounded Q&A tool into a project execution surface. **Grok (xAI/SpaceXSI)** ships **Grok Bot 0.78.1**, which introduces product cards with photo carousels, order tracking, Shop Pay Vault integration, and subscription-management templates — the most agentic commerce interaction pattern yet shipped by any major AI agent platform.

---

## At a Glance: October 30 Highlights

Today's window is defined by a convergence of supply-chain trust (where does a developer's tool actually come from, and how would they know if it was tampered?), generative document surface design (the chat thread as the primary editing environment), and the emergence of agentic commerce as a first-class interaction pattern inside AI agent UIs.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Trojanized Claude Code 2.1.313 circulated in the Cursor marketplace for ~11 hours on October 29, affecting up to 5,000 users; Anthropic published clean 2.1.314 to Open VSX and Microsoft VS Code Marketplace; October 30 changelog fixes gateway key leakage, policy loading, agent flag persistence across auto-updates, and non-interactive subcommand blocking** — the 2.1.313 incident is the first major supply-chain trust event in the Claude Code extension ecosystem; the clean 2.1.314 skips the compromised version number entirely; October 30 fixes include agents losing `--model`, `--effort`, and `--permission-mode` after auto-update relaunches, and stray `Authorization` headers leaking to Foundry/Vertex/Bedrock upstreams. [1][2][3] |
| **ChatGPT** | **GPT-6.1 Terra rolls out October 26 in ChatGPT Work and Codex for Plus, Pro, Business, Enterprise, and Edu plans — visual reasoning plus precise computer use; Dot text-message access via iMessage and RCS launches in beta for US Pro users; ChatGPT doubles Work and Codex usage allowances for Pro and Business Premium on October 29** — Terra is scoped to Work and Codex only, not Chat; the iMessage/RCS Dot texting beta makes the proactive agent reachable without opening any app; doubled allowances directly expand how many delegated computer-use tasks a Pro user can run per period. [4][5][6] |
| **Google Gemini** | **In-chat file generation, preview, and editing ships October 29 to all Gemini users in all supported languages: generate, preview, and edit documents, PDFs, presentations, spreadsheets, Markdown, and code without leaving the chat; three edit modes — full-screen manual edit, highlight-and-prompt, and conversational follow-up; Neural Expressive design overlay rolls out to all Android devices October 29** — PDF preview/edit works on web and mobile; all other file types are web-only at launch; highlight-and-prompt edit is the highest-precision interaction mode, minimizing the risk of unintended edits. [7][8][9] |
| **Microsoft Copilot** | **Copilot Notebooks October 2026 update (Frontier): task delegation from notebook chat, model choice per chat, in-notebook Office file editing on canvas, interactive reports, PDF creation, and expanded reference types (Markdown, TXT, RTF); Copilot Feedback UX update rolling out late October adds selectable issue categories to thumbs-down** — task delegation and model choice are in Frontier now; scheduled automations and audio overview updates arrive in coming weeks; the feedback update adds structured thumbs-down categories for more actionable signal, applying to organizational, consumer, and education accounts. [10][11][12] |
| **Grok (xAI/SpaceXSI)** | **Grok Bot 0.78.1 ships October 27: shopping results render as product cards with photos, ratings, price, store, and badges; four-item photo carousel; order tracking with carrier and shipment stage; Shop Pay Vault integration; three subscription-management templates (Try It/Don't Pay, Find Unused Subscriptions, Watch Subscription Prices); Bots confirm with user before cancelling anything** — 0.78.1 is the fullest expression yet of commerce as an agentic interaction pattern; the confirm-before-change trust pattern applies to all cancellation and payment operations; connector error display now shows connector name instead of internal ID. [13][14][15] |
| **Perplexity** | **Perplexity Remote MCP Server now available as a hosted endpoint at api.perplexity.ai/mcp, connecting any MCP client via Streamable HTTP with API-key bearer token — no local server process required; Gemini 4 Argon added to Agent API; xhigh preset output budget raised to 512,000 tokens** — the Remote MCP Server converts Perplexity's search and Computer capabilities into an always-on, zero-local-infrastructure MCP endpoint any agent can call; the Gemini 4 Argon addition brings multi-model orchestration flexibility to the Agent API. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: Supply-Chain Trust Crisis and Clean Recovery via 2.1.314

The most significant Claude interaction-design event in this window is not a capability release but a trust-design emergency: the **Claude Code 2.1.313 supply-chain compromise**, which ran in the Cursor marketplace for approximately eleven hours on October 29, 2026, before being identified and neutralised.



A modified version of the Claude Code extension, 2.1.313, stayed on the Cursor marketplace from 2:27 to 13:35 Pacific time on October 29, 2026.

 The attack vector exploited the Cursor-specific distribution channel: 

the attackers distributed it as version 2.1.313 under Anthropic's legitimate Claude Code extension ID (anthropic.claude-code), and the malicious update was distributed only through Cursor's marketplace, with no evidence that it reached Open VSX or Microsoft's official VS Code Marketplace.

 The response was immediate: 

Cursor temporarily shut down the marketplace, removed the malicious software in coordination with service providers, and reopened it after confirming no further risks; users are advised to update the extension to version 2.1.314 and scan for malicious packages.



The trust-design implication for the Claude Code ecosystem is structural. 

Cursor and other VS Code forks run their own extension stores, so each operator must secure its own publishing pipeline.

 The attack succeeded not because of a flaw in Claude Code itself but because Cursor's marketplace accepted a malicious package under a legitimate publisher identity — a class of supply-chain vulnerability that is distinct from model-layer or tool-layer failures, and one that the broader ecosystem of Claude Code distributions (CLI on npm, Open VSX, Microsoft Marketplace, Cursor) must now treat as a first-class threat surface. 

Anthropic's Claude Code changelog goes from 2.1.312 to 2.1.314, with no 2.1.313 entry

 — the correct recovery posture: by skipping the compromised version number entirely in the official changelog, Anthropic ensures that automated systems comparing installed version to latest release will flag any instance of 2.1.313 as anomalous rather than current.

Separately, 

the October 30 Claude Code changelog fixes feature flag, startup, fast mode, profile, and feedback requests carrying the API key configured for a third-party gateway; fixes agents losing `--model`, `--effort`, `--permission-mode`, `--allow-dangerously-skip-permissions`, and `--agent` after an auto-update relaunch; and fixes the Claude apps gateway sending stray host Authorization or profile headers to Foundry, Vertex, and Bedrock upstreams.

 The agent flag persistence fix is the most operationally significant for practitioners running multi-agent pipelines: when a Claude Code agent auto-updates mid-session and relaunches, the previous behaviour silently dropped the operator-configured effort level, model, and permission profile — producing a post-update session that could behave substantially differently from the pre-update session without any visible signal to the operator.

---

### ChatGPT / OpenAI: GPT-6.1 Terra Brings Visual Reasoning into the Computer-Use Agentic Loop

OpenAI's most consequential interaction-design advance in this window is the arrival of **GPT-6.1 Terra** in ChatGPT Work and Codex — a model whose design philosophy is explicitly scoped to the agentic, computer-use workflow rather than the general chat surface.



GPT-6.1 Terra is rolling out in ChatGPT Work and Codex, supports a range of tasks including visual reasoning, computer use, and writing, and the rollout includes Plus, Pro, Business, Enterprise, and Edu plans.

 The surface-scoping decision is the interaction-design detail that warrants the most practitioner attention: 

in ChatGPT, it can be used in Work and Codex, but cannot be selected in Chat.

 This is the correct design for a model built around computer-use orchestration — by restricting Terra to Work and Codex, OpenAI ensures that users encounter it only in the interaction contexts where visual reasoning and multi-step computer control are the operative behaviours, rather than in the free-form Chat surface where a computer-use-optimised model would be incongruously specialised.

The practical consequence for agentic workflows is significant. 

It's a fast, efficient model for professional work that combines strong image understanding with precise computer use — use Terra to reason about images and screens, then take action across your browser, desktop, and apps.

 The read-screen-then-act loop is the core agentic computer-use primitive, and Terra's positioning as the mid-tier model for this loop — rather than requiring the full Sol or Astra reasoning effort for every computer-use step — is the correct cost-to-capability mapping for the class of work that involves many lightweight visual-reasoning decisions (is this form field filled correctly? does this UI state match the expected state?) interspersed with occasional deeper reasoning steps.

Accompanying Terra's rollout, 

ChatGPT doubled Work and Codex usage allowances for Pro and Business Premium plans, with Pro 200 increases starting October 29.

 Separately, 

Dots can now be reached through iMessage or RCS on Android for one-to-one conversations with text, photos, and voice messages — texting is rolling out in beta to ChatGPT Pro users in the US.

 The iMessage/RCS Dot access is the ambient-delegation advance with the broadest daily-workflow reach: it makes OpenAI's proactive background agent reachable through the messaging surface that Pro users already have open all day, without requiring them to open the ChatGPT app or a browser.

---

### Google Gemini: In-Chat File Editing Collapses the Document Production Loop

Google's most structurally significant Gemini interaction-design release in this window is the elimination of a friction loop that has defined every AI-assisted document workflow since generative file creation was introduced: the generate-then-leave cycle. **In-chat file preview and editing**, announced October 29, keeps the document inside the conversation from creation through to final export.



Google is introducing new ways to create and refine files and code in the Gemini app — users can now generate, preview, and edit files right within the Gemini app chat by expanding to full screen to type edits directly, highlighting text to ask questions, or having Gemini refine them; PDF preview and editing is supported on both the web and mobile, while all other formats are supported on the web only.

 The interaction-design shift this enables is precise: 

a file created in a Gemini conversation no longer needs to leave the chat to be revised — users can generate a file, preview it in place, and edit it without switching to a separate application.



The three-mode editing design is the correct interaction-design architecture for a chat-native document editor. 

Users can expand to full screen and type changes themselves, highlight text to ask a question, or ask Gemini to refine the file.

 Each mode serves a different precision level: the full-screen manual mode is for precise character-level corrections the user can make faster than prompting; highlight-and-prompt is the highest-trust mode for scoped AI edits, because the selection explicitly bounds what the model can touch; and conversational follow-up is the lowest-friction mode for structural changes where the user trusts Gemini's interpretation of the intent. The fact that all three are available in the same session — and the user can switch between them freely — is what makes this a genuine editing surface rather than a prompt-and-pray workflow. 

PDF preview and editing are supported on gemini.google.com and the mobile apps, while Google Docs, Google Sheets, Google Slides, Markdown files, TXT files, and code are web-only.



Arriving on the same day, 

Google is rolling out a redesigned Gemini overlay across Android phones, introducing sparkling animations and Google's Neural Expressive design language to more devices through the Google app.

The refreshed Gemini overlay began appearing through Google's latest app update on October 29, 2026; previously, the animation appeared on Pixel 11 devices, limiting access to Google's newer visual experience — the wider rollout now extends the redesigned interface to Android users without requiring a new Pixel phone.

 The design democratisation is significant from a trust-UX perspective: when the ambient Gemini overlay that activates over any application looks materially different across device cohorts, it creates inconsistent mental models about what Gemini is and where it lives on the screen. The Neural Expressive rollout normalises that experience across the Android install base.

---

### Microsoft Copilot: Notebooks Becomes a Project Execution Surface in Frontier

Microsoft's most consequential Copilot interaction-design advance in this window is the transformation of **Copilot Notebooks** from a knowledge-collection and Q&A surface into a project execution environment — a shift that arrives in Frontier and establishes the design direction for the next phase of the Microsoft agentic workspace.



The October 2026 update brings task delegation, recurring automations, direct Office editing, interactive reports, and new ways to turn project information into polished deliverables.

 The task delegation capability is the most structurally significant: 

Copilot can now carry out simple tasks — use Copilot to manage references and keep notebooks current, synthesize information across project context, and create and edit single files like Word, Excel, or PowerPoint documents from chat; users can scope a prompt to just the Notebook or change to "Work and web" for broader context beyond the references.

 The scope-toggle between Notebook-only and Work-and-web context is the correct trust-design primitive for task delegation inside a curated knowledge workspace: a user who has assembled a specific set of references for a project can confine the agent's context to exactly that set, preventing it from pulling in ambient Work context that might be relevant but unintended.



Frontier users can view documents inline, edit files on the canvas, or prompt Copilot to add content — such as an intro paragraph or a graph — or restyle fonts and layouts, with teams co-editing alongside.

 The co-editing dimension is the temporal-UX advance that matters most for enterprise teams: when multiple team members can edit the same artifact from within a shared Notebook, the Notebook becomes the shared workspace for a delegated deliverable — not a personal scratchpad that one person then shares. 

Model choice is available in Frontier, allowing users to pick the model per chat for deeper reasoning or a GPT model.



Simultaneously, 

Microsoft Copilot is updating the thumbs-down feedback to include selectable issue categories and optional comments for more actionable input, rolling out worldwide in late October 2026.

When a user selects thumbs down on a Copilot response, they may see selectable categories describing the issue, can select more than one category, and can optionally enter additional feedback in a free-text field.

 This is the correct trust-design evolution for a product at Copilot's deployment scale: a binary thumbs-down signal tells the platform that something went wrong but not what class of failure occurred — the categorical feedback surface gives the platform actionable signal that can drive specific improvement, while the optional free-text field preserves the ability to capture edge cases the taxonomy doesn't anticipate.

---

### Grok (xAI/SpaceXSI): Grok Bot 0.78.1 Makes Agentic Commerce a First-Class Interaction Pattern

SpaceXSI's most interaction-design-significant release in this window is **Grok Bot 0.78.1**, which ships the fullest expression yet of commerce as a native agentic workflow pattern — converting shopping, order tracking, and subscription management from actions the user performs inside third-party apps into tasks the agent handles within the conversation surface, with explicit confirmation checkpoints at every financial action.



Shopping with a Bot now shows products as cards with photos, rating, price, and store, plus up to two badges such as "Top rated" — three or four product results scroll in a carousel, and users can swipe through each product's photos.

 The product-card format is the correct interaction-design choice for agentic shopping recommendations: a plain text list of product names and prices requires the user to context-switch to a browser to evaluate each option, breaking the agentic loop; the card format with photo carousel gives the user enough visual and contextual information to make a selection entirely within the agent conversation. 

After an order is placed, the Bot tracks it and tells the user when it ships or arrives, with shipment cards showing the carrier and stage.

 This closes the post-purchase loop: the agent that initiated the order also monitors it, surfacing status updates in the same conversation thread rather than requiring the user to check a retailer's tracking page.

The subscription-management templates are where the trust-design work in 0.78.1 is most clearly visible. 

Three subscription workflows ship: "Try it, don't pay for it" starts a free trial and cancels it or reminds the user before billing; "Find unused subscriptions" can cancel plans the user chooses from subscriptions they still pay for; and "Watch subscription prices" checks renewal prices.

 The trust-design primitive that governs all three is the confirmation checkpoint: 

Bots can cancel a subscription or look up its price and renewal date, and confirm with the user before changing anything.

 This is the correct pattern for any agentic action that has financial consequences and is difficult to reverse — the agent proposes, the user confirms, the agent executes. The explicit confirm-before-change architecture prevents the class of agentic failure where an agent interprets "clean up my subscriptions" as authorisation to cancel services the user did not intend to cancel. 

App cards, plugin rows, sign-in errors, and connector errors the Bot relays now show the connector's name instead of an internal ID

 — a transparency improvement that ensures users can identify which connector is responsible for a given error without decoding platform internals.

---

### Perplexity: Remote MCP Server Converts Perplexity into a Zero-Infrastructure Agent Tool

Perplexity's most structurally significant interaction-design advance reaching practitioners in this window is not a consumer UI change but a developer-layer primitive that will quietly expand Perplexity's reach into multi-agent pipelines: the **Remote MCP Server**, now available as a hosted endpoint.



The Perplexity MCP Server is now available as a remote server hosted by Perplexity at `https://api.perplexity.ai/mcp`, allowing any MCP client that supports Streamable HTTP to connect using an API key as a bearer token, with no local server process required.

 The interaction-design significance of "no local server process" is the elimination of the integration overhead that has historically limited MCP adoption in ephemeral or constrained environments: a Claude Code subagent, a Codex session, or a Grok Build worktree that has network access can now call Perplexity's search and Computer capabilities without the orchestrating environment maintaining a local MCP server process. This is the correct architecture for a search-and-research tool that agents want to call opportunistically rather than setting up as a persistent local dependency.



The Agent API's xhigh preset now allows up to 512,000 output tokens, up from 128,000, and xhigh has used Fast Search since the October update that moved lower presets to Fast Search.

 The output budget expansion is the temporal-UX change that matters most for practitioners running long-horizon research tasks: an agent that previously hit the 128,000-token ceiling mid-task had to either truncate its output or restructure the task into multiple API calls — the 512,000-token ceiling makes large-document synthesis and extended research deliverables viable in a single API call. 

The Agent API now also supports `google/gemini-4-argon`, with introductory pricing through November 30, 2026.

 The Gemini 4 Argon addition gives Agent API operators a second frontier-tier reasoning option alongside existing OpenAI and Anthropic models, enabling the kind of per-task model routing — send the deep-reasoning task to Argon, the fast retrieval task to a lighter model — that defines mature multi-model agentic pipeline design.

---

## The Bigger Picture: Supply Chain Trust, In-Chat Document Editing, and the Agentic Shopping Surface

The 48 hours ending October 30, 2026 surface a structural tension that the entire Agent2Agent2Human ecosystem will need to resolve as it matures: the trust contract between a user and their agent tools now extends well beyond the model's behaviour or the platform's permission model — it reaches into the software-delivery infrastructure that keeps those tools current. The Claude Code 2.1.313 incident is the clearest articulation of the new threat surface: the agent was trustworthy, the platform was trustworthy, but the delivery channel — Cursor's extension marketplace — was the point of compromise. This is not a Claude Code failure or a Cursor failure in the narrow sense; it is the first high-profile demonstration that the marketplace layer for AI coding agent extensions has not yet developed the publisher-identity verification and signing infrastructure that the stakes of the agentic developer-tool category now demand. The correct long-term response is not user vigilance (check your version numbers) but platform-layer signing (cryptographic proof that a package was built by the claimed publisher, not merely labelled with their identity). Alongside this trust emergency, the product advances in this window are consistently pointing toward the chat thread as the primary work surface — not a gateway to work performed elsewhere. Google's in-chat file editing is the clearest expression: when a user can generate a presentation, preview it, highlight a section to refine, manually correct a data point, and then download or share — all without leaving the chat — the conversation thread has become a document editor. Microsoft's Copilot Notebooks Frontier update makes the same move at the knowledge-workspace layer: the Notebook is no longer where you store references before doing work in other apps; it is where you do the work. Grok Bot 0.78.1 makes the move at the commerce layer: the conversation is where you shop, track, and manage subscriptions — with the agent executing actions and the user confirming them without ever visiting a retailer's site. GPT-6.1 Terra's arrival in Work and Codex makes the move at the computer-use layer: the agent reasons about screens and takes action across browser and desktop as a native capability of the work surface, not a separately invoked tool. Perplexity's Remote MCP Server makes the move at the infrastructure layer: Perplexity's search and research capabilities are now a zero-overhead callable endpoint for any agent, anywhere. Taken together, these advances define the design agenda that the next phase of the agentic UX cycle must address: as the chat thread absorbs more of what used to require separate applications, the governance, auditability, and delivery-pipeline integrity of the tools that power that thread become as important as the quality of the AI reasoning inside it.

---

## References

[1] code.claude.com. (2026). *Claude Code changelog — October 30, 2026*. [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

[2] thehackernews.com. (2026). *Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor*. [https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html)

[3] technology.org. (2026). *Cursor Says Tampered Claude Code Extension Reached Up to 5,000 Users*. [https://www.technology.org/2026/10/30/cursor-tampered-claude-code-extension-5000-users/](https://www.technology.org/2026/10/30/cursor-tampered-claude-code-extension-5000-users/)

[4] help.openai.com. (2026). *ChatGPT release notes — October 26, 2026*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[5] learn.chatgpt.com. (2026). *October 26–30, 2026*. [https://learn.chatgpt.com/docs/whats-new/october-26-30-2026](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)

[6] releasebot.io. (2026). *ChatGPT Updates by OpenAI — October 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] workspaceupdates.googleblog.com. (2026). *Create, preview, and edit files directly in the Gemini app*. [https://workspaceupdates.googleblog.com/2026/10/create-preview-and-edit-files-directly-in-the-Gemini-app.html](https://workspaceupdates.googleblog.com/2026/10/create-preview-and-edit-files-directly-in-the-Gemini-app.html)

[8] unite.ai. (2026). *Gemini App Now Lets Users Edit Documents and PDFs In-Chat*. [https://www.unite.ai/gemini-app-now-lets-users-edit-documents-and-pdfs-in-chat/](https://www.unite.ai/gemini-app-now-lets-users-edit-documents-and-pdfs-in-chat/)

[9] analyticsinsight.net. (2026). *Google Gemini Redesign: New Sparkling Overlay Reaches Android Phones*. [https://www.analyticsinsight.net/news/google-gemini-redesign-new-sparkling-overlay-reaches-android-phones](https://www.analyticsinsight.net/news/google-gemini-redesign-new-sparkling-overlay-reaches-android-phones)

[10] techcommunity.microsoft.com. (2026). *What's New in Notebooks — October 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105)

[11] windowsreport.com. (2026). *Copilot Notebooks October 2026 Update Adds Office Editing, AI Automations & Interactive Reports*. [https://windowsreport.com/copilot-notebooks-october-2026-update-adds-office-editing-ai-automations-interactive-reports/](https://windowsreport.com/copilot-notebooks-october-2026-update-adds-office-editing-ai-automations-interactive-reports/)

[12] pupuweb.com. (2026). *MC1530595 Microsoft Copilot Feedback UX update*. [https://pupuweb.com/mc1530595-microsoft-copilot-feedback-ux-update/](https://pupuweb.com/mc1530595-microsoft-copilot-feedback-ux-update/)

[13] x.ai. (2026). *Grok Bot Changelog*. [https://x.ai/changelog/bot](https://x.ai/changelog/bot)

[14] fourweekmba.com. (2026). *xAI's Grok Bot Adds Shop Pay and Buy-Now Product Cards*. [https://fourweekmba.com/ai-xais-grok-bot-adds-shop-pay-and-buy-now-product-cards/](https://fourweekmba.com/ai-xais-grok-bot-adds-shop-pay-and-buy-now-product-cards/)

[15] aicatchup.com. (2026). *Grok Bot 0.78.1: Shopping, Shop Pay, and Subscriptions*. [https://aicatchup.com/news/grok-bot-v0-78-1-shopping-subscriptions](https://aicatchup.com/news/grok-bot-v0-78-1-shopping-subscriptions)

[16] docs.perplexity.ai. (2026). *Changelog — Perplexity*. [https://docs.perplexity.ai/docs/resources/changelog](https://docs.perplexity.ai/docs/resources/changelog)

[17] releasebot.io. (2026). *OpenAI Release Notes — October 2026*. [https://releasebot.io/updates/openai](https://releasebot.io/updates/openai)

[18] releasebot.io. (2026). *Gemini API Updates by Google — October 2026*. [https://releasebot.io/updates/google/gemini-api](https://releasebot.io/updates/google/gemini-api)