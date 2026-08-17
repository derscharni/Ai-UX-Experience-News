# UX Briefing: Provenance Signals, Generative Canvases, and the Ambient Desktop Agent

**August 17, 2026**

Good morning. The 48 hours ending August 17 are shaped by four distinct but converging design bets about what AI agents should leave behind — in the workspace, on the filesystem, and in the output itself. **Anthropic** makes its most consequential trust-transparency move since launching auto mode, with full public confirmation that Claude models released on or after August 2 embed invisible watermarks into all generated text and attach C2PA-signed provenance metadata to image files, worldwide and at the model level with no opt-out; simultaneously, the **Claude Compliance API** completes its expansion to cover Cowork and Claude Code sessions under a single audit endpoint in beta for Enterprise customers, and the Claude Code desktop app ships an **auto-continue checkbox** that closes the most-requested temporal UX gap in agentic coding — sessions now resume automatically after a usage-limit reset without human intervention. **Google** lands the most significant generative-UI event in Workspace history: **Sheets Canvas**, a Gemini-powered capability that transforms any spreadsheet into a read-write interactive mini-application from a plain-language prompt, rolling out to Rapid Release domains from August 10 and explicitly positioned to compete with Airtable, Notion, and Coda on their home turf. **ChatGPT/OpenAI** ships two trust-design primitives in parallel — **Google Drive in Library**, which lets paid users browse, annotate, and directly edit Drive files from inside the chat without leaving the session, and **Computer History** for macOS, an opt-in feature that builds a timeline of app and web activity to give ChatGPT and Codex persistent cross-session context. And **Grok (xAI)** completes the broadest distribution launch for a single model in this cycle, with **Grok 4.6 now selectable in GitHub Copilot across eight development surfaces** — VS Code, Visual Studio, the Copilot CLI, the cloud agent, JetBrains IDEs, Xcode, Eclipse, and the Copilot app — making it the first xAI model to reach the developer environments where enterprise agentic coding decisions actually get made.

---

## At a Glance: August 17 Highlights

Today's releases collectively ask what an AI agent leaves behind — in the form of provenance signals in its outputs, audit trails across its sessions, interactive UIs generated from its prompts, and context it accumulates from a user's desktop — and the answers arriving this window reveal a platform-by-platform theory of what "transparency" means in practice.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude text and file outputs now carry invisible watermarks and C2PA provenance metadata globally** — model-level marking, no opt-out, applies across claude.ai, Claude Code, Cowork, Tag, and cloud partners; Compliance API expands to cover Cowork and Claude Code sessions in one unified audit endpoint (beta for Enterprise); Claude Code desktop ships auto-continue checkbox for usage-limit recovery; GitLab MR support, custom TLS certs, and Linux memory cap land in the same update wave. [1][2][3] |
| **ChatGPT** | **Google Drive in Library ships to Plus, Pro, Enterprise, Edu, Healthcare, and Business** — users can browse, @mention, and edit Drive files (Docs, Sheets, Slides) directly inside the chat without switching windows; Computer History (opt-in, macOS) builds a timeline of app and web activity for ChatGPT and Codex context; interactive quizzes, per-project memory switching, and personalized homepage suggestions also launch this week. [4][5][6] |
| **Google Gemini** | **Sheets Canvas launches August 10–13** — Gemini turns any spreadsheet into a custom read-write interactive mini-app (Kanban boards, dashboards, seating charts) from a plain-language prompt, with bidirectional real-time sync; Google Meet now auto-generates structured notes, action items, and full transcripts into Google Docs on meeting end; Gemini 3.7 Flash hits GA in the Enterprise mobile app. [7][8][9] |
| **Microsoft Copilot** | **Copilot app retirement wave lands August 18** — Group Chats, Podcasts, Copilot Labs, and consumer Deep Research all retire as the unified app consolidation completes; a build-regression bug removed Copilot buttons from classic Outlook (build 20026.20182+) for both Basic and Premium license holders, currently under active Microsoft investigation; SharePoint Canvas HTML dashboards continue rolling out. [10][11][12] |
| **Grok (xAI)** | **Grok 4.6 enters GitHub Copilot across eight surfaces** — VS Code, Visual Studio, Copilot CLI, cloud agent, Copilot app, JetBrains, Xcode, and Eclipse; selectable from model picker for Pro, Pro+, Max, Business, and Enterprise plans; doubled included usage in Grok Build and Cursor through August 19; Grok Build ships custom TLS root certs, clickable session rows, and faster subagent spawning. [13][14][15] |
| **Perplexity** | **Perplexity Computer enters Microsoft Teams** and deepens enterprise controls — Computer in Teams enables agents inside Word, Excel, PowerPoint, Outlook, and Teams; Deep Research in Computer turns research outputs directly into reports, spreadsheets, and decks within a single session; Agent API expanded with additional third-party model support (Claude Opus 4.8, Gemini 3.5 Flash, Grok families). [16][17][18] |
| **Samsung** | **Galaxy S26 ships with Perplexity at the OS level** — first non-Google company to receive system-level access on a Samsung device; "Hey Plex" wake word, side-button shortcut, and deep integration across Samsung Notes, Calendar, Gallery, Clock, and Reminders; Perplexity APIs now power Bixby's real-time web search and reasoning backend. [19][20][21] |

---

## Product Highlights

### Claude / Anthropic: Watermarks as Trust Infrastructure and the Audit-Trail Completion

Anthropic's most consequential trust-design event in this window is now fully confirmed and in active public discussion: all Claude models launched on or after August 2, 2026 embed invisible watermarks into generated text and attach signed provenance metadata to image files, globally, with no opt-out mechanism for users. 

Starting August 2, 2026, every Claude model launched from that date onward produces text with an embedded digital watermark, and the official documentation describes "an imperceptible watermark woven into the words themselves" — a signal that the reader cannot see and that does not alter meaning, quality, or readability.

 The compliance trigger is explicit: 

Anthropic will add machine-readable watermarks to text generated by new Claude models starting August 2, 2026, responding to transparency requirements under Article 50 of the EU AI Act.

 The governance scope is wider than most users initially understood: 

the marking happens at the model level, not the product level — it appears regardless of where the text comes from: the platform API, Claude's web interface, Claude Code, Claude Cowork, Claude Tag, and even when a supported model runs inside AWS Bedrock, Google Cloud, or Microsoft Foundry.



The file-provenance system runs alongside the text watermark on a different technical track. 

On files in supported formats — .svg, .png, and .jpg — a package of cryptographically signed provenance metadata is attached following the open C2PA standard; the signed metadata also serves to detect whether a file has been tampered with after generation.

 On August 14, Anthropic published a full technical FAQ on the mechanism, 

naming it a version of Google DeepMind's SynthID-Text and citing real quality data from an A/B test on live Gemini traffic and a controlled human-rater study for the first time.

 The UX implication that warrants careful reading is what the watermark does and does not prove: 

a detected watermark means that content may have been assessed or processed by Claude, not that Claude wrote it.

 This distinction matters enormously for workflows where Claude edits, translates, or corrects human-authored material — the provenance signal can travel with content the human substantially authored, which is the source of the user backlash the announcement generated. 

The marks survive copying and light edits but fade with heavy changes, and detection tools will soon let anyone verify them; users have shared mixed feelings, from irony over data scraping to worries about their own writing picking up marks during edits, with some canceling subscriptions and developers building tools to remove them.



The **Claude Compliance API expansion** that lands in the same window is the enterprise audit-trail event the watermark story overshadowed. 

Claude's Compliance API now covers Cowork across the desktop app, web, and mobile, as well as Claude Code in the CLI and desktop app, with coverage in beta for Claude Enterprise customers; compliance and security teams can pull session content and metadata from both products through the same Compliance API interface they already use for Claude chats.

The new session endpoints return a consolidated, server-hosted transcript for each Cowork and Claude Code session, so prompts, responses, and tool activity come back together in a single session record.

 The trust-design significance of this expansion is the closure of what was the most consequential audit gap in Anthropic's enterprise offering: agentic coding and collaborative Cowork sessions were previously invisible to the compliance layer that governed regular Claude chats. That gap closes in beta here. The **auto-continue checkbox** for Claude Code desktop is the temporal UX fix that operationalises long-running agentic tasks more directly than any model capability change. 

On August 14, Anthropic's official developer account posted that hitting a usage limit in Claude Code desktop now surfaces an auto-continue checkbox — turn it on and it will automatically continue where you left off once your limit resets.

This is part of the same broader pattern: Anthropic shipping automation that reduces how much a human needs to babysit a running session, whether that's approving actions or restarting a stalled one.

 The CLI still lacks the feature — it is desktop-only for now — which means overnight unattended runs on the CLI path still require third-party tooling to bridge the gap.

---

### ChatGPT / OpenAI: Google Drive in the Workspace and Computer History as Persistent Context

OpenAI's most interaction-design-significant launch in this window is **Google Drive in Library**, which fundamentally changes the relationship between the chat session and a user's existing document store. 

If you have the Google Drive plugin connected, you can now see and browse your Google Drive files and folders directly from Library, including items shared directly with you; you can also quickly pull up a Drive file from the composer or with @mentions and add it to any chat without uploading it again.

 The deeper capability is live document co-editing: 

when working with a file, users can now keep Google Docs, Sheets, and Slides open beside the conversation while asking ChatGPT to summarise, analyse, compare, or create something new from them; users can also select a folder and ask ChatGPT to work across the files it contains.

ChatGPT edits the actual file in Google Drive, rather than copying a static file based on the existing document.

 The UX shift this represents is from upload-and-forget to live-grounded document editing: the AI is not working on a snapshot; it is working on the live source of truth, which means every edit it makes propagates immediately to the shared Drive rather than requiring a re-upload cycle.

The second major trust-design launch running in parallel is **Computer History** for the ChatGPT macOS desktop app. 

Computer History is an optional feature in the ChatGPT macOS app that lets ChatGPT and Codex reference selected activity from apps and websites, helping users continue work without re-explaining every detail; it records interaction events — not screenshots, screen recordings, microphone input, or system audio — and private browsing is not included.

 The governance architecture that makes enterprise adoption viable is the admin-gate pattern: 

Computer History is off by default and available to Pro, Business, and Enterprise users, with Business and Enterprise admins required to grant access before members can opt in.

 The trust-design distinction that makes Computer History different from Perplexity's Personal Computer is the narrowness of what it records — interaction events rather than screen content — which is the architectural choice that keeps the permission surface legible enough for enterprise security teams to approve. 

For eligible unshared projects, users can now switch between default and project-only memory without starting a new project.

 The memory-scope toggle on existing projects is the governance primitive that makes memory feel safe for professional use — the ability to bound what the agent knows to a single project before sharing that project with a team.

---

### Google Gemini: Sheets Canvas and the Generative UI Moment in Workspace

Google's most UX-consequential launch in this window is not an agent product or a model update — it is a generative-UI primitive built into a surface that 900 million people already have open. 

Google has launched Sheets Canvas, a new Gemini-powered capability that transforms spreadsheets into custom, interactive, read-write applications using simple natural language prompts.

 The interaction design of Sheets Canvas is a significant departure from how generative AI has been grafted onto productivity tools: 

key capabilities include end-to-end creation — building an advanced visualization with a single natural language prompt without requiring coding, formulas, or third-party tools — and it is fully read-write, meaning changes made in the canvas, such as dragging task cards or adding new entries, instantly update the source sheet.

Users can open a spreadsheet, select "Create canvas" in the Ask Gemini side panel, and describe the result they want in natural language; Gemini builds a layout from the existing data, and follow-up prompts can alter its design, arrangement, or functionality; edits made in either the canvas or the underlying sheet sync in real time; because the canvas lives as a tab in Google Sheets, it can be shared with collaborators like a regular sheet.



The competitive positioning is explicit: 

the launch puts Google in direct competition with Airtable, Notion, and Coda — not by building a new platform, but by grafting their core value proposition onto a spreadsheet hundreds of millions of those platforms' target users already have open.

 The UX implication for the broader generative-UI space is that Google is betting the spreadsheet as a data model is already good enough — that users do not need a new application paradigm, they need a better rendering layer on top of the data they already maintain. That is a fundamentally different bet from building a new agentic canvas from scratch, and it has a significant adoption advantage: the context is already there. In **Google Meet**, a parallel UX event ships in the same window: 

when a meeting finishes, Gemini automatically compiles a structured notes summary, action items, and complete transcript into a Google Doc, saved directly to Google Drive, and emails the link to the user.

 This is the full-session ambient capture pattern — the meeting requires no explicit summarisation prompt; Gemini monitors the session and generates the structured output at the boundary event of meeting end, which is the temporal UX primitive that makes passive capture feel supervised rather than surveillance.

---

### Microsoft Copilot: The Retirement Wave Lands and the Outlook Regression

Microsoft's most consequential UX event in this window is not a feature launch but the completion of the retirement timeline announced August 13. 

Account updates begin on August 18, 2026; before the account updates, users are advised to download any media shared by other participants they want to keep; Podcasts is being retired from Copilot and will no longer be available after August 18, 2026 — after retirement, customers will no longer be able to create or access Podcasts in Copilot.

Deep Research is being retired in the Copilot app for consumers starting August 18, 2026; users who have used Deep Research to create detailed reports and analyses in Copilot may have questions about what this change means; the Microsoft support page explains what is changing and how to access existing research content.

 The interaction design verdict encoded in these retirements is a clear organisational signal: the consumer experiment is over, the enterprise-and-premium surface is the design focus, and the surviving features are those where the governance contract is clear and the output is auditable.

The trust-and-reliability event running alongside the planned retirement is an unplanned one: a build regression in Classic Outlook for Windows. 

A bug appearing with build 20026.20182 of classic Outlook prevents access to Copilot Chat and removes Copilot entry points within the app — as a Microsoft support document reads: "After classic Outlook for Windows updates to build 20026.20182 and higher, you no longer have Copilot Chat or Copilot entry points in Outlook. This issue happens if you have a Copilot Chat (Basic) license or a paid M365 Copilot (Premium) account."

Microsoft accidentally broke Copilot integration in Outlook Classic while trying to integrate more AI-powered features.

The Microsoft support page for known issues lists the Copilot buttons situation as currently "INVESTIGATING".

 The UX design implication of this incident is worth noting beyond the immediate bug: Microsoft has committed to releasing no new features for Outlook Classic unless AI-related, which concentrates the regression risk of its rapid AI integration cadence on the surface that enterprise users are most reluctant to leave. 

On the SharePoint side, Copilot in SharePoint can now turn a list, Excel file, or CSV into a live, interactive HTML dashboard that stays connected to the underlying data and refreshes each time it's opened — the update also adds one-click "page buttons" that launch a saved Copilot prompt, shifting Copilot from simply answering questions to helping users build and act on content.



---

### Grok (xAI): Grok 4.6 Goes Ecosystem-Wide in GitHub Copilot

SpaceXAI's most significant UX-distribution event in this window is the completion of Grok 4.6's rollout into GitHub Copilot. 

xAI's Grok 4.6 is now rolling out in GitHub Copilot, two days after the model's August 12 release; outside Copilot, Grok 4.6 remains available through xAI's API, Cursor, Grok Build, and partners including OpenRouter, Vercel, and Cloudflare.

 The distribution breadth is unusually wide: 

the model is selectable from Copilot's model picker across eight surfaces — VS Code, Visual Studio, the Copilot CLI, the Copilot cloud agent, the Copilot app, JetBrains IDEs, Xcode, and Eclipse; GitHub's changelog confirms the rollout covers Copilot Pro, Pro+, Max, Business, and Enterprise plans.

That spread is unusually wide for a new model addition: JetBrains, Xcode, and Eclipse support puts Grok 4.6 in front of developers well outside the VS Code core where most Copilot model launches concentrate.

 The interaction-design significance of GitHub Copilot as a distribution target is that it is not a model-picker toggle — it is an enterprise admin approval decision. 

With the Business and Enterprise policy gate now in administrators' hands, the pace of the model's enterprise uptake will show up in Copilot settings before it shows up in any leaderboard.



On the Grok Build side, the same window delivers meaningful developer-experience reliability improvements. 

Grok Build adds custom TLS root certs — via GROK_EXTRA_CA_BUNDLE — faster terminal resize, and fixes task and approval handling; it also adds clickable session rows, faster subagent spawning, and smoother high-refresh TUI rendering, with /session-info letting users click any row to copy its value with hover highlights and a copy-all shortcut.

 The custom TLS root cert support is the enterprise deployment primitive that has been missing from Grok Build's early releases: without it, teams running corporate network proxies with internal certificate authorities could not route Grok Build traffic through their inspection layer, which blocked enterprise adoption as surely as a missing feature. Its arrival signals that Grok Build's enterprise deployment posture is maturing alongside its model capabilities. 

The 2x doubled included usage in Grok Build and Cursor closes on August 19, 2026

 — the final day of the first-week adoption window that xAI used to accelerate workflow integration at the point of model launch.

---

### Perplexity: Computer Enters Microsoft Teams and the Enterprise Skills Layer Deepens

Perplexity's most UX-significant development in this window is the expansion of **Computer** into Microsoft Teams, completing the M365 integration arc the company began in June 2026. 

Computer is now faster, more powerful, and more connected to the enterprise with improved models, Microsoft Teams, and skills in Spaces.

Perplexity's agentic product is now available directly inside Word, Excel, PowerPoint, Outlook, and Teams, letting users draft documents, analyse spreadsheets, build presentations, and manage communications using context already present across their files and email.

 The interaction pattern this creates is a Computer agent that lives inside the tools enterprise workers already have open — not a separate agentic window they must switch to, but an orchestration layer embedded in the productivity surface. The UX significance is the same architectural bet Microsoft makes with @mention-invoked agents in Copilot Chat: the human does not leave the workflow to access the agent; the agent arrives inside the workflow when invoked.

The **Agent API** expansion continuing in this window deepens the programmable surface for developers building on Perplexity's orchestration stack. 

The Agent API added support for Claude Opus 4.8, Gemini 3.5 Flash, Gemini 3.1 Flash Lite, and the Grok 4.3 and 4.20 family, all with direct first-party token pricing.

 The addition of cross-lab model support — Claude, Gemini, and Grok families accessible through Perplexity's orchestration layer — is the multi-model routing primitive that makes Perplexity's Agent API a genuine orchestration platform rather than a Sonar-only search wrapper. For enterprise developers, 

Perplexity adds enterprise roles and permissions, custom API credentials, Brain memory in more languages, and SCIM group sync with credit usage limits per group; custom roles, SCIM group sync, and group credit limits are available to Enterprise orgs on an annual sales contract.



---

### Samsung: The First Multi-Agent OS and What It Means for Ambient UX

Samsung's Galaxy S26 launch — confirmed shipping in this window — is the most consequential mobile UX event of the period from an ambient-agent design perspective: it establishes the first smartphone operating system explicitly designed around a multi-agent user model. 

Perplexity is now integrated into Samsung Galaxy S26 phones at a deep level, powering search and reasoning for both the Perplexity assistant and Samsung's Bixby — making Perplexity the AI behind two of the three assistants on the device; the integration was built at the system level, with a dedicated wake word, access to physical controls, and the ability to read from and write to native apps like Notes, Calendar, Gallery, Clock, and Reminders; Perplexity is the first non-Google company to have OS-level access in a Samsung phone.

 The UX architecture Samsung has shipped is explicitly agent-routing rather than single-assistant: 

Samsung confirmed it will expand Galaxy AI to offer a multi-agent system, with deep Perplexity integration leading the charge; Samsung has always offered Bixby alongside Google Assistant and Gemini as virtual assistants, but with One UI 8.5 it expands this lineup further by adding Perplexity as part of its multi-agent expansion.



The trust-design questions this architecture raises for UX practitioners are significant: when three distinct agents — Bixby, Gemini, and Perplexity — have OS-level access to the same native apps, the permission model is no longer "did the user authorise this agent?"; it becomes "which agent did the user invoke, and which apps can that agent reach?" 

Samsung designed the S26 around a multi-agent approach; their internal data shows that 8 in 10 users already rely on more than two AI agents daily, and Samsung is the first major device maker to match the operating system to that behavior.

 The interaction pattern that emerges from this is not assistant-switching — it is agent-selection at the task level, with the OS routing intent to the appropriate agent based on the invocation mechanism and the task type. 

Samsung's Bixby uses Perplexity's APIs on the backend for its search and reasoning capabilities; the APIs combine real-time web search with large language model reasoning, so Bixby can deliver grounded, up-to-date answers rather than relying on static training data alone.



---

## The Bigger Picture: Provenance Signals, Generative Canvases, and the Ambient Desktop Agent

The 48 hours ending August 17, 2026 are defined not by a single product arc but by three separate design questions that have each reached a resolution point simultaneously. The first is the provenance question: what does AI-generated content leave behind, and who can read it? Anthropic's watermark implementation — model-level, worldwide, no opt-out, with a forthcoming public detection API — is the most comprehensive answer any major lab has shipped, and it raises the hardest design challenge in the space: a watermark that marks Claude-edited content in addition to Claude-authored content is a trust signal that can mislead as easily as it can inform. Google's Meet auto-summary and Sheets Canvas are provenance answers of a different kind — not signals embedded in output, but structured outputs that make the agent's contribution explicit and editable by design, without requiring any detection layer. The second question is the ambient context question: how should an agent know what a user has been doing, without asking them to explain it repeatedly? OpenAI's Computer History on macOS, Samsung's Perplexity OS integration, and Perplexity's Computer-in-Teams expansion each answer this from a different layer — the desktop timeline, the device OS, and the enterprise productivity suite — but all three share the same underlying design bet: ambient context should be opt-in, auditable, and bounded by surface rather than universal. Microsoft's Compliance API parallel at Anthropic and ChatGPT's admin-gated Computer History are the governance expressions of this same bet in enterprise deployments. The third question is the generative-UI question: where does AI generation belong in the document interface? Sheets Canvas is the most data-grounded answer in this window — it generates the interactive layer directly from the user's existing structured data, keeps the two surfaces in real-time bidirectional sync, and requires no new application model. Google's answer is that generative UI belongs inside the data the user already maintains, not in a separate canvas they must populate from scratch. The convergence across all three questions is visible in the Grok 4.6 GitHub Copilot rollout: a model designed for long-running agents is being placed behind the admin approval gate of the enterprise coding environment, which means the trust architecture of the IDE — not the model's capabilities — will determine how quickly the agentic workflow default shifts.

---

## References

[1] Interesting Engineering. (2026). *Copy-paste no more: Anthropic puts invisible watermarks on Claude text under EU rules*. [https://interestingengineering.com/ai-robotics/anthropic-claude-text-invisible-watermarks](https://interestingengineering.com/ai-robotics/anthropic-claude-text-invisible-watermarks)

[2] Claude by Anthropic. (2026). *Compliance API coverage extends to Claude Cowork and Claude Code*. [https://claude.com/blog/compliance-api-cowork-and-claude-code](https://claude.com/blog/compliance-api-cowork-and-claude-code)

[3] explainx.ai. (2026). *Claude Code Auto-Continue Checkbox Explained (Aug 2026)*. [https://explainx.ai/blog/claude-code-desktop-auto-continue-usage-limit-august-2026](https://explainx.ai/blog/claude-code-desktop-auto-continue-usage-limit-august-2026)

[4] Releasebot. (2026). *ChatGPT Updates by OpenAI — August 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[5] 9to5Mac. (2026). *ChatGPT subscribers can now open and edit Google Drive files from inside the chat*. [https://9to5mac.com/2026/08/14/chatgpt-subscribers-can-now-open-and-edit-google-drive-files-from-inside-the-chat/](https://9to5mac.com/2026/08/14/chatgpt-subscribers-can-now-open-and-edit-google-drive-files-from-inside-the-chat/)

[6] OpenAI Help Center. (2026). *ChatGPT — Release Notes*. [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

[7] Google Workspace Updates. (2026). *Use Sheets canvas to visualize data in custom, interactive mini-apps*. [https://workspaceupdates.googleblog.com/2026/08/use-google-sheets-canvas-to-visualize-data.html](https://workspaceupdates.googleblog.com/2026/08/use-google-sheets-canvas-to-visualize-data.html)

[8] Google Blog. (2026). *Bring your spreadsheet data to life with Sheets canvas*. [https://blog.google/products-and-platforms/products/workspace/sheets-canvas-for-google-sheets-spreadsheets/](https://blog.google/products-and-platforms/products/workspace/sheets-canvas-for-google-sheets-spreadsheets/)

[9] Releasebot. (2026). *Google Release Notes — August 2026*. [https://releasebot.io/updates/google](https://releasebot.io/updates/google)

[10] Microsoft Support. (2026). *Updates to Copilot and the Microsoft Copilot app*. [https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app](https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app)

[11] Windows Latest. (2026). *Microsoft confirms it accidentally disabled Copilot in Outlook Classic*. [https://www.windowslatest.com/2026/08/15/microsoft-confirms-it-accidentally-disabled-copilot-in-outlook-classic-and-we-wish-it-wasnt-a-mistake/](https://www.windowslatest.com/2026/08/15/microsoft-confirms-it-accidentally-disabled-copilot-in-outlook-classic-and-we-wish-it-wasnt-a-mistake/)

[12] CIAOPS. (2026). *CIA Brief 20260815*. [https://blog.ciaops.com/2026/08/15/cia-brief-20260815/](https://blog.ciaops.com/2026/08/15/cia-brief-20260815/)

[13] GitHub Changelog. (2026). *Grok 4.6 is now available in GitHub Copilot*. [https://github.blog/changelog/2026-08-14-grok-4-6-is-now-available-in-github-copilot/](https://github.blog/changelog/2026-08-14-grok-4-6-is-now-available-in-github-copilot/)

[14] Unite.AI. (2026). *Grok 4.6 Arrives in GitHub Copilot Across Eight Development Surfaces*. [https://www.unite.ai/grok-4-6-arrives-in-github-copilot-across-eight-development-surfaces/](https://www.unite.ai/grok-4-6-arrives-in-github-copilot-across-eight-development-surfaces/)

[15] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Releases.sh. (2026). *Perplexity Release Notes & Changelog — August 2026*. [https://releases.sh/perplexity](https://releases.sh/perplexity)

[17] fatjoe.com. (2026). *Perplexity AI Stats July 2026: Uses, Users, Market Share, and More*. [https://fatjoe.com/blog/perplexity-ai-stats/](https://fatjoe.com/blog/perplexity-ai-stats/)

[18] Releasebot. (2026). *Perplexity Release Notes — July/August 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[19] Perplexity AI Hub. (2026). *Perplexity APIs deliver powerful AI to the world's largest Android device maker*. [https://www.perplexity.ai/hub/blog/perplexity-apis-deliver-powerful-ai-to-the-world%E2%80%99s-largest-android-device-maker](https://www.perplexity.ai/hub/blog/perplexity-apis-deliver-powerful-ai-to-the-world%E2%80%99s-largest-android-device-maker)

[20] Android Police. (2026). *Galaxy S26 will add Perplexity to Samsung's AI lineup*. [https://www.androidpolice.com/galaxy-s26-will-add-perplexity-to-samsungs-ai-lineup/](https://www.androidpolice.com/galaxy-s26-will-add-perplexity-to-samsungs-ai-lineup/)

[21] 9to5Google. (2026). *Galaxy S26 will have a 'Hey Plex' Perplexity hotword alongside 'Hey Google' & Bixby*. [https://9to5google.com/2026/02/22/samsung-galaxy-s26-perplexity-integration/](https://9to5google.com/2026/02/22/samsung-galaxy-s26-perplexity-integration/)