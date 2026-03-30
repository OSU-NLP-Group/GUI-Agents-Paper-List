# Papers with Keyword: security

- [AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents](https://arxiv.org/abs/2603.23007)
    - Yutao Luo, Haotian Zhu, Shuchao Pang, Zhigang Lu, Tian Dong
    - 🏛️ Institutions: Nanjing University of Science and Technology, Macquarie University, Western Sydney University, University of Hong Kong, CSIRO's Data61
    - 📅 Date: March 24, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile agent], [backdoor attack], [security], [contrastive learning], [multimodal LLM]
    - 📖 TLDR: AgentRAE introduces a novel backdoor attack against screenshot-based mobile GUI agents that uses visually natural notification icons as triggers, employing a two-stage pipeline (contrastive learning followed by poisoning training) to achieve over 90% attack success rate across ten mobile operations while evading eight state-of-the-art defenses.

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Mauro Li, Reuben Binns, Soheil Feizi, Lind Seelig, Kasper Luckow
    - 🏛️ Institutions: vLLM Semantic Router Project, MBZUAI, McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [safety], [computer-use agent], [visual grounding], [guardrail], [adversarial attacks]
    - 📖 TLDR: Formalizes the "visual confused deputy" as a security vulnerability in computer-using agents where misperceived screen states (from grounding errors, adversarial screenshot manipulation, or TOCTOU races) cause agents to authorize unintended privileged actions, and proposes a dual-channel contrastive classification guardrail that independently verifies the visual click target and the agent's textual reasoning to block risky executions.

- [SlowBA: An efficiency backdoor attack towards VLM-based GUI agents](https://arxiv.org/abs/2603.08316)
    - Junjie He, Zhizheng Zhang, Haoyu Chen, Sitao Huang, Xuyang Ye
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [attack], [VLM], [backdoor attack], [reinforcement learning], [security]
    - 📖 TLDR: SlowBA is a novel backdoor attack targeting the response efficiency of VLM-based GUI agents by inducing excessively long reasoning chains when triggered by realistic pop-up windows, using a two-stage reward-level backdoor injection strategy with reinforcement learning that significantly increases latency while preserving task accuracy.

- [Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System](https://arxiv.org/abs/2602.10915)
    - Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Tao Yu, Kun Zhang
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile agent], [agent security], [prompt injection], [access control], [operating system], [benchmark]
    - 📖 TLDR: This paper conducts a systematic security analysis of GUI-based mobile agents (using Doubao Mobile Assistant as a case study), identifying vulnerabilities across identity, perception, cognition, and execution dimensions, and proposes Aura, an Agent Universal Runtime Architecture that replaces GUI scraping with a structured intent-driven interaction model secured by cryptographic identity, semantic firewalls, taint-aware memory, and granular access control, achieving 94.3% task success rate while reducing attack success rate to 4.4% on MobileSafetyBench.

- [MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks](https://arxiv.org/abs/2602.09222)
    - Georgios Syros, Evan Rose, Brian Grinstead, Christoph Kerschbaumer, William Robertson, Cristina Nita-Rotaru, Alina Oprea
    - 🏛️ Institutions: Northeastern University, Mozilla Corporation
    - 📅 Date: 2026-02-09
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [attack], [web agent security], [indirect prompt injection], [red-teaming], [MUZZLE]
    - 📖 TLDR: MUZZLE is an automated agentic red-teaming framework that adaptively discovers indirect prompt injection attacks against LLM-based web agents by identifying high-salience injection surfaces and iteratively refining context-aware malicious payloads, discovering 37 new attacks including cross-application prompt injections across 4 web applications.

- [Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense](https://arxiv.org/abs/2602.09012)
    - Jiacheng Liu, Yaxin Luo, Jiacheng Cui, Zhaoyi Li, Xiaohan Zhao
    - 🏛️ Institutions: Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), University College London
    - 📅 Date: February 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agent security], [GUI agent], [web agent], [CAPTCHA], [multimodal agent]
    - 📖 TLDR: Introduces Next-Gen CAPTCHAs, a scalable defense framework that exploits the persistent cognitive gap between humans and GUI-enabled agents in interactive perception, memory, and decision-making, re-establishing robust human-machine differentiation as advanced reasoning models have rendered traditional CAPTCHAs obsolete.

- [WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents](https://arxiv.org/abs/2602.03792)
    - Xilong Wang, Yinuo Liu, Zhun Wang, Dawn Song, Neil Gong
    - 🏛️ Institutions: Duke University, UC Berkeley
    - 📅 Date: 2026-02-03
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [defense], [prompt injection], [web agent], [WebSentinel], [security], [attack detection]
    - 📖 TLDR: WebSentinel is a two-step defense framework that detects and localizes prompt injection attacks in webpages by first extracting segments of interest that may be contaminated and then evaluating each segment's consistency with the webpage content, substantially outperforming baseline methods on multiple datasets.

- [Environmental Injection Attacks against GUI Agents in Realistic Dynamic Environments](https://arxiv.org/abs/2509.11250)
    - Yitong Zhang, Ximo Li, Liyi Cai, Jia Li
    - 🏛️ Institutions: Tsinghua University, Peking University
    - 📅 Date: 2026-01-31
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [attack], [web agent], [benchmark], [grounding], [vision]
    - 📖 TLDR: This paper introduces a realistic dynamic-environment threat model for Environmental Injection Attacks (EIAs) against GUI agents and proposes Chameleon, an attack framework using LLM-driven environment simulation and an Attention Black Hole mechanism to expose hidden vulnerabilities of LVLM-powered GUI agents on real-world websites.

- [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/abs/2601.08406)
    - Xinyi Wu, Jiagui Chen, Geng Hong, Jiayi Dong, Xudong Pan, Jiarun Dai, Min Yang
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute
    - 📅 Date: 2026-01-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [safety], [agent framework], [security evaluation], [attack]
    - 📖 TLDR: WebTrap Park is an automated platform for systematic security evaluation of web agents that instantiates three major security risk sources into 1,226 executable tasks on live web pages, revealing that agent architecture matters more than the underlying model for security robustness.

- [MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction](https://arxiv.org/abs/2601.12822)
    - Yinhao Jiang, Hao Ye, Juntao Ren, Zhenying He, Jian Hou
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute
    - 📅 Date: January 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [agent safety], [benchmark], [framework], [GUI agent], [security], [simulation]
    - 📖 TLDR: MirrorGuard is a plug-and-play defense framework that uses a neural-symbolic simulation pipeline to generate high-risk GUI interaction trajectories in a text-based environment, training a module to intercept and rectify insecure reasoning chains of Computer Use Agents before they execute harmful actions. On the ByteDance UI-TARS system, it reduces the unsafe rate from 66.5% to 13.0% while maintaining low false refusal rates, significantly outperforming prior defenses.

- [Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?](https://arxiv.org/abs/2601.12349)
    - Chenhao Lin, Zichen Ding, Lingming Zhang, Yuanchun Li, Xuanzhe Liu
    - 🏛️ Institutions: Nanjing University, Honor Device Co. Ltd, Institute of Dataspace Hefei Comprehensive National Science Center
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [security], [attack], [Android], [mobile], [benchmark], [LMM]
    - 📖 TLDR: This paper presents "Action Rebinding," a zero-permission attack that exploits the observation-to-action gap in LMM-powered Android GUI agents to hijack their actions, achieving 100% success on atomic rebinding across six agents and 15 tasks while evading all malware scanners, revealing a fundamental architectural flaw in current agent-OS integration.

- [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](https://arxiv.org/abs/2512.23128)
    - Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H. S. Torr, Adam Mahdi, Adel Bibi
    - 🏛️ Institutions: University of Oxford, SoftServe, Independent, Johannes Kepler University Linz
    - 📅 Date: 2025-12-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [safety], [prompt injection], [security], [LLM]
    - 📖 TLDR: TRAP is a benchmark for evaluating how persuasion-based prompt injection attacks can redirect LLM-powered web agents from their intended tasks, finding that across six frontier models agents are susceptible to such attacks in 25% of tasks on average, with psychologically-driven social engineering techniques and small interface changes often doubling attack success rates.

- [Privacy Practices of Browser Agents](https://arxiv.org/abs/2512.07725)
    - Alisha Ukani, Hamed Haddadi, Ali Shahin Shamsabadi, Peter Snyder
    - 🏛️ Institutions: University of California San Diego, Brave Software, Imperial College London
    - 📅 Date: 2025-12-08
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [privacy], [security], [browser agent], [evaluation]
    - 📖 TLDR: This paper presents a systematic framework of 15 measurements across five categories to evaluate the privacy practices of eight popular browser agents, identifying 30 vulnerabilities ranging from disabled browser privacy features to leaking sensitive personal information in form fields.

- [BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents](https://arxiv.org/abs/2511.20597)
    - Kaiyuan Zhang, Mark Tenenholtz, Kyle Polley, Jerry Ma, Denis Yarats, Ninghui Li
    - 🏛️ Institutions: Purdue University, Perplexity AI
    - 📅 Date: 2025-11-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [safety], [prompt injection], [defense], [security]
    - 📖 TLDR: BrowseSafe introduces a benchmark of prompt injection attacks embedded in realistic HTML payloads targeting AI browser agents, and proposes a multi-layered defense-in-depth strategy combining architectural and model-based defenses to protect web agents from evolving prompt injection threats.

- [Building Browser Agents: Architecture, Security, and Practical Solutions](https://arxiv.org/abs/2511.19477)
    - Aram Vardanyan
    - 🏛️ Institutions: FillApp
    - 📅 Date: 2025-11-22
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [browser agent], [security], [prompt injection], [accessibility tree], [benchmark]
    - 📖 TLDR: This paper presents practical findings from building a production browser agent, arguing that architectural decisions (hybrid context management, specialized tooling, programmatic safety constraints) matter more than model capability, and that prompt injection attacks make general-purpose autonomous browsing fundamentally unsafe; the system achieves ~85% on the WebGames benchmark.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: 2025-10-16
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [prompt injection], [attack], [adversarial attack], [multimodal LLM], [security]
    - 📖 TLDR: WebInject proposes a prompt injection attack against MLLM-based web agents by adding optimized pixel-level perturbations to rendered webpages, using a neural network to approximate the non-differentiable webpage-to-screenshot mapping and projected gradient descent to find perturbations that induce attacker-specified actions.

- [In-Browser LLM-Guided Fuzzing for Real-Time Prompt Injection Testing in Agentic AI Browsers](https://arxiv.org/abs/2510.13543)
    - Avihay Cohen
    - 🏛️ Institutions: BrowserTotal
    - 📅 Date: 2025-10-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [browser agent], [security], [prompt injection], [fuzzing], [attack]
    - 📖 TLDR: Presents an in-browser LLM-guided fuzzing framework that automatically discovers prompt injection vulnerabilities in agentic AI browsers, finding that while tested tools block simple attacks, they fail 58-74% of the time after 10 adaptive fuzzing iterations, with page summarization and Q&A features being particularly vulnerable (73% and 71% attack success rates).

- [HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities](https://arxiv.org/abs/2510.12200)
    - Xiaoxue Ren, Penghao Jiang, Kaixin Li, Zhiyong Huang, Xiaoning Du, Jiaojiao Jiang, Zhenchang Xing, Jiamou Sun, Terry Yue Zhuo
    - 🏛️ Institutions: Zhejiang University, University of New South Wales, National University of Singapore, Monash University, CSIRO's Data61, Australian National University
    - 📅 Date: October 14, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [computer-use agent], [web vulnerabilities], [CTF], [HackWorld]
    - 📖 TLDR: This paper introduces HackWorld, the first benchmark for evaluating whether computer-use agents can discover and exploit realistic web application vulnerabilities through visual interaction. It places agents in vulnerable real-world-style web applications and measures attack performance in a Capture-the-Flag setting rather than simplified static security tasks. The benchmark shows that current CUAs have low exploitation success and weak cybersecurity awareness, making it a useful security stress test for web-based computer-use agents.

- [Cross-Modal Content Optimization for Steering Web Agent Preferences](https://arxiv.org/abs/2510.03612)
    - Tanqiu Jiang, Min Bai, Nikolaos Pappas, Yanjun Qi, Sandesh Swamy
    - 🏛️ Institutions: Stony Brook University, AWS AI Labs
    - 📅 Date: 2025-10-03
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [adversarial attack], [VLM], [multimodal], [security], [benchmark]
    - 📖 TLDR: Introduces Cross-Modal Preference Steering (CPS), a black-box adversarial attack that jointly optimizes imperceptible visual and textual modifications to steer VLM-based web agent preferences, demonstrating significantly higher attack success rates than single-modal baselines while maintaining low detection rates across GPT-4.1, Qwen-2.5VL, and Pixtral-Large on movie selection and e-commerce tasks.

- [WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents](https://arxiv.org/abs/2510.01354)
    - Yinuo Liu, Ruohan Xu, Xilong Wang, Yuqi Jia, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: 2025-10-01
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [security], [prompt injection], [attack detection], [safety]
    - 📖 TLDR: WAInjectBench presents the first comprehensive benchmark for evaluating prompt injection detection methods targeting web agents, finding that while some detectors handle explicit textual attacks or visible image perturbations reasonably well, they largely fail against attacks that omit explicit instructions or use imperceptible perturbations.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [CUA], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Chuan Guo, Aaron Grattafiori, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Independent Researcher
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [web agent], [prompt injection], [security], [WASP]
    - 📖 TLDR: This paper introduces WASP, a benchmark for end-to-end evaluation of web-agent security against prompt injection attacks in realistic multi-step web tasks. It shows that even strong web agents can be partially deceived at very high rates by simple human-written injections, while also revealing a more nuanced failure mode where agents are often insecure yet too incompetent to fully execute the attacker's goal. The benchmark is designed to measure security under realistic web-agent deployment conditions rather than simplified single-step attacks.

- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434)
    - Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu
    - 🏛️ Institutions: University of Georgia, Tencent AI Seattle Lab, Microsoft Research, University of Waterloo, Hong Kong Polytechnic University
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [GUI agent], [trustworthiness], [safety], [security], [benchmark]
    - 📖 TLDR: A survey on trustworthy GUI agents that introduces a workflow-aligned taxonomy decomposing trust into Perception Trust, Reasoning Trust, and Interaction Trust, systematically reviewing failure modes, adversarial attacks, defense mechanisms, and evaluation practices for deploying GUI agents safely.

- [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)
    - Lukas Aichberger, Alasdair Paren, Guohao Li, Philip Torr, Yarin Gal, Adel Bibi
    - 🏛️ Institutions: Johannes Kepler University Linz, University of Oxford
    - 📅 Date: March 13, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [security], [adversarial attacks], [computer-use agent], [OS agent], [MIP against agent]
    - 📖 TLDR: This paper identifies Malicious Image Patches as a new attack vector against multimodal OS agents, where adversarially perturbed visual regions on the screen can trigger harmful actions when captured by the agent. The attack generalizes across prompts and screen setups, showing that benign-looking visual content such as wallpapers or social media images can hijack computer-use agents. The paper exposes a concrete security weakness in OS-level agents that goes beyond text-only prompt injection.

- [In-Context Defense in Computer Agents: An Empirical Study](https://arxiv.org/abs/2503.09241)
    - Pei Yang, Hai Ci, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: March 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [defense], [in-context learning], [chain-of-thought], [context deception], [security]
    - 📖 TLDR: This paper introduces an in-context defense strategy for computer agents powered by vision-language models (VLMs), targeting context deception attacks such as malicious pop-ups and deceptive HTML elements. By incorporating a small set of curated exemplars and employing chain-of-thought reasoning, the approach guides agents to perform explicit defensive reasoning before action planning. Experiments demonstrate significant reductions in attack success rates across various attack types, highlighting the effectiveness of the method in enhancing agent reliability without requiring model fine-tuning.

- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis](https://arxiv.org/abs/2502.20383)
    - Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
    - 🏛️ Institutions: University of Maryland
    - 📅 Date: March 4, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [security], [jailbreaking], [evaluation], [OpenHands]
    - 📖 TLDR: This paper investigates why Web AI agents are significantly more susceptible to executing harmful commands compared to standalone LLMs, despite sharing the same underlying models. Through a fine-grained evaluation, the authors identify three critical factors contributing to this vulnerability: embedding user goals into system prompts, multi-step action generation, and processing of event streams from web navigation. The study introduces a five-level harmfulness evaluation framework and utilizes the OpenHands platform to systematically assess these vulnerabilities, revealing a 46.6% success rate in malicious task execution by Web AI agents versus 0% for standalone LLMs.

- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://arxiv.org/abs/2402.10196)
    - Lingbo Mo, Zeyi Liao, Boyuan Zheng, Yu Su, Chaowei Xiao, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of Wisconsin-Madison
    - 📅 Date: February 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [adversarial attacks], [security risks], [language agents], [perception-brain-action]
    - 📖 TLDR: This paper introduces a conceptual framework to assess and understand adversarial vulnerabilities in language agents, dividing the agent structure into three components—Perception, Brain, and Action. It discusses 12 specific adversarial attack types that exploit these components, ranging from input manipulation to complex backdoor and jailbreak attacks. The framework provides a basis for identifying and mitigating risks before the widespread deployment of these agents in real-world applications.
