# Papers with Keyword: framework

- [Continual GUI Agents](https://arxiv.org/abs/2601.20732)
    - Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng
    - 🏛️ Institutions: Department of Computer Science and Technology, Tsinghua, College of Computer Science, ZJU, Photogrammetry and Remote Sensing Lab, ETH, College of Computer Science, Beijing University of Posts and Telecommunications
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement fine-tuning], [domain shift], [resolution shift], [GUI-AiF]
    - 📖 TLDR: This paper defines continual GUI agents as agents that must keep grounding accurately while interface domains and resolutions shift over time. It introduces GUI-AiF, a reinforcement fine-tuning method with anchoring-point and anchoring-region rewards, and reports stronger continual-domain and continual-resolution performance than prior baselines.

- [MAGNET: Towards Adaptive GUI Agents with Memory-Driven Knowledge Evolution](https://arxiv.org/abs/2601.19199)
    - Libo Sun, Jiwen Zhang, Siyuan Wang, Zhongyu Wei
    - 🏛️ Institutions: Fudan, USC, Shanghai Innovation Institute
    - 📅 Date: January 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [procedural memory], [stationary memory], [dynamic memory evolution], [UI-40K], [MAGNET]
    - 📖 TLDR: MAGNET targets appearance drift and workflow drift in mobile GUI agents with dual-level memory: stationary memory for stable functional semantics and procedural memory for reusable task workflows. It also adds a dynamic memory evolution mechanism and the UI-40K dataset, and improves results on AndroidWorld and offline distribution-shift benchmarks.

- [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197)
    - Shaokang Wang, Pei Fu, Ruoceng Zhang, Shaojie Zhang, Xiuwen Xi, Jiahui Yang, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [critic model], [test-time scaling], [data flywheel], [Intuitive Critic Model], [GAIA]
    - 📖 TLDR: GAIA trains an Intuitive Critic Model that judges the immediate correctness of candidate GUI actions before execution. It then uses a data flywheel that recycles agent-generated positive and negative action samples to iteratively improve the critic, yielding better test-time performance for both open-source and closed-source GUI agents.

- [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE)
    - Bin Kang, Shaoguo Wen, Yifei Bi, Shunlong Wu, Xinbin Yuan, Rui Shao, Junle Wang, Zhuotao Tian
    - 🏛️ Institutions: Chengdu Institute of Computer Applications, CAS, University of Chinese Academy of Sciences, Tencent Turing Lab, Georgia Tech, Tsinghua, Nankai University, Shenzhen Loop Area Institute
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [benchmark], [long-horizon tasks], [reflection], [rollback], [LongGUIBench], [LongHorizonUI]
    - 📖 TLDR: LongHorizonUI targets error accumulation in long-horizon GUI control by combining indexed multimodal perception, structured reflective decision-making, and rollback-based compensatory execution. It also introduces LongGUIBench for tasks longer than 15 steps across games and complex applications, and reports substantial gains on long-horizon evaluation while staying competitive on public benchmarks.

- [GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents](https://arxiv.org/abs/2601.18842)
    - Yanxi Wang, Zhiling Zhang, Wenbo Zhou, Weiming Zhang, Jie Zhang, Qiannan Zhu, Yu Shi, Shuxin Zheng, Jiyan He
    - 🏛️ Institutions: Beijing Normal University, Zhongguancun Academy, USTC, A*STAR, Zhongguancun Institution of Artificial Intelligence
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [privacy recognition], [privacy protection], [privacy grounding], [GUIGuard], [GUIGuard-Bench]
    - 📖 TLDR: GUIGuard formulates privacy-preserving GUI automation as privacy recognition, privacy protection, and protected task execution. It also introduces GUIGuard-Bench, a cross-platform benchmark with 630 trajectories and 13,830 screenshots annotated for region-level privacy grounding, risk level, privacy category, and task necessity, and shows that current models still recognize private content very poorly.

- [GraphPilot: GUI Task Automation with One-Step LLM Reasoning Powered by Knowledge Graph](https://arxiv.org/abs/2601.17418)
    - Mingxian Yu, Siqi Luo, Xu Chen
    - 🏛️ Institutions: School of Computer Science and Engineering, Sun Yat-sen University
    - 📅 Date: January 24, 2026
    - 📑 Publisher: Journal of Intelligent Computing and Networking
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [knowledge graph], [one-query planning], [validator], [GraphPilot]
    - 📖 TLDR: GraphPilot builds app-specific knowledge graphs that encode page functions, element roles, and transition rules, then uses them to plan nearly complete action sequences in almost one LLM query. On DroidTask it improves task completion while sharply reducing latency and the number of LLM calls relative to stepwise mobile agents.

- [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)
    - Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu
    - 🏛️ Institutions: Meituan, Fudan, Tongji University, HKUST
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [framework], [synthetic experience], [verifiable synthesis], [OSWorld], [EvoCUA]
    - 📖 TLDR: EvoCUA replaces static imitation with an evolving training loop built on verifiable task synthesis, high-throughput sandbox rollouts, and iterative policy optimization from both successful and failed trajectories. On OSWorld it reaches 56.7% success, outperforming prior open-source computer-use agents and even some leading closed-weight systems.

- [MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction](https://arxiv.org/abs/2601.12822)
    - Wenqi Zhang, Yulin Shen, Changyue Jiang, Jiarun Dai, Geng Hong, Xudong Pan
    - 🏛️ Institutions: Fudan, Shanghai Innovation Institute
    - 📅 Date: January 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [simulation-to-real], [reasoning correction], [MirrorWorld], [MirrorGuard]
    - 📖 TLDR: MirrorGuard is a plug-and-play defense that trains on high-risk trajectories synthesized in a neural-symbolic text simulator called MirrorWorld, then corrects insecure reasoning before real computer-use agents act. Across multiple benchmarks and architectures, it cuts unsafe behavior sharply while preserving utility better than prior defenses.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: USTC, Institute of Artificial Intelligence (TeleAI), China Telecom, Shanghai Innovation Institute, SJTU
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [active perception], [tool-augmented perception], [ScreenSpot-pro], [GUI-Eyes]
    - 📖 TLDR: GUI-Eyes frames GUI grounding as active perception, letting the agent learn when and how to call tools such as cropping and zooming inside a two-stage reasoning process. It pairs that policy with a spatially continuous reward for tool use and reaches 44.8% grounding accuracy on ScreenSpot-Pro using only 3k labeled samples.

- [Compress to Focus: Efficient Coordinate Compression for Policy Optimization in Multi-Turn GUI Agents](https://arxiv.org/abs/2601.11631)
    - Yurun Song, Jiong Yin, Rongjunchen Zhang, Ian G. Harris
    - 🏛️ Institutions: HiThink Research, UC Irvine, Hangzhou Dianzi University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [policy optimization], [coordinate compression], [Coordinate-Aware Spatial Compression], [distance-based advantage], [CCPO]
    - 📖 TLDR: CCPO tackles context inflation in multi-turn GUI agents by compressing historical screenshots around task-relevant coordinates collected across rollouts. Its Coordinate-Aware Spatial Compression and distance-based advantage improve both compression quality and grounding, reaching state-of-the-art results with up to 55% token compression and 3.8x training speedup.

- [ExpSeek: Self-Triggered Experience Seeking for Web Agents](https://arxiv.org/abs/2601.08605)
    - Wenyuan Zhang, Xinghua Zhang, Haiyang Yu, Shuaiyi Nie, Bingli Wu, Juwei Yue, Tingwen Liu, Yongbin Li
    - 🏛️ Institutions: Institute of Information Engineering, CAS, School of Cyber Security, University of Chinese Academy of Sciences, Tongyi Lab, Alibaba Group
    - 📅 Date: January 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [experience seeking], [entropy-based triggering], [experience intervention], [ExpSeek]
    - 📖 TLDR: ExpSeek turns experience intervention from a passive pre-task context into a step-level mechanism that is triggered only when the agent’s own entropy signal indicates uncertainty. It also generates tailored experience content per step, improving Qwen3-8B and 32B web agents by 9.3 and 7.5 absolute points across four benchmarks.

- [ShowUI-Aloha: Human-Taught GUI Agent](https://arxiv.org/abs/2601.07181)
    - Yichun Zhang, Xiangwu Guo, Yauhong Goh, Jessica Hu, Zhiheng Chen, Xin Wang, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS
    - 📅 Date: January 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [learning from demonstration], [screen recording], [human teaching], [ShowUI-Aloha]
    - 📖 TLDR: ShowUI-Aloha converts in-the-wild desktop screen recordings into structured teaching trajectories through a recorder, learner, planner, and executor pipeline. The goal is to let GUI agents learn complex desktop tasks from ordinary human demonstrations rather than curated annotations or synthetic traces.

- [ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](https://arxiv.org/abs/2601.07262)
    - Jihong Wang, Jiamu Zhou, Weiming Zhang, Weiwen Liu, Zhuosheng Zhang, Xingyu Lou, Weinan Zhang, Huarong Deng, Jun Wang
    - 🏛️ Institutions: OPPO Research Institute, SJTU
    - 📅 Date: January 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-in-the-loop], [knowledge adaptation], [progress summarization], [WebArena], [ColorBrowserAgent]
    - 📖 TLDR: ColorBrowserAgent targets site heterogeneity and long-horizon instability in web automation with two mechanisms: human-in-the-loop knowledge adaptation and progressive progress summarization. On WebArena it reaches 71.2% success, and the paper also reports transfer to WebChoreArena and gains in industrial deployment.

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu
    - 🏛️ Institutions: NJU, PKU, Microsoft Research Asia
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [RLVR], [off-policy assimilation], [BEPA], [OSWorld]
    - 📖 TLDR: BEPA improves end-to-end GUI-agent training with verifiable rewards by turning scarce off-policy expert traces into policy-aligned guidance through self-rolled reachable trajectories and a dynamically updated per-task cache. On OSWorld-Verified it raises UI-TARS-1.5-7B from 22.87% to 32.13%, with additional gains on MMBench-GUI and Online-Mind2Web.

- [GUITester: Enabling GUI Agents for Exploratory Defect Discovery](https://arxiv.org/abs/2601.04500)
    - Yifei Gao, Jiang Wu, Xiaoyi Chen, Yifan Yang, Zhe Cui, Tianyi Ma, Jiaming Zhang, Jitao Sang
    - 🏛️ Institutions: Beijing Jiaotong University, Hithink Research, NTU
    - 📅 Date: January 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [GUI testing], [defect discovery], [GUITestBench], [GUITester]
    - 📖 TLDR: GUITester targets exploratory defect discovery in mobile apps, where agents must both navigate and recognize that anomalous behavior is a product defect rather than their own mistake. It introduces GUITestBench with 143 tasks across 26 defects and a multi-agent framework that separates planning-execution from hierarchical reflection, reaching 48.90% F1 (Pass@3).

- [InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](https://arxiv.org/abs/2601.04126)
    - Ziyun Zhang, Zezhou Wang, Xiaoyi Zhang, Zongyu Guo, Jiahao Li, Bin Li, Yan Lu
    - 🏛️ Institutions: PKU, NJU, Microsoft Research Asia
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [environment synthesis], [data generation], [verifiable rewards], [InfiniteWeb]
    - 📖 TLDR: InfiniteWeb automatically builds functional multi-page web environments for GUI-agent training rather than just generating isolated webpages. It uses unified specifications, task-centric test-driven development, and reference design images, and the resulting environments improve agent training on Online-Mind2Web and OSWorld.

- [MobileDreamer: Generative Sketch World Model for GUI Agent](https://arxiv.org/abs/2601.04035)
    - Yilin Cao, Yufeng Zhong, Zhixiong Zeng, Liming Zheng, Jing Huang, Haibo Qiu, Peng Shi, Wenji Mao, Wan Guanglu
    - 🏛️ Institutions: State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, CAS, School of Artificial Intelligence, University of Chinese Academy of Sciences, Meituan
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [lookahead], [rollout imagination], [MobileDreamer]
    - 📖 TLDR: MobileDreamer equips mobile GUI agents with a lightweight world model that predicts task-relevant textual sketches of future interface states instead of full screenshots. It then uses rollout imagination over those predicted futures for action selection, improving AndroidWorld performance by 5.25% and reaching state of the art.

- [WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation](https://arxiv.org/abs/2510.22732)
    - Jiali Cheng, Anjishnu Kumar, Roshan Lal, Rishi Rajasekaran, Hani Ramezani, Omar Zia Khan, Oleg Rokhlenko, Sunny Chiu-Webster, Gang Hua, Hadi Amiri
    - 🏛️ Institutions: University of Massachusetts Lowell, Amazon Alexa AI
    - 📅 Date: October 26, 2025
    - 📑 Publisher: NeurIPS 2025 Workshop on Language Agents and World Models
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [memory], [planning], [action simulation], [WebArena-Lite], [WebATLAS]
    - 📖 TLDR: WebATLAS is a training-free web agent that reuses past interaction outcomes as persistent experience memory and simulates candidate actions before executing them. Its planner-simulator-critic loop is designed to improve long-horizon behavior on unseen websites, and it reports 63% success on WebArena-Lite without site-specific fine-tuning.

- [Surfer 2: The Next Generation of Cross-Platform Computer Use Agents](https://arxiv.org/abs/2510.19949)
    - Mathieu Andreux, Märt Bakler, Yanael Barbier, Hamza Benchekroun, Emilien Biré, Antoine Bonnet, Riaz Bordie, Nathan Bout, Matthias Brunel, Aleix Cambray, Pierre-Louis Cedoz, Antoine Chassang, Gautier Cloix, Ethan Connelly, Alexandra Constantinou, Ramzi De Coster, Hubert de la Jonquiere, Aurélien Delfosse, Maxime Delpit, Alexis Deprez, Augustin Derupti, Mathieu Diaz, Shannon D'Souza, Julie Dujardin, Abai Edmund, Michael Eickenberg, Armand Fatalot, Wissem Felissi, Isaac Herring, Xavier Koegler, Erwan Le Jumeau de Kergaradec, Aurélien Lac, Maxime Langevin, Corentin Lauverjat, Antonio Loison, Avshalom Manevich, Axel Moyal, Axel Nguyen Kerbel, Marinela Parovic, Julien Revelle, Guillaume Richard, Mats Richter, Ronan Riochet, María Santos, Romain Savidan, Laurent Sifre, Maxime Theillard, Marc Thibault, Ivan Valentini, Tony Wu, Laura Yie, Kai Yuan, Jevgenij Zubovskij
    - 🏛️ Institutions: H Company
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [framework], [cross-platform], [hierarchical context management], [self-verification], [adaptive recovery], [Surfer 2]
    - 📖 TLDR: Surfer 2 is a visual-only cross-platform computer-use agent designed to work across web, desktop, and mobile without task-specific fine-tuning. It combines hierarchical context management, decoupled planning and execution, and self-verification with adaptive recovery, and reports state-of-the-art results on WebVoyager, WebArena, OSWorld, and AndroidWorld.

- [CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs](https://arxiv.org/abs/2510.15455)
    - Gucongcong Fan, Chaoyue Niu, Chengfei Lyu, Fan Wu, Guihai Chen
    - 🏛️ Institutions: SJTU, Alibaba Group
    - 📅 Date: October 17, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [privacy], [cloud-local collaboration], [UI exposure reduction], [CORE]
    - 📖 TLDR: CORE studies how to reduce unnecessary screen exposure when mobile agents depend on cloud LLMs for planning and action selection. It partitions the UI into layout-aware blocks and lets local and cloud models collaborate on planning and decision-making so only task-relevant UI subsets are sent to the cloud, substantially reducing exposure while keeping accuracy close to cloud-only systems.

- [PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction](https://arxiv.org/abs/2510.15863)
    - Simon Yu, Gang Li, Weiyan Shi, Peng Qi
    - 🏛️ Institutions: Northeastern University, Uniphore
    - 📅 Date: October 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [skill learning], [compositional skills], [transfer generalization], [polymorphism], [PolySkill], [continual learning]
    - 📖 TLDR: PolySkill targets the tendency of web-agent skills to overfit one site by separating each skill's abstract goal from its concrete site-specific implementation. This polymorphic abstraction improves skill reuse, cross-site transfer, and continual learning behavior on Mind2Web-style settings.

- [BIMgent: Towards Autonomous Building Modeling via Computer-use Agents](https://arxiv.org/abs/2506.07217)
    - Zihan Deng, Changyu Du, Stavros Nousias, André Borrmann
    - 🏛️ Institutions: TUM, TUM Georg Nemetschek Institute
    - 📅 Date: June 08, 2025
    - 📑 Publisher: ICML 2025 Workshop on Computer-use Agents
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [building information modeling], [GUI authoring], [AEC], [BIMgent]
    - 📖 TLDR: BIMgent studies whether general computer-use agents can handle specialized Building Information Modeling software rather than ordinary desktop tasks. It proposes an MLLM-based framework for conceptual design input, software-specific planning, and GUI execution, and reports nontrivial success on real-world 3D building authoring tasks where baseline agents fail.

- [LLM-Guided Scenario-based GUI Testing](https://arxiv.org/abs/2506.05079)
    - Shengcheng Yu, Yuchen Ling, Chunrong Fang, Quan Zhou, Yi Zhao, Chunyang Chen, Shaomin Zhu, Zhenyu Chen
    - 🏛️ Institutions: TUM, NJU, Tongji University
    - 📅 Date: June 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [scenario-based GUI testing], [multi-agent testing], [business-logic testing], [ScenGen]
    - 📖 TLDR: This paper targets the gap between mobile GUI testing and app business logic, arguing that exploration-heavy methods miss scenario-level functionality. It proposes ScenGen, a five-agent testing framework that interprets GUI semantics and executes business-logic-driven scenarios, yielding test actions that better match app functionality than exploration-based baselines.

- [Agent-SAMA: State-Aware Mobile Assistant](https://arxiv.org/abs/2505.23596)
    - Linqiang Guo, Wei Liu, Yi Wen Heng, Tse-Hsun Chen, Yang Wang
    - 🏛️ Institutions: SPEAR Lab, Concordia University
    - 📅 Date: May 29, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [finite state machine], [error recovery], [state-aware planning], [Agent-SAMA]
    - 📖 TLDR: Agent-SAMA addresses the reactive behavior of existing mobile agents by explicitly modeling app navigation as a finite state machine. Its four-agent framework uses that state structure for planning, verification, and recovery, improving both task success and recovery rates on cross-app mobile benchmarks.

- [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660)
    - Qinzhuo Wu, Pengzhi Gao, Wei Liu, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi
    - 📅 Date: May 27, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [error detection], [backtracking], [judgment reward], [BacktrackAgent]
    - 📖 TLDR: BacktrackAgent addresses the lack of error recovery in mobile GUI agents by adding verifier, judger, and reflector modules plus an explicit backtracking mechanism. It also builds training data for judgment and reflection over post-action outcome pages, improving both task success and step accuracy on Mobile3M and Auto-UI.

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [MCP server], [environmental contextualization], [OSWorld], [LiteCUA]
    - 📖 TLDR: LiteCUA argues that computer-use agents need better environment contextualization rather than only larger models or heavier agent stacks. It introduces AIOS 1.0, which exposes computer states and actions through an MCP server, and shows that the resulting lightweight desktop agent outperforms several stronger baselines on OSWorld.

- [GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://aclanthology.org/2025.acl-long.282/)
    - Bin Xie, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Jie Liu, Min Zhang, Liqiang Nie
    - 🏛️ Institutions: HIT-Shenzhen, Huawei Noah’s Ark Lab
    - 📅 Date: May 22, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [autonomous exploration], [transition-aware knowledge], [GUI-KRB], [GUI-explorer]
    - 📖 TLDR: GUI-explorer is a training-free mobile GUI agent that automatically explores app functionality and mines transition-aware knowledge from observed state changes. It also introduces the GUI-KRB benchmark for mobile GUI reasoning, and shows strong gains on SPA-Bench and AndroidWorld without parameter updates for new apps.

- [Unlocking Smarter Device Control: Foresighted Planning with a World Model-Driven Code Execution Approach](https://arxiv.org/abs/2505.16422)
    - Xiaoran Yin, Xu Luo, Hao Wu, Lianli Gao, Jingkuan Song
    - 🏛️ Institutions: University of Electronic Science and Technology of China, Tongji University, University of Trento
    - 📅 Date: May 22, 2025
    - 📑 Publisher: Findings of EMNLP 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [executable code], [self‑verification], [self‑refinement], [FPWC]
    - 📖 TLDR: FPWC targets the myopic decision-making of reactive mobile agents by constructing a task-oriented world model before execution and expressing plans as executable code. It then self-verifies and refines both the plan and world model during execution, yielding large gains on simulated and real-device mobile control tasks.

- [Building a Stable Planner: An Extended Finite State Machine Based Planning Module for Mobile GUI Agent](https://arxiv.org/abs/2505.14141)
    - Fanglin Mo, Junzhe Chen, Haoxuan Zhu, Xuming Hu
    - 🏛️ Institutions: HKUST(GZ), School of Computer Science & Engineering, South China University of Technology
    - 📅 Date: May 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [EFSM], [planning], [plug-and-play planner], [SPlanner]
    - 📖 TLDR: SPlanner addresses the instability of step-by-step mobile planning by modeling apps as extended finite state machines and converting traversed execution paths into natural-language plans. As a plug-and-play planning module, it substantially improves mobile-agent task completion on AndroidWorld.

- [MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation](https://aclanthology.org/2025.naacl-demo.43/)
    - Zichen Zhu, Hao Tang, Yansi Li, Dingye Liu, Hongshen Xu, Kunyao Lan, Danyang Zhang, Yixuan Jiang, Hao Zhou, Chenrun Wang, Situo Zhang, Liangtai Sun, Yixiao Wang, Yuheng Sun, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, Department of Computer Science and Engineering, MoE Key Lab of Artificial Intelligence, SJTU AI Institute, SJTU
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [memory], [adaptive planning], [MobBench], [MobA]
    - 📖 TLDR: MobA is a mobile assistant system for complex GUI tasks in dynamic app contexts where execution capabilities vary across pages. It combines reflection-based adaptive planning with a multifaceted memory module, and introduces the MobBench dataset for complex mobile interactions alongside results on MobBench and AndroidArena.

- [ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation](https://aclanthology.org/2025.naacl-long.244/)
    - Qinzhuo Wu, Wei Liu, Jian Luan, Bin Wang
    - 🏛️ Institutions: XiaoMi AI Lab
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [page reaching], [page operation], [MobileReach], [ReachAgent]
    - 📖 TLDR: ReachAgent addresses the tendency of mobile agents to optimize for the next local action while ignoring the larger GUI flow. It introduces the MobileReach training dataset, which decomposes tasks into page-reaching and page-operation subtasks, and uses those subtasks together with reward-based preference GUI flows to train a two-stage mobile agent.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, CMU
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-agent collaboration], [mixed-initiative web navigation], [data collection], [CowPilot]
    - 📖 TLDR: CowPilot is a mixed-initiative web-navigation framework where an agent proposes next steps while the user can pause, reject, override, or hand control back at any time. Across five websites, the collaborative mode reaches the highest success rate while requiring humans to perform only a small fraction of the total steps, and the system is also positioned as a data-collection and evaluation tool.

- [Infogent: An Agent-Based Framework for Web Information Aggregation](https://aclanthology.org/2025.findings-naacl.318/)
    - Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tur, Heng Ji
    - 🏛️ Institutions: UIUC
    - 📅 Date: April 29, 2025
    - 📑 Publisher: Findings of NAACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [information aggregation], [interactive visual access], [direct API-driven access], [AssistantBench], [Infogent]
    - 📖 TLDR: Infogent studies web information aggregation rather than single-site completion, asking agents to visit multiple websites and decide when enough evidence has been collected for a complex query. Its Navigator-Extractor-Aggregator design is evaluated in both direct API-driven and browser-based visual settings, including gains on AssistantBench under interactive visual access.

- [UFO2: The Desktop AgentOS](https://arxiv.org/abs/2504.14603)
    - Chaoyun Zhang, He Huang, Chiming Ni, Jian Mu, Si Qin, Shilin He, Lu Wang, Fangkai Yang, Pu Zhao, Chao Du, Liqun Li, Yu Kang, Zhao Jiang, Suzhen Zheng, Rujia Wang, Jiaxu Qian, Minghua Ma, Jian-Guang Lou, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
    - 🏛️ Institutions: Microsoft, ZJU-UIUC Institute, NJU, PKU
    - 📅 Date: April 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hybrid GUI-API control], [multi-agent], [speculative execution], [PiP virtual desktop], [UFO2]
    - 📖 TLDR: UFO2 presents a Windows AgentOS that pairs a coordinating HostAgent with specialized AppAgents for individual applications. Its main system ideas are a unified GUI-API action layer, hybrid UIA-plus-vision perception, speculative multi-action execution, and a picture-in-picture virtual desktop that lets users and the agent operate concurrently.

- [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, Shibo He, Wenchao Meng
    - 🏛️ Institutions: ZJU, vivo AI Lab
    - 📅 Date: April 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [few-shot learning], [LearnAct], [LearnGUI]
    - 📖 TLDR: LearnAct studies demonstration-based learning for mobile GUI agents rather than scaling generic pretraining alone. It introduces the LearnGUI dataset and benchmark for offline and online demonstration reuse, and uses a DemoParser-KnowSeeker-ActExecutor pipeline to extract, retrieve, and execute demonstration-derived knowledge in unseen mobile tasks.

- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: CMU, Microsoft
    - 📅 Date: April 09, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [programmatic skills], [programmatic verification], [skill induction], [ASI], [WebArena]
    - 📖 TLDR: This paper proposes Agent Skill Induction (ASI), which learns executable program-based skills online from web interaction experience and reuses them as tasks evolve. The use of programs makes skill induction verifiable, improving both WebArena success rate and step efficiency over static agents and text-skill baselines while also supporting cross-website transfer.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: OSU, CMU, University of Virginia, Purdue University, Cisco Research
    - 📅 Date: April 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [practice-and-distill], [transferable skills], [SkillWeaver]
    - 📖 TLDR: SkillWeaver is a skill-centric self-improvement framework for web agents that discovers website-specific skills, practices them, and distills the resulting experience into reusable APIs. Its iterative exploration grows a library of lightweight skills that improve performance on WebArena and real websites, and those APIs can also be transferred to weaker agents.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 01, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [mixture-of-grounding], [proactive hierarchical planning], [OSWorld], [WindowsAgentArena], [Agent S2]
    - 📖 TLDR: Agent S2 is a compositional generalist-specialist framework that splits computer-use responsibilities across specialized and generalist models rather than using a single monolithic agent. Its core methods are Mixture-of-Grounding for precise localization and Proactive Hierarchical Planning for long-horizon control, yielding strong gains on OSWorld, WindowsAgentArena, and AndroidWorld.

- [LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](https://aclanthology.org/2025.naacl-demo.36/)
    - Danqing Zhang, Balaji Rama, Jingyi Ni, Shiying He, Fu Zhao, Kunyu Chen, Arnold Chen, Junyu Cao
    - 🏛️ Institutions: PathOnAI.org, Rutgers University, UT Austin
    - 📅 Date: March 04, 2025
    - 📑 Publisher: NAACL 2025 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [workflow memory], [tree search], [CDP], [LiteWebAgent]
    - 📖 TLDR: LiteWebAgent is an open-source suite for web-agent applications built around a modular framework that decouples action generation from action grounding. It integrates planning, workflow memory, and tree search, and ships both as a remote-browser web app and as a Chrome extension controlled through CDP.

- [WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point](https://arxiv.org/abs/2502.08047)
    - Henry Hengyuan Zhao, Kaiming Yang, Wendi Yu, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS
    - 📅 Date: February 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [framework], [dynamic initial states], [planning robustness], [WorldGUI-Agent], [WorldGUI]
    - 📖 TLDR: WorldGUI is a benchmark for evaluating desktop and web GUI agents from diverse non-default starting states instead of only canonical initial setups. The paper also introduces WorldGUI-Agent, a model-agnostic three-stage critique framework that improves adaptation and recovery in those dynamic settings.

- [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)
    - Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Linhai Zhang, Yulan He, Deyu Zhou, Pengjun Xie, Fei Huang
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: January 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [web traversal], [explore-critic], [WebWalkerQA], [WebWalker]
    - 📖 TLDR: WebWalker studies web traversal for multi-layered information retrieval rather than shallow page lookup. It introduces the WebWalkerQA benchmark and an explore-critic multi-agent framework that improves traversal-based RAG in real-world website hierarchies.

- [PC Agent: While You Sleep, AI Works -- A Cognitive Journey into Digital World](https://arxiv.org/abs/2412.17589)
    - Yanheng He, Jiahe Jin, Shijie Xia, Jiadi Su, Runze Fan, Haoyang Zou, Xiangkun Hu, Pengfei Liu
    - 🏛️ Institutions: SJTU, GAIR
    - 📅 Date: December 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [PC agent], [human cognition transfer], [PC tracker], [cognition completion], [multi-agent system]
    - 📖 TLDR: PC Agent studies how to transfer human cognitive processes into desktop agents for complex digital work rather than short isolated tasks. It introduces PC Tracker for collecting cognitive interaction traces, a two-stage cognition-completion pipeline, and a planning-plus-grounding multi-agent system, showing promising results on long PowerPoint workflows with limited data.

- [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://proceedings.mlr.press/v267/zhou25ah.html)
    - Yifei Zhou, Qianlan Yang, Kaixiang Lin, Min Bai, Xiong Zhou, Yu-Xiong Wang, Sergey Levine, Li Erran Li
    - 🏛️ Institutions: UC Berkeley, UIUC, Amazon
    - 📅 Date: December 17, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [skill discovery], [autonomous task proposal], [VLM-based success evaluator], [PAE]
    - 📖 TLDR: PAE is a web-agent learning system that lets foundation-model agents autonomously propose tasks, attempt them, and score the resulting trajectories with a VLM-based evaluator. By turning those evaluations into RL signals, it improves zero-shot generalization on unseen websites and tasks for vision-based internet agents.

- [The BrowserGym Ecosystem for Web Agent Research](https://openreview.net/forum?id=5298fKGmv3)
    - Thibault Le Sellier de Chezelles, Maxime Gasse, Alexandre Lacoste, Massimo Caccia, Alexandre Drouin, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Graham Neubig, Quentin Cappart, Russ Salakhutdinov, Nicolas Chapados
    - 🏛️ Institutions: ServiceNow Research, ServiceNow, Laval University, imean.ai, Microsoft, CMU, Polytechnique Montréal, Université de Montréal
    - 📅 Date: December 06, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [BrowserGym], [AgentLab], [evaluation ecosystem]
    - 📖 TLDR: BrowserGym is a unified ecosystem for web-agent research that standardizes observation and action spaces while wrapping multiple existing benchmarks under one interface. The paper also introduces AgentLab for agent creation and analysis, and uses the ecosystem to run a large cross-benchmark comparison of six frontier LLMs.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://aclanthology.org/2025.findings-acl.76/)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Shenzhen International Graduate School, Tsinghua
    - 📅 Date: December 02, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [framework], [pure vision], [GUI grounding], [interpreter-locator], [ScreenSpot], [Ponder & Press]
    - 📖 TLDR: Ponder & Press is a pure-vision divide-and-conquer GUI-control framework that separates high-level instruction interpretation from element localization. It pairs a general-purpose MLLM interpreter with a GUI-specific locator, improves ScreenSpot grounding by 22.5%, and reports strong performance across web, desktop, and mobile GUI benchmarks.

- [AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://aclanthology.org/2025.acl-long.1008/)
    - Gaurav Verma, Rachneet Kaur, Nishan Srishankar, Zhen Zeng, Tucker Balch, Manuela Veloso
    - 🏛️ Institutions: Georgia Tech, J.P. Morgan AI Research
    - 📅 Date: November 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [few-shot adaptation], [human demonstrations], [website adaptation], [AdaptAgent]
    - 📖 TLDR: AdaptAgent studies how multimodal web agents can adapt to unseen websites with only a few human demonstrations instead of relying solely on broad pretraining or large-scale fine-tuning. It shows that both proprietary and open-weight agents benefit from few-shot demonstrations, with clear gains on Mind2Web and VisualWebArena.

- [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)
    - Anthony Nguyen
    - 🏛️ Institutions: Algoma University
    - 📅 Date: November 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [framework], [GUI grounding], [visual prompting], [iterative narrowing]
    - 📖 TLDR: Iterative Narrowing is a visual-prompting framework for GUI grounding that repeatedly zooms into smaller image regions to refine predictions. The paper shows that this simple test-time strategy improves both general and fine-tuned VLMs on one-shot grounding across multiple UI platforms.

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Shanghai AI Laboratory, HKU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [multi-agent system], [MetaAgent], [AgentToken], [AgentStore]
    - 📖 TLDR: Proposes AgentStore, a platform for integrating heterogeneous third-party agents into a single computer assistant. Its MetaAgent and AgentToken design lets the system coordinate specialized and generalist capabilities, substantially improving performance on challenging desktop-computing benchmarks such as OSWorld.

- [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b9e472cd579c83e2f6aa3459f46aac28-Abstract-Conference.html)
    - Taiyi Wang, Zhihao Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Powersense Technology Limited, Huawei Noah's Ark Lab, UCL, Tianjin University
    - 📅 Date: October 18, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [distributed RL fine-tuning], [centralized training], [decentralized data acquisition], [A-RIDE], [DistRL]
    - 📖 TLDR: DistRL is a distributed RL fine-tuning framework for mobile control agents that separates centralized training from decentralized data collection across worker devices. It is paired with the A-RIDE off-policy RL algorithm, and the paper reports 3x higher training efficiency, 2.4x faster data collection, and a 20% relative success-rate gain on open Android control tasks.

- [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://proceedings.iclr.cc/paper_files/paper/2025/hash/394c7c30ea87b5c3521b4d9e9d419071-Abstract-Conference.html)
    - Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: October 10, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hierarchical planning], [retrieval-augmented planning], [agent-computer interface], [Agent S]
    - 📖 TLDR: Agent S is an open computer-use framework built around an Agent-Computer Interface plus experience-augmented hierarchical planning that combines online web knowledge with narrative and episodic memory. The paper reports state-of-the-art OSWorld results and shows transfer to WindowsAgentArena without explicit adaptation.

- [ClickAgent: Enhancing UI Location Capabilities of Autonomous Agents](https://aclanthology.org/2025.sigdial-1.38/)
    - Jakub Hoscilowicz, Bartosz Maj, Bartosz Kozakiewicz, Oleksii Tymoshchuk, Artur Janicki
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 09, 2024
    - 📑 Publisher: SIGDIAL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI grounding], [AITW], [ClickAgent], [mobile control]
    - 📖 TLDR: Proposes ClickAgent, a mobile agent framework that separates high-level reasoning from precise UI element localization. By pairing an MLLM planner with a dedicated grounding component, it improves task success on AITW and on real-device Android evaluations.

- [AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://aclanthology.org/2025.acl-long.381/)
    - Junting Lu, Zhiyang Zhang, Fangkai Yang, Jue Zhang, Lu Wang, Chao Du, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: PKU, NJU, Microsoft
    - 📅 Date: September 26, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [API-first], [AXIS], [HACI], [agent OS]
    - 📖 TLDR: AXIS is an API-first agent framework that prioritizes application APIs over direct UI actions and also expands API coverage through automated exploration. On Microsoft Word tasks, it reduces completion time by 65-70% and cognitive workload by 38-53% while maintaining 97-98% accuracy relative to human performance, and it motivates a Human-Agent-Computer Interaction design framework for agent-centric software.

- [WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration](https://ojs.aaai.org/index.php/AAAI/article/view/34505)
    - Yao Zhang, Zijian Ma, Yunpu Ma, Zhen Han, Yu Wu, Volker Tresp
    - 🏛️ Institutions: LMU Munich, TUM, Munich Center for Machine Learning (MCML)
    - 📅 Date: August 28, 2024
    - 📑 Publisher: AAAI 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [monte carlo tree search], [strategic exploration], [global-local optimization], [WebPilot]
    - 📖 TLDR: WebPilot is a web-agent system that splits decision making into a global planning phase and a local MCTS-based execution phase to handle uncertain web environments. On WebArena and MiniWoB++, it reports stronger performance than prior tree-search baselines, including a 93% relative success-rate gain on WebArena with GPT-4.

- [AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/abs/2408.11824)
    - Yanda Li, Chi Zhang, Wenjia Jiang, Wanqi Yang, Bin Fu, Pei Cheng, Xin Chen, Ling Chen, Yunchao Wei
    - 🏛️ Institutions: University of Technology Sydney, Tencent, Beijing Jiaotong University, Westlake University
    - 📅 Date: August 05, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [knowledge base], [RAG], [exploration phase], [flexible action space], [AppAgent v2]
    - 📖 TLDR: AppAgent v2 is a mobile agent framework with separate exploration and deployment phases, where explored UI functionality is written into a structured knowledge base and later retrieved with RAG. The paper argues that this combination of flexible actions and reusable app knowledge improves cross-app mobile task execution on several benchmarks.

- [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032)
    - Tamer Abuelsaad, Deepak Akkil, Prasenjit Dey, Ashish Jagmohan, Aditya Vempaty, Ravi Kokku
    - 🏛️ Institutions: Emergence AI
    - 📅 Date: July 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [hierarchical architecture], [DOM distillation], [change observation], [self-improvement], [Agent-E]
    - 📖 TLDR: Agent-E is a web-agent architecture built around hierarchical control, DOM distillation and denoising, and explicit change observation. The paper reports 10-30% gains over prior web agents on WebVoyager and then distills the implementation lessons into broader agent-system design principles.

- [MobileExperts: A Dynamic Tool-Enabled Agent Team in Mobile Devices](https://arxiv.org/abs/2407.03913)
    - Jiayi Zhang, Chuang Zhao, Yihan Zhao, Zhaoyang Yu, Ming He, Jianping Fan
    - 🏛️ Institutions: AI Lab at Lenovo Research, Renmin University of China, HKUST
    - 📅 Date: July 04, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [tool formulation], [multi-agent collaboration], [double-layer planning], [Expert-Eval], [MobileExperts]
    - 📖 TLDR: MobileExperts is a mobile multi-agent framework that forms tool-enabled expert teams through device-specific exploration and then coordinates them with dual-layer planning. The paper also introduces the Expert-Eval benchmark and reports better performance across task difficulty levels with about 22% lower reasoning cost.

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://openreview.net/forum?id=3WWFrg8UjJ)
    - Zhiyong Wu, Chengcheng Han, Zichen Ding, Zhenmin Weng, Zhoumianze Liu, Shunyu Yao, Tao Yu, Lingpeng Kong
    - 🏛️ Institutions: Shanghai AI Laboratory, East China Normal University, Princeton, HKU
    - 📅 Date: February 12, 2024
    - 📑 Publisher: LLMAgents @ ICLR 2024
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [framework], [FRIDAY], [self-directed learning], [skill accumulation], [OS-Copilot]
    - 📖 TLDR: OS-Copilot is a framework for building generalist computer agents that interact with operating-system elements including the web, code terminals, files, multimedia, and third-party applications. The paper instantiates it with FRIDAY, a self-improving embodied agent that learns new application skills over time and reports a 35% improvement over prior methods on GAIA.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: January 03, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [grounding], [SeeAct], [live website evaluation], [Mind2Web]
    - 📖 TLDR: SeeAct studies GPT-4V as a generalist web agent and adds an online evaluation setup for running agents on live websites. It shows that GPT-4V is strong when grounding is handled manually, and identifies grounding as the main remaining bottleneck.

- [AppAgent: Multimodal Agents as Smartphone Users](https://doi.org/10.1145/3706598.3713600)
    - Chi Zhang, Zhao Yang, Jiaxuan Liu, Yucheng Han, Xin Chen, Zebiao Huang, Bin Fu, Gang Yu
    - 🏛️ Institutions: Tencent
    - 📅 Date: December 21, 2023
    - 📑 Publisher: CHI 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [AppAgent], [knowledge base], [autonomous exploration], [human demonstrations], [tap-and-swipe control]
    - 📖 TLDR: AppAgent is a smartphone-use agent that operates through a simple tap-and-swipe action space without backend app access. It learns app usage through autonomous exploration or human demonstrations, stores that knowledge in a reference document, and is evaluated on 50 tasks across 10 apps.

- [SteP: Stacked LLM Policies for Web Actions](https://openreview.net/forum?id=5fg0VtRxgi)
    - Paloma Sodhi, S.R.K Branavan, Yoav Artzi, Ryan McDonald
    - 🏛️ Institutions: ASAPP Research, Cornell
    - 📅 Date: October 05, 2023
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [policy composition], [control stack], [WebArena], [SteP]
    - 📖 TLDR: SteP is a web-agent framework that composes LLM policies through an explicit control stack rather than a single monolithic prompt. It evaluates on WebArena, MiniWoB++, and a CRM environment, and substantially improves WebArena performance over prior GPT-4-based baselines.

- [You Only Look at Screens: Multimodal Chain-of-Action Agents](https://aclanthology.org/2024.findings-acl.186/)
    - Zhuosheng Zhang, Aston Zhang
    - 🏛️ Institutions: SJTU, Meta
    - 📅 Date: September 20, 2023
    - 📑 Publisher: Findings of ACL 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [chain-of-action], [Auto-GUI], [AITW], [screenshot-only control]
    - 📖 TLDR: Auto-GUI is a screenshot-only mobile GUI agent that avoids environment parsing and application-specific APIs. The paper introduces a chain-of-action prompting technique and evaluates the method on AITW, a device-control benchmark with 30K unique instructions.

- [LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/abs/2309.08172)
    - Kaixin Ma, Hongming Zhang, Hongwei Wang, Xiaoman Pan, Wenhao Yu, Dong Yu
    - 🏛️ Institutions: Tencent AI Lab
    - 📅 Date: September 15, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [LASER], [state-space exploration], [backtracking], [WebShop], [amazon.com]
    - 📖 TLDR: LASER reformulates web navigation as state-space exploration so an LLM agent can move among predefined states and backtrack after mistakes. It evaluates on both WebShop and amazon.com and shows stronger robustness than forward-only prompt baselines.

- [AutoDroid: LLM-powered Task Automation in Android](https://doi.org/10.1145/3636534.3649379)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - 🏛️ Institutions: Tsinghua, Harbin Institute of Technology, University of Notre Dame, Microsoft Research Asia
    - 📅 Date: August 29, 2023
    - 📑 Publisher: MobiCom 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [Android task automation], [dynamic analysis], [memory injection], [AutoDroid]
    - 📖 TLDR: AutoDroid is an Android task-automation framework that combines LLM commonsense with app-specific knowledge collected through automated dynamic analysis. It introduces functionality-aware UI representations and exploration-based memory injection, and evaluates the system on a 158-task benchmark for memory-augmented Android automation.

- [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://openreview.net/forum?id=9JQtrumvg8)
    - Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust
    - 🏛️ Institutions: Google DeepMind, The University of Tokyo
    - 📅 Date: July 24, 2023
    - 📑 Publisher: ICLR 2024 (Oral)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [HTML-T5], [program synthesis], [WebAgent]
    - 📖 TLDR: WebAgent is a modular real-world web agent that decomposes instructions into sub-instructions, summarizes long HTML into task-relevant snippets, and executes generated Python programs on websites. The paper pairs that agent design with HTML-T5, a long-context model for HTML planning and summarization.

- [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://openreview.net/forum?id=Pc8AU1aF5e)
    - Longtao Zheng, Rundong Wang, Xinrun Wang, Bo An
    - 🏛️ Institutions: NTU
    - 📅 Date: June 13, 2023
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [trajectory prompting], [state abstraction], [memory retrieval], [Synapse]
    - 📖 TLDR: Presents Synapse, a computer-control framework that uses trajectory exemplars plus memory retrieval to guide action selection on long multi-step tasks. Its main contribution is to show that state abstraction and exemplar retrieval can make prompting-based computer agents much more stable.

- [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0ff30c4bf31db0119a6219e0d250e037-Abstract-Conference.html)
    - Hongxin Li, Jingran Su, Yuntao Chen, Qing Li, Zhaoxiang Zhang
    - 🏛️ Institutions: University of Chinese Academy of Sciences, Hong Kong Institute of Science and Innovation, CAS, PolyU, Shanghai AI Laboratory
    - 📅 Date: May 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [spreadsheet automation], [state machine planning], [SheetCopilot]
    - 📖 TLDR: SheetCopilot studies spreadsheet control with an LLM agent that plans over a state-machine abstraction of spreadsheet operations. The paper also releases a 221-task spreadsheet-control dataset and an automated evaluation pipeline for benchmarking software-control performance.

- [META-GUI: Towards Multi-modal Conversational Agents on Mobile GUI](https://aclanthology.org/2022.emnlp-main.449/)
    - Liangtai Sun, Xingyu Chen, Lu Chen, Tianle Dai, Zichen Zhu, Kai Yu
    - 🏛️ Institutions: SJTU
    - 📅 Date: May 23, 2022
    - 📑 Publisher: EMNLP 2022
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [task-oriented dialogue], [GUI-TOD], [META-GUI]
    - 📖 TLDR: META-GUI introduces a GUI-based task-oriented dialogue architecture in which the assistant acts on real mobile apps instead of calling task-specific backend APIs. The paper also releases a dataset for training multimodal conversational agents under that GUI-TOD setup.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://aclanthology.org/2021.naacl-main.80/)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - 🏛️ Institutions: Stanford, Viv Labs, Samsung Research
    - 📅 Date: March 30, 2021
    - 📑 Publisher: NAACL 2021
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [ThingTalk], [RUSS], [web support tasks]
    - 📖 TLDR: This paper introduces RUSS, a system for executing open-domain customer-support instructions on websites by parsing them into a ThingTalk representation and grounding webpage elements. It also contributes a dataset of 80 support problems with 741 step-by-step instructions and their corresponding actions.

- [Interactive Task Learning from GUI-Grounded Natural Language Instructions and Demonstrations](https://aclanthology.org/2020.acl-demos.25/)
    - Toby Jia-Jun Li, Tom Mitchell, Brad Myers
    - 🏛️ Institutions: CMU
    - 📅 Date: July 31, 2020
    - 📑 Publisher: ACL 2020 Demo Track
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [SUGILITE], [interactive task learning], [programming-by-demonstration], [concept learning]
    - 📖 TLDR: This demo paper presents an interactive version of Sugilite in which users teach Android automation tasks through natural-language instructions plus GUI demonstrations. Its focus is learning reusable task procedures and concepts through conversational clarification grounded in app interfaces.

- [PUMICE: A Multi-Modal Agent that Learns Concepts and Conditionals from Natural Language and Demonstrations](https://dl.acm.org/doi/10.1145/3332165.3347899)
    - Toby Jia-Jun Li, Marissa Radensky, Justin Jia, Kirielle Singarajah, Tom M. Mitchell, Brad A. Myers
    - 🏛️ Institutions: CMU, Amherst College
    - 📅 Date: August 30, 2019
    - 📑 Publisher: UIST 2019
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [PUMICE], [programming-by-demonstration], [concept learning], [conditional automation]
    - 📖 TLDR: PUMICE is an end-user programmable mobile agent that combines natural-language programming with programming-by-demonstration. Its core contribution is a multimodal teaching loop where users resolve ambiguous concepts and conditions through conversation plus GUI demonstrations.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://openreview.net/forum?id=ryTp3f-0-)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Stanford
    - 📅 Date: February 24, 2018
    - 📑 Publisher: ICLR 2018 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [workflow-guided exploration], [MiniWoB]
    - 📖 TLDR: This paper introduces workflow-guided exploration, where demonstrations are converted into high-level workflows that constrain web-agent exploration during RL. It shows that this makes sparse-reward web interaction much more sample-efficient than pure behavioral cloning on World of Bits style tasks.

- [SUGILITE: Creating Multimodal Smartphone Automation by Demonstration](https://dl.acm.org/doi/abs/10.1145/3025453.3025483)
    - Toby Jia-Jun Li, Amos Azaria, Brad A. Myers
    - 🏛️ Institutions: CMU, Ariel University
    - 📅 Date: May 06, 2017
    - 📑 Publisher: CHI 2017
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [SUGILITE], [programming-by-demonstration], [Android accessibility API], [smartphone automation]
    - 📖 TLDR: Sugilite is an early smartphone automation system that lets users teach tasks by demonstrating actions inside ordinary Android apps. It combines verbal instructions, recorded procedures, and app UI hierarchies to generalize from a single demonstration and handle later UI variation.
