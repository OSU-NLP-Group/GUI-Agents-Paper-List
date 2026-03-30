# Papers with Keyword: mobile GUI agent

- [UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience](https://arxiv.org/abs/2603.24533)
    - Zichuan Lin, Feiyu Liu, Yijun Yang, Jiafei Lyu, Yiming Gao
    - 🏛️ Institutions: Tencent
    - 📅 Date: March 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [reinforcement learning], [mobile GUI agent], [self-evolving], [AndroidWorld]
    - 📖 TLDR: UI-Voyager is a two-stage self-evolving mobile GUI agent that uses Rejection Fine-Tuning (RFT) for autonomous data-model co-evolution and Group Relative Self-Distillation (GRSD) to construct dense step-level supervision from successful trajectories at fork points, enabling a 4B model to achieve 81.0% Pass@1 on AndroidWorld, surpassing human-level performance without manual annotation.

- [K²-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676)
    - Zhe Wu, Donglin Mo, Hongjin Lu, Junliang Xing, Jianheng Liu, Yuheng Jing, Kai Li, Kun Shao, Jianye Hao, Yuanchun Shi
    - 🏛️ Institutions: Tsinghua University, Huawei Noah's Ark Lab, Institute of Automation CAS
    - 📅 Date: February 28, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [hierarchical planning], [mobile GUI agent], [AndroidWorld], [K²-agent]
    - 📖 TLDR: This paper introduces K²-Agent, a hierarchical mobile device control framework that separates declarative “know-what” reasoning from procedural “know-how” execution and co-evolves them during training. Its high-level module refines task knowledge through an SRLR loop, while the low-level executor is trained with curriculum-guided GRPO and dynamic demonstration injection. On AndroidWorld, K²-Agent reaches a new state of the art among open-source screenshot-only systems and also generalizes competitively to ScreenSpot-v2 and Android-in-the-Wild.

- [AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild](https://arxiv.org/abs/2602.11750)
    - Jiazheng Sun, Mingxuan Li, Yingying Zhang, Jiayang Niu, Yachen Wu, Ruihan Jin, Shuyu Lei, Pengrongrui Tan, Zongyu Zhang, Ruoyi Wang, Jiachen Yang, Boyu Yang, Jiacheng Liu, Xin Peng
    - 🏛️ Institutions: Fudan University, Jilin University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [mobile GUI agent], [agent-user interaction], [MUSE], [AmbiBench]
    - 📖 TLDR: This paper introduces AmbiBench, a mobile GUI agent benchmark designed to move beyond idealized one-shot instructions toward realistic intent alignment. It organizes tasks by instruction clarity, includes 240 tasks across 25 applications, and evaluates not only execution success but also interaction quality through the MUSE judge framework. The benchmark highlights how current mobile agents struggle when users are ambiguous or incomplete, and reframes mobile agent evaluation around bidirectional interaction rather than pure instruction following.

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, Princeton University, Shenzhen Loop Area Institute, Shanghai AI Lab
    - 📅 Date: February 5, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [memory], [reinforcement learning], [online RL], [mobile GUI agent], [UI-mem]
    - 📖 TLDR: This paper proposes UI-Mem, a mobile GUI agent training framework that augments online reinforcement learning with a hierarchical experience memory storing reusable workflows, subtask skills, and failure patterns. It introduces stratified group sampling to mix strong, weak, and unguided rollouts, plus a self-evolving loop that continually abstracts new successful plans and error diagnoses back into memory. Experiments on AndroidWorld and AndroidLab show strong gains over standard online RL and static reuse baselines, especially on unseen applications.

- [M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining](https://arxiv.org/abs/2602.05429)
    - Rui Lv, Juncheng Mo, Tianyi Chu, Yiming Liu, Hongling Zhuo
    - 🏛️ Institutions: Ant Group, Zhejiang University
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile GUI agent], [data mining], [monte carlo tree search], [multi-agent framework], [trajectory annotation], [training data]
    - 📖 TLDR: M2-Miner is an automated mobile GUI agent data-mining framework that uses Monte Carlo Tree Search enhanced by a collaborative multi-agent system (InferAgent, OrchestraAgent, JudgeAgent) to efficiently generate high-quality intent-trajectory training data, along with intent recycling and progressive model-in-the-loop training strategies. GUI agents fine-tuned on the mined data achieve state-of-the-art performance on multiple mobile GUI benchmarks.

- [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Shun Zhang, Yiming Liu
    - 🏛️ Institutions: Zhejiang University, Nankai University, The Chinese University of Hong Kong, Shanghai Jiao Tong University, vivo AI Lab
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [memory], [evaluation], [mobile GUI agent], [framework]
    - 📖 TLDR: MemGUI-Bench is a comprehensive memory-centric benchmark for mobile GUI agents featuring 128 tasks across 26 applications where 89.8% require memory through cross-temporal and cross-spatial retention, along with MemGUI-Eval, a progressive scrutiny evaluation pipeline with 7 hierarchical metrics. Evaluation of 11 state-of-the-art agents reveals significant memory deficits with 4-10x capability gaps hidden by standard benchmarks, identifying 5 distinct failure modes and design implications.

- [Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training](https://arxiv.org/abs/2601.22781)
    - Linjia Kang, Zhimin Wang, Yongkang Zhang, Yuanchun Li, Gang Yin
    - 🏛️ Institutions: Tsinghua University, Huazhong Agricultural University, Kuaishou Technology
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile GUI agent], [data generation], [curriculum learning], [multi-agent], [VLM], [training data]
    - 📖 TLDR: MobileGen is an adaptive data generation framework for mobile GUI agent training that decouples task difficulty into structural and semantic dimensions, profiles the agent's capability frontier, and uses a multi-agent controllable generator to synthesize difficulty-aligned interaction trajectories, improving average agent performance by 1.57x over baselines across multiple benchmarks.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence Renmin University of China, MiLM Plus Xiaomi Inc., Institute for AI Industry Research Tsinghua University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile GUI agent], [multi-path evaluation], [ambiguous instruction], [noisy environment], [SMAN-bench]
    - 📖 TLDR: This paper introduces SMAN-Bench, a mobile-agent benchmark that moves beyond single golden trajectories by evaluating single-path, multi-path, ambiguous, and noisy task settings in one framework. It builds instructions from an existing graph-structured mobile corpus, adds offline multi-path reward evaluation, and explicitly includes noisy pop-up-heavy environments plus clarification-style ambiguous tasks. The benchmark is designed to better reflect realistic mobile-agent deployment conditions than cleaner or purely online settings.

- [MobileDreamer: Generative Sketch World Model for GUI Agent](https://arxiv.org/abs/2601.04035)
    - Yilin Cao, Yufeng Zhong, Zhixiong Zeng, Liming Zheng, Jing Huang, Haibo Qiu, Peng Shi, Wenji Mao, Wan Guanglu
    - 🏛️ Institutions: CAS, UCAS, Meituan
    - 📅 Date: January 7, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [planning], [lookahead], [mobile GUI agent], [MobileDreamer]
    - 📖 TLDR: This paper introduces MobileDreamer, a world-model-based lookahead framework for mobile GUI agents that predicts compact task-relevant future interface sketches rather than full screenshots. Its textual sketch world model preserves spatial information while remaining efficient, and its rollout imagination strategy uses these predicted futures to improve action selection on long-horizon tasks. On AndroidWorld, MobileDreamer achieves state-of-the-art performance and improves task success by 5.25%, showing that lightweight future imagination can materially strengthen mobile GUI planning.

- [MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive, and MCP-Augmented Environments](https://arxiv.org/abs/2512.19432)
    - Quyu Kong, Xu Zhang, Zhenyu Yang, Nolan Gao, Chen Liu, Panrong Tong, Chenglin Cai, Hanzhang Zhou, Jianan Zhang, Liangyu Chen, Zhidan Liu, Steven Hoi, Yue Wang
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group, HKUST(GZ), University of Florida
    - 📅 Date: December 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile GUI agent], [agent-user interaction], [MCP], [cross-app tasks], [MobileWorld]
    - 📖 TLDR: This paper introduces MobileWorld, a more realistic mobile-use benchmark designed to go beyond AndroidWorld by adding longer cross-application tasks, agent-user interaction, and MCP-augmented tool use. It contains 201 tasks across 20 applications with deterministic evaluation backed by snapshots, backend inspection, local storage checks, and callback APIs. Results show a steep performance drop relative to AndroidWorld, highlighting that current mobile GUI agents still struggle substantially with clarification dialogue and hybrid GUI-plus-tool workflows.

- [SmartSnap: Proactive Evidence Seeking for Self-Verifying Agents](https://arxiv.org/abs/2512.22322)
    - Yuncong Zhang, Jiahao Wu, Chenxu Wang, Ziming Liu, Ang Lv
    - 🏛️ Institutions: Tencent Youtu Lab, Peking University
    - 📅 Date: December 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [framework], [mobile GUI agent], [evaluation], [model], [benchmark]
    - 📖 TLDR: SmartSnap introduces a paradigm shift from passive post-hoc task verification to proactive in-situ self-verification for GUI agents, where a Self-Verifying Agent both completes tasks and proves accomplishment through curated snapshot evidence guided by 3C Principles (Completeness, Conciseness, Creativity), achieving up to 26% performance gains on mobile tasks with 8B-30B models competitive with much larger models like DeepSeek V3.1 and Qwen3-235B.

- [GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments?](https://arxiv.org/abs/2510.20333)
    - Chiyu Chen, Xinhao Song, Yunkai Chai, Yang Yao, Haodong Zhao, Lijun Li, Jie Li, Yan Teng, Gongshen Liu, Yingchun Wang
    - 🏛️ Institutions: Shanghai Jiao Tong University, School of Computer Science, Shanghai Artificial Intelligence Laboratory, The University of Hong Kong
    - 📅 Date: October 23, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [mobile GUI agent], [environmental injection], [adversarial robustness], [GhostEI-bench]
    - 📖 TLDR: This paper introduces GhostEI-Bench, a benchmark for evaluating mobile agents under dynamic environmental injection attacks such as deceptive overlays, spoofed notifications, and pop-ups inside realistic Android workflows. Rather than testing static screenshots, it injects adversarial events into executable mobile environments and uses judge-based trajectory analysis to localize failure points. The benchmark shows that current mobile agents remain highly vulnerable to these runtime visual attacks.

- [CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs](https://arxiv.org/abs/2510.15455)
    - Gucongcong Fan, Chaoyue Niu, Chengfei Lyu, Fan Wu, Guihai Chen
    - 🏛️ Institutions: Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: October 17, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [privacy], [mobile GUI agent], [cloud-local collaboration], [UI exposure reduction], [CORE]
    - 📖 TLDR: This paper studies privacy leakage in mobile agents that repeatedly upload full-screen UI context to cloud LLMs for planning and action selection. It proposes CORE, a collaborative framework where local and cloud LLMs split planning and decision-making through layout-aware block partitioning, co-planning, and co-decision, so only a smaller relevant UI subset is exposed upstream. On diverse mobile apps and tasks, CORE cuts UI exposure by up to 55.6% while keeping task success close to cloud-only agents.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Unaffiliated
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [mobile GUI agent], [GUI-shift]
    - 📖 TLDR: This paper introduces GUI-Shift, a self-supervised reinforcement learning framework for VLM-based GUI agents built around the K-step GUI Transition task, which learns GUI dynamics from unlabeled trajectories without natural-language instruction annotation. The method combines rule-based optimization with data filtering and improves both GUI automation and grounding performance across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro. The paper shows a scalable path to training stronger mobile GUI agents from large amounts of unlabeled interaction data.

- [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119)
    - Yifan Xu, Xiao Liu, Xinghan Liu, Jiaqi Fu, Hanchen Zhang, Bohao Jing, Shudan Zhang, Yuting Wang, Wenyi Zhao, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Z.AI
    - 📅 Date: September 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [mobile GUI agent], [AndroidWorld], [AndroidLab], [MobileRL], [ADAGRPO]
    - 📖 TLDR: This paper introduces MobileRL, an online reinforcement learning framework for mobile GUI agents centered on the ADAGRPO algorithm for difficulty-adaptive replay, curriculum filtering, and reward shaping over multi-turn tasks. Applied to Qwen2.5-VL-7B-Instruct and GLM-4.1V-9B-Base, it improves sample efficiency and pushes performance to state-of-the-art success rates on both AndroidWorld and AndroidLab. The work is a focused training-framework contribution for strengthening open mobile agents rather than a new benchmark release.

- [Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control](https://arxiv.org/abs/2509.01720)
    - Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: September 1, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [mobile GUI agent], [sample efficiency], [AndroidWorld], [SoLS]
    - 📖 TLDR: This paper introduces SoLS, an off-policy reinforcement learning algorithm for mobile app control that treats successful and unsuccessful samples differently to improve stability and sample efficiency. It also adds Successful Transition Replay to focus learning on successful interactions. On AndroidWorld, the method substantially outperforms prior prompt-based and RL baselines while using much less computation than large proprietary agents.

- [MobileUse: A GUI Agent with Hierarchical Reflection for Autonomous Mobile Operation](https://arxiv.org/abs/2507.16853)
    - Ning Li, Xiangmou Qu, Jiamu Zhou, Jun Wang, Muning Wen, Kounianhua Du, Xingyu Lou, Qiuying Peng, Jun Wang, Weinan Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: July 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [mobile GUI agent], [hierarchical reflection], [proactive exploration], [AndroidWorld], [AndroidLab], [MobileUse]
    - 📖 TLDR: This paper introduces MobileUse, a mobile GUI agent designed to handle long-horizon execution, error recovery, and cold-start operation in unfamiliar apps. Its core design combines hierarchical reflection across multiple temporal scales with a reflection-on-demand strategy and proactive exploration to build environment understanding before acting. The result sets new state-of-the-art success rates on AndroidWorld and AndroidLab and is released with a toolkit for execution on physical mobile devices.

- [FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://arxiv.org/abs/2507.21071)
    - Qinglong Yang, Haoming Li, Haotian Zhao, Xiaokai Yan, Jingtao Ding, Fengli Xu, Yong Li
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: June 9, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile GUI agent], [proactive assistance], [personalization], [FingerTip 20K]
    - 📖 TLDR: This paper introduces FingerTip 20K, a mobile-agent benchmark built from long-term real-life Android demonstrations that emphasizes proactive task suggestion and personalized execution rather than only instruction-following. It contributes 20K user episodes with contextual and historical signals, then shows that current mobile LLM agents still perform far below humans on these user-oriented settings. Fine-tuning on the collected data substantially improves the use of user context and preferences.

- [Agent-SAMA: State-Aware Mobile Assistant](https://arxiv.org/abs/2505.23596)
    - Linqiang Guo, Wei Liu, Yi Wen Heng, Tse-Hsun, Chen, Yang Wang
    - 🏛️ Institutions: Concordia University
    - 📅 Date: 2025-05-29
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile GUI agent], [multi-agent framework], [finite state machine], [error recovery], [Android], [benchmark]
    - 📖 TLDR: Agent-SAMA is a state-aware multi-agent framework that models mobile app execution as a Finite State Machine (FSM), using four specialized agents to collaboratively construct FSMs in real time for task planning, execution verification, and error recovery, achieving up to 84% task success rate and 71.9% recovery rate on cross-app benchmarks.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reward model], [self-improvement], [synthetic data], [mobile GUI agent], [UI-genie-RM], [UI-genie-agent]
    - 📖 TLDR: This paper introduces UI-Genie, a self-improving mobile GUI-agent framework that tackles two bottlenecks at once: outcome verification and scalable high-quality trajectory generation. It builds a dedicated reward model, UI-Genie-RM, plus a reward-guided self-improvement loop that iteratively upgrades both the agent and the reward model in dynamic environments. The paper also releases the first reward-specific GUI-agent dataset and reports state-of-the-art performance across multiple mobile GUI benchmarks after several generations of self-improvement.

- [ViMo: A Generative Visual GUI World Model for App Agents](https://arxiv.org/abs/2504.13936)
    - Dezhao Luo, Bohan Tang, Kang Li, Georgios Papoudakis, Jifei Song, Shaogang Gong, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Queen Mary University of London, University of Oxford, Huawei Noah's Ark Lab, University College London
    - 📅 Date: May 20, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [world model], [visual prediction], [mobile GUI agent], [long-horizon planning], [ViMo]
    - 📖 TLDR: This paper introduces ViMo, the first visual GUI world model for app agents that predicts future GUI observations directly as images rather than only as text descriptions. To handle the hard problem of rendering GUI text accurately, it separates graphic generation from text generation with a Symbolic Text Representation and dedicated predictors for each part. The generated future screens are then used to help agents compare action outcomes and make better long-horizon decisions in mobile apps.

- [MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation](https://aclanthology.org/2025.naacl-demo.43/)
    - Zichen Zhu, Hao Tang, Yansi Li, Dingye Liu, Hongshen Xu, Kunyao Lan, Danyang Zhang, Yixuan Jiang, Hao Zhou, Chenrun Wang, Situo Zhang, Liangtai Sun, Yixiao Wang, Yuheng Sun, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, Department of Computer Science and Engineering, MoE Key Lab of Artificial Intelligence, SJTU AI Institute, Shanghai Jiao Tong University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [memory], [adaptive planning], [mobile GUI agent], [MobBench], [MobA]
    - 📖 TLDR: This paper presents MobA, a mobile assistant system built for complex GUI interaction under changing page contexts and limited executor capability. Its core contributions are an adaptive planning module with reflection-based recovery and a multifaceted memory module that supports dynamic execution. The paper also introduces MobBench and reports strong results on both MobBench and AndroidArena for complex mobile task automation.

- [ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation](https://aclanthology.org/2025.naacl-long.244/)
    - Qinzhuo Wu, Wei Liu, Jian Luan, Bin Wang
    - 🏛️ Institutions: XiaoMi AI Lab
    - 📅 Date: April 2025
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile GUI agent], [page reaching], [task decomposition], [ReachAgent], [MobileReach]
    - 📖 TLDR: This paper argues that mobile agents often optimize locally for the next UI action while missing the larger GUI flow needed to finish a task. It introduces MobileReach, a dataset that decomposes tasks into page-reaching and page-operation subtasks, and trains ReachAgent as a two-stage framework over those subtasks plus reward-based preference flows. The result is stronger step-level and task-level accuracy than prior mobile-agent baselines.
