# Papers with Keyword: OSWorld

- [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/abs/2603.26266)
    - Rui Xie, Zhi Gao, Chenrui Shi, Zirui Shang, Lu Chen, Qing Li
    - 🏛️ Institutions: Shanghai Jiao Tong University, State Key Laboratory for General Artificial Intelligence, BIGAI, Beijing Institute of Technology
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [video retrieval], [automatic annotation], [domain adaptation], [training-free], [OSWorld], [GUIDE]
    - 📖 TLDR: GUIDE is a training-free plug-and-play framework for desktop GUI agents that retrieves relevant tutorial videos, converts them into planning and grounding annotations, and injects that knowledge into existing agents without changing their parameters or architectures. On OSWorld, it improves multiple agent families while also reducing execution steps.

- [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995)
    - Sizhe Tang, Rongqian Chen, Tian Lan, Rui Chen, Ze-Feng Gao
    - 🏛️ Institutions: George Washington University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time compute], [tree search], [MCTS], [benchmark], [OSWorld]
    - 📖 TLDR: Agent Alpha is a unified framework that applies step-level Monte Carlo Tree Search (MCTS) with alpha-UCT guided exploration, comparison-driven evaluation, and diversity-constrained expansion to GUI/computer-use agents, achieving a state-of-the-art ~77% success rate on the OSWorld benchmark while significantly outperforming trajectory-level sampling baselines under equivalent compute.

- [BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://arxiv.org/abs/2601.21352)
    - Ziyu Lu, Tengjin Weng, Yiying Yang, Hanchu Zhou, Kenji Kawaguchi
    - 🏛️ Institutions: Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shenzhen University, Guangdong University of Technology
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [backtracking], [DFS], [planning], [error recovery], [OSWorld]
    - 📖 TLDR: BEAP-Agent models long-horizon GUI execution as depth-first search and adds a systematic multi-level backtracking mechanism for recovering from wrong exploration paths. Its Planner, Executor, and Tracker coordinate both execution and task-state updates, and the paper validates the value of explicit backtracking on OSWorld.

- [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)
    - Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu
    - 🏛️ Institutions: Meituan
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [synthetic data], [reinforcement learning], [OSWorld], [EvoCUA]
    - 📖 TLDR: This paper introduces EvoCUA, a native computer-use agent trained through an evolving learning cycle that tightly couples scalable synthetic task generation, large-scale sandbox rollouts, and iterative policy optimization. Instead of relying on static imitation data, EvoCUA turns successful and failed experience into supervision through verification, error analysis, and self-correction, enabling continual capability growth. On OSWorld, it reaches 56.7% success rate, surpassing prior open-source computer-use agents and even some leading closed-weight systems.

- [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)
    - Hanna Foerster, Tom Blanchard, Kristina Nikolić, Ilia Shumailov, Cheng Zhang, Robert Mullins, Nicolas Papernot, Florian Tramèr, Yiren Zhao
    - 🏛️ Institutions: University of Cambridge, University of Toronto, Vector Institute, ETH Zurich, AI Sequrity Company
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [single-shot planning], [branch steering], [OSWorld]
    - 📖 TLDR: This paper studies system-level security for computer-use agents under prompt injection attacks. It introduces Single-Shot Planning, where a trusted planner produces a full execution graph with conditional branches before the agent observes potentially malicious content, giving provable control-flow integrity against injected instructions. The paper also identifies Branch Steering as an additional attack surface and shows on OSWorld that strong security guarantees can be achieved while retaining meaningful utility.

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu
    - 🏛️ Institutions: Nanjing University, Peking University, Microsoft Research Asia
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [RLVR], [OSWorld], [training]
    - 📖 TLDR: BEPA (Bi-Level Expert-to-Policy Assimilation) bridges the gap between off-policy expert trajectories and on-policy reinforcement learning for GUI agents by converting static expert traces into policy-aligned guidance via self-rolled reachable trajectories and a dynamically updated cache, improving UITARS1.5-7B success rate from 22.87% to 32.13% on OSWorld-Verified.

- [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790)
    - Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple, The University of Hong Kong
    - 📅 Date: October 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [hybrid action], [tool-use], [reinforcement learning], [working memory], [OSWorld], [WindowsAgentArena], [UltraCUA]
    - 📖 TLDR: UltraCUA is a foundation computer-use model that mixes primitive GUI actions with high-level tool calls, using automated tool extraction, synthetic verifiable tasks, supervised fine-tuning, and online reinforcement learning. The hybrid action design improves both robustness and efficiency, yielding strong gains on OSWorld and solid transfer to WindowsAgentArena.

- [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892)
    - Kai Mei, Jiang Guo, Shuaichen Chang, Mingwen Dong, Dongkyu Lee, Xing Niu, Jiarong Jiang
    - 🏛️ Institutions: Rutgers University, AWS Agentic AI
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [world model], [retrieval-augmented planning], [OSWorld], [WebArena], [r-WoM]
    - 📖 TLDR: This paper studies whether LLMs can reliably serve as world models for computer-use agents and finds that their simulations degrade sharply over long-horizon procedures despite reasonable short-range predictions. To address this, it proposes R-WoM, a retrieval-augmented world model that grounds planning with up-to-date external tutorials. R-WoM improves planning quality on OSWorld and WebArena, with especially strong gains on longer-horizon tasks where ungrounded simulation is most brittle.

- [Scaling Agents for Computer Use](https://arxiv.org/abs/2510.02250)
    - Gonzalo Gonzalez-Pumariega, Vincent Tu, Chih-Lun Lee, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular AI, UCSB, Cornell
    - 📅 Date: October 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [test-time scaling], [evaluation], [OSWorld], [behavior cloning]
    - 📖 TLDR: BJudge (Behavior Judge) scales CUAs over multiple rollouts by representing agent executions as behavior narratives for structured comparison and selection, achieving a new state-of-the-art on OSWorld (72.6%) that surpasses human-level performance (72.36%) and generalizes to WindowsAgentArena and AndroidWorld.

- [CoAct-1: Computer-using Multi-Agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: University of Southern California, Salesforce Research, University of Washington
    - 📅 Date: August 05, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [multi-agent system], [coding actions], [hybrid execution], [OSWorld], [WindowsAgentArena], [CoAct-1]
    - 📖 TLDR: Combines GUI control with direct Python/Bash execution by letting an orchestrator delegate subtasks to either a GUI operator or a programmer agent. This hybrid action space makes long-horizon desktop tasks more reliable and efficient, reaching state-of-the-art results on OSWorld and WindowsAgentArena with fewer interaction steps than GUI-only systems.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [harmful task completion], [OSWorld], [RiOSWorld]
    - 📖 TLDR: RiOSWorld measures misuse risk for multimodal desktop and web agents in realistic interactive settings rather than ordinary chat-style safety probes. Its 492 risky tasks score both harmful intent and harmful task completion, showing that current agents remain highly exposed to real-world misuse despite strong task-solving abilities.

- [UI-Evol: Automatic Knowledge Evolving for Computer Use Agents](https://arxiv.org/abs/2505.21964)
    - Ziyun Zhang, Xinyi Liu, Xiaoyi Zhang, Jun Wang, Gang Chen, Yan Lu
    - 🏛️ Institutions: School of Software and Microelectronics, Peking University, Microsoft Research Asia
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [knowledge-execution gap], [critique stage], [retrace stage], [OSWorld], [self‑evolution]
    - 📖 TLDR: The paper identifies a “knowledge‑execution gap” where even highly accurate external knowledge (90%) only yields a 41% execution success rate. To bridge this, the authors introduce **UI‑Evol**, a plug‑and‑play two‑stage module for GUI agents—**Retrace** recovers actual action sequences from real agent–environment interactions, and **Critique** refines knowledge by comparing these sequences with external references. Experiments using Agent S2 on the OSWorld benchmark show significant gains in task performance and reduced behavioral variance, improving agent reliability.

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [model context protocol], [MCP], [OSWorld], [LiteCUA]
    - 📖 TLDR: Introduces AIOS 1.0, which contextualizes desktop computer states via an MCP server so LLM-powered agents can better understand and operate GUIs. Built on top, LiteCUA—a lightweight agent—achieves 14.66 % success on the OSWorld benchmark, outperforming several heavier agent frameworks, showing the benefits of environment contextualization.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Institute of Technology, The University of Hong Kong, Stanford University
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [attack], [adversarial pop-ups], [safety], [OSWorld], [VisualWebArena]
    - 📖 TLDR: Shows that vision-language computer agents can be reliably distracted by adversarial pop-ups that human users would typically ignore. On OSWorld and VisualWebArena, these pop-ups achieve high attack success rates and sharply reduce task completion, while simple defenses like warning prompts remain ineffective.
