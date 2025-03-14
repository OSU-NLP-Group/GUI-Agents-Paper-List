# Kun Shao's Papers

- [VSC-RL: Advancing Autonomous Vision-Language Agents with Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, Univ. College London
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [subgoal generation], [VSC-RL], [learning efficiency]
    - 📖 TLDR: This paper introduces **VSC-RL**, a novel reinforcement learning framework that enhances learning efficiency for vision-language agents in complex sequential decision-making tasks. By reformulating these tasks as variational goal-conditioned problems, VSC-RL leverages advanced optimization techniques and utilizes vision-language models to autonomously decompose goals into feasible subgoals. Empirical results demonstrate that VSC-RL significantly outperforms state-of-the-art agents, particularly in challenging mobile device control tasks.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Univ. of Cambridge, Huawei Noah's Ark Lab, Univ. College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [evaluation], [AppVLM], [on-device control]
    - 📖 TLDR: This paper introduces **AppVLM**, a lightweight Vision-Language Model designed for efficient on-device control of smartphone applications. AppVLM is fine-tuned on the AndroidControl dataset and further refined through interactions within the AndroidWorld environment. It achieves superior action prediction accuracy in offline evaluations and matches GPT-4o in online task completion success rates, while operating up to ten times faster, making it a practical solution for real-world deployment.

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890)
    - Shuai Wang, Weiwen Liu, Jingxuan Chen, Weinan Gan, Xingshan Zeng, Shuai Yu, Xinlong Hao, Kun Shao, Yasheng Wang, Ruiming Tang
    - 🏛️ Institutions: Huawei Noah’s Ark Lab
    - 📅 Date: November 7, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This survey consolidates recent research on GUI agents powered by foundation models, particularly Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs). It discusses representative datasets and benchmarks, summarizes a unified framework capturing essential components from prior studies, and explores commercial applications. The paper identifies key challenges and proposes future research directions to inspire further developments in (M)LLM-based GUI agents.

- [Lightweight Neural App Control](https://arxiv.org/abs/2410.17883)
    - Filippos Christianos, Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, UCL
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [vision language model], [Action Transformer], [app agent], [Android control], [multi-modal]
    - 📖 TLDR: This paper introduces LiMAC, a mobile control framework for Android that integrates an Action Transformer and fine-tuned vision-language models to execute precise actions in mobile apps. Tested on open-source datasets, LiMAC improves action accuracy by up to 42% over traditional prompt engineering baselines, demonstrating enhanced efficiency and accuracy in mobile app control tasks.

- [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://ai-agents-2030.github.io/SPA-Bench/)
    - Jingxuan Chen, Derek Yuen, Bin Xie, Yuhao Yang, Gongwei Chen, Zhihao Wu, Li Yixing, Xurui Zhou, Weiwen Liu, Shuai Wang, Rui Shao, Liqiang Nie, Yasheng Wang, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, Harbin Institute of Technology, Shenzhen, UCL
    - 📅 Date: October 19, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [AI agent], [smartphone control], [framework]
    - 📖 TLDR: SPA-Bench is introduced as a benchmark designed to evaluate multimodal large language model (MLLM)-based smartphone agents, offering a task set that spans common smartphone functionalities across system and third-party applications. It includes a plug-and-play framework for real-time agent interactions on Android, integrating over ten agents with an adaptable evaluation pipeline measuring success across diverse metrics. Through this, the benchmark exposes challenges such as UI interpretation, action grounding, and memory retention in mobile environments, advancing research in smartphone-based agent applications.

- [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://ai-agents-2030.github.io/DistRL/)
    - Taiyi Wang, Zhihao Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Univ. of Cambridge, Huawei Noah's Ark Lab, Univ. College London
    - 📅 Date: October 18, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [distributed training], [A-RIDE], [on-device control]
    - 📖 TLDR: This paper introduces **DistRL**, a novel framework designed to enhance the efficiency of online reinforcement learning fine-tuning for mobile device control agents. DistRL employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in dynamic online interactions. The framework is supported by a custom RL algorithm, A-RIDE, which balances exploration with prioritized data utilization to ensure stable and robust training. Experiments demonstrate that DistRL improves training efficiency by 3× and accelerates data collection by 2.4× compared to leading synchronous multi-machine methods. Notably, after training, DistRL achieves a 20% relative improvement in success rate on general Android tasks from an open benchmark, outperforming existing approaches while maintaining the same training time.
