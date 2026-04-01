# Papers with Keyword: mobile

- [GUI-CEval: A Hierarchical and Comprehensive Chinese Benchmark for Mobile GUI Agents](https://arxiv.org/abs/2603.15039)
    - Haotian Zhao, Yuzhe Qin, Dongliang Li, Dongdong Hu, Xingshuai Zhang
    - 🏛️ Institutions: Xiaomi
    - 📅 Date: March 16, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile], [chinese], [evaluation], [GUI grounding], [agent]
    - 📖 TLDR: GUI-CEval is the first comprehensive Chinese benchmark for mobile GUI agents, spanning 201 apps across four device types with a hierarchical two-level evaluation structure (atomic abilities and application-level tasks) along five dimensions (perception, planning, reflection, execution, evaluation), revealing that most MLLMs still struggle with reflective decision-making and post-action self-evaluation.

- [PIRA-Bench: A Transition from Reactive GUI Agents to GUI-based Proactive Intent Recommendation Agents](https://arxiv.org/abs/2603.08013)
    - Zihao Wu, Zihan Ding, Fan Zhou, Hao Shi, Xiaomin Zhang
    - 🏛️ Institutions: The Chinese University of Hong Kong (MMLab @ CUHK), Nankai University, Huawei Research
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [proactive agent], [GUI agent], [intent recommendation], [mobile], [multimodal LLM]
    - 📖 TLDR: PIRA-Bench introduces a benchmark for evaluating proactive GUI agents that anticipate user intentions from continuous visual inputs (screenshots) without explicit instructions, featuring complex trajectories with interleaved intents and noisy segments, along with a memory-aware baseline framework (PIRF) for managing multiple task threads.

- [SecAgent: Efficient Mobile GUI Agent with Semantic Context](https://arxiv.org/abs/2603.08533)
    - Yanyang Li, Kaizhe Hu, Guohao Li, Heyang Gong, Yeye He
    - 🏛️ Institutions: Alibaba Group
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile], [efficiency], [dataset], [benchmark], [reinforcement learning]
    - 📖 TLDR: SecAgent is a 3B-scale mobile GUI agent that introduces a semantic context mechanism to distill history screenshots into concise natural language summaries, reducing computational costs while preserving task-relevant information. It also contributes a large-scale human-verified Chinese mobile GUI dataset (18k grounding samples, 121k navigation steps) and benchmark, achieving performance comparable to 7B-8B models through supervised and reinforcement fine-tuning.

- [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725)
    - Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: February 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [world model], [mobile], [code generation], [VLM], [benchmark]
    - 📖 TLDR: gWorld proposes visual world modeling for mobile GUIs via renderable code generation, where a single VLM predicts the next GUI state as executable web code rather than generating pixels directly, achieving state-of-the-art accuracy on multiple benchmarks while being over 50x smaller than competing models.

- [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528)
    - Hongze Mi, Yibo Feng, Wenjie Lu, Wenbin Jiang, Yasheng Wang
    - 🏛️ Institutions: Didichuxing Co. Ltd, The Chinese University of Hong Kong Shenzhen, Tianjin University, Sun Yat-sen University, Fudan University
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [memory system], [training-free], [MLLM], [multi-app], [mobile]
    - 📖 TLDR: Darwinian Memory System (DMS) is a training-free, self-evolving memory architecture for GUI agents that treats memory as a dynamic ecosystem governed by natural selection, decomposing trajectories into reusable units and pruning suboptimal paths via utility-driven selection, achieving 18.0% gains in success rate and 33.9% in execution stability on real-world multi-app benchmarks.

- [MAGNET: Towards Adaptive GUI Agents with Memory-Driven Knowledge Evolution](https://arxiv.org/abs/2601.19199)
    - Hui Zhang, Kangyang Luo, Haoxiang Jia, Li Zhang, Zhaohui Jiang
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute, University of Southern California
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [memory], [mobile], [Android], [knowledge transfer], [adaptation]
    - 📖 TLDR: MAGNET is a memory-driven adaptive GUI agent framework that uses dual-level memory (stationary memory for mapping visual features to functional semantics and procedural memory for capturing task intents) with a dynamic evolution mechanism, enabling robust performance on mobile GUI tasks despite UI updates and distribution shifts, as demonstrated on AndroidWorld and offline benchmarks.

- [SwipeGen: Bridging the Execution Gap in GUI Agents via Human-like Swipe Synthesis](https://arxiv.org/abs/2601.18305)
    - Zishuo Liu, Yongwen Zhu, Tao Xu, Xinyu Xu, Mingxuan Yuan
    - 🏛️ Institutions: Fudan University, Shanghai Key Laboratory of Intelligent Information Processing
    - 📅 Date: January 20, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [swipe interaction], [data synthesis], [benchmark], [action execution], [mobile]
    - 📖 TLDR: SwipeGen proposes an automated pipeline to synthesize human-like swipe gestures for GUI agents and introduces the first swipe execution benchmark, along with GUISwiper, a GUI agent that achieves 69.07% swipe execution accuracy (a 214% improvement over VLM baselines).

- [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197)
    - Jingyang Zhou, Yan Feng, Wei Chen, Cheng Zhang, Ziyang Luo
    - 🏛️ Institutions: Xiaomi
    - 📅 Date: January 20, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [test-time scaling], [critic model], [data flywheel], [training framework], [mobile]
    - 📖 TLDR: GAIA proposes a data flywheel system that trains an Intuitive Critic Model (ICM) to evaluate and filter GUI agent actions at test time, using iterative cycles of positive/negative sample collection to progressively improve critic accuracy and boost the performance of both open-source and closed-source GUI agents.

- [GraphPilot: GUI Task Automation with One-Step LLM Reasoning Powered by Knowledge Graph](https://arxiv.org/abs/2601.17418)
    - Pengxiang Zhao, Yuxiang Chai, Haotian Zhao, Yiyuan Liu, Shuai Ren
    - 🏛️ Institutions: Sun Yat-sen University
    - 📅 Date: January 17, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile], [knowledge graph], [LLM], [task automation], [efficiency]
    - 📖 TLDR: GraphPilot constructs app-specific knowledge graphs offline to encode page functions, element roles, and transition rules, then uses these graphs to guide LLM reasoning online so that a mobile GUI agent can plan a complete action sequence in nearly one LLM query, improving task completion rate on DroidTask while substantially reducing latency and the number of LLM calls compared to stepwise approaches.

- [Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?](https://arxiv.org/abs/2601.12349)
    - Chenhao Lin, Zichen Ding, Lingming Zhang, Yuanchun Li, Xuanzhe Liu
    - 🏛️ Institutions: Nanjing University, Honor Device Co. Ltd, Institute of Dataspace Hefei Comprehensive National Science Center
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [security], [attack], [Android], [mobile], [benchmark], [LMM]
    - 📖 TLDR: This paper presents "Action Rebinding," a zero-permission attack that exploits the observation-to-action gap in LMM-powered Android GUI agents to hijack their actions, achieving 100% success on atomic rebinding across six agents and 15 tasks while evading all malware scanners, revealing a fundamental architectural flaw in current agent-OS integration.

- [AndroidLens: Long-latency Evaluation with Nested Sub-targets for Android GUI Agents](https://arxiv.org/abs/2512.21302)
    - Yue Cao, Yingyao Wang, Pi Bu...
    - 🏛️ Institutions: Nanjing University, Alibaba Group, Fudan University, Zhejiang University
    - 📅 Date: December 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [Android], [benchmark], [evaluation], [GUI testing], [mobile]
    - 📖 TLDR: AndroidLens is a challenging evaluation framework for Android GUI agents comprising 571 long-latency tasks across 38 domains in Chinese and English environments, featuring both static evaluation with multiple valid paths and dynamic milestone-based evaluation via Average Task Progress (ATP). Even the best models achieve only 12.7% task success rate and 50.47% ATP, highlighting key challenges in environmental anomalies, adaptive exploration, and long-term memory retention.

- [GUITester: Enabling GUI Agents for Exploratory Defect Discovery](https://arxiv.org/abs/2601.04500)
    - Yixuan Yue, Yiming Liu, Tao Xie, Yuanchun Li, Xuanzhe Liu
    - 🏛️ Institutions: Beijing Jiaotong University, Hithink Research, Nanyang Technological University
    - 📅 Date: December 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI testing], [mobile], [multi-agent], [benchmark], [defect detection], [MLLM]
    - 📖 TLDR: GUITester is a multi-agent framework that enables MLLM-based GUI agents to autonomously discover defects in mobile apps by decoupling navigation from verification through a Planning-Execution Module and a Hierarchical Reflection Module, achieving 48.90% F1-score on the newly introduced GUITestBench benchmark with 143 tasks across 26 defects.

- [Modular and Multi-Path-Aware Offline Benchmarking for Mobile GUI Agents](https://arxiv.org/abs/2512.12634)
    - Youngmin Im, Byeongung Jo, Jaeyoung Wi...
    - 🏛️ Institutions: KAIST, Sungkyunkwan University, Korea University, Fluiz
    - 📅 Date: December 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile], [Android], [benchmark], [evaluation], [modular], [multi-path]
    - 📖 TLDR: MobiBench is the first modular and multi-path-aware offline benchmarking framework for mobile GUI agents that achieves 94.72% agreement with human evaluators while enabling scalable, reproducible evaluation, and provides comprehensive module-level analysis uncovering optimal configurations and actionable design guidelines for mobile agents.

- [NaviMaster: Learning a Unified Policy for GUI and Embodied Navigation Tasks](https://arxiv.org/abs/2508.02046)
    - Zhihao Luo, Wentao Yan, Jingyu Gong, Min Wang, Zhizhong Zhang, Xuhong Wang, Yuan Xie, Xin Tan
    - 🏛️ Institutions: East China Normal University, Shanghai AI Laboratory, SenseTime Research
    - 📅 Date: August 04, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI navigation], [embodied navigation], [reinforcement learning], [unified agent], [mobile], [web]
    - 📖 TLDR: NaviMaster is the first unified agent that combines GUI navigation (mobile/web/desktop) and embodied navigation within a single reinforcement learning framework, using a visual-target trajectory collection pipeline and distance-aware reward to outperform state-of-the-art agents on out-of-domain benchmarks across both domains.

- [LLM-Guided Scenario-based GUI Testing](https://arxiv.org/abs/2506.05079)
    - Shengcheng Yu, Yuchen Ling, Chunrong Fang, Quan Zhou, Yi Zhao, Chunyang Chen, Shaomin Zhu, Zhenyu Chen
    - 🏛️ Institutions: Technical University of Munich, Nanjing University, Tongji University
    - 📅 Date: June 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [LLM], [GUI testing], [multi-agent], [mobile], [framework], [benchmark]
    - 📖 TLDR: ScenGen is an LLM-guided multi-agent framework for scenario-based mobile GUI testing that uses five collaborative agents (Observer, Decider, Executor, Supervisor, Recorder) to automate business-logic-driven test scenario completion, achieving higher relevance to app functionality than existing exploration-based approaches.

- [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, Renmin University of China, Xiaomi, Tsinghua University
    - 📅 Date: May 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile], [evaluation], [dataset], [GUI testing], [multimodal]
    - 📖 TLDR: Mobile-Bench-v2 is a more realistic benchmark for VLM-based mobile agents that introduces multi-path offline evaluation, noisy environments with pop-ups and ads, and ambiguous instruction splits to test proactive interaction capabilities, addressing key limitations of existing mobile agent benchmarks.

- [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337)
    - Longxi Gao, Li Zhang, Shihe Wang, Pengzhi Gao, Wei Liu, Jian Luan, Shangguang Wang, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [mobile], [Android], [GUI grounding], [data collection], [benchmark]
    - 📖 TLDR: MobileViews is a million-scale mobile GUI dataset comprising over 1.2 million screenshot-view hierarchy pairs from 30K+ Android apps, collected via an automated VLM-enhanced traversal framework on mobile SoC clusters, which improves GUI grounding accuracy by up to 6.1% when used to train visual language models.
