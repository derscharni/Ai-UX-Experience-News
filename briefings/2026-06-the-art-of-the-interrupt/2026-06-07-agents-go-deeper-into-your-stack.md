# UX Briefing: Agents Go Deeper Into Your Stack

**June 07, 2026**

Good morning. Today's briefing is defined by a single directional force: AI agents are no longer living at the edge of your workflow — they are burrowing into its infrastructure. Perplexity is rethinking where computation itself happens with a hybrid local-cloud task router; Google is shipping generative UI that builds interactive interfaces on-the-fly; Microsoft rewired its Copilot prompt box into a task-aware workspace; and Claude Code is hardening its cross-session security model as multi-agent orchestration becomes the default. The era of the chatbot sidebar is over. The agentic core is moving in.

---

## At a Glance: June 7 Highlights

Across the board, this week's releases reveal a maturation from agents that *assist* users to agents that *operate systems* — with all the trust, permission, and control design challenges that entails.

| Product | Key UX Developments |
| :--- | :--- |
| **Claude** | Claude Code introduces hardened cross-session messaging security and a new `ultracode` effort mode, while Managed Agents gain self-hosted sandbox support so enterprises can run tool execution on their own infrastructure. [1][2] |
| **ChatGPT** | OpenAI ships a revamped memory system called "Dreaming" that automatically updates stale context over time, alongside a new Trusted Contact safety feature for personal accounts. [3][4] |
| **Google Gemini** | Two new experimental Labs features — **Visual Layout** and **Dynamic View** — generate fully interactive, custom-coded UI on the fly in response to a user's prompt, while **Gemini Spark** debuts as a 24/7 background agentic layer. [5][6] |
| **Microsoft Copilot** | Microsoft redesigns the Copilot prompt line from a static text box into a task-aware workspace with progressive disclosure, while GitHub Copilot CLI gains a built-in **Rubber Duck** critic agent and local voice input. [7][8] |
| **Grok (xAI)** | xAI launches **Grok Connectors** for Grok Web, enabling direct integrations with SharePoint, Outlook, Google Workspace, Notion, GitHub, and custom MCP servers, alongside Grok Build's worktree support for multi-agent coding. [9][10] |
| **Perplexity** | Perplexity announces **Hybrid Agentic Reasoning** for Personal Computer, a system that automatically routes task components between on-device local models and cloud frontier models — with sensitive data never leaving the device. [11][12] |

---

## Product Highlights

### Perplexity: The Trust Architecture of Hybrid Inference

The most structurally significant UX announcement of the week is Perplexity's forthcoming **Hybrid Agentic Reasoning** system for Personal Computer. 

Perplexity announced a hybrid reasoning system for its AI agent "Personal Computer" that automatically distributes tasks between local devices and the cloud, set to launch in July — processing sensitive data such as financial records and medical information using small models on-device, while routing complex workloads to high-performance cloud models, with users not needing to choose in advance.



The UX implication is profound. This is the first major AI agent product to make *data locality* a first-class, automatic UX concern — rather than a buried settings toggle. 

The new hybrid inference orchestrator gives the system itself the ability to reason about where each piece of a task should execute — not just which model to use, but which physical location should process it — and the system reportedly asks for user permission before sending sensitive tasks to the cloud.

 This shifts the UX trust model from "trust that the cloud is secure" to "your device is the vault, the cloud is the engine." The permission-before-cloud-send pattern is a new interaction primitive for agentic UX that the industry will likely have to adopt broadly. 

According to Perplexity, most real-world tasks involve a mix of both elements, so Personal Computer breaks tasks down into granular components and routes each part to the appropriate execution environment.



---

### Google Gemini: Generative UI as a Native Response Format

Google's most consequential interface move this week is the introduction of **Visual Layout** and **Dynamic View** as experimental Labs features in the Gemini app. 

The two new experimental Labs features are powered by Gemini 3, with Visual Layout using multimodal capabilities to move beyond text, generating a visually immersive response with photos and interactive modules that solicit user feedback and help further customize Gemini's response across multiple turns.

Dynamic View takes this a step further using agentic coding capabilities, with Gemini designing and coding a unique experience with a user interface that's perfect for each specific prompt.



This establishes a new pattern for what a "response" can mean: not a block of text, but a purpose-built, interactive application generated in real time. The UX implication is a move from static output consumption to dynamic output *exploration*. 

By creating dynamic, interactive interfaces on the fly, Gemini can help users explore information in a way that is more intuitive and tailored to specific needs, with user feedback on these experiments helping shape the future of generative UI.



Running in parallel, **Gemini Spark** pushes the proactive agent model further. 

Google describes Gemini Spark as a 24/7 personal AI agent that helps users navigate their digital life, transforming Gemini from an assistant into an active partner that does real work on their behalf — and since it's a cloud-based agent, Spark keeps working in the background even when the user locks their phone.

 The combination of a generative-UI response layer (Dynamic View) and a persistent background agent (Spark) signals Google's intent to control both the *output surface* and the *execution layer* of the user's digital life.

---

### Microsoft Copilot: The Prompt Box Becomes a Workspace

Microsoft's most important UX change this week is a rethinking of the fundamental input metaphor. 

The new designs shift Copilot toward a more connected, adaptive system by turning a once static text box — the prompt line — into a task-aware workspace, with the prompt line now giving users more space within the Copilot app.

Among the most significant new features is progressive disclosure: Copilot displays tools and options contextually with the prompt, avoiding cognitive overload, making the experience smoother on both desktop and mobile devices.

 This shifts the UX from a blank box demanding user initiative to an adaptive surface that *surfaces relevant controls* based on what the user is trying to do — a meaningful reduction in the expertise gap between power users and new ones.

On the developer side, GitHub Copilot CLI is introducing an equally interesting trust and multi-agent pattern. 

Rubber Duck is a built-in CLI agent that acts as a constructive critic: while working on a task, the main CLI agent can pass its current plan, design, implementation, or tests over to the rubber duck agent for review, which looks for blind spots, design flaws, and substantive issues and reports back with concrete, actionable feedback — which Copilot then takes into account before continuing.

 This is a notable agent-to-agent UX pattern: a second, adversarial subagent is baked into the workflow as a quality gate, making AI self-critique visible and legible to the user. 

Copilot CLI also now includes hands-free dictation — hold the space bar and talk to input a prompt — with voice input running locally so all audio stays on the user's machine.



---

### Claude: Security-First Agentic Architecture

Anthropic's week has been defined by hardening the security surface of multi-agent workflows. 

Claude Code adds fallback models, broader deny-rule glob support, stronger cross-session message security, and more reliable thinking controls, while also improving retries, update messaging, agent filtering, and fixing a wide range of terminal, auth, session, and UI bugs.

 The cross-session security hardening is particularly noteworthy for agentic UX: 

messages relayed via SendMessage from other Claude sessions no longer carry user authority — receivers refuse relayed permission requests, and auto mode blocks them.

 This closes a meaningful trust-escalation attack surface that becomes dangerous as multi-agent orchestrations grow more complex.

On the enterprise control side, 

Claude Managed Agents can now operate in a sandbox the enterprise controls and connect to private MCP servers, so both the environment where an agent executes tools and the services it reaches run within the established boundaries of the enterprise.

 For enterprise UX, this is the difference between "the agent can theoretically do anything" and "the agent operates within a perimeter you can audit." 

With Claude Managed Agents, operators can now update the agent's MCP server and tool configurations associated with an active session, and large tool outputs exceeding 100K tokens are automatically spilled to a file in the sandbox, with the model receiving a truncated preview and the file path to read the full content from.



---

## The Bigger Picture: Agents Go Deeper Into Your Stack

This week's releases collectively describe the same architectural shift: AI agents are no longer optional companions perched on top of existing tools — they are becoming the connective tissue running *through* them. Perplexity routes task components between your device and the cloud automatically. Google's Dynamic View turns Gemini into an application factory. Microsoft's progressive disclosure prompt reinvents the input box. Grok wires directly into Outlook, SharePoint, and GitHub without requiring copy-paste. And Anthropic hardens the security boundaries between agents that increasingly orchestrate other agents. The shared UX challenge that emerges from all of this is the same: as agents operate deeper and more autonomously, the interface design work shifts from "how do users prompt the agent?" to "how do users maintain meaningful oversight of what the agent is doing, and where?" Permission-before-cloud-send, rubber duck critics, cross-session authority limits, and self-hosted sandboxes are all answers to that same question — and the industry is only beginning to develop the vocabulary.

---

## References

[1] Releasebot. (2026). *Claude Code Updates by Anthropic — June 2026*. [https://releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[2] Anthropic Claude Platform Docs. (2026). *Claude Platform Release Notes*. [https://platform.claude.com/docs/en/release-notes/overview](https://platform.claude.com/docs/en/release-notes/overview) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[3] OpenAI Research. (2026, June 4). *Dreaming: Better memory for a more helpful ChatGPT*. [https://openai.com/research/index/release/](https://openai.com/research/index/release/) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[4] Releasebot. (2026). *ChatGPT Updates by OpenAI — June 2026*. [https://releasebot.io/updates/openai/chatgpt](https://releasebot.io/updates/openai/chatgpt) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[5] Gemini Apps Release Notes. (2026). *Visual Layout and Dynamic View*. [https://gemini.google/release-notes/](https://gemini.google/release-notes/) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[6] TechCrunch. (2026, May 19). *Google updates its Gemini app to take on ChatGPT and Claude at IO 2026*. [https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/](https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[7] Microsoft 365 Blog. (2026, May 28). *Introducing a new design for Microsoft 365 Copilot*. [https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/](https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[8] GitHub Changelog. (2026, June 2). *Copilot CLI: Improved UI, rubber duck, prompt scheduling, and voice input*. [https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input/](https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input/) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[9] xAI Release Notes. (2026). *xAI Latest Updates — June 2026*. [https://releasebot.io/updates/xai](https://releasebot.io/updates/xai) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[10] xAI Grok Build Changelog. (2026). *Grok Build Changelog*. [https://x.ai/build/changelog](https://x.ai/build/changelog) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[11] BigGo Finance. (2026, June 2). *Perplexity Unveils Feature That Automatically Distributes AI Processing Between Devices and Cloud*. [https://finance.biggo.com/news/N7OWjJ4B-PfaobXfmrrz](https://finance.biggo.com/news/N7OWjJ4B-PfaobXfmrrz) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->

[12] VentureBeat. (2026). *Perplexity AI unveils hybrid local-cloud inference system at Computex 2026*. [https://venturebeat.com/technology/perplexity-ai-unveils-hybrid-local-cloud-inference-system-at-computex-2026](https://venturebeat.com/technology/perplexity-ai-unveils-hybrid-local-cloud-inference-system-at-computex-2026) <!-- verified: 2026-06-14 | status: ✅ accessible & matches | checker: source-verification-agent -->
