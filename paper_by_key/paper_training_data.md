# Papers with Keyword: training data

- [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440)
    - Xiangru Jian, Shravan Nayak, Kevin Qinghong Lin, Aarash Feizi, Kaixin Li, Patrice Bechard, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: ServiceNow, University of Waterloo, Mila, Université de Montréal, McGill University, University of Oxford, National University of Singapore
    - 📅 Date: March 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [video demonstration], [training data], [desktop automation], [UI-Vision], [GroundCUA], [CUA-Suite]
    - 📖 TLDR: CUA-Suite is a desktop-agent data ecosystem built around continuous expert demonstration video rather than sparse screenshots. It combines VideoCUA, UI-Vision, and GroundCUA to provide large-scale video trajectories, grounding annotations, and evaluation data for professional desktop applications that remain hard for current foundation action models.

- [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178)
    - Linxin Song, Jieyu Zhang, Huanxin Sheng, Taiwei Shi, Gupta Rahul, Yang Liu, Ranjay Krishna, Jian Kang, Jieyu Zhao
    - 🏛️ Institutions: University of Southern California, University of Washington, MBZUAI, Amazon AGI
    - 📅 Date: March 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [reward model], [video understanding], [evaluation], [training data], [ExeVR-53k], [ExeVRM]
    - 📖 TLDR: This work studies reward modeling from execution video instead of agent internals, introducing ExeVR-53k and an execution-video reward model that judges task success from keyframes plus the user instruction. The method scales task-completion evaluation across operating systems and outperforms strong proprietary models while giving finer temporal feedback.

- [WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces](https://arxiv.org/abs/2603.05295)
    - Sicheng Fan, Rui Wan, Yifei Leng, Gaoning Liang, Li Ling
    - 🏛️ Institutions: Fudan University, IMean AI
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [grounding], [training data], [multimodal]
    - 📖 TLDR: WebChain is the largest open-source dataset of 31,725 human-annotated web interaction trajectories (318k steps) on real-world websites, featuring triple-aligned visual, structural, and action data. Leveraging this dataset, the authors propose a Dual Mid-Training recipe that decouples spatial grounding from planning, achieving state-of-the-art performance on their WebChainBench and other public GUI benchmarks.

- [ANCHOR: Branch-Point Data Generation for GUI Agents](https://arxiv.org/abs/2602.07153)
    - Jinbiao Wei, Yilun Zhao, Kangqi Ni, Haotian Zhao, Chen Qian
    - 🏛️ Institutions: Yale University, University of North Carolina at Chapel Hill
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [data generation], [trajectory expansion], [desktop automation], [training data], [benchmark]
    - 📖 TLDR: ANCHOR is a trajectory expansion framework that generates diverse, high-quality GUI interaction data by identifying branch points in seed demonstrations and proposing new state-grounded task variants, with verification and denoising to ensure quality. Models fine-tuned on the expanded data show consistent improvements on OSWorld and WindowsAgentArena benchmarks over zero-shot and synthesis baselines.

- [M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining](https://arxiv.org/abs/2602.05429)
    - Rui Lv, Juncheng Mo, Tianyi Chu, Yiming Liu, Hongling Zhuo
    - 🏛️ Institutions: Ant Group, Zhejiang University
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [data mining], [monte carlo tree search], [multi-agent framework], [trajectory annotation], [training data]
    - 📖 TLDR: M2-Miner is an automated mobile GUI agent data-mining framework that uses Monte Carlo Tree Search enhanced by a collaborative multi-agent system (InferAgent, OrchestraAgent, JudgeAgent) to efficiently generate high-quality intent-trajectory training data, along with intent recycling and progressive model-in-the-loop training strategies. GUI agents fine-tuned on the mined data achieve state-of-the-art performance on multiple mobile GUI benchmarks.

- [Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training](https://arxiv.org/abs/2601.22781)
    - Linjia Kang, Zhimin Wang, Yongkang Zhang, Yuanchun Li, Gang Yin
    - 🏛️ Institutions: Tsinghua University, Huazhong Agricultural University, Kuaishou Technology
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [data generation], [curriculum learning], [multi-agent], [VLM], [training data]
    - 📖 TLDR: MobileGen is an adaptive data generation framework for mobile GUI agent training that decouples task difficulty into structural and semantic dimensions, profiles the agent's capability frontier, and uses a multi-agent controllable generator to synthesize difficulty-aligned interaction trajectories, improving average agent performance by 1.57x over baselines across multiple benchmarks.

- [Step-GUI Technical Report](https://arxiv.org/abs/2512.15431)
    - Haolong Yan, Jia Wang, Xin Huang, Yeqing Shen, Ziyang Meng, Zhimin Fan, Kaijun Tan, Jin Gao, Lieyu Shi, Mi Yang, Shiliang Yang, Zhirui Wang, Brian Li, Kang An, Chenyang Li, Lei Lei, Mengmeng Duan, Danxun Liang, Guodong Liu, Hang Cheng, Hao Wu, Jie Dong, Junhao Huang, Mei Chen, Renjie Yu, Shunshan Li, Xu Zhou, Yiting Dai, Yineng Deng, Yingdan Liang, Zelin Chen, Wen Sun, Chengxu Yan, Chunqin Xu, Dong Li, Fengqiong Xiao, Guanghao Fan, Guopeng Li, Guozhen Peng, Hongbing Li, Hang Li, Hongming Chen, Jingjing Xie, Jianyong Li, Jingyang Zhang, Jiaju Ren, Jiayu Yuan, Jianpeng Yin, Kai Cao, Liang Zhao, Liguo Tan, Liying Shi, Mengqiang Ren, Min Xu, Manjiao Liu, Mao Luo, Mingxin Wan, Na Wang, Nan Wu, Ning Wang, Peiyao Ma, Qingzhou Zhang, Qiao Wang, Qinlin Zeng, Qiong Gao, Qiongyao Li, Shangwu Zhong, Shuli Gao, Shaofan Liu, Shisi Gao, Shuang Luo, Xingbin Liu, Xiaojia Liu, Xiaojie Hou, Xin Liu, Xuanti Feng, Xuedan Cai, Xuan Wen, Xianwei Zhu, Xin Liang, Xin Zhou, Yifan Sui, Yingxiu Zhao, Yukang Shi, Yunfang Xu, Yuqing Zeng, Yixun Zhang, Zejia Weng, Zhonghao Yan, Zhiguo Huang, Zhuoyu Wang, Zihan Yan, Zheng Ge, Jing Li, Yibo Zhu, Binxing Jiao, Xiangyu Zhang, Daxin Jiang
    - 🏛️ Institutions: StepFun
    - 📅 Date: December 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multimodal LLM], [reinforcement learning], [benchmark], [MCP], [training data]
    - 📖 TLDR: Step-GUI introduces a self-evolving training pipeline with a Calibrated Step Reward System that produces high-quality trajectory data at 10-100x lower cost, yielding 4B/8B GUI agent models achieving state-of-the-art performance (80.2% AndroidWorld, 48.5% OSWorld), along with GUI-MCP (a privacy-preserving Model Context Protocol for GUI automation) and AndroidDaily (a real-world mobile benchmark).

- [Adapting Web Agents with Synthetic Supervision](https://arxiv.org/abs/2511.06101)
    - Zhaoyang Wang, Yiming Liang, Xuchao Zhang, Qianhui Wu, Siwei Han, Anson Bastos, Rujia Wang, Chetan Bansal, Baolin Peng, Jianfeng Gao, Saravan Rajmohan, Huaxiu Yao
    - 🏛️ Institutions: UNC-Chapel Hill, Purdue University, Microsoft
    - 📅 Date: November 08, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [synthetic data], [training data], [fine-tuning], [trajectory refinement], [task synthesis]
    - 📖 TLDR: SynthAgent is a fully synthetic supervision framework for adapting web agents to new websites by generating and refining both tasks and trajectories, using dual refinement to address hallucinations in synthesized tasks and noise in collected trajectories, then fine-tuning open-source agents on the refined data.

- [Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents](https://arxiv.org/abs/2510.24702)
    - Yueqi Song, Ketan Ramaneti, Zaid Sheikh, Ziru Chen, Boyu Gou, Tianbao Xie, Yiheng Xu, Danyang Zhang, Apurva Gandhi, Fan Yang, Joseph Liu, Tianyue Ou, Zhihao Yuan, Frank Xu, Shuyan Zhou, Xingyao Wang, Xiang Yue, Tao Yu, Huan Sun, Yu Su, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University, The Ohio State University, University of Hong Kong, Duke University, Fujitsu Research, All Hands AI
    - 📅 Date: October 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [data protocol], [training data], [supervised fine-tuning], [dataset unification], [ADP]
    - 📖 TLDR: Agent Data Protocol (ADP) standardizes heterogeneous agent trajectories into a lightweight schema and conversion pipeline so diverse agent datasets can plug into multiple SFT pipelines without per-dataset engineering. Converting 13 existing datasets into ADP and fine-tuning on the unified corpus improves base models by about 20% on average across coding, browsing, tool-use, and research benchmarks.

- [Synthesizing Agentic Data for Web Agents with Progressive Difficulty Enhancement Mechanisms](https://arxiv.org/abs/2510.13913)
    - Shrey Pandit, Xuan-Phi Nguyen, Yifei Ming, Austin Xu, Jiayu Wang, Caiming Xiong, Shafiq Joty
    - 🏛️ Institutions: Salesforce AI Research, University of Wisconsin-Madison
    - 📅 Date: October 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [data synthesis], [training data], [progressive difficulty], [distillation], [deep research]
    - 📖 TLDR: This paper introduces a data synthesis pipeline that generates question-answer pairs for training web agents by progressively increasing task complexity until a frontier baseline agent fails, producing smaller but more effective and diverse training datasets than existing approaches across multiple web-based benchmarks.

- [Watch and Learn: Learning to Use Computers from Online Videos](https://arxiv.org/abs/2510.04673)
    - Chan Hee Song, Yiwen Song, Palash Goyal, Yu Su, Oriana Riva, Hamid Palangi, Tomas Pfister
    - 🏛️ Institutions: Google Cloud AI Research, The Ohio State University
    - 📅 Date: October 06, 2025
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [training data], [video understanding], [data generation], [inverse dynamics]
    - 📖 TLDR: Watch & Learn (W&L) converts Internet computer-use videos into 53K+ executable UI trajectories by casting annotation as an inverse dynamics problem—predicting user actions from consecutive screen states—enabling scalable CUA training data collection from readily available human-recorded videos.

- [Scaling Synthetic Task Generation for Agents via Exploration](https://arxiv.org/abs/2509.25047)
    - Ram Ramrakhya, Andrew Szot, Omar Attia, Yuhao Yang, Anh Nguyen, Bogdan Mazoure, Zhe Gan, Harsh Agrawal, Alexander Toshev
    - 🏛️ Institutions: Apple
    - 📅 Date: September 29, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [task generation], [training data], [exploration]
    - 📖 TLDR: AutoPlay is a scalable pipeline for synthetic agentic task generation that explicitly explores interactive environments to discover possible interactions, producing diverse, feasible, and verifiable tasks for post-training MLLMs as interactive agents for computer-use and web navigation.
