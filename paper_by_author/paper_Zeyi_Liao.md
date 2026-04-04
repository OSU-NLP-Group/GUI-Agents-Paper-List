# Zeyi Liao's Papers

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL]
    - 📖 TLDR: This paper studies continual learning for computer-use agents in dynamic, shifting target environments without relying on human demonstrations. It introduces ACuRL, an autonomous curriculum reinforcement learning framework that explores environments, synthesizes progressively tailored tasks, and trains with CUAJudge, an automatic evaluator aligned closely with human judgments. The method improves both intra-environment and cross-environment adaptation while avoiding catastrophic forgetting, making it directly relevant to real-world deployment of CUAs.

- [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725)
    - Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, The Chinese University of Hong Kong, Shenzhen
    - 📅 Date: February 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [guardrail], [world model], [risk prediction], [safety], [long-horizon risk]
    - 📖 TLDR: SafePred is a predictive guardrail for computer-use agents that uses a world model to simulate future states and align current actions with delayed risk, targeting long-horizon hazards that reactive guardrails miss because the danger only emerges after later state transitions.

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Zeyi Liao, Yadong Lu, Boyu Gou, Huan Sun, Ahmed Awadallah
    - 🏛️ Institutions: The Ohio State University, Microsoft Research, Redmond
    - 📅 Date: November 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [dataset], [benchmark], [text dragging], [multimodal LLM]
    - 📖 TLDR: This paper introduces GUI-Drag, a 161K-example dataset for text dragging in GUIs, and ScreenDrag, a benchmark with 5,333 examples, extending GUI grounding beyond click-only actions to support drag-based text selection and manipulation while maintaining click performance.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets & Benchmarks Track)
    - 💻 Env: [Web], [Search]
    - 🔑 Key: [benchmark], [agentic search], [agent-as-a-judge], [information synthesis], [evaluation], [Mind2Web 2]
    - 📖 TLDR: Mind2Web 2 is a benchmark of 130 realistic long-horizon agentic-search tasks built with more than 1,000 hours of human labor, focusing on real-time browsing plus citation-backed synthesis rather than short static-answer retrieval. Its main technical contribution is Agent-as-a-Judge: task-specific judge agents built from tree-structured rubrics that score both answer correctness and source attribution, enabling large-scale evaluation of frontier deep-research systems against humans.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://arxiv.org/abs/2410.17401)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, University of Chicago, The Ohio State University, University of Science and Technology of China
    - 📅 Date: October 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [attack], [black-box attack], [adversarial prompt injection], [DPO], [AdvAgent]
    - 📖 TLDR: AdvAgent is a black-box red-teaming framework for web agents that trains an adversarial prompter with DPO to craft stealthy, controllable attacks against VLM-powered agents. It achieves high attack success rates on realistic web tasks and shows that existing prompt-based defenses remain insufficient.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Los Angeles, The University of Chicago, University of Illinois Urbana-Champaign, University of Wisconsin-Madison
    - 📅 Date: September 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [EIA]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://arxiv.org/abs/2402.10196)
    - Lingbo Mo, Zeyi Liao, Boyuan Zheng, Yu Su, Chaowei Xiao, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of Wisconsin-Madison
    - 📅 Date: February 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [adversarial attacks], [security risks], [language agents], [perception-brain-action]
    - 📖 TLDR: Maps adversarial attacks on language agents through a Perception-Brain-Action decomposition and surveys 12 attack types across those layers. The paper is mainly a threat-modeling taxonomy, useful as a security lens for later web and computer-use agents.
