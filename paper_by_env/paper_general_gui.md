- [Rethinking Token Pruning for Historical Screenshots in GUI Visual Agents: Semantic, Spatial, and Temporal Perspectives](https://arxiv.org/abs/2603.26041)
    - Daiqiang Li, Zihao Pan, Zeyu Zhang, Ronghao Chen, Huacan Wang, Honggang Chen, Haiyun Jiang
    - 🏛️ Institutions: Sichuan University, Sun Yat-sen University, Australian National University, Peking University, University of Chinese Academy of Sciences
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [token pruning], [historical screenshots], [random pruning], [recency effect], [empirical study]
    - 📖 TLDR: This paper studies token pruning for historical GUI screenshots and finds that background regions still carry useful state-transition cues, random pruning preserves spatial structure surprisingly well, and allocating larger token budgets to recent screenshots keeps performance nearly unchanged while reducing cost.

- [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](https://arxiv.org/abs/2603.26211)
    - Shrinidhi Kumbhar, Haofu Liao, Srikar Appalaraju, Kunwar Yashraj Singh
    - 🏛️ Institutions: Arizona State University, Amazon (AWS Agentic AI)
    - 📅 Date: March 27, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [diffusion models], [hybrid masking], [bounding-box prediction], [LLaDA-V], [cross-platform]
    - 📖 TLDR: This paper adapts the discrete diffusion model LLaDA-V to GUI grounding and proposes a hybrid masking schedule for bounding-box prediction. Across web, desktop, and mobile benchmarks, the diffusion model outperforms its linear-masked variant and remains competitive with autoregressive VLMs.

- [GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks](https://arxiv.org/abs/2603.25864)
    - Saelyne Yang, Jaesang Yu, Yi-Hao Peng, Kevin Qinghong Lin, Jae Won Cho, Yale Song, Juho Kim
    - 🏛️ Institutions: KAIST, Carnegie Mellon University, University of Oxford, Konkuk University, Google Inc., SkillBench
    - 📅 Date: March 26, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [collaborative assistance], [behavior state detection], [intent prediction], [help prediction], [think-aloud data], [GUIDE]
    - 📖 TLDR: GUIDE studies collaborative GUI assistance rather than pure task automation, using 67.5 hours of think-aloud recordings from 120 novice users across 10 software applications. It benchmarks behavior-state detection, intent prediction, and help prediction, and shows that current multimodal models still struggle to infer what users are doing and when intervention would be useful.

- [CAPTCHA Solving for Native GUI Agents: Automated Reasoning-Action Data Generation and Self-Corrective Training](https://arxiv.org/abs/2603.23559)
    - Yuxi Chen, Haoyu Zhai, Chenkai Wang, Rui Yang, Lingming Zhang, Gang Wang, Huan Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign
    - 📅 Date: March 23, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [CAPTCHA], [reasoning-action data generation], [self-correction], [native GUI agent], [ReCAP]
    - 📖 TLDR: ReCAP is a native GUI agent specialized for interactive CAPTCHA solving. It builds a seven-type CAPTCHA environment, generates large-scale reasoning-action trajectories plus self-correction data from failed attempts, and improves success from about 30% to 80% without sacrificing general GUI-agent performance.

- [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191)
    - Zehao Li, Zhenyu Wu, Yibo Zhao, Bowen Yang, Jingjing Xie, Zhaoyang Liu, Zhoumianze Liu, Kaiming Jin, Jianze Liang, Zonglin Li, Feng Wu, Bowen Zhou, Zun Wang, Zichen Ding
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory, CUHK MMLab, The Hong Kong University of Science and Technology, National University of Singapore
    - 📅 Date: March 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [reinforcement learning], [critic framework], [OmniGUIRewardBench], [milestone decomposition], [OS-Themis]
    - 📖 TLDR: OS-Themis is a scalable critic framework for GUI reward modeling that breaks trajectories into verifiable milestones and audits the evidence chain before issuing a verdict. It improves AndroidWorld training and filtering loops and introduces OmniGUIRewardBench as a cross-platform benchmark for GUI outcome rewards.

- [AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement](https://arxiv.org/abs/2603.17441)
    - Siqi Pei, Liang Tang, Tiaonan Duan, Long Chen, Shuxian Li, Kaer Huang, Yanzhe Jing, Yiqiang Yan, Bo Zhang, Chenghao Jiang, Borui Zhang, Jiwen Lu
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [instruction refinement], [adaptive zoom], [GRPO], [bounding-box prediction], [AdaZoom-GUI]
    - 📖 TLDR: AdaZoom-GUI targets two concrete GUI-grounding bottlenecks: ambiguous natural-language instructions and tiny UI elements in high-resolution screenshots. It combines instruction rewriting with a conditional second-stage zoom-in pass and reports state-of-the-art grounding performance among comparable model sizes.

- [FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair](https://arxiv.org/abs/2603.17826)
    - Ruize Ma, Yilei Jiang, Shilin Zhang, Zheng Ma, Yi Feng, Vincent Ng, Zhi Wang, Xiangyu Yue, Chuanyi Li, Lewei Lu
    - 🏛️ Institutions: Nanjing University, SenseTime, The Chinese University of Hong Kong, University of Texas at Dallas
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [multimodal program repair], [software engineering], [program repair], [failure memory], [visual grounding], [SWE-bench Multimodal], [FailureMem]
    - 📖 TLDR: FailureMem is a multimodal automated program repair framework for settings where repair requires joint reasoning over code, issue text, and GUI screenshots. It combines hybrid workflow-agent control, region-level visual grounding, and a Failure Memory Bank that converts failed repair attempts into reusable guidance, improving resolved rate over GUIRepair on SWE-bench Multimodal.

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
    - 🏛️ Institutions: McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [security], [guardrail], [visual confused deputy], [TOCTOU], [grounding errors], [dual-channel contrastive classification]
    - 📖 TLDR: This paper reframes perception failures in GUI agents as a security problem rather than just a performance issue, formalizing the visual confused deputy where misperceived UI state causes privileged actions on the wrong target. It then proposes a dual-channel guardrail that separately checks the visual target and the agent's textual reasoning to block unsafe executions.

- [Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements](https://arxiv.org/abs/2603.14448)
    - Ziwei Liu, Tao Feng, Borui Kang, Yanbing Yang, Jun Luo
    - 🏛️ Institutions: Department of Computer Science and Technology, Sichuan University, Department of Computer Science and Technology, Tsinghua University, School of Computer Science, Nanjing University, College of Computing and Data Science, Nanyang Technological University
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [inference scaling], [ZoomUI], [instruction rewriting], [progressive zooming]
    - 📖 TLDR: ZoomUI is a training-free GUI grounding method built on the idea that complex interfaces can be decomposed into simpler visual elements that generic MLLMs already understand. It rewrites instructions into element-level visual descriptions and progressively zooms onto candidate UI regions, reaching or surpassing fine-tuned baselines without additional training.

- [Adaptive Vision-Language Model Routing for Computer Use Agents](https://arxiv.org/abs/2603.12823)
    - Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
    - 🏛️ Institutions: vLLM Semantic Router Project, MBZUAI, McGill University, AMD, Red Hat
    - 📅 Date: March 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [VLM routing], [cost-accuracy tradeoff], [semantic routing], [OpenClaw], [AVR], [guardrail escalation]
    - 📖 TLDR: AVR inserts a semantic routing layer between a computer-use agent and a pool of VLMs, selecting the cheapest model that satisfies a target reliability threshold for each action. It projects up to 78% inference-cost reduction while staying close to all-large-model performance, and can escalate risky actions when combined with the Visual Confused Deputy guardrail.

- [Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291)
    - Sibo Zhu, Wenyi Wu, Kun Zhou, Stephen Wang, Biwei Huang
    - 🏛️ Institutions: University of California, San Diego, Abel.ai
    - 📅 Date: March 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [memory], [graph-based retrieval], [self-evolving memory], [HyMEM], [multi-hop retrieval]
    - 📖 TLDR: HyMEM is a graph-based memory system for GUI agents that couples symbolic nodes with continuous trajectory embeddings, supports multi-hop retrieval, and updates itself over time. It substantially boosts open-source 7B/8B GUI agents and can match or surpass stronger closed-source models on several benchmarks.

- [SlowBA: An efficiency backdoor attack towards VLM-based GUI agents](https://arxiv.org/abs/2603.08316)
    - Junxian Li, Tu Lan, Haozhen Tan, Yan Meng, Haojin Zhu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [backdoor attack], [response latency], [reward-level backdoor injection], [popup trigger], [security], [SlowBA]
    - 📖 TLDR: SlowBA studies a backdoor attack on VLM-based GUI agents that targets response efficiency rather than action correctness, using realistic pop-up triggers to induce excessively long reasoning chains. Its two-stage reward-level backdoor injection stays stealthy, preserves task accuracy, and substantially increases latency under trigger conditions.

- [CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning](https://arxiv.org/abs/2603.02951)
    - Zhenquan Yao, Zitong Huang, Yihan Zeng, Jianhua Han, Hang Xu, Chun-Mei Feng, Jianwei Ma, Wangmeng Zuo
    - 🏛️ Institutions: Harbin Institute of Technology, Huawei Noah's Ark Lab, University College Dublin, Peking University
    - 📅 Date: March 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [gradient surgery], [policy entropy], [AndroidControl-CL], [CGL]
    - 📖 TLDR: CGL studies continual GUI learning under app updates, combining supervised adaptation with reinforcement fine-tuning to retain prior interaction skills. It uses policy-entropy-guided SFT weighting and gradient surgery against GRPO anchor gradients, and introduces AndroidControl-CL to benchmark continual adaptation without catastrophic forgetting.

- [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190)
    - Rui Yang, Qianhui Wu, Zhaoyang Wang, Hanyang Chen, Ke Yang, Hao Cheng, Huaxiu Yao, Baoling Peng, Huan Zhang, Jianfeng Gao, Tong Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, Microsoft, University of North Carolina at Chapel Hill
    - 📅 Date: February 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [post-training], [reinforcement learning], [action-aware supervision], [partial verifiability], [GUI reasoning dataset], [GUI-Libra]
    - 📖 TLDR: GUI-Libra is a post-training recipe for native GUI agents that combines curated reasoning data, action-aware supervised fine-tuning, and partially verifiable RL. It targets the mismatch between chain-of-thought reasoning and grounding, and improves both step-level accuracy and end-to-end task completion on web and mobile benchmarks.

- [ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502)
    - Hongbin Zhong, Fazle Faisal, Luis França, Tanakorn Leesatapornwongsa, Adriana Szekeres, Kexin Rong, Suman Nath
    - 🏛️ Institutions: Georgia Institute of Technology, Microsoft Research
    - 📅 Date: February 24, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [programmatic planning], [state machine memory], [crawling agent], [execution agent], [re-grounding fallback], [ActionEngine]
    - 📖 TLDR: ActionEngine shifts GUI agents from reactive step-by-step execution to programmatic planning by building an updatable state-machine memory and synthesizing executable programs from it. Its crawler-plus-executor design reaches 95% success on WebArena Reddit tasks while greatly reducing cost and latency.

- [Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision](https://arxiv.org/abs/2602.14276)
    - A. Said Gurbuz, Sunghwan Hong, Ahmed Nassar, Marc Pollefeys, Peter Staar
    - 🏛️ Institutions: IBM Research, ETH Zurich, KAIST
    - 📅 Date: February 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [dataset], [screen parsing], [dense supervision], [ScreenParse], [UI understanding]
    - 📖 TLDR: This paper argues that sparse grounding supervision is insufficient for GUI understanding and introduces ScreenParse, a large-scale densely annotated screen-parsing dataset. It provides complete UI-element supervision across web screenshots to support richer grounding and UI understanding models.

- [Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization](https://arxiv.org/abs/2602.13653)
    - Yibo Wang, Guangda Huzhang, Yuwei Hu, Yu Xia, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Lijun Zhang
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, Nanjing University, Ovis Team, Alibaba Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [agentic-Q estimation], [step-wise policy optimization], [Ovis2.5-9B], [GUI navigation], [grounding]
    - 📖 TLDR: This paper trains GUI agents with an agentic-Q model that estimates each action's contribution to task completion and a step-wise policy optimization routine decoupled from online interaction. The design keeps data collection manageable while stabilizing updates and improving navigation and grounding performance.

- [Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2602.11858)
    - Lai Wei, Liangbo He, Jun Lan, Lingzhong Dong, Yutong Cai, Siyuan Li, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Ant Group, Zhongguancun Academy, Shanghai Innovation Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [knowledge distillation], [fine-grained perception], [region-to-image distillation], [ZoomBench], [training data generation], [multimodal perception]
    - 📖 TLDR: This paper proposes Region-to-Image Distillation, which teaches a model to internalize zoom-in behavior without requiring explicit crop-and-reason inference at test time. It also introduces ZoomBench and shows stronger fine-grained perception on both perception and GUI-agent benchmarks.

- [How Smart Is Your GUI Agent? A Framework for the Future of Software Interaction](https://arxiv.org/abs/2602.11514)
    - Sidong Feng, Chunyang Chen
    - 🏛️ Institutions: The Chinese University of Hong Kong (Shenzhen), Technical University of Munich
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [autonomy levels], [taxonomy], [trustworthy AI], [software interaction], [GUI Agent Autonomy Levels], [conceptual framework]
    - 📖 TLDR: This paper is a conceptual framing proposal rather than a new agent system. It introduces GUI Agent Autonomy Levels, a six-level taxonomy for describing capability, responsibility, and risk, with the goal of giving the field a clearer language for benchmarking and trustworthy deployment.

- [See, Plan, Snap: Evaluating Multimodal GUI Agents in Scratch](https://arxiv.org/abs/2602.10814)
    - Xingyi Zhang, Yulei Ye, Kaifeng Huang, Wenhao Li, Xiangfeng Wang
    - 🏛️ Institutions: East China Normal University, Tongji University
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [ScratchWorld], [drag-and-drop], [block-based programming], [reasoning-acting gap], [scratch]
    - 📖 TLDR: ScratchWorld evaluates multimodal GUI agents on Scratch program construction tasks that require fine-grained drag-and-drop manipulation. The benchmark exposes a large gap between high-level planning success and low-level GUI execution.

- [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662)
    - Deyang Jiang, Jing Huang, Xuanle Zhao, Lei Chen, Liming Zheng, Fanfan Liu, Haibo Qiu, Peng Shi, Zhixiong Zeng
    - 🏛️ Institutions: Meituan
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [planning], [multi-agent], [tree-structured evolution], [trajectory generation], [TreeCUA], [TreeCUA-DPO]
    - 📖 TLDR: TreeCUA tackles the scaling bottleneck in GUI planning by organizing exploration trajectories as reusable tree structures with verification, summarization, and evaluation. The resulting data supports TreeCUA-DPO, which improves planning quality and out-of-domain generalization.

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL], [curriculum learning]
    - 📖 TLDR: ACuRL studies continual adaptation for computer-use agents in changing environments without human demonstrations. It combines autonomous curriculum generation with CUAJudge-based evaluation to improve both within-environment and cross-environment adaptation while limiting forgetting.

- [POINTS-GUI-G: GUI-Grounding Journey](https://arxiv.org/abs/2602.06391)
    - Zhongyin Zhao, Yuan Liu, Yikun Liu, Haicheng Wang, Le Tian, Xiao Zhou, Yangxiu You, Zilin Yu, Yang Yu, Jie Zhou
    - 🏛️ Institutions: WeChat AI
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [data engineering], [vision encoder training], [verifiable rewards], [POINTS-GUI-G-8B], [ScreenSpot-pro]
    - 📖 TLDR: POINTS-GUI-G studies how to build strong GUI grounding from a base model without strong initial spatial grounding. It attributes gains to multi-source data engineering, improved vision-encoder training, and RL with verifiable rewards, producing competitive results across several grounding benchmarks.

- [Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion](https://arxiv.org/abs/2602.06351)
    - Longhui Ma, Di Zhao, Siwei Wang, Zhao Lv, Miao Wang
    - 🏛️ Institutions: College of Computer Science and Technology, National University of Defense Technology, Intelligent Game and Decision Lab, Academy of Military Sciences
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [multimodal fusion], [attention mechanism], [training-free], [OCR], [Trifuse]
    - 📖 TLDR: Trifuse is a training-free GUI grounding method that fuses MLLM attention, OCR text, and icon caption signals through a consensus-based fusion strategy. It improves grounding across multiple benchmarks without task-specific fine-tuning.

- [SVRepair: Structured Visual Reasoning for Automated Program Repair](https://arxiv.org/abs/2602.06090)
    - Xiaoxuan Tang, Jincheng Wang, Liwei Luo, Jingxuan Xu, Sheng Zhou, Dajun Chen, Wei Jiang, Yong Li
    - 🏛️ Institutions: Ant Group, Zhejiang Key Laboratory of Accessible Perception and Intelligent Systems, Zhejiang University
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI understanding], [multimodal LLM], [program repair], [scene graph], [visual reasoning], [coding agent]
    - 📖 TLDR: SVRepair is a multimodal automated program repair framework that fine-tunes a vision-language model to convert GUI visual artifacts (screenshots, control-flow graphs) into structured semantic scene graphs, enabling a coding agent to localize faults and synthesize patches with state-of-the-art results on SWE-Bench M, MMCode, and CodeVision benchmarks.

- [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995)
    - Sizhe Tang, Rongqian Chen, Tian Lan
    - 🏛️ Institutions: The George Washington University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [test-time compute], [tree search], [MCTS], [alpha-UCT], [OSWorld], [Agent Alpha]
    - 📖 TLDR: Agent Alpha applies step-level MCTS with alpha-UCT exploration, comparison-based evaluation, and diversity-aware expansion to computer-use agents. It improves OSWorld performance substantially over trajectory-level sampling under similar compute.

- [LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios](https://arxiv.org/abs/2602.03255)
    - Tianyu Chen, Chujia Hu, Ge Gao, Ruofeng Yu, Yao Lu
    - 🏛️ Institutions: ShanghaiTech University, Shanghai Artificial Intelligence Laboratory, Rice University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [safety], [MCP], [long-horizon planning], [LLM agent]
    - 📖 TLDR: LPS-Bench is a benchmark evaluating the planning-time safety awareness of MCP-based computer-use agents under long-horizon tasks, covering 65 scenarios across 7 task domains and 9 risk types with both benign and adversarial interactions, revealing substantial safety deficiencies in existing agents.

- [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725)
    - Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, The Chinese University of Hong Kong, Shenzhen
    - 📅 Date: February 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [guardrail], [world model], [risk prediction], [safety], [long-horizon risk], [SafePred]
    - 📖 TLDR: SafePred is a predictive guardrail that uses a world model to simulate future states and assess delayed risk before a computer-use agent acts. It targets long-horizon hazards that reactive safety filters tend to miss.

- [Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction](https://arxiv.org/abs/2602.00575)
    - Chaoqun Cui, Jing Huang, Shijing Wang, Liming Zheng, Qingchao Kong, Zhixiong Zeng
    - 🏛️ Institutions: MAIS, Institute of Automation, Chinese Academy of Sciences, School of Artificial Intelligence, University of Chinese Academy of Sciences, Meituan, School of Computer Science & Technology, Beijing Jiaotong University
    - 📅 Date: January 31, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward modeling], [verification], [proactive interaction], [VAGEN], [OSWorld], [AndroidWorld]
    - 📖 TLDR: VAGEN turns GUI-agent verification into an active interaction problem, using a verifier agent to probe the environment for evidence of task completion instead of relying on passive judgment. This substantially improves verification accuracy on OSWorld and AndroidWorld.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548)
    - Xiaoce Wang, Guibin Zhang, Junzhe Li, Jinzhe Tu, Chun Li, Ming Li
    - 🏛️ Institutions: Department of Computer Science, Tsinghua University, National University of Singapore, Peking University, MSU-BIT-SMBU Joint Research Center of Applied Mathematics, Shenzhen MSU-BIT University, Guangming Laboratory
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [tool use], [tokenization], [curriculum learning], [visual grounding], [data efficiency], [ToolTok]
    - 📖 TLDR: ToolTok treats GUI operations as paths over learnable tool tokens with semantic anchoring and curriculum learning. This makes GUI agents more efficient and generalizable, reaching competitive performance with far less training data than other post-training methods.

- [Where Not to Learn: Prior-Aligned Training with Subset-based Attribution Constraints for Reliable Decision-Making](https://arxiv.org/abs/2602.07008)
    - Ruoyu Chen, Shangquan Sun, Xiaoqing Guo, Sanyi Zhang, Kangwei Liu, Shiming Liu, Zhangcheng Wang, Qunli Zhang, Hua Zhang, Xiaochun Cao
    - 🏛️ Institutions: Institute of Information Engineering, Chinese Academy of Sciences, University of Chinese Academy of Sciences, College of Computing and Data Science, Nanyang Technological University, Department of Computer Science, Hong Kong Baptist University, Communication University of China, Huawei, University of Science and Technology of China, School of Cyber Science and Technology, Shenzhen Campus of Sun Yat-sen University
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [training], [attribution], [subset-based attribution constraints], [human prior alignment], [reliability], [explainability]
    - 📖 TLDR: This paper proposes prior-aligned training with subset-based attribution constraints, penalizing models for relying on evidence that conflicts with human priors. It improves both accuracy and decision reasonability on image classification and GUI-agent click decision tasks.

- [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528)
    - Hongze Mi, Yibo Feng, WenJie Lu, Song Cao, Jinyuan Li, Yanming Li, Xuelin Zhang, Haotian Luo, Songyang Peng, He Cui, Tengfei Tian, Jun Fang, Hua Chai, Naiqiang Tan
    - 🏛️ Institutions: Didichuxing Co. Ltd, The Chinese University of Hong Kong, Shenzhen, Tianjin University, Sun Yat-sen University, Fudan University
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [memory system], [training-free], [self-regulating memory], [multi-app], [Darwinian Memory], [trajectory pruning]
    - 📖 TLDR: Darwinian Memory is a training-free memory system that treats agent memories as an evolving ecosystem, selecting and pruning trajectories through utility-driven competition. It improves success rate and execution stability on real-world multi-app GUI benchmarks.

- [SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization](https://arxiv.org/abs/2601.22491)
    - Jinyang Wu, Changpeng Yang, Yuhao Shen, Fangzhi Xu, Bolin Ni, Chonghua Liao, Yuchen Liu, Hongzhen Wang, Shuai Nie, Shuai Zhang, Haoran Luo, Jiaming Xu
    - 🏛️ Institutions: Tsinghua University, Xiaomi Corporation, Zhejiang University, Nanyang Technological University, Institute of Automation, Chinese Academy of Sciences
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [tiered rewards], [reward shaping], [GUI grounding], [planning], [SSL]
    - 📖 TLDR: SSL replaces binary verifier rewards with progressively amplified tiered rewards that distinguish higher- and lower-quality successful trajectories. Across GUI perception, short- and long-horizon planning, and reasoning benchmarks, it improves optimization stability and reaches up to 2.5x better sample efficiency than binary-reward baselines.

- [BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://arxiv.org/abs/2601.21352)
    - Ziyu Lu, Tengjin Weng, Yiying Yang, Yuhang Zhao, Xinxin Huang, Wenhao Jiang
    - 🏛️ Institutions: Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shenzhen University, Guangdong University of Technology
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [backtracking], [DFS planning], [task tracking], [error recovery], [OSWorld], [BEAP-Agent]
    - 📖 TLDR: BEAP-Agent formulates long-horizon GUI execution as depth-first search and adds explicit multi-level backtracking when the agent commits to a wrong exploration branch. Its Planner, Executor, and Tracker jointly support state rollback and task updates, improving recovery on OSWorld.

- [Continual GUI Agents](https://arxiv.org/abs/2601.20732)
    - Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng
    - 🏛️ Institutions: Department of Computer Science and Technology, Tsinghua University, College of Computer Science, Zhejiang University, Photogrammetry and Remote Sensing Lab, ETH Zurich, College of Computer Science, Beijing University of Posts and Telecommunications
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement fine-tuning], [domain shift], [resolution shift], [GUI-AiF]
    - 📖 TLDR: This paper defines continual GUI agents as agents that must keep grounding accurately while interface domains and resolutions shift over time. It introduces GUI-AiF, a reinforcement fine-tuning method with anchoring-point and anchoring-region rewards, and reports stronger continual-domain and continual-resolution performance than prior baselines.

- [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197)
    - Shaokang Wang, Pei Fu, Ruoceng Zhang, Shaojie Zhang, Xiuwen Xi, Jiahui Yang, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [critic model], [test-time scaling], [data flywheel], [Intuitive Critic Model], [GAIA]
    - 📖 TLDR: GAIA trains an Intuitive Critic Model that judges the immediate correctness of candidate GUI actions before execution. It then uses a data flywheel that recycles agent-generated positive and negative action samples to iteratively improve the critic, yielding better test-time performance for both open-source and closed-source GUI agents.

- [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE)
    - Bin Kang, Shaoguo Wen, Yifei Bi, Shunlong Wu, Xinbin Yuan, Rui Shao, Junle Wang, Zhuotao Tian
    - 🏛️ Institutions: Chengdu Institute of Computer Applications, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Tencent Turing Lab, Georgia Institute of Technology, Tsinghua University, Nankai University, Shenzhen Loop Area Institute
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [benchmark], [long-horizon tasks], [reflection], [rollback], [LongGUIBench], [LongHorizonUI]
    - 📖 TLDR: LongHorizonUI targets error accumulation in long-horizon GUI control by combining indexed multimodal perception, structured reflective decision-making, and rollback-based compensatory execution. It also introduces LongGUIBench for tasks longer than 15 steps across games and complex applications, and reports substantial gains on long-horizon evaluation while staying competitive on public benchmarks.

- [GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents](https://arxiv.org/abs/2601.18842)
    - Yanxi Wang, Zhiling Zhang, Wenbo Zhou, Weiming Zhang, Jie Zhang, Qiannan Zhu, Yu Shi, Shuxin Zheng, Jiyan He
    - 🏛️ Institutions: Beijing Normal University, Zhongguancun Academy, University of Science and Technology of China, A*STAR, Zhongguancun Institution of Artificial Intelligence
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [privacy recognition], [privacy protection], [privacy grounding], [GUIGuard], [GUIGuard-Bench]
    - 📖 TLDR: GUIGuard formulates privacy-preserving GUI automation as privacy recognition, privacy protection, and protected task execution. It also introduces GUIGuard-Bench, a cross-platform benchmark with 630 trajectories and 13,830 screenshots annotated for region-level privacy grounding, risk level, privacy category, and task necessity, and shows that current models still recognize private content very poorly.

- [MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux](https://arxiv.org/abs/2601.13060)
    - Zecheng Li, Zhihui Cao, Wenke Huang, Yudong Zhang, Keying Qi, Rui Wang, Zeyu Zheng, Jian Zhao, Hao Zhu, Hengxin Wu, Yuran Wang, Guitao Fan, Guokun Wu, Yicong Liu, Zhilin Gao, Haikun Xu, He Yang, Minqi Xiang, Xingyu Liu, Zuojian Wang
    - 🏛️ Institutions: Honor Device Co., Ltd.
    - 📅 Date: January 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [multi-agent system], [data construction], [data reflux], [MagicGUI-RMS]
    - 📖 TLDR: MagicGUI-RMS combines a domain-specific reward model with a general-purpose reward model to score GUI trajectories, propose corrections, and feed improved data back into later training rounds. It also introduces an automated reward-data construction pipeline and reports gains in task accuracy and behavioral robustness.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: University of Science and Technology of China, Institute of Artificial Intelligence (TeleAI), China Telecom, Shanghai Innovation Institute, Shanghai Jiao Tong University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [active perception], [tool-augmented perception], [ScreenSpot-pro], [GUI-Eyes]
    - 📖 TLDR: GUI-Eyes frames GUI grounding as active perception, letting the agent learn when and how to call tools such as cropping and zooming inside a two-stage reasoning process. It pairs that policy with a spatially continuous reward for tool use and reaches 44.8% grounding accuracy on ScreenSpot-Pro using only 3k labeled samples.

- [Compress to Focus: Efficient Coordinate Compression for Policy Optimization in Multi-Turn GUI Agents](https://arxiv.org/abs/2601.11631)
    - Yurun Song, Jiong Yin, Rongjunchen Zhang, Ian G. Harris
    - 🏛️ Institutions: HiThink Research, University of California, Irvine, Hangzhou Dianzi University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [policy optimization], [coordinate compression], [Coordinate-Aware Spatial Compression], [distance-based advantage], [CCPO]
    - 📖 TLDR: CCPO tackles context inflation in multi-turn GUI agents by compressing historical screenshots around task-relevant coordinates collected across rollouts. Its Coordinate-Aware Spatial Compression and distance-based advantage improve both compression quality and grounding, reaching state-of-the-art results with up to 55% token compression and 3.8x training speedup.

- [V2P: Visual Attention Calibration for GUI Grounding via Background Suppression and Center Peaking](https://arxiv.org/abs/2601.06899)
    - Jikai Chen, Long Chen, Dong Wang, Qinglin Su, Zhixuan Chu, Bingguang Hao, Leilei Gan, Chenyi Zhuang, Jinjie Gu
    - 🏛️ Institutions: Zhejiang University, Inclusion AI, Ant Group
    - 📅 Date: January 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [visual attention], [background suppression], [Fitts' law], [V2P]
    - 📖 TLDR: V2P improves attention-based GUI grounding by suppressing irrelevant background regions and using a Fitts’ Law-inspired Gaussian peak to emphasize an element’s actionable center over its edges. The paper reports 92.4% on ScreenSpot-v2 and 52.5% on ScreenSpot-Pro, with ablations confirming both components matter.

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu
    - 🏛️ Institutions: Nanjing University, Peking University, Microsoft Research Asia
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [RLVR], [off-policy assimilation], [BEPA], [OSWorld]
    - 📖 TLDR: BEPA improves end-to-end GUI-agent training with verifiable rewards by turning scarce off-policy expert traces into policy-aligned guidance through self-rolled reachable trajectories and a dynamically updated per-task cache. On OSWorld-Verified it raises UI-TARS-1.5-7B from 22.87% to 32.13%, with additional gains on MMBench-GUI and Online-Mind2Web.

- [Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning](https://arxiv.org/abs/2601.03641)
    - Zheng Wu, Xingyu Lou, Xinbei Ma, Yansi Li, Weiwen Liu, Weinan Zhang, Jun Wang, Zhuosheng Zhang
    - 🏛️ Institutions: School of Computer Science, Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [parameter fusion], [catastrophic forgetting], [geometric consensus], [Agent-Dice]
    - 📖 TLDR: Agent-Dice addresses the stability-plasticity dilemma in agent continual learning by separating shared knowledge from task-specific interference during parameter fusion. Its two-stage method combines geometric consensus filtering with curvature-based importance weighting, and the paper reports strong continual-learning results for both GUI and tool-use agents.

- [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009)
    - Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu, Vineeth N Balasubramanian
    - 🏛️ Institutions: Indian Institute of Technology, Bombay, Indian Institute of Technology, Hyderabad
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [slow-fast reasoning], [visual grounding], [latent thinking], [adaptive perception], [iSHIFT]
    - 📖 TLDR: iSHIFT is a 2.5B GUI agent that combines latent thinking with perception-control tokens so it can switch between a fast global mode and a slower grounding-heavy mode. The paper positions this as a way to allocate reasoning depth and visual focus adaptively while still matching state-of-the-art results on multiple GUI benchmarks.

- [GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection](https://arxiv.org/abs/2512.09396)
    - Zishu Wei, Qixiang Ma, Xavier Hu, Yuhang Liu, Hui Zang, Yudong Zhao, Tao Wang, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Huawei Technologies Ltd.
    - 📅 Date: December 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [information-joint reasoning], [group reflection], [multi-model collaboration], [decision making], [GAIR]
    - 📖 TLDR: GAIR builds a GUI automation system by combining several GUI-specific MLLMs with a general-purpose decision model that jointly reasons over their observations. When evidence is insufficient, its group-reflection stage sends targeted follow-up instructions back to the specialist models, and the framework reports gains on web, desktop, and mobile GUI benchmarks such as UI-I2E-Bench and ScreenSpot.

- [MVP: Multiple View Prediction Improves GUI Grounding](https://arxiv.org/abs/2512.08529)
    - Yunzhu Zhang, Zeyu Pan, Zhengwen Zeng, Shuheng Shen, Changhua Meng, Linchao Zhu
    - 🏛️ Institutions: Zhejiang University, Hangzhou Dianzi University, Ant Group
    - 📅 Date: December 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [multi-view inference], [prediction instability], [coordinate clustering], [MVP]
    - 📖 TLDR: MVP studies prediction instability in GUI grounding, where tiny visual perturbations can flip coordinate predictions between correct and incorrect. It improves training-free grounding by proposing attention-guided cropped views and clustering the resulting coordinate predictions, yielding consistent gains on ScreenSpot-Pro, UI-Vision, and OS-World-G.

- [Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding](https://arxiv.org/abs/2512.05941)
    - Zhiyuan Jiang, Shenghao Xie, Wenyi Li, Wenqiang Zu, Peihang Li, Jiahao Qiu, Siqi Pei, Lei Ma, Tiejun Huang, Mengdi Wang, Shilong Liu
    - 🏛️ Institutions: Xi’an Jiaotong University, Princeton University, Peking University, University of Chinese Academy of Sciences, The University of Hong Kong, Michigan State University
    - 📅 Date: December 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [zoom], [test-time scaling], [ZoomClick], [GUIZoom-Bench]
    - 📖 TLDR: This paper studies zooming as a test-time prior for GUI grounding and proposes ZoomClick, which decides when to zoom, how far to zoom, and when to return to the original view during localization. It also introduces GUIZoom-Bench and reports stronger grounding results across several mainstream benchmarks.

- [GUI Exploration Lab: Enhancing Screen Navigation in Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2512.02423)
    - Haolong Yan, Yeqing Shen, Xin Huang, Jia Wang, Kaijun Tan, Zhixuan Liang, Hongxin Li, Zheng Ge, Osamu Yoshie, Si Li, Xiangyu Zhang, Daxin Jiang
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, StepFun, Waseda University, Institute of Automation, Chinese Academy of Sciences
    - 📅 Date: December 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [screen navigation], [simulation environment], [reinforcement learning], [exploration strategy], [GUI Exploration Lab]
    - 📖 TLDR: GUI Exploration Lab is a simulation engine for studying screen navigation, exposing full screen and navigation-graph structure so agents can be trained and evaluated without proprietary GUI environments. The paper compares supervised fine-tuning, single-turn RL, and multi-turn RL, and finds that multi-turn RL is what most clearly induces exploratory navigation behavior.

- [HiconAgent: History Context-aware Policy Optimization for GUI Agents](https://arxiv.org/abs/2512.01763)
    - Xurui Zhou, Gongwei Chen, Yuquan Xie, Zaijing Li, Kaiwen Zhou, Shuai Wang, Shuo Yang, Zhuotao Tian, Rui Shao
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Huawei Noah’s Ark Lab
    - 📅 Date: December 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [history usage], [Dynamic Context Sampling], [Anchor-guided History Compression], [HiconAgent]
    - 📖 TLDR: HiconAgent studies how GUI agents should use historical context during sequential navigation instead of always keeping a fixed full history. Its HCPO training recipe combines Dynamic Context Sampling with Anchor-guided History Compression, and the resulting 3B model improves GUI-Odyssey while matching or approaching larger baselines on AndroidControl and AITW at lower compute cost.

- [DrawingBench: Evaluating Spatial Reasoning and UI Interaction Capabilities of Large Language Models through Mouse-Based Drawing Tasks](https://arxiv.org/abs/2512.01174)
    - Hyunjun Kim, Sooyoung Ryu
    - 🏛️ Institutions: Independent
    - 📅 Date: December 01, 2025
    - 📑 Publisher: AAAI 2026 TrustAgent Workshop
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [spatial reasoning], [mouse-based drawing], [verifiable evaluation], [multi-turn feedback], [DrawingBench]
    - 📖 TLDR: DrawingBench evaluates agentic models through mouse-based drawing tasks that require issuing low-level GUI actions on a canvas UI rather than answering static spatial questions. It provides 250 prompts, deterministic rule-based scoring, and multi-turn external feedback, showing both strong baseline performance and clear failure modes in tool-state management and long-horizon control.

- [MPR-GUI: Benchmarking and Enhancing Multilingual Perception and Reasoning in GUI Agents](https://arxiv.org/abs/2512.00756)
    - Ruihan Chen, Qiming Li, Xiaocheng Feng, Xiaoliang Yang, Weihong Zhong, Yuxuan Gu, Zekun Zhou, Bing Qin
    - 🏛️ Institutions: Harbin Institute of Technology, Peng Cheng Laboratory
    - 📅 Date: November 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [multilingual], [cross-lingual], [perception and reasoning], [MPR-GUI-Bench], [GUI-XLI]
    - 📖 TLDR: MPR-GUI studies the gap between English and non-English GUI understanding by introducing a fine-grained multilingual benchmark for GUI perception and reasoning. It also proposes GUI-XLI, a hidden-state intervention method for cross-lingual transfer, and reports average multilingual gains of 6.5%.

- [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235)
    - Zehao Deng, Tianjie Ju, Zheng Wu, Zhuosheng Zhang, Gongshen Liu
    - 🏛️ Institutions: Soochow University, Shanghai Jiao Tong University
    - 📅 Date: November 27, 2025
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [long-horizon tasks], [state tracking], [task decomposition], [CES]
    - 📖 TLDR: This paper targets long-horizon GUI automation by training high-level scheduling modules instead of a single end-to-end executor. Its CES framework separates coordination, execution, and state tracking, and uses execution-feedback reinforcement learning to improve planning and task-state management across different low-level executors.

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Zeyi Liao, Yadong Lu, Boyu Gou, Huan Sun, Ahmed Awadallah
    - 🏛️ Institutions: The Ohio State University, Microsoft Research, Redmond
    - 📅 Date: November 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [dataset], [benchmark], [text dragging], [GUI-Drag], [ScreenDrag]
    - 📖 TLDR: This paper expands GUI grounding beyond click actions by focusing on text dragging, a common but previously underexplored mouse interaction. It introduces the GUI-Drag training set and the ScreenDrag benchmark, and shows that continual training for dragging can improve drag performance without sacrificing click grounding.

- [VideoAgentTrek: Computer Use Pretraining from Unlabeled Videos](https://arxiv.org/abs/2510.19488)
    - Dunjie Lu, Yiheng Xu, Junli Wang, Haoyuan Wu, Xinyuan Wang, Zekun Wang, Junlin Yang, Hongjin Su, Jixuan Chen, Junda Chen, Yuchen Mao, Jingren Zhou, Junyang Lin, Binyuan Hui, Tao Yu
    - 🏛️ Institutions: Google Cloud AI Research, The Ohio State University
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [pretraining], [video mining], [inverse dynamics], [Video2Action], [VideoAgentTrek]
    - 📖 TLDR: VideoAgentTrek studies how to pretrain computer-use agents from passive screen recordings instead of manually labeled trajectories. Its Video2Action pipeline recovers action boundaries and structured parameters from 39,000 tutorial videos, yielding 1.52 million steps that improve both OSWorld-Verified and AgentNetBench after continued pretraining.

- [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892)
    - Kai Mei, Jiang Guo, Shuaichen Chang, Mingwen Dong, Dongkyu Lee, Xing Niu, Jiarong Jiang
    - 🏛️ Institutions: Rutgers University, AWS Agentic AI
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [world model], [tutorial retrieval], [future state prediction], [OSWorld], [WebArena], [R-WoM]
    - 📖 TLDR: This paper tests whether LLMs can act as world models for computer-use agents and finds that simulation quality degrades sharply on full-procedure planning even when short-range prediction remains reasonable. R-WoM addresses this by grounding simulated rollouts with retrieved up-to-date tutorials, improving performance on OSWorld and WebArena, especially on longer-horizon tasks.

- [GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding](https://arxiv.org/abs/2510.04039)
    - Bin Lei, Nuo Xu, Ali Payani, Mingyi Hong, Chunhua Liao, Yu Cao, Caiwen Ding
    - 🏛️ Institutions: University of Minnesota, Cisco Research, Lawrence Livermore National Labs
    - 📅 Date: October 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [image-grounded reasoning], [iterative focus refinement], [ScreenSpot-pro], [GUI-Spotlight]
    - 📖 TLDR: GUI-Spotlight is a GUI grounding model that performs image-grounded reasoning by iteratively invoking specialized tools to narrow attention to the relevant screen region. Trained with only 18.5K examples, it reaches 52.8% accuracy on ScreenSpot-Pro, outperforming prior 7B grounding models trained on much larger datasets.

- [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670)
    - Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
    - 🏛️ Institutions: Microsoft Research AI Frontiers, Microsoft AI Red Team, University of California, Riverside, NVIDIA
    - 📅 Date: October 02, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [blind goal-directedness], [safety benchmark], [OSWorld], [thought-action disconnect], [BLIND-ACT]
    - 📖 TLDR: This paper identifies Blind Goal-Directedness (BGD), where computer-use agents continue pursuing goals despite feasibility, safety, reliability, or context concerns. It introduces BLIND-ACT, a 90-task benchmark on OSWorld, and finds high average BGD rates across frontier models even after prompting-based mitigations.

- [GUI-KV: Efficient GUI Agents via KV Cache with Spatio-Temporal Awareness](https://arxiv.org/abs/2510.00536)
    - Kung-Hsiang Huang, Haoyi Qiu, Yutong Dai, Caiming Xiong, Chien-Sheng Wu
    - 🏛️ Institutions: Salesforce AI Research, University of California, Los Angeles
    - 📅 Date: October 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [KV cache compression], [spatio-temporal redundancy], [spatial saliency], [AgentNetBench], [GUI-KV]
    - 📖 TLDR: GUI-KV is a training-free KV-cache compression method for GUI agents that exploits two GUI-specific signals: spatial saliency within a frame and temporal redundancy across frames. It closely matches or beats full-cache performance on standard benchmarks, and in a 5-screenshot AgentNetBench setting cuts decoding FLOPs by 38.9% while improving step accuracy.

- [SCUBA: Salesforce Computer Use Benchmark](https://openreview.net/forum?id=bkjKnO9s7T)
    - Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: September 30, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [CRM workflows], [Salesforce sandbox], [milestone evaluation], [SCUBA]
    - 📖 TLDR: SCUBA is a benchmark for computer-use agents on Salesforce customer-relationship-management workflows, with 300 task instances derived from real user interviews across administrator, sales, and service personas. It runs in Salesforce sandbox environments with interpretable milestone evaluation and shows that enterprise tasks remain much harder than standard CUA benchmarks, especially for open models in zero-shot settings.

- [Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents](https://arxiv.org/abs/2509.26539)
    - Zhen Yang, Zi-Yi Dou, Di Feng, Forrest Huang, Anh Nguyen, Keen You, Omar Attia, Yuhao Yang, Michael Feng, Haotian Zhang, Ram Ramrakhya, Chao Jia, Jeffrey Nichols, Alexander Toshev, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [on-device agent], [3B model], [visual tool-use], [ScreenSpot-V2], [OSWorld-G], [Ferret-UI Lite]
    - 📖 TLDR: Ferret-UI Lite is a compact 3B end-to-end GUI agent for on-device use across mobile, web, and desktop environments. Built from a mixed real-and-synthetic data recipe plus chain-of-thought, visual tool-use, and reward-designed RL, it reaches competitive grounding scores and navigation success despite the constraints of small on-device models.

- [Scaling Synthetic Task Generation for Agents via Exploration](https://arxiv.org/abs/2509.25047)
    - Ram Ramrakhya, Andrew Szot, Omar Attia, Yuhao Yang, Anh Nguyen, Bogdan Mazoure, Zhe Gan, Harsh Agrawal, Alexander Toshev
    - 🏛️ Institutions: Apple
    - 📅 Date: September 29, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [task generation], [environment exploration], [synthetic tasks], [AutoPlay], [Android apps], [Ubuntu apps]
    - 📖 TLDR: AutoPlay is a scalable task-generation pipeline that first explores interactive environments to uncover functionalities and then synthesizes diverse, executable, verifiable tasks grounded in those states. It generates 20k Android tasks and 10k Ubuntu tasks, enabling large-scale post-training and additional RL gains for UI agents without human annotation.

- [ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration](https://arxiv.org/abs/2509.21823)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuqing Yang, Yuanchun Li, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Nanyang Technological University, Microsoft Research, Institute for AI Industry Research (AIR), Tsinghua University, Hong Kong University of Science and Technology
    - 📅 Date: September 26, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [proactive reward], [state probing], [reasoner-actor collaboration], [chain-of-claims], [reward accuracy], [ProRe]
    - 📖 TLDR: ProRe turns GUI-agent reward assignment into an active probing process: a general-purpose reasoner schedules targeted checks and evaluator agents interact with the environment to gather extra evidence before scoring a trajectory. On more than 3,000 trajectories it improves reward accuracy and F1 over static judges, and those rewards also improve downstream policy-agent success rates.

- [BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent](https://arxiv.org/abs/2509.15566)
    - Shaojie Zhang, Ruoceng Zhang, Pei Fu, Shaokang Wang, Jiahui Yang, Xin Du, Shiqi Cui, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: September 19, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [blink-think-link], [blink data generation], [BTL Reward], [process-and-outcome reward], [human-GUI interaction], [BTL-UI]
    - 📖 TLDR: BTL-UI models GUI interaction as Blink, Think, and Link phases inspired by human visual attention, planning, and action. It adds a blink-oriented data generation pipeline and a rule-based reward that supervises both process and outcome, and reports competitive results on both static GUI understanding and dynamic interaction benchmarks.

- [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://arxiv.org/abs/2509.02322)
    - Longrong Yang, Zhixiong Zeng, Yufeng Zhong, Huang Jing, Liming Zheng, Lei Chen, Haibo Qiu, Zequn Qin, Lin Ma, Xi Li
    - 🏛️ Institutions: College of Computer Science and Technology, Zhejiang University, Meituan Technology, School of Software Technology, Zhejiang University
    - 📅 Date: September 02, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [generalist agent], [layer-heterogeneous MoE], [unified action space], [GUI-embodied transfer], [2D and 3D worlds], [OmniActor]
    - 📖 TLDR: OmniActor studies a single agent that can act in both GUI-based 2D environments and embodied 3D settings. It uses a layer-heterogeneous MoE design to share shallow GUI/embodied representations while separating deeper action-specific parameters, and combines that structure with unified action spaces and mixed training data to improve both GUI and embodied performance.

- [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)
    - Haoming Wang, Haoyang Zou, Huatong Song, Jiazhan Feng, Junjie Fang, Junting Lu, Longxiang Liu, Qinyu Luo, Shihao Liang, Shijue Huang, Wanjun Zhong, Yining Ye, Yujia Qin, Yuwen Xiong, Yuxin Song, Zhiyong Wu, Aoyan Li, Bo Li, Chen Dun, Chong Liu, Daoguang Zan, Fuxing Leng, Hanbin Wang, Hao Yu, Haobin Chen, Hongyi Guo, Jing Su, Jingjia Huang, Kai Shen, Kaiyu Shi, Lin Yan, Peiyao Zhao, Pengfei Liu, Qinghao Ye, Renjie Zheng, Shulin Xin, Wayne Xin Zhao, Wen Heng, Wenhao Huang, Wenqian Wang, Xiaobo Qin, Yi Lin, Youbin Wu, Zehui Chen, Zihao Wang, Baoquan Zhong, Xinchun Zhang, Xujing Li, Yuanfan Li, Zhongkai Zhao, Chengquan Jiang, Faming Wu, Haotian Zhou, Jinlin Pang, Li Han, Qi Liu, Qianli Ma, Siyao Liu, Songhua Cai, Wenqi Fu, Xin Liu, Yaohui Wang, Zhi Zhang, Bo Zhou, Guoliang Li, Jiajun Shi, Jiale Yang, Jie Tang, Li Li, Qihua Han, Taoran Lu, Woyu Lin, Xiaokang Tong, Xinyao Li, Yichi Zhang, Yu Miao, Zhengxuan Jiang, Zili Li, Ziyuan Zhao, Chenxin Li, Dehua Ma, Feng Lin, Ge Zhang, Haihua Yang, Hangyu Guo, Hongda Zhu, Jiaheng Liu, Junda Du, Kai Cai, Kuanye Li, Lichen Yuan, Meilan Han, Minchao Wang, Shuyue Guo, Tianhao Cheng, Xiaobo Ma, Xiaojun Xiao, Xiaolong Huang, Xinjie Chen, Yidi Du, Yilin Chen, Yiwen Wang, Zhaojian Li, Zhenzhu Yang, Zhiyuan Zeng, Chaolin Jin, Chen Li, Hao Chen, Haoli Chen, Jian Chen, Qinghao Zhao, Guang Shi
    - 🏛️ Institutions: ByteDance Seed
    - 📅 Date: September 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [data flywheel], [multi-turn reinforcement learning], [hybrid GUI-terminal environment], [unified sandbox], [online-Mind2Web], [UI-TARS-2]
    - 📖 TLDR: UI-TARS-2 studies how to scale native GUI agents with a data flywheel, stabilized multi-turn reinforcement learning, hybrid GUI-plus-terminal environments, and a unified sandbox. It reports strong results across GUI benchmarks, games, information-seeking tasks, and software-engineering settings, and also analyzes training dynamics and parameter interpolation during RL.

- [A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants](https://arxiv.org/abs/2510.06223)
    - Hans G.W. van Dam
    - 🏛️ Institutions: uxx.ai
    - 📅 Date: August 31, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [MCP], [MVVM], [GUI tree router], [speech-enabled assistants], [voice accessibility]
    - 📖 TLDR: This paper proposes an MCP-driven GUI architecture that lets existing applications expose navigation structure and action semantics to speech-enabled assistants through ViewModels and a GUI tree router. The design targets multimodal interaction with aligned spoken and visual feedback, and the paper also reports a small evaluation of locally deployable open-weight models for this setting.

- [You Don’t Know Until You Click: Automated GUI Testing for Production-Ready Software Evaluation](https://arxiv.org/abs/2508.14104)
    - Yutong Bian, Xianhao Lin, Yupeng Xie, Tianyang Liu, Mingchen Zhuge, Siyuan Lu, Haoming Tang, Jinlin Wang, Jiayi Zhang, Jiaqi Chen, Xiangru Tang, Yongxin Ni, Sirui Hong, Chenglin Wu
    - 🏛️ Institutions: DeepWisdom, Fudan University, HKUST(GZ), UC San Diego, KAUST, Westlake University, Stanford University, Yale University, NUS
    - 📅 Date: August 17, 2025
    - 📑 Publisher: SEA @ NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [RealDevWorld], [RealDevBench], [AppEvalPilot], [agent-as-a-judge], [interactive GUI testing], [production-ready software]
    - 📖 TLDR: RealDevWorld is an evaluation framework for repository-scale software generation that judges whether produced applications actually work when interacted with through their GUIs. It pairs a 194-task benchmark, RealDevBench, with AppEvalPilot, an agent-as-a-judge system for functional, visual, and runtime evaluation, and reports strong alignment with expert human assessments.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, School of Computer Science, MoE Key Lab of Artificial Intelligence, SJTU AI Institute, Shanghai Jiao Tong University, Jiangsu Key Lab of Language Computing, Suzhou Laboratory
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [progress reward], [dense rewards], [LCS self-annotation], [ProgRM]
    - 📖 TLDR: ProgRM studies how to replace coarse outcome-only rewards with dense step-level progress signals for GUI-agent reinforcement learning. It uses an LCS-based self-annotation method to assign progress labels from successful trajectories and shows that progress rewards outperform outcome reward models across GUI benchmarks.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Gaoling School of Artificial Intelligence, Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [reinforcement learning], [fast thinking template], [difficulty-aware scaling], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets and Benchmarks Track (Spotlight)
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [benchmark], [GUI grounding], [OSWorld-G], [Jedi], [compositional generalization]
    - 📖 TLDR: This paper targets the mismatch between simplified grounding benchmarks and real computer-use grounding. It introduces the OSWorld-G benchmark and the 4M-example Jedi grounding dataset generated by UI decomposition and synthesis, showing that better grounding data transfers into large gains on both grounding benchmarks and downstream agent performance.

- [GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents](https://arxiv.org/abs/2505.12842)
    - Zheng Wu, Pengzhou Cheng, Zongru Wu, Lingzhong Dong, Zhuosheng Zhang
    - 🏛️ Institutions: School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [out-of-distribution detection], [gaussian embedding modeling], [capability boundary], [safety], [GEM]
    - 📖 TLDR: GEM studies out-of-distribution instruction detection for GUI agents whose capability boundaries are hard to characterize in evolving interfaces. It models embedding-distance clusters with a Gaussian mixture and improves OOD detection accuracy across mobile, desktop, and web settings, while also boosting step-wise success by escalating OOD cases to a stronger cloud model.

- [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: VCIP, School of Computer Science, NKU, vivo Mobile Communication Co., Ltd, National University of Singapore, Fudan University, East China University of Science and Technology
    - 📅 Date: May 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [GUI grounding], [dense policy gradient], [self-evolutionary finetuning], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?](https://arxiv.org/abs/2505.10924)
    - Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
    - 🏛️ Institutions: Carnegie Mellon University, The Chinese University of Hong Kong, KAUST, Johns Hopkins University, Nanyang Technological University, The Hong Kong University of Science and Technology
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [safety], [security], [threat taxonomy], [defense taxonomy]
    - 📖 TLDR: This survey systematizes safety and security risks in computer-using agents, from reasoning failures and multimodal vulnerabilities to risks introduced by multi-component agent stacks. It organizes the field around threat categories, defensive strategies, and the benchmarks and datasets currently used to study secure CUA deployment.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: University of Michigan, LG AI Research
    - 📅 Date: May 01, 2025
    - 📑 Publisher: ICCV 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [RegionFocus], [visual test-time scaling], [image-as-map], [visual search]
    - 📖 TLDR: This paper frames GUI grounding as an iterative visual search process rather than a single full-screen prediction. Its RegionFocus method repeatedly zooms into promising regions and uses an image-as-map view to expose landmarks and action candidates, improving grounding on ScreenSpot-Pro and WebVoyager without retraining the base model.

- [A Survey on GUI Agents with Foundation Models Enhanced by Reinforcement Learning](https://arxiv.org/abs/2504.20464)
    - Jiahao Li, Kaer Huang
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: April 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [reinforcement learning], [MDP formulation], [training taxonomy], [perception-planning-acting]
    - 📖 TLDR: This survey reviews GUI agents through a reinforcement-learning lens by formalizing GUI interaction as an MDP and organizing prior work around perception, planning, and acting modules. Its main contribution is a training-oriented taxonomy connecting prompt-based methods, supervised fine-tuning, and RL-style policy learning for GUI agents.

- [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)
    - Yuhang Liu, Pengxiang Li, Congkai Xie, Xavier Hu, Xiaotian Han, Shengyu Zhang, Hongxia Yang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Dalian University of Technology, Reallm Labs, The Hong Kong Polytechnic University
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [reasoning injection], [sub-goal guidance], [error recovery], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: InfiGUI-R1 is trained to shift GUI agents from reactive action prediction toward explicit deliberative reasoning. Its Actor2Reasoner pipeline first distills cross-modal spatial reasoning into the model, then uses reinforcement learning with sub-goal guidance and failure-recovery scenarios to strengthen planning and recovery.

- [TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents](https://arxiv.org/abs/2504.12679)
    - Bofei Zhang, Zirui Shang, Zhi Gao, Wang Zhang, Rui Xie, Xiaojian Ma, Tao Yuan, Xinxiao Wu, Song-Chun Zhu, Qing Li
    - 🏛️ Institutions: State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing Key Laboratory of Intelligent Information Technology, School of Computer Science & Technology, Beijing Institute of Technology, School of Intelligence Science and Technology, Peking University, Shanghai Jiao Tong University, Department of Automation, Tsinghua University
    - 📅 Date: April 17, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [tutorial mining], [trajectory generation], [GUI-Net], [TongUI]
    - 📖 TLDR: TongUI turns multimodal web tutorials into large-scale GUI-agent training trajectories by crawling and processing tutorial videos and articles. The resulting GUI-Net dataset spans 143K trajectories across five operating systems and more than 200 applications, and fine-tuning on it improves generalized GUI-agent performance.

- [UI-E2I-Synth: Advancing GUI Grounding with Large-Scale Instruction Synthesis](https://aclanthology.org/2025.findings-acl.809/)
    - Xinyi Liu, Xiaoyi Zhang, Ziyun Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia, School of Software and Microelectronics, Peking University
    - 📅 Date: April 15, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [benchmark], [instruction synthesis], [GUI grounding], [UI-E2I-Synth], [UI-I2E-Bench]
    - 📖 TLDR: UI-E2I-Synth addresses the annotation bottleneck in vision-based GUI grounding by using GPT-4o to synthesize large-scale grounding instructions with varied difficulty and annotation properties. The paper also introduces the UI-I2E-Bench benchmark for evaluating GUI instruction grounding under challenges such as implicit instructions, small elements, and underrepresented element types.

- [Breaking the Data Barrier -- Building GUI Agents Through Task Generalization](https://openreview.net/forum?id=QDtORaZt8K)
    - Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, Qiushi Sun, Zhenzhong Lan, Junxian He
    - 🏛️ Institutions: Zhejiang University, Westlake University, Shanghai Artificial Intelligence Laboratory, University of Hong Kong, Hong Kong University of Science and Technology
    - 📅 Date: April 14, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [mid-training], [task generalization], [multimodal reasoning], [textual reasoning], [GUIMid]
    - 📖 TLDR: This paper studies whether GUI agents benefit from a dedicated mid-training stage on non-GUI but reasoning-intensive tasks before GUI tuning. Across 11 mid-training tasks, it finds that multimodal and even text-only reasoning data can transfer strongly to downstream GUI performance on WebArena and AndroidWorld, motivating optimized non-GUI mixture design for GUI-agent training.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 01, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [mixture-of-grounding], [proactive hierarchical planning], [OSWorld], [WindowsAgentArena], [Agent S2]
    - 📖 TLDR: Agent S2 is a compositional generalist-specialist framework that splits computer-use responsibilities across specialized and generalist models rather than using a single monolithic agent. Its core methods are Mixture-of-Grounding for precise localization and Proactive Hierarchical Planning for long-horizon control, yielding strong gains on OSWorld, WindowsAgentArena, and AndroidWorld.

- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434)
    - Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu
    - 🏛️ Institutions: University of Georgia, Tencent AI Seattle Lab, Microsoft Research, University of Waterloo, Hong Kong Polytechnic University
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [trustworthiness], [Perception Trust], [Reasoning Trust], [Interaction Trust]
    - 📖 TLDR: This survey studies trustworthy GUI agents through a workflow-aligned taxonomy that separates trust into Perception Trust, Reasoning Trust, and Interaction Trust. It reviews benign failures, adversarial attacks, defenses, and evaluation practices, arguing that task completion alone is insufficient for trust assessment.

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, Microsoft Research Asia
    - 📅 Date: March 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [dual-system cognition], [adaptive system switching], [progressive decomposition], [Focus]
    - 📖 TLDR: Focus is a GUI grounding model that switches between fast prediction and slower analysis depending on task complexity. It decomposes grounding into summarization, focused visual analysis, and coordinate prediction, and reaches strong ScreenSpot and ScreenSpot-Pro performance with a 2B model trained on 300K examples.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://aclanthology.org/2025.acl-long.277/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Laboratory, The University of Hong Kong, Johns Hopkins University, Shanghai Jiao Tong University, University of Oxford, Hong Kong University of Science and Technology
    - 📅 Date: December 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [trajectory synthesis], [reverse task synthesis], [reward model], [OS-Genesis]
    - 📖 TLDR: OS-Genesis tackles the lack of high-quality GUI trajectories by synthesizing them without preset tasks or human demonstrations. It first explores with step-level interactions, then retrospectively derives tasks and filters the resulting trajectories with a reward model, producing more diverse training data for GUI agents.

- [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shenzhi Wang, Xinchen Xu, Shuofei Qiao, Zhaokai Wang, Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao, Hongxia Yang, Fan Wu, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Fudan University, OPPO AI Center, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, The Chinese University of Hong Kong, Tsinghua University, Shanghai Jiao Tong University, 01.AI, The Hong Kong Polytechnic University
    - 📅 Date: December 20, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [architectures], [benchmarks], [training], [safety]
    - 📖 TLDR: This survey reviews MLLM-based OS agents across computers, phones, and browsers, covering their environments, observation and action spaces, capabilities, and system designs. It also organizes the benchmark landscape and highlights open problems such as safety, privacy, personalization, and self-evolution.

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research, Alibaba Group, Australian National University, Independent Researcher
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [pure vision], [instruction synthesis], [context-aware grounding], [Aria-UI]
    - 📖 TLDR: Aria-UI is a GUI-grounding model that deliberately avoids HTML or AXTree inputs and instead works from pure visual observations. It pairs a scalable instruction-synthesis pipeline with interleaved textual and text-image action histories for context-aware grounding, and reports state-of-the-art results across offline and online grounding benchmarks.

- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501)
    - Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen, Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Branislav Kveton, Jihyung Kil, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, Franck Dernoncourt
    - 🏛️ Institutions: University of Maryland, State University of New York at Buffalo, University of Oregon, Adobe Research, University of Rochester, University of California, San Diego, Carnegie Mellon University, Dolby Labs, Cisco Research, University of New South Wales
    - 📅 Date: December 18, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [benchmarks], [architectures], [training], [evaluation]
    - 📖 TLDR: This survey organizes GUI-agent research around benchmarks, evaluation metrics, architectures, and training methods for agents powered by large foundation models. It proposes a unified perception-reasoning-planning-acting framework and highlights the open problems that remain across the stack.

- [Falcon-UI: Understanding GUI Before Following User Instructions](https://arxiv.org/abs/2412.09362)
    - Huawen Shen, Chang Liu, Gengluo Li, Xinlong Wang, Yu Zhou, Can Ma, Xiangyang Ji
    - 🏛️ Institutions: Institute of Information Engineering, Chinese Academy of Sciences, Nankai University, Tsinghua University, Beijing Academy of Artificial Intelligence, University of Chinese Academy of Sciences
    - 📅 Date: December 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [Insight-UI Dataset], [GUI understanding], [instruction-free pretraining], [Falcon-UI]
    - 📖 TLDR: Falcon-UI studies whether GUI-context understanding should be learned before instruction following. It introduces the large instruction-free Insight-UI Dataset for GUI pretraining and shows that this staged training improves a 7B model enough to approach much larger baselines.

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: University of Hong Kong, Salesforce Research
    - 📅 Date: December 05, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [pure vision], [inner monologue], [two-stage training], [Aguvis]
    - 📖 TLDR: Aguvis is a pure-vision GUI agent that removes textual interface representations and operates directly on screen images. It combines a large grounding-and-reasoning dataset with a two-stage training pipeline and inner-monologue reasoning, reporting strong offline and online performance without relying on closed-source models.

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890)
    - Shuai Wang, Weiwen Liu, Jingxuan Chen, Yuqi Zhou, Weinan Gan, Xingshan Zeng, Yuhan Che, Shuai Yu, Xinlong Hao, Kun Shao, Bin Wang, Chuhan Wu, Yasheng Wang, Ruiming Tang, Jianye Hao
    - 🏛️ Institutions: Huawei Noah's Ark Lab
    - 📅 Date: November 07, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [foundation models], [taxonomy], [industrial applications]
    - 📖 TLDR: This survey organizes foundation-model GUI agents around data resources, agent construction, taxonomy, and industrial applications. It also summarizes open challenges around the benchmark-reality gap, agent self-evolution, and inference efficiency.

- [EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data](https://arxiv.org/abs/2410.19461)
    - Xuetian Chen, Hangcheng Li, Jiaqing Liang, Sihang Jiang, Deqing Yang
    - 🏛️ Institutions: Fudan University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [synthetic data], [GUI grounding], [multi-granularity data], [EDGE]
    - 📖 TLDR: EDGE is a synthetic-data pipeline for GUI understanding that generates large-scale multi-granularity supervision from webpages. Models trained on the resulting dataset improve webpage understanding first and then transfer that gain to previously unseen desktop and mobile GUI environments with much less manual annotation.

- [Grounded GUI Understanding for Vision-Based Spatial Intelligent Agent: Exemplified by Extended Reality Apps](https://arxiv.org/abs/2409.10811)
    - Shuqing Li, Binchang Li, Yepang Liu, Cuiyun Gao, Jianping Zhang, Shing-Chi Cheung, Michael R. Lyu
    - 🏛️ Institutions: The Chinese University of Hong Kong, Harbin Institute of Technology, Southern University of Science and Technology, The Hong Kong University of Science and Technology
    - 📅 Date: September 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [XR apps], [interactable element detection], [zero-shot detection], [Orienter]
    - 📖 TLDR: This paper proposes Orienter, a zero-shot framework for detecting context-sensitive interactable GUI elements in extended-reality apps. It targets XR-specific challenges such as open-vocabulary GUI elements, context-dependent interactability, and spatial perception, and the paper reports stronger performance than prior GUI element detection approaches on VR app data.

- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203)
    - Yadong Lu, Jianwei Yang, Yelong Shen, Ahmed Awadallah
    - 🏛️ Institutions: Microsoft Research, Microsoft GenAI
    - 📅 Date: August 01, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [screen parsing], [GUI grounding], [icon detection], [icon captioning], [OmniParser]
    - 📖 TLDR: OmniParser parses UI screenshots into structured screen elements by combining interactable icon detection with element captioning. The paper also curates icon-related datasets and shows that this screen parsing layer improves GPT-4V grounding on ScreenSpot, Mind2Web, and AITW.

- [Read Anywhere Pointed: Layout-aware GUI Screen Reading with Tree-of-Lens Grounding](https://aclanthology.org/2024.emnlp-main.533/)
    - Yue Fan, Lei Ding, Ching-Chen Kuo, Shan Jiang, Yang Zhao, Xinze Guan, Jie Yang, Yi Zhang, Xin Eric Wang
    - 🏛️ Institutions: University of California, Santa Cruz, eBay Inc., Cybever
    - 📅 Date: June 27, 2024
    - 📑 Publisher: EMNLP 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [dataset], [screen reading], [ScreenPR], [Tree-of-Lens], [ASHL]
    - 📖 TLDR: This paper introduces the Screen Point-and-Read task, where a model must explain the region indicated by a user point on a GUI screenshot, and proposes the Tree-of-Lens agent to solve it. It also releases the ScreenPR benchmark across mobile, web, and operating-system GUIs plus the ASHL dataset for hierarchical screen-region detection.

- [VGA: Vision GUI Assistant - Minimizing Hallucinations through Image-Centric Fine-Tuning](https://aclanthology.org/2024.findings-emnlp.68/)
    - Ziyang Meng, Yu Dai, Zezheng Gong, Shaoxiong Guo, Minglong Tang, Tongquan Wei
    - 🏛️ Institutions: East China Normal University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [GUI VQA], [hallucination mitigation], [Referent Method], [FAC], [VGA]
    - 📖 TLDR: VGA is a GUI-understanding model fine-tuned to reduce hallucinations caused by relying on textual priors instead of screen evidence. The paper builds a 63.8k GUI VQA dataset with the Referent Method and uses a two-stage Foundation-and-Advanced-Comprehension training scheme to improve visually grounded answers.

- [GUICourse: From General Vision Language Model to Versatile GUI Agent](https://aclanthology.org/2025.acl-long.1065/)
    - Wentong Chen, Junbo Cui, Jinyi Hu, Yujia Qin, Junjie Fang, Yue Zhao, Chongyi Wang, Jun Liu, Guirong Chen, Yupeng Huo, Yuan Yao, Yankai Lin, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Renmin University of China, Tsinghua University, Xiamen University, Beijing University of Posts and Telecommunications, ModelBest, Chinese Academy of Sciences, National University of Singapore, Shanghai Qi Zhi Institute
    - 📅 Date: June 17, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [GUIEnv], [GUIAct], [GUIChat], [OCR and grounding]
    - 📖 TLDR: GUICourse introduces a staged dataset suite for turning general vision-language models into GUI agents, with GUIEnv for OCR and grounding, GUIAct for GUI navigation, and GUIChat for GUI-related dialogue. The paper shows that these datasets let even a 3.1B model perform effectively on single-step and multi-step GUI tasks and transfer better to AITW and Mind2Web than the original VLM baselines.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: Carnegie Mellon University, University of California, Santa Barbara, Google Research
    - 📅 Date: June 16, 2024
    - 📑 Publisher: NAACL 2024 Industry Track
    - 💻 Env: [General GUI]
    - 🔑 Key: [visual grounding], [UI element localization], [layout-guided contrastive learning], [multi-context learning], [LVG]
    - 📖 TLDR: This paper defines visual UI grounding, where a model must localize the UI element referenced by a natural-language command directly from a screenshot without relying on UI metadata. It proposes LVG, which combines layout-guided contrastive learning with synthetic-to-real multi-context learning and improves top-1 accuracy by more than 4.9 points over strong baselines.

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://www.ijcai.org/proceedings/2024/339)
    - Gilles Baechler, Srinivas Sunkara, Maria Wang, Fedir Zubach, Hassan Mansoor, Vincent Etter, Victor Cărbune, Jason Lin, Jindong Chen, Abhanshu Sharma
    - 🏛️ Institutions: Google Research
    - 📅 Date: February 07, 2024
    - 📑 Publisher: IJCAI 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [screen annotation], [UI understanding], [ScreenAI]
    - 📖 TLDR: ScreenAI is a vision-language model for UI and infographics understanding that combines a PaLI-style architecture with pix2struct-style flexible patching. It introduces a screen-annotation task, uses it to generate large-scale UI training data, and releases three datasets for screen annotation and screen question answering.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia
    - 📅 Date: October 07, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [instruction grounding], [pixel-to-sequence], [reinforcement learning], [RUIG]
    - 📖 TLDR: Presents RUIG, a metadata-free grounding model that maps natural-language instructions to coordinates on UI screenshots using a pixel-to-sequence decoder. The main contribution is an RL-style training objective that strengthens spatial decoding quality, positioning RUIG as a generic UI-grounding API rather than a full agent stack.

- [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0ff30c4bf31db0119a6219e0d250e037-Abstract-Conference.html)
    - Hongxin Li, Jingran Su, Yuntao Chen, Qing Li, Zhaoxiang Zhang
    - 🏛️ Institutions: University of Chinese Academy of Sciences, Hong Kong Institute of Science and Innovation, Chinese Academy of Sciences, The Hong Kong Polytechnic University, Shanghai AI Laboratory
    - 📅 Date: May 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [spreadsheet automation], [Excel automation], [SheetCopilot]
    - 📖 TLDR: Presents SheetCopilot, an LLM-based system for carrying out spreadsheet operations from natural-language requests. The work focuses on spreadsheet-specific planning and execution over real productivity software rather than generic GUI navigation.
