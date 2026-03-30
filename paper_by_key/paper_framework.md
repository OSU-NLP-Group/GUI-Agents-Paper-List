# Papers with Keyword: framework

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

- [K²-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676)
    - Zhe Wu, Donglin Mo, Hongjin Lu, Junliang Xing, Jianheng Liu, Yuheng Jing, Kai Li, Kun Shao, Jianye Hao, Yuanchun Shi
    - 🏛️ Institutions: Tsinghua University, Huawei Noah's Ark Lab, Institute of Automation CAS
    - 📅 Date: February 28, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [hierarchical planning], [mobile GUI agent], [AndroidWorld], [K²-Agent]
    - 📖 TLDR: This paper introduces K²-Agent, a hierarchical mobile device control framework that separates declarative “know-what” reasoning from procedural “know-how” execution and co-evolves them during training. Its high-level module refines task knowledge through an SRLR loop, while the low-level executor is trained with curriculum-guided GRPO and dynamic demonstration injection. On AndroidWorld, K²-Agent reaches a new state of the art among open-source screenshot-only systems and also generalizes competitively to ScreenSpot-v2 and Android-in-the-Wild.

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
    - 🔑 Key: [framework], [planning], [tool-use], [typed action abstraction], [agentic web], [Web Verbs]
    - 📖 TLDR: This paper argues that web agents need a semantic action layer above brittle low-level clicks and keystrokes, and proposes Web Verbs as typed, composable web actions with explicit contracts, policies, and logging support. The abstraction unifies API-based and browser-based execution into stable callable units that agents can discover and compose into short programs. Through a proof-of-concept implementation and case studies, the paper positions typed web actions as a route to more reliable, efficient, and verifiable web agents.

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL]
    - 📖 TLDR: This paper studies continual learning for computer-use agents in dynamic, shifting target environments without relying on human demonstrations. It introduces ACuRL, an autonomous curriculum reinforcement learning framework that explores environments, synthesizes progressively tailored tasks, and trains with CUAJudge, an automatic evaluator aligned closely with human judgments. The method improves both intra-environment and cross-environment adaptation while avoiding catastrophic forgetting, making it directly relevant to real-world deployment of CUAs.

- [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662)
    - Deyang Jiang, Jing Huang, Xuanle Zhao, Lei Chen, Liming Zheng, Fanfan Liu, Haibo Qiu, Peng Shi, Zhixiong Zeng
    - 🏛️ Institutions: Meituan
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [planning], [multi-agent], [synthetic trajectory generation], [TreeCUA], [TreeCUA-DPO]
    - 📖 TLDR: This paper targets the scaling bottleneck of GUI planning rather than GUI grounding. It introduces TreeCUA, a multi-agent framework that organizes large-scale GUI exploration trajectories as reusable tree structures, reducing redundant exploration while improving trajectory quality through verification, summarization, and evaluation. The work further proposes TreeCUA-DPO to learn planning from adjacent branch information, yielding strong gains and improved out-of-domain generalization.

- [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235)
    - Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, LawZero, Mila - Quebec AI Institute, Universite de Montreal, University of California, Berkeley
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [safety], [red teaming], [unintended behavior], [computer-use agent], [AutoElicit]
    - 📖 TLDR: This paper studies unsafe unintended behaviors in computer-use agents under benign user inputs rather than adversarial prompts. It introduces AutoElicit, an agentic framework that iteratively perturbs realistic benign instructions using execution feedback to surface severe harmful behaviors in frontier CUAs. The results show that even strong CUAs remain broadly susceptible to harmful deviations, establishing a concrete framework for systematically probing unintended safety failures in realistic computer-use settings.

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, Princeton University, Shenzhen Loop Area Institute, Shanghai AI Lab
    - 📅 Date: February 5, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [memory], [reinforcement learning], [online RL], [mobile GUI agent], [UI-Mem]
    - 📖 TLDR: This paper proposes UI-Mem, a mobile GUI agent training framework that augments online reinforcement learning with a hierarchical experience memory storing reusable workflows, subtask skills, and failure patterns. It introduces stratified group sampling to mix strong, weak, and unguided rollouts, plus a self-evolving loop that continually abstracts new successful plans and error diagnoses back into memory. Experiments on AndroidWorld and AndroidLab show strong gains over standard online RL and static reuse baselines, especially on unseen applications.

- [Continual GUI Agents](https://arxiv.org/abs/2601.20732)
    - Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng
    - 🏛️ Institutions: Tsinghua University, Zhejiang University, ETH Zurich, Beijing University of Posts and Telecommunications
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [GUI grounding], [domain shift], [GUI-AiF], [Continual GUI Agents]
    - 📖 TLDR: This paper introduces Continual GUI Agents as a continual learning setting where GUI agents must adapt to domain and resolution shifts over time without losing stable grounding. It proposes GUI-AiF, a reinforcement fine-tuning framework with anchoring-point and anchoring-region rewards that keep agents aligned to changing interaction targets instead of overfitting to static cues. Experiments show the method outperforms prior baselines and frames continual adaptation as a core systems challenge for GUI agents.

- [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE)
    - Bin Kang, Shaoguo Wen, Yifei Bi, Shunlong Wu, Xinbin Yuan, Rui Shao, Junle Wang, Zhuotao Tian
    - 🏛️ Institutions: Chengdu Institute of Computer Applications, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Tencent Turing Lab, Georgia Institute of Technology, Tsinghua University, Nankai University, Shenzhen Loop Area Institute
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [long-horizon planning], [GUI perception], [GUI task automation], [LongGUIBench], [LongHorizonUI]
    - 📖 TLDR: This paper studies the long-horizon setting where GUI agents fail as interaction chains grow longer and errors compound over time. It introduces LongHorizonUI, a unified framework that combines indexed multimodal perception, structured reflective decision-making, and compensatory execution with rollback to improve robustness on long tasks. The paper also presents LongGUIBench, a benchmark of 371 long-horizon GUI scenarios across apps and games, and reports clear gains over prior GUI-agent baselines on long-horizon automation.

- [GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents](https://arxiv.org/abs/2601.18842)
    - Yanxi Wang, Zhiling Zhang, Wenbo Zhou, Weiming Zhang, Jie Zhang, Qiannan Zhu, Yu Shi, Shuxin Zheng, Jiyan He
    - 🏛️ Institutions: Beijing Normal University, Zhongguancun Academy, USTC, A*STAR, Zhongguancun Institution of Artificial Intelligence
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [safety], [privacy-preserving GUI agent], [GUIGuard], [GUIGuard-Bench]
    - 📖 TLDR: This paper introduces GUIGuard, a general privacy-preserving framework for GUI agents that separates privacy recognition, privacy protection, and protected task execution. It also builds GUIGuard-Bench, a cross-platform benchmark with 630 trajectories and 13,830 screenshots annotated for privacy grounding, risk levels, categories, and task necessity. Results show that current GUI agents have very weak privacy recognition, while carefully designed protection policies can retain usable task-planning fidelity, making privacy-aware GUI agents a concrete and measurable systems problem.

- [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)
    - Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu
    - 🏛️ Institutions: Meituan
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [synthetic data], [reinforcement learning], [OSWorld], [EvoCUA]
    - 📖 TLDR: This paper introduces EvoCUA, a native computer-use agent trained through an evolving learning cycle that tightly couples scalable synthetic task generation, large-scale sandbox rollouts, and iterative policy optimization. Instead of relying on static imitation data, EvoCUA turns successful and failed experience into supervision through verification, error analysis, and self-correction, enabling continual capability growth. On OSWorld, it reaches 56.7% success rate, surpassing prior open-source computer-use agents and even some leading closed-weight systems.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: University of Science and Technology of China, Institute of Artificial Intelligence (TeleAI) China Telecom, Shanghai Innovation Institute, Shanghai Jiao Tong University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [tool-augmented perception], [active perception], [GUI-Eyes]
    - 📖 TLDR: This paper proposes GUI-Eyes, a reinforcement learning framework for active visual perception in GUI grounding. Instead of relying on a single static observation, the agent learns when and how to invoke tools such as cropping and zooming through a two-stage perception policy, supported by a spatially continuous reward tailored to tool usage. With only 3k labeled samples, GUI-Eyes-3B substantially improves grounding accuracy on ScreenSpot-Pro, highlighting the value of tool-aware perception for robust GUI agents.

- [MobileDreamer: Generative Sketch World Model for GUI Agent](https://arxiv.org/abs/2601.04035)
    - Yilin Cao, Yufeng Zhong, Zhixiong Zeng, Liming Zheng, Jing Huang, Haibo Qiu, Peng Shi, Wenji Mao, Wan Guanglu
    - 🏛️ Institutions: CAS, UCAS, Meituan
    - 📅 Date: January 7, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [planning], [lookahead], [mobile GUI agent], [MobileDreamer]
    - 📖 TLDR: This paper introduces MobileDreamer, a world-model-based lookahead framework for mobile GUI agents that predicts compact task-relevant future interface sketches rather than full screenshots. Its textual sketch world model preserves spatial information while remaining efficient, and its rollout imagination strategy uses these predicted futures to improve action selection on long-horizon tasks. On AndroidWorld, MobileDreamer achieves state-of-the-art performance and improves task success by 5.25%, showing that lightweight future imagination can materially strengthen mobile GUI planning.

- [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047)
    - Hanzhang Zhou, Xu Zhang, Panrong Tong, Jianan Zhang, Liangyu Chen, Quyu Kong, Chenglin Cai, Chen Liu, Yue Wang, Jingren Zhou, Steven Hoi
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [reinforcement learning], [MCP], [device-cloud collaboration], [MAI-UI]
    - 📖 TLDR: This technical report introduces MAI-UI, a family of foundation GUI agents spanning multiple scales and designed for realistic deployment. The work expands beyond UI-only operation by incorporating agent-user interaction, MCP tool calls, a native device-cloud collaboration architecture, and an online reinforcement learning framework for long-horizon training. MAI-UI sets strong results on GUI grounding, AndroidWorld, and MobileWorld, positioning it as a broad real-world-oriented foundation agent stack rather than a single narrow benchmark model.

- [GUI Exploration Lab: Enhancing Screen Navigation in Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2512.02423)
    - Yujie Shen, Ruobing Xie, Xuanze Xu, Yichao Zhou, Jinyang Wang, Guangyao Feng, Lifan Yuan, Xiang Ao
    - 🏛️ Institutions: Unknown
    - 📅 Date: December 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [screen navigation], [multi-turn RL], [GUI Exploration Lab]
    - 📖 TLDR: This paper focuses on improving screen navigation for GUI agents through multi-turn reinforcement learning rather than one-step action imitation alone. It introduces GUI Exploration Lab as a training setting for iterative exploration and feedback-driven policy improvement over interface trajectories. The work emphasizes that stable navigation competence in GUI agents benefits from explicit long-horizon RL training loops and structured exploration signals.

- [ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2511.19719)
    - Hongbin Zhong, Fazle Faisal, Luis Franca, Tanakorn Leesatapornwongsa, Adriana Szekeres, Kexin Rong, Suman Nath
    - 🏛️ Institutions: Microsoft Research, Georgia Tech
    - 📅 Date: November 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [memory], [planning], [state machine], [programmatic agent], [ActionEngine]
    - 📖 TLDR: This paper argues that GUI agents should move beyond purely reactive next-action prediction and instead build programmatic control abstractions over repeated interface states. It introduces ActionEngine, which stores execution knowledge as state-machine-style memory and uses that memory to compose reusable programs for future tasks. The approach targets more reliable long-horizon automation by turning interaction experience into explicit control structure rather than latent-only policy updates.

- [Computer-Use Agents as Judges for Generative User Interface](https://arxiv.org/abs/2511.15567)
    - Kevin Qinghong Lin, Siyuan Hu, Linjie Li, Zhengyuan Yang, Lijuan Wang, Philip Torr, Mike Zheng Shou
    - 🏛️ Institutions: University of Oxford, Show Lab, National University of Singapore, Microsoft
    - 📅 Date: November 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-native GUI], [automatic GUI design], [AUI-Gym], [Coder-CUA collaboration]
    - 📖 TLDR: This paper studies how computer-use agents can actively improve interfaces rather than only operate them. It introduces AUI-Gym, a benchmark for automatic GUI development across 52 applications and 1,560 synthesized tasks, together with a Coder-CUA collaboration framework in which a coding model iteratively redesigns interfaces while a computer-use agent judges task solvability through interaction. The work shifts GUI design toward agent-centric efficiency and reliability, showing that agent feedback can materially improve downstream execution success.

- [GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation](https://arxiv.org/abs/2510.27210)
    - Tao Liu, Chongyu Wang, Rongjie Li, Yingchen Yu, Xuming He, Bai Song
    - 🏛️ Institutions: ShanghaiTech University, ByteDance, Shanghai Engineering Research Center of Intelligent Vision and Imaging
    - 📅 Date: October 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reasoning], [history summarization], [reinforcement learning], [GUI navigation], [GUI-Rise]
    - 📖 TLDR: This paper targets two persistent GUI-agent weaknesses: poor cross-domain generalization and weak use of long interaction history. GUI-Rise addresses them with a reasoning-enhanced framework that jointly trains structured reasoning, action prediction, and history summarization, then further improves the agent with GRPO and a history-aware reward. Under matched training data, it reports state-of-the-art GUI-navigation performance, especially on out-of-domain settings.

- [PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction For Continual Learning](https://arxiv.org/abs/2510.15863)
    - Simon Yu, Gang Li, Weiyan Shi, Peng Qi
    - 🏛️ Institutions: Northeastern University, Uniphore
    - 📅 Date: October 17, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [skill learning], [compositional skills], [transfer generalization], [Polymorphism], [PolySkill], [continual learning]
    - 📖 TLDR: This paper introduces **PolySkill**, a framework that enables LLM-based web agents to acquire generalizable and composable skills by decoupling a skill's abstract goal from its concrete implementation, inspired by polymorphic abstraction in software engineering. Evaluated on the Mind2Web benchmark, PolySkill significantly enhances skill reuse, improves task success rates on both seen and unseen websites, and reduces the number of interaction steps, demonstrating effective continual learning and skill transfer capabilities.

- [CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs](https://arxiv.org/abs/2510.15455)
    - Gucongcong Fan, Chaoyue Niu, Chengfei Lyu, Fan Wu, Guihai Chen
    - 🏛️ Institutions: Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: October 17, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [privacy], [mobile GUI agent], [cloud-local collaboration], [UI exposure reduction], [CORE]
    - 📖 TLDR: This paper studies privacy leakage in mobile agents that repeatedly upload full-screen UI context to cloud LLMs for planning and action selection. It proposes CORE, a collaborative framework where local and cloud LLMs split planning and decision-making through layout-aware block partitioning, co-planning, and co-decision, so only a smaller relevant UI subset is exposed upstream. On diverse mobile apps and tasks, CORE cuts UI exposure by up to 55.6% while keeping task success close to cloud-only agents.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Unaffiliated
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [mobile GUI agent], [GUI-Shift]
    - 📖 TLDR: This paper introduces GUI-Shift, a self-supervised reinforcement learning framework for VLM-based GUI agents built around the K-step GUI Transition task, which learns GUI dynamics from unlabeled trajectories without natural-language instruction annotation. The method combines rule-based optimization with data filtering and improves both GUI automation and grounding performance across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro. The paper shows a scalable path to training stronger mobile GUI agents from large amounts of unlabeled interaction data.

- [GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding](https://arxiv.org/abs/2510.04039)
    - Bin Lei, Nuo Xu, Ali Payani, Mingyi Hong, Chunhua Liao, Yu Cao, Caiwen Ding
    - 🏛️ Institutions: University of Minnesota, Cisco Research, Lawrence Livermore National Laboratory
    - 📅 Date: October 5, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [tool coordination], [iterative refinement], [visual grounding]
    - 📖 TLDR: This paper proposes GUI-Spotlight, a model for GUI visual grounding that iteratively refines its focus using specialized tools like crop, extract, and find_color. Trained with a hybrid of supervised learning and reinforcement learning, the method dynamically invokes tools over multiple rounds, improving accuracy and efficiency. It significantly outperforms previous methods on benchmarks like ScreenSpot-Pro and UI-Vision with less training data.

- [Say One Thing, Do Another? Diagnosing Reasoning‑Execution Gaps in VLM‑Powered Mobile‑Use Agents](https://arxiv.org/abs/2510.02204)
    - Lingzhong Dong, Ziqi Zhou, Shuaibo Yang, Haiyue Sheng, Pengzhou Cheng, Zongru Wu, Zheng Wu, Gongshen Liu, Zhuosheng Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Beijing Institute of Technology
    - 📅 Date: October 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [evaluation framework], [Ground-Truth Alignment], [reasoning-execution gap], [chain-of-thought], [VLM]
    - 📖 TLDR: This paper investigates reasoning-execution mismatches in VLM-powered mobile agents, revealing that models often generate correct reasoning but fail in execution. It introduces an evaluation framework combining execution accuracy and a new metric called Ground-Truth Alignment (GTA). The authors identify two types of errors—Execution Gap and Reasoning Gap—and show that model scaling alleviates but does not resolve these issues.

- [GUI‑KV: Efficient GUI Agents via KV Cache with Spatio‑Temporal Awareness](https://arxiv.org/abs/2510.00536)
    - Kung‑Hsiang Huang, Haoyi Qiu, Yutong Dai, Caiming Xiong, Chien‑Sheng Wu
    - 🏛️ Institutions: Salesforce AI Research, University of California, Los Angeles
    - 📅 Date: October 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [KV cache compression], [spatial saliency], [temporal redundancy], [plug‑and‑play]
    - 📖 TLDR: This paper proposes GUI-KV, a plug-and-play KV cache compression method for GUI agents, which improves efficiency by combining spatial saliency-guided token selection and temporal redundancy pruning. It significantly reduces memory and computation costs while maintaining or even surpassing original model performance across multiple GUI agent benchmarks.

- [Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents](https://arxiv.org/abs/2509.26539)
    - Zhen Yang, Zi-Yi Dou, Di Feng, Forrest Huang, Anh Nguyen, Keen You, Omar Attia, Yuhao Yang, Michael Feng, Haotian Zhang, Ram Ramrakhya, Chao Jia, Jeffrey Nichols, Alexander Toshev, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [chain-of-thought], [visual tool-use]
    - 📖 TLDR: This paper presents **Ferret-UI Lite**, a compact 3B end-to-end GUI agent designed for on-device deployment across mobile, web, and desktop. It introduces a mixed real and synthetic GUI dataset, a two-stage training pipeline combining supervised fine-tuning and reinforcement learning with verifiable rewards, and inference-time reasoning and visual cropping strategies. Ferret-UI Lite achieves strong grounding accuracy (91.6% on ScreenSpot-V2) and promising task success rates (28.0% on AndroidWorld, 19.8% on OSWorld), illustrating both the opportunities and challenges of building efficient on-device GUI agents.

- [BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent](https://arxiv.org/abs/2509.15566)
    - Shaojie Zhang, Ruoceng Zhang, Pei Fu, Shaokang Wang, Jiahui Yang, Xin Du, Shiqi Cui, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: September 19, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI agent], [reinforcement fine-tuning], [reasoning], [reward design], [BTL-UI]
    - 📖 TLDR: This paper proposes Blink-Think-Link, a brain-inspired framework for GUI agents that decomposes interaction into rapid visual attention, higher-level reasoning, and executable action generation. It also introduces blink-specific data generation and a rule-based reward that supervises both the reasoning process and final outcome. The resulting BTL-UI model reports competitive performance across static GUI understanding and dynamic GUI interaction benchmarks.

- [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119)
    - Yifan Xu, Xiao Liu, Xinghan Liu, Jiaqi Fu, Hanchen Zhang, Bohao Jing, Shudan Zhang, Yuting Wang, Wenyi Zhao, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Z.AI
    - 📅 Date: September 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [mobile GUI agent], [AndroidWorld], [AndroidLab], [MobileRL], [ADAGRPO]
    - 📖 TLDR: This paper introduces MobileRL, an online reinforcement learning framework for mobile GUI agents centered on the ADAGRPO algorithm for difficulty-adaptive replay, curriculum filtering, and reward shaping over multi-turn tasks. Applied to Qwen2.5-VL-7B-Instruct and GLM-4.1V-9B-Base, it improves sample efficiency and pushes performance to state-of-the-art success rates on both AndroidWorld and AndroidLab. The work is a focused training-framework contribution for strengthening open mobile agents rather than a new benchmark release.

- [Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control](https://arxiv.org/abs/2509.01720)
    - Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: September 1, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [mobile GUI agent], [sample efficiency], [AndroidWorld], [SoLS]
    - 📖 TLDR: This paper introduces SoLS, an off-policy reinforcement learning algorithm for mobile app control that treats successful and unsuccessful samples differently to improve stability and sample efficiency. It also adds Successful Transition Replay to focus learning on successful interactions. On AndroidWorld, the method substantially outperforms prior prompt-based and RL baselines while using much less computation than large proprietary agents.

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
    - 🔑 Key: [benchmark], [dataset], [framework], [long-horizon reasoning], [unknown-tools challenge], [execution-based evaluation], [MCP-Universe]
    - 📖 TLDR: MCP-Universe introduces the first comprehensive benchmark for evaluating large language models (LLMs) through interactions with real-world Model Context Protocol (MCP) servers. It spans six core domains—Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, and Web Searching—across 11 MCP servers. The benchmark employs execution-based evaluators (format, static, dynamic) to rigorously assess agent performance. Despite progress, state-of-the-art models like GPT-5 (43.72% success), Grok-4 (33.33%), and Claude-4.0-Sonnet (29.44%) show significant limitations. The benchmark highlights challenges in long-context reasoning and unfamiliar tool handling, and provides an open-source extensible evaluation framework with UI support to accelerate future research. 

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Z.AI, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [benchmark], [API-GUI paradigm], [dataset], [distributed RL], [Entropulse]
    - 📖 TLDR: This paper presents **ComputerRL**, a large-scale end-to-end reinforcement learning framework enabling agents to operate complex desktop tasks. It introduces the **API-GUI paradigm**, combining programmatic API calls with GUI actions, and a **distributed RL infrastructure** managing thousands of parallel virtual Ubuntu desktops for scalable training. A novel **Entropulse** training strategy alternates between reinforcement learning and supervised fine-tuning to prevent entropy collapse over long training runs. Applied to open models like GLM-4-9B-0414, ComputerRL achieves a new state-of-the-art success rate of **48.9%** on the OSWorld benchmark via the GLM-ComputerRL-9B model.

- [You Don’t Know Until You Click: Automated GUI Testing for Production-Ready Software Evaluation](https://arxiv.org/abs/2508.14104)
    - Yutong Bian, Xianhao Lin, Yupeng Xie, Tianyang Liu, Mingchen Zhuge, Siyuan Lu, Haoming Tang, Jinlin Wang, Jiayi Zhang, Jiaqi Chen, Xiangru Tang, Yongxin Ni, Sirui Hong, Chenglin Wu
    - 🏛️ Institutions: DeepWisdom, Fudan University, Hong Kong University of Science and Technology (Guangzhou), University of California San Diego, King Abdullah University of Science and Technology, Westlake University, Stanford University, Yale University, National University of Singapore
    - 📅 Date: August 17, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-as-a-judge], [RealDevWorld], [RealDevBench], [AppEvalPilot], [multimodal]
    - 📖 TLDR: This paper presents **RealDevWorld**, a novel framework to automatically evaluate production-ready GUI software generated by LLMs. It includes **RealDevBench**, a suite of 194 open-ended, multimodal software engineering tasks, and **AppEvalPilot**, an “agent-as-judge” system that simulates realistic GUI interactions to assess functional correctness, visual fidelity, and runtime behavior. It achieves high alignment with human judgment (accuracy 0.92, correlation 0.85), reducing the need for manual review and offering scalable, human-aligned evaluation. Code is available on GitHub.

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y. Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Moonshot AI, Stanford University, University of Waterloo, Carnegie Mellon University
    - 📅 Date: August 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [chain-of-thought], [vision language model], [AgentNet]
    - 📖 TLDR: Introduces **OpenCUA**, an open-source framework to train computer-use agents (CUAs) using vision-language models. It includes a cross-platform annotation tool (AgentNet Tool), a large-scale dataset covering 3 OSes and 200+ apps/websites (AgentNet), and a data processing pipeline that builds state-action pairs enhanced with reflective long chain-of-thought reasoning. The resulting models—especially OpenCUA-72B—achieve SOTA performance on the OSWorld-Verified benchmark (45.0% success), surpassing prior open-source baselines and demonstrating strong generalization and scalability. All tools, models, and data are publicly released.

- [CoAct‑1: Computer‑using Multi-agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: University of Southern California, Salesforce Research, University of Washington
    - 📅 Date: August 5, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hybrid agent], [coding action], [multi-agent system], [OSWorld]
    - 📖 TLDR: This paper introduces **CoAct‑1**, a multi-agent system where an Orchestrator coordinates between a GUI Operator and a Programmer agent that can execute code (Python/Bash) directly. This hybrid design allows the agent to perform complex desktop tasks more efficiently than GUI-only agents. Evaluated on OSWorld and WindowsAgentArena, CoAct‑1 achieves state-of-the-art success rates of 60.8% and 52.5% respectively, while reducing average steps to 10.15.

- [Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training](https://arxiv.org/abs/2508.00414)
    - Tianqing Fang, Zhisong Zhang, Xiaoyang Wang, Rui Wang, Can Qin, Yuxuan Wan, Jun-Yu Ma, Ce Zhang, Jiaqi Chen, Xiyun Li, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: Tencent AI Lab
    - 📅 Date: August 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [dataset], [model], [deep research], [reflection], [voting], [Agent Foundation Models]
    - 📖 TLDR: This work introduces **Cognitive Kernel-Pro**, a fully open-source, multi-module agent framework designed to democratize advanced AI agent development. It curates high-quality training data across four domains—web, files, code, and general reasoning—and introduces test-time strategies like reflection and voting to enhance robustness. Evaluated on the GAIA benchmark, its open 8B-parameter model outperforms previous open-source agents such as WebDancer and WebSailor, setting a new performance standard. Code is publicly available.

- [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358)
    - Hussein Mozannar, Gagan Bansal, Cheng Tan, Adam Fourney, Victor Dibia, Jingya Chen, Jack Gerrits, Tyler Payne, Matheus Kunzler Maldaner, Madeleine Grunde-McLaughlin, Eric Zhu, Griffin Bassman, Jacob Alber, Peter Chang, Ricky Loynd, Friederike Niedtner, Ece Kamar, Maya Murad, Rafah Hosn, Saleema Amershi
    - 🏛️ Institutions: Microsoft Research AI Frontiers
    - 📅 Date: July 30, 2025
    - 📑 Publisher: arXiv (also MSR Technical Report MSR-TR-2025-40)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-in-the-loop], [multi-agent], [planning], [memory], [MCP], [safety]
    - 📖 TLDR: Magentic-UI (Multi-agentic User Interface) is an open-source web interface enabling safe, efficient human–agent collaboration through a flexible multi-agent architecture. It supports web browsing, code execution, and file manipulation, and provides six interaction mechanisms—co-planning, co-tasking, multi-tasking, action guards, answer verification, and long-term memory—to integrate human oversight with AI autonomy. Evaluated via agentic benchmarks, simulated user tests, qualitative user study, and safety assessments, it demonstrates how incorporating human-in-the-loop dynamics can significantly improve agentic systems' reliability and performance.

- [MobileUse: A GUI Agent with Hierarchical Reflection for Autonomous Mobile Operation](https://arxiv.org/abs/2507.16853)
    - Ning Li, Xiangmou Qu, Jiamu Zhou, Jun Wang, Muning Wen, Kounianhua Du, Xingyu Lou, Qiuying Peng, Jun Wang, Weinan Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: July 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [mobile GUI agent], [hierarchical reflection], [proactive exploration], [AndroidWorld], [AndroidLab], [MobileUse]
    - 📖 TLDR: This paper introduces MobileUse, a mobile GUI agent designed to handle long-horizon execution, error recovery, and cold-start operation in unfamiliar apps. Its core design combines hierarchical reflection across multiple temporal scales with a reflection-on-demand strategy and proactive exploration to build environment understanding before acting. The result sets new state-of-the-art success rates on AndroidWorld and AndroidLab and is released with a toolkit for execution on physical mobile devices.

- [How to Train Your LLM Web Agent: A Statistical Diagnosis](https://arxiv.org/abs/2507.04103)
    - Dheeraj Vattikonda, Santhoshi Ravichandran, Emiliano Penaloza, Hadi Nekoei, Megh Thakkar, Thibault Le Sellier de Chezelles, Nicolas Gontier, Miguel Munoz-Marmol, Sahar Omidi Shayegan, Stefania Raimondo, Xue Liu, Alexandre Drouin, Laurent Charlin, Alexandre Piche, Alexandre Lacoste, Massimo Caccia
    - 🏛️ Institutions: ServiceNow AI Research, Mila - Quebec AI Institute, Polytechnique Montreal, HEC Montreal, McGill University, Universite de Montreal
    - 📅 Date: July 5, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [reinforcement learning], [imitation learning], [training analysis], [WorkArena]
    - 📖 TLDR: This paper studies how to post-train open web agents under a strict compute budget, combining supervised imitation from a stronger teacher with on-policy reinforcement learning. Using large hyperparameter sweeps and bootstrapped sensitivity analysis, it provides one of the first statistically grounded compute-allocation studies for LLM web-agent training. The main result is that a mixed SFT-plus-RL pipeline is both more compute efficient and more effective than using either approach alone on WorkArena and MiniWoB++.

- [Interactive Evolution: A Neural-Symbolic Self-Training Framework For Large Language Models](https://aclanthology.org/2025.acl-long.635/)
    - Fangzhi Xu, Qiushi Sun, Kanzhi Cheng, Jun Liu, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Shanghai AI Laboratory, The University of Hong Kong, Nanjing University
    - 📅 Date: July 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [dataset], [neural-symbolic self-training], [online exploration], [self-refinement]
    - 📖 TLDR: This paper introduces *ENVISIONS*, a neural-symbolic self-training framework designed to improve large language models (LLMs) by enabling self-training through interaction with a symbolic environment. The framework addresses symbolic data scarcity and enhances LLMs' symbolic reasoning proficiency by iteratively exploring, refining, and learning from symbolic tasks without reinforcement learning. Extensive evaluations across web navigation, math, and logical reasoning tasks highlight *ENVISIONS* as a promising approach for enhancing LLM symbolic processing.

- [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://arxiv.org/abs/2506.08012)
    - Penghao Wu, Shengnan Ma, Bo Wang, Jiaheng Yu, Lewei Lu, Ziwei Liu
    - 🏛️ Institutions: Nanyang Technological University, SenseTime Research
    - 📅 Date: June 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [model], [benchmark], [self-reflection], [GUI‑Reflection Task Suite]
    - 📖 TLDR: Introduces **GUI‑Reflection**, a framework that enhances multimodal GUI agents with self-reflection and error correction. It spans three training stages—pre‑training with reflection tasks, offline supervised fine‑tuning with autogenerated error scenarios, and online iterative reflection tuning—resulting in improved robustness on AndroidWorld and the novel GUI‑Reflection Task Suite using entirely automated pipelines.

- [DeepShop: A Benchmark for Deep Research Shopping Agents](https://arxiv.org/abs/2506.02839)
    - Yougang Lyu, Xiaoyu Zhang, Lingyong Yan, Maarten de Rijke, Zhaochun Ren, Xiuying Chen
    - 🏛️ Institutions: U Amsterdam, Shandong U, Baidu Inc., Leiden U, MBZUAI
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation framework], [RAG], [query complexity], [DeepShop]
    - 📖 TLDR: DeepShop introduces a comprehensive benchmark for web shopping agents, mirroring the real first-use complexity of online shopping scenarios. It features diversified query evolution across five domains, complexity-tier classification (easy/medium/hard), and a fine‐grained scoring system analyzing attribute matching, filters, and sorting. Evaluations across RAG and agentic systems reveal significant shortcomings, especially in handling filters and sorting, underscoring gaps in current research capabilities.

- [GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents](https://arxiv.org/abs/2506.03143)
    - Qianhui Wu, Kanzhi Cheng, Rui Yang, Chaoyun Zhang, Jianwei Yang, Huiqiang Jiang, Jian Mu, Baolin Peng, Bo Qiao, Reuben Tan, Si Qin, Lars Liden, Qingwei Lin, Huan Zhang, Tong Zhang, Jianbing Zhang, Dongmei Zhang, Jianfeng Gao
    - 🏛️ Institutions: Microsoft, Nanjing University, University of Illinois Urbana-Champaign
    - 📅 Date: June 3, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [grounding verifier], [attention mechanism], [coordinate‑free grounding], [GUI‑Actor]
    - 📖 TLDR: GUI‑Actor introduces a coordinate‑free visual grounding approach for GUI agents by adding an attention‑based “<ACTOR>” action head atop a frozen vision‑language model. It learns to align with relevant visual patches and produces multiple candidate regions per forward pass. An optional grounding verifier scores candidates to select the best. The method improves spatial‑semantic alignment and generalizes well across unseen resolutions. On benchmarks like ScreenSpot‑Pro, GUI‑Actor‑7B outperforms prior SOTA UI‑TARS‑72B, with verifier‑augmented versions achieving even higher accuracy—while only fine‑tuning ~100 M parameters.

- [Surfer‑H Meets Holo1: Cost‑Efficient Web Agent Powered by Open Weights](https://arxiv.org/abs/2506.02865)
    - Mathieu Andreux, Breno Baldas Skuk, Hamza Benchekroun, Emilien Biré, Antoine Bonnet, Riaz Bordie, Matthias Brunel, Pierre‑Louis Cedoz, Antoine Chassang, Mickaël Chen, Alexandra D. Constantinou, Antoine d’Andigné, Hubert de La Jonquière, Aurélien Delfosse, Ludovic Denoyer, Alexis Deprez, Augustin Derupti, Michael Eickenberg, Mathïs Federico, Charles Kantor, Xavier Koegler, Yann Labbé, Matthew C. H. Lee, Erwan Le Jumeau de Kergaradec, Amir Mahla, Avshalom Manevich, Adrien Maret, Charles Masson, Rafaël Maurin, Arturo Mena, Philippe Modard, Axel Moyal, Axel Nguyen Kerbel, Julien Revelle, Mats L. Richter, María Santos, Laurent Sifre, Maxime Theillard, Marc Thibault, Louis Thiry, Léo Tronchon, Nicolas Usunier, Tony Wu
    - 🏛️ Institutions: H Company
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [vision language model], [Holo1], [WebClick], [WebVoyager], [Surfer-H]
    - 📖 TLDR: Introduces **Surfer‑H**, a modular web-browsing agent (policy, localizer, validator) that operates purely via screenshots, paired with **Holo1**, a family of open-weight VLMs specialized in UI interaction. Holo1 is trained on a 31B token dataset across GUI grounding, visual reasoning, and agent traces, enabling strong UI localization via the new **WebClick** benchmark. Surfer‑H + Holo1‑7B achieves 92.2% success on WebVoyager—a state-of-the-art and cost-efficient web navigation performance—while releasing both the model weights and evaluation dataset.

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

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [CUA], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [UI-Evol: Automatic Knowledge Evolving for Computer Use Agents](https://arxiv.org/abs/2505.21964)
    - Ziyun Zhang, Xinyi Liu, Xiaoyi Zhang, Jun Wang, Gang Chen, Yan Lu
    - 🏛️ Institutions: Peking University, Microsoft Research Asia
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [knowledge-execution gap], [Critique Stage], [Retrace Stage], [OSWorld], [self‑evolution]
    - 📖 TLDR: The paper identifies a “knowledge‑execution gap” where even highly accurate external knowledge (90%) only yields a 41% execution success rate. To bridge this, the authors introduce **UI‑Evol**, a plug‑and‑play two‑stage module for GUI agents—**Retrace** recovers actual action sequences from real agent–environment interactions, and **Critique** refines knowledge by comparing these sequences with external references. Experiments using Agent S2 on the OSWorld benchmark show significant gains in task performance and reduced behavioral variance, improving agent reliability.

- [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)
    - Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: May 28, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [information seeking], [reinforcement learning], [GAIA], [WebDancer]
    - 📖 TLDR: This paper presents WebDancer, an end-to-end web agent for autonomous information seeking built through a data-centric four-stage training pipeline: browsing data construction, trajectory sampling, supervised fine-tuning, and reinforcement learning. It targets long-horizon information-seeking problems rather than short templated web tasks. The resulting system achieves strong performance on GAIA and WebWalkerQA and offers a concrete recipe for training more capable research-style web agents.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reward model], [self-improvement], [synthetic data], [mobile GUI agent], [UI-Genie-RM], [UI-Genie-Agent]
    - 📖 TLDR: This paper introduces UI-Genie, a self-improving mobile GUI-agent framework that tackles two bottlenecks at once: outcome verification and scalable high-quality trajectory generation. It builds a dedicated reward model, UI-Genie-RM, plus a reward-guided self-improvement loop that iteratively upgrades both the agent and the reward model in dynamic environments. The paper also releases the first reward-specific GUI-agent dataset and reports state-of-the-art performance across multiple mobile GUI benchmarks after several generations of self-improvement.

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

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, and Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [model context protocol], [MCP], [OSWorld], [LiteCUA]
    - 📖 TLDR: Introduces AIOS 1.0, which contextualizes desktop computer states via an MCP server so LLM-powered agents can better understand and operate GUIs. Built on top, LiteCUA—a lightweight agent—achieves 14.66 % success on the OSWorld benchmark, outperforming several heavier agent frameworks, showing the benefits of environment contextualization.

- [SE-GUI: Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: VCIP, School of Computer Science, Nankai University, vivo Mobile Communication Co., Ltd
    - 📅 Date: May 24, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [visual grounding], [ScreenSpot-Pro], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [Unlocking Smarter Device Control: Foresighted Planning with a World Model-Driven Code Execution Approach](https://arxiv.org/abs/2505.16422)
    - Xiaoran Yin, Xu Luo, Hao Wu, Lianli Gao, Jingkuan Song
    - 🏛️ Institutions: University of Electronic Science and Technology of China, Tongji University, University of Trento
    - 📅 Date: May 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [world model], [executable code], [self‑verification], [self‑refinement], [FPWC]
    - 📖 TLDR: This paper introduces **Foresighted Planning with World Model-Driven Code Execution** (FPWC), a novel framework that improves multi-step mobile device control by constructing a text-based, refinable world model at task start. Plans are generated as executable Python code enabling structured reasoning, loops, and conditional logic. The system dynamically self-verifies via zoom-in visual confirmation and iteratively refines both model and plan based on new observations. Experiments in simulation and on real devices show ~44% relative improvement in task success over prior reactive baselines, demonstrating strong performance in both single- and cross-app tasks.

- [GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://aclanthology.org/2025.acl-long.282/)
    - Bin Xie, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Jie Liu, Min Zhang, Liqiang Nie
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Huawei Noah's Ark Lab
    - 📅 Date: May 22, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [transition-aware knowledge], [autonomous exploration], [benchmark], [GUI-KRB]
    - 📖 TLDR: Introduces **GUI‑explorer**, a training‑free agent for mobile GUIs that auto‑generates function‑aware exploration goals and mines transition‑aware knowledge from UI transitions. It builds a multimodal knowledge store and dynamically guides MLLMs like GPT‑4o at runtime, achieving state‑of‑the‑art success rates (53.7% on SPA‑Bench, 47.4% on AndroidWorld) without retraining. Also introduces GUI‑KRB, a benchmark highlighting GUI reasoning limitations and guiding future work.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Gaoling School of Artificial Intelligence, Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [visual grounding], [reinforcement learning], [ScreenSpot], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

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
    - 🔑 Key: [dataset], [benchmark], [framework], [Jedi], [OSWorld‑G], [GUI grounding], [compositional generalization], [fine‑grained manipulation]
    - 📖 TLDR: This work tackles limitations in GUI grounding by introducing **OSWorld‑G**, a 564‑sample benchmark covering text matching, element recognition, layout understanding, fine‑grained manipulation, and refusal detection. They also synthesize **Jedi**, a massive 4 M‑example dataset generated via UI decomposition and synthesis. Training multi‑scale models on Jedi achieves state‑of‑the‑art grounding across benchmarks (ScreenSpot‑v2/Pro and OSWorld‑G), boosting agentic task performance from 5 % to ~27 % success. Ablations demonstrate compositional benefits. All artifacts are publicly released.

- [ScaleTrack: Scaling and back-tracking Automated GUI Agents](https://arxiv.org/abs/2505.00416)
    - Jing Huang, Zhixiong Zeng, Wenkang Han, Yufeng Zhong, Liming Zheng, Shuai Fu, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, University of Adelaide
    - 📅 Date: May 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [training strategy], [back-tracking], [grounding], [planning], [ScaleTrack]
    - 📖 TLDR: This paper introduces *ScaleTrack*, a training framework designed to enhance automated GUI agents by addressing two primary challenges: insufficient training data for GUI grounding and the lack of back-tracking in GUI planning. The authors aggregate diverse GUI samples from various synthesis methods into a unified template to scale the grounding process. Additionally, they propose a hybrid training strategy that combines forward-planning and back-tracking, enabling the agent to predict both the next action and the historical actions leading to the current GUI state. Experimental results demonstrate that ScaleTrack significantly improves task success rates across multiple benchmarks, highlighting the effectiveness of integrating back-tracking into GUI agent training.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: UMich, LG AI Research
    - 📅 Date: May 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [RegionFocus], [test-time scaling], [grounding], [Qwen2.5-VL], [UI-TARS]
    - 📖 TLDR: This paper introduces *RegionFocus*, a visual test-time scaling method for GUI agents that dynamically zooms into relevant regions within GUI images, reducing background clutter and enhancing grounding accuracy. By integrating an "image-as-map" mechanism to visualize key landmarks during each interaction step, the approach improves transparency and decision-making. Applied to state-of-the-art vision-language models like UI-TARS and Qwen2.5-VL, RegionFocus achieves significant performance gains—28% on ScreenSpot-Pro and 24% on WebVoyager benchmarks—setting a new state-of-the-art grounding accuracy of 61.6% on ScreenSpot-Pro.

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

- [Infogent: An Agent-Based Framework for Web Information Aggregation](https://aclanthology.org/2025.findings-naacl.318/)
    - Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tur, Heng Ji
    - 🏛️ Institutions: University of Illinois at Urbana-Champaign
    - 📅 Date: April 29, 2025
    - 📑 Publisher: Findings of NAACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [information aggregation], [browser navigation], [AssistantBench], [Infogent]
    - 📖 TLDR: This paper targets web information aggregation rather than single-site task completion, asking agents to explore multiple websites and decide when enough evidence has been gathered for a complex query. It introduces Infogent, a modular framework with Navigator, Extractor, and Aggregator components, plus enhanced actions for backtracking and feedback-driven navigation. The framework improves over prior baselines in both API-driven and interactive visual web-access settings, including gains on AssistantBench.

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
    - 🔑 Key: [framework], [dataset], [benchmark], [Qwen2.5-VL], [GUI-Net], [multimodal], [trajectory generation]
    - 📖 TLDR: This paper introduces **TongUI**, a framework for building generalized GUI agents by learning from multimodal web tutorials. By crawling and processing online tutorials into GUI agent trajectory data, the authors construct the **GUI-Net** dataset containing 143K trajectories across five operating systems and over 200 applications. Fine-tuning Qwen2.5-VL-3B/7B models on GUI-Net leads to significant performance improvements on grounding and navigation benchmarks, demonstrating the effectiveness of the TongUI framework.

- [UI-E2I-Synth: Advancing GUI Grounding with Large-Scale Instruction Synthesis](https://aclanthology.org/2025.findings-acl.809/)
    - Xinyi Liu, Xiaoyi Zhang, Ziyun Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia, Peking University
    - 📅 Date: April 15, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [instruction synthesis], [UI-E2I-Synth], [UI-I2E-Bench], [GPT-4o]
    - 📖 TLDR: This paper introduces **UI-E2I-Synth**, a large-scale data synthesis pipeline that generates diverse GUI grounding instructions using GPT-4o, addressing challenges like implicit instructions and unbalanced element types. It also presents **UI-I2E-Bench**, a new benchmark with detailed annotations for evaluating GUI instruction grounding. Models trained on the synthesized data demonstrate superior performance across multiple platforms, highlighting the effectiveness of the proposed approach.

- [REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)
    - Divyansh Garg, Shaun VanWeelden, Diego Caples, Andis Draguns, Nikil Ravi, Pranav Putta, Naman Garg, Tomas Abraham, Michael Lara, Federico Lopez, James Liu, Atharva Gundawar, Prannay Hebbar, Youngchul Joo, Jindong Gu, Charles London, Christian Schroeder de Witt, Sumeet Motwani
    - 🏛️ Institutions: The AGI Company, Stanford University, University of Oxford, Mercor, Contramont Research, Plato, Independent
    - 📅 Date: April 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [dataset], [evaluation], [reproducibility], [multi-turn tasks], [REAL]
    - 📖 TLDR: This paper introduces **REAL**, a benchmark and framework designed for evaluating autonomous agents through deterministic simulations of real-world websites. REAL encompasses high-fidelity replicas of 11 widely-used websites across domains like e-commerce, travel, communication, and professional networking. It includes 112 practical tasks that mirror complex user interactions requiring both accurate information retrieval and state-changing actions. The controlled environment ensures safety and reproducibility, combining programmatic checks for action-based tasks with rubric-guided LLM-based judgments for information retrieval. Empirical results reveal that current frontier language models achieve at most a 41% success rate on REAL, highlighting significant gaps in autonomous web navigation and task completion capabilities.

- [GUI-R1: A Generalist R1-Style Vision-Language Action Model for GUI Agents](https://arxiv.org/abs/2504.10458)
    - Run Luo, Lu Wang, Wanwei He, Longze Chen, Jiaming Li, Min Yang, Xiaobo Xia
    - 🏛️ Institutions: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences, National University of Singapore
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [GRPO], [GUI-R1]
    - 📖 TLDR: GUI-R1 introduces a reinforcement learning framework that enhances the capabilities of Large Vision-Language Models (LVLMs) for GUI agents. By employing a unified action space and a rule-based reward function, the model efficiently learns to perform high-level tasks across multiple platforms, including Windows, Linux, MacOS, Android, and Web. Utilizing only 0.02% of the data compared to previous methods, GUI-R1 demonstrates superior performance on eight benchmarks, showcasing the potential of reinforcement learning in GUI agent tasks.

- [Breaking the Data Barrier -- Building GUI Agents Through Task Generalization](https://openreview.net/forum?id=QDtORaZt8K)
    - Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, Qiushi Sun, Zhenzhong Lan, Junxian He
    - 🏛️ Institutions: Zhejiang University, Westlake University, Shanghai AI Laboratory, The University of Hong Kong, Hong Kong University of Science and Technology
    - 📅 Date: April 14, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [mid-training], [reasoning], [GUIMid]
    - 📖 TLDR: This paper introduces a mid-training approach to enhance GUI agents by leveraging diverse, reasoning-intensive datasets such as mathematical and coding tasks. The authors demonstrate that training Vision Language Models (VLMs) on these data-rich tasks before fine-tuning on limited GUI trajectory data significantly improves performance on GUI benchmarks like WebArena and AndroidWorld. Notably, text-only mathematical reasoning data led to substantial cross-modal gains, highlighting the effectiveness of task generalization in overcoming data scarcity challenges in GUI agent development.

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

- [ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation](https://aclanthology.org/2025.naacl-long.244/)
    - Qinzhuo Wu, Wei Liu, Jian Luan, Bin Wang
    - 🏛️ Institutions: XiaoMi AI Lab
    - 📅 Date: April 2025
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile GUI agent], [page reaching], [task decomposition], [ReachAgent], [MobileReach]
    - 📖 TLDR: This paper argues that mobile agents often optimize locally for the next UI action while missing the larger GUI flow needed to finish a task. It introduces MobileReach, a dataset that decomposes tasks into page-reaching and page-operation subtasks, and trains ReachAgent as a two-stage framework over those subtasks plus reward-based preference flows. The result is stronger step-level and task-level accuracy than prior mobile-agent baselines.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 1, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [Mixture-of-Grounding], [Proactive Hierarchical Planning], [benchmark], [OSWorld], [WindowsAgentArena], [AndroidWorld]
    - 📖 TLDR: This paper introduces *Agent S2*, a compositional framework for computer use agents that combines generalist and specialist models to address challenges in GUI element grounding and long-horizon task planning. The framework employs a novel Mixture-of-Grounding technique for precise GUI localization and Proactive Hierarchical Planning to dynamically refine action plans. Evaluations demonstrate that Agent S2 achieves state-of-the-art performance on benchmarks like OSWorld, WindowsAgentArena, and AndroidWorld, outperforming existing agents such as Claude Computer Use and UI-TARS.

- [A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350)
    - Liangbo Ning, Ziran Liang, Zhuohang Jiang, Haohao Qu, Yujuan Ding, Wenqi Fan, Xiao-yong Wei, Shanru Lin, Hui Liu, Philip S. Yu, Qing Li
    - 🏛️ Institutions: The Hong Kong Polytechnic University, City University of Hong Kong, Michigan State University, University of Illinois Chicago
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [survey], [framework], [training], [trustworthiness], [WebAgents], [Large Foundation Models]
    - 📖 TLDR: This comprehensive survey examines the development of WebAgents—AI agents designed to automate web tasks—by leveraging Large Foundation Models (LFMs). It delves into the architectures, training methodologies, and trustworthiness of these agents, providing a detailed overview of current research and proposing future directions to enhance their effectiveness and reliability in web automation.

- [UI-R1: Enhancing Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, The Chinese University of Hong Kong
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [UI-R1-3B], [GRPO], [AndroidControl], [ScreenSpot-Pro]
    - 📖 TLDR: This paper introduces **UI-R1**, a framework that enhances the reasoning capabilities of multimodal large language models (MLLMs) for GUI action prediction tasks through rule-based reinforcement learning. Utilizing a small, high-quality dataset of 136 challenging mobile tasks, the authors design a unified rule-based action reward function and optimize the model using Group Relative Policy Optimization (GRPO). The resulting model, **UI-R1-3B**, demonstrates significant improvements over the base model (Qwen2.5-VL-3B) on both in-domain (AndroidControl) and out-of-domain (ScreenSpot-Pro) benchmarks, showcasing the effectiveness of rule-based RL in advancing GUI understanding and control.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Tsinghua University, Nanyang Technological University, The University of Texas at Austin
    - 📅 Date: March 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [benchmark], [V-Droid], [verifier-driven], [pair-wise preference training], [human-agent joint annotation], [low-latency]
    - 📖 TLDR: This paper introduces **V-Droid**, a mobile GUI automation agent that leverages large language models (LLMs) as verifiers rather than generators. By evaluating candidate actions before execution, V-Droid enhances decision-making accuracy and reduces latency. The framework incorporates discretized action space construction, a prefilling-only workflow, pair-wise preference training, and a scalable human-agent joint annotation scheme. Evaluated on benchmarks like AndroidWorld, AndroidLab, and MobileAgentBench, V-Droid achieves state-of-the-art success rates and operates with near-real-time decision-making capabilities.

- [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661)
    - Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Juan A. Rodriguez, Montek Kalsi, Rabiul Awal, Nicolas Chapados, M. Tamer Özsu, Aishwarya Agrawal, David Vazquez, Christopher Pal, Perouz Taslakian, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, Universite de Montreal, ServiceNow, University of Waterloo, National University of Singapore, Ecole de Technologie Superieure, CIFAR AI Chair, Polytechnique Montreal
    - 📅 Date: March 19, 2025
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [framework], [UI-Vision], [UI-TARS-72B], [spatial reasoning], [drag-and-drop], [element grounding], [layout grounding], [action prediction]
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
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [model], [AutoCaptioner], [DeskVision], [DeskVision-Eval], [GUIExplorer]
    - 📖 TLDR: This paper introduces *AutoCaptioner*, an automated pipeline for generating richly annotated GUI data with minimal human effort. Utilizing AutoCaptioner, the authors created *DeskVision*, a large-scale desktop GUI dataset comprising 54,855 images and over 303,622 annotations across various operating systems. They also developed *DeskVision-Eval*, the largest desktop benchmark reflecting daily usage scenarios. Leveraging DeskVision, the authors trained *GUIExplorer*, a GUI understanding model that achieves state-of-the-art performance in grounding visual elements without complex architectural designs. The effectiveness of DeskVision was further validated through ablation studies on various large visual language models (LVLMs).

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
    - 🔑 Key: [framework], [dataset], [benchmark], [dual-system cognition], [FOCUS], [ScreenSpot], [ScreenSpot-Pro]
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
    - 💻 Env: [GUI], [Robotics]
    - 🔑 Key: [model], [framework], [SoM], [ToM], [robotics], [UI navigation]
    - 📖 TLDR: This paper introduces **Magma**, a foundation model designed for multimodal AI agents operating in both digital and physical environments. Magma extends traditional vision-language models by incorporating planning and action capabilities, enabling tasks from UI navigation to robotic manipulation. The model is pretrained on diverse datasets, including images, videos, and robotics data, utilizing **Set-of-Mark (SoM)** for action grounding and **Trace-of-Mark (ToM)** for action planning. Experiments demonstrate that SoM and ToM synergistically enhance Magma's spatial-temporal intelligence, achieving state-of-the-art performance in UI navigation and robotic manipulation tasks.

- [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents](https://aclanthology.org/2025.findings-acl.326/)
    - Vardaan Pahuja, Yadong Lu, Corby Rosset, Boyu Gou, Arindam Mitra, Spencer Whitehead, Yu Su, Ahmed Hassan Awadallah
    - 🏛️ Institutions: Microsoft Research, The Ohio State University
    - 📅 Date: February 17, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [web agents], [reinforcement learning], [Explorer]
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
    - 🔑 Key: [framework], [Auto-Annotation], [federated learning], [privacy], [non-IID], [adapted aggregation]
    - 📖 TLDR: This paper introduces *MobileA3gent*, a framework for training mobile GUI agents using decentralized, self-sourced data from diverse users. It addresses challenges in extracting user instructions without human intervention and utilizing distributed data while preserving privacy. The framework comprises two key techniques: *Auto-Annotation*, which automatically collects high-quality datasets during users' routine phone usage, and *FedVLM-A*, which enhances federated training on non-IID user data by incorporating both episode- and step-level distributions. Experiments demonstrate that MobileA3gent achieves performance comparable to centralized human-annotated models at less than 1% of the cost, highlighting its potential for real-world applications.

- [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)
    - Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Deyu Zhou, Pengjun Xie, Fei Huang
    - 🏛️ Institutions: Tongyi Lab, Alibaba NLP
    - 📅 Date: January 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [RAG], [WebWalker], [WebWalkerQA]
    - 📖 TLDR: This paper presents **WebWalker**, a multi-agent framework designed to improve the ability of large language models (LLMs) to traverse websites, addressing the challenges of retrieving complex, multi-layered information. WebWalker integrates an "explore-critic" paradigm, where the explorer agent navigates the web, and the critic agent evaluates the progress. The **WebWalkerQA** benchmark is introduced to assess web traversal tasks, showing how retrieval-augmented generation (RAG) can be enhanced with vertical exploration to solve real-world queries.

- [PC Agent: While You Sleep, AI Works -- A Cognitive Journey into Digital World](https://arxiv.org/abs/2412.17589)
    - Yanheng He, Jiahe Jin, Shijie Xia, Jiadi Su, Runze Fan, Haoyang Zou, Xiangkun Hu, Pengfei Liu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: Dec 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [PC Agent], [human cognition transfer], [PC Tracker], [Cognition Completion], [multi-agent system]
    - 📖 TLDR: This paper introduces *PC Agent*, an AI system designed to autonomously perform complex computer-based tasks by emulating human cognitive processes. The system comprises three key components: **PC Tracker**, a lightweight infrastructure for collecting high-quality human-computer interaction data; a **Cognition Completion** pipeline that enriches raw interaction data into detailed cognitive trajectories; and a **multi-agent system** combining a planning agent for decision-making with a grounding agent for precise visual grounding. This approach represents a significant advancement toward AI systems capable of handling intricate real-world work autonomously.

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
    - 🔑 Key: [framework], [Information-Sensitive Cropping], [Self-Refining Dual Learning], [visual grounding], [model]
    - 📖 TLDR: This paper introduces *Iris*, a visual agent designed to enhance GUI automation by addressing challenges in high-resolution, complex digital environments. It employs two key innovations: **Information-Sensitive Cropping (ISC)**, which dynamically identifies and prioritizes visually dense regions using an edge detection algorithm for efficient processing, and **Self-Refining Dual Learning (SRDL)**, which enhances the agent's ability to handle complex tasks through a dual-learning loop that iteratively refines its performance without requiring additional annotated data. Empirical evaluations demonstrate that Iris achieves state-of-the-art performance across multiple benchmarks with only 850K GUI annotations, outperforming methods using ten times more training data.

- [The BrowserGym Ecosystem for Web Agent Research](https://openreview.net/forum?id=5298fKGmv3)
    - Thibault Le Sellier De Chezelles, Maxime Gasse, Alexandre Drouin, Massimo Caccia, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Quentin Cappart, Graham Neubig, Ruslan Salakhutdinov, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Carnegie Mellon University, McGill University, Tel Aviv University, Université de Montréal, iMean AI
    - 📅 Date: December 6, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [LLM], [automation], [BrowserGym], [AgentLab]
    - 📖 TLDR: This paper presents *BrowserGym*, an ecosystem designed to standardize the evaluation and benchmarking of web agents, particularly those leveraging Large Language Models (LLMs). It addresses the challenges posed by fragmented benchmarks and inconsistent methodologies in web agent research. BrowserGym provides a unified, gym-like environment with clearly defined observation and action spaces, enabling reproducible comparisons across various benchmarks. Additionally, *AgentLab*, a complementary framework, supports agent creation, testing, and analysis. The paper also features a large-scale experiment comparing the performance of 6 leading LLMs, highlighting the strengths and weaknesses of different models in real-world web tasks, while emphasizing the ongoing challenges in building efficient and robust web agents.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://aclanthology.org/2025.findings-acl.76/)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: December 2, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [reinforcement learning], [Ponder & Press]
    - 📖 TLDR: This paper introduces *Ponder & Press*, a divide-and-conquer framework for general computer control using only visual input. The approach combines a general-purpose multimodal large language model (MLLM) as an 'interpreter' to translate high-level user instructions into detailed action descriptions, with a GUI-specific MLLM as a 'locator' that precisely identifies GUI elements for action execution. By relying solely on visual inputs, the agent offers a versatile, human-like interaction paradigm applicable across various platforms, achieving state-of-the-art performance in GUI grounding and control tasks.

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [UI-Guided Visual Token Selection], [Interleaved Vision-Language-Action Streaming], [ShowUI]
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

- [The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](https://arxiv.org/abs/2411.10323)
    - Siyuan Hu, Mingyu Ouyang, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: Nov 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [Claude 3.5 Computer Use], [GUI automation], [planning], [action], [critic]
    - 📖 TLDR: This study evaluates Claude 3.5 Computer Use, an AI model enabling end-to-end language-to-desktop actions, through curated tasks across various domains. It introduces an out-of-the-box framework for deploying API-based GUI automation models, analyzing the model's planning, action execution, and adaptability to dynamic environments.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://openreview.net/forum?id=c6l7yA0HSq)
    - Yu Gu, Kai Zhang, Yuting Ning, Boyuan Zheng, Boyu Gou, Tianci Xue, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [WebDreamer], [model-based planning], [world model]
    - 📖 TLDR: This paper investigates whether Large Language Models (LLMs) can function as world models within web environments, enabling model-based planning for web agents. Introducing **WebDreamer**, a framework that leverages LLMs to simulate potential action sequences in web environments, the study demonstrates significant performance improvements over reactive baselines on benchmarks like VisualWebArena and Mind2Web-live. The findings suggest that LLMs possess the capability to model the dynamic nature of the internet, paving the way for advancements in automated web interaction and opening new research avenues in optimizing LLMs for complex, evolving environments.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://openreview.net/forum?id=oVKEAFjEqv)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Jiadai Sun, Xinyue Yang, Yu Yang, Shuntian Yao, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Shanghai Qi Zhi Institute
    - 📅 Date: November 4, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [self-evolving curriculum], [WebRL], [outcome-supervised reward model]
    - 📖 TLDR: This paper introduces *WebRL*, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open large language models (LLMs). WebRL addresses challenges such as the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. It incorporates a self-evolving curriculum that generates new tasks from unsuccessful attempts, a robust outcome-supervised reward model (ORM), and adaptive reinforcement learning strategies to ensure consistent improvements. Applied to Llama-3.1 and GLM-4 models, WebRL significantly enhances their performance on web-based tasks, surpassing existing state-of-the-art web agents.

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

- [Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/abs/2410.22552)
    - Jaekyeom Kim, Dong-Ki Kim, Lajanugen Logeswaran, Sungryull Sohn, Honglak Lee
    - 🏛️ Institutions: LG AI Research, Field AI, University of Michigan
    - 📅 Date: October 29, 2024
    - 📑 Publisher: EMNLP 2024 (Findings)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [Auto-Intent]
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

- [Lightweight Neural App Control](https://openreview.net/forum?id=BL4WBIfyrz)
    - Filippos Christianos, Georgios Papoudakis, Thomas Coste, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 23, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [vision language model], [Action Transformer], [app agent], [Android control], [multi-modal]
    - 📖 TLDR: This paper introduces LiMAC, a mobile control framework for Android that integrates an Action Transformer and fine-tuned vision-language models to execute precise actions in mobile apps. Tested on open-source datasets, LiMAC improves action accuracy by up to 42% over traditional prompt engineering baselines, demonstrating enhanced efficiency and accuracy in mobile app control tasks.

- [Large Language Models Empowered Personalized Web Agents](https://openreview.net/forum?id=kAzqfqsCC5)
    - Hongru Cai, Yongqi Li, Wenjie Wang, Fengbin Zhu, Xiaoyu Shen, Wenjie Li, Tat-Seng Chua
    - 🏛️ Institutions: The Hong Kong Polytechnic University, Nanyang Technological University
    - 📅 Date: Oct 22, 2024
    - 📑 Publisher: WWW 2025 (Oral)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [personalized web agent], [user behavior alignment], [memory-enhanced alignment]
    - 📖 TLDR: This paper proposes a novel framework, *Personalized User Memory-enhanced Alignment (PUMA)*, enabling large language models to serve as personalized web agents by incorporating user-specific data and historical web interactions. The authors also introduce a benchmark, *PersonalWAB*, to evaluate these agents on various personalized web tasks. Results show that PUMA improves web agent performance by optimizing action execution based on user-specific preferences.

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
    - 🔑 Key: [framework], [reinforcement learning], [distributed training], [A-RIDE], [on-device control]
    - 📖 TLDR: This paper introduces **DistRL**, a novel framework designed to enhance the efficiency of online reinforcement learning fine-tuning for mobile device control agents. DistRL employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in dynamic online interactions. The framework is supported by a custom RL algorithm, A-RIDE, which balances exploration with prioritized data utilization to ensure stable and robust training. Experiments demonstrate that DistRL improves training efficiency by 3× and accelerates data collection by 2.4× compared to leading synchronous multi-machine methods. Notably, after training, DistRL achieves a 20% relative improvement in success rate on general Android tasks from an open benchmark, outperforming existing approaches while maintaining the same training time.

- [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab87cdfe514bf8f9c07e5e7aa247f55f-Abstract-Conference.html)
    - Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular, Carnegie Mellon University
    - 📅 Date: October 10, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI agent], [hierarchical planning], [retrieval-augmented planning], [Agent-Computer Interface], [Agent S]
    - 📖 TLDR: This paper introduces Agent S, an open agentic framework that enables autonomous interaction with computers through a Graphical User Interface (GUI). The system addresses key challenges in automating computer tasks through experience-augmented hierarchical planning and an Agent-Computer Interface (ACI). Agent S demonstrates significant improvements over baselines on the OSWorld benchmark, achieving a 20.58% success rate (83.6% relative improvement). The framework shows generalizability across different operating systems and provides insights for developing more effective GUI agents.

- [ClickAgent: Enhancing UI Location Capabilities of Autonomous Agents](https://aclanthology.org/2025.sigdial-1.38/)
    - Jakub Hoscilowicz, Bartosz Maj, Bartosz Kozakiewicz, Oleksii Tymoshchuk, Artur Janicki
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 9, 2024
    - 📑 Publisher: SIGDIAL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI grounding], [mobile agent], [AITW], [InternVL2], [TinyClick], [ClickAgent]
    - 📖 TLDR: The paper introduces *ClickAgent*, a framework that enhances autonomous agents' interaction with mobile UIs by improving their ability to locate interface elements accurately. This is achieved through a dual-component system where an MLLM performs reasoning and action planning, while a dedicated UI location model (e.g., SeeClick) handles element identification. ClickAgent, evaluated on the AITW benchmark and tested on both emulators and real Android devices, surpasses other agents like CogAgent and AppAgent in task success rate, advancing automation reliability on mobile platforms.

- [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html)
    - Xiao Yu, Baolin Peng, Vineeth Vajipey, Hao Cheng, Michel Galley, Jianfeng Gao, Zhou Yu
    - 🏛️ Institutions: Columbia University, Microsoft Research
    - 📅 Date: October 2, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [tree search], [self-improvement], [R-MCTS], [Exploratory Learning], [VisualWebArena]
    - 📖 TLDR: This paper introduces ExACT, an approach that combines Reflective Monte Carlo Tree Search (R-MCTS) and Exploratory Learning to enhance AI agents' exploration and decision-making capabilities in complex web environments. R-MCTS incorporates contrastive reflection and multi-agent debate for improved search efficiency and reliable state evaluation. Evaluated on the VisualWebArena benchmark, the GPT-4o-based R-MCTS agent demonstrates significant performance improvements over previous state-of-the-art methods. Additionally, knowledge gained from test-time search is effectively transferred back to GPT-4o through fine-tuning, enabling the model to explore, evaluate, and backtrack without external search algorithms, achieving 87% of R-MCTS's performance with reduced computational resources.

- [Dynamic Planning for LLM-based Graphical User Interface Automation](https://aclanthology.org/2024.findings-emnlp.70/)
    - Shaoqing Zhang, Zhuosheng Zhang, Kehai Chen, Xinbei Ma, Muyun Yang, Tiejun Zhao, Min Zhang
    - 🏛️ Institutions: Harbin Institute of Technology, Shanghai Jiao Tong University
    - 📅 Date: October 1, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dynamic planning], [D-PoT], [mobile agent]
    - 📖 TLDR: This paper introduces a novel method called Dynamic Planning of Thoughts (D-PoT) aimed at enhancing LLM-based agents for GUI tasks. It addresses the challenges of task execution by dynamically adjusting planning based on environmental feedback and action history, outperforming existing methods such as ReAct by improving accuracy significantly in navigating GUI environments. The study emphasizes the importance of integrating execution history and contextual cues to optimize decision-making processes for autonomous agents.

- [AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://aclanthology.org/2025.acl-long.381/)
    - Junting Lu, Zhiyang Zhang, Fangkai Yang, Jue Zhang, Lu Wang, Chao Du, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Peking University, Nanjing University, Microsoft
    - 📅 Date: September 26, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [API-first], [AXIS], [HACI], [Agent OS]
    - 📖 TLDR: This paper proposes an API-centered framework called **AXIS**, enhancing the efficiency and reliability of LLM-based agents by prioritizing API interactions over UI-based actions. This approach aims to reduce the high latency and error rates of traditional UI-interaction models. AXIS not only supports the rapid creation and extension of APIs through automated application exploration but also contributes to a new **Human-Agent-Computer Interaction (HACI)** framework. The paper outlines the development of an agent-centric operating system (Agent OS), which improves task completion times by up to 70% and reduces cognitive load on users while maintaining high accuracy across complex multi-application tasks.

- [Turn Every Application into an Agent: Towards Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://arxiv.org/abs/2409.17140)
    - Junting Lu, Zhiyang Zhang, Fangkai Yang, Jue Zhang, Lu Wang, Chao Du, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Peking University, Microsoft
    - 📅 Date: September 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [API interaction], [HACI], [Agent OS]
    - 📖 TLDR: This paper proposes an API-centered framework called **AXIS**, enhancing the efficiency and reliability of LLM-based agents by prioritizing API interactions over UI-based actions. This approach aims to reduce the high latency and error rates of traditional UI-interaction models. AXIS not only supports the rapid creation and extension of APIs through automated application exploration but also contributes to a new **Human-Agent-Computer Interaction (HACI)** framework. The paper outlines the development of an agent-centric operating system (Agent OS), which improves task completion times by up to 70% and reduces cognitive load on users while maintaining high accuracy across complex multi-application tasks.

- [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://proceedings.mlr.press/v267/bonatti25a.html)
    - Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, Yadong Lu, Justin Wagle, Kazuhito Koishida, Arthur Bucker, Lawrence Keunho Jang, Zheng Hui
    - 🏛️ Institutions: Microsoft
    - 📅 Date: September 13, 2024
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [desktop agent], [Windows OS], [Navi], [Windows Agent Arena]
    - 📖 TLDR: This paper introduces the *Windows Agent Arena (WAA)*, a scalable platform for testing and benchmarking multi-modal AI agents within a realistic Windows OS environment. WAA enables researchers to evaluate agentic workflows across diverse tasks and supports large-scale deployment using Azure ML. The study also presents *Navi*, a multi-modal agent achieving a 19.5% success rate on Windows tasks, highlighting the platform's potential for advancing AI agent development.

- [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
    - Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University, Massachusetts Institute of Technology
    - 📅 Date: September 11, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [memory], [workflow induction], [web navigation], [AWM]
    - 📖 TLDR: The paper proposes *Agent Workflow Memory (AWM)*, a method enabling language model-based agents to induce and utilize reusable workflows from past experiences to guide future actions in web navigation tasks. AWM operates in both offline and online settings, significantly improving performance on benchmarks like Mind2Web and WebArena, and demonstrating robust generalization across tasks, websites, and domains.

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
    - 🔑 Key: [framework], [Monte Carlo Tree Search], [reinforcement learning], [WebPilot]
    - 📖 TLDR: This paper introduces **WebPilot**, a multi-agent system designed to execute complex web tasks requiring dynamic interaction. By employing a dual optimization strategy grounded in Monte Carlo Tree Search (MCTS), WebPilot enhances adaptability in complex web environments. The system's Global Optimization phase generates high-level plans by decomposing tasks into manageable subtasks, while the Local Optimization phase executes each subtask using a tailored MCTS approach. Experimental results on WebArena and MiniWoB++ demonstrate WebPilot's effectiveness, achieving state-of-the-art performance with GPT-4 and marking a significant advancement in autonomous web agent capabilities.

- [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199)
    - Pranav Putta, Edmund Mills, Naman Garg, Sumeet Ramesh Motwani, Elan Sopher Markowitz, Julia Kiseleva, Chelsea Finn, Divyansh Garg, Rafael Rafailov
    - 🏛️ Institutions: MultiOn, Stanford University
    - 📅 Date: August 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [MCTS], [tree search], [DPO], [reinforcement learning], [web navigation], [Agent Q]
    - 📖 TLDR: TBD

- [AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/abs/2408.11824)
    - Yanda Li, Chi Zhang, Wenjia Jiang, Wanqi Yang, Bin Fu, Pei Cheng, Xin Chen, Ling Chen, Yunchao Wei
    - 🏛️ Institutions: University of Technology Sydney, Tencent, Beijing Jiaotong University, Westlake University
    - 📅 Date: August 5, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [mobile agent], [knowledge base], [RAG], [AppAgent v2]
    - 📖 TLDR: This work presents *AppAgent v2*, a novel LLM-based multimodal agent framework for mobile devices capable of navigating applications by emulating human-like interactions such as tapping and swiping. The agent constructs a flexible action space that enhances adaptability across various applications, including parsing text and vision descriptions. It operates through two main phases: exploration and deployment, utilizing retrieval-augmented generation (RAG) technology to efficiently retrieve and update information from a knowledge base, thereby empowering the agent to perform tasks effectively and accurately.

- [CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://aclanthology.org/2024.findings-acl.539)
    - Xinbei Ma, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: August 2024
    - 📑 Publisher: Findings of ACL 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [smartphone automation], [comprehensive environment perception], [conditional action prediction], [CoCo-Agent]
    - 📖 TLDR: This paper presents CoCo-Agent, a multimodal large language model (MLLM) designed for smartphone GUI automation. It introduces two novel approaches: Comprehensive Environment Perception (CEP) for enhanced GUI understanding, and Conditional Action Prediction (CAP) to improve action response accuracy. The proposed agent achieves state-of-the-art performance on GUI automation benchmarks such as AITW and META-GUI, showcasing its capabilities in realistic scenarios.

- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203)
    - Yadong Lu, Jianwei Yang, Yelong Shen, Ahmed Awadallah
    - 🏛️ Institutions: Microsoft Research, Microsoft GenAI
    - 📅 Date: August 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [OmniParser]
    - 📖 TLDR: This paper introduces **OmniParser**, a method for parsing user interface screenshots into structured elements, enhancing the ability of models like GPT-4V to generate actions accurately grounded in corresponding UI regions. The authors curated datasets for interactable icon detection and icon description, fine-tuning models to parse interactable regions and extract functional semantics of UI elements.

- [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://openreview.net/forum?id=xgtXkyqw1f)
    - Zehui Chen, Kuikun Liu, Qiuchen Wang, Jiangning Liu, Wenwei Zhang, Kai Chen, Feng Zhao
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory
    - 📅 Date: July 29, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [information seeking], [planning], [AI search], [MindSearch]
    - 📖 TLDR: This paper presents MindSearch, a novel approach to web information seeking and integration that mimics human cognitive processes. The system uses a multi-agent framework consisting of a WebPlanner and WebSearcher. The WebPlanner models multi-step information seeking as a dynamic graph construction process, decomposing complex queries into sub-questions. The WebSearcher performs hierarchical information retrieval for each sub-question. MindSearch demonstrates significant improvements in response quality and depth compared to existing AI search solutions, processing information from over 300 web pages in just 3 minutes.

- [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032)
    - Tamer Abuelsaad, Deepak Akkil, Prasenjit Dey, Ashish Jagmohan, Aditya Vempaty, Ravi Kokku
    - 🏛️ Institutions: Emergence AI
    - 📅 Date: July 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [hierarchical architecture], [DOM distillation], [change observation], [self-improvement], [Agent-E]
    - 📖 TLDR: This paper presents Agent-E, a novel web agent that introduces several architectural improvements over previous state-of-the-art systems. Key features include a hierarchical architecture, flexible DOM distillation and denoising methods, and a "change observation" concept for improved performance. Agent-E outperforms existing text and multi-modal web agents by 10-30% on the WebVoyager benchmark. The authors synthesize their findings into general design principles for developing agentic systems, including the use of domain-specific primitive skills, hierarchical architectures, and agentic self-improvement.

- [AUITestAgent: Automatic Requirements Oriented GUI Function Testing](https://arxiv.org/abs/2407.09018)
    - Yongxiang Hu, Xuan Wang, Yingchuan Wang, Yu Zhang, Shiyu Guo, Chaoyi Chen, Xin Wang, Yangfan Zhou
    - 🏛️ Institutions: Fudan University, Meituan
    - 📅 Date: July 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI testing], [AUITestAgent]
    - 📖 TLDR: This paper presents **AUITestAgent**, the first automatic, natural language-driven GUI testing tool for mobile apps. It automates the entire process of GUI interaction and function verification by extracting GUI interactions from test requirements via dynamically organized agents and employing a multi-dimensional data extraction strategy for verification.

- [Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence](https://openreview.net/forum?id=o1Et3MogPw)
    - Weize Chen, Ziming You, Ran Li, Yitong Guan, Chen Qian, Chenyang Zhao, Cheng Yang, Ruobing Xie, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Tsinghua University, Peking University, Beijing University of Posts and Telecommunications, Tencent
    - 📅 Date: July 7, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [multi-agent], [heterogeneous agents], [distributed collaboration], [IoA]
    - 📖 TLDR: The paper proposes the **Internet of Agents (IoA)**, a framework inspired by the Internet to facilitate collaboration among diverse autonomous agents. IoA introduces an agent integration protocol, dynamic teaming mechanisms, and conversation flow control, enabling flexible and scalable multi-agent collaboration. Experiments demonstrate IoA's superior performance across various tasks, highlighting its effectiveness in integrating heterogeneous agents.

- [MobileExperts: A Dynamic Tool-Enabled Agent Team in Mobile Devices](https://arxiv.org/abs/2407.03913)
    - Jiayi Zhang, Chuang Zhao, Yihan Zhao, Zhaoyang Yu, Ming He, Jianping Fan
    - 🏛️ Institutions: AI Lab at Lenovo Research, Renmin University of China, The Hong Kong University of Science and Technology
    - 📅 Date: July 4, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [tool formulation], [multi-agent], [double-layer planning], [Expert-Eval], [MobileExperts]
    - 📖 TLDR: This paper introduces *MobileExperts*, a framework that enhances autonomous operations on mobile devices by dynamically assembling agent teams based on user requirements. Each agent independently explores and formulates tools to evolve into an expert, improving efficiency and reducing reasoning costs.

- [Vision-driven Automated Mobile GUI Testing via Multimodal Large Language Model](https://arxiv.org/abs/2407.03037)
    - Zhe Liu, Cheng Li, Chunyang Chen, Junjie Wang, Boyu Wu, Yawen Wang, Jun Hu, Qing Wang
    - 🏛️ Institutions: Institute of Software, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Technical University of Munich, DiDi Global Inc.
    - 📅 Date: July 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI testing], [bug detection], [VisionDroid], [mobile agent]
    - 📖 TLDR: The paper presents **VisionDroid**, a vision-driven automated GUI testing approach utilizing Multimodal Large Language Models (MLLM) to detect non-crash functional bugs in mobile applications. By extracting GUI text information and aligning it with screenshots, VisionDroid enables MLLM to understand GUI context, facilitating deeper and function-oriented exploration. The approach segments exploration history into logically cohesive parts, prompting MLLM for bug detection, demonstrating superior performance over existing methods.

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
    - 🔑 Key: [model], [framework], [Octo-planner], [on-device], [planning]
    - 📖 TLDR: This paper presents Octo-planner, an on-device planning model designed for the Planner-Action Agents Framework. Octo-planner utilizes a fine-tuned model based on Phi-3 Mini (3.8 billion parameters) for high efficiency and low power consumption. It separates planning and action execution into two distinct components: a planner agent optimized for edge devices and an action agent using the Octopus model for function execution. The model achieves a planning success rate of 98.1% on benchmark datasets, providing reliable and effective performance.

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
    - 🔑 Key: [dataset], [framework], [Act2Cap], [GUI Narrator]
    - 📖 TLDR: The authors present **Act2Cap**, a GUI action dataset containing 4,189 video-caption pairs depicting various GUI actions such as clicks, drags, and typing across multiple software environments. They also propose **GUI Narrator**, a framework that leverages cursor detection as a visual prompt to enhance the interpretation of high-resolution screenshots for GUI video captioning. Evaluations reveal that even advanced multimodal models face challenges in this domain, highlighting the need for specialized approaches to improve performance.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: iMean AI, Carnegie Mellon University
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [Mind2Web-Live], [key-node evaluation]
    - 📖 TLDR: This paper presents WebCanvas, an online evaluation framework for web agents designed to address the dynamic nature of web interactions. It introduces a key-node-based evaluation metric to capture critical actions or states necessary for task completion while disregarding noise from insignificant events or changed web elements. The framework includes the Mind2Web-Live dataset, a refined version of the original Mind2Web static dataset, containing 542 tasks with 2,439 intermediate evaluation states. Despite advancements, the best-performing model achieves a task success rate of 23.1%, highlighting substantial room for improvement.

- [GUICourse: From General Vision Language Models to Versatile GUI Agents](https://aclanthology.org/2025.acl-long.1065/)
    - Wentong Chen, Junbo Cui, Jinyi Hu, Yujia Qin, Junjie Fang, Yue Zhao, Chongyi Wang, Jun Liu, Guirong Chen, Yupeng Huo, Yuan Yao, Yankai Lin, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Renmin University of China, Tsinghua University, Xiamen University, Beijing University of Posts and Telecommunications, ModelBest, Chinese Academy of Sciences, National University of Singapore, Shanghai Qi Zhi Institute
    - 📅 Date: June 17, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [framework], [GUICourse]
    - 📖 TLDR: This paper introduces *GUICourse*, a suite of datasets aimed at training visual-based GUI agents from general vision-language models. It addresses challenges in OCR, grounding, and GUI knowledge, enhancing the models' capabilities in GUI navigation tasks.

- [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html)
    - Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, Aviral Kumar
    - 🏛️ Institutions: University of California, Berkeley, University of Illinois Urbana-Champaign, Carnegie Mellon University, Google DeepMind
    - 📅 Date: June 14, 2024
    - 📑 Publisher: NeurIPS 2024 Main Conference Track
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [Android-in-the-Wild], [AitW], [device control], [DigiRL]
    - 📖 TLDR: The authors present *DigiRL*, an autonomous reinforcement learning approach for training device-control agents. By fine-tuning a pre-trained vision-language model in two stages—offline and offline-to-online RL—DigiRL achieves a significant improvement in success rates on the Android-in-the-Wild dataset, establishing a new state-of-the-art for digital agents in device control.

- [Practical, Automated Scenario-based Mobile App Testing](https://arxiv.org/abs/2406.08340)
    - Shengcheng Yu, Chunrong Fang, Mingzhe Du, Zimin Ding, Zhenyu Chen, Zhendong Su
    - 🏛️ Institutions: Nanjing University, ETH Zurich
    - 📅 Date: June 12, 2024
    - 📑 Publisher: IEEE Transactions on Software Engineering
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [ScenTest], [event knowledge graph], [GUI image understanding]
    - 📖 TLDR: This paper introduces *ScenTest*, a novel approach for scenario-based mobile app testing that integrates event knowledge graphs (EKGs) with GUI image understanding. By extracting entities and relationships from crowdsourced test reports, ScenTest constructs EKGs for specific scenarios, guiding automated testing processes. This method bridges the gap between testing execution and app business logic, achieving fully automated testing on target scenarios for the first time.

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

- [Search Beyond Queries: Training Smaller Language Models for Web Interactions via Reinforcement Learning](https://arxiv.org/abs/2404.10887)
    - Moghis Fereidouni, A.B. Siddique
    - 🏛️ Institutions: University of Kentucky
    - 📅 Date: April 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [grounded language agent], [Flan-T5], [unsupervised domain adaptation]
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

- [Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)
    - Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
    - 🏛️ Institutions: University of California, Berkeley, University of Michigan
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [evaluation model], [domain transfer]
    - 📖 TLDR: This paper presents an autonomous evaluation framework for digital agents to enhance performance on web navigation and device control. The study introduces modular, cost-effective evaluators achieving up to 92.9% accuracy in benchmarks like WebArena and outlines their use in fine-tuning agents, improving state-of-the-art by 29% without additional supervision.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://dl.acm.org/doi/10.1145/3637528.3671620)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences
    - 📅 Date: April 4, 2024
    - 📑 Publisher: KDD 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [web navigation], [AutoWebBench], [ChatGLM3-6B]
    - 📖 TLDR: AutoWebGLM introduces a web navigation agent based on ChatGLM3-6B, designed to autonomously navigate and interact with webpages for complex tasks. The paper highlights a two-phase data construction approach using a hybrid human-AI methodology for diverse, curriculum-based web task training. It also presents AutoWebBench, a benchmark for evaluating agent performance in web tasks, and uses reinforcement learning to fine-tune operations, addressing complex webpage interaction and grounding.

- [Enhancing Mobile "How-to" Queries with Automated Search Results Verification and Reranking](https://arxiv.org/abs/2404.08860)
    - Lei Ding, Jeshwanth Bheemanpally, Yi Zhang
    - 🏛️ Institutions: University of California, Santa Cruz
    - 📅 Date: April 2024
    - 📑 Publisher: SIGIR 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [reranking], [verification], [mobile task automation]
    - 📖 TLDR: This paper presents a system that enhances mobile "how-to" queries by verifying and reranking search results through automated instruction extraction, on-device action execution, and reranking based on relevance. The method improves on traditional ranking by analyzing device-specific execution success. The approach comprises a three-stage pipeline: 1) extracting step-by-step instructions from top search results, 2) validating these instructions on mobile devices, and 3) reranking based on performance. The system leverages a pre-trained GPT model for initial processing, ensuring adaptability across diverse apps and systems.

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

- [Android in the Zoo: Chain-of-Action-Thought for GUI Agents](https://aclanthology.org/2024.findings-emnlp.702/)
    - Jiwen Zhang, Jihao Wu, Teng Yihua, Minghui Liao, Nuo Xu, Xiao Xiao, Zhongyu Wei, Duyu Tang
    - 🏛️ Institutions: Fudan University, Huawei
    - 📅 Date: March 5, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [Android GUI], [Chain-of-Action-Thought], [autonomous GUI agents]
    - 📖 TLDR: This paper introduces *Chain-of-Action-Thought* (CoAT), a novel paradigm to improve GUI agent task completion by enabling agents to interpret previous actions, current screen content, and action rationale for next steps. The authors present the *Android-In-The-Zoo* (AitZ) dataset, which includes 18,643 screen-action pairs with detailed annotations, supporting CoAT's development and evaluation. The study demonstrates that fine-tuning with the AitZ dataset improves performance of a baseline large language model in predicting correct action sequences in Android tasks.

- [Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II as a Case Study](https://arxiv.org/abs/2403.03186)
    - Weihao Tan, Ziluo Ding, Wentao Zhang, Boyu Li, Bohan Zhou, Junpeng Yue, Haochong Xia, Jiechuan Jiang, Longtao Zheng, Xinrun Xu, Yifei Bi, Pengjie Gu, Xinrun Wang, Börje F. Karlsson, Bo An, Zongqing Lu
    - 🏛️ Institutions: Nanyang Technological University, Beijing Academy of Artificial Intelligence, Peking University
    - 📅 Date: March 5, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [Cradle], [General Computer Control], [multimodal], [keyboard and mouse control], [long-term memory], [reasoning], [self-improvement]
    - 📖 TLDR: This paper introduces *Cradle*, a framework designed to achieve General Computer Control (GCC) by enabling agents to perform any computer task using only screen images (and possibly audio) as input and producing keyboard and mouse operations as output. The authors deploy Cradle in the complex AAA game Red Dead Redemption II, demonstrating its capability to follow the main storyline and complete real missions with minimal reliance on prior knowledge or resources.

- [Cradle: Empowering Foundation Agents Towards General Computer Control](https://proceedings.mlr.press/v267/tan25h.html)
    - Weihao Tan, Wentao Zhang, Xinrun Xu, Haochong Xia, Ziluo Ding, Boyu Li, Bohan Zhou, Junpeng Yue, Jiechuan Jiang, Yewen Li, Ruyi An, Molei Qin, Chuqiao Zong, Longtao Zheng, Yujie Wu, Xiaoqiang Chai, Yifei Bi, Tianbao Xie, Pengjie Gu, Xiyun Li, Ceyao Zhang, Long Tian, Chaojie Wang, Xinrun Wang, Börje F. Karlsson, Bo An, Shuicheng Yan, Zongqing Lu
    - 🏛️ Institutions: Skywork AI, Beijing Academy of Artificial Intelligence, Nanyang Technological University, Peking University, Institute of Software, Chinese Academy of Sciences, The University of Hong Kong, The Chinese University of Hong Kong
    - 📅 Date: March 5, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [general computer control], [skill curation], [self-improvement]
    - 📖 TLDR: This paper introduces the Cradle framework, designed to enable general computer control (GCC) through multimodal input (e.g., screen images and optional audio) and outputs (keyboard and mouse). Cradle’s six core modules, including self-reflection, skill curation, and memory, allow for generalized task handling in complex environments like AAA games. Demonstrated in *Red Dead Redemption II*, the framework exhibits adaptability by performing real missions and following the storyline with minimal prior knowledge, showcasing its potential as a generalist agent for diverse computer tasks.

- [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26/)
    - Chaoyun Zhang, Liqun Li, Shilin He, Xu Zhang, Bo Qiao, Si Qin, Minghua Ma, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Microsoft
    - 📅 Date: February 14, 2024
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [UI automation], [Windows], [UFO]
    - 📖 TLDR: This paper presents UFO, a pioneering multimodal LLM-based agent designed to fulfill user requests on Windows OS. UFO employs a dual-agent architecture—comprising AppAgent and ActAgent—that can interpret and execute complex tasks across multiple Windows applications by observing UI elements and utilizing control interactions. The framework allows UFO to handle intricate, cross-application workflows and execute commands seamlessly based on natural language prompts. It integrates GPT-Vision to recognize and interact with graphical elements, enabling flexible, autonomous task completion within and across diverse Windows applications.

- [ScreenAgent: A Computer Control Agent Driven by Visual Language Large Model](https://arxiv.org/abs/2402.07945)
    - Runliang Niu, Jindong Li, Shiqi Wang, Yali Fu, Xiyu Hu, Xueyuan Leng, He Kong, Yi Chang, Qi Wang
    - 🏛️ Institutions: Jilin University
    - 📅 Date: February 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual language model], [computer control agent]
    - 📖 TLDR: This paper introduces ScreenAgent, a computer control agent powered by a visual language large model. The system can interpret natural language instructions and execute them on various computer applications by analyzing screen content. ScreenAgent employs a novel action grounding mechanism to map high-level instructions to specific UI interactions. Evaluated on a diverse set of tasks across different applications, ScreenAgent demonstrates superior performance in task completion and generalization compared to existing methods.

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
    - 🔑 Key: [framework], [self-directed learning], [GAIA], [FRIDAY], [OS-Copilot]
    - 📖 TLDR: The OS-Copilot framework supports building generalist agents capable of performing diverse tasks across an operating system (OS). This work introduces FRIDAY, an embodied agent using OS-Copilot to self-improve by learning from task outcomes. It operates with a memory-based architecture to tackle OS-level tasks across applications like terminals, web browsers, and third-party tools. Tested on the GAIA benchmark, FRIDAY achieved 35% higher performance than prior methods, proving effective in adapting to unfamiliar applications and refining its capabilities with minimal guidance.

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

- [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://openreview.net/forum?id=jE6pDYCnVF)
    - Junyang Wang, Haiyang Xu, Jiabo Ye, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - 🏛️ Institutions: Beijing Jiaotong University, Alibaba Group
    - 📅 Date: January 29, 2024
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark]
    - 📖 TLDR: This paper presents Mobile-Agent, an autonomous multi-modal agent designed for mobile device interaction. The system integrates visual perception, natural language processing, and action prediction to navigate and operate mobile applications. The authors introduce a new dataset and benchmark for evaluating mobile agents, demonstrating Mobile-Agent's superior performance in task completion and generalization across various apps compared to existing methods.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://aclanthology.org/2024.acl-long.50/)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [dataset], [multimodal agent evaluation], [visually grounded tasks]
    - 📖 TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [grounding], [SeeAct], [Multimodal-Mind2web]
    - 📖 TLDR: This paper explores the capability of GPT-4V(ision), a multimodal model, as a web agent that can perform tasks across various websites by following natural language instructions. It introduces the **SEEACT** framework, enabling GPT-4V to navigate, interpret, and interact with elements on websites. Evaluated using the **Mind2Web** benchmark and an online test environment, the framework demonstrates high performance on complex web tasks by integrating grounding strategies like element attributes and image annotations to improve HTML element targeting. However, grounding remains challenging, presenting opportunities for further improvement.

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

- [GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](https://arxiv.org/abs/2311.07562)
    - An Yan, Zhengyuan Yang, Wanrong Zhu, Kevin Lin, Linjie Li, Jianfeng Wang, Jianwei Yang, Yiwu Zhong, Julian McAuley, Jianfeng Gao, Zicheng Liu, Lijuan Wang
    - 🏛️ Institutions: University of California San Diego, Microsoft, University of California, Santa Barbara, University of Wisconsin-Madison
    - 📅 Date: November 13, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [benchmark], [zero-shot GUI navigation], [MM-Navigator], [MobileNav], [GPT-4V]
    - 📖 TLDR: This paper explores the capabilities of GPT-4V in navigating smartphone GUIs without prior training. The authors introduce a novel framework for GUI navigation and a new benchmark, MobileNav, featuring 1,000 navigation tasks across 100 mobile apps. The study demonstrates GPT-4V's impressive zero-shot performance in understanding and interacting with mobile interfaces, outperforming previous methods and even approaching human-level performance on some tasks.

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
    - 🔑 Key: [framework], [policy composition], [dynamic control], [SteP]
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

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: July 26, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [multi-tab navigation], [web-based interaction], [agent simulation]
    - 📖 TLDR: *WebArena* provides a standalone, realistic web simulation environment where autonomous agents can perform complex web-based tasks. The platform offers functionalities such as multi-tab browsing, element interaction, and customized user profiles. Its benchmark suite contains 812 tasks grounded in high-level natural language commands. WebArena uses multi-modal observations, including HTML and accessibility tree views, supporting advanced tasks that require contextual understanding across diverse web pages, making it suitable for evaluating generalist agents in real-world web environments.

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

- [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0ff30c4bf31db0119a6219e0d250e037-Abstract-Conference.html)
    - Hongxin Li, Jingran Su, Yuntao Chen, Qing Li, Zhaoxiang Zhang
    - 🏛️ Institutions: University of Chinese Academy of Sciences, Hong Kong Institute of Science and Innovation, Chinese Academy of Sciences, The Hong Kong Polytechnic University, Shanghai AI Laboratory
    - 📅 Date: May 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [spreadsheet automation], [natural language interface]
    - 📖 TLDR: This paper introduces SheetCopilot, an innovative system that leverages large language models to automate spreadsheet tasks through natural language interactions. The framework includes a novel prompt design for task decomposition and execution, and a feedback loop for error correction. SheetCopilot demonstrates significant improvements in task completion rates and efficiency across various spreadsheet operations, outperforming existing methods and showing potential for enhancing productivity in spreadsheet software.

- [Augmenting Autotelic Agents with Large Language Models](https://arxiv.org/abs/2305.12487)
    - Cédric Colas, Laetitia Teodorescu, Pierre-Yves Oudeyer, Xingdi Yuan, Marc-Alexandre Côté
    - 🏛️ Institutions: MIT, Inria, Microsoft
    - 📅 Date: May 22, 2023
    - 📑 Publisher: CoLLAs 2023
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [goal generation], [large language models], [autotelic learning]
    - 📖 TLDR: This study introduces the *Language Model-Augmented Autotelic Agent (LMA3)*, a framework leveraging large language models to help agents autonomously generate, represent, and learn diverse goals in a task-agnostic, text-based environment. LMA3 integrates pretrained language models to emulate human cultural knowledge, aiming to dynamically relabel goals, generate new goals, and create goal-driven reward functions without manual inputs. This approach supports skill development by autonomously expanding goal repertoires in ways that resemble human open-ended learning, showcasing potential for achieving complex, self-directed learning in AI.

- [Language Models can Solve Computer Tasks](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7cc1005ec73cfbaac9fa21192b622507-Abstract-Conference.html)
    - Geunwoo Kim, Pierre Baldi, Stephen McAleer
    - 🏛️ Institutions: University of California, Irvine, Carnegie Mellon University
    - 📅 Date: March 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [Recursive Critique and Improve], [RCI], [MiniWoB++], [general computer tasks]
    - 📖 TLDR: This study demonstrates that large language models (LLMs) can effectively automate computer tasks using a Recursive Critique and Improve (RCI) prompting method, enabling agents to handle complex desktop tasks like email and file management. By combining RCI with existing Chain of Thought (CoT) prompting, the method outperforms prior LLM approaches and traditional supervised and reinforcement learning models on the **MiniWoB++** benchmark, showing potential for broad computer task automation.

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)
    - Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
    - 🏛️ Institutions: Northeastern University, Massachusetts Institute of Technology, Princeton University
    - 📅 Date: March 20, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [learning], [verbal reinforcement learning], [Reflexion]
    - 📖 TLDR: This paper introduces *Reflexion*, a framework that enhances language agents by enabling them to reflect on task feedback linguistically, storing these reflections in an episodic memory to improve decision-making in future trials. Reflexion allows agents to learn from various feedback types without traditional weight updates, achieving significant performance improvements across tasks like decision-making, coding, and reasoning. For instance, Reflexion attains a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4's 80%.

- [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://proceedings.mlr.press/v202/lee23g.html)
    - Kenton Lee, Mandar Joshi, Iulia Raluca Turc, Hexiang Hu, Fangyu Liu, Julian Martin Eisenschlos, Urvashi Khandelwal, Peter Shaw, Ming-Wei Chang, Kristina Toutanova
    - 🏛️ Institutions: Google
    - 📅 Date: February 1, 2023
    - 📑 Publisher: ICML 2023
    - 💻 Env: [Web], [Doc]
    - 🔑 Key: [model], [framework], [vision encoder], [visual language understanding], [screenshot parsing], [image-to-text]
    - 📖 TLDR: This paper introduces Pix2Struct, a model pre-trained to parse masked screenshots into simplified HTML for tasks requiring visual language understanding. By leveraging the structure of HTML and diverse web page elements, Pix2Struct captures pretraining signals like OCR and image captioning, achieving state-of-the-art performance across tasks in domains including documents, user interfaces, and illustrations.

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

- [A Data-Driven Approach for Learning to Control Computers](https://proceedings.mlr.press/v162/humphreys22a.html)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - 🏛️ Institutions: DeepMind
    - 📅 Date: February 16, 2022
    - 📑 Publisher: ICML 2022
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [computer control], [reinforcement learning], [behavioral cloning], [MiniWoB++]
    - 📖 TLDR: This study presents a reinforcement learning-based approach to train agents for computer control tasks, using keyboard and mouse interactions guided by natural language. By leveraging human demonstration data, agents trained in this environment achieved strong cross-task generalization across the MiniWob++ benchmark. This framework demonstrates how agents can control computers as humans would, enabling enhanced performance in complex computer tasks with high transferability.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://aclanthology.org/2021.naacl-main.80/)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - 🏛️ Institutions: Stanford University, Samsung Research
    - 📅 Date: March 30, 2021
    - 📑 Publisher: NAACL 2021
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [grounding], [task automation], [open-domain instructions], [RUSS]
    - 📖 TLDR: This paper introduces RUSS (Rapid Universal Support Service), a framework designed to interpret and execute open-domain, step-by-step web instructions automatically. RUSS uses a BERT-LSTM model for semantic parsing into a custom language, ThingTalk, which allows the system to map language to actions across various web elements. The framework, including a dataset of instructions, facilitates agent-based web support task automation by grounding natural language to interactive commands.

- [Interactive Task Learning from GUI-Grounded Natural Language Instructions and Demonstrations](https://aclanthology.org/2020.acl-demos.25/)
    - Toby Jia-Jun Li, Tom Mitchell, Brad Myers
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: July 2020
    - 📑 Publisher: ACL 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [Sugilite], [programming-by-demonstration]
    - 📖 TLDR: This paper introduces *Sugilite*, an intelligent task automation agent that learns new tasks and associated concepts interactively from users' natural language instructions and demonstrations on third-party mobile app GUIs. The system allows users to teach procedures and concepts through verbal instructions combined with GUI demonstrations, supports intent clarification for demonstrated actions, infers task parameters using hierarchical app GUI structures, and generalizes taught concepts across different contexts and domains. A prototype is presented as a conversational assistant on Android.

- [Mapping Natural Language Instructions to Mobile UI Action Sequences](https://aclanthology.org/2020.acl-main.729)
    - Yang Li, Jiacong He, Xin Zhou, Yuan Zhang, Jason Baldridge
    - 🏛️ Institutions: Google Research
    - 📅 Date: July 2020
    - 📑 Publisher: ACL 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile UI automation], [natural language instructions], [action grounding], [RicoSCA]
    - 📖 TLDR: This paper introduces a method for grounding natural language instructions to mobile UI actions, aiming to automate mobile task execution through user interface manipulation. It introduces three key datasets: **PixelHelp** for task instruction-performance mappings on a Pixel emulator, **AndroidHowTo** for detailed phrase extraction, and **RicoSCA** for synthetic UI command training. The system utilizes a Transformer model to extract action phrase tuples, aligning them to UI elements with contextual screen positioning. Achieving over 70% accuracy in task completion, this approach is foundational for natural language-driven mobile UI automation.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://openreview.net/forum?id=ryTp3f-0-)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Stanford University
    - 📅 Date: February 24, 2018
    - 📑 Publisher: ICLR 2018 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [web tasks], [workflow-guided exploration]
    - 📖 TLDR: This paper presents a novel RL approach using *workflow-guided exploration* to efficiently train agents on web-based tasks, where actions are restricted based on demonstrated workflows to streamline learning. Evaluated on MiniWoB and MiniWoB++ benchmarks, the method significantly outperforms traditional RL techniques in sparse reward settings by structuring exploration according to high-level action constraints.

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
