- [Rethinking Token Pruning for Historical Screenshots in GUI Visual Agents: Semantic, Spatial, and Temporal Perspectives](https://arxiv.org/abs/2603.26041)
    - Daiqiang Li, Zihao Pan, Zeyu Zhang, Ronghao Chen, Huacan Wang, Honggang Chen, Haiyun Jiang
    - 🏛️ Institutions: Sichuan University, Sun Yat-sen University, Australian National University, Peking University, University of Chinese Academy of Sciences
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [token pruning], [historical screenshots], [random pruning], [recency effect], [empirical study]
    - 📖 TLDR: This paper studies token pruning for historical GUI screenshots and finds that background regions still carry useful state-transition cues, random pruning preserves spatial structure surprisingly well, and allocating larger token budgets to recent screenshots keeps performance nearly unchanged while reducing cost.

- [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](https://arxiv.org/abs/2603.26211)
    - Shrinidhi Kumbhar, Haofu Liao, Srikar Appalaraju, Kunwar Yashraj Singh
    - 🏛️ Institutions: Arizona State University, Amazon (AWS Agentic AI)
    - 📅 Date: March 27, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [diffusion models], [hybrid masking], [bounding-box prediction], [LLaDA-V], [cross-platform]
    - 📖 TLDR: This paper adapts the discrete diffusion model LLaDA-V to GUI grounding and proposes a hybrid masking schedule for bounding-box prediction. Across web, desktop, and mobile benchmarks, the diffusion model outperforms its linear-masked variant and remains competitive with autoregressive VLMs.

- [GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks](https://arxiv.org/abs/2603.25864)
    - Saelyne Yang, Jaesang Yu, Yi-Hao Peng, Kevin Qinghong Lin, Jae Won Cho, Yale Song, Juho Kim
    - 🏛️ Institutions: KAIST, Carnegie Mellon University, University of Oxford, Konkuk University, Google Inc., SkillBench
    - 📅 Date: March 26, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [collaborative assistance], [behavior state detection], [intent prediction], [help prediction], [think-aloud data], [GUIDE]
    - 📖 TLDR: GUIDE studies collaborative GUI assistance rather than pure task automation, using 67.5 hours of think-aloud recordings from 120 novice users across 10 software applications. It benchmarks behavior-state detection, intent prediction, and help prediction, and shows that current multimodal models still struggle to infer what users are doing and when intervention would be useful.

- [CAPTCHA Solving for Native GUI Agents: Automated Reasoning-Action Data Generation and Self-Corrective Training](https://arxiv.org/abs/2603.23559)
    - Yuxi Chen, Haoyu Zhai, Chenkai Wang, Rui Yang, Lingming Zhang, Gang Wang, Huan Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign
    - 📅 Date: March 23, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [CAPTCHA], [reasoning-action data generation], [self-correction], [native GUI agent], [ReCAP]
    - 📖 TLDR: ReCAP is a native GUI agent specialized for interactive CAPTCHA solving. It builds a seven-type CAPTCHA environment, generates large-scale reasoning-action trajectories plus self-correction data from failed attempts, and improves success from about 30% to 80% without sacrificing general GUI-agent performance.

- [Seed1.8 Model Card: Towards Generalized Real-World Agency](https://arxiv.org/abs/2603.20633)
    - Bytedance Seed
    - 🏛️ Institutions: ByteDance Seed
    - 📅 Date: March 21, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI], [Search]
    - 🔑 Key: [foundation model], [generalist agency], [tool use], [code execution], [GUI interaction], [Seed1.8]
    - 📖 TLDR: Seed1.8 is a foundation model for generalized real-world agency that unifies search, code generation and execution, and GUI interaction under one agentic interface. The model card emphasizes strong language-vision performance plus latency- and cost-aware inference modes for deployment.

- [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191)
    - Zehao Li, Zhenyu Wu, Yibo Zhao, Bowen Yang, Jingjing Xie, Zhaoyang Liu, Zhoumianze Liu, Kaiming Jin, Jianze Liang, Zonglin Li, Feng Wu, Bowen Zhou, Zun Wang, Zichen Ding
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory, CUHK MMLab, The Hong Kong University of Science and Technology, National University of Singapore
    - 📅 Date: March 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reward model], [reinforcement learning], [critic framework], [OmniGUIRewardBench], [milestone decomposition], [OS-Themis]
    - 📖 TLDR: OS-Themis is a scalable critic framework for GUI reward modeling that breaks trajectories into verifiable milestones and audits the evidence chain before issuing a verdict. It improves AndroidWorld training and filtering loops and introduces OmniGUIRewardBench as a cross-platform benchmark for GUI outcome rewards.

- [FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair](https://arxiv.org/abs/2603.17826)
    - Ruize Ma, Yilei Jiang, Shilin Zhang, Zheng Ma, Yi Feng, Vincent Ng, Zhi Wang, Xiangyu Yue, Chuanyi Li, Lewei Lu
    - 🏛️ Institutions: Nanjing University, SenseTime, The Chinese University of Hong Kong, University of Texas at Dallas
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multimodal program repair], [software engineering], [program repair], [failure memory], [visual grounding], [SWE-bench Multimodal], [FailureMem]
    - 📖 TLDR: FailureMem is a multimodal automated program repair framework for settings where repair requires joint reasoning over code, issue text, and GUI screenshots. It combines hybrid workflow-agent control, region-level visual grounding, and a Failure Memory Bank that converts failed repair attempts into reusable guidance, improving resolved rate over GUIRepair on SWE-bench Multimodal.

- [AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement](https://arxiv.org/abs/2603.17441)
    - Siqi Pei, Liang Tang, Tiaonan Duan, Long Chen, Shuxian Li, Kaer Huang, Yanzhe Jing, Yiqiang Yan, Bo Zhang, Chenghao Jiang, Borui Zhang, Jiwen Lu
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [instruction refinement], [adaptive zoom], [GRPO], [bounding-box prediction], [AdaZoom-GUI]
    - 📖 TLDR: AdaZoom-GUI targets two concrete GUI-grounding bottlenecks: ambiguous natural-language instructions and tiny UI elements in high-resolution screenshots. It combines instruction rewriting with a conditional second-stage zoom-in pass and reports state-of-the-art grounding performance among comparable model sizes.

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
    - 🏛️ Institutions: McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [guardrail], [visual confused deputy], [TOCTOU], [grounding errors], [dual-channel contrastive classification]
    - 📖 TLDR: This paper reframes perception failures in GUI agents as a security problem rather than just a performance issue, formalizing the visual confused deputy where misperceived UI state causes privileged actions on the wrong target. It then proposes a dual-channel guardrail that separately checks the visual target and the agent's textual reasoning to block unsafe executions.

- [Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements](https://arxiv.org/abs/2603.14448)
    - Ziwei Liu, Tao Feng, Borui Kang, Yanbing Yang, Jun Luo
    - 🏛️ Institutions: Department of Computer Science and Technology, Sichuan University, Department of Computer Science and Technology, Tsinghua University, School of Computer Science, Nanjing University, College of Computing and Data Science, Nanyang Technological University
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [training-free], [inference scaling], [ZoomUI], [instruction rewriting], [progressive zooming]
    - 📖 TLDR: ZoomUI is a training-free GUI grounding method built on the idea that complex interfaces can be decomposed into simpler visual elements that generic MLLMs already understand. It rewrites instructions into element-level visual descriptions and progressively zooms onto candidate UI regions, reaching or surpassing fine-tuned baselines without additional training.

- [Adaptive Vision-Language Model Routing for Computer Use Agents](https://arxiv.org/abs/2603.12823)
    - Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
    - 🏛️ Institutions: vLLM Semantic Router Project, MBZUAI, McGill University, AMD, Red Hat
    - 📅 Date: March 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [VLM routing], [cost-accuracy tradeoff], [semantic routing], [OpenClaw], [AVR], [guardrail escalation]
    - 📖 TLDR: AVR inserts a semantic routing layer between a computer-use agent and a pool of VLMs, selecting the cheapest model that satisfies a target reliability threshold for each action. It projects up to 78% inference-cost reduction while staying close to all-large-model performance, and can escalate risky actions when combined with the Visual Confused Deputy guardrail.

- [Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291)
    - Sibo Zhu, Wenyi Wu, Kun Zhou, Stephen Wang, Biwei Huang
    - 🏛️ Institutions: University of California, San Diego, Abel.ai
    - 📅 Date: March 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [memory], [graph-based retrieval], [self-evolving memory], [HyMEM], [multi-hop retrieval]
    - 📖 TLDR: HyMEM is a graph-based memory system for GUI agents that couples symbolic nodes with continuous trajectory embeddings, supports multi-hop retrieval, and updates itself over time. It substantially boosts open-source 7B/8B GUI agents and can match or surpass stronger closed-source models on several benchmarks.

- [SlowBA: An efficiency backdoor attack towards VLM-based GUI agents](https://arxiv.org/abs/2603.08316)
    - Junxian Li, Tu Lan, Haozhen Tan, Yan Meng, Haojin Zhu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [backdoor attack], [response latency], [reward-level backdoor injection], [popup trigger], [security], [SlowBA]
    - 📖 TLDR: SlowBA studies a backdoor attack on VLM-based GUI agents that targets response efficiency rather than action correctness, using realistic pop-up triggers to induce excessively long reasoning chains. Its two-stage reward-level backdoor injection stays stealthy, preserves task accuracy, and substantially increases latency under trigger conditions.

- [CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning](https://arxiv.org/abs/2603.02951)
    - Zhenquan Yao, Zitong Huang, Yihan Zeng, Jianhua Han, Hang Xu, Chun-Mei Feng, Jianwei Ma, Wangmeng Zuo
    - 🏛️ Institutions: Harbin Institute of Technology, Huawei Noah's Ark Lab, University College Dublin, Peking University
    - 📅 Date: March 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [gradient surgery], [policy entropy], [AndroidControl-CL], [CGL]
    - 📖 TLDR: CGL studies continual GUI learning under app updates, combining supervised adaptation with reinforcement fine-tuning to retain prior interaction skills. It uses policy-entropy-guided SFT weighting and gradient surgery against GRPO anchor gradients, and introduces AndroidControl-CL to benchmark continual adaptation without catastrophic forgetting.

- [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190)
    - Rui Yang, Qianhui Wu, Zhaoyang Wang, Hanyang Chen, Ke Yang, Hao Cheng, Huaxiu Yao, Baoling Peng, Huan Zhang, Jianfeng Gao, Tong Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, Microsoft, University of North Carolina at Chapel Hill
    - 📅 Date: February 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [post-training], [reinforcement learning], [action-aware supervision], [partial verifiability], [GUI reasoning dataset], [GUI-Libra]
    - 📖 TLDR: GUI-Libra is a post-training recipe for native GUI agents that combines curated reasoning data, action-aware supervised fine-tuning, and partially verifiable RL. It targets the mismatch between chain-of-thought reasoning and grounding, and improves both step-level accuracy and end-to-end task completion on web and mobile benchmarks.

- [ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502)
    - Hongbin Zhong, Fazle Faisal, Luis França, Tanakorn Leesatapornwongsa, Adriana Szekeres, Kexin Rong, Suman Nath
    - 🏛️ Institutions: Georgia Institute of Technology, Microsoft Research
    - 📅 Date: February 24, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [programmatic planning], [state machine memory], [crawling agent], [execution agent], [re-grounding fallback], [ActionEngine]
    - 📖 TLDR: ActionEngine shifts GUI agents from reactive step-by-step execution to programmatic planning by building an updatable state-machine memory and synthesizing executable programs from it. Its crawler-plus-executor design reaches 95% success on WebArena Reddit tasks while greatly reducing cost and latency.

- [Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision](https://arxiv.org/abs/2602.14276)
    - A. Said Gurbuz, Sunghwan Hong, Ahmed Nassar, Marc Pollefeys, Peter Staar
    - 🏛️ Institutions: IBM Research, ETH Zurich, KAIST
    - 📅 Date: February 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [dataset], [screen parsing], [dense supervision], [ScreenParse], [UI understanding]
    - 📖 TLDR: This paper argues that sparse grounding supervision is insufficient for GUI understanding and introduces ScreenParse, a large-scale densely annotated screen-parsing dataset. It provides complete UI-element supervision across web screenshots to support richer grounding and UI understanding models.

- [Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization](https://arxiv.org/abs/2602.13653)
    - Yibo Wang, Guangda Huzhang, Yuwei Hu, Yu Xia, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Lijun Zhang
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, Nanjing University, Ovis Team, Alibaba Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [agentic-Q estimation], [step-wise policy optimization], [Ovis2.5-9B], [GUI navigation], [grounding]
    - 📖 TLDR: This paper trains GUI agents with an agentic-Q model that estimates each action's contribution to task completion and a step-wise policy optimization routine decoupled from online interaction. The design keeps data collection manageable while stabilizing updates and improving navigation and grounding performance.

- [How Smart Is Your GUI Agent? A Framework for the Future of Software Interaction](https://arxiv.org/abs/2602.11514)
    - Sidong Feng, Chunyang Chen
    - 🏛️ Institutions: The Chinese University of Hong Kong (Shenzhen), Technical University of Munich
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [autonomy levels], [taxonomy], [trustworthy AI], [software interaction], [GUI Agent Autonomy Levels], [conceptual framework]
    - 📖 TLDR: This paper is a conceptual framing proposal rather than a new agent system. It introduces GUI Agent Autonomy Levels, a six-level taxonomy for describing capability, responsibility, and risk, with the goal of giving the field a clearer language for benchmarking and trustworthy deployment.

- [Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2602.11858)
    - Lai Wei, Liangbo He, Jun Lan, Lingzhong Dong, Yutong Cai, Siyuan Li, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Ant Group, Zhongguancun Academy, Shanghai Innovation Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [knowledge distillation], [fine-grained perception], [region-to-image distillation], [ZoomBench], [training data generation], [multimodal perception]
    - 📖 TLDR: This paper proposes Region-to-Image Distillation, which teaches a model to internalize zoom-in behavior without requiring explicit crop-and-reason inference at test time. It also introduces ZoomBench and shows stronger fine-grained perception on both perception and GUI-agent benchmarks.

- [See, Plan, Snap: Evaluating Multimodal GUI Agents in Scratch](https://arxiv.org/abs/2602.10814)
    - Xingyi Zhang, Yulei Ye, Kaifeng Huang, Wenhao Li, Xiangfeng Wang
    - 🏛️ Institutions: East China Normal University, Tongji University
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [ScratchWorld], [drag-and-drop], [block-based programming], [reasoning-acting gap], [scratch]
    - 📖 TLDR: ScratchWorld evaluates multimodal GUI agents on Scratch program construction tasks that require fine-grained drag-and-drop manipulation. The benchmark exposes a large gap between high-level planning success and low-level GUI execution.

- [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662)
    - Deyang Jiang, Jing Huang, Xuanle Zhao, Lei Chen, Liming Zheng, Fanfan Liu, Haibo Qiu, Peng Shi, Zhixiong Zeng
    - 🏛️ Institutions: Meituan
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [planning], [multi-agent], [tree-structured evolution], [trajectory generation], [TreeCUA], [TreeCUA-DPO]
    - 📖 TLDR: TreeCUA tackles the scaling bottleneck in GUI planning by organizing exploration trajectories as reusable tree structures with verification, summarization, and evaluation. The resulting data supports TreeCUA-DPO, which improves planning quality and out-of-domain generalization.

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL], [curriculum learning]
    - 📖 TLDR: ACuRL studies continual adaptation for computer-use agents in changing environments without human demonstrations. It combines autonomous curriculum generation with CUAJudge-based evaluation to improve both within-environment and cross-environment adaptation while limiting forgetting.

- [POINTS-GUI-G: GUI-Grounding Journey](https://arxiv.org/abs/2602.06391)
    - Zhongyin Zhao, Yuan Liu, Yikun Liu, Haicheng Wang, Le Tian, Xiao Zhou, Yangxiu You, Zilin Yu, Yang Yu, Jie Zhou
    - 🏛️ Institutions: WeChat AI
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [data engineering], [vision encoder training], [verifiable rewards], [POINTS-GUI-G-8B], [ScreenSpot-pro]
    - 📖 TLDR: POINTS-GUI-G studies how to build strong GUI grounding from a base model without strong initial spatial grounding. It attributes gains to multi-source data engineering, improved vision-encoder training, and RL with verifiable rewards, producing competitive results across several grounding benchmarks.

- [Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion](https://arxiv.org/abs/2602.06351)
    - Longhui Ma, Di Zhao, Siwei Wang, Zhao Lv, Miao Wang
    - 🏛️ Institutions: College of Computer Science and Technology, National University of Defense Technology, Intelligent Game and Decision Lab, Academy of Military Sciences
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [multimodal fusion], [attention mechanism], [training-free], [OCR], [Trifuse]
    - 📖 TLDR: Trifuse is a training-free GUI grounding method that fuses MLLM attention, OCR text, and icon caption signals through a consensus-based fusion strategy. It improves grounding across multiple benchmarks without task-specific fine-tuning.

- [SVRepair: Structured Visual Reasoning for Automated Program Repair](https://arxiv.org/abs/2602.06090)
    - Xiaoxuan Tang, Jincheng Wang, Liwei Luo, Jingxuan Xu, Sheng Zhou, Dajun Chen, Wei Jiang, Yong Li
    - 🏛️ Institutions: Ant Group, Zhejiang Key Laboratory of Accessible Perception and Intelligent Systems, Zhejiang University
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI understanding], [multimodal LLM], [program repair], [scene graph], [visual reasoning], [coding agent]
    - 📖 TLDR: SVRepair is a multimodal automated program repair framework that fine-tunes a vision-language model to convert GUI visual artifacts (screenshots, control-flow graphs) into structured semantic scene graphs, enabling a coding agent to localize faults and synthesize patches with state-of-the-art results on SWE-Bench M, MMCode, and CodeVision benchmarks.

- [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995)
    - Sizhe Tang, Rongqian Chen, Tian Lan
    - 🏛️ Institutions: The George Washington University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time compute], [tree search], [MCTS], [alpha-UCT], [OSWorld], [Agent Alpha]
    - 📖 TLDR: Agent Alpha applies step-level MCTS with alpha-UCT exploration, comparison-based evaluation, and diversity-aware expansion to computer-use agents. It improves OSWorld performance substantially over trajectory-level sampling under similar compute.

- [LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios](https://arxiv.org/abs/2602.03255)
    - Tianyu Chen, Chujia Hu, Ge Gao, Ruofeng Yu, Yao Lu
    - 🏛️ Institutions: ShanghaiTech University, Shanghai Artificial Intelligence Laboratory, Rice University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [MCP], [long-horizon planning], [LLM agent]
    - 📖 TLDR: LPS-Bench is a benchmark evaluating the planning-time safety awareness of MCP-based computer-use agents under long-horizon tasks, covering 65 scenarios across 7 task domains and 9 risk types with both benign and adversarial interactions, revealing substantial safety deficiencies in existing agents.

- [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725)
    - Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, The Chinese University of Hong Kong, Shenzhen
    - 📅 Date: February 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [guardrail], [world model], [risk prediction], [safety], [long-horizon risk], [SafePred]
    - 📖 TLDR: SafePred is a predictive guardrail that uses a world model to simulate future states and assess delayed risk before a computer-use agent acts. It targets long-horizon hazards that reactive safety filters tend to miss.

- [Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction](https://arxiv.org/abs/2602.00575)
    - Chaoqun Cui, Jing Huang, Shijing Wang, Liming Zheng, Qingchao Kong, Zhixiong Zeng
    - 🏛️ Institutions: MAIS, Institute of Automation, Chinese Academy of Sciences, School of Artificial Intelligence, University of Chinese Academy of Sciences, Meituan, School of Computer Science & Technology, Beijing Jiaotong University
    - 📅 Date: January 31, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reward modeling], [verification], [proactive interaction], [VAGEN], [OSWorld], [AndroidWorld]
    - 📖 TLDR: VAGEN turns GUI-agent verification into an active interaction problem, using a verifier agent to probe the environment for evidence of task completion instead of relying on passive judgment. This substantially improves verification accuracy on OSWorld and AndroidWorld.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548)
    - Xiaoce Wang, Guibin Zhang, Junzhe Li, Jinzhe Tu, Chun Li, Ming Li
    - 🏛️ Institutions: Department of Computer Science, Tsinghua University, National University of Singapore, Peking University, MSU-BIT-SMBU Joint Research Center of Applied Mathematics, Shenzhen MSU-BIT University, Guangming Laboratory
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [tool use], [tokenization], [curriculum learning], [visual grounding], [data efficiency], [ToolTok]
    - 📖 TLDR: ToolTok treats GUI operations as paths over learnable tool tokens with semantic anchoring and curriculum learning. This makes GUI agents more efficient and generalizable, reaching competitive performance with far less training data than other post-training methods.

- [Where Not to Learn: Prior-Aligned Training with Subset-based Attribution Constraints for Reliable Decision-Making](https://arxiv.org/abs/2602.07008)
    - Ruoyu Chen, Shangquan Sun, Xiaoqing Guo, Sanyi Zhang, Kangwei Liu, Shiming Liu, Zhangcheng Wang, Qunli Zhang, Hua Zhang, Xiaochun Cao
    - 🏛️ Institutions: Institute of Information Engineering, Chinese Academy of Sciences, University of Chinese Academy of Sciences, College of Computing and Data Science, Nanyang Technological University, Department of Computer Science, Hong Kong Baptist University, Communication University of China, Huawei, University of Science and Technology of China, School of Cyber Science and Technology, Shenzhen Campus of Sun Yat-sen University
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [training], [attribution], [subset-based attribution constraints], [human prior alignment], [reliability], [explainability]
    - 📖 TLDR: This paper proposes prior-aligned training with subset-based attribution constraints, penalizing models for relying on evidence that conflicts with human priors. It improves both accuracy and decision reasonability on image classification and GUI-agent click decision tasks.

- [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528)
    - Hongze Mi, Yibo Feng, WenJie Lu, Song Cao, Jinyuan Li, Yanming Li, Xuelin Zhang, Haotian Luo, Songyang Peng, He Cui, Tengfei Tian, Jun Fang, Hua Chai, Naiqiang Tan
    - 🏛️ Institutions: Didichuxing Co. Ltd, The Chinese University of Hong Kong, Shenzhen, Tianjin University, Sun Yat-sen University, Fudan University
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [memory system], [training-free], [self-regulating memory], [multi-app], [Darwinian Memory], [trajectory pruning]
    - 📖 TLDR: Darwinian Memory is a training-free memory system that treats agent memories as an evolving ecosystem, selecting and pruning trajectories through utility-driven competition. It improves success rate and execution stability on real-world multi-app GUI benchmarks.

- [SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization](https://arxiv.org/abs/2601.22491)
    - Jinyang Wu, Changpeng Yang, Yuhao Shen, Fangzhi Xu, Bolin Ni, Chonghua Liao, Yuchen Liu, Hongzhen Wang, Shuai Nie, Shuai Zhang, Haoran Luo, Jiaming Xu
    - 🏛️ Institutions: Tsinghua University, Xiaomi Corporation, Zhejiang University, Nanyang Technological University, Institute of Automation, Chinese Academy of Sciences
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [tiered rewards], [reward shaping], [GUI grounding], [planning], [SSL]
    - 📖 TLDR: SSL replaces binary verifier rewards with progressively amplified tiered rewards that distinguish higher- and lower-quality successful trajectories. Across GUI perception, short- and long-horizon planning, and reasoning benchmarks, it improves optimization stability and reaches up to 2.5x better sample efficiency than binary-reward baselines.

- [BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://arxiv.org/abs/2601.21352)
    - Ziyu Lu, Tengjin Weng, Yiying Yang, Yuhang Zhao, Xinxin Huang, Wenhao Jiang
    - 🏛️ Institutions: Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shenzhen University, Guangdong University of Technology
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [backtracking], [DFS planning], [task tracking], [error recovery], [OSWorld], [BEAP-Agent]
    - 📖 TLDR: BEAP-Agent formulates long-horizon GUI execution as depth-first search and adds explicit multi-level backtracking when the agent commits to a wrong exploration branch. Its Planner, Executor, and Tracker jointly support state rollback and task updates, improving recovery on OSWorld.

- [Continual GUI Agents](https://arxiv.org/abs/2601.20732)
    - Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng
    - 🏛️ Institutions: Department of Computer Science and Technology, Tsinghua University, College of Computer Science, Zhejiang University, Photogrammetry and Remote Sensing Lab, ETH Zurich, College of Computer Science, Beijing University of Posts and Telecommunications
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement fine-tuning], [domain shift], [resolution shift], [GUI-AiF]
    - 📖 TLDR: This paper defines continual GUI agents as agents that must keep grounding accurately while interface domains and resolutions shift over time. It introduces GUI-AiF, a reinforcement fine-tuning method with anchoring-point and anchoring-region rewards, and reports stronger continual-domain and continual-resolution performance than prior baselines.

- [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197)
    - Shaokang Wang, Pei Fu, Ruoceng Zhang, Shaojie Zhang, Xiuwen Xi, Jiahui Yang, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [critic model], [test-time scaling], [data flywheel], [Intuitive Critic Model], [GAIA]
    - 📖 TLDR: GAIA trains an Intuitive Critic Model that judges the immediate correctness of candidate GUI actions before execution. It then uses a data flywheel that recycles agent-generated positive and negative action samples to iteratively improve the critic, yielding better test-time performance for both open-source and closed-source GUI agents.

- [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE)
    - Bin Kang, Shaoguo Wen, Yifei Bi, Shunlong Wu, Xinbin Yuan, Rui Shao, Junle Wang, Zhuotao Tian
    - 🏛️ Institutions: Chengdu Institute of Computer Applications, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Tencent Turing Lab, Georgia Institute of Technology, Tsinghua University, Nankai University, Shenzhen Loop Area Institute
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [long-horizon tasks], [reflection], [rollback], [LongGUIBench], [LongHorizonUI]
    - 📖 TLDR: LongHorizonUI targets error accumulation in long-horizon GUI control by combining indexed multimodal perception, structured reflective decision-making, and rollback-based compensatory execution. It also introduces LongGUIBench for tasks longer than 15 steps across games and complex applications, and reports substantial gains on long-horizon evaluation while staying competitive on public benchmarks.

- [GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents](https://arxiv.org/abs/2601.18842)
    - Yanxi Wang, Zhiling Zhang, Wenbo Zhou, Weiming Zhang, Jie Zhang, Qiannan Zhu, Yu Shi, Shuxin Zheng, Jiyan He
    - 🏛️ Institutions: Beijing Normal University, Zhongguancun Academy, University of Science and Technology of China, A*STAR, Zhongguancun Institution of Artificial Intelligence
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [privacy recognition], [privacy protection], [privacy grounding], [GUIGuard], [GUIGuard-Bench]
    - 📖 TLDR: GUIGuard formulates privacy-preserving GUI automation as privacy recognition, privacy protection, and protected task execution. It also introduces GUIGuard-Bench, a cross-platform benchmark with 630 trajectories and 13,830 screenshots annotated for region-level privacy grounding, risk level, privacy category, and task necessity, and shows that current models still recognize private content very poorly.

- [MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux](https://arxiv.org/abs/2601.13060)
    - Zecheng Li, Zhihui Cao, Wenke Huang, Yudong Zhang, Keying Qi, Rui Wang, Zeyu Zheng, Jian Zhao, Hao Zhu, Hengxin Wu, Yuran Wang, Guitao Fan, Guokun Wu, Yicong Liu, Zhilin Gao, Haikun Xu, He Yang, Minqi Xiang, Xingyu Liu, Zuojian Wang
    - 🏛️ Institutions: Honor Device Co., Ltd.
    - 📅 Date: January 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reward model], [multi-agent system], [data construction], [data reflux], [MagicGUI-RMS]
    - 📖 TLDR: MagicGUI-RMS combines a domain-specific reward model with a general-purpose reward model to score GUI trajectories, propose corrections, and feed improved data back into later training rounds. It also introduces an automated reward-data construction pipeline and reports gains in task accuracy and behavioral robustness.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: University of Science and Technology of China, Institute of Artificial Intelligence (TeleAI), China Telecom, Shanghai Innovation Institute, Shanghai Jiao Tong University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [active perception], [tool-augmented perception], [ScreenSpot-pro], [GUI-Eyes]
    - 📖 TLDR: GUI-Eyes frames GUI grounding as active perception, letting the agent learn when and how to call tools such as cropping and zooming inside a two-stage reasoning process. It pairs that policy with a spatially continuous reward for tool use and reaches 44.8% grounding accuracy on ScreenSpot-Pro using only 3k labeled samples.

- [Compress to Focus: Efficient Coordinate Compression for Policy Optimization in Multi-Turn GUI Agents](https://arxiv.org/abs/2601.11631)
    - Yurun Song, Jiong Yin, Rongjunchen Zhang, Ian G. Harris
    - 🏛️ Institutions: HiThink Research, University of California, Irvine, Hangzhou Dianzi University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [policy optimization], [coordinate compression], [Coordinate-Aware Spatial Compression], [distance-based advantage], [CCPO]
    - 📖 TLDR: CCPO tackles context inflation in multi-turn GUI agents by compressing historical screenshots around task-relevant coordinates collected across rollouts. Its Coordinate-Aware Spatial Compression and distance-based advantage improve both compression quality and grounding, reaching state-of-the-art results with up to 55% token compression and 3.8x training speedup.

- [V2P: Visual Attention Calibration for GUI Grounding via Background Suppression and Center Peaking](https://arxiv.org/abs/2601.06899)
    - Jikai Chen, Long Chen, Dong Wang, Qinglin Su, Zhixuan Chu, Bingguang Hao, Leilei Gan, Chenyi Zhuang, Jinjie Gu
    - 🏛️ Institutions: Zhejiang University, Inclusion AI, Ant Group
    - 📅 Date: January 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [visual attention], [background suppression], [Fitts' law], [V2P]
    - 📖 TLDR: V2P improves attention-based GUI grounding by suppressing irrelevant background regions and using a Fitts’ Law-inspired Gaussian peak to emphasize an element’s actionable center over its edges. The paper reports 92.4% on ScreenSpot-v2 and 52.5% on ScreenSpot-Pro, with ablations confirming both components matter.

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu
    - 🏛️ Institutions: Nanjing University, Peking University, Microsoft Research Asia
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [RLVR], [off-policy assimilation], [BEPA], [OSWorld]
    - 📖 TLDR: BEPA improves end-to-end GUI-agent training with verifiable rewards by turning scarce off-policy expert traces into policy-aligned guidance through self-rolled reachable trajectories and a dynamically updated per-task cache. On OSWorld-Verified it raises UI-TARS-1.5-7B from 22.87% to 32.13%, with additional gains on MMBench-GUI and Online-Mind2Web.

- [Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning](https://arxiv.org/abs/2601.03641)
    - Zheng Wu, Xingyu Lou, Xinbei Ma, Yansi Li, Weiwen Liu, Weinan Zhang, Jun Wang, Zhuosheng Zhang
    - 🏛️ Institutions: School of Computer Science, Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [continual learning], [parameter fusion], [catastrophic forgetting], [geometric consensus], [Agent-Dice]
    - 📖 TLDR: Agent-Dice addresses the stability-plasticity dilemma in agent continual learning by separating shared knowledge from task-specific interference during parameter fusion. Its two-stage method combines geometric consensus filtering with curvature-based importance weighting, and the paper reports strong continual-learning results for both GUI and tool-use agents.

- [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009)
    - Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu, Vineeth N Balasubramanian
    - 🏛️ Institutions: Indian Institute of Technology, Bombay, Indian Institute of Technology, Hyderabad
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [slow-fast reasoning], [visual grounding], [latent thinking], [adaptive perception], [iSHIFT]
    - 📖 TLDR: iSHIFT is a 2.5B GUI agent that combines latent thinking with perception-control tokens so it can switch between a fast global mode and a slower grounding-heavy mode. The paper positions this as a way to allocate reasoning depth and visual focus adaptively while still matching state-of-the-art results on multiple GUI benchmarks.

- [GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection](https://arxiv.org/abs/2512.09396)
    - Zishu Wei, Qixiang Ma, Xavier Hu, Yuhang Liu, Hui Zang, Yudong Zhao, Tao Wang, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Huawei Technologies Ltd.
    - 📅 Date: December 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multi-agent], [grounding], [reasoning], [reflection], [benchmark]
    - 📖 TLDR: GAIR is a multi-agent GUI automation framework that uses a general-purpose MLLM to jointly reason over information gathered by multiple GUI-specific models, with a group reflection mechanism that drives specialized models to collect more targeted information when the decision-maker determines insufficient evidence, achieving state-of-the-art results on GUI benchmarks like ScreenSpot and UI-I2E-Bench with only 7B models.

- [Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning](https://arxiv.org/abs/2512.09706)
    - Kaichen He, Zihao Wang, Muyao Li, Anji Liu, Yitao Liang
    - 🏛️ Institutions: Peking University, National University of Singapore
    - 📅 Date: December 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [heterogeneous action space], [multi-turn GRPO], [Minecraft agent], [cross-level actions], [LLM agent]
    - 📖 TLDR: CrossAgent is a unified agentic model trained via supervised fine-tuning and multi-turn Group Relative Policy Optimization (GRPO) that dynamically switches between heterogeneous action spaces (APIs, GUI events, low-level commands) within a single trajectory, achieving state-of-the-art performance on 800+ Minecraft tasks by adaptively balancing high-level efficiency with low-level precision.

- [MVP: Multiple View Prediction Improves GUI Grounding](https://arxiv.org/abs/2512.08529)
    - Yunzhu Zhang, Zeyu Pan, Zhengwen Zeng, Shuheng Shen, Changhua Meng, Linchao Zhu
    - 🏛️ Institutions: College of Computer Science and Technology, Zhejiang University, College of Computer Science and Technology, Hangzhou Dianzi University, Venus Team, Ant Group
    - 📅 Date: December 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [training-free], [multi-view inference], [test-time augmentation], [coordinate clustering]
    - 📖 TLDR: MVP is a training-free framework that improves GUI grounding accuracy by aggregating coordinate predictions from multiple attention-guided cropped views of a screenshot and selecting the centroid of the densest spatial cluster, significantly boosting performance of existing grounding models on benchmarks like ScreenSpot-Pro.

- [Single-Agent Scaling Fails Multi-Agent Intelligence: Towards Foundation Models with Native Multi-Agent Intelligence](https://arxiv.org/abs/2512.08743)
    - Shuyue Hu, Haoyang Yan, Yiqun Zhang, Yang Chen, Dongzhan Zhou, Lei Bai
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory
    - 📅 Date: December 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multi-agent systems], [foundation models], [LLM], [benchmark], [scaling], [survey]
    - 📖 TLDR: This paper demonstrates through extensive empirical evaluation across 41 LLMs and 7 benchmarks that scaling single-agent performance does not automatically yield robust multi-agent intelligence, and outlines key research directions for building foundation models with native multi-agent capabilities including understanding, planning, communication, and adaptation.

- [Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding](https://arxiv.org/abs/2512.05941)
    - Zhiyuan Jiang, Shenghao Xie, Wenyi Li, Wenqiang Zu, Peihang Li, Jiahao Qiu, Siqi Pei, Lei Ma, Tiejun Huang, Mengdi Wang, Shilong Liu
    - 🏛️ Institutions: Xi’an Jiaotong University, Princeton University, Peking University, University of Chinese Academy of Sciences, The University of Hong Kong, Michigan State University
    - 📅 Date: December 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [benchmark], [training-free], [zoom], [test-time scaling], [visual grounding]
    - 📖 TLDR: Proposes ZoomClick, a training-free method that leverages zoom as a prior for GUI grounding to dynamically focus on screen regions and switch context, achieving state-of-the-art results on benchmarks like ScreenSpot-Pro, and introduces GUIZoom-Bench for evaluating model adaptability to zoom.

- [GUI Exploration Lab: Enhancing Screen Navigation in Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2512.02423)
    - Haolong Yan, Yeqing Shen, Xin Huang, Jia Wang, Kaijun Tan, Zhixuan Liang, Hongxin Li, Zheng Ge, Osamu Yoshie, Si Li, Xiangyu Zhang, Daxin Jiang
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, StepFun, Waseda University, Institute of Automation, Chinese Academy of Sciences
    - 📅 Date: December 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [screen navigation], [reinforcement learning], [simulation environment], [multi-turn RL], [exploration strategy]
    - 📖 TLDR: GUI Exploration Lab is a simulation environment engine for GUI agent navigation research that enables flexible composition of screens and navigation graphs; experiments show that supervised fine-tuning provides foundational knowledge, single-turn RL improves generalization, and multi-turn RL develops exploration strategies via trial and error, with findings validated on real-world benchmarks.

- [DrawingBench: Evaluating Spatial Reasoning and UI Interaction Capabilities of Large Language Models through Mouse-Based Drawing Tasks](https://arxiv.org/abs/2512.01174)
    - Hyunjun Kim, Sooyoung Ryu
    - 🏛️ Institutions: Independent
    - 📅 Date: December 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [spatial reasoning], [UI interaction], [LLM agent], [evaluation]
    - 📖 TLDR: DrawingBench is a verification framework that evaluates agentic LLMs' spatial reasoning and GUI interaction capabilities through mouse-based drawing tasks on a browser canvas, using 250 prompts with 8 objective criteria and multi-turn feedback, finding that specification clarity matters more than task complexity and external oversight outperforms self-correction.

- [HiconAgent: History Context-aware Policy Optimization for GUI Agents](https://arxiv.org/abs/2512.01763)
    - Xurui Zhou, Gongwei Chen, Yuquan Xie, Zaijing Li, Kaiwen Zhou, Shuai Wang, Shuo Yang, Zhuotao Tian, Rui Shao
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Huawei Noah’s Ark Lab
    - 📅 Date: December 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [history modeling], [policy optimization], [GUI navigation], [HiconAgent]
    - 📖 TLDR: This paper studies how GUI agents should use historical context during sequential decision making, arguing that naively including full history is both expensive and distracting. It introduces History Context-aware Policy Optimization, combining dynamic context sampling with anchor-guided history compression to train lightweight agents that use past observations and actions more effectively. The resulting HiconAgent-3B improves performance on benchmarks such as GUI-Odyssey, AndroidControl, and AITW while reducing FLOPs and inference cost.

- [MPR-GUI: Benchmarking and Enhancing Multilingual Perception and Reasoning in GUI Agents](https://arxiv.org/abs/2512.00756)
    - Ruihan Chen, Qiming Li, Xiaocheng Feng, Xiaoliang Yang, Weihong Zhong, Yuxuan Gu, Zekun Zhou, Bing Qin
    - 🏛️ Institutions: Harbin Institute of Technology, Peng Cheng Laboratory
    - 📅 Date: November 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [multilingual], [GUI understanding], [cross-lingual], [perception and reasoning], [LVLM]
    - 📖 TLDR: MPR-GUI introduces a multilingual fine-grained benchmark (MPR-GUI-Bench) for evaluating GUI agents' perception and reasoning capabilities across languages, and proposes GUI-XLI, a cross-lingual intervention method that improves multilingual GUI agent performance by 6.5% on average by manipulating hidden states at capability-related layers.

- [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235)
    - Zehao Deng, Tianjie Ju, Zheng Wu, Zhuosheng Zhang, Gongshen Liu
    - 🏛️ Institutions: School of Computer Science and Technology, Soochow University, School of Computer Science, Shanghai Jiao Tong University
    - 📅 Date: November 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multi-agent framework], [reinforcement learning], [long-horizon task planning], [state tracking], [task decomposition]
    - 📖 TLDR: This paper proposes CES, a multi-agent framework consisting of a Coordinator, Executor, and State Tracker, where high-level scheduling models are trained via execution-feedback reinforcement learning to improve long-horizon GUI automation by decoupling planning from low-level action execution.

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Zeyi Liao, Yadong Lu, Boyu Gou, Huan Sun, Ahmed Awadallah
    - 🏛️ Institutions: The Ohio State University, Microsoft Research, Redmond
    - 📅 Date: November 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [dataset], [benchmark], [text dragging], [multimodal LLM]
    - 📖 TLDR: This paper introduces GUI-Drag, a 161K-example dataset for text dragging in GUIs, and ScreenDrag, a benchmark with 5,333 examples, extending GUI grounding beyond click-only actions to support drag-based text selection and manipulation while maintaining click performance.

- [VideoAgentTrek: Computer Use Pretraining from Unlabeled Videos](https://arxiv.org/abs/2510.19488)
    - Dunjie Lu, Yiheng Xu, Junli Wang, Haoyuan Wu, Xinyuan Wang, Zekun Wang, Junlin Yang, Hongjin Su, Jixuan Chen, Junda Chen, Yuchen Mao, Jingren Zhou, Junyang Lin, Binyuan Hui, Tao Yu
    - 🏛️ Institutions: Google Cloud AI Research, The Ohio State University
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [pretraining], [video mining], [inverse dynamics], [tutorial videos], [VideoAgentTrek], [Video2Action]
    - 📖 TLDR: VideoAgentTrek turns unlabeled tutorial videos into large-scale computer-use pretraining data by detecting action events, recovering structured actions, and generating paired interaction traces. Mining 39,000 videos yields 1.52 million steps, and continued pretraining on this data materially improves both offline and online computer-use benchmarks.

- [Surfer 2: The Next Generation of Cross-Platform Computer Use Agents](https://arxiv.org/abs/2510.19949)
    - Mathieu Andreux, Märt Bakler, Yanael Barbier, Hamza Benchekroun, Emilien Biré, Antoine Bonnet, Riaz Bordie, Nathan Bout, Matthias Brunel, Aleix Cambray, Pierre-Louis Cedoz, Antoine Chassang, Gautier Cloix, Ethan Connelly, Alexandra Constantinou, Ramzi De Coster, Hubert de la Jonquiere, Aurélien Delfosse, Maxime Delpit, Alexis Deprez, Augustin Derupti, Mathieu Diaz, Shannon D'Souza, Julie Dujardin, Abai Edmund, Michael Eickenberg, Armand Fatalot, Wissem Felissi, Isaac Herring, Xavier Koegler, Erwan Le Jumeau de Kergaradec, Aurélien Lac, Maxime Langevin, Corentin Lauverjat, Antonio Loison, Avshalom Manevich, Axel Moyal, Axel Nguyen Kerbel, Marinela Parovic, Julien Revelle, Guillaume Richard, Mats Richter, Ronan Riochet, María Santos, Romain Savidan, Laurent Sifre, Maxime Theillard, Marc Thibault, Ivan Valentini, Tony Wu, Laura Yie, Kai Yuan, Jevgenij Zubovskij
    - 🏛️ Institutions: H Company
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [cross-platform]
    - 📖 TLDR: Surfer 2 is a unified visual-only cross-platform agent achieving state-of-the-art across web (97.1% WebVoyager, 69.6% WebArena), desktop (60.1% OSWorld), and mobile (87.1% AndroidWorld) without task-specific fine-tuning, via hierarchical context management, decoupled planning/execution, and self-verification with adaptive recovery.

- [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892)
    - Kai Mei, Jiang Guo, Shuaichen Chang, Mingwen Dong, Dongkyu Lee, Xing Niu, Jiarong Jiang
    - 🏛️ Institutions: Rutgers University, AWS Agentic AI
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [world model], [retrieval-augmented planning], [OSWorld], [WebArena], [r-WoM]
    - 📖 TLDR: This paper studies whether LLMs can reliably serve as world models for computer-use agents and finds that their simulations degrade sharply over long-horizon procedures despite reasonable short-range predictions. To address this, it proposes R-WoM, a retrieval-augmented world model that grounds planning with up-to-date external tutorials. R-WoM improves planning quality on OSWorld and WebArena, with especially strong gains on longer-horizon tasks where ungrounded simulation is most brittle.

- [GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding](https://arxiv.org/abs/2510.04039)
    - Bin Lei, Nuo Xu, Ali Payani, Mingyi Hong, Chunhua Liao, Yu Cao, Caiwen Ding
    - 🏛️ Institutions: University of Minnesota, Cisco Research, Lawrence Livermore National Labs
    - 📅 Date: October 05, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [tool use], [iterative refinement], [ScreenSpot-pro], [GUI-Spotlight]
    - 📖 TLDR: GUI-Spotlight is a GUI visual-grounding model that performs image-grounded reasoning by iteratively invoking specialized tools to narrow attention to the relevant screen region. The paper positions tool-driven focus refinement as the core mechanism and reports stronger ScreenSpot-Pro accuracy than prior 7B grounding models while using far less training data.

- [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670)
    - Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
    - 🏛️ Institutions: Microsoft Research AI Frontiers, Microsoft AI Red Team, University of California, Riverside, NVIDIA
    - 📅 Date: October 02, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [blind goal-directedness], [BLIND-ACT], [risk evaluation]
    - 📖 TLDR: This paper identifies Blind Goal-Directedness as a recurring failure mode in computer-use agents, where agents keep pursuing user goals despite infeasibility, ambiguity, or unsafe context. It introduces BLIND-ACT, a benchmark built on OSWorld to evaluate these subtle safety failures in realistic desktop environments. The results show high rates of blind goal pursuit across frontier CUAs, making the paper directly relevant to safety evaluation of GUI agents beyond prompt injection alone.

- [GUI-KV: Efficient GUI Agents via KV Cache with Spatio-Temporal Awareness](https://arxiv.org/abs/2510.00536)
    - Kung-Hsiang Huang, Haoyi Qiu, Yutong Dai, Caiming Xiong, Chien-Sheng Wu
    - 🏛️ Institutions: Salesforce AI Research, University of California, Los Angeles
    - 📅 Date: October 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [efficiency], [KV cache compression], [vision-language model], [attention sparsity], [training-free]
    - 📖 TLDR: GUI-KV is a training-free, plug-and-play KV cache compression method for GUI agents that exploits GUI-specific spatial saliency and temporal redundancy to reduce decoding FLOPs by 38.9% while matching or exceeding full-cache accuracy on standard benchmarks.

- [SCUBA: Salesforce Computer Use Benchmark](https://openreview.net/forum?id=bkjKnO9s7T)
    - Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: September 30, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [enterprise software], [CRM], [milestone evaluation], [SCUBA]
    - 📖 TLDR: SCUBA is a Salesforce-based computer-use benchmark covering 300 CRM task instances derived from real user interviews across administrator, sales, and service personas. It emphasizes realistic sandbox execution and milestone-level evaluation, and shows that enterprise workflows remain much harder than standard agent benchmarks, with large gaps between open and closed models even after demonstration augmentation.

- [Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents](https://arxiv.org/abs/2509.26539)
    - Zhen Yang, Zi-Yi Dou, Di Feng, Forrest Huang, Anh Nguyen, Keen You, Omar Attia, Yuhao Yang, Michael Feng, Haotian Zhang, Ram Ramrakhya, Chao Jia, Jeffrey Nichols, Alexander Toshev, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [chain-of-thought], [visual tool-use]
    - 📖 TLDR: This paper presents **Ferret-UI Lite**, a compact 3B end-to-end GUI agent designed for on-device deployment across mobile, web, and desktop. It introduces a mixed real and synthetic GUI dataset, a two-stage training pipeline combining supervised fine-tuning and reinforcement learning with verifiable rewards, and inference-time reasoning and visual cropping strategies. Ferret-UI Lite achieves strong grounding accuracy (91.6% on ScreenSpot-V2) and promising task success rates (28.0% on AndroidWorld, 19.8% on OSWorld), illustrating both the opportunities and challenges of building efficient on-device GUI agents.

- [Scaling Synthetic Task Generation for Agents via Exploration](https://arxiv.org/abs/2509.25047)
    - Ram Ramrakhya, Andrew Szot, Omar Attia, Yuhao Yang, Anh Nguyen, Bogdan Mazoure, Zhe Gan, Harsh Agrawal, Alexander Toshev
    - 🏛️ Institutions: Apple
    - 📅 Date: September 29, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [task generation], [training data], [exploration]
    - 📖 TLDR: AutoPlay is a scalable pipeline for synthetic agentic task generation that explicitly explores interactive environments to discover possible interactions, producing diverse, feasible, and verifiable tasks for post-training MLLMs as interactive agents for computer-use and web navigation.

- [ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration](https://arxiv.org/abs/2509.21823)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuqing Yang, Yuanchun Li, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Nanyang Technological University, Microsoft Research, Institute for AI Industry Research (AIR), Tsinghua University, Hong Kong University of Science and Technology
    - 📅 Date: September 26, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reward system], [agentic evaluation], [state probing], [ProRe]
    - 📖 TLDR: ProRe is a reward system for GUI agents that replaces purely static trajectory judging with active state probing: a reasoner schedules targeted checks and evaluator agents interact with the environment to collect missing evidence before assigning rewards. This proactive setup improves reward accuracy and F1 on more than 3,000 trajectories and also improves downstream policy performance.

- [BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent](https://arxiv.org/abs/2509.15566)
    - Shaojie Zhang, Ruoceng Zhang, Pei Fu, Shaokang Wang, Jiahui Yang, Xin Du, Shiqi Cui, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: September 19, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement fine-tuning], [reasoning], [reward design], [BTL-UI]
    - 📖 TLDR: BTL-UI organizes GUI interaction into three phases, Blink, Think, and Link, to better align agent behavior with human-style GUI perception, reasoning, and action. The paper's main additions are blink-oriented data generation and a rule-based reward that supervises both process and outcome, and the resulting model performs competitively on both static understanding and dynamic interaction benchmarks.

- [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221)
    - Zhaoyang Liu, Jingjing Xie, Zichen Ding, Zehao Li, Bowen Yang, Zhenyu Wu, Xuehui Wang, Qiushi Sun, Shi Liu, Weiyun Wang, Shenglong Ye, Qingyun Li, Xuan Dong, Yue Yu, Chenyu Lu, YunXiang Mo, Yao Yan, Zeyue Tian, Xiao Zhang, Yuan Huang, Yiqian Liu, Weijie Su, Gen Luo, Xiangyu Yue, Biqing Qi, Kai Chen, Bowen Zhou, Yu Qiao, Qifeng Chen, Wenhai Wang
    - 🏛️ Institutions: Shanghai AI Laboratory
    - 📅 Date: September 18, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [model], [ScaleCUA]
    - 📖 TLDR: This paper presents **ScaleCUA**, a large-scale open-source project for training general-purpose computer use agents (CUAs). The dataset spans 6 operating systems and 3 task domains, built using a hybrid pipeline combining automated agents with human experts. ScaleCUA supports tasks like GUI understanding, grounding, and full interaction. The trained models outperform baselines and set new SOTA on key benchmarks like WebArena-Lite-v2 and MMBench-GUI. The authors also release the full dataset, models, and codebase to promote further research in GUI-based agents.

- [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://arxiv.org/abs/2509.02322)
    - Longrong Yang, Zhixiong Zeng, Yufeng Zhong, Jing Huang, Liming Zheng, Lei Chen, Haibo Qiu, Zequn Qin, Lin Ma, Xi Li
    - 🏛️ Institutions: Meituan, Zhejiang University
    - 📅 Date: September 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [embodied agent], [multitask learning], [Mixture-of-Experts], [OmniActor]
    - 📖 TLDR: This paper studies how to build a single multimodal agent that can act in both GUI-based 2D environments and embodied 3D settings. It proposes OmniActor, which uses a layer-heterogeneous MoE design to separate deep-layer conflicts between GUI and embodied data while sharing shallow-layer synergy, together with a unified action space and large-scale mixed training data. The reported gains are especially strong on GUI tasks, making it relevant as a broader generalist-agent direction that still materially advances GUI agents.

- [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)
    - Haoming Wang, Haoyang Zou, Huatong Song, Jiazhan Feng, Junjie Fang, Junting Lu, Longxiang Liu, Qinyu Luo, Shihao Liang, Shijue Huang, Wanjun Zhong, Yining Ye, Yujia Qin, Yuwen Xiong, Yuxin Song, Zhiyong Wu, Aoyan Li, Bo Li, Chen Dun, Chong Liu, Daoguang Zan, Fuxing Leng, Hanbin Wang, Hao Yu, Haobin Chen, Hongyi Guo, Jing Su, Jingjia Huang, Kai Shen, Kaiyu Shi, Lin Yan, Peiyao Zhao, Pengfei Liu, Qinghao Ye, Renjie Zheng, Shulin Xin, Wayne Xin Zhao, Wen Heng, Wenhao Huang, Wenqian Wang, Xiaobo Qin, Yi Lin, Youbin Wu, Zehui Chen, Zihao Wang, Baoquan Zhong, Xinchun Zhang, Xujing Li, Yuanfan Li, Zhongkai Zhao, Chengquan Jiang, Faming Wu, Haotian Zhou, Jinlin Pang, Li Han, Qi Liu, Qianli Ma, Siyao Liu, Songhua Cai, Wenqi Fu, Xin Liu, Yaohui Wang, Zhi Zhang, Bo Zhou, Guoliang Li, Jiajun Shi, Jiale Yang, Jie Tang, Li Li, Qihua Han, Taoran Lu, Woyu Lin, Xiaokang Tong, Xinyao Li, Yichi Zhang, Yu Miao, Zhengxuan Jiang, Zili Li, Ziyuan Zhao, Chenxin Li, Dehua Ma, Feng Lin, Ge Zhang, Haihua Yang, Hangyu Guo, Hongda Zhu, Jiaheng Liu, Junda Du, Kai Cai, Kuanye Li, Lichen Yuan, Meilan Han, Minchao Wang, Shuyue Guo, Tianhao Cheng, Xiaobo Ma, Xiaojun Xiao, Xiaolong Huang, Xinjie Chen, Yidi Du, Yilin Chen, Yiwen Wang, Zhaojian Li, Zhenzhu Yang, Zhiyuan Zeng, Chaolin Jin, Chen Li, Hao Chen, Haoli Chen, Jian Chen, Qinghao Zhao, Guang Shi
    - 🏛️ Institutions: ByteDance Seed
    - 📅 Date: September 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [UI-TARS-2]
    - 📖 TLDR: UI‑TARS‑2 is a newly trained native GUI‑centered agent that uses a scalable data flywheel, stabilized multi‑turn reinforcement learning, hybrid GUI + terminal environments, and a unified sandbox. It achieves leading performance across diverse GUI benchmarks (e.g., 88.2 on Online‑Mind2Web), game tasks (~60% human-level), and generalizes to information-seeking and software engineering tasks. Training dynamics and parameter interpolation offer insights into robust, efficient agent RL at scale.

- [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)
    - Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, Zhengxi Lu, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: August 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [multi-agent], [GUI automation], [trajectory production], [TRPO]
    - 📖 TLDR: The paper introduces **GUI-Owl**, a foundational multimodal GUI agent model built on Qwen2.5-VL, integrating perception, grounding, reasoning, planning, and action execution into one policy network. GUI-Owl-7B achieves strong baseline performance (66.4 on AndroidWorld, 29.4 on OSWorld). The authors further propose **Mobile-Agent-v3**, a general-purpose, multi-agent GUI automation framework that builds on GUI-Owl and achieves state-of-the-art open-source results (73.3 on AndroidWorld, 37.7 on OSWorld). Core innovations include: a large-scale cross-platform cloud-based environment infrastructure with Self-Evolving GUI Trajectory Production; modular foundational agent capabilities; and scalable, asynchronous reinforcement learning using Trajectory-aware Relative Policy Optimization (TRPO). The framework is open-sourced at the X-PLUG MobileAgent GitHub repository.

- [You Don’t Know Until You Click: Automated GUI Testing for Production-Ready Software Evaluation](https://arxiv.org/abs/2508.14104)
    - Yutong Bian, Xianhao Lin, Yupeng Xie, Tianyang Liu, Mingchen Zhuge, Siyuan Lu, Haoming Tang, Jinlin Wang, Jiayi Zhang, Jiaqi Chen, Xiangru Tang, Yongxin Ni, Sirui Hong, Chenglin Wu
    - 🏛️ Institutions: DeepWisdom, Fudan University, Hong Kong University of Science and Technology (Guangzhou), University of California San Diego, King Abdullah University of Science and Technology, Westlake University, Stanford University, Yale University, National University of Singapore
    - 📅 Date: August 17, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-as-a-judge], [RealDevWorld], [RealDevBench], [AppEvalPilot], [multimodal]
    - 📖 TLDR: This paper presents **RealDevWorld**, a novel framework to automatically evaluate production-ready GUI software generated by LLMs. It includes **RealDevBench**, a suite of 194 open-ended, multimodal software engineering tasks, and **AppEvalPilot**, an “agent-as-judge” system that simulates realistic GUI interactions to assess functional correctness, visual fidelity, and runtime behavior. It achieves high alignment with human judgment (accuracy 0.92, correlation 0.85), reducing the need for manual review and offering scalable, human-aligned evaluation. Code is available on GitHub.

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
    - 📅 Date: August 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time scaling], [reinforcement learning], [self‑supervised], [GUI‑RC], [GUI‑RCPO], [benchmark], [region consistency], [GUI grounding]
    - 📖 TLDR: This paper introduces **GUI‑RC (Region Consistency)**, a test-time method that aggregates multiple model predictions via spatial voting to derive a consensus region—achieving 2–3% accuracy improvements on ScreenSpot benchmarks without any additional training. It extends this idea with **GUI‑RCPO (Region Consistency Policy Optimization)**, which turns region-consistency patterns into self-supervised rewards for reinforcement learning at inference time, refining model predictions on unlabeled data and yielding further improvements (e.g., from 83.57% to 85.14% on ScreenSpot‑v2). The approach demonstrates a novel and effective use of test-time optimization for more robust, data-efficient GUI grounding.

- [GuirlVG: Incentivize GUI Visual Grounding via Empirical Exploration on Reinforcement Learning](https://arxiv.org/abs/2508.04389)
    - Weitai Kang, Bin Lei, Gaowen Liu, Caiwen Ding, Yan Yan
    - 🏛️ Institutions: University of Illinois Chicago, University of Minnesota, Cisco Research
    - 📅 Date: August 06, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [reinforcement learning], [reinforcement fine-tuning], [ScreenSpot], [GuirlVG]
    - 📖 TLDR: This paper studies reinforcement fine-tuning for GUI visual grounding and argues that naive rule-based RL underperforms strong supervised baselines without careful formulation. It introduces GuirlVG, which systematically redesigns the reward, training setup, and stabilization mechanism, including an Adversarial KL Factor to reduce reward over-optimization. With only 5.2K training samples, the method surpasses prior GUI grounding approaches trained on much larger datasets across ScreenSpot, ScreenSpot-Pro, and ScreenSpot-V2.

- [NaviMaster: Learning a Unified Policy for GUI and Embodied Navigation Tasks](https://arxiv.org/abs/2508.02046)
    - Zhihao Luo, Wentao Yan, Jingyu Gong, Min Wang, Zhizhong Zhang, Xuhong Wang, Yuan Xie, Xin Tan
    - 🏛️ Institutions: East China Normal University, Shanghai AI Laboratory, SenseTime Research
    - 📅 Date: August 04, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI navigation], [embodied navigation], [reinforcement learning], [unified agent]
    - 📖 TLDR: NaviMaster is the first unified agent that combines GUI navigation (mobile/web/desktop) and embodied navigation within a single reinforcement learning framework, using a visual-target trajectory collection pipeline and distance-aware reward to outperform state-of-the-art agents on out-of-domain benchmarks across both domains.

- [NaturalGAIA: Pushing the Frontiers of GUI Agents with a Challenging Benchmark and High-Quality Trajectory Dataset](https://arxiv.org/abs/2508.01330)
    - Zihan Zheng, Tianle Cui, Chuwen Xie, Jiahui Zhang, Jiahui Pan, Lewei He, Qianglong Chen
    - 🏛️ Institutions: South China Normal University, Zhejiang University
    - 📅 Date: August 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [trajectory dataset], [causal pathways], [hierarchical agent], [reinforcement fine-tuning], [WPSR], [NaturalGAIA], [LightManus]
    - 📖 TLDR: NaturalGAIA is a GUI benchmark built around causal pathways and programmatically verifiable atomic steps, paired with a human-verified trajectory dataset collected using the hierarchical LightManus agent. It shows that complex cross-platform GUI tasks remain difficult even for strong models, and that reinforcement fine-tuning improves execution but does not eliminate the broader capability ceiling.

- [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976)
    - Junhong Shen, Hao Bai, Lunjun Zhang, Yifei Zhou, Amrith Setlur, Shengbang Tong, Diego Caples, Nan Jiang, Tong Zhang, Ameet Talwalkar, Aviral Kumar
    - 🏛️ Institutions: Carnegie Mellon University, Scribe, University of Illinois Urbana-Champaign, University of Toronto, University of California, Berkeley, The AGI Company, New York University
    - 📅 Date: June 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [test-time scaling], [exploration], [planning], [reinforcement learning]
    - 📖 TLDR: Proposes test-time interaction scaling—increasing agent interaction horizons rather than reasoning trace length—showing that richer behaviors including exploration, backtracking, and dynamic adaptation from more interactions outperform extended pre-action thinking for GUI-based computer tasks.

- [ZeroGUI: Automating Online GUI Learning at Zero Human Cost](https://arxiv.org/abs/2505.23762)
    - Chenyu Yang, Shiqian Su, Shi Liu, Xuan Dong, Yue Yu, Weijie Su, Xuehui Wang, Zhaoyang Liu, Jinguo Zhu, Hao Li, Wenhai Wang, Yu Qiao, Xizhou Zhu, Jifeng Dai
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, Tsinghua University, Shanghai Jiao Tong University, Hong Kong University of Science and Technology, The Chinese University of Hong Kong
    - 📅 Date: May 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [model-free], [VLM-task-generation], [VLM-reward-estimation], [ZeroGUI]
    - 📖 TLDR: Introduces **ZeroGUI**, a novel online learning framework that enables GUI agents (based on VLMs) to learn by autonomous interaction without human labels. It uses vision-language models to (i) generate diverse task instructions, (ii) evaluate task success, and (iii) apply a two-stage RL strategy (task-generated training + test-time adaptation). The method shows strong performance gains (e.g., +14% on UI-TARS, +63% on Aguvis) in desktop (OSWorld) and mobile (AndroidLab) GUI benchmarks, proving scalable, human-free GUI-agent training.  

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, School of Computer Science, MoE Key Lab of Artificial Intelligence, SJTU AI Institute, Shanghai Jiao Tong University, Jiangsu Key Lab of Language Computing, Suzhou Laboratory
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [reward model], [progress reward], [LCS], [ProgRM]
    - 📖 TLDR: Introduces **ProgRM**, a novel framework giving dense intermediate rewards to GUI agents by estimating per‑step task progress. Labels are generated through an LCS‑based self‑annotation algorithm that identifies key steps in successful trajectories. Agents trained with ProgRM outperform outcome‑based reward models and proprietary LLMs like Claude‑3.7‑Sonnet across benchmarks.

- [ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282)
    - Fanbin Lu, Zhisheng Zhong, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: The Chinese University of Hong Kong, SmartMore, Hong Kong University of Science and Technology
    - 📅 Date: May 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [policy optimization], [training], [multi-turn]
    - 📖 TLDR: ARPO (End-to-End Policy Optimization for GUI Agents with Experience Replay) addresses multi-turn RL for VLM-based GUI agents through experience replay to mitigate sparse rewards, delayed feedback, and high rollout costs, enabling efficient optimization of long-horizon GUI action sequences.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Gaoling School of Artificial Intelligence, Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [visual grounding], [reinforcement learning], [ScreenSpot], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets and Benchmarks Track (Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [framework], [jedi], [OSWorld‑G], [GUI grounding], [compositional generalization], [fine‑grained manipulation]
    - 📖 TLDR: This work tackles limitations in GUI grounding by introducing **OSWorld‑G**, a 564‑sample benchmark covering text matching, element recognition, layout understanding, fine‑grained manipulation, and refusal detection. They also synthesize **Jedi**, a massive 4 M‑example dataset generated via UI decomposition and synthesis. Training multi‑scale models on Jedi achieves state‑of‑the‑art grounding across benchmarks (ScreenSpot‑v2/Pro and OSWorld‑G), boosting agentic task performance from 5 % to ~27 % success. Ablations demonstrate compositional benefits. All artifacts are publicly released.

- [GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents](https://arxiv.org/abs/2505.12842)
    - Zheng Wu, Pengzhou Cheng, Zongru Wu, Lingzhong Dong, Zhuosheng Zhang
    - 🏛️ Institutions: School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [out-of-distribution detection], [safety], [gaussian mixture model], [MLLM], [robustness]
    - 📖 TLDR: GEM proposes a Gaussian mixture model-based method for detecting out-of-distribution instructions in GUI agents by modeling input embedding distances, achieving a 23.70% average accuracy improvement over baselines across eight datasets spanning smartphones, computers, and web browsers.

- [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: VCIP, School of Computer Science, NKU, vivo Mobile Communication Co., Ltd, National University of Singapore, Fudan University, East China University of Science and Technology
    - 📅 Date: May 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [visual grounding], [ScreenSpot-pro], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?](https://arxiv.org/abs/2505.10924)
    - Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
    - 🏛️ Institutions: Carnegie Mellon University, The Chinese University of Hong Kong, KAUST, Johns Hopkins University, Nanyang Technological University, The Hong Kong University of Science and Technology
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [safety], [security]
    - 📖 TLDR: A comprehensive survey of safety and security threats to computer-using agents, covering vulnerabilities in LLM-driven reasoning, multi-component integration, and GUI interaction, analyzing novel risks as CUAs evolve from prototype tools to sophisticated autonomous systems.

- [Talk to Your Slides: High-Efficiency Slide Editing via Language-Driven Structured Data Manipulation](https://arxiv.org/abs/2505.11604)
    - Kyudan Jung, Hojun Cho, Jooyeol Yun, Soyoung Yang, Jaehyeok Jang, Jaegul Choo
    - 🏛️ Institutions: Chung-ang University, KAIST AI
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [LLM agent], [slide editing], [benchmark], [code generation], [structured data manipulation]
    - 📖 TLDR: Talk-to-Your-Slides is a language-driven slide editing agent that manipulates structured document data (XML/COM object model) instead of relying on GUI-based visual interactions, achieving 34% faster processing, 34% better instruction fidelity, and 87% lower cost than GUI-based baselines, along with a new benchmark (TSBench) of 379 human-verified editing instructions.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: University of Michigan, LG AI Research
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [RegionFocus], [test-time scaling], [grounding], [zoom-in reasoning]
    - 📖 TLDR: Presents RegionFocus, a test-time scaling method that repeatedly zooms into promising GUI regions instead of relying on a single full-screen pass. The paper treats grounding as an iterative visual search problem and shows strong gains on ScreenSpot-Pro and WebVoyager without retraining the base model.

- [ScaleTrack: Scaling and back-tracking Automated GUI Agents](https://arxiv.org/abs/2505.00416)
    - Jing Huang, Zhixiong Zeng, Wenkang Han, Yufeng Zhong, Liming Zheng, Shuai Fu, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, University of Adelaide
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [training strategy], [back-tracking], [grounding], [ScaleTrack]
    - 📖 TLDR: Presents ScaleTrack, a training framework that tackles GUI-agent weaknesses at both the data and planning levels. It scales grounding data through unified sample aggregation and explicitly trains back-tracking behavior so agents can recover from wrong turns instead of only moving forward.

- [A Survey on GUI Agents with Foundation Models Enhanced by Reinforcement Learning](https://arxiv.org/abs/2504.20464)
    - Jiahao Li, Kaer Huang
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: April 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [reinforcement learning], [multimodal], [training taxonomy], [MDP formulation]
    - 📖 TLDR: Surveys GUI agents through the lens of reinforcement learning, framing GUI interaction as an MDP and organizing the field around perception, planning, and acting modules. Its main value is a training-oriented taxonomy that connects prompting, supervised fine-tuning, and RL-style policy optimization.

- [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)
    - Yuhang Liu, Pengxiang Li, Congkai Xie, Xavier Hu, Xiaotian Han, Shengyu Zhang, Hongxia Yang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Dalian University of Technology, Reallm Labs, The Hong Kong Polytechnic University
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [planning], [reasoning], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: Presents InfiGUI-R1 as a GUI agent designed to move from reactive action prediction toward explicit deliberative reasoning. The Actor2Reasoner pipeline first injects spatial reasoning and then strengthens planning and recovery through RL with sub-goal guidance and error-recovery scenarios.

- [TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents](https://arxiv.org/abs/2504.12679)
    - Bofei Zhang, Zirui Shang, Zhi Gao, Wang Zhang, Rui Xie, Xiaojian Ma, Tao Yuan, Xinxiao Wu, Song-Chun Zhu, Qing Li
    - 🏛️ Institutions: State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing Key Laboratory of Intelligent Information Technology, School of Computer Science & Technology, Beijing Institute of Technology, School of Intelligence Science and Technology, Peking University, Shanghai Jiao Tong University, Department of Automation, Tsinghua University
    - 📅 Date: April 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [GUI-Net], [web tutorials], [trajectory generation], [TongUI]
    - 📖 TLDR: Presents TongUI, a pipeline for turning multimodal web tutorials into large-scale GUI-agent trajectories. Its main contribution is GUI-Net, a tutorial-derived corpus spanning multiple operating systems and applications, showing that tutorial mining can be an effective data source for generalized GUI agents.

- [UI-E2I-Synth: Advancing GUI Grounding with Large-Scale Instruction Synthesis](https://aclanthology.org/2025.findings-acl.809/)
    - Xinyi Liu, Xiaoyi Zhang, Ziyun Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia, School of Software and Microelectronics, Peking University
    - 📅 Date: April 15, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [instruction synthesis], [GUI grounding], [UI-E2I-Synth], [UI-I2E-Bench]
    - 📖 TLDR: UI-E2I-Synth targets the data bottleneck in vision-based GUI instruction grounding, especially for implicit instructions, small elements, and underrepresented element types. It introduces a GPT-4o-based large-scale instruction synthesis pipeline and the UI-I2E-Bench benchmark, showing that models trained on the synthesized data achieve stronger GUI grounding performance across platforms.

- [Breaking the Data Barrier -- Building GUI Agents Through Task Generalization](https://openreview.net/forum?id=QDtORaZt8K)
    - Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, Qiushi Sun, Zhenzhong Lan, Junxian He
    - 🏛️ Institutions: Zhejiang University, Westlake University, Shanghai Artificial Intelligence Laboratory, University of Hong Kong, Hong Kong University of Science and Technology
    - 📅 Date: April 14, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [mid-training], [task generalization], [multimodal reasoning], [textual reasoning], [GUI agent training], [GUIMid]
    - 📖 TLDR: This paper studies whether GUI agents can improve by mid-training on non-GUI but reasoning-intensive tasks before GUI fine-tuning. It finds that task generalization is highly effective: multimodal and even text-only reasoning data substantially improve downstream WebArena and AndroidWorld performance, showing that scarce GUI trajectories can be complemented by broader reasoning data.

- [GUI-R1: A Generalist R1-Style Vision-Language Action Model for GUI Agents](https://arxiv.org/abs/2504.10458)
    - Run Luo, Lu Wang, Wanwei He, Longze Chen, Jiaming Li, Min Yang, Xiaobo Xia
    - 🏛️ Institutions: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences, National University of Singapore
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [unified action space], [GRPO], [data efficiency], [GUI-R1]
    - 📖 TLDR: GUI-R1 is an R1-style reinforcement learning framework for GUI agents that trains vision-language action models with a unified action space and rule-based rewards across Windows, Linux, macOS, Android, and Web. Using only a small curated dataset, it achieves stronger results than prior methods across eight benchmarks, showing that RL can substantially improve data efficiency for GUI-agent training.

- [On the Robustness of GUI Grounding Models Against Image Attacks](https://arxiv.org/abs/2504.04716)
    - Haoren Zhao, Tianyi Chen, Zhen Wang
    - 🏛️ Institutions: HDU, Microsoft
    - 📅 Date: April 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [robustness], [adversarial attacks], [UGround], [ScreenSpot-V2]
    - 📖 TLDR: This paper systematically evaluates the robustness of GUI grounding models, such as UGround, against natural noise, untargeted adversarial attacks, and targeted adversarial attacks. Experiments conducted across mobile, desktop, and web interfaces reveal that these models are highly sensitive to adversarial perturbations and low-resolution conditions. The findings highlight vulnerabilities in current GUI grounding models and establish a benchmark for future research aimed at enhancing their robustness in practical applications.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 01, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [mixture-of-grounding], [proactive hierarchical planning], [Agent S2]
    - 📖 TLDR: Agent S2 is a compositional computer-use framework that delegates grounding and planning across specialized and generalist models instead of relying on a single agent. It introduces Mixture-of-Grounding for precise GUI localization and Proactive Hierarchical Planning for dynamic long-horizon control, and reports strong gains on OSWorld, WindowsAgentArena, and AndroidWorld.

- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434)
    - Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu
    - 🏛️ Institutions: University of Georgia, Tencent AI Seattle Lab, Microsoft Research, University of Waterloo, Hong Kong Polytechnic University
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [trustworthiness], [safety], [security], [benchmark]
    - 📖 TLDR: A survey on trustworthy GUI agents that introduces a workflow-aligned taxonomy decomposing trust into Perception Trust, Reasoning Trust, and Interaction Trust, systematically reviewing failure modes, adversarial attacks, defense mechanisms, and evaluation practices for deploying GUI agents safely.

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, Microsoft Research Asia
    - 📅 Date: March 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [dual-system cognition], [FOCUS], [ScreenSpot], [ScreenSpot-pro]
    - 📖 TLDR: Proposes FOCUS, a GUI grounding framework inspired by fast and slow human reasoning, which switches between quick prediction and deeper analysis based on task complexity. By decomposing grounding into interface summarization, focused visual analysis, and final coordinate prediction, it reaches strong ScreenSpot and ScreenSpot-Pro results with only 300K training examples.

- [SpiritSight Agent: Advanced GUI Agent with One Look](https://arxiv.org/abs/2503.03196)
    - Zhiyuan Huang, Ziming Cheng, Junting Pan, Zhaohui Hou, Mingjie Zhan
    - 🏛️ Institutions: SenseTime Research, Beijing University of Posts and Telecommunications, MMLab, CUHK
    - 📅 Date: March 05, 2025
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [VLM], [single-screenshot inference], [cross-platform], [SpiritSight Agent]
    - 📖 TLDR: SpiritSight Agent is a vision-based GUI agent that aims to improve grounding accuracy and latency using only a single screenshot per decision step. Its one-look design targets efficient cross-platform GUI interaction without relying on heavier multi-stage perception pipelines.

- [Magma: A Foundation Model for Multimodal AI Agents](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html)
    - Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai, Seonghyeon Ye, Joel Jang, Yuquan Deng, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research, University of Maryland, University of Wisconsin-Madison, KAIST, University of Washington
    - 📅 Date: February 18, 2025
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [SoM], [ToM], [robotics], [UI navigation]
    - 📖 TLDR: This paper introduces **Magma**, a foundation model designed for multimodal AI agents operating in both digital and physical environments. Magma extends traditional vision-language models by incorporating planning and action capabilities, enabling tasks from UI navigation to robotic manipulation. The model is pretrained on diverse datasets, including images, videos, and robotics data, utilizing **Set-of-Mark (SoM)** for action grounding and **Trace-of-Mark (ToM)** for action planning. Experiments demonstrate that SoM and ToM synergistically enhance Magma's spatial-temporal intelligence, achieving state-of-the-art performance in UI navigation and robotic manipulation tasks.

- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)
    - Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng, Xin Liu, Guang Shi
    - 🏛️ Institutions: ByteDance Seed, Tsinghua University
    - 📅 Date: January 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [action modeling], [system-2 reasoning], [reflective online traces], [UI-TARS]
    - 📖 TLDR: UI-TARS is an end-to-end native GUI agent model that operates directly from screenshots rather than wrapping a commercial foundation model with handcrafted prompting workflows. It combines enhanced GUI perception, unified cross-platform action modeling, deliberate multi-step reasoning, and iterative training on reflective online traces, and reports strong results across more than ten GUI-agent benchmarks.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://aclanthology.org/2025.acl-long.277/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Laboratory, The University of Hong Kong, Johns Hopkins University, Shanghai Jiao Tong University, University of Oxford, Hong Kong University of Science and Technology
    - 📅 Date: December 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [trajectory synthesis], [reverse task synthesis], [reward model], [GUI agent training], [OS-Genesis]
    - 📖 TLDR: OS-Genesis tackles the scarcity of high-quality GUI trajectories by synthesizing them without preset tasks or human demonstrations. It reverses the usual collection process by first exploring with step-level interactions, then retrospectively deriving tasks and filtering trajectories with a reward model, producing more diverse training data and improving online GUI-agent performance.

- [OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://github.com/OS-Agent-Survey/OS-Agent-Survey)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shawn Wang, Xinchen Xu, Shuofei Qiao , Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao, Hongxia Yang, Fan Wu, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Fudan University, OPPO AI Center, University of Chinese Academy of Sciences, Chinese Academy of Sciences, The Chinese HKU, Tsinghua University, 01.AI, The Hong Kong Polytechnic University, SJTU
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Github Repo
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This paper conducts a comprehensive survey on OS Agents, which are (M)LLM-based agents that use computing devices (e.g., computers and mobile phones) by operating within the environments and interfaces (e.g., Graphical User Interface (GUI)) provided by operating systems (OS) to automate tasks. The survey begins by elucidating the fundamentals of OS Agents, exploring their key components including the environment, observation space, and action space, and outlining essential capabilities such as understanding, planning, and grounding. Methodologies for constructing OS Agents are examined, with a focus on domain-specific foundation models and agent frameworks. A detailed review of evaluation protocols and benchmarks highlights how OS Agents are assessed across diverse tasks. Finally, current challenges and promising future research directions, including safety and privacy, personalization and self-evolution, are discussed.

- [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shenzhi Wang, Xinchen Xu, Shuofei Qiao, Zhaokai Wang, Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao, Hongxia Yang, Fan Wu, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Fudan University, OPPO AI Center, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, The Chinese University of Hong Kong, Tsinghua University, Shanghai Jiao Tong University, 01.AI, The Hong Kong Polytechnic University
    - 📅 Date: December 20, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This paper conducts a comprehensive survey on OS Agents, which are (M)LLM-based agents that use computing devices (e.g., computers and mobile phones) by operating within the environments and interfaces (e.g., Graphical User Interface (GUI)) provided by operating systems (OS) to automate tasks. The survey begins by elucidating the fundamentals of OS Agents, exploring their key components including the environment, observation space, and action space, and outlining essential capabilities such as understanding, planning, and grounding. Methodologies for constructing OS Agents are examined, with a focus on domain-specific foundation models and agent frameworks. A detailed review of evaluation protocols and benchmarks highlights how OS Agents are assessed across diverse tasks. Finally, current challenges and promising future research directions, including safety and privacy, personalization and self-evolution, are discussed. 

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research, Alibaba Group, Australian National University, Independent Researcher
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [pure vision], [instruction synthesis], [context-aware grounding], [Aria-UI]
    - 📖 TLDR: Aria-UI is a GUI-grounding model that deliberately avoids HTML or AXTree inputs and instead works from pure visual observations. It pairs a scalable instruction-synthesis pipeline with interleaved textual and text-image action histories for context-aware grounding, and reports state-of-the-art results across offline and online grounding benchmarks.

- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501)
    - Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen, Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Branislav Kveton, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, Franck Dernoncourt
    - 🏛️ Institutions: University of Maryland, SUNY Buffalo, University of Oregon, Adobe Research, Meta AI, University of Rochester, University of California San Diego, Carnegie Mellon University, Dolby Laboratories, Intel AI Research, University of New South Wales
    - 📅 Date: December 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This survey provides a comprehensive overview of GUI agents powered by Large Foundation Models, detailing their benchmarks, evaluation metrics, architectures, and training methods. It introduces a unified framework outlining their perception, reasoning, planning, and acting capabilities, identifies open challenges, and discusses future research directions, serving as a resource for both practitioners and researchers in the field.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, National University of Singapore
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [information-sensitive cropping], [self-refining dual learning], [visual grounding], [model]
    - 📖 TLDR: This paper introduces *Iris*, a visual agent designed to enhance GUI automation by addressing challenges in high-resolution, complex digital environments. It employs two key innovations: **Information-Sensitive Cropping (ISC)**, which dynamically identifies and prioritizes visually dense regions using an edge detection algorithm for efficient processing, and **Self-Refining Dual Learning (SRDL)**, which enhances the agent's ability to handle complex tasks through a dual-learning loop that iteratively refines its performance without requiring additional annotated data. Empirical evaluations demonstrate that Iris achieves state-of-the-art performance across multiple benchmarks with only 850K GUI annotations, outperforming methods using ten times more training data.

- [Falcon-UI: Understanding GUI Before Following User Instructions](https://arxiv.org/abs/2412.09362)
    - Huawen Shen, Chang Liu, Gengluo Li, Xinlong Wang, Yu Zhou, Can Ma, Xiangyang Ji
    - 🏛️ Institutions: Chinese Academy of Sciences, Tsinghua University, Nankai University, Beijing Academy of Artificial Intelligence
    - 📅 Date: December 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [falcon-UI], [GUI understanding]
    - 📖 TLDR: This paper introduces *Falcon-UI*, a GUI agent model that emphasizes understanding GUI contexts before following user instructions. The authors present the *Insight-UI Dataset*, an instruction-free GUI navigation dataset generated from the Common Crawl corpus, simulating various platforms like iOS, Android, Windows, and Linux across multiple resolutions on 312K domains. Falcon-UI is pretrained on this dataset and fine-tuned on Android and Web GUI datasets, achieving performance comparable to larger models, highlighting the importance of decoupling GUI understanding from instruction following in agent performance. 

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Nanyang Technological University, Salesforce Research
    - 📅 Date: December 05, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [pure vision], [inner monologue], [two-stage training], [Aguvis]
    - 📖 TLDR: Aguvis is a pure-vision GUI agent framework that removes textual representations and unifies cross-platform interaction directly from screen images. It combines a large-scale grounding-and-reasoning dataset with a two-stage training pipeline and inner-monologue reasoning, reporting state-of-the-art offline and online results without relying on closed-source models.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://aclanthology.org/2025.findings-acl.76/)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Shenzhen International Graduate School, Tsinghua University
    - 📅 Date: December 02, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [pure vision], [GUI grounding], [interpreter-locator], [ScreenSpot], [Ponder & Press]
    - 📖 TLDR: Ponder & Press is a pure-vision divide-and-conquer GUI-control framework that separates high-level instruction interpretation from element localization. It pairs a general-purpose MLLM interpreter with a GUI-specific locator, improves ScreenSpot grounding by 22.5%, and reports strong performance across web, desktop, and mobile GUI benchmarks.

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [UI-guided visual token selection], [interleaved vision-language-action streaming], [screenshot grounding], [ShowUI]
    - 📖 TLDR: ShowUI is a lightweight vision-language-action model for GUI visual agents that focuses on efficient screenshot perception and action-history modeling. It introduces UI-guided visual token selection and interleaved vision-language-action streaming, reaching 75.1% zero-shot screenshot-grounding accuracy while remaining competitive on web and mobile GUI tasks.

- [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)
    - Anthony Nguyen
    - 🏛️ Institutions: Algoma University
    - 📅 Date: November 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [visual prompting], [iterative narrowing]
    - 📖 TLDR: Proposes Iterative Narrowing, a visual prompting framework for GUI grounding that repeatedly focuses on smaller image regions to refine predictions. The method improves both general and fine-tuned VLMs on one-shot GUI grounding, with later versions reporting gains of up to 61% on a multi-platform benchmark.

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890)
    - Shuai Wang, Weiwen Liu, Jingxuan Chen, Yuqi Zhou, Weinan Gan, Xingshan Zeng, Yuhan Che, Shuai Yu, Xinlong Hao, Kun Shao, Bin Wang, Chuhan Wu, Yasheng Wang, Ruiming Tang, Jianye Hao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, Renmin University of China
    - 📅 Date: November 07, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [foundation models], [taxonomy]
    - 📖 TLDR: Surveys GUI agents built on LLMs and multimodal foundation models, covering data resources, benchmark design, agent frameworks, and industrial applications. It also proposes a unified taxonomy of prior work and highlights open challenges around personalization, safety, and inference efficiency.

- [EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data](https://arxiv.org/abs/2410.19461)
    - Xuetian Chen, Hangcheng Li, Jiaqing Liang, Sihang Jiang, Deqing Yang
    - 🏛️ Institutions: Fudan University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [synthetic data], [GUI grounding], [multi-granularity data], [EDGE]
    - 📖 TLDR: Proposes EDGE, a synthetic-data pipeline for GUI understanding that enriches supervision at multiple granularities using webpage-derived data. The resulting training data improves grounding and interaction performance across desktop and mobile GUI tasks without relying on large amounts of manual annotation.

- [TinyClick: Single-Turn Agent for Empowering GUI Automation](https://www.isca-archive.org/interspeech_2025/pawlowski25_interspeech.html)
    - Pawel Pawlowski, Krystian Zawistowski, Wojciech Lapacz, Adam Wiacek, Marcin Skorupa, Sebastien Postansque, Jakub Hoscilowicz
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 09, 2024
    - 📑 Publisher: INTERSPEECH 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [single-turn agent], [on-device model], [ScreenSpot], [OmniAct], [TinyClick]
    - 📖 TLDR: TinyClick is a compact, single-turn agent designed to automate GUI tasks by precisely locating screen elements via the Vision-Language Model Florence-2-Base. Trained with multi-task strategies and MLLM-based data augmentation, TinyClick achieves high accuracy on Screenspot and OmniAct, outperforming specialized GUI interaction models and general MLLMs like GPT-4V. The model's lightweight design (0.27B parameters) ensures fast processing and minimal latency, making it efficient for real-world applications on multiple platforms.

- [Grounded GUI Understanding for Vision-Based Spatial Intelligent Agent: Exemplified by Extended Reality Apps](https://arxiv.org/abs/2409.10811)
    - Shuqing Li, Binchang Li, Yepang Liu, Cuiyun Gao, Jianping Zhang, Shing-Chi Cheung, Michael R. Lyu
    - 🏛️ Institutions: The Chinese University of Hong Kong, Harbin Institute of Technology, Southern University of Science and Technology, The Hong Kong University of Science and Technology
    - 📅 Date: September 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI understanding], [GUI grounding], [VR/AR], [zero-shot detection], [multimodal LLM], [software testing]
    - 📖 TLDR: Proposes Orienter, the first zero-shot context-sensitive interactable GUI element detection framework for Extended Reality (XR/VR) apps, which uses semantic context comprehension and reflection-directed detection to identify interactable GUI elements in 3D virtual environments more effectively than existing approaches.

- [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/eea71dc576381b88f2a0ca4dedc2140d-Abstract-Conference.html)
    - Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Song XiXuan, Yifan Xu, Shudan Zhang, Hanyu Lai, Jiadai Sun, Xinyue Yang, Yu Yang, Zehan Qi, Shuntian Yao, Xueqiao Sun, Siyi Cheng, Qinkai Zheng, Hao Yu, Hanchen Zhang, Wenyi Hong, Ming Ding, Lihang Pan, Xiaotao Gu, Aohan Zeng, Zhengxiao Du, Chan Hee Song, Yu Su, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Microsoft Research Asia, The Ohio State University
    - 📅 Date: August 12, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [embodied], [visual design], [VisualAgentBench], [VAB]
    - 📖 TLDR: The authors introduce *VisualAgentBench (VAB)*, a comprehensive benchmark designed to train and evaluate large multimodal models (LMMs) as visual foundation agents across diverse scenarios, including embodied tasks, graphical user interfaces, and visual design. VAB comprises five distinct environments that systematically challenge LMMs' understanding and interaction capabilities. Additionally, the benchmark offers supervised fine-tuning trajectory data for behavior cloning training, demonstrating the potential to improve open LMMs for serving as visual foundation agents.

- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203)
    - Yadong Lu, Jianwei Yang, Yelong Shen, Ahmed Awadallah
    - 🏛️ Institutions: Microsoft Research, Microsoft GenAI
    - 📅 Date: August 01, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [OmniParser]
    - 📖 TLDR: This paper introduces **OmniParser**, a method for parsing user interface screenshots into structured elements, enhancing the ability of models like GPT-4V to generate actions accurately grounded in corresponding UI regions. The authors curated datasets for interactable icon detection and icon description, fine-tuning models to parse interactable regions and extract functional semantics of UI elements.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: Carnegie Mellon University, University of California, Santa Barbara
    - 📅 Date: June 30, 2024
    - 📑 Publisher: NAACL 2024 Industry Track
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [UI element localization], [LVG]
    - 📖 TLDR: This work introduces the task of visual UI grounding, which unifies detection and grounding by enabling models to identify UI elements referenced by natural language commands solely from visual input. The authors propose **LVG**, a model that outperforms baselines pre-trained on larger datasets by over 4.9 points in top-1 accuracy, demonstrating its effectiveness in localizing referenced UI elements without relying on UI metadata.

- [Read Anywhere Pointed: Layout-aware GUI Screen Reading with Tree-of-Lens Grounding](https://aclanthology.org/2024.emnlp-main.533/)
    - Yue Fan, Lei Ding, Ching-Chen Kuo, Shan Jiang, Yang Zhao, Xinze Guan, Jie Yang, Yi Zhang, Xin Eric Wang
    - 🏛️ Institutions: University of California, Santa Cruz, Microsoft Research
    - 📅 Date: June 27, 2024
    - 📑 Publisher: EMNLP 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [Tree-of-Lens], [screen reading], [accessibility]
    - 📖 TLDR: Proposes Tree-of-Lens for the Screen Point-and-Read task, where an agent must describe the content around user-pointed regions on a screen. The method uses layout-aware grounding over GUI elements and is evaluated on the new ScreenPR benchmark spanning web, mobile, and operating-system screenshots.

- [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://aclanthology.org/2024.findings-emnlp.68/)
    - Ziyang Meng, Yu Dai, Zezheng Gong, Shaoxiong Guo, Minglong Tang, Tongquan Wei
    - 🏛️ Institutions: East China Normal University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI VQA], [hallucination mitigation], [FAC], [referent method], [VGA]
    - 📖 TLDR: Introduces VGA, a GUI-understanding model trained to reduce hallucinations caused by over-reliance on textual priors instead of on-screen evidence. The paper builds a 63.8K GUI VQA dataset with a referent-based construction method and uses a two-stage FAC fine-tuning procedure to improve visually grounded answers.

- [GUICourse: From General Vision Language Models to Versatile GUI Agents](https://aclanthology.org/2025.acl-long.1065/)
    - Wentong Chen, Junbo Cui, Jinyi Hu, Yujia Qin, Junjie Fang, Yue Zhao, Chongyi Wang, Jun Liu, Guirong Chen, Yupeng Huo, Yuan Yao, Yankai Lin, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Renmin University of China, Tsinghua University, Xiamen University, Beijing University of Posts and Telecommunications, ModelBest, Chinese Academy of Sciences, National University of Singapore, Shanghai Qi Zhi Institute
    - 📅 Date: June 17, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [framework], [GUICourse]
    - 📖 TLDR: This paper introduces *GUICourse*, a suite of datasets aimed at training visual-based GUI agents from general vision-language models. It addresses challenges in OCR, grounding, and GUI knowledge, enhancing the models' capabilities in GUI navigation tasks.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Jing Hua Toh, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Carnegie Mellon University, Salesforce Research, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [real computer tasks], [online environment], [online benchmark]
    - 📖 TLDR: OSWorld introduces a groundbreaking benchmark for multimodal agents to perform open-ended tasks within real computer environments across platforms like Ubuntu, Windows, and macOS. It includes 369 real-world tasks involving web and desktop apps, file management, and multi-app workflows, with custom evaluation scripts for reproducibility. The results reveal current agents’ limitations in GUI interaction and operational knowledge, as they achieve just 12.24% task success compared to humans' 72.36%, highlighting critical gaps for future model improvement.

- [Improving Language Understanding from Screenshots](https://arxiv.org/abs/2402.14073)
    - Tianyu Gao, Zirui Wang, Adithya Bhaskar, Danqi Chen
    - 🏛️ Institutions: Princeton Language and Intelligence (PLI), Princeton University
    - 📅 Date: February 21, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [screenshot language model], [PTP], [pretraining objective], [multimodal language understanding]
    - 📖 TLDR: Studies how to make screenshot language models better at text-heavy understanding by pretraining them with a patch-and-text prediction objective that reconstructs both image regions and embedded text. The resulting models close much of the gap to text-only baselines on GLUE-style tasks and also improve autoregressive screenshot language modeling.

- [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Abstract-Conference.html)
    - Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
    - 🏛️ Institutions: Renmin University of China, Peking University, Tencent
    - 📅 Date: February 17, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [attack], [backdoor], [agent security], [trigger placement]
    - 📖 TLDR: Studies backdoor attacks against LLM-based agents by categorizing them according to trigger placement and attack outcome. The paper shows that agent pipelines introduce distinct backdoor surfaces that are not captured by standard single-model safety evaluation.

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://arxiv.org/abs/2402.04615)
    - Gilles Baechler, Srinivas Sunkara, Maria Wang, Fedir Zubach, Hassan Mansoor, Vincent Etter, Victor Cărbune, Jason Lin, Jindong Chen, Abhanshu Sharma
    - 🏛️ Institutions: Google DeepMind
    - 📅 Date: February 07, 2024
    - 📑 Publisher: IJCAI 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [UI understanding], [infographics understanding], [ScreenAI], [screen annotation]
    - 📖 TLDR: Presents ScreenAI, a vision-language model specialized for screen understanding across both UI and infographic settings. It combines PaLI-style modeling with pix2struct-style patching and is trained on a mixture designed specifically for screen-centric perception tasks.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Li YanTao, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: Nanjing University, Shanghai AI Lab
    - 📅 Date: January 19, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [GUI grounding], [ScreenSpot], [SeeClick]
    - 📖 TLDR: SeeClick is a screenshot-only visual GUI agent that targets the core GUI grounding problem without relying on structured accessibility trees or HTML-like inputs. The paper introduces GUI-grounding pretraining data generation and the ScreenSpot benchmark, and shows that better grounding directly improves downstream GUI agent performance.

- [CogAgent: A Visual Language Model for GUI Agents](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_CogAgent_A_Visual_Language_Model_for_GUI_Agents_CVPR_2024_paper.html)
    - Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhao Chen, Yuxuan Wang, Yining Ye, Jiayi Zhang, Hao Dong, Wenhu Chen, Yizhou Wang, Kai-Wei Chang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI
    - 📅 Date: December 15, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [visual language model]
    - 📖 TLDR: This paper presents CogAgent, a visual language model designed for GUI agents. The authors introduce a new dataset, CogBench, featuring 1,430 GUI tasks across various applications. CogAgent employs a novel training approach combining supervised fine-tuning and decision-making fine-tuning. The model demonstrates superior performance on CogBench and generalizes well to unseen applications, outperforming existing models like GPT-4V in GUI task completion.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia
    - 📅 Date: October 07, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [instruction grounding], [pixel-to-sequence], [reinforcement learning], [RUIG]
    - 📖 TLDR: Presents RUIG, a metadata-free grounding model that maps natural-language instructions to coordinates on UI screenshots using a pixel-to-sequence decoder. The main contribution is an RL-style training objective that strengthens spatial decoding quality, positioning RUIG as a generic UI-grounding API rather than a full agent stack.

- [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0ff30c4bf31db0119a6219e0d250e037-Abstract-Conference.html)
    - Hongxin Li, Jingran Su, Yuntao Chen, Qing Li, Zhaoxiang Zhang
    - 🏛️ Institutions: University of Chinese Academy of Sciences, Hong Kong Institute of Science and Innovation, Chinese Academy of Sciences, The Hong Kong Polytechnic University, Shanghai AI Laboratory
    - 📅 Date: May 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [spreadsheet automation], [Excel automation], [SheetCopilot]
    - 📖 TLDR: Presents SheetCopilot, an LLM-based system for carrying out spreadsheet operations from natural-language requests. The work focuses on spreadsheet-specific planning and execution over real productivity software rather than generic GUI navigation.
