# Papers with Keyword: planning

- [IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/abs/2602.17049)
    - Seoyoung Lee, Seobin Yoon, Seongbeen Lee, Yoojung Chun, Dayoung Park, Doyeon Kim, Joo Yong Sim
    - 🏛️ Institutions: Sookmyung Women's University
    - 📅 Date: February 19, 2026
    - 📑 Publisher: AAMAS 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [multi-agent], [memory], [planning], [skill abstraction], [intent representation], [IntentCUA]
    - 📖 TLDR: This paper introduces IntentCUA, a multi-agent computer-use framework for stabilizing long-horizon desktop automation through intent-aligned plan memory. It learns intent-level representations from interaction traces, abstracts reusable skills, and coordinates a Planner, Plan-Optimizer, and Critic over shared memory to reduce redundant replanning and error accumulation. On end-to-end evaluations over desktop applications, IntentCUA outperforms RL-based and trajectory-centric baselines, highlighting intent abstraction and memory-grounded multi-agent planning as an effective systems design for computer-use agents.

- [Web Verbs: Typed Abstractions for Reliable Task Composition on the Agentic Web](https://arxiv.org/abs/2602.17245)
    - Linxi Jiang, Rui Xi, Zhijie Liu, Shuo Chen, Zhiqiang Lin, Suman Nath
    - 🏛️ Institutions: The Ohio State University, University of British Columbia, Microsoft Research
    - 📅 Date: February 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [tool-use], [typed action abstraction], [agentic web], [web verbs]
    - 📖 TLDR: This paper argues that web agents need a semantic action layer above brittle low-level clicks and keystrokes, and proposes Web Verbs as typed, composable web actions with explicit contracts, policies, and logging support. The abstraction unifies API-based and browser-based execution into stable callable units that agents can discover and compose into short programs. Through a proof-of-concept implementation and case studies, the paper positions typed web actions as a route to more reliable, efficient, and verifiable web agents.

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
    - 🔑 Key: [GUI agent], [reinforcement learning], [reward shaping], [GUI grounding], [planning], [training framework]
    - 📖 TLDR: SSL (Sweet Spot Learning) introduces a tiered reward framework for reinforcement learning that replaces binary rewards with progressively amplified, quality-ordered rewards to guide agent policies toward optimal solution regions. Evaluated across GUI perception, short/long-term planning, and complex reasoning tasks, SSL achieves up to 2.5x sample efficiency gains over binary reward baselines on 12 benchmarks.

- [BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://arxiv.org/abs/2601.21352)
    - Ziyu Lu, Tengjin Weng, Yiying Yang, Hanchu Zhou, Kenji Kawaguchi
    - 🏛️ Institutions: Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shenzhen University, Guangdong University of Technology
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [backtracking], [DFS], [planning], [error recovery], [OSWorld]
    - 📖 TLDR: BEAP-Agent models GUI task execution as a depth-first search process, introducing a framework with backtrackable execution and adaptive planning that enables multi-level state backtracking for error recovery, achieving 28.2% accuracy on the OSWorld benchmark.

- [WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](https://arxiv.org/abs/2504.11788)
    - Zhisong Zhang, Tianqing Fang, Kaixin Ma, Wenhao Yu, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: City University of Hong Kong, Tencent AI Lab
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [planning], [benchmark], [model], [reasoning]
    - 📖 TLDR: WebRollback introduces an explicit rollback mechanism for web agents that allows them to revert to previous states in their navigation trajectory when they encounter errors, replacing the typical greedy one-way search strategy. Evaluated on Mind2Web-Live and WebVoyager benchmarks under both zero-shot and fine-tuning settings, the approach demonstrates improved effectiveness and efficiency in live web navigation tasks.

- [MobileDreamer: Generative Sketch World Model for GUI Agent](https://arxiv.org/abs/2601.04035)
    - Yilin Cao, Yufeng Zhong, Zhixiong Zeng, Liming Zheng, Jing Huang, Haibo Qiu, Peng Shi, Wenji Mao, Wan Guanglu
    - 🏛️ Institutions: CAS, UCAS, Meituan
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [planning], [lookahead], [mobile GUI agent], [MobileDreamer]
    - 📖 TLDR: This paper introduces MobileDreamer, a world-model-based lookahead framework for mobile GUI agents that predicts compact task-relevant future interface sketches rather than full screenshots. Its textual sketch world model preserves spatial information while remaining efficient, and its rollout imagination strategy uses these predicted futures to improve action selection on long-horizon tasks. On AndroidWorld, MobileDreamer achieves state-of-the-art performance and improves task success by 5.25%, showing that lightweight future imagination can materially strengthen mobile GUI planning.

- [WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation](https://arxiv.org/abs/2510.22732)
    - Jiali Cheng, Anjishnu Kumar, Roshan Lal, Rishi Rajasekaran, Hani Ramezani, Omar Zia Khan, Oleg Rokhlenko, Sunny Chiu-Webster, Gang Hua, Hadi Amiri
    - 🏛️ Institutions: University of Massachusetts Lowell, Amazon Alexa AI
    - 📅 Date: December 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agent framework], [memory], [web navigation], [planning], [WebArena]
    - 📖 TLDR: WebATLAS is a memory-augmented LLM web agent that combines experience-driven memory with look-ahead action simulation via a planner-simulator-critic loop, achieving 63% success rate on WebArena-Lite without requiring website-specific fine-tuning.

- [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014)
    - Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover
    - 🏛️ Institutions: UCLA, Panasonic AI Research, Salesforce AI Research
    - 📅 Date: December 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [world model], [planning], [semantic state transition], [MobileWorldBench], [MobileWorld]
    - 📖 TLDR: This paper reframes world modeling for mobile GUI agents as semantic state transition prediction in natural language rather than pixel-space forecasting. It introduces MobileWorldBench to evaluate vision-language models as mobile world models, releases the 1.4M-sample MobileWorld dataset for training, and shows that integrating these semantic world models into planning improves downstream mobile agent success rates. The work establishes semantic world modeling as a practical intermediate layer for stronger mobile GUI planning.

- [WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment](https://arxiv.org/abs/2512.12692)
    - Mahir Labib Dihan, Tanzima Hashem, Mohammed Eunus Ali, Md Rizwan Parvez
    - 🏛️ Institutions: Bangladesh University of Engineering and Technology (BUET), Monash University, Qatar Computing Research Institute (QCRI)
    - 📅 Date: December 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [search algorithm], [LLM], [WebArena], [planning]
    - 📖 TLDR: WebOperator is a tree-search framework for web agents that enables safe backtracking and strategic exploration through best-first search with action-aware safety ranking, achieving state-of-the-art 54.6% success rate on WebArena with GPT-4o.

- [PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents](https://arxiv.org/abs/2510.00413)
    - Zikang Liu, Junyi Li, Wayne Xin Zhao, Dawei Gao, Yaliang Li, Ji-rong Wen
    - 🏛️ Institutions: Renmin University of China, City University of Hong Kong, Alibaba Group
    - 📅 Date: October 04, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [memory retrieval], [mobile navigation], [vision-language model], [planning], [web navigation]
    - 📖 TLDR: PAL-UI introduces an active look-back framework for vision-based GUI agents that uses dual-level summarization and a dedicated retrieval tool to recall historical screenshots during planning, significantly improving performance on mobile and web GUI navigation tasks with models trained on Qwen2.5-VL.

- [CODA: Coordinating the Cerebrum and Cerebellum for a Dual-Brain Computer Use Agent with Decoupled Reinforcement Learning](https://arxiv.org/abs/2508.20096)
    - Zeyi Sun, Yuhang Cao, Jianze Liang, Qiushi Sun, Ziyu Liu, Zhixiong Zhang, Yuhang Zang, Xiaoyi Dong, Kai Chen, Dahua Lin, Jiaqi Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: August 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [computer-use agent], [reinforcement learning], [planning], [dual-system cognition]
    - 📖 TLDR: CODA (Coordinating the Cerebrum and Cerebellum) is a dual-brain framework for CUAs in specialized domains that decouples planning (cerebrum) from execution (cerebellum) and trains them jointly via decoupled reinforcement learning, enabling adaptive coordination of long-horizon planning with precise GUI execution.

- [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358)
    - Hussein Mozannar, Gagan Bansal, Cheng Tan, Adam Fourney, Victor Dibia, Jingya Chen, Jack Gerrits, Tyler Payne, Matheus Kunzler Maldaner, Madeleine Grunde-McLaughlin, Eric Zhu, Griffin Bassman, Jacob Alber, Peter Chang, Ricky Loynd, Friederike Niedtner, Ece Kamar, Maya Murad, Rafah Hosn, Saleema Amershi
    - 🏛️ Institutions: Microsoft Research AI Frontiers
    - 📅 Date: July 30, 2025
    - 📑 Publisher: arXiv (also MSR Technical Report MSR-TR-2025-40)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-in-the-loop], [multi-agent], [planning], [memory], [MCP], [safety]
    - 📖 TLDR: Magentic-UI (Multi-agentic User Interface) is an open-source web interface enabling safe, efficient human–agent collaboration through a flexible multi-agent architecture. It supports web browsing, code execution, and file manipulation, and provides six interaction mechanisms—co-planning, co-tasking, multi-tasking, action guards, answer verification, and long-term memory—to integrate human oversight with AI autonomy. Evaluated via agentic benchmarks, simulated user tests, qualitative user study, and safety assessments, it demonstrates how incorporating human-in-the-loop dynamics can significantly improve agentic systems' reliability and performance.

- [GTA1: GUI Test-time Scaling Agent](https://arxiv.org/abs/2507.05791)
    - Yan Yang, Dongxu Li, Yutong Dai, Yuhao Yang, Ziyang Luo, Zirui Zhao, Zhiyuan Hu, Junzhe Huang, Amrita Saha, Zeyuan Chen, Ran Xu, Liyuan Pan, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research, Australian National University, The University of Hong Kong
    - 📅 Date: July 08, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time scaling], [reinforcement learning], [planning], [grounding], [GTA1]
    - 📖 TLDR: This paper tackles two major challenges in GUI agents — planning ambiguity and visual grounding accuracy. It introduces **GTA1**, a GUI Test-time Scaling Agent that improves action decision-making by sampling multiple candidate actions at each step and selecting the best one via a judge model. Additionally, it enhances grounding through reinforcement learning with success-based rewards. GTA1 achieves state-of-the-art results on GUI grounding and execution benchmarks such as ScreenSpot and OSWorld.

- [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976)
    - Junhong Shen, Hao Bai, Lunjun Zhang, Yifei Zhou, Amrith Setlur, Shengbang Tong, Diego Caples, Nan Jiang, Tong Zhang, Ameet Talwalkar, Aviral Kumar
    - 🏛️ Institutions: Unknown
    - 📅 Date: June 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [computer-use agent], [test-time scaling], [exploration], [planning], [reinforcement learning]
    - 📖 TLDR: Proposes test-time interaction scaling—increasing agent interaction horizons rather than reasoning trace length—showing that richer behaviors including exploration, backtracking, and dynamic adaptation from more interactions outperform extended pre-action thinking for GUI-based computer tasks.

- [Building a Stable Planner: An Extended Finite State Machine Based Planning Module for Mobile GUI Agent](https://arxiv.org/abs/2505.14141)
    - Fanglin Mo, Junzhe Chen, Haoxuan Zhu, Xuming Hu
    - 🏛️ Institutions: Hong Kong University of Science and Technology (Guangzhou), South China University of Technology
    - 📅 Date: May 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [EFSM], [SPlanner], [planning], [vision language model], [AndroidWorld benchmark]
    - 📖 TLDR: Introduces **SPlanner**, a plug‑and‑play planning module that models mobile apps as Extended Finite State Machines (EFSMs). It decomposes user instructions into primary functions, traverses EFSMs to obtain execution paths, and refines these into natural-language plans to guide vision‑language models. On the AndroidWorld benchmark, pairing SPlanner with Qwen2.5‑VL‑72B achieves 63.8% success—28.8 points higher than the baseline, demonstrating improved stability and task planning in mobile GUI agents.

- [ScaleTrack: Scaling and back-tracking Automated GUI Agents](https://arxiv.org/abs/2505.00416)
    - Jing Huang, Zhixiong Zeng, Wenkang Han, Yufeng Zhong, Liming Zheng, Shuai Fu, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, University of Adelaide
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [training strategy], [back-tracking], [grounding], [planning], [ScaleTrack]
    - 📖 TLDR: This paper introduces *ScaleTrack*, a training framework designed to enhance automated GUI agents by addressing two primary challenges: insufficient training data for GUI grounding and the lack of back-tracking in GUI planning. The authors aggregate diverse GUI samples from various synthesis methods into a unified template to scale the grounding process. Additionally, they propose a hybrid training strategy that combines forward-planning and back-tracking, enabling the agent to predict both the next action and the historical actions leading to the current GUI state. Experimental results demonstrate that ScaleTrack significantly improves task success rates across multiple benchmarks, highlighting the effectiveness of integrating back-tracking into GUI agent training.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, Wenhao Wang, Tianze Wu, Linghao Li, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab, The Chinese University of Hong Kong MMLab
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
    - 🔑 Key: [framework], [model], [reinforcement learning], [planning], [reasoning], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: This paper introduces **InfiGUI-R1**, a multimodal GUI agent developed through the **Actor2Reasoner** framework, aiming to transition agents from reactive behaviors to deliberative reasoning. The framework comprises two stages: *Reasoning Injection*, which employs Spatial Reasoning Distillation to integrate GUI visual-spatial information with logical reasoning, and *Deliberation Enhancement*, which uses Reinforcement Learning with Sub-goal Guidance and Error Recovery Scenario Construction to refine the agent's planning and error correction capabilities. Evaluations on benchmarks like AndroidControl and ScreenSpot demonstrate that InfiGUI-R1-3B achieves state-of-the-art performance in GUI grounding and trajectory tasks, outperforming larger models in several categories.

- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University, Microsoft
    - 📅 Date: April 09, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [model], [benchmark], [learning], [reasoning], [planning], [ASI], [WebArena]
    - 📖 TLDR: This paper introduces Agent Skill Induction (ASI), a framework enabling web agents to learn and apply programmatic skills dynamically. By representing skills as executable programs, ASI allows agents to verify and reuse these skills across tasks, enhancing adaptability and efficiency. Evaluated on the WebArena benchmark, ASI outperforms static and text-based skill agents in success rate and step efficiency, demonstrating improved generalization and adaptability to new web environments.

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
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: February 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [desktop], [web], [planning], [robustness], [world model]
    - 📖 TLDR: WorldGUI is a benchmark for desktop and web GUI automation that evaluates agents under diverse, non-default initial states to test robustness and adaptive planning, revealing that state-of-the-art GUI agents suffer substantial performance degradation when the environment deviates from canonical starting points. It also introduces WorldGUI-Agent, a model-agnostic framework using three critique stages to improve reliability in dynamic environments.

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Nanyang Technological University, Salesforce
    - 📅 Date: December 05, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [planning], [reasoning], [aguvis], [visual grounding]
    - 📖 TLDR: This paper introduces *Aguvis*, a unified pure vision-based framework for autonomous GUI agents that operates across various platforms. It leverages image-based observations and grounds natural language instructions to visual elements, employing a consistent action space to ensure cross-platform generalization. The approach integrates explicit planning and reasoning within the model, enhancing its ability to autonomously navigate and interact with complex digital environments. A large-scale dataset of GUI agent trajectories is constructed, incorporating multimodal reasoning and grounding. Comprehensive experiments demonstrate that Aguvis surpasses previous state-of-the-art methods in both offline and real-world online scenarios, achieving the first fully autonomous pure vision GUI agent capable of performing tasks independently without collaboration with external closed-source models. All datasets, models, and training recipes are open-sourced to facilitate future research.

- [Language Agents: Foundations, Prospects, and Risks](https://aclanthology.org/2024.emnlp-tutorials.3/)
    - Yu Su, Diyi Yang, Shunyu Yao, Tao Yu
    - 🏛️ Institutions: The Ohio State University, Stanford University, Princeton University, The University of Hong Kong
    - 📅 Date: November 30, 2024
    - 📑 Publisher: EMNLP 2024 Tutorial Abstracts
    - 💻 Env: [Misc]
    - 🔑 Key: [survey], [tutorial], [reasoning], [planning], [memory], [multi-agent systems], [safety]
    - 📖 TLDR: This tutorial provides a comprehensive exploration of language agents—autonomous systems powered by large language models capable of executing complex tasks through language instructions. It delves into their theoretical foundations, potential applications, associated risks, and future directions, covering topics such as reasoning, memory, planning, tool augmentation, grounding, multi-agent systems, and safety considerations.

- [The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](https://arxiv.org/abs/2411.10323)
    - Siyuan Hu, Mingyu Ouyang, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: November 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [claude 3.5 computer use], [GUI automation], [planning], [action], [critic]
    - 📖 TLDR: This study evaluates Claude 3.5 Computer Use, an AI model enabling end-to-end language-to-desktop actions, through curated tasks across various domains. It introduces an out-of-the-box framework for deploying API-based GUI automation models, analyzing the model's planning, action execution, and adaptability to dynamic environments.

- [From Grounding to Planning: Benchmarking Bottlenecks in Web Agents](https://ebooks.iospress.nl/doi/10.3233/FAIA250590)
    - Segev Shlomov, Ben Wiesel, Aviad Sela, Ido Levy, Liane Galanti, Roy Abitbol
    - 🏛️ Institutions: IBM Research - Haifa, University of Haifa
    - 📅 Date: September 03, 2024
    - 📑 Publisher: ECAI 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [grounding], [Mind2Web], [AssistantBench], [web navigation]
    - 📖 TLDR: This paper analyzes performance bottlenecks in web agents by separately evaluating grounding and planning tasks, isolating their individual impacts on navigation efficacy. Using an enhanced version of the Mind2Web dataset, the study reveals planning as a significant bottleneck, with advancements in grounding and task-specific benchmarking for elements like UI component recognition. Through experimental adjustments, the authors propose a refined evaluation framework, aiming to enhance web agents' contextual adaptability and accuracy in complex web environments.

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
    - 🏛️ Institutions: Unknown
    - 📅 Date: July 01, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [tree search], [planning], [exploration], [MCTS]
    - 📖 TLDR: Proposes an inference-time best-first tree search algorithm for language model agents in interactive web environments, enabling explicit multi-step exploration and planning by leveraging environmental feedback to overcome LM limitations in multi-step reasoning for complex computer tasks.

- [Octo-planner: On-device Language Model for Planner-Action Agents](https://arxiv.org/abs/2406.18082)
    - Nexa AI Team
    - 🏛️ Institutions: Nexa AI
    - 📅 Date: June 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [model], [framework], [octo-planner], [on-device], [planning]
    - 📖 TLDR: This paper presents Octo-planner, an on-device planning model designed for the Planner-Action Agents Framework. Octo-planner utilizes a fine-tuned model based on Phi-3 Mini (3.8 billion parameters) for high efficiency and low power consumption. It separates planning and action execution into two distinct components: a planner agent optimized for edge devices and an action agent using the Octopus model for function execution. The model achieves a planning success rate of 98.1% on benchmark datasets, providing reliable and effective performance.

- [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://openreview.net/forum?id=O0nBMRlkc8)
    - Junyang Wang, Haiyang Xu, Haitao Jia, Xi Zhang, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Alibaba Group, Beijing University of Posts and Telecommunications
    - 📅 Date: June 03, 2024
    - 📑 Publisher: NeurIPS 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [multi-agent], [planning], [decision-making], [reflection]
    - 📖 TLDR: The paper presents **Mobile-Agent-v2**, a multi-agent architecture designed to assist with mobile device operations. It comprises three agents: a planning agent that generates task progress, a decision agent that navigates tasks using a memory unit, and a reflection agent that corrects erroneous operations. This collaborative approach addresses challenges in navigation and long-context input scenarios, achieving over a 30% improvement in task completion compared to single-agent architectures.
