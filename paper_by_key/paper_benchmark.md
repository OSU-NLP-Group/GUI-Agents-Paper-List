# Papers with Keyword: benchmark

- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596)
    - Haojia Lin, Xiaoyu Tan, Yulei Qin, Zihan Xu, Yuchen Shi, Zongyi Li, Gang Li, Shaofei Cai, Siqi Cai, Chaoyou Fu, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, PKU, NJU
    - 📅 Date: October 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [reward model], [computer-using agent], [CUARewardBench], [Unanimous Prompt Ensemble (UPE)]
    - 📖 TLDR: This paper introduces CUARewardBench, the first benchmark for evaluating reward models tailored to computer-using agents. It includes step-level and trajectory-level annotations from tasks across 10 software types and 7 agent architectures. The study identifies the limitations of current reward models and proposes UPE, a prompting-based method that significantly improves evaluation accuracy.

- [SCUBA: Salesforce Computer Use Benchmark](https://sfrcua.github.io/SCUBA/)
    - Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce
    - 📅 Date: Sep 30, 2025
    - 📑 Publisher: arXiv
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

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: arXiv (preprint)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [benchmark], [API-GUI paradigm], [dataset], [distributed RL], [Entropulse]
    - 📖 TLDR: This paper presents **ComputerRL**, a large-scale end-to-end reinforcement learning framework enabling agents to operate complex desktop tasks. It introduces the **API-GUI paradigm**, combining programmatic API calls with GUI actions, and a **distributed RL infrastructure** managing thousands of parallel virtual Ubuntu desktops for scalable training. A novel **Entropulse** training strategy alternates between reinforcement learning and supervised fine-tuning to prevent entropy collapse over long training runs. Applied to open models like GLM-4-9B-0414, ComputerRL achieves a new state-of-the-art success rate of **48.1%** on the OSWorld benchmark via the AutoGLM-OS-9B model.  

- [You Don’t Know Until You Click: Automated GUI Testing for Production-Ready Software Evaluation](https://arxiv.org/abs/2508.14104)
    - Yutong Bian, Xianhao Lin, Yupeng Xie, Tianyang Liu, Mingchen Zhuge, Siyuan Lu, Haoming Tang, Jinlin Wang, Jiayi Zhang, Jiaqi Chen, Xiangru Tang, Yongxin Ni, Sirui Hong, Chenglin Wu
    - 🏛️ Institutions: DeepWisdom, Fudan Univ., HKUST(GZ), UC San Diego, KAUST, Westlake Univ., Stanford Univ., Yale Univ., NUS
    - 📅 Date: August 17, 2025
    - 📑 Publisher: arXiv (no conference/journal indicated)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-as-a-judge], [RealDevWorld], [RealDevBench], [AppEvalPilot], [multimodal]
    - 📖 TLDR: This paper presents **RealDevWorld**, a novel framework to automatically evaluate production-ready GUI software generated by LLMs. It includes **RealDevBench**, a suite of 194 open-ended, multimodal software engineering tasks, and **AppEvalPilot**, an “agent-as-judge” system that simulates realistic GUI interactions to assess functional correctness, visual fidelity, and runtime behavior. It achieves high alignment with human judgment (accuracy 0.92, correlation 0.85), reducing the need for manual review and offering scalable, human-aligned evaluation. Code is available on GitHub.

- [MM-BrowseComp: A Comprehensive Benchmark for Multimodal Browsing Agents](https://arxiv.org/abs/2508.13186)
    - Shilong Li, Xingyuan Bu, Wenjie Wang, Jiaheng Liu, Jun Dong, Haoyang He, Hao Lu, Haozhe Zhang, Chenchen Jing, Zhen Li, Chuanhao Li, Jiayi Tian, Chenchen Zhang, Tianhao Peng, Yancheng He, Jihao Gu, Yuanxing Zhang, Jian Yang, Ge Zhang, Wenhao Huang, Wangchunshu Zhou, Zhaoxiang Zhang, Ruizhe Ding, Shilei Wen
    - 🏛️ Institutions: ByteDance, Nanjing University, M-A-P, CASIA, Zhejiang University :contentReference[oaicite:1]{index=1}
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [benchmark], [dataset], [multimodal], [tool-use], [multimodal reasoning]
    - 📖 TLDR: Introduces **MM-BrowseComp**, a challenging benchmark of 224 handcrafted, multi-hop questions designed to evaluate AI agents’ ability to retrieve and reason over multimodal web content—including images and videos—instead of text alone. Each question includes a verified checklist detailing the necessary reasoning steps. Even top models like OpenAI’s o3 with tools score only ~29% accuracy, underscoring significant shortcomings in current agents' multimodal capabilities and native multimodal reasoning. :contentReference

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y. Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: XLANG Lab (HKU), Moonshot AI, Stanford, University of Waterloo, Carnegie Mellon University
    - 📅 Date: August 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [chain-of-thought], [vision-language-model], [AgentNet]
    - 📖 TLDR: Introduces **OpenCUA**, an open-source framework to train computer-use agents (CUAs) using vision-language models. It includes a cross-platform annotation tool (AgentNet Tool), a large-scale dataset covering 3 OSes and 200+ apps/websites (AgentNet), and a data processing pipeline that builds state–action pairs enhanced with reflective long chain-of-thought reasoning. The resulting models—especially OpenCUA-32B—achieve SOTA performance on the OSWorld-Verified benchmark (34.8% success), surpassing OpenAI’s GPT-4o CUA and demonstrating strong generalization and scalability. All tools, models, and data are publicly released. :contentReference[oaicite:4]{index=4}

- [BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent](https://arxiv.org/abs/2508.06600)
    - Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Andrew Liu, Joshua Green, Kshama Patel, Ruoxi Meng, Mingyi Su, Sahel Sharifymoghaddam, Yanxi Li, Haoran Hong, Xinyu Shi, Xuye Liu, Nandan Thakur, Crystina Zhang, Luyu Gao, Wenhu Chen, Jimmy Lin
    - 🏛️ Institutions: University of Waterloo, CSIRO, Independent, CMU, University of Queensland
    - 📅 Date: August 8, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [benchmark], [dataset], [transparency], [reproducibility], [retriever-LLM disentanglement]
    - 📖 TLDR: Introduces **BrowseComp-Plus**, a fixed-corpus benchmark for evaluating deep-research agents. It enables controlled, fair, and transparent comparisons by providing human-verified supporting and challenging negative documents for each query. Results reveal significant performance variation—for example, an open-source model (Search-R1 + BM25) only achieves 3.86% accuracy, while GPT-5 reaches 55.9%, and GPT-5 with Qwen3-Embedding-8B retriever achieves 70.1% with fewer queries—highlighting the critical importance of retrieval quality and enabling disentangled analysis of retrieval vs. reasoning components.

- [Test‑Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615)
    - Yong Du, Yuchen Yan, Fei Tang, Zhengxi Lu, Chang Zong, Weiming Lu, Shengpei Jiang, and Yongliang Shen
    - 🏛️ Institutions: Zhejiang University (ZJU), Central South University (CSU), Zhejiang University of Science and Technology (ZUST), SF Technology
    - 📅 Date: August 7, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [test‑time scaling], [reinforcement learning], [self‑supervised], [GUI‑RC], [GUI‑RCPO], [benchmark], [Region Consistency], [GUI grounding]
    - 📖 TLDR: This paper introduces **GUI‑RC (Region Consistency)**, a test-time method that aggregates multiple model predictions via spatial voting to derive a consensus region—achieving 2–3% accuracy improvements on ScreenSpot benchmarks without any additional training. It extends this idea with **GUI‑RCPO (Region Consistency Policy Optimization)**, which turns region-consistency patterns into self-supervised rewards for reinforcement learning at inference time, refining model predictions on unlabeled data and yielding further improvements (e.g., from 83.57% to 85.14% on ScreenSpot‑v2). The approach demonstrates a novel and effective use of test-time optimization for more robust, data-efficient GUI grounding.

- [Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL](https://arxiv.org/abs/2508.13167)
    - Weizhen Li, Jianbo Lin, Zhuosong Jiang, Jingyi Cao, Xinpeng Liu, Jiayu Zhang, Zhenqiang Huang, Qianben Chen, Weichen Sun, Qiexiang Wang, Hongxuan Lu, Tianrui Qin, Chenghao Zhu, Yi Yao, Shuying Fan, Xiaowan Li, Tiannan Wang, Pai Liu, King Zhu, He Zhu, Dingfeng Shi, Piaohong Wang, Yeyi Guan, Xiangru Tang, Minghao Liu, Yuchen Eleanor Jiang, Jian Yang, Jiaheng Liu, Ge Zhang, Wangchunshu Zhou
    - 🏛️ Institutions: OPPO Personal AI Lab, OPPO Research Institute
    - 📅 Date: August 6, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [framework] (Chain-of-Agents paradigm), [agent foundation model], [multi-agent distillation], [agentic reinforcement learning], [dataset], [benchmark], [AFM]
    - 📖 TLDR: The paper introduces **Chain-of-Agents (CoA)**, a novel paradigm enabling a single large language model (LLM) to perform multi-agent style reasoning by dynamically activating tool and role agents within one end-to-end model. They train **Agent Foundation Models (AFMs)** using a two-step approach: first, **multi-agent distillation** to convert trajectories from specialized multi-agent systems into supervised fine-tuning data; second, **agentic reinforcement learning (RL)** to further improve on verifiable tasks. AFMs achieve state-of-the-art performance across web-agent and code-agent benchmarks (e.g., GAIA, WebWalker, BrowseComp, HLE), and the authors open-source all data, model weights, code, and training resources

- [NatureGAIA: Pushing the Frontiers of GUI Agents with a Challenging Benchmark and High-Quality Trajectory Dataset](https://arxiv.org/abs/2508.01330)
    - Zihan Zheng, Tianle Cui, Chuwen Xie, Jiahui Zhang, Jiahui Pan, Lewei He, Qianglong Chen
    - 🏛️ Institutions: South China Normal University, Zhejiang University :contentReference[oaicite:1]{index=1}
    - 📅 Date: August 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [framework], [hierarchical agent], [reinforcement fine-tuning (RFT)], [causal pathways], [Agent (hierarchical)], [Qwen2.5-VL-7B], [Claude-sonnet-4], [WPSR]
    - 📖 TLDR: This paper introduces **NatureGAIA**, a new benchmark based on the principle of **Causal Pathways**, which decomposes complex GUI tasks into programmatically verifiable atomic steps for rigorous and reproducible evaluation. A hierarchical agent architecture (called **Agent**) was used to generate a human-verified trajectory dataset representing diverse and self-correcting interaction patterns. This dataset was used to conduct Reinforcement Fine-Tuning (RFT) on the Qwen2.5-VL-7B model. Even top-performing models like Claude-sonnet-4 only reached a Weighted Pathway Success Rate (WPSR) of 34.6 %, while RFT improved the smaller model from 3.3 % to 10.8 %, yet performance dropped significantly in complex scenarios—highlighting current limitations in GUI agent capabilities.

- [Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training](https://arxiv.org/abs/2508.00414)
    - Tianqing Fang, Zhisong Zhang, Xiaoyang Wang, Rui Wang, Can Qin, Yuxuan Wan, Jun-Yu Ma, Ce Zhang, Jiaqi Chen, Xiyun Li, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: Tencent AI Lab
    - 📅 Date: August 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [model], [benchmark], [multimodule], [reflection], [voting], [Agent Foundation Models]
    - 📖 TLDR: This work introduces **Cognitive Kernel-Pro**, a fully open-source, multi-module agent framework designed to democratize advanced AI agent development. It curates high-quality training data across four domains—web, files, code, and general reasoning—and introduces test-time strategies like reflection and voting to enhance robustness. Evaluated on the GAIA benchmark, its open 8B-parameter model outperforms previous open-source agents such as WebDancer and WebSailor, setting a new performance standard. Code is publicly available.

- [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358)
    - Hussein Mozannar, Gagan Bansal, Cheng Tan, Adam Fourney, Victor Dibia, Jingya Chen, Jack Gerrits, Tyler Payne, Matheus Kunzler Maldaner, Madeleine Grunde-McLaughlin, Eric Zhu, Griffin Bassman, Jacob Alber, Peter Chang, Ricky Loynd, Friederike Niedtner, Ece Kamar, Maya Murad, Rafah Hosn, Saleema Amershi
    - 🏛️ Institutions: MSR
    - 📅 Date: July 30, 2025
    - 📑 Publisher: arXiv (also MSR Technical Report MSR-TR-2025-40)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-in-the-loop], [multi-agent], [interaction mechanisms], [MCP (Model Context Protocol)], [safety], [auto-planning], [benchmark evaluation]
    - 📖 TLDR: Magentic-UI (Multi-agentic User Interface) is an open-source web interface enabling safe, efficient human–agent collaboration through a flexible multi-agent architecture. It supports web browsing, code execution, and file manipulation, and provides six interaction mechanisms—co-planning, co-tasking, multi-tasking, action guards, answer verification, and long-term memory—to integrate human oversight with AI autonomy. Evaluated via agentic benchmarks, simulated user tests, qualitative user study, and safety assessments, it demonstrates how incorporating human-in-the-loop dynamics can significantly improve agentic systems' reliability and performance.

- [GLM-4.5V and GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning](https://arxiv.org/abs/2507.01006)
    - Wenyi Hong, Wenmeng Yu, Xiaotao Gu, Guo Wang, Guobing Gan, Haomiao Tang, Jiale Cheng, Ji Qi, Junhui Ji, Lihang Pan, Shuaiqi Duan, Weihan Wang, Yan Wang, Yean Cheng, Zehai He, Zhe Su, Zhen Yang, Ziyang Pan, Aohan Zeng, Baoxu Wang, Bin Chen, Boyan Shi, Changyu Pang, Chenhui Zhang, Da Yin, Fan Yang, Guoqing Chen, Jiazheng Xu, Jiale Zhu, Jiali Chen, Jing Chen, Jinhao Chen, Jinghao Lin, Jinjiang Wang, Junjie Chen, Leqi Lei, Letian Gong, Leyi Pan, Mingdao Liu, Mingde Xu, Mingzhi Zhang, Qinkai Zheng, Sheng Yang, Shi Zhong, Shiyu Huang, Shuyuan Zhao, Siyan Xue, Shangqin Tu, Shengbiao Meng, Tianshu Zhang, Tianwei Luo, Tianxiang Hao, Tianyu Tong, Wenkai Li, Wei Jia, Xiao Liu, Xiaohan Zhang, Xin Lyu, Xinyue Fan, Xuancheng Huang, Yanling Wang, Yadong Xue, Yanfeng Wang, Yanzi Wang, Yifan An, Yifan Du, Yiming Shi, Yiheng Huang, Yilin Niu, Yuan Wang, Yuanchang Yue, Yuchen Li, Yutao Zhang, Yuting Wang, Yu Wang, Yuxuan Zhang, Zhao Xue, Zhenyu Hou, Zhengxiao Duan, Zihan Wang, Peng Zhang, Debing Liu, Bin Xu, Juanzi Li, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu AI, Tsinghua University
    - 📅 Date: July 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [reinforcement learning], [RLCS], [multimodal], [vision-language model], [thinking-mode], [grounding], [GLM-4.1V-Thinking], [GLM-4.5V]
    - 📖 TLDR: Introduces two vision-language models—**GLM-4.1V-9B-Thinking**, a 9B-parameter model designed for multimodal reasoning, and **GLM-4.5V**, a larger version based on GLM-4.5-Air (106B parameters, 12B active). The authors propose a reasoning-centric training pipeline including large-scale pretraining and a novel **Reinforcement Learning with Curriculum Sampling (RLCS)** framework. The models show state-of-the-art performance across 42 (GLM-4.5V) and 28 (GLM-4.1V-Thinking) public multimodal benchmarks, often outperforming much larger models (e.g., Qwen-2.5-VL-72B and Gemini-2.5-Flash), especially in tasks like STEM reasoning, video/document understanding, coding, GUI agents, and grounding. Both models and training code are open-sourced. :contentReference[oaicite:2]{index=2}

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://arxiv.org/abs/2506.21506)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Amazon AGI
    - 📅 Date: June 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agentic search], [Agent-as-a-Judge], [evaluation], [Mind2Web 2]
    - 📖 TLDR: This paper introduces **Mind2Web 2**, a benchmark of 130 long-horizon, real-world tasks requiring web browsing and extensive information synthesis. It proposes an **Agent-as-a-Judge** framework to automatically and rigorously evaluate the correctness and source attribution of answers for agentic search systems. Through a detailed evaluation of nine frontier systems, the paper highlights OpenAI’s Deep Research system as the best performer, achieving 50-70% of human performance while reducing time consumption by half. Mind2Web 2 offers a foundation for benchmarking next-generation agentic search systems.

- [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://penghao-wu.github.io/GUI_Reflection/)
    - Penghao Wu, Shengnan Ma, Bo Wang, Jiaheng Yu, Lewei Lu, Ziwei Liu
    - 🏛️ Institutions: NTU (S‑Lab), SenseTime Research
    - 📅 Date: June 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [model], [benchmark], [self-reflection], [GUI‑Reflection Task Suite]
    - 📖 TLDR: Introduces **GUI‑Reflection**, a framework that enhances multimodal GUI agents with self-reflection and error correction. It spans three training stages—pre‑training with reflection tasks, offline supervised fine‑tuning with autogenerated error scenarios, and online iterative reflection tuning—resulting in improved robustness on AndroidWorld and the novel GUI‑Reflection Task Suite using entirely automated pipelines.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, and Mike Zheng Shou
    - 🏛️ Institutions: NUS
    - 📅 Date: June 4, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [desktop]
    - 🔑 Key: [benchmark], [multilingual], [safety], [macOSWorld]
    - 📖 TLDR: Introduces **macOSWorld**, the first interactive benchmark for GUI agents on macOS, with 202 tasks across 30 apps (28 macOS-exclusive) in 5 languages plus a safety subset for deception attacks; evaluates 6 agents, showing proprietary CUAs outperform open-source and VLM-based agents, significant language gaps (Arabic –27.5%), and both grounding and safety challenges.

- [WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks](https://arxiv.org/abs/2506.01952)
    - Atsuyuki Miyai, Zaiying Zhao, Kazuki Egashira, Atsuki Sato, Tatsumi Sunada, Shota Onohara, Hiromasa Yamanishi, Mashiro Toyooka, Kunato Nishina, Ryoma Maeda, Kiyoharu Aizawa, Toshihiko Yamasaki
    - 🏛️ Institutions: The University of Tokyo
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [memory], [WebChoreArena]
    - 📖 TLDR: This paper introduces *WebChoreArena*, a new fully reproducible benchmark comprising 532 carefully curated tasks designed to extend the scope of WebArena beyond general browsing to more labor-intensive and tedious tasks. WebChoreArena systematically integrates three key challenges: (i) Massive Memory tasks requiring accurate retrieval of large amounts of information in the observations, (ii) Calculation tasks demanding precise mathematical reasoning, and (iii) Long-Term Memory tasks necessitating long-term memory across multiple webpages. Our experiments indicate that even with Gemini 2.5 Pro, there remains substantial room for improvement compared to WebArena, highlighting the increased challenges posed by WebChoreArena.

- [Surfer‑H Meets Holo1: Cost‑Efficient Web Agent Powered by Open Weights](https://arxiv.org/abs/2506.02865)
    - Mathieu Andreux, Breno Baldas Skuk, Hamza Benchekroun, Emilien Biré, Antoine Bonnet, Riaz Bordie, Matthias Brunel, Pierre‑Louis Cedoz, Antoine Chassang, Mickaël Chen, Alexandra D. Constantinou, Antoine d’Andigné, Hubert de La Jonquière, Aurélien Delfosse, Ludovic Denoyer, Alexis Deprez, Augustin Derupti, Michael Eickenberg, Mathïs Federico, Charles Kantor, Xavier Koegler, Yann Labbé, Matthew C. H. Lee, Erwan Le Jumeau de Kergaradec, Amir Mahla, Avshalom Manevich, Adrien Maret, Charles Masson, Rafaël Maurin, Arturo Mena, Philippe Modard, Axel Moyal, Axel Nguyen Kerbel, Julien Revelle, Mats L. Richter, María Santos, Laurent Sifre, Maxime Theillard, Marc Thibault, Louis Thiry, Léo Tronchon, Nicolas Usunier, Tony Wu
    - 🏛️ Institutions: H Company
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [vision-language], [Holo1], [WebClick], [WebVoyager], [Surfer-H]
    - 📖 TLDR: Introduces **Surfer‑H**, a modular web-browsing agent (policy, localizer, validator) that operates purely via screenshots, paired with **Holo1**, a family of open-weight VLMs specialized in UI interaction. Holo1 is trained on a 31B token dataset across GUI grounding, visual reasoning, and agent traces, enabling strong UI localization via the new **WebClick** benchmark. Surfer‑H + Holo1‑7B achieves 92.2% success on WebVoyager—a state-of-the-art and cost-efficient web navigation performance—while releasing both the model weights and evaluation dataset

- [GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents](https://arxiv.org/abs/2506.03143)
    - Qianhui Wu, Kanzhi Cheng, Rui Yang, Chaoyun Zhang, Jianwei Yang, Huiqiang Jiang, Jian Mu, Baolin Peng, Bo Qiao, Reuben Tan, Si Qin, Lars Liden, Qingwei Lin, Huan Zhang, Tong Zhang, Jianbing Zhang, Dongmei Zhang, Jianfeng Gao
    - 🏛️ Institutions: Microsoft, Nanjing Univ., UIUC
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv (α); (likely under review / not yet accepted)
    - 💻 Env: [GUI] (applies across web/mobile/desktop)
    - 🔑 Key: [model], [framework], [grounding verifier], [attention mechanism], [coordinate‑free grounding], [GUI‑Actor]
    - 📖 TLDR: GUI‑Actor introduces a coordinate‑free visual grounding approach for GUI agents by adding an attention‑based “<ACTOR>” action head atop a frozen vision‑language model. It learns to align with relevant visual patches and produces multiple candidate regions per forward pass. An optional grounding verifier scores candidates to select the best. The method improves spatial‑semantic alignment and generalizes well across unseen resolutions. On benchmarks like ScreenSpot‑Pro, GUI‑Actor‑7B outperforms prior SOTA UI‑TARS‑72B, with verifier‑augmented versions achieving even higher accuracy—while only fine‑tuning ~100 M parameters.


- [DeepShop: A Benchmark for Deep Research Shopping Agents](https://arxiv.org/abs/2506.02839)
    - Yougang Lyu, Xiaoyu Zhang, Lingyong Yan, Maarten de Rijke, Zhaochun Ren, Xiuying Chen
    - 🏛️ Institutions: U Amsterdam, Shandong U, Baidu Inc., Leiden U, MBZUAI
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation framework], [RAG], [query complexity], [DeepShop]
    - 📖 TLDR: DeepShop introduces a comprehensive benchmark for web shopping agents, mirroring the real first-use complexity of online shopping scenarios. It features diversified query evolution across five domains, complexity-tier classification (easy/medium/hard), and a fine‐grained scoring system analyzing attribute matching, filters, and sorting. Evaluations across RAG and agentic systems reveal significant shortcomings, especially in handling filters and sorting, underscoring gaps in current research capabilities.

- [AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning](https://github.com/OpenBMB/AgentCPM-GUI)
    - Zhong Zhang, Yaxi Lu, Yikun Fu, Yupeng Huo, Shenzhi Yang, Yesai Wu, Han Si, Xin Cong, Haotian Chen, Yankai Lin, Jie Xie, Wei Zhou, Wang Xu, Yuanheng Zhang, Zhou Su, Zhongwu Zhai, Xiaoming Liu, Yudong Mei, Jianming Xu, Hongyan Tian, Chongyi Wang, Chi Chen, Yuan Yao, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: THUNLP, RUC, ModelBest
    - 📅 Date: June 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [benchmark], [reinforcement learning], [grounding], [CAGUI], [mobile use]
    - 📖 TLDR: AgentCPM-GUI is an 8B-parameter on-device GUI agent tailored for Android applications, emphasizing robust multilingual interaction. Built upon MiniCPM-V, it undergoes a three-stage training pipeline: grounding-aware pre-training on a 12M-sample bilingual dataset, supervised fine-tuning with 55K high-quality trajectories from over 30 Chinese apps, and reinforcement fine-tuning using the Group Relative Policy Optimization (GRPO) algorithm to enhance reasoning capabilities. The model introduces a compact JSON-based action space optimized for mobile efficiency. Evaluated across five benchmarks, including the newly introduced Chinese GUI benchmark CAGUI, AgentCPM-GUI achieves state-of-the-art performance, notably 96.9% Type-Match and 91.3% Exact-Match on CAGUI. All code, model checkpoints, and evaluation data are publicly released to support further research.

- [AgentCPM‑GUI: Building Mobile‑Use Agents with Reinforcement Fine‑Tuning](https://github.com/OpenBMB/AgentCPM-GUI)
    - Zhong Zhang, Yaxi Lu, Yikun Fu, Yupeng Huo, Shenzhi Yang, Yesai Wu, Han Si, Xin Cong, Haotian Chen, Yankai Lin, Jie Xie, Wei Zhou, Wang Xu, Yuanheng Zhang, Zhou Su, Zhongwu Zhai, Xiaoming Liu, Yudong Mei, Jianming Xu, Hongyan Tian, Chongyi Wang, Chi Chen, Yuan Yao, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Tsinghua, RUC, ModelBest
    - 📅 Date: June 2, 2025
    - 📑 Publisher: arXiv (arXiv:2506.01391)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [reinforcement fine‑tuning], [compact action space], [CAGUI], [GRPO]
    - 📖 TLDR: Introduces an 8 B Vision–Language GUI agent for on‑device mobile app interaction. Training uses grounding pre-training, supervised fine‑tuning on 55 K Chinese & English trajectories, and reinforcement fine‑tuning (GRPO). A compact JSON action schema enables low-latency inference. Achieves SOTA on five benchmarks including the new Chinese CAGUI (96 %+ TM, 91 % EM). All code, model, and data released.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://arxiv.org/abs/2505.21936)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: OSU
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [CUA], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [XBOUND: Exploring the Capability Boundaries of Device-Control Agents through Trajectory Tree Exploration](https://arxiv.org/abs/2505.21279)
    - Shaoqing Zhang, Kehai Chen, Zhuosheng Zhang, Rumei Li, Rongxiang Weng, Yang Xiang, Liqiang Nie, Min Zhang
    - 🏛️ Institutions: HIT Shenzhen (Harbin Institute of Technology), Pengcheng Lab, SJTU, Meituan
    - 📅 Date: May 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [dataset], [Explore Metric], [trajectory tree], [OS‑Atlas], [UI‑TARS]
    - 📖 TLDR: Introduces **XBOUND**, a novel evaluation framework assessing device-control (DC) agents at a fine-grained level by constructing "trajectory trees" from Android GUI interaction traces. The method defines an **Explore Metric**, measuring how well agents generalize across branching states and actions. A large-scale pseudo trajectory-tree dataset (~1,536 episodes, 43,759 instructions) was built using GPT4o-mini and Qwen2.5-vl. The study benchmarks OS‑Atlas and UI‑TARS agents across width/depth dimensions, revealing state and action comprehension gaps. It offers actionable insights into DC agent limitations and proposes directions for improving GUI-based agent capabilities. :contentReference[oaicite:0]{index=0}

- [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897)
    - Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiaochong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu
    - 🏛️ Institutions: HKU, Shanghai AI Lab, Fudan, Peking U, Nanjing U, ECNU, Yale
    - 📅 Date: May 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [environment], [POMDP], [GUI/CLI agents], [multimodal], [modular design], [ScienceBoard]
    - 📖 TLDR: Introduces **ScienceBoard**, a first-of-its-kind realistic multimodal environment and benchmark (169 tasks across six scientific domains) for evaluating agents that operate GUI and CLI workflows. Agents like GPT‑4o and Claude reach only ~15% success, revealing limitations in visual grounding and domain reasoning. Modular agent designs (separating planning and action) improve performance. Environment integrates real scientific tools via VM, accessibility trees, and screenshot inputs, setting the stage for more capable AI co‑scientists.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: likely Chinese institutions (not explicitly stated) — Unknown
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [progress reward model], [LCS-based self‑annotation], [reinforcement learning], [dataset: WikiHow task set / Android navigation benchmark]
    - 📖 TLDR: Introduces **ProgRM**, a novel framework giving dense intermediate rewards to GUI agents by estimating per‑step task progress. Labels are generated through an LCS‑based self‑annotation algorithm that identifies key steps in successful trajectories. Agents trained with ProgRM outperform outcome‑based reward models and proprietary LLMs like Claude‑3.7‑Sonnet across benchmarks.

- [GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://github.com/JiuTian-VL/GUI-explorer)
    - Bin Xie, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Jie Liu, Min Zhang, Liqiang Nie
    - 🏛️ Institutions: HIT‑SZ (Harbin Institute of Technology, Shenzhen), Huawei Noah’s Ark Lab
    - 📅 Date: May 22, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [transition-aware knowledge], [autonomous exploration], [benchmark], [GUI-KRB]
    - 📖 TLDR: Introduces **GUI‑explorer**, a training‑free agent for mobile GUIs that auto‑generates function‑aware exploration goals and mines transition‑aware knowledge from UI transitions. It builds a multimodal knowledge store and dynamically guides MLLMs like GPT‑4o at runtime, achieving state‑of‑the‑art success rates (53.7% on SPA‑Bench, 47.4% on AndroidWorld) without retraining. Also introduces GUI‑KRB, a benchmark highlighting GUI reasoning limitations and guiding future work.

- [Building a Stable Planner: An Extended Finite State Machine Based Planning Module for Mobile GUI Agent](https://arxiv.org/abs/2505.14141)
    - Fanglin Mo, Junzhe Chen, Haoxuan Zhu, Xuming Hu
    - 🏛️ Institutions: HKUST‑GZ, SCUT
    - 📅 Date: May 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [EFSM], [SPlanner], [planning], [vision-language model], [AndroidWorld benchmark]
    - 📖 TLDR: Introduces **SPlanner**, a plug‑and‑play planning module that models mobile apps as Extended Finite State Machines (EFSMs). It decomposes user instructions into primary functions, traverses EFSMs to obtain execution paths, and refines these into natural-language plans to guide vision‑language models. On the AndroidWorld benchmark, pairing SPlanner with Qwen2.5‑VL‑72B achieves 63.8% success—28.8 points higher than the baseline, demonstrating improved stability and task planning in mobile GUI agents.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://osworld-grounding.github.io/)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv (preprint)
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [framework], [Jedi], [OSWorld‑G], [GUI grounding], [compositional generalization], [fine‑grained manipulation]
    - 📖 TLDR: This work tackles limitations in GUI grounding by introducing **OSWorld‑G**, a 564‑sample benchmark covering text matching, element recognition, layout understanding, fine‑grained manipulation, and refusal detection. They also synthesize **Jedi**, a massive 4 M‑example dataset generated via UI decomposition and synthesis. Training multi‑scale models on Jedi achieves state‑of‑the‑art grounding across benchmarks (ScreenSpot‑v2/Pro and OSWorld‑G), boosting agentic task performance from 5 % to ~27 % success. Ablations demonstrate compositional benefits. All artifacts are publicly released.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: UMich, LG AI Research
    - 📅 Date: May 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [RegionFocus], [test-time scaling], [grounding], [Qwen2.5-VL], [UI-TARS]
    - 📖 TLDR: This paper introduces *RegionFocus*, a visual test-time scaling method for GUI agents that dynamically zooms into relevant regions within GUI images, reducing background clutter and enhancing grounding accuracy. By integrating an "image-as-map" mechanism to visualize key landmarks during each interaction step, the approach improves transparency and decision-making. Applied to state-of-the-art vision-language models like UI-TARS and Qwen2.5-VL, RegionFocus achieves significant performance gains—28% on ScreenSpot-Pro and 24% on WebVoyager benchmarks—setting a new state-of-the-art grounding accuracy of 61.6% on ScreenSpot-Pro.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://github.com/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, Wenhao Wang, Tianze Wu, Linghao Li, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: Zhejiang Univ., vivo AI Lab, CUHK MMLab
    - 📅 Date: April 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [framework], [dataset], [benchmark], [planning], [multimodal], [taxonomy]
    - 📖 TLDR: This comprehensive survey examines the evolution of LLM-powered GUI agents in mobile phone automation, transitioning from static scripts to intelligent, adaptive systems. It presents a taxonomy encompassing agent frameworks (single-agent, multi-agent, plan-then-act), modeling approaches (prompt engineering, training-based), and essential datasets and benchmarks. The paper discusses how LLMs enhance language understanding, multimodal perception, and decision-making in GUI tasks, and addresses challenges such as dataset diversity, on-device deployment efficiency, user-centric adaptation, and security concerns. It serves as a definitive reference for researchers and practitioners aiming to leverage LLMs in designing scalable, user-friendly phone GUI agents.

- [UFO2: The Desktop AgentOS](https://arxiv.org/abs/2504.14603)
    - Chaoyun Zhang, He Huang, Chiming Ni, Jian Mu, Si Qin, Shilin He, Lu Wang, Fangkai Yang, Pu Zhao, Chao Du, Liqun Li, Yu Kang, Zhao Jiang, Suzhen Zheng, Rujia Wang, Jiaxu Qian, Minghua Ma, Jian-Guang Lou, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
    - 🏛️ Institutions: Microsoft Research, ZJU-UIUC Institute, Nanjing University, Peking University
    - 📅 Date: April 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [hybrid control], [multi-agent], [speculative execution], [knowledge substrate], [UFO2]
    - 📖 TLDR: UFO2 introduces a multi-agent AgentOS for Windows desktops, aiming to transform Computer-Using Agents (CUAs) from fragile prototypes into robust, system-level automation tools. It features a centralized HostAgent for task decomposition and coordination, along with specialized AppAgents equipped with native APIs and domain-specific knowledge. The system employs a hybrid control detection pipeline combining Windows UI Automation with vision-based parsing, and enhances runtime efficiency through speculative multi-action planning. A Picture-in-Picture interface allows agents and users to operate concurrently without interference. Evaluated across over 20 real-world Windows applications, UFO2 demonstrates significant improvements in robustness and execution accuracy over prior CUAs.

- [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://lgy0404.github.io/LearnAct)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, Shibo He, Wenchao Meng
    - 🏛️ Institutions: ZJU, vivo AI Lab
    - 📅 Date: April 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [few-shot learning], [LearnAct], [LearnGUI], [DemoParser], [KnowSeeker], [ActExecutor]
    - 📖 TLDR: This paper introduces **LearnAct**, a multi-agent framework designed to enhance mobile GUI agents through few-shot demonstration learning. Accompanied by **LearnGUI**, a dataset comprising 2,252 offline and 101 online tasks with high-quality human demonstrations, the framework integrates three specialized agents—DemoParser, KnowSeeker, and ActExecutor—to extract, retrieve, and apply knowledge from demonstrations. Experimental results show significant performance improvements in both offline and online evaluations, establishing demonstration-based learning as a promising direction for developing adaptable and personalized mobile GUI agents.

- [TongUI: Building Generalized GUI Agents by Learning from Multimodal Web Tutorials](https://tongui-agent.github.io/)
    - Bofei Zhang, Zirui Shang, Zhi Gao, Wang Zhang, Rui Xie, Xiaojian Ma, Tao Yuan, Xinxiao Wu, Song-Chun Zhu, Qing Li
    - 🏛️ Institutions: BIGAI, BIT, PKU, SJTU, THU
    - 📅 Date: April 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [Qwen2.5-VL], [GUI-Net], [multimodal], [trajectory generation]
    - 📖 TLDR: This paper introduces **TongUI**, a framework for building generalized GUI agents by learning from multimodal web tutorials. By crawling and processing online tutorials into GUI agent trajectory data, the authors construct the **GUI-Net** dataset containing 143K trajectories across five operating systems and over 200 applications. Fine-tuning Qwen2.5-VL-3B/7B models on GUI-Net leads to significant performance improvements on grounding and navigation benchmarks, demonstrating the effectiveness of the TongUI framework.

- [REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://realevals.xyz)
    - Divyansh Garg, Shaun VanWeelden, Diego Caples, Andis Draguns, Nikil Ravi, Pranav Putta, Naman Garg, Tomas Abraham, Michael Lara, Federico Lopez, James Liu, Atharva Gundawar, Prannay Hebbar, Youngchul Joo, Charles London, Christian Schroeder de Witt, Sumeet Motwani
    - 🏛️ Institutions: AGI Inc.
    - 📅 Date: April 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [dataset], [evaluation], [reproducibility], [multi-turn tasks], [REAL]
    - 📖 TLDR: This paper introduces **REAL**, a benchmark and framework designed for evaluating autonomous agents through deterministic simulations of real-world websites. REAL encompasses high-fidelity replicas of 11 widely-used websites across domains like e-commerce, travel, communication, and professional networking. It includes 112 practical tasks that mirror complex user interactions requiring both accurate information retrieval and state-changing actions. The controlled environment ensures safety and reproducibility, combining programmatic checks for action-based tasks with rubric-guided LLM-based judgments for information retrieval. Empirical results reveal that current frontier language models achieve at most a 41% success rate on REAL, highlighting significant gaps in autonomous web navigation and task completion capabilities.

- [UI-E2I-Synth: Advancing GUI Grounding with Large-Scale Instruction Synthesis](https://arxiv.org/abs/2504.11257)
    - Xinyi Liu, Xiaoyi Zhang, Ziyun Zhang, Yan Lu
    - 🏛️ Institutions: MSRA, PKU
    - 📅 Date: April 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [instruction synthesis], [UI-E2I-Synth], [UI-I2E-Bench], [GPT-4o]
    - 📖 TLDR: This paper introduces **UI-E2I-Synth**, a large-scale data synthesis pipeline that generates diverse GUI grounding instructions using GPT-4o, addressing challenges like implicit instructions and unbalanced element types. It also presents **UI-I2E-Bench**, a new benchmark with detailed annotations for evaluating GUI instruction grounding. Models trained on the synthesized data demonstrate superior performance across multiple platforms, highlighting the effectiveness of the proposed approach.

- [Breaking the Data Barrier -- Building GUI Agents Through Task Generalization](https://arxiv.org/abs/2504.10127)
    - Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, Qiushi Sun, Zhenzhong Lan, Junxian He
    - 🏛️ Institutions: ZJU, WestlakeU, Shanghai AI Lab, HKU, HKUST
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [mid-training], [reasoning], [GUIMid]
    - 📖 TLDR: This paper introduces a mid-training approach to enhance GUI agents by leveraging diverse, reasoning-intensive datasets such as mathematical and coding tasks. The authors demonstrate that training Vision Language Models (VLMs) on these data-rich tasks before fine-tuning on limited GUI trajectory data significantly improves performance on GUI benchmarks like WebArena and AndroidWorld. Notably, text-only mathematical reasoning data led to substantial cross-modal gains, highlighting the effectiveness of task generalization in overcoming data scarcity challenges in GUI agent development.

- [RealWebAssist: A Benchmark for Long-Horizon Web Assistance with Real-World Users](https://scai.cs.jhu.edu/projects/RealWebAssist/)
    - Suyu Ye, Haojun Shi, Darren Shih, Hyokun Yun, Tanya Roosta, Tianmin Shu
    - 🏛️ Institutions: JHU, Amazon
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [GUI grounding], [speech input], [spatial reasoning], [temporal reasoning], [multi-step planning], [routine learning], [RealWebAssist]
    - 📖 TLDR: RealWebAssist introduces a benchmark for evaluating AI agents' ability to assist with long-horizon web tasks using sequential instructions from real-world users. The dataset includes 1,885 instructions across 107 tasks on 66 websites, featuring challenges like ambiguous instructions, GUI grounding, and evolving user goals. Evaluations show that current state-of-the-art models struggle with these complex, realistic scenarios.

- [AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://agent-reward-bench.github.io/)
    - Xing Han Lù, Amirhossein Kazemnejad, Nicholas Meade, Arkil Patel, Dongchan Shin, Alejandra Zambrano, Karolina Stańczak, Peter Shaw, Christopher J. Pal, Siva Reddy
    - 🏛️ Institutions: McGill, Mila, Google DeepMind, Polytechnique Montréal, ServiceNow Research
    - 📅 Date: April 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [LLM judges], [AgentRewardBench]
    - 📖 TLDR: This paper introduces *AgentRewardBench*, a benchmark designed to assess the effectiveness of large language model (LLM) judges in evaluating web agent trajectories. The benchmark comprises 1,302 trajectories across five web benchmarks, each annotated by experts for success, side effects, and repetitiveness. Evaluations of 12 LLM judges reveal that no single model excels across all benchmarks, and that rule-based evaluations often underreport agent success rates, highlighting the need for more adaptable automatic evaluation methods.

- [Inducing Programmatic Skills for Agentic Tasks](https://arxiv.org/abs/2504.06821)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: CMU, Microsoft
    - 📅 Date: April 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [model], [benchmark], [learning], [reasoning], [planning], [ASI], [WebArena]
    - 📖 TLDR: This paper introduces Agent Skill Induction (ASI), a framework enabling web agents to learn and apply programmatic skills dynamically. By representing skills as executable programs, ASI allows agents to verify and reuse these skills across tasks, enhancing adaptability and efficiency. Evaluated on the WebArena benchmark, ASI outperforms static and text-based skill agents in success rate and step efficiency, demonstrating improved generalization and adaptability to new web environments.

- [On the Robustness of GUI Grounding Models Against Image Attacks](https://arxiv.org/abs/2504.04716)
    - Haoren Zhao, Tianyi Chen, Zhen Wang
    - 🏛️ Institutions: HDU, Microsoft
    - 📅 Date: April 7, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [robustness], [adversarial attacks], [UGround], [ScreenSpot-V2]
    - 📖 TLDR: This paper systematically evaluates the robustness of GUI grounding models, such as UGround, against natural noise, untargeted adversarial attacks, and targeted adversarial attacks. Experiments conducted across mobile, desktop, and web interfaces reveal that these models are highly sensitive to adversarial perturbations and low-resolution conditions. The findings highlight vulnerabilities in current GUI grounding models and establish a benchmark for future research aimed at enhancing their robustness in practical applications.

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://arxiv.org/abs/2504.01382)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, UC Berkeley
    - 📅 Date: April 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [Online-Mind2Web], [WebJudge], [Operator], [LLM-as-a-Judge]
    - 📖 TLDR: This paper critically evaluates the performance of current web agents, revealing that many underperform on the newly introduced **Online-Mind2Web** benchmark, which comprises 300 realistic tasks across 136 websites. The study highlights a discrepancy between reported successes and actual capabilities, attributing this to shortcomings in existing benchmarks. To address evaluation scalability, the authors propose **WebJudge**, an automatic LLM-based evaluation method achieving approximately 85% agreement with human judgments. The comprehensive analysis underscores the need for more robust assessment frameworks in web agent research.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://arxiv.org/abs/2504.00906)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [Mixture-of-Grounding], [Proactive Hierarchical Planning], [benchmark], [OSWorld], [WindowsAgentArena], [AndroidWorld]
    - 📖 TLDR: This paper introduces *Agent S2*, a compositional framework for computer use agents that combines generalist and specialist models to address challenges in GUI element grounding and long-horizon task planning. The framework employs a novel Mixture-of-Grounding technique for precise GUI localization and Proactive Hierarchical Planning to dynamically refine action plans. Evaluations demonstrate that Agent S2 achieves state-of-the-art performance on benchmarks like OSWorld, WindowsAgentArena, and AndroidWorld, outperforming existing agents such as Claude Computer Use and UI-TARS.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Tsinghua University, NTU, UT Austin
    - 📅 Date: March 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [benchmark], [V-Droid], [verifier-driven], [pair-wise preference training], [human-agent joint annotation], [low-latency]
    - 📖 TLDR: This paper introduces **V-Droid**, a mobile GUI automation agent that leverages large language models (LLMs) as verifiers rather than generators. By evaluating candidate actions before execution, V-Droid enhances decision-making accuracy and reduces latency. The framework incorporates discretized action space construction, a prefilling-only workflow, pair-wise preference training, and a scalable human-agent joint annotation scheme. Evaluated on benchmarks like AndroidWorld, AndroidLab, and MobileAgentBench, V-Droid achieves state-of-the-art success rates and operates with near-real-time decision-making capabilities.

- [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661)
    - Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Juan A. Rodriguez, Montek Kalsi, Rabiul Awal, Nicolas Chapados, M. Tamer Özsu, Aishwarya Agrawal, David Vazquez, Christopher Pal, Perouz Taslakian, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [framework], [UI-Vision], [UI-TARS-72B], [spatial reasoning], [drag-and-drop], [element grounding], [layout grounding], [action prediction]
    - 📖 TLDR: This paper introduces *UI-Vision*, a comprehensive, license-permissive benchmark designed for evaluating autonomous agents in real-world desktop GUI environments. It encompasses 83 software applications with dense annotations of human demonstrations, including bounding boxes, UI labels, and action trajectories. The benchmark defines three tasks—Element Grounding, Layout Grounding, and Action Prediction—to assess agents' performance. Evaluations reveal limitations in state-of-the-art models like UI-TARS-72B, particularly in understanding professional software, spatial reasoning, and complex actions such as drag-and-drop. By releasing UI-Vision as open-source, the authors aim to advance the development of more capable agents for desktop tasks.

- [STEVE: A Step Verification Pipeline for Computer-use Agent Training](https://github.com/FanbinLu/STEVE)
    - Fanbin Lu, Zhisheng Zhong, Ziqin Wei, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: CUHK, SmartMore, HKUST
    - 📅 Date: March 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [model], [UI grounding], [KTO], [GPT-4o], [WinAgentArena]
    - 📖 TLDR: This paper introduces **STEVE**, a step verification pipeline designed to enhance the training of computer-use agents. The approach involves creating a large instruction set and collecting trajectory data using suboptimal agents. GPT-4o is employed to verify the correctness of each action step by comparing pre- and post-action screenshots, assigning binary labels. The agent is then optimized using Kahneman and Tversky Optimization (KTO) based on these labels. The result is a 7B vision-language model that achieves state-of-the-art performance in the WinAgentArena desktop environment, outperforming supervised fine-tuning methods by effectively leveraging both positive and negative action data.

- [DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents](https://arxiv.org/abs/2503.11170)
    - Yibin Xu, Liang Yang, Hao Chen, Hua Wang, Zhi Chen, Yaohua Tang
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [model], [AutoCaptioner], [DeskVision], [DeskVision-Eval], [GUIExplorer]
    - 📖 TLDR: This paper introduces *AutoCaptioner*, an automated pipeline for generating richly annotated GUI data with minimal human effort. Utilizing AutoCaptioner, the authors created *DeskVision*, a large-scale desktop GUI dataset comprising 54,855 images and over 303,622 annotations across various operating systems. They also developed *DeskVision-Eval*, the largest desktop benchmark reflecting daily usage scenarios. Leveraging DeskVision, the authors trained *GUIExplorer*, a GUI understanding model that achieves state-of-the-art performance in grounding visual elements without complex architectural designs. The effectiveness of DeskVision was further validated through ablation studies on various large visual language models (LVLMs).

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: March 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [dual-system cognition], [FOCUS], [ScreenSpot], [ScreenSpot-Pro]
    - 📖 TLDR: This paper introduces **FOCUS**, a novel GUI grounding framework inspired by human dual-system cognition. FOCUS dynamically switches between a fast, intuitive system and a slow, analytical system based on task complexity. The framework decomposes GUI grounding into three stages: interface summarization, focused analysis, and precise coordinate prediction. Trained on a synthesized dataset of 300,000 samples, FOCUS achieves state-of-the-art performance on the ScreenSpot and ScreenSpot-Pro benchmarks, demonstrating significant improvements in both efficiency and accuracy for complex GUI interactions.

- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis](https://vulnerable-ai-agents.github.io/)
    - Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
    - 🏛️ Institutions: UMD
    - 📅 Date: March 4, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [security], [jailbreaking], [evaluation], [OpenHands]
    - 📖 TLDR: This paper investigates why Web AI agents are significantly more susceptible to executing harmful commands compared to standalone LLMs, despite sharing the same underlying models. Through a fine-grained evaluation, the authors identify three critical factors contributing to this vulnerability: embedding user goals into system prompts, multi-step action generation, and processing of event streams from web navigation. The study introduces a five-level harmfulness evaluation framework and utilizes the OpenHands platform to systematically assess these vulnerabilities, revealing a 46.6% success rate in malicious task execution by Web AI agents versus 0% for standalone LLMs.

- [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)
    - Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Deyu Zhou, Pengjun Xie, Fei Huang
    - 🏛️ Institutions: Tongyi Lab, Alibaba NLP
    - 📅 Date: January 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [RAG], [WebWalker], [WebWalkerQA]
    - 📖 TLDR: This paper presents **WebWalker**, a multi-agent framework designed to improve the ability of large language models (LLMs) to traverse websites, addressing the challenges of retrieving complex, multi-layered information. WebWalker integrates an "explore-critic" paradigm, where the explorer agent navigates the web, and the critic agent evaluates the progress. The **WebWalkerQA** benchmark is introduced to assess web traversal tasks, showing how retrieval-augmented generation (RAG) can be enhanced with vertical exploration to solve real-world queries.

- [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://likaixin2000.github.io/papers/ScreenSpot_Pro.pdf)
    - Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, Tat-Seng Chua
    - 🏛️ Institutions: NUS, ECNU, HKBU
    - 📅 Date: January 3, 2025
    - 📑 Publisher: GitHub
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [GUI grounding], [high-resolution], [ScreenSpot-Pro]
    - 📖 TLDR: ScreenSpot-Pro introduces a benchmark designed to evaluate GUI grounding models in professional, high-resolution environments. It encompasses 1,581 tasks across 23 applications in various industries, highlighting the challenges models face with complex software interfaces. Current models achieve low accuracy, underscoring the need for further research in this domain.

- [The BrowserGym Ecosystem for Web Agent Research](https://arxiv.org/abs/2412.05467)
    - Thibault Le Sellier De Chezelles, Maxime Gasse, Alexandre Drouin, Massimo Caccia, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Quentin Cappart, Graham Neubig, Ruslan Salakhutdinov, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, CMU, McGill University, Tel Aviv University, Université de Montréal, iMean AI
    - 📅 Date: December 6, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [LLM], [automation], [BrowserGym], [AgentLab]
    - 📖 TLDR: This paper presents *BrowserGym*, an ecosystem designed to standardize the evaluation and benchmarking of web agents, particularly those leveraging Large Language Models (LLMs). It addresses the challenges posed by fragmented benchmarks and inconsistent methodologies in web agent research. BrowserGym provides a unified, gym-like environment with clearly defined observation and action spaces, enabling reproducible comparisons across various benchmarks. Additionally, *AgentLab*, a complementary framework, supports agent creation, testing, and analysis. The paper also features a large-scale experiment comparing the performance of 6 leading LLMs, highlighting the strengths and weaknesses of different models in real-world web tasks, while emphasizing the ongoing challenges in building efficient and robust web agents.

- [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://arxiv.org/abs/2410.24024)
    - Yifan Xu, Xiao Liu, Xueqiao Sun, Siyi Cheng, Hao Yu, Hanyu Lai, Shudan Zhang, Dan Zhang, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Peking University
    - 📅 Date: October 31, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [AndroidLab]
    - 📖 TLDR: This paper introduces **AndroidLab**, a comprehensive framework for training and systematically benchmarking Android autonomous agents. It provides an operational environment with diverse modalities and action spaces, supporting both large language models (LLMs) and multimodal models (LMMs). The benchmark includes 138 tasks across nine apps on predefined Android virtual devices. Utilizing AndroidLab, the authors developed an Android Instruction dataset and trained six open-source LLMs and LMMs, significantly improving their average success rates.

- [OS-ATLAS: A Foundation Action Model For Generalist GUI Agents](https://osatlas.github.io/)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Lab, SJTU, HKU, MIT
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [OS-Atlas]
    - 📖 TLDR: This paper introduces OS-Atlas, a foundational GUI action model designed to enhance GUI grounding and out-of-distribution tasks. The authors developed a toolkit to synthesize multi-platform GUI grounding data, resulting in a cross-platform corpus of over 13 million GUI elements. OS-Atlas demonstrates significant performance improvements across six benchmarks spanning mobile, desktop, and web platforms.

- [Evaluating Cultural and Social Awareness of LLM Web Agents](https://arxiv.org/abs/2410.23252)
    - Haoyi Qiu, Alexander R. Fabbri, Divyansh Agarwal, Kung-Hsiang Huang, Sarah Tan, Nanyun Peng, Chien-Sheng Wu
    - 🏛️ Institutions: UCLA, Salesforce AI Research
    - 📅 Date: October 30, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [CASA], [cultural awareness], [social awareness], [fine-tuning], [prompting]
    - 📖 TLDR: This paper introduces CASA, a benchmark designed to assess the cultural and social awareness of LLM web agents in tasks like online shopping and social discussion forums. It evaluates agents' abilities to detect and appropriately respond to norm-violating user queries and observations. The study finds that current LLM agents have limited cultural and social awareness, with less than 10% awareness coverage and over 40% violation rates. To enhance performance, the authors explore prompting and fine-tuning methods, demonstrating that combining both can offer complementary advantages.

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: XJTU, Shanghai AI Lab, HKU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [multi-agent systems], [specialized generalist agent], [OSWorld benchmark]
    - 📖 TLDR: AgentStore introduces a scalable platform to integrate and manage heterogeneous agents, designed to enhance generalist assistant capabilities for diverse computer tasks. Using a MetaAgent and AgentToken strategy, AgentStore shows improved generalization on the OSWorld benchmark.

- [Beyond Browsing: API-Based Web Agents](https://arxiv.org/pdf/2410.16464)
    - Yueqi Song, Frank Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: CMU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [benchmark], [WebArena], [SOTA performance]
    - 📖 TLDR: This paper introduces API-based and hybrid agents designed to execute online tasks by accessing both APIs and traditional web browsing interfaces. In evaluations using WebArena, a benchmark for web navigation, the API-based agent achieves higher performance than browser-based agents, and the hybrid model achieves a success rate of 35.8%, setting a new state-of-the-art (SOTA) in task-agnostic web navigation. The findings highlight the efficiency and reliability gains of API interactions for web agents.

- [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://doi.org/10.48550/arXiv.2410.19100)
    - Lawrence Jang, Yinheng Li, Charles Ding, Justin Lin, Paul Pu Liang, Dan Zhao, Rogerio Bonatti, Kazuhito Koishida
    - 🏛️ Institutions: CMU, MIT, NYU, Microsoft
    - 📅 Date: October 24, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [video understanding], [long-context], [VideoWA]
    - 📖 TLDR: This paper introduces **VideoWebArena (VideoWA)**, a benchmark assessing multimodal agents in video-based tasks. It features over 2,000 tasks focused on skill and factual retention, using video tutorials to simulate long-context environments. Results highlight current challenges in agentic abilities, providing a critical testbed for long-context video understanding improvements.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, UT at Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [evaluation], [Android emulator]
    - 📖 TLDR: *MobileSafetyBench* introduces a benchmark for evaluating the safety of large language model (LLM)-based autonomous agents in mobile device control. Using Android emulators, the benchmark simulates real-world tasks in apps such as messaging and banking to assess agents' safety and helpfulness. The safety-focused tasks test for privacy risk management and robustness against adversarial prompt injections. Experiments show agents perform well in helpful tasks but struggle with safety-related challenges, underscoring the need for continued advancements in mobile safety mechanisms for autonomous agents.

- [Large Language Models Empowered Personalized Web Agents](https://ar5iv.org/abs/2410.17236)
    - Hongru Cai, Yongqi Li, Wenjie Wang, Fengbin Zhu, Xiaoyu Shen, Wenjie Li, Tat-Seng Chua
    - 🏛️ Institutions: HK PolyU, NTU Singapore
    - 📅 Date: Oct 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [personalized web agent], [user behavior alignment], [memory-enhanced alignment]
    - 📖 TLDR: This paper proposes a novel framework, *Personalized User Memory-enhanced Alignment (PUMA)*, enabling large language models to serve as personalized web agents by incorporating user-specific data and historical web interactions. The authors also introduce a benchmark, *PersonalWAB*, to evaluate these agents on various personalized web tasks. Results show that PUMA improves web agent performance by optimizing action execution based on user-specific preferences.

- [AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://arxiv.org/abs/2407.15711)
    - Ori Yoran, Samuel Joseph Amouyal, Chaitanya Malaviya, Ben Bogin, Ofir Press, Jonathan Berant
    - 🏛️ Institutions: Tel Aviv University
    - 📅 Date: October 21, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [planning and reasoning]
    - 📖 TLDR: AssistantBench is a benchmark designed to test the abilities of web agents in completing time-intensive, realistic web-based tasks. Covering 214 tasks across various domains, the benchmark introduces the SPA (See-Plan-Act) framework to handle multi-step planning and memory retention. AssistantBench emphasizes realistic task completion, showing that current agents achieve only modest success, with significant improvements needed for complex information synthesis and execution across multiple web domains.

- [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://ai-agents-2030.github.io/SPA-Bench/)
    - Jingxuan Chen, Derek Yuen, Bin Xie, Yuhao Yang, Gongwei Chen, Zhihao Wu, Li Yixing, Xurui Zhou, Weiwen Liu, Shuai Wang, Rui Shao, Liqiang Nie, Yasheng Wang, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, Harbin Institute of Technology, Shenzhen, UCL
    - 📅 Date: October 19, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [AI agent], [smartphone control], [framework]
    - 📖 TLDR: SPA-Bench is introduced as a benchmark designed to evaluate multimodal large language model (MLLM)-based smartphone agents, offering a task set that spans common smartphone functionalities across system and third-party applications. It includes a plug-and-play framework for real-time agent interactions on Android, integrating over ten agents with an adaptable evaluation pipeline measuring success across diverse metrics. Through this, the benchmark exposes challenges such as UI interpretation, action grounding, and memory retention in mobile environments, advancing research in smartphone-based agent applications.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2404.03648)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU
    - 📅 Date: October 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [reinforcement learning]
    - 📖 TLDR: AutoWebGLM introduces a web navigation agent based on ChatGLM3-6B, designed to autonomously navigate and interact with webpages for complex tasks. The paper highlights a two-phase data construction approach using a hybrid human-AI methodology for diverse, curriculum-based web task training. It also presents AutoWebBench, a benchmark for evaluating agent performance in web tasks, and uses reinforcement learning to fine-tune operations, addressing complex webpage interaction and grounding.

- [ClickAgent: Enhancing UI Location Capabilities of Autonomous Agents](https://arxiv.org/abs/2410.11872)
    - Jakub Hoscilowicz, Bartosz Maj, Bartosz Kozakiewicz, Oleksii Tymoschuk, Artur Janicki
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 9, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [SeeClick], [AITW benchmark]
    - 📖 TLDR: The paper introduces *ClickAgent*, a framework that enhances autonomous agents' interaction with mobile UIs by improving their ability to locate interface elements accurately. This is achieved through a dual-component system where an MLLM performs reasoning and action planning, while a dedicated UI location model (e.g., SeeClick) handles element identification. ClickAgent, evaluated on the AITW benchmark and tested on both emulators and real Android devices, surpasses other agents like CogAgent and AppAgent in task success rate, advancing automation reliability on mobile platforms.

- [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://sites.google.com/view/st-webagentbench/home)
    - Ido Levy, Ben Wiesel, Sami Marreed, Alon Oved, Avi Yaeli, Segev Shlomov
    - 🏛️ Institutions: IBM Research
    - 📅 Date: October 9, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [trustworthiness], [ST-WebAgentBench]
    - 📖 TLDR: This paper introduces **ST-WebAgentBench**, a benchmark designed to evaluate the safety and trustworthiness of web agents in enterprise contexts. It defines safe and trustworthy agent behavior, outlines the structure of safety policies, and introduces the "Completion under Policies" metric to assess agent performance. The study reveals that current state-of-the-art agents struggle with policy adherence, highlighting the need for improved policy awareness and compliance in web agents.

- [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://microsoft.github.io/WindowsAgentArena/)
    - Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, Yadong Lu, Justin Wagle, Kazuhito Koishida, Arthur Bucker, Lawrence Jang, Zack Hui
    - 🏛️ Institutions: Microsoft
    - 📅 Date: September 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [Navi]
    - 📖 TLDR: This paper introduces the *Windows Agent Arena (WAA)*, a scalable platform for testing and benchmarking multi-modal AI agents within a realistic Windows OS environment. WAA enables researchers to evaluate agentic workflows across diverse tasks and supports large-scale deployment using Azure ML. The study also presents *Navi*, a multi-modal agent achieving a 19.5% success rate on Windows tasks, highlighting the platform's potential for advancing AI agent development.

- [From Grounding to Planning: Benchmarking Bottlenecks in Web Agents](https://arxiv.org/abs/2409.01927)
    - Segev Shlomov, Ben Wiesel, Aviad Sela, Ido Levy, Liane Galanti, Roy Abitbol
    - 🏛️ Institutions: IBM
    - 📅 Date: September 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [grounding], [Mind2Web dataset], [web navigation]
    - 📖 TLDR: This paper analyzes performance bottlenecks in web agents by separately evaluating grounding and planning tasks, isolating their individual impacts on navigation efficacy. Using an enhanced version of the Mind2Web dataset, the study reveals planning as a significant bottleneck, with advancements in grounding and task-specific benchmarking for elements like UI component recognition. Through experimental adjustments, the authors propose a refined evaluation framework, aiming to enhance web agents' contextual adaptability and accuracy in complex web environments.

- [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://arxiv.org/abs/2408.06327)
    - Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Yifan Xu, Xixuan Song, Shudan Zhang, Hanyu Lai, Xinyi Liu, Hanlin Zhao, Jiadai Sun, Xinyue Yang, Yu Yang, Zehan Qi, Shuntian Yao, Xueqiao Sun, Siyi Cheng, Qinkai Zheng, Hao Yu, Hanchen Zhang, Wenyi Hong, Ming Ding, Lihang Pan, Xiaotao Gu, Aohan Zeng, Zhengxiao Du, Chan Hee Song, Yu Su, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, MSRA, The Ohio State University
    - 📅 Date: August 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [VisualAgentBench], [VAB]
    - 📖 TLDR: The authors introduce *VisualAgentBench (VAB)*, a comprehensive benchmark designed to train and evaluate large multimodal models (LMMs) as visual foundation agents across diverse scenarios, including embodied tasks, graphical user interfaces, and visual design. VAB comprises five distinct environments that systematically challenge LMMs' understanding and interaction capabilities. Additionally, the benchmark offers supervised fine-tuning trajectory data for behavior cloning training, demonstrating the potential to improve open LMMs for serving as visual foundation agents.

- [CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://aclanthology.org/2024.findings-acl.539)
    - Xinbei Ma, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: SJTU
    - 📅 Date: August 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [benchmark]
    - 📖 TLDR: This paper presents CoCo-Agent, a multimodal large language model (MLLM) designed for smartphone GUI automation. It introduces two novel approaches: Comprehensive Environment Perception (CEP) for enhanced GUI understanding, and Conditional Action Prediction (CAP) to improve action response accuracy. The proposed agent achieves state-of-the-art performance on GUI automation benchmarks such as AITW and META-GUI, showcasing its capabilities in realistic scenarios.

- [OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation](https://arxiv.org/abs/2407.19056)
    - Zilong Wang, Yuedong Cui, Li Zhong, Zimin Zhang, Da Yin, Bill Yuchen Lin, Jingbo Shang
    - 🏛️ Institutions: UCSD, UCLA, AI2
    - 📅 Date: July 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multi-application], [office automation]
    - 📖 TLDR: OfficeBench introduces a benchmark that evaluates language models' ability to automate office tasks across a range of applications like Word, Excel, and email. The benchmark tests agents’ skills in task-switching, planning, and decision-making by simulating realistic office workflows. Current models, including GPT-4, demonstrate significant gaps in task accuracy and efficiency, revealing areas for improvement in managing complex, multi-application tasks in office environments.

- [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://spider2-v.github.io/)
    - Ruisheng Cao, Fangyu Lei, Haoyuan Wu, Jixuan Chen, Yeqiao Fu, Hongcheng Gao, Xinzhuang Xiong, Hanchong Zhang, Yuchen Mao, Wenjing Hu, Tianbao Xie, Hongsheng Xu, Danyang Zhang, Sida Wang, Ruoxi Sun, Pengcheng Yin, Caiming Xiong, Ansong Ni, Qian Liu, Victor Zhong, Lu Chen, Kai Yu, Tao Yu
    - 🏛️ Institutions: HKU, SJTU, Google Cloud AI Research, Google DeepMind, Salesforce Research, Yale University, Sea AI Lab, University of Waterloo
    - 📅 Date: July 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [data science], [engineering workflows], [Spider2-V]
    - 📖 TLDR: This paper introduces **Spider2-V**, a multimodal agent benchmark designed to evaluate the capability of agents in automating professional data science and engineering workflows. It comprises 494 real-world tasks across 20 enterprise-level applications, assessing agents' proficiency in code generation and GUI operations within authentic computer environments.

- [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://arxiv.org/abs/2407.05291)
    - Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, Alexandre Drouin
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Université de Montréal
    - 📅 Date: July 7, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [reasoning], [WorkArena++]
    - 📖 TLDR: This paper introduces **WorkArena++**, a benchmark comprising 682 tasks that simulate realistic workflows performed by knowledge workers. It evaluates web agents' capabilities in planning, problem-solving, logical/arithmetic reasoning, retrieval, and contextual understanding. The study reveals challenges faced by current large language models and vision-language models in serving as effective workplace assistants, providing a resource to advance autonomous agent development. [oai_citation_attribution:0‡arXiv](https://arxiv.org/abs/2407.05291?utm_source=chatgpt.com)

- [AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents](https://yuxiangchai.github.io/AMEX/)
    - Yuxiang Chai, Siyuan Huang, Yazhe Niu, Han Xiao, Liang Liu, Dingyu Zhang, Peng Gao, Shuai Ren, Hongsheng Li
    - 🏛️ Institutions: CUHK, SJTU, Shanghai AI Lab, vivo AI Lab
    - 📅 Date: July 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [AMEX]
    - 📖 TLDR: This paper introduces the **Android Multi-annotation EXpo (AMEX)**, a comprehensive dataset designed for training and evaluating mobile GUI-control agents. AMEX comprises over 104K high-resolution screenshots from 110 popular mobile applications, annotated at multiple levels, including GUI interactive element grounding, functionality descriptions, and complex natural language instructions. The dataset aims to advance research on AI agents capable of completing complex tasks by interacting directly with mobile device GUIs.

- [CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents](https://arxiv.org/abs/2407.01511)
    - Tianqi Xu, Linyao Chen, Dai-Jie Wu, Yanjun Chen, Zecheng Zhang, Xiang Yao, Zhiqiang Xie, Yongchao Chen, Shilong Liu, Bochen Qian, Philip Torr, Bernard Ghanem, Guohao Li
    - 🏛️ Institutions: KAUST, UTokyo, CMU, Stanford, Harvard, Tsinghua University, SUSTech, Oxford
    - 📅 Date: July 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [framework], [evaluation], [CRAB]
    - 📖 TLDR: The authors present *CRAB*, a benchmark framework designed to evaluate Multimodal Language Model agents across multiple environments. It features a graph-based fine-grained evaluation method and supports automatic task generation, addressing limitations in existing benchmarks.

- [E-ANT: A Large-Scale Dataset for Efficient Automatic GUI NavigaTion](https://arxiv.org/abs/2406.14250)
    - Ke Wang, Tianyu Xia, Zhangxuan Gu, Yi Zhao, Shuheng Shen, Changhua Meng, Weiqiang Wang, Ke Xu
    - 🏛️ Institutions: Ant Group, Tsinghua University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [E-ANT]
    - 📖 TLDR: This paper introduces **E-ANT**, the first large-scale Chinese GUI navigation dataset comprising over 40,000 real human interaction traces across more than 5,000 tiny apps. The dataset includes high-quality screenshots with annotations, facilitating the evaluation and development of GUI navigation and decision-making capabilities in multimodal large language models (MLLMs). The authors also assess various MLLMs on E-ANT, providing insights into their performance and potential improvements.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: iMean AI, CMU
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [Mind2Web-Live], [key-node evaluation]
    - 📖 TLDR: This paper presents WebCanvas, an online evaluation framework for web agents designed to address the dynamic nature of web interactions. It introduces a key-node-based evaluation metric to capture critical actions or states necessary for task completion while disregarding noise from insignificant events or changed web elements. The framework includes the Mind2Web-Live dataset, a refined version of the original Mind2Web static dataset, containing 542 tasks with 2,439 intermediate evaluation states. Despite advancements, the best-performing model achieves a task success rate of 23.1%, highlighting substantial room for improvement.

- [Adversarial Attacks on Multimodal Agents](https://chenwu.io/attack-agent/)
    - Chen Henry Wu, Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: CMU
    - 📅 Date: Jun 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [VisualWebArena-Adv]
    - 📖 TLDR: This paper investigates the safety risks posed by multimodal agents built on vision-enabled language models (VLMs). The authors introduce two adversarial attack methods: a captioner attack targeting white-box captioners and a CLIP attack that transfers to proprietary VLMs. To evaluate these attacks, they curated VisualWebArena-Adv, a set of adversarial tasks based on VisualWebArena. The study demonstrates that within a limited perturbation norm, the captioner attack can achieve a 75% success rate in making a captioner-augmented GPT-4V agent execute adversarial goals. The paper also discusses the robustness of agents based on other VLMs and provides insights into factors contributing to attack success and potential defenses. [oai_citation_attribution:0‡ArXiv](https://arxiv.org/abs/2406.12814?utm_source=chatgpt.com)

- [GUI-WORLD: A Dataset for GUI-oriented Multimodal LLM-based Agents](https://arxiv.org/abs/2406.10819)
    - Dongping Chen, Yue Huang, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan, Pan Zhou, Jianfeng Gao, Lichao Sun
    - 🏛️ Institutions: Huazhong University of Science and Technology (HUST), MSR, University of Illinois at Chicago (UIC)
    - 📅 Date: June 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [GUI-World], [GUI-Vid]
    - 📖 TLDR: This paper introduces *GUI-World*, a comprehensive dataset designed to evaluate Multimodal Large Language Models (MLLMs) in dynamic and complex GUI environments. It includes over 12,000 annotated GUI interaction videos covering diverse applications and scenarios. The study highlights the limitations of current MLLMs in handling dynamic and multi-step tasks and presents *GUI-Vid*, a fine-tuned VideoLLM, demonstrating improved understanding of various GUI tasks.

- [MobileAgentBench: An Efficient and User-Friendly Benchmark for Mobile LLM Agents](https://mobileagentbench.github.io/)
    - Luyuan Wang, Yongyu Deng, Yiwei Zha, Guodong Mao, Qinmin Wang, Tianchen Min, Wei Chen, Shoufa Chen
    - 🏛️ Institutions: CMU, University of Michigan, Northeastern University, HKU
    - 📅 Date: June 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [MobileAgentBench]
    - 📖 TLDR: This paper introduces *MobileAgentBench*, a benchmark designed to evaluate the performance of large language model-based mobile agents. It defines 100 tasks across 10 open-source apps, categorized by difficulty levels, and assesses existing agents like AppAgent and MobileAgent to facilitate systematic comparisons.

- [WebSuite: Systematically Evaluating Why Web Agents Fail](https://arxiv.org/abs/2406.01623)
    - Eric Li, Jim Waldo
    - 🏛️ Institutions: Harvard
    - 📅 Date: June 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [failure analysis], [analysis], [task disaggregation]
    - 📖 TLDR: This paper introduces *WebSuite*, a diagnostic benchmark to investigate the causes of web agent failures. By categorizing agent tasks using a taxonomy of operational, informational, and navigational actions, WebSuite offers granular insights into the specific actions where agents struggle, like filtering or form completion. It enables detailed comparison across agents, identifying areas for architectural and UX adaptation to improve agent reliability and task success on the web.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://arxiv.org/abs/2406.10227)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen WU, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: NUS, Microsoft Gen AI
    - 📅 Date: June 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [Desktop, Web]
    - 🔑 Key: [benchmark], [instructional videos], [visual planning], [hierarchical task decomposition], [complex software interaction]
    - 📖 TLDR: VideoGUI presents a benchmark for evaluating GUI automation on tasks derived from instructional videos, focusing on visually intensive applications like Adobe Photoshop and video editing software. The benchmark includes 178 tasks, with a hierarchical evaluation method distinguishing high-level planning, mid-level procedural steps, and precise action execution. VideoGUI reveals current model limitations in complex visual tasks, marking a significant step toward improved visual planning in GUI automation.

- [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)
    - Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Toyama, Robert Berry, Divya Tyamagundlu, Timothy Lillicrap, Oriana Riva
    - 🏛️ Institutions: Google DeepMind, Google
    - 📅 Date: May 23, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [Android-based agents], [task diversity], [reinforcement learning], [dynamic environment]
    - 📖 TLDR: AndroidWorld introduces a dynamic Android environment for benchmarking autonomous agents across 116 tasks spanning 20 Android apps. These tasks vary through parameterized and natural language prompts, fostering a realistic testing ground for agents designed to operate in complex mobile environments. The benchmark supports millions of task variations, allowing agents to respond to the Android system's changing states and improving real-world applicability.

- [MMInA: Benchmarking Multihop Multimodal Internet Agents](https://arxiv.org/abs/2404.09992)
    - Ziniu Zhang, Shulin Tian, Liangyu Chen, Ziwei Liu
    - 🏛️ Institutions: NTU
    - 📅 Date: April 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [multihop web browsing], [multimodal tasks], [long-range reasoning]
    - 📖 TLDR: The **MMInA** benchmark is designed to evaluate agents' capacity to complete complex, multihop web tasks by navigating and extracting information across evolving real-world websites. Composed of 1,050 tasks across diverse domains, MMInA challenges agents with realistic, multimodal information retrieval and reasoning tasks, such as comparative shopping and travel inquiries. Despite recent advances, agents show difficulties in handling tasks requiring sequential steps across multiple sites, underscoring the need for enhanced multimodal and memory-augmented models.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Automation Task Evaluation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: BUPT, Tsinghua University
    - 📅 Date: April 12, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [UI automation], [mobile agent evaluation]
    - 📖 TLDR: LlamaTouch is an evaluation testbed designed for mobile UI automation, enabling reliable task assessment across 495 annotated tasks. It provides a scalable solution to evaluate agents in real-world mobile settings, comparing agent actions to essential UI states for accurate task completion. LlamaTouch supports dynamic environments, advancing mobile agent reliability and scalability in task automation.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: HKU, CMU, Salesforce, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [real computer tasks], [online environment], [online benchmark]
    - 📖 TLDR: OSWorld introduces a groundbreaking benchmark for multimodal agents to perform open-ended tasks within real computer environments across platforms like Ubuntu, Windows, and macOS. It includes 369 real-world tasks involving web and desktop apps, file management, and multi-app workflows, with custom evaluation scripts for reproducibility. The results reveal current agents’ limitations in GUI interaction and operational knowledge, as they achieve just 12.24% task success compared to humans' 72.36%, highlighting critical gaps for future model improvement.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - 🏛️ Institutions: CMU
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web page understanding], [grounding]
    - 📖 TLDR: VisualWebBench introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on web-based tasks. It includes 1.5K human-curated instances across 139 websites in 87 sub-domains. The benchmark spans seven tasks—such as OCR, grounding, and web-based QA—aiming to test MLLMs' capabilities in fine-grained web page understanding. Results reveal significant performance gaps, particularly in grounding tasks, highlighting the need for advancement in MLLM web understanding.

- [Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)
    - Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
    - 🏛️ Institutions: UCB, UMich
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [evaluation model], [domain transfer]
    - 📖 TLDR: This paper presents an autonomous evaluation framework for digital agents to enhance performance on web navigation and device control. The study introduces modular, cost-effective evaluators achieving up to 92.9% accuracy in benchmarks like WebArena and outlines their use in fine-tuning agents, improving state-of-the-art by 29% without additional supervision.

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://machinelearning.apple.com/research/ferretui-mobile)
    - Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeffrey Nichols, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: April 8, 2024
    - 📑 Publisher: ECCV 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [mobile UI understanding]
    - 📖 TLDR: This paper presents **Ferret-UI**, a multimodal large language model (MLLM) designed to understand and interact with mobile user interfaces. The model incorporates advanced capabilities for referring, grounding, and reasoning about UI elements. By training on a variety of UI tasks, Ferret-UI achieves high performance in tasks such as icon recognition and text extraction. The authors introduce a unique architecture that allows for improved visual feature extraction from mobile screens, paving the way for applications in accessibility and user interaction.

- [Enhancing Mobile "How-to" Queries with Automated Search Results Verification and Reranking](https://arxiv.org/abs/2404.08860)
    - Lei Ding, Jeshwanth Bheemanpally, Yi Zhang
    - 🏛️ Institutions: UCSC
    - 📅 Date: April 2024
    - 📑 Publisher: SIGIR 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [reranking], [verification], [mobile task automation]
    - 📖 TLDR: This paper presents a system that enhances mobile "how-to" queries by verifying and reranking search results through automated instruction extraction, on-device action execution, and reranking based on relevance. The method improves on traditional ranking by analyzing device-specific execution success. The approach comprises a three-stage pipeline: 1) extracting step-by-step instructions from top search results, 2) validating these instructions on mobile devices, and 3) reranking based on performance. The system leverages a pre-trained GPT model for initial processing, ensuring adaptability across diverse apps and systems.

- [Benchmarking Mobile Device Control Agents across Diverse Configurations](https://arxiv.org/abs/2404.16660)
    - Juyong Lee, Taywon Min, Minyong An, Dongyoon Hahm, Haeone Lee, Changyeon Kim, Kimin Lee
    - 🏛️ Institutions: KAIST, Seoul National University, Yonsei University
    - 📅 Date: April 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile device control], [agent performance]
    - 📖 TLDR: This paper presents **B-MoCA**, a comprehensive benchmark for evaluating mobile device control agents using an Android-based testbed with 131 tasks and various device configurations. The benchmark assesses agents' abilities across tasks that include device-specific variations, navigation, and human-like dual-gesture interactions. B-MoCA highlights that current agents perform well on basic tasks but struggle with complex configurations, pointing to opportunities for future improvements in mobile automation capabilities.

- [AgentStudio: A Toolkit for Building General Virtual Agents](https://arxiv.org/abs/2403.17918)
    - Longtao Zheng, Zhiyuan Huang, Zhenghai Xue, Xinrun Wang, Bo An, Shuicheng Yan
    - 🏛️ Institutions: NTU, Skywork AI, ETH Zurich
    - 📅 Date: March 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [general virtual agents], [open-ended learning], [tool creation], [GroundUI], [benchmark]
    - 📖 TLDR: AgentStudio is a robust toolkit for developing virtual agents with versatile actions, such as GUI automation and code execution. It unifies real-world human-computer interactions across OS platforms and includes diverse observation and action spaces, facilitating comprehensive training and benchmarking in complex settings. The toolkit's flexibility promotes agent generalization across varied tasks, supporting tool creation and a multimodal interaction interface to advance agent adaptability and learning.

- [Tur[k]ingBench: A Challenge Benchmark for Web Agents](https://arxiv.org/abs/2403.11905)
    - Kevin Xu, Yeganeh Kordi, Kate Sanders, Yizhong Wang, Adam Byerly, Jingyu Zhang, Benjamin Van Durme, Daniel Khashabi
    - 🏛️ Institutions: JHU, Brown, UW
    - 📅 Date: March 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [multi-modal reasoning], [TurkingBench], [Turking]
    - 📖 TLDR: This paper introduces **Tur[k]ingBench**, a benchmark comprising 158 web-grounded tasks designed to evaluate AI agents' capabilities in complex web-based environments. Unlike prior benchmarks that utilize synthetic web pages, Tur[k]ingBench leverages natural HTML pages from crowdsourcing platforms, presenting tasks with rich multi-modal contexts. The benchmark includes 32.2K instances, each with diverse inputs, challenging models to interpret and interact with web pages effectively. Evaluations of state-of-the-art models reveal significant room for improvement, highlighting the need for advanced web-based agents capable of handling real-world web interactions. 

- [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718)
    - Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montreal, McGill University, University de Montreal
    - 📅 Date: March 11, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [enterprise task automation], [ServiceNow], [knowledge work automation]
    - 📖 TLDR: WorkArena introduces a robust benchmark hosted on the ServiceNow platform to assess the effectiveness of large language model-based agents in performing 33 knowledge tasks common to enterprise environments. Leveraging BrowserGym, an environment that simulates complex browser interactions, WorkArena provides web agents with realistic challenges like data entry, form completion, and information retrieval in knowledge bases. Despite promising initial results, open-source models show a 42.7% success rate compared to closed-source counterparts, underlining the current gap in task automation for enterprise applications and highlighting key areas for improvement.

- [On the Multi-turn Instruction Following for Conversational Web Agents](https://arxiv.org/abs/2402.15057)
    - Yang Deng, Xuan Zhang, Wenxuan Zhang, Yifei Yuan, See-Kiong Ng, Tat-Seng Chua
    - 🏛️ Institutions: NUS, DAMO Academy, University of Copenhagen
    - 📅 Date: February 23, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [multi-turn dialogue], [memory utilization], [self-reflective planning]
    - 📖 TLDR: This paper explores multi-turn conversational web navigation, introducing the MT-Mind2Web dataset to support instruction-following tasks for web agents. The proposed Self-MAP (Self-Reflective Memory-Augmented Planning) framework enhances agent performance by integrating memory with self-reflection for sequential decision-making in complex interactions. Extensive evaluations using MT-Mind2Web demonstrate Self-MAP's efficacy in addressing the limitations of current models in multi-turn interactions, providing a novel dataset and framework for evaluating and training agents on detailed, multi-step web-based tasks.

- [WebLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://arxiv.org/abs/2402.05930)
    - Xing Han Lu, Zdeněk Kasner, Siva Reddy
    - 🏛️ Institutions: Mila, McGill University
    - 📅 Date: February 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [multi-turn dialogue], [real-world navigation], [WebLINX]
    - 📖 TLDR: WebLINX addresses the complexity of real-world website navigation for conversational agents, with a benchmark featuring over 2,300 demonstrations across 150+ websites. The benchmark allows agents to handle multi-turn instructions and interact dynamically across diverse domains, including geographic and thematic categories. The study proposes a retrieval-inspired model that selectively extracts key HTML elements and browser actions, achieving efficient task-specific representations. Experiments reveal that smaller finetuned decoders outperform larger zero-shot multimodal models, though generalization to new environments remains challenging.

- [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553)
    - Raghav Kapoor, Yash Parag Butala, Melisa Russak, Jing Yu Koh, Kiran Kamble, Waseem Alshikh, Ruslan Salakhutdinov
    - 🏛️ Institutions: CMU
    - 📅 Date: February 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [benchmark]
    - 📖 TLDR: OmniACT introduces a dataset and benchmark to train and evaluate multimodal agents capable of autonomously performing diverse tasks across desktop and web environments. Using annotated UI elements across applications, it combines visual grounding with natural language instructions, providing 9,802 data points for developing agents that integrate high-level reasoning with UI interactions. The study highlights the limited proficiency of current models, with baselines like GPT-4 only achieving 15% of human performance on executable scripts, emphasizing OmniACT's potential as a testbed for advancing multimodal AI.

- [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158)
    - Junyang Wang, Haiyang Xu, Jiabo Ye, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Beijing Jiaotong University, Alibaba
    - 📅 Date: January 29, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark]
    - 📖 TLDR: This paper presents Mobile-Agent, an autonomous multi-modal agent designed for mobile device interaction. The system integrates visual perception, natural language processing, and action prediction to navigate and operate mobile applications. The authors introduce a new dataset and benchmark for evaluating mobile agents, demonstrating Mobile-Agent's superior performance in task completion and generalization across various apps compared to existing methods.

- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab, Westlake University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: This paper introduces WebVoyager, an innovative web agent powered by Large Multimodal Models (LMMs) that can complete user instructions end-to-end by interacting with real-world websites. The authors establish a new benchmark with tasks from 15 popular websites and propose an automatic evaluation protocol using GPT-4V. WebVoyager achieves a 59.1% task success rate, significantly outperforming GPT-4 (All Tools) and text-only setups. The study demonstrates the effectiveness of multimodal approaches in web automation and provides insights into developing more intelligent web interaction solutions.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: CMU
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [dataset], [multimodal agent evaluation], [visually grounded tasks]
    - 📖 TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Yantao Li, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: Nanjing University, Shanghai AI Lab
    - 📅 Date: January 19, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [benchmark], [GUI grounding], [visual grounding]
    - 📖 TLDR: TBD.

- [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://huggingface.co/papers/2305.11854)
    - Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu, Izzeddin Gur
    - 🏛️ Institutions: Univ. of Tokyo, Google DeepMind
    - 📅 Date: Jan 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [model], [dataset], [web navigation], [instruction-following], [WebShop]
    - 📖 TLDR: This paper introduces WebGUM, an instruction-following multimodal agent for autonomous web navigation that leverages both visual (webpage screenshots) and textual (HTML) inputs to perform actions such as click and type. The model is trained on a vast corpus of demonstrations and shows improved capabilities in visual perception, HTML comprehension, and multi-step decision-making, achieving state-of-the-art performance on benchmarks like MiniWoB and WebShop. WebGUM provides a scalable approach to web-based tasks without task-specific architectures, enabling high-performance web navigation with generalizable, multimodal foundation models.

- [AgentBench: Evaluating LLMs as Agents](https://llmbench.ai/agent)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU, ByteDance
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI], [General]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://osu-nlp-group.github.io/SeeAct/)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [grounding], [SeeAct], [Multimodal-Mind2web]
    - 📖 TLDR: This paper explores the capability of GPT-4V(ision), a multimodal model, as a web agent that can perform tasks across various websites by following natural language instructions. It introduces the **SEEACT** framework, enabling GPT-4V to navigate, interpret, and interact with elements on websites. Evaluated using the **Mind2Web** benchmark and an online test environment, the framework demonstrates high performance on complex web tasks by integrating grounding strategies like element attributes and image annotations to improve HTML element targeting. However, grounding remains challenging, presenting opportunities for further improvement.

- [AssistGUI: Task-Oriented Desktop Graphical User Interface Automation](https://arxiv.org/abs/2312.13108)
    - Difei Gao, Lei Ji, Zechen Bai, Mingyu Ouyang, Peiran Li, Dongxing Mao, Qinchen Wu, Weichen Zhang, Peiyi Wang, Xiangwu Guo, Hengxu Wang, Luowei Zhou, Mike Zheng Shou
    - 🏛️ Institutions: NUS
    - 📅 Date: December 20, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [desktop productivity tasks]
    - 📖 TLDR: This study presents *AssistGUI*, a benchmark and framework for desktop GUI automation, featuring an LLM-based agent capable of completing complex user requests by analyzing instructional videos and performing actions on the desktop. Utilizing a novel Actor-Critic framework and GUI parser, *AssistGUI* was tested on 100 tasks across nine applications, such as MS Word and After Effects. Despite advances, the top-performing model achieved only a 46% success rate, illustrating the challenge of comprehensive desktop automation and underscoring areas for future research in agent-driven GUI tasks.

- [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914)
    - Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhao Chen, Yuxuan Wang, Yining Ye, Jiayi Zhang, Hao Dong, Wenhu Chen, Yizhou Wang, Kai-Wei Chang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI
    - 📅 Date: December 15, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [visual language model], [GUI agent]
    - 📖 TLDR: This paper presents CogAgent, a visual language model designed for GUI agents. The authors introduce a new dataset, CogBench, featuring 1,430 GUI tasks across various applications. CogAgent employs a novel training approach combining supervised fine-tuning and decision-making fine-tuning. The model demonstrates superior performance on CogBench and generalizes well to unseen applications, outperforming existing models like GPT-4V in GUI task completion.

- [GAIA: a benchmark for General AI Assistants](https://huggingface.co/gaia-benchmark)
    - Grégoire Mialon, Yassine Nakkach, Aslan Tchamkerten, Albert Thomas, Laurent Dinh, and a research team from Meta AI and Hugging Face.
    - 🏛️ Institutions: Meta AI, Hugging Face
    - 📅 Date: November 21, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [benchmark], [multi-modality], [tool use], [reasoning]
    - 📖 TLDR: GAIA is a benchmark developed for evaluating general-purpose AI assistants. It aims to test assistant models across multiple modalities and complex reasoning tasks in real-world settings, including scenarios that require tool usage and open-ended question answering. With a dataset comprising 466 questions across various domains, GAIA highlights gaps between current AI performance and human capability, presenting a significant challenge for large language models such as GPT-4.

- [GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](https://arxiv.org/abs/2311.07562)
    - An Yan, Zhengyuan Yang, Wanrong Zhu, Kevin Lin, Linjie Li, Jianfeng Wang, Jianwei Yang, Yiwu Zhong, Julian McAuley, Jianfeng Gao, Zicheng Liu, Lijuan Wang
    - 🏛️ Institutions: UCSD, Microsoft, UCSB, UWM
    - 📅 Date: November 13, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [zero-shot GUI navigation], [multimodal LLMs]
    - 📖 TLDR: This paper explores the capabilities of GPT-4V in navigating smartphone GUIs without prior training. The authors introduce a novel framework for GUI navigation and a new benchmark, MobileNav, featuring 1,000 navigation tasks across 100 mobile apps. The study demonstrates GPT-4V's impressive zero-shot performance in understanding and interacting with mobile interfaces, outperforming previous methods and even approaching human-level performance on some tasks.

- [Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V](https://arxiv.org/abs/2310.11441)
    - Jianwei Yang, Hao Zhang, Feng Li, Xueyan Zou, Chunyuan Li, Jianfeng Gao
    - 🏛️ Institutions: MSR
    - 📅 Date: October 17, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [visual prompting], [framework], [benchmark], [visual grounding], [zero-shot]
    - 📖 TLDR: This paper introduces Set-of-Mark (SoM), a novel visual prompting approach designed to enhance the visual grounding capabilities of multimodal models like GPT-4V. By overlaying images with spatially and semantically distinct marks, SoM enables fine-grained object recognition and interaction within visual data, surpassing conventional zero-shot segmentation methods in accuracy. The framework is validated on tasks requiring detailed spatial reasoning, demonstrating a significant improvement over existing visual-language models without fine-tuning.

- [You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/abs/2309.11436)
    - Zhuosheng Zhang, Aston Zhang
    - 🏛️ Institutions: SJTU
    - 📅 Date: September 20, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [multimodal agent], [chain-of-action technique]
    - 📖 TLDR: This paper presents Auto-GUI, a multimodal agent capable of directly interacting with graphical user interfaces without relying on environment parsing or application-specific APIs. The authors introduce a novel chain-of-action technique that leverages previous action histories and future action plans to improve decision-making. Auto-GUI is evaluated on a new device-control benchmark, AITW, demonstrating state-of-the-art performance in action prediction and task completion across various applications and web-based tasks.

- [AutoDroid: LLM-powered Task Automation in Android](https://arxiv.org/abs/2308.15272)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - 🏛️ Institutions: Tsinghua University, Shanghai AI Lab, University of Notre Dame, MSR
    - 📅 Date: August 29, 2023
    - 📑 Publisher: MobiCom 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [Android task automation], [LLM-powered agent]
    - 📖 TLDR: This paper introduces AutoDroid, a novel mobile task automation system capable of handling arbitrary tasks on any Android application without manual efforts. The framework combines the commonsense knowledge of LLMs with domain-specific knowledge of apps through automated dynamic analysis. AutoDroid features a functionality-aware UI representation method, exploration-based memory injection techniques, and a multi-granularity query optimization module. Evaluated on a new benchmark with 158 common tasks, AutoDroid achieves a 90.9% action generation accuracy and a 71.3% task completion rate, significantly outperforming GPT-4-powered baselines.

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
    - 🏛️ Institutions: CMU
    - 📅 Date: July 26, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [multi-tab navigation], [web-based interaction], [agent simulation]
    - 📖 TLDR: *WebArena* provides a standalone, realistic web simulation environment where autonomous agents can perform complex web-based tasks. The platform offers functionalities such as multi-tab browsing, element interaction, and customized user profiles. Its benchmark suite contains 812 tasks grounded in high-level natural language commands. WebArena uses multi-modal observations, including HTML and accessibility tree views, supporting advanced tasks that require contextual understanding across diverse web pages, making it suitable for evaluating generalist agents in real-world web environments.

- [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088)
    - Christopher Rawles, Alice Li, Daniel Rodriguez, Oriana Riva, Timothy Lillicrap
    - 🏛️ Institutions: Google Research, Google DeepMind
    - 📅 Date: July 19, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [device control], [natural language interaction], [gesture-based actions]
    - 📖 TLDR: The *Android in the Wild (AitW)* dataset introduces a significant benchmark for Android device control, encompassing over 715,000 human-labeled episodes with natural language commands and corresponding UI actions. Collected from Android devices across versions 10-13, it captures complex multi-step tasks requiring both visual and contextual understanding. The dataset is structured to test the robustness of device-control systems under varying conditions, such as new tasks or applications, and includes data to evaluate gesture-based interactions, providing a unique foundation for mobile interface automation and task execution research.

- [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863)
    - Longtao Zheng, Rundong Wang, Xinrun Wang, Bo An
    - 🏛️ Institutions: NTU
    - 📅 Date: June 13, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [trajectory prompting], [state abstraction], [memory retrieval]
    - 📖 TLDR: Synapse introduces a novel framework for computer control tasks, leveraging trajectory-as-exemplar prompting and memory to enhance LLM performance in complex, multi-step computer tasks. The system combines state abstraction, trajectory-based prompts, and memory retrieval, overcoming LLM limitations by filtering task-irrelevant data, storing exemplar trajectories, and retrieving relevant instances for improved decision-making. Synapse achieves significant performance gains on benchmarks such as MiniWoB++ and Mind2Web, demonstrating enhanced task success rates and generalization across diverse web-based tasks.

- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: June 9, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [model], [Mind2Web], [MindAct]
    - 📖 TLDR: *Mind2Web* presents a dataset and benchmark specifically crafted for generalist web agents capable of performing language-guided tasks across varied websites. Featuring over 2,000 tasks from 137 sites, it spans 31 domains and emphasizes open-ended, realistic tasks in authentic, unsimplified web settings. The study proposes the *MindAct* framework, which optimizes LLMs for handling complex HTML elements by using small LMs to rank elements before full processing, thereby enhancing the efficiency and versatility of web agents in diverse contexts.

- [Mobile-Env: Building Qualified Evaluation Benchmarks for LLM-GUI Interaction](https://arxiv.org/abs/2305.08144)
    - Danyang Zhang, Zhennan Shen, Rui Xie, Situo Zhang, Tianbao Xie, Zihan Zhao, Siyuan Chen, Lu Chen, Hongshen Xu, Ruisheng Cao, Kai Yu
    - 🏛️ Institutions: SJTU, HKU
    - 📅 Date: May 14, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [interaction platform], [multistep interaction], [InfoUI]
    - 📖 TLDR: This paper introduces *Mobile-Env*, a novel interaction platform and benchmark aimed at assessing large language models' (LLMs) capabilities in interactive environments. It builds on the InfoUI task set, derived from WikiHow, to create structured text-based challenges that simulate real-world mobile interactions. The platform is designed to support task expansions from the community, aiming to drive advancements in LLM-based interactive agents.

- [Language Models can Solve Computer Tasks](https://arxiv.org/abs/2303.17491)
    - Geunwoo Kim, Pierre Baldi, Stephen McAleer
    - 🏛️ Institutions: UCI
    - 📅 Date: March 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [Recursive Critique and Improve], [RCI], [MiniWoB++], [general computer tasks]
    - 📖 TLDR: This study demonstrates that large language models (LLMs) can effectively automate computer tasks using a Recursive Critique and Improve (RCI) prompting method, enabling agents to handle complex desktop tasks like email and file management. By combining RCI with existing Chain of Thought (CoT) prompting, the method outperforms prior LLM approaches and traditional supervised and reinforcement learning models on the **MiniWoB++** benchmark, showing potential for broad computer task automation.

- [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)
    - Shunyu Yao, Howard Chen, John Yang, Karthik Narasimhan
    - 🏛️ Institutions: Princeton
    - 📅 Date: July 2022
    - 📑 Publisher: NeurIPS 2022
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [e-commerce web interaction], [language grounding]
    - 📖 TLDR: This paper introduces **WebShop**, a simulated web-based shopping environment with over 1 million real-world products and 12,087 annotated instructions. It allows language agents to navigate, search, and make purchases based on natural language commands. The study explores how agents handle compositional instructions and noisy web data, providing a robust environment for reinforcement learning and imitation learning. The best models show effective sim-to-real transfer on websites like Amazon, illustrating WebShop’s potential for training grounded agents.

- [META-GUI: Towards Multi-modal Conversational Agents on Mobile GUI](https://arxiv.org/abs/2205.11029)
    - Liangtai Sun, Xingyu Chen, Lu Chen, Tianle Dai, Zichen Zhu, Kai Yu
    - 🏛️ Institutions: SJTU
    - 📅 Date: May 23, 2022
    - 📑 Publisher: EMNLP 2022
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [task-oriented dialogue], [GUI-based interaction], [multi-modal agent]
    - 📖 TLDR: This paper presents META-GUI, a dataset and framework for training multi-modal conversational agents capable of interacting directly with mobile app interfaces without the need for backend APIs. META-GUI includes over 1,100 dialogues with annotated action sequences on various tasks such as booking and scheduling. The authors propose a GUI-based task-oriented dialogue system that allows agents to navigate mobile interfaces via direct GUI actions, with performance shown to improve in multi-modal task-oriented dialogue contexts.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://arxiv.org/abs/2103.16057)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - 🏛️ Institutions: Stanford
    - 📅 Date: March 30, 2021
    - 📑 Publisher: NAACL 2021
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [grounding], [task automation], [open-domain instructions], [RUSS]
    - 📖 TLDR: This paper introduces RUSS (Rapid Universal Support Service), a framework designed to interpret and execute open-domain, step-by-step web instructions automatically. RUSS uses a BERT-LSTM model for semantic parsing into a custom language, ThingTalk, which allows the system to map language to actions across various web elements. The framework, including a dataset of instructions, facilitates agent-based web support task automation by grounding natural language to interactive commands.

- [Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements](https://arxiv.org/abs/2010.04295)
    - Yang Li, Gang Li, Luheng He, Jingjie Zheng, Hong Li, Zhiwei Guan
    - 🏛️ Institutions: Google Research
    - 📅 Date: November 2020
    - 📑 Publisher: EMNLP 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [model], [accessibility], [natural language generation], [WidgetCaption]
    - 📖 TLDR: This paper introduces the task of *widget captioning*, which aims to automatically generate natural language descriptions for UI elements in mobile apps to enhance accessibility. Using both visual and structural data from UI components, the study presents a novel dataset of 162,859 captions across 61,285 UI elements. Multiple deep learning models were tested on this dataset, with findings suggesting the potential for improving screen reader usability for visually impaired users by generating descriptive captions of UI elements.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Stanford
    - 📅 Date: February 24, 2018
    - 📑 Publisher: ICLR 2018
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [web tasks], [workflow-guided exploration]
    - 📖 TLDR: This paper presents a novel RL approach using *workflow-guided exploration* to efficiently train agents on web-based tasks, where actions are restricted based on demonstrated workflows to streamline learning. Evaluated on MiniWoB and MiniWoB++ benchmarks, the method significantly outperforms traditional RL techniques in sparse reward settings by structuring exploration according to high-level action constraints.

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, and Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025 (submitted to arXiv on May 24, 2025) :contentReference[oaicite:0]{index=0}
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [model context protocol], [MCP], [OSWorld], [LiteCUA]
    - 📖 TLDR: Introduces AIOS 1.0, which contextualizes desktop computer states via an MCP server so LLM-powered agents can better understand and operate GUIs. Built on top, LiteCUA—a lightweight agent—achieves 14.66 % success on the OSWorld benchmark, outperforming several heavier agent frameworks, showing the benefits of environment contextualization.
