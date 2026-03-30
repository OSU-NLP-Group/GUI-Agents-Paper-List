# Papers with Keyword: OSWorld

- [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)
    - Thomas Kuntz, Agatha Duzan, Hao Zhao, Francesco Croce, J Zico Kolter, Nicolas Flammarion, Maksym Andriushchenko
    - 🏛️ Institutions: EPFL, Carnegie Mellon University
    - 📅 Date: October 29, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets and Benchmarks Track Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer-use agent], [prompt injection], [OSWorld], [OS-Harm]
    - 📖 TLDR: This paper introduces OS-Harm, a safety benchmark for computer-use agents built on top of OSWorld. It covers 150 tasks spanning deliberate misuse, prompt injection, and model misbehavior across applications such as browsers, editors, and email clients, and includes an automated judge for both safety and task correctness. Evaluations show that current frontier agents often comply with harmful requests, remain vulnerable to prompt injection, and can execute unsafe actions in realistic computer-use settings.

- [CoAct‑1: Computer‑using Multi-agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: USC, Salesforce, UW
    - 📅 Date: August 5, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hybrid agent], [coding action], [multi-agent system], [OSWorld]
    - 📖 TLDR: This paper introduces **CoAct‑1**, a multi-agent system where an Orchestrator coordinates between a GUI Operator and a Programmer agent that can execute code (Python/Bash) directly. This hybrid design allows the agent to perform complex desktop tasks more efficiently than GUI-only agents. Evaluated on OSWorld and WindowsAgentArena, CoAct‑1 achieves state-of-the-art success rates of 60.8% and 52.5% respectively, while reducing average steps to 10.15.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, and Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS
    - 📅 Date: June 4, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multilingual], [safety], [macOSWorld]
    - 📖 TLDR: Introduces **macOSWorld**, the first interactive benchmark for GUI agents on macOS, with 202 tasks across 30 apps (28 macOS-exclusive) in 5 languages plus a safety subset for deception attacks; evaluates 6 agents, showing proprietary CUAs outperform open-source and VLM-based agents, significant language gaps (Arabic –27.5%), and both grounding and safety challenges.

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

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://osworld-grounding.github.io/)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [framework], [Jedi], [OSWorld‑G], [GUI grounding], [compositional generalization], [fine‑grained manipulation]
    - 📖 TLDR: This work tackles limitations in GUI grounding by introducing **OSWorld‑G**, a 564‑sample benchmark covering text matching, element recognition, layout understanding, fine‑grained manipulation, and refusal detection. They also synthesize **Jedi**, a massive 4 M‑example dataset generated via UI decomposition and synthesis. Training multi‑scale models on Jedi achieves state‑of‑the‑art grounding across benchmarks (ScreenSpot‑v2/Pro and OSWorld‑G), boosting agentic task performance from 5 % to ~27 % success. Ablations demonstrate compositional benefits. All artifacts are publicly released.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://arxiv.org/abs/2504.00906)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [Mixture-of-Grounding], [Proactive Hierarchical Planning], [benchmark], [OSWorld], [WindowsAgentArena], [AndroidWorld]
    - 📖 TLDR: This paper introduces *Agent S2*, a compositional framework for computer use agents that combines generalist and specialist models to address challenges in GUI element grounding and long-horizon task planning. The framework employs a novel Mixture-of-Grounding technique for precise GUI localization and Proactive Hierarchical Planning to dynamically refine action plans. Evaluations demonstrate that Agent S2 achieves state-of-the-art performance on benchmarks like OSWorld, WindowsAgentArena, and AndroidWorld, outperforming existing agents such as Claude Computer Use and UI-TARS.

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: XJTU, Shanghai AI Lab, HKU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [multi-agent systems], [specialized generalist agent], [OSWorld benchmark]
    - 📖 TLDR: AgentStore introduces a scalable platform to integrate and manage heterogeneous agents, designed to enhance generalist assistant capabilities for diverse computer tasks. Using a MetaAgent and AgentToken strategy, AgentStore shows improved generalization on the OSWorld benchmark.
