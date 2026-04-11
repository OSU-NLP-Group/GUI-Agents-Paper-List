# Papers with Keyword: security

- [AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents](https://arxiv.org/abs/2603.23007)
    - Yutao Luo, Haotian Zhu, Shuchao Pang, Zhigang Lu, Tian Dong, Yongbin Zhou, Minhui Xue
    - 🏛️ Institutions: Nanjing University of Science and Technology, Macquarie University, Western Sydney University, The University of Hong Kong, CSIRO Data61
    - 📅 Date: March 24, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [backdoor attack], [notification trigger], [security], [contrastive learning], [Remote Action Execution], [AgentRAE]
    - 📖 TLDR: AgentRAE is a backdoor attack against screenshot-based mobile GUI agents that uses benign-looking notification icons as triggers for remote action execution. Its contrastive-pretraining plus poisoning pipeline preserves clean performance, exceeds 90% attack success over ten mobile operations, and evades eight representative defenses.

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
    - 🏛️ Institutions: McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [guardrail], [visual confused deputy], [TOCTOU], [grounding errors], [dual-channel contrastive classification]
    - 📖 TLDR: This paper reframes perception failures in GUI agents as a security problem rather than just a performance issue, formalizing the visual confused deputy where misperceived UI state causes privileged actions on the wrong target. It then proposes a dual-channel guardrail that separately checks the visual target and the agent's textual reasoning to block unsafe executions.

- [You Told Me to Do It: Measuring Instructional Text-induced Private Data Leakage in LLM Agents](https://arxiv.org/abs/2603.11862)
    - Ching-Yu Kao, Xinfeng Li, Shenyu Dai, Tianze Qiu, Pengcheng Zhou, Eric Hanchen Jiang, Philip Sperl
    - 🏛️ Institutions: Fraunhofer AISEC, NTU, KTH, NUS, UCLA
    - 📅 Date: March 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [security], [documentation injection], [privacy], [data leakage], [ReadSecBench], [Trusted Executor Dilemma]
    - 📖 TLDR: This paper studies documentation-embedded instruction injection in high-privilege LLM agents and frames the failure mode as the Trusted Executor Dilemma. It introduces ReadSecBench, shows exfiltration success up to 85%, and finds that both rule-based and LLM-based defenses still fail to catch the attacks reliably.

- [SlowBA: An efficiency backdoor attack towards VLM-based GUI agents](https://arxiv.org/abs/2603.08316)
    - Junxian Li, Tu Lan, Haozhen Tan, Yan Meng, Haojin Zhu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [backdoor attack], [response latency], [reward-level backdoor injection], [popup trigger], [security], [SlowBA]
    - 📖 TLDR: SlowBA studies a backdoor attack on VLM-based GUI agents that targets response efficiency rather than action correctness, using realistic pop-up triggers to induce excessively long reasoning chains. Its two-stage reward-level backdoor injection stays stealthy, preserves task accuracy, and substantially increases latency under trigger conditions.

- [WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents](https://arxiv.org/abs/2602.03792)
    - Xilong Wang, Yinuo Liu, Zhun Wang, Dawn Song, Neil Gong
    - 🏛️ Institutions: Duke University, UC Berkeley
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [defense], [prompt injection], [WebSentinel], [security], [attack detection]
    - 📖 TLDR: WebSentinel is a two-step defense framework that detects and localizes prompt injection attacks in webpages by first extracting segments of interest that may be contaminated and then evaluating each segment's consistency with the webpage content, substantially outperforming baseline methods on multiple datasets.

- [Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?](https://arxiv.org/abs/2601.12349)
    - Yi Qian, Kunwei Qian, Xingbang He, Ligeng Chen, Jikang Zhang, Tiantai Zhang, Haiyang Wei, Linzhang Wang, Hao Wu, Bing Mao
    - 🏛️ Institutions: State Key Laboratory for Novel Software Technology, Nanjing University, Honor Device Co., Ltd., Institute of Dataspace, Hefei Comprehensive National Science Center
    - 📅 Date: January 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [security], [attack], [Android], [Action Rebinding], [verification gates]
    - 📖 TLDR: This paper introduces Action Rebinding, a zero-permission Android attack that exploits the observation-to-action gap in multimodal GUI agents by changing foreground UI state before the planned action executes. Across six agents and 15 tasks it achieves 100% atomic rebinding success, and with intent alignment can also bypass confirmation-style verification gates.

- [Privacy Practices of Browser Agents](https://arxiv.org/abs/2512.07725)
    - Alisha Ukani, Hamed Haddadi, Ali Shahin Shamsabadi, Peter Snyder
    - 🏛️ Institutions: University of California, San Diego, Brave Software, Imperial College London
    - 📅 Date: December 08, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [privacy], [security], [evaluation]
    - 📖 TLDR: This paper presents a systematic framework of 15 measurements across five categories to evaluate the privacy practices of eight popular browser agents, identifying 30 vulnerabilities ranging from disabled browser privacy features to leaking sensitive personal information in form fields.

- [In-Browser LLM-Guided Fuzzing for Real-Time Prompt Injection Testing in Agentic AI Browsers](https://arxiv.org/abs/2510.13543)
    - Avihay Cohen
    - 🏛️ Institutions: BrowserTotal
    - 📅 Date: October 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [security], [prompt injection], [fuzzing], [attack]
    - 📖 TLDR: Presents an in-browser LLM-guided fuzzing framework that automatically discovers prompt injection vulnerabilities in agentic AI browsers, finding that while tested tools block simple attacks, they fail 58-74% of the time after 10 adaptive fuzzing iterations, with page summarization and Q&A features being particularly vulnerable (73% and 71% attack success rates).

- [HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities](https://arxiv.org/abs/2510.12200)
    - Xiaoxue Ren, Penghao Jiang, Kaixin Li, Zhiyong Huang, Xiaoning Du, Jiaojiao Jiang, Zhenchang Xing, Jiamou Sun, Terry Yue Zhuo
    - 🏛️ Institutions: Zhejiang University, University of New South Wales, National University of Singapore, Monash University, CSIRO’s Data61, Australian National University
    - 📅 Date: October 14, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [web vulnerabilities], [CTF], [penetration testing], [HackWorld]
    - 📖 TLDR: HackWorld uses a CTF-style setup over 36 vulnerable web applications spanning 11 frameworks and 7 languages to test whether computer-use agents can discover and exploit realistic web flaws through GUI interaction. Current agents achieve exploitation rates below 12% and often fail at multi-step attack planning and security-tool use.

- [AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents](https://arxiv.org/abs/2509.07764)
    - Haitao Hu, Peng Chen, Yanpeng Zhao, Yuqi Chen
    - 🏛️ Institutions: ShanghaiTech University, Independent Researcher
    - 📅 Date: September 09, 2025
    - 📑 Publisher: CCS 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [defense framework], [real-time auditing], [system traces], [BadComputerUse], [AgentSentinel]
    - 📖 TLDR: AgentSentinel is an end-to-end real-time defense framework for computer-use agents that intercepts sensitive operations and audits them against task context and system traces before execution. Its companion BadComputerUse benchmark shows that current agents are highly vulnerable to harmful operations, while AgentSentinel substantially improves defense success against these attacks.

- [VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents](https://arxiv.org/abs/2506.02456)
    - Tri Cao, Bennett Lim, Yue Liu, Yuan Sui, Yuexin Li, Shumin Deng, Lin Lu, Nay Oo, Shuicheng Yan, Bryan Hooi
    - 🏛️ Institutions: National University of Singapore, Cyber Emerging Tech and R&D
    - 📅 Date: June 03, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [visual prompt injection], [security], [attack], [browser-use agents], [VPI-Bench]
    - 📖 TLDR: VPI-Bench studies visual prompt injection attacks on computer-use agents, where malicious instructions are embedded directly into rendered user interfaces rather than hidden in HTML. Across 306 cases on five platforms, it shows that both full-system-access CUAs and browser-use agents remain highly vulnerable, and that prompt-only defenses offer limited protection.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [prompt injection], [attack], [adversarial attack], [multimodal LLM], [security]
    - 📖 TLDR: WebInject proposes a prompt injection attack against MLLM-based web agents by adding optimized pixel-level perturbations to rendered webpages, using a neural network to approximate the non-differentiable webpage-to-screenshot mapping and projected gradient descent to find perturbations that induce attacker-specified actions.

- [A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?](https://arxiv.org/abs/2505.10924)
    - Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
    - 🏛️ Institutions: Carnegie Mellon University, The Chinese University of Hong Kong, KAUST, Johns Hopkins University, Nanyang Technological University, The Hong Kong University of Science and Technology
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [safety], [security]
    - 📖 TLDR: A comprehensive survey of safety and security threats to computer-using agents, covering vulnerabilities in LLM-driven reasoning, multi-component integration, and GUI interaction, analyzing novel risks as CUAs evolve from prototype tools to sophisticated autonomous systems.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Aaron Grattafiori, Chuan Guo, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [security], [WASP]
    - 📖 TLDR: Evaluates web-agent security under realistic multi-step prompt injection attacks instead of simplified single-step setups. WASP shows that even strong agents can be partially deceived at very high rates by low-effort human-written injections, while also revealing a security-by-incompetence pattern where agents are unsafe but often too weak to fully realize the attacker’s goal.

- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434)
    - Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu
    - 🏛️ Institutions: University of Georgia, Tencent AI Seattle Lab, Microsoft Research, University of Waterloo, Hong Kong Polytechnic University
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [trustworthiness], [safety], [security], [benchmark]
    - 📖 TLDR: A survey on trustworthy GUI agents that introduces a workflow-aligned taxonomy decomposing trust into Perception Trust, Reasoning Trust, and Interaction Trust, systematically reviewing failure modes, adversarial attacks, defense mechanisms, and evaluation practices for deploying GUI agents safely.

- [sudo rm -rf agentic_security](https://arxiv.org/abs/2503.20279)
    - Sejin Lee, Jian Kim, Haon Park, Ashkan Yousefpour, Sangyoon Yu, Min Song
    - 🏛️ Institutions: Aim Intelligence, Yonsei University, SNU
    - 📅 Date: March 26, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [attack], [jailbreaking], [safety]
    - 📖 TLDR: SUDO (Screen-based Universal Detox2Tox Offense) is a novel attack framework that bypasses refusal-trained safeguards in commercial CUAs (e.g., Claude Computer Use) by transforming harmful requests into seemingly benign ones via a Detox2Tox mechanism, exposing critical vulnerabilities in CUA safety.

- [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)
    - Lukas Aichberger, Alasdair Paren, Guohao Li, Philip Torr, Yarin Gal, Adel Bibi
    - 🏛️ Institutions: Johannes Kepler University Linz, University of Oxford
    - 📅 Date: March 13, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [security], [adversarial attacks], [OS agent], [MIP against agent]
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
    - 📅 Date: February 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [security], [jailbreaking], [evaluation], [OpenHands]
    - 📖 TLDR: This paper investigates why Web AI agents are significantly more susceptible to executing harmful commands compared to standalone LLMs, despite sharing the same underlying models. Through a fine-grained evaluation, the authors identify three critical factors contributing to this vulnerability: embedding user goals into system prompts, multi-step action generation, and processing of event streams from web navigation. The study introduces a five-level harmfulness evaluation framework and utilizes the OpenHands platform to systematically assess these vulnerabilities, revealing a 46.6% success rate in malicious task execution by Web AI agents versus 0% for standalone LLMs.
