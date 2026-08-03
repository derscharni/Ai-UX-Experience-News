# UX Briefing: Surface Consolidations, Ambient Overlay Redesigns, and the Voice Agent Threshold

**August 03, 2026**

Good morning. The 48 hours ending August 3 are defined by a single structural thesis playing out across four separate platforms simultaneously: the standalone AI product surface is dying, and the ambient-embedded surface is winning. **Google** delivers the most decisive demonstration of this thesis by cancelling its AI Studio mobile app on July 31 — despite 800,000 pre-orders — and announcing that app-creation capabilities will live natively inside Gemini conversations instead, while simultaneously rolling out a full-screen frosted-glass overlay redesign to Android devices that replaces Gemini's floating card with an immersive, always-layered presence across the entire phone surface. **OpenAI** is six days from its own consolidation deadline: **ChatGPT Atlas** stops working on August 9, completing the collapse of a standalone AI browser back into the single ChatGPT desktop app — the most compressed product lifespan (nine months, macOS-only) of any major AI surface in this cycle. **xAI (SpaceXAI)** ships the most consequential voice-agent infrastructure change of the month with **Grok Voice Think Fast 2.0**, a speech-to-speech model that reasons in parallel with speaking and whose `grok-voice-latest` alias auto-migrates all connected voice agents on August 5 with no action required — the first forced-default voice model migration at scale the industry has seen. **Microsoft Copilot** confirms the final surface in Classic Outlook: a new persistent Copilot entry point above the ribbon, rolling from late August, completing the ambition to make Copilot a first-class layer of every email session rather than a tucked-away option — alongside the Cowork usage-limits window expiring August 5 on the Claude side, creating a rare moment where two platforms are simultaneously closing promotional windows that were designed to drive agentic habit formation.

---

## At a Glance: August 03 Highlights

The releases in this window collectively resolve a year-long design question — whether AI should be a separate place you go or a layer present wherever you already are — and the answer, from Google, OpenAI, Microsoft, and xAI simultaneously, is unambiguously the latter.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Cowork mobile/web doubled-limits window closes August 5** — the promotional habit-formation period for the July 7 multi-device expansion ends, with Cowork remote sessions (cloud-hosted, device-agnostic, scheduled tasks) now available to Max subscribers on iOS, Android, and web; legacy Workbench sunset continues toward August 17. [1][2][3] |
| **ChatGPT** | **ChatGPT Atlas browser deprecates August 9** — the nine-month macOS-only AI browser shuts down, folding all browsing and agentic capabilities into the ChatGPT desktop app (multiple tabs, downloads, account login support); users must manually export bookmarks, cookies, and open tabs before cutoff; GPT-5.4/mini retiring from Codex August 31. [4][5][6] |
| **Google Gemini** | **AI Studio mobile app cancelled July 31** despite 800,000 pre-orders — app-creation tools absorbed into Gemini's conversational flow instead; **Gemini Android frosted-glass overlay** rolling August 1–2, replacing floating card with full-screen immersive backdrop on Pixel 10 Pro XL and Galaxy S26 Ultra. [7][8][9] |
| **Microsoft Copilot** | **Copilot persistent entry point in Classic Outlook ribbon** — confirmed August 2026 GA rollout, contextual AI recommendations surface above the email workspace for the first time; Copilot inline rich images in responses now rolling (July 15–29 window); Copilot Search shorter summaries arriving late July to late August. [10][11][12] |
| **Grok (xAI)** | **Grok Voice Think Fast 2.0** launches July 29 — speech-to-speech with in-parallel reasoning, 0.70s first-audio latency, 82.9 quality index; `grok-voice-latest` auto-migrates all connected voice agents August 5; **Grok Build** adds MCP CLI controls, `/undo` slash command, streaming JSON headless output, and loop recovery. [13][14][15] |
| **Perplexity** | **Enterprise roles/permissions and SCIM group sync** ship July 27 — custom roles with granular permissions, group credit limits, custom API credential vault; **Claude Opus 5 now in Search and Computer**; **Computer in Comet Assistant** adds in-browser agentic execution; **Agent API Skills** extend multi-step orchestration to third-party workflows. [16][17][18] |

---

## Product Highlights

### Claude / Anthropic: The Cowork Habit-Formation Window and What Closes on August 5

Anthropic's most UX-consequential event in this window is not a new feature launch but the expiration of a deliberate design mechanism: the doubled **Claude Cowork** usage limits that have been running since the July 7 mobile and web expansion close on August 5. The timing is architectural — Anthropic extended the limits specifically to create a month-long window in which users could form the habit of delegating multi-step agentic work from any device, with no resource scarcity creating friction.



On July 7, 2026, Anthropic announced that Cowork — previously a desktop-app-only product — is expanding to the web at claude.ai and to mobile on iOS and Android in beta, starting with Max plan subscribers; the new surfaces run on remote sessions hosted on Anthropic's servers, saved to the Claude account, and able to keep working with no device online at all.

 The interaction-design shift this represents is the elimination of device-as-execution-boundary: 

from this update, users can delegate a task on their computer, close the lid to head into a meeting, and review the final result from their smartphone.

Cowork launched as a desktop-first idea — give Claude a task, access to local files and connected tools, and let it work autonomously while you watch — and the July announcement removes the desk from that equation; Cowork tasks can now be started, steered, and collected on the web, the desktop app, and the Claude mobile apps, and the session itself has moved to the cloud, untethered from any one machine.

 The trust-design nuance that matters here is the capability gradient across surfaces: 

mobile is strongest for starting tasks, checking status, steering mid-task, and picking up results, while deep local-folder access and desktop-file workflows remain the desktop app's territory.

 This capability transparency — the mobile surface is a monitor and director, not a full executor — is the right interaction model for a product that is asking users to delegate work they cannot fully observe.

The broader developer-platform context this week is the continued countdown toward the legacy Workbench retirement. 

The legacy Workbench at platform.claude.com/workbench is being sunset with access ending on August 17, 2026; saved prompts, variables, and evals are not supported in the updated Workbench, and users can export any data they want to keep from the banner and under Organizational Settings.

 The combination of the Cowork mobile launch with the Workbench retirement signals a consistent Anthropic design direction: consolidate the developer surface toward a more disciplined, cloud-hosted execution model while clearing the legacy tooling that accumulated during an earlier, more exploratory phase.

---

### ChatGPT / OpenAI: Atlas Closes August 9 and What It Proves About the Standalone AI Surface

OpenAI's most interaction-design-consequential event in this window is not a launch but a deadline that arrives in six days: **ChatGPT Atlas** stops working on August 9, 2026, completing the formal retirement of OpenAI's standalone AI browser and concentrating all agentic browsing capability inside the single ChatGPT desktop application.



Atlas was pitched as a new way to use the web, with ChatGPT sitting between search, browsing, and task automation — nine months later, the lesson looks blunt: the browser was the wrong package; Atlas launched on October 21, 2025 initially for macOS, and will not make it to its first birthday.

 The specific design failure that accelerated its end is one the whole industry should study: 

Atlas never escaped macOS during its eight-month lifespan — promised Windows, iOS, and Android versions were never released even as public betas — which limited its audience and kept it behind cross-platform competitors like Perplexity Comet and AI-enhanced versions of Chrome and Edge.

 Single-platform AI surfaces are not sustainable at consumer scale.



OpenAI is moving browser-based agentic capabilities into ChatGPT and Codex, building on what was learned from Atlas to support a more capable browser experience in ChatGPT including multiple tabs, downloads, improved navigation, account login support, and other browser improvements where available.

 The migration UX is notably ungoverned: 

before the shutdown, users should move any Atlas data they want to keep, as Atlas browser data including bookmarks, open tabs, and browser history will not transfer automatically; users can export cookies and passwords to the ChatGPT desktop app and bookmarks to Chrome.

 A manual-export-only migration path for a product that users have been actively using for months is the trust-design gap that this deprecation leaves open: there is no session-continuity guarantee, no automatic context migration, and no path for users who were relying on Atlas agent-mode workflows inside their daily browsing. 

OpenAI's product lead framed the move as a graduation rather than a failure, saying that Atlas users "taught us how agents can help make browsing and doing work on the open web better," with those lessons going into the main ChatGPT app instead of staying in a separate browser.



Separately, a model-picker governance change approaching in Codex matters for enterprise UX: 

on August 31, 2026, GPT-5.4 and GPT-5.4 mini will no longer be available in Codex for users signed in with ChatGPT, though they remain available on the OpenAI API and Codex sessions authenticated with an API key.

OpenAI is rolling out an updated model picker for ChatGPT Enterprise and Edu on web, iOS, and Android, making it easier to choose the balance of speed and reasoning effort that works best for a task without changing the underlying models available to a workspace.

 The model-picker redesign is the trust-design element worth watching: when the same picker must simultaneously communicate capability, reasoning effort, and speed tradeoff to a user choosing between Terra and Luna mid-task, the labelling and information architecture of that chooser is a consequential decision, not a cosmetic one.

---

### Google Gemini: AI Studio Absorbed, the Overlay Goes Frosted, and What Both Signal About the Gemini-as-Platform Play

Google has the most structurally significant UX event of the August 1–3 window, and it arrived not as a product launch but as a cancellation: on July 31, Google confirmed it would not release the standalone **AI Studio mobile app** despite roughly 800,000 pre-orders, choosing instead to fold app-building capabilities directly into the Gemini conversational interface.



The AI Studio team confirmed the decision in a post on X, saying: "Thank you to the ~800,000 of you that pre-ordered our mobile app on iOS and Android, it's clear that people are interested in building software on the go. Instead of asking you to download yet another app, we've decided to take an entirely different approach: one where apps emerge naturally, in the course of your everyday conversations with Gemini."

 The UX implication is profound: 

what the cancellation reveals about the future of the Gemini app is that Gemini being able to create apps that help address whatever problem or need you have while chatting sounds like the natural next step for generative user interfaces.

 Rather than a dedicated creation tool separate from the conversational surface, Google is betting that the conversational thread itself is the right context for app creation — the same interaction pattern that Grok Build Mode introduced in July and that Anthropic's dynamic view Labs experiments have been probing since I/O.



The cancellation, announced on July 31 via the official Google AI Studio account, is a striking move: 800,000 pre-registrations is a significant show of interest, and pulling the plug that close to release suggests an internal strategic shift rather than a technical problem.

 The strategic interpretation that matters for UX practitioners is precisely what Android Authority identified: 

rather than shipping a dedicated mobile experience, Google is folding the AI Studio mobile app into Gemini, and it looks like the company wants Gemini to be a central hub for all its AI experiences, rather than maintaining separate apps.



Simultaneously and independently, the Gemini Android surface is undergoing its most visible interaction redesign of 2026. 

On August 1, 2026, Google is rolling out a refreshed Gemini AI overlay, which was first teased at Google I/O.

The updated interface is appearing on both Pixel devices (like the Pixel 10 Pro XL) and Samsung hardware (like the Galaxy S26 Ultra); the signature visual tweak replaces the basic floating box with a prominent blurred backdrop.

 The design significance of the frosted-glass transition is about context-presence, not just aesthetics: the previous floating card communicated that Gemini was a guest on your screen — a bounded widget living within the app layer. The full-screen frosted backdrop communicates that Gemini is the ambient layer of the phone itself, present behind and above whatever you are doing. That is a fundamentally different relationship between the AI and the device surface, and it arrives on the same week that Google decided app-building should "emerge naturally, in the course of your everyday conversations" — the two changes are coherent expressions of the same design thesis.

---

### Microsoft Copilot: The Classic Outlook Ribbon and the Last Holdout Surface Gets Its AI Layer

Microsoft's most UX-consequential structural development in this window is the confirmation of the **Copilot Classic Outlook ribbon redesign** — a change that completes the coverage of every major Microsoft 365 surface with a persistent, context-aware Copilot entry point, including the one surface that had previously required users to actively seek it out.



Microsoft is planning a notable interface update for classic Outlook for Windows: a new, persistent Copilot entry point that sits above the email workspace, designed to make AI assistance more discoverable and context-aware; the change targets general availability in August 2026 and mirrors a Copilot interaction model already rolled out to other Outlook endpoints and Office desktop apps.

 The design shift from optional to persistent is the trust-UX event that enterprises need to prepare for: 

the heart of the update is not a new AI feature but a redesigned gateway to existing Copilot capabilities; instead of scattering Copilot controls across menus, ribbons, and context-specific buttons, Microsoft positions the assistant as a persistent layer directly above whatever the user is working on — be it an email, a calendar entry, or a draft reply.



The contextual intelligence architecture behind the placement is more consequential than the visual change: 

Copilot in Outlook Classic has contextual awareness, meaning it can read and understand entire email threads and surface contextual recommendations based on what it can see — for example, if a user is in a conversation about a refund for cancelled tickets, Copilot could help draft an email based on its understanding that a refund was previously requested.

 This thread-reading ambient awareness is structurally different from a side-panel assistant that waits to be invoked: the agent is now reading the same surface the user inhabits and acting on contextual understanding of its contents, making it an ambient participant rather than a tool. 

Microsoft has come unstuck in recent months over design decisions regarding Copilot and its productivity applications — a floating Copilot button in Word, Excel, and PowerPoint did not meet with universal approval, leading to a rare climbdown as Microsoft allowed users to move the button back to the ribbon area.

 The Outlook ribbon placement learns directly from that backlash: rather than a floating widget competing for screen real estate, the new entry point is anchored in the ribbon — the established structural convention of Classic Outlook — while still being persistent and default-on.

On the broader Copilot update front, 

Copilot now displays rich images from files and meetings directly within responses, having previously returned text only.

Visual information helps users understand complex content faster and reduces the need to switch between apps or documents.

 The inline-image pattern is the multimodal response design that makes Copilot's answers feel more like working with a document rather than reading a chat transcript — a subtle but important shift in the modality of the response surface.

---

### Grok (xAI): Voice Think Fast 2.0 and the Forced Default Migration as a Trust-Design Event

xAI's most UX-consequential release of this window arrived on July 29 and carries a hard action-deadline two days from now: **Grok Voice Think Fast 2.0**, a next-generation speech-to-speech model, ships with a mechanism that makes it the most structurally significant voice-agent launch since Claude's voice mode model-picker fix — because on August 5, `grok-voice-latest` auto-migrates every connected voice agent to the new model with no developer action required.



Grok Voice Think Fast 2.0 is xAI's next-generation voice model with improved intelligence, transcription accuracy, and conversational capabilities.

 The architectural differentiator that makes this more than a capability upgrade is the unified pipeline: 

the model brings faster response times, sharper transcription accuracy, and more natural conversational behaviour, with the updated model listening, reasoning, and speaking in a single unified pipeline, allowing it to respond with noticeably lower latency than its predecessor.

Grok Voice Think Fast models have a unique characteristic — they reason through queries while speaking; reasoning in parallel with speech makes the model substantially smarter than other speech-to-speech models with no impact on latency.

 The time-to-first-audio figure tells the production story: 

time to first audio fell from 1.25 seconds to 0.70 seconds.



The forced-default migration mechanism is the trust-design event that warrants careful examination by any team running voice agents on the platform. 

On August 5, 2026, `grok-voice-latest` will move from `grok-voice-think-fast-1.0` to `grok-voice-think-fast-2.0`; no action is needed to upgrade, but to stay on Grok Voice Think Fast 1.0, developers must pin `grok-voice-think-fast-1.0` before then.

 This opt-out-to-stay migration design — where inaction means upgrade — is the default-assumption pattern that pushes the industry toward faster deployment of improved voice experiences, but it puts the burden of regression-testing on developers rather than the platform. 

The Grok Voice Agent Builder advertised $0.05 per minute at its July 1 launch, and the default model underneath it moves to Think Fast 2.0, whose raw rate is $0.08 per minute

 — a pricing change that arrives automatically for anyone who has not pinned a version, compounding the transparency question about forced-default migrations.

On the Grok Build CLI side, the releases shipping alongside Think Fast 2.0 address day-to-day agent workflow reliability. 

Grok Build adds streaming JSON headless output with tool calls, results, and usage, plus a new `/undo` slash command to restore files and chat to an earlier turn; it also improves slash command handling, login stability, draft history warnings, settings pickers, and deep-linked settings behavior.

 The `/undo` command is the reversibility primitive that matters most for trust: in an agent that can modify files across a working session, giving users a named, discoverable rollback point is the design signal that the agent's actions are recoverable, not permanent by default. 

MCP servers can also now be enabled or disabled from the CLI with `grok mcp enable` and `grok mcp disable`, with full plan markdown copyable to the clipboard during plan approval or preview.

 The per-server MCP toggle is the least-privilege pattern applied at the tool-access layer — the right governance primitive for an agent that can reach external services.

---

### Perplexity: Enterprise Governance Layer, SCIM Group Sync, and Computer in the Browser

Perplexity's most structurally significant development in this window is the July 27 enterprise governance release that ships the infrastructure layer necessary for large-scale agentic deployment: **custom roles, SCIM group sync, and group credit limits** — the control primitives that move Computer from a capability individual employees adopt to a product IT departments can govern.



Perplexity adds enterprise roles and permissions, custom API credentials, Brain memory in more languages, Claude Opus 5 across Search and Computer, Agent API Skills, Computer in Comet Assistant, Check Sources, a Source Context Panel, and new session management tools; admins can create custom roles with granular permissions, sync groups from an identity provider through SCIM, and set credit usage limits per group — available to Enterprise orgs on an annual sales contract.

 The SCIM integration is the governance primitive that makes role-based access to an agentic platform manageable at enterprise scale: rather than assigning Computer permissions user-by-user, IT teams can define access profiles at the group level and sync them from their existing identity provider, ensuring that the agentic access model mirrors the organisational access model they already govern.

The **Computer in Comet Assistant** addition is the in-browser deployment pattern that closes a meaningful gap: 

Perplexity shipped Comet iOS, Computer updates for individuals and enterprise, multimodal Deep Research, and Health Computer

 in recent weeks, and bringing Computer into the Comet browser's assistant layer means the same agentic execution that was previously desktop-or-app-only is now reachable from within the browsing surface without switching contexts. This mirrors the surface-consolidation thesis playing out across every platform this week: the agentic layer moves into the surface you already inhabit rather than existing as a separate destination.

The **Agent API Skills** extension is the multi-step orchestration primitive that matters most for third-party developers: 

the Perplexity API has been rebuilt as a full-stack agent platform: an Agent API for multi-step workflow orchestration, a Search API for up-to-date information, and skills for integrating with enterprise systems

 — a stack that positions Perplexity's agentic capabilities as infrastructure other products can build on, not only a consumer-facing application. The trust-design implication of this architecture is that the provenance and attribution layer Perplexity has invested in — inline citations, Source Context Panels, Check Sources — becomes the trust guarantee that third-party products inherit when they build on the Agent API, making Perplexity's source-transparency model a de-facto standard for the applications that integrate it.

---

## The Bigger Picture: Surface Consolidations, Ambient Overlay Redesigns, and the Voice Agent Threshold

The 48 hours ending August 3, 2026 mark the moment when the industry's surface consolidation thesis stops being a directional trend and becomes an executed strategy — confirmed simultaneously and independently by every major platform in this window. Google cancelled a standalone app with 800,000 pre-orders rather than maintain a separate surface, and began rolling the full-screen frosted-glass overlay that makes Gemini an ambient backdrop rather than a floating card. OpenAI is six days from closing Atlas, the AI browser whose nine-month macOS-only life confirmed the same lesson: users will not switch browsers to get AI, but they will accept AI arriving inside the surface they already inhabit. Microsoft is completing that same argument at the enterprise layer, moving Copilot from a side-panel option in Classic Outlook to a persistent ribbon-level presence that reads every email thread before the user asks for help. Anthropic is closing the promotional window it built specifically to accelerate the habit of treating a mobile phone as a legitimate delegation surface for long-running agentic work, having spent a month proving that users will start tasks on one device and trust remote cloud sessions to finish them on another. What xAI's Grok Voice Think Fast 2.0 adds to this picture is the voice-agent dimension: the forced-default alias migration on August 5 is the industry's first large-scale test of what happens when a platform upgrades every connected voice agent automatically, shifting the governance burden from opt-in to opt-out — a design choice that accelerates capability deployment but demands a new kind of regression-testing contract between platform and developer. Together, these events describe a single design destination the industry is approaching from five different angles at once: AI not as a mode you switch into, a browser you open, or an app you download, but as the ambient reasoning layer of every surface you already use — and the trust architecture that makes that transition feel governed rather than imposed is the design problem that defines the next quarter of releases.

---

## References

[1] AIToolsReview. (2026). *Claude Cowork Goes Mobile: The Beta, Explained (August 2026)*. [https://aitoolsreview.co.uk/insights/claude-cowork-mobile](https://aitoolsreview.co.uk/insights/claude-cowork-mobile)

[2] DigitalApplied. (2026). *Claude Cowork Goes Web and Mobile: A Team Rollout Guide*. [https://www.digitalapplied.com/blog/claude-cowork-web-mobile-expansion-guide-2026](https://www.digitalapplied.com/blog/claude-cowork-web-mobile-expansion-guide-2026)

[3] Anthropic. (2026). *Claude Cowork on web and mobile: hand off work anywhere*. [https://claude.com/blog/cowork-web-mobile](https://claude.com/blog/cowork-web-mobile)

[4] Digitbin. (2026). *ChatGPT Atlas Shutting Down: What Happens to Your Data*. [https://www.digitbin.com/chatgpt-atlas-shutting-down/](https://www.digitbin.com/chatgpt-atlas-shutting-down/)

[5] OpenAI Help Center. (2026). *Evolving Atlas into ChatGPT for browser-based agentic work*. [https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work)

[6] Releasebot. (2026). *ChatGPT Updates by OpenAI — August 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt)

[7] 9to5Google. (2026). *Gemini will create mobile & desktop apps in the future as AI Studio for Android, iOS is canceled*. [https://9to5google.com/2026/07/31/gemini-ai-studio-app/](https://9to5google.com/2026/07/31/gemini-ai-studio-app/)

[8] AndroidPure. (2026). *Google Cancels AI Studio App After 800,000 Pre-Registrations, Folds It Into Gemini*. [https://www.androidpure.com/google-cancels-ai-studio-app-gemini/](https://www.androidpure.com/google-cancels-ai-studio-app-gemini/)

[9] Android Central. (2026). *Gemini's new blurred UI is finally reaching Android phones*. [https://www.androidcentral.com/apps-software/ai/geminis-new-blurred-ui-is-finally-reaching-android-phones](https://www.androidcentral.com/apps-software/ai/geminis-new-blurred-ui-is-finally-reaching-android-phones)

[10] Windows Latest. (2026). *Microsoft says Classic Outlook's Copilot button is getting bigger and will nudge you with AI suggestions as you work*. [https://www.windowslatest.com/2026/07/30/sorry-outlook-classic-holdouts-you-cant-escape-microsoft-copilot-and-the-button-is-getting-bigger/](https://www.windowslatest.com/2026/07/30/sorry-outlook-classic-holdouts-you-cant-escape-microsoft-copilot-and-the-button-is-getting-bigger/)

[11] Microsoft Learn. (2026). *Release Notes for Microsoft 365 Copilot*. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)

[12] The Register. (2026). *Microsoft makes Copilot harder to miss in Classic Outlook*. [https://www.theregister.com/on-prem/2026/07/30/microsoft-makes-copilot-harder-to-miss-in-classic-outlook/5280997](https://www.theregister.com/on-prem/2026/07/30/microsoft-makes-copilot-harder-to-miss-in-classic-outlook/5280997)

[13] xAI. (2026). *Introducing Grok Voice Think Fast 2.0*. [https://x.ai/news/grok-voice-think-fast-2](https://x.ai/news/grok-voice-think-fast-2)

[14] Releasebot. (2026). *xAI Release Notes — August 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai)

[15] Releasebot. (2026). *Grok Build Updates by xAI — August 2026*. [https://releasebot.io/updates/xai/grok-build](https://releasebot.io/updates/xai/grok-build)

[16] Releasebot. (2026). *Perplexity Release Notes — July 2026*. [https://releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai)

[17] Releases.sh. (2026). *Perplexity Release Notes & Changelog — August 2026*. [https://releases.sh/perplexity](https://releases.sh/perplexity)

[18] FatJoe. (2026). *Perplexity AI Stats July 2026: Uses, Users, Market Share, and More*. [https://fatjoe.com/blog/perplexity-ai-stats/](https://fatjoe.com/blog/perplexity-ai-stats/)