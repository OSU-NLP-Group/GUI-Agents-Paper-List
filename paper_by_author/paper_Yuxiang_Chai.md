# Yuxiang Chai's Papers

- [PIRA-Bench: A Transition from Reactive GUI Agents to GUI-based Proactive Intent Recommendation Agents](https://arxiv.org/abs/2603.08013)
    - Yuxiang Chai, Shunye Tang, Han Xiao, Rui Liu, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, Nankai University, Huawei Research
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [benchmark], [proactive recommendation], [intent inference], [continuous screenshots], [PIRF], [multithreaded trajectories]
    - 📖 TLDR: PIRA-Bench studies proactive GUI assistance, where an agent infers user intent from continuous visual streams instead of waiting for explicit commands. It focuses on long, noisy, interleaved trajectories with user-profile context, and introduces PIRF as a memory-aware baseline for proactive intent recommendation.

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: Multimedia Laboratory (MMLab), CUHK, vivo AI Lab, Princeton, Shenzhen Loop Area Institute, Shanghai AI Laboratory
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [memory], [reinforcement learning], [online RL], [hierarchical experience memory], [stratified group sampling], [UI-Mem]
    - 📖 TLDR: UI-Mem augments online RL for mobile GUI agents with a hierarchical experience memory that stores reusable workflows, subtask skills, and failure patterns as transferable templates. Its stratified group sampling lets the policy absorb memory-informed behavior and improves over standard online RL baselines.

- [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Qinyi Luo, Shunye Tang, Yuxiang Chai, Weifeng Lin, Han Xiao, WenHao Wang, Siheng Chen, Zhengxi Lu, Gao Wu, Hao Wang, Liang Liu, Yong Liu
    - 🏛️ Institutions: ZJU, Nankai University, CUHK, SJTU, vivo AI Lab
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
    - 🏛️ Institutions: ZJU, vivo AI Lab, CUHK MMLab, SJTU
    - 📅 Date: April 28, 2025
    - 📑 Publisher: TMLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [mobile automation], [training taxonomy], [benchmark taxonomy], [planning], [security]
    - 📖 TLDR: This survey reviews the development of LLM-powered mobile GUI agents for phone automation, from script-like systems to adaptive multimodal agents. It organizes the space around agent architectures, training approaches, datasets and benchmarks, and closes with open problems such as user adaptation, on-device efficiency, and security.

- [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, Shibo He, Wenchao Meng
    - 🏛️ Institutions: ZJU, vivo AI Lab
    - 📅 Date: April 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [few-shot learning], [LearnAct], [LearnGUI]
    - 📖 TLDR: LearnAct studies demonstration-based learning for mobile GUI agents rather than scaling generic pretraining alone. It introduces the LearnGUI dataset and benchmark for offline and online demonstration reuse, and uses a DemoParser-KnowSeeker-ActExecutor pipeline to extract, retrieve, and execute demonstration-derived knowledge in unseen mobile tasks.

- [UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Han Xiao, Shuai Ren, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, CUHK
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [reinforcement learning], [rule-based action reward], [GRPO], [UI-R1-3B], [AndroidControl], [ScreenSpot-pro]
    - 📖 TLDR: UI-R1 studies whether rule-based reinforcement learning can improve efficient GUI action prediction for multimodal mobile agents. It trains UI-R1-3B with GRPO on a curated set of 136 challenging mobile tasks using a rule-based action reward, and reports gains on ScreenSpot, ScreenSpot-Pro, and AndroidControl over the base model.

- [A3: Android Agent Arena for Mobile GUI Agents with Essential-State Procedural Evaluation](https://arxiv.org/abs/2501.01149)
    - Yuxiang Chai, Shunye Tang, Han Xiao, Weifeng Lin, Hanhao Li, Jiayu Zhang, Liang Liu, Pengxiang Zhao, Guangyi Liu, Guozhi Wang, Shuai Ren, Rongduo Han, Haining Zhang, Siyuan Huang, Hongsheng Li
    - 🏛️ Institutions: MMLab @ CUHK, EE department @ CUHK, vivo AI Lab, SJTU
    - 📅 Date: January 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [essential-state evaluation], [procedural evaluation], [reward model], [A3]
    - 📖 TLDR: A3 is a mobile GUI benchmark built from 100 tasks over 20 dynamic online Android apps to evaluate agents beyond static or offline settings. Its essential-state procedural evaluation uses MLLMs as reward models to verify both intermediate progress and final completion on real online apps.

- [AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents](https://aclanthology.org/2025.findings-acl.110/)
    - Yuxiang Chai, Siyuan Huang, Yazhe Niu, Han Xiao, Liang Liu, Guozhi Wang, Dingyu Zhang, Shuai Ren, Hongsheng Li
    - 🏛️ Institutions: MMLab @ CUHK, SJTU, vivo AI Lab
    - 📅 Date: July 03, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [mobile GUI control], [multi-level annotations], [element grounding], [GUI-action chains], [AMEX]
    - 📖 TLDR: AMEX is a mobile GUI-control dataset with over 104K high-resolution screenshots annotated at three levels: interactive element grounding, screen and element functionality descriptions, and instruction-action chains. The paper positions it as a supplementary training resource for generalist mobile agents and shows gains after fine-tuning SPHINX Agent on the collected annotations.
