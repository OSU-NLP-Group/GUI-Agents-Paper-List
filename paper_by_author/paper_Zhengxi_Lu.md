# Zhengxi Lu's Papers

- [UI-Zoomer: Uncertainty-Driven Adaptive Zoom-In for GUI Grounding](https://arxiv.org/abs/2604.14113)
    - Fei Tang, Bofan Chen, Zhengxi Lu, Tongbo Chen, Songqin Nong, Tao Jiang, Wenhao Xu, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
    - 🏛️ Institutions: ZJU
    - 📅 Date: April 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [uncertainty quantification], [adaptive zoom], [UI-Zoomer]
    - 📖 TLDR: UI-Zoomer treats the trigger and scale of zoom-in as a prediction uncertainty quantification problem. A confidence-aware gate activates zoom-in only when needed, while an uncertainty-driven module picks per-instance crop sizes via variance decomposition. The training-free method improves GUI grounding by 4.2-13.4% on three benchmarks and is compatible with multiple model architectures.

- [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/abs/2604.08455)
    - Tongbo Chen, Zhengxi Lu, Zhan Xu, Guocheng Shao, Shaohan Zhao, Fei Tang, Yong Du, Kaitao Song, Yizhou Liu, Yuchen Yan, Wenqi Zhang, Xu Tan, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
    - 🏛️ Institutions: ZJU, Apple, Tencent
    - 📅 Date: April 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [personalization], [proactive agents], [KnowU-Bench]
    - 📖 TLDR: KnowU-Bench is an online benchmark for personalized mobile agents on Android emulation with 42 general, 86 personalized, and 64 proactive tasks. It hides user profiles from the agent and forces genuine preference inference through multi-turn dialogues. Even frontier models fall below 50% under vague instructions requiring preference inference.

- [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Qinyi Luo, Shunye Tang, Yuxiang Chai, Weifeng Lin, Han Xiao, WenHao Wang, Siheng Chen, Zhengxi Lu, Gao Wu, Hao Wang, Liang Liu, Yong Liu
    - 🏛️ Institutions: ZJU, Nankai University, CUHK, SJTU, vivo AI Lab
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [memory], [evaluation], [MemGUI-Eval], [MemGUI-Bench]
    - 📖 TLDR: MemGUI-Bench is a memory-focused benchmark for mobile GUI agents covering dynamic tasks that require cross-temporal and cross-spatial retention. Paired with MemGUI-Eval, it reveals large hidden memory deficits in current agents that standard benchmarks miss.

- [MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/abs/2509.06477)
    - Pengxiang Zhao, Guangyi Liu, Yaozhen Liang, Weiqing He, Zhengxi Lu, Yuehao Huang, Yaxuan Guo, Kexin Zhang, Hao Wang, Liang Liu, Yong Liu
    - 🏛️ Institutions: ZJU, vivo AI Lab, Huzhou Institute of Zhejiang University
    - 📅 Date: September 08, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [shortcut-augmented agents], [APIs], [deep links], [RPA scripts], [shortcut generation], [MAS-Bench]
    - 📖 TLDR: MAS-Bench benchmarks hybrid mobile agents that can combine ordinary GUI interaction with shortcuts such as APIs, deep links, and RPA scripts. It covers 139 tasks across 11 real-world apps, includes 88 predefined shortcuts and 7 evaluation metrics, and explicitly tests whether agents can discover and construct reusable low-cost workflows on their own.

- [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)
    - Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, Zhengxi Lu, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: August 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [model], [GUI-Owl], [self-evolving trajectory production], [trajectory correctness judgment], [TRPO], [multi-agent framework], [Mobile-Agent-v3]
    - 📖 TLDR: This paper introduces GUI-Owl as a foundation model for GUI automation and builds Mobile-Agent-v3 as a multi-agent framework on top of it. The work combines cross-OS trajectory production, diverse GUI data synthesis, reasoning enhancement, and trajectory-aware RL, and reports stronger open-source results on both AndroidWorld and OSWorld.

- [Test‑Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615)
    - Yong Du, Yuchen Yan, Fei Tang, Zhengxi Lu, Chang Zong, Weiming Lu, Shengpei Jiang, Yongliang Shen
    - 🏛️ Institutions: ZJU, Central South University, Zhejiang University of Science and Technology, SF Technology
    - 📅 Date: August 07, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [GUI-RC], [GUI-RCPO], [region consistency], [test-time scaling], [test-time reinforcement learning]
    - 📖 TLDR: This paper uses consistency across multiple grounding predictions as a test-time signal for GUI grounding. GUI-RC aggregates sampled outputs into consensus regions without extra training, while GUI-RCPO turns the same signal into rewards for test-time policy optimization on unlabeled data, improving ScreenSpot results across several model families.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, WenHao Wang, Tianze Wu, Zhengxi Lu, Siheng Chen, LiLinghao, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: ZJU, vivo AI Lab, CUHK MMLab, SJTU
    - 📅 Date: April 28, 2025
    - 📑 Publisher: TMLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [mobile automation], [training taxonomy], [benchmark taxonomy], [planning], [security]
    - 📖 TLDR: This survey reviews the development of LLM-powered mobile GUI agents for phone automation, from script-like systems to adaptive multimodal agents. It organizes the space around agent architectures, training approaches, datasets and benchmarks, and closes with open problems such as user adaptation, on-device efficiency, and security.

- [UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Han Xiao, Shuai Ren, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, CUHK
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [reinforcement learning], [rule-based action reward], [GRPO], [UI-R1-3B], [AndroidControl], [ScreenSpot-pro]
    - 📖 TLDR: UI-R1 studies whether rule-based reinforcement learning can improve efficient GUI action prediction for multimodal mobile agents. It trains UI-R1-3B with GRPO on a curated set of 136 challenging mobile tasks using a rule-based action reward, and reports gains on ScreenSpot, ScreenSpot-Pro, and AndroidControl over the base model.
