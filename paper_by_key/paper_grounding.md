# Papers with Keyword: grounding

- [Rethinking Token Pruning for Historical Screenshots in GUI Visual Agents: Semantic, Spatial, and Temporal Perspectives](https://arxiv.org/abs/2603.26041)
    - Daiqiang Li, Zihao Pan, Zeyu Zhang, Ronghao Chen, Huacan Wang, Honggang Chen, Haiyun Jiang
    - 🏛️ Institutions: Sichuan University, Sun Yat-sen University, Australian National University, Peking University, University of Chinese Academy of Sciences, Shanghai Jiao Tong University
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [token pruning], [efficiency], [MLLM], [visual grounding], [empirical study]
    - 📖 TLDR: This paper conducts an empirical study on token pruning for historical screenshots in GUI visual agents, revealing three key insights: background regions capture valuable interface-state transitions, random pruning better preserves spatial structure than designed strategies, and a temporal recency effect allows heavy compression of distant screenshots with minimal performance loss.

- [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](https://arxiv.org/abs/2603.26211)
    - Shrinidhi Kumbhar, Haofu Liao, Srikar Appalaraju, Kunwar Yashraj Singh
    - 🏛️ Institutions: Arizona State University, Amazon (AWS Agentic AI)
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [diffusion model], [vision-language model], [hybrid masking], [bounding box prediction], [cross-platform]
    - 📖 TLDR: This paper adapts discrete diffusion vision-language models (LLaDA-V) for GUI grounding, proposing a hybrid masking schedule that combines linear and deterministic masking to improve bounding-box prediction accuracy across web, desktop, and mobile interfaces, demonstrating that diffusion-based models are a competitive alternative to autoregressive VLMs for GUI agent tasks.

- [AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement](https://arxiv.org/abs/2603.17441)
    - Siqi Pei, Liang Tang, Tiaonan Duan, Long Chen, Shuxian Li, Kaer Huang, Yanzhe Jing, Yiqiang Yan, Bo Zhang, Chenghao Jiang, Borui Zhang, Jiwen Lu
    - 🏛️ Institutions: Lenovo Research, Tsinghua University
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [GUI grounding], [instruction refinement], [adaptive zoom], [AdaZoom-GUI]
    - 📖 TLDR: This paper proposes AdaZoom-GUI, a GUI grounding framework that improves both instruction understanding and fine-grained localization on high-resolution interface screenshots. It combines an instruction refinement module with a conditional second-stage zoom-in strategy, and trains the grounding model with GRPO on a newly constructed GUI grounding dataset. The method reports state-of-the-art results among comparable model sizes and is positioned as a practical improvement for robust GUI agent deployment.

- [FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair](https://arxiv.org/abs/2603.17826)
    - Weifeng He, Zhiyi Hu, Yiming Li, Jiguang Ren, Yuexing Li
    - 🏛️ Institutions: Nanjing University, SenseTime, The Chinese University of Hong Kong, University of Texas at Dallas
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multimodal], [software engineering], [program repair], [memory-augmented], [visual grounding], [benchmark]
    - 📖 TLDR: FailureMem is a multimodal automated program repair framework that combines a hybrid workflow-agent architecture, active perception tools for region-level visual grounding of GUI screenshots, and a Failure Memory Bank that converts past failed repair attempts into reusable guidance, achieving a 3.7% improvement over GUIRepair on SWE-bench Multimodal.

- [GUI-CEval: A Hierarchical and Comprehensive Chinese Benchmark for Mobile GUI Agents](https://arxiv.org/abs/2603.15039)
    - Haotian Zhao, Yuzhe Qin, Dongliang Li, Dongdong Hu, Xingshuai Zhang
    - 🏛️ Institutions: Xiaomi
    - 📅 Date: March 16, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile], [chinese], [evaluation], [GUI grounding], [agent]
    - 📖 TLDR: GUI-CEval is the first comprehensive Chinese benchmark for mobile GUI agents, spanning 201 apps across four device types with a hierarchical two-level evaluation structure (atomic abilities and application-level tasks) along five dimensions (perception, planning, reflection, execution, evaluation), revealing that most MLLMs still struggle with reflective decision-making and post-action self-evaluation.

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Mauro Li, Reuben Binns, Soheil Feizi, Lind Seelig, Kasper Luckow
    - 🏛️ Institutions: vLLM Semantic Router Project, MBZUAI, McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [safety], [computer-use agent], [visual grounding], [guardrail], [adversarial attacks]
    - 📖 TLDR: Formalizes the "visual confused deputy" as a security vulnerability in computer-using agents where misperceived screen states (from grounding errors, adversarial screenshot manipulation, or TOCTOU races) cause agents to authorize unintended privileged actions, and proposes a dual-channel contrastive classification guardrail that independently verifies the visual click target and the agent's textual reasoning to block risky executions.

- [Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements](https://arxiv.org/abs/2603.14448)
    - Jingfeng Yang, Yu Tan, Haofeng Gao, Xiaozhi Gao, Jianguo Li
    - 🏛️ Institutions: Sichuan University, Tsinghua University, Nanjing University, Nanyang Technological University
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [inference scaling], [training-free], [MLLM], [visual grounding], [image pyramid]
    - 📖 TLDR: ZoomUI is a training-free GUI grounding method that leverages inference scaling to guide general MLLMs in progressively anchoring instruction elements to increasingly detailed interface elements, using latent thinking for visual feature description and internal attention for iteratively zooming into target element regions, achieving SOTA performance without fine-tuning.

- [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](https://arxiv.org/abs/2603.14248)
    - Mohamed Aghzal, Gregory J. Stein, Ziyu Yao
    - 🏛️ Institutions: George Mason University
    - 📅 Date: 2026-03-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [failure analysis], [hierarchical planning], [PDDL], [grounding]
    - 📖 TLDR: This paper proposes a hierarchical planning framework that analyzes LLM-based web agent failures across three layers (high-level planning, low-level execution, and replanning), finding that while structured PDDL plans outperform natural language plans for high-level strategy, low-level execution and perceptual grounding remain the dominant bottleneck for achieving human-level reliability.

- [MM-CondChain: A Programmatically Verified Benchmark for Visually Grounded Deep Compositional Reasoning](https://arxiv.org/abs/2603.12266)
    - Zhouheng Sun, Yingyao Zhou, Yang Liu, Junlu Tang, Jian Xie
    - 🏛️ Institutions: Alibaba Group, Zhejiang University
    - 📅 Date: March 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [multimodal LLM], [compositional reasoning], [visual grounding], [GUI], [evaluation]
    - 📖 TLDR: MM-CondChain is a benchmark for evaluating visually grounded deep compositional reasoning in multimodal LLMs, featuring multi-layer conditional chains across natural images, charts, and GUI trajectories, where even the best model achieves only 53.33 Path F1, revealing that deeply chained compositional reasoning remains a fundamental challenge.

- [WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces](https://arxiv.org/abs/2603.05295)
    - Xiao Liu, Ziyang Luo, Jiawei Liu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Fudan University, IMean AI
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [dataset], [benchmark], [grounding], [training data], [multimodal]
    - 📖 TLDR: WebChain is the largest open-source dataset of 31,725 human-annotated web interaction trajectories (318k steps) on real-world websites, featuring triple-aligned visual, structural, and action data. Leveraging this dataset, the authors propose a Dual Mid-Training recipe that decouples spatial grounding from planning, achieving state-of-the-art performance on their WebChainBench and other public GUI benchmarks.

- [How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors](https://arxiv.org/abs/2601.21961)
    - Kuai Yu, Naicheng Yu, Han Wang, Rui Yang, Huan Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, Columbia University, University of California San Diego
    - 📅 Date: 2026-02-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [evaluation], [GUI understanding], [visual grounding], [robustness]
    - 📖 TLDR: Introduces VAF, a controlled evaluation pipeline that systematically measures how webpage visual attribute factors (e.g., background color contrast, item size, position, card clarity) influence web agent decision-making across 48 variants, 5 real-world websites, and 4 representative agents.

- [Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision](https://arxiv.org/abs/2602.14276)
    - A. Said Gurbuz, Sunghwan Hong, Ahmed Nassar, Marc Pollefeys, Peter Staar
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-02-15
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [dataset], [screen parsing], [computer-use agent], [UI understanding]
    - 📖 TLDR: ScreenParse is a large-scale dataset providing dense annotations of all visible UI elements (bounding boxes, 55-class types, and text) across 771K web screenshots (21M elements), generated by an automated pipeline to enable complete screen parsing supervision beyond sparse grounding.

- [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430)
    - Renjun Xu, Yang Yan
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [LLM agent], [agent skills], [CUA], [GUI grounding], [benchmark]
    - 📖 TLDR: A comprehensive survey of the agent skills landscape for LLMs, organized along four axes: architectural foundations (SKILL.md, MCP), skill acquisition (RL, autonomous discovery), deployment at scale (CUA stack, GUI grounding, OSWorld/SWE-bench), and security (skill trust governance framework).

- [WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements](https://arxiv.org/abs/2602.11724)
    - Xiwen Teoh, Yun Lin, Duc-Minh Nguyen, Lei Xu, David S. Rosenbluth
    - 🏛️ Institutions: National University of Singapore, Shanghai Jiao Tong University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web testing], [LLM agent], [bug detection], [GUI grounding], [test oracle], [software engineering]
    - 📖 TLDR: WebTestPilot is an LLM-based agent for end-to-end web testing that symbolizes GUI elements and infers pre/post-conditions from natural language specifications as test oracles, achieving 96% precision and 96% recall in bug detection on a benchmark of bug-injected web apps, significantly outperforming existing baselines.

- [UI-Venus-1.5 Technical Report](https://arxiv.org/abs/2602.09082)
    - Venus Team, Changlong Gao, Zhangxuan Gu, Yingying Zhou, Yang Liu
    - 🏛️ Institutions: Ant Group
    - 📅 Date: February 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reinforcement learning], [model merging], [mobile navigation], [web navigation], [grounding]
    - 📖 TLDR: UI-Venus-1.5 is a unified end-to-end GUI agent family (2B/8B/30B-A3B) that combines mid-training on 10B tokens, online reinforcement learning with full-trajectory rollouts, and model merging to achieve state-of-the-art performance on GUI grounding and navigation benchmarks including ScreenSpot-Pro (69.6%), VenusBench-GD (75.0%), and AndroidWorld (77.6%).

- [POINTS-GUI-G: GUI-Grounding Journey](https://arxiv.org/abs/2602.06391)
    - Zhongyin Zhao, Yuan Liu, Yikun Liu, Haicheng Wang, Le Tian, Xiao Zhou, Yangxiu You, Zilin Yu, Yang Yu, Jie Zhou
    - 🏛️ Institutions: WeChat AI
    - 📅 Date: February 6, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [reinforcement learning], [data engineering], [POINTS-GUI-g]
    - 📖 TLDR: This paper studies how to build strong GUI grounding capability starting from a base model without strong pre-existing spatial grounding. It introduces POINTS-GUI-G-8B and attributes its gains to refined multi-source data engineering, improved training strategy for the vision encoder, and reinforcement learning with verifiable rewards. The resulting model achieves state-of-the-art or competitive results across GUI grounding benchmarks including ScreenSpot-Pro, OSWorld-G, ScreenSpot-v2, and UI-Vision.

- [Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion](https://arxiv.org/abs/2602.06351)
    - Longhui Ma, Di Zhao, Siwei Wang, Yingce Xia, Ting Liu
    - 🏛️ Institutions: National University of Defense Technology, Academy of Military Sciences
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [multimodal fusion], [attention mechanism], [training-free], [OCR], [MLLM]
    - 📖 TLDR: Trifuse is a training-free GUI grounding framework that fuses attention maps from MLLMs with OCR-derived textual cues and icon-level caption semantics via a Consensus-SinglePeak fusion strategy, achieving strong performance on four grounding benchmarks without task-specific fine-tuning.

- [Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts](https://arxiv.org/abs/2602.02468)
    - Aiden Yiliu Li, Xinyue Hao, Shilong Liu, Mengdi Wang
    - 🏛️ Institutions: University College London, Princeton University, The University of Edinburgh
    - 📅 Date: 2026-02-02
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [avenir-web], [mixture of grounding experts], [multimodal LLM], [online-Mind2Web]
    - 📖 TLDR: Avenir-Web is a multimodal web agent that combines Mixture of Grounding Experts, Experience-Imitation Planning, and task-tracking checklists with adaptive memory to achieve a new open-source state-of-the-art (53.7% success rate) on the Online-Mind2Web benchmark, reaching performance parity with top proprietary models on live web tasks.

- [Environmental Injection Attacks against GUI Agents in Realistic Dynamic Environments](https://arxiv.org/abs/2509.11250)
    - Yitong Zhang, Ximo Li, Liyi Cai, Jia Li
    - 🏛️ Institutions: Tsinghua University, Peking University
    - 📅 Date: 2026-01-31
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [attack], [web agent], [benchmark], [grounding], [vision]
    - 📖 TLDR: This paper introduces a realistic dynamic-environment threat model for Environmental Injection Attacks (EIAs) against GUI agents and proposes Chameleon, an attack framework using LLM-driven environment simulation and an Attention Black Hole mechanism to expose hidden vulnerabilities of LVLM-powered GUI agents on real-world websites.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548)
    - Xiaoce Wang, Guibin Zhang, Junzhe Li, Fang Li, Chen Zhang
    - 🏛️ Institutions: Tsinghua University, National University of Singapore, Peking University, Shenzhen MSU-BIT University, Guangming Laboratory
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [tool use], [tokenization], [curriculum learning], [visual grounding], [data efficiency]
    - 📖 TLDR: ToolTok introduces a tool tokenization paradigm for GUI agents that models operations as multi-step pathfinding through learnable tool tokens with semantic anchoring and curriculum learning, achieving competitive performance with models 50x larger while using less than 1% of the training data required by other post-training approaches.

- [SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization](https://arxiv.org/abs/2601.22491)
    - Jinyang Wu, Changpeng Yang, Yuhao Shen, Wentao Zhang, Gang Pan
    - 🏛️ Institutions: Tsinghua University, Xiaomi Corporation, Zhejiang University, Nanyang Technological University, Institute of Automation Chinese Academy of Sciences
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reinforcement learning], [reward shaping], [GUI grounding], [planning], [training framework]
    - 📖 TLDR: SSL (Sweet Spot Learning) introduces a tiered reward framework for reinforcement learning that replaces binary rewards with progressively amplified, quality-ordered rewards to guide agent policies toward optimal solution regions. Evaluated across GUI perception, short/long-term planning, and complex reasoning tasks, SSL achieves up to 2.5x sample efficiency gains over binary reward baselines on 12 benchmarks.

- [Continual GUI Agents](https://arxiv.org/abs/2601.20732)
    - Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng
    - 🏛️ Institutions: Tsinghua University, Zhejiang University, ETH Zurich, Beijing University of Posts and Telecommunications
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [GUI grounding], [domain shift], [GUI-AiF], [continual GUI agents]
    - 📖 TLDR: This paper introduces Continual GUI Agents as a continual learning setting where GUI agents must adapt to domain and resolution shifts over time without losing stable grounding. It proposes GUI-AiF, a reinforcement fine-tuning framework with anchoring-point and anchoring-region rewards that keep agents aligned to changing interaction targets instead of overfitting to static cues. Experiments show the method outperforms prior baselines and frames continual adaptation as a core systems challenge for GUI agents.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: University of Science and Technology of China, Institute of Artificial Intelligence (TeleAI) China Telecom, Shanghai Innovation Institute, Shanghai Jiao Tong University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [tool-augmented perception], [active perception], [GUI-eyes]
    - 📖 TLDR: This paper proposes GUI-Eyes, a reinforcement learning framework for active visual perception in GUI grounding. Instead of relying on a single static observation, the agent learns when and how to invoke tools such as cropping and zooming through a two-stage perception policy, supported by a spatially continuous reward tailored to tool usage. With only 3k labeled samples, GUI-Eyes-3B substantially improves grounding accuracy on ScreenSpot-Pro, highlighting the value of tool-aware perception for robust GUI agents.

- [Compress to Focus: Efficient Coordinate Compression for Policy Optimization in Multi-Turn GUI Agents](https://arxiv.org/abs/2601.11631)
    - Shiyu Huang, Zishuo Liu, Mingxuan Yuan, Yanzhen Chen, Hao Wen
    - 🏛️ Institutions: HiThink Research, University of California Irvine, Hangzhou Dianzi University
    - 📅 Date: January 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [policy optimization], [token compression], [visual compression], [reinforcement learning], [multi-turn agent]
    - 📖 TLDR: CCPO is a policy optimization framework for multi-turn GUI agents that uses Coordinate-Aware Spatial Compression to progressively crop screenshots to task-relevant regions across rollouts and a distance-based advantage for finer reward signals, achieving state-of-the-art grounding accuracy with up to 55% token compression and 3.8x training speedup.

- [V2P: Visual Attention Calibration for GUI Grounding via Background Suppression and Center Peaking](https://arxiv.org/abs/2601.06899)
    - Haolin Zhang, Jiahao He, Yawen Zeng, Zheng Wang, Gang Zhou
    - 🏛️ Institutions: Zhejiang University, Ant Group
    - 📅 Date: December 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [visual attention], [heatmap regression], [Fitts' law], [background suppression], [GUI agent]
    - 📖 TLDR: V2P (Valley-to-Peak) improves GUI element grounding by introducing a suppression attention mechanism to reduce background distractions and a Fitts' Law-inspired 2D Gaussian heatmap to distinguish element centers from edges, achieving 92.4% on ScreenSpot-v2 and 52.5% on ScreenSpot-Pro.

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu, Zihan Ding
    - 🏛️ Institutions: The Ohio State University, Microsoft Research
    - 📅 Date: December 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [GUI agent], [dataset], [benchmark], [text dragging], [multimodal LLM]
    - 📖 TLDR: This paper introduces GUI-Drag, a 161K-example dataset for text dragging in GUIs, and ScreenDrag, a benchmark with 5,333 examples, extending GUI grounding beyond click-only actions to support drag-based text selection and manipulation while maintaining click performance.

- [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009)
    - Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu...
    - 🏛️ Institutions: Indian Institute of Technology Bombay, Indian Institute of Technology Hyderabad
    - 📅 Date: 2025-12-26
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [multimodal LLM], [slow-fast reasoning], [visual grounding], [implicit chain-of-thought], [adaptive perception]
    - 📖 TLDR: iSHIFT is a lightweight 2.5B-parameter multimodal GUI agent that integrates latent thinking (implicit chain-of-thought) with a perception control module, enabling adaptive switching between a fast mode for routine actions and a slow mode with detailed visual grounding for precision tasks, matching state-of-the-art performance on multiple GUI benchmarks despite its compact size.

- [InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](https://arxiv.org/abs/2601.04126)
    - Yiming Liu, Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu
    - 🏛️ Institutions: Peking University, Nanjing University, Microsoft Research Asia
    - 📅 Date: December 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [data generation], [training], [benchmark], [GUI grounding], [framework]
    - 📖 TLDR: InfiniteWeb is a system that automatically synthesizes functional, diverse web environments at scale for GUI agent training, using unified specifications, task-centric test-driven development, and reference design images; agents trained on these generated environments achieve significant improvements on OSWorld and Online-Mind2Web benchmarks.

- [VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks](https://arxiv.org/abs/2512.16501)
    - Beitong Zhou, Zhexiao Huang, Yuan Guo...
    - 🏛️ Institutions: Ant Group, iMean AI
    - 📅 Date: 2025-12-18
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [GUI grounding], [cross-platform], [multi-platform], [evaluation], [dataset]
    - 📖 TLDR: VenusBench-GD is a comprehensive, bilingual GUI grounding benchmark spanning multiple platforms (mobile, desktop, web) with a hierarchical task taxonomy of six subtasks divided into basic and advanced categories, revealing that general-purpose multimodal models now match specialized GUI models on basic grounding tasks while advanced tasks still favor GUI-specialized models despite their significant overfitting and poor robustness.

- [OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models](https://arxiv.org/abs/2512.16295)
    - Zhenyu Wu, Jingjing Xie, Zehao Li...
    - 🏛️ Institutions: Shanghai Jiao Tong University, Shanghai AI Laboratory, The Chinese University of Hong Kong, The University of Hong Kong, The Hong Kong University of Science and Technology
    - 📅 Date: 2025-12-18
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [evaluation], [GUI grounding], [cross-platform], [training], [dataset]
    - 📖 TLDR: OS-Oracle introduces a comprehensive framework for training and evaluating cross-platform GUI critic models, including a scalable data pipeline (310k samples), a two-stage training paradigm (SFT + CP-GRPO), and OS-Critic Bench for step-level action evaluation across mobile, web, and desktop; the resulting OS-Oracle-7B model achieves state-of-the-art performance among open-source VLMs and improves GUI agent performance when used as a pre-critic.

- [GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection](https://arxiv.org/abs/2512.09396)
    - Zishu Wei, Qixiang Ma, Xavier Hu...
    - 🏛️ Institutions: Zhejiang University, Huawei Technologies Ltd.
    - 📅 Date: 2025-12-10
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [multi-agent], [grounding], [reasoning], [reflection], [benchmark]
    - 📖 TLDR: GAIR is a multi-agent GUI automation framework that uses a general-purpose MLLM to jointly reason over information gathered by multiple GUI-specific models, with a group reflection mechanism that drives specialized models to collect more targeted information when the decision-maker determines insufficient evidence, achieving state-of-the-art results on GUI benchmarks like ScreenSpot and UI-I2E-Bench with only 7B models.

- [MVP: Multiple View Prediction Improves GUI Grounding](https://arxiv.org/abs/2512.08529)
    - Yunzhu Zhang, Zeyu Pan, Zhengwen Zeng...
    - 🏛️ Institutions: Zhejiang University, Hangzhou Dianzi University, Ant Group
    - 📅 Date: 2025-12-09
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [training-free], [multi-view inference], [test-time augmentation], [coordinate clustering], [GUI agent]
    - 📖 TLDR: MVP is a training-free framework that improves GUI grounding accuracy by aggregating coordinate predictions from multiple attention-guided cropped views of a screenshot and selecting the centroid of the densest spatial cluster, significantly boosting performance of existing grounding models on benchmarks like ScreenSpot-Pro.

- [Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding](https://arxiv.org/abs/2512.05941)
    - Zhiyuan Jiang, Shenghao Xie, Wenyi Li...
    - 🏛️ Institutions: Xi'an Jiaotong University, Princeton University, Peking University, University of Chinese Academy of Sciences, The University of Hong Kong, Michigan State University
    - 📅 Date: 2025-12-05
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [benchmark], [training-free], [zoom], [test-time scaling], [visual grounding]
    - 📖 TLDR: Proposes ZoomClick, a training-free method that leverages zoom as a prior for GUI grounding to dynamically focus on screen regions and switch context, achieving state-of-the-art results on benchmarks like ScreenSpot-Pro, and introduces GUIZoom-Bench for evaluating model adaptability to zoom.

- [AFRAgent : An Adaptive Feature Renormalization Based High Resolution Aware GUI agent](https://arxiv.org/abs/2512.00846)
    - Neeraj Anand, Rishabh Jain, Sohan Patnaik...
    - 🏛️ Institutions: Adobe
    - 📅 Date: 2025-11-30
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile agent], [multimodal LLM], [GUI grounding], [smartphone automation], [vision-language model]
    - 📖 TLDR: AFRAgent is a compact InstructBLIP-based multimodal architecture that uses adaptive feature renormalization to fuse high-resolution image details into low-resolution embeddings, achieving state-of-the-art smartphone GUI automation on Meta-GUI and AITW benchmarks at less than one-fourth the size of competing models.

- [Prune4Web: DOM Tree Pruning Programming for Web Agent](https://arxiv.org/abs/2511.21398)
    - Jiayuan Zhang, Kaiquan Chen, Zhihao Lu, Enshen Zhou, Qian Yu, Jing Zhang
    - 🏛️ Institutions: Beihang University
    - 📅 Date: 2025-11-26
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [DOM pruning], [grounding], [LLM], [code generation], [observation simplification]
    - 📖 TLDR: Prune4Web introduces DOM Tree Pruning Programming, where an LLM generates executable Python scoring scripts to programmatically filter DOM elements based on sub-task semantics, achieving 25-50x reduction in candidate elements and improving web grounding accuracy from 46.8% to 88.28%.

- [MEGA-GUI: Multi-stage Enhanced Grounding Agents for GUI Elements](https://arxiv.org/abs/2511.13087)
    - SeokJoo Kwak, Jihoon Kim, Boyoun Kim...
    - 🏛️ Institutions: Samsung SDS
    - 📅 Date: 2025-11-17
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [multi-agent framework], [vision-language model], [region-of-interest], [benchmark], [desktop]
    - 📖 TLDR: MEGA-GUI is a multi-stage framework that decomposes GUI grounding into coarse Region-of-Interest selection and fine-grained element grounding using specialized vision-language agents, achieving state-of-the-art accuracy of 73.18% on ScreenSpot-Pro and 68.63% on OSWorld-G benchmarks.

- [Co-EPG: A Framework for Co-Evolution of Planning and Grounding in Autonomous GUI Agents](https://arxiv.org/abs/2511.10705)
    - Yuan Zhao, Hualei Zhu, Tingyu Jiang...
    - 🏛️ Institutions: Alibaba Cloud Computing, The University of Tokyo
    - 📅 Date: 2025-11-13
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [planning and grounding], [reinforcement learning], [GRPO], [co-evolution], [training framework]
    - 📖 TLDR: Co-EPG is a self-iterative training framework that co-evolves planning and grounding models for GUI agents through a positive feedback loop using GRPO and confidence-based reward ensembles, achieving state-of-the-art results on Multimodal-Mind2Web and AndroidControl benchmarks without external data.

- [Grounding Computer Use Agents on Human Demonstrations](https://arxiv.org/abs/2511.07332)
    - Aarash Feizi, Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Kaixin Li, Rabiul Awal, Xing Han Lu, Johan Obando-Ceron, Juan A. Rodriguez, Nicolas Chapados, David Vazquez, Adriana Romero-Soriano, Reihaneh Rabbany, Perouz Taslakian, Christopher Pal, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, McGill University, Universite de Montreal, ServiceNow Research, University of Waterloo, University of Oxford, National University of Singapore, Polytechnique Montreal, Ecole de Technologie Superieure, CIFAR
    - 📅 Date: November 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [model], [GUI grounding], [desktop grounding], [reinforcement learning], [GroundCUA], [GroundNext]
    - 📖 TLDR: This paper introduces GroundCUA, a large-scale desktop grounding dataset built from expert human demonstrations, covering 87 applications, 56K screenshots, and more than 3.56M human-verified UI annotations. Using this data, the authors train the GroundNext family of grounding models, which achieve state-of-the-art results across five benchmarks with far less training data than prior work, and improve further with reinforcement learning post-training. The paper shows that high-quality human demonstration data is a key driver for robust grounding in general-purpose computer-use agents.

- [AUTO-Explorer: Automated Data Collection for GUI Agent](https://arxiv.org/abs/2511.06417)
    - Xiangwu Guo, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: 2025-11-09
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [data collection], [benchmark], [GUI grounding], [exploration], [fine-tuning]
    - 📖 TLDR: Auto-Explorer is an automated data collection method that autonomously parses and explores GUI environments to gather training data for GUI agents, accompanied by the UIXplore benchmark for evaluating exploration quality. The collected data is used to fine-tune multimodal LLMs, demonstrating improved GUI element grounding capabilities on novel software and websites.

- [GUI-360☆: A Comprehensive Dataset and Benchmark for Computer-Using Agents](https://arxiv.org/abs/2511.04307)
    - Jian Mu, Chaoyun Zhang, Chiming Ni, Lu Wang, Bo Qiao...
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [computer-use agent], [GUI grounding], [screen parsing]
    - 📖 TLDR: GUI-360☆ is a large-scale dataset and benchmark suite with an LLM-augmented automated pipeline for CUAs, jointly evaluating GUI grounding, screen parsing, and action prediction to address the scarcity of real-world CUA tasks and the absence of a unified multi-capability benchmark.

- [GUI-AIMA: Aligning Intrinsic Multimodal Attention with a Context Anchor for GUI Grounding](https://arxiv.org/abs/2511.00810)
    - Shijie Zhou, Viet Dac Lai, Hao Tan, Jihyung Kil, Wanrong Zhu...
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-02
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [attention mechanism], [visual grounding], [VLM], [coordinate-free]
    - 📖 TLDR: GUI-AIMA is a coordinate-free supervised fine-tuning framework for GUI grounding that aligns intrinsic multimodal attention with a context anchor, leveraging native MLLM attention maps to identify instruction-relevant visual patches and refine exact click locations—improving efficiency over direct coordinate generation.

- [UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning](https://arxiv.org/abs/2510.20286)
    - Liangyu Chen, Hanzhang Zhou, Chenglin Cai, Jianan Zhang, Panrong Tong, Quyu Kong, Xu Zhang, Chen Liu, Yuqi Liu, Wenxuan Wang, Yue Wang, Qin Jin, Steven Hoi
    - 🏛️ Institutions: Renmin University of China, Tongyi Lab, Alibaba Group, The Chinese University of Hong Kong
    - 📅 Date: October 23, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [GUI grounding], [instruction-as-reasoning], [UI-ins]
    - 📖 TLDR: This paper reframes GUI grounding instructions as reasoning pathways rather than static text prompts. It first synthesizes diverse, high-quality instruction variants for supervised training, then uses reinforcement learning to optimize pathway selection and composition at inference time. The resulting UI-Ins-7B and UI-Ins-32B models achieve state-of-the-art grounding accuracy across five benchmarks and also improve downstream AndroidWorld agent execution.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Unaffiliated
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [mobile GUI agent], [GUI-shift]
    - 📖 TLDR: This paper introduces GUI-Shift, a self-supervised reinforcement learning framework for VLM-based GUI agents built around the K-step GUI Transition task, which learns GUI dynamics from unlabeled trajectories without natural-language instruction annotation. The method combines rule-based optimization with data filtering and improves both GUI automation and grounding performance across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro. The paper shows a scalable path to training stronger mobile GUI agents from large amounts of unlabeled interaction data.

- [GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding](https://arxiv.org/abs/2510.04039)
    - Bin Lei, Nuo Xu, Ali Payani, Mingyi Hong, Chunhua Liao, Yu Cao, Caiwen Ding
    - 🏛️ Institutions: University of Minnesota, Cisco Research, Lawrence Livermore National Laboratory
    - 📅 Date: October 5, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [tool coordination], [iterative refinement], [visual grounding]
    - 📖 TLDR: This paper proposes GUI-Spotlight, a model for GUI visual grounding that iteratively refines its focus using specialized tools like crop, extract, and find_color. Trained with a hybrid of supervised learning and reinforcement learning, the method dynamically invokes tools over multiple rounds, improving accuracy and efficiency. It significantly outperforms previous methods on benchmarks like ScreenSpot-Pro and UI-Vision with less training data.

- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
    - Zhangxuan Gu, Zhengwen Zeng, Zhenyu Xu, Xingran Zhou, Shuheng Shen, Yunfei Liu, Beitong Zhou, Changhua Meng, Tianyu Xia, Weizhi Chen, Yue Wen, Jingya Dou, Fei Tang, Jinzhen Lin, Yulin Liu, Zhenlin Guo, Yichen Gong, Heng Jia, Changlong Gao, Yuan Guo, Yong Deng, Zhenyu Guo, Liang Chen, Weiqiang Wang
    - 🏛️ Institutions: Ant Group
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [grounding], [navigation], [data cleaning], [Qwen2.5-VL], [UI-venus]
    - 📖 TLDR: This technical report introduces **UI-Venus**, a screenshot-based UI agent built on the multimodal Qwen2.5-VL model and fine-tuned via **reinforcement fine-tuning (RFT)**. It achieves state-of-the-art performance on UI grounding and navigation benchmarks—e.g., Screenspot-V2/Pro (up to 95.3% / 61.9%) and AndroidWorld navigation (up to 65.9%)—by leveraging carefully crafted reward functions, efficient data cleaning pipelines, and a novel **self-evolving framework** (trajectory alignment and sparse action enhancement) to enhance reasoning coherence and handle rare actions. The code and checkpoints are open-sourced to encourage further development.

- [Test‑Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615)
    - Yong Du, Yuchen Yan, Fei Tang, Zhengxi Lu, Chang Zong, Weiming Lu, Shengpei Jiang, Yongliang Shen
    - 🏛️ Institutions: Zhejiang University, Central South University, Zhejiang University of Science and Technology, SF Technology
    - 📅 Date: August 7, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time scaling], [reinforcement learning], [self‑supervised], [GUI‑RC], [GUI‑RCPO], [benchmark], [region consistency], [GUI grounding]
    - 📖 TLDR: This paper introduces **GUI‑RC (Region Consistency)**, a test-time method that aggregates multiple model predictions via spatial voting to derive a consensus region—achieving 2–3% accuracy improvements on ScreenSpot benchmarks without any additional training. It extends this idea with **GUI‑RCPO (Region Consistency Policy Optimization)**, which turns region-consistency patterns into self-supervised rewards for reinforcement learning at inference time, refining model predictions on unlabeled data and yielding further improvements (e.g., from 83.57% to 85.14% on ScreenSpot‑v2). The approach demonstrates a novel and effective use of test-time optimization for more robust, data-efficient GUI grounding.

- [GuirlVG: Incentivize GUI Visual Grounding via Empirical Exploration on Reinforcement Learning](https://arxiv.org/abs/2508.04389)
    - Weitai Kang, Bin Lei, Gaowen Liu, Caiwen Ding, Yan Yan
    - 🏛️ Institutions: University of Illinois Chicago, University of Minnesota, Cisco Research
    - 📅 Date: August 6, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [reinforcement learning], [reinforcement fine-tuning], [ScreenSpot], [GuirlVG]
    - 📖 TLDR: This paper studies reinforcement fine-tuning for GUI visual grounding and argues that naive rule-based RL underperforms strong supervised baselines without careful formulation. It introduces GuirlVG, which systematically redesigns the reward, training setup, and stabilization mechanism, including an Adversarial KL Factor to reduce reward over-optimization. With only 5.2K training samples, the method surpasses prior GUI grounding approaches trained on much larger datasets across ScreenSpot, ScreenSpot-Pro, and ScreenSpot-V2.

- [Phi-Ground Tech Report: Advancing Perception in GUI Grounding](https://arxiv.org/abs/2507.23779)
    - Miaosen Zhang, Ziqiang Xu, Jialiang Zhu, Qi Dai, Kai Qiu...
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-07-31
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [model], [computer-use agent], [visual grounding], [benchmark]
    - 📖 TLDR: Phi-Ground is a tech report advancing GUI grounding perception for CUAs, presenting a model series significantly improving accuracy on challenging benchmarks including ScreenSpot-Pro and UI-Vision beyond the ~65% ceiling of existing end-to-end grounding models.

- [GTA1: GUI Test-time Scaling Agent](https://arxiv.org/abs/2507.05791)
    - Yan Yang, Dongxu Li, Yutong Dai, Yuhao Yang, Ziyang Luo, Zirui Zhao, Zhiyuan Hu, Junzhe Huang, Amrita Saha, Zeyuan Chen, Ran Xu, Liyuan Pan, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research, Australian National University, The University of Hong Kong
    - 📅 Date: July 8, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time scaling], [reinforcement learning], [planning], [grounding], [GTA1]
    - 📖 TLDR: This paper tackles two major challenges in GUI agents — planning ambiguity and visual grounding accuracy. It introduces **GTA1**, a GUI Test-time Scaling Agent that improves action decision-making by sampling multiple candidate actions at each step and selecting the best one via a judge model. Additionally, it enhances grounding through reinforcement learning with success-based rewards. GTA1 achieves state-of-the-art results on GUI grounding and execution benchmarks such as ScreenSpot and OSWorld.

- [GLM-4.5V and GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning](https://arxiv.org/abs/2507.01006)
    - Wenyi Hong, Wenmeng Yu, Xiaotao Gu, Guo Wang, Guobing Gan, Haomiao Tang, Jiale Cheng, Ji Qi, Junhui Ji, Lihang Pan, Shuaiqi Duan, Weihan Wang, Yan Wang, Yean Cheng, Zehai He, Zhe Su, Zhen Yang, Ziyang Pan, Aohan Zeng, Baoxu Wang, Bin Chen, Boyan Shi, Changyu Pang, Chenhui Zhang, Da Yin, Fan Yang, Guoqing Chen, Haochen Li, Jiale Zhu, Jiali Chen, Jiaxing Xu, Jing Chen, Jinghao Lin, Jinhao Chen, Jinjiang Wang, Junjie Chen, Leqi Lei, Letian Gong, Leyi Pan, Mingdao Liu, Mingde Xu, Mingzhi Zhang, Qinkai Zheng, Ruiliang Lyu, Shangqin Tu, Sheng Yang, Shengbiao Meng, Shi Zhong, Shiyu Huang, Shuyuan Zhao, Siyan Xue, Tianshu Zhang, Tianwei Luo, Tianxiang Hao, Tianyu Tong, Wei Jia, Wenkai Li, Xiao Liu, Xiaohan Zhang, Xin Lyu, Xinyu Zhang, Xinyue Fan, Xuancheng Huang, Yadong Xue, Yanfeng Wang, Yanling Wang, Yanzi Wang, Yifan An, Yifan Du, Yiheng Huang, Yilin Niu, Yiming Shi, Yu Wang, Yuan Wang, Yuanchang Yue, Yuchen Li, Yusen Liu, Yutao Zhang, Yuting Wang, Yuxuan Zhang, Zhao Xue, Zhengxiao Du, Zhenyu Hou, Zihan Wang, Peng Zhang, Debing Liu, Bin Xu, Juanzi Li, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu AI, Tsinghua University
    - 📅 Date: July 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [RLCS], [multimodal], [vision language model], [grounding], [GLM-4.1V-thinking], [GLM-4.5V]
    - 📖 TLDR: Introduces two vision-language models—**GLM-4.1V-9B-Thinking**, a 9B-parameter model designed for multimodal reasoning, and **GLM-4.5V**, a larger version based on GLM-4.5-Air (106B parameters, 12B active). The authors propose a reasoning-centric training pipeline including large-scale pretraining and a novel **Reinforcement Learning with Curriculum Sampling (RLCS)** framework. The models show state-of-the-art performance across 42 (GLM-4.5V) and 28 (GLM-4.1V-Thinking) public multimodal benchmarks, often outperforming much larger models (e.g., Qwen-2.5-VL-72B and Gemini-2.5-Flash), especially in tasks like STEM reasoning, video/document understanding, coding, GUI agents, and grounding. Both models and training code are open-sourced.

- [LPO: Towards Accurate GUI Agent Interaction via Location Preference Optimization](https://arxiv.org/abs/2506.09373)
    - Jiaqi Tang, Yu Xia, Yi‑Feng Wu, Yuwei Hu, Yuhui Chen, Qing‑Guo Chen, Xiaogang Xu, Xiangyu Wu, Hao Lu, Yanqing Ma, Shiyin Lu, Qifeng Chen
    - 🏛️ Institutions: Hong Kong University of Science and Technology, Alibaba Group, The Chinese University of Hong Kong, Nanjing University of Science and Technology
    - 📅 Date: June 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [grounding], [navigation], [location reward], [GRPO], [LPO]
    - 📖 TLDR: The paper introduces **Location Preference Optimization (LPO)** to improve GUI agent interaction accuracy. It uses information-entropy-driven zones of interest and a dynamic distance-based reward function. Built atop Group Relative Preference Optimization (GRPO), it enables more precise spatial grounding. Results show SOTA performance on offline benchmarks and real-world online GUI tasks.

- [UITron-Speech: Towards Automated GUI Agents Based on Speech Instructions](https://arxiv.org/abs/2506.11127)
    - Wenkang Han, Zhixiong Zeng, Jing Huang, Shu Jiang, Liming Zheng, Longrong Yang, Haibo Qiu, Chang Yao, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, Harbin Institute of Technology
    - 📅 Date: 2025-06-10
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [speech input], [multimodal], [grounding], [mobile], [training strategy]
    - 📖 TLDR: UITron-Speech is the first end-to-end GUI agent that directly processes speech instructions and on-device screenshots to predict user actions, using synthesized speech datasets, a mixed-modality training strategy, and a training-free grounding refinement method to address data scarcity, modality imbalance, and localization deviations.

- [GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents](https://arxiv.org/abs/2506.03143)
    - Qianhui Wu, Kanzhi Cheng, Rui Yang, Chaoyun Zhang, Jianwei Yang, Huiqiang Jiang, Jian Mu, Baolin Peng, Bo Qiao, Reuben Tan, Si Qin, Lars Liden, Qingwei Lin, Huan Zhang, Tong Zhang, Jianbing Zhang, Dongmei Zhang, Jianfeng Gao
    - 🏛️ Institutions: Microsoft, Nanjing University, University of Illinois Urbana-Champaign
    - 📅 Date: June 3, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [grounding verifier], [attention mechanism], [coordinate‑free grounding], [GUI‑Actor]
    - 📖 TLDR: GUI‑Actor introduces a coordinate‑free visual grounding approach for GUI agents by adding an attention‑based “<ACTOR>” action head atop a frozen vision‑language model. It learns to align with relevant visual patches and produces multiple candidate regions per forward pass. An optional grounding verifier scores candidates to select the best. The method improves spatial‑semantic alignment and generalizes well across unseen resolutions. On benchmarks like ScreenSpot‑Pro, GUI‑Actor‑7B outperforms prior SOTA UI‑TARS‑72B, with verifier‑augmented versions achieving even higher accuracy—while only fine‑tuning ~100 M parameters.

- [SE-GUI: Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: VCIP, School of Computer Science, Nankai University, vivo Mobile Communication Co., Ltd
    - 📅 Date: May 24, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [visual grounding], [ScreenSpot-pro], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Gaoling School of Artificial Intelligence, Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [visual grounding], [reinforcement learning], [ScreenSpot], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [ReGUIDE: Data Efficient GUI Grounding via Spatial Reasoning and Search](https://arxiv.org/abs/2505.15259)
    - Hyunseok Lee, Jeonghoon Kim, Beomjun Kim, Jihoon Tack, Chansong Jo...
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-21
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [GUI grounding], [web agent], [spatial reasoning], [data efficiency], [framework]
    - 📖 TLDR: ReGUIDE (Reasoning GUI Grounding for Data Efficiency) is a data-efficient web GUI grounding framework enabling MLLMs to learn accurate element localization via spatial reasoning and search, significantly reducing reliance on large-scale web datasets while improving grounding accuracy.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets and Benchmarks Track (Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [framework], [jedi], [OSWorld‑G], [GUI grounding], [compositional generalization], [fine‑grained manipulation]
    - 📖 TLDR: This work tackles limitations in GUI grounding by introducing **OSWorld‑G**, a 564‑sample benchmark covering text matching, element recognition, layout understanding, fine‑grained manipulation, and refusal detection. They also synthesize **Jedi**, a massive 4 M‑example dataset generated via UI decomposition and synthesis. Training multi‑scale models on Jedi achieves state‑of‑the‑art grounding across benchmarks (ScreenSpot‑v2/Pro and OSWorld‑G), boosting agentic task performance from 5 % to ~27 % success. Ablations demonstrate compositional benefits. All artifacts are publicly released.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: UMich, LG AI Research
    - 📅 Date: May 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [RegionFocus], [test-time scaling], [grounding], [Qwen2.5-VL], [UI-TARS]
    - 📖 TLDR: This paper introduces *RegionFocus*, a visual test-time scaling method for GUI agents that dynamically zooms into relevant regions within GUI images, reducing background clutter and enhancing grounding accuracy. By integrating an "image-as-map" mechanism to visualize key landmarks during each interaction step, the approach improves transparency and decision-making. Applied to state-of-the-art vision-language models like UI-TARS and Qwen2.5-VL, RegionFocus achieves significant performance gains—28% on ScreenSpot-Pro and 24% on WebVoyager benchmarks—setting a new state-of-the-art grounding accuracy of 61.6% on ScreenSpot-Pro.

- [ScaleTrack: Scaling and back-tracking Automated GUI Agents](https://arxiv.org/abs/2505.00416)
    - Jing Huang, Zhixiong Zeng, Wenkang Han, Yufeng Zhong, Liming Zheng, Shuai Fu, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, University of Adelaide
    - 📅 Date: May 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [training strategy], [back-tracking], [grounding], [planning], [ScaleTrack]
    - 📖 TLDR: This paper introduces *ScaleTrack*, a training framework designed to enhance automated GUI agents by addressing two primary challenges: insufficient training data for GUI grounding and the lack of back-tracking in GUI planning. The authors aggregate diverse GUI samples from various synthesis methods into a unified template to scale the grounding process. Additionally, they propose a hybrid training strategy that combines forward-planning and back-tracking, enabling the agent to predict both the next action and the historical actions leading to the current GUI state. Experimental results demonstrate that ScaleTrack significantly improves task success rates across multiple benchmarks, highlighting the effectiveness of integrating back-tracking into GUI agent training.

- [RealWebAssist: A Benchmark for Long-Horizon Web Assistance with Real-World Users](https://arxiv.org/abs/2504.10445)
    - Suyu Ye, Haojun Shi, Darren Shih, Hyokun Yun, Tanya G. Roosta, Tianmin Shu
    - 🏛️ Institutions: Johns Hopkins University, Amazon
    - 📅 Date: April 14, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [GUI grounding], [speech input], [spatial reasoning], [temporal reasoning], [multi-step planning], [routine learning], [RealWebAssist]
    - 📖 TLDR: RealWebAssist introduces a benchmark for evaluating AI agents' ability to assist with long-horizon web tasks using sequential instructions from real-world users. The dataset includes 1,885 instructions across 107 tasks on 66 websites, featuring challenges like ambiguous instructions, GUI grounding, and evolving user goals. Evaluations show that current state-of-the-art models struggle with these complex, realistic scenarios.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 1, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [mixture-of-grounding], [proactive hierarchical planning], [benchmark], [OSWorld], [WindowsAgentArena], [AndroidWorld]
    - 📖 TLDR: This paper introduces *Agent S2*, a compositional framework for computer use agents that combines generalist and specialist models to address challenges in GUI element grounding and long-horizon task planning. The framework employs a novel Mixture-of-Grounding technique for precise GUI localization and Proactive Hierarchical Planning to dynamically refine action plans. Evaluations demonstrate that Agent S2 achieves state-of-the-art performance on benchmarks like OSWorld, WindowsAgentArena, and AndroidWorld, outperforming existing agents such as Claude Computer Use and UI-TARS.

- [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661)
    - Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Juan A. Rodriguez, Montek Kalsi, Rabiul Awal, Nicolas Chapados, M. Tamer Özsu, Aishwarya Agrawal, David Vazquez, Christopher Pal, Perouz Taslakian, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, Universite de Montreal, ServiceNow, University of Waterloo, National University of Singapore, Ecole de Technologie Superieure, CIFAR AI Chair, Polytechnique Montreal
    - 📅 Date: March 19, 2025
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [framework], [UI-vision], [UI-TARS-72B], [spatial reasoning], [drag-and-drop], [element grounding], [layout grounding], [action prediction]
    - 📖 TLDR: This paper introduces *UI-Vision*, a comprehensive, license-permissive benchmark designed for evaluating autonomous agents in real-world desktop GUI environments. It encompasses 83 software applications with dense annotations of human demonstrations, including bounding boxes, UI labels, and action trajectories. The benchmark defines three tasks—Element Grounding, Layout Grounding, and Action Prediction—to assess agents' performance. Evaluations reveal limitations in state-of-the-art models like UI-TARS-72B, particularly in understanding professional software, spatial reasoning, and complex actions such as drag-and-drop. By releasing UI-Vision as open-source, the authors aim to advance the development of more capable agents for desktop tasks.

- [STEVE: A Step Verification Pipeline for Computer-use Agent Training](https://arxiv.org/abs/2503.12532)
    - Fanbin Lu, Zhisheng Zhong, Ziqin Wei, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: The Chinese University of Hong Kong, SmartMore, Hong Kong University of Science and Technology
    - 📅 Date: March 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [model], [UI grounding], [KTO], [GPT-4o], [WinAgentArena]
    - 📖 TLDR: This paper introduces **STEVE**, a step verification pipeline designed to enhance the training of computer-use agents. The approach involves creating a large instruction set and collecting trajectory data using suboptimal agents. GPT-4o is employed to verify the correctness of each action step by comparing pre- and post-action screenshots, assigning binary labels. The agent is then optimized using Kahneman and Tversky Optimization (KTO) based on these labels. The result is a 7B vision-language model that achieves state-of-the-art performance in the WinAgentArena desktop environment, outperforming supervised fine-tuning methods by effectively leveraging both positive and negative action data.

- [DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents](https://arxiv.org/abs/2503.11170)
    - Yibin Xu, Liang Yang, Hao Chen, Hua Wang, Zhi Chen, Yaohua Tang
    - 🏛️ Institutions: Moore Threads AI
    - 📅 Date: March 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [desktop], [GUI understanding], [grounding], [data pipeline], [benchmark]
    - 📖 TLDR: DeskVision introduces an automated data pipeline (AutoCaptioner) and a large-scale desktop GUI dataset with 54,855 images and 303,622 annotations across Windows, macOS, and Linux, along with the DeskVision-Eval benchmark, and trains a GUI understanding model (GUIExplorer) that achieves state-of-the-art performance on visual element understanding and grounding tasks.

- [SpiritSight Agent: Advanced GUI Agent with One Look](https://arxiv.org/abs/2503.03196)
    - Zhiyuan Huang, Ziming Cheng, Junting Pan, Zhaohui Hou, Mingjie Zhan
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-03-05
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [GUI grounding], [VLM], [framework], [efficiency]
    - 📖 TLDR: SpiritSight Agent is a vision-based GUI agent that addresses element grounding accuracy limitations by proposing a novel single-screenshot architecture enabling high-accuracy, low-latency, cross-platform GUI interaction with improved element grounding through efficient screen comprehension.

- [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981)
    - Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, Tat-Seng Chua
    - 🏛️ Institutions: National University of Singapore, East China Normal University, Hong Kong Baptist University
    - 📅 Date: January 3, 2025
    - 📑 Publisher: ACM Multimedia 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [GUI grounding], [high-resolution], [ScreenSpot-pro]
    - 📖 TLDR: ScreenSpot-Pro introduces a benchmark designed to evaluate GUI grounding models in professional, high-resolution environments. It encompasses 1,581 tasks across 23 applications in various industries, highlighting the challenges models face with complex software interfaces. Current models achieve low accuracy, underscoring the need for further research in this domain.

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research, Alibaba Group, Australian National University, Independent
    - 📅 Date: Dec 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [grounding], [visual grounding], [aria-UI]
    - 📖 TLDR: This paper introduces *Aria-UI*, a large multimodal model specifically designed for GUI grounding. Aria-UI employs a pure-vision approach, avoiding reliance on auxiliary inputs like HTML or AXTree. It utilizes a scalable data pipeline to synthesize diverse and high-quality instruction samples and incorporates textual and text-image interleaved action histories for robust context-aware reasoning. Aria-UI achieves state-of-the-art results across offline and online agent benchmarks, outperforming both vision-only and AXTree-reliant baselines.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, National University of Singapore
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [information-sensitive cropping], [self-refining dual learning], [visual grounding], [model]
    - 📖 TLDR: This paper introduces *Iris*, a visual agent designed to enhance GUI automation by addressing challenges in high-resolution, complex digital environments. It employs two key innovations: **Information-Sensitive Cropping (ISC)**, which dynamically identifies and prioritizes visually dense regions using an edge detection algorithm for efficient processing, and **Self-Refining Dual Learning (SRDL)**, which enhances the agent's ability to handle complex tasks through a dual-learning loop that iteratively refines its performance without requiring additional annotated data. Empirical evaluations demonstrate that Iris achieves state-of-the-art performance across multiple benchmarks with only 850K GUI annotations, outperforming methods using ten times more training data.

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Nanyang Technological University, Salesforce
    - 📅 Date: Dec 5, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [planning], [reasoning], [aguvis], [visual grounding]
    - 📖 TLDR: This paper introduces *Aguvis*, a unified pure vision-based framework for autonomous GUI agents that operates across various platforms. It leverages image-based observations and grounds natural language instructions to visual elements, employing a consistent action space to ensure cross-platform generalization. The approach integrates explicit planning and reasoning within the model, enhancing its ability to autonomously navigate and interact with complex digital environments. A large-scale dataset of GUI agent trajectories is constructed, incorporating multimodal reasoning and grounding. Comprehensive experiments demonstrate that Aguvis surpasses previous state-of-the-art methods in both offline and real-world online scenarios, achieving the first fully autonomous pure vision GUI agent capable of performing tasks independently without collaboration with external closed-source models. All datasets, models, and training recipes are open-sourced to facilitate future research.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://aclanthology.org/2025.findings-acl.76/)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: December 2, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [reinforcement learning], [ponder & press]
    - 📖 TLDR: This paper introduces *Ponder & Press*, a divide-and-conquer framework for general computer control using only visual input. The approach combines a general-purpose multimodal large language model (MLLM) as an 'interpreter' to translate high-level user instructions into detailed action descriptions, with a GUI-specific MLLM as a 'locator' that precisely identifies GUI elements for action execution. By relying solely on visual inputs, the agent offers a versatile, human-like interaction paradigm applicable across various platforms, achieving state-of-the-art performance in GUI grounding and control tasks.

- [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)
    - Anthony Nguyen
    - 🏛️ Institutions: Algoma University
    - 📅 Date: November 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [grounding], [visual grounding], [iterative narrowing]
    - 📖 TLDR: This paper introduces a visual framework to enhance GUI grounding. By iteratively refining model predictions through progressively focused image crops, the proposed method improves the performance of both general and fine-tuned Vision-Language Models (VLMs) in GUI grounding tasks.

- [ClickAgent: Enhancing UI Location Capabilities of Autonomous Agents](https://aclanthology.org/2025.sigdial-1.38/)
    - Jakub Hoscilowicz, Bartosz Maj, Bartosz Kozakiewicz, Oleksii Tymoshchuk, Artur Janicki
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 9, 2024
    - 📑 Publisher: SIGDIAL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI grounding], [mobile agent], [AITW], [InternVL2], [TinyClick], [ClickAgent]
    - 📖 TLDR: The paper introduces *ClickAgent*, a framework that enhances autonomous agents' interaction with mobile UIs by improving their ability to locate interface elements accurately. This is achieved through a dual-component system where an MLLM performs reasoning and action planning, while a dedicated UI location model (e.g., SeeClick) handles element identification. ClickAgent, evaluated on the AITW benchmark and tested on both emulators and real Android devices, surpasses other agents like CogAgent and AppAgent in task success rate, advancing automation reliability on mobile platforms.

- [TinyClick: Single-Turn Agent for Empowering GUI Automation](https://www.isca-archive.org/interspeech_2025/pawlowski25_interspeech.html)
    - Pawel Pawlowski, Krystian Zawistowski, Wojciech Lapacz, Adam Wiacek, Marcin Skorupa, Sebastien Postansque, Jakub Hoscilowicz
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 9, 2024
    - 📑 Publisher: INTERSPEECH 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [single-turn agent], [on-device model], [ScreenSpot], [OmniAct], [TinyClick]
    - 📖 TLDR: TinyClick is a compact, single-turn agent designed to automate GUI tasks by precisely locating screen elements via the Vision-Language Model Florence-2-Base. Trained with multi-task strategies and MLLM-based data augmentation, TinyClick achieves high accuracy on Screenspot and OmniAct, outperforming specialized GUI interaction models and general MLLMs like GPT-4V. The model's lightweight design (0.27B parameters) ensures fast processing and minimal latency, making it efficient for real-world applications on multiple platforms.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0faa4bc5f522076947a030273629d4fe-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: October 7, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [visual grounding], [GUI agent], [cross-platform generalization], [UGround], [SeeAct-v], [synthetic data]
    - 📖 TLDR: This paper introduces UGround, a universal visual grounding model for GUI agents that enables human-like navigation of digital interfaces. The authors advocate for GUI agents with human-like embodiment that perceive the environment entirely visually and take pixel-level actions. UGround is trained on a large-scale synthetic dataset of 10M GUI elements across 1.3M screenshots. Evaluated on six benchmarks spanning grounding, offline, and online agent tasks, UGround significantly outperforms existing visual grounding models by up to 20% absolute. Agents using UGround achieve comparable or better performance than state-of-the-art agents that rely on additional textual input, demonstrating the feasibility of vision-only GUI agents.

- [MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a2c3c86679300047c740c9900f19ddac-Abstract-Conference.html)
    - Haotian Zhang, Mingfei Gao, Zhe Gan, Philipp Dufter, Nina Wenzel, Forrest Huang, Dhruti Shah, Xianzhi Du, Bowen Zhang, Yanghao Li, Sam Dodge, Keen You, Zhen Yang, Aleksei Timofeev, Mingze Xu, Hong-You Chen, Jean-Philippe Fauconnier, Zhengfeng Lai, Haoxuan You, Zirui Wang, Afshin Dehghan, Peter Grasch, Yinfei Yang
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Misc]
    - 🔑 Key: [model], [MM1.5], [vision language model], [visual grounding], [reasoning], [data-centric], [analysis]
    - 📖 TLDR: This paper introduces MM1.5, a family of multimodal large language models (MLLMs) ranging from 1B to 30B parameters, including dense and mixture-of-experts variants. MM1.5 enhances capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning. The authors employ a data-centric training approach, utilizing high-quality OCR data and synthetic captions for continual pre-training, alongside an optimized visual instruction-tuning data mixture for supervised fine-tuning. Specialized variants, MM1.5-Video and MM1.5-UI, are designed for video understanding and mobile UI comprehension, respectively. Extensive empirical studies provide insights into the training processes, offering guidance for future MLLM development.

- [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337)
    - Longxi Gao, Li Zhang, Shihe Wang, Pengzhi Gao, Wei Liu, Jian Luan, Shangguang Wang, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [mobile], [Android], [GUI grounding], [data collection], [benchmark]
    - 📖 TLDR: MobileViews is a million-scale mobile GUI dataset comprising over 1.2 million screenshot-view hierarchy pairs from 30K+ Android apps, collected via an automated VLM-enhanced traversal framework on mobile SoC clusters, which improves GUI grounding accuracy by up to 6.1% when used to train visual language models.

- [Grounded GUI Understanding for Vision-Based Spatial Intelligent Agent: Exemplified by Extended Reality Apps](https://arxiv.org/abs/2409.10811)
    - Shuqing Li, Binchang Li, Yepang Liu, Cuiyun Gao, Jianping Zhang, Shing-Chi Cheung, Michael R. Lyu
    - 🏛️ Institutions: The Chinese University of Hong Kong, Harbin Institute of Technology, Southern University of Science and Technology, The Hong Kong University of Science and Technology
    - 📅 Date: September 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI understanding], [GUI grounding], [VR/AR], [zero-shot detection], [multimodal LLM], [software testing]
    - 📖 TLDR: Proposes Orienter, the first zero-shot context-sensitive interactable GUI element detection framework for Extended Reality (XR/VR) apps, which uses semantic context comprehension and reflection-directed detection to identify interactable GUI elements in 3D virtual environments more effectively than existing approaches.

- [From Grounding to Planning: Benchmarking Bottlenecks in Web Agents](https://ebooks.iospress.nl/doi/10.3233/FAIA250590)
    - Segev Shlomov, Ben Wiesel, Aviad Sela, Ido Levy, Liane Galanti, Roy Abitbol
    - 🏛️ Institutions: IBM Research - Haifa, University of Haifa
    - 📅 Date: September 3, 2024
    - 📑 Publisher: ECAI 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [grounding], [Mind2Web], [AssistantBench], [web navigation]
    - 📖 TLDR: This paper analyzes performance bottlenecks in web agents by separately evaluating grounding and planning tasks, isolating their individual impacts on navigation efficacy. Using an enhanced version of the Mind2Web dataset, the study reveals planning as a significant bottleneck, with advancements in grounding and task-specific benchmarking for elements like UI component recognition. Through experimental adjustments, the authors propose a refined evaluation framework, aiming to enhance web agents' contextual adaptability and accuracy in complex web environments.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: Carnegie Mellon University, University of California, Santa Barbara
    - 📅 Date: June 2024
    - 📑 Publisher: NAACL 2024 Industry Track
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [UI element localization], [LVG]
    - 📖 TLDR: This work introduces the task of visual UI grounding, which unifies detection and grounding by enabling models to identify UI elements referenced by natural language commands solely from visual input. The authors propose **LVG**, a model that outperforms baselines pre-trained on larger datasets by over 4.9 points in top-1 accuracy, demonstrating its effectiveness in localizing referenced UI elements without relying on UI metadata.

- [Visual Grounding Methods for Efficient Interaction with Desktop Graphical User Interfaces](https://arxiv.org/abs/2407.01558)
    - El Hassane Ettifouri, Jessica López Espejel, Laura Minkova, Tassnim Dardouri, Walid Dahhane
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2024-05-05
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [GUI grounding], [visual grounding], [desktop], [GUI agent], [benchmark]
    - 📖 TLDR: Explores Instruction Visual Grounding (IVG) for desktop GUI automation, benchmarking multi-modal approaches to element identification within GUI interfaces for automated software testing, accessibility, and human-computer interaction applications.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web page understanding], [grounding]
    - 📖 TLDR: VisualWebBench introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on web-based tasks. It includes 1.5K human-curated instances across 139 websites in 87 sub-domains. The benchmark spans seven tasks—such as OCR, grounding, and web-based QA—aiming to test MLLMs' capabilities in fine-grained web page understanding. Results reveal significant performance gaps, particularly in grounding tasks, highlighting the need for advancement in MLLM web understanding.

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://eccv.ecva.net/virtual/2024/poster/749)
    - Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeff Nichols, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: April 8, 2024
    - 📑 Publisher: ECCV 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [benchmark], [grounding], [reasoning], [mobile UI understanding], [ferret-UI]
    - 📖 TLDR: This paper presents **Ferret-UI**, a multimodal large language model (MLLM) designed to understand and interact with mobile user interfaces. The model incorporates advanced capabilities for referring, grounding, and reasoning about UI elements. By training on a variety of UI tasks, Ferret-UI achieves high performance in tasks such as icon recognition and text extraction. The authors introduce a unique architecture that allows for improved visual feature extraction from mobile screens, paving the way for applications in accessibility and user interaction.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Li YanTao, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: Nanjing University, Shanghai AI Lab
    - 📅 Date: January 19, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [benchmark], [GUI grounding], [visual grounding]
    - 📖 TLDR: TBD.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [grounding], [SeeAct], [multimodal-Mind2web]
    - 📖 TLDR: This paper explores the capability of GPT-4V(ision), a multimodal model, as a web agent that can perform tasks across various websites by following natural language instructions. It introduces the **SEEACT** framework, enabling GPT-4V to navigate, interpret, and interact with elements on websites. Evaluated using the **Mind2Web** benchmark and an online test environment, the framework demonstrates high performance on complex web tasks by integrating grounding strategies like element attributes and image annotations to improve HTML element targeting. However, grounding remains challenging, presenting opportunities for further improvement.

- [Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V](https://arxiv.org/abs/2310.11441)
    - Jianwei Yang, Hao Zhang, Feng Li, Xueyan Zou, Chunyuan Li, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research
    - 📅 Date: October 17, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [visual prompting], [framework], [benchmark], [visual grounding], [zero-shot]
    - 📖 TLDR: This paper introduces Set-of-Mark (SoM), a novel visual prompting approach designed to enhance the visual grounding capabilities of multimodal models like GPT-4V. By overlaying images with spatially and semantically distinct marks, SoM enables fine-grained object recognition and interaction within visual data, surpassing conventional zero-shot segmentation methods in accuracy. The framework is validated on tasks requiring detailed spatial reasoning, demonstrating a significant improvement over existing visual-language models without fine-tuning.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia
    - 📅 Date: October 7, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [reinforcement learning], [UI task automation], [instruction grounding]
    - 📖 TLDR: This paper introduces a multimodal model, termed RUIG (Reinforced UI Instruction Grounding), for automating UI tasks through natural language instructions. By leveraging a pixel-to-sequence approach, the model directly decodes UI element locations from screenshots based on user commands, removing the need for metadata like element coordinates. The framework uses a transformer-based encoder-decoder setup optimized through reinforcement learning to improve spatial accuracy. This novel approach outperforms prior methods, offering a generalized solution for UI task automation.

- [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://proceedings.neurips.cc/paper_files/paper/2022/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html)
    - Shunyu Yao, Howard Chen, John Yang, Karthik Narasimhan
    - 🏛️ Institutions: Princeton University
    - 📅 Date: July 2022
    - 📑 Publisher: NeurIPS 2022
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [e-commerce web interaction], [language grounding]
    - 📖 TLDR: This paper introduces **WebShop**, a simulated web-based shopping environment with over 1 million real-world products and 12,087 annotated instructions. It allows language agents to navigate, search, and make purchases based on natural language commands. The study explores how agents handle compositional instructions and noisy web data, providing a robust environment for reinforcement learning and imitation learning. The best models show effective sim-to-real transfer on websites like Amazon, illustrating WebShop’s potential for training grounded agents.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://aclanthology.org/2021.naacl-main.80/)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - 🏛️ Institutions: Stanford University, Samsung Research
    - 📅 Date: March 30, 2021
    - 📑 Publisher: NAACL 2021
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [grounding], [task automation], [open-domain instructions], [RUSS]
    - 📖 TLDR: This paper introduces RUSS (Rapid Universal Support Service), a framework designed to interpret and execute open-domain, step-by-step web instructions automatically. RUSS uses a BERT-LSTM model for semantic parsing into a custom language, ThingTalk, which allows the system to map language to actions across various web elements. The framework, including a dataset of instructions, facilitates agent-based web support task automation by grounding natural language to interactive commands.

- [Mapping Natural Language Instructions to Mobile UI Action Sequences](https://aclanthology.org/2020.acl-main.729)
    - Yang Li, Jiacong He, Xin Zhou, Yuan Zhang, Jason Baldridge
    - 🏛️ Institutions: Google Research
    - 📅 Date: July 2020
    - 📑 Publisher: ACL 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile UI automation], [natural language instructions], [action grounding], [RicoSCA]
    - 📖 TLDR: This paper introduces a method for grounding natural language instructions to mobile UI actions, aiming to automate mobile task execution through user interface manipulation. It introduces three key datasets: **PixelHelp** for task instruction-performance mappings on a Pixel emulator, **AndroidHowTo** for detailed phrase extraction, and **RicoSCA** for synthetic UI command training. The system utilizes a Transformer model to extract action phrase tuples, aligning them to UI elements with contextual screen positioning. Achieving over 70% accuracy in task completion, this approach is foundational for natural language-driven mobile UI automation.
