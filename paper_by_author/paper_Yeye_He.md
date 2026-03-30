# Yeye He's Papers

- [SecAgent: Efficient Mobile GUI Agent with Semantic Context](https://arxiv.org/abs/2603.08533)
    - Yanyang Li, Kaizhe Hu, Guohao Li, Heyang Gong, Yeye He
    - 🏛️ Institutions: Alibaba Group
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI Agent], [Mobile], [Efficiency], [Dataset], [Benchmark], [Reinforcement Learning]
    - 📖 TLDR: SecAgent is a 3B-scale mobile GUI agent that introduces a semantic context mechanism to distill history screenshots into concise natural language summaries, reducing computational costs while preserving task-relevant information. It also contributes a large-scale human-verified Chinese mobile GUI dataset (18k grounding samples, 121k navigation steps) and benchmark, achieving performance comparable to 7B-8B models through supervised and reinforcement fine-tuning.

- [Generalization in Online Reinforcement Learning for Mobile Agents](https://arxiv.org/abs/2603.07432)
    - Mingkai Deng, Jing Yu, Zhou Yu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Mila, Concordia University, Universite de Montreal, University of Toronto, McMaster University
    - 📅 Date: March 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI Agent], [Mobile Agent], [Reinforcement Learning], [Benchmark], [Generalization], [Android]
    - 📖 TLDR: Introduces AndroidWorld-Generalization, a benchmark for evaluating zero-shot generalization of GUI-based mobile agents across unseen task instances, templates, and applications, and proposes an open-source RL training system using GRPO that shows RL outperforms supervised fine-tuning but reveals significant challenges in generalizing to unseen templates and apps.

- [WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces](https://arxiv.org/abs/2603.05295)
    - Xiao Liu, Ziyang Luo, Jiawei Liu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Fudan University, IMean AI
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [Web Agent], [Dataset], [Benchmark], [Grounding], [Training Data], [Multimodal]
    - 📖 TLDR: WebChain is the largest open-source dataset of 31,725 human-annotated web interaction trajectories (318k steps) on real-world websites, featuring triple-aligned visual, structural, and action data. Leveraging this dataset, the authors propose a Dual Mid-Training recipe that decouples spatial grounding from planning, achieving state-of-the-art performance on their WebChainBench and other public GUI benchmarks.

- [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)
    - Xiao Liu, Ziyang Luo, Jiawei Liu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Fudan University, IMean AI, The Chinese University of Hong Kong, Tsinghua University
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [Web Agent], [Reinforcement Learning], [GUI Agent], [Synthetic Data], [Environment Synthesis], [Knowledge Distillation]
    - 📖 TLDR: WebFactory introduces a fully automated closed-loop reinforcement learning pipeline that compresses LLM-encoded internet knowledge into grounded GUI web agents through scalable environment synthesis, knowledge-aware task generation, and decomposed reward RL training, achieving performance comparable to agents trained on human-annotated data while using synthetic data from only 10 websites.

- [ShowUI-Aloha: Human-Taught GUI Agent](https://arxiv.org/abs/2601.07181)
    - Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu, Zihan Ding
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: December 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI Agent], [Learning from Demonstration], [Screen Recording], [Data Pipeline], [Desktop Automation], [Human Teaching]
    - 📖 TLDR: ShowUI-Aloha presents a pipeline that transforms unstructured, in-the-wild human screen recordings from desktop environments into structured, actionable training data for GUI agents, comprising a recorder, learner, planner, and executor that together enable agents to learn complex GUI tasks by simply observing humans.

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu, Zihan Ding
    - 🏛️ Institutions: The Ohio State University, Microsoft Research
    - 📅 Date: December 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI Grounding], [GUI Agent], [Dataset], [Benchmark], [Text Dragging], [Multimodal LLM]
    - 📖 TLDR: This paper introduces GUI-Drag, a 161K-example dataset for text dragging in GUIs, and ScreenDrag, a benchmark with 5,333 examples, extending GUI grounding beyond click-only actions to support drag-based text selection and manipulation while maintaining click performance.

- [InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](https://arxiv.org/abs/2601.04126)
    - Yiming Liu, Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu
    - 🏛️ Institutions: Peking University, Nanjing University, Microsoft Research Asia
    - 📅 Date: December 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [Web Agent], [Data Generation], [Training], [Benchmark], [GUI Grounding], [Framework]
    - 📖 TLDR: InfiniteWeb is a system that automatically synthesizes functional, diverse web environments at scale for GUI agent training, using unified specifications, task-centric test-driven development, and reference design images; agents trained on these generated environments achieve significant improvements on OSWorld and Online-Mind2Web benchmarks.

- [Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning](https://arxiv.org/abs/2601.03641)
    - Yiming Liu, Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: December 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI Agent], [Continual Learning], [Parameter Fusion], [Catastrophic Forgetting], [LLM Agent], [Tool-Use Agent]
    - 📖 TLDR: Agent-Dice is a parameter fusion framework that addresses catastrophic forgetting in LLM-based agents through geometric consensus filtering and curvature-based importance weighting, disentangling common knowledge from task-specific conflicting knowledge to enable effective continual learning for GUI and tool-use agents.
