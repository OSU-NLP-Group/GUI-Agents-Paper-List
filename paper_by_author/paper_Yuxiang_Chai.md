# Yuxiang Chai's Papers

- [PIRA-Bench: A Transition from Reactive GUI Agents to GUI-based Proactive Intent Recommendation Agents](https://arxiv.org/abs/2603.08013)
    - Yuxiang Chai, Shunye Tang, Han Xiao, Rui Liu, Hongsheng Li
    - 🏛️ Institutions: The Chinese University of Hong Kong (MMLab @ CUHK), Nankai University, Huawei Research
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [benchmark], [proactive recommendation], [intent inference], [continuous screenshots], [PIRF], [multithreaded trajectories]
    - 📖 TLDR: PIRA-Bench studies proactive GUI assistance, where an agent infers user intent from continuous visual streams instead of waiting for explicit commands. It focuses on long, noisy, interleaved trajectories with user-profile context, and introduces PIRF as a memory-aware baseline for proactive intent recommendation.

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: Multimedia Laboratory (MMLab), The Chinese University of Hong Kong, vivo AI Lab, Princeton University, Shenzhen Loop Area Institute, Shanghai AI Lab
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [memory], [reinforcement learning], [online RL], [hierarchical experience memory], [stratified group sampling], [UI-Mem]
    - 📖 TLDR: UI-Mem augments online RL for mobile GUI agents with a hierarchical experience memory that stores reusable workflows, subtask skills, and failure patterns as transferable templates. Its stratified group sampling lets the policy absorb memory-informed behavior and improves over standard online RL baselines.

- [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Qinyi Luo, Shunye Tang, Yuxiang Chai, Weifeng Lin, Han Xiao, WenHao Wang, Siheng Chen, Zhengxi Lu, Gao Wu, Hao Wang, Liang Liu, Yong Liu
    - 🏛️ Institutions: Zhejiang University, Nankai University, The Chinese University of Hong Kong, Shanghai Jiao Tong University, vivo AI Lab
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [memory], [evaluation], [MemGUI-Eval], [MemGUI-Bench]
    - 📖 TLDR: MemGUI-Bench is a memory-focused benchmark for mobile GUI agents covering dynamic tasks that require cross-temporal and cross-spatial retention. Paired with MemGUI-Eval, it reveals large hidden memory deficits in current agents that standard benchmarks miss.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [reward model], [self-improvement], [outcome verification], [UI-Genie]
    - 📖 TLDR: UI-Genie targets two mobile-agent bottlenecks: reliable outcome verification and scalable high-quality training data. It combines an interleaved reward model with a reward-guided self-improvement loop, releases reward-specific GUI datasets, and reports stronger mobile-agent performance across multiple rounds of self-improvement.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, WenHao Wang, Tianze Wu, Zhengxi Lu, Siheng Chen, LiLinghao, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab, CUHK MMLab, Shanghai Jiao Tong University
    - 📅 Date: April 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [framework], [dataset], [benchmark], [planning], [multimodal], [taxonomy]
    - 📖 TLDR: This comprehensive survey examines the evolution of LLM-powered GUI agents in mobile phone automation, transitioning from static scripts to intelligent, adaptive systems. It presents a taxonomy encompassing agent frameworks (single-agent, multi-agent, plan-then-act), modeling approaches (prompt engineering, training-based), and essential datasets and benchmarks. The paper discusses how LLMs enhance language understanding, multimodal perception, and decision-making in GUI tasks, and addresses challenges such as dataset diversity, on-device deployment efficiency, user-centric adaptation, and security concerns. It serves as a definitive reference for researchers and practitioners aiming to leverage LLMs in designing scalable, user-friendly phone GUI agents.

- [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, Shibo He, Wenchao Meng
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab
    - 📅 Date: April 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [few-shot learning], [LearnAct], [LearnGUI]
    - 📖 TLDR: Presents LearnAct, a mobile GUI framework built around few-shot demonstration learning rather than large generic pretraining alone. The paired LearnGUI benchmark studies how human demonstrations can be parsed, retrieved, and reused to improve task completion in unseen mobile scenarios.

- [UI-R1: Enhancing Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, The Chinese University of Hong Kong
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [UI-R1-3B], [GRPO], [AndroidControl], [ScreenSpot-pro]
    - 📖 TLDR: Explores whether R1-style rule-based reinforcement learning can improve multimodal GUI action prediction with very little data. UI-R1 uses a unified action reward and only 136 high-quality mobile tasks to train UI-R1-3B with GRPO, yielding large gains on AndroidControl, ScreenSpot, and ScreenSpot-Pro relative to the base model.

- [A3: Android Agent Arena for Mobile GUI Agents with Essential-State Procedural Evaluation](https://arxiv.org/abs/2501.01149)
    - Yuxiang Chai, Shunye Tang, Han Xiao, Weifeng Lin, Hanhao Li, Jiayu Zhang, Liang Liu, Pengxiang Zhao, Guangyi Liu, Guozhi Wang, Shuai Ren, Rongduo Han, Haining Zhang, Siyuan Huang, Hongsheng Li
    - 🏛️ Institutions: MMLab at The Chinese University of Hong Kong, EE Department at The Chinese University of Hong Kong, vivo AI Lab, Shanghai Jiao Tong University
    - 📅 Date: January 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [Android], [essential-state evaluation], [reward model], [A3]
    - 📖 TLDR: A3 is a mobile GUI benchmark built around 100 tasks in 20 dynamic online Android apps, targeting the gap between offline/static evaluation and real mobile use. Its essential-state procedural evaluation uses MLLMs as reward models to verify intermediate progress and task completion on real online apps.

- [AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents](https://aclanthology.org/2025.findings-acl.110/)
    - Yuxiang Chai, Siyuan Huang, Yazhe Niu, Han Xiao, Liang Liu, Guozhi Wang, Dingyu Zhang, Shuai Ren, Hongsheng Li
    - 🏛️ Institutions: The Chinese University of Hong Kong, Shanghai Jiao Tong University, Shanghai AI Laboratory, vivo AI Lab
    - 📅 Date: July 03, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [AMEX], [multi-annotation], [mobile GUI control]
    - 📖 TLDR: Introduces AMEX, a large-scale dataset for mobile GUI-control agents with over 104K screenshots from 110 apps and three levels of supervision: interactive element grounding, functionality descriptions, and instruction-action chains. The dataset is designed to support more capable generalist mobile agents than prior single-annotation resources.
