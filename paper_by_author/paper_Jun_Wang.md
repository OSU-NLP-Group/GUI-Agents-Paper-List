# Jun Wang's Papers

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
    - 💻 Env: [GUI]
    - 🔑 Key: [continual learning], [parameter fusion], [catastrophic forgetting], [geometric consensus], [Agent-Dice]
    - 📖 TLDR: Agent-Dice addresses the stability-plasticity dilemma in agent continual learning by separating shared knowledge from task-specific interference during parameter fusion. Its two-stage method combines geometric consensus filtering with curvature-based importance weighting, and the paper reports strong continual-learning results for both GUI and tool-use agents.

- [Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control](https://arxiv.org/abs/2509.01720)
    - Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, University College London
    - 📅 Date: September 01, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [off-policy reinforcement learning], [positive-sample updates], [negative-sample regularization], [successful transition replay], [AndroidWorld], [SoLS], [STR]
    - 📖 TLDR: SoLS is an off-policy RL algorithm for mobile app control that updates directly on successful samples but applies conservative regularized updates on negative ones to avoid policy degradation in sparse-reward settings. With Successful Transition Replay, it improves AndroidWorld performance substantially while using far less compute than GPT-4o-based baselines.

- [UI-Evol: Automatic Knowledge Evolving for Computer Use Agents](https://arxiv.org/abs/2505.21964)
    - Ziyun Zhang, Xinyi Liu, Xiaoyi Zhang, Jun Wang, Gang Chen, Yan Lu
    - 🏛️ Institutions: School of Software and Microelectronics, Peking University, Microsoft Research Asia
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [knowledge-execution gap], [critique stage], [retrace stage], [OSWorld], [self‑evolution]
    - 📖 TLDR: The paper identifies a “knowledge‑execution gap” where even highly accurate external knowledge (90%) only yields a 41% execution success rate. To bridge this, the authors introduce **UI‑Evol**, a plug‑and‑play two‑stage module for GUI agents—**Retrace** recovers actual action sequences from real agent–environment interactions, and **Critique** refines knowledge by comparing these sequences with external references. Experiments using Agent S2 on the OSWorld benchmark show significant gains in task performance and reduced behavioral variance, improving agent reliability.

- [Advancing Autonomous VLM Agents via Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [VLM agent], [subgoal-conditioned RL], [learning efficiency], [VSC-RL]
    - 📖 TLDR: This paper reformulates long-horizon VLM-agent training as a variational subgoal-conditioned reinforcement learning problem, introducing the SGC-ELBO objective to balance subgoal-conditioned return maximization against divergence from a reference policy. Across mobile and web control benchmarks, VSC-RL improves both learning efficiency and final performance over prior RL methods.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, University College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [lightweight VLM], [on-device control], [AndroidControl], [AndroidWorld], [AppVLM]
    - 📖 TLDR: AppVLM is a lightweight mobile-control VLM that is first fine-tuned offline on AndroidControl and then refined with data collected from AndroidWorld. It reaches state-of-the-art offline action prediction and matches GPT-4o on online AndroidWorld success rate while running up to 10x faster.

- [Lightweight Neural App Control](https://openreview.net/forum?id=BL4WBIfyrz)
    - Filippos Christianos, Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 23, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Mobile]
    - 🔑 Key: [LiMAC], [mobile control], [action transformer], [vision-language model]
    - 📖 TLDR: Introduces LiMAC, a lightweight neural framework for Android app control that combines an Action Transformer with fine-tuned vision-language models. The paper reports large gains over prompt-only baselines on mobile control benchmarks while keeping the control stack compact.

- [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9a75f4dd9679aa4ff80a4e6f0a1dc700-Abstract-Conference.html)
    - Jingxuan Chen, Derek Yuen, Bin Xie, Yuhao Yang, Gongwei Chen, Zhihao Wu, Li Yixing, Xurui Zhou, Weiwen Liu, Shuai Wang, Rui Shao, Liqiang Nie, Yasheng Wang, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, Harbin Institute of Technology, Shenzhen, University College London
    - 📅 Date: October 19, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [SPA-Bench], [smartphone agent evaluation], [Android interaction]
    - 📖 TLDR: Introduces SPA-Bench, a benchmark and evaluation stack for multimodal smartphone agents operating on Android system and third-party apps. It exposes persistent challenges in UI interpretation, action grounding, and memory over multi-step mobile tasks while providing a common plug-and-play evaluation framework.

- [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b9e472cd579c83e2f6aa3459f46aac28-Abstract-Conference.html)
    - Taiyi Wang, Zhihao Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 18, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [distributed training], [a-RIDE], [on-device control]
    - 📖 TLDR: This paper introduces **DistRL**, a novel framework designed to enhance the efficiency of online reinforcement learning fine-tuning for mobile device control agents. DistRL employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in dynamic online interactions. The framework is supported by a custom RL algorithm, A-RIDE, which balances exploration with prioritized data utilization to ensure stable and robust training. Experiments demonstrate that DistRL improves training efficiency by 3× and accelerates data collection by 2.4× compared to leading synchronous multi-machine methods. Notably, after training, DistRL achieves a 20% relative improvement in success rate on general Android tasks from an open benchmark, outperforming existing approaches while maintaining the same training time.
