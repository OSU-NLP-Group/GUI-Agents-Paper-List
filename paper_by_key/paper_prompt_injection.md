# Papers with Keyword: prompt injection

- [Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System](https://arxiv.org/abs/2602.10915)
    - Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, Zhuotao Liu
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [agent security], [prompt injection], [access control], [intent-centric OS], [MobileSafetyBench], [Aura]
    - 📖 TLDR: This paper analyzes security failures in mobile GUI agents and proposes Aura, an intent-centric runtime architecture that replaces GUI scraping with structured interaction mediated by identity, semantic firewalls, taint-aware memory, and access control. It reports strong task performance while greatly reducing attack success on MobileSafetyBench.

- [WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents](https://arxiv.org/abs/2602.03792)
    - Xilong Wang, Yinuo Liu, Zhun Wang, Dawn Song, Neil Gong
    - 🏛️ Institutions: Duke University, UC Berkeley
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [defense], [prompt injection], [WebSentinel], [security], [attack detection]
    - 📖 TLDR: WebSentinel is a two-step defense framework that detects and localizes prompt injection attacks in webpages by first extracting segments of interest that may be contaminated and then evaluating each segment's consistency with the webpage content, substantially outperforming baseline methods on multiple datasets.

- [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)
    - Hanna Foerster, Tom Blanchard, Kristina Nikolić, Ilia Shumailov, Cheng Zhang, Robert Mullins, Nicolas Papernot, Florian Tramèr, Yiren Zhao
    - 🏛️ Institutions: University of Cambridge, University of Toronto, Vector Institute, ETH Zurich, AI Sequrity Company
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [Single-Shot Planning], [Branch Steering], [OSWorld], [CaMeLs]
    - 📖 TLDR: This paper adapts the Dual-LLM security paradigm to computer-use agents through Single-Shot Planning, where a trusted planner writes a full branching execution graph before seeing untrusted UI content. That gives control-flow integrity against injected instructions, but the paper also identifies Branch Steering as a remaining data-flow threat and studies its tradeoff with utility on OSWorld.

- [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](https://arxiv.org/abs/2512.23128)
    - Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H.S. Torr, Adam Mahdi, Adel Bibi
    - 🏛️ Institutions: University of Oxford, SoftServe, Independent, Johannes Kepler University Linz
    - 📅 Date: December 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [social engineering], [TRAP]
    - 📖 TLDR: TRAP studies persuasion-style prompt injection on realistic cloned websites, varying factors such as injection interface, persuasion principle, placement, and tailoring. Across six frontier models, it finds web agents are redirected in 25% of tasks on average, and small interface or contextual changes often double attack success.

- [Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming](https://arxiv.org/abs/2510.18314)
    - Zheng Zhang, Jiarui He, Yuchen Cai, Deheng Ye, Peilin Zhao, Ruili Feng, Hao Wang
    - 🏛️ Institutions: HKUST(GZ), Tencent, Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: October 21, 2025
    - 📑 Publisher: ICME 2026
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [attack], [prompt injection], [genetic algorithm], [red-teaming], [Genesis]
    - 📖 TLDR: Genesis studies automated red-teaming for web agents by evolving attack strategies over repeated interactions instead of relying on fixed prompts or manually designed attacks. Its attacker-scorer-strategist loop builds and reuses a growing strategy library, yielding stronger adversarial injections across web tasks.

- [In-Browser LLM-Guided Fuzzing for Real-Time Prompt Injection Testing in Agentic AI Browsers](https://arxiv.org/abs/2510.13543)
    - Avihay Cohen
    - 🏛️ Institutions: BrowserTotal
    - 📅 Date: October 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [prompt injection], [in-browser fuzzing], [feedback-guided fuzzing], [progressive evasion], [page summarization], [question answering]
    - 📖 TLDR: This paper studies prompt-injection testing for agentic AI browsers with an LLM-guided fuzzing loop that runs inside a real browser and mutates malicious pages using immediate attack feedback. It reports that simple attacks are usually blocked, but adaptive mutations drive failure rates to 58-74% by the tenth iteration, with page summarization and question-answering features showing the highest risk.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: May 16, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Web]
    - 🔑 Key: [security], [prompt injection], [pixel perturbation], [screenshot attack], [neural rendering approximation], [WebInject]
    - 📖 TLDR: WebInject attacks screenshot-based web agents by perturbing the raw pixels of a rendered webpage so the resulting screenshot steers the agent toward an attacker-chosen action. To optimize that attack despite the non-differentiable render-to-screenshot pipeline, it learns a neural approximation of the mapping and then applies projected gradient descent.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Aaron Grattafiori, Chuan Guo, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [prompt injection], [security-by-incompetence], [WASP]
    - 📖 TLDR: WASP is a benchmark for end-to-end web-agent security under realistic multi-step prompt injection attacks rather than simplified single-step tests. It shows that strong agents can be partially deceived at very high rates by low-effort human-written injections, while also exposing a security-by-incompetence pattern where unsafe agents often fail to fully realize the attacker goal.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, The University of Texas at Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [Android emulator], [MobileSafetyBench]
    - 📖 TLDR: Introduces MobileSafetyBench, a benchmark for measuring safety failures of mobile-control agents in realistic Android tasks involving apps like messaging and banking. It evaluates both ordinary safety behavior and robustness to indirect prompt injection, and shows that current agents still struggle to avoid harmful actions.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: OSU, Amazon, UIUC, University of Chicago, Johns Hopkins University, University of Virginia
    - 📅 Date: September 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [EIA]
    - 📖 TLDR: EIA studies privacy leakage in generalist web agents under adversarial webpages and introduces Environmental Injection Attack, which hides malicious content in the environment to steal user information. Using 177 action steps built from realistic Mind2Web scenarios, the paper reports up to 70% attack success for stealing specific PII and 16% for stealing a full user request at a step, while also arguing that well-adapted attacks are difficult to detect or mitigate.
