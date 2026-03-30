# Silvio Savarese's Papers

- [WALT: Web Agents that Learn Tools](https://arxiv.org/abs/2510.01524)
    - Viraj Prabhu, Yutong Dai, Matthew Fernandez, Jing Gu, Krithika Ramakrishnan, Yanqi Luo, Silvio Savarese, Caiming Xiong, Junnan Li, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: October 1, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [tool learning], [tool discovery], [browser automation], [WALT]
    - 📖 TLDR: This paper introduces WALT, a framework that reverse-engineers website functionality into reusable deterministic tools for web agents. Instead of relying on brittle step-by-step UI interaction, the agent invokes learned high-level operations such as search, filter, and content management. On WebArena and VisualWebArena, WALT improves success rates while reducing interaction steps and heavy reasoning overhead, making tool-centric web automation substantially more robust.

- [SCUBA: Salesforce Computer Use Benchmark](https://sfrcua.github.io/SCUBA/)
    - Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: Sep 30, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [enterprise automation], [demonstration augmentation], [process rewards], [SCUBA]
    - 📖 TLDR: This paper introduces **SCUBA**, a benchmark for evaluating computer-use agents on 300 enterprise-critical CRM tasks within Salesforce. Tasks span personas like admins and service agents, testing UI navigation, automation, data handling, and troubleshooting. SCUBA includes sandbox environments, milestone-based evaluations, and supports parallel execution. Baseline results show large performance gaps across agent designs, especially between open- and closed-source models, with success rates ranging from 5% to 50% depending on demonstration usage.

- [MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers](https://arxiv.org/abs/2508.14704)
    - Ziyang Luo, Zhiqi Shen, Wenzhuo Yang, Zirui Zhao, Prathyusha Jwalapuram, Amrita Saha, Doyen Sahoo, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: August 20, 2025
    - 📑 Publisher: NeurIPS 2025 Workshop
    - 💻 Env: [Misc]
    - 🔑 Key: [benchmark], [dataset], [framework], [long-horizon reasoning], [unknown-tools challenge], [execution-based evaluation], [MCP-Universe]
    - 📖 TLDR: MCP-Universe introduces the first comprehensive benchmark for evaluating large language models (LLMs) through interactions with real-world Model Context Protocol (MCP) servers. It spans six core domains—Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, and Web Searching—across 11 MCP servers. The benchmark employs execution-based evaluators (format, static, dynamic) to rigorously assess agent performance. Despite progress, state-of-the-art models like GPT-5 (43.72% success), Grok-4 (33.33%), and Claude-4.0-Sonnet (29.44%) show significant limitations. The benchmark highlights challenges in long-context reasoning and unfamiliar tool handling, and provides an open-source extensible evaluation framework with UI support to accelerate future research. 

- [CoAct‑1: Computer‑using Multi-agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: USC, Salesforce, UW
    - 📅 Date: August 5, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hybrid agent], [coding action], [multi-agent system], [OSWorld]
    - 📖 TLDR: This paper introduces **CoAct‑1**, a multi-agent system where an Orchestrator coordinates between a GUI Operator and a Programmer agent that can execute code (Python/Bash) directly. This hybrid design allows the agent to perform complex desktop tasks more efficiently than GUI-only agents. Evaluated on OSWorld and WindowsAgentArena, CoAct‑1 achieves state-of-the-art success rates of 60.8% and 52.5% respectively, while reducing average steps to 10.15.

- [GTA1: GUI Test-time Scaling Agent](https://arxiv.org/abs/2507.05791)
    - Yan Yang, Dongxu Li, Yutong Dai, Yuhao Yang, Ziyang Luo, Zirui Zhao, Zhiyuan Hu, Junzhe Huang, Amrita Saha, Zeyuan Chen, Ran Xu, Liyuan Pan, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research, ANU, HKU
    - 📅 Date: July 8, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time scaling], [reinforcement learning], [planning], [grounding], [GTA1]
    - 📖 TLDR: This paper tackles two major challenges in GUI agents — planning ambiguity and visual grounding accuracy. It introduces **GTA1**, a GUI Test-time Scaling Agent that improves action decision-making by sampling multiple candidate actions at each step and selecting the best one via a judge model. Additionally, it enhances grounding through reinforcement learning with success-based rewards. GTA1 achieves state-of-the-art results on GUI grounding and execution benchmarks such as ScreenSpot and OSWorld.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: HKU, CMU, Salesforce, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [real computer tasks], [online environment], [online benchmark]
    - 📖 TLDR: OSWorld introduces a groundbreaking benchmark for multimodal agents to perform open-ended tasks within real computer environments across platforms like Ubuntu, Windows, and macOS. It includes 369 real-world tasks involving web and desktop apps, file management, and multi-app workflows, with custom evaluation scripts for reproducibility. The results reveal current agents’ limitations in GUI interaction and operational knowledge, as they achieve just 12.24% task success compared to humans' 72.36%, highlighting critical gaps for future model improvement.
