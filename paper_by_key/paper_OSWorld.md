# Papers with Keyword: OSWorld

- [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/abs/2603.26266)
    - Rui Xie, Zhi Gao, Chenrui Shi, Zirui Shang, Lu Chen, Qing Li
    - 🏛️ Institutions: SJTU, State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing Institute of Technology
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [video retrieval], [automatic annotation], [domain bias], [training-free], [OSWorld], [GUIDE]
    - 📖 TLDR: GUIDE is a training-free add-on for desktop GUI agents that retrieves relevant tutorial videos, turns them into planning and grounding annotations, and injects that expertise into existing agents without changing model parameters. On OSWorld, it improves multiple agent families while also reducing execution steps.

- [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995)
    - Sizhe Tang, Rongqian Chen, Tian Lan
    - 🏛️ Institutions: George Washington University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [test-time compute], [tree search], [MCTS], [alpha-UCT], [OSWorld], [Agent Alpha]
    - 📖 TLDR: Agent Alpha applies step-level MCTS with alpha-UCT exploration, comparison-based evaluation, and diversity-aware expansion to computer-use agents. It improves OSWorld performance substantially over trajectory-level sampling under similar compute.

- [Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction](https://arxiv.org/abs/2602.00575)
    - Chaoqun Cui, Jing Huang, Shijing Wang, Liming Zheng, Qingchao Kong, Zhixiong Zeng
    - 🏛️ Institutions: Institute of Automation, CAS, University of Chinese Academy of Sciences, Meituan, Beijing Jiaotong University
    - 📅 Date: January 31, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward modeling], [verification], [proactive interaction], [VAGEN], [OSWorld], [AndroidWorld]
    - 📖 TLDR: VAGEN turns GUI-agent verification into an active interaction problem, using a verifier agent to probe the environment for evidence of task completion instead of relying on passive judgment. This substantially improves verification accuracy on OSWorld and AndroidWorld.

- [BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://arxiv.org/abs/2601.21352)
    - Ziyu Lu, Tengjin Weng, Yiying Yang, Yuhang Zhao, Xinxin Huang, Wenhao Jiang
    - 🏛️ Institutions: Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shenzhen University, Guangdong University of Technology
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [backtracking], [DFS planning], [task tracking], [error recovery], [OSWorld], [BEAP-Agent]
    - 📖 TLDR: BEAP-Agent formulates long-horizon GUI execution as depth-first search and adds explicit multi-level backtracking when the agent commits to a wrong exploration branch. Its Planner, Executor, and Tracker jointly support state rollback and task updates, improving recovery on OSWorld.

- [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)
    - Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu
    - 🏛️ Institutions: Meituan, Fudan, Tongji University, HKUST
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [framework], [synthetic experience], [verifiable synthesis], [OSWorld], [EvoCUA]
    - 📖 TLDR: EvoCUA replaces static imitation with an evolving training loop built on verifiable task synthesis, high-throughput sandbox rollouts, and iterative policy optimization from both successful and failed trajectories. On OSWorld it reaches 56.7% success, outperforming prior open-source computer-use agents and even some leading closed-weight systems.

- [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)
    - Hanna Foerster, Tom Blanchard, Kristina Nikolić, Ilia Shumailov, Cheng Zhang, Robert Mullins, Nicolas Papernot, Florian Tramèr, Yiren Zhao
    - 🏛️ Institutions: University of Cambridge, University of Toronto, Vector Institute, ETH, AI Sequrity Company
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [Single-Shot Planning], [Branch Steering], [OSWorld], [CaMeLs]
    - 📖 TLDR: This paper adapts the Dual-LLM security paradigm to computer-use agents through Single-Shot Planning, where a trusted planner writes a full branching execution graph before seeing untrusted UI content. That gives control-flow integrity against injected instructions, but the paper also identifies Branch Steering as a remaining data-flow threat and studies its tradeoff with utility on OSWorld.

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu
    - 🏛️ Institutions: NJU, PKU, Microsoft Research Asia
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [RLVR], [off-policy assimilation], [BEPA], [OSWorld]
    - 📖 TLDR: BEPA improves end-to-end GUI-agent training with verifiable rewards by turning scarce off-policy expert traces into policy-aligned guidance through self-rolled reachable trajectories and a dynamically updated per-task cache. On OSWorld-Verified it raises UI-TARS-1.5-7B from 22.87% to 32.13%, with additional gains on MMBench-GUI and Online-Mind2Web.

- [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892)
    - Kai Mei, Jiang Guo, Shuaichen Chang, Mingwen Dong, Dongkyu Lee, Xing Niu, Jiarong Jiang
    - 🏛️ Institutions: Rutgers University, AWS Agentic AI
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [world model], [tutorial retrieval], [future state prediction], [OSWorld], [WebArena], [R-WoM]
    - 📖 TLDR: This paper tests whether LLMs can act as world models for computer-use agents and finds that simulation quality degrades sharply on full-procedure planning even when short-range prediction remains reasonable. R-WoM addresses this by grounding simulated rollouts with retrieved up-to-date tutorials, improving performance on OSWorld and WebArena, especially on longer-horizon tasks.

- [Watch and Learn: Learning to Use Computers from Online Videos](https://arxiv.org/abs/2510.04673)
    - Chan Hee Song, Yiwen Song, Palash Goyal, Yu Su, Oriana Riva, Hamid Palangi, Tomas Pfister
    - 🏛️ Institutions: Google Cloud AI Research, OSU
    - 📅 Date: October 06, 2025
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [video demonstrations], [inverse dynamics], [trajectory annotation], [OSWorld], [WindowsAgentArena], [Watch & Learn]
    - 📖 TLDR: Watch & Learn converts Internet videos of human computer use into more than 53K executable UI trajectories by framing annotation as an inverse dynamics problem over consecutive screen states. The resulting data improves both general-purpose and specialized CUAs on OSWorld and yields state-of-the-art 7B-scale performance on WindowsAgentArena under the 15-step limit.

- [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670)
    - Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
    - 🏛️ Institutions: Microsoft Research AI Frontiers, Microsoft AI Red Team, University of California, Riverside, NVIDIA
    - 📅 Date: October 02, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [blind goal-directedness], [safety benchmark], [OSWorld], [thought-action disconnect], [BLIND-ACT]
    - 📖 TLDR: This paper identifies Blind Goal-Directedness (BGD), where computer-use agents continue pursuing goals despite feasibility, safety, reliability, or context concerns. It introduces BLIND-ACT, a 90-task benchmark on OSWorld, and finds high average BGD rates across frontier models even after prompting-based mitigations.

- [Scaling Agents for Computer Use](https://arxiv.org/abs/2510.02250)
    - Gonzalo Gonzalez-Pumariega, Vincent Tu, Chih-Lun Lee, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: October 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [test-time scaling], [multiple rollouts], [behavior narratives], [behavior judge], [OSWorld], [BJudge]
    - 📖 TLDR: This paper argues that computer-use agents scale more effectively across multiple rollouts than within a single rollout, and introduces Behavior Judge (BJudge) to compare candidate trajectories via compact behavior narratives. BJudge reaches 72.6% on OSWorld, slightly surpassing reported human performance, and also generalizes to WindowsAgentArena and AndroidWorld.

- [Efficient Multi-turn RL for GUI Agents via Decoupled Training and Adaptive Data Curation](https://arxiv.org/abs/2509.23866)
    - Pengxiang Li, Zechen Hu, Zirui Shang, Jingrong Wu, Yang Liu, Hui Liu, Zhi Gao, Chenrui Shi, Bofei Zhang, Zihao Zhang, Xiaochuan Shi, Zedong YU, Yuwei Wu, Xinxiao Wu, Yunde Jia, Liuyu Xiang, Zhaofeng He, Qing Li
    - 🏛️ Institutions: Beijing Institute of Technology, State Key Laboratory of General Artificial Intelligence, BIGAI, DataCanvas, Beijing University of Posts and Telecommunications, Shenzhen MSU-BIT University
    - 📅 Date: September 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [reinforcement learning], [decoupled training], [adaptive data curation], [asynchronous modules], [OSWorld], [DART]
    - 📖 TLDR: DART is a decoupled RL training framework for GUI agents that separates environment execution, rollout service, data management, and training into asynchronous modules to improve multi-turn learning efficiency. It pairs that system design with adaptive data curation, including difficulty-aware rollout control and high-entropy step selection, and substantially improves OSWorld performance over the base model.

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua, Zhipu, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [API-GUI paradigm], [distributed RL infrastructure], [parallel virtual desktops], [Entropulse], [OSWorld], [ComputerRL]
    - 📖 TLDR: ComputerRL is a desktop-agent training framework that combines direct GUI interaction with programmatic APIs and scales online RL through a distributed infrastructure over thousands of parallel virtual desktops. Its Entropulse schedule alternates RL and supervised fine-tuning to stabilize long training runs, and the resulting GLM-ComputerRL-9B reaches 48.9% on OSWorld.

- [Evolving in Tasks: Empowering the Multi-modality Large Language Model as the Computer Use Agent](https://arxiv.org/abs/2508.04037)
    - Yuhao Cheng, Liang Tang, Shuxian Li, Yukang Huo, Tiaonan Duan, Kaer Huang, Yanzhe Jing, Yiqiang Yan
    - 🏛️ Institutions: Lenovo, China Agricultural University
    - 📅 Date: August 06, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [Self-Evolution Agent], [step-wise reinforcement learning], [grounding-based generalization enhancement], [temporal compressed sensing], [OSWorld]
    - 📖 TLDR: This paper proposes the Self-Evolution Agent (SEA) for computer use, combining automatic verifiable trajectory generation, efficient step-wise reinforcement learning, and a model-enhancement path that merges grounding and planning ability. It evaluates the resulting agent on grounding benchmarks and OSWorld and frames the method as a way to improve computer-use performance without relying purely on manually curated data.

- [CoAct-1: Computer-using Multi-Agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: USC, Salesforce AI Research, University of Washington
    - 📅 Date: August 05, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [coding actions], [programmer agent], [orchestrator], [OSWorld], [WindowsAgentArena], [CoAct-1]
    - 📖 TLDR: CoAct-1 augments desktop GUI control with direct Python and Bash execution by letting an orchestrator assign subtasks to either a GUI operator or a programmer agent. On OSWorld and WindowsAgentArena, this hybrid setup reduces brittle GUI-only action chains and improves both success rate and step efficiency.

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [MCP server], [environmental contextualization], [OSWorld], [LiteCUA]
    - 📖 TLDR: LiteCUA argues that computer-use agents need better environment contextualization rather than only larger models or heavier agent stacks. It introduces AIOS 1.0, which exposes computer states and actions through an MCP server, and shows that the resulting lightweight desktop agent outperforms several stronger baselines on OSWorld.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 01, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [mixture-of-grounding], [proactive hierarchical planning], [OSWorld], [WindowsAgentArena], [Agent S2]
    - 📖 TLDR: Agent S2 is a compositional generalist-specialist framework that splits computer-use responsibilities across specialized and generalist models rather than using a single monolithic agent. Its core methods are Mixture-of-Grounding for precise localization and Proactive Hierarchical Planning for long-horizon control, yielding strong gains on OSWorld, WindowsAgentArena, and AndroidWorld.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Tech, HKU, Stanford
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [attack], [adversarial pop-ups], [safety], [OSWorld], [VisualWebArena]
    - 📖 TLDR: Shows that vision-language computer agents can be reliably distracted by adversarial pop-ups that human users would typically ignore. On OSWorld and VisualWebArena, these pop-ups achieve high attack success rates and sharply reduce task completion, while simple defenses like warning prompts remain ineffective.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Jing Hua Toh, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: HKU, CMU, Salesforce AI Research, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [OSWorld], [real computer environment], [execution-based evaluation], [multi-app workflows]
    - 📖 TLDR: OSWorld provides a real computer environment and benchmark for open-ended tasks across Ubuntu, Windows, and macOS, with 369 tasks spanning real web apps, desktop apps, file I/O, and multi-application workflows. Its execution-based evaluation setup exposes a large gap between humans and current multimodal agents, with the best reported model reaching 12.24% task success versus 72.36% for humans.
