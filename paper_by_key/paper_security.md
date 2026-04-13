# Papers with Keyword: security

- [WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks](https://arxiv.org/abs/2604.06367)
    - Guruprasad Viswanathan Ramesh, Asmit Nayak, Basieem Siddique, Kassem Fawaz
    - 🏛️ Institutions: UW-Madison
    - 📅 Date: April 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [privacy], [WebSP-Eval]
    - 📖 TLDR: WebSP-Eval is the first framework evaluating web agents on user-facing website security and privacy tasks such as cookie preferences, privacy settings, and session revocation. Across 200 task instances on 28 websites, agents fail more than 45% on tasks with stateful UI elements like toggles and checkboxes.

- [AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents](https://arxiv.org/abs/2603.23007)
    - Yutao Luo, Haotian Zhu, Shuchao Pang, Zhigang Lu, Tian Dong, Yongbin Zhou, Minhui Xue
    - 🏛️ Institutions: Nanjing University of Science and Technology, Macquarie University, Western Sydney University, HKU, CSIRO Data61
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
    - 💻 Env: [General GUI]
    - 🔑 Key: [security], [guardrail], [visual confused deputy], [TOCTOU], [grounding errors], [dual-channel contrastive classification]
    - 📖 TLDR: This paper reframes perception failures in GUI agents as a security problem rather than just a performance issue, formalizing the visual confused deputy where misperceived UI state causes privileged actions on the wrong target. It then proposes a dual-channel guardrail that separately checks the visual target and the agent's textual reasoning to block unsafe executions.

- [SlowBA: An efficiency backdoor attack towards VLM-based GUI agents](https://arxiv.org/abs/2603.08316)
    - Junxian Li, Tu Lan, Haozhen Tan, Yan Meng, Haojin Zhu
    - 🏛️ Institutions: SJTU
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
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
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, NJU, Honor Device Co., Ltd., Institute of Dataspace, Hefei Comprehensive National Science Center
    - 📅 Date: January 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [security], [attack], [Android], [Action Rebinding], [verification gates]
    - 📖 TLDR: This paper introduces Action Rebinding, a zero-permission Android attack that exploits the observation-to-action gap in multimodal GUI agents by changing foreground UI state before the planned action executes. Across six agents and 15 tasks it achieves 100% atomic rebinding success, and with intent alignment can also bypass confirmation-style verification gates.

- [HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities](https://arxiv.org/abs/2510.12200)
    - Xiaoxue Ren, Penghao Jiang, Kaixin Li, Zhiyong Huang, Xiaoning Du, Jiaojiao Jiang, Zhenchang Xing, Jiamou Sun, Terry Yue Zhuo
    - 🏛️ Institutions: ZJU, University of New South Wales, NUS, Monash University, CSIRO’s Data61, Australian National University
    - 📅 Date: October 14, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [web vulnerabilities], [CTF], [penetration testing], [HackWorld]
    - 📖 TLDR: HackWorld uses a CTF-style setup over 36 vulnerable web applications spanning 11 frameworks and 7 languages to test whether computer-use agents can discover and exploit realistic web flaws through GUI interaction. Current agents achieve exploitation rates below 12% and often fail at multi-step attack planning and security-tool use.

- [VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents](https://arxiv.org/abs/2506.02456)
    - Tri Cao, Bennett Lim, Yue Liu, Yuan Sui, Yuexin Li, Shumin Deng, Lin Lu, Nay Oo, Shuicheng Yan, Bryan Hooi
    - 🏛️ Institutions: NUS, Cyber Emerging Tech and R&D
    - 📅 Date: June 03, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [visual prompt injection], [security], [attack], [browser-use agents], [VPI-Bench]
    - 📖 TLDR: VPI-Bench studies visual prompt injection attacks on computer-use agents, where malicious instructions are embedded directly into rendered user interfaces rather than hidden in HTML. Across 306 cases on five platforms, it shows that both full-system-access CUAs and browser-use agents remain highly vulnerable, and that prompt-only defenses offer limited protection.

- [A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?](https://arxiv.org/abs/2505.10924)
    - Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
    - 🏛️ Institutions: CMU, CUHK, KAUST, JHU, NTU, HKUST
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [safety], [security], [threat taxonomy], [defense taxonomy]
    - 📖 TLDR: This survey systematizes safety and security risks in computer-using agents, from reasoning failures and multimodal vulnerabilities to risks introduced by multi-component agent stacks. It organizes the field around threat categories, defensive strategies, and the benchmarks and datasets currently used to study secure CUA deployment.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: May 16, 2025
    - 📑 Publisher: EMNLP 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [security], [prompt injection], [pixel perturbation], [screenshot attack], [neural rendering approximation], [WebInject]
    - 📖 TLDR: WebInject attacks screenshot-based web agents by perturbing the raw pixels of a rendered webpage so the resulting screenshot steers the agent toward an attacker-chosen action. To optimize that attack despite the non-differentiable render-to-screenshot pipeline, it learns a neural approximation of the mapping and then applies projected gradient descent.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, WenHao Wang, Tianze Wu, Zhengxi Lu, Siheng Chen, LiLinghao, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: ZJU, vivo AI Lab, CUHK MMLab, SJTU
    - 📅 Date: April 28, 2025
    - 📑 Publisher: TMLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [mobile automation], [training taxonomy], [benchmark taxonomy], [planning], [security]
    - 📖 TLDR: This survey reviews the development of LLM-powered mobile GUI agents for phone automation, from script-like systems to adaptive multimodal agents. It organizes the space around agent architectures, training approaches, datasets and benchmarks, and closes with open problems such as user adaptation, on-device efficiency, and security.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Aaron Grattafiori, Chuan Guo, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [prompt injection], [security-by-incompetence], [WASP]
    - 📖 TLDR: WASP is a benchmark for end-to-end web-agent security under realistic multi-step prompt injection attacks rather than simplified single-step tests. It shows that strong agents can be partially deceived at very high rates by low-effort human-written injections, while also exposing a security-by-incompetence pattern where unsafe agents often fail to fully realize the attacker goal.

- [sudo rm -rf agentic_security](https://arxiv.org/abs/2503.20279)
    - Sejin Lee, Jian Kim, Haon Park, Ashkan Yousefpour, Sangyoon Yu, Min Song
    - 🏛️ Institutions: Aim Intelligence, Yonsei University, SNU
    - 📅 Date: March 26, 2025
    - 📑 Publisher: ACL 2025 Industry Track
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [security], [jailbreak], [Detox2Tox], [refusal feedback], [SUDO]
    - 📖 TLDR: SUDO is a screen-based jailbreak attack for computer-use agents that rewrites harmful requests into benign-looking ones, extracts detailed instructions from stronger VLMs, and then reintroduces the malicious content before execution. Its iterative refusal-feedback loop substantially raises attack success against Claude for Computer Use on real desktop and web tasks.

- [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)
    - Lukas Aichberger, Alasdair Paren, Guohao Li, Philip Torr, Yarin Gal, Adel Bibi
    - 🏛️ Institutions: Johannes Kepler University Linz, Oxford
    - 📅 Date: March 13, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [adversarial attacks], [malicious image patches], [screen hijacking], [MIP]
    - 📖 TLDR: This paper shows that adversarial image patches embedded in on-screen content can hijack multimodal OS agents into harmful actions. The attacks transfer across prompts and screen configurations, exposing a visual attack surface that goes beyond text-only prompt injection.

- [In-Context Defense in Computer Agents: An Empirical Study](https://arxiv.org/abs/2503.09241)
    - Pei Yang, Hai Ci, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS
    - 📅 Date: March 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [security], [in-context defense], [context deception], [environment injection], [chain-of-thought defense]
    - 📖 TLDR: This paper studies in-context defense for computer agents facing context deception attacks such as malicious pop-ups, deceptive HTML, and distracting ads. A small set of defensive exemplars plus explicit reasoning before action planning sharply reduces attack success without model fine-tuning.

- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis](https://arxiv.org/abs/2502.20383)
    - Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
    - 🏛️ Institutions: UMD
    - 📅 Date: February 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [security], [component-level analysis], [harmfulness taxonomy], [observational capabilities], [OpenHands]
    - 📖 TLDR: This paper analyzes why web AI agents are more vulnerable than standalone LLMs even when they use the same underlying models. It attributes the gap to user-goal embedding in system prompts, multi-step action generation, and observational signals, and proposes a more granular evaluation taxonomy for studying those failures.

- [Evaluating the Robustness of Multimodal Agents Against Active Environmental Injection Attacks](https://arxiv.org/abs/2502.13053)
    - Yurun Chen, Xavier Hu, Keting Yin, Juncheng Li, Shengyu Zhang
    - 🏛️ Institutions: ZJU
    - 📅 Date: February 18, 2025
    - 📑 Publisher: ACM MM 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [security], [AEIA], [AEIA-MN], [mobile notifications], [reasoning gap vulnerabilities]
    - 📖 TLDR: This paper defines Active Environment Injection Attacks, where malicious content is disguised as ordinary environmental elements to manipulate multimodal agents. Its AEIA-MN attack uses mobile notifications and reasoning-gap exploitation to show that AndroidWorld agents remain highly vulnerable.
