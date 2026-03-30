# Papers with Keyword: OSWorld

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
    - 🏛️ Institutions: University of Cambridge, University of Toronto & Vector Institute, ETH Zurich, AI Sequrity Company
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [Single-Shot Planning], [Branch Steering], [OSWorld]
    - 📖 TLDR: This paper studies system-level security for computer-use agents under prompt injection attacks. It introduces Single-Shot Planning, where a trusted planner produces a full execution graph with conditional branches before the agent observes potentially malicious content, giving provable control-flow integrity against injected instructions. The paper also identifies Branch Steering as an additional attack surface and shows on OSWorld that strong security guarantees can be achieved while retaining meaningful utility.

- [OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents](https://arxiv.org/abs/2510.24563)
    - Hongrui Jia, Jitong Liao, Xi Zhang, Haiyang Xu, Tianbao Xie, Chaoya Jiang, Ming Yan, Si Liu, Wei Ye, Fei Huang
    - 🏛️ Institutions: Peking University, Tongyi Lab, Alibaba Group, Beijing Zhongguancun Academy
    - 📅 Date: November 11, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [MCP], [tool-use], [computer-use agent], [OSWorld-MCP]
    - 📖 TLDR: This paper introduces OSWorld-MCP, the first benchmark specifically designed to evaluate tool invocation in computer-use agents alongside standard GUI interaction and decision-making. It builds a validated suite of 158 practical MCP tools across seven common applications and shows that tool access can substantially improve task success, while also revealing that current agents still invoke tools surprisingly rarely. The benchmark adds an important missing dimension to CUA evaluation by explicitly measuring real-world tool-usage capability.

- [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)
    - Thomas Kuntz, Agatha Duzan, Hao Zhao, Francesco Croce, J Zico Kolter, Nicolas Flammarion, Maksym Andriushchenko
    - 🏛️ Institutions: EPFL, Carnegie Mellon University
    - 📅 Date: October 29, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets and Benchmarks Track Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer-use agent], [prompt injection], [OSWorld], [OS-Harm]
    - 📖 TLDR: This paper introduces OS-Harm, a safety benchmark for computer-use agents built on top of OSWorld. It covers 150 tasks spanning deliberate misuse, prompt injection, and model misbehavior across applications such as browsers, editors, and email clients, and includes an automated judge for both safety and task correctness. Evaluations show that current frontier agents often comply with harmful requests, remain vulnerable to prompt injection, and can execute unsafe actions in realistic computer-use settings.

- [Scaling Computer-Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research
    - 📅 Date: October 24, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets and Benchmarks Track)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [GUI grounding], [computer-use grounding], [OSWorld-G], [JEDI]
    - 📖 TLDR: This paper tackles GUI grounding as a core bottleneck for computer-use agents by introducing OSWorld-G, a benchmark of complex grounding tasks that go beyond short referring expressions, and JEDI, a 4 million-example synthetic grounding dataset built through multi-perspective task decomposition. Models trained on JEDI outperform prior grounding approaches across ScreenSpot-style benchmarks and substantially improve downstream agent performance on OSWorld. The work is directly relevant because it shows that scaling specialized GUI grounding data can materially lift full computer-use agent capability.

- [VideoAgentTrek: Computer Use Pretraining from Unlabeled Videos](https://arxiv.org/abs/2510.19488)
    - Dunjie Lu, Yiheng Xu, Junli Wang, Haoyuan Wu, Xinyuan Wang, Zekun Wang, Junlin Yang, Hongjin Su, Jixuan Chen, Junda Chen, Yuchen Mao, Jingren Zhou, Junyang Lin, Binyuan Hui, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Qwen Team, Alibaba Group
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [pretraining], [computer-use agent], [video mining], [inverse dynamics], [OSWorld-Verified], [VideoAgentTrek], [Video2Action]
    - 📖 TLDR: This paper introduces VideoAgentTrek, a scalable pipeline that converts unlabeled screen-recorded videos into structured computer-use trajectories for pretraining GUI agents. Its Video2Action inverse-dynamics module first localizes GUI actions in time and then recovers structured action parameters such as click coordinates and typed text. Mining 39,000 YouTube tutorials yields 1.52 million interaction steps, and using this data for continued pretraining substantially improves downstream performance on OSWorld-Verified and AgentNetBench.

- [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790)
    - Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple, The University of Hong Kong
    - 📅 Date: October 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [tool-use], [hybrid action], [reinforcement learning], [OSWorld], [WindowsAgentArena], [UltraCUA]
    - 📖 TLDR: This paper introduces UltraCUA, a foundation model for computer-use agents that combines low-level GUI actions with high-level programmatic tool calls through a hybrid action space. To support this setting, the authors build an automated tool-collection pipeline, synthesize 17,000+ verifiable computer-use tasks, and train 7B and 32B models with supervised fine-tuning followed by online reinforcement learning. UltraCUA improves OSWorld performance by 22% relative on average while reducing steps, and it also generalizes strongly to WindowsAgentArena without Windows-specific training.

- [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892)
    - Kai Mei, Jiang Guo, Shuaichen Chang, Mingwen Dong, Dongkyu Lee, Xing Niu, Jiarong Jiang
    - 🏛️ Institutions: Rutgers University, AWS Agentic AI
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [world model], [retrieval-augmented planning], [computer-use agent], [OSWorld], [WebArena], [R-WoM]
    - 📖 TLDR: This paper studies whether LLMs can reliably serve as world models for computer-use agents and finds that their simulations degrade sharply over long-horizon procedures despite reasonable short-range predictions. To address this, it proposes R-WoM, a retrieval-augmented world model that grounds planning with up-to-date external tutorials. R-WoM improves planning quality on OSWorld and WebArena, with especially strong gains on longer-horizon tasks where ungrounded simulation is most brittle.

- [CoAct‑1: Computer‑using Multi-agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: University of Southern California, Salesforce Research, University of Washington
    - 📅 Date: August 5, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hybrid agent], [coding action], [multi-agent system], [OSWorld]
    - 📖 TLDR: This paper introduces **CoAct‑1**, a multi-agent system where an Orchestrator coordinates between a GUI Operator and a Programmer agent that can execute code (Python/Bash) directly. This hybrid design allows the agent to perform complex desktop tasks more efficiently than GUI-only agents. Evaluated on OSWorld and WindowsAgentArena, CoAct‑1 achieves state-of-the-art success rates of 60.8% and 52.5% respectively, while reducing average steps to 10.15.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, and Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: June 4, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multilingual], [safety], [macOSWorld]
    - 📖 TLDR: Introduces **macOSWorld**, the first interactive benchmark for GUI agents on macOS, with 202 tasks across 30 apps (28 macOS-exclusive) in 5 languages plus a safety subset for deception attacks; evaluates 6 agents, showing proprietary CUAs outperform open-source and VLM-based agents, significant language gaps (Arabic –27.5%), and both grounding and safety challenges.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [computer-use agent], [OSWorld], [RiOSWorld]
    - 📖 TLDR: This paper introduces RiOSWorld, a benchmark for evaluating safety risks in multimodal computer-use agents during realistic computer manipulation. It covers 492 risky tasks across applications such as web, social media, multimedia, email, office software, and operating-system interactions, and evaluates both harmful intent and harmful task completion. The benchmark shows that current computer-use agents remain exposed to substantial real-world safety risks even when they are aligned for ordinary dialogue settings.

- [UI-Evol: Automatic Knowledge Evolving for Computer Use Agents](https://arxiv.org/abs/2505.21964)
    - Ziyun Zhang, Xinyi Liu, Xiaoyi Zhang, Jun Wang, Gang Chen, Yan Lu
    - 🏛️ Institutions: Peking University, Microsoft Research Asia
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [knowledge-execution gap], [Critique Stage], [Retrace Stage], [OSWorld], [self‑evolution]
    - 📖 TLDR: The paper identifies a “knowledge‑execution gap” where even highly accurate external knowledge (90%) only yields a 41% execution success rate. To bridge this, the authors introduce **UI‑Evol**, a plug‑and‑play two‑stage module for GUI agents—**Retrace** recovers actual action sequences from real agent–environment interactions, and **Critique** refines knowledge by comparing these sequences with external references. Experiments using Agent S2 on the OSWorld benchmark show significant gains in task performance and reduced behavioral variance, improving agent reliability.

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, and Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [model context protocol], [MCP], [OSWorld], [LiteCUA]
    - 📖 TLDR: Introduces AIOS 1.0, which contextualizes desktop computer states via an MCP server so LLM-powered agents can better understand and operate GUIs. Built on top, LiteCUA—a lightweight agent—achieves 14.66 % success on the OSWorld benchmark, outperforming several heavier agent frameworks, showing the benefits of environment contextualization.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets and Benchmarks Track (Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [framework], [Jedi], [OSWorld‑G], [GUI grounding], [compositional generalization], [fine‑grained manipulation]
    - 📖 TLDR: This work tackles limitations in GUI grounding by introducing **OSWorld‑G**, a 564‑sample benchmark covering text matching, element recognition, layout understanding, fine‑grained manipulation, and refusal detection. They also synthesize **Jedi**, a massive 4 M‑example dataset generated via UI decomposition and synthesis. Training multi‑scale models on Jedi achieves state‑of‑the‑art grounding across benchmarks (ScreenSpot‑v2/Pro and OSWorld‑G), boosting agentic task performance from 5 % to ~27 % success. Ablations demonstrate compositional benefits. All artifacts are publicly released.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 1, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [Mixture-of-Grounding], [Proactive Hierarchical Planning], [benchmark], [OSWorld], [WindowsAgentArena], [AndroidWorld]
    - 📖 TLDR: This paper introduces *Agent S2*, a compositional framework for computer use agents that combines generalist and specialist models to address challenges in GUI element grounding and long-horizon task planning. The framework employs a novel Mixture-of-Grounding technique for precise GUI localization and Proactive Hierarchical Planning to dynamically refine action plans. Evaluations demonstrate that Agent S2 achieves state-of-the-art performance on benchmarks like OSWorld, WindowsAgentArena, and AndroidWorld, outperforming existing agents such as Claude Computer Use and UI-TARS.

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Shanghai AI Laboratory, The University of Hong Kong
    - 📅 Date: October 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [multi-agent systems], [specialized generalist agent], [OSWorld benchmark]
    - 📖 TLDR: AgentStore introduces a scalable platform to integrate and manage heterogeneous agents, designed to enhance generalist assistant capabilities for diverse computer tasks. Using a MetaAgent and AgentToken strategy, AgentStore shows improved generalization on the OSWorld benchmark.
