# Papers with Keyword: mobile GUI agent

- [K²-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676)
    - Zhe Wu, Donglin Mo, Hongjin Lu, Junliang Xing, Jianheng Liu, Yuheng Jing, Kai Li, Kun Shao, Jianye Hao, Yuanchun Shi
    - 🏛️ Institutions: Tsinghua University, Huawei Noah's Ark Lab, Institute of Automation CAS
    - 📅 Date: February 28, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [hierarchical planning], [mobile GUI agent], [AndroidWorld], [K²-Agent]
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
    - 🔑 Key: [framework], [memory], [reinforcement learning], [online RL], [mobile GUI agent], [UI-Mem]
    - 📖 TLDR: This paper proposes UI-Mem, a mobile GUI agent training framework that augments online reinforcement learning with a hierarchical experience memory storing reusable workflows, subtask skills, and failure patterns. It introduces stratified group sampling to mix strong, weak, and unguided rollouts, plus a self-evolving loop that continually abstracts new successful plans and error diagnoses back into memory. Experiments on AndroidWorld and AndroidLab show strong gains over standard online RL and static reuse baselines, especially on unseen applications.

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

- [GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments?](https://arxiv.org/abs/2510.20333)
    - Chiyu Chen, Xinhao Song, Yunkai Chai, Yang Yao, Haodong Zhao, Lijun Li, Jie Li, Yan Teng, Gongshen Liu, Yingchun Wang
    - 🏛️ Institutions: Shanghai Jiao Tong University, School of Computer Science, Shanghai Artificial Intelligence Laboratory, The University of Hong Kong
    - 📅 Date: October 23, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [mobile GUI agent], [environmental injection], [adversarial robustness], [GhostEI-Bench]
    - 📖 TLDR: This paper introduces GhostEI-Bench, a benchmark for evaluating mobile agents under dynamic environmental injection attacks such as deceptive overlays, spoofed notifications, and pop-ups inside realistic Android workflows. Rather than testing static screenshots, it injects adversarial events into executable mobile environments and uses judge-based trajectory analysis to localize failure points. The benchmark shows that current mobile agents remain highly vulnerable to these runtime visual attacks.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Unaffiliated
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [mobile GUI agent], [GUI-Shift]
    - 📖 TLDR: This paper introduces GUI-Shift, a self-supervised reinforcement learning framework for VLM-based GUI agents built around the K-step GUI Transition task, which learns GUI dynamics from unlabeled trajectories without natural-language instruction annotation. The method combines rule-based optimization with data filtering and improves both GUI automation and grounding performance across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro. The paper shows a scalable path to training stronger mobile GUI agents from large amounts of unlabeled interaction data.

- [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119)
    - Yifan Xu, Xiao Liu, Xinghan Liu, Jiaqi Fu, Hanchen Zhang, Bohao Jing, Shudan Zhang, Yuting Wang, Wenyi Zhao, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Z.AI
    - 📅 Date: September 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [mobile GUI agent], [AndroidWorld], [AndroidLab], [MobileRL], [ADAGRPO]
    - 📖 TLDR: This paper introduces MobileRL, an online reinforcement learning framework for mobile GUI agents centered on the ADAGRPO algorithm for difficulty-adaptive replay, curriculum filtering, and reward shaping over multi-turn tasks. Applied to Qwen2.5-VL-7B-Instruct and GLM-4.1V-9B-Base, it improves sample efficiency and pushes performance to state-of-the-art success rates on both AndroidWorld and AndroidLab. The work is a focused training-framework contribution for strengthening open mobile agents rather than a new benchmark release.

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
