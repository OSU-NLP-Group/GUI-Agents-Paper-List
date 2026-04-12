# Kun Shao's Papers

- [K²-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676)
    - Zhe Wu, Donglin Mo, Hongjin Lu, Junliang Xing, Jianheng Liu, Yuheng Jing, Kai Li, Kun Shao, Jianye Hao, Yuanchun Shi
    - 🏛️ Institutions: Department of Computer Science and Technology, Tsinghua University, Huawei Noah’s Ark Lab, Institute of Automation, Chinese Academy of Sciences
    - 📅 Date: February 28, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [hierarchical control], [declarative knowledge], [procedural knowledge], [SRLR], [C-GRPO], [K²-Agent]
    - 📖 TLDR: K²-Agent separates mobile control into a high-level declarative reasoner and a low-level procedural executor, then co-evolves both through self-refinement and curriculum-guided RL. The design reaches 76.1% on AndroidWorld and transfers well to ScreenSpot-v2 and AITW.

- [Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control](https://arxiv.org/abs/2509.01720)
    - Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, University College London
    - 📅 Date: September 01, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [off-policy reinforcement learning], [positive-sample updates], [negative-sample regularization], [successful transition replay], [AndroidWorld], [SoLS], [STR]
    - 📖 TLDR: SoLS is an off-policy RL algorithm for mobile app control that updates directly on successful samples but applies conservative regularized updates on negative ones to avoid policy degradation in sparse-reward settings. With Successful Transition Replay, it improves AndroidWorld performance substantially while using far less compute than GPT-4o-based baselines.

- [Advancing Autonomous VLM Agents via Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Liverpool, University of Southampton, Huawei Noah's Ark Lab, Tianjin University, University College London
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [reinforcement learning], [subgoal-conditioned RL], [SGC-ELBO], [learning efficiency], [VSC-RL]
    - 📖 TLDR: This paper reformulates long-horizon VLM-agent training as a variational subgoal-conditioned reinforcement learning problem with the SGC-ELBO objective. Across mobile-device and web-control benchmarks, VSC-RL improves both learning efficiency and final performance over prior RL methods.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, University College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [lightweight VLM], [offline-to-online training], [AndroidControl], [AndroidWorld], [AppVLM]
    - 📖 TLDR: AppVLM is a lightweight vision-language model for mobile app control that is trained first on AndroidControl and then refined with trajectories collected in AndroidWorld. It achieves the best offline action prediction among the compared baselines and matches GPT-4o on online AndroidWorld success rate while running much faster.

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890)
    - Shuai Wang, Weiwen Liu, Jingxuan Chen, Yuqi Zhou, Weinan Gan, Xingshan Zeng, Yuhan Che, Shuai Yu, Xinlong Hao, Kun Shao, Bin Wang, Chuhan Wu, Yasheng Wang, Ruiming Tang, Jianye Hao
    - 🏛️ Institutions: Huawei Noah's Ark Lab
    - 📅 Date: November 07, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [foundation models], [taxonomy], [industrial applications]
    - 📖 TLDR: This survey organizes foundation-model GUI agents around data resources, agent construction, taxonomy, and industrial applications. It also summarizes open challenges around the benchmark-reality gap, agent self-evolution, and inference efficiency.

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
