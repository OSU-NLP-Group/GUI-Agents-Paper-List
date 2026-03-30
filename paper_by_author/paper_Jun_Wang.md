# Jun Wang's Papers

- [ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](https://arxiv.org/abs/2601.07262)
    - Jihong Wang, Jiamu Zhou, Weiming Zhang, Weiwen Liu, Zhuosheng Zhang, Xingyu Lou, Weinan Zhang, Huarong Deng, Jun Wang
    - 🏛️ Institutions: OPPO Research Institute, Shanghai Jiao Tong University
    - 📅 Date: 2026-02-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [Web Agent], [Knowledge Evolution], [Human-in-the-Loop], [Long-Horizon Tasks], [WebArena], [Memory Management]
    - 📖 TLDR: ColorBrowserAgent is a knowledge-evolving web automation agent that tackles site heterogeneity and long-horizon instability through human-in-the-loop knowledge adaptation and knowledge-aligned progressive summarization, achieving 71.2% success rate on WebArena and strong performance on WebChoreArena and industrial deployment.

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

- [UI-Evol: Automatic Knowledge Evolving for Computer Use Agents](https://arxiv.org/abs/2505.21964)
    - Ziyun Zhang, Xinyi Liu, Xiaoyi Zhang, Jun Wang, Gang Chen, Yan Lu
    - 🏛️ Institutions: Peking University, Microsoft Research Asia
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [knowledge-execution gap], [Critique Stage], [Retrace Stage], [OSWorld], [self‑evolution]
    - 📖 TLDR: The paper identifies a “knowledge‑execution gap” where even highly accurate external knowledge (90%) only yields a 41% execution success rate. To bridge this, the authors introduce **UI‑Evol**, a plug‑and‑play two‑stage module for GUI agents—**Retrace** recovers actual action sequences from real agent–environment interactions, and **Critique** refines knowledge by comparing these sequences with external references. Experiments using Agent S2 on the OSWorld benchmark show significant gains in task performance and reduced behavioral variance, improving agent reliability.

- [ViMo: A Generative Visual GUI World Model for App Agents](https://arxiv.org/abs/2504.13936)
    - Dezhao Luo, Bohan Tang, Kang Li, Georgios Papoudakis, Jifei Song, Shaogang Gong, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Queen Mary University of London, University of Oxford, Huawei Noah's Ark Lab, University College London
    - 📅 Date: May 20, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [world model], [visual prediction], [mobile GUI agent], [long-horizon planning], [ViMo]
    - 📖 TLDR: This paper introduces ViMo, the first visual GUI world model for app agents that predicts future GUI observations directly as images rather than only as text descriptions. To handle the hard problem of rendering GUI text accurately, it separates graphic generation from text generation with a Symbolic Text Representation and dedicated predictors for each part. The generated future screens are then used to help agents compare action outcomes and make better long-horizon decisions in mobile apps.

- [VSC-RL: Advancing Autonomous Vision-Language Agents with Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [subgoal generation], [VSC-RL], [learning efficiency]
    - 📖 TLDR: This paper introduces **VSC-RL**, a novel reinforcement learning framework that enhances learning efficiency for vision-language agents in complex sequential decision-making tasks. By reformulating these tasks as variational goal-conditioned problems, VSC-RL leverages advanced optimization techniques and utilizes vision-language models to autonomously decompose goals into feasible subgoals. Empirical results demonstrate that VSC-RL significantly outperforms state-of-the-art agents, particularly in challenging mobile device control tasks.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Huawei Noah's Ark Lab, University College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [evaluation], [AppVLM], [on-device control]
    - 📖 TLDR: This paper introduces **AppVLM**, a lightweight Vision-Language Model designed for efficient on-device control of smartphone applications. AppVLM is fine-tuned on the AndroidControl dataset and further refined through interactions within the AndroidWorld environment. It achieves superior action prediction accuracy in offline evaluations and matches GPT-4o in online task completion success rates, while operating up to ten times faster, making it a practical solution for real-world deployment.

- [Lightweight Neural App Control](https://openreview.net/forum?id=BL4WBIfyrz)
    - Filippos Christianos, Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 23, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [vision language model], [Action Transformer], [app agent], [Android control], [multi-modal]
    - 📖 TLDR: This paper introduces LiMAC, a mobile control framework for Android that integrates an Action Transformer and fine-tuned vision-language models to execute precise actions in mobile apps. Tested on open-source datasets, LiMAC improves action accuracy by up to 42% over traditional prompt engineering baselines, demonstrating enhanced efficiency and accuracy in mobile app control tasks.

- [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9a75f4dd9679aa4ff80a4e6f0a1dc700-Abstract-Conference.html)
    - Jingxuan Chen, Derek Yuen, Bin Xie, Yuhao Yang, Gongwei Chen, Zhihao Wu, Li Yixing, Xurui Zhou, Weiwen Liu, Shuai Wang, Rui Shao, Liqiang Nie, Yasheng Wang, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, Harbin Institute of Technology, Shenzhen, University College London
    - 📅 Date: October 19, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [AI agent], [smartphone control], [framework]
    - 📖 TLDR: SPA-Bench is introduced as a benchmark designed to evaluate multimodal large language model (MLLM)-based smartphone agents, offering a task set that spans common smartphone functionalities across system and third-party applications. It includes a plug-and-play framework for real-time agent interactions on Android, integrating over ten agents with an adaptable evaluation pipeline measuring success across diverse metrics. Through this, the benchmark exposes challenges such as UI interpretation, action grounding, and memory retention in mobile environments, advancing research in smartphone-based agent applications.

- [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b9e472cd579c83e2f6aa3459f46aac28-Abstract-Conference.html)
    - Taiyi Wang, Zhihao Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 18, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [distributed training], [A-RIDE], [on-device control]
    - 📖 TLDR: This paper introduces **DistRL**, a novel framework designed to enhance the efficiency of online reinforcement learning fine-tuning for mobile device control agents. DistRL employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in dynamic online interactions. The framework is supported by a custom RL algorithm, A-RIDE, which balances exploration with prioritized data utilization to ensure stable and robust training. Experiments demonstrate that DistRL improves training efficiency by 3× and accelerates data collection by 2.4× compared to leading synchronous multi-machine methods. Notably, after training, DistRL achieves a 20% relative improvement in success rate on general Android tasks from an open benchmark, outperforming existing approaches while maintaining the same training time.
