# UX Briefing: Animated Output, Enterprise Agent Governance, and the Guided Learning Lockdown

**November 05, 2026**

Good morning. The 48 hours ending November 5, 2026 are defined by three simultaneous design movements: **ChatGPT Images 2.6** shipping native animated-GIF creation and persistent reference-image libraries to all plans — the first time motion has returned to ChatGPT's generative output surface since Sora's shutdown — alongside **Dots for Enterprise** reaching its admin-preview governance phase with per-role permission controls, data-residency enforcement, and a free preview window closing November 18; a **Gemini Guided Learning** deployment to Google Classroom that inverts the standard AI surface design by deliberately restricting what the AI can do — hiding navigation, disabling new chats, and locking students into a step-by-step coaching mode assigned by the teacher; and a **Grok API text-watermarking** announcement scheduled for November 7 that makes xAI the first North American platform to default-enable invisible statistical provenance signals across its full text-generation stack, while Anthropic's **Claude Duet** proactive agent continues expanding its US research preview waitlist with a trust architecture centred on approval gates before high-stakes actions. **Microsoft Copilot** delivers the November wave of its **Skills-in-Chat** rollout and the **Copilot Home** unification completing worldwide distribution this month, alongside an interactive **Excel canvas** going generally available. **Perplexity Computer** extends its agentic mandate to e-commerce with the launch of a Shopify-to-Meta-to-Klaviyo end-to-end campaign execution workflow and the introduction of **Agent Plugins** that can be imported from GitHub or zip files.

---

## At a Glance: November 5 Highlights

Today's window is defined by the tension between AI surfaces opening up — adding motion, persistent references, and cross-platform execution — and AI surfaces deliberately closing down, with Guided Learning mode, Enterprise Dots governance gates, and watermark provenance signals each representing a designed constraint on what an agent can do without human authorisation.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | **Claude Duet research preview continues expanding its US waitlist: the proactive agent sends a morning brief, monitors connected apps every few hours in its own cloud VM, and requires explicit approval before sending, paying, signing, or deleting; it imports a subscriber's existing memory, skills, and app connections at setup; passwords are never exposed to the model; Anthropic also updates its game-cloning policy to offer an original-genre alternative rather than a blanket block** — the approval-gate architecture is the defining trust-design choice: every high-stakes action surfaces a confirmation step that keeps consequential decisions with the user rather than the agent. [111-4,113-3,113-4,116-9,116-10,119-13,119-14,7-1,7-2] |
| **ChatGPT** | **ChatGPT Images 2.6 ships November 4 to all plans on web, desktop, and mobile: native animated-GIF creation from prompts or existing images with per-frame editing and speed control; a persistent reference-image library stores likenesses of people, pets, and characters for reuse without re-uploading; two new API models launch — GPT-Image-2.6 Flare (images in as little as six seconds) and GPT-Image-2.6 Sunburst (higher quality, edit consistency, SVG export); separately, Dots for Enterprise enters an admin preview until November 18 with per-role access gates, data residency, and Enterprise Key Management** — the GIF surface returns motion to ChatGPT's creative output for the first time since Sora was discontinued, via a workflow-safe looping format rather than a full video pipeline. [65-3,65-14,65-17,66-3,70-13,70-14,70-15,70-16,120-4,120-5,120-8] |
| **Google Gemini** | **Gemini Guided Learning launches globally in Google Classroom on November 3–4: teachers attach a Guided Learning activity to any assignment; when students open it, the Gemini side-navigation panel is automatically hidden, new chats are disabled within the tab, and the student remains locked in the coaching mode; Guided Learning coaches through open-ended questions and step-by-step breakdowns rather than providing direct answers** — this is the most deliberate AI-surface restriction shipped by any major platform in this window: the design explicitly removes capabilities a student would normally have access to in Gemini, in service of a pedagogically defined interaction constraint. [130-2,130-3,130-4,133-3,133-4,135-9] |
| **Microsoft Copilot** | **Skills in Copilot Chat rolling out worldwide in November: users create skills directly in Chat using natural language, discover organisation-shared skills through the Agents & Plugins section, and Copilot surfaces which skills it used while generating a response; the Copilot Home unification (Chat + Cowork + Projects + Workspaces in one navigation) continues worldwide rollout this month; the Excel Interactive Canvas goes generally available worldwide in November with auto-updating on source data changes** — Skills-in-Chat is the most significant Copilot interaction pattern of the month: reusable instruction sets created from plain-language descriptions replace repeated manual prompting and become shareable team assets. [94-5,94-6,100-5,100-8,100-9,100-10,95-7,95-8,95-10] |
| **Grok (xAI)** | **xAI announces that from November 7, 2026, invisible statistical watermarks will be enabled by default on API text outputs across seven Grok models (grok-4.7, 4.6, 4.5, 4.3, and all three grok-4.20 variants); the watermark covers plain text, structured outputs, and tool-call arguments; developers do not need to change any code; team admins can opt out per model through the xAI Console; each response includes an x-watermark header surfacing the feature's status at the API level** — xAI becomes the first North American AI platform to default-enable text provenance signals across its full production API stack, contrasting with OpenAI's phased EU-only product watermarking approach and Anthropic's model-by-model rollout. [85-1,85-3,85-4,87-4,87-5,88-8,90-7,90-8,90-9] |
| **Perplexity** | **Perplexity Computer for e-commerce launches November 3: Computer analyses Shopify product-sales data, builds an on-brand Shopify landing page, and executes the same products and offers into Meta ad campaigns and Klaviyo email campaigns in a single agentic workflow; Agent Plugins launch simultaneously, bundling app integrations and capabilities into importable packages from GitHub or .zip files that are compatible with other agents** — the end-to-end Shopify-to-Meta-to-Klaviyo execution loop is the most complete agentic cross-platform workflow any AI platform has shipped to a vertical segment, compressing what previously required a marketing team plus an agency into a single Computer task. [102-1,102-2,102-4,102-5,103-3,103-4,109-5] |

---

## Product Highlights

### Claude / Anthropic: Claude Duet's Approval-Gate Architecture Defines the Proactive Agent Trust Pattern

Anthropic's most consequential interaction-design development active in this 48-hour window is the continued and expanding rollout of **Claude Duet** — the proactive agent research preview that launched October 21 and has been progressively admitting US Pro, Max, and Ultra waitlist subscribers over the past two weeks. Duet is not covered here because it is new; it is covered because, as it reaches more users, its trust-design architecture is becoming the reference implementation against which every other proactive agent in the ecosystem will be measured.



Claude Duet is a standalone app where Claude works as a proactive agent instead of waiting for a chat to be opened; in Anthropic's words, it "comes to you with what needs your attention, completes tasks you ask of it, keeps working when you step away, and checks with you before it acts on your behalf."

 The interaction pattern this produces is structurally different from reactive chat: 

each morning, Duet sends a short brief on priority items across connected apps, and throughout the day Anthropic says it checks those apps every few hours.

 The critical trust-design constraint is the approval gate: 

Duet asks approval before sending, paying, signing, or deleting.

 This creates a clear and legible boundary between the agent's autonomous monitoring and preparation work (which runs without user intervention) and its consequential actions (which never execute without an explicit user confirmation). The gate is not a limitation on Duet's capability — it is the interaction design that makes the capability safe to extend into background autonomy in the first place.

The technical trust architecture beneath the gate is equally deliberate: 

Duet reads, drafts and prepares work on its own but the agent never directly sees passwords or sign-in tokens; its actions pass through the same auto-mode classifier that guards Claude Code, and its defences against hidden instructions come from Anthropic's browser-agent research.

Setup takes little effort because Duet brings over a subscriber's stored memory, skills and app connections from their Claude account.

 This continuity-of-context design is the correct onboarding pattern for a proactive agent: a system that requires the user to re-establish their context, preferences, and connections from scratch imposes a setup cost high enough to deter the sustained use a background agent requires to deliver value.

Anthropic also shipped a notable policy refinement in this window relevant to Claude Code and the web product. 

Claude will now offer to build an original game in the same genre instead of copying an existing title, following complaints that the restriction blocked legitimate projects — the rise of AI-assisted game cloning and reverse-engineering had led Anthropic to block its tools from carrying out those tasks, but game developers complained that the restriction also prevented them from using Claude for legitimate work.

 This is a principled interaction-design revision: a blanket refusal that blocked legitimate use cases is replaced with a constrained offer that serves the legitimate case while still declining the problematic one, and that communicates the distinction to the user in the moment.

---

### ChatGPT / OpenAI: Images 2.6 Returns Motion to the Creative Surface and Dots Enterprise Governance Lands

OpenAI's dominant interaction-design story in this window is the double release of **ChatGPT Images 2.6** and the **Dots for Enterprise** admin preview — two advances on opposite ends of the creative-to-autonomous spectrum that together illustrate the breadth of the interaction-design surface OpenAI is now managing simultaneously.



ChatGPT Images 2.6 is OpenAI's November 4 image update: 50% faster generation, animated GIFs, saved reference images, and two new API models.

 The GIF feature is the most significant new interaction primitive: 

in ChatGPT users can turn a prompt or an image into an animated GIF, adjust its speed and edit individual frames.

Eight months after OpenAI shut down its video app, the company is bringing motion back to ChatGPT another way — with the new image model, ChatGPT Images 2.6, users can turn a prompt or a photo into an animated GIF, edit it frame by frame and share it on a loop.

 The reference-image library is the second major interaction advance: 

users can keep reference images of themselves, pets, and characters ready to reuse in new creations — no need to upload them again.

 This shifts image generation from a stateless per-session activity to a persistent creative workflow where the user's established visual vocabulary (characters, brand assets, faces) is a durable resource rather than a file to re-upload each session. On the developer side, 

two new API models launched: GPT-Image-2.6 Flare generates images in as little as six seconds, while GPT-Image-2.6 Sunburst targets higher quality, edit consistency and SVG export.



The Dots for Enterprise admin preview, which became active November 4, is the governance-layer story of the window. 

Personal Dots can continue working on tasks between conversations; they are generally available to eligible ChatGPT Enterprise, Edu, and Healthcare workspaces, with an admin preview until November 18, 2026, during which workspace owners and admins can enable access or opt out before Dots become available by default.

 The admin control surface is granular: 

owners and admins can control which members can use Dots, view personal Dots and their connections, pause or resume them, and review usage and admin activity; workspace owners can also delete personal Dots.

 Three specific capabilities ship off by default for Enterprise: 

the ability for a Dot to join supported Slack or Microsoft Teams workspaces and post with its own identity, and the ability for members to add or edit custom rules that guide their Dot's actions and confirmations.

 The critical governance gap that Enterprise administrators should note: 

Enterprise model controls and default model settings do not apply to Dots

 — meaning the model-governance policies an organisation has established for standard ChatGPT use do not automatically extend to Dot-powered background agents, requiring a separate governance review before the November 18 default-on date.

---

### Google Gemini: Guided Learning's Deliberate Restriction Is the Most Interesting AI Surface Design of the Window

Google's most interaction-design-significant release in this 48-hour window is not an expansion of AI capability but its deliberate limitation: **Gemini Guided Learning in Google Classroom**, which rolled out globally beginning November 3–4 and represents a surface design philosophy the AI industry has rarely applied — the intentional removal of features the user would otherwise have access to, in service of a defined interaction goal.



A new Google Classroom integration lets teachers add Guided Learning to any assignment, now rolling out globally in all Gemini-supported languages; Guided Learning is a mode in the Gemini app designed to help students deepen their understanding with step-by-step guidance, rather than giving the answer.

 The UX constraints Google ships with this feature are the design story: 

when students open the assigned Guided Learning from Classroom, the Gemini side-navigation panel is automatically hidden, new chats are disabled within the tab, and they remain in Guided Learning mode.

Google Classroom Guided Learning disables new chats and hides Gemini's side navigation within an assigned activity.

 This is the inverse of every other AI-surface design decision in this briefing window: where every other platform is adding capability, expanding context, and removing friction, Guided Learning deliberately removes capability — the ability to open a new chat, to access Gemini's navigation, to escape the tutoring mode — to enforce an interaction pattern that the teacher has designed.



Google is introducing Guided Learning to Google Search and Google Classroom to support active student problem solving; Guided Learning coaches students through complex topics with step-by-step prompts instead of providing direct final answers.

 The governance model is clean: 

school administrators have full control to decide which AI tools are available to their students, ensuring technology supports classroom learning.

 The teacher-assigns, administrator-enables, student-receives chain is the correct trust architecture for an educational AI surface: the student interacts with a constrained agent whose constraint parameters were set by accountable adults above them in the authority hierarchy, rather than by the AI platform itself.

---

### Microsoft Copilot: Skills in Chat Complete the Reusable-Instruction Loop Across the Copilot Surface

Microsoft's most significant interaction-design advance reaching users in this window is the November worldwide rollout of **Skills in Copilot Chat** — a feature that converts the act of typing a recurring prompt into an organisational asset, and that closes the gap between the Cowork and Chat surfaces by making the same skill callable from either entry point.



Skills help turn know-how into reusable capabilities that Copilot can apply automatically, enabling faster execution, more consistent results, and easier knowledge sharing across teams; Skills are expanding from availability in Cowork to Copilot Chat, bringing reusable expertise directly into the flow of everyday work.

 The creation model is the critical interaction-design detail: 

a skill is a reusable set of instructions, so if you find yourself typing the same prompt every week, you can save it once and share it with your team, and you can create one just by describing it in plain English.

 This natural-language skill creation eliminates the prompt-engineering overhead that has historically made reusable instruction sets a power-user feature: a user who cannot write a formal prompt template can still author a skill by describing what they want in conversational terms. The discoverability mechanism is equally important: 

a skill is a reusable set of instructions for a job, such as preparing a weekly summary in your team's format; Microsoft says Chat will show the Skills it used while generating a response.

 The in-line attribution — Copilot surfacing which Skill drove a given output — is an audit-trail primitive that makes the agent's instruction source legible to the user at the moment of use, not only in a settings panel.



The Copilot app's Home screen now puts Chat and Cowork side by side — Chat for quick questions, ideas and first drafts; Cowork when you want to hand over a bigger, multi-step task; Plugins are where users will find agents, skills, and connectors, while Automations let Cowork tasks run on a schedule or when something happens.

 The Excel Interactive Canvas, also reaching worldwide rollout this month, extends the natural-language interaction pattern into data visualisation: 

the Interactive Canvas in Excel uses Copilot to turn workbook data into a polished report of key visualisations, metrics, and insights; the canvas updates automatically as the underlying data changes, and users can change it by chatting with Copilot; teams get a current, shareable view of their data without building reports by hand; the feature rolled out to Insiders in October and rolls out worldwide in November.



---

### Grok (xAI): Default Text Watermarking from November 7 Makes xAI the North American Provenance Trailhead

xAI's most consequential interaction-design and trust-design development in this window is not a UI change but a provenance primitive: the **default text watermarking** of Grok API outputs, announced to take effect November 7, 2026 — two days from today's briefing date — across seven production Grok models.



xAI will begin automatically applying invisible watermarks to the text outputs of seven Grok models via API starting November 7; this applies to both global and regional endpoints.

 The scope is broader than image-only provenance signals: 

watermarking applies to ordinary text, structured outputs and generated tool-call arguments through both the Responses API and Chat Completions API.

 The seven models covered are: 

grok-4.7, 4.6, 4.5, 4.3, and all three versions of grok-4.20 — reasoning, non-reasoning, and multi-agent.

 The developer experience design is zero-disruption: 

starting November 7, xAI will switch on invisible statistical watermarking across its Grok API models by default; developers will not need to flip a setting — it simply arrives.

 The governance model balances default-on accountability with operator control: 

crucially, xAI is keeping developers in control — teams can opt out on a per-model basis, and every response includes an x-watermark header that makes the feature's status transparent at the API level.



The comparative market position is the design story that most matters for the industry: 

xAI has chosen to enable watermarks globally by default via API; Anthropic is rolling out watermarks for new models globally, while OpenAI is implementing a phased enablement for products in the EU with global API watermarks disabled by default.

 This means the x-watermark header arriving in every Grok API response from Saturday becomes an observable trust signal that application builders can consume — creating, for the first time, a mechanism by which a downstream system can verify that text it received originated from a watermark-covered Grok model. 

From November 7, 2026, every text response generated by one of the seven Grok models in the documentation carries an invisible watermark, and developers don't have to change a line of code.

 The opt-out-per-model design is the correct governance granularity: an operator building a consumer-facing product that publishes Grok-generated content and an operator building an internal tool that never surfaces model outputs externally have meaningfully different provenance requirements, and a per-model opt-out lets them express that distinction without blanket disabling.

---

### Perplexity: Computer for E-Commerce Closes the Shopify-to-Campaign Loop and Agent Plugins Open the Extension Layer

Perplexity's most consequential agentic-workflow advance in this 48-hour window is the launch of **Computer for e-commerce** — announced November 3 — which extends the platform's autonomous task-execution model into a specific vertical workflow that runs from sales-data analysis through content creation to paid-media execution, without the user having to leave the Computer interface.



Perplexity announced new e-commerce workflows for its Computer digital worker on November 3, 2026, connecting Shopify sales analysis and landing pages with Meta advertising and Klaviyo email campaigns; Computer examines product sales to recommend items or collections, builds an on-brand Shopify page, then uses the same products and offers in Meta ads and Klaviyo emails.

 The approval-gate design is embedded at the highest-stakes step: 

Computer builds the page for selected products, a collection or a launch, and staff can make final edits directly in the Shopify editor before publication.

 This is the correct human-in-the-loop point for a commerce workflow — the moment before a page goes live and before ad spend is committed — rather than a blanket confirmation of every intermediate step that would defeat the value of automation. 

On the same day, Perplexity highlighted that Computer can directly run Meta ads, manage Klaviyo email campaigns, and control Shopify stores; Aravind Srinivas noted that many Shopify merchants are already using Computer to automate competitor analysis, audits, store setup, marketing campaigns, and Instagram ad placements.



The simultaneous launch of **Agent Plugins** is the developer-layer story that determines whether the e-commerce workflow is an isolated vertical feature or the first template in an extensible ecosystem: 

on November 3, Perplexity announced that its agent product Computer now supports Agent Plugins; plugins bundle app integrations and capabilities together, allowing users to browse existing plugins or import their own from GitHub or .zip files, and plugins are compatible with other agents.

 The GitHub and zip-import mechanism is a low-friction extension primitive that positions Computer's plugin layer as a permeable boundary — any developer with an existing integration can package it as an Agent Plugin and make it callable from Computer's orchestration layer, without waiting for Perplexity to build or certify the integration itself. 

In October, Perplexity had also open-sourced SPACE, the sandbox platform behind Computer, to help developers build safer autonomous AI agents

 — the agent plugin launch is the downstream consequence of that infrastructure decision, turning the open-sourced sandbox into a foundation that third-party plugin authors can build on with confidence about the security model.

---

## The Bigger Picture: Animated Output, Enterprise Agent Governance, and the Guided Learning Lockdown

The 48 hours ending November 5, 2026 reveal a design split that has been building for months but is now sharp enough to name: the AI industry is simultaneously pursuing **surface expansion** and **surface restriction** as complementary rather than contradictory design strategies, and the platforms that understand both are pulling ahead in the trust-design dimension that will ultimately determine enterprise and institutional adoption. ChatGPT Images 2.6's animated GIFs and persistent reference libraries expand the creative surface; Gemini Guided Learning's forced navigation lockdown and chat-disabling deliberately contract it — and both are correct for their respective interaction contexts. Claude Duet's approval gates before high-stakes actions, xAI's opt-out-able default watermarking, and Dots for Enterprise's pre-November-18 governance window represent the same insight from three different angles: autonomous agent capability is only socially sustainable when it is paired with a legible, accessible, and timely mechanism by which the humans who initiated it can inspect, constrain, or revoke what it is doing. The industry arrived at Guided Learning's constraint model and Duet's approval gate by different routes — one from an educational trust requirement, the other from consumer agent safety research — but both converge on the same design conclusion: the value of an AI surface is not determined solely by what it can do, but by the precision with which the humans deploying it can define what it should and should not do in a specific context. The governance gap that remains — across Dots for Enterprise (where model controls do not apply to Dots), across xAI's watermarking (where only API-level admins can opt out), and across Perplexity's e-commerce Computer (where the approval gate is at publication, not at ad-spend commitment) — is the same gap in each case: the boundary between agent capability and human authorisation is drawn at a platform-default level that may not align with the specific governance requirements of a given operator, enterprise, or regulated context. The platforms that solve for configurable, context-specific authority delegation — not just default-on or default-off — will define the next phase of agent interface design.

---

## References

[1] aiweekly.co. (2026). *Anthropic News Today, November 5*. [https://aiweekly.co/ai-news-today/anthropic-news](https://aiweekly.co/ai-news-today/anthropic-news)

[2] mezha.net. (2026). *Anthropic updates Claude's rule on copying games*. [https://mezha.net/eng/news/mezha-4dbe1cd1ad8f0f67640d502d_anthropic_updates_claude-s](https://mezha.net/eng/news/mezha-4dbe1cd1ad8f0f67640d502d_anthropic_updates_claude-s)

[3] betanews.com. (2026). *Claude Duet: Anthropic opens proactive AI agent preview*. [https://betanews.com/article/proactive-ai-agent-claude-duet/](https://betanews.com/article/proactive-ai-agent-claude-duet/)

[4] pasqualepillitteri.it. (2026). *Claude Duet launches as Anthropic's agent that messages you first*. [https://pasqualepillitteri.it/en/news/26185/claude-duet-anthropic-proactive-agent-en](https://pasqualepillitteri.it/en/news/26185/claude-duet-anthropic-proactive-agent-en)

[5] cellcog.ai. (2026). *Claude Duet: Anthropic's Proactive Agent, Explained*. [https://cellcog.ai/blog/claude-duet/](https://cellcog.ai/blog/claude-duet/)

[6] aitoolsreview.co.uk. (2026). *Claude Duet: Anthropic's Proactive Agent, Explained (October 2026)*. [https://aitoolsreview.co.uk/insights/claude-duet-proactive-agent](https://aitoolsreview.co.uk/insights/claude-duet-proactive-agent)

[7] technology.org. (2026). *Anthropic Launches Claude Duet Proactive AI Agent*. [https://www.technology.org/2026/10/22/anthropic-claude-duet-proactive-ai-agent-research-preview/](https://www.technology.org/2026/10/22/anthropic-claude-duet-proactive-ai-agent-research-preview/)

[8] techmymoney.com. (2026). *Claude Duet research preview opens for US Pro, Max, and Ultra*. [https://techmymoney.com/2026/11/01/anthropic-claude-duet-research-preview/](https://techmymoney.com/2026/11/01/anthropic-claude-duet-research-preview/)

[9] aiweekly.co. (2026). *OpenAI Ships ChatGPT Images 2.6 With GIFs and Faster API Models*. [https://aiweekly.co/alerts/openai-ships-chatgpt-images-26-with-gifs-and-faster-api-models](https://aiweekly.co/alerts/openai-ships-chatgpt-images-26-with-gifs-and-faster-api-models)

[10] eesel.ai. (2026). *ChatGPT Images 2.6: GIFs, API models, and real per-image cost*. [https://www.eesel.ai/blog/chatgpt-images-2-6](https://www.eesel.ai/blog/chatgpt-images-2-6)

[11] trendingtopics.eu. (2026). *ChatGPT Images 2.6: OpenAI Adds GIFs*. [https://www.trendingtopics.eu/chatgpt-images-2-6-gifs-en/](https://www.trendingtopics.eu/chatgpt-images-2-6-gifs-en/)

[12] x.com/OpenAI. (2026). *OpenAI on X: "Images, upgraded—introducing ChatGPT Images 2.6"*. [https://x.com/OpenAI/status/2118124944928432327](https://x.com/OpenAI/status/2118124944928432327)

[13] help.openai.com. (2026). *ChatGPT Enterprise and Edu release notes — November 4, 2026*. [https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)

[14] help.openai.com. (2026). *Getting started with your dot*. [https://help.openai.com/en/articles/20001530-getting-started-with-your-dot](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)

[15] help.openai.com. (2026). *Manage dots in ChatGPT workspaces*. [https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces](https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces)

[16] workspaceupdates.googleblog.com. (2026). *Educators can now add Guided Learning to assignments in Google Classroom to help students get extra support*. [https://workspaceupdates.googleblog.com/2026/11/educators-can-now-add-guided-learning-to-assignments-in-Google-Classroom-to-help-students-get-extra-support.html](https://workspaceupdates.googleblog.com/2026/11/educators-can-now-add-guided-learning-to-assignments-in-Google-Classroom-to-help-students-get-extra-support.html)

[17] blog.google. (2026). *Responsible AI for schools with Guided Learning*. [https://blog.google/products-and-platforms/products/education/ai-learning-era-updates-2026/](https://blog.google/products-and-platforms/products/education/ai-learning-era-updates-2026/)

[18] datastudios.org. (2026). *Google turns off Gemini and Search by default for K-12 student accounts, Guided Learning arrives*. [https://www.datastudios.org/post/google-gemini-search-off-by-default-k-12-student-accounts-guided-learning](https://www.datastudios.org/post/google-gemini-search-off-by-default-k-12-student-accounts-guided-learning)

[19] techjournal.org. (2026). *Google Classroom Guided Learning: What Changes*. [https://techjournal.org/google-classroom-guided-learning](https://techjournal.org/google-classroom-guided-learning)

[20] changingsocial.com. (2026). *What's new in Microsoft Copilot — November 2026*. [https://www.changingsocial.com/blog/whats-new-in-microsoft-copilot-november-2026/](https://www.changingsocial.com/blog/whats-new-in-microsoft-copilot-november-2026/)

[21] techcommunity.microsoft.com. (2026). *What's New in Microsoft Copilot — October 2026*. [https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528)

[22] m365admin.handsontek.net. (2026). *Microsoft 365 Copilot: Skills in Copilot Chat*. [https://m365admin.handsontek.net/microsoft-365-copilot-skills-copilot-chat/](https://m365admin.handsontek.net/microsoft-365-copilot-skills-copilot-chat/)

[23] elevenforum.com. (2026). *What is New in Microsoft Copilot for October 2026*. [https://www.elevenforum.com/t/what-is-new-in-microsoft-copilot-for-october-2026.50496/](https://www.elevenforum.com/t/what-is-new-in-microsoft-copilot-for-october-2026.50496/)

[24] pasqualepillitteri.it. (2026). *Grok watermark arrives on xAI API text on November 7*. [https://pasqualepillitteri.it/en/news/29128/grok-watermark-xai-api-text-november-7](https://pasqualepillitteri.it/en/news/29128/grok-watermark-xai-api-text-november-7)

[25] kucoin.com. (2026). *xAI to Add Default Text Watermarks to Grok API Amid EU Regulatory Pressure*. [https://www.kucoin.com/news/flash/xai-to-add-default-text-watermarks-to-grok-api-amid-eu-regulatory-pressure](https://www.kucoin.com/news/flash/xai-to-add-default-text-watermarks-to-grok-api-amid-eu-regulatory-pressure)

[26] cryptobriefing.com. (2026). *xAI adds invisible text watermarking to Grok API models*. [https://cryptobriefing.com/xai-grok-text-watermarking-api/](https://cryptobriefing.com/xai-grok-text-watermarking-api/)

[27] allthings-elon.com. (2026). *xAI Adds Invisible Watermark to Grok API Text Output*. [https://www.allthings-elon.com/articles/xai-grok-api-invisible-watermark-text-output-2026-11-03](https://www.allthings-elon.com/articles/xai-grok-api-invisible-watermark-text-output-2026-11-03)

[28] superpowerdaily.com. (2026). *xAI will watermark Grok API text by default starting November 7*. [https://superpowerdaily.com/posts/xai-will-watermark-grok-api-text-by-default-starting-november-7](https://superpowerdaily.com/posts/xai-will-watermark-grok-api-text-by-default-starting-november-7)

[29] unite.ai. (2026). *Perplexity Computer Links Shopify Sales to Meta and Klaviyo Campaigns*. [https://www.unite.ai/perplexity-computer-links-shopify-sales-to-meta-and-klaviyo-campaigns/](https://www.unite.ai/perplexity-computer-links-shopify-sales-to-meta-and-klaviyo-campaigns/)

[30] kucoin.com. (2026). *Perplexity: Computer now supports Agent Plugins and expands e-commerce automation*. [https://www.kucoin.com/news/insight/META/6aeb281abbcb52000745cb4f](https://www.kucoin.com/news/insight/META/6aeb281abbcb52000745cb4f)

[31] perplexity.ai. (2026). *Computer for e-commerce is built for brand growth*. [https://www.perplexity.ai/hub/blog/category/news](https://www.perplexity.ai/hub/blog/category/news)