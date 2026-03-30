# Fei Huang's Papers

- [WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721)
    - Zikai Xiao, Jianhong Tu, Chuhang Zou, Yuxin Zuo, Zhi Li, Peng Wang, Bowen Yu, Fei Huang, Junyang Lin, Zuozhu Liu
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-02-16
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [world model], [simulator], [trajectory synthesis], [open-web]
    - 📖 TLDR: Large-scale web simulator (WebWorld) trained on 1M+ open-web interactions supporting 30+ step simulations, enabling trajectory synthesis and exhibiting cross-domain generalization to code, GUI, and game environments.

- [OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents](https://arxiv.org/abs/2510.24563)
    - Hongrui Jia, Jitong Liao, Xi Zhang, Haiyang Xu, Tianbao Xie, Chaoya Jiang, Ming Yan, Si Liu, Wei Ye, Fei Huang
    - 🏛️ Institutions: Peking University, Tongyi Lab, Alibaba Group, Beijing Zhongguancun Academy
    - 📅 Date: November 11, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [MCP], [tool-use], [computer-use agent], [OSWorld-MCP]
    - 📖 TLDR: This paper introduces OSWorld-MCP, the first benchmark specifically designed to evaluate tool invocation in computer-use agents alongside standard GUI interaction and decision-making. It builds a validated suite of 158 practical MCP tools across seven common applications and shows that tool access can substantially improve task success, while also revealing that current agents still invoke tools surprisingly rarely. The benchmark adds an important missing dimension to CUA evaluation by explicitly measuring real-world tool-usage capability.

- [AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/abs/2510.24699)
    - Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen Zhang, Zile Qiao, Xinyu Wang, Pengjun Xie, Fei Huang, Siheng Chen, Jingren Zhou, Yong Jiang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: 
    - 📖 TLDR: AgentFold introduces a web agent with proactive context management that dynamically condenses historical information at multiple scales, achieving 36.2% on BrowseComp while surpassing larger open-source models.

- [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)
    - Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, Zhengxi Lu, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: August 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [multi-agent], [GUI automation], [trajectory production], [TRPO]
    - 📖 TLDR: The paper introduces **GUI-Owl**, a foundational multimodal GUI agent model built on Qwen2.5-VL, integrating perception, grounding, reasoning, planning, and action execution into one policy network. GUI-Owl-7B achieves strong baseline performance (66.4 on AndroidWorld, 29.4 on OSWorld). The authors further propose **Mobile-Agent-v3**, a general-purpose, multi-agent GUI automation framework that builds on GUI-Owl and achieves state-of-the-art open-source results (73.3 on AndroidWorld, 37.7 on OSWorld). Core innovations include: a large-scale cross-platform cloud-based environment infrastructure with Self-Evolving GUI Trajectory Production; modular foundational agent capabilities; and scalable, asynchronous reinforcement learning using Trajectory-aware Relative Policy Optimization (TRPO). The framework is open-sourced at the X-PLUG MobileAgent GitHub repository.

- [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)
    - Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: May 28, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [information seeking], [reinforcement learning], [GAIA], [WebDancer]
    - 📖 TLDR: This paper presents WebDancer, an end-to-end web agent for autonomous information seeking built through a data-centric four-stage training pipeline: browsing data construction, trajectory sampling, supervised fine-tuning, and reinforcement learning. It targets long-horizon information-seeking problems rather than short templated web tasks. The resulting system achieves strong performance on GAIA and WebWalkerQA and offers a concrete recipe for training more capable research-style web agents.

- [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)
    - Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Deyu Zhou, Pengjun Xie, Fei Huang
    - 🏛️ Institutions: Tongyi Lab, Alibaba NLP
    - 📅 Date: January 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [RAG], [WebWalker], [WebWalkerQA]
    - 📖 TLDR: This paper presents **WebWalker**, a multi-agent framework designed to improve the ability of large language models (LLMs) to traverse websites, addressing the challenges of retrieving complex, multi-layered information. WebWalker integrates an "explore-critic" paradigm, where the explorer agent navigates the web, and the critic agent evaluates the progress. The **WebWalkerQA** benchmark is introduced to assess web traversal tasks, showing how retrieval-augmented generation (RAG) can be enhanced with vertical exploration to solve real-world queries.

- [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://openreview.net/forum?id=O0nBMRlkc8)
    - Junyang Wang, Haiyang Xu, Haitao Jia, Xi Zhang, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Alibaba Group, Beijing University of Posts and Telecommunications
    - 📅 Date: June 3, 2024
    - 📑 Publisher: NeurIPS 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [multi-agent], [planning], [decision-making], [reflection]
    - 📖 TLDR: The paper presents **Mobile-Agent-v2**, a multi-agent architecture designed to assist with mobile device operations. It comprises three agents: a planning agent that generates task progress, a decision agent that navigates tasks using a memory unit, and a reflection agent that corrects erroneous operations. This collaborative approach addresses challenges in navigation and long-context input scenarios, achieving over a 30% improvement in task completion compared to single-agent architectures.

- [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://openreview.net/forum?id=jE6pDYCnVF)
    - Junyang Wang, Haiyang Xu, Jiabo Ye, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Beijing Jiaotong University, Alibaba Group
    - 📅 Date: January 29, 2024
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark]
    - 📖 TLDR: This paper presents Mobile-Agent, an autonomous multi-modal agent designed for mobile device interaction. The system integrates visual perception, natural language processing, and action prediction to navigate and operate mobile applications. The authors introduce a new dataset and benchmark for evaluating mobile agents, demonstrating Mobile-Agent's superior performance in task completion and generalization across various apps compared to existing methods.
