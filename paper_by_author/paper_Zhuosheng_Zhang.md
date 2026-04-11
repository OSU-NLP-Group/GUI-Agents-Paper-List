# Zhuosheng Zhang's Papers

- [Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2602.11858)
    - Lai Wei, Liangbo He, Jun Lan, Lingzhong Dong, Yutong Cai, Siyuan Li, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Ant Group, Zhongguancun Academy, Shanghai Innovation Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [knowledge distillation], [fine-grained perception], [region-to-image distillation], [ZoomBench], [training data generation], [multimodal perception]
    - 📖 TLDR: This paper proposes Region-to-Image Distillation, which teaches a model to internalize zoom-in behavior without requiring explicit crop-and-reason inference at test time. It also introduces ZoomBench and shows stronger fine-grained perception on both perception and GUI-agent benchmarks.

- [Adaptive Milestone Reward for GUI Agents](https://arxiv.org/abs/2602.11524)
    - Congmin Zheng, Xiaoyun Mo, Xinbei Ma, Qiqiang Lin, Yin Zhao, Jiachen Zhu, Xingyu Lou, Jun Wang, Zhaoxiang Wang, Weiwen Liu, Zhuosheng Zhang, Yong Yu, Weinan Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [reward shaping], [credit assignment], [milestone reward], [ADMIRE], [AndroidWorld]
    - 📖 TLDR: ADMIRE is a reinforcement-learning reward design for GUI agents that distills adaptive, verifiable milestones from successful trajectories and pairs them with asymmetric credit assignment. It improves AndroidWorld performance by more than 10 absolute points and transfers to other RL algorithms and environments.

- [ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](https://arxiv.org/abs/2601.07262)
    - Jihong Wang, Jiamu Zhou, Weiming Zhang, Weiwen Liu, Zhuosheng Zhang, Xingyu Lou, Weinan Zhang, Huarong Deng, Jun Wang
    - 🏛️ Institutions: OPPO Research Institute, Shanghai Jiao Tong University
    - 📅 Date: January 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-in-the-loop], [knowledge adaptation], [progress summarization], [WebArena], [ColorBrowserAgent]
    - 📖 TLDR: ColorBrowserAgent targets site heterogeneity and long-horizon instability in web automation with two mechanisms: human-in-the-loop knowledge adaptation and progressive progress summarization. On WebArena it reaches 71.2% success, and the paper also reports transfer to WebChoreArena and gains in industrial deployment.

- [Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning](https://arxiv.org/abs/2601.03641)
    - Zheng Wu, Xingyu Lou, Xinbei Ma, Yansi Li, Weiwen Liu, Weinan Zhang, Jun Wang, Zhuosheng Zhang
    - 🏛️ Institutions: School of Computer Science, Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [parameter fusion], [catastrophic forgetting], [geometric consensus], [Agent-Dice]
    - 📖 TLDR: Agent-Dice addresses the stability-plasticity dilemma in agent continual learning by separating shared knowledge from task-specific interference during parameter fusion. Its two-stage method combines geometric consensus filtering with curvature-based importance weighting, and the paper reports strong continual-learning results for both GUI and tool-use agents.

- [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235)
    - Zehao Deng, Tianjie Ju, Zheng Wu, Zhuosheng Zhang, Gongshen Liu
    - 🏛️ Institutions: School of Computer Science and Technology, Soochow University, School of Computer Science, Shanghai Jiao Tong University
    - 📅 Date: November 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [multi-agent framework], [reinforcement learning], [long-horizon task planning], [state tracking], [task decomposition]
    - 📖 TLDR: This paper proposes CES, a multi-agent framework consisting of a Coordinator, Executor, and State Tracker, where high-level scheduling models are trained via execution-feedback reinforcement learning to improve long-horizon GUI automation by decoupling planning from low-level action execution.

- [Say One Thing, Do Another? Diagnosing Reasoning-Execution Gaps in VLM-Powered Mobile-Use Agents](https://arxiv.org/abs/2510.02204)
    - Lingzhong Dong, Ziqi Zhou, Shuaibo Yang, Haiyue Sheng, Pengzhou Cheng, Zongru Wu, Zheng Wu, Gongshen Liu, Zhuosheng Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Beijing Institute of Technology
    - 📅 Date: October 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reasoning-execution gap], [ground-truth alignment], [execution gap], [reasoning gap], [mobile evaluation], [GTA]
    - 📖 TLDR: This paper introduces Ground-Truth Alignment (GTA), a metric for checking whether a mobile agent's chain-of-thought implies the ground-truth action rather than only whether the final action is correct. Combined with Exact Match, the framework separates execution gaps from reasoning gaps and shows that execution gaps are common across mobile benchmarks even for larger VLM agents.

- [XBOUND: Exploring Capability Boundaries of Device-Control Agents at the State Level](https://arxiv.org/abs/2505.21279)
    - Shaoqing Zhang, Kehai Chen, Zhuosheng Zhang, Rumei Li, Rongxiang Weng, Yang Xiang, Liqiang Nie, Min Zhang
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Pengcheng Laboratory, Shanghai Jiao Tong University, Meituan
    - 📅 Date: May 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [evaluation], [device-control agent], [state-level evaluation], [Explore Metric], [OS-Atlas], [UI-TARS]
    - 📖 TLDR: XBOUND argues that instruction-level success is too coarse for device-control agents because each GUI state contains multiple actionable branches. It introduces a state-level evaluation framework and shows that current agents exhibit bimodal performance on instruction unification, that sub-7B models remain weak at state mastery, and that planning and grounding data contribute differently to performance.

- [GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents](https://arxiv.org/abs/2505.12842)
    - Zheng Wu, Pengzhou Cheng, Zongru Wu, Lingzhong Dong, Zhuosheng Zhang
    - 🏛️ Institutions: School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [out-of-distribution detection], [safety], [gaussian mixture model], [MLLM], [robustness]
    - 📖 TLDR: GEM proposes a Gaussian mixture model-based method for detecting out-of-distribution instructions in GUI agents by modeling input embedding distances, achieving a 23.70% average accuracy improvement over baselines across eight datasets spanning smartphones, computers, and web browsers.

- [Dynamic Planning for LLM-based Graphical User Interface Automation](https://aclanthology.org/2024.findings-emnlp.70/)
    - Shaoqing Zhang, Zhuosheng Zhang, Kehai Chen, Xinbei Ma, Muyun Yang, Tiejun Zhao, Min Zhang
    - 🏛️ Institutions: School of Computer Science and Technology, Harbin Institute of Technology, School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University
    - 📅 Date: October 01, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [dynamic planning], [D-PoT], [mobile GUI automation]
    - 📖 TLDR: Proposes Dynamic Planning of Thoughts (D-PoT), a mobile GUI automation method that updates plans using execution history and environmental feedback instead of relying on long static reasoning traces. The paper shows that this dynamic replanning setup substantially outperforms ReAct-style baselines on smartphone GUI tasks.

- [CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://aclanthology.org/2024.findings-acl.539)
    - Xinbei Ma, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: August 31, 2024
    - 📑 Publisher: Findings of ACL 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [smartphone automation], [comprehensive environment perception], [conditional action prediction], [CoCo-Agent]
    - 📖 TLDR: Presents CoCo-Agent, a smartphone GUI agent built around comprehensive environment perception and conditional action prediction. The paper reports strong gains on mobile GUI automation benchmarks such as AITW and META-GUI, showing that richer environment modeling improves action selection.

- [You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/abs/2309.11436)
    - Zhuosheng Zhang, Aston Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: September 20, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [multimodal agent], [chain-of-action], [Auto-GUI], [AITW]
    - 📖 TLDR: Presents Auto-GUI, a screenshot-only mobile GUI agent that avoids external environment parsing and app-specific APIs. Its key idea is chain-of-action prompting, which conditions on prior actions and future plans, and it demonstrates strong results on the AITW device-control benchmark.
