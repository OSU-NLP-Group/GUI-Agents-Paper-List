# Papers with Keyword: computer-use agent

- [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235)
    - Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, LawZero, Mila - Quebec AI Institute, Universite de Montreal, University of California, Berkeley
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [safety], [red teaming], [unintended behavior], [computer-use agent], [AutoElicit]
    - 📖 TLDR: This paper studies unsafe unintended behaviors in computer-use agents under benign user inputs rather than adversarial prompts. It introduces AutoElicit, an agentic framework that iteratively perturbs realistic benign instructions using execution feedback to surface severe harmful behaviors in frontier CUAs. The results show that even strong CUAs remain broadly susceptible to harmful deviations, establishing a concrete framework for systematically probing unintended safety failures in realistic computer-use settings.

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

- [VideoAgentTrek: Computer Use Pretraining from Unlabeled Videos](https://arxiv.org/abs/2510.19488)
    - Dunjie Lu, Yiheng Xu, Junli Wang, Haoyuan Wu, Xinyuan Wang, Zekun Wang, Junlin Yang, Hongjin Su, Jixuan Chen, Junda Chen, Yuchen Mao, Jingren Zhou, Junyang Lin, Binyuan Hui, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Qwen Team, Alibaba Group
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [pretraining], [computer-use agent], [video mining], [inverse dynamics], [OSWorld-Verified], [VideoAgentTrek], [Video2Action]
    - 📖 TLDR: This paper introduces VideoAgentTrek, a scalable pipeline that converts unlabeled screen-recorded videos into structured computer-use trajectories for pretraining GUI agents. Its Video2Action inverse-dynamics module first localizes GUI actions in time and then recovers structured action parameters such as click coordinates and typed text. Mining 39,000 YouTube tutorials yields 1.52 million interaction steps, and using this data for continued pretraining substantially improves downstream performance on OSWorld-Verified and AgentNetBench.

- [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892)
    - Kai Mei, Jiang Guo, Shuaichen Chang, Mingwen Dong, Dongkyu Lee, Xing Niu, Jiarong Jiang
    - 🏛️ Institutions: Rutgers University, AWS Agentic AI
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [world model], [retrieval-augmented planning], [computer-use agent], [OSWorld], [WebArena], [R-WoM]
    - 📖 TLDR: This paper studies whether LLMs can reliably serve as world models for computer-use agents and finds that their simulations degrade sharply over long-horizon procedures despite reasonable short-range predictions. To address this, it proposes R-WoM, a retrieval-augmented world model that grounds planning with up-to-date external tutorials. R-WoM improves planning quality on OSWorld and WebArena, with especially strong gains on longer-horizon tasks where ungrounded simulation is most brittle.

- [AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents](https://arxiv.org/abs/2506.14205)
    - Jingxu Xie, Dylan Xu, Xuandong Zhao, Dawn Song
    - 🏛️ Institutions: University of California, Berkeley
    - 📅 Date: June 17, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [synthetic data], [task generation], [computer-use agent], [long-horizon task], [AgentSynth]
    - 📖 TLDR: This paper introduces AgentSynth, a scalable pipeline for automatically generating high-quality tasks and trajectory datasets for generalist computer-use agents. By exploiting information asymmetry between generation and evaluation, it composes simple subtasks into difficult long-horizon tasks and produces more than 6,000 diverse tasks at low cost. The resulting benchmark exposes steep performance degradation in current state-of-the-art agents as task difficulty increases and provides a scalable alternative to expensive human-collected trajectories.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [computer-use agent], [OSWorld], [RiOSWorld]
    - 📖 TLDR: This paper introduces RiOSWorld, a benchmark for evaluating safety risks in multimodal computer-use agents during realistic computer manipulation. It covers 492 risky tasks across applications such as web, social media, multimedia, email, office software, and operating-system interactions, and evaluates both harmful intent and harmful task completion. The benchmark shows that current computer-use agents remain exposed to substantial real-world safety risks even when they are aligned for ordinary dialogue settings.

- [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)
    - Lukas Aichberger, Alasdair Paren, Guohao Li, Philip Torr, Yarin Gal, Adel Bibi
    - 🏛️ Institutions: Johannes Kepler University Linz, University of Oxford
    - 📅 Date: March 13, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [security], [adversarial attacks], [computer-use agent], [OS agent], [MIP against Agent]
    - 📖 TLDR: This paper identifies Malicious Image Patches as a new attack vector against multimodal OS agents, where adversarially perturbed visual regions on the screen can trigger harmful actions when captured by the agent. The attack generalizes across prompts and screen setups, showing that benign-looking visual content such as wallpapers or social media images can hijack computer-use agents. The paper exposes a concrete security weakness in OS-level agents that goes beyond text-only prompt injection.

- [Programming with Pixels: Can Computer-Use Agents do Software Engineering?](https://arxiv.org/abs/2502.18525)
    - Pranjal Aggarwal, Sean Welleck
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: February 24, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [environment], [computer-use agent], [software engineering], [tool-use], [PwP], [PwP-Bench]
    - 📖 TLDR: This paper introduces Programming with Pixels, a visual IDE environment for evaluating whether generalist computer-use agents can handle software engineering tasks rather than only simple desktop or web interactions. It also presents PwP-Bench, a benchmark spanning 15 software-engineering tasks across languages and modalities. The results show that purely visual computer-use agents lag behind specialist coding agents, but narrow text APIs such as file editing and bash dramatically narrow that gap.
