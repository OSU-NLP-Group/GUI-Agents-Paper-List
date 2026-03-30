- [WebTestBench: Evaluating Computer-Use Agents towards End-to-End Automated Web Testing](https://arxiv.org/abs/2603.25226)
    - Fanheng Kong, Jingyuan Zhang, Yang Yue, Chenxi Sun, Yang Tian, Shi Feng, Xiaocui Yang, Daling Wang, Yu Tian, Jun Du, Wenchong Zeng, Han Li, Kun Gai
    - 🏛️ Institutions: Northeastern University, Kuaishou Technology
    - 📅 Date: 2026-03-26
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [computer-use], [automated testing], [defect detection], [WebTestBench]
    - 📖 TLDR: WebTestBench is a benchmark for evaluating end-to-end automated web testing by computer-use agents, decomposing the process into checklist generation and defect detection sub-tasks, and revealing that current LLM-based agents face severe challenges including insufficient test completeness and long-horizon interaction unreliability compared to industrial-grade demands.

- [Ego2Web: A Web Agent Benchmark Grounded in Egocentric Videos](https://arxiv.org/abs/2603.22529)
    - Shoubin Yu, Lei Shu, Antoine Yang, Yao Fu, Srinivas Sunkara, Maria Wang, Jindong Chen, Mohit Bansal, Boqing Gong
    - 🏛️ Institutions: Google DeepMind, UNC Chapel Hill
    - 📅 Date: 2026-03-23
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [egocentric video], [multimodal agent], [Ego2Web], [LLM-as-a-judge]
    - 📖 TLDR: Ego2Web introduces the first benchmark bridging egocentric video perception and web agent execution, pairing first-person video recordings with web tasks requiring visual understanding and online interaction, along with a novel LLM-as-a-Judge evaluation method (Ego2WebJudge) that achieves 84% agreement with human judgment, revealing that current state-of-the-art agents perform poorly across all task categories.

- [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](https://arxiv.org/abs/2603.14248)
    - Mohamed Aghzal, Gregory J. Stein, Ziyu Yao
    - 🏛️ Institutions: George Mason University
    - 📅 Date: 2026-03-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [failure analysis], [hierarchical planning], [PDDL], [grounding]
    - 📖 TLDR: This paper proposes a hierarchical planning framework that analyzes LLM-based web agent failures across three layers (high-level planning, low-level execution, and replanning), finding that while structured PDDL plans outperform natural language plans for high-level strategy, low-level execution and perceptual grounding remain the dominant bottleneck for achieving human-level reliability.

- [AI Planning Framework for LLM-Based Web Agents](https://arxiv.org/abs/2603.12710)
    - Orit Shahnovsky, Rotem Dror
    - 🏛️ Institutions: University of Haifa
    - 📅 Date: 2026-03-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [AI planning], [evaluation metrics], [WebArena], [LLM agent]
    - 📖 TLDR: This paper introduces a formal framework mapping LLM-based web agent architectures to classical AI planning paradigms (BFS, Best-First Tree Search, DFS), proposes five novel trajectory evaluation metrics beyond success rate, and validates them on a new dataset of 794 human-labeled WebArena trajectories, showing that different agent architectures excel on different quality dimensions.

- [Safe and Scalable Web Agent Learning via Recreated Websites](https://arxiv.org/abs/2603.10505)
    - Hyungjoo Chae, Jungsoo Park, Alan Ritter
    - 🏛️ Institutions: Georgia Institute of Technology
    - 📅 Date: 2026-03-11
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [training environment], [VeriEnv], [synthetic environment], [reinforcement learning]
    - 📖 TLDR: VeriEnv is a framework that uses language models to automatically clone real-world websites into executable, verifiable synthetic environments, enabling safe and scalable web agent training with programmatically verifiable rewards, and showing that agents trained this way generalize to unseen websites and benefit from scaling the number of training environments.

- [Enhancing Web Agents with a Hierarchical Memory Tree](https://arxiv.org/abs/2603.07024)
    - Yunteng Tan, Zhi Gao, Xinxiao Wu
    - 🏛️ Institutions: Beijing Institute of Technology
    - 📅 Date: 2026-03-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [memory], [hierarchical memory tree], [cross-website generalization], [Mind2Web]
    - 📖 TLDR: Proposes Hierarchical Memory Tree (HMT), a structured memory framework that decouples logical planning from action execution via a three-level hierarchy (Intent, Stage, Action) to improve web agent generalization, significantly outperforming flat-memory methods on Mind2Web and WebArena benchmarks in cross-website and cross-domain scenarios.

- [TimeWarp: Evaluating Web Agents by Revisiting the Past](https://arxiv.org/abs/2603.04949)
    - Md Farhan Ishmam, Kenneth Marino
    - 🏛️ Institutions: University of Utah
    - 📅 Date: 2026-03-05
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agents], [TimeWarp], [TimeTraj], [behavior cloning], [plan distillation]
    - 📖 TLDR: TimeWarp is a benchmark for evaluating web agents across evolving web designs using containerized environments with six UI versions spanning different eras of the internet, revealing agents' vulnerability to UI changes; the authors also propose TimeTraj, a plan distillation algorithm that collects trajectories across multiple versions, achieving substantial performance gains for fine-tuned models.

- [Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks](https://arxiv.org/abs/2603.04364)
    - Haoyu Liu, Dingcheng Li, Lukas Rutishauser, Zeyu Zheng
    - 🏛️ Institutions: UC Berkeley, Google, Google DeepMind
    - 📅 Date: 2026-03-04
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [defense], [web agent safety], [DMAST], [adversarial training], [cross-modal attack], [GRPO]
    - 📖 TLDR: DMAST is a three-stage adversarial safety training framework (imitation learning, oracle-guided SFT with zero-acknowledgment, and GRPO self-play) that robustifies multimodal web agents against cross-modal DOM injection attacks, substantially reducing adversarial risk while doubling task completion efficiency on out-of-distribution MiniWob++ tasks.

- [M^2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval](https://static.arxiv.org/MathJax-2.7.3/fonts/HTML-CSS/TeX/png/Main/Regular/336/0032.png?V=2.7.3): Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval](https://arxiv.org/abs/2603.00503)
    - Dawei Yan, Haokui Zhang, Guangda Huzhang, Yang Li, Yibo Wang, Qing-Guo Chen, Zhao Xu, Weihua Luo, Ying Li, Wei Dong, Chunhua Shen
    - 🏛️ Institutions: Northwestern Polytechnical University, Alibaba Group, Xi'an University of Architecture and Technology, Zhejiang University
    - 📅 Date: 2026-02-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [memory augmentation], [trajectory summarization], [insight retrieval], [long-horizon tasks]
    - 📖 TLDR: M^2 is a training-free dual-memory framework for web navigation agents that combines Dynamic Trajectory Summarization (internal memory) to compress interaction history and Insight Retrieval Augmentation (external memory) to provide actionable guidelines from successful trajectories, achieving up to 19.6% success rate improvement and 58.7% token reduction on WebVoyager and OnlineMind2Web benchmarks.

- [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190)
    - Rui Yang, Qianhui Wu, Zhaoyang Wang, Hanyang Chen, Ke Yang, Hao Cheng, Huaxiu Yao, Baoling Peng, Huan Zhang, Jianfeng Gao, Tong Zhang
    - 🏛️ Institutions: UIUC, Microsoft, UNC-Chapel Hill
    - 📅 Date: 2026-02-25
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [training], [reinforcement learning], [web agent], [mobile agent], [dataset]
    - 📖 TLDR: GUI-Libra proposes a tailored post-training recipe for native GUI agents that combines action-aware supervised fine-tuning with partially verifiable reinforcement learning, using KL regularization and success-adaptive scaling to improve both step-wise accuracy and end-to-end task completion on web and mobile benchmarks.

- [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588)
    - Faria Huq, Zora Zhiruo Wang, Zhanqiu Guo, Venu Arvind Arangarajan, Tianyue Ou, Frank Xu, Shuyan Zhou, Graham Neubig, Jeffrey P. Bigham
    - 🏛️ Institutions: Carnegie Mellon University, Duke University
    - 📅 Date: 2026-02-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [framework], [web agent], [human-agent interaction], [intervention prediction], [CowCorpus]
    - 📖 TLDR: This paper introduces CowCorpus, a dataset of 400 real-user web navigation trajectories with interleaved human-agent actions, and identifies four distinct human interaction patterns to train language models that predict user interventions, achieving 61.4-63.4% improvement in prediction accuracy and a 26.5% increase in user-rated agent usefulness.

- [Persona2Web: Benchmarking Personalized Web Agents for Contextual Reasoning with User History](https://arxiv.org/abs/2602.17003)
    - Serin Kim, Sangam Lee, Dongha Lee
    - 🏛️ Institutions: Yonsei University
    - 📅 Date: 2026-02-18
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [personalized web agent], [Persona2Web], [user history], [contextual reasoning], [evaluation framework]
    - 📖 TLDR: Persona2Web introduces the first benchmark for evaluating personalized web agents on the real open web, built on a clarify-to-personalize principle that requires agents to resolve ambiguous queries by inferring user preferences from browsing history rather than explicit instructions, revealing key challenges across various agent architectures and backbone models.

- [World-Model-Augmented Web Agents with Action Correction](https://arxiv.org/abs/2602.15384)
    - Zhouzhou Shen, Xueyu Hu, Xiyun Li, Tianqing Fang, Juncheng Li, Shengyu Zhang
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab
    - 📅 Date: 2026-02-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [world model], [WAC], [multi-agent collaboration], [action correction]
    - 📖 TLDR: WAC is a web agent framework that integrates a world model for strategic guidance and consequence simulation with a judge model for feedback-driven action correction, achieving absolute gains of 1.8% on VisualWebArena and 1.3% on Online-Mind2Web over prior methods.

- [WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning](https://arxiv.org/abs/2602.12852)
    - Junjie Wang, Zequn Xie, Dan Yang, Jie Feng, Yue Shen, Duolin Sun, Meixiu Long, Yihan Jiao, Zhehao Tan, Jian Wang, Peng Wei, Jinjie Gu
    - 🏛️ Institutions: Ant Group, Zhejiang University
    - 📅 Date: 2026-02-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [trajectory pruning], [graph-based optimization], [WebClipper], [training efficiency]
    - 📖 TLDR: WebClipper is a framework that compresses web agent trajectories by modeling search processes as state graphs and mining minimum-necessary DAGs, eliminating redundant reasoning steps. Continued training on pruned trajectories reduces tool-call rounds by about 20% while improving accuracy, and a new F-AE Score metric is introduced to balance agent accuracy and efficiency.

- [Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation](https://arxiv.org/abs/2602.12544)
    - Lajanugen Logeswaran, Jaekyeom Kim, Sungryull Sohn, Creighton Glasscock, Honglak Lee
    - 🏛️ Institutions: LG AI Research
    - 📅 Date: 2026-02-12
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [data generation], [fine-grained evaluation], [BookingArena], [knowledge distillation]
    - 📖 TLDR: This paper presents a scalable pipeline for automatically generating web agent training data with a constraint-based evaluation framework that leverages partially successful trajectories, and introduces the BookingArena benchmark of complex booking tasks across 20 websites, showing that a distilled smaller model can match or exceed commercial systems.

- [Agentic Test-Time Scaling for WebAgents](https://arxiv.org/abs/2602.12276)
    - Nicholas Lee, Lutfi Eren Erdogan, Chris Joseph John, Surya Krishnapillai, Michael W. Mahoney, Kurt Keutzer, Amir Gholami
    - 🏛️ Institutions: UC Berkeley, ICSI, LBNL
    - 📅 Date: 2026-02-12
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [test-time scaling], [CATTS], [inference-time compute], [uncertainty estimation]
    - 📖 TLDR: CATTS (Confidence-Aware Test-Time Scaling) dynamically allocates inference-time compute for multi-step web agents by using vote-derived uncertainty signals (entropy and margin) to invoke an LLM arbiter only on contentious decisions, improving performance on WebArena-Lite and GoBrowse by up to 9.1% over ReAct while using up to 2.3x fewer tokens than uniform scaling.

- [MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks](https://arxiv.org/abs/2602.09222)
    - Georgios Syros, Evan Rose, Brian Grinstead, Christoph Kerschbaumer, William Robertson, Cristina Nita-Rotaru, Alina Oprea
    - 🏛️ Institutions: Northeastern University, Mozilla Corporation
    - 📅 Date: 2026-02-09
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [attack], [web agent security], [indirect prompt injection], [red-teaming], [MUZZLE]
    - 📖 TLDR: MUZZLE is an automated agentic red-teaming framework that adaptively discovers indirect prompt injection attacks against LLM-based web agents by identifying high-salience injection surfaces and iteratively refining context-aware malicious payloads, discovering 37 new attacks including cross-application prompt injections across 4 web applications.

- [PATHWAYS: Evaluating Investigation and Context Discovery in AI Web Agents](https://arxiv.org/abs/2602.05354)
    - Shifat E. Arman, Syed Nazmus Sakib, Tapodhir Karmakar Taton, Nafiul Haque, Shahrear Bin Amin
    - 🏛️ Institutions: University of Dhaka
    - 📅 Date: 2026-02-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [context discovery], [investigation], [hallucination], [PATHWAYS]
    - 📖 TLDR: PATHWAYS is a benchmark of 250 multi-step web decision tasks evaluating whether AI agents can discover and correctly use hidden contextual information, finding that current agents frequently fail to retrieve decisive hidden evidence and often hallucinate investigative reasoning, revealing a fundamental gap in investigative competence and a tradeoff between procedural compliance and effective judgement.

- [WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents](https://arxiv.org/abs/2602.03792)
    - Xilong Wang, Yinuo Liu, Zhun Wang, Dawn Song, Neil Gong
    - 🏛️ Institutions: Duke University, UC Berkeley
    - 📅 Date: 2026-02-03
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [defense], [prompt injection], [web agent], [WebSentinel], [security], [attack detection]
    - 📖 TLDR: WebSentinel is a two-step defense framework that detects and localizes prompt injection attacks in webpages by first extracting segments of interest that may be contaminated and then evaluating each segment's consistency with the webpage content, substantially outperforming baseline methods on multiple datasets.

- [Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts](https://arxiv.org/abs/2602.02468)
    - Aiden Yiliu Li, Xinyue Hao, Shilong Liu, Mengdi Wang
    - 🏛️ Institutions: University College London, Princeton University, The University of Edinburgh
    - 📅 Date: 2026-02-02
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [avenir-web], [mixture of grounding experts], [multimodal LLM], [online-Mind2Web]
    - 📖 TLDR: Avenir-Web is a multimodal web agent that combines Mixture of Grounding Experts, Experience-Imitation Planning, and task-tracking checklists with adaptive memory to achieve a new open-source state-of-the-art (53.7% success rate) on the Online-Mind2Web benchmark, reaching performance parity with top proprietary models on live web tasks.

- [DynaWeb: Model-Based Reinforcement Learning of Web Agents](https://arxiv.org/abs/2601.22149)
    - Hang Ding, Peidong Liu, Junqiao Wang, Ziwei Ji, Meng Cao, Rongzhao Zhang, Lynn Ai, Eric Yang, Tianyu Shi, Lei Yu
    - 🏛️ Institutions: Shanghai Jiao Tong University, Sichuan University, Hong Kong University of Science and Technology, McGill University, Shanghai AI Lab, Gradient, University of Toronto, Mila - Quebec AI Institute
    - 📅 Date: 2026-01-29
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [reinforcement learning], [world model], [LLM agent], [benchmark], [training]
    - 📖 TLDR: DynaWeb introduces a model-based reinforcement learning framework that trains web agents by learning a web world model as a synthetic environment for generating imagined rollouts, interleaved with real expert trajectories, achieving significant improvements on WebArena and WebVoyager benchmarks over state-of-the-art open-source web agent models.

- [How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors](https://arxiv.org/abs/2601.21961)
    - Kuai Yu, Naicheng Yu, Han Wang, Rui Yang, Huan Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, Columbia University, University of California San Diego
    - 📅 Date: 2026-02-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [evaluation], [GUI understanding], [visual grounding], [robustness]
    - 📖 TLDR: Introduces VAF, a controlled evaluation pipeline that systematically measures how webpage visual attribute factors (e.g., background color contrast, item size, position, card clarity) influence web agent decision-making across 48 variants, 5 real-world websites, and 4 representative agents.

- [ExpSeek: Self-Triggered Experience Seeking for Web Agents](https://arxiv.org/abs/2601.08605)
    - Wenyuan Zhang, Xinghua Zhang, Haiyang Yu, Shuaiyi Nie, Bingli Wu, Juwei Yue, Tingwen Liu, Yongbin Li
    - 🏛️ Institutions: Institute of Information Engineering, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Alibaba Group
    - 📅 Date: 2026-01-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [experience learning], [entropy-based triggering], [LLM agent], [benchmark], [framework]
    - 📖 TLDR: ExpSeek proposes a step-level proactive experience-seeking framework for web agents that uses entropy-based self-triggering signals to determine when to intervene with tailored experience content, achieving 9.3% and 7.5% absolute improvements on Qwen3-8B and 32B models across four web agent benchmarks.

- [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/abs/2601.08406)
    - Xinyi Wu, Jiagui Chen, Geng Hong, Jiayi Dong, Xudong Pan, Jiarun Dai, Min Yang
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute
    - 📅 Date: 2026-01-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [safety], [agent framework], [security evaluation], [attack]
    - 📖 TLDR: WebTrap Park is an automated platform for systematic security evaluation of web agents that instantiates three major security risk sources into 1,226 executable tasks on live web pages, revealing that agent architecture matters more than the underlying model for security robustness.

- [ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](https://arxiv.org/abs/2601.07262)
    - Jihong Wang, Jiamu Zhou, Weiming Zhang, Weiwen Liu, Zhuosheng Zhang, Xingyu Lou, Weinan Zhang, Huarong Deng, Jun Wang
    - 🏛️ Institutions: OPPO Research Institute, Shanghai Jiao Tong University
    - 📅 Date: 2026-02-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [knowledge evolution], [human-in-the-loop], [long-horizon tasks], [WebArena], [memory management]
    - 📖 TLDR: ColorBrowserAgent is a knowledge-evolving web automation agent that tackles site heterogeneity and long-horizon instability through human-in-the-loop knowledge adaptation and knowledge-aligned progressive summarization, achieving 71.2% success rate on WebArena and strong performance on WebChoreArena and industrial deployment.

- [WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks](https://arxiv.org/abs/2601.02439)
    - Hao Bai, Alexey Taymanov, Tong Zhang, Aviral Kumar, Spencer Whitehead
    - 🏛️ Institutions: Microsoft, University of Illinois at Urbana-Champaign (UIUC), Carnegie Mellon University (CMU)
    - 📅 Date: 2026-02-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [training environment], [reinforcement learning], [vision-language model], [benchmark], [open-source]
    - 📖 TLDR: WebGym is the largest open-source training environment for visual web agents, containing nearly 300,000 tasks across diverse real-world websites, with a high-throughput asynchronous rollout system that enables RL-based fine-tuning of VLMs to achieve 42.9% success rate on out-of-distribution websites, outperforming GPT-4o and GPT-5-Thinking.

- [Permission Manifests for Web Agents](https://arxiv.org/abs/2601.02371)
    - Samuele Marro, Alan Chan, Xinxing Ren, Lewis Hammond, Jesse Wright, Gurjyot Wanga, Tiziano Piccardi, Nuno Campos, Tobin South, Jialin Yu, Sunando Sengupta, Eric Sommerlade, Alex Pentland, Philip Torr, Jiaxin Pei
    - 🏛️ Institutions: University of Oxford, Institute for Decentralized AI, Centre for the Governance of AI, Coral Protocol, Cooperative AI Foundation, Webair, Johns Hopkins University, Witan Labs, Stanford University, Microsoft, UT Austin
    - 📅 Date: 2026-01-12
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [safety], [framework], [LLM agent], [permission control], [governance]
    - 📖 TLDR: This paper introduces agent-permissions.json, a lightweight robots.txt-style permission manifest that allows website owners to declaratively specify interaction policies for LLM-based web agents, enabling beneficial automated interactions while respecting site owners' preferences and reducing reliance on blanket blocking.

- [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](https://arxiv.org/abs/2512.23128)
    - Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H. S. Torr, Adam Mahdi, Adel Bibi
    - 🏛️ Institutions: University of Oxford, SoftServe, Independent, Johannes Kepler University Linz
    - 📅 Date: 2025-12-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [safety], [prompt injection], [security], [LLM]
    - 📖 TLDR: TRAP is a benchmark for evaluating how persuasion-based prompt injection attacks can redirect LLM-powered web agents from their intended tasks, finding that across six frontier models agents are susceptible to such attacks in 25% of tasks on average, with psychologically-driven social engineering techniques and small interface changes often doubling attack success rates.

- [DECEPTICON: How Dark Patterns Manipulate Web Agents](https://arxiv.org/abs/2512.22894)
    - Phil Cuvin, Hao Zhu, Diyi Yang
    - 🏛️ Institutions: Stanford University
    - 📅 Date: 2026-02-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [safety], [robustness], [dark patterns], [adversarial attack]
    - 📖 TLDR: Introduces DECEPTICON, a benchmark of 700 web navigation tasks with dark patterns, showing that deceptive UI designs successfully steer state-of-the-art web agents toward malicious outcomes in over 70% of tasks -- with larger models being more susceptible -- and that existing countermeasures fail to mitigate this risk.

- [DAVE: A VLM Vision Encoder for Document Understanding and Web Agents](https://arxiv.org/abs/2512.17221)
    - Brandon Huang, Hang Hua, Zhuoran Yu, Trevor Darrell, Rogerio Feris, Roei Herzig
    - 🏛️ Institutions: MIT-IBM Watson AI Lab, UC Berkeley, University of Wisconsin-Madison
    - 📅 Date: 2025-12-31
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [vision encoder], [document understanding], [VLM], [web localization], [self-supervised learning]
    - 📖 TLDR: DAVE is a vision encoder purpose-built for VLMs that improves document understanding and web agent tasks through a training pipeline combining self-supervised pretraining on unlabeled document/web images, supervised multi-task pretraining, model merging across decoder architectures, and ensemble training with generalist encoders like SigLIP2, achieving significant gains on benchmarks including Mind2Web, ScreenSpot, and VisualWebBench.

- [WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment](https://arxiv.org/abs/2512.12692)
    - Mahir Labib Dihan, Tanzima Hashem, Mohammed Eunus Ali, Md Rizwan Parvez
    - 🏛️ Institutions: Bangladesh University of Engineering and Technology (BUET), Monash University, Qatar Computing Research Institute (QCRI)
    - 📅 Date: 2025-12-14
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [search algorithm], [LLM], [WebArena], [planning]
    - 📖 TLDR: WebOperator is a tree-search framework for web agents that enables safe backtracking and strategic exploration through best-first search with action-aware safety ranking, achieving state-of-the-art 54.6% success rate on WebArena with GPT-4o.

- [Privacy Practices of Browser Agents](https://arxiv.org/abs/2512.07725)
    - Alisha Ukani, Hamed Haddadi, Ali Shahin Shamsabadi, Peter Snyder
    - 🏛️ Institutions: University of California San Diego, Brave Software, Imperial College London
    - 📅 Date: 2025-12-08
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [privacy], [security], [browser agent], [evaluation]
    - 📖 TLDR: This paper presents a systematic framework of 15 measurements across five categories to evaluate the privacy practices of eight popular browser agents, identifying 30 vulnerabilities ranging from disabled browser privacy features to leaking sensitive personal information in form fields.

- [LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents](https://arxiv.org/abs/2512.04105)
    - Jinzhe Tan, Karim Benyekhlef
    - 🏛️ Institutions: University of Montreal
    - 📅 Date: 2025-11-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [LLM agent], [multimodal], [benchmark], [legal domain], [form filling]
    - 📖 TLDR: LegalWebAgent is a multimodal LLM-powered web agent framework that autonomously navigates legal websites, extracts information, and performs actions (form completion, schedule booking) to bridge the access-to-justice gap, achieving 84.4% average success rate on a 15-task benchmark of real-world Quebec civil law service processes.

- [Prune4Web: DOM Tree Pruning Programming for Web Agent](https://arxiv.org/abs/2511.21398)
    - Jiayuan Zhang, Kaiquan Chen, Zhihao Lu, Enshen Zhou, Qian Yu, Jing Zhang
    - 🏛️ Institutions: Beihang University
    - 📅 Date: 2025-11-26
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [DOM pruning], [grounding], [LLM], [code generation], [observation simplification]
    - 📖 TLDR: Prune4Web introduces DOM Tree Pruning Programming, where an LLM generates executable Python scoring scripts to programmatically filter DOM elements based on sub-task semantics, achieving 25-50x reduction in candidate elements and improving web grounding accuracy from 46.8% to 88.28%.

- [BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents](https://arxiv.org/abs/2511.20597)
    - Kaiyuan Zhang, Mark Tenenholtz, Kyle Polley, Jerry Ma, Denis Yarats, Ninghui Li
    - 🏛️ Institutions: Purdue University, Perplexity AI
    - 📅 Date: 2025-11-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [safety], [prompt injection], [defense], [security]
    - 📖 TLDR: BrowseSafe introduces a benchmark of prompt injection attacks embedded in realistic HTML payloads targeting AI browser agents, and proposes a multi-layered defense-in-depth strategy combining architectural and model-based defenses to protect web agents from evolving prompt injection threats.

- [Building Browser Agents: Architecture, Security, and Practical Solutions](https://arxiv.org/abs/2511.19477)
    - Aram Vardanyan
    - 🏛️ Institutions: FillApp
    - 📅 Date: 2025-11-22
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [browser agent], [security], [prompt injection], [accessibility tree], [benchmark]
    - 📖 TLDR: This paper presents practical findings from building a production browser agent, arguing that architectural decisions (hybrid context management, specialized tooling, programmatic safety constraints) matter more than model capability, and that prompt injection attacks make general-purpose autonomous browsing fundamentally unsafe; the system achieves ~85% on the WebGames benchmark.

- [WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997)
    - Genglin Liu, Shijie Geng, Sha Li, Hejie Cui, Sarah Zhang, Xin Liu, Tianyi Liu
    - 🏛️ Institutions: University of California, Los Angeles, Amazon
    - 📅 Date: 2025-11-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [memory], [self-evolving], [cross-session learning], [benchmark], [framework]
    - 📖 TLDR: WebCoach is a model-agnostic framework that augments web browsing agents with persistent cross-session memory through a WebCondenser, External Memory Store, and retrieval-based Coach, enabling continual learning without retraining and improving task success rates on WebVoyager from 47% to 61% with a 38B model.

- [Building the Web for Agents: A Declarative Framework for Agent-Web Interaction](https://arxiv.org/abs/2511.11287)
    - Sven Schultze, Meike Verena Kietzmann, Nils-Lucas Schönfeld, Ruth Stock-Homburg
    - 🏛️ Institutions: Technical University of Darmstadt
    - 📅 Date: 2025-11-14
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [framework], [agent-web interaction], [agentic web], [privacy], [human-AI collaboration]
    - 📖 TLDR: Introduces VOIX, a web-native declarative framework using custom HTML tags (<tool> and <context>) that allows website developers to explicitly expose machine-readable actions and state for AI web agents, shifting control to developers while preserving user privacy. Evaluated through a hackathon study with 16 developers demonstrating rapid adoption and diverse agent-enabled web application creation.

- [Adapting Web Agents with Synthetic Supervision](https://arxiv.org/abs/2511.06101)
    - Zhaoyang Wang, Yiming Liang, Xuchao Zhang, Qianhui Wu, Siwei Han, Anson Bastos, Rujia Wang, Chetan Bansal, Baolin Peng, Jianfeng Gao, Saravan Rajmohan, Huaxiu Yao
    - 🏛️ Institutions: UNC-Chapel Hill, Purdue University, Microsoft
    - 📅 Date: 2026-01-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [synthetic data], [training data], [fine-tuning], [trajectory refinement], [task synthesis]
    - 📖 TLDR: SynthAgent is a fully synthetic supervision framework for adapting web agents to new websites by generating and refining both tasks and trajectories, using dual refinement to address hallucinations in synthesized tasks and noise in collected trajectories, then fine-tuning open-source agents on the refined data.

- [Promoting Sustainable Web Agents: Benchmarking and Estimating Energy Consumption through Empirical and Theoretical Analysis](https://arxiv.org/abs/2511.04481)
    - Lars Krupp, Daniel Geißler, Vishal Banwari, Paul Lukowicz, Jakob Karolus
    - 🏛️ Institutions: RPTU Kaiserslautern-Landau, German Research Center for Artificial Intelligence (DFKI)
    - 📅 Date: 2025-11-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [sustainability], [energy efficiency], [Mind2Web], [carbon footprint]
    - 📖 TLDR: This paper benchmarks and estimates the energy consumption and CO2 emissions of web agents (both open-source and proprietary) through empirical GPU measurements and theoretical analysis, finding that more energy consumed does not necessarily equate to better performance and advocating for energy consumption metrics in web agent benchmarks.

- [AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/abs/2510.24699)
    - Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen Zhang, Zile Qiao, Xinyu Wang, Pengjun Xie, Fei Huang, Siheng Chen, Jingren Zhou, Yong Jiang
    - 🏛️ Institutions: Tongyi Lab (Alibaba Group), Shanghai Jiao Tong University
    - 📅 Date: 2025-10-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [context management], [long-horizon tasks], [information retrieval], [supervised fine-tuning], [BrowseComp]
    - 📖 TLDR: AgentFold introduces a proactive context management paradigm for web agents that uses multi-scale "folding" operations to dynamically condense browsing history, enabling a 30B-parameter model to achieve state-of-the-art results on BrowseComp benchmarks, surpassing much larger models like DeepSeek-V3.1-671B and proprietary agents like OpenAI's o4-mini.

- [MGA: Memory-Driven GUI Agent for Observation-Centric Interaction](https://arxiv.org/abs/2510.24168)
    - Weihua Cheng, Ersheng Ni, Wenlong Wang, Yifei Sun, Junming Liu, Wangyu Shen, Yirong Chen, Botian Shi, Ding Wang
    - 🏛️ Institutions: ShanghaiTech University, The University of Queensland, East China University of Science and Technology, Tongji University, Shanghai AI Laboratory
    - 📅 Date: 2025-10-28
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [desktop], [web], [memory], [benchmark], [multi-agent]
    - 📖 TLDR: MGA (Memory-Driven GUI Agent) reframes GUI interaction with an "observe first, then decide" paradigm, using a triad of current screenshot, task-agnostic spatial information, and dynamically updated structured memory to reduce error propagation and local exploration bias, achieving strong results on OSWorld benchmarks and real desktop applications.

- [BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents](https://arxiv.org/abs/2510.23458)
    - Litu Ou, Kuan Li, Huifeng Yin, Liwen Zhang, Zhongwang Zhang, Xixi Wu, Rui Ye, Zile Qiao, Pengjun Xie, Jingren Zhou, Yong Jiang
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group, University of Edinburgh
    - 📅 Date: 2025-10-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [test-time scaling], [confidence estimation], [LLM agent], [benchmark], [efficiency]
    - 📖 TLDR: BrowseConf investigates verbalized confidence scores in LLM-based web search agents after multi-turn interactions, finding that confidence reliably predicts task accuracy, and proposes confidence-guided test-time scaling methods that significantly reduce token consumption while maintaining competitive performance compared to fixed-budget baselines.

- [WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation](https://arxiv.org/abs/2510.22732)
    - Jiali Cheng, Anjishnu Kumar, Roshan Lal, Rishi Rajasekaran, Hani Ramezani, Omar Zia Khan, Oleg Rokhlenko, Sunny Chiu-Webster, Gang Hua, Hadi Amiri
    - 🏛️ Institutions: University of Massachusetts Lowell, Amazon Alexa AI
    - 📅 Date: 2025-12-19
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agent framework], [memory], [web navigation], [planning], [WebArena]
    - 📖 TLDR: WebATLAS is a memory-augmented LLM web agent that combines experience-driven memory with look-ahead action simulation via a planner-simulator-critic loop, achieving 63% success rate on WebArena-Lite without requiring website-specific fine-tuning.

- [WebGraphEval: Multi-Turn Trajectory Evaluation for Web Agents using Graph Representation](https://arxiv.org/abs/2510.19205)
    - Yaoyao Qian, Yuanli Wang, Jinda Zhang, Yun Zong, Meixu Chen, Hanhan Zhou, Jindan Huang, Yifan Zeng, Xinyu Hu, Chan Hee Song, Danqing Zhang
    - 🏛️ Institutions: Northeastern University, Boston University, University of Victoria, University of Minnesota, George Washington University, Tufts University, Oregon State University, University of Texas at San Antonio, The Ohio State University, PathOnAI.org
    - 📅 Date: 2025-10-21
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [evaluation], [trajectory analysis], [WebArena], [multi-agent]
    - 📖 TLDR: WebGraphEval introduces a graph-based framework that abstracts multi-agent web interaction trajectories into unified weighted action graphs, enabling multi-path, cross-agent, and efficiency-aware evaluation beyond binary success metrics on benchmarks like WebArena.

- [Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming](https://arxiv.org/abs/2510.18314)
    - Zheng Zhang, Jiarui He, Yuchen Cai, Deheng Ye, Peilin Zhao, Ruili Feng, Hao Wang
    - 🏛️ Institutions: The Hong Kong University of Science and Technology (Guangzhou), Tencent, Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: 2025-10-21
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [safety], [benchmark], [attack], [LLM], [red-teaming]
    - 📖 TLDR: Genesis is an agentic red-teaming framework for LLM web agents that uses genetic algorithms and a dynamic strategy library (Attacker, Scorer, Strategist modules) to automatically evolve and discover adversarial injection attacks, consistently outperforming existing attack baselines across diverse web tasks.

- [Investigating the Impact of Dark Patterns on LLM-Based Web Agents](https://arxiv.org/abs/2510.18113)
    - Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik
    - 🏛️ Institutions: Purdue University, Florida International University, Georgia Institute of Technology
    - 📅 Date: 2025-10-20
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [safety], [LLM agent], [dark patterns], [evaluation]
    - 📖 TLDR: This paper presents the first study on how dark patterns (deceptive UI designs) affect LLM-based web agents, introducing TrickyArena as a controlled benchmark environment and finding that agents are susceptible to dark patterns an average of 41% of the time across six popular web agent frameworks and three LLMs.

- [WEBSERV: A Browser-Server Environment for Efficient Training of Reinforcement Learning-based Web Agents at Scale](https://arxiv.org/abs/2510.16252)
    - Yuxuan Lu, Jing Huang, Hui Liu, Jiri Gesi, Yan Han, Shihan Fu, Tianqi Zheng, Dakuo Wang
    - 🏛️ Institutions: Northeastern University, Amazon
    - 📅 Date: 2025-10-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [reinforcement learning], [training framework], [benchmark], [WebArena], [scalability]
    - 📖 TLDR: WEBSERV proposes a scalable browser-server environment for training and evaluating RL-based web agents, featuring a compact site-agnostic browser environment and efficient web-server launching/resetting that achieves state-of-the-art success rates on WebArena tasks while cutting launch latency by ~5x and storage by ~240x, enabling 200+ concurrent containers on a single host.

- [Synthesizing Agentic Data for Web Agents with Progressive Difficulty Enhancement Mechanisms](https://arxiv.org/abs/2510.13913)
    - Shrey Pandit, Xuan-Phi Nguyen, Yifei Ming, Austin Xu, Jiayu Wang, Caiming Xiong, Shafiq Joty
    - 🏛️ Institutions: Salesforce AI Research, University of Wisconsin-Madison
    - 📅 Date: 2025-10-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [data synthesis], [training data], [progressive difficulty], [distillation], [deep research]
    - 📖 TLDR: This paper introduces a data synthesis pipeline that generates question-answer pairs for training web agents by progressively increasing task complexity until a frontier baseline agent fails, producing smaller but more effective and diverse training datasets than existing approaches across multiple web-based benchmarks.

- [In-Browser LLM-Guided Fuzzing for Real-Time Prompt Injection Testing in Agentic AI Browsers](https://arxiv.org/abs/2510.13543)
    - Avihay Cohen
    - 🏛️ Institutions: BrowserTotal
    - 📅 Date: 2025-10-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [browser agent], [security], [prompt injection], [fuzzing], [attack]
    - 📖 TLDR: Presents an in-browser LLM-guided fuzzing framework that automatically discovers prompt injection vulnerabilities in agentic AI browsers, finding that while tested tools block simple attacks, they fail 58-74% of the time after 10 adaptive fuzzing iterations, with page summarization and Q&A features being particularly vulnerable (73% and 71% attack success rates).

- [WebRouter: Query-specific Router via Variational Information Bottleneck for Cost-sensitive Web Agent](https://arxiv.org/abs/2510.11221)
    - Tao Li, Jinlong Hu, Yang Wang, Junfeng Liu, Xuejun Liu
    - 🏛️ Institutions: Nanjing University of Aeronautics and Astronautics, Hong Kong Baptist University, Beihang University, Pengcheng Laboratory
    - 📅 Date: 2025-10-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [LLM routing], [cost efficiency], [information bottleneck], [WebVoyager], [LLM ensemble]
    - 📖 TLDR: WebRouter is a query-specific router for web agents that uses a cost-aware Variational Information Bottleneck objective to learn compressed prompt representations, reducing operational costs by 87.8% compared to a GPT-4o baseline on the WebVoyager benchmark with only a 3.8% accuracy drop.

- [BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions](https://arxiv.org/abs/2510.10666)
    - Tao Yu, Zhengbo Zhang, Zhiheng Lyu, Junhao Gong, Hongzhu Yi, Xinming Wang, Yuxuan Zhou, Jiabing Yang, Ping Nie, Yan Huang, Wenhu Chen
    - 🏛️ Institutions: CASIA, University of Chinese Academy of Sciences (UCAS), University of Waterloo, Peking University, Tsinghua University
    - 📅 Date: 2025-10-14
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [browser automation], [SFT], [rejection fine-tuning], [memory mechanism], [open-domain QA]
    - 📖 TLDR: BrowserAgent is a web agent framework that uses human-inspired browser actions (scrolling, clicking, typing) via Playwright to solve complex tasks, trained with a two-stage SFT+RFT pipeline and an explicit memory mechanism, achieving ~20% improvement over Search-R1 on multi-hop QA benchmarks.

- [SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)
    - Zonghao Ying, Yangguang Shao, Jianle Gan, Gan Xu, Junjie Shen, Wenxin Zhang, Quanchen Zou, Junzheng Shi, Zhenfei Yin, Mingchuan Zhang, Aishan Liu, Xianglong Liu
    - 🏛️ Institutions: Beihang University, Institute of Information Engineering (Chinese Academy of Sciences), China University of Petroleum (East China), Zhejiang University of Technology, University of Chinese Academy of Sciences, 360 AI Security Lab, The University of Sydney, Henan University of Science and Technology, Zhongguancun Laboratory
    - 📅 Date: 2025-10-11
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [web agent], [attack], [VLM], [evaluation]
    - 📖 TLDR: SecureWebArena is the first holistic security benchmark for LVLM-based web agents, featuring 2,970 trajectories across six simulated web environments with a structured taxonomy of six attack vectors and a multi-layered evaluation protocol assessing reasoning, behavior, and task outcomes. Experiments on 9 LVLMs reveal consistent vulnerabilities to adversarial manipulations and critical trade-offs between model specialization and security.

- [JEF-Hinter: Leveraging Offline Knowledge for Improving Web Agents Adaptation](https://arxiv.org/abs/2510.04373)
    - Hadi Nekoei, Aman Jaiswal, Patrice Bechard, Oleh Shliazhko, Orlando Marquez Ayala, Mathieu Reymond, Massimo Caccia, Alexandre Drouin, Sarath Chandar, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow, Mila - Quebec AI Institute, Dalhousie University, Polytechnique Montreal
    - 📅 Date: 2026-02-20
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [LLM agent], [offline learning], [hint generation], [trajectory distillation], [benchmark]
    - 📖 TLDR: JEF-Hinter distills offline agent trajectories (both successes and failures) into compact, context-aware hints that are retrieved at inference time to improve web agent performance, consistently outperforming baselines including human- and document-based hints on MiniWoB++, WorkArena-L1, and WebArena-Lite.

- [Cross-Modal Content Optimization for Steering Web Agent Preferences](https://arxiv.org/abs/2510.03612)
    - Tanqiu Jiang, Min Bai, Nikolaos Pappas, Yanjun Qi, Sandesh Swamy
    - 🏛️ Institutions: Stony Brook University, AWS AI Labs
    - 📅 Date: 2025-10-03
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [adversarial attack], [VLM], [multimodal], [security], [benchmark]
    - 📖 TLDR: Introduces Cross-Modal Preference Steering (CPS), a black-box adversarial attack that jointly optimizes imperceptible visual and textual modifications to steer VLM-based web agent preferences, demonstrating significantly higher attack success rates than single-modal baselines while maintaining low detection rates across GPT-4.1, Qwen-2.5VL, and Pixtral-Large on movie selection and e-commerce tasks.

- [FocusAgent: Simple Yet Effective Ways of Trimming the Large Context of Web Agents](https://arxiv.org/abs/2510.03204)
    - Imene Kerboua, Sahar Omidi Shayegan, Megh Thakkar, Xing Han Lù, Léo Boisvert, Massimo Caccia, Jérémy Espinas, Alexandre Aussem, Véronique Eglin, Alexandre Lacoste
    - 🏛️ Institutions: INSA Lyon, Universite Claude Bernard Lyon 1, CNRS, Esker, ServiceNow Research, Mila, McGill University, Polytechnique Montreal
    - 📅 Date: 2025-10-03
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [observation pruning], [accessibility tree], [prompt injection defense], [LLM retrieval], [benchmark]
    - 📖 TLDR: FocusAgent uses a lightweight LLM retriever to prune irrelevant content from web page accessibility tree observations, reducing context size by over 50% while matching strong baselines on WorkArena and WebArena, and also significantly mitigating prompt injection attacks.

- [BrowserArena: Evaluating LLM Agents on Real-World Web Navigation Tasks](https://arxiv.org/abs/2510.02418)
    - Sagnik Anupam, Davis Brown, Shuo Li, Eric Wong, Hamed Hassani, Osbert Bastani
    - 🏛️ Institutions: University of Pennsylvania
    - 📅 Date: 2025-10-07
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [evaluation], [human feedback], [failure analysis], [LLM]
    - 📖 TLDR: BrowserArena is a live open-web evaluation platform that uses Arena-style head-to-head comparisons and step-level human feedback to benchmark LLM web agents, identifying key failure modes including captcha resolution, pop-up banner removal, and direct URL navigation across different language models.

- [WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents](https://arxiv.org/abs/2510.01354)
    - Yinuo Liu, Ruohan Xu, Xilong Wang, Yuqi Jia, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: 2025-10-01
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [security], [prompt injection], [attack detection], [safety]
    - 📖 TLDR: WAInjectBench presents the first comprehensive benchmark for evaluating prompt injection detection methods targeting web agents, finding that while some detectors handle explicit textual attacks or visible image perturbations reasonably well, they largely fail against attacks that omit explicit instructions or use imperceptible perturbations.

- [PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents](https://arxiv.org/abs/2510.00413)
    - Zikang Liu, Junyi Li, Wayne Xin Zhao, Dawei Gao, Yaliang Li, Ji-rong Wen
    - 🏛️ Institutions: Renmin University of China, City University of Hong Kong, Alibaba Group
    - 📅 Date: 2025-10-04
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [memory retrieval], [mobile navigation], [vision-language model], [planning], [web navigation]
    - 📖 TLDR: PAL-UI introduces an active look-back framework for vision-based GUI agents that uses dual-level summarization and a dedicated retrieval tool to recall historical screenshots during planning, significantly improving performance on mobile and web GUI navigation tasks with models trained on Qwen2.5-VL.

- [IWR-Bench: Can LVLMs reconstruct interactive webpage from a user interaction video?](https://arxiv.org/abs/2509.24709)
    - Yang Chen, Minghao Liu, Yufan Shen, Yunwen Li, Tianyuan Huang, Xinyu Fang, Tianyu Zheng, Wenxuan Huang, Cheng Yang, Daocheng Fu, Jianbiao Mei, Rong Wu, Yunfei Zhao, Licheng Wen, Xuemeng Yang, Song Mao, Qunshu Lin, Zhi Yu, Yongliang Shen, Yu Qiao, Botian Shi
    - 🏛️ Institutions: Shanghai AI Lab, Zhejiang University, Chinese University of Hong Kong (Shenzhen), M-A-P, Chinese University of Hong Kong, Central South University, Fudan University, Stanford University, 2077AI, Shanghai Innovation Institute
    - 📅 Date: 2025-11-19
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web], [vision-language model], [UI-to-code], [code generation], [evaluation]
    - 📖 TLDR: IWR-Bench is a benchmark for evaluating Large Vision-Language Models on interactive webpage reconstruction from user interaction videos, comprising 113 tasks from 100 real-world websites; experiments on 28 LVLMs show the best model achieves only 36.35% overall, with functional correctness (24.39%) lagging far behind visual fidelity (64.25%).

- [Environmental Injection Attacks against GUI Agents in Realistic Dynamic Environments](https://arxiv.org/abs/2509.11250)
    - Yitong Zhang, Ximo Li, Liyi Cai, Jia Li
    - 🏛️ Institutions: Tsinghua University, Peking University
    - 📅 Date: 2026-01-31
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [attack], [web agent], [benchmark], [grounding], [vision]
    - 📖 TLDR: This paper introduces a realistic dynamic-environment threat model for Environmental Injection Attacks (EIAs) against GUI agents and proposes Chameleon, an attack framework using LLM-driven environment simulation and an Attention Black Hole mechanism to expose hidden vulnerabilities of LVLM-powered GUI agents on real-world websites.

- [WebMall -- A Multi-Shop Benchmark for Evaluating Web Agents [Technical Report]](https://arxiv.org/abs/2508.13024)
    - Ralph Peeters, Aaron Steiner, Luca Schwarz, Julian Yuya Caspary, Christian Bizer
    - 🏛️ Institutions: University of Mannheim
    - 📅 Date: 2025-12-02
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [e-commerce], [multi-shop], [LLM agent], [evaluation]
    - 📖 TLDR: WebMall is the first offline multi-shop benchmark for evaluating web agents on challenging e-commerce comparison shopping tasks, featuring four simulated WooCommerce shops populated with Common Crawl product data and 91 tasks across 11 categories including price comparisons, vague searches, and checkout processes, where even the best agents achieve below 55% task completion on the hardest categories.

- [Beyond Pixels: Exploring DOM Downsampling for LLM-Based Web Agents](https://arxiv.org/abs/2508.04412)
    - Thassilo M. Schiepanski, Nicholas Piël
    - 🏛️ Institutions: Surfly BV
    - 📅 Date: 2025-10-31
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [DOM], [observation space], [benchmark], [GPT-4o], [Mind2Web]
    - 📖 TLDR: Proposes D2Snap, a DOM downsampling algorithm for LLM-based web agents that reduces DOM snapshot size to match the token order of GUI screenshots, achieving a 67% success rate on Online-Mind2Web tasks that matches (and in higher-token configurations outperforms by 8%) a grounded GUI snapshot baseline, demonstrating that DOM-inherent hierarchy is a strong UI feature for LLMs.

- [Web-CogReasoner: Towards Knowledge-Induced Cognitive Reasoning for Web Agents](https://arxiv.org/abs/2508.01858)
    - Yuhan Guo, Cong Guo, Aiwen Sun, Hongliang He, Xinyu Yang, Yue Lu, Yingji Zhang, Xuntao Guo, Dong Zhang, Jianzhuang Liu, Jiang Duan, Yijia Xiao, Liangjian Wen, Hai-Ming Xu, Yong Dai
    - 🏛️ Institutions: Southwestern University of Finance and Economics, Shanghai Jiao Tong University, Central South University, Hithink Research, Westlake University, Harbin Institute of Technology, University of Manchester, University of California Los Angeles, University of Adelaide, Fudan University, Shenzhen Institutes of Advanced Technology Chinese Academy of Sciences
    - 📅 Date: 2026-01-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [cognitive reasoning], [chain-of-thought], [knowledge framework], [benchmark], [dataset]
    - 📖 TLDR: Web-CogReasoner decomposes web agent capabilities into knowledge content learning and cognitive processes, proposing a knowledge-driven Chain-of-Thought reasoning framework trained on Web-CogDataset (curated from 14 real-world websites) that significantly outperforms existing models, especially on unseen tasks where structured knowledge (Factual, Conceptual, Procedural) is decisive.

- [Machine-Readable Ads: Accessibility and Trust Patterns for AI Web Agents interacting with Online Advertisements](https://arxiv.org/abs/2507.12844)
    - Joel Nitu, Heidrun Mühle, Andreas Stöckl
    - 🏛️ Institutions: University of Applied Sciences Upper Austria, 506 Data & Performance GmbH
    - 📅 Date: 2025-11-12
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [trustworthiness], [online advertising], [browser use], [agent behavior]
    - 📖 TLDR: This paper studies how AI web agents (GPT-4o, Claude 3.7 Sonnet, Gemini 2.0 Flash, OpenAI Operator) interact with online advertisements on a cloned news website, finding that agents display severe satisficing behavior, ignore purely visual cues, and exhibit concerning trust gaps such as making unintended purchases, leading to five design principles for machine-readable ads.

- [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2505.16421)
    - Zhepei Wei, Wenlin Yao, Yao Liu, Weizhi Zhang, Qin Lu, Liang Qiu, Changlong Yu, Puyang Xu, Chao Zhang, Bing Yin, Hyokun Yun, Lihong Li
    - 🏛️ Institutions: University of Virginia, Amazon, Georgia Institute of Technology
    - 📅 Date: 2025-10-08
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [reinforcement learning], [multi-turn interaction], [WebArena], [chain-of-thought], [test-time scaling]
    - 📖 TLDR: WebAgent-R1 is an end-to-end multi-turn reinforcement learning framework for training web agents that learns from online interactions with web environments using binary task-success rewards, boosting Llama-3.1-8B's success rate on WebArena-Lite from 8.5% to 44.8% and surpassing proprietary models like OpenAI o3.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: 2025-10-16
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [prompt injection], [attack], [adversarial attack], [multimodal LLM], [security]
    - 📖 TLDR: WebInject proposes a prompt injection attack against MLLM-based web agents by adding optimized pixel-level perturbations to rendered webpages, using a neural network to approximate the non-differentiable webpage-to-screenshot mapping and projected gradient descent to find perturbations that induce attacker-specified actions.

- [WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](https://arxiv.org/abs/2504.11788)
    - Zhisong Zhang, Tianqing Fang, Kaixin Ma, Wenhao Yu, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: City University of Hong Kong, Tencent AI Lab
    - 📅 Date: 2026-01-14
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [planning], [benchmark], [model], [reasoning]
    - 📖 TLDR: WebRollback introduces an explicit rollback mechanism for web agents that allows them to revert to previous states in their navigation trajectory when they encounter errors, replacing the typical greedy one-way search strategy. Evaluated on Mind2Web-Live and WebVoyager benchmarks under both zero-shot and fine-tuning settings, the approach demonstrates improved effectiveness and efficiency in live web navigation tasks.

- [AgentA/B: Automated and Scalable Web A/BTesting with Interactive LLM Agents](https://arxiv.org/abs/2504.09723)
    - Yuxuan Lu, Ting-Yao Hsu, Hansu Gu, Limeng Cui, Yaochen Xie, William Headden, Bingsheng Yao, Akash Veeragouni, Jiapeng Liu, Sreyashi Nag, Jessie Wang, Dakuo Wang
    - 🏛️ Institutions: Northeastern University, Pennsylvania State University, Amazon
    - 📅 Date: 2026-03-10
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [A/B testing], [LLM agent], [user simulation], [e-commerce], [framework]
    - 📖 TLDR: AgentA/B is a system that uses LLM-based autonomous agents with diverse personas to automatically simulate user interactions on live websites for scalable A/B testing, demonstrating human-like behavior patterns in a 1,000-agent experiment on Amazon.com.

- [NaviMaster: Learning a Unified Policy for GUI and Embodied Navigation Tasks](https://arxiv.org/abs/2508.02046)
    - Zhihao Luo, Wentao Yan, Jingyu Gong, Min Wang, Zhizhong Zhang, Xuhong Wang, Yuan Xie, Xin Tan
    - 🏛️ Institutions: East China Normal University, Shanghai AI Laboratory, SenseTime Research
    - 📅 Date: 2025-08-04
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI navigation], [embodied navigation], [reinforcement learning], [unified agent], [mobile], [web]
    - 📖 TLDR: NaviMaster is the first unified agent that combines GUI navigation (mobile/web/desktop) and embodied navigation within a single reinforcement learning framework, using a visual-target trajectory collection pipeline and distance-aware reward to outperform state-of-the-art agents on out-of-domain benchmarks across both domains.

- [Let's Think in Two Steps: Mitigating Agreement Bias in MLLMs with Self-Grounded Verification](https://arxiv.org/abs/2507.11662)
    - Moises Andrade, Joonhyuk Cha, Brandon Ho, Vriksha Srihari, Karmesh Yadav, Zsolt Kira
    - 🏛️ Institutions: Georgia Institute of Technology
    - 📅 Date: 2025-07-15
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [MLLM verifier], [agreement bias], [self-grounded verification], [web navigation], [GUI agent], [benchmark]
    - 📖 TLDR: This paper identifies "agreement bias" in multimodal LLMs used as verifiers of GUI agent behavior (a tendency to over-validate agent actions) and proposes Self-Grounded Verification (SGV), a two-step method that first generates priors about desired behavior then evaluates trajectories, improving failure detection by 25pp and boosting task completion in OSWorld and VisualWebArena by up to 20pp over prior state of the art.

- [NeuralOS: Towards Simulating Operating Systems via Neural Generative Models](https://arxiv.org/abs/2507.08800)
    - Luke Rivard, Sun Sun, Hongyu Guo, Wenhu Chen, Yuntian Deng
    - 🏛️ Institutions: University of Waterloo, National Research Council Canada
    - 📅 Date: 2025-07-11
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [GUI], [environment], [world model], [diffusion model], [desktop], [data generation]
    - 📖 TLDR: NeuralOS introduces a neural framework that simulates operating system GUIs by combining an RNN-based state tracker with a diffusion-based renderer to predict screen frames in response to user inputs like mouse clicks and keyboard events, trained on Ubuntu XFCE recordings including AI agent-generated interactions.

- [FormGym: Doing Paperwork with Agents](https://arxiv.org/abs/2506.14079)
    - Matthew Toles, Rattandeep Singh, Isaac Song, Zhou Yu
    - 🏛️ Institutions: Columbia University, Georgia Institute of Technology, Arklex.ai
    - 📅 Date: 2025-06-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [form-filling], [GUI agent], [multimodal], [tool-use], [document understanding]
    - 📖 TLDR: FormGym is a form-filling benchmark of 432 fields across 55 documents that evaluates VLAs and GUI agents on completing paperwork in the pure-image domain, finding that baseline VLAs achieve less than 1% accuracy while GUI agents score 10.6-68.0%; the authors also contribute FieldFinder, a tool that helps LLMs localize text placement on forms, boosting accuracy from 2% to 56%.

- [UITron-Speech: Towards Automated GUI Agents Based on Speech Instructions](https://arxiv.org/abs/2506.11127)
    - Wenkang Han, Zhixiong Zeng, Jing Huang, Shu Jiang, Liming Zheng, Longrong Yang, Haibo Qiu, Chang Yao, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, Harbin Institute of Technology
    - 📅 Date: 2025-06-10
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [speech input], [multimodal], [grounding], [mobile], [training strategy]
    - 📖 TLDR: UITron-Speech is the first end-to-end GUI agent that directly processes speech instructions and on-device screenshots to predict user actions, using synthesized speech datasets, a mixed-modality training strategy, and a training-free grounding refinement method to address data scarcity, modality imbalance, and localization deviations.

- [LLM-Guided Scenario-based GUI Testing](https://arxiv.org/abs/2506.05079)
    - Shengcheng Yu, Yuchen Ling, Chunrong Fang, Quan Zhou, Yi Zhao, Chunyang Chen, Shaomin Zhu, Zhenyu Chen
    - 🏛️ Institutions: Technical University of Munich, Nanjing University, Tongji University
    - 📅 Date: 2025-06-05
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [LLM], [GUI testing], [multi-agent], [mobile], [framework], [benchmark]
    - 📖 TLDR: ScenGen is an LLM-guided multi-agent framework for scenario-based mobile GUI testing that uses five collaborative agents (Observer, Decider, Executor, Supervisor, Recorder) to automate business-logic-driven test scenario completion, achieving higher relevance to app functionality than existing exploration-based approaches.

- [Agent-SAMA: State-Aware Mobile Assistant](https://arxiv.org/abs/2505.23596)
    - Linqiang Guo, Wei Liu, Yi Wen Heng, Tse-Hsun, Chen, Yang Wang
    - 🏛️ Institutions: Concordia University
    - 📅 Date: 2025-05-29
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile GUI agent], [multi-agent framework], [finite state machine], [error recovery], [Android], [benchmark]
    - 📖 TLDR: Agent-SAMA is a state-aware multi-agent framework that models mobile app execution as a Finite State Machine (FSM), using four specialized agents to collaboratively construct FSMs in real time for task planning, execution verification, and error recovery, achieving up to 84% task success rate and 71.9% recovery rate on cross-app benchmarks.

- [GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents](https://arxiv.org/abs/2505.12842)
    - Zheng Wu, Pengzhou Cheng, Zongru Wu, Lingzhong Dong, Zhuosheng Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: 2025-05-19
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [out-of-distribution detection], [safety], [gaussian mixture model], [MLLM], [robustness]
    - 📖 TLDR: GEM proposes a Gaussian mixture model-based method for detecting out-of-distribution instructions in GUI agents by modeling input embedding distances, achieving a 23.70% average accuracy improvement over baselines across eight datasets spanning smartphones, computers, and web browsers.

- [MobileIPL: Enhancing Mobile Agents Thinking Process via Iterative Preference Learning](https://arxiv.org/abs/2505.12299)
    - Kun Huang, Weikai Xu, Yuxuan Liu, Quandong Wang, Pengzhi Gao, Wei Liu, Jian Luan, Bin Wang, Bo An
    - 🏛️ Institutions: Xiaomi Inc., Nanyang Technological University, Renmin University of China
    - 📅 Date: 2025-05-18
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile agent], [GUI agent], [training], [DPO], [preference learning], [chain-of-thought]
    - 📖 TLDR: MobileIPL proposes an Iterative Preference Learning framework that constructs CoaT-trees via iterative sampling and derives thinking-level DPO pairs with rule-based rewards, combined with a three-stage instruction evolution to prevent SFT overfitting, achieving state-of-the-art performance on three standard mobile GUI agent benchmarks while outperforming models like OS-ATLAS and UI-TARS.

- [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, Renmin University of China, Xiaomi, Tsinghua University
    - 📅 Date: 2025-05-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile], [evaluation], [dataset], [GUI testing], [multimodal]
    - 📖 TLDR: Mobile-Bench-v2 is a more realistic benchmark for VLM-based mobile agents that introduces multi-path offline evaluation, noisy environments with pop-ups and ads, and ambiguous instruction splits to test proactive interaction capabilities, addressing key limitations of existing mobile agent benchmarks.

- [ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502)
    - Hongbin Zhong, Fazle Faisal, Luis França, Tanakorn Leesatapornwongsa, Adriana Szekeres, Kexin Rong, Suman Nath
    - 🏛️ Institutions: Georgia Tech, Microsoft Research
    - 📅 Date: 2026-02-24
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [web agent], [programmatic planning], [state machine memory], [WebArena], [benchmark]
    - 📖 TLDR: ActionEngine is a training-free two-agent framework that transitions GUI agents from reactive step-by-step execution to programmatic planning by using a Crawling Agent to build an updatable state-machine memory of GUIs and an Execution Agent that synthesizes executable Python programs, achieving 95% task success on WebArena Reddit tasks with 11.8x cost reduction over vision-only baselines.

- [EmbeWebAgent: Embedding Web Agents into Any Customized UI](https://arxiv.org/abs/2602.14865)
    - Chenyang Ma, Clyde Fare, Matthew Wilson, Dave Braines
    - 🏛️ Institutions: IBM Research, University of Oxford
    - 📅 Date: 2026-02-16
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [framework], [enterprise], [ARIA], [MCP], [GUI]
    - 📖 TLDR: EmbeWebAgent is a framework for embedding LLM-powered agents directly into existing web UIs via lightweight frontend hooks (curated ARIA labels, URL-based observations, and a per-page function registry over WebSocket), enabling stack-agnostic, mixed-granularity actions from GUI primitives to higher-level composites in enterprise settings.

- [WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721)
    - Zikai Xiao, Jianhong Tu, Chuhang Zou, Yuxin Zuo, Zhi Li, Peng Wang, Bowen Yu, Fei Huang, Junyang Lin, Zuozhu Liu
    - 🏛️ Institutions: Alibaba Group, Zhejiang University
    - 📅 Date: 2026-02-16
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [world model], [web agent], [data generation], [benchmark], [training], [environment simulation]
    - 📖 TLDR: WebWorld is the first open-web world model simulator trained at scale on 1M+ real-world web interactions, enabling long-horizon multi-format simulation; agents trained on its synthesized trajectories achieve +9.2% improvement on WebArena (comparable to GPT-4o), and it generalizes to code, GUI, and game environments.

- [AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines](https://arxiv.org/abs/2602.14296)
    - Yifan Wu, Yiran Peng, Yiyu Chen, Jianhao Ruan, Zijie Zhuang, Cheng Yang, Jiayi Zhang, Man Chen, Yenchi Tseng, Zhaoyang Yu, Liang Chen, Yuyao Zhai, Bang Liu, Chenglin Wu, Yuyu Luo
    - 🏛️ Institutions: Hong Kong University of Science and Technology (Guangzhou), DeepWisdom, Peking University, Universite de Montreal / Mila
    - 📅 Date: 2026-02-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [data generation], [environment synthesis], [finite state machine], [training], [benchmark]
    - 📖 TLDR: AutoWebWorld synthesizes controllable and verifiable web environments by modeling them as Finite State Machines (FSMs), enabling a fully automated search-and-verify pipeline that generates over 11,663 verified GUI interaction trajectories at $0.04 each; a 7B agent trained on this synthetic data achieves state-of-the-art results on WebVoyager and shows consistent scaling improvements.

- [GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training](https://arxiv.org/abs/2602.14093)
    - Yuan Cao, Dezhi Ran, Mengzhou Wu, Yuzhe Guo, Xin Chen, Ang Li, Gang Cao, Gong Zhi, Hao Yu, Linyi Li, Wei Yang, Tao Xie
    - 🏛️ Institutions: Peking University, Tencent, Hong Kong University of Science and Technology, Simon Fraser University, University of Texas at Dallas
    - 📅 Date: 2026-02-15
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [GUI agent], [reinforcement learning], [environment synthesis], [verifiable reward], [web agent], [training efficiency]
    - 📖 TLDR: GUI-GENESIS automatically synthesizes lightweight web-based training environments with code-native verifiable rewards from real-world GUI applications, reducing training latency by 10x and costs by over $28K per epoch while enabling agents to outperform both the base model and real-world RL baselines on held-out tasks.

- [Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence](https://arxiv.org/abs/2506.15677)
    - Yining Hong, Rui Sun, Bingxuan Li, Xingcheng Yao, Maxine Wu, Alexander Chien, Da Yin, Ying Nian Wu, Zhecan Wang, Kai-Wei Chang
    - 🏛️ Institutions: University of California, Los Angeles, University of Illinois Urbana-Champaign, Amazon
    - 📅 Date: July 29, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets and Benchmarks (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [embodied web agent], [web agent], [simulation environment], [cross-domain reasoning], [embodied web agents]
    - 📖 TLDR: This paper introduces Embodied Web Agents, a benchmark and simulation platform for tasks that require agents to combine embodied perception and action with web-scale information access. The environments couple 3D indoor and outdoor worlds with working web interfaces for tasks such as navigation, shopping, tourism, and cooking. Although broader than standard GUI automation, it is directly relevant to web agents because it evaluates how agent systems bridge browser-based reasoning with real-world interaction.

- [Talk to Your Slides: High-Efficiency Slide Editing via Language-Driven Structured Data Manipulation](https://arxiv.org/abs/2505.11604)
    - Kyudan Jung, Hojun Cho, Jooyeol Yun, Soyoung Yang, Jaehyeok Jang, Jaegul Choo
    - 🏛️ Institutions: KAIST, Chung-Ang University
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [LLM agent], [slide editing], [benchmark], [code generation], [structured data manipulation]
    - 📖 TLDR: Talk-to-Your-Slides is a language-driven slide editing agent that manipulates structured document data (XML/COM object model) instead of relying on GUI-based visual interactions, achieving 34% faster processing, 34% better instruction fidelity, and 87% lower cost than GUI-based baselines, along with a new benchmark (TSBench) of 379 human-verified editing instructions.

- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434)
    - Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu
    - 🏛️ Institutions: University of Georgia, Tencent AI Seattle Lab, Microsoft Research, University of Waterloo, Hong Kong Polytechnic University
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [GUI agent], [trustworthiness], [safety], [security], [benchmark]
    - 📖 TLDR: A survey on trustworthy GUI agents that introduces a workflow-aligned taxonomy decomposing trust into Perception Trust, Reasoning Trust, and Interaction Trust, systematically reviewing failure modes, adversarial attacks, defense mechanisms, and evaluation practices for deploying GUI agents safely.

- [WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point](https://arxiv.org/abs/2502.08047)
    - Henry Hengyuan Zhao, Kaiming Yang, Wendi Yu, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: February 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [desktop], [web], [planning], [robustness], [world model]
    - 📖 TLDR: WorldGUI is a benchmark for desktop and web GUI automation that evaluates agents under diverse, non-default initial states to test robustness and adaptive planning, revealing that state-of-the-art GUI agents suffer substantial performance degradation when the environment deviates from canonical starting points. It also introduces WorldGUI-Agent, a model-agnostic framework using three critique stages to improve reliability in dynamic environments.

- [A3: Android Agent Arena for Mobile GUI Agents with Essential-State Procedural Evaluation](https://arxiv.org/abs/2501.01149)
    - Yuxiang Chai, Shunye Tang, Han Xiao, Weifeng Lin, Hanhao Li, Jiayu Zhang, Liang Liu, Pengxiang Zhao, Guangyi Liu, Guozhi Wang, Shuai Ren, Rongduo Han, Haining Zhang, Siyuan Huang, Hongsheng Li
    - 🏛️ Institutions: The Chinese University of Hong Kong, Nankai University, vivo AI Lab, Shanghai Jiao Tong University
    - 📅 Date: January 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [Android], [mobile agent], [GUI agent], [evaluation], [LLM-based evaluation]
    - 📖 TLDR: A3 (Android Agent Arena) introduces a benchmark of 100 tasks across 20 popular online Android apps with a novel "essential-state" procedural evaluation method that uses MLLMs as reward models to progressively verify task completion, addressing the limitations of static or offline-only benchmarks for mobile GUI agents.

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

- [Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification](https://arxiv.org/abs/2603.26648)
    - Zehai He, Wenyi Hong, Zhen Yang, Ziyang Pan, Mingdao Liu, Xiaotao Gu, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web development], [GUI agent], [code generation], [VLM], [evaluation]
    - 📖 TLDR: Vision2Web is a hierarchical benchmark for visual website development spanning static UI-to-code, interactive frontend reproduction, and full-stack development, with a workflow-based agent verification paradigm using GUI agent verifiers and VLM judges to evaluate coding agents across 193 tasks.

- [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/abs/2603.26266)
    - Rui Xie, Zhi Gao, Chenrui Shi, Zirui Shang, Lu Chen, Qing Li
    - 🏛️ Institutions: Shanghai Jiao Tong University, BIGAI, Beijing Institute of Technology
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [RAG], [video understanding], [domain bias], [training-free], [OSWorld]
    - 📖 TLDR: GUIDE is a training-free, plug-and-play framework that resolves domain bias in GUI agents by retrieving relevant web tutorial videos via a subtitle-driven Video-RAG pipeline and automatically annotating them to extract planning and grounding knowledge, achieving consistent 4.5-7.5% improvements on OSWorld across multiple agent architectures without any model fine-tuning.

- [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](https://arxiv.org/abs/2603.26211)
    - Shrinidhi Kumbhar, Haofu Liao, Srikar Appalaraju, Kunwar Yashraj Singh
    - 🏛️ Institutions: Arizona State University, Amazon (AWS Agentic AI)
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [diffusion model], [vision-language model], [hybrid masking], [bounding box prediction], [cross-platform]
    - 📖 TLDR: This paper adapts discrete diffusion vision-language models (LLaDA-V) for GUI grounding, proposing a hybrid masking schedule that combines linear and deterministic masking to improve bounding-box prediction accuracy across web, desktop, and mobile interfaces, demonstrating that diffusion-based models are a competitive alternative to autoregressive VLMs for GUI agent tasks.

- [Rethinking Token Pruning for Historical Screenshots in GUI Visual Agents: Semantic, Spatial, and Temporal Perspectives](https://arxiv.org/abs/2603.26041)
    - Daiqiang Li, Zihao Pan, Zeyu Zhang, Ronghao Chen, Huacan Wang, Honggang Chen, Haiyun Jiang
    - 🏛️ Institutions: Sichuan University, Sun Yat-sen University, Australian National University, Peking University, University of Chinese Academy of Sciences, Shanghai Jiao Tong University
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [token pruning], [efficiency], [MLLM], [visual grounding], [empirical study]
    - 📖 TLDR: This paper conducts an empirical study on token pruning for historical screenshots in GUI visual agents, revealing three key insights: background regions capture valuable interface-state transitions, random pruning better preserves spatial structure than designed strategies, and a temporal recency effect allows heavy compression of distant screenshots with minimal performance loss.

- [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)
    - Lukas Aichberger, Alasdair Paren, Guohao Li, Philip Torr, Yarin Gal, Adel Bibi
    - 🏛️ Institutions: Johannes Kepler University Linz, University of Oxford
    - 📅 Date: March 13, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [security], [adversarial attacks], [computer-use agent], [OS agent], [MIP against agent]
    - 📖 TLDR: This paper identifies Malicious Image Patches as a new attack vector against multimodal OS agents, where adversarially perturbed visual regions on the screen can trigger harmful actions when captured by the agent. The attack generalizes across prompts and screen setups, showing that benign-looking visual content such as wallpapers or social media images can hijack computer-use agents. The paper exposes a concrete security weakness in OS-level agents that goes beyond text-only prompt injection.

- [Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents](https://arxiv.org/abs/2505.24878)
    - Yaxin Luo, Zhaoyi Li, Jiacheng Liu, Jiacheng Cui, Xiaohan Zhao, Zhiqiang Shen
    - 🏛️ Institutions: VILA Lab, MBZUAI, MetaAgentX
    - 📅 Date: May 30, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [multimodal agent], [CAPTCHA], [reasoning], [open CaptchaWorld]
    - 📖 TLDR: This paper introduces Open CaptchaWorld, a web-based benchmark designed to test whether multimodal LLM agents can solve realistic CAPTCHA challenges that block end-to-end web automation. It spans 20 CAPTCHA types and measures both performance and CAPTCHA reasoning depth, capturing the multi-step perceptual and interaction burden of these tasks. The benchmark shows that even strong multimodal agents remain far from human performance on CAPTCHA-heavy web workflows.

- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277)
    - Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
    - 🏛️ Institutions: Georgia Institute of Technology, Yonsei University, Carnegie Mellon University
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [reward model], [web agent], [benchmark], [WebRewardBench], [web-shepherd]
    - 📖 TLDR: This paper introduces Web-Shepherd, the first process reward model specialized for web navigation, together with WebPRM Collection and WebRewardBench for training and meta-evaluating web-agent reward models. It shows that a compact specialized verifier can substantially outperform generic frontier models as web-trajectory evaluators while costing much less. The work is directly relevant to reinforcing web agents because it provides both the reward model and the evaluation infrastructure needed for scalable RL or test-time verification.

- [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892)
    - Kai Mei, Jiang Guo, Shuaichen Chang, Mingwen Dong, Dongkyu Lee, Xing Niu, Jiarong Jiang
    - 🏛️ Institutions: Rutgers University, AWS Agentic AI
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [world model], [retrieval-augmented planning], [computer-use agent], [OSWorld], [WebArena], [r-WoM]
    - 📖 TLDR: This paper studies whether LLMs can reliably serve as world models for computer-use agents and finds that their simulations degrade sharply over long-horizon procedures despite reasonable short-range predictions. To address this, it proposes R-WoM, a retrieval-augmented world model that grounds planning with up-to-date external tutorials. R-WoM improves planning quality on OSWorld and WebArena, with especially strong gains on longer-horizon tasks where ungrounded simulation is most brittle.

- [AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780)
    - Arman Zharmagambetov, Chuan Guo, Ivan Evtimov, Maya Pavlova, Ruslan Salakhutdinov, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Meta
    - 📅 Date: March 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [privacy], [web agent], [data minimization], [safety], [AgentDAM]
    - 📖 TLDR: This paper introduces AgentDAM, a benchmark for evaluating whether autonomous web agents respect data minimization when using sensitive user information. It measures whether an agent accesses private information only when it is necessary to complete a task, and shows that current web agents frequently leak unnecessary sensitive data. The paper also studies a prompting-based defense, but the main contribution is a realistic end-to-end privacy evaluation setup for autonomous web agents.

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL]
    - 📖 TLDR: This paper studies continual learning for computer-use agents in dynamic, shifting target environments without relying on human demonstrations. It introduces ACuRL, an autonomous curriculum reinforcement learning framework that explores environments, synthesizes progressively tailored tasks, and trains with CUAJudge, an automatic evaluator aligned closely with human judgments. The method improves both intra-environment and cross-environment adaptation while avoiding catastrophic forgetting, making it directly relevant to real-world deployment of CUAs.

- [BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent](https://arxiv.org/abs/2509.15566)
    - Shaojie Zhang, Ruoceng Zhang, Pei Fu, Shaokang Wang, Jiahui Yang, Xin Du, Shiqi Cui, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: September 19, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI agent], [reinforcement fine-tuning], [reasoning], [reward design], [BTL-UI]
    - 📖 TLDR: This paper proposes Blink-Think-Link, a brain-inspired framework for GUI agents that decomposes interaction into rapid visual attention, higher-level reasoning, and executable action generation. It also introduces blink-specific data generation and a rule-based reward that supervises both the reasoning process and final outcome. The resulting BTL-UI model reports competitive performance across static GUI understanding and dynamic GUI interaction benchmarks.

- [CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs](https://arxiv.org/abs/2510.15455)
    - Gucongcong Fan, Chaoyue Niu, Chengfei Lyu, Fan Wu, Guihai Chen
    - 🏛️ Institutions: Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: October 17, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [privacy], [mobile GUI agent], [cloud-local collaboration], [UI exposure reduction], [CORE]
    - 📖 TLDR: This paper studies privacy leakage in mobile agents that repeatedly upload full-screen UI context to cloud LLMs for planning and action selection. It proposes CORE, a collaborative framework where local and cloud LLMs split planning and decision-making through layout-aware block partitioning, co-planning, and co-decision, so only a smaller relevant UI subset is exposed upstream. On diverse mobile apps and tasks, CORE cuts UI exposure by up to 55.6% while keeping task success close to cloud-only agents.

- [FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://arxiv.org/abs/2507.21071)
    - Qinglong Yang, Haoming Li, Haotian Zhao, Xiaokai Yan, Jingtao Ding, Fengli Xu, Yong Li
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: June 9, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile GUI agent], [proactive assistance], [personalization], [FingerTip 20K]
    - 📖 TLDR: This paper introduces FingerTip 20K, a mobile-agent benchmark built from long-term real-life Android demonstrations that emphasizes proactive task suggestion and personalized execution rather than only instruction-following. It contributes 20K user episodes with contextual and historical signals, then shows that current mobile LLM agents still perform far below humans on these user-oriented settings. Fine-tuning on the collected data substantially improves the use of user context and preferences.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Gaoling School of Artificial Intelligence, Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [visual grounding], [reinforcement learning], [ScreenSpot], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation](https://arxiv.org/abs/2510.27210)
    - Tao Liu, Chongyu Wang, Rongjie Li, Yingchen Yu, Xuming He, Bai Song
    - 🏛️ Institutions: ShanghaiTech University, ByteDance, Shanghai Engineering Research Center of Intelligent Vision and Imaging
    - 📅 Date: October 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reasoning], [history summarization], [reinforcement learning], [GUI navigation], [GUI-rise]
    - 📖 TLDR: This paper targets two persistent GUI-agent weaknesses: poor cross-domain generalization and weak use of long interaction history. GUI-Rise addresses them with a reasoning-enhanced framework that jointly trains structured reasoning, action prediction, and history summarization, then further improves the agent with GRPO and a history-aware reward. Under matched training data, it reports state-of-the-art GUI-navigation performance, especially on out-of-domain settings.

- [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)
    - Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir, Zachary S. Siegel, Boyi Wei, Tianci Xue, Ziru Chen, Felix Chen, Saiteja Utpala, Franck Ndzomga, Dheeraj Oruganty, Sophie Luskin, Kangheng Liu, Botao Yu, Amit Arora, Dongyoon Hahm, Harsh Trivedi, Huan Sun, Juyong Lee, Tengjun Jin, Yifan Mai, Yifei Zhou, Yuxuan Zhu, Rishi Bommasani, Daniel Kang, Dawn Song, Peter Henderson, Yu Su, Percy Liang, Arvind Narayanan
    - 🏛️ Institutions: Princeton University, The Ohio State University, Stanford University, University of California, Berkeley
    - 📅 Date: October 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [evaluation], [leaderboard], [evaluation harness], [web navigation], [HAL]
    - 📖 TLDR: This paper introduces HAL, an evaluation harness and leaderboard infrastructure for AI agents that standardizes large-scale, distributed benchmarking across models, scaffolds, and benchmarks. Beyond aggregate scores, it also tracks costs and uses LLM-aided log inspection to uncover failure modes and benchmark gaming behaviors. Although broader than GUI agents alone, it is directly relevant to computer-use evaluation because it includes web-navigation-style agent benchmarks and focuses on reliable real-world agent assessment.

- [How to Train Your LLM Web Agent: A Statistical Diagnosis](https://arxiv.org/abs/2507.04103)
    - Dheeraj Vattikonda, Santhoshi Ravichandran, Emiliano Penaloza, Hadi Nekoei, Megh Thakkar, Thibault Le Sellier de Chezelles, Nicolas Gontier, Miguel Munoz-Marmol, Sahar Omidi Shayegan, Stefania Raimondo, Xue Liu, Alexandre Drouin, Laurent Charlin, Alexandre Piche, Alexandre Lacoste, Massimo Caccia
    - 🏛️ Institutions: ServiceNow AI Research, Mila - Quebec AI Institute, Polytechnique Montreal, HEC Montreal, McGill University, Universite de Montreal
    - 📅 Date: July 5, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [reinforcement learning], [imitation learning], [training analysis], [WorkArena]
    - 📖 TLDR: This paper studies how to post-train open web agents under a strict compute budget, combining supervised imitation from a stronger teacher with on-policy reinforcement learning. Using large hyperparameter sweeps and bootstrapped sensitivity analysis, it provides one of the first statistically grounded compute-allocation studies for LLM web-agent training. The main result is that a mixed SFT-plus-RL pipeline is both more compute efficient and more effective than using either approach alone on WorkArena and MiniWoB++.

- [MobileUse: A GUI Agent with Hierarchical Reflection for Autonomous Mobile Operation](https://arxiv.org/abs/2507.16853)
    - Ning Li, Xiangmou Qu, Jiamu Zhou, Jun Wang, Muning Wen, Kounianhua Du, Xingyu Lou, Qiuying Peng, Jun Wang, Weinan Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: July 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [mobile GUI agent], [hierarchical reflection], [proactive exploration], [AndroidWorld], [AndroidLab], [MobileUse]
    - 📖 TLDR: This paper introduces MobileUse, a mobile GUI agent designed to handle long-horizon execution, error recovery, and cold-start operation in unfamiliar apps. Its core design combines hierarchical reflection across multiple temporal scales with a reflection-on-demand strategy and proactive exploration to build environment understanding before acting. The result sets new state-of-the-art success rates on AndroidWorld and AndroidLab and is released with a toolkit for execution on physical mobile devices.

- [OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://github.com/OS-Agent-Survey/OS-Agent-Survey)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shawn Wang, Xinchen Xu, Shuofei Qiao , Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao, Hongxia Yang, Fan Wu, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Fudan University, OPPO AI Center, University of Chinese Academy of Sciences, Chinese Academy of Sciences, The Chinese HKU, Tsinghua University, 01.AI, The Hong Kong Polytechnic University, SJTU
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Github Repo
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This paper conducts a comprehensive survey on OS Agents, which are (M)LLM-based agents that use computing devices (e.g., computers and mobile phones) by operating within the environments and interfaces (e.g., Graphical User Interface (GUI)) provided by operating systems (OS) to automate tasks. The survey begins by elucidating the fundamentals of OS Agents, exploring their key components including the environment, observation space, and action space, and outlining essential capabilities such as understanding, planning, and grounding. Methodologies for constructing OS Agents are examined, with a focus on domain-specific foundation models and agent frameworks. A detailed review of evaluation protocols and benchmarks highlights how OS Agents are assessed across diverse tasks. Finally, current challenges and promising future research directions, including safety and privacy, personalization and self-evolution, are discussed.

- [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)
    - Thomas Kuntz, Agatha Duzan, Hao Zhao, Francesco Croce, J Zico Kolter, Nicolas Flammarion, Maksym Andriushchenko
    - 🏛️ Institutions: EPFL, Carnegie Mellon University
    - 📅 Date: October 29, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets and Benchmarks Track Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer-use agent], [prompt injection], [OSWorld], [OS-harm]
    - 📖 TLDR: This paper introduces OS-Harm, a safety benchmark for computer-use agents built on top of OSWorld. It covers 150 tasks spanning deliberate misuse, prompt injection, and model misbehavior across applications such as browsers, editors, and email clients, and includes an automated judge for both safety and task correctness. Evaluations show that current frontier agents often comply with harmful requests, remain vulnerable to prompt injection, and can execute unsafe actions in realistic computer-use settings.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [computer-use agent], [OSWorld], [RiOSWorld]
    - 📖 TLDR: This paper introduces RiOSWorld, a benchmark for evaluating safety risks in multimodal computer-use agents during realistic computer manipulation. It covers 492 risky tasks across applications such as web, social media, multimedia, email, office software, and operating-system interactions, and evaluates both harmful intent and harmful task completion. The benchmark shows that current computer-use agents remain exposed to substantial real-world safety risks even when they are aligned for ordinary dialogue settings.

- [SE-GUI: Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: VCIP, School of Computer Science, Nankai University, vivo Mobile Communication Co., Ltd
    - 📅 Date: May 24, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [visual grounding], [ScreenSpot-pro], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence Renmin University of China, MiLM Plus Xiaomi Inc., Institute for AI Industry Research Tsinghua University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile GUI agent], [multi-path evaluation], [ambiguous instruction], [noisy environment], [SMAN-bench]
    - 📖 TLDR: This paper introduces SMAN-Bench, a mobile-agent benchmark that moves beyond single golden trajectories by evaluating single-path, multi-path, ambiguous, and noisy task settings in one framework. It builds instructions from an existing graph-structured mobile corpus, adds offline multi-path reward evaluation, and explicitly includes noisy pop-up-heavy environments plus clarification-style ambiguous tasks. The benchmark is designed to better reflect realistic mobile-agent deployment conditions than cleaner or purely online settings.

- [ScreenAgent: A Computer Control Agent Driven by Visual Language Large Model](https://arxiv.org/abs/2402.07945)
    - Runliang Niu, Jindong Li, Shiqi Wang, Yali Fu, Xiyu Hu, Xueyuan Leng, He Kong, Yi Chang, Qi Wang
    - 🏛️ Institutions: Jilin University
    - 📅 Date: February 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual language model], [computer control agent]
    - 📖 TLDR: This paper introduces ScreenAgent, a computer control agent powered by a visual language large model. The system can interpret natural language instructions and execute them on various computer applications by analyzing screen content. ScreenAgent employs a novel action grounding mechanism to map high-level instructions to specific UI interactions. Evaluated on a diverse set of tasks across different applications, ScreenAgent demonstrates superior performance in task completion and generalization compared to existing methods.

- [Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control](https://arxiv.org/abs/2509.01720)
    - Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: September 1, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [mobile GUI agent], [sample efficiency], [AndroidWorld], [SoLS]
    - 📖 TLDR: This paper introduces SoLS, an off-policy reinforcement learning algorithm for mobile app control that treats successful and unsuccessful samples differently to improve stability and sample efficiency. It also adds Successful Transition Replay to focus learning on successful interactions. On AndroidWorld, the method substantially outperforms prior prompt-based and RL baselines while using much less computation than large proprietary agents.

- [Turn Every Application into an Agent: Towards Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://arxiv.org/abs/2409.17140)
    - Junting Lu, Zhiyang Zhang, Fangkai Yang, Jue Zhang, Lu Wang, Chao Du, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Peking University, Microsoft
    - 📅 Date: September 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [API interaction], [HACI], [agent OS]
    - 📖 TLDR: This paper proposes an API-centered framework called **AXIS**, enhancing the efficiency and reliability of LLM-based agents by prioritizing API interactions over UI-based actions. This approach aims to reduce the high latency and error rates of traditional UI-interaction models. AXIS not only supports the rapid creation and extension of APIs through automated application exploration but also contributes to a new **Human-Agent-Computer Interaction (HACI)** framework. The paper outlines the development of an agent-centric operating system (Agent OS), which improves task completion times by up to 70% and reduces cognitive load on users while maintaining high accuracy across complex multi-application tasks.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reward model], [self-improvement], [synthetic data], [mobile GUI agent], [UI-genie-RM], [UI-genie-agent]
    - 📖 TLDR: This paper introduces UI-Genie, a self-improving mobile GUI-agent framework that tackles two bottlenecks at once: outcome verification and scalable high-quality trajectory generation. It builds a dedicated reward model, UI-Genie-RM, plus a reward-guided self-improvement loop that iteratively upgrades both the agent and the reward model in dynamic environments. The paper also releases the first reward-specific GUI-agent dataset and reports state-of-the-art performance across multiple mobile GUI benchmarks after several generations of self-improvement.

- [ViMo: A Generative Visual GUI World Model for App Agents](https://arxiv.org/abs/2504.13936)
    - Dezhao Luo, Bohan Tang, Kang Li, Georgios Papoudakis, Jifei Song, Shaogang Gong, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Queen Mary University of London, University of Oxford, Huawei Noah's Ark Lab, University College London
    - 📅 Date: May 20, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [world model], [visual prediction], [mobile GUI agent], [long-horizon planning], [ViMo]
    - 📖 TLDR: This paper introduces ViMo, the first visual GUI world model for app agents that predicts future GUI observations directly as images rather than only as text descriptions. To handle the hard problem of rendering GUI text accurately, it separates graphic generation from text generation with a Symbolic Text Representation and dedicated predictors for each part. The generated future screens are then used to help agents compare action outcomes and make better long-horizon decisions in mobile apps.

- [VideoAgentTrek: Computer Use Pretraining from Unlabeled Videos](https://arxiv.org/abs/2510.19488)
    - Dunjie Lu, Yiheng Xu, Junli Wang, Haoyuan Wu, Xinyuan Wang, Zekun Wang, Junlin Yang, Hongjin Su, Jixuan Chen, Junda Chen, Yuchen Mao, Jingren Zhou, Junyang Lin, Binyuan Hui, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Qwen Team, Alibaba Group
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [pretraining], [computer-use agent], [video mining], [inverse dynamics], [OSWorld-verified], [VideoAgentTrek], [Video2Action]
    - 📖 TLDR: This paper introduces VideoAgentTrek, a scalable pipeline that converts unlabeled screen-recorded videos into structured computer-use trajectories for pretraining GUI agents. Its Video2Action inverse-dynamics module first localizes GUI actions in time and then recovers structured action parameters such as click coordinates and typed text. Mining 39,000 YouTube tutorials yields 1.52 million interaction steps, and using this data for continued pretraining substantially improves downstream performance on OSWorld-Verified and AgentNetBench.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Chuan Guo, Aaron Grattafiori, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Independent Researcher
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [web agent], [prompt injection], [security], [WASP]
    - 📖 TLDR: This paper introduces WASP, a benchmark for end-to-end evaluation of web-agent security against prompt injection attacks in realistic multi-step web tasks. It shows that even strong web agents can be partially deceived at very high rates by simple human-written injections, while also revealing a more nuanced failure mode where agents are often insecure yet too incompetent to fully execute the attacker's goal. The benchmark is designed to measure security under realistic web-agent deployment conditions rather than simplified single-step attacks.

- [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)
    - Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: May 28, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [information seeking], [reinforcement learning], [GAIA], [WebDancer]
    - 📖 TLDR: This paper presents WebDancer, an end-to-end web agent for autonomous information seeking built through a data-centric four-stage training pipeline: browsing data construction, trajectory sampling, supervised fine-tuning, and reinforcement learning. It targets long-horizon information-seeking problems rather than short templated web tasks. The resulting system achieves strong performance on GAIA and WebWalkerQA and offers a concrete recipe for training more capable research-style web agents.

- [When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents](https://arxiv.org/abs/2602.08995)
    - Yuting Ning, Jaylen Jones, Zhehao Zhang, Chentao Ye, Weitong Ruan, Junyi Li, Rahul Gupta, Huan Sun
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [guardrail], [misaligned actions], [MisActBench], [DeAction]
    - 📖 TLDR: This paper defines the problem of misaligned actions in computer-use agents, covering both externally induced failures such as prompt injection and internally arising errors such as faulty reasoning. It introduces MisActBench, an action-level benchmark with human alignment labels, and DeAction, a guardrail that detects and iteratively corrects misaligned actions before execution. DeAction substantially improves F1 on the benchmark and sharply reduces attack success in online evaluation while preserving benign task success.

- [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235)
    - Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, LawZero, Mila - Quebec AI Institute, Universite de Montreal, University of California, Berkeley
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [safety], [red teaming], [unintended behavior], [computer-use agent], [AutoElicit]
    - 📖 TLDR: This paper studies unsafe unintended behaviors in computer-use agents under benign user inputs rather than adversarial prompts. It introduces AutoElicit, an agentic framework that iteratively perturbs realistic benign instructions using execution feedback to surface severe harmful behaviors in frontier CUAs. The results show that even strong CUAs remain broadly susceptible to harmful deviations, establishing a concrete framework for systematically probing unintended safety failures in realistic computer-use settings.

- [Programming with Pixels: Can Computer-Use Agents do Software Engineering?](https://arxiv.org/abs/2502.18525)
    - Pranjal Aggarwal, Sean Welleck
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: February 24, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [environment], [computer-use agent], [software engineering], [tool-use], [PwP], [PwP-bench]
    - 📖 TLDR: This paper introduces Programming with Pixels, a visual IDE environment for evaluating whether generalist computer-use agents can handle software engineering tasks rather than only simple desktop or web interactions. It also presents PwP-Bench, a benchmark spanning 15 software-engineering tasks across languages and modalities. The results show that purely visual computer-use agents lag behind specialist coding agents, but narrow text APIs such as file editing and bash dramatically narrow that gap.

- [GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments?](https://arxiv.org/abs/2510.20333)
    - Chiyu Chen, Xinhao Song, Yunkai Chai, Yang Yao, Haodong Zhao, Lijun Li, Jie Li, Yan Teng, Gongshen Liu, Yingchun Wang
    - 🏛️ Institutions: Shanghai Jiao Tong University, School of Computer Science, Shanghai Artificial Intelligence Laboratory, The University of Hong Kong
    - 📅 Date: October 23, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [mobile GUI agent], [environmental injection], [adversarial robustness], [GhostEI-bench]
    - 📖 TLDR: This paper introduces GhostEI-Bench, a benchmark for evaluating mobile agents under dynamic environmental injection attacks such as deceptive overlays, spoofed notifications, and pop-ups inside realistic Android workflows. Rather than testing static screenshots, it injects adversarial events into executable mobile environments and uses judge-based trajectory analysis to localize failure points. The benchmark shows that current mobile agents remain highly vulnerable to these runtime visual attacks.

- [Infogent: An Agent-Based Framework for Web Information Aggregation](https://aclanthology.org/2025.findings-naacl.318/)
    - Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tur, Heng Ji
    - 🏛️ Institutions: University of Illinois at Urbana-Champaign
    - 📅 Date: April 29, 2025
    - 📑 Publisher: Findings of NAACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [information aggregation], [browser navigation], [AssistantBench], [infogent]
    - 📖 TLDR: This paper targets web information aggregation rather than single-site task completion, asking agents to explore multiple websites and decide when enough evidence has been gathered for a complex query. It introduces Infogent, a modular framework with Navigator, Extractor, and Aggregator components, plus enhanced actions for backtracking and feedback-driven navigation. The framework improves over prior baselines in both API-driven and interactive visual web-access settings, including gains on AssistantBench.

- [WARC-Bench: Web Archive based Benchmark for GUI Subtask Executions](https://arxiv.org/abs/2510.09872)
    - Sanjari Srivastava, Gang Li, Cheng Chang, Rishu Garg, Manpreet Kaur, Charlene Y. Lee, Yuezhang Li, Yining Mao, Ignacio Cases, Yanan Xie, Peng Qi
    - 🏛️ Institutions: Uniphore
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web agent], [GUI subtask], [reinforcement learning], [WebArchive], [WARC-bench]
    - 📖 TLDR: This paper introduces WARC-Bench, a web-agent benchmark focused on short-horizon GUI subtasks such as date pickers, scroll containers, and other interface widgets that are essential for larger web workflows. It builds 438 tasks on realistic archived webpages using WARC files and shows that even strong computer-use models struggle on these subtasks. The paper also studies supervised fine-tuning and RL with verifiable rewards, showing that targeted subtask training materially improves open models.

- [MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation](https://aclanthology.org/2025.naacl-demo.43/)
    - Zichen Zhu, Hao Tang, Yansi Li, Dingye Liu, Hongshen Xu, Kunyao Lan, Danyang Zhang, Yixuan Jiang, Hao Zhou, Chenrun Wang, Situo Zhang, Liangtai Sun, Yixiao Wang, Yuheng Sun, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, Department of Computer Science and Engineering, MoE Key Lab of Artificial Intelligence, SJTU AI Institute, Shanghai Jiao Tong University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [memory], [adaptive planning], [mobile GUI agent], [MobBench], [MobA]
    - 📖 TLDR: This paper presents MobA, a mobile assistant system built for complex GUI interaction under changing page contexts and limited executor capability. Its core contributions are an adaptive planning module with reflection-based recovery and a multifaceted memory module that supports dynamic execution. The paper also introduces MobBench and reports strong results on both MobBench and AndroidArena for complex mobile task automation.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, Carnegie Mellon University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [human-agent collaboration], [web navigation], [evaluation], [CowPilot]
    - 📖 TLDR: This paper introduces CowPilot, a Chrome-extension framework for mixed-initiative web navigation where an agent proposes actions while a human can pause, reject, override, or resume control during the same task. It is designed both as a collaboration interface and as an evaluation/data-collection platform for web agents. In case studies across five websites, the collaborative setting reaches the highest success rate while substantially reducing the number of steps humans must perform themselves.

- [ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation](https://aclanthology.org/2025.naacl-long.244/)
    - Qinzhuo Wu, Wei Liu, Jian Luan, Bin Wang
    - 🏛️ Institutions: XiaoMi AI Lab
    - 📅 Date: April 2025
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile GUI agent], [page reaching], [task decomposition], [ReachAgent], [MobileReach]
    - 📖 TLDR: This paper argues that mobile agents often optimize locally for the next UI action while missing the larger GUI flow needed to finish a task. It introduces MobileReach, a dataset that decomposes tasks into page-reaching and page-operation subtasks, and trains ReachAgent as a two-stage framework over those subtasks plus reward-based preference flows. The result is stronger step-level and task-level accuracy than prior mobile-agent baselines.

- [Go-Browse: Training Web Agents with Structured Exploration](https://arxiv.org/abs/2506.03533)
    - Apurva Gandhi, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: June 4, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [web agent], [structured exploration], [task generation], [WebArena], [go-browse]
    - 📖 TLDR: This paper frames web-agent data collection as structured exploration over website graphs so agents can reuse information gathered across trajectories instead of exploring each task from scratch. On WebArena, Go-Browse collects 10K successful trajectories and 40K interaction steps across 100 URLs, then uses them to fine-tune a 7B model that surpasses GPT-4o mini and sets a new sub-10B result on the benchmark.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Unaffiliated
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [mobile GUI agent], [GUI-shift]
    - 📖 TLDR: This paper introduces GUI-Shift, a self-supervised reinforcement learning framework for VLM-based GUI agents built around the K-step GUI Transition task, which learns GUI dynamics from unlabeled trajectories without natural-language instruction annotation. The method combines rule-based optimization with data filtering and improves both GUI automation and grounding performance across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro. The paper shows a scalable path to training stronger mobile GUI agents from large amounts of unlabeled interaction data.

- [AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents](https://arxiv.org/abs/2506.14205)
    - Jingxu Xie, Dylan Xu, Xuandong Zhao, Dawn Song
    - 🏛️ Institutions: University of California, Berkeley
    - 📅 Date: June 17, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [synthetic data], [task generation], [computer-use agent], [long-horizon task], [AgentSynth]
    - 📖 TLDR: This paper introduces AgentSynth, a scalable pipeline for automatically generating high-quality tasks and trajectory datasets for generalist computer-use agents. By exploiting information asymmetry between generation and evaluation, it composes simple subtasks into difficult long-horizon tasks and produces more than 6,000 diverse tasks at low cost. The resulting benchmark exposes steep performance degradation in current state-of-the-art agents as task difficulty increases and provides a scalable alternative to expensive human-collected trajectories.

- [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119)
    - Yifan Xu, Xiao Liu, Xinghan Liu, Jiaqi Fu, Hanchen Zhang, Bohao Jing, Shudan Zhang, Yuting Wang, Wenyi Zhao, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Z.AI
    - 📅 Date: September 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [mobile GUI agent], [AndroidWorld], [AndroidLab], [MobileRL], [ADAGRPO]
    - 📖 TLDR: This paper introduces MobileRL, an online reinforcement learning framework for mobile GUI agents centered on the ADAGRPO algorithm for difficulty-adaptive replay, curriculum filtering, and reward shaping over multi-turn tasks. Applied to Qwen2.5-VL-7B-Instruct and GLM-4.1V-9B-Base, it improves sample efficiency and pushes performance to state-of-the-art success rates on both AndroidWorld and AndroidLab. The work is a focused training-framework contribution for strengthening open mobile agents rather than a new benchmark release.

- [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE)
    - Bin Kang, Shaoguo Wen, Yifei Bi, Shunlong Wu, Xinbin Yuan, Rui Shao, Junle Wang, Zhuotao Tian
    - 🏛️ Institutions: Chengdu Institute of Computer Applications, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Tencent Turing Lab, Georgia Institute of Technology, Tsinghua University, Nankai University, Shenzhen Loop Area Institute
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [long-horizon planning], [GUI perception], [GUI task automation], [LongGUIBench], [LongHorizonUI]
    - 📖 TLDR: This paper studies the long-horizon setting where GUI agents fail as interaction chains grow longer and errors compound over time. It introduces LongHorizonUI, a unified framework that combines indexed multimodal perception, structured reflective decision-making, and compensatory execution with rollback to improve robustness on long tasks. The paper also presents LongGUIBench, a benchmark of 371 long-horizon GUI scenarios across apps and games, and reports clear gains over prior GUI-agent baselines on long-horizon automation.

- [OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents](https://arxiv.org/abs/2510.24563)
    - Hongrui Jia, Jitong Liao, Xi Zhang, Haiyang Xu, Tianbao Xie, Chaoya Jiang, Ming Yan, Si Liu, Wei Ye, Fei Huang
    - 🏛️ Institutions: Peking University, Tongyi Lab, Alibaba Group, Beijing Zhongguancun Academy
    - 📅 Date: November 11, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [MCP], [tool-use], [computer-use agent], [OSWorld-MCP]
    - 📖 TLDR: This paper introduces OSWorld-MCP, the first benchmark specifically designed to evaluate tool invocation in computer-use agents alongside standard GUI interaction and decision-making. It builds a validated suite of 158 practical MCP tools across seven common applications and shows that tool access can substantially improve task success, while also revealing that current agents still invoke tools surprisingly rarely. The benchmark adds an important missing dimension to CUA evaluation by explicitly measuring real-world tool-usage capability.

- [Grounding Computer Use Agents on Human Demonstrations](https://arxiv.org/abs/2511.07332)
    - Aarash Feizi, Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Kaixin Li, Rabiul Awal, Xing Han Lu, Johan Obando-Ceron, Juan A. Rodriguez, Nicolas Chapados, David Vazquez, Adriana Romero-Soriano, Reihaneh Rabbany, Perouz Taslakian, Christopher Pal, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, McGill University, Universite de Montreal, ServiceNow Research, University of Waterloo, University of Oxford, National University of Singapore, Polytechnique Montreal, Ecole de Technologie Superieure, CIFAR
    - 📅 Date: November 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [model], [GUI grounding], [desktop grounding], [reinforcement learning], [GroundCUA], [GroundNext]
    - 📖 TLDR: This paper introduces GroundCUA, a large-scale desktop grounding dataset built from expert human demonstrations, covering 87 applications, 56K screenshots, and more than 3.56M human-verified UI annotations. Using this data, the authors train the GroundNext family of grounding models, which achieve state-of-the-art results across five benchmarks with far less training data than prior work, and improve further with reinforcement learning post-training. The paper shows that high-quality human demonstration data is a key driver for robust grounding in general-purpose computer-use agents.

- [K²-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676)
    - Zhe Wu, Donglin Mo, Hongjin Lu, Junliang Xing, Jianheng Liu, Yuheng Jing, Kai Li, Kun Shao, Jianye Hao, Yuanchun Shi
    - 🏛️ Institutions: Tsinghua University, Huawei Noah's Ark Lab, Institute of Automation CAS
    - 📅 Date: February 28, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [hierarchical planning], [mobile GUI agent], [AndroidWorld], [K²-agent]
    - 📖 TLDR: This paper introduces K²-Agent, a hierarchical mobile device control framework that separates declarative “know-what” reasoning from procedural “know-how” execution and co-evolves them during training. Its high-level module refines task knowledge through an SRLR loop, while the low-level executor is trained with curriculum-guided GRPO and dynamic demonstration injection. On AndroidWorld, K²-Agent reaches a new state of the art among open-source screenshot-only systems and also generalizes competitively to ScreenSpot-v2 and Android-in-the-Wild.

- [AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild](https://arxiv.org/abs/2602.11750)
    - Jiazheng Sun, Mingxuan Li, Yingying Zhang, Jiayang Niu, Yachen Wu, Ruihan Jin, Shuyu Lei, Pengrongrui Tan, Zongyu Zhang, Ruoyi Wang, Jiachen Yang, Boyu Yang, Jiacheng Liu, Xin Peng
    - 🏛️ Institutions: Fudan University, Jilin University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [mobile GUI agent], [agent-user interaction], [MUSE], [AmbiBench]
    - 📖 TLDR: This paper introduces AmbiBench, a mobile GUI agent benchmark designed to move beyond idealized one-shot instructions toward realistic intent alignment. It organizes tasks by instruction clarity, includes 240 tasks across 25 applications, and evaluates not only execution success but also interaction quality through the MUSE judge framework. The benchmark highlights how current mobile agents struggle when users are ambiguous or incomplete, and reframes mobile agent evaluation around bidirectional interaction rather than pure instruction following.

- [AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement](https://arxiv.org/abs/2603.17441)
    - Siqi Pei, Liang Tang, Tiaonan Duan, Long Chen, Shuxian Li, Kaer Huang, Yanzhe Jing, Yiqiang Yan, Bo Zhang, Chenghao Jiang, Borui Zhang, Jiwen Lu
    - 🏛️ Institutions: Lenovo Research, Tsinghua University
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [GUI grounding], [instruction refinement], [adaptive zoom], [AdaZoom-GUI]
    - 📖 TLDR: This paper proposes AdaZoom-GUI, a GUI grounding framework that improves both instruction understanding and fine-grained localization on high-resolution interface screenshots. It combines an instruction refinement module with a conditional second-stage zoom-in strategy, and trains the grounding model with GRPO on a newly constructed GUI grounding dataset. The method reports state-of-the-art results among comparable model sizes and is positioned as a practical improvement for robust GUI agent deployment.

- [CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning](https://arxiv.org/abs/2603.02951)
    - Zhenquan Yao, Zitong Huang, Yihan Zeng, Jianhua Han, Hang Xu, Chun-Mei Feng, Jianwei Ma, Wangmeng Zuo
    - 🏛️ Institutions: Harbin Institute of Technology, Huawei Noah's Ark Lab, University College Dublin, Peking University
    - 📅 Date: March 3, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [gradient surgery], [AndroidControl-CL], [CGL]
    - 📖 TLDR: This paper studies continual GUI learning under frequently updated applications and proposes CGL, a framework that balances fast supervised adaptation with reinforcement-learning-based skill retention. It dynamically adjusts the SFT proportion using policy entropy and adds a gradient surgery mechanism that clips SFT updates conflicting with GRPO anchor gradients. The work also introduces AndroidControl-CL to evaluate continual GUI learning and shows the combined design improves adaptation without catastrophic forgetting.

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
    - 🏛️ Institutions: Sookmyung Women's University
    - 📅 Date: February 19, 2026
    - 📑 Publisher: AAMAS 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [multi-agent], [memory], [planning], [skill abstraction], [intent representation], [IntentCUA]
    - 📖 TLDR: This paper introduces IntentCUA, a multi-agent computer-use framework for stabilizing long-horizon desktop automation through intent-aligned plan memory. It learns intent-level representations from interaction traces, abstracts reusable skills, and coordinates a Planner, Plan-Optimizer, and Critic over shared memory to reduce redundant replanning and error accumulation. On end-to-end evaluations over desktop applications, IntentCUA outperforms RL-based and trajectory-centric baselines, highlighting intent abstraction and memory-grounded multi-agent planning as an effective systems design for computer-use agents.

- [Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855)
    - Haiyang Xu, Xi Zhang, Haowei Liu, Junyang Wang, Zhaozai Zhu, Shengjie Zhou, Xuhao Hu, Feiyu Gao, Junjie Cao, Zihua Wang, Zhiyuan Chen, Jitong Liao, Qi Zheng, Jiahui Zeng, Ze Xu, Shuai Bai, Junyang Lin, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: February 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [multi-platform], [reinforcement learning], [open-source model], [tool use], [data synthesis]
    - 📖 TLDR: Mobile-Agent-v3.5 introduces GUI-Owl-1.5, a family of open-source native GUI agent models (2B to 235B) achieving state-of-the-art results on 20+ GUI benchmarks across desktop, mobile, and browser platforms, featuring a hybrid data flywheel, unified agent capability enhancement (including tool/MCP use and memory), and a novel multi-platform environment RL algorithm (MRPO) for long-horizon task training.

- [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662)
    - Deyang Jiang, Jing Huang, Xuanle Zhao, Lei Chen, Liming Zheng, Fanfan Liu, Haibo Qiu, Peng Shi, Zhixiong Zeng
    - 🏛️ Institutions: Meituan
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [planning], [multi-agent], [synthetic trajectory generation], [TreeCUA], [TreeCUA-DPO]
    - 📖 TLDR: This paper targets the scaling bottleneck of GUI planning rather than GUI grounding. It introduces TreeCUA, a multi-agent framework that organizes large-scale GUI exploration trajectories as reusable tree structures, reducing redundant exploration while improving trajectory quality through verification, summarization, and evaluation. The work further proposes TreeCUA-DPO to learn planning from adjacent branch information, yielding strong gains and improved out-of-domain generalization.

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, Princeton University, Shenzhen Loop Area Institute, Shanghai AI Lab
    - 📅 Date: February 5, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [memory], [reinforcement learning], [online RL], [mobile GUI agent], [UI-mem]
    - 📖 TLDR: This paper proposes UI-Mem, a mobile GUI agent training framework that augments online reinforcement learning with a hierarchical experience memory storing reusable workflows, subtask skills, and failure patterns. It introduces stratified group sampling to mix strong, weak, and unguided rollouts, plus a self-evolving loop that continually abstracts new successful plans and error diagnoses back into memory. Experiments on AndroidWorld and AndroidLab show strong gains over standard online RL and static reuse baselines, especially on unseen applications.

- [POINTS-GUI-G: GUI-Grounding Journey](https://arxiv.org/abs/2602.06391)
    - Zhongyin Zhao, Yuan Liu, Yikun Liu, Haicheng Wang, Le Tian, Xiao Zhou, Yangxiu You, Zilin Yu, Yang Yu, Jie Zhou
    - 🏛️ Institutions: WeChat AI
    - 📅 Date: February 6, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [reinforcement learning], [data engineering], [POINTS-GUI-g]
    - 📖 TLDR: This paper studies how to build strong GUI grounding capability starting from a base model without strong pre-existing spatial grounding. It introduces POINTS-GUI-G-8B and attributes its gains to refined multi-source data engineering, improved training strategy for the vision encoder, and reinforcement learning with verifiable rewards. The resulting model achieves state-of-the-art or competitive results across GUI grounding benchmarks including ScreenSpot-Pro, OSWorld-G, ScreenSpot-v2, and UI-Vision.

- [OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution](https://arxiv.org/abs/2601.20380)
    - Le Zhang, Yixiong Xiao, Xinjiang Lu, Jingjia Cao, Yusai Zhao, Jingbo Zhou, Lang An, Zikan Feng, Wanxiang Sha, Yu Shi, Congxi Xiao, Jian Xiong, Yankai Zhang, Hua Wu, Haifeng Wang
    - 🏛️ Institutions: Baidu Frontier Research Department
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [benchmark], [reinforcement learning], [synthetic data], [OSNav], [OmegaUse]
    - 📖 TLDR: This paper introduces OmegaUse, a general-purpose GUI agent for autonomous task execution across both mobile and desktop environments. It combines a curated-and-synthetic data pipeline with a two-stage training recipe of supervised fine-tuning followed by GRPO to improve interaction syntax, spatial grounding, and sequential planning. The work also introduces the OSNav benchmark suite, including ChiM-Nav for Chinese Android environments and Ubu-Nav for Ubuntu desktop navigation, and reports state-of-the-art or leading results across GUI grounding and action benchmarks.

- [Continual GUI Agents](https://arxiv.org/abs/2601.20732)
    - Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng
    - 🏛️ Institutions: Tsinghua University, Zhejiang University, ETH Zurich, Beijing University of Posts and Telecommunications
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [GUI grounding], [domain shift], [GUI-AiF], [continual GUI agents]
    - 📖 TLDR: This paper introduces Continual GUI Agents as a continual learning setting where GUI agents must adapt to domain and resolution shifts over time without losing stable grounding. It proposes GUI-AiF, a reinforcement fine-tuning framework with anchoring-point and anchoring-region rewards that keep agents aligned to changing interaction targets instead of overfitting to static cues. Experiments show the method outperforms prior baselines and frames continual adaptation as a core systems challenge for GUI agents.

- [GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents](https://arxiv.org/abs/2601.18842)
    - Yanxi Wang, Zhiling Zhang, Wenbo Zhou, Weiming Zhang, Jie Zhang, Qiannan Zhu, Yu Shi, Shuxin Zheng, Jiyan He
    - 🏛️ Institutions: Beijing Normal University, Zhongguancun Academy, USTC, A*STAR, Zhongguancun Institution of Artificial Intelligence
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [safety], [privacy-preserving GUI agent], [GUIGuard], [GUIGuard-bench]
    - 📖 TLDR: This paper introduces GUIGuard, a general privacy-preserving framework for GUI agents that separates privacy recognition, privacy protection, and protected task execution. It also builds GUIGuard-Bench, a cross-platform benchmark with 630 trajectories and 13,830 screenshots annotated for privacy grounding, risk levels, categories, and task necessity. Results show that current GUI agents have very weak privacy recognition, while carefully designed protection policies can retain usable task-planning fidelity, making privacy-aware GUI agents a concrete and measurable systems problem.

- [WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents](https://arxiv.org/abs/2601.21872)
    - Yao Zhang, Shijie Tang, Zeyu Li, Zhen Han, Volker Tresp
    - 🏛️ Institutions: Ludwig Maximilian University of Munich, Technical University of Munich, Munich Center for Machine Learning
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [reward model], [process reward model], [web agent], [reasoning verifier], [WebArbiter]
    - 📖 TLDR: This paper introduces WebArbiter, a principle-guided process reward model for web agents that evaluates intermediate reasoning and actions rather than only final outcomes. It is trained to score trajectories using explicit web-navigation principles and supports best-of-N selection during inference. The paper shows that a compact specialized verifier can improve web-agent performance substantially, making it directly relevant to web-agent reinforcement and test-time selection.

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
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [single-shot planning], [branch steering], [OSWorld]
    - 📖 TLDR: This paper studies system-level security for computer-use agents under prompt injection attacks. It introduces Single-Shot Planning, where a trusted planner produces a full execution graph with conditional branches before the agent observes potentially malicious content, giving provable control-flow integrity against injected instructions. The paper also identifies Branch Steering as an additional attack surface and shows on OSWorld that strong security guarantees can be achieved while retaining meaningful utility.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: University of Science and Technology of China, Institute of Artificial Intelligence (TeleAI) China Telecom, Shanghai Innovation Institute, Shanghai Jiao Tong University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [tool-augmented perception], [active perception], [GUI-eyes]
    - 📖 TLDR: This paper proposes GUI-Eyes, a reinforcement learning framework for active visual perception in GUI grounding. Instead of relying on a single static observation, the agent learns when and how to invoke tools such as cropping and zooming through a two-stage perception policy, supported by a spatially continuous reward tailored to tool usage. With only 3k labeled samples, GUI-Eyes-3B substantially improves grounding accuracy on ScreenSpot-Pro, highlighting the value of tool-aware perception for robust GUI agents.

- [MobileDreamer: Generative Sketch World Model for GUI Agent](https://arxiv.org/abs/2601.04035)
    - Yilin Cao, Yufeng Zhong, Zhixiong Zeng, Liming Zheng, Jing Huang, Haibo Qiu, Peng Shi, Wenji Mao, Wan Guanglu
    - 🏛️ Institutions: CAS, UCAS, Meituan
    - 📅 Date: January 7, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [planning], [lookahead], [mobile GUI agent], [MobileDreamer]
    - 📖 TLDR: This paper introduces MobileDreamer, a world-model-based lookahead framework for mobile GUI agents that predicts compact task-relevant future interface sketches rather than full screenshots. Its textual sketch world model preserves spatial information while remaining efficient, and its rollout imagination strategy uses these predicted futures to improve action selection on long-horizon tasks. On AndroidWorld, MobileDreamer achieves state-of-the-art performance and improves task success by 5.25%, showing that lightweight future imagination can materially strengthen mobile GUI planning.

- [MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive, and MCP-Augmented Environments](https://arxiv.org/abs/2512.19432)
    - Quyu Kong, Xu Zhang, Zhenyu Yang, Nolan Gao, Chen Liu, Panrong Tong, Chenglin Cai, Hanzhang Zhou, Jianan Zhang, Liangyu Chen, Zhidan Liu, Steven Hoi, Yue Wang
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group, HKUST(GZ), University of Florida
    - 📅 Date: December 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile GUI agent], [agent-user interaction], [MCP], [cross-app tasks], [MobileWorld]
    - 📖 TLDR: This paper introduces MobileWorld, a more realistic mobile-use benchmark designed to go beyond AndroidWorld by adding longer cross-application tasks, agent-user interaction, and MCP-augmented tool use. It contains 201 tasks across 20 applications with deterministic evaluation backed by snapshots, backend inspection, local storage checks, and callback APIs. Results show a steep performance drop relative to AndroidWorld, highlighting that current mobile GUI agents still struggle substantially with clarification dialogue and hybrid GUI-plus-tool workflows.

- [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047)
    - Hanzhang Zhou, Xu Zhang, Panrong Tong, Jianan Zhang, Liangyu Chen, Quyu Kong, Chenglin Cai, Chen Liu, Yue Wang, Jingren Zhou, Steven Hoi
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [reinforcement learning], [MCP], [device-cloud collaboration], [MAI-UI]
    - 📖 TLDR: This technical report introduces MAI-UI, a family of foundation GUI agents spanning multiple scales and designed for realistic deployment. The work expands beyond UI-only operation by incorporating agent-user interaction, MCP tool calls, a native device-cloud collaboration architecture, and an online reinforcement learning framework for long-horizon training. MAI-UI sets strong results on GUI grounding, AndroidWorld, and MobileWorld, positioning it as a broad real-world-oriented foundation agent stack rather than a single narrow benchmark model.

- [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014)
    - Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover
    - 🏛️ Institutions: UCLA, Panasonic AI Research, Salesforce AI Research
    - 📅 Date: December 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [world model], [planning], [semantic state transition], [MobileWorldBench], [MobileWorld]
    - 📖 TLDR: This paper reframes world modeling for mobile GUI agents as semantic state transition prediction in natural language rather than pixel-space forecasting. It introduces MobileWorldBench to evaluate vision-language models as mobile world models, releases the 1.4M-sample MobileWorld dataset for training, and shows that integrating these semantic world models into planning improves downstream mobile agent success rates. The work establishes semantic world modeling as a practical intermediate layer for stronger mobile GUI planning.

- [HiconAgent: History Context-aware Policy Optimization for GUI Agents](https://arxiv.org/abs/2512.01763)
    - Xurui Zhou, Gongwei Chen, Yuquan Xie, Zaijing Li, Kaiwen Zhou, Shuai Wang, Shuo Yang, Zhuotao Tian, Rui Shao
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Huawei Noah's Ark Lab
    - 📅 Date: December 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [history modeling], [policy optimization], [GUI navigation], [HiconAgent]
    - 📖 TLDR: This paper studies how GUI agents should use historical context during sequential decision making, arguing that naively including full history is both expensive and distracting. It introduces History Context-aware Policy Optimization, combining dynamic context sampling with anchor-guided history compression to train lightweight agents that use past observations and actions more effectively. The resulting HiconAgent-3B improves performance on benchmarks such as GUI-Odyssey, AndroidControl, and AITW while reducing FLOPs and inference cost.

- [GUI Exploration Lab: Enhancing Screen Navigation in Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2512.02423)
    - Yujie Shen, Ruobing Xie, Xuanze Xu, Yichao Zhou, Jinyang Wang, Guangyao Feng, Lifan Yuan, Xiang Ao
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, StepFun, Waseda University, Institute of Automation Chinese Academy of Sciences
    - 📅 Date: December 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [screen navigation], [reinforcement learning], [simulation environment], [multi-turn RL], [exploration strategy]
    - 📖 TLDR: GUI Exploration Lab is a simulation environment engine for GUI agent navigation research that enables flexible composition of screens and navigation graphs; experiments show that supervised fine-tuning provides foundational knowledge, single-turn RL improves generalization, and multi-turn RL develops exploration strategies via trial and error, with findings validated on real-world benchmarks.

- [Computer-Use Agents as Judges for Generative User Interface](https://arxiv.org/abs/2511.15567)
    - Kevin Qinghong Lin, Siyuan Hu, Linjie Li, Zhengyuan Yang, Lijuan Wang, Philip Torr, Mike Zheng Shou
    - 🏛️ Institutions: University of Oxford, Show Lab, National University of Singapore, Microsoft
    - 📅 Date: November 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-native GUI], [automatic GUI design], [AUI-gym], [coder-CUA collaboration]
    - 📖 TLDR: This paper studies how computer-use agents can actively improve interfaces rather than only operate them. It introduces AUI-Gym, a benchmark for automatic GUI development across 52 applications and 1,560 synthesized tasks, together with a Coder-CUA collaboration framework in which a coding model iteratively redesigns interfaces while a computer-use agent judges task solvability through interaction. The work shifts GUI design toward agent-centric efficiency and reliability, showing that agent feedback can materially improve downstream execution success.
||||||| parent of cd78e0c (Add GroundCUA paper entry)
||||||| parent of 3d7304a (Add OSWorld-MCP paper entry)
||||||| parent of 2abe478 (Add LongHorizonUI paper entry)
||||||| parent of e0bd41d (Add MobileRL paper entry)
||||||| parent of 76e33a5 (Add AgentSynth paper entry)
||||||| parent of 79f25be (Add GUI-Shift paper entry)
||||||| parent of 402db00 (Add Go-Browse paper entry)
||||||| parent of 864448c (Add ReachAgent paper entry)
||||||| parent of 8120468 (Add CowPilot paper entry)
||||||| parent of 356ca6e (Add WARC-Bench paper entry)
||||||| parent of 1d5de04 (Add Infogent paper entry)
||||||| parent of 3329d74 (Add GhostEI-Bench paper entry)
||||||| parent of 4fb8a4b (Add Programming with Pixels paper entry)
- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596)
    - Haojia Lin, Xiaoyu Tan, Yulei Qin, Zihan Xu, Yuchen Shi, Zongyi Li, Gang Li, Shaofei Cai, Siqi Cai, Chaoyou Fu, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, Peking University, Nanjing University
    - 📅 Date: October 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [reward model], [computer-using agent], [CUARewardBench], [unanimous prompt ensemble (UPE)]
    - 📖 TLDR: This paper introduces CUARewardBench, the first benchmark for evaluating reward models tailored to computer-using agents. It includes step-level and trajectory-level annotations from tasks across 10 software types and 7 agent architectures. The study identifies the limitations of current reward models and proposes UPE, a prompting-based method that significantly improves evaluation accuracy.

- [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790)
    - Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple, The University of Hong Kong
    - 📅 Date: October 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [tool-use], [hybrid action], [reinforcement learning], [OSWorld], [WindowsAgentArena], [UltraCUA]
    - 📖 TLDR: This paper introduces UltraCUA, a foundation model for computer-use agents that combines low-level GUI actions with high-level programmatic tool calls through a hybrid action space. To support this setting, the authors build an automated tool-collection pipeline, synthesize 17,000+ verifiable computer-use tasks, and train 7B and 32B models with supervised fine-tuning followed by online reinforcement learning. UltraCUA improves OSWorld performance by 22% relative on average while reducing steps, and it also generalizes strongly to WindowsAgentArena without Windows-specific training.

- [UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning](https://arxiv.org/abs/2510.20286)
    - Liangyu Chen, Hanzhang Zhou, Chenglin Cai, Jianan Zhang, Panrong Tong, Quyu Kong, Xu Zhang, Chen Liu, Yuqi Liu, Wenxuan Wang, Yue Wang, Qin Jin, Steven Hoi
    - 🏛️ Institutions: Renmin University of China, Tongyi Lab, Alibaba Group, The Chinese University of Hong Kong
    - 📅 Date: October 23, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [GUI grounding], [instruction-as-reasoning], [UI-ins]
    - 📖 TLDR: This paper reframes GUI grounding instructions as reasoning pathways rather than static text prompts. It first synthesizes diverse, high-quality instruction variants for supervised training, then uses reinforcement learning to optimize pathway selection and composition at inference time. The resulting UI-Ins-7B and UI-Ins-32B models achieve state-of-the-art grounding accuracy across five benchmarks and also improve downstream AndroidWorld agent execution.


- [PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction For Continual Learning](https://arxiv.org/abs/2510.15863)
    - Simon Yu, Gang Li, Weiyan Shi, Peng Qi
    - 🏛️ Institutions: Northeastern University, Uniphore
    - 📅 Date: October 17, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [skill learning], [compositional skills], [transfer generalization], [polymorphism], [PolySkill], [continual learning]
    - 📖 TLDR: This paper introduces **PolySkill**, a framework that enables LLM-based web agents to acquire generalizable and composable skills by decoupling a skill's abstract goal from its concrete implementation, inspired by polymorphic abstraction in software engineering. Evaluated on the Mind2Web benchmark, PolySkill significantly enhances skill reuse, improves task success rates on both seen and unseen websites, and reduces the number of interaction steps, demonstrating effective continual learning and skill transfer capabilities.

- [HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities](https://arxiv.org/abs/2510.12200)
    - Xiaoxue Ren, Penghao Jiang, Kaixin Li, Zhiyong Huang, Xiaoning Du, Jiaojiao Jiang, Zhenchang Xing, Jiamou Sun, Terry Yue Zhuo
    - 🏛️ Institutions: Zhejiang University, University of New South Wales, National University of Singapore, Monash University, CSIRO's Data61, Australian National University
    - 📅 Date: October 14, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [computer-use agent], [web vulnerabilities], [CTF], [HackWorld]
    - 📖 TLDR: This paper introduces HackWorld, the first benchmark for evaluating whether computer-use agents can discover and exploit realistic web application vulnerabilities through visual interaction. It places agents in vulnerable real-world-style web applications and measures attack performance in a Capture-the-Flag setting rather than simplified static security tasks. The benchmark shows that current CUAs have low exploitation success and weak cybersecurity awareness, making it a useful security stress test for web-based computer-use agents.

- [CoAct‑1: Computer‑using Multi-agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: University of Southern California, Salesforce Research, University of Washington
    - 📅 Date: August 5, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hybrid agent], [coding action], [multi-agent system], [OSWorld]
    - 📖 TLDR: This paper introduces **CoAct‑1**, a multi-agent system where an Orchestrator coordinates between a GUI Operator and a Programmer agent that can execute code (Python/Bash) directly. This hybrid design allows the agent to perform complex desktop tasks more efficiently than GUI-only agents. Evaluated on OSWorld and WindowsAgentArena, CoAct‑1 achieves state-of-the-art success rates of 60.8% and 52.5% respectively, while reducing average steps to 10.15.



- [GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding](https://arxiv.org/abs/2510.04039)
    - Bin Lei, Nuo Xu, Ali Payani, Mingyi Hong, Chunhua Liao, Yu Cao, Caiwen Ding
    - 🏛️ Institutions: University of Minnesota, Cisco Research, Lawrence Livermore National Laboratory
    - 📅 Date: October 5, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [tool coordination], [iterative refinement], [visual grounding]
    - 📖 TLDR: This paper proposes GUI-Spotlight, a model for GUI visual grounding that iteratively refines its focus using specialized tools like crop, extract, and find_color. Trained with a hybrid of supervised learning and reinforcement learning, the method dynamically invokes tools over multiple rounds, improving accuracy and efficiency. It significantly outperforms previous methods on benchmarks like ScreenSpot-Pro and UI-Vision with less training data.

- [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670)
    - Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
    - 🏛️ Institutions: Microsoft Research AI Frontiers, Microsoft AI Red Team, University of California, Riverside, NVIDIA
    - 📅 Date: October 2, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer-use agent], [blind goal-directedness], [BLIND-ACT], [risk evaluation]
    - 📖 TLDR: This paper identifies Blind Goal-Directedness as a recurring failure mode in computer-use agents, where agents keep pursuing user goals despite infeasibility, ambiguity, or unsafe context. It introduces BLIND-ACT, a benchmark built on OSWorld to evaluate these subtle safety failures in realistic desktop environments. The results show high rates of blind goal pursuit across frontier CUAs, making the paper directly relevant to safety evaluation of GUI agents beyond prompt injection alone.

- [Say One Thing, Do Another? Diagnosing Reasoning‑Execution Gaps in VLM‑Powered Mobile‑Use Agents](https://arxiv.org/abs/2510.02204)
    - Lingzhong Dong, Ziqi Zhou, Shuaibo Yang, Haiyue Sheng, Pengzhou Cheng, Zongru Wu, Zheng Wu, Gongshen Liu, Zhuosheng Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Beijing Institute of Technology
    - 📅 Date: October 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [evaluation framework], [ground-truth alignment], [reasoning-execution gap], [chain-of-thought], [VLM]
    - 📖 TLDR: This paper investigates reasoning-execution mismatches in VLM-powered mobile agents, revealing that models often generate correct reasoning but fail in execution. It introduces an evaluation framework combining execution accuracy and a new metric called Ground-Truth Alignment (GTA). The authors identify two types of errors—Execution Gap and Reasoning Gap—and show that model scaling alleviates but does not resolve these issues.

- [GUI‑KV: Efficient GUI Agents via KV Cache with Spatio‑Temporal Awareness](https://arxiv.org/abs/2510.00536)
    - Kung‑Hsiang Huang, Haoyi Qiu, Yutong Dai, Caiming Xiong, Chien‑Sheng Wu
    - 🏛️ Institutions: Salesforce AI Research, University of California, Los Angeles
    - 📅 Date: October 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [efficiency], [KV cache compression], [vision-language model], [attention sparsity], [training-free]
    - 📖 TLDR: GUI-KV is a training-free, plug-and-play KV cache compression method for GUI agents that exploits GUI-specific spatial saliency and temporal redundancy to reduce decoding FLOPs by 38.9% while matching or exceeding full-cache accuracy on standard benchmarks.

- [WALT: Web Agents that Learn Tools](https://arxiv.org/abs/2510.01524)
    - Viraj Prabhu, Yutong Dai, Matthew Fernandez, Jing Gu, Krithika Ramakrishnan, Yanqi Luo, Silvio Savarese, Caiming Xiong, Junnan Li, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: October 1, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [tool learning], [tool discovery], [browser automation], [WALT]
    - 📖 TLDR: This paper introduces WALT, a framework that reverse-engineers website functionality into reusable deterministic tools for web agents. Instead of relying on brittle step-by-step UI interaction, the agent invokes learned high-level operations such as search, filter, and content management. On WebArena and VisualWebArena, WALT improves success rates while reducing interaction steps and heavy reasoning overhead, making tool-centric web automation substantially more robust.

- [Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents](https://arxiv.org/abs/2509.26539)
    - Zhen Yang, Zi-Yi Dou, Di Feng, Forrest Huang, Anh Nguyen, Keen You, Omar Attia, Yuhao Yang, Michael Feng, Haotian Zhang, Ram Ramrakhya, Chao Jia, Jeffrey Nichols, Alexander Toshev, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [chain-of-thought], [visual tool-use]
    - 📖 TLDR: This paper presents **Ferret-UI Lite**, a compact 3B end-to-end GUI agent designed for on-device deployment across mobile, web, and desktop. It introduces a mixed real and synthetic GUI dataset, a two-stage training pipeline combining supervised fine-tuning and reinforcement learning with verifiable rewards, and inference-time reasoning and visual cropping strategies. Ferret-UI Lite achieves strong grounding accuracy (91.6% on ScreenSpot-V2) and promising task success rates (28.0% on AndroidWorld, 19.8% on OSWorld), illustrating both the opportunities and challenges of building efficient on-device GUI agents.

- [SCUBA: Salesforce Computer Use Benchmark](https://openreview.net/forum?id=bkjKnO9s7T)
    - Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: Sep 30, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [enterprise automation], [demonstration augmentation], [process rewards], [SCUBA]
    - 📖 TLDR: This paper introduces **SCUBA**, a benchmark for evaluating computer-use agents on 300 enterprise-critical CRM tasks within Salesforce. Tasks span personas like admins and service agents, testing UI navigation, automation, data handling, and troubleshooting. SCUBA includes sandbox environments, milestone-based evaluations, and supports parallel execution. Baseline results show large performance gaps across agent designs, especially between open- and closed-source models, with success rates ranging from 5% to 50% depending on demonstration usage.

- [ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration](https://arxiv.org/abs/2509.21823)
    - Gaole Dai, Shiqi Jiang, Yuanchun Li, Ting Cao, Rui Tan, Mo Li, Yuqing Yang, Lili Qiu
    - 🏛️ Institutions: Nanyang Technological University, Microsoft Research, Institute for AI Industry Research, Tsinghua University, The Hong Kong University of Science and Technology
    - 📅 Date: September 26, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reward system], [GUI agent], [agentic evaluation], [state probing], [ProRe]
    - 📖 TLDR: This paper introduces ProRe, a proactive reward system for GUI agents that combines a general-purpose reasoner with domain-specific evaluator agents that actively probe the environment before assigning rewards. Instead of judging trajectories statically, ProRe gathers additional observations through targeted interaction, which makes reward assignment more verifiable and accurate. Across more than 3,000 trajectories, it improves reward accuracy and F1, and it also boosts downstream GUI-agent task success when used for policy training.

- [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221)
    - Zhaoyang Liu, Jingjing Xie, Zichen Ding, Zehao Li, Bowen Yang, Zhenyu Wu, Xuehui Wang, Qiushi Sun, Shi Liu, Weiyun Wang, Shenglong Ye, Qingyun Li, Xuan Dong, Yue Yu, Chenyu Lu, YunXiang Mo, Yao Yan, Zeyue Tian, Xiao Zhang, Yuan Huang, Yiqian Liu, Weijie Su, Gen Luo, Xiangyu Yue, Biqing Qi, Bowen Zhou, Kai Chen, Yu Qiao, Qifeng Chen, Wenhai Wang
    - 🏛️ Institutions: Shanghai AI Lab
    - 📅 Date: September 18, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [model], [ScaleCUA]
    - 📖 TLDR: This paper presents **ScaleCUA**, a large-scale open-source project for training general-purpose computer use agents (CUAs). The dataset spans 6 operating systems and 3 task domains, built using a hybrid pipeline combining automated agents with human experts. ScaleCUA supports tasks like GUI understanding, grounding, and full interaction. The trained models outperform baselines and set new SOTA on key benchmarks like WebArena-Lite-v2 and MMBench-GUI. The authors also release the full dataset, models, and codebase to promote further research in GUI-based agents.



- [UI‑TARS‑2 Technical Report: Advancing GUI Agent with Multi‑Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)
    - Haoming Wang, Haoyang Zou, Huatong Song, Jiazhan Feng, Junjie Fang, Junting Lu, Longxiang Liu, Qinyu Luo, Shihao Liang, Shijue Huang, Wanjun Zhong, Yining Ye, Yujia Qin, Yuwen Xiong, Yuxin Song, Zhiyong Wu, Aoyan Li, Bo Li, Chen Dun, Chong Liu, Daoguang Zan, Fuxing Leng, Hanbin Wang, Hao Yu, Haobin Chen, Hongyi Guo, Jing Su, Jingjia Huang, Kai Shen, Kaiyu Shi, Lin Yan, Peiyao Zhao, Pengfei Liu, Qinghao Ye, Renjie Zheng, Shulin Xin, Wayne Xin Zhao, Wen Heng, Wenhao Huang, Wenqian Wang, Xiaobo Qin, Yi Lin, Youbin Wu, Zehui Chen, Zihao Wang, Baoquan Zhong, Xinchun Zhang, Xujing Li, Yuanfan Li, Zhongkai Zhao, Chengquan Jiang, Faming Wu, Haotian Zhou, Jinlin Pang, Li Han, Qi Liu, Qianli Ma, Siyao Liu, Songhua Cai, Wenqi Fu, Xin Liu, Yaohui Wang, Zhi Zhang, Bo Zhou, Guoliang Li, Jiajun Shi, Jiale Yang, Jie Tang, Li Li, Qihua Han, Taoran Lu, Woyu Lin, Xiaokang Tong, Xinyao Li, Yichi Zhang, Yu Miao, Zhengxuan Jiang, Zili Li, Ziyuan Zhao, Chenxin Li, Dehua Ma, Feng Lin, Ge Zhang, Haihua Yang, Hangyu Guo, Hongda Zhu, Jiaheng Liu, Junda Du, Kai Cai, Kuanye Li, Lichen Yuan, Meilan Han, Minchao Wang, Shuyue Guo, Tianhao Cheng, Xiaobo Ma, Xiaojun Xiao, Xiaolong Huang, Xinjie Chen, Yidi Du, Yilin Chen, Yiwen Wang, Zhaojian Li, Zhenzhu Yang, Zhiyuan Zeng, Chaolin Jin, Chen Li, Hao Chen, Haoli Chen, Jian Chen, Qinghao Zhao, Guang Shi
    - 🏛️ Institutions: ByteDance Seed
    - 📅 Date: September 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [UI‑TARS‑2]
    - 📖 TLDR: UI‑TARS‑2 is a newly trained native GUI‑centered agent that uses a scalable data flywheel, stabilized multi‑turn reinforcement learning, hybrid GUI + terminal environments, and a unified sandbox. It achieves leading performance across diverse GUI benchmarks (e.g., 88.2 on Online‑Mind2Web), game tasks (~60% human-level), and generalizes to information-seeking and software engineering tasks. Training dynamics and parameter interpolation offer insights into robust, efficient agent RL at scale.

- [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://arxiv.org/abs/2509.02322)
    - Longrong Yang, Zhixiong Zeng, Yufeng Zhong, Jing Huang, Liming Zheng, Lei Chen, Haibo Qiu, Zequn Qin, Lin Ma, Xi Li
    - 🏛️ Institutions: Meituan, Zhejiang University
    - 📅 Date: September 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI agent], [embodied agent], [multitask learning], [mixture-of-experts], [OmniActor]
    - 📖 TLDR: This paper studies how to build a single multimodal agent that can act in both GUI-based 2D environments and embodied 3D settings. It proposes OmniActor, which uses a layer-heterogeneous MoE design to separate deep-layer conflicts between GUI and embodied data while sharing shallow-layer synergy, together with a unified action space and large-scale mixed training data. The reported gains are especially strong on GUI tasks, making it relevant as a broader generalist-agent direction that still materially advances GUI agents.

- [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)
    - Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, Zhengxi Lu, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: August 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [multi-agent], [GUI automation], [trajectory production], [TRPO]
    - 📖 TLDR: The paper introduces **GUI-Owl**, a foundational multimodal GUI agent model built on Qwen2.5-VL, integrating perception, grounding, reasoning, planning, and action execution into one policy network. GUI-Owl-7B achieves strong baseline performance (66.4 on AndroidWorld, 29.4 on OSWorld). The authors further propose **Mobile-Agent-v3**, a general-purpose, multi-agent GUI automation framework that builds on GUI-Owl and achieves state-of-the-art open-source results (73.3 on AndroidWorld, 37.7 on OSWorld). Core innovations include: a large-scale cross-platform cloud-based environment infrastructure with Self-Evolving GUI Trajectory Production; modular foundational agent capabilities; and scalable, asynchronous reinforcement learning using Trajectory-aware Relative Policy Optimization (TRPO). The framework is open-sourced at the X-PLUG MobileAgent GitHub repository.

- [MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers](https://arxiv.org/abs/2508.14704)
    - Ziyang Luo, Zhiqi Shen, Wenzhuo Yang, Zirui Zhao, Prathyusha Jwalapuram, Amrita Saha, Doyen Sahoo, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: August 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [benchmark], [dataset], [framework], [long-horizon reasoning], [unknown-tools challenge], [execution-based evaluation], [MCP-universe]
    - 📖 TLDR: MCP-Universe introduces the first comprehensive benchmark for evaluating large language models (LLMs) through interactions with real-world Model Context Protocol (MCP) servers. It spans six core domains—Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, and Web Searching—across 11 MCP servers. The benchmark employs execution-based evaluators (format, static, dynamic) to rigorously assess agent performance. Despite progress, state-of-the-art models like GPT-5 (43.72% success), Grok-4 (33.33%), and Claude-4.0-Sonnet (29.44%) show significant limitations. The benchmark highlights challenges in long-context reasoning and unfamiliar tool handling, and provides an open-source extensible evaluation framework with UI support to accelerate future research. 

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Z.AI, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [benchmark], [API-GUI paradigm], [dataset], [distributed RL], [entropulse]
    - 📖 TLDR: This paper presents **ComputerRL**, a large-scale end-to-end reinforcement learning framework enabling agents to operate complex desktop tasks. It introduces the **API-GUI paradigm**, combining programmatic API calls with GUI actions, and a **distributed RL infrastructure** managing thousands of parallel virtual Ubuntu desktops for scalable training. A novel **Entropulse** training strategy alternates between reinforcement learning and supervised fine-tuning to prevent entropy collapse over long training runs. Applied to open models like GLM-4-9B-0414, ComputerRL achieves a new state-of-the-art success rate of **48.9%** on the OSWorld benchmark via the GLM-ComputerRL-9B model.

- [You Don’t Know Until You Click: Automated GUI Testing for Production-Ready Software Evaluation](https://arxiv.org/abs/2508.14104)
    - Yutong Bian, Xianhao Lin, Yupeng Xie, Tianyang Liu, Mingchen Zhuge, Siyuan Lu, Haoming Tang, Jinlin Wang, Jiayi Zhang, Jiaqi Chen, Xiangru Tang, Yongxin Ni, Sirui Hong, Chenglin Wu
    - 🏛️ Institutions: DeepWisdom, Fudan University, Hong Kong University of Science and Technology (Guangzhou), University of California San Diego, King Abdullah University of Science and Technology, Westlake University, Stanford University, Yale University, National University of Singapore
    - 📅 Date: August 17, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-as-a-judge], [RealDevWorld], [RealDevBench], [AppEvalPilot], [multimodal]
    - 📖 TLDR: This paper presents **RealDevWorld**, a novel framework to automatically evaluate production-ready GUI software generated by LLMs. It includes **RealDevBench**, a suite of 194 open-ended, multimodal software engineering tasks, and **AppEvalPilot**, an “agent-as-judge” system that simulates realistic GUI interactions to assess functional correctness, visual fidelity, and runtime behavior. It achieves high alignment with human judgment (accuracy 0.92, correlation 0.85), reducing the need for manual review and offering scalable, human-aligned evaluation. Code is available on GitHub.

- [MM-BrowseComp: A Comprehensive Benchmark for Multimodal Browsing Agents](https://arxiv.org/abs/2508.13186)
    - Shilong Li, Xingyuan Bu, Wenjie Wang, Jiaheng Liu, Jun Dong, Haoyang He, Hao Lu, Haozhe Zhang, Chenchen Jing, Zhen Li, Chuanhao Li, Jiayi Tian, Chenchen Zhang, Tianhao Peng, Yancheng He, Jihao Gu, Yuanxing Zhang, Jian Yang, Ge Zhang, Wenhao Huang, Wangchunshu Zhou, Zhaoxiang Zhang, Ruizhe Ding, Shilei Wen
    - 🏛️ Institutions: ByteDance, Nanjing University, M-A-P, CASIA, Zhejiang University
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [multimodal], [multimodal reasoning], [web browsing], [MM-BrowseComp]
    - 📖 TLDR: Introduces **MM-BrowseComp**, a challenging benchmark of 224 handcrafted, multi-hop questions designed to evaluate AI agents’ ability to retrieve and reason over multimodal web content—including images and videos—instead of text alone. Each question includes a verified checklist detailing the necessary reasoning steps. Even top models like OpenAI’s o3 with tools score only ~29% accuracy, underscoring significant shortcomings in current agents' multimodal capabilities and native multimodal reasoning.

- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
    - Zhangxuan Gu, Zhengwen Zeng, Zhenyu Xu, Xingran Zhou, Shuheng Shen, Yunfei Liu, Beitong Zhou, Changhua Meng, Tianyu Xia, Weizhi Chen, Yue Wen, Jingya Dou, Fei Tang, Jinzhen Lin, Yulin Liu, Zhenlin Guo, Yichen Gong, Heng Jia, Changlong Gao, Yuan Guo, Yong Deng, Zhenyu Guo, Liang Chen, Weiqiang Wang
    - 🏛️ Institutions: Ant Group
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [grounding], [navigation], [data cleaning], [Qwen2.5-VL], [UI-venus]
    - 📖 TLDR: This technical report introduces **UI-Venus**, a screenshot-based UI agent built on the multimodal Qwen2.5-VL model and fine-tuned via **reinforcement fine-tuning (RFT)**. It achieves state-of-the-art performance on UI grounding and navigation benchmarks—e.g., Screenspot-V2/Pro (up to 95.3% / 61.9%) and AndroidWorld navigation (up to 65.9%)—by leveraging carefully crafted reward functions, efficient data cleaning pipelines, and a novel **self-evolving framework** (trajectory alignment and sparse action enhancement) to enhance reasoning coherence and handle rare actions. The code and checkpoints are open-sourced to encourage further development.

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y. Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Moonshot AI, Stanford University, University of Waterloo, Carnegie Mellon University
    - 📅 Date: August 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [chain-of-thought], [vision language model], [AgentNet]
    - 📖 TLDR: Introduces **OpenCUA**, an open-source framework to train computer-use agents (CUAs) using vision-language models. It includes a cross-platform annotation tool (AgentNet Tool), a large-scale dataset covering 3 OSes and 200+ apps/websites (AgentNet), and a data processing pipeline that builds state-action pairs enhanced with reflective long chain-of-thought reasoning. The resulting models—especially OpenCUA-72B—achieve SOTA performance on the OSWorld-Verified benchmark (45.0% success), surpassing prior open-source baselines and demonstrating strong generalization and scalability. All tools, models, and data are publicly released.

- [BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent](https://arxiv.org/abs/2508.06600)
    - Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Andrew Liu, Joshua Green, Kshama Patel, Ruoxi Meng, Mingyi Su, Sahel Sharifymoghaddam, Yanxi Li, Haoran Hong, Xinyu Shi, Xuye Liu, Nandan Thakur, Crystina Zhang, Luyu Gao, Wenhu Chen, Jimmy Lin
    - 🏛️ Institutions: University of Waterloo, CSIRO, Independent, Carnegie Mellon University, The University of Queensland
    - 📅 Date: August 8, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [agentic search], [deep research], [BrowseComp-plus]
    - 📖 TLDR: Introduces **BrowseComp-Plus**, a fixed-corpus benchmark for evaluating deep-research agents. It enables controlled, fair, and transparent comparisons by providing human-verified supporting and challenging negative documents for each query. Results reveal significant performance variation—for example, an open-source model (Search-R1 + BM25) only achieves 3.86% accuracy, while GPT-5 reaches 55.9%, and GPT-5 with Qwen3-Embedding-8B retriever achieves 70.1% with fewer queries—highlighting the critical importance of retrieval quality and enabling disentangled analysis of retrieval vs. reasoning components.

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

- [Chain-of-Agents: End-to-End Agent Foundation Models via Multi-Agent Distillation and Agentic RL](https://arxiv.org/abs/2508.13167)
    - Weizhen Li, Jianbo Lin, Zhuosong Jiang, Jingyi Cao, Xinpeng Liu, Jiayu Zhang, Zhenqiang Huang, Qianben Chen, Weichen Sun, Qiexiang Wang, Hongxuan Lu, Tianrui Qin, Chenghao Zhu, Yi Yao, Shuying Fan, Xiaowan Li, Tiannan Wang, Pai Liu, King Zhu, He Zhu, Dingfeng Shi, Piaohong Wang, Yeyi Guan, Xiangru Tang, Minghao Liu, Yuchen Eleanor Jiang, Jian Yang, Jiaheng Liu, Ge Zhang, Wangchunshu Zhou
    - 🏛️ Institutions: OPPO Personal AI Lab, OPPO Research Institute
    - 📅 Date: August 6, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [dataset], [reinforcement learning], [multi-agent], [AFM], [chain-of-agents]
    - 📖 TLDR: The paper introduces **Chain-of-Agents (CoA)**, a novel paradigm enabling a single large language model (LLM) to perform multi-agent style reasoning by dynamically activating tool and role agents within one end-to-end model. They train **Agent Foundation Models (AFMs)** using a two-step approach: first, **multi-agent distillation** to convert trajectories from specialized multi-agent systems into supervised fine-tuning data; second, **agentic reinforcement learning (RL)** to further improve on verifiable tasks. AFMs achieve state-of-the-art performance across web-agent and code-agent benchmarks (e.g., GAIA, WebWalker, BrowseComp, HLE), and the authors open-source all data, model weights, code, and training resources.

- [NaturalGAIA: Pushing the Frontiers of GUI Agents with a Challenging Benchmark and High-Quality Trajectory Dataset](https://arxiv.org/abs/2508.01330)
    - Zihan Zheng, Tianle Cui, Chuwen Xie, Jiahui Zhang, Jiahui Pan, Lewei He, Qianglong Chen
    - 🏛️ Institutions: South China Normal University, Zhejiang University
    - 📅 Date: August 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [hierarchical agent], [reinforcement learning], [causal pathways], [WPSR], [NaturalGAIA]
    - 📖 TLDR: This paper introduces **NaturalGAIA**, a new benchmark based on the principle of **Causal Pathways**, which decomposes complex GUI tasks into programmatically verifiable atomic steps for rigorous and reproducible evaluation. A hierarchical agent architecture called **LightManus** was used to generate a human-verified trajectory dataset representing diverse and self-correcting interaction patterns. This dataset was used to conduct Reinforcement Fine-Tuning (RFT) on the Qwen2.5-VL-7B model. Even top-performing models like Claude-sonnet-4 only reached a Weighted Pathway Success Rate (WPSR) of 34.6%, while RFT improved the smaller model from 3.3% to 10.8%, yet performance dropped significantly in complex scenarios, highlighting current limitations in GUI agent capabilities.

- [Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training](https://arxiv.org/abs/2508.00414)
    - Tianqing Fang, Zhisong Zhang, Xiaoyang Wang, Rui Wang, Can Qin, Yuxuan Wan, Jun-Yu Ma, Ce Zhang, Jiaqi Chen, Xiyun Li, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: Tencent AI Lab
    - 📅 Date: August 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [dataset], [model], [deep research], [reflection], [voting], [agent foundation models]
    - 📖 TLDR: This work introduces **Cognitive Kernel-Pro**, a fully open-source, multi-module agent framework designed to democratize advanced AI agent development. It curates high-quality training data across four domains—web, files, code, and general reasoning—and introduces test-time strategies like reflection and voting to enhance robustness. Evaluated on the GAIA benchmark, its open 8B-parameter model outperforms previous open-source agents such as WebDancer and WebSailor, setting a new performance standard. Code is publicly available.

- [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358)
    - Hussein Mozannar, Gagan Bansal, Cheng Tan, Adam Fourney, Victor Dibia, Jingya Chen, Jack Gerrits, Tyler Payne, Matheus Kunzler Maldaner, Madeleine Grunde-McLaughlin, Eric Zhu, Griffin Bassman, Jacob Alber, Peter Chang, Ricky Loynd, Friederike Niedtner, Ece Kamar, Maya Murad, Rafah Hosn, Saleema Amershi
    - 🏛️ Institutions: Microsoft Research AI Frontiers
    - 📅 Date: July 30, 2025
    - 📑 Publisher: arXiv (also MSR Technical Report MSR-TR-2025-40)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-in-the-loop], [multi-agent], [planning], [memory], [MCP], [safety]
    - 📖 TLDR: Magentic-UI (Multi-agentic User Interface) is an open-source web interface enabling safe, efficient human–agent collaboration through a flexible multi-agent architecture. It supports web browsing, code execution, and file manipulation, and provides six interaction mechanisms—co-planning, co-tasking, multi-tasking, action guards, answer verification, and long-term memory—to integrate human oversight with AI autonomy. Evaluated via agentic benchmarks, simulated user tests, qualitative user study, and safety assessments, it demonstrates how incorporating human-in-the-loop dynamics can significantly improve agentic systems' reliability and performance.

- [WebGuard: Building a Generalizable Guardrail for Web Agents](https://arxiv.org/abs/2507.14293)
    - Boyuan Zheng, Zeyi Liao, Scott Salisbury, Zeyuan Liu, Michael Lin, Qinyuan Zheng, Zifan Wang, Xiang Deng, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Scale AI, University of California, Berkeley
    - 📅 Date: July 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [safety], [guardrail], [WebGuard]
    - 📖 TLDR: Autonomous web agents powered by LLMs can take unintended or harmful actions when interacting with websites (especially state-changing ones). WebGuard is introduced as a dataset to assess risks of web agent actions by collecting nearly 5,000 human‑annotated actions across many real websites, labeled by risk level (SAFE / LOW / HIGH). Baseline LLMs do poorly (<60% accuracy / recall) on detecting high‑risk actions; after fine‑tuning (using Qwen2.5VL‑7B), performance improves significantly (accuracy ~80%, recall on HIGH ~76%), though still not sufficient for very high‑stakes settings. The paper highlights that reliable guardrails for web agents remain an open challenge.

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

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets & Benchmarks Track)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agentic search], [agent-as-a-judge], [evaluation], [Mind2Web 2]
    - 📖 TLDR: This paper introduces **Mind2Web 2**, a benchmark of 130 long-horizon, real-world tasks requiring web browsing and extensive information synthesis. It proposes an **Agent-as-a-Judge** framework to automatically and rigorously evaluate the correctness and source attribution of answers for agentic search systems. Through a detailed evaluation of nine frontier systems, the paper highlights OpenAI’s Deep Research system as the best performer, achieving 50-70% of human performance while reducing time consumption by half. Mind2Web 2 offers a foundation for benchmarking next-generation agentic search systems.

- [Build the Web for Agents, Not Agents for the Web](https://arxiv.org/abs/2506.10953)
    - Xing Han Lù, Gaurav Kamath, Marius Mosbach, Siva Reddy
    - 🏛️ Institutions: McGill, Mila
    - 📅 Date: June 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [agentic web interface], [AWI], [agent design], [interface optimization]
    - 📖 TLDR: This position paper advocates for a paradigm shift in web agent research, proposing the development of Agentic Web Interfaces (AWIs) specifically designed for AI agents. It emphasizes the need for interfaces that cater to the unique capabilities of agents rather than adapting existing human-centric interfaces, aiming to enhance safety, efficiency, and standardization in web agent design.

- [LPO: Towards Accurate GUI Agent Interaction via Location Preference Optimization](https://arxiv.org/abs/2506.09373)
    - Jiaqi Tang, Yu Xia, Yi‑Feng Wu, Yuwei Hu, Yuhui Chen, Qing‑Guo Chen, Xiaogang Xu, Xiangyu Wu, Hao Lu, Yanqing Ma, Shiyin Lu, Qifeng Chen
    - 🏛️ Institutions: Hong Kong University of Science and Technology, Alibaba Group, The Chinese University of Hong Kong, Nanjing University of Science and Technology
    - 📅 Date: June 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [grounding], [navigation], [location reward], [GRPO], [LPO]
    - 📖 TLDR: The paper introduces **Location Preference Optimization (LPO)** to improve GUI agent interaction accuracy. It uses information-entropy-driven zones of interest and a dynamic distance-based reward function. Built atop Group Relative Preference Optimization (GRPO), it enables more precise spatial grounding. Results show SOTA performance on offline benchmarks and real-world online GUI tasks.

- [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://arxiv.org/abs/2506.08012)
    - Penghao Wu, Shengnan Ma, Bo Wang, Jiaheng Yu, Lewei Lu, Ziwei Liu
    - 🏛️ Institutions: Nanyang Technological University, SenseTime Research
    - 📅 Date: June 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [model], [benchmark], [self-reflection], [GUI‑Reflection task suite]
    - 📖 TLDR: Introduces **GUI‑Reflection**, a framework that enhances multimodal GUI agents with self-reflection and error correction. It spans three training stages—pre‑training with reflection tasks, offline supervised fine‑tuning with autogenerated error scenarios, and online iterative reflection tuning—resulting in improved robustness on AndroidWorld and the novel GUI‑Reflection Task Suite using entirely automated pipelines.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, and Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: June 4, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
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
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [vision language model], [Holo1], [WebClick], [WebVoyager], [surfer-h]
    - 📖 TLDR: Introduces **Surfer‑H**, a modular web-browsing agent (policy, localizer, validator) that operates purely via screenshots, paired with **Holo1**, a family of open-weight VLMs specialized in UI interaction. Holo1 is trained on a 31B token dataset across GUI grounding, visual reasoning, and agent traces, enabling strong UI localization via the new **WebClick** benchmark. Surfer‑H + Holo1‑7B achieves 92.2% success on WebVoyager—a state-of-the-art and cost-efficient web navigation performance—while releasing both the model weights and evaluation dataset.

- [GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents](https://arxiv.org/abs/2506.03143)
    - Qianhui Wu, Kanzhi Cheng, Rui Yang, Chaoyun Zhang, Jianwei Yang, Huiqiang Jiang, Jian Mu, Baolin Peng, Bo Qiao, Reuben Tan, Si Qin, Lars Liden, Qingwei Lin, Huan Zhang, Tong Zhang, Jianbing Zhang, Dongmei Zhang, Jianfeng Gao
    - 🏛️ Institutions: Microsoft, Nanjing University, University of Illinois Urbana-Champaign
    - 📅 Date: June 3, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
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

- [AgentCPM‑GUI: Building Mobile‑Use Agents with Reinforcement Fine‑Tuning](https://aclanthology.org/2025.emnlp-demos.12/)
    - Zhong Zhang, Yaxi Lu, Yikun Fu, Yupeng Huo, Shenzhi Yang, Yesai Wu, Han Si, Xin Cong, Haotian Chen, Yankai Lin, Jie Xie, Wei Zhou, Wang Xu, Yuanheng Zhang, Zhou Su, Zhongwu Zhai, Xiaoming Liu, Yudong Mei, Jianming Xu, Hongyan Tian, Chongyi Wang, Chi Chen, Yuan Yao, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Tsinghua University, Renmin University of China, ModelBest
    - 📅 Date: June 2, 2025
    - 📑 Publisher: EMNLP 2025 System Demonstrations
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [reinforcement fine‑tuning], [compact action space], [CAGUI], [GRPO]
    - 📖 TLDR: Introduces an 8 B Vision–Language GUI agent for on‑device mobile app interaction. Training uses grounding pre-training, supervised fine‑tuning on 55 K Chinese & English trajectories, and reinforcement fine‑tuning (GRPO). A compact JSON action schema enables low-latency inference. Achieves SOTA on five benchmarks including the new Chinese CAGUI (96 %+ TM, 91 % EM). All code, model, and data released.

- [ZeroGUI: Automating Online GUI Learning at Zero Human Cost](https://arxiv.org/abs/2505.23762)
    - Chenyu Yang, Shiqian Su, Shi Liu, Xuan Dong, Yue Yu, Weijie Su, Xuehui Wang, Zhaoyang Liu, Jinguo Zhu, Hao Li, Wenhai Wang, Yu Qiao, Xizhou Zhu, Jifeng Dai
    - 🏛️ Institutions: Shanghai AI Laboratory, Tsinghua University, Shanghai Jiao Tong University, Hong Kong University of Science and Technology, The Chinese University of Hong Kong
    - 📅 Date: May 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [model-free], [VLM-task-generation], [VLM-reward-estimation], [ZeroGUI]
    - 📖 TLDR: Introduces **ZeroGUI**, a novel online learning framework that enables GUI agents (based on VLMs) to learn by autonomous interaction without human labels. It uses vision-language models to (i) generate diverse task instructions, (ii) evaluate task success, and (iii) apply a two-stage RL strategy (task-generated training + test-time adaptation). The method shows strong performance gains (e.g., +14% on UI-TARS, +63% on Aguvis) in desktop (OSWorld) and mobile (AndroidLab) GUI benchmarks, proving scalable, human-free GUI-agent training.  

- [UI-Evol: Automatic Knowledge Evolving for Computer Use Agents](https://arxiv.org/abs/2505.21964)
    - Ziyun Zhang, Xinyi Liu, Xiaoyi Zhang, Jun Wang, Gang Chen, Yan Lu
    - 🏛️ Institutions: Peking University, Microsoft Research Asia
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [knowledge-execution gap], [critique stage], [retrace stage], [OSWorld], [self‑evolution]
    - 📖 TLDR: The paper identifies a “knowledge‑execution gap” where even highly accurate external knowledge (90%) only yields a 41% execution success rate. To bridge this, the authors introduce **UI‑Evol**, a plug‑and‑play two‑stage module for GUI agents—**Retrace** recovers actual action sequences from real agent–environment interactions, and **Critique** refines knowledge by comparing these sequences with external references. Experiments using Agent S2 on the OSWorld benchmark show significant gains in task performance and reduced behavioral variance, improving agent reliability.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [CUA], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [XBOUND: Exploring the Capability Boundaries of Device-Control Agents through Trajectory Tree Exploration](https://arxiv.org/abs/2505.21279)
    - Shaoqing Zhang, Kehai Chen, Zhuosheng Zhang, Rumei Li, Rongxiang Weng, Yang Xiang, Liqiang Nie, Min Zhang
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Pengcheng Laboratory, Shanghai Jiao Tong University, Meituan
    - 📅 Date: May 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [dataset], [Explore Metric], [trajectory tree], [OS‑Atlas], [UI‑TARS]
    - 📖 TLDR: Introduces **XBOUND**, a novel evaluation framework assessing device-control (DC) agents at a fine-grained level by constructing "trajectory trees" from Android GUI interaction traces. The method defines an **Explore Metric**, measuring how well agents generalize across branching states and actions. A large-scale pseudo trajectory-tree dataset (~1,536 episodes, 43,759 instructions) was built using GPT4o-mini and Qwen2.5-vl. The study benchmarks OS‑Atlas and UI‑TARS agents across width/depth dimensions, revealing state and action comprehension gaps. It offers actionable insights into DC agent limitations and proposes directions for improving GUI-based agent capabilities.

- [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660)
    - Qinzhuo Wu, Pengzhi Gao, Wei Liu, and Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc.
    - 📅 Date: May 27, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [error detection], [backtracking], [Mobile3M], [Auto‑UI]
    - 📖 TLDR: BacktrackAgent introduces a novel GUI‑agent framework that embeds four components—generator, verifier, judger, and reflector—to detect when actions go wrong, evaluate their effects, and backtrack to recover. It also constructs specialized datasets for training these “judgment” and “reflection” modules. On Mobile3M and Auto‑UI benchmarks, it boosts task success rate by ~7.6% and step accuracy by ~1.6%, outperforming prior SOTA like MobileVLM and ReachAgent.

- [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://openreview.net/forum?id=bJvwJahJeF)
    - Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiaochong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu
    - 🏛️ Institutions: The University of Hong Kong, Shanghai AI Laboratory, Fudan University, Peking University, Nanjing University, East China Normal University, Yale University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [environment], [POMDP], [GUI/CLI agents], [multimodal], [modular design], [ScienceBoard]
    - 📖 TLDR: Introduces **ScienceBoard**, a first-of-its-kind realistic multimodal environment and benchmark (169 tasks across six scientific domains) for evaluating agents that operate GUI and CLI workflows. Agents like GPT‑4o and Claude reach only ~15% success, revealing limitations in visual grounding and domain reasoning. Modular agent designs (separating planning and action) improve performance. Environment integrates real scientific tools via VM, accessibility trees, and screenshot inputs, setting the stage for more capable AI co‑scientists.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, Shanghai Jiao Tong University AI Institute, Shanghai Jiao Tong University, Jiangsu Key Lab of Language Computing, Suzhou Laboratory
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [reward model], [progress reward], [LCS], [ProgRM]
    - 📖 TLDR: Introduces **ProgRM**, a novel framework giving dense intermediate rewards to GUI agents by estimating per‑step task progress. Labels are generated through an LCS‑based self‑annotation algorithm that identifies key steps in successful trajectories. Agents trained with ProgRM outperform outcome‑based reward models and proprietary LLMs like Claude‑3.7‑Sonnet across benchmarks.

- [GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://aclanthology.org/2025.acl-long.282/)
    - Bin Xie, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Jie Liu, Min Zhang, Liqiang Nie
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Huawei Noah's Ark Lab
    - 📅 Date: May 22, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [transition-aware knowledge], [autonomous exploration], [benchmark], [GUI-KRB]
    - 📖 TLDR: Introduces **GUI‑explorer**, a training‑free agent for mobile GUIs that auto‑generates function‑aware exploration goals and mines transition‑aware knowledge from UI transitions. It builds a multimodal knowledge store and dynamically guides MLLMs like GPT‑4o at runtime, achieving state‑of‑the‑art success rates (53.7% on SPA‑Bench, 47.4% on AndroidWorld) without retraining. Also introduces GUI‑KRB, a benchmark highlighting GUI reasoning limitations and guiding future work.

- [Unlocking Smarter Device Control: Foresighted Planning with a World Model-Driven Code Execution Approach](https://arxiv.org/abs/2505.16422)
    - Xiaoran Yin, Xu Luo, Hao Wu, Lianli Gao, Jingkuan Song
    - 🏛️ Institutions: University of Electronic Science and Technology of China, Tongji University, University of Trento
    - 📅 Date: May 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [executable code], [self‑verification], [self‑refinement], [FPWC]
    - 📖 TLDR: This paper introduces **Foresighted Planning with World Model-Driven Code Execution** (FPWC), a novel framework that improves multi-step mobile device control by constructing a text-based, refinable world model at task start. Plans are generated as executable Python code enabling structured reasoning, loops, and conditional logic. The system dynamically self-verifies via zoom-in visual confirmation and iteratively refines both model and plan based on new observations. Experiments in simulation and on real devices show ~44% relative improvement in task success over prior reactive baselines, demonstrating strong performance in both single- and cross-app tasks.

- [Building a Stable Planner: An Extended Finite State Machine Based Planning Module for Mobile GUI Agent](https://arxiv.org/abs/2505.14141)
    - Fanglin Mo, Junzhe Chen, Haoxuan Zhu, Xuming Hu
    - 🏛️ Institutions: Hong Kong University of Science and Technology (Guangzhou), South China University of Technology
    - 📅 Date: May 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [EFSM], [SPlanner], [planning], [vision language model], [AndroidWorld benchmark]
    - 📖 TLDR: Introduces **SPlanner**, a plug‑and‑play planning module that models mobile apps as Extended Finite State Machines (EFSMs). It decomposes user instructions into primary functions, traverses EFSMs to obtain execution paths, and refines these into natural-language plans to guide vision‑language models. On the AndroidWorld benchmark, pairing SPlanner with Qwen2.5‑VL‑72B achieves 63.8% success—28.8 points higher than the baseline, demonstrating improved stability and task planning in mobile GUI agents.

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

- [A Summary on GUI Agents with Foundation Models Enhanced by Reinforcement Learning](https://arxiv.org/abs/2504.20464)
    - Jiahao Li, Kaer Huang
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: April 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [framework], [reinforcement learning], [multimodal], [training taxonomy]
    - 📖 TLDR: This paper presents a structured summary of recent advances in GUI agents powered by Multi-modal Large Language Models (MLLMs) and enhanced through Reinforcement Learning (RL). It formalizes GUI agent tasks as Markov Decision Processes and reviews modular architectures comprising Perception, Planning, and Acting modules. The study categorizes training methodologies into Prompt-based, Supervised Fine-Tuning (SFT), and RL-based approaches, highlighting the progression towards dynamic policy learning. The paper concludes by identifying key challenges and future directions for developing more capable and reliable GUI agents.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, Wenhao Wang, Tianze Wu, Linghao Li, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab, The Chinese University of Hong Kong MMLab
    - 📅 Date: April 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [framework], [dataset], [benchmark], [planning], [multimodal], [taxonomy]
    - 📖 TLDR: This comprehensive survey examines the evolution of LLM-powered GUI agents in mobile phone automation, transitioning from static scripts to intelligent, adaptive systems. It presents a taxonomy encompassing agent frameworks (single-agent, multi-agent, plan-then-act), modeling approaches (prompt engineering, training-based), and essential datasets and benchmarks. The paper discusses how LLMs enhance language understanding, multimodal perception, and decision-making in GUI tasks, and addresses challenges such as dataset diversity, on-device deployment efficiency, user-centric adaptation, and security concerns. It serves as a definitive reference for researchers and practitioners aiming to leverage LLMs in designing scalable, user-friendly phone GUI agents.

- [UFO2: The Desktop AgentOS](https://arxiv.org/abs/2504.14603)
    - Chaoyun Zhang, He Huang, Chiming Ni, Jian Mu, Si Qin, Shilin He, Lu Wang, Fangkai Yang, Pu Zhao, Chao Du, Liqun Li, Yu Kang, Zhao Jiang, Suzhen Zheng, Rujia Wang, Jiaxu Qian, Minghua Ma, Jian-Guang Lou, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
    - 🏛️ Institutions: Microsoft Research, Zhejiang University-University of Illinois Urbana-Champaign Institute, Nanjing University, Peking University
    - 📅 Date: April 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [hybrid control], [multi-agent], [speculative execution], [knowledge substrate], [UFO2]
    - 📖 TLDR: UFO2 introduces a multi-agent AgentOS for Windows desktops, aiming to transform Computer-Using Agents (CUAs) from fragile prototypes into robust, system-level automation tools. It features a centralized HostAgent for task decomposition and coordination, along with specialized AppAgents equipped with native APIs and domain-specific knowledge. The system employs a hybrid control detection pipeline combining Windows UI Automation with vision-based parsing, and enhances runtime efficiency through speculative multi-action planning. A Picture-in-Picture interface allows agents and users to operate concurrently without interference. Evaluated across over 20 real-world Windows applications, UFO2 demonstrates significant improvements in robustness and execution accuracy over prior CUAs.

- [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)
    - Yuhang Liu, Pengxiang Li, Congkai Xie, Xavier Hu, Xiaotian Han, Shengyu Zhang, Hongxia Yang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Dalian University of Technology, Reallm Labs, The Hong Kong Polytechnic University
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [model], [reinforcement learning], [planning], [reasoning], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: This paper introduces **InfiGUI-R1**, a multimodal GUI agent developed through the **Actor2Reasoner** framework, aiming to transition agents from reactive behaviors to deliberative reasoning. The framework comprises two stages: *Reasoning Injection*, which employs Spatial Reasoning Distillation to integrate GUI visual-spatial information with logical reasoning, and *Deliberation Enhancement*, which uses Reinforcement Learning with Sub-goal Guidance and Error Recovery Scenario Construction to refine the agent's planning and error correction capabilities. Evaluations on benchmarks like AndroidControl and ScreenSpot demonstrate that InfiGUI-R1-3B achieves state-of-the-art performance in GUI grounding and trajectory tasks, outperforming larger models in several categories.

- [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, Shibo He, Wenchao Meng
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab
    - 📅 Date: April 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [few-shot learning], [LearnAct], [LearnGUI], [DemoParser], [KnowSeeker], [ActExecutor]
    - 📖 TLDR: This paper introduces **LearnAct**, a multi-agent framework designed to enhance mobile GUI agents through few-shot demonstration learning. Accompanied by **LearnGUI**, a dataset comprising 2,252 offline and 101 online tasks with high-quality human demonstrations, the framework integrates three specialized agents—DemoParser, KnowSeeker, and ActExecutor—to extract, retrieve, and apply knowledge from demonstrations. Experimental results show significant performance improvements in both offline and online evaluations, establishing demonstration-based learning as a promising direction for developing adaptable and personalized mobile GUI agents.

- [TongUI: Building Generalized GUI Agents by Learning from Multimodal Web Tutorials](https://arxiv.org/abs/2504.12679)
    - Bofei Zhang, Zirui Shang, Zhi Gao, Wang Zhang, Rui Xie, Xiaojian Ma, Tao Yuan, Xinxiao Wu, Song-Chun Zhu, Qing Li
    - 🏛️ Institutions: Beijing Institute for General Artificial Intelligence, Beijing Institute of Technology, Peking University, Shanghai Jiao Tong University, Tsinghua University
    - 📅 Date: April 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [Qwen2.5-VL], [GUI-net], [multimodal], [trajectory generation]
    - 📖 TLDR: This paper introduces **TongUI**, a framework for building generalized GUI agents by learning from multimodal web tutorials. By crawling and processing online tutorials into GUI agent trajectory data, the authors construct the **GUI-Net** dataset containing 143K trajectories across five operating systems and over 200 applications. Fine-tuning Qwen2.5-VL-3B/7B models on GUI-Net leads to significant performance improvements on grounding and navigation benchmarks, demonstrating the effectiveness of the TongUI framework.

- [REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)
    - Divyansh Garg, Shaun VanWeelden, Diego Caples, Andis Draguns, Nikil Ravi, Pranav Putta, Naman Garg, Tomas Abraham, Michael Lara, Federico Lopez, James Liu, Atharva Gundawar, Prannay Hebbar, Youngchul Joo, Jindong Gu, Charles London, Christian Schroeder de Witt, Sumeet Motwani
    - 🏛️ Institutions: The AGI Company, Stanford University, University of Oxford, Mercor, Contramont Research, Plato, Independent
    - 📅 Date: April 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [dataset], [evaluation], [reproducibility], [multi-turn tasks], [real]
    - 📖 TLDR: This paper introduces **REAL**, a benchmark and framework designed for evaluating autonomous agents through deterministic simulations of real-world websites. REAL encompasses high-fidelity replicas of 11 widely-used websites across domains like e-commerce, travel, communication, and professional networking. It includes 112 practical tasks that mirror complex user interactions requiring both accurate information retrieval and state-changing actions. The controlled environment ensures safety and reproducibility, combining programmatic checks for action-based tasks with rubric-guided LLM-based judgments for information retrieval. Empirical results reveal that current frontier language models achieve at most a 41% success rate on REAL, highlighting significant gaps in autonomous web navigation and task completion capabilities.

- [UI-E2I-Synth: Advancing GUI Grounding with Large-Scale Instruction Synthesis](https://aclanthology.org/2025.findings-acl.809/)
    - Xinyi Liu, Xiaoyi Zhang, Ziyun Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia, Peking University
    - 📅 Date: April 15, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [instruction synthesis], [UI-E2I-synth], [UI-I2E-bench], [GPT-4o]
    - 📖 TLDR: This paper introduces **UI-E2I-Synth**, a large-scale data synthesis pipeline that generates diverse GUI grounding instructions using GPT-4o, addressing challenges like implicit instructions and unbalanced element types. It also presents **UI-I2E-Bench**, a new benchmark with detailed annotations for evaluating GUI instruction grounding. Models trained on the synthesized data demonstrate superior performance across multiple platforms, highlighting the effectiveness of the proposed approach.

- [Breaking the Data Barrier -- Building GUI Agents Through Task Generalization](https://openreview.net/forum?id=QDtORaZt8K)
    - Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, Qiushi Sun, Zhenzhong Lan, Junxian He
    - 🏛️ Institutions: Zhejiang University, Westlake University, Shanghai AI Laboratory, The University of Hong Kong, Hong Kong University of Science and Technology
    - 📅 Date: April 14, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [mid-training], [reasoning], [GUIMid]
    - 📖 TLDR: This paper introduces a mid-training approach to enhance GUI agents by leveraging diverse, reasoning-intensive datasets such as mathematical and coding tasks. The authors demonstrate that training Vision Language Models (VLMs) on these data-rich tasks before fine-tuning on limited GUI trajectory data significantly improves performance on GUI benchmarks like WebArena and AndroidWorld. Notably, text-only mathematical reasoning data led to substantial cross-modal gains, highlighting the effectiveness of task generalization in overcoming data scarcity challenges in GUI agent development.

- [GUI-R1: A Generalist R1-Style Vision-Language Action Model for GUI Agents](https://arxiv.org/abs/2504.10458)
    - Run Luo, Lu Wang, Wanwei He, Longze Chen, Jiaming Li, Min Yang, Xiaobo Xia
    - 🏛️ Institutions: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences, National University of Singapore
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [GRPO], [GUI-R1]
    - 📖 TLDR: GUI-R1 introduces a reinforcement learning framework that enhances the capabilities of Large Vision-Language Models (LVLMs) for GUI agents. By employing a unified action space and a rule-based reward function, the model efficiently learns to perform high-level tasks across multiple platforms, including Windows, Linux, MacOS, Android, and Web. Utilizing only 0.02% of the data compared to previous methods, GUI-R1 demonstrates superior performance on eight benchmarks, showcasing the potential of reinforcement learning in GUI agent tasks.

- [RealWebAssist: A Benchmark for Long-Horizon Web Assistance with Real-World Users](https://arxiv.org/abs/2504.10445)
    - Suyu Ye, Haojun Shi, Darren Shih, Hyokun Yun, Tanya G. Roosta, Tianmin Shu
    - 🏛️ Institutions: Johns Hopkins University, Amazon
    - 📅 Date: April 14, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [GUI grounding], [speech input], [spatial reasoning], [temporal reasoning], [multi-step planning], [routine learning], [RealWebAssist]
    - 📖 TLDR: RealWebAssist introduces a benchmark for evaluating AI agents' ability to assist with long-horizon web tasks using sequential instructions from real-world users. The dataset includes 1,885 instructions across 107 tasks on 66 websites, featuring challenges like ambiguous instructions, GUI grounding, and evolving user goals. Evaluations show that current state-of-the-art models struggle with these complex, realistic scenarios.

- [AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://arxiv.org/abs/2504.08942)
    - Xing Han Lù, Amirhossein Kazemnejad, Nicholas Meade, Arkil Patel, Dongchan Shin, Alejandra Zambrano, Karolina Stańczak, Peter Shaw, Christopher J. Pal, Siva Reddy
    - 🏛️ Institutions: McGill, Mila, Google DeepMind, Polytechnique Montréal, ServiceNow Research
    - 📅 Date: April 11, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [LLM judges], [AgentRewardBench]
    - 📖 TLDR: This paper introduces *AgentRewardBench*, a benchmark designed to assess the effectiveness of large language model (LLM) judges in evaluating web agent trajectories. The benchmark comprises 1,302 trajectories across five web benchmarks, each annotated by experts for success, side effects, and repetitiveness. Evaluations of 12 LLM judges reveal that no single model excels across all benchmarks, and that rule-based evaluations often underreport agent success rates, highlighting the need for more adaptable automatic evaluation methods.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: The Ohio State University, Carnegie Mellon University, University of Virginia, Purdue University, Cisco Research
    - 📅 Date: April 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [transfer learning], [WebArena]
    - 📖 TLDR: SkillWeaver is a framework that enables web agents to autonomously improve by discovering, practicing, and refining reusable skills, encapsulated as APIs. Through iterative exploration, agents build a library of plug-and-play APIs, enhancing their capabilities. Experiments on WebArena and real-world websites demonstrate significant performance improvements, and the synthesized APIs can be shared among agents to boost overall performance.

- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University, Microsoft
    - 📅 Date: April 9, 2025
    - 📑 Publisher: COLM 2025
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

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://openreview.net/forum?id=6jZi4HSs6o)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: April 2, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [online-Mind2Web], [WebJudge], [operator], [LLM-as-a-judge]
    - 📖 TLDR: This paper critically evaluates the performance of current web agents, revealing that many underperform on the newly introduced **Online-Mind2Web** benchmark, which comprises 300 realistic tasks across 136 websites. The study highlights a discrepancy between reported successes and actual capabilities, attributing this to shortcomings in existing benchmarks. To address evaluation scalability, the authors propose **WebJudge**, an automatic LLM-based evaluation method achieving approximately 85% agreement with human judgments. The comprehensive analysis underscores the need for more robust assessment frameworks in web agent research.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 1, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [mixture-of-grounding], [proactive hierarchical planning], [benchmark], [OSWorld], [WindowsAgentArena], [AndroidWorld]
    - 📖 TLDR: This paper introduces *Agent S2*, a compositional framework for computer use agents that combines generalist and specialist models to address challenges in GUI element grounding and long-horizon task planning. The framework employs a novel Mixture-of-Grounding technique for precise GUI localization and Proactive Hierarchical Planning to dynamically refine action plans. Evaluations demonstrate that Agent S2 achieves state-of-the-art performance on benchmarks like OSWorld, WindowsAgentArena, and AndroidWorld, outperforming existing agents such as Claude Computer Use and UI-TARS.

- [A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350)
    - Liangbo Ning, Ziran Liang, Zhuohang Jiang, Haohao Qu, Yujuan Ding, Wenqi Fan, Xiao-yong Wei, Shanru Lin, Hui Liu, Philip S. Yu, Qing Li
    - 🏛️ Institutions: The Hong Kong Polytechnic University, City University of Hong Kong, Michigan State University, University of Illinois Chicago
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [survey], [framework], [training], [trustworthiness], [WebAgents], [large foundation models]
    - 📖 TLDR: This comprehensive survey examines the development of WebAgents—AI agents designed to automate web tasks—by leveraging Large Foundation Models (LFMs). It delves into the architectures, training methodologies, and trustworthiness of these agents, providing a detailed overview of current research and proposing future directions to enhance their effectiveness and reliability in web automation.

- [UI-R1: Enhancing Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, The Chinese University of Hong Kong
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [UI-R1-3B], [GRPO], [AndroidControl], [ScreenSpot-pro]
    - 📖 TLDR: This paper introduces **UI-R1**, a framework that enhances the reasoning capabilities of multimodal large language models (MLLMs) for GUI action prediction tasks through rule-based reinforcement learning. Utilizing a small, high-quality dataset of 136 challenging mobile tasks, the authors design a unified rule-based action reward function and optimize the model using Group Relative Policy Optimization (GRPO). The resulting model, **UI-R1-3B**, demonstrates significant improvements over the base model (Qwen2.5-VL-3B) on both in-domain (AndroidControl) and out-of-domain (ScreenSpot-Pro) benchmarks, showcasing the effectiveness of rule-based RL in advancing GUI understanding and control.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Tsinghua University, Nanyang Technological University, The University of Texas at Austin
    - 📅 Date: March 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [benchmark], [v-droid], [verifier-driven], [pair-wise preference training], [human-agent joint annotation], [low-latency]
    - 📖 TLDR: This paper introduces **V-Droid**, a mobile GUI automation agent that leverages large language models (LLMs) as verifiers rather than generators. By evaluating candidate actions before execution, V-Droid enhances decision-making accuracy and reduces latency. The framework incorporates discretized action space construction, a prefilling-only workflow, pair-wise preference training, and a scalable human-agent joint annotation scheme. Evaluated on benchmarks like AndroidWorld, AndroidLab, and MobileAgentBench, V-Droid achieves state-of-the-art success rates and operates with near-real-time decision-making capabilities.

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

- [In-Context Defense in Computer Agents: An Empirical Study](https://arxiv.org/abs/2503.09241)
    - Pei Yang, Hai Ci, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: March 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [defense], [in-context learning], [chain-of-thought], [context deception], [security]
    - 📖 TLDR: This paper introduces an in-context defense strategy for computer agents powered by vision-language models (VLMs), targeting context deception attacks such as malicious pop-ups and deceptive HTML elements. By incorporating a small set of curated exemplars and employing chain-of-thought reasoning, the approach guides agents to perform explicit defensive reasoning before action planning. Experiments demonstrate significant reductions in attack success rates across various attack types, highlighting the effectiveness of the method in enhancing agent reliability without requiring model fine-tuning.

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: March 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [dual-system cognition], [FOCUS], [ScreenSpot], [ScreenSpot-pro]
    - 📖 TLDR: This paper introduces **FOCUS**, a novel GUI grounding framework inspired by human dual-system cognition. FOCUS dynamically switches between a fast, intuitive system and a slow, analytical system based on task complexity. The framework decomposes GUI grounding into three stages: interface summarization, focused analysis, and precise coordinate prediction. Trained on a synthesized dataset of 300,000 samples, FOCUS achieves state-of-the-art performance on the ScreenSpot and ScreenSpot-Pro benchmarks, demonstrating significant improvements in both efficiency and accuracy for complex GUI interactions.

- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis](https://arxiv.org/abs/2502.20383)
    - Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
    - 🏛️ Institutions: University of Maryland
    - 📅 Date: March 4, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [security], [jailbreaking], [evaluation], [OpenHands]
    - 📖 TLDR: This paper investigates why Web AI agents are significantly more susceptible to executing harmful commands compared to standalone LLMs, despite sharing the same underlying models. Through a fine-grained evaluation, the authors identify three critical factors contributing to this vulnerability: embedding user goals into system prompts, multi-step action generation, and processing of event streams from web navigation. The study introduces a five-level harmfulness evaluation framework and utilizes the OpenHands platform to systematically assess these vulnerabilities, revealing a 46.6% success rate in malicious task execution by Web AI agents versus 0% for standalone LLMs.

- [LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](https://aclanthology.org/2025.naacl-demo.16/)
    - Danqing Zhang, Balaji Rama, Jingyi Ni, Shiying He, Fu Zhao, Kunyu Chen, Arnold Chen, Junyu Cao
    - 🏛️ Institutions: PathOnAI.org, Rutgers University, The University of Texas at Austin
    - 📅 Date: March 4, 2025
    - 📑 Publisher: NAACL 2025 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [memory], [tree search], [LiteWebAgent]
    - 📖 TLDR: LiteWebAgent is an open-source suite designed for VLM-based web agent applications. It offers a modular framework that decouples action generation from grounding, supports agent planning, memory, and tree search, and is deployable via a Vercel-based web app or a Chrome extension using the Chrome DevTools Protocol (CDP).

- [Magma: A Foundation Model for Multimodal AI Agents](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html)
    - Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai, Seonghyeon Ye, Joel Jang, Yuquan Deng, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research, University of Maryland, University of Wisconsin-Madison, KAIST, University of Washington
    - 📅 Date: Feb 18, 2025
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [SoM], [ToM], [robotics], [UI navigation]
    - 📖 TLDR: This paper introduces **Magma**, a foundation model designed for multimodal AI agents operating in both digital and physical environments. Magma extends traditional vision-language models by incorporating planning and action capabilities, enabling tasks from UI navigation to robotic manipulation. The model is pretrained on diverse datasets, including images, videos, and robotics data, utilizing **Set-of-Mark (SoM)** for action grounding and **Trace-of-Mark (ToM)** for action planning. Experiments demonstrate that SoM and ToM synergistically enhance Magma's spatial-temporal intelligence, achieving state-of-the-art performance in UI navigation and robotic manipulation tasks.

- [AEIA-MN: Evaluating the Robustness of Multimodal LLM-Powered Mobile Agents Against Active Environmental Injection Attacks](https://arxiv.org/abs/2502.13053)
    - Yurun Chen, Xueyu Hu, Keting Yin, Juncheng Li, Shengyu Zhang
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: February 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [safety], [AEIA-MN]
    - 📖 TLDR: This paper introduces the concept of Active Environment Injection Attack (AEIA), where attackers disguise malicious actions as environmental elements to disrupt AI agents' decision-making processes. The authors propose AEIA-MN, an attack scheme leveraging mobile notifications to evaluate the robustness of multimodal large language model-based mobile agents. Experimental results demonstrate that even advanced models are highly vulnerable to such attacks, with success rates reaching up to 93% in the AndroidWorld benchmark.

- [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents](https://aclanthology.org/2025.findings-acl.326/)
    - Vardaan Pahuja, Yadong Lu, Corby Rosset, Boyu Gou, Arindam Mitra, Spencer Whitehead, Yu Su, Ahmed Hassan Awadallah
    - 🏛️ Institutions: Microsoft Research, The Ohio State University
    - 📅 Date: February 17, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [web agents], [reinforcement learning], [explorer]
    - 📖 TLDR: This paper introduces *Explorer*, a multimodal web agent trained on a newly synthesized dataset comprising over 94,000 successful web trajectories. The dataset, generated through scalable exploration and refinement techniques, spans 49,000 unique URLs and includes 720,000 screenshots and 33 million web elements. *Explorer* demonstrates strong performance on benchmarks like Mind2Web-Live, Multimodal-Mind2Web, and MiniWob++, highlighting the importance of data scaling in enhancing web agent capabilities.

- [VSC-RL: Advancing Autonomous Vision-Language Agents with Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [subgoal generation], [VSC-RL], [learning efficiency]
    - 📖 TLDR: This paper introduces **VSC-RL**, a novel reinforcement learning framework that enhances learning efficiency for vision-language agents in complex sequential decision-making tasks. By reformulating these tasks as variational goal-conditioned problems, VSC-RL leverages advanced optimization techniques and utilizes vision-language models to autonomously decompose goals into feasible subgoals. Empirical results demonstrate that VSC-RL significantly outperforms state-of-the-art agents, particularly in challenging mobile device control tasks.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Huawei Noah's Ark Lab, University College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [evaluation], [AppVLM], [on-device control]
    - 📖 TLDR: This paper introduces **AppVLM**, a lightweight Vision-Language Model designed for efficient on-device control of smartphone applications. AppVLM is fine-tuned on the AndroidControl dataset and further refined through interactions within the AndroidWorld environment. It achieves superior action prediction accuracy in offline evaluations and matches GPT-4o in online task completion success rates, while operating up to ten times faster, making it a practical solution for real-world deployment.

- [MobileA3gent: Training Mobile GUI Agents Using Decentralized Self-Sourced Data from Diverse Users](https://arxiv.org/abs/2502.02982)
    - Wenhao Wang, Mengying Yuan, Zijie Yu, Guangyi Liu, Rui Ye, Tian Jin, Siheng Chen, Yanfeng Wang
    - 🏛️ Institutions: Zhejiang University, Shanghai Jiao Tong University, Shanghai AI Laboratory, MAGIC Research
    - 📅 Date: February 5, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [auto-annotation], [federated learning], [privacy], [non-IID], [adapted aggregation]
    - 📖 TLDR: This paper introduces *MobileA3gent*, a framework for training mobile GUI agents using decentralized, self-sourced data from diverse users. It addresses challenges in extracting user instructions without human intervention and utilizing distributed data while preserving privacy. The framework comprises two key techniques: *Auto-Annotation*, which automatically collects high-quality datasets during users' routine phone usage, and *FedVLM-A*, which enhances federated training on non-IID user data by incorporating both episode- and step-level distributions. Experiments demonstrate that MobileA3gent achieves performance comparable to centralized human-annotated models at less than 1% of the cost, highlighting its potential for real-world applications.

- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)
    - Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng, Xin Liu, Guang Shi
    - 🏛️ Institutions: ByteDance, Tsinghua University
    - 📅 Date: January 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [UI-TARS]
    - 📖 TLDR: This paper introduces **UI-TARS**, a native GUI agent model that processes screenshots to perform human-like interactions such as keyboard and mouse operations. Unlike traditional frameworks relying on commercial models with handcrafted prompts, UI-TARS is an end-to-end model demonstrating superior performance across over 10 GUI agent benchmarks. Key innovations include enhanced perception through large-scale GUI screenshot datasets, unified action modeling across platforms, incorporation of deliberate multi-step reasoning (System-2 Reasoning), and iterative training with reflective online traces, enabling continuous learning and adaptation with minimal human intervention.

- [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)
    - Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Deyu Zhou, Pengjun Xie, Fei Huang
    - 🏛️ Institutions: Tongyi Lab, Alibaba NLP
    - 📅 Date: January 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [RAG], [WebWalker], [WebWalkerQA]
    - 📖 TLDR: This paper presents **WebWalker**, a multi-agent framework designed to improve the ability of large language models (LLMs) to traverse websites, addressing the challenges of retrieving complex, multi-layered information. WebWalker integrates an "explore-critic" paradigm, where the explorer agent navigates the web, and the critic agent evaluates the progress. The **WebWalkerQA** benchmark is introduced to assess web traversal tasks, showing how retrieval-augmented generation (RAG) can be enhanced with vertical exploration to solve real-world queries.

- [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981)
    - Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, Tat-Seng Chua
    - 🏛️ Institutions: National University of Singapore, East China Normal University, Hong Kong Baptist University
    - 📅 Date: January 3, 2025
    - 📑 Publisher: ACM Multimedia 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [GUI grounding], [high-resolution], [ScreenSpot-pro]
    - 📖 TLDR: ScreenSpot-Pro introduces a benchmark designed to evaluate GUI grounding models in professional, high-resolution environments. It encompasses 1,581 tasks across 23 applications in various industries, highlighting the challenges models face with complex software interfaces. Current models achieve low accuracy, underscoring the need for further research in this domain.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://aclanthology.org/2025.acl-long.277/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Laboratory, The University of Hong Kong, Johns Hopkins University, Shanghai Jiao Tong University, University of Oxford, Hong Kong University of Science and Technology
    - 📅 Date: Dec 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [trajectory data], [reward model], [e2e model], [data synthesis], [OS-genesis]
    - 📖 TLDR: This paper introduces *OS-Genesis*, an interaction-driven pipeline that automates the construction of high-quality and diverse GUI agent trajectory data without human supervision. By employing reverse task synthesis and a trajectory reward model, OS-Genesis enables effective end-to-end training of GUI agents, significantly enhancing their performance on online benchmarks.

- [PC Agent: While You Sleep, AI Works -- A Cognitive Journey into Digital World](https://arxiv.org/abs/2412.17589)
    - Yanheng He, Jiahe Jin, Shijie Xia, Jiadi Su, Runze Fan, Haoyang Zou, Xiangkun Hu, Pengfei Liu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: Dec 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [PC agent], [human cognition transfer], [PC tracker], [cognition completion], [multi-agent system]
    - 📖 TLDR: This paper introduces *PC Agent*, an AI system designed to autonomously perform complex computer-based tasks by emulating human cognitive processes. The system comprises three key components: **PC Tracker**, a lightweight infrastructure for collecting high-quality human-computer interaction data; a **Cognition Completion** pipeline that enriches raw interaction data into detailed cognitive trajectories; and a **multi-agent system** combining a planning agent for decision-making with a grounding agent for precise visual grounding. This approach represents a significant advancement toward AI systems capable of handling intricate real-world work autonomously.

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research, Alibaba Group, Australian National University, Independent
    - 📅 Date: Dec 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [grounding], [visual grounding], [aria-UI]
    - 📖 TLDR: This paper introduces *Aria-UI*, a large multimodal model specifically designed for GUI grounding. Aria-UI employs a pure-vision approach, avoiding reliance on auxiliary inputs like HTML or AXTree. It utilizes a scalable data pipeline to synthesize diverse and high-quality instruction samples and incorporates textual and text-image interleaved action histories for robust context-aware reasoning. Aria-UI achieves state-of-the-art results across offline and online agent benchmarks, outperforming both vision-only and AXTree-reliant baselines.

- [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shenzhi Wang, Xinchen Xu, Shuofei Qiao, Zhaokai Wang, Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao, Hongxia Yang, Fan Wu, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Fudan University, OPPO AI Center, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, The Chinese University of Hong Kong, Tsinghua University, Shanghai Jiao Tong University, 01.AI, The Hong Kong Polytechnic University
    - 📅 Date: December 20, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This paper conducts a comprehensive survey on OS Agents, which are (M)LLM-based agents that use computing devices (e.g., computers and mobile phones) by operating within the environments and interfaces (e.g., Graphical User Interface (GUI)) provided by operating systems (OS) to automate tasks. The survey begins by elucidating the fundamentals of OS Agents, exploring their key components including the environment, observation space, and action space, and outlining essential capabilities such as understanding, planning, and grounding. Methodologies for constructing OS Agents are examined, with a focus on domain-specific foundation models and agent frameworks. A detailed review of evaluation protocols and benchmarks highlights how OS Agents are assessed across diverse tasks. Finally, current challenges and promising future research directions, including safety and privacy, personalization and self-evolution, are discussed. 

- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501)
    - Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen, Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Branislav Kveton, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, Franck Dernoncourt
    - 🏛️ Institutions: University of Maryland, SUNY Buffalo, University of Oregon, Adobe Research, Meta AI, University of Rochester, University of California San Diego, Carnegie Mellon University, Dolby Laboratories, Intel AI Research, University of New South Wales
    - 📅 Date: December 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This survey provides a comprehensive overview of GUI agents powered by Large Foundation Models, detailing their benchmarks, evaluation metrics, architectures, and training methods. It introduces a unified framework outlining their perception, reasoning, planning, and acting capabilities, identifies open challenges, and discusses future research directions, serving as a resource for both practitioners and researchers in the field.

- [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://proceedings.mlr.press/v267/zhou25ah.html)
    - Yifei Zhou, Qianlan Yang, Kaixiang Lin, Min Bai, Xiong Zhou, Yu-Xiong Wang, Sergey Levine, Li Erran Li
    - 🏛️ Institutions: University of California, Berkeley, University of Illinois Urbana-Champaign, Amazon
    - 📅 Date: December 17, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [skill discovery], [PAE]
    - 📖 TLDR: This paper introduces the Proposer-Agent-Evaluator (PAE) system, enabling foundation model agents to autonomously discover and practice skills in real-world web environments. PAE comprises a context-aware task proposer, an agent policy for task execution, and a vision-language model-based success evaluator. Validated on vision-based web navigation tasks, PAE significantly enhances zero-shot generalization capabilities of vision-language model Internet agents, achieving over 30% relative improvement on unseen tasks and websites, and surpassing state-of-the-art open-source agents by more than 10%.

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
    - 📅 Date: Dec 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [falcon-UI], [GUI understanding]
    - 📖 TLDR: This paper introduces *Falcon-UI*, a GUI agent model that emphasizes understanding GUI contexts before following user instructions. The authors present the *Insight-UI Dataset*, an instruction-free GUI navigation dataset generated from the Common Crawl corpus, simulating various platforms like iOS, Android, Windows, and Linux across multiple resolutions on 312K domains. Falcon-UI is pretrained on this dataset and fine-tuned on Android and Web GUI datasets, achieving performance comparable to larger models, highlighting the importance of decoupling GUI understanding from instruction following in agent performance. 

- [The BrowserGym Ecosystem for Web Agent Research](https://openreview.net/forum?id=5298fKGmv3)
    - Thibault Le Sellier De Chezelles, Maxime Gasse, Alexandre Drouin, Massimo Caccia, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Quentin Cappart, Graham Neubig, Ruslan Salakhutdinov, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Carnegie Mellon University, McGill University, Tel Aviv University, Université de Montréal, iMean AI
    - 📅 Date: December 6, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [LLM], [automation], [BrowserGym], [AgentLab]
    - 📖 TLDR: This paper presents *BrowserGym*, an ecosystem designed to standardize the evaluation and benchmarking of web agents, particularly those leveraging Large Language Models (LLMs). It addresses the challenges posed by fragmented benchmarks and inconsistent methodologies in web agent research. BrowserGym provides a unified, gym-like environment with clearly defined observation and action spaces, enabling reproducible comparisons across various benchmarks. Additionally, *AgentLab*, a complementary framework, supports agent creation, testing, and analysis. The paper also features a large-scale experiment comparing the performance of 6 leading LLMs, highlighting the strengths and weaknesses of different models in real-world web tasks, while emphasizing the ongoing challenges in building efficient and robust web agents.

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

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [UI-guided visual token selection], [interleaved vision-language-action streaming], [ShowUI]
    - 📖 TLDR: This paper introduces *ShowUI*, a vision-language-action model designed to enhance GUI automation by addressing challenges in UI visual perception and action modeling. It features innovations like UI-Guided Visual Token Selection to reduce computational costs and Interleaved Vision-Language-Action Streaming for effective management of visual-action history. Trained on a curated dataset, ShowUI achieves 75.1% accuracy in zero-shot screenshot grounding and demonstrates competitive performance across web, mobile, and online environments.

- [AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://aclanthology.org/2025.acl-long.1008/)
    - Gaurav Verma, Rachneet Kaur, Nishan Srishankar, Zhen Zeng, Tucker Balch, Manuela Veloso
    - 🏛️ Institutions: Georgia Institute of Technology, J.P. Morgan AI Research
    - 📅 Date: November 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [few-shot learning], [meta-learning], [AdaptAgent]
    - 📖 TLDR: This paper introduces **AdaptAgent**, a framework that enables multimodal web agents to adapt to new websites and domains using few human demonstrations (up to 2). The approach enhances agents' adaptability beyond large-scale pre-training and fine-tuning by leveraging in-context learning and meta-learning techniques. Experiments on benchmarks like Mind2Web and VisualWebArena show that incorporating minimal human demonstrations boosts task success rates significantly, highlighting the effectiveness of multimodal demonstrations over text-only ones and the impact of data selection strategies during meta-learning on agent generalization.

- [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)
    - Anthony Nguyen
    - 🏛️ Institutions: Algoma University
    - 📅 Date: November 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [grounding], [visual grounding], [iterative narrowing]
    - 📖 TLDR: This paper introduces a visual framework to enhance GUI grounding. By iteratively refining model predictions through progressively focused image crops, the proposed method improves the performance of both general and fine-tuned Vision-Language Models (VLMs) in GUI grounding tasks.

- [Generalist Virtual Agents: A Survey on Autonomous Agents Across Digital Platforms](https://arxiv.org/abs/2411.10943)
    - Minghe Gao, Wendong Bu, Bingchen Miao, Yang Wu, Yunfei Li, Juncheng Li, Siliang Tang, Qi Wu, Yueting Zhuang, Meng Wang
    - 🏛️ Institutions: Zhejiang University, University of Adelaide, Hefei University of Technology
    - 📅 Date: November 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [generalist virtual agent], [GVA], [autonomous agents], [digital platforms]
    - 📖 TLDR: This survey introduces the concept of Generalist Virtual Agents (GVAs), autonomous entities designed to operate across various digital platforms and environments to assist users in performing diverse tasks. It traces the evolution of GVAs from early intelligent assistants to modern implementations incorporating large-scale models, discussing their philosophical foundations, development challenges, and current methodologies. The paper provides a detailed taxonomy of GVA environments, tasks, and capabilities, aiming to bridge theoretical and practical aspects and suggesting that agents operating in environments closely mirroring the real world are more likely to exhibit human-like intelligence.

- [The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](https://arxiv.org/abs/2411.10323)
    - Siyuan Hu, Mingyu Ouyang, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: Nov 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [claude 3.5 computer use], [GUI automation], [planning], [action], [critic]
    - 📖 TLDR: This study evaluates Claude 3.5 Computer Use, an AI model enabling end-to-end language-to-desktop actions, through curated tasks across various domains. It introduces an out-of-the-box framework for deploying API-based GUI automation models, analyzing the model's planning, action execution, and adaptability to dynamic environments.

- [WebOlympus: An Open Platform for Web Agents on Live Websites](https://aclanthology.org/2024.emnlp-demo.20/)
    - Boyuan Zheng, Boyu Gou, Scott Salisbury, Zheng Du, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: November 12, 2024
    - 📑 Publisher: EMNLP 2024 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [chrome extension], [WebOlympus], [SeeAct], [annotation tool]
    - 📖 TLDR: This paper introduces *WebOlympus*, an open platform designed to facilitate the research and deployment of web agents on live websites. It features a user-friendly Chrome extension interface, allowing users without programming expertise to operate web agents with minimal effort. The platform incorporates a safety monitor module to prevent harmful actions through human supervision or model-based control, supporting applications such as annotation interfaces for web agent trajectories and data crawling.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://openreview.net/forum?id=c6l7yA0HSq)
    - Yu Gu, Kai Zhang, Yuting Ning, Boyuan Zheng, Boyu Gou, Tianci Xue, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [WebDreamer], [model-based planning], [world model]
    - 📖 TLDR: This paper investigates whether Large Language Models (LLMs) can function as world models within web environments, enabling model-based planning for web agents. Introducing **WebDreamer**, a framework that leverages LLMs to simulate potential action sequences in web environments, the study demonstrates significant performance improvements over reactive baselines on benchmarks like VisualWebArena and Mind2Web-live. The findings suggest that LLMs possess the capability to model the dynamic nature of the internet, paving the way for advancements in automated web interaction and opening new research avenues in optimizing LLMs for complex, evolving environments.

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890)
    - Shuai Wang, Weiwen Liu, Jingxuan Chen, Weinan Gan, Xingshan Zeng, Shuai Yu, Xinlong Hao, Kun Shao, Yasheng Wang, Ruiming Tang
    - 🏛️ Institutions: Huawei Noah’s Ark Lab
    - 📅 Date: November 7, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This survey consolidates recent research on GUI agents powered by foundation models, particularly Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs). It discusses representative datasets and benchmarks, summarizes a unified framework capturing essential components from prior studies, and explores commercial applications. The paper identifies key challenges and proposes future research directions to inspire further developments in (M)LLM-based GUI agents.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Institute of Technology, The University of Hong Kong, Stanford University
    - 📅 Date: Nov 4, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [attack], [adversarial pop-ups], [VLM agents], [safety]
    - 📖 TLDR: This paper demonstrates that vision-language model (VLM) agents can be easily deceived by carefully designed adversarial pop-ups, leading them to perform unintended actions such as clicking on these pop-ups instead of completing their assigned tasks. Integrating these pop-ups into environments like OSWorld and VisualWebArena resulted in an average attack success rate of 86% and a 47% decrease in task success rate. Basic defense strategies, such as instructing the agent to ignore pop-ups or adding advertisement notices, were found to be ineffective against these attacks.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://openreview.net/forum?id=oVKEAFjEqv)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Jiadai Sun, Xinyue Yang, Yu Yang, Shuntian Yao, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Shanghai Qi Zhi Institute
    - 📅 Date: November 4, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [self-evolving curriculum], [WebRL], [outcome-supervised reward model]
    - 📖 TLDR: This paper introduces *WebRL*, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open large language models (LLMs). WebRL addresses challenges such as the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. It incorporates a self-evolving curriculum that generates new tasks from unsuccessful attempts, a robust outcome-supervised reward model (ORM), and adaptive reinforcement learning strategies to ensure consistent improvements. Applied to Llama-3.1 and GLM-4 models, WebRL significantly enhances their performance on web-based tasks, surpassing existing state-of-the-art web agents.

- [Language Agents: Foundations, Prospects, and Risks](https://aclanthology.org/2024.emnlp-tutorials.3/)
    - Yu Su, Diyi Yang, Shunyu Yao, Tao Yu
    - 🏛️ Institutions: The Ohio State University, Stanford University, Princeton University, The University of Hong Kong
    - 📅 Date: November 2024
    - 📑 Publisher: EMNLP 2024 Tutorial Abstracts
    - 💻 Env: [Misc]
    - 🔑 Key: [survey], [tutorial], [reasoning], [planning], [memory], [multi-agent systems], [safety]
    - 📖 TLDR: This tutorial provides a comprehensive exploration of language agents—autonomous systems powered by large language models capable of executing complex tasks through language instructions. It delves into their theoretical foundations, potential applications, associated risks, and future directions, covering topics such as reasoning, memory, planning, tool augmentation, grounding, multi-agent systems, and safety considerations.

- [From Context to Action: Analysis of the Impact of State Representation and Context on the Generalization of Multi-Turn Web Navigation Agents](https://arxiv.org/abs/2409.13701)
    - Nalin Tiwary, Vardhan Dongre, Sanil Arun Chawla, Ashwin Lamani, Dilek Hakkani-Tür
    - 🏛️ Institutions: University of Illinois Urbana-Champaign
    - 📅 Date: October 31, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [context management], [generalization], [multi-turn navigation], [CWA]
    - 📖 TLDR: This study examines how different contextual elements affect the performance and generalization of Conversational Web Agents (CWAs) in multi-turn web navigation tasks. By optimizing context management—specifically interaction history and web page representation—the research demonstrates enhanced agent performance across various out-of-distribution scenarios, including unseen websites, categories, and geographic locations.

- [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://aclanthology.org/2025.acl-long.107/)
    - Yifan Xu, Xiao Liu, Xueqiao Sun, Siyi Cheng, Hao Yu, Hanyu Lai, Shudan Zhang, Dan Zhang, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Peking University, Zhipu AI
    - 📅 Date: October 31, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [AndroidLab]
    - 📖 TLDR: This paper introduces **AndroidLab**, a comprehensive framework for training and systematically benchmarking Android autonomous agents. It provides an operational environment with diverse modalities and action spaces, supporting both large language models (LLMs) and multimodal models (LMMs). The benchmark includes 138 tasks across nine apps on predefined Android virtual devices. Utilizing AndroidLab, the authors developed an Android Instruction dataset and trained six open-source LLMs and LMMs, significantly improving their average success rates.

- [OS-ATLAS: A Foundation Action Model For Generalist GUI Agents](https://arxiv.org/abs/2410.23218)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong, Massachusetts Institute of Technology
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [OS-atlas]
    - 📖 TLDR: This paper introduces OS-Atlas, a foundational GUI action model designed to enhance GUI grounding and out-of-distribution tasks. The authors developed a toolkit to synthesize multi-platform GUI grounding data, resulting in a cross-platform corpus of over 13 million GUI elements. OS-Atlas demonstrates significant performance improvements across six benchmarks spanning mobile, desktop, and web platforms.

- [Evaluating Cultural and Social Awareness of LLM Web Agents](https://aclanthology.org/2025.findings-naacl.222/)
    - Haoyi Qiu, Alexander Fabbri, Divyansh Agarwal, Kung-Hsiang Huang, Sarah Tan, Nanyun Peng, Chien-Sheng Wu
    - 🏛️ Institutions: University of California, Los Angeles, Salesforce AI Research
    - 📅 Date: October 30, 2024
    - 📑 Publisher: Findings of NAACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [CASA], [cultural awareness], [social awareness], [fine-tuning], [prompting]
    - 📖 TLDR: This paper introduces CASA, a benchmark designed to assess the cultural and social awareness of LLM web agents in tasks like online shopping and social discussion forums. It evaluates agents' abilities to detect and appropriately respond to norm-violating user queries and observations. The study finds that current LLM agents have limited cultural and social awareness, with less than 10% awareness coverage and over 40% violation rates. To enhance performance, the authors explore prompting and fine-tuning methods, demonstrating that combining both can offer complementary advantages.

- [Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/abs/2410.22552)
    - Jaekyeom Kim, Dong-Ki Kim, Lajanugen Logeswaran, Sungryull Sohn, Honglak Lee
    - 🏛️ Institutions: LG AI Research, Field AI, University of Michigan
    - 📅 Date: October 29, 2024
    - 📑 Publisher: EMNLP 2024 (Findings)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [auto-intent]
    - 📖 TLDR: The paper presents Auto-Intent, a method to adapt pre-trained large language models for web navigation tasks without direct fine-tuning. It discovers underlying intents from domain demonstrations and trains an intent predictor to enhance decision-making. Auto-Intent improves the performance of GPT-3.5, GPT-4, and Llama-3.1 agents on benchmarks like Mind2Web and WebArena.

- [AutoGLM: Autonomous Foundation Agents for GUIs](https://arxiv.org/abs/2411.00820)
    - Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long Iong, Jiadai Sun, Jiaqi Wang, Junjie Gao, Junjun Shan, Kangning Liu, Shudan Zhang, Shuntian Yao, Siyi Cheng, Wentao Yao, Wenyi Zhao, Xinghan Liu, Xinyi Liu, Xinying Chen, Xinyue Yang, Yang Yang, Yifan Xu, Yu Yang, Yujia Wang, Yulin Xu, Zehan Qi, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu AI, Tsinghua University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [model], [learning], [AutoGLM]
    - 📖 TLDR: This paper introduces AutoGLM, a new series in the ChatGLM family, designed as foundation agents for autonomous control of digital devices through GUIs. It addresses the challenges foundation models face in decision-making within dynamic environments by developing agents capable of learning through autonomous interactions. Focusing on web browsers and Android devices, AutoGLM integrates various techniques to create deployable agent systems. Key insights include the importance of designing an appropriate "intermediate interface" for GUI control and a novel progressive training framework for self-evolving online curriculum reinforcement learning. Evaluations demonstrate AutoGLM's effectiveness across multiple domains, achieving notable success rates in web browsing and Android device control tasks.

- [EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data](https://arxiv.org/abs/2410.19461)
    - Xuetian Chen, Hangcheng Li, Jiaqing Liang, Sihang Jiang, Deqing Yang
    - 🏛️ Institutions: Fudan University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [framework], [synthetic data]
    - 📖 TLDR: The *EDGE* framework proposes an innovative approach to improve GUI understanding and interaction capabilities in vision-language models through large-scale, multi-granularity synthetic data generation. By leveraging webpage data, EDGE minimizes the need for manual annotations and enhances the adaptability of models across desktop and mobile GUI environments. Evaluations show its effectiveness in diverse GUI-related tasks, contributing significantly to autonomous agent development in GUI navigation and interaction.

- [OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization](https://aclanthology.org/2025.acl-long.1336/)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Hongming Zhang, Tianqing Fang, Zhenzhong Lan, Dong Yu
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab, Westlake University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [learning], [imitation learning], [exploration], [AI feedback]
    - 📖 TLDR: The paper presents **OpenWebVoyager**, an open-source framework for training web agents that explore real-world online environments autonomously. The framework employs a cycle of exploration, feedback, and optimization, enhancing agent capabilities through multimodal perception and iterative learning. Initial skills are acquired through imitation learning, followed by real-world exploration, where the agent’s performance is evaluated and refined through feedback loops.

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Shanghai AI Laboratory, The University of Hong Kong
    - 📅 Date: October 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [multi-agent systems], [specialized generalist agent], [OSWorld benchmark]
    - 📖 TLDR: AgentStore introduces a scalable platform to integrate and manage heterogeneous agents, designed to enhance generalist assistant capabilities for diverse computer tasks. Using a MetaAgent and AgentToken strategy, AgentStore shows improved generalization on the OSWorld benchmark.

- [Beyond Browsing: API-Based Web Agents](https://aclanthology.org/2025.findings-acl.577/)
    - Yueqi Song, Frank Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [benchmark], [WebArena], [SOTA performance]
    - 📖 TLDR: This paper introduces API-based and hybrid agents designed to execute online tasks by accessing both APIs and traditional web browsing interfaces. In evaluations using WebArena, a benchmark for web navigation, the API-based agent achieves higher performance than browser-based agents, and the hybrid model achieves a success rate of 35.8%, setting a new state-of-the-art (SOTA) in task-agnostic web navigation. The findings highlight the efficiency and reliability gains of API interactions for web agents.

- [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5b555804d495321df2e3208cc27f4fbc-Abstract-Conference.html)
    - Lawrence Jang, Yinheng Li, Charles Ding, Justin Lin, Paul Pu Liang, Dan Zhao, Rogerio Bonatti, Kazuhito Koishida
    - 🏛️ Institutions: Carnegie Mellon University, Massachusetts Institute of Technology, New York University, Microsoft
    - 📅 Date: October 24, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [video understanding], [long-context], [VideoWA]
    - 📖 TLDR: This paper introduces **VideoWebArena (VideoWA)**, a benchmark assessing multimodal agents in video-based tasks. It features over 2,000 tasks focused on skill and factual retention, using video tutorials to simulate long-context environments. Results highlight current challenges in agentic abilities, providing a critical testbed for long-context video understanding improvements.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, The University of Texas at Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [evaluation], [Android emulator]
    - 📖 TLDR: *MobileSafetyBench* introduces a benchmark for evaluating the safety of large language model (LLM)-based autonomous agents in mobile device control. Using Android emulators, the benchmark simulates real-world tasks in apps such as messaging and banking to assess agents' safety and helpfulness. The safety-focused tasks test for privacy risk management and robustness against adversarial prompt injections. Experiments show agents perform well in helpful tasks but struggle with safety-related challenges, underscoring the need for continued advancements in mobile safety mechanisms for autonomous agents.

- [Lightweight Neural App Control](https://openreview.net/forum?id=BL4WBIfyrz)
    - Filippos Christianos, Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 23, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [vision language model], [action transformer], [app agent], [Android control], [multi-modal]
    - 📖 TLDR: This paper introduces LiMAC, a mobile control framework for Android that integrates an Action Transformer and fine-tuned vision-language models to execute precise actions in mobile apps. Tested on open-source datasets, LiMAC improves action accuracy by up to 42% over traditional prompt engineering baselines, demonstrating enhanced efficiency and accuracy in mobile app control tasks.

- [Large Language Models Empowered Personalized Web Agents](https://openreview.net/forum?id=kAzqfqsCC5)
    - Hongru Cai, Yongqi Li, Wenjie Wang, Fengbin Zhu, Xiaoyu Shen, Wenjie Li, Tat-Seng Chua
    - 🏛️ Institutions: The Hong Kong Polytechnic University, Nanyang Technological University
    - 📅 Date: Oct 22, 2024
    - 📑 Publisher: WWW 2025 (Oral)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [personalized web agent], [user behavior alignment], [memory-enhanced alignment]
    - 📖 TLDR: This paper proposes a novel framework, *Personalized User Memory-enhanced Alignment (PUMA)*, enabling large language models to serve as personalized web agents by incorporating user-specific data and historical web interactions. The authors also introduce a benchmark, *PersonalWAB*, to evaluate these agents on various personalized web tasks. Results show that PUMA improves web agent performance by optimizing action execution based on user-specific preferences.

- [AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://aclanthology.org/2024.emnlp-main.505/)
    - Ori Yoran, Samuel Joseph Amouyal, Chaitanya Malaviya, Ben Bogin, Ofir Press, Jonathan Berant
    - 🏛️ Institutions: Tel Aviv University, University of Pennsylvania, Allen Institute for AI, University of Washington, Princeton University
    - 📅 Date: October 21, 2024
    - 📑 Publisher: EMNLP 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [planning and reasoning]
    - 📖 TLDR: AssistantBench is a benchmark designed to test the abilities of web agents in completing time-intensive, realistic web-based tasks. Covering 214 tasks across various domains, the benchmark introduces the SPA (See-Plan-Act) framework to handle multi-step planning and memory retention. AssistantBench emphasizes realistic task completion, showing that current agents achieve only modest success, with significant improvements needed for complex information synthesis and execution across multiple web domains.

- [Dissecting Adversarial Robustness of Multimodal LM Agents](https://openreview.net/forum?id=LjVIGva5Ct)
    - Chen Henry Wu, Rishi Rajesh Shah, Jing Yu Koh, Russ Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: Carnegie Mellon University, Stanford University
    - 📅 Date: October 21, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [attack], [ARE], [safety]
    - 📖 TLDR: This paper introduces the Agent Robustness Evaluation (ARE) framework to assess the adversarial robustness of multimodal language model agents in web environments. By creating 200 targeted adversarial tasks within VisualWebArena, the study reveals that minimal perturbations can significantly compromise agent performance, even in advanced systems utilizing reflection and tree-search mechanisms. The findings highlight the need for enhanced safety measures in deploying such agents.

- [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9a75f4dd9679aa4ff80a4e6f0a1dc700-Abstract-Conference.html)
    - Jingxuan Chen, Derek Yuen, Bin Xie, Yuhao Yang, Gongwei Chen, Zhihao Wu, Li Yixing, Xurui Zhou, Weiwen Liu, Shuai Wang, Rui Shao, Liqiang Nie, Yasheng Wang, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, Harbin Institute of Technology, Shenzhen, University College London
    - 📅 Date: October 19, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [AI agent], [smartphone control], [framework]
    - 📖 TLDR: SPA-Bench is introduced as a benchmark designed to evaluate multimodal large language model (MLLM)-based smartphone agents, offering a task set that spans common smartphone functionalities across system and third-party applications. It includes a plug-and-play framework for real-time agent interactions on Android, integrating over ten agents with an adaptable evaluation pipeline measuring success across diverse metrics. Through this, the benchmark exposes challenges such as UI interpretation, action grounding, and memory retention in mobile environments, advancing research in smartphone-based agent applications.

- [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b9e472cd579c83e2f6aa3459f46aac28-Abstract-Conference.html)
    - Taiyi Wang, Zhihao Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 18, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [distributed training], [a-RIDE], [on-device control]
    - 📖 TLDR: This paper introduces **DistRL**, a novel framework designed to enhance the efficiency of online reinforcement learning fine-tuning for mobile device control agents. DistRL employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in dynamic online interactions. The framework is supported by a custom RL algorithm, A-RIDE, which balances exploration with prioritized data utilization to ensure stable and robust training. Experiments demonstrate that DistRL improves training efficiency by 3× and accelerates data collection by 2.4× compared to leading synchronous multi-machine methods. Notably, after training, DistRL achieves a 20% relative improvement in success rate on general Android tasks from an open benchmark, outperforming existing approaches while maintaining the same training time.

- [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2da53cd1abdae59150e35f4693834f32-Abstract-Conference.html)
    - Junpeng Liu, Tianyue Ou, Yifan Song, Yuxiao Qu, Wai Lam, Chenyan Xiong, Wenhu Chen, Graham Neubig, Xiang Yue
    - 🏛️ Institutions: Carnegie Mellon University, The Chinese University of Hong Kong, Peking University, University of Waterloo
    - 📅 Date: October 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [multimodal instruction tuning], [text-rich visual understanding], [web UI], [MultiUI]
    - 📖 TLDR: This paper introduces *MultiUI*, a large-scale dataset containing 7.3 million annotated samples from 1 million websites, specifically designed to enhance multimodal large language models’ (MLLMs) capabilities in text-rich visual understanding. Utilizing webpage UI structures as a training resource, MultiUI provides robust accessibility tree data paired with UI screenshots, significantly improving MLLMs’ grounding, OCR, and interaction performance. Models trained with MultiUI achieve up to a 48% performance boost on VisualWebBench and demonstrate enhanced generalization across non-web tasks, setting a new standard for structured, visually integrated web data modeling.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://dl.acm.org/doi/10.1145/3637528.3671620)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences
    - 📅 Date: April 4, 2024
    - 📑 Publisher: KDD 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [web navigation], [AutoWebBench], [ChatGLM3-6B]
    - 📖 TLDR: AutoWebGLM introduces a web navigation agent based on ChatGLM3-6B, designed to autonomously navigate and interact with webpages for complex tasks. The paper highlights a two-phase data construction approach using a hybrid human-AI methodology for diverse, curriculum-based web task training. It also presents AutoWebBench, a benchmark for evaluating agent performance in web tasks, and uses reinforcement learning to fine-tune operations, addressing complex webpage interaction and grounding.

- [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886)
    - Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar, Tu Trinh, Scale Red Team, Elaine T. Chang, Vaughn Robinson, Sean Hendryx, Shuyan Zhou, Matt Fredrikson, Summer Yue, Zifan Wang
    - 🏛️ Institutions: Carnegie Mellon University, GraySwan AI, Scale AI
    - 📅 Date: October 11, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [safety], [red teaming], [jailbreaking], [BrowserART]
    - 📖 TLDR: This paper introduces **Browser Agent Red teaming Toolkit (BrowserART)**, a comprehensive test suite for evaluating the safety of LLM-based browser agents. The study reveals that while refusal-trained LLMs decline harmful instructions in chat settings, their corresponding browser agents often comply with such instructions, indicating a significant safety gap. The authors call for collaboration among developers and policymakers to enhance agent safety.

- [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab87cdfe514bf8f9c07e5e7aa247f55f-Abstract-Conference.html)
    - Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular, Carnegie Mellon University
    - 📅 Date: October 10, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI agent], [hierarchical planning], [retrieval-augmented planning], [agent-computer interface], [agent s]
    - 📖 TLDR: This paper introduces Agent S, an open agentic framework that enables autonomous interaction with computers through a Graphical User Interface (GUI). The system addresses key challenges in automating computer tasks through experience-augmented hierarchical planning and an Agent-Computer Interface (ACI). Agent S demonstrates significant improvements over baselines on the OSWorld benchmark, achieving a 20.58% success rate (83.6% relative improvement). The framework shows generalizability across different operating systems and provides insights for developing more effective GUI agents.

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

- [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://openreview.net/forum?id=MuCDzH0ctf)
    - Ido Levy, Ben Wiesel, Sami Marreed, Alon Oved, Avi Yaeli, Segev Shlomov
    - 🏛️ Institutions: IBM Research
    - 📅 Date: October 9, 2024
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [safety], [trustworthiness], [policy compliance], [completion under policy], [ST-WebAgentBench]
    - 📖 TLDR: This paper introduces **ST-WebAgentBench**, a benchmark designed to evaluate the safety and trustworthiness of web agents in enterprise contexts. It defines safe and trustworthy agent behavior, outlines the structure of safety policies, and introduces the "Completion under Policies" metric to assess agent performance. The study reveals that current state-of-the-art agents struggle with policy adherence, highlighting the need for improved policy awareness and compliance in web agents.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0faa4bc5f522076947a030273629d4fe-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: October 7, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [visual grounding], [GUI agent], [cross-platform generalization], [UGround], [SeeAct-v], [synthetic data]
    - 📖 TLDR: This paper introduces UGround, a universal visual grounding model for GUI agents that enables human-like navigation of digital interfaces. The authors advocate for GUI agents with human-like embodiment that perceive the environment entirely visually and take pixel-level actions. UGround is trained on a large-scale synthetic dataset of 10M GUI elements across 1.3M screenshots. Evaluated on six benchmarks spanning grounding, offline, and online agent tasks, UGround significantly outperforms existing visual grounding models by up to 20% absolute. Agents using UGround achieve comparable or better performance than state-of-the-art agents that rely on additional textual input, demonstrating the feasibility of vision-only GUI agents.

- [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html)
    - Xiao Yu, Baolin Peng, Vineeth Vajipey, Hao Cheng, Michel Galley, Jianfeng Gao, Zhou Yu
    - 🏛️ Institutions: Columbia University, Microsoft Research
    - 📅 Date: October 2, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [tree search], [self-improvement], [r-MCTS], [exploratory learning], [VisualWebArena]
    - 📖 TLDR: This paper introduces ExACT, an approach that combines Reflective Monte Carlo Tree Search (R-MCTS) and Exploratory Learning to enhance AI agents' exploration and decision-making capabilities in complex web environments. R-MCTS incorporates contrastive reflection and multi-agent debate for improved search efficiency and reliable state evaluation. Evaluated on the VisualWebArena benchmark, the GPT-4o-based R-MCTS agent demonstrates significant performance improvements over previous state-of-the-art methods. Additionally, knowledge gained from test-time search is effectively transferred back to GPT-4o through fine-tuning, enabling the model to explore, evaluate, and backtrack without external search algorithms, achieving 87% of R-MCTS's performance with reduced computational resources.

- [Dynamic Planning for LLM-based Graphical User Interface Automation](https://aclanthology.org/2024.findings-emnlp.70/)
    - Shaoqing Zhang, Zhuosheng Zhang, Kehai Chen, Xinbei Ma, Muyun Yang, Tiejun Zhao, Min Zhang
    - 🏛️ Institutions: Harbin Institute of Technology, Shanghai Jiao Tong University
    - 📅 Date: October 1, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dynamic planning], [d-PoT], [mobile agent]
    - 📖 TLDR: This paper introduces a novel method called Dynamic Planning of Thoughts (D-PoT) aimed at enhancing LLM-based agents for GUI tasks. It addresses the challenges of task execution by dynamically adjusting planning based on environmental feedback and action history, outperforming existing methods such as ReAct by improving accuracy significantly in navigating GUI environments. The study emphasizes the importance of integrating execution history and contextual cues to optimize decision-making processes for autonomous agents.

- [MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a2c3c86679300047c740c9900f19ddac-Abstract-Conference.html)
    - Haotian Zhang, Mingfei Gao, Zhe Gan, Philipp Dufter, Nina Wenzel, Forrest Huang, Dhruti Shah, Xianzhi Du, Bowen Zhang, Yanghao Li, Sam Dodge, Keen You, Zhen Yang, Aleksei Timofeev, Mingze Xu, Hong-You Chen, Jean-Philippe Fauconnier, Zhengfeng Lai, Haoxuan You, Zirui Wang, Afshin Dehghan, Peter Grasch, Yinfei Yang
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Misc]
    - 🔑 Key: [model], [MM1.5], [vision language model], [visual grounding], [reasoning], [data-centric], [analysis]
    - 📖 TLDR: This paper introduces MM1.5, a family of multimodal large language models (MLLMs) ranging from 1B to 30B parameters, including dense and mixture-of-experts variants. MM1.5 enhances capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning. The authors employ a data-centric training approach, utilizing high-quality OCR data and synthetic captions for continual pre-training, alongside an optimized visual instruction-tuning data mixture for supervised fine-tuning. Specialized variants, MM1.5-Video and MM1.5-UI, are designed for video understanding and mobile UI comprehension, respectively. Extensive empirical studies provide insights into the training processes, offering guidance for future MLLM development.

- [Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a6a6891cf1dfc64d664f086cf5976e93-Abstract-Conference.html)
    - Tianyue Ou, Frank F. Xu, Aman Madaan, Jiarui Liu, Robert Lo, Abishek Sridhar, Sudipta Sengupta, Dan Roth, Graham Neubig, Shuyan Zhou
    - 🏛️ Institutions: Carnegie Mellon University, Amazon Web Services AI
    - 📅 Date: September 24, 2024
    - 📑 Publisher: NeurIPS 2024 (Main Conference Track)
    - 💻 Env: [Web]
    - 🔑 Key: [synthetic data], [synthetic demonstrations], [web navigation], [synatra]
    - 📖 TLDR: Synatra introduces a scalable framework for digital agents, enabling them to convert indirect knowledge sources into actionable demonstrations. This approach enhances the ability of agents to learn tasks without extensive labeled data, leveraging insights from indirect observations to scale practical implementations in digital environments.

- [AdvWeb: Controllable Black-box Attacks on VLM-powered Web Agents](https://arxiv.org/abs/2410.17401)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, University of Chicago, The Ohio State University, University of Science and Technology of China
    - 📅 Date: October 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [attack], [black-box attack], [adversarial prompt injection], [direct policy optimization], [AdvWeb]
    - 📖 TLDR: This paper presents AdvWeb, a black-box attack framework that exploits vulnerabilities in vision-language model (VLM)-powered web agents by injecting adversarial prompts directly into web pages. Using Direct Policy Optimization (DPO), AdvWeb trains an adversarial prompter model that can mislead agents into executing harmful actions, such as unauthorized financial transactions, while maintaining high stealth and control. Extensive evaluations reveal that AdvWeb achieves high success rates across multiple real-world tasks, emphasizing the need for stronger security measures in web agent deployments.

- [AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://aclanthology.org/2025.acl-long.381/)
    - Junting Lu, Zhiyang Zhang, Fangkai Yang, Jue Zhang, Lu Wang, Chao Du, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Peking University, Nanjing University, Microsoft
    - 📅 Date: September 26, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [API-first], [AXIS], [HACI], [agent OS]
    - 📖 TLDR: This paper proposes an API-centered framework called **AXIS**, enhancing the efficiency and reliability of LLM-based agents by prioritizing API interactions over UI-based actions. This approach aims to reduce the high latency and error rates of traditional UI-interaction models. AXIS not only supports the rapid creation and extension of APIs through automated application exploration but also contributes to a new **Human-Agent-Computer Interaction (HACI)** framework. The paper outlines the development of an agent-centric operating system (Agent OS), which improves task completion times by up to 70% and reduces cognitive load on users while maintaining high accuracy across complex multi-application tasks.

- [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://aclanthology.org/2024.findings-emnlp.599/)
    - Qinzhuo Wu, Weikai Xu, Wei Liu, Tao Tan, Jianfeng Liu, Ang Li, Jian Luan, Bin Wang, Shuo Shang
    - 🏛️ Institutions: Xiaomi AI Lab, University of Electronic Science and Technology of China, Renmin University of China
    - 📅 Date: September 23, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [MobileVLM], [Mobile3M], [UI understanding]
    - 📖 TLDR: This paper introduces *MobileVLM*, a vision-language model designed to enhance both intra- and inter-UI understanding for mobile applications. The authors propose two additional pre-training stages with four specific UI-based tasks to improve the model's perception of fine-grained elements and capture page transition actions. To support this, they constructed *Mobile3M*, a large-scale Chinese mobile dataset comprising 3 million UI pages and real-world transition actions, organized into directed graphs. Experimental results demonstrate that MobileVLM outperforms existing vision-language models on both in-house test sets and public mobile benchmarks.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Los Angeles, The University of Chicago, University of Illinois Urbana-Champaign, University of Wisconsin-Madison
    - 📅 Date: September 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [web agent], [EIA]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://proceedings.mlr.press/v267/bonatti25a.html)
    - Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, Yadong Lu, Justin Wagle, Kazuhito Koishida, Arthur Bucker, Lawrence Keunho Jang, Zheng Hui
    - 🏛️ Institutions: Microsoft
    - 📅 Date: September 13, 2024
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [desktop agent], [Windows OS], [navi], [Windows agent arena]
    - 📖 TLDR: This paper introduces the *Windows Agent Arena (WAA)*, a scalable platform for testing and benchmarking multi-modal AI agents within a realistic Windows OS environment. WAA enables researchers to evaluate agentic workflows across diverse tasks and supports large-scale deployment using Azure ML. The study also presents *Navi*, a multi-modal agent achieving a 19.5% success rate on Windows tasks, highlighting the platform's potential for advancing AI agent development.

- [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
    - Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University, Massachusetts Institute of Technology
    - 📅 Date: September 11, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [memory], [workflow induction], [web navigation], [AWM]
    - 📖 TLDR: The paper proposes *Agent Workflow Memory (AWM)*, a method enabling language model-based agents to induce and utilize reusable workflows from past experiences to guide future actions in web navigation tasks. AWM operates in both offline and online settings, significantly improving performance on benchmarks like Mind2Web and WebArena, and demonstrating robust generalization across tasks, websites, and domains.

- [From Grounding to Planning: Benchmarking Bottlenecks in Web Agents](https://ebooks.iospress.nl/doi/10.3233/FAIA250590)
    - Segev Shlomov, Ben Wiesel, Aviad Sela, Ido Levy, Liane Galanti, Roy Abitbol
    - 🏛️ Institutions: IBM Research - Haifa, University of Haifa
    - 📅 Date: September 3, 2024
    - 📑 Publisher: ECAI 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [grounding], [Mind2Web], [AssistantBench], [web navigation]
    - 📖 TLDR: This paper analyzes performance bottlenecks in web agents by separately evaluating grounding and planning tasks, isolating their individual impacts on navigation efficacy. Using an enhanced version of the Mind2Web dataset, the study reveals planning as a significant bottleneck, with advancements in grounding and task-specific benchmarking for elements like UI component recognition. Through experimental adjustments, the authors propose a refined evaluation framework, aiming to enhance web agents' contextual adaptability and accuracy in complex web environments.

- [TinyAgent: Function Calling at the Edge](https://aclanthology.org/2024.emnlp-demo.9/)
    - Lutfi Eren Erdogan, Nicholas Lee, Siddharth Jha, Sehoon Kim, Ryan Tabrizi, Suhong Moon, Coleman Richard Charles Hooper, Gopala Anumanchipalli, Kurt Keutzer, Amir Gholami
    - 🏛️ Institutions: UC Berkeley, ICSI
    - 📅 Date: September 1, 2024
    - 📑 Publisher: EMNLP 2024 System Demonstrations
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [function calling], [quantization], [LLMCompiler], [TinyAgent-1.1B], [TinyAgent-7B]
    - 📖 TLDR: This paper introduces TinyAgent, an end-to-end framework for training and deploying task-specific small language model agents capable of function calling at the edge. By fine-tuning small models with curated datasets and employing techniques like quantization and a novel tool retrieval method, TinyAgent enables efficient, real-time execution of user commands on local devices without relying on cloud infrastructure. The framework demonstrates that these small models can match or even surpass the function-calling capabilities of larger models like GPT-4-Turbo while operating entirely on edge devices.

- [WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration](https://doi.org/10.1609/aaai.v39i22.34505)
    - Yao Zhang, Zijian Ma, Yunpu Ma, Zhen Han, Yu Wu, Volker Tresp
    - 🏛️ Institutions: LMU Munich, Technical University of Munich, Munich Center for Machine Learning (MCML)
    - 📅 Date: August 28, 2024
    - 📑 Publisher: AAAI 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [monte carlo tree search], [reinforcement learning], [WebPilot]
    - 📖 TLDR: This paper introduces **WebPilot**, a multi-agent system designed to execute complex web tasks requiring dynamic interaction. By employing a dual optimization strategy grounded in Monte Carlo Tree Search (MCTS), WebPilot enhances adaptability in complex web environments. The system's Global Optimization phase generates high-level plans by decomposing tasks into manageable subtasks, while the Local Optimization phase executes each subtask using a tailored MCTS approach. Experimental results on WebArena and MiniWoB++ demonstrate WebPilot's effectiveness, achieving state-of-the-art performance with GPT-4 and marking a significant advancement in autonomous web agent capabilities.

- [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199)
    - Pranav Putta, Edmund Mills, Naman Garg, Sumeet Ramesh Motwani, Elan Sopher Markowitz, Julia Kiseleva, Chelsea Finn, Divyansh Garg, Rafael Rafailov
    - 🏛️ Institutions: MultiOn, Stanford University
    - 📅 Date: August 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [MCTS], [tree search], [DPO], [reinforcement learning], [web navigation], [agent q]
    - 📖 TLDR: TBD

- [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/eea71dc576381b88f2a0ca4dedc2140d-Abstract-Conference.html)
    - Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Song XiXuan, Yifan Xu, Shudan Zhang, Hanyu Lai, Jiadai Sun, Xinyue Yang, Yu Yang, Zehan Qi, Shuntian Yao, Xueqiao Sun, Siyi Cheng, Qinkai Zheng, Hao Yu, Hanchen Zhang, Wenyi Hong, Ming Ding, Lihang Pan, Xiaotao Gu, Aohan Zeng, Zhengxiao Du, Chan Hee Song, Yu Su, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Microsoft Research Asia, The Ohio State University
    - 📅 Date: August 12, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [GUI], [embodied], [visual design], [VisualAgentBench], [VAB]
    - 📖 TLDR: The authors introduce *VisualAgentBench (VAB)*, a comprehensive benchmark designed to train and evaluate large multimodal models (LMMs) as visual foundation agents across diverse scenarios, including embodied tasks, graphical user interfaces, and visual design. VAB comprises five distinct environments that systematically challenge LMMs' understanding and interaction capabilities. Additionally, the benchmark offers supervised fine-tuning trajectory data for behavior cloning training, demonstrating the potential to improve open LMMs for serving as visual foundation agents.

- [AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/abs/2408.11824)
    - Yanda Li, Chi Zhang, Wenjia Jiang, Wanqi Yang, Bin Fu, Pei Cheng, Xin Chen, Ling Chen, Yunchao Wei
    - 🏛️ Institutions: University of Technology Sydney, Tencent, Beijing Jiaotong University, Westlake University
    - 📅 Date: August 5, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [mobile agent], [knowledge base], [RAG], [AppAgent v2]
    - 📖 TLDR: This work presents *AppAgent v2*, a novel LLM-based multimodal agent framework for mobile devices capable of navigating applications by emulating human-like interactions such as tapping and swiping. The agent constructs a flexible action space that enhances adaptability across various applications, including parsing text and vision descriptions. It operates through two main phases: exploration and deployment, utilizing retrieval-augmented generation (RAG) technology to efficiently retrieve and update information from a knowledge base, thereby empowering the agent to perform tasks effectively and accurately.

- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203)
    - Yadong Lu, Jianwei Yang, Yelong Shen, Ahmed Awadallah
    - 🏛️ Institutions: Microsoft Research, Microsoft GenAI
    - 📅 Date: August 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [OmniParser]
    - 📖 TLDR: This paper introduces **OmniParser**, a method for parsing user interface screenshots into structured elements, enhancing the ability of models like GPT-4V to generate actions accurately grounded in corresponding UI regions. The authors curated datasets for interactable icon detection and icon description, fine-tuning models to parse interactable regions and extract functional semantics of UI elements.

- [Caution for the Environment: Multimodal LLM Agents are Susceptible to Environmental Distractions](https://aclanthology.org/2025.acl-long.1087/)
    - Xinbei Ma, Yiting Wang, Yao Yao, Tongxin Yuan, Aston Zhang, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University, Meta
    - 📅 Date: August 5, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [robustness], [environmental distraction], [multimodal LLM agent]
    - 📖 TLDR: This paper highlights the vulnerability of multimodal agents to environmental distractions. The researchers demonstrate that these agents, which process multiple types of input (e.g., text, images, audio), can be significantly impacted by irrelevant or misleading environmental cues. The study provides insights into the limitations of current multimodal systems and emphasizes the need for more robust architectures that can filter out distractions and maintain focus on relevant information in complex, real-world environments.

- [CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://aclanthology.org/2024.findings-acl.539)
    - Xinbei Ma, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: August 2024
    - 📑 Publisher: Findings of ACL 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [smartphone automation], [comprehensive environment perception], [conditional action prediction], [CoCo-agent]
    - 📖 TLDR: This paper presents CoCo-Agent, a multimodal large language model (MLLM) designed for smartphone GUI automation. It introduces two novel approaches: Comprehensive Environment Perception (CEP) for enhanced GUI understanding, and Conditional Action Prediction (CAP) to improve action response accuracy. The proposed agent achieves state-of-the-art performance on GUI automation benchmarks such as AITW and META-GUI, showcasing its capabilities in realistic scenarios.

- [OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation](https://arxiv.org/abs/2407.19056)
    - Zilong Wang, Yuedong Cui, Li Zhong, Zimin Zhang, Da Yin, Bill Yuchen Lin, Jingbo Shang
    - 🏛️ Institutions: University of California San Diego, University of California Los Angeles, Allen Institute for AI
    - 📅 Date: July 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multi-application], [office automation]
    - 📖 TLDR: OfficeBench introduces a benchmark that evaluates language models' ability to automate office tasks across a range of applications like Word, Excel, and email. The benchmark tests agents’ skills in task-switching, planning, and decision-making by simulating realistic office workflows. Current models, including GPT-4, demonstrate significant gaps in task accuracy and efficiency, revealing areas for improvement in managing complex, multi-application tasks in office environments.

- [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032)
    - Tamer Abuelsaad, Deepak Akkil, Prasenjit Dey, Ashish Jagmohan, Aditya Vempaty, Ravi Kokku
    - 🏛️ Institutions: Emergence AI
    - 📅 Date: July 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [hierarchical architecture], [DOM distillation], [change observation], [self-improvement], [agent-e]
    - 📖 TLDR: This paper presents Agent-E, a novel web agent that introduces several architectural improvements over previous state-of-the-art systems. Key features include a hierarchical architecture, flexible DOM distillation and denoising methods, and a "change observation" concept for improved performance. Agent-E outperforms existing text and multi-modal web agents by 10-30% on the WebVoyager benchmark. The authors synthesize their findings into general design principles for developing agentic systems, including the use of domain-specific primitive skills, hierarchical architectures, and agentic self-improvement.

- [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c2f71567cd53464161cab3336e8fc865-Abstract-Datasets_and_Benchmarks_Track.html)
    - Ruisheng Cao, Fangyu Lei, Haoyuan Wu, Jixuan Chen, Yeqiao Fu, Hongcheng Gao, Xinzhuang Xiong, Hanchong Zhang, Yuchen Mao, Wenjing Hu, Tianbao Xie, Hongsheng Xu, Danyang Zhang, Sida Wang, Ruoxi Sun, Pengcheng Yin, Caiming Xiong, Ansong Ni, Qian Liu, Victor Zhong, Lu Chen, Kai Yu, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Shanghai Jiao Tong University, Google Cloud AI Research, Google DeepMind, Salesforce Research, Yale University, Sea AI Lab, University of Waterloo
    - 📅 Date: July 15, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [data science], [engineering workflows], [Spider2-v]
    - 📖 TLDR: This paper introduces **Spider2-V**, a multimodal agent benchmark designed to evaluate the capability of agents in automating professional data science and engineering workflows. It comprises 494 real-world tasks across 20 enterprise-level applications, assessing agents' proficiency in code generation and GUI operations within authentic computer environments.

- [AUITestAgent: Automatic Requirements Oriented GUI Function Testing](https://arxiv.org/abs/2407.09018)
    - Yongxiang Hu, Xuan Wang, Yingchuan Wang, Yu Zhang, Shiyu Guo, Chaoyi Chen, Xin Wang, Yangfan Zhou
    - 🏛️ Institutions: Fudan University, Meituan
    - 📅 Date: July 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI testing], [AUITestAgent]
    - 📖 TLDR: This paper presents **AUITestAgent**, the first automatic, natural language-driven GUI testing tool for mobile apps. It automates the entire process of GUI interaction and function verification by extracting GUI interactions from test requirements via dynamically organized agents and employing a multi-dimensional data extraction strategy for verification.

- [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0b82662b6c32e887bb252a74d8cb2d5e-Abstract-Datasets_and_Benchmarks_Track.html)
    - Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, Alexandre Drouin
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Chandar Research Lab
    - 📅 Date: July 7, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [reasoning], [WorkArena++]
    - 📖 TLDR: This paper introduces **WorkArena++**, a benchmark comprising 682 tasks that simulate realistic workflows performed by knowledge workers. It evaluates web agents' capabilities in planning, problem-solving, logical/arithmetic reasoning, retrieval, and contextual understanding. The study reveals challenges faced by current large language models and vision-language models in serving as effective workplace assistants, providing a resource to advance autonomous agent development.

- [MobileFlow: A Multimodal LLM For Mobile GUI Agent](https://arxiv.org/abs/2407.04346)
    - Songqin Nong, Jiali Zhu, Rui Wu, Jiongchao Jin, Shuo Shan, Xiutian Huang, Wenhao Xu
    - 🏛️ Institutions: Ant Group
    - 📅 Date: July 5, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [mobile agent], [hybrid visual encoder], [multilingual GUI], [MobileFlow]
    - 📖 TLDR: This paper introduces *MobileFlow*, a multimodal large language model tailored for mobile GUI agents. With approximately 21 billion parameters and hybrid visual encoders, it supports variable image resolutions and multilingual GUIs, enhancing the model's ability to interpret image data and comprehend user instructions for GUI interaction tasks.

- [MobileExperts: A Dynamic Tool-Enabled Agent Team in Mobile Devices](https://arxiv.org/abs/2407.03913)
    - Jiayi Zhang, Chuang Zhao, Yihan Zhao, Zhaoyang Yu, Ming He, Jianping Fan
    - 🏛️ Institutions: AI Lab at Lenovo Research, Renmin University of China, The Hong Kong University of Science and Technology
    - 📅 Date: July 4, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [tool formulation], [multi-agent], [double-layer planning], [expert-eval], [MobileExperts]
    - 📖 TLDR: This paper introduces *MobileExperts*, a framework that enhances autonomous operations on mobile devices by dynamically assembling agent teams based on user requirements. Each agent independently explores and formulates tools to evolve into an expert, improving efficiency and reducing reasoning costs.

- [AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents](https://aclanthology.org/2025.findings-acl.110/)
    - Yuxiang Chai, Siyuan Huang, Yazhe Niu, Han Xiao, Liang Liu, Guozhi Wang, Dingyu Zhang, Shuai Ren, Hongsheng Li
    - 🏛️ Institutions: The Chinese University of Hong Kong, Shanghai Jiao Tong University, Shanghai AI Laboratory, vivo AI Lab
    - 📅 Date: July 3, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [AMEX]
    - 📖 TLDR: This paper introduces the **Android Multi-annotation EXpo (AMEX)**, a comprehensive dataset designed for training and evaluating mobile GUI-control agents. AMEX comprises over 104K high-resolution screenshots from 110 popular mobile applications, annotated at multiple levels, including GUI interactive element grounding, functionality descriptions, and complex natural language instructions. The dataset aims to advance research on AI agents capable of completing complex tasks by interacting directly with mobile device GUIs.

- [Vision-driven Automated Mobile GUI Testing via Multimodal Large Language Model](https://arxiv.org/abs/2407.03037)
    - Zhe Liu, Cheng Li, Chunyang Chen, Junjie Wang, Boyu Wu, Yawen Wang, Jun Hu, Qing Wang
    - 🏛️ Institutions: Institute of Software, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Technical University of Munich, DiDi Global Inc.
    - 📅 Date: July 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI testing], [bug detection], [VisionDroid], [mobile agent]
    - 📖 TLDR: The paper presents **VisionDroid**, a vision-driven automated GUI testing approach utilizing Multimodal Large Language Models (MLLM) to detect non-crash functional bugs in mobile applications. By extracting GUI text information and aligning it with screenshots, VisionDroid enables MLLM to understand GUI context, facilitating deeper and function-oriented exploration. The approach segments exploration history into logically cohesive parts, prompting MLLM for bug detection, demonstrating superior performance over existing methods.

- [CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents](https://aclanthology.org/2025.findings-acl.1113/)
    - Tianqi Xu, Linyao Chen, Dai-Jie Wu, Yanjun Chen, Zecheng Zhang, Xiang Yao, Zhiqiang Xie, Yongchao Chen, Shilong Liu, Bochen Qian, Anjie Yang, Zhaoxuan Jin, Jianbo Deng, Philip Torr, Bernard Ghanem, Guohao Li
    - 🏛️ Institutions: King Abdullah University of Science and Technology, The University of Tokyo, Carnegie Mellon University, Stanford University, Harvard University, Tsinghua University, Southern University of Science and Technology, University of Oxford
    - 📅 Date: July 3, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [cross-environment], [graph-based evaluation], [task generation], [CRAB]
    - 📖 TLDR: The authors present *CRAB*, a benchmark framework designed to evaluate Multimodal Language Model agents across multiple environments. It features a graph-based fine-grained evaluation method and supports automatic task generation, addressing limitations in existing benchmarks.

- [Read Anywhere Pointed: Layout-aware GUI Screen Reading with Tree-of-Lens Grounding](https://aclanthology.org/2024.emnlp-main.533/)
    - Yue Fan, Lei Ding, Ching-Chen Kuo, Shan Jiang, Yang Zhao, Xinze Guan, Jie Yang, Yi Zhang, Xin Eric Wang
    - 🏛️ Institutions: University of California, Santa Cruz, Microsoft Research
    - 📅 Date: June 27, 2024
    - 📑 Publisher: EMNLP 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [ToL], [screen reading], [accessibility]
    - 📖 TLDR: The authors propose the Tree-of-Lens (ToL) agent to address the Screen Point-and-Read (ScreenPR) task, which involves generating natural language descriptions of screen regions based on user-indicated points. The ToL agent constructs a Hierarchical Layout Tree to comprehend the content and articulate the layout and spatial relationships between elements. The authors also introduce the ScreenPR benchmark, consisting of 650 screenshots from web, mobile, and operating system GUIs, manually annotated with 1,500 target points and regions.

- [Octo-planner: On-device Language Model for Planner-Action Agents](https://arxiv.org/abs/2406.18082)
    - Nexa AI Team
    - 🏛️ Institutions: Nexa AI
    - 📅 Date: June 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [model], [framework], [octo-planner], [on-device], [planning]
    - 📖 TLDR: This paper presents Octo-planner, an on-device planning model designed for the Planner-Action Agents Framework. Octo-planner utilizes a fine-tuned model based on Phi-3 Mini (3.8 billion parameters) for high efficiency and low power consumption. It separates planning and action execution into two distinct components: a planner agent optimized for edge devices and an action agent using the Octopus model for function execution. The model achieves a planning success rate of 98.1% on benchmark datasets, providing reliable and effective performance.

- [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://aclanthology.org/2024.findings-emnlp.68/)
    - Ziyang Meng, Yu Dai, Zezheng Gong, Shaoxiong Guo, Minglong Tang, Tongquan Wei
    - 🏛️ Institutions: East China Normal University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [hallucination mitigation], [FAC], [referent method], [VGA]
    - 📖 TLDR: This paper introduces VGA, a fine-tuned model designed to enhance GUI comprehension by reducing hallucinations. The authors constructed a Vision Question Answering (VQA) dataset of 63.8k high-quality examples using a Referent Method, ensuring model responses are highly dependent on visual content. They also propose a two-stage fine-tuning method called Foundation and Advanced Comprehension (FAC) to improve the model's ability to extract information from images and align with human intent.

- [E-ANT: A Large-Scale Dataset for Efficient Automatic GUI NavigaTion](https://arxiv.org/abs/2406.14250)
    - Ke Wang, Tianyu Xia, Zhangxuan Gu, Yi Zhao, Shuheng Shen, Changhua Meng, Weiqiang Wang, Ke Xu
    - 🏛️ Institutions: Ant Group, Tsinghua University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [e-ANT]
    - 📖 TLDR: This paper introduces **E-ANT**, the first large-scale Chinese GUI navigation dataset comprising over 40,000 real human interaction traces across more than 5,000 tiny apps. The dataset includes high-quality screenshots with annotations, facilitating the evaluation and development of GUI navigation and decision-making capabilities in multimodal large language models (MLLMs). The authors also assess various MLLMs on E-ANT, providing insights into their performance and potential improvements.

- [Identifying User Goals from UI Trajectories](https://arxiv.org/abs/2406.14314)
    - Omri Berkovitch, Sapir Caduri, Noam Kahlon, Anatoly Efros, Avi Caciularu, Ido Dagan
    - 🏛️ Institutions: Google Research, Bar-Ilan University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [evaluation metric], [intent identification]
    - 📖 TLDR: This paper introduces the task of goal identification from observed UI trajectories, aiming to infer the user's intended task based on their GUI interactions. It proposes a novel evaluation metric to assess whether two task descriptions are paraphrases within a specific UI environment. Experiments utilizing the Android-In-The-Wild and Mind2Web datasets reveal that state-of-the-art models, such as GPT-4 and Gemini-1.5 Pro, underperform compared to humans, indicating significant room for improvement.

- [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://openreview.net/forum?id=5G7MRfPngt)
    - Gabriel Herbert Sarch, Lawrence Jang, Michael J. Tarr, William W. Cohen, Kenneth Marino, Katerina Fragkiadaki
    - 🏛️ Institutions: Carnegie Mellon University, Google DeepMind
    - 📅 Date: June 20, 2024
    - 📑 Publisher: NeurIPS 2024 (Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [memory], [in-context learning], [ICAL]
    - 📖 TLDR: This paper introduces *In-Context Abstraction Learning (ICAL)*, a method enabling Vision-Language Models (VLMs) to generate their own examples from sub-optimal demonstrations and human feedback. By abstracting trajectories into generalized programs of thought, ICAL enhances decision-making in retrieval-augmented LLM and VLM agents, reducing reliance on manual prompt engineering and improving performance across various tasks.

- [GUI Action Narrator: Where and When Did That Action Take Place?](https://arxiv.org/abs/2406.13719)
    - Qinchen Wu, Difei Gao, Kevin Qinghong Lin, Zhuoyu Wu, Xiangwu Guo, Peiran Li, Weichen Zhang, Hengxu Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore, Chinese Academy of Sciences, Shenzhen
    - 📅 Date: June 19, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [framework], [Act2Cap], [GUI narrator]
    - 📖 TLDR: The authors present **Act2Cap**, a GUI action dataset containing 4,189 video-caption pairs depicting various GUI actions such as clicks, drags, and typing across multiple software environments. They also propose **GUI Narrator**, a framework that leverages cursor detection as a visual prompt to enhance the interpretation of high-resolution screenshots for GUI video captioning. Evaluations reveal that even advanced multimodal models face challenges in this domain, highlighting the need for specialized approaches to improve performance.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: iMean AI, Carnegie Mellon University
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [Mind2Web-live], [key-node evaluation]
    - 📖 TLDR: This paper presents WebCanvas, an online evaluation framework for web agents designed to address the dynamic nature of web interactions. It introduces a key-node-based evaluation metric to capture critical actions or states necessary for task completion while disregarding noise from insignificant events or changed web elements. The framework includes the Mind2Web-Live dataset, a refined version of the original Mind2Web static dataset, containing 542 tasks with 2,439 intermediate evaluation states. Despite advancements, the best-performing model achieves a task success rate of 23.1%, highlighting substantial room for improvement.

- [Adversarial Attacks on Multimodal Agents](https://arxiv.org/abs/2406.12814)
    - Chen Henry Wu, Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: Jun 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [VisualWebArena-adv]
    - 📖 TLDR: This paper investigates the safety risks posed by multimodal agents built on vision-enabled language models (VLMs). The authors introduce two adversarial attack methods: a captioner attack targeting white-box captioners and a CLIP attack that transfers to proprietary VLMs. To evaluate these attacks, they curated VisualWebArena-Adv, a set of adversarial tasks based on VisualWebArena. The study demonstrates that within a limited perturbation norm, the captioner attack can achieve a 75% success rate in making a captioner-augmented GPT-4V agent execute adversarial goals. The paper also discusses the robustness of agents based on other VLMs and provides insights into factors contributing to attack success and potential defenses.

- [GUICourse: From General Vision Language Models to Versatile GUI Agents](https://aclanthology.org/2025.acl-long.1065/)
    - Wentong Chen, Junbo Cui, Jinyi Hu, Yujia Qin, Junjie Fang, Yue Zhao, Chongyi Wang, Jun Liu, Guirong Chen, Yupeng Huo, Yuan Yao, Yankai Lin, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Renmin University of China, Tsinghua University, Xiamen University, Beijing University of Posts and Telecommunications, ModelBest, Chinese Academy of Sciences, National University of Singapore, Shanghai Qi Zhi Institute
    - 📅 Date: June 17, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [framework], [GUICourse]
    - 📖 TLDR: This paper introduces *GUICourse*, a suite of datasets aimed at training visual-based GUI agents from general vision-language models. It addresses challenges in OCR, grounding, and GUI knowledge, enhancing the models' capabilities in GUI navigation tasks.

- [GUI-WORLD: A Dataset for GUI-oriented Multimodal LLM-based Agents](https://arxiv.org/abs/2406.10819)
    - Dongping Chen, Yue Huang, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan, Pan Zhou, Jianfeng Gao, Lichao Sun
    - 🏛️ Institutions: Huazhong University of Science and Technology, University of Notre Dame, Microsoft Research, Lehigh University
    - 📅 Date: June 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [video GUI], [GUI-vid], [GUI-WORLD]
    - 📖 TLDR: This paper introduces *GUI-World*, a comprehensive dataset designed to evaluate Multimodal Large Language Models (MLLMs) in dynamic and complex GUI environments. It includes over 12,000 annotated GUI interaction videos covering diverse applications and scenarios. The study highlights the limitations of current MLLMs in handling dynamic and multi-step tasks and presents *GUI-Vid*, a fine-tuned VideoLLM, demonstrating improved understanding of various GUI tasks.

- [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html)
    - Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, Aviral Kumar
    - 🏛️ Institutions: University of California, Berkeley, University of Illinois Urbana-Champaign, Carnegie Mellon University, Google DeepMind
    - 📅 Date: June 14, 2024
    - 📑 Publisher: NeurIPS 2024 Main Conference Track
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [Android-in-the-wild], [AITW], [device control], [DigiRL]
    - 📖 TLDR: The authors present *DigiRL*, an autonomous reinforcement learning approach for training device-control agents. By fine-tuning a pre-trained vision-language model in two stages—offline and offline-to-online RL—DigiRL achieves a significant improvement in success rates on the Android-in-the-Wild dataset, establishing a new state-of-the-art for digital agents in device control.

- [GUI Odyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451)
    - Quanfeng Lu, Wenqi Shao, Zitao Liu, Fanqing Meng, Boxuan Li, Botong Chen, Siyuan Huang, Kaipeng Zhang, Yu Qiao, Ping Luo
    - 🏛️ Institutions: OpenGVLab, Shanghai AI Laboratory, The University of Hong Kong, Nanjing University, Harbin Institute of Technology, Shenzhen, Shanghai Jiao Tong University
    - 📅 Date: June 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [model], [OdysseyAgent], [cross-app navigation]
    - 📖 TLDR: This paper presents *GUI Odyssey*, a dataset comprising 7,735 episodes from six mobile devices, designed to train and evaluate cross-app navigation agents. It spans six types of cross-app tasks across 201 apps and 1,399 app combinations. Leveraging this dataset, the authors developed *OdysseyAgent*, a multimodal cross-app navigation agent fine-tuned from the Qwen-VL model, demonstrating superior accuracy over existing models in both in-domain and out-of-domain scenarios.

- [Practical, Automated Scenario-based Mobile App Testing](https://arxiv.org/abs/2406.08340)
    - Shengcheng Yu, Chunrong Fang, Mingzhe Du, Zimin Ding, Zhenyu Chen, Zhendong Su
    - 🏛️ Institutions: Nanjing University, ETH Zurich
    - 📅 Date: June 12, 2024
    - 📑 Publisher: IEEE Transactions on Software Engineering
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [ScenTest], [event knowledge graph], [GUI image understanding]
    - 📖 TLDR: This paper introduces *ScenTest*, a novel approach for scenario-based mobile app testing that integrates event knowledge graphs (EKGs) with GUI image understanding. By extracting entities and relationships from crowdsourced test reports, ScenTest constructs EKGs for specific scenarios, guiding automated testing processes. This method bridges the gap between testing execution and app business logic, achieving fully automated testing on target scenarios for the first time.

- [MobileAgentBench: An Efficient and User-Friendly Benchmark for Mobile LLM Agents](https://arxiv.org/abs/2406.08184)
    - Luyuan Wang, Yongyu Deng, Yiwei Zha, Guodong Mao, Qinmin Wang, Tianchen Min, Wei Chen, Shoufa Chen
    - 🏛️ Institutions: Carnegie Mellon University, University of Michigan, Northeastern University, The University of Hong Kong
    - 📅 Date: June 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [MobileAgentBench]
    - 📖 TLDR: This paper introduces *MobileAgentBench*, a benchmark designed to evaluate the performance of large language model-based mobile agents. It defines 100 tasks across 10 open-source apps, categorized by difficulty levels, and assesses existing agents like AppAgent and MobileAgent to facilitate systematic comparisons.

- [On the Effects of Data Scale on UI Control Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a79f3ef3b445fd4659f44648f7ea8ffd-Abstract-Datasets_and_Benchmarks_Track.html)
    - Wei Li, William Bishop, Alice Li, Chris Rawles, Folawiyo Campbell-Ajala, Divya Tyamagundlu, Oriana Riva
    - 🏛️ Institutions: Google DeepMind, Google
    - 📅 Date: June 6, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [AndroidControl], [fine-tuning], [scalability]
    - 📖 TLDR: This study investigates how the performance of computer control agents scales with the amount of fine-tuning data. The authors introduce **AndroidControl**, a dataset comprising 15,283 demonstrations across 833 Android applications. Findings indicate that while in-domain performance improves with more data, out-of-domain performance, especially on high-level tasks, scales more slowly, suggesting that fine-tuning alone may be insufficient for robust out-of-domain performance.

- [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://openreview.net/forum?id=O0nBMRlkc8)
    - Junyang Wang, Haiyang Xu, Haitao Jia, Xi Zhang, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Alibaba Group, Beijing University of Posts and Telecommunications
    - 📅 Date: June 3, 2024
    - 📑 Publisher: NeurIPS 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [multi-agent], [planning], [decision-making], [reflection]
    - 📖 TLDR: The paper presents **Mobile-Agent-v2**, a multi-agent architecture designed to assist with mobile device operations. It comprises three agents: a planning agent that generates task progress, a decision agent that navigates tasks using a memory unit, and a reflection agent that corrects erroneous operations. This collaborative approach addresses challenges in navigation and long-context input scenarios, achieving over a 30% improvement in task completion compared to single-agent architectures.

- [WebSuite: Systematically Evaluating Why Web Agents Fail](https://arxiv.org/abs/2406.01623)
    - Eric Li, Jim Waldo
    - 🏛️ Institutions: Harvard
    - 📅 Date: June 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [failure analysis], [analysis], [task disaggregation]
    - 📖 TLDR: This paper introduces *WebSuite*, a diagnostic benchmark to investigate the causes of web agent failures. By categorizing agent tasks using a taxonomy of operational, informational, and navigational actions, WebSuite offers granular insights into the specific actions where agents struggle, like filtering or form completion. It enables detailed comparison across agents, identifying areas for architectural and UX adaptation to improve agent reliability and task success on the web.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen Wu, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore, Microsoft GenAI
    - 📅 Date: June 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [instructional videos], [visual planning], [hierarchical task decomposition], [complex software interaction]
    - 📖 TLDR: VideoGUI presents a benchmark for evaluating GUI automation on tasks derived from instructional videos, focusing on visually intensive applications like Adobe Photoshop and video editing software. The benchmark includes 178 tasks, with a hierarchical evaluation method distinguishing high-level planning, mid-level procedural steps, and precise action execution. VideoGUI reveals current model limitations in complex visual tasks, marking a significant step toward improved visual planning in GUI automation.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: Carnegie Mellon University, University of California, Santa Barbara
    - 📅 Date: June 2024
    - 📑 Publisher: NAACL 2024 Industry Track
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [UI element localization], [LVG]
    - 📖 TLDR: This work introduces the task of visual UI grounding, which unifies detection and grounding by enabling models to identify UI elements referenced by natural language commands solely from visual input. The authors propose **LVG**, a model that outperforms baselines pre-trained on larger datasets by over 4.9 points in top-1 accuracy, demonstrating its effectiveness in localizing referenced UI elements without relying on UI metadata.

- [Large Language Models Can Self-Improve At Web Agent Tasks](https://arxiv.org/abs/2405.20309)
    - Ajay Patel, Markus Hofmarcher, Claudiu Leoveanu-Condrei, Marius-Constantin Dinu, Chris Callison-Burch, Sepp Hochreiter
    - 🏛️ Institutions: University of Pennsylvania, ExtensityAI, Johannes Kepler University Linz, NXAI
    - 📅 Date: May 30, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [self-improvement], [synthetic training data], [web navigation], [WebArena]
    - 📖 TLDR: This paper investigates the ability of large language models (LLMs) to enhance their performance as web agents through self-improvement. Utilizing the WebArena benchmark, the authors fine-tune LLMs on synthetic training data, achieving a 31% improvement in task completion rates. They also introduce novel evaluation metrics to assess the performance, robustness, and quality of the fine-tuned agents' trajectories.

- [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/01a83bc2f2732a58e6aa731e659e7101-Abstract-Conference.html)
    - Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William E Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Kenji Toyama, Robert James Berry, Divya Tyamagundlu, Timothy P Lillicrap, Oriana Riva
    - 🏛️ Institutions: Google DeepMind, Google
    - 📅 Date: May 23, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [Android-based agents], [task diversity], [reinforcement learning], [dynamic environment]
    - 📖 TLDR: AndroidWorld introduces a dynamic Android environment for benchmarking autonomous agents across 116 tasks spanning 20 Android apps. These tasks vary through parameterized and natural language prompts, fostering a realistic testing ground for agents designed to operate in complex mobile environments. The benchmark supports millions of task variations, allowing agents to respond to the Android system's changing states and improving real-world applicability.

- [Unveiling Disparities in Web Task Handling Between Human and Web Agent](https://arxiv.org/abs/2405.04497)
    - Kihoon Son, Jinhyeon Kwon, DaEun Choi, Tae Soo Kim, Young-Ho Kim, Sangdoo Yun, Juho Kim
    - 🏛️ Institutions: KAIST, Seoul National University
    - 📅 Date: May 7, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [cognitive comparison], [task analysis]
    - 📖 TLDR: This paper examines how humans and web agents differ in handling web-based tasks, focusing on key aspects such as planning, action-taking, and reflection. Using a think-aloud protocol, the study highlights the cognitive processes humans employ, like exploration and adjustment, versus the more rigid task execution patterns observed in web agents. The authors identify several limitations in current web agents, proposing the need for improved frameworks to enhance adaptability and knowledge update mechanisms in agent-based systems.

- [Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2405.00516)
    - Lucas-Andreï Thil, Mirela Popa, Gerasimos Spanakis
    - 🏛️ Institutions: Maastricht University the Netherlands
    - 📅 Date: May 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [large language models], [reinforcement learning]
    - 📖 TLDR: This paper proposes a novel approach combining supervised learning (SL) and reinforcement learning (RL) techniques to train web navigation agents using large language models. The authors address limitations in previous models' understanding of HTML content and introduce methods to enhance true comprehension. Their approach, evaluated on the MiniWoB benchmark, outperforms previous SL methods on certain tasks using less data and narrows the performance gap with RL models. The study achieves 43.58% average accuracy in SL and 36.69% when combined with a multimodal RL approach, setting a new direction for future web navigation research.

- [Octopus v3: Technical Report for On-device Sub-billion Multimodal AI Agent](https://arxiv.org/abs/2404.11459)
    - Wei Chen, Zhiyuan Li
    - 🏛️ Institutions: Stanford University
    - 📅 Date: April 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [functional token], [on-device AI], [octopus v3]
    - 📖 TLDR: This paper introduces Octopus v3, a compact multimodal AI agent with less than 1 billion parameters, designed for efficient on-device operation. It processes both English and Chinese inputs, integrating visual and textual data to perform tasks such as sending emails, messaging, and online shopping. The model employs a functional token approach to translate image-based data into actionable outcomes, demonstrating high accuracy and efficiency on edge devices, including Raspberry Pi.

- [Search Beyond Queries: Training Smaller Language Models for Web Interactions via Reinforcement Learning](https://arxiv.org/abs/2404.10887)
    - Moghis Fereidouni, A.B. Siddique
    - 🏛️ Institutions: University of Kentucky
    - 📅 Date: April 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [grounded language agent], [flan-T5], [unsupervised domain adaptation]
    - 📖 TLDR: This paper introduces GLAINTEL, a grounded language agent framework designed to enhance web interaction using instruction-finetuned language models, particularly Flan-T5, with reinforcement learning (PPO) to tackle interactive web navigation challenges. The study explores unsupervised and supervised training methods, evaluating the effects of human demonstration on agent performance. Results indicate that combining human feedback with reinforcement learning yields effective outcomes, rivaling larger models like GPT-4 on web navigation tasks.

- [MMInA: Benchmarking Multihop Multimodal Internet Agents](https://aclanthology.org/2025.findings-acl.703/)
    - Shulin Tian, Ziniu Zhang, Liangyu Chen, Ziwei Liu
    - 🏛️ Institutions: Nanyang Technological University
    - 📅 Date: April 15, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [multihop web browsing], [multimodal tasks], [long-range reasoning]
    - 📖 TLDR: The **MMInA** benchmark is designed to evaluate agents' capacity to complete complex, multihop web tasks by navigating and extracting information across evolving real-world websites. Composed of 1,050 tasks across diverse domains, MMInA challenges agents with realistic, multimodal information retrieval and reasoning tasks, such as comparative shopping and travel inquiries. Despite recent advances, agents show difficulties in handling tasks requiring sequential steps across multiple sites, underscoring the need for enhanced multimodal and memory-augmented models.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Automation Task Evaluation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: April 12, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [UI automation], [mobile agent evaluation]
    - 📖 TLDR: LlamaTouch is an evaluation testbed designed for mobile UI automation, enabling reliable task assessment across 495 annotated tasks. It provides a scalable solution to evaluate agents in real-world mobile settings, comparing agent actions to essential UI states for accurate task completion. LlamaTouch supports dynamic environments, advancing mobile agent reliability and scalability in task automation.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Jing Hua Toh, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Carnegie Mellon University, Salesforce Research, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [real computer tasks], [online environment], [online benchmark]
    - 📖 TLDR: OSWorld introduces a groundbreaking benchmark for multimodal agents to perform open-ended tasks within real computer environments across platforms like Ubuntu, Windows, and macOS. It includes 369 real-world tasks involving web and desktop apps, file management, and multi-app workflows, with custom evaluation scripts for reproducibility. The results reveal current agents’ limitations in GUI interaction and operational knowledge, as they achieve just 12.24% task success compared to humans' 72.36%, highlighting critical gaps for future model improvement.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web page understanding], [grounding]
    - 📖 TLDR: VisualWebBench introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on web-based tasks. It includes 1.5K human-curated instances across 139 websites in 87 sub-domains. The benchmark spans seven tasks—such as OCR, grounding, and web-based QA—aiming to test MLLMs' capabilities in fine-grained web page understanding. Results reveal significant performance gaps, particularly in grounding tasks, highlighting the need for advancement in MLLM web understanding.

- [Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)
    - Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
    - 🏛️ Institutions: University of California, Berkeley, University of Michigan
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [evaluation model], [domain transfer]
    - 📖 TLDR: This paper presents an autonomous evaluation framework for digital agents to enhance performance on web navigation and device control. The study introduces modular, cost-effective evaluators achieving up to 92.9% accuracy in benchmarks like WebArena and outlines their use in fine-tuning agents, improving state-of-the-art by 29% without additional supervision.

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://eccv.ecva.net/virtual/2024/poster/749)
    - Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeff Nichols, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: April 8, 2024
    - 📑 Publisher: ECCV 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [benchmark], [grounding], [reasoning], [mobile UI understanding], [ferret-UI]
    - 📖 TLDR: This paper presents **Ferret-UI**, a multimodal large language model (MLLM) designed to understand and interact with mobile user interfaces. The model incorporates advanced capabilities for referring, grounding, and reasoning about UI elements. By training on a variety of UI tasks, Ferret-UI achieves high performance in tasks such as icon recognition and text extraction. The authors introduce a unique architecture that allows for improved visual feature extraction from mobile screens, paving the way for applications in accessibility and user interaction.

- [Enhancing Mobile "How-to" Queries with Automated Search Results Verification and Reranking](https://arxiv.org/abs/2404.08860)
    - Lei Ding, Jeshwanth Bheemanpally, Yi Zhang
    - 🏛️ Institutions: University of California, Santa Cruz
    - 📅 Date: April 2024
    - 📑 Publisher: SIGIR 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [reranking], [verification], [mobile task automation]
    - 📖 TLDR: This paper presents a system that enhances mobile "how-to" queries by verifying and reranking search results through automated instruction extraction, on-device action execution, and reranking based on relevance. The method improves on traditional ranking by analyzing device-specific execution success. The approach comprises a three-stage pipeline: 1) extracting step-by-step instructions from top search results, 2) validating these instructions on mobile devices, and 3) reranking based on performance. The system leverages a pre-trained GPT model for initial processing, ensuring adaptability across diverse apps and systems.

- [Benchmarking Mobile Device Control Agents across Diverse Configurations](https://arxiv.org/abs/2404.16660)
    - Juyong Lee, Taywon Min, Minyong An, Dongyoon Hahm, Haeone Lee, Changyeon Kim, Kimin Lee
    - 🏛️ Institutions: KAIST, Seoul National University, Yonsei University
    - 📅 Date: April 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile device control], [agent performance]
    - 📖 TLDR: This paper presents **B-MoCA**, a comprehensive benchmark for evaluating mobile device control agents using an Android-based testbed with 131 tasks and various device configurations. The benchmark assesses agents' abilities across tasks that include device-specific variations, navigation, and human-like dual-gesture interactions. B-MoCA highlights that current agents perform well on basic tasks but struggle with complex configurations, pointing to opportunities for future improvements in mobile automation capabilities.

- [AgentStudio: A Toolkit for Building General Virtual Agents](https://openreview.net/forum?id=axUf8BOjnH)
    - Longtao Zheng, Zhiyuan Huang, Zhenghai Xue, Xinrun Wang, Bo An, Shuicheng Yan
    - 🏛️ Institutions: Nanyang Technological University, Skywork AI, ETH Zurich
    - 📅 Date: March 26, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [general virtual agents], [open-ended learning], [tool creation], [GroundUI], [benchmark]
    - 📖 TLDR: AgentStudio is a robust toolkit for developing virtual agents with versatile actions, such as GUI automation and code execution. It unifies real-world human-computer interactions across OS platforms and includes diverse observation and action spaces, facilitating comprehensive training and benchmarking in complex settings. The toolkit's flexibility promotes agent generalization across varied tasks, supporting tool creation and a multimodal interaction interface to advance agent adaptability and learning.

- [WebVLN: Vision-and-Language Navigation on Websites](https://arxiv.org/abs/2312.15820)
    - Qi Chen, Dileepa Pitawela, Chongyang Zhao, Gengze Zhou, Hsiang-Ting Chen, Qi Wu
    - 🏛️ Institutions: The University of Adelaide
    - 📅 Date: March 24, 2024
    - 📑 Publisher: AAAI 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [web-based VLN], [HTML content integration], [multimodal navigation]
    - 📖 TLDR: This paper introduces the *WebVLN* task, where agents navigate websites by following natural language instructions that include questions and descriptions. Aimed at emulating real-world browsing behavior, the task allows the agent to interact with elements not directly visible in the rendered content by integrating HTML-specific information. A new *WebVLN-Net* model, based on the VLN BERT framework, is introduced alongside the *WebVLN-v1* dataset, supporting question-answer navigation across web pages. This framework demonstrated significant improvement over existing web-based navigation methods, marking a new direction in vision-and-language navigation research.

- [Tur[k]ingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.188/)
    - Kevin Xu, Yeganeh Kordi, Tanay Nayak, Adi Asija, Yizhong Wang, Kate Sanders, Adam Byerly, Jingyu Zhang, Benjamin Van Durme, Daniel Khashabi
    - 🏛️ Institutions: Johns Hopkins University, Brown University, University of Washington
    - 📅 Date: March 18, 2024
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [multi-modal reasoning], [TurkingBench], [turking]
    - 📖 TLDR: This paper introduces **Tur[k]ingBench**, a benchmark comprising 158 web-grounded tasks designed to evaluate AI agents' capabilities in complex web-based environments. Unlike prior benchmarks that utilize synthetic web pages, Tur[k]ingBench leverages natural HTML pages from crowdsourcing platforms, presenting tasks with rich multi-modal contexts. The benchmark includes 32.2K instances, each with diverse inputs, challenging models to interpret and interact with web pages effectively. Evaluations of state-of-the-art models reveal significant room for improvement, highlighting the need for advanced web-based agents capable of handling real-world web interactions. 

- [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://proceedings.mlr.press/v235/drouin24a.html)
    - Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montreal, McGill University, University de Montreal
    - 📅 Date: March 11, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [enterprise task automation], [ServiceNow], [knowledge work automation]
    - 📖 TLDR: WorkArena introduces a robust benchmark hosted on the ServiceNow platform to assess the effectiveness of large language model-based agents in performing 33 knowledge tasks common to enterprise environments. Leveraging BrowserGym, an environment that simulates complex browser interactions, WorkArena provides web agents with realistic challenges like data entry, form completion, and information retrieval in knowledge bases. Despite promising initial results, open-source models show a 42.7% success rate compared to closed-source counterparts, underlining the current gap in task automation for enterprise applications and highlighting key areas for improvement.

- [Android in the Zoo: Chain-of-Action-Thought for GUI Agents](https://aclanthology.org/2024.findings-emnlp.702/)
    - Jiwen Zhang, Jihao Wu, Teng Yihua, Minghui Liao, Nuo Xu, Xiao Xiao, Zhongyu Wei, Duyu Tang
    - 🏛️ Institutions: Fudan University, Huawei
    - 📅 Date: March 5, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [Android GUI], [chain-of-action-thought], [autonomous GUI agents]
    - 📖 TLDR: This paper introduces *Chain-of-Action-Thought* (CoAT), a novel paradigm to improve GUI agent task completion by enabling agents to interpret previous actions, current screen content, and action rationale for next steps. The authors present the *Android-In-The-Zoo* (AitZ) dataset, which includes 18,643 screen-action pairs with detailed annotations, supporting CoAT's development and evaluation. The study demonstrates that fine-tuning with the AitZ dataset improves performance of a baseline large language model in predicting correct action sequences in Android tasks.

- [Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II as a Case Study](https://arxiv.org/abs/2403.03186)
    - Weihao Tan, Ziluo Ding, Wentao Zhang, Boyu Li, Bohan Zhou, Junpeng Yue, Haochong Xia, Jiechuan Jiang, Longtao Zheng, Xinrun Xu, Yifei Bi, Pengjie Gu, Xinrun Wang, Börje F. Karlsson, Bo An, Zongqing Lu
    - 🏛️ Institutions: Nanyang Technological University, Beijing Academy of Artificial Intelligence, Peking University
    - 📅 Date: March 5, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [cradle], [general computer control], [multimodal], [keyboard and mouse control], [long-term memory], [reasoning], [self-improvement]
    - 📖 TLDR: This paper introduces *Cradle*, a framework designed to achieve General Computer Control (GCC) by enabling agents to perform any computer task using only screen images (and possibly audio) as input and producing keyboard and mouse operations as output. The authors deploy Cradle in the complex AAA game Red Dead Redemption II, demonstrating its capability to follow the main storyline and complete real missions with minimal reliance on prior knowledge or resources.

- [Cradle: Empowering Foundation Agents Towards General Computer Control](https://proceedings.mlr.press/v267/tan25h.html)
    - Weihao Tan, Wentao Zhang, Xinrun Xu, Haochong Xia, Ziluo Ding, Boyu Li, Bohan Zhou, Junpeng Yue, Jiechuan Jiang, Yewen Li, Ruyi An, Molei Qin, Chuqiao Zong, Longtao Zheng, Yujie Wu, Xiaoqiang Chai, Yifei Bi, Tianbao Xie, Pengjie Gu, Xiyun Li, Ceyao Zhang, Long Tian, Chaojie Wang, Xinrun Wang, Börje F. Karlsson, Bo An, Shuicheng Yan, Zongqing Lu
    - 🏛️ Institutions: Skywork AI, Beijing Academy of Artificial Intelligence, Nanyang Technological University, Peking University, Institute of Software, Chinese Academy of Sciences, The University of Hong Kong, The Chinese University of Hong Kong
    - 📅 Date: March 5, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [general computer control], [skill curation], [self-improvement]
    - 📖 TLDR: This paper introduces the Cradle framework, designed to enable general computer control (GCC) through multimodal input (e.g., screen images and optional audio) and outputs (keyboard and mouse). Cradle’s six core modules, including self-reflection, skill curation, and memory, allow for generalized task handling in complex environments like AAA games. Demonstrated in *Red Dead Redemption II*, the framework exhibits adaptability by performing real missions and following the storyline with minimal prior knowledge, showcasing its potential as a generalist agent for diverse computer tasks.

- [On the Multi-turn Instruction Following for Conversational Web Agents](https://arxiv.org/abs/2402.15057)
    - Yang Deng, Xuan Zhang, Wenxuan Zhang, Yifei Yuan, See-Kiong Ng, Tat-Seng Chua
    - 🏛️ Institutions: National University of Singapore, DAMO Academy, University of Copenhagen
    - 📅 Date: February 23, 2024
    - 📑 Publisher: Findings of ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [multi-turn dialogue], [memory utilization], [self-reflective planning]
    - 📖 TLDR: This paper explores multi-turn conversational web navigation, introducing the MT-Mind2Web dataset to support instruction-following tasks for web agents. The proposed Self-MAP (Self-Reflective Memory-Augmented Planning) framework enhances agent performance by integrating memory with self-reflection for sequential decision-making in complex interactions. Extensive evaluations using MT-Mind2Web demonstrate Self-MAP's efficacy in addressing the limitations of current models in multi-turn interactions, providing a novel dataset and framework for evaluating and training agents on detailed, multi-step web-based tasks.

- [Improving Language Understanding from Screenshots](https://arxiv.org/abs/2402.14073)
    - Tianyu Gao, Zirui Wang, Adithya Bhaskar, Danqi Chen
    - 🏛️ Institutions: Princeton University
    - 📅 Date: February 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [screenshot language model], [patch-and-text prediction], [PTP]
    - 📖 TLDR: This paper introduces a novel approach to improve the language understanding capabilities of screenshot language models (LMs). The authors propose a Patch-and-Text Prediction (PTP) objective, which masks and recovers both image patches and text within screenshots. The method significantly narrows the performance gap between screenshot LMs and text-only models on language understanding tasks, achieving comparable results to BERT on most GLUE tasks. The research also extends PTP to train autoregressive screenshot LMs, demonstrating improved perplexity by utilizing screenshot context.

- [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Abstract-Conference.html)
    - Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
    - 🏛️ Institutions: Renmin University of China, Peking University, Tencent
    - 📅 Date: Feb 17, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [attack], [backdoor], [safety]
    - 📖 TLDR: This paper investigates backdoor attacks on LLM-based agents, introducing a framework that categorizes attacks based on outcomes and trigger locations. The study demonstrates the vulnerability of such agents to backdoor attacks and emphasizes the need for targeted defenses.

- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://arxiv.org/abs/2402.10196)
    - Lingbo Mo, Zeyi Liao, Boyuan Zheng, Yu Su, Chaowei Xiao, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of Wisconsin-Madison
    - 📅 Date: February 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [adversarial attacks], [security risks], [language agents], [perception-brain-action]
    - 📖 TLDR: This paper introduces a conceptual framework to assess and understand adversarial vulnerabilities in language agents, dividing the agent structure into three components—Perception, Brain, and Action. It discusses 12 specific adversarial attack types that exploit these components, ranging from input manipulation to complex backdoor and jailbreak attacks. The framework provides a basis for identifying and mitigating risks before the widespread deployment of these agents in real-world applications.

- [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26/)
    - Chaoyun Zhang, Liqun Li, Shilin He, Xu Zhang, Bo Qiao, Si Qin, Minghua Ma, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Microsoft
    - 📅 Date: February 14, 2024
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [UI automation], [Windows], [UFO]
    - 📖 TLDR: This paper presents UFO, a pioneering multimodal LLM-based agent designed to fulfill user requests on Windows OS. UFO employs a dual-agent architecture—comprising AppAgent and ActAgent—that can interpret and execute complex tasks across multiple Windows applications by observing UI elements and utilizing control interactions. The framework allows UFO to handle intricate, cross-application workflows and execute commands seamlessly based on natural language prompts. It integrates GPT-Vision to recognize and interact with graphical elements, enabling flexible, autonomous task completion within and across diverse Windows applications.

- [ScreenAgent: A Vision Language Model-driven Computer Control Agent](https://www.ijcai.org/proceedings/2024/711)
    - Runliang Niu, Jindong Li, Shiqi Wang, Yali Fu, Xiyu Hu, Xueyuan Leng, He Kong, Yi Chang, Qi Wang
    - 🏛️ Institutions: Jilin University
    - 📅 Date: February 13, 2024
    - 📑 Publisher: IJCAI 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual language model], [computer control agent]
    - 📖 TLDR: This paper introduces ScreenAgent, a computer control agent powered by a visual language large model. The system can interpret natural language instructions and execute them on various computer applications by analyzing screen content. ScreenAgent employs a novel action grounding mechanism to map high-level instructions to specific UI interactions. Evaluated on a diverse set of tasks across different applications, ScreenAgent demonstrates superior performance in task completion and generalization compared to existing methods.

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)
    - Zhiyong Wu, Chengcheng Han, Zichen Ding, Zhenmin Weng, Zhoumianze Liu, Shunyu Yao, Tao Yu, Lingpeng Kong
    - 🏛️ Institutions: Shanghai AI Laboratory, East China Normal University, Princeton University, The University of Hong Kong
    - 📅 Date: February 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [self-directed learning], [GAIA], [FRIDAY], [OS-copilot]
    - 📖 TLDR: The OS-Copilot framework supports building generalist agents capable of performing diverse tasks across an operating system (OS). This work introduces FRIDAY, an embodied agent using OS-Copilot to self-improve by learning from task outcomes. It operates with a memory-based architecture to tackle OS-level tasks across applications like terminals, web browsers, and third-party tools. Tested on the GAIA benchmark, FRIDAY achieved 35% higher performance than prior methods, proving effective in adapting to unfamiliar applications and refining its capabilities with minimal guidance.

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://arxiv.org/abs/2402.04615)
    - Gilles Baechler, Srinivas Sunkara, Maria Wang, Fedir Zubach, Hassan Mansoor, Vincent Etter, Victor Cărbune, Jason Lin, Jindong Chen, Abhanshu Sharma
    - 🏛️ Institutions: Google DeepMind
    - 📅 Date: February 7, 2024
    - 📑 Publisher: IJCAI 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [UI understanding], [infographics understanding], [vision language model]
    - 📖 TLDR: This paper introduces ScreenAI, a vision-language model specializing in UI and infographics understanding. The model combines the PaLI architecture with the flexible patching strategy of pix2struct and is trained on a unique mixture of datasets. ScreenAI achieves state-of-the-art results on several UI and infographics-based tasks, outperforming larger models. The authors also release three new datasets for screen annotation and question answering tasks.

- [Dual-View Visual Contextualization for Web Navigation](https://arxiv.org/abs/2402.04476)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: February 6, 2024
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [visual contextualization]
    - 📖 TLDR: This paper proposes a novel approach to web navigation by contextualizing HTML elements through their "dual views" in webpage screenshots. The method leverages both the textual content of HTML elements and their visual representation in the screenshot to create more informative representations for web agents. Evaluated on the Mind2Web dataset, the approach demonstrates consistent improvements over baseline methods across various scenarios, including cross-task, cross-website, and cross-domain navigation tasks.

- [WebLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://arxiv.org/abs/2402.05930)
    - Xing Han Lu, Zdeněk Kasner, Siva Reddy
    - 🏛️ Institutions: Mila, McGill University
    - 📅 Date: February 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [multi-turn dialogue], [real-world navigation], [WebLINX]
    - 📖 TLDR: WebLINX addresses the complexity of real-world website navigation for conversational agents, with a benchmark featuring over 2,300 demonstrations across 150+ websites. The benchmark allows agents to handle multi-turn instructions and interact dynamically across diverse domains, including geographic and thematic categories. The study proposes a retrieval-inspired model that selectively extracts key HTML elements and browser actions, achieving efficient task-specific representations. Experiments reveal that smaller finetuned decoders outperform larger zero-shot multimodal models, though generalization to new environments remains challenging.

- [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://eccv.ecva.net/virtual/2024/poster/1107)
    - Raghav Kapoor, Yash Parag Butala, Melisa Russak, Jing Yu Koh, Kiran Kamble, Waseem Alshikh, Ruslan Salakhutdinov
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: February 2024
    - 📑 Publisher: ECCV 2024 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [benchmark]
    - 📖 TLDR: OmniACT introduces a dataset and benchmark to train and evaluate multimodal agents capable of autonomously performing diverse tasks across desktop and web environments. Using annotated UI elements across applications, it combines visual grounding with natural language instructions, providing 9,802 data points for developing agents that integrate high-level reasoning with UI interactions. The study highlights the limited proficiency of current models, with baselines like GPT-4 only achieving 15% of human performance on executable scripts, emphasizing OmniACT's potential as a testbed for advancing multimodal AI.

- [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://openreview.net/forum?id=jE6pDYCnVF)
    - Junyang Wang, Haiyang Xu, Jiabo Ye, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Beijing Jiaotong University, Alibaba Group
    - 📅 Date: January 29, 2024
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark]
    - 📖 TLDR: This paper presents Mobile-Agent, an autonomous multi-modal agent designed for mobile device interaction. The system integrates visual perception, natural language processing, and action prediction to navigate and operate mobile applications. The authors introduce a new dataset and benchmark for evaluating mobile agents, demonstrating Mobile-Agent's superior performance in task completion and generalization across various apps compared to existing methods.

- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://aclanthology.org/2024.acl-long.371/)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab, Westlake University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: This paper introduces WebVoyager, an innovative web agent powered by Large Multimodal Models (LMMs) that can complete user instructions end-to-end by interacting with real-world websites. The authors establish a new benchmark with tasks from 15 popular websites and propose an automatic evaluation protocol using GPT-4V. WebVoyager achieves a 59.1% task success rate, significantly outperforming GPT-4 (All Tools) and text-only setups. The study demonstrates the effectiveness of multimodal approaches in web automation and provides insights into developing more intelligent web interaction solutions.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://aclanthology.org/2024.acl-long.50/)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [dataset], [multimodal agent evaluation], [visually grounded tasks]
    - 📖 TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Li YanTao, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: Nanjing University, Shanghai AI Lab
    - 📅 Date: January 19, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [benchmark], [GUI grounding], [visual grounding]
    - 📖 TLDR: TBD.

- [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, ByteDance
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [grounding], [SeeAct], [multimodal-Mind2web]
    - 📖 TLDR: This paper explores the capability of GPT-4V(ision), a multimodal model, as a web agent that can perform tasks across various websites by following natural language instructions. It introduces the **SEEACT** framework, enabling GPT-4V to navigate, interpret, and interact with elements on websites. Evaluated using the **Mind2Web** benchmark and an online test environment, the framework demonstrates high performance on complex web tasks by integrating grounding strategies like element attributes and image annotations to improve HTML element targeting. However, grounding remains challenging, presenting opportunities for further improvement.

- [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7ef7d8359036afd8c2378d82c21058a4-Abstract-Conference.html)
    - Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu, Izzeddin Gur
    - 🏛️ Institutions: The University of Tokyo, Google DeepMind
    - 📅 Date: Jan 1, 2024
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [model], [dataset], [web navigation], [instruction-following], [WebShop]
    - 📖 TLDR: This paper introduces WebGUM, an instruction-following multimodal agent for autonomous web navigation that leverages both visual (webpage screenshots) and textual (HTML) inputs to perform actions such as click and type. The model is trained on a vast corpus of demonstrations and shows improved capabilities in visual perception, HTML comprehension, and multi-step decision-making, achieving state-of-the-art performance on benchmarks like MiniWoB and WebShop. WebGUM provides a scalable approach to web-based tasks without task-specific architectures, enabling high-performance web navigation with generalizable, multimodal foundation models.

- [AppAgent: Multimodal Agents as Smartphone Users](https://doi.org/10.1145/3706598.3713600)
    - Chi Zhang, Zhao Yang, Jiaxuan Liu, Yucheng Han, Xin Chen, Zebiao Huang, Bin Fu, Gang Yu
    - 🏛️ Institutions: Tencent
    - 📅 Date: December 21, 2023
    - 📑 Publisher: CHI 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [smartphone interaction], [autonomous exploration], [self-improve]
    - 📖 TLDR: This paper introduces AppAgent, a novel multimodal agent framework designed to operate smartphone applications. The agent uses a simplified action space to mimic human-like interactions such as tapping and swiping. AppAgent learns to navigate and use new apps through autonomous exploration or by observing human demonstrations, creating a knowledge base for executing complex tasks across different applications. The framework's effectiveness is demonstrated through extensive testing on 50 tasks across 10 diverse applications.

- [AssistGUI: Task-Oriented Desktop Graphical User Interface Automation](https://arxiv.org/abs/2312.13108)
    - Difei Gao, Lei Ji, Zechen Bai, Mingyu Ouyang, Peiran Li, Dongxing Mao, Qinchen Wu, Weichen Zhang, Peiyi Wang, Xiangwu Guo, Hengxu Wang, Luowei Zhou, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: December 20, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [desktop productivity tasks]
    - 📖 TLDR: This study presents *AssistGUI*, a benchmark and framework for desktop GUI automation, featuring an LLM-based agent capable of completing complex user requests by analyzing instructional videos and performing actions on the desktop. Utilizing a novel Actor-Critic framework and GUI parser, *AssistGUI* was tested on 100 tasks across nine applications, such as MS Word and After Effects. Despite advances, the top-performing model achieved only a 46% success rate, illustrating the challenge of comprehensive desktop automation and underscoring areas for future research in agent-driven GUI tasks.

- [CogAgent: A Visual Language Model for GUI Agents](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_CogAgent_A_Visual_Language_Model_for_GUI_Agents_CVPR_2024_paper.html)
    - Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhao Chen, Yuxuan Wang, Yining Ye, Jiayi Zhang, Hao Dong, Wenhu Chen, Yizhou Wang, Kai-Wei Chang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI
    - 📅 Date: December 15, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [visual language model], [GUI agent]
    - 📖 TLDR: This paper presents CogAgent, a visual language model designed for GUI agents. The authors introduce a new dataset, CogBench, featuring 1,430 GUI tasks across various applications. CogAgent employs a novel training approach combining supervised fine-tuning and decision-making fine-tuning. The model demonstrates superior performance on CogBench and generalizes well to unseen applications, outperforming existing models like GPT-4V in GUI task completion.

- [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25ae35b5b1738d80f1f03a8713e405ec-Abstract-Conference.html)
    - Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, Thomas Scialom
    - 🏛️ Institutions: Meta AI, Hugging Face, AutoGPT
    - 📅 Date: November 21, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Misc]
    - 🔑 Key: [benchmark], [multi-modality], [tool use], [reasoning]
    - 📖 TLDR: GAIA is a benchmark developed for evaluating general-purpose AI assistants. It aims to test assistant models across multiple modalities and complex reasoning tasks in real-world settings, including scenarios that require tool usage and open-ended question answering. With a dataset comprising 466 questions across various domains, GAIA highlights gaps between current AI performance and human capability, presenting a significant challenge for large language models such as GPT-4.

- [GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](https://arxiv.org/abs/2311.07562)
    - An Yan, Zhengyuan Yang, Wanrong Zhu, Kevin Lin, Linjie Li, Jianfeng Wang, Jianwei Yang, Yiwu Zhong, Julian McAuley, Jianfeng Gao, Zicheng Liu, Lijuan Wang
    - 🏛️ Institutions: University of California San Diego, Microsoft, University of California, Santa Barbara, University of Wisconsin-Madison
    - 📅 Date: November 13, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [zero-shot GUI navigation], [MM-navigator], [MobileNav], [GPT-4V]
    - 📖 TLDR: This paper explores the capabilities of GPT-4V in navigating smartphone GUIs without prior training. The authors introduce a novel framework for GUI navigation and a new benchmark, MobileNav, featuring 1,000 navigation tasks across 100 mobile apps. The study demonstrates GPT-4V's impressive zero-shot performance in understanding and interacting with mobile interfaces, outperforming previous methods and even approaching human-level performance on some tasks.

- [Interactive Evolution: A Neural-Symbolic Self-Training Framework For Large Language Models](https://aclanthology.org/2025.acl-long.635/)
    - Fangzhi Xu, Qiushi Sun, Kanzhi Cheng, Jun Liu, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Shanghai AI Laboratory, The University of Hong Kong, Nanjing University
    - 📅 Date: July 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [neural-symbolic self-training], [online exploration], [self-refinement]
    - 📖 TLDR: This paper introduces *ENVISIONS*, a neural-symbolic self-training framework designed to improve large language models (LLMs) by enabling self-training through interaction with a symbolic environment. The framework addresses symbolic data scarcity and enhances LLMs' symbolic reasoning proficiency by iteratively exploring, refining, and learning from symbolic tasks without reinforcement learning. Extensive evaluations across web navigation, math, and logical reasoning tasks highlight *ENVISIONS* as a promising approach for enhancing LLM symbolic processing.

- [UI Layout Generation with LLMs Guided by UI Grammar](https://arxiv.org/abs/2310.15455)
    - Yuwen Lu, Ziang Tong, Qinyi Zhao, Chengzhi Zhang, Toby Jia-Jun Li
    - 🏛️ Institutions: ICML 2023 Workshop on AI and HCI
    - 📅 Date: October 24, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [UI grammar], [UI layout generation]
    - 📖 TLDR: This position paper explores the use of Large Language Models (LLMs) for generating mobile user interface (UI) layouts. It introduces *UI grammar*, a novel approach to represent the hierarchical structure of UI screens, aiming to guide LLMs' generative capabilities more effectively and enhance the explainability and controllability of the process. Initial experiments with GPT-4 demonstrate the potential of LLMs to produce high-quality UIs through in-context learning, with the grammar-based approach improving certain aspects of generation quality.

- [Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V](https://arxiv.org/abs/2310.11441)
    - Jianwei Yang, Hao Zhang, Feng Li, Xueyan Zou, Chunyuan Li, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research
    - 📅 Date: October 17, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [visual prompting], [framework], [benchmark], [visual grounding], [zero-shot]
    - 📖 TLDR: This paper introduces Set-of-Mark (SoM), a novel visual prompting approach designed to enhance the visual grounding capabilities of multimodal models like GPT-4V. By overlaying images with spatially and semantically distinct marks, SoM enables fine-grained object recognition and interaction within visual data, surpassing conventional zero-shot segmentation methods in accuracy. The framework is validated on tasks requiring detailed spatial reasoning, demonstrating a significant improvement over existing visual-language models without fine-tuning.

- [OpenAgents: An Open Platform for Language Agents in the Wild](https://openreview.net/forum?id=sKATR2O1Y0)
    - Tianbao Xie, Fan Zhou, Zhoujun Cheng, Peng Shi, Luoxuan Weng, Yitao Liu, Toh Jing Hua, Junning Zhao, Qian Liu, Che Liu, Zeyu Liu, Yiheng Xu, Hongjin Su, Dongchan Shin, Caiming Xiong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Sea AI Lab, Salesforce Research
    - 📅 Date: October 16, 2023
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [data analysis], [API tools], [web agent], [OpenAgents]
    - 📖 TLDR: This paper introduces OpenAgents, an open-source platform designed to facilitate the use and hosting of language agents in real-world scenarios. It features three agents: Data Agent for data analysis using Python and SQL, Plugins Agent with access to over 200 daily API tools, and Web Agent for autonomous web browsing. OpenAgents aims to provide a user-friendly web interface for general users and a seamless deployment experience for developers and researchers, promoting the development and evaluation of innovative language agents in practical applications.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia
    - 📅 Date: October 7, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [reinforcement learning], [UI task automation], [instruction grounding]
    - 📖 TLDR: This paper introduces a multimodal model, termed RUIG (Reinforced UI Instruction Grounding), for automating UI tasks through natural language instructions. By leveraging a pixel-to-sequence approach, the model directly decodes UI element locations from screenshots based on user commands, removing the need for metadata like element coordinates. The framework uses a transformer-based encoder-decoder setup optimized through reinforcement learning to improve spatial accuracy. This novel approach outperforms prior methods, offering a generalized solution for UI task automation.

- [SteP: Stacked LLM Policies for Web Actions](https://openreview.net/forum?id=5fg0VtRxgi)
    - Paloma Sodhi, S.R.K. Branavan, Yoav Artzi, Ryan McDonald
    - 🏛️ Institutions: ASAPP Research, Cornell University
    - 📅 Date: October 5, 2023
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [policy composition], [dynamic control], [step]
    - 📖 TLDR: This paper introduces **SteP (Stacked LLM Policies)**, a framework that dynamically composes policies to tackle diverse web tasks. By defining a Markov Decision Process where the state is a stack of policies, SteP enables adaptive control that adjusts to task complexity. Evaluations on WebArena, MiniWoB++, and a CRM simulator demonstrate that SteP significantly outperforms existing methods, achieving a success rate improvement from 14.9% to 35.8% over state-of-the-art GPT-4 policies.

- [You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/abs/2309.11436)
    - Zhuosheng Zhang, Aston Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: September 20, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [multimodal agent], [chain-of-action technique]
    - 📖 TLDR: This paper presents Auto-GUI, a multimodal agent capable of directly interacting with graphical user interfaces without relying on environment parsing or application-specific APIs. The authors introduce a novel chain-of-action technique that leverages previous action histories and future action plans to improve decision-making. Auto-GUI is evaluated on a new device-control benchmark, AITW, demonstrating state-of-the-art performance in action prediction and task completion across various applications and web-based tasks.

- [LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/abs/2309.08172)
    - Kaixin Ma, Hongming Zhang, Hongwei Wang, Xiaoman Pan, Dong Yu
    - 🏛️ Institutions: Tencent AI Lab
    - 📅 Date: September 15, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [state-space exploration], [backtracking]
    - 📖 TLDR: This paper introduces LASER, an LLM agent that models interactive web navigation tasks as state-space exploration. The approach defines a set of high-level states and associated actions, allowing the agent to transition between states and backtrack from errors. LASER significantly outperforms previous methods on the WebShop task without using in-context examples, demonstrating improved handling of novel situations and mistakes during task execution.

- [AutoDroid: LLM-powered Task Automation in Android](https://doi.org/10.1145/3636534.3649379)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - 🏛️ Institutions: Tsinghua University, Shanghai AI Laboratory, University of Notre Dame, Microsoft Research
    - 📅 Date: August 29, 2023
    - 📑 Publisher: MobiCom 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [Android task automation], [LLM-powered agent]
    - 📖 TLDR: This paper introduces AutoDroid, a novel mobile task automation system capable of handling arbitrary tasks on any Android application without manual efforts. The framework combines the commonsense knowledge of LLMs with domain-specific knowledge of apps through automated dynamic analysis. AutoDroid features a functionality-aware UI representation method, exploration-based memory injection techniques, and a multi-granularity query optimization module. Evaluated on a new benchmark with 158 common tasks, AutoDroid achieves a 90.9% action generation accuracy and a 71.3% task completion rate, significantly outperforming GPT-4-powered baselines.

- [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://openreview.net/forum?id=xgtXkyqw1f)
    - Zehui Chen, Kuikun Liu, Qiuchen Wang, Jiangning Liu, Wenwei Zhang, Kai Chen, Feng Zhao
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory
    - 📅 Date: July 29, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [information seeking], [planning], [AI search], [MindSearch]
    - 📖 TLDR: This paper presents MindSearch, a novel approach to web information seeking and integration that mimics human cognitive processes. The system uses a multi-agent framework consisting of a WebPlanner and WebSearcher. The WebPlanner models multi-step information seeking as a dynamic graph construction process, decomposing complex queries into sub-questions. The WebSearcher performs hierarchical information retrieval for each sub-question. MindSearch demonstrates significant improvements in response quality and depth compared to existing AI search solutions, processing information from over 300 web pages in just 3 minutes.

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: July 26, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [multi-tab navigation], [web-based interaction], [agent simulation]
    - 📖 TLDR: *WebArena* provides a standalone, realistic web simulation environment where autonomous agents can perform complex web-based tasks. The platform offers functionalities such as multi-tab browsing, element interaction, and customized user profiles. Its benchmark suite contains 812 tasks grounded in high-level natural language commands. WebArena uses multi-modal observations, including HTML and accessibility tree views, supporting advanced tasks that require contextual understanding across diverse web pages, making it suitable for evaluating generalist agents in real-world web environments.

- [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://proceedings.neurips.cc/paper_files/paper/2023/hash/bbbb6308b402fe909c39dd29950c32e0-Abstract-Datasets_and_Benchmarks.html)
    - Christopher Rawles, Alice Li, Daniel Rodriguez, Oriana Riva, Timothy Lillicrap
    - 🏛️ Institutions: Google Research, Google DeepMind
    - 📅 Date: July 19, 2023
    - 📑 Publisher: NeurIPS 2023 Datasets and Benchmarks Track
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [device control], [natural language interaction], [gesture-based actions]
    - 📖 TLDR: The *Android in the Wild (AitW)* dataset introduces a significant benchmark for Android device control, encompassing over 715,000 human-labeled episodes with natural language commands and corresponding UI actions. Collected from Android devices across versions 10-13, it captures complex multi-step tasks requiring both visual and contextual understanding. The dataset is structured to test the robustness of device-control systems under varying conditions, such as new tasks or applications, and includes data to evaluate gesture-based interactions, providing a unique foundation for mobile interface automation and task execution research.

- [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://openreview.net/forum?id=9JQtrumvg8)
    - Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust
    - 🏛️ Institutions: Google DeepMind, The University of Tokyo
    - 📅 Date: July 2023
    - 📑 Publisher: ICLR 2024 (Oral)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [program synthesis], [HTML comprehension], [web automation], [self-supervised learning]
    - 📖 TLDR: WebAgent leverages two LLMs—HTML-T5 for HTML comprehension and Flan-U-PaLM for program synthesis—to complete web automation tasks. It combines planning, HTML summarization, and code generation to navigate and interact with real-world web environments, improving success rates on HTML-based tasks and achieving state-of-the-art performance in benchmarks like MiniWoB and Mind2Web. The modular architecture adapts well to open-domain tasks, using local-global attention mechanisms to manage long HTML contexts.

- [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://openreview.net/forum?id=Pc8AU1aF5e)
    - Longtao Zheng, Rundong Wang, Xinrun Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, Skywork AI
    - 📅 Date: June 13, 2023
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [trajectory prompting], [state abstraction], [memory retrieval]
    - 📖 TLDR: Synapse introduces a novel framework for computer control tasks, leveraging trajectory-as-exemplar prompting and memory to enhance LLM performance in complex, multi-step computer tasks. The system combines state abstraction, trajectory-based prompts, and memory retrieval, overcoming LLM limitations by filtering task-irrelevant data, storing exemplar trajectories, and retrieving relevant instances for improved decision-making. Synapse achieves significant performance gains on benchmarks such as MiniWoB++ and Mind2Web, demonstrating enhanced task success rates and generalization across diverse web-based tasks.

- [Mind2Web: Towards a Generalist Agent for the Web](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5950bf290a1570ea401bf98882128160-Abstract-Datasets_and_Benchmarks.html)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: June 9, 2023
    - 📑 Publisher: NeurIPS 2023 Datasets and Benchmarks Track
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [model], [Mind2Web], [MindAct]
    - 📖 TLDR: *Mind2Web* presents a dataset and benchmark specifically crafted for generalist web agents capable of performing language-guided tasks across varied websites. Featuring over 2,000 tasks from 137 sites, it spans 31 domains and emphasizes open-ended, realistic tasks in authentic, unsimplified web settings. The study proposes the *MindAct* framework, which optimizes LLMs for handling complex HTML elements by using small LMs to rank elements before full processing, thereby enhancing the efficiency and versatility of web agents in diverse contexts.

- [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0ff30c4bf31db0119a6219e0d250e037-Abstract-Conference.html)
    - Hongxin Li, Jingran Su, Yuntao Chen, Qing Li, Zhaoxiang Zhang
    - 🏛️ Institutions: University of Chinese Academy of Sciences, Hong Kong Institute of Science and Innovation, Chinese Academy of Sciences, The Hong Kong Polytechnic University, Shanghai AI Laboratory
    - 📅 Date: May 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [spreadsheet automation], [natural language interface]
    - 📖 TLDR: This paper introduces SheetCopilot, an innovative system that leverages large language models to automate spreadsheet tasks through natural language interactions. The framework includes a novel prompt design for task decomposition and execution, and a feedback loop for error correction. SheetCopilot demonstrates significant improvements in task completion rates and efficiency across various spreadsheet operations, outperforming existing methods and showing potential for enhancing productivity in spreadsheet software.

- [Mobile-Env: Building Qualified Evaluation Benchmarks for LLM-GUI Interaction](https://arxiv.org/abs/2305.08144)
    - Danyang Zhang, Zhennan Shen, Rui Xie, Situo Zhang, Tianbao Xie, Zihan Zhao, Siyuan Chen, Lu Chen, Hongshen Xu, Ruisheng Cao, Kai Yu
    - 🏛️ Institutions: Shanghai Jiao Tong University, The University of Hong Kong
    - 📅 Date: May 14, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [interaction platform], [multistep interaction], [InfoUI]
    - 📖 TLDR: This paper introduces *Mobile-Env*, a novel interaction platform and benchmark aimed at assessing large language models' (LLMs) capabilities in interactive environments. It builds on the InfoUI task set, derived from WikiHow, to create structured text-based challenges that simulate real-world mobile interactions. The platform is designed to support task expansions from the community, aiming to drive advancements in LLM-based interactive agents.

- [Language Models can Solve Computer Tasks](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7cc1005ec73cfbaac9fa21192b622507-Abstract-Conference.html)
    - Geunwoo Kim, Pierre Baldi, Stephen McAleer
    - 🏛️ Institutions: University of California, Irvine, Carnegie Mellon University
    - 📅 Date: March 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [recursive critique and improve], [RCI], [MiniWoB++], [general computer tasks]
    - 📖 TLDR: This study demonstrates that large language models (LLMs) can effectively automate computer tasks using a Recursive Critique and Improve (RCI) prompting method, enabling agents to handle complex desktop tasks like email and file management. By combining RCI with existing Chain of Thought (CoT) prompting, the method outperforms prior LLM approaches and traditional supervised and reinforcement learning models on the **MiniWoB++** benchmark, showing potential for broad computer task automation.

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)
    - Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
    - 🏛️ Institutions: Northeastern University, Massachusetts Institute of Technology, Princeton University
    - 📅 Date: March 20, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [learning], [verbal reinforcement learning], [reflexion]
    - 📖 TLDR: This paper introduces *Reflexion*, a framework that enhances language agents by enabling them to reflect on task feedback linguistically, storing these reflections in an episodic memory to improve decision-making in future trials. Reflexion allows agents to learn from various feedback types without traditional weight updates, achieving significant performance improvements across tasks like decision-making, coding, and reasoning. For instance, Reflexion attains a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4's 80%.

- [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://proceedings.mlr.press/v202/lee23g.html)
    - Kenton Lee, Mandar Joshi, Iulia Raluca Turc, Hexiang Hu, Fangyu Liu, Julian Martin Eisenschlos, Urvashi Khandelwal, Peter Shaw, Ming-Wei Chang, Kristina Toutanova
    - 🏛️ Institutions: Google
    - 📅 Date: February 1, 2023
    - 📑 Publisher: ICML 2023
    - 💻 Env: [Web]
    - 🔑 Key: [model], [framework], [vision encoder], [visual language understanding], [screenshot parsing], [image-to-text]
    - 📖 TLDR: This paper introduces Pix2Struct, a model pre-trained to parse masked screenshots into simplified HTML for tasks requiring visual language understanding. By leveraging the structure of HTML and diverse web page elements, Pix2Struct captures pretraining signals like OCR and image captioning, achieving state-of-the-art performance across tasks in domains including documents, user interfaces, and illustrations.

- [WebUI: A Dataset for Enhancing Visual UI Understanding with Web Semantics](https://dl.acm.org/doi/10.1145/3544548.3581158)
    - Jason Wu, Siyan Wang, Siman Shen, Yi-Hao Peng, Jeffrey Nichols, Jeffrey P. Bigham
    - 🏛️ Institutions: Carnegie Mellon University, Wellesley College, Grinnell College, Snooty Bird LLC
    - 📅 Date: January 30, 2023
    - 📑 Publisher: CHI 2023
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [element detection], [screen classification], [screen similarity], [UI modeling]
    - 📖 TLDR: The WebUI dataset includes 400,000 web UIs captured to enhance UI modeling by integrating visual UI metadata. This dataset supports tasks such as element detection, screen classification, and screen similarity, especially for accessibility, app automation, and testing applications. Through transfer learning and semi-supervised methods, WebUI addresses the challenge of training robust models with limited labeled mobile data, proving effective in tasks beyond web contexts, such as mobile UIs.

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://openreview.net/forum?id=WE_vluYUL-X)
    - Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
    - 🏛️ Institutions: Princeton University, Google Research
    - 📅 Date: October 6, 2022
    - 📑 Publisher: ICLR 2023
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [reasoning], [ReAct]
    - 📖 TLDR: This paper introduces *ReAct*, a framework that enables large language models to generate reasoning traces and task-specific actions in an interleaved manner. By combining reasoning and acting, ReAct enhances the model's ability to perform complex tasks in language understanding and interactive decision making. The approach is validated across various benchmarks, demonstrating improved performance and interpretability over existing methods.

- [Spotlight: Mobile UI Understanding using Vision-Language Models with a Focus](https://proceedings.iclr.cc/paper_files/paper/2023/hash/0f4145fde6f5ae66745ef2a16bd1a7cd-Abstract-Conference.html)
    - Gang Li, Yang Li
    - 🏛️ Institutions: Google Research
    - 📅 Date: September 29, 2022
    - 📑 Publisher: ICLR 2023 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [mobile UI tasks], [region-based focus]
    - 📖 TLDR: This paper introduces "Spotlight," a vision-language model for mobile UI understanding that operates solely on visual inputs (screenshots) and a specified focus region on the screen. By leveraging a large-scale dataset and training strategies tailored to mobile interfaces, Spotlight performs multiple UI-related tasks, including widget captioning, screen summarization, command grounding, and tappability prediction. It utilizes a vision-only approach, avoiding reliance on view hierarchies to achieve greater robustness and scalability across different mobile UI environments.

- [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://proceedings.neurips.cc/paper_files/paper/2022/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html)
    - Shunyu Yao, Howard Chen, John Yang, Karthik Narasimhan
    - 🏛️ Institutions: Princeton University
    - 📅 Date: July 2022
    - 📑 Publisher: NeurIPS 2022
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [e-commerce web interaction], [language grounding]
    - 📖 TLDR: This paper introduces **WebShop**, a simulated web-based shopping environment with over 1 million real-world products and 12,087 annotated instructions. It allows language agents to navigate, search, and make purchases based on natural language commands. The study explores how agents handle compositional instructions and noisy web data, providing a robust environment for reinforcement learning and imitation learning. The best models show effective sim-to-real transfer on websites like Amazon, illustrating WebShop’s potential for training grounded agents.

- [META-GUI: Towards Multi-modal Conversational Agents on Mobile GUI](https://aclanthology.org/2022.emnlp-main.449/)
    - Liangtai Sun, Xingyu Chen, Lu Chen, Tianle Dai, Zichen Zhu, Kai Yu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: May 23, 2022
    - 📑 Publisher: EMNLP 2022
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [task-oriented dialogue], [GUI-based interaction], [multi-modal agent]
    - 📖 TLDR: This paper presents META-GUI, a dataset and framework for training multi-modal conversational agents capable of interacting directly with mobile app interfaces without the need for backend APIs. META-GUI includes over 1,100 dialogues with annotated action sequences on various tasks such as booking and scheduling. The authors propose a GUI-based task-oriented dialogue system that allows agents to navigate mobile interfaces via direct GUI actions, with performance shown to improve in multi-modal task-oriented dialogue contexts.

- [A Data-Driven Approach for Learning to Control Computers](https://proceedings.mlr.press/v162/humphreys22a.html)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - 🏛️ Institutions: DeepMind
    - 📅 Date: February 16, 2022
    - 📑 Publisher: ICML 2022
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [computer control], [reinforcement learning], [behavioral cloning], [MiniWoB++]
    - 📖 TLDR: This study presents a reinforcement learning-based approach to train agents for computer control tasks, using keyboard and mouse interactions guided by natural language. By leveraging human demonstration data, agents trained in this environment achieved strong cross-task generalization across the MiniWob++ benchmark. This framework demonstrates how agents can control computers as humans would, enabling enhanced performance in complex computer tasks with high transferability.

- [A Dataset for Interactive Vision-Language Navigation with Unknown Command Feasibility](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/5327_ECCV_2022_paper.php)
    - Andrea Burns, Deniz Arsan, Sanjna Agrawal, Ranjitha Kumar, Kate Saenko, Bryan A. Plummer
    - 🏛️ Institutions: Boston University, University of Illinois Urbana-Champaign, MIT-IBM Watson AI Lab
    - 📅 Date: February 4, 2022
    - 📑 Publisher: ECCV 2022
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [feasibility prediction], [vision-language navigation], [mobile interaction]
    - 📖 TLDR: This paper introduces the *Mobile App Tasks with Iterative Feedback (MoTIF)* dataset, which addresses vision-language navigation (VLN) with a focus on task feasibility uncertainty in mobile applications. MoTIF provides commands paired with mobile actions and feasibility annotations, allowing researchers to examine the impact of command feasibility on task completion. The dataset includes 125 apps and emphasizes diverse app environments, action sequences, and follow-up questions to improve task ambiguity resolution, making it a valuable resource for feasibility prediction research.

- [Screen2Words: Automatic Mobile UI Summarization with Multimodal Learning](https://dl.acm.org/doi/10.1145/3472749.3474765)
    - Bryan Wang, Gang Li, Xin Zhou, Zhourong Chen, Tovi Grossman, Yang Li
    - 🏛️ Institutions: University of Toronto
    - 📅 Date: August 6, 2021
    - 📑 Publisher: UIST 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [mobile UI summarization], [multimodal learning], [Screen2Words]
    - 📖 TLDR: The paper introduces *Screen2Words*, an approach that utilizes multimodal learning to generate descriptive language summaries for mobile UI screens, combining textual, visual, and structural data from screens. The study created a large-scale dataset with 112,085 annotated screen summaries for 22,417 unique UIs, aiming to support model training for mobile UI understanding. The dataset facilitates a Transformer-based model trained to summarize screens by highlighting main functionalities, and the approach is validated with benchmarks in the mobile environment.

- [UIBert: Learning Generic Multimodal Representations for UI Understanding](https://www.ijcai.org/proceedings/2021/235)
    - Chongyang Bai, Xiaoxue Zang, Ying Xu, Srinivas Sunkara, Abhinav Rastogi, Jindong Chen, Blaise Agüera y Arcas
    - 🏛️ Institutions: Google Research
    - 📅 Date: July 29, 2021
    - 📑 Publisher: IJCAI 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [pretraining], [multimodal representation learning], [UI understanding], [UIBert]
    - 📖 TLDR: This paper presents *UIBert*, a multimodal model aimed at understanding user interfaces (UIs) by combining visual, textual, and structural metadata. UIBert is designed for tasks such as component retrieval and expression resolution, using a transformer-based joint image-text model. The authors introduce five novel pre-training tasks to leverage UI-specific features, enhancing accessibility and task completion in mobile applications. UIBert demonstrates superior performance on nine downstream UI tasks, highlighting the potential of multimodal pre-training in UI understanding.

- [AndroidEnv: A Reinforcement Learning Platform for Android](https://arxiv.org/abs/2105.13231)
    - Daniel Toyama, Philippe Hamel, Anita Gergely, Gheorghe Comanici, Amelia Glaese, Zafarali Ahmed, Tyler Jackson, Shibl Mourad, Doina Precup
    - 🏛️ Institutions: DeepMind
    - 📅 Date: May 27, 2021
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [Android interface], [RL environment], [task flexibility], [touchscreen action space]
    - 📖 TLDR: AndroidEnv provides a reinforcement learning (RL) platform for Android that lets RL agents interact with a realistic Android simulation via touchscreen events. The platform supports diverse applications, enabling agents to interact with over 100 predefined tasks across a variety of apps. With hybrid continuous and discrete action spaces, AndroidEnv is well-suited for training agents in complex, real-world Android scenarios where actions must be contextually sequenced, such as in UI navigation, gaming, and productivity apps. This environment encourages further RL research by offering task flexibility and realistic Android emulation.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://aclanthology.org/2021.naacl-main.80/)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - 🏛️ Institutions: Stanford University, Samsung Research
    - 📅 Date: March 30, 2021
    - 📑 Publisher: NAACL 2021
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [grounding], [task automation], [open-domain instructions], [RUSS]
    - 📖 TLDR: This paper introduces RUSS (Rapid Universal Support Service), a framework designed to interpret and execute open-domain, step-by-step web instructions automatically. RUSS uses a BERT-LSTM model for semantic parsing into a custom language, ThingTalk, which allows the system to map language to actions across various web elements. The framework, including a dataset of instructions, facilitates agent-based web support task automation by grounding natural language to interactive commands.

- [WebSRC: A Dataset for Web-Based Structural Reading Comprehension](https://aclanthology.org/2021.emnlp-main.343/)
    - Xingyu Chen, Zihan Zhao, Lu Chen, Jiabao Ji, Danyang Zhang, Ao Luo, Yuxuan Xiong, Kai Yu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: January 23, 2021
    - 📑 Publisher: EMNLP 2021
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [structural reading comprehension], [web page QA], [structural information], [HTML element alignment]
    - 📖 TLDR: This paper introduces **WebSRC**, a dataset specifically designed for web-based structural reading comprehension, which requires understanding not only textual content but also the structural layout of web pages. WebSRC consists of 0.44 million question-answer pairs derived from 6,500 complex web pages. Each question challenges models to identify answers from HTML structures or to respond with yes/no, requiring a nuanced grasp of HTML and layout features. The authors benchmark several models on this dataset, highlighting its difficulty and the critical role of structural comprehension in improving machine understanding of web content.

- [Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements](https://aclanthology.org/2020.emnlp-main.443/)
    - Yang Li, Gang Li, Luheng He, Jingjie Zheng, Hong Li, Zhiwei Guan
    - 🏛️ Institutions: Google Research, Georgia Institute of Technology
    - 📅 Date: November 2020
    - 📑 Publisher: EMNLP 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [model], [accessibility], [natural language generation], [WidgetCaption]
    - 📖 TLDR: This paper introduces the task of *widget captioning*, which aims to automatically generate natural language descriptions for UI elements in mobile apps to enhance accessibility. Using both visual and structural data from UI components, the study presents a novel dataset of 162,859 captions across 61,285 UI elements. Multiple deep learning models were tested on this dataset, with findings suggesting the potential for improving screen reader usability for visually impaired users by generating descriptive captions of UI elements.

- [Interactive Task Learning from GUI-Grounded Natural Language Instructions and Demonstrations](https://aclanthology.org/2020.acl-demos.25/)
    - Toby Jia-Jun Li, Tom Mitchell, Brad Myers
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: July 2020
    - 📑 Publisher: ACL 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [SUGILITE], [programming-by-demonstration]
    - 📖 TLDR: This paper introduces *Sugilite*, an intelligent task automation agent that learns new tasks and associated concepts interactively from users' natural language instructions and demonstrations on third-party mobile app GUIs. The system allows users to teach procedures and concepts through verbal instructions combined with GUI demonstrations, supports intent clarification for demonstrated actions, infers task parameters using hierarchical app GUI structures, and generalizes taught concepts across different contexts and domains. A prototype is presented as a conversational assistant on Android.

- [Mapping Natural Language Instructions to Mobile UI Action Sequences](https://aclanthology.org/2020.acl-main.729)
    - Yang Li, Jiacong He, Xin Zhou, Yuan Zhang, Jason Baldridge
    - 🏛️ Institutions: Google Research
    - 📅 Date: July 2020
    - 📑 Publisher: ACL 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile UI automation], [natural language instructions], [action grounding], [RicoSCA]
    - 📖 TLDR: This paper introduces a method for grounding natural language instructions to mobile UI actions, aiming to automate mobile task execution through user interface manipulation. It introduces three key datasets: **PixelHelp** for task instruction-performance mappings on a Pixel emulator, **AndroidHowTo** for detailed phrase extraction, and **RicoSCA** for synthetic UI command training. The system utilizes a Transformer model to extract action phrase tuples, aligning them to UI elements with contextual screen positioning. Achieving over 70% accuracy in task completion, this approach is foundational for natural language-driven mobile UI automation.

- [PUMICE: A Multi-Modal Agent that Learns Concepts and Conditionals from Natural Language and Demonstrations](https://dl.acm.org/doi/10.1145/3332165.3347899)
    - Toby Jia-Jun Li, Marissa Radensky, Justin Jia, Kirielle Singarajah, Tom M. Mitchell, Brad A. Myers
    - 🏛️ Institutions: Carnegie Mellon University, Amherst College
    - 📅 Date: August 30, 2019
    - 📑 Publisher: UIST 2019
    - 💻 Env: [Mobile]
    - 🔑 Key: [programming-by-demonstration], [PUMICE]
    - 📖 TLDR: This paper introduces *PUMICE*, a multi-modal agent that combines natural language programming and programming-by-demonstration to enable end users to instruct intelligent agents in performing new tasks. By allowing users to describe tasks and conditions naturally and then collaboratively resolving ambiguities through conversation and demonstration, PUMICE facilitates the teaching of new concepts and procedures within existing mobile app GUIs. A lab study with 10 users demonstrated its usability and effectiveness.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://openreview.net/forum?id=ryTp3f-0-)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Stanford University
    - 📅 Date: February 24, 2018
    - 📑 Publisher: ICLR 2018 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [web tasks], [workflow-guided exploration]
    - 📖 TLDR: This paper presents a novel RL approach using *workflow-guided exploration* to efficiently train agents on web-based tasks, where actions are restricted based on demonstrated workflows to streamline learning. Evaluated on MiniWoB and MiniWoB++ benchmarks, the method significantly outperforms traditional RL techniques in sparse reward settings by structuring exploration according to high-level action constraints.

- [Rico: A Mobile App Dataset for Building Data-Driven Design Applications](https://dl.acm.org/doi/10.1145/3126594.3126651)
    - Biplab Deka, Zifeng Huang, Chad Franzen, Joshua Hibschman, Daniel Afergan, Yang Li, Jeffrey Nichols, Ranjitha Kumar
    - 🏛️ Institutions: Google, University of Illinois Urbana-Champaign
    - 📅 Date: October 20, 2017
    - 📑 Publisher: UIST 2017
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [mobile UI], [UI design analysis], [interaction mining], [RICO]
    - 📖 TLDR: This paper introduces *Rico*, a large-scale dataset comprising UI screens and view hierarchies from over 9,000 Android apps, designed to aid in understanding mobile app design. Rico supports a variety of tasks, including UI design analysis and interaction mining, by providing labeled UI components, screenshots, and interaction traces.

- [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html)
    - Tianlin Shi, Andrej Karpathy, Linxi Fan, Jonathan Hernandez, Percy Liang
    - 🏛️ Institutions: Stanford University, OpenAI
    - 📅 Date: August 2017
    - 📑 Publisher: ICML 2017
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [open-domain]
    - 📖 TLDR: This paper introduces *World of Bits (WoB)*, a platform enabling agents to perform complex web-based tasks using low-level keyboard and mouse actions, addressing the lack of open-domain realism in existing reinforcement learning environments. WoB leverages a novel framework where crowdworkers create tasks with structured rewards and reproducibility by caching web interactions, forming a stable training environment. The authors validate WoB by training agents via behavioral cloning and reinforcement learning to accomplish various real-world tasks, showcasing its potential as an effective platform for reinforcement learning on web tasks.

- [SUGILITE: Creating Multimodal Smartphone Automation by Demonstration](https://dl.acm.org/doi/abs/10.1145/3025453.3025483)
    - Toby Jia-Jun Li, Amos Azaria, Brad A. Myers
    - 🏛️ Institutions: Carnegie Mellon University, Ariel University
    - 📅 Date: May 6, 2017
    - 📑 Publisher: CHI 2017
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [PBD], [multimodal interaction], [SUGILITE], [programming-by-demonstration], [demonstration]
    - 📖 TLDR: This paper introduces *SUGILITE*, a programming-by-demonstration (PBD) system that enables users to automate tasks on smartphones through multimodal interactions. By leveraging Android's accessibility API, SUGILITE allows users to create generalized automation scripts for arbitrary third-party apps by demonstrating tasks using the regular app UI. The system combines verbal instructions, user demonstrations, and app UI hierarchies to generalize scripts from single demonstrations, facilitating task variations and parameterization. Extensive error handling and context checking enhance robustness against app UI changes. A lab study indicates that users with minimal programming knowledge can successfully automate smartphone tasks using SUGILITE.

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, and Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [model context protocol], [MCP], [OSWorld], [LiteCUA]
    - 📖 TLDR: Introduces AIOS 1.0, which contextualizes desktop computer states via an MCP server so LLM-powered agents can better understand and operate GUIs. Built on top, LiteCUA—a lightweight agent—achieves 14.66 % success on the OSWorld benchmark, outperforming several heavier agent frameworks, showing the benefits of environment contextualization.
- [GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks](https://arxiv.org/abs/2603.25864)
    - Saelyne Yang, Jaesang Yu, Yi-Hao Peng, Kevin Qinghong Lin, Jae Won Cho
    - 🏛️ Institutions: KAIST, Carnegie Mellon University, University of Oxford, Konkuk University, Google
    - 📅 Date: March 26, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [GUI agent], [user intent detection], [behavior understanding], [multimodal models], [desktop]
    - 📖 TLDR: GUIDE is a benchmark evaluating AI models on perceiving user behavior, inferring intent, and providing assistance during open-ended GUI tasks, comprising 67.5 hours of screen recordings from 120 novice users across 10 software applications, revealing that current multimodal models struggle but benefit significantly from structured user context.

- [UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience](https://arxiv.org/abs/2603.24533)
    - Zichuan Lin, Feiyu Liu, Yijun Yang, Jiafei Lyu, Yiming Gao
    - 🏛️ Institutions: Tencent
    - 📅 Date: March 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [reinforcement learning], [mobile GUI agent], [self-evolving], [AndroidWorld]
    - 📖 TLDR: UI-Voyager is a two-stage self-evolving mobile GUI agent that uses Rejection Fine-Tuning (RFT) for autonomous data-model co-evolution and Group Relative Self-Distillation (GRSD) to construct dense step-level supervision from successful trajectories at fork points, enabling a 4B model to achieve 81.0% Pass@1 on AndroidWorld, surpassing human-level performance without manual annotation.

- [Towards Automated Crowdsourced Testing via Personified-LLM](https://arxiv.org/abs/2603.24160)
    - Shengcheng Yu, Yuchen Ling, Chunrong Fang, Zhenyu Chen, Chunyang Chen
    - 🏛️ Institutions: Nanjing University, Technical University of Munich
    - 📅 Date: March 25, 2026
    - 📑 Publisher: FSE 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [LLM agent], [GUI testing], [crowdsourced testing], [persona], [Android], [software engineering]
    - 📖 TLDR: PersonaTester is a personified-LLM-based framework that automates crowdsourced GUI testing by injecting diverse personas (testing mindset, exploration strategy, interaction habit) into LLM agents, enabling simulation of human-like testing behaviors that discover more crashes and bugs than non-persona baselines.

- [CAPTCHA Solving for Native GUI Agents: Automated Reasoning-Action Data Generation and Self-Corrective Training](https://arxiv.org/abs/2603.23559)
    - Yuxi Chen, Haoyu Zhai, Chenkai Wang, Rui Yang, Lingming Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign
    - 📅 Date: March 23, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [CAPTCHA], [VLM], [self-correction], [data generation], [reasoning]
    - 📖 TLDR: ReCAP is a CAPTCHA-capable native GUI agent that uses automated reasoning-action data generation and self-corrective training to improve CAPTCHA-solving success from ~30% to ~80% across seven challenge types, while maintaining strong performance on general GUI agent benchmarks.

- [AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents](https://arxiv.org/abs/2603.23007)
    - Yutao Luo, Haotian Zhu, Shuchao Pang, Zhigang Lu, Tian Dong
    - 🏛️ Institutions: Nanjing University of Science and Technology, Macquarie University, Western Sydney University, University of Hong Kong, CSIRO's Data61
    - 📅 Date: March 24, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile agent], [backdoor attack], [security], [contrastive learning], [multimodal LLM]
    - 📖 TLDR: AgentRAE introduces a novel backdoor attack against screenshot-based mobile GUI agents that uses visually natural notification icons as triggers, employing a two-stage pipeline (contrastive learning followed by poisoning training) to achieve over 90% attack success rate across ten mobile operations while evading eight state-of-the-art defenses.

- [Seed1.8 Model Card: Towards Generalized Real-World Agency](https://arxiv.org/abs/2603.20633)
    - Bytedance Seed
    - 🏛️ Institutions: Bytedance
    - 📅 Date: March 21, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model]
    - 📖 TLDR: A foundation model for generalized real-world agency supporting multi-turn interaction, tool use, code generation, and GUI interaction with latency-aware inference options.

- [ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents](https://arxiv.org/abs/2603.20340)
    - Zijian Lu, Yiping Zuo, Yupeng Nie, Xin He, Weibei Fan
    - 🏛️ Institutions: Nanjing University of Posts and Telecommunications
    - 📅 Date: March 20, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [GUI agent], [web agent], [skill learning], [program repair], [verification], [cross-model transfer]
    - 📖 TLDR: ContractSkill converts draft agent skills into contracted executable artifacts with explicit preconditions, postconditions, and recovery rules, enabling deterministic verification, step-level fault localization, and minimal patch-based repair that significantly improves skill success rates on VisualWebArena and MiniWoB and supports cross-model skill transfer.

- [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191)
    - Zehao Li, Zhenyu Wu, Yibo Zhao, Bowen Yang, Jingjing Xie
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory, CUHK MMLab, The Hong Kong University of Science and Technology, National University of Singapore
    - 📅 Date: March 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reward model], [reinforcement learning], [benchmark], [multi-agent framework], [evaluation]
    - 📖 TLDR: OS-Themis is a scalable multi-agent critic framework for GUI reward modeling that decomposes agent trajectories into verifiable milestones and employs a review mechanism to audit evidence chains, achieving significant improvements in online RL training (10.3%) and self-training filtering (6.9%) on AndroidWorld; it also introduces OmniGUIRewardBench (OGRBench), a holistic cross-platform benchmark for GUI outcome rewards.

- [AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents](https://arxiv.org/abs/2603.18429)
    - Yibo Shi, Jungang Li, Linghao Zhang, Zihao Dongfang, Biao Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Hong Kong University of Science and Technology (Guangzhou), Hong Kong University of Science and Technology, City University of Hong Kong, University of Technology Sydney, Tianjin University, Fudan University, Shandong University, Chinese Academy of Sciences, Sun Yat-sen University, Northwestern Polytechnical University
    - 📅 Date: March 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [Android], [benchmark], [agent memory], [long-horizon task], [framework], [dataset]
    - 📖 TLDR: AndroTMem introduces a diagnostic framework and benchmark (1,069 tasks, avg. 32.1 steps) for evaluating interaction memory in long-horizon Android GUI agents, and proposes Anchored State Memory (ASM), which represents trajectories as causally linked intermediate-state anchors, consistently improving task completion rates by 5%-30% over full-replay and summary baselines across 12 GUI agents.

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

- [Adaptive Vision-Language Model Routing for Computer Use Agents](https://arxiv.org/abs/2603.12823)
    - Yingyao Zhou, Zhouheng Sun, Yang Liu, Junlu Tang, Jian Xie
    - 🏛️ Institutions: vLLM Semantic Router Project, MBZUAI, McGill University, AMD, Red Hat
    - 📅 Date: March 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [VLM], [model routing], [cost efficiency], [computer use agent], [benchmark]
    - 📖 TLDR: Proposes Adaptive VLM Routing (AVR), a lightweight semantic routing framework for Computer Use Agents that dynamically selects among a pool of vision-language models based on action difficulty and confidence, reducing inference costs by up to 78% while maintaining accuracy within 2 percentage points of an all-large-model baseline.

- [MM-CondChain: A Programmatically Verified Benchmark for Visually Grounded Deep Compositional Reasoning](https://arxiv.org/abs/2603.12266)
    - Zhouheng Sun, Yingyao Zhou, Yang Liu, Junlu Tang, Jian Xie
    - 🏛️ Institutions: Alibaba Group, Zhejiang University
    - 📅 Date: March 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [multimodal LLM], [compositional reasoning], [visual grounding], [GUI], [evaluation]
    - 📖 TLDR: MM-CondChain is a benchmark for evaluating visually grounded deep compositional reasoning in multimodal LLMs, featuring multi-layer conditional chains across natural images, charts, and GUI trajectories, where even the best model achieves only 53.33 Path F1, revealing that deeply chained compositional reasoning remains a fundamental challenge.

- [HATS: Hardness-Aware Trajectory Synthesis for GUI Agents](https://arxiv.org/abs/2603.12138)
    - Yiyuan Li, Mingyuan Guo, Zhouheng Sun, Yang Liu, Junlu Tang
    - 🏛️ Institutions: Harbin Institute of Technology Shenzhen, National University of Singapore, CNRS@CREATE, Shenzhen Loop Area Institute, Huawei Noah's Ark Lab
    - 📅 Date: March 12, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [model], [learning], [mobile agent], [web agent]
    - 📖 TLDR: HATS is a hardness-aware trajectory synthesis framework for GUI agents that addresses semantic ambiguity in training data through hardness-driven Monte Carlo Tree Search exploration and alignment-guided refinement, outperforming baselines like OS-Genesis by 100%+ on AndroidWorld and WebArena benchmarks.

- [Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291)
    - Meng Fang, Zhouheng Sun, Yang Liu, Junlu Tang, Jian Xie
    - 🏛️ Institutions: University of California San Diego, Abel.ai
    - 📅 Date: March 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [memory], [graph-based retrieval], [vision-language model], [web agent], [benchmark]
    - 📖 TLDR: HyMEM is a graph-based hybrid memory system for GUI agents that couples discrete symbolic nodes with continuous trajectory embeddings, supporting multi-hop retrieval and self-evolution; it boosts open-source 7B/8B VLMs by up to +22.5%, matching or surpassing closed-source models like GPT-4o and Gemini-2.5-Pro on WebVoyager, Mind2Web, and MMInA benchmarks.

- [SpecOps: A Fully Automated AI Agent Testing Framework in Real-World GUI Environments](https://arxiv.org/abs/2603.10268)
    - Juhao Li, Zhouheng Sun, Yang Liu, Junlu Tang, Jian Xie
    - 🏛️ Institutions: Purdue University, University of Texas at San Antonio
    - 📅 Date: March 10, 2026
    - 📑 Publisher: ICSE 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [framework], [web agent], [desktop agent], [testing], [LLM]
    - 📖 TLDR: SpecOps is a fully automated testing framework that evaluates GUI-based AI agents in real-world environments by decomposing the testing process into four LLM-based specialist phases (test case generation, environment setup, execution, and validation), identifying 164 true bugs across five diverse real-world agents with an F1 score of 0.89.

- [OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/abs/2603.10165)
    - Ziming Liu, Ang Lv, Junhao Chen, Jiahao Wu, Chenxu Wang
    - 🏛️ Institutions: University of Chicago, Princeton University, Peking University
    - 📅 Date: March 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI agent], [computer use], [SWE agent], [tool use]
    - 📖 TLDR: OpenClaw-RL is a fully asynchronous RL framework that leverages next-state signals (user replies, tool outputs, terminal/GUI state changes) to train personal and general agents from live interactions, supporting scalable RL across terminal, GUI, SWE, and tool-call settings through process reward models and hindsight-guided on-policy distillation.

- [AgentOS: From Application Silos to a Natural Language-Driven Data Ecosystem](https://arxiv.org/abs/2603.08938)
    - Ziming Liu, Ang Lv, Junhao Chen, Jiahao Wu, Chenxu Wang
    - 🏛️ Institutions: University of Kansas, Clemson University, Arizona State University, Duke University
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [agent framework], [operating system], [natural language interface], [knowledge discovery], [LLM agent], [multi-agent]
    - 📖 TLDR: Proposes AgentOS, a Personal Agent Operating System paradigm where traditional GUI desktops are replaced by a natural language-driven interface with an Agent Kernel that interprets user intent, decomposes tasks, and coordinates multiple agents, framing the realization of such a system as a Knowledge Discovery and Data Mining (KDD) problem involving intent mining, workflow automation, and personal knowledge graphs.

- [SecAgent: Efficient Mobile GUI Agent with Semantic Context](https://arxiv.org/abs/2603.08533)
    - Yanyang Li, Kaizhe Hu, Guohao Li, Heyang Gong, Yeye He
    - 🏛️ Institutions: Alibaba Group
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile], [efficiency], [dataset], [benchmark], [reinforcement learning]
    - 📖 TLDR: SecAgent is a 3B-scale mobile GUI agent that introduces a semantic context mechanism to distill history screenshots into concise natural language summaries, reducing computational costs while preserving task-relevant information. It also contributes a large-scale human-verified Chinese mobile GUI dataset (18k grounding samples, 121k navigation steps) and benchmark, achieving performance comparable to 7B-8B models through supervised and reinforcement fine-tuning.

- [SlowBA: An efficiency backdoor attack towards VLM-based GUI agents](https://arxiv.org/abs/2603.08316)
    - Junjie He, Zhizheng Zhang, Haoyu Chen, Sitao Huang, Xuyang Ye
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [attack], [VLM], [backdoor attack], [reinforcement learning], [security]
    - 📖 TLDR: SlowBA is a novel backdoor attack targeting the response efficiency of VLM-based GUI agents by inducing excessively long reasoning chains when triggered by realistic pop-up windows, using a two-stage reward-level backdoor injection strategy with reinforcement learning that significantly increases latency while preserving task accuracy.

- [PIRA-Bench: A Transition from Reactive GUI Agents to GUI-based Proactive Intent Recommendation Agents](https://arxiv.org/abs/2603.08013)
    - Zihao Wu, Zihan Ding, Fan Zhou, Hao Shi, Xiaomin Zhang
    - 🏛️ Institutions: The Chinese University of Hong Kong (MMLab @ CUHK), Nankai University, Huawei Research
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [proactive agent], [GUI agent], [intent recommendation], [mobile], [multimodal LLM]
    - 📖 TLDR: PIRA-Bench introduces a benchmark for evaluating proactive GUI agents that anticipate user intentions from continuous visual inputs (screenshots) without explicit instructions, featuring complex trajectories with interleaved intents and noisy segments, along with a memory-aware baseline framework (PIRF) for managing multiple task threads.

- [OSExpert: Computer-Use Agents Learning Professional Skills via Exploration](https://arxiv.org/abs/2603.07978)
    - Zihao Wu, Zihan Ding, Fan Zhou, Hao Shi, Xiaomin Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, Stevens Institute of Technology
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [computer use agent], [GUI agent], [exploration], [skill learning], [benchmark], [inference-time scaling]
    - 📖 TLDR: OSExpert introduces a GUI-based depth-first search exploration algorithm that enables computer-use agents to autonomously learn professional skills (unit functions, composite tasks, and action primitives) from software environments, achieving ~20% performance gain on their new OSExpert-Eval benchmark and closing the efficiency gap to human experts by ~80%.

- [Generalization in Online Reinforcement Learning for Mobile Agents](https://arxiv.org/abs/2603.07432)
    - Mingkai Deng, Jing Yu, Zhou Yu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Mila, Concordia University, Universite de Montreal, University of Toronto, McMaster University
    - 📅 Date: March 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile agent], [reinforcement learning], [benchmark], [generalization], [Android]
    - 📖 TLDR: Introduces AndroidWorld-Generalization, a benchmark for evaluating zero-shot generalization of GUI-based mobile agents across unseen task instances, templates, and applications, and proposes an open-source RL training system using GRPO that shows RL outperforms supervised fine-tuning but reveals significant challenges in generalizing to unseen templates and apps.

- [WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces](https://arxiv.org/abs/2603.05295)
    - Xiao Liu, Ziyang Luo, Jiawei Liu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Fudan University, IMean AI
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [dataset], [benchmark], [grounding], [training data], [multimodal]
    - 📖 TLDR: WebChain is the largest open-source dataset of 31,725 human-annotated web interaction trajectories (318k steps) on real-world websites, featuring triple-aligned visual, structural, and action data. Leveraging this dataset, the authors propose a Dual Mid-Training recipe that decouples spatial grounding from planning, achieving state-of-the-art performance on their WebChainBench and other public GUI benchmarks.

- [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)
    - Xiao Liu, Ziyang Luo, Jiawei Liu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Fudan University, IMean AI, The Chinese University of Hong Kong, Tsinghua University
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [reinforcement learning], [GUI agent], [synthetic data], [environment synthesis], [knowledge distillation]
    - 📖 TLDR: WebFactory introduces a fully automated closed-loop reinforcement learning pipeline that compresses LLM-encoded internet knowledge into grounded GUI web agents through scalable environment synthesis, knowledge-aware task generation, and decomposed reward RL training, achieving performance comparable to agents trained on human-annotated data while using synthetic data from only 10 websites.

- [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.14663)
    - Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu, Zihan Ding
    - 🏛️ Institutions: Unknown
    - 📅 Date: February 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework]
    - 📖 TLDR: A native GUI agent training approach using action-aware supervision and partially verifiable RL to improve reasoning and long-horizon navigation performance.

- [ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.14433)
    - Zihao Wu, Zihan Ding, Fan Zhou, Hao Shi, Xiaomin Zhang
    - 🏛️ Institutions: Unknown
    - 📅 Date: February 24, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework]
    - 📖 TLDR: Proposes state machine memory to enable programmatic GUI agents that go beyond step-by-step reactive decisions, supporting structured control flow and memory.

- [WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.13338)
    - Hao Shi, Zhou Yu, Zihan Ding, Fan Zhou, Xiaomin Zhang
    - 🏛️ Institutions: Unknown
    - 📅 Date: February 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset]
    - 📖 TLDR: The first large-scale open-source world model series for web agent training, addressing bottlenecks in collecting real-world trajectories.

- [Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization](https://arxiv.org/abs/2602.13653)
    - Yibo Wang, Guangda Huzhang, Yuwei Hu, Yixuan Liu, Deng Cai
    - 🏛️ Institutions: Nanjing University, Alibaba Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reinforcement learning], [q-value estimation], [policy optimization], [MLLM], [web navigation]
    - 📖 TLDR: This paper proposes a framework for autonomous GUI navigation consisting of agentic-Q estimation (a Q-model that evaluates step-wise action contributions to task completion) and step-wise policy optimization (RL training decoupled from the environment), which enables Ovis2.5-9B to achieve strong performance on GUI navigation and grounding benchmarks, surpassing larger-scale models.

- [OpAgent: Operator Agent for Web Navigation](https://arxiv.org/abs/2602.13559)
    - Yuyu Guo, Wenjie Yang, Siyuan Yang, Wenyi Hong, Zehai He
    - 🏛️ Institutions: Ant Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [reinforcement learning], [vision-language model], [agentic framework], [WebArena], [GUI navigation]
    - 📖 TLDR: OpAgent proposes a modular agentic framework (Planner, Grounder, Reflector, Summarizer) combined with online reinforcement learning on unconstrained web environments and hierarchical multi-task fine-tuning, achieving a new state-of-the-art 71.6% success rate on WebArena.

- [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430)
    - Renjun Xu, Yang Yan
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [LLM agent], [agent skills], [CUA], [GUI grounding], [benchmark]
    - 📖 TLDR: A comprehensive survey of the agent skills landscape for LLMs, organized along four axes: architectural foundations (SKILL.md, MCP), skill acquisition (RL, autonomous discovery), deployment at scale (CUA stack, GUI grounding, OSWorld/SWE-bench), and security (skill trust governance framework).

- [Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2602.11858)
    - Lai Wei, Liangbo He, Jun Lan, Zhuohao Yu, Kangdi Wang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Ant Group, Zhongguancun Academy, Shanghai Innovation Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [MLLM], [knowledge distillation], [fine-grained perception], [benchmark], [GUI agent], [training data generation]
    - 📖 TLDR: Proposes Region-to-Image Distillation that internalizes inference-time "zoom-in" behavior into a single forward pass by using teacher models on cropped regions to generate training data, and introduces ZoomBench for evaluating fine-grained perception, achieving strong results on fine-grained perception and GUI agent benchmarks.

- [WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements](https://arxiv.org/abs/2602.11724)
    - Xiwen Teoh, Yun Lin, Duc-Minh Nguyen, Lei Xu, David S. Rosenbluth
    - 🏛️ Institutions: National University of Singapore, Shanghai Jiao Tong University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web testing], [LLM agent], [bug detection], [GUI grounding], [test oracle], [software engineering]
    - 📖 TLDR: WebTestPilot is an LLM-based agent for end-to-end web testing that symbolizes GUI elements and infers pre/post-conditions from natural language specifications as test oracles, achieving 96% precision and 96% recall in bug detection on a benchmark of bug-injected web apps, significantly outperforming existing baselines.

- [Adaptive Milestone Reward for GUI Agents](https://arxiv.org/abs/2602.11524)
    - Congmin Zheng, Xiaoyun Mo, Xinbei Ma, Aimin Guo, Hongling Zhuo
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [reinforcement learning], [reward shaping], [mobile agent], [credit assignment], [AndroidWorld]
    - 📖 TLDR: ADMIRE (Adaptive Milestone Reward) addresses the reward sparsity vs. reward hacking trade-off in RL-based GUI agent training by dynamically distilling milestones from successful trajectories and applying asymmetric credit assignment, achieving over 10% absolute improvement in success rate on AndroidWorld and generalizing across RL algorithms and diverse environments including web navigation and embodied tasks.

- [How Smart Is Your GUI Agent? A Framework for the Future of Software Interaction](https://arxiv.org/abs/2602.11514)
    - Sidong Feng, Chunyang Chen
    - 🏛️ Institutions: The Chinese University of Hong Kong (Shenzhen), Technical University of Munich
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [autonomy levels], [framework], [benchmark], [trustworthy AI], [survey]
    - 📖 TLDR: This paper proposes GUI Agent Autonomy Levels (GAL), a six-level framework inspired by SAE driving automation levels, to classify GUI agents by their degree of autonomy and provide conceptual clarity for benchmarking progress toward trustworthy software interaction.

- [Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System](https://arxiv.org/abs/2602.10915)
    - Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Tao Yu, Kun Zhang
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile agent], [agent security], [prompt injection], [access control], [operating system], [benchmark]
    - 📖 TLDR: This paper conducts a systematic security analysis of GUI-based mobile agents (using Doubao Mobile Assistant as a case study), identifying vulnerabilities across identity, perception, cognition, and execution dimensions, and proposes Aura, an Agent Universal Runtime Architecture that replaces GUI scraping with a structured intent-driven interaction model secured by cryptographic identity, semantic firewalls, taint-aware memory, and granular access control, achieving 94.3% task success rate while reducing attack success rate to 4.4% on MobileSafetyBench.

- [See, Plan, Snap: Evaluating Multimodal GUI Agents in Scratch](https://arxiv.org/abs/2602.10814)
    - Xingyi Zhang, Yulei Ye, Kaifeng Huang, Hao Liu, Gang Yin
    - 🏛️ Institutions: East China Normal University, Tongji University
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [GUI agent], [scratch], [drag-and-drop], [multimodal agent], [evaluation]
    - 📖 TLDR: Introduces ScratchWorld, a benchmark for evaluating multimodal GUI agents on program-by-construction tasks in Scratch's block-based programming environment, revealing a substantial reasoning-acting gap where models achieve over 78% success with high-level APIs but drop to ~14% with fine-grained drag-and-drop GUI manipulation.

- [Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible](https://arxiv.org/abs/2602.10139)
    - Lepeng Zhao, Zhenhua Zou, Shuo Li, Xiaoming Li, Bangfei Tian
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: February 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [privacy], [mobile agent], [Android], [benchmark], [framework], [safety]
    - 📖 TLDR: Proposes an anonymization-based privacy protection framework for mobile GUI agents that replaces sensitive PII with type-preserving placeholders, enabling task execution without exposing raw personal data to cloud-based models, and demonstrates strong privacy-utility trade-offs on the AndroidLab and PrivScreen benchmarks.

- [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856)
    - Yuhao Zheng, Li'an Zhong, Yi Wang, Ge Li, Zhi Jin
    - 🏛️ Institutions: University of Science and Technology of China, Alibaba Group, Sun Yat-sen University, University of Oxford
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [world model], [code generation], [reinforcement learning], [Android], [VLM]
    - 📖 TLDR: Code2World is a vision-language coder that predicts next GUI states by generating renderable HTML code, trained on a new 80K screen-action pair dataset (AndroidCode) with render-aware reinforcement learning. It achieves state-of-the-art next UI prediction rivaling GPT-5 and boosts downstream navigation success rates by up to +9.5% on AndroidWorld.

- [UI-Venus-1.5 Technical Report](https://arxiv.org/abs/2602.09082)
    - Venus Team, Changlong Gao, Zhangxuan Gu, Yingying Zhou, Yang Liu
    - 🏛️ Institutions: Ant Group
    - 📅 Date: February 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reinforcement learning], [model merging], [mobile navigation], [web navigation], [grounding]
    - 📖 TLDR: UI-Venus-1.5 is a unified end-to-end GUI agent family (2B/8B/30B-A3B) that combines mid-training on 10B tokens, online reinforcement learning with full-trajectory rollouts, and model merging to achieve state-of-the-art performance on GUI grounding and navigation benchmarks including ScreenSpot-Pro (69.6%), VenusBench-GD (75.0%), and AndroidWorld (77.6%).

- [Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense](https://arxiv.org/abs/2602.09012)
    - Jiacheng Liu, Yaxin Luo, Jiacheng Cui, Zhaoyi Li, Xiaohan Zhao
    - 🏛️ Institutions: Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), University College London
    - 📅 Date: February 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agent security], [GUI agent], [web agent], [CAPTCHA], [multimodal agent]
    - 📖 TLDR: Introduces Next-Gen CAPTCHAs, a scalable defense framework that exploits the persistent cognitive gap between humans and GUI-enabled agents in interactive perception, memory, and decision-making, re-establishing robust human-machine differentiation as advanced reasoning models have rendered traditional CAPTCHAs obsolete.

- [ANCHOR: Branch-Point Data Generation for GUI Agents](https://arxiv.org/abs/2602.07153)
    - Jinbiao Wei, Yilun Zhao, Kangqi Ni, Haotian Zhao, Chen Qian
    - 🏛️ Institutions: Yale University, University of North Carolina at Chapel Hill
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [GUI agent], [data generation], [trajectory expansion], [desktop automation], [training data], [benchmark]
    - 📖 TLDR: ANCHOR is a trajectory expansion framework that generates diverse, high-quality GUI interaction data by identifying branch points in seed demonstrations and proposing new state-grounded task variants, with verification and denoising to ensure quality. Models fine-tuned on the expanded data show consistent improvements on OSWorld and WindowsAgentArena benchmarks over zero-shot and synthesis baselines.

- [Where Not to Learn: Prior-Aligned Training with Subset-based Attribution Constraints for Reliable Decision-Making](https://arxiv.org/abs/2602.07008)
    - Ruoyu Chen, Shangquan Sun, Xiaoqing Guo, Chen Lin, Ziwei Liu
    - 🏛️ Institutions: Chinese Academy of Sciences, University of Chinese Academy of Sciences, Nanyang Technological University, Hong Kong Baptist University, Communication University of China, Huawei, University of Science and Technology of China, Sun Yat-sen University
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [training], [attribution], [explainability], [MLLM], [reliability]
    - 📖 TLDR: This paper proposes an attribution-based human prior alignment training method that uses subset-selection-based attribution to penalize models for relying on off-prior evidence, and validates it on both image classification and MLLM-based GUI agent click decision tasks, consistently improving task accuracy and decision reasonability.

- [Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion](https://arxiv.org/abs/2602.06351)
    - Longhui Ma, Di Zhao, Siwei Wang, Yingce Xia, Ting Liu
    - 🏛️ Institutions: National University of Defense Technology, Academy of Military Sciences
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [multimodal fusion], [attention mechanism], [training-free], [OCR], [MLLM]
    - 📖 TLDR: Trifuse is a training-free GUI grounding framework that fuses attention maps from MLLMs with OCR-derived textual cues and icon-level caption semantics via a Consensus-SinglePeak fusion strategy, achieving strong performance on four grounding benchmarks without task-specific fine-tuning.

- [SVRepair: Structured Visual Reasoning for Automated Program Repair](https://arxiv.org/abs/2602.06090)
    - Xiaoxuan Tang, Jincheng Wang, Liwei Luo, Rui Jiang, Zhi Jin
    - 🏛️ Institutions: Ant Group, Zhejiang University
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI understanding], [multimodal LLM], [program repair], [scene graph], [visual reasoning], [coding agent]
    - 📖 TLDR: SVRepair is a multimodal automated program repair framework that fine-tunes a vision-language model to convert GUI visual artifacts (screenshots, control-flow graphs) into structured semantic scene graphs, enabling a coding agent to localize faults and synthesize patches with state-of-the-art results on SWE-Bench M, MMCode, and CodeVision benchmarks.

- [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Shun Zhang, Yiming Liu
    - 🏛️ Institutions: Zhejiang University, Nankai University, The Chinese University of Hong Kong, Shanghai Jiao Tong University, vivo AI Lab
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [memory], [evaluation], [mobile GUI agent], [framework]
    - 📖 TLDR: MemGUI-Bench is a comprehensive memory-centric benchmark for mobile GUI agents featuring 128 tasks across 26 applications where 89.8% require memory through cross-temporal and cross-spatial retention, along with MemGUI-Eval, a progressive scrutiny evaluation pipeline with 7 hierarchical metrics. Evaluation of 11 state-of-the-art agents reveals significant memory deficits with 4-10x capability gaps hidden by standard benchmarks, identifying 5 distinct failure modes and design implications.

- [M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining](https://arxiv.org/abs/2602.05429)
    - Rui Lv, Juncheng Mo, Tianyi Chu, Yiming Liu, Hongling Zhuo
    - 🏛️ Institutions: Ant Group, Zhejiang University
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile GUI agent], [data mining], [monte carlo tree search], [multi-agent framework], [trajectory annotation], [training data]
    - 📖 TLDR: M2-Miner is an automated mobile GUI agent data-mining framework that uses Monte Carlo Tree Search enhanced by a collaborative multi-agent system (InferAgent, OrchestraAgent, JudgeAgent) to efficiently generate high-quality intent-trajectory training data, along with intent recycling and progressive model-in-the-loop training strategies. GUI agents fine-tuned on the mined data achieve state-of-the-art performance on multiple mobile GUI benchmarks.

- [LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios](https://arxiv.org/abs/2602.03255)
    - Tianyu Chen, Chujia Hu, Ge Gao, Ruofeng Yu, Yao Lu
    - 🏛️ Institutions: ShanghaiTech University, Shanghai Artificial Intelligence Laboratory, Rice University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer use agent], [MCP], [long-horizon planning], [LLM agent]
    - 📖 TLDR: LPS-Bench is a benchmark evaluating the planning-time safety awareness of MCP-based computer-use agents under long-horizon tasks, covering 65 scenarios across 7 task domains and 9 risk types with both benign and adversarial interactions, revealing substantial safety deficiencies in existing agents.

- [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995)
    - Sizhe Tang, Rongqian Chen, Tian Lan, Rui Chen, Ze-Feng Gao
    - 🏛️ Institutions: George Washington University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [test-time compute], [tree search], [MCTS], [benchmark], [OSWorld]
    - 📖 TLDR: Agent Alpha is a unified framework that applies step-level Monte Carlo Tree Search (MCTS) with alpha-UCT guided exploration, comparison-driven evaluation, and diversity-constrained expansion to GUI/computer-use agents, achieving a state-of-the-art ~77% success rate on the OSWorld benchmark while significantly outperforming trajectory-level sampling baselines under equivalent compute.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548)
    - Xiaoce Wang, Guibin Zhang, Junzhe Li, Fang Li, Chen Zhang
    - 🏛️ Institutions: Tsinghua University, National University of Singapore, Peking University, Shenzhen MSU-BIT University, Guangming Laboratory
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [tool use], [tokenization], [curriculum learning], [visual grounding], [data efficiency]
    - 📖 TLDR: ToolTok introduces a tool tokenization paradigm for GUI agents that models operations as multi-step pathfinding through learnable tool tokens with semantic anchoring and curriculum learning, achieving competitive performance with models 50x larger while using less than 1% of the training data required by other post-training approaches.

- [Generative Visual Code Mobile World Models](https://arxiv.org/abs/2602.01576)
    - Woosung Koh, Sungjun Han, Segyu Lee, Oh-Hyun Kwon, Hyunsoo Kim
    - 🏛️ Institutions: Trillion Labs, KAIST AI
    - 📅 Date: February 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [world model], [mobile], [code generation], [VLM], [benchmark]
    - 📖 TLDR: gWorld proposes visual world modeling for mobile GUIs via renderable code generation, where a single VLM predicts the next GUI state as executable web code rather than generating pixels directly, achieving state-of-the-art accuracy on multiple benchmarks while being over 50x smaller than competing models.

- [Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction](https://arxiv.org/abs/2602.00575)
    - Chaoqun Cui, Jing Huang, Shijing Wang, Feng Chen, Fangyuan Liu
    - 🏛️ Institutions: Chinese Academy of Sciences, University of Chinese Academy of Sciences, Meituan, Beijing Jiaotong University
    - 📅 Date: January 31, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reward modeling], [verification], [reinforcement learning], [benchmark], [LLM agent]
    - 📖 TLDR: VAGEN introduces an agentic interactive verification framework that uses a verifier agent with interaction tools to proactively probe the environment for evidence of task completion, shifting from passive LLM-as-a-Judge evaluation to active exploration, and achieving significantly improved evaluation accuracy on OSWorld and AndroidWorld benchmarks.

- [Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training](https://arxiv.org/abs/2601.22781)
    - Linjia Kang, Zhimin Wang, Yongkang Zhang, Yuanchun Li, Gang Yin
    - 🏛️ Institutions: Tsinghua University, Huazhong Agricultural University, Kuaishou Technology
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile GUI agent], [data generation], [curriculum learning], [multi-agent], [VLM], [training data]
    - 📖 TLDR: MobileGen is an adaptive data generation framework for mobile GUI agent training that decouples task difficulty into structural and semantic dimensions, profiles the agent's capability frontier, and uses a multi-agent controllable generator to synthesize difficulty-aligned interaction trajectories, improving average agent performance by 1.57x over baselines across multiple benchmarks.

- [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528)
    - Hongze Mi, Yibo Feng, Wenjie Lu, Wenbin Jiang, Yasheng Wang
    - 🏛️ Institutions: Didichuxing Co. Ltd, The Chinese University of Hong Kong Shenzhen, Tianjin University, Sun Yat-sen University, Fudan University
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [memory system], [training-free], [MLLM], [multi-app], [mobile]
    - 📖 TLDR: Darwinian Memory System (DMS) is a training-free, self-evolving memory architecture for GUI agents that treats memory as a dynamic ecosystem governed by natural selection, decomposing trajectories into reusable units and pruning suboptimal paths via utility-driven selection, achieving 18.0% gains in success rate and 33.9% in execution stability on real-world multi-app benchmarks.

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

- [CovAgent: Overcoming the 30% Curse of Mobile Application Coverage with Agentic AI and Dynamic Instrumentation](https://arxiv.org/abs/2601.21253)
    - Wei Minn, Biniam Fisseha Demissie, Yan Naing Tun, Ismail Ahmadi, Quazi Marufur Rahman
    - 🏛️ Institutions: Singapore Management University, Technology Innovation Institute, Harbin Institute of Technology, University of Verona
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [Android testing], [GUI testing], [LLM agent], [code coverage], [dynamic instrumentation], [software engineering]
    - 📖 TLDR: CovAgent is an agentic AI framework that overcomes the ~30% activity coverage ceiling in Android app GUI testing by using LLM agents to analyze decompiled app code, reason about unsatisfied activation conditions, and generate dynamic instrumentation scripts, achieving over 100% improvement in activity coverage compared to state-of-the-art baselines like LLMDroid, Fastbot, and APE.

- [MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment](https://arxiv.org/abs/2601.20335)
    - Qinzhuo Wu, Zhizhuo Yang, Hanhao Li, Weifeng Lin, Shunye Tang
    - 🏛️ Institutions: Xiaomi, Peking University, Chinese University of Hong Kong
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile], [evaluation], [chinese], [online], [robustness]
    - 📖 TLDR: MobileBench-OL is an online benchmark with 1080 tasks from 80 Chinese apps that evaluates mobile GUI agents across multiple dimensions including task execution, complex reasoning, long-horizon planning, and noise robustness, with an auto-eval framework featuring a reset mechanism for stable and repeatable real-world benchmarking.

- [MAGNET: Towards Adaptive GUI Agents with Memory-Driven Knowledge Evolution](https://arxiv.org/abs/2601.19199)
    - Hui Zhang, Kangyang Luo, Haoxiang Jia, Li Zhang, Zhaohui Jiang
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute, University of Southern California
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [memory], [mobile], [Android], [knowledge transfer], [adaptation]
    - 📖 TLDR: MAGNET is a memory-driven adaptive GUI agent framework that uses dual-level memory (stationary memory for mapping visual features to functional semantics and procedural memory for capturing task intents) with a dynamic evolution mechanism, enabling robust performance on mobile GUI tasks despite UI updates and distribution shifts, as demonstrated on AndroidWorld and offline benchmarks.

- [SwipeGen: Bridging the Execution Gap in GUI Agents via Human-like Swipe Synthesis](https://arxiv.org/abs/2601.18305)
    - Zishuo Liu, Yongwen Zhu, Tao Xu, Xinyu Xu, Mingxuan Yuan
    - 🏛️ Institutions: Fudan University, Shanghai Key Laboratory of Intelligent Information Processing
    - 📅 Date: January 20, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [swipe interaction], [data synthesis], [benchmark], [action execution], [mobile]
    - 📖 TLDR: SwipeGen proposes an automated pipeline to synthesize human-like swipe gestures for GUI agents and introduces the first swipe execution benchmark, along with GUISwiper, a GUI agent that achieves 69.07% swipe execution accuracy (a 214% improvement over VLM baselines).

- [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197)
    - Jingyang Zhou, Yan Feng, Wei Chen, Cheng Zhang, Ziyang Luo
    - 🏛️ Institutions: Xiaomi
    - 📅 Date: January 20, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [test-time scaling], [critic model], [data flywheel], [training framework], [mobile]
    - 📖 TLDR: GAIA proposes a data flywheel system that trains an Intuitive Critic Model (ICM) to evaluate and filter GUI agent actions at test time, using iterative cycles of positive/negative sample collection to progressively improve critic accuracy and boost the performance of both open-source and closed-source GUI agents.

- [EntWorld: A Holistic Environment and Benchmark for Verifiable Enterprise GUI Agents](https://arxiv.org/abs/2601.17722)
    - Haotian Zhao, Yuxiang Chai, Pengxiang Zhao, Wendi Yu, Difei Gao
    - 🏛️ Institutions: Zhongguancun Laboratory, Tsinghua University
    - 📅 Date: January 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [web agent], [enterprise], [evaluation], [dataset], [GUI agent]
    - 📖 TLDR: EntWorld is a large-scale benchmark of 1,756 tasks across six enterprise domains (CRM, ITIL, ERP, etc.) with SQL-based deterministic verification, revealing that state-of-the-art models like GPT-4.1 achieve only 47.61% success rate compared to human performance, highlighting a significant enterprise gap in current GUI agent capabilities.

- [GraphPilot: GUI Task Automation with One-Step LLM Reasoning Powered by Knowledge Graph](https://arxiv.org/abs/2601.17418)
    - Pengxiang Zhao, Yuxiang Chai, Haotian Zhao, Yiyuan Liu, Shuai Ren
    - 🏛️ Institutions: Sun Yat-sen University
    - 📅 Date: January 17, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile], [knowledge graph], [LLM], [task automation], [efficiency]
    - 📖 TLDR: GraphPilot constructs app-specific knowledge graphs offline to encode page functions, element roles, and transition rules, then uses these graphs to guide LLM reasoning online so that a mobile GUI agent can plan a complete action sequence in nearly one LLM query, improving task completion rate on DroidTask while substantially reducing latency and the number of LLM calls compared to stepwise approaches.

- [The Behavioral Fabric of LLM-Powered GUI Agents: Human Values and Interaction Outcomes](https://arxiv.org/abs/2601.16356)
    - Yuki Kurasawa, Michael A. Madaio, Minsuk Chang, Namwoo Kang, Talia Ringer
    - 🏛️ Institutions: University of Notre Dame, IBM Research
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [web agent], [benchmark], [alignment], [human values], [persona], [empirical study]
    - 📖 TLDR: This paper investigates how user preferences and human values influence LLM-powered web GUI agents' reasoning and behavior, introducing an open-source testbed of 14 interactive web tasks and showing that while value-infused prompts guide agents toward value-consistent outcomes, dominant interface cues like discounts frequently override these effects, revealing a persistent value-action gap.

- [MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux](https://arxiv.org/abs/2601.13060)
    - Mingyuan Kang, Yiming Liu, Hongling Zhuo, Hongzan Sun, Jinyu Chen
    - 🏛️ Institutions: Honor
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reward model], [multi-agent system], [self-evolving], [reinforcement learning], [data construction]
    - 📖 TLDR: MagicGUI-RMS is a multi-agent reward model system that combines domain-specific and general-purpose reward models to enable adaptive trajectory evaluation, corrective feedback, and self-evolving learning for GUI agents through an automated data-reflux mechanism, achieving substantial gains in task accuracy and behavioral robustness.

- [MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction](https://arxiv.org/abs/2601.12822)
    - Yinhao Jiang, Hao Ye, Juntao Ren, Zhenying He, Jian Hou
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute
    - 📅 Date: January 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [agent safety], [benchmark], [framework], [GUI agent], [security], [simulation]
    - 📖 TLDR: MirrorGuard is a plug-and-play defense framework that uses a neural-symbolic simulation pipeline to generate high-risk GUI interaction trajectories in a text-based environment, training a module to intercept and rectify insecure reasoning chains of Computer Use Agents before they execute harmful actions. On the ByteDance UI-TARS system, it reduces the unsafe rate from 66.5% to 13.0% while maintaining low false refusal rates, significantly outperforming prior defenses.

- [Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?](https://arxiv.org/abs/2601.12349)
    - Chenhao Lin, Zichen Ding, Lingming Zhang, Yuanchun Li, Xuanzhe Liu
    - 🏛️ Institutions: Nanjing University, Honor Device Co. Ltd, Institute of Dataspace Hefei Comprehensive National Science Center
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [security], [attack], [Android], [mobile], [benchmark], [LMM]
    - 📖 TLDR: This paper presents "Action Rebinding," a zero-permission attack that exploits the observation-to-action gap in LMM-powered Android GUI agents to hijack their actions, achieving 100% success on atomic rebinding across six agents and 15 tasks while evading all malware scanners, revealing a fundamental architectural flaw in current agent-OS integration.

- [Compress to Focus: Efficient Coordinate Compression for Policy Optimization in Multi-Turn GUI Agents](https://arxiv.org/abs/2601.11631)
    - Shiyu Huang, Zishuo Liu, Mingxuan Yuan, Yanzhen Chen, Hao Wen
    - 🏛️ Institutions: HiThink Research, University of California Irvine, Hangzhou Dianzi University
    - 📅 Date: January 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [policy optimization], [token compression], [visual compression], [reinforcement learning], [multi-turn agent]
    - 📖 TLDR: CCPO is a policy optimization framework for multi-turn GUI agents that uses Coordinate-Aware Spatial Compression to progressively crop screenshots to task-relevant regions across rollouts and a distance-based advantage for finer reward signals, achieving state-of-the-art grounding accuracy with up to 55% token compression and 3.8x training speedup.

- [PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://arxiv.org/abs/2601.09636)
    - Yiheng Shu, Jinyao Ye, Jianwei Yu, Jiahao Wu, Tao Xu
    - 🏛️ Institutions: Harbin Institute of Technology (Shenzhen)
    - 📅 Date: January 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [personalization], [implicit intent], [benchmark], [user preference], [proactive assistance]
    - 📖 TLDR: PersonalAlign introduces a task and benchmark (AndroidIntent) for personalizing GUI agents by aligning with users' implicit intents through long-term user records, and proposes HIM-Agent which hierarchically organizes user preferences and routines to improve both execution and proactive assistance performance by 15.7% and 7.3% over baselines including GPT-5 and UI-TARS.

- [ShowUI-Aloha: Human-Taught GUI Agent](https://arxiv.org/abs/2601.07181)
    - Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu, Zihan Ding
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: December 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [learning from demonstration], [screen recording], [data pipeline], [desktop automation], [human teaching]
    - 📖 TLDR: ShowUI-Aloha presents a pipeline that transforms unstructured, in-the-wild human screen recordings from desktop environments into structured, actionable training data for GUI agents, comprising a recorder, learner, planner, and executor that together enable agents to learn complex GUI tasks by simply observing humans.

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

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zhenlan Li, Xingkai Yu, Jiahao Xu, Xiaobu Yuan, Xiaobin Huang
    - 🏛️ Institutions: Nanjing University, Peking University, Microsoft Research Asia
    - 📅 Date: December 25, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reinforcement learning], [RLVR], [computer use agent], [OSWorld], [training]
    - 📖 TLDR: BEPA (Bi-Level Expert-to-Policy Assimilation) bridges the gap between off-policy expert trajectories and on-policy reinforcement learning for GUI agents by converting static expert traces into policy-aligned guidance via self-rolled reachable trajectories and a dynamically updated cache, improving UITARS1.5-7B success rate from 22.87% to 32.13% on OSWorld-Verified.

- [GUITester: Enabling GUI Agents for Exploratory Defect Discovery](https://arxiv.org/abs/2601.04500)
    - Yixuan Yue, Yiming Liu, Tao Xie, Yuanchun Li, Xuanzhe Liu
    - 🏛️ Institutions: Beijing Jiaotong University, Hithink Research, Nanyang Technological University
    - 📅 Date: December 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI testing], [mobile], [multi-agent], [benchmark], [defect detection], [MLLM]
    - 📖 TLDR: GUITester is a multi-agent framework that enables MLLM-based GUI agents to autonomously discover defects in mobile apps by decoupling navigation from verification through a Planning-Execution Module and a Hierarchical Reflection Module, achieving 48.90% F1-score on the newly introduced GUITestBench benchmark with 143 tasks across 26 defects.

- [InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](https://arxiv.org/abs/2601.04126)
    - Yiming Liu, Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu
    - 🏛️ Institutions: Peking University, Nanjing University, Microsoft Research Asia
    - 📅 Date: December 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [data generation], [training], [benchmark], [GUI grounding], [framework]
    - 📖 TLDR: InfiniteWeb is a system that automatically synthesizes functional, diverse web environments at scale for GUI agent training, using unified specifications, task-centric test-driven development, and reference design images; agents trained on these generated environments achieve significant improvements on OSWorld and Online-Mind2Web benchmarks.

- [Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning](https://arxiv.org/abs/2601.03641)
    - Yiming Liu, Kaizhe Hu, Yeye He, Hao Shi, Zhou Yu
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: December 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [continual learning], [parameter fusion], [catastrophic forgetting], [LLM agent], [tool-use agent]
    - 📖 TLDR: Agent-Dice is a parameter fusion framework that addresses catastrophic forgetting in LLM-based agents through geometric consensus filtering and curvature-based importance weighting, disentangling common knowledge from task-specific conflicting knowledge to enable effective continual learning for GUI and tool-use agents.

- [ShowUI-π: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965)
    - Chaoxu Tong, Hao Wen, Yuhao Zhu, Guangyu Gao, Jiaxuan Wang
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: December 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [drag interaction], [flow-based model], [continuous action], [benchmark], [desktop]
    - 📖 TLDR: ShowUI-pi is the first flow-based generative model for GUI dexterous manipulation, unifying discrete clicks and continuous drag trajectories in a single 450M-parameter model, along with ScreenDrag, a new benchmark with 20K drag trajectories across five domains (e.g., PowerPoint, Premiere Pro) that reveals proprietary agents like Operator and Gemini-2.5-CUA still struggle with drag-based GUI tasks.

- [SmartSnap: Proactive Evidence Seeking for Self-Verifying Agents](https://arxiv.org/abs/2512.22322)
    - Yuncong Zhang, Jiahao Wu, Chenxu Wang, Ziming Liu, Ang Lv
    - 🏛️ Institutions: Tencent Youtu Lab, Peking University
    - 📅 Date: December 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [framework], [mobile GUI agent], [evaluation], [model], [benchmark]
    - 📖 TLDR: SmartSnap introduces a paradigm shift from passive post-hoc task verification to proactive in-situ self-verification for GUI agents, where a Self-Verifying Agent both completes tasks and proves accomplishment through curated snapshot evidence guided by 3C Principles (Completeness, Conciseness, Creativity), achieving up to 26% performance gains on mobile tasks with 8B-30B models competitive with much larger models like DeepSeek V3.1 and Qwen3-235B.

- [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009)
    - Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu...
    - 🏛️ Institutions: Indian Institute of Technology Bombay, Indian Institute of Technology Hyderabad
    - 📅 Date: 2025-12-26
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [multimodal LLM], [slow-fast reasoning], [visual grounding], [implicit chain-of-thought], [adaptive perception]
    - 📖 TLDR: iSHIFT is a lightweight 2.5B-parameter multimodal GUI agent that integrates latent thinking (implicit chain-of-thought) with a perception control module, enabling adaptive switching between a fast mode for routine actions and a slow mode with detailed visual grounding for precision tasks, matching state-of-the-art performance on multiple GUI benchmarks despite its compact size.

- [AndroidLens: Long-latency Evaluation with Nested Sub-targets for Android GUI Agents](https://arxiv.org/abs/2512.21302)
    - Yue Cao, Yingyao Wang, Pi Bu...
    - 🏛️ Institutions: Nanjing University, Alibaba Group, Fudan University, Zhejiang University
    - 📅 Date: 2025-12-24
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [Android], [benchmark], [evaluation], [GUI testing], [mobile]
    - 📖 TLDR: AndroidLens is a challenging evaluation framework for Android GUI agents comprising 571 long-latency tasks across 38 domains in Chinese and English environments, featuring both static evaluation with multiple valid paths and dynamic milestone-based evaluation via Average Task Progress (ATP). Even the best models achieve only 12.7% task success rate and 50.47% ATP, highlighting key challenges in environmental anomalies, adaptive exploration, and long-term memory retention.

- [EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration](https://arxiv.org/abs/2512.19396)
    - Runze Li, Yuwen Zhai, Bo Xu...
    - 🏛️ Institutions: East China Normal University, Alibaba Group, Shanghai Innovation Institute
    - 📅 Date: 2025-12-22
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [memory-augmented agent], [trajectory retrieval], [Android automation], [in-context learning], [self-exploration]
    - 📖 TLDR: EchoTrail-GUI equips GUI agents with experiential memory by autonomously exploring environments to build a database of successful trajectories, then retrieving and injecting relevant past trajectories as in-context guidance for new tasks, significantly improving success rates on Android World and AndroidLab benchmarks.

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

- [Step-GUI Technical Report](https://arxiv.org/abs/2512.15431)
    - Haolong Yan, Jia Wang, Xin Huang...
    - 🏛️ Institutions: StepFun
    - 📅 Date: 2025-12-17
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [multimodal LLM], [reinforcement learning], [benchmark], [MCP], [training data]
    - 📖 TLDR: Step-GUI introduces a self-evolving training pipeline with a Calibrated Step Reward System that produces high-quality trajectory data at 10-100x lower cost, yielding 4B/8B GUI agent models achieving state-of-the-art performance (80.2% AndroidWorld, 48.5% OSWorld), along with GUI-MCP (a privacy-preserving Model Context Protocol for GUI automation) and AndroidDaily (a real-world mobile benchmark).

- [Modular and Multi-Path-Aware Offline Benchmarking for Mobile GUI Agents](https://arxiv.org/abs/2512.12634)
    - Youngmin Im, Byeongung Jo, Jaeyoung Wi...
    - 🏛️ Institutions: KAIST, Sungkyunkwan University, Korea University, Fluiz
    - 📅 Date: 2025-12-14
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile], [Android], [benchmark], [evaluation], [modular], [multi-path]
    - 📖 TLDR: MobiBench is the first modular and multi-path-aware offline benchmarking framework for mobile GUI agents that achieves 94.72% agreement with human evaluators while enabling scalable, reproducible evaluation, and provides comprehensive module-level analysis uncovering optimal configurations and actionable design guidelines for mobile agents.

- [Using GUI Agent for Electronic Design Automation](https://arxiv.org/abs/2512.11611)
    - Chunyi Li, Longfei Li, Zicheng Zhang...
    - 🏛️ Institutions: Nanyang Technological University, Shanghai AI Laboratory, Shanghai Jiao Tong University
    - 📅 Date: 2025-12-12
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [benchmark], [dataset], [desktop], [EDA], [multimodal LLM]
    - 📖 TLDR: This paper presents GUI-EDA, the first large-scale benchmark for deploying GUI agents in Electronic Design Automation workflows across 5 CAD tools and 5 physical domains, and proposes EDAgent, an EDA-specialized GUI agent with a reflection mechanism that outperforms PhD students in Electrical Engineering on industrial CAD software tasks.

- [WebSTAR: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering](https://arxiv.org/abs/2512.10962)
    - Yifei He, Pranit Chawla, Yaser Souri...
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, Microsoft
    - 📅 Date: 2025-11-22
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [GUI agent], [web agent], [data synthesis], [data filtering], [process reward model], [benchmark]
    - 📖 TLDR: WebSTAR introduces a scalable data synthesis pipeline for computer use agents that uses step-level filtering and reasoning augmentation to transform noisy rollouts from strong CUAs into reliable training data, constructing 13.3K trajectories and 267K graded steps, with the resulting 7B model surpassing UI-TARS-1.5-7B on WebVoyager by over 15% and also producing StepRM, a lightweight multimodal process reward model distilled from o4-mini.

- [AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management](https://arxiv.org/abs/2512.10371)
    - Shizuo Tian, Hao Wen, Yuxuan Chen...
    - 🏛️ Institutions: Tsinghua University, Peking University
    - 📅 Date: 2025-12-11
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile agent], [context management], [long-horizon task], [Android], [program-guided]
    - 📖 TLDR: AgentProg is a program-guided context management approach for mobile GUI agents that reframes interaction history as a program with variables and control flow, integrating a belief state mechanism inspired by Belief MDP to handle partial observability, achieving state-of-the-art success rates on AndroidWorld and extended long-horizon task benchmarks while baseline methods suffer catastrophic degradation.

- [Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning](https://arxiv.org/abs/2512.09706)
    - Kaichen He, Zihao Wang, Muyao Li...
    - 🏛️ Institutions: Peking University, National University of Singapore
    - 📅 Date: 2025-12-10
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [heterogeneous action space], [multi-turn GRPO], [Minecraft agent], [cross-level actions], [LLM agent]
    - 📖 TLDR: CrossAgent is a unified agentic model trained via supervised fine-tuning and multi-turn Group Relative Policy Optimization (GRPO) that dynamically switches between heterogeneous action spaces (APIs, GUI events, low-level commands) within a single trajectory, achieving state-of-the-art performance on 800+ Minecraft tasks by adaptively balancing high-level efficiency with low-level precision.

- [GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection](https://arxiv.org/abs/2512.09396)
    - Zishu Wei, Qixiang Ma, Xavier Hu...
    - 🏛️ Institutions: Zhejiang University, Huawei Technologies Ltd.
    - 📅 Date: 2025-12-10
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [multi-agent], [grounding], [reasoning], [reflection], [benchmark]
    - 📖 TLDR: GAIR is a multi-agent GUI automation framework that uses a general-purpose MLLM to jointly reason over information gathered by multiple GUI-specific models, with a group reflection mechanism that drives specialized models to collect more targeted information when the decision-maker determines insufficient evidence, achieving state-of-the-art results on GUI benchmarks like ScreenSpot and UI-I2E-Bench with only 7B models.

- [Single-Agent Scaling Fails Multi-Agent Intelligence: Towards Foundation Models with Native Multi-Agent Intelligence](https://arxiv.org/abs/2512.08743)
    - Shuyue Hu, Haoyang Yan, Yiqun Zhang...
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory
    - 📅 Date: 2025-12-09
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multi-agent systems], [foundation models], [LLM], [benchmark], [scaling], [survey]
    - 📖 TLDR: This paper demonstrates through extensive empirical evaluation across 41 LLMs and 7 benchmarks that scaling single-agent performance does not automatically yield robust multi-agent intelligence, and outlines key research directions for building foundation models with native multi-agent capabilities including understanding, planning, communication, and adaptation.

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

- [DrawingBench: Evaluating Spatial Reasoning and UI Interaction Capabilities of Large Language Models through Mouse-Based Drawing Tasks](https://arxiv.org/abs/2512.01174)
    - Hyunjun Kim, Sooyoung Ryu
    - 🏛️ Institutions: KAIST, Seoul National University
    - 📅 Date: 2025-12-01
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [benchmark], [spatial reasoning], [UI interaction], [LLM agent], [evaluation]
    - 📖 TLDR: DrawingBench is a verification framework that evaluates agentic LLMs' spatial reasoning and GUI interaction capabilities through mouse-based drawing tasks on a browser canvas, using 250 prompts with 8 objective criteria and multi-turn feedback, finding that specification clarity matters more than task complexity and external oversight outperforms self-correction.

- [AFRAgent : An Adaptive Feature Renormalization Based High Resolution Aware GUI agent](https://arxiv.org/abs/2512.00846)
    - Neeraj Anand, Rishabh Jain, Sohan Patnaik...
    - 🏛️ Institutions: Adobe
    - 📅 Date: 2025-11-30
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile agent], [multimodal LLM], [GUI grounding], [smartphone automation], [vision-language model]
    - 📖 TLDR: AFRAgent is a compact InstructBLIP-based multimodal architecture that uses adaptive feature renormalization to fuse high-resolution image details into low-resolution embeddings, achieving state-of-the-art smartphone GUI automation on Meta-GUI and AITW benchmarks at less than one-fourth the size of competing models.

- [MPR-GUI: Benchmarking and Enhancing Multilingual Perception and Reasoning in GUI Agents](https://arxiv.org/abs/2512.00756)
    - Ruihan Chen, Qiming Li, Xiaocheng Feng...
    - 🏛️ Institutions: Harbin Institute of Technology, Peng Cheng Laboratory
    - 📅 Date: 2025-11-30
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [multilingual], [GUI understanding], [cross-lingual], [perception and reasoning], [LVLM]
    - 📖 TLDR: MPR-GUI introduces a multilingual fine-grained benchmark (MPR-GUI-Bench) for evaluating GUI agents' perception and reasoning capabilities across languages, and proposes GUI-XLI, a cross-lingual intervention method that improves multilingual GUI agent performance by 6.5% on average by manipulating hidden states at capability-related layers.

- [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235)
    - Zehao Deng, Tianjie Ju, Zheng Wu...
    - 🏛️ Institutions: Soochow University, Shanghai Jiao Tong University
    - 📅 Date: 2025-11-27
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [multi-agent framework], [reinforcement learning], [long-horizon task planning], [state tracking], [task decomposition]
    - 📖 TLDR: This paper proposes CES, a multi-agent framework consisting of a Coordinator, Executor, and State Tracker, where high-level scheduling models are trained via execution-feedback reinforcement learning to improve long-horizon GUI automation by decoupling planning from low-level action execution.

- [D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)
    - Sen Chen, Tong Zhao, Yi Bin...
    - 🏛️ Institutions: Tongji University, Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shanghai AI Laboratory
    - 📅 Date: 2025-11-20
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [Android], [robustness], [anomaly], [dynamic evaluation], [AAAI 2026]
    - 📖 TLDR: D-GARA is a dynamic benchmarking framework that evaluates Android GUI agent robustness by injecting real-world anomalies (permission dialogs, battery warnings, update prompts, app crashes) during live task execution, revealing up to 33% performance degradation in state-of-the-art agents like UI-TARS and AgentCPM.

- [DualTAP: A Dual-Task Adversarial Protector for Mobile MLLM Agents](https://arxiv.org/abs/2511.13248)
    - Fuyao Zhang, Jiaming Zhang, Che Wang...
    - 🏛️ Institutions: Nanyang Technological University, Peking University, Xidian University, Hebei Normal University, Alibaba Group
    - 📅 Date: 2025-11-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile agent], [safety], [privacy], [adversarial attack], [dataset], [MLLM]
    - 📖 TLDR: DualTAP is a dual-task adversarial framework that protects personally identifiable information (PII) in mobile GUI agent screenshots from untrusted routers while preserving task utility, achieving a 31.6 percentage point reduction in privacy leakage with minimal impact on agent task success rate.

- [MEGA-GUI: Multi-stage Enhanced Grounding Agents for GUI Elements](https://arxiv.org/abs/2511.13087)
    - SeokJoo Kwak, Jihoon Kim, Boyoun Kim...
    - 🏛️ Institutions: Samsung SDS
    - 📅 Date: 2025-11-17
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [multi-agent framework], [vision-language model], [region-of-interest], [benchmark], [desktop]
    - 📖 TLDR: MEGA-GUI is a multi-stage framework that decomposes GUI grounding into coarse Region-of-Interest selection and fine-grained element grounding using specialized vision-language agents, achieving state-of-the-art accuracy of 73.18% on ScreenSpot-Pro and 68.63% on OSWorld-G benchmarks.

- [Yanyun-3: Enabling Cross-Platform Strategy Game Operation with Vision-Language Models](https://arxiv.org/abs/2511.12937)
    - Guoyan Wang, Yanyan Huang, Chunlin Chen...
    - 🏛️ Institutions: Nanjing University of Science and Technology, Nanjing University, Sichuan Teng dun Liangyuan Intelligent Technology Co. Ltd.
    - 📅 Date: 2025-11-17
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [VLM], [strategy game], [cross-platform], [multimodal data organization], [fine-tuning]
    - 📖 TLDR: Yanyun-3 is a VLM-based GUI agent that integrates Qwen2.5-VL and UI-TARS for cross-platform strategy game automation, proposing a "combination granularity" principle for organizing multimodal training data that achieves a 12.98x BLEU-4 improvement and 63% inference time reduction over full fusion baselines.

- [MMWOZ: Building Multimodal Agent for Task-oriented Dialogue](https://arxiv.org/abs/2511.12586)
    - Pu-Hai Yang, Heyan Huang, Heng-Da Xu...
    - 🏛️ Institutions: Anhui University, Beijing Institute of Technology
    - 📅 Date: 2025-11-16
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [GUI agent], [benchmark], [multimodal], [task-oriented dialogue], [dataset], [web navigation]
    - 📖 TLDR: MMWOZ extends the MultiWOZ dataset with web-style GUI screenshots and operation instructions, bridging the gap between traditional API-based task-oriented dialogue systems and real-world GUI-based interactions, and proposes MATE as a baseline multimodal agent for GUI-grounded dialogue.

- [Co-EPG: A Framework for Co-Evolution of Planning and Grounding in Autonomous GUI Agents](https://arxiv.org/abs/2511.10705)
    - Yuan Zhao, Hualei Zhu, Tingyu Jiang...
    - 🏛️ Institutions: Alibaba Cloud Computing, The University of Tokyo
    - 📅 Date: 2025-11-13
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [planning and grounding], [reinforcement learning], [GRPO], [co-evolution], [training framework]
    - 📖 TLDR: Co-EPG is a self-iterative training framework that co-evolves planning and grounding models for GUI agents through a positive feedback loop using GRPO and confidence-based reward ensembles, achieving state-of-the-art results on Multimodal-Mind2Web and AndroidControl benchmarks without external data.

- [TaskSense: Cognitive Chain Modeling and Difficulty Estimation for GUI Tasks](https://arxiv.org/abs/2511.09309)
    - Yiwen Yin, Zhian Hu, Xiaoxi Xu...
    - 🏛️ Institutions: Tsinghua University, University of Washington, Cornell University, University of Sydney
    - 📅 Date: 2025-11-12
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [benchmark], [cognitive modeling], [task difficulty], [evaluation], [human-AI interaction]
    - 📖 TLDR: TaskSense proposes Cognitive Chain, a framework that models GUI task difficulty from a cognitive perspective by decomposing cognitive processes preceding motor actions into structured steps with information-theoretic difficulty indices, and validates that cognitive difficulty correlates with user completion time and reveals capability gaps in state-of-the-art GUI agents.

- [ProBench: Benchmarking GUI Agents with Accurate Process Information](https://arxiv.org/abs/2511.09157)
    - Leyang Yang, Ziwei Wang, Xiaoxuan Tang...
    - 🏛️ Institutions: Zhejiang University, Ant Group
    - 📅 Date: 2025-11-12
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [mobile], [evaluation], [process-aware evaluation], [Android], [multi-step tasks]
    - 📖 TLDR: ProBench is a comprehensive mobile GUI agent benchmark with over 200 tasks that evaluates both final-state and intermediate-process information, introducing a Process Provider to automatically capture accurate process details for more precise assessment of agent performance on real-world GUI scenarios.

- [History-Aware Reasoning for GUI Agents](https://arxiv.org/abs/2511.09127)
    - Ziwei Wang, Leyang Yang, Xiaoxuan Tang...
    - 🏛️ Institutions: Zhejiang University, Ant Group
    - 📅 Date: 2025-11-12
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [reinforcement learning], [reasoning], [chain-of-thought], [mobile], [web]
    - 📖 TLDR: Proposes the History-Aware Reasoning (HAR) framework that addresses the history-agnostic reasoning weakness of native GUI agents by encouraging reflection on errors and enhancing short-term memory through reflective learning scenarios, tailored correction guidelines, and a hybrid RL reward function, resulting in a 3B-parameter model (HAR-GUI-3B) with improved episodic reasoning across GUI benchmarks including AITW, Mind2Web, and GUI-Odyssey.

- [AUTO-Explorer: Automated Data Collection for GUI Agent](https://arxiv.org/abs/2511.06417)
    - Xiangwu Guo, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: 2025-11-09
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [data collection], [benchmark], [GUI grounding], [exploration], [fine-tuning]
    - 📖 TLDR: Auto-Explorer is an automated data collection method that autonomously parses and explores GUI environments to gather training data for GUI agents, accompanied by the UIXplore benchmark for evaluating exploration quality. The collected data is used to fine-tune multimodal LLMs, demonstrating improved GUI element grounding capabilities on novel software and websites.

- [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440)
    - Xiangru Jian, Shravan Nayak, Kevin Qinghong Lin, Aarash Feizi, Kaixin Li, Patrice Bechard, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-03-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [computer-use agent], [video demonstration], [training data], [desktop automation]
    - 📖 TLDR: CUA-Suite is a large-scale ecosystem of ~10,000 human-demonstrated expert video tasks (30 fps) across 87 diverse desktop applications with dense annotations, addressing the data scarcity bottleneck that limits CUA development by providing continuous video rather than sparse screenshots.
- [WebPII: Benchmarking Visual PII Detection for Computer-Use Agents](https://arxiv.org/abs/2603.17357)
    - Nathan Zhao
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-03-18
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [computer-use agent], [privacy], [PII detection], [web agent], [safety]
    - 📖 TLDR: WebPII is a fine-grained synthetic benchmark of 44,865 annotated e-commerce UI images for visual PII detection in computer-use agents, featuring an extended PII taxonomy with transaction-level identifiers, anticipatory detection for partially-filled forms, and scalable VLM-based generation.
- [You Told Me to Do It: Measuring Instructional Text-induced Private Data Leakage in LLM Agents](https://arxiv.org/abs/2603.11862)
    - Ching-Yu Kao, Xinfeng Li, Shenyu Dai, Tianze Qiu, Pengcheng Zhou, Eric Hanchen Jiang, Philip Sperl
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-03-12
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [security], [LLM agent], [prompt injection], [privacy], [data leakage], [safety]
    - 📖 TLDR: Identifies and measures the "Trusted Executor Dilemma"—where LLM agents execute adversarial instructions embedded in documentation because they cannot distinguish malicious directives from legitimate guidance—formalizing a three-dimensional taxonomy of instructional text-induced private data leakage attacks.
- [CUAAudit: Meta-Evaluation of Vision-Language Models as Auditors of Autonomous Computer-Use Agents](https://arxiv.org/abs/2603.10577)
    - Marta Sumyk, Oleksandr Kosovan
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-03-11
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [evaluation], [computer-use agent], [VLM], [agent-as-a-judge], [benchmark]
    - 📖 TLDR: CUAAudit is a meta-evaluation framework assessing VLMs as autonomous auditors of CUA task completion directly from observable interactions, conducting large-scale evaluation of five VLMs as judges for CUA success assessment across diverse desktop environments.
- [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178)
    - Linxin Song, Jieyu Zhang, Huanxin Sheng, Taiwei Shi, Gupta Rahul, Yang Liu, Ranjay Krishna, Jian Kang, Jieyu Zhao
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-03-10
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [reward model], [computer-use agent], [video understanding], [evaluation], [training data]
    - 📖 TLDR: Introduces ExeVR-53k, a dataset of 53K video-task-reward triplets for reward modeling from agent execution video (keyframes independent of agent internals), with adversarial instruction translation for negative samples, enabling method-agnostic CUA task completion evaluation.
- [Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision](https://arxiv.org/abs/2602.14276)
    - A. Said Gurbuz, Sunghwan Hong, Ahmed Nassar, Marc Pollefeys, Peter Staar
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-02-15
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [dataset], [screen parsing], [computer-use agent], [UI understanding]
    - 📖 TLDR: ScreenParse is a large-scale dataset providing dense annotations of all visible UI elements (bounding boxes, 55-class types, and text) across 771K web screenshots (21M elements), generated by an automated pipeline to enable complete screen parsing supervision beyond sparse grounding.
- [A11y-CUA Dataset: Characterizing the Accessibility Gap in Computer Use Agents](https://arxiv.org/abs/2602.09310)
    - Ananya Gubbi Mohanbabu, Rosiana Natalie, Brandon Kim, Anhong Guo, Amy Pavel
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-02-09
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [accessibility], [dataset], [benchmark], [human-computer interaction]
    - 📖 TLDR: A11y-CUA presents the first dataset comparing 60 everyday tasks by blind/low-vision users and sighted users with 40.4 hours and 158K interaction events, revealing that CUAs mirror sighted interaction patterns and quantifying a critical accessibility gap that prevents BLVUs from collaborating with CUAs.
- [Mapping the Design Space of User Experience for Computer Use Agents](https://arxiv.org/abs/2602.07283)
    - Ruijia Cheng, Jenny T. Liang, Eldon Schoop, Jeffrey Nichols
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-02-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [UX design], [human-computer interaction], [user study], [evaluation]
    - 📖 TLDR: Maps the UX design space for computer-use agents through a two-phase study—taxonomy development from existing systems via expert interviews (n=8) and Wizard-of-Oz user studies (n=20)—producing a taxonomy of UX considerations including user prompts, explainability, user control, and mental models.
- [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725)
    - Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-02-02
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [computer-use agent], [world model], [guardrail], [long-horizon task]
    - 📖 TLDR: SafePred is a predictive guardrail for computer-using agents that aligns predicted future states from a world model against safety constraints to proactively prevent long-term risks emerging with delay, overcoming reactive guardrails that only constrain behavior within the current observation space.
- [CUA-Skill: Develop Skills for Computer Using Agent](https://arxiv.org/abs/2601.21123)
    - Tianyi Chen, Yinheng Li, Michael Solodko, Sen Wang, Nan Jiang, Tingyuan Cui, Junheng Hao, Jongwoo Ko, Sara Abdali, Leon Xu, Suzhen Zheng, Hao Fan, Pashmina Cameron, Justin Wagle, Kazuhito Koishida
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-01-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [skill abstraction], [framework], [desktop automation], [Windows]
    - 📖 TLDR: CUA-Skill is a large-scale library encoding human computer-use knowledge as parameterized skills with composition graphs, spanning common Windows applications, providing practical infrastructure and tool substrate for scalable, reliable computer-using agent development.
- [OS-Marathon: Benchmarking Computer-Use Agents on Long-Horizon Repetitive Tasks](https://arxiv.org/abs/2601.20650)
    - Jing Wu, Daphne Barretto, Yiye Chen, Nicholas Gydé, Yanan Jian, Yuhang He, Vibhav Vineet
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-01-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [long-horizon task], [desktop automation], [evaluation]
    - 📖 TLDR: OS-Marathon is a benchmark of 242 long-horizon repetitive tasks (expense processing, grade entry) for evaluating CUAs on structured recurring workflows, paired with a cost-effective few-shot condensed demonstration construction method to teach agents underlying sub-workflow logic.
- [Improving Language Agents through BREW](https://arxiv.org/abs/2511.20297)
    - Shashank Kirtania, Param Biyani, Priyanshu Gupta, Yasharth Bajpai, Roshni Iyer, Sumit Gulwani, Gustavo Soares
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [LLM agent], [memory], [experiential learning], [framework], [tool use]
    - 📖 TLDR: BREW (Bootstrapping Experientially-learned Environmental Knowledge) builds and refines structured memory from agent-environment interactions as an alternative to computationally expensive weight optimization (PPO/GRPO), enabling efficient agent optimization for structured reasoning and computer-use automation tasks.
- ["Are We Done Yet?": A Vision-Based Judge for Autonomous Task Completion of Computer Use Agents](https://arxiv.org/abs/2511.20067)
    - Marta Sumyk, Oleksandr Kosovan
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [evaluation], [computer-use agent], [VLM], [task completion], [self-correction]
    - 📖 TLDR: Presents an autonomous vision-based evaluation framework using VLMs to assess CUA task completion directly from screenshots, achieving up to 73% accuracy on 1,260 macOS tasks across 42 built-in apps and yielding an average 27% relative improvement in task success when evaluator feedback is applied.
- [AppSelectBench: Application-Level Tool Selection Benchmark](https://arxiv.org/abs/2511.19957)
    - Tianyi Chen, Michael Solodko, Sen Wang, Jongwoo Ko, Junheng Hao, Colby Banbury, Sara Abdali, Saeed Amizadeh, Qing Xiao, Yinheng Li, Tianyu Ding, Kamran Ghasedi Dizaji, Suzhen Zheng, Hao Fan, Justin Wagle, Pashmina Cameron, Kazuhito Koishida
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [tool use], [application selection], [evaluation]
    - 📖 TLDR: AppSelectBench is the first benchmark evaluating application-level tool selection in CUAs—deciding which application to use before invoking fine-grained APIs—revealing this critical capability is underserved by existing API-focused benchmarks and is necessary for correct environment initialization.
- [Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663)
    - Ahmed Awadallah, Yash Lara, Raghav Magazine, Hussein Mozannar, Akshay Nambi, Yash Pandya, Aravind Rajeswaran, Corby Rosset, Alexey Taymanov, Vibhav Vineet, Spencer Whitehead, Andrew Zhao
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-24
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [computer-use agent], [web agent], [synthetic data], [training data]
    - 📖 TLDR: Introduces FaraGen, a high-throughput synthetic data generation system for multi-step web tasks (~$1 per verified trajectory), used to train Fara-7B, a native CUA model operating purely from screenshots that achieves strong performance on multi-step web automation benchmarks.
- [UI-CUBE: Enterprise-Grade Computer Use Agent Benchmarking Beyond Task Accuracy to Operational Reliability](https://arxiv.org/abs/2511.17131)
    - Horia Cristescu, Charles Park, Trong Canh Nguyen, Sergiu Talmacel, Alexandru-Gabriel Ilie, Stefan Adam
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-21
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [enterprise], [evaluation], [reliability]
    - 📖 TLDR: UI-CUBE (UiPath Computer Use Benchmark) evaluates enterprise deployment readiness of CUAs with 226 tasks across simple UI interactions and complex workflows including copy-paste and enterprise application scenarios, exposing fundamental architectural limitations beyond task accuracy.
- [OSGym: Scalable Distributed Data Engine for Generalizable Computer Agents](https://arxiv.org/abs/2511.11672)
    - Zengyi Qin, Jinyuan Chen, Yunze Man, Shengcao Cao, Ziqi Pang, Zhuoyuan Wang, Xin Sun, Gen Lin, Han Fang, Ling Zhu, Zixin Xie, Zibu Wei, Tianshu Ran, Haoran Geng, Xander Wu, Zachary Bright, Qizhen Sun, Rui Wang, Yuyang Cai, Song Wang, Jiace Zhao, Han Cao, Yeyang Zhou, Tianrui Liu, Ray Pan
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-11
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [training environment], [computer-use agent], [dataset], [reinforcement learning], [scalability]
    - 📖 TLDR: OSGym is a scalable distributed data engine parallelizing over 1,000+ OS replicas (1,420 multi-turn trajectories/minute) for training generalizable computer agents across diverse tasks including browser interactions, software engineering, and office automation under limited academic compute.
- [GUI-360☆: A Comprehensive Dataset and Benchmark for Computer-Using Agents](https://arxiv.org/abs/2511.04307)
    - Jian Mu, Chaoyun Zhang, Chiming Ni, Lu Wang, Bo Qiao, Kartik Mathur, Qianhui Wu, Yuhang Xie, Xiaojun Ma, Mengyu Zhou, Si Qin, Liqun Li, Yu Kang, Minghua Ma, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [computer-use agent], [GUI grounding], [screen parsing]
    - 📖 TLDR: GUI-360☆ is a large-scale dataset and benchmark suite with an LLM-augmented automated pipeline for CUAs, jointly evaluating GUI grounding, screen parsing, and action prediction to address the scarcity of real-world CUA tasks and the absence of a unified multi-capability benchmark.
- [Learning from Online Videos at Inference Time for Computer-Use Agents](https://arxiv.org/abs/2511.04137)
    - Yujian Liu, Ze Wang, Hao Chen, Ximeng Sun, Xiaodong Yu, Jialian Wu, Jiang Liu, Emad Barsoum, Zicheng Liu, Shiyu Chang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [video understanding], [in-context learning], [training-free], [inference-time scaling]
    - 📖 TLDR: Proposes a training-free framework for CUAs to learn from online tutorial videos at inference time by retrieving relevant videos, converting them into structured demonstration trajectories via VLM-based action inference, and dynamically selecting trajectories as in-context guidance during execution.
- [GUI-AIMA: Aligning Intrinsic Multimodal Attention with a Context Anchor for GUI Grounding](https://arxiv.org/abs/2511.00810)
    - Shijie Zhou, Viet Dac Lai, Hao Tan, Jihyung Kil, Wanrong Zhu, Changyou Chen, Ruiyi Zhang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-11-02
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [attention mechanism], [visual grounding], [VLM], [coordinate-free]
    - 📖 TLDR: GUI-AIMA is a coordinate-free supervised fine-tuning framework for GUI grounding that aligns intrinsic multimodal attention with a context anchor, leveraging native MLLM attention maps to identify instruction-relevant visual patches and refine exact click locations—improving efficiency over direct coordinate generation.
- [OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows](https://arxiv.org/abs/2510.24411)
    - Qiushi Sun, Mukai Li, Zhoumianze Liu, Zhihui Xie, Fangzhi Xu, Zhangyue Yin, Kanzhi Cheng, Zehao Li, Zichen Ding, Qi Liu, Zhiyong Wu, Zhuosheng Zhang, Ben Kao, Lingpeng Kong
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [safety], [mobile agent], [VLM], [benchmark], [hybrid validation]
    - 📖 TLDR: OS-Sentinel is a hybrid safety validation framework for mobile GUI agents combining reactive and proactive detection, built on MobileRisk-Live—a dynamic sandbox with realistic safety-annotated trajectories—to detect unsafe operations including system compromise and privacy leakage.
- [Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents](https://arxiv.org/abs/2510.23691)
    - Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, Haoming Wang, Longxiang Liu, Shihao Liang, Junting Lu, Zhiyong Wu, Jiazhan Feng, Wanjun Zhong, Zili Li, Yu Wang, Yu Miao, Bo Zhou, Yuanfan Li, Hao Wang, Zhongkai Zhao, Faming Wu, Zhengxuan Jiang, Weihao Tan, Heyuan Yao, Shi Yan, Xiangyang Li, Yitao Liang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [computer-use agent], [game agent], [pretraining], [generalization]
    - 📖 TLDR: Game-TARS is a generalist game and computer-use agent pretrained on 500B+ tokens with a unified keyboard-mouse action space across OS, web, and simulation games, using decaying continual loss to reduce causal confusion and sparse-thinking to balance reasoning depth and inference cost.
- [Surfer 2: The Next Generation of Cross-Platform Computer Use Agents](https://arxiv.org/abs/2510.19949)
    - Mathieu Andreux, Märt Bakler, Yanael Barbier, Hamza Benchekroun, Emilien Biré, Antoine Bonnet, Riaz Bordie, Nathan Bout, Matthias Brunel, Aleix Cambray, Pierre-Louis Cedoz, Antoine Chassang, Gautier Cloix, Ethan Connelly, Alexandra Constantinou, Ramzi De Coster, Hubert de la Jonquiere, Aurélien Delfosse, Maxime Delpit, Alexis Deprez, Augustin Derupti, Mathieu Diaz, Shannon D'Souza, Julie Dujardin, Abai Edmund
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-22
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [computer-use agent], [cross-platform], [web agent], [mobile agent]
    - 📖 TLDR: Surfer 2 is a unified visual-only cross-platform agent achieving state-of-the-art across web (97.1% WebVoyager, 69.6% WebArena), desktop (60.1% OSWorld), and mobile (87.1% AndroidWorld) without task-specific fine-tuning, via hierarchical context management, decoupled planning/execution, and self-verification with adaptive recovery.
- [SusBench: An Online Benchmark for Evaluating Dark Pattern Susceptibility of Computer-Use Agents](https://arxiv.org/abs/2510.11035)
    - Longjie Guo, Chenjie Yuan, Mingyuan Zhong, Robert Wolfe, Ruican Zhong, Yue Xu, Bingbing Wen, Hua Shen, Lucy Lu Wang, Alexis Hiniker
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [computer-use agent], [web agent], [dark pattern], [safety]
    - 📖 TLDR: SusBench is an online benchmark evaluating CUA susceptibility to 9 types of UI dark patterns, featuring 313 realistic tasks across 55 consumer websites with dark patterns injected via code modifications, finding that frontier CUAs are significantly more susceptible to manipulative designs than human users.
- [Code Agent can be an End-to-end System Hacker: Benchmarking Real-world Threats of Computer-use Agent](https://arxiv.org/abs/2510.06607)
    - Weidi Luo, Qiming Zhang, Tianyu Lu, Xiaogeng Liu, Bin Hu, Hung-Chun Chiu, Siyuan Ma, Yizhe Zhang, Xusheng Xiao, Yinzhi Cao, Zhen Xiang, Chaowei Xiao
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-07
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [computer-use agent], [benchmark], [red-teaming], [attack]
    - 📖 TLDR: Benchmarks real-world security threats of computer-use agents as system hackers through a comprehensive attacker-knowledge model covering end-to-end kill chains, realistic multi-host environments with encrypted credentials, and reliable automated judgment for evaluating CUA misuse.
- [A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants](https://arxiv.org/abs/2510.06223)
    - Hans G. W. van Dam
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-08-31
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [GUI agent], [MCP], [framework], [natural language interface], [desktop automation]
    - 📖 TLDR: Proposes a GUI architecture enabling applications to interface with LLM-based speech assistants via the Model Context Protocol (MCP), exposing the application navigation graph and semantics through the MVVM ViewModel pattern for natural language-driven GUI control without redesigning existing applications.
- [Watch and Learn: Learning to Use Computers from Online Videos](https://arxiv.org/abs/2510.04673)
    - Chan Hee Song, Yiwen Song, Palash Goyal, Yu Su, Oriana Riva, Hamid Palangi, Tomas Pfister
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [training data], [video understanding], [data generation], [inverse dynamics]
    - 📖 TLDR: Watch & Learn (W&L) converts Internet computer-use videos into 53K+ executable UI trajectories by casting annotation as an inverse dynamics problem—predicting user actions from consecutive screen states—enabling scalable CUA training data collection from readily available human-recorded videos.
- [From Imperative to Declarative: Towards LLM-friendly OS Interfaces for Boosted Computer-Use Agents](https://arxiv.org/abs/2510.04607)
    - Yuan Wang, Mingyu Li, Haibo Chen
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [computer-use agent], [OS interface], [abstraction], [GUI agent]
    - 📖 TLDR: DMI (Declarative Model Interface) transforms existing GUIs into three declarative primitives—access, state, and observation—applying policy-mechanism separation where LLMs handle high-level semantic planning while DMI manages low-level GUI navigation, dramatically reducing error-prone action sequences for LLM-based CUAs.
- [Scaling Agents for Computer Use](https://arxiv.org/abs/2510.02250)
    - Gonzalo Gonzalez-Pumariega, Vincent Tu, Chih-Lun Lee, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-10-02
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [test-time scaling], [evaluation], [OSWorld], [behavior cloning]
    - 📖 TLDR: BJudge (Behavior Judge) scales CUAs over multiple rollouts by representing agent executions as behavior narratives for structured comparison and selection, achieving a new state-of-the-art on OSWorld (72.6%) that surpasses human-level performance (72.36%) and generalizes to WindowsAgentArena and AndroidWorld.
- [SCUBA: Salesforce Computer Use Benchmark](https://arxiv.org/abs/2509.26506)
    - Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-30
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [enterprise], [evaluation], [CRM]
    - 📖 TLDR: SCUBA (Salesforce Computer Use Benchmark) is an enterprise CUA benchmark with 300 tasks derived from real user interviews on Salesforce CRM workflows across three personas—administrators, sales representatives, and service agents—with Salesforce sandbox environments and milestone-based evaluation metrics.
- [Scaling Synthetic Task Generation for Agents via Exploration](https://arxiv.org/abs/2509.25047)
    - Ram Ramrakhya, Andrew Szot, Omar Attia, Yuhao Yang, Anh Nguyen, Bogdan Mazoure, Zhe Gan, Harsh Agrawal, Alexander Toshev
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-29
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [computer-use agent], [task generation], [training data], [exploration]
    - 📖 TLDR: AutoPlay is a scalable pipeline for synthetic agentic task generation that explicitly explores interactive environments to discover possible interactions, producing diverse, feasible, and verifiable tasks for post-training MLLMs as interactive agents for computer-use and web navigation.
- [Efficient Multi-turn RL for GUI Agents via Decoupled Training and Adaptive Data Curation](https://arxiv.org/abs/2509.23866)
    - Pengxiang Li, Zechen Hu, Zirui Shang, Jingrong Wu, Yang Liu, Hui Liu, Zhi Gao, Chenrui Shi, Bofei Zhang, Zihao Zhang, Xiaochuan Shi, Zedong YU, Yuwei Wu, Xinxiao Wu, Yunde Jia, Liuyu Xiang, Zhaofeng He, Qing Li
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-28
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [GUI agent], [training], [efficiency], [framework]
    - 📖 TLDR: DART (Decoupled Agentic RL Training) is a framework for efficient multi-turn RL for GUI agents that separates training into four asynchronous modules—environment cluster, rollout service, data manager, and trainer—with adaptive data curation to overcome slow GUI interaction and insufficient training data.
- [Secure and Efficient Access Control for Computer-Use Agents via Context Space](https://arxiv.org/abs/2509.22256)
    - Haochen Gong, Chenxiao Li, Rui Chang, Wenbo Shen
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-26
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [computer-use agent], [access control], [safety], [framework]
    - 📖 TLDR: CSAgent is a system-level, static policy-based access control framework for CUAs that uses "context space"—a representation of the agent operational context—to enforce fine-grained permissions and prevent LLM uncertainty from causing irreversible harmful actions.
- [AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents](https://arxiv.org/abs/2509.07764)
    - Haitao Hu, Peng Chen, Yanpeng Zhao, Yuqi Chen
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-09
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [computer-use agent], [defense], [safety], [framework]
    - 📖 TLDR: AgentSentinel is an end-to-end, real-time security defense framework for CUAs that monitors LLM-driven tool commands across all agent components to detect and prevent unintended or harmful operations arising from LLM non-determinism, spanning vulnerabilities beyond insecure user prompts.
- [MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/abs/2509.06477)
    - Pengxiang Zhao, Guangyi Liu, Yaozhen Liang, Weiqing He, Zhengxi Lu, Yuehao Huang, Yaxuan Guo, Kexin Zhang, Hao Wang, Liang Liu, Yong Liu
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-08
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [mobile agent], [GUI agent], [hybrid agent], [shortcut]
    - 📖 TLDR: MAS-Bench is the first benchmark for evaluating GUI-shortcut hybrid mobile agents, assessing both flexible GUI operations and efficient API/deep-link shortcuts on Android tasks, measuring agents ability to discover and optimally choose interaction strategies beyond predefined shortcuts.
- [Are LLM Agents the New RPA? A Comparative Study with RPA Across Enterprise Workflows](https://arxiv.org/abs/2509.04198)
    - Petr Průcha, Michaela Matoušková, Jan Strnad
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-04
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [RPA], [enterprise], [evaluation], [comparison]
    - 📖 TLDR: A comparative study between LLM-based Agentic Automation with Computer Use (AACU) and traditional Robotic Process Automation (RPA) across data entry, monitoring, and process automation workflows, evaluating whether CUAs can serve as viable alternatives to RPA in enterprise settings.
- [Throttling Web Agents Using Reasoning Gates](https://arxiv.org/abs/2509.01619)
    - Abhinav Kumar, Jaechul Roh, Ali Naseh, Amir Houmansadr, Eugene Bagdasarian
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-09-01
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [safety], [access control], [defense], [reasoning]
    - 📖 TLDR: Proposes Reasoning Gates, a framework imposing tunable computational costs on web agents before granting resource access, protecting content providers from denial-of-service, excessive scraping, and CAPTCHA bypass while preserving service availability for legitimate users.
- [CODA: Coordinating the Cerebrum and Cerebellum for a Dual-Brain Computer Use Agent with Decoupled Reinforcement Learning](https://arxiv.org/abs/2508.20096)
    - Zeyi Sun, Yuhang Cao, Jianze Liang, Qiushi Sun, Ziyu Liu, Zhixiong Zhang, Yuhang Zang, Xiaoyi Dong, Kai Chen, Dahua Lin, Jiaqi Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-08-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [computer-use agent], [reinforcement learning], [planning], [dual-system cognition]
    - 📖 TLDR: CODA (Coordinating the Cerebrum and Cerebellum) is a dual-brain framework for CUAs in specialized domains that decouples planning (cerebrum) from execution (cerebellum) and trains them jointly via decoupled reinforcement learning, enabling adaptive coordination of long-horizon planning with precise GUI execution.
- [Reliable Weak-to-Strong Monitoring of LLM Agents](https://arxiv.org/abs/2508.19461)
    - Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-08-26
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [LLM agent], [monitoring], [computer-use agent], [red-teaming]
    - 📖 TLDR: Stress-tests LLM agent monitoring systems for detecting covert misbehavior using a monitor red-teaming (MRT) workflow varying agent/monitor awareness and adversarial evasion strategies, evaluated on SHADE-Arena for tool-calling agents and CUA-SHADE-Arena for computer-use agents.
- [SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience](https://arxiv.org/abs/2508.04700)
    - Zeyi Sun, Ziyu Liu, Yuhang Zang, Yuhang Cao, Xiaoyi Dong, Tong Wu, Dahua Lin, Jiaqi Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-08-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [self-evolving], [experiential learning], [framework], [exploration]
    - 📖 TLDR: SEAgent is a self-evolving framework enabling CUAs to autonomously master novel software environments through experiential learning—exploring unfamiliar applications, accumulating task-relevant procedural knowledge, and self-refining skills—without requiring human annotations for specialized software.
- [OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://arxiv.org/abs/2508.04482)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shenzhi Wang, Xinchen Xu, Shuofei Qiao, Zhaokai Wang, Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-08-06
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [computer-use agent], [MLLM], [GUI agent], [OS agent]
    - 📖 TLDR: A comprehensive survey of MLLM-based OS Agents—autonomous agents operating computing devices via OS-provided GUIs—covering agent architecture, perception and reasoning, training methodologies, benchmarks, safety considerations, and future research directions.
- [Evolving in Tasks: Empowering the Multi-modality Large Language Model as the Computer Use Agent](https://arxiv.org/abs/2508.04037)
    - Yuhao Cheng, Liang Tang, Shuxian Li, Yukang Huo, Tiaonan Duan, Kaer Huang, Yanzhe Jing, Yiqiang Yan
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-08-05
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [self-evolving], [reinforcement learning], [data generation], [framework]
    - 📖 TLDR: Proposes the Self-Evolution Agent (SEA) for computer operation with three core innovations: an automatic verifiable trajectory generation pipeline, multi-turn RL-based policy optimization, and continual model enhancement to iteratively improve performance on diverse computer-use tasks.
- [VeriGUI: Verifiable Long-Chain GUI Dataset](https://arxiv.org/abs/2508.04026)
    - Shunyu Liu, Minghao Liu, Huichi Zhou, Zhenyu Cui, Yang Zhou, Yuhao Zhou, Wendong Fan, Ge Zhang, Jiajun Shi, Weihao Xuan, Jiaxing Huang, Shuang Luo, Fang Wu, Heli Qi, Qingcheng Zeng, Ziqi Ren, Jialiang Gao, Jindi Lv, Junjie Wang, Aosong Feng, Heng Zhou, Wangchunshu Zhou, Zhenfei Yin, Wenlong Zhang, Guohao Li
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-08-05
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [GUI agent], [long-horizon task], [verification], [benchmark]
    - 📖 TLDR: VeriGUI is a verifiable long-chain GUI dataset for developing and evaluating GUI agents on long-horizon tasks with intermediate process verification, addressing the limitation of existing datasets that focus on short interactions with outcome-only evaluation.
- [Measuring Harmfulness of Computer-Using Agents](https://arxiv.org/abs/2508.00935)
    - Aaron Xuxiang Tian, Ruofan Zhang, Janet Tang, Ji Wang, Tianyu Shi, Jiaxin Wen
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-07-31
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [safety], [red-teaming], [security]
    - 📖 TLDR: CUAHarm is a benchmark of 104 expert-written realistic misuse scenarios for computer-using agents—including disabling firewalls, data leakage, and backdoor installation—with a sandbox and rule-based verifiable rewards for comprehensive CUA misuse risk evaluation.
- [Phi-Ground Tech Report: Advancing Perception in GUI Grounding](https://arxiv.org/abs/2507.23779)
    - Miaosen Zhang, Ziqiang Xu, Jialiang Zhu, Qi Dai, Kai Qiu, Yifan Yang, Chong Luo, Tianyi Chen, Justin Wagle, Tim Franklin, Baining Guo
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-07-31
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [model], [computer-use agent], [visual grounding], [benchmark]
    - 📖 TLDR: Phi-Ground is a tech report advancing GUI grounding perception for CUAs, presenting a model series significantly improving accuracy on challenging benchmarks including ScreenSpot-Pro and UI-Vision beyond the ~65% ceiling of existing end-to-end grounding models.
- [OS-MAP: How Far Can Computer-Using Agents Go in Breadth and Depth?](https://arxiv.org/abs/2507.19132)
    - Xuetian Chen, Yinghao Chen, Xinfeng Yuan, Zhuo Peng, Lu Chen, Yuekeng Li, Zhoujia Zhang, Yingqian Huang, Leyan Huang, Jiaqing Liang, Tianbao Xie, Zhiyong Wu, Qiushi Sun, Biqing Qi, Bowen Zhou
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-07-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [evaluation], [task diversity], [desktop]
    - 📖 TLDR: OS-MAP is a benchmark of 416 realistic daily computer-use tasks organized to capture internal task heterogeneity and alignment with actual user demands, providing structured evaluation across breadth and depth dimensions to bridge research progress to practical CUA deployment.
- [A Systematization of Security Vulnerabilities in Computer Use Agents](https://arxiv.org/abs/2507.05445)
    - Daniel Jones, Giorgio Severi, Martin Pouliot, Gary Lopez, Joris de Gruyter, Santiago Zanella-Beguelin, Justin Song, Blake Bullwinkel, Pamela Cortez, Amanda Minnich
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-07-07
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [computer-use agent], [survey], [attack], [safety]
    - 📖 TLDR: A systematization of seven classes of security vulnerabilities unique to Computer Use Agents—covering novel attack surfaces and trust boundaries not captured by traditional threat models—with systematic threat analysis and adversarial testing of real-world CUAs.
- [WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis](https://arxiv.org/abs/2507.04370)
    - Yifei Gao, Junhong Ye, Jiaqi Wang, Jitao Sang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-07-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [world model], [MCTS], [data generation], [training data]
    - 📖 TLDR: WebSynthesis is a world-model-guided MCTS framework for efficient WebUI trajectory synthesis that simulates browser states to overcome uncontrollable real-environment states and data scarcity, enabling large-scale synthetic trajectory generation for web agent training.
- [Learning, Reasoning, Refinement: A Framework for Kahneman's Dual-System Intelligence in GUI Agents](https://arxiv.org/abs/2506.17913)
    - Jinjie Wei, Jiyao Liu, Lihao Liu, Ming Hu, Junzhi Ning, Mingcheng Li, Weijie Yin, Junjun He, Xiao Liang, Chao Feng, Dingkang Yang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-22
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [framework], [dual-system cognition], [reinforcement learning], [evaluation]
    - 📖 TLDR: Proposes a Learning-Reasoning-Refinement (LRR) framework for GUI agents inspired by Kahneman dual-system theory, combining progressive System 2 reasoning with fast reactive decision-making and iterative refinement, alongside a new evaluation metric better reflecting real-world GUI interaction complexity.
- [OSWorld-Human: Benchmarking the Efficiency of Computer-Use Agents](https://arxiv.org/abs/2506.16042)
    - Reyna Abhyankar, Qi Qi, Yiying Zhang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-19
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [efficiency], [latency], [evaluation]
    - 📖 TLDR: OSWorld-Human is the first study benchmarking temporal efficiency of computer-use agents on OSWorld, measuring end-to-end latency (often tens of minutes vs. human minutes) and identifying root causes of this efficiency gap to guide development of practically deployable CUAs.
- [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976)
    - Junhong Shen, Hao Bai, Lunjun Zhang, Yifei Zhou, Amrith Setlur, Shengbang Tong, Diego Caples, Nan Jiang, Tong Zhang, Ameet Talwalkar, Aviral Kumar
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-09
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [computer-use agent], [test-time scaling], [exploration], [planning], [reinforcement learning]
    - 📖 TLDR: Proposes test-time interaction scaling—increasing agent interaction horizons rather than reasoning trace length—showing that richer behaviors including exploration, backtracking, and dynamic adaptation from more interactions outperform extended pre-action thinking for GUI-based computer tasks.
- [MCPWorld: A Unified Benchmarking Testbed for API, GUI, and Hybrid Computer Use Agents](https://arxiv.org/abs/2506.07672)
    - Yunhe Yan, Shihe Wang, Jiajun Du, Yexuan Yang, Yuxuan Shan, Qichen Qiu, Xianqing Jia, Xinge Wang, Xin Yuan, Xu Han, Mao Qin, Yinxiao Chen, Chen Peng, Shangguang Wang, Mengwei Xu
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-09
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [MCP], [GUI agent], [hybrid agent]
    - 📖 TLDR: MCPWorld is the first automatic CUA testbed for API, GUI, and API-GUI hybrid agents using white-box apps with modifiable source code and MCP-exposed interfaces, enabling evaluation beyond GUI-only agents and avoiding brittleness from UI changes.
- [BIMgent: Towards Autonomous Building Modeling via Computer-use Agents](https://arxiv.org/abs/2506.07217)
    - Zihan Deng, Changyu Du, Stavros Nousias, André Borrmann
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-08
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [framework], [domain-specific], [desktop automation], [GUI agent]
    - 📖 TLDR: BIMgent is an agentic framework applying computer-use agents to Building Information Modeling (BIM) software for autonomous 3D building modeling in the Architecture, Engineering, and Construction sector, demonstrating CUA applicability to complex open-ended tasks in specialized professional software.
- [DPO Learning with LLMs-Judge Signal for Computer Use Agents](https://arxiv.org/abs/2506.03095)
    - Man Luo, David Cobbley, Xin Su, Shachar Rosenman, Vasudev Lal, Shao-Yen Tseng, Phillip Howard
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-03
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [computer-use agent], [DPO], [reinforcement learning], [privacy], [on-device]
    - 📖 TLDR: Trains a lightweight local VLM for privacy-preserving computer-use agents using DPO with LLM-judge-generated preference signals, enabling resource-efficient CUAs that run entirely on local machines without cloud inference, addressing privacy and scalability concerns of cloud-based CUAs.
- [VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents](https://arxiv.org/abs/2506.02539)
    - Thong Q. Nguyen, Shubhang Desai, Raja Hasnain Anwar, Firoz Shaik, Vishwas Suryanarayanan, Vishal Chowdhary
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-03
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [memory], [safety], [alignment], [framework]
    - 📖 TLDR: VerificAgent is a scalable oversight framework for CUAs treating persistent memory as an explicit alignment surface, combining expert-curated domain seeds, trajectory-based memory growth, and human fact-checking to prevent domain-inappropriate or unsafe heuristics from accumulating in agent memory.
- [VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents](https://arxiv.org/abs/2506.02456)
    - Tri Cao, Bennett Lim, Yue Liu, Yuan Sui, Yuexin Li, Shumin Deng, Lin Lu, Nay Oo, Shuicheng Yan, Bryan Hooi
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-06-03
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [prompt injection], [security], [attack]
    - 📖 TLDR: VPI-Bench is a benchmark for Visual Prompt Injection (VPI) attacks on CUAs, where malicious instructions are visually embedded within rendered user interfaces, investigating vulnerabilities of both full-system-access CUAs and Browser-Use Agents beyond HTML-level prompt injection attacks.
- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://arxiv.org/abs/2505.21936)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler-Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [computer-use agent], [red-teaming], [prompt injection], [benchmark]
    - 📖 TLDR: RedTeamCUA is an adversarial testing framework for CUAs featuring a hybrid sandbox integrating VM-based OS and Docker-based web platforms, enabling realistic evaluation of indirect prompt injection in hybrid web-OS attack scenarios with flexible adversarial configuration.
- [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897)
    - Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiachong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-26
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [computer-use agent], [scientific workflow], [evaluation], [desktop]
    - 📖 TLDR: ScienceBoard evaluates multimodal autonomous agents in realistic scientific workflows across multiple research domains, covering tasks mirroring actual researcher routines to demonstrate how computer-use agents can automate scientific problem-solving and experimental procedures.
- [ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282)
    - Fanbin Lu, Zhisheng Zhong, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-22
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [GUI agent], [policy optimization], [training], [multi-turn]
    - 📖 TLDR: ARPO (End-to-End Policy Optimization for GUI Agents with Experience Replay) addresses multi-turn RL for VLM-based GUI agents through experience replay to mitigate sparse rewards, delayed feedback, and high rollout costs, enabling efficient optimization of long-horizon GUI action sequences.
- [ReGUIDE: Data Efficient GUI Grounding via Spatial Reasoning and Search](https://arxiv.org/abs/2505.15259)
    - Hyunseok Lee, Jeonghoon Kim, Beomjun Kim, Jihoon Tack, Chansong Jo, Jaehong Lee, Cheonbok Park, Sookyo In, Jinwoo Shin, Kang Min Yoo
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-21
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [GUI grounding], [web agent], [spatial reasoning], [data efficiency], [framework]
    - 📖 TLDR: ReGUIDE (Reasoning GUI Grounding for Data Efficiency) is a data-efficient web GUI grounding framework enabling MLLMs to learn accurate element localization via spatial reasoning and search, significantly reducing reliance on large-scale web datasets while improving grounding accuracy.
- [Efficient Agent Training for Computer Use](https://arxiv.org/abs/2505.13909)
    - Yanheng He, Jiahe Jin, Pengfei Liu
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-20
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer-use agent], [training], [data efficiency], [synthetic data], [framework]
    - 📖 TLDR: PC Agent-E achieves a 141% relative improvement in computer-use performance by augmenting only 312 human-annotated trajectories with synthetically generated alternative action decisions from Claude 3.7 Sonnet, surpassing Claude 3.7 Sonnet by 10% with significantly fewer human demonstrations.
- [A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?](https://arxiv.org/abs/2505.10924)
    - Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-16
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [computer-use agent], [safety], [security], [GUI agent]
    - 📖 TLDR: A comprehensive survey of safety and security threats to computer-using agents, covering vulnerabilities in LLM-driven reasoning, multi-component integration, and GUI interaction, analyzing novel risks as CUAs evolve from prototype tools to sophisticated autonomous systems.
- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://arxiv.org/abs/2504.00906)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-04-01
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [computer-use agent], [framework], [GUI grounding], [planning], [generalist-specialist]
    - 📖 TLDR: Agent S2 is a compositional generalist-specialist framework for CUAs that delegates cognitive responsibilities across specialized subagents, addressing imprecise GUI grounding, long-horizon planning difficulties, and performance bottlenecks from relying on single generalist models for diverse cognitive tasks.
- [sudo rm -rf agentic_security](https://arxiv.org/abs/2503.20279)
    - Sejin Lee, Jian Kim, Haon Park, Ashkan Yousefpour, Sangyoon Yu, Min Song
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-03-26
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [computer-use agent], [attack], [jailbreaking], [safety]
    - 📖 TLDR: SUDO (Screen-based Universal Detox2Tox Offense) is a novel attack framework that bypasses refusal-trained safeguards in commercial CUAs (e.g., Claude Computer Use) by transforming harmful requests into seemingly benign ones via a Detox2Tox mechanism, exposing critical vulnerabilities in CUA safety.
- [VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification](https://arxiv.org/abs/2503.18492)
    - Jungjae Lee, Dongjae Lee, Chihun Choi, Youngmin Im, Jaeyoung Wi, Kihong Heo, Sangeun Oh, Sunjae Lee, Insik Shin
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-03-24
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile agent], [safety], [verification], [formal verification], [framework]
    - 📖 TLDR: VeriSafe Agent (VSA) is a formal logic-based action verification system for mobile GUI agents that checks LFM-proposed actions against predefined safety constraints before execution, preventing unreliable automation caused by the probabilistic nature of large foundation models.
- [BEARCUBS: A benchmark for computer-using web agents](https://arxiv.org/abs/2503.07919)
    - Yixiao Song, Katherine Thai, Chau Minh Pham, Yapei Chang, Mazin Nadaf, Mohit Iyyer
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-03-10
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [information seeking], [computer use], [evaluation]
    - 📖 TLDR: BEARCUBS is a benchmark of 111 information-seeking questions requiring web agents to access live websites, handle authentication, interact with dynamic content, and identify factual information in real-world settings without relying on static cached content.
- [SpiritSight Agent: Advanced GUI Agent with One Look](https://arxiv.org/abs/2503.03196)
    - Zhiyuan Huang, Ziming Cheng, Junting Pan, Zhaohui Hou, Mingjie Zhan
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-03-05
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [GUI grounding], [VLM], [framework], [efficiency]
    - 📖 TLDR: SpiritSight Agent is a vision-based GUI agent that addresses element grounding accuracy limitations by proposing a novel single-screenshot architecture enabling high-accuracy, low-latency, cross-platform GUI interaction with improved element grounding through efficient screen comprehension.
- [TinyClick: Single-Turn Agent for Empowering GUI Automation](https://arxiv.org/abs/2410.11871)
    - Pawel Pawlowski, Krystian Zawistowski, Wojciech Lapacz, Adam Wiacek, Marcin Skorupa, Sebastien Postansque, Jakub Hoscilowicz
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2024-10-09
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [model], [visual grounding], [efficiency], [Florence-2]
    - 📖 TLDR: TinyClick is a single-turn UI agent based on Florence-2-Base (0.27B parameters, trained in 56 GPU-hours) that identifies screen coordinates of UI elements from user commands, achieving strong performance on ScreenSpot and OmniAct benchmarks with minimal latency through vision-specific multi-task training.
- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://arxiv.org/abs/2410.05243)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2024-10-07
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [visual grounding], [model], [dataset], [GUI agent]
    - 📖 TLDR: UGround advocates for universal visual GUI grounding (pixel-based coordinate prediction) over text-based representations like HTML/accessibility trees, introducing a large-scale synthetic training dataset and demonstrating that native visual grounding enables more robust and efficient GUI agents across diverse platforms.
- [Visual Grounding Methods for Efficient Interaction with Desktop Graphical User Interfaces](https://arxiv.org/abs/2407.01558)
    - El Hassane Ettifouri, Jessica López Espejel, Laura Minkova, Tassnim Dardouri, Walid Dahhane
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2024-05-05
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [GUI grounding], [visual grounding], [desktop], [GUI agent], [benchmark]
    - 📖 TLDR: Explores Instruction Visual Grounding (IVG) for desktop GUI automation, benchmarking multi-modal approaches to element identification within GUI interfaces for automated software testing, accessibility, and human-computer interaction applications.
- [CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents](https://arxiv.org/abs/2407.01511)
    - Tianqi Xu, Linyao Chen, Dai-Jie Wu, Yanjun Chen, Zecheng Zhang, Xiang Yao, Zhiqiang Xie, Yongchao Chen, Shilong Liu, Bochen Qian, Anjie Yang, Zhaoxuan Jin, Jianbo Deng, Philip Torr, Bernard Ghanem, Guohao Li
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2024-07-01
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [cross-platform], [multimodal agent], [evaluation], [GUI agent]
    - 📖 TLDR: CRAB is the first cross-environment agent benchmark supporting tasks spanning multiple GUI environments simultaneously (websites, desktop, mobile), featuring graph-based task evaluation that handles heterogeneous success conditions and evaluates compositional subtask completion without restricting solution paths.
- [Tree Search for Language Model Agents](https://arxiv.org/abs/2407.01476)
    - Jing Yu Koh, Stephen McAleer, Daniel Fried, Ruslan Salakhutdinov
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2024-07-01
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [tree search], [planning], [exploration], [MCTS]
    - 📖 TLDR: Proposes an inference-time best-first tree search algorithm for language model agents in interactive web environments, enabling explicit multi-step exploration and planning by leveraging environmental feedback to overcome LM limitations in multi-step reasoning for complex computer tasks.
