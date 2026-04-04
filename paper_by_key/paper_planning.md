# Papers with Keyword: planning

- [Web Verbs: Typed Abstractions for Reliable Task Composition on the Agentic Web](https://arxiv.org/abs/2602.17245)
    - Linxi Jiang, Rui Xi, Zhijie Liu, Shuo Chen, Zhiqiang Lin, Suman Nath
    - 🏛️ Institutions: The Ohio State University, University of British Columbia, Microsoft Research
    - 📅 Date: February 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [tool-use], [typed action abstraction], [agentic web], [web verbs]
    - 📖 TLDR: This paper argues that web agents need a semantic action layer above brittle low-level clicks and keystrokes, and proposes Web Verbs as typed, composable web actions with explicit contracts, policies, and logging support. The abstraction unifies API-based and browser-based execution into stable callable units that agents can discover and compose into short programs. Through a proof-of-concept implementation and case studies, the paper positions typed web actions as a route to more reliable, efficient, and verifiable web agents.

- [IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/abs/2602.17049)
    - Seoyoung Lee, Seobin Yoon, Seongbeen Lee, Yoojung Chun, Dayoung Park, Doyeon Kim, Joo Yong Sim
    - 🏛️ Institutions: Sookmyung Women’s University
    - 📅 Date: February 19, 2026
    - 📑 Publisher: AAMAS 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [multi-agent], [memory], [planning], [skill abstraction], [intent representation], [IntentCUA]
    - 📖 TLDR: Uses intent-aligned plan memory to stabilize long-horizon desktop automation, with a Planner, Plan-Optimizer, and Critic coordinating over shared abstractions of past interaction traces. By retrieving intent-matched reusable skills instead of repeatedly replanning from scratch, IntentCUA improves both task success and step efficiency over RL-based and trajectory-centric baselines.

- [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662)
    - Deyang Jiang, Jing Huang, Xuanle Zhao, Lei Chen, Liming Zheng, Fanfan Liu, Haibo Qiu, Peng Shi, Zhixiong Zeng
    - 🏛️ Institutions: Meituan
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [planning], [multi-agent], [synthetic trajectory generation], [TreeCUA], [TreeCUA-DPO]
    - 📖 TLDR: This paper targets the scaling bottleneck of GUI planning rather than GUI grounding. It introduces TreeCUA, a multi-agent framework that organizes large-scale GUI exploration trajectories as reusable tree structures, reducing redundant exploration while improving trajectory quality through verification, summarization, and evaluation. The work further proposes TreeCUA-DPO to learn planning from adjacent branch information, yielding strong gains and improved out-of-domain generalization.

- [SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization](https://arxiv.org/abs/2601.22491)
    - Jinyang Wu, Changpeng Yang, Yuhao Shen, Wentao Zhang, Gang Pan
    - 🏛️ Institutions: Tsinghua University, Xiaomi Corporation, Zhejiang University, Nanyang Technological University, Institute of Automation Chinese Academy of Sciences
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [reward shaping], [GUI grounding], [planning], [training framework]
    - 📖 TLDR: SSL (Sweet Spot Learning) introduces a tiered reward framework for reinforcement learning that replaces binary rewards with progressively amplified, quality-ordered rewards to guide agent policies toward optimal solution regions. Evaluated across GUI perception, short/long-term planning, and complex reasoning tasks, SSL achieves up to 2.5x sample efficiency gains over binary reward baselines on 12 benchmarks.

- [BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://arxiv.org/abs/2601.21352)
    - Ziyu Lu, Tengjin Weng, Yiying Yang, Hanchu Zhou, Kenji Kawaguchi
    - 🏛️ Institutions: Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shenzhen University, Guangdong University of Technology
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [backtracking], [DFS], [planning], [error recovery], [OSWorld]
    - 📖 TLDR: BEAP-Agent models long-horizon GUI execution as depth-first search and adds a systematic multi-level backtracking mechanism for recovering from wrong exploration paths. Its Planner, Executor, and Tracker coordinate both execution and task-state updates, and the paper validates the value of explicit backtracking on OSWorld.

- [MobileDreamer: Generative Sketch World Model for GUI Agent](https://arxiv.org/abs/2601.04035)
    - Yilin Cao, Yufeng Zhong, Zhixiong Zeng, Liming Zheng, Jing Huang, Haibo Qiu, Peng Shi, Wenji Mao, Wan Guanglu
    - 🏛️ Institutions: State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences, School of Artificial Intelligence, University of Chinese Academy of Sciences, Meituan
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [planning], [lookahead], [MobileDreamer]
    - 📖 TLDR: This paper introduces MobileDreamer, a world-model-based lookahead framework for mobile GUI agents that predicts compact task-relevant future interface sketches rather than full screenshots. Its textual sketch world model preserves spatial information while remaining efficient, and its rollout imagination strategy uses these predicted futures to improve action selection on long-horizon tasks. On AndroidWorld, MobileDreamer achieves state-of-the-art performance and improves task success by 5.25%, showing that lightweight future imagination can materially strengthen mobile GUI planning.

- [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014)
    - Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover
    - 🏛️ Institutions: UCLA, Panasonic AI Research, Salesforce AI Research
    - 📅 Date: December 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [world model], [semantic state transition], [planning], [MobileWorldBench], [MobileWorld]
    - 📖 TLDR: MobileWorldBench studies mobile world modeling through language-described state transitions instead of pixel prediction. It benchmarks vision-language models as mobile world models, releases a 1.4M-sample MobileWorld training set, and shows that these semantic world models can directly improve downstream mobile-agent planning.

- [WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment](https://arxiv.org/abs/2512.12692)
    - Mahir Labib Dihan, Tanzima Hashem, Mohammed Eunus Ali, Md Rizwan Parvez
    - 🏛️ Institutions: Department of Computer Science and Engineering, Bangladesh University of Engineering and Technology (BUET), Faculty of Information Technology, Monash University, Qatar Computing Research Institute (QCRI)
    - 📅 Date: December 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [search algorithm], [LLM], [WebArena], [planning]
    - 📖 TLDR: WebOperator is a tree-search framework for web agents that enables safe backtracking and strategic exploration through best-first search with action-aware safety ranking, achieving state-of-the-art 54.6% success rate on WebArena with GPT-4o.

- [WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation](https://arxiv.org/abs/2510.22732)
    - Jiali Cheng, Anjishnu Kumar, Roshan Lal, Rishi Rajasekaran, Hani Ramezani, Omar Zia Khan, Oleg Rokhlenko, Sunny Chiu-Webster, Gang Hua, Hadi Amiri
    - 🏛️ Institutions: University of Massachusetts Lowell, Amazon Alexa AI
    - 📅 Date: October 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agent framework], [memory], [planning], [WebArena]
    - 📖 TLDR: WebATLAS is a memory-augmented LLM web agent that combines experience-driven memory with look-ahead action simulation via a planner-simulator-critic loop, achieving 63% success rate on WebArena-Lite without requiring website-specific fine-tuning.

- [CODA: Coordinating the Cerebrum and Cerebellum for a Dual-Brain Computer Use Agent with Decoupled Reinforcement Learning](https://arxiv.org/abs/2508.20096)
    - Zeyi Sun, Yuhang Cao, Jianze Liang, Qiushi Sun, Ziyu Liu, Zhixiong Zhang, Yuhang Zang, Xiaoyi Dong, Kai Chen, Dahua Lin, Jiaqi Wang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Shanghai AI Laboratory, The Chinese University of Hong Kong, The University of Hong Kong
    - 📅 Date: August 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [reinforcement learning], [planning], [dual-system cognition]
    - 📖 TLDR: CODA (Coordinating the Cerebrum and Cerebellum) is a dual-brain framework for CUAs in specialized domains that decouples planning (cerebrum) from execution (cerebellum) and trains them jointly via decoupled reinforcement learning, enabling adaptive coordination of long-horizon planning with precise GUI execution.

- [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976)
    - Junhong Shen, Hao Bai, Lunjun Zhang, Yifei Zhou, Amrith Setlur, Shengbang Tong, Diego Caples, Nan Jiang, Tong Zhang, Ameet Talwalkar, Aviral Kumar
    - 🏛️ Institutions: Carnegie Mellon University, Scribe, University of Illinois Urbana-Champaign, University of Toronto, University of California, Berkeley, The AGI Company, New York University
    - 📅 Date: June 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time scaling], [exploration], [planning], [reinforcement learning]
    - 📖 TLDR: Proposes test-time interaction scaling—increasing agent interaction horizons rather than reasoning trace length—showing that richer behaviors including exploration, backtracking, and dynamic adaptation from more interactions outperform extended pre-action thinking for GUI-based computer tasks.

- [Building a Stable Planner: An Extended Finite State Machine Based Planning Module for Mobile GUI Agent](https://arxiv.org/abs/2505.14141)
    - Fanglin Mo, Junzhe Chen, Haoxuan Zhu, Xuming Hu
    - 🏛️ Institutions: Hong Kong University of Science and Technology (Guangzhou), School of Computer Science & Engineering, South China University of Technology
    - 📅 Date: May 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [EFSM], [SPlanner], [planning], [vision language model], [AndroidWorld benchmark]
    - 📖 TLDR: Introduces **SPlanner**, a plug‑and‑play planning module that models mobile apps as Extended Finite State Machines (EFSMs). It decomposes user instructions into primary functions, traverses EFSMs to obtain execution paths, and refines these into natural-language plans to guide vision‑language models. On the AndroidWorld benchmark, pairing SPlanner with Qwen2.5‑VL‑72B achieves 63.8% success—28.8 points higher than the baseline, demonstrating improved stability and task planning in mobile GUI agents.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, WenHao Wang, Tianze Wu, Zhengxi Lu, Siheng Chen, LiLinghao, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab, CUHK MMLab, Shanghai Jiao Tong University
    - 📅 Date: April 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [framework], [dataset], [benchmark], [planning], [multimodal], [taxonomy]
    - 📖 TLDR: This comprehensive survey examines the evolution of LLM-powered GUI agents in mobile phone automation, transitioning from static scripts to intelligent, adaptive systems. It presents a taxonomy encompassing agent frameworks (single-agent, multi-agent, plan-then-act), modeling approaches (prompt engineering, training-based), and essential datasets and benchmarks. The paper discusses how LLMs enhance language understanding, multimodal perception, and decision-making in GUI tasks, and addresses challenges such as dataset diversity, on-device deployment efficiency, user-centric adaptation, and security concerns. It serves as a definitive reference for researchers and practitioners aiming to leverage LLMs in designing scalable, user-friendly phone GUI agents.

- [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)
    - Yuhang Liu, Pengxiang Li, Congkai Xie, Xavier Hu, Xiaotian Han, Shengyu Zhang, Hongxia Yang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Dalian University of Technology, Reallm Labs, The Hong Kong Polytechnic University
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [planning], [reasoning], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: Presents InfiGUI-R1 as a GUI agent designed to move from reactive action prediction toward explicit deliberative reasoning. The Actor2Reasoner pipeline first injects spatial reasoning and then strengthens planning and recovery through RL with sub-goal guidance and error-recovery scenarios.

- [WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](https://arxiv.org/abs/2504.11788)
    - Zhisong Zhang, Tianqing Fang, Kaixin Ma, Wenhao Yu, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: City University of Hong Kong, Tencent AI Lab
    - 📅 Date: April 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [benchmark], [model], [reasoning]
    - 📖 TLDR: WebRollback introduces an explicit rollback mechanism for web agents that allows them to revert to previous states in their navigation trajectory when they encounter errors, replacing the typical greedy one-way search strategy. Evaluated on Mind2Web-Live and WebVoyager benchmarks under both zero-shot and fine-tuning settings, the approach demonstrates improved effectiveness and efficiency in live web navigation tasks.

- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University, Microsoft
    - 📅 Date: April 09, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [model], [benchmark], [learning], [reasoning], [planning], [ASI], [WebArena]
    - 📖 TLDR: Proposes Agent Skill Induction (ASI), which induces executable program skills from web interaction experience and reuses them online as tasks evolve. Program-based skills make verification possible during induction, improving both WebArena success rate and step efficiency over static agents and text-skill alternatives while also transferring better across websites.

- [LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](https://aclanthology.org/2025.naacl-demo.16/)
    - Danqing Zhang, Balaji Rama, Jingyi Ni, Shiying He, Fu Zhao, Kunyu Chen, Arnold Chen, Junyu Cao
    - 🏛️ Institutions: PathOnAI.org, Rutgers University, The University of Texas at Austin
    - 📅 Date: March 04, 2025
    - 📑 Publisher: NAACL 2025 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [memory], [tree search], [LiteWebAgent]
    - 📖 TLDR: LiteWebAgent is an open-source suite designed for VLM-based web agent applications. It offers a modular framework that decouples action generation from grounding, supports agent planning, memory, and tree search, and is deployable via a Vercel-based web app or a Chrome extension using the Chrome DevTools Protocol (CDP).

- [WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point](https://arxiv.org/abs/2502.08047)
    - Henry Hengyuan Zhao, Kaiming Yang, Wendi Yu, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: February 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [dynamic initial state], [planning], [robustness], [GUI-Thinker], [WorldGUI]
    - 📖 TLDR: WorldGUI evaluates GUI agents under diverse non-default starting states instead of only canonical initial setups, exposing brittle planning and poor recovery when interfaces are partially configured or mid-workflow. The paper also proposes GUI-Thinker, a critique-driven framework that improves robustness in these dynamic settings.

- [Language Agents: Foundations, Prospects, and Risks](https://aclanthology.org/2024.emnlp-tutorials.3/)
    - Yu Su, Diyi Yang, Shunyu Yao, Tao Yu
    - 🏛️ Institutions: The Ohio State University, Stanford University, Princeton University, The University of Hong Kong
    - 📅 Date: November 30, 2024
    - 📑 Publisher: EMNLP 2024 Tutorial Abstracts
    - 💻 Env: [Misc]
    - 🔑 Key: [survey], [tutorial], [reasoning], [planning], [memory], [multi-agent systems], [safety]
    - 📖 TLDR: This tutorial provides a comprehensive exploration of language agents—autonomous systems powered by large language models capable of executing complex tasks through language instructions. It delves into their theoretical foundations, potential applications, associated risks, and future directions, covering topics such as reasoning, memory, planning, tool augmentation, grounding, multi-agent systems, and safety considerations.

- [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://openreview.net/forum?id=xgtXkyqw1f)
    - Zehui Chen, Kuikun Liu, Qiuchen Wang, Jiangning Liu, Wenwei Zhang, Kai Chen, Feng Zhao
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory
    - 📅 Date: July 29, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [information seeking], [planning], [AI search], [MindSearch]
    - 📖 TLDR: This paper presents MindSearch, a novel approach to web information seeking and integration that mimics human cognitive processes. The system uses a multi-agent framework consisting of a WebPlanner and WebSearcher. The WebPlanner models multi-step information seeking as a dynamic graph construction process, decomposing complex queries into sub-questions. The WebSearcher performs hierarchical information retrieval for each sub-question. MindSearch demonstrates significant improvements in response quality and depth compared to existing AI search solutions, processing information from over 300 web pages in just 3 minutes.

- [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0b82662b6c32e887bb252a74d8cb2d5e-Abstract-Datasets_and_Benchmarks_Track.html)
    - Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, Alexandre Drouin
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Chandar Research Lab
    - 📅 Date: July 07, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [reasoning], [WorkArena++]
    - 📖 TLDR: This paper introduces **WorkArena++**, a benchmark comprising 682 tasks that simulate realistic workflows performed by knowledge workers. It evaluates web agents' capabilities in planning, problem-solving, logical/arithmetic reasoning, retrieval, and contextual understanding. The study reveals challenges faced by current large language models and vision-language models in serving as effective workplace assistants, providing a resource to advance autonomous agent development.

- [Tree Search for Language Model Agents](https://arxiv.org/abs/2407.01476)
    - Jing Yu Koh, Stephen McAleer, Daniel Fried, Ruslan Salakhutdinov
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: July 01, 2024
    - 📑 Publisher: TMLR 2025
    - 💻 Env: [Web]
    - 🔑 Key: [tree search], [planning], [exploration], [value function]
    - 📖 TLDR: Proposes an inference-time best-first tree search algorithm for language-model web agents that explicitly explores future actions in the environment. By combining search with a learned value function, the method improves multi-step planning over reactive agent policies on realistic web tasks.

- [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://openreview.net/forum?id=O0nBMRlkc8)
    - Junyang Wang, Haiyang Xu, Haitao Jia, Xi Zhang, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Alibaba Group, Beijing University of Posts and Telecommunications
    - 📅 Date: June 03, 2024
    - 📑 Publisher: NeurIPS 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [multi-agent], [planning], [reflection], [Mobile-Agent-v2]
    - 📖 TLDR: Presents Mobile-Agent-v2, a mobile assistant architecture that splits operation into planning, decision, and reflection agents. This decomposition specifically targets task-progress navigation and focus-content navigation, improving on prior single-agent mobile assistants.

- [Unveiling Disparities in Web Task Handling Between Human and Web Agent](https://arxiv.org/abs/2405.04497)
    - Kihoon Son, Jinhyeon Kwon, DaEun Choi, Tae Soo Kim, Young-Ho Kim, Sangdoo Yun, Juho Kim
    - 🏛️ Institutions: KAIST, Seoul National University
    - 📅 Date: May 07, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [human-agent comparison], [think-aloud study], [planning], [reflection], [knowledge updating]
    - 📖 TLDR: Compares how humans and web agents handle web tasks through a think-aloud user study centered on planning, action, and reflection. The paper finds that humans more actively update knowledge, revise plans, and investigate failures, exposing design gaps in current web-agent pipelines.

- [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://openreview.net/forum?id=9JQtrumvg8)
    - Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust
    - 🏛️ Institutions: Google DeepMind, The University of Tokyo
    - 📅 Date: July 31, 2023
    - 📑 Publisher: ICLR 2024 (Oral)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [program synthesis], [HTML comprehension], [planning], [WebAgent]
    - 📖 TLDR: Presents WebAgent, a modular web agent that combines HTML comprehension, explicit planning, and program synthesis for real-world web automation. Its core design choice is to separate long-context webpage understanding from action generation through specialized components rather than a single monolithic model.
