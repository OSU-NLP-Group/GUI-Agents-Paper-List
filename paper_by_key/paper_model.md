# Papers with Keyword: model

- [MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516)
    - Tanmay Gupta, Piper Wolters, Zixian Ma, Peter Sushko, Rock Yuren Pang, Diego Llanes, Yue Yang, Taira Anderson, Boyuan Zheng, Zhongzheng Ren, Harsh Trivedi, Taylor Blanton, Caleb Ouellette, Winson Han, Ali Farhadi, Ranjay Krishna
    - 🏛️ Institutions: AI2, UW, UNC
    - 📅 Date: April 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [dataset], [MolmoWeb], [open-source]
    - 📖 TLDR: MolmoWeb is a family of fully open multimodal web agents (4B and 8B) trained on MolmoWebMix (100K+ synthetic trajectories and 30K+ human demonstrations). Operating as screenshot-only visual-language action policies without HTML or accessibility tree access, it achieves SOTA on WebVoyager, Online-Mind2Web, and DeepShop, outperforming larger closed models like GPT-4o.

- [IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents](https://arxiv.org/abs/2604.05157)
    - Rongqian Chen, Yu Li, Zeyu Fang, Sizhe Tang, Weidong Cao, Tian Lan
    - 🏛️ Institutions: George Washington University
    - 📅 Date: April 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [reward model], [model], [plan-aware reward], [contrastive alignment], [margin ranking], [OSWorld], [IntentScore]
    - 📖 TLDR: IntentScore is a plan-aware reward model for computer-use agents trained from 398K offline GUI interaction steps across three OSes, using contrastive alignment and margin ranking objectives. It achieves 97.5% pairwise discrimination and, when used as a re-ranker for Agent S3 on OSWorld, improves task success rate by 6.9 points.

- [SecAgent: Efficient Mobile GUI Agent with Semantic Context](https://arxiv.org/abs/2603.08533)
    - Yiping Xie, Song Chen, Jingxuan Xing, Wei Jiang, Zekun Zhu, Yingyao Wang, Pi Bu, Jun Song, Yuning Jiang, Bo Zheng
    - 🏛️ Institutions: Taobao & Tmall Group of Alibaba
    - 📅 Date: March 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [semantic context], [dataset], [benchmark], [history summarization], [chinese mobile apps], [SecAgent]
    - 📖 TLDR: SecAgent is a 3B mobile GUI agent that summarizes history screenshots and actions into concise semantic context, reducing computation while preserving task-relevant information. It also introduces a human-verified Chinese mobile GUI dataset and benchmark, and reaches performance comparable to 7B-8B models through supervised and reinforcement fine-tuning.

- [Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855)
    - Haiyang Xu, Xi Zhang, Haowei Liu, Junyang Wang, Zhaozai Zhu, Shengjie Zhou, Xuhao Hu, Feiyu Gao, Junjie Cao, Zihua Wang, Zhiyuan Chen, Jitong Liao, Qi Zheng, Jiahui Zeng, Ze Xu, Shuai Bai, Junyang Lin, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: February 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [GUI-Owl-1.5], [multi-platform], [tool use], [memory], [MRPO], [data flywheel]
    - 📖 TLDR: Mobile-Agent-v3.5 introduces GUI-Owl-1.5, a family of native GUI agents spanning desktop, mobile, and browser settings. The work combines a hybrid data flywheel, stronger memory and tool use, and multi-platform RL with MRPO to improve results across many open GUI benchmarks.

- [UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics](https://arxiv.org/abs/2604.02345)
    - Mengzhou Wu, Yuzhe Guo, Yuan Cao, Haochuan Lu, Songhe Zhu, Pingzhe Qu, Xin Chen, Kang Qin, Zhongpu Wang, Xiaode Zhang, Xinyi Wang, Wei Dai, Gang Cao, Yuetang Deng, Zhi Gong, Dezhi Ran, Linyi Li, Wei Yang, Tao Xie
    - 🏛️ Institutions: PKU, Tencent
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [world model], [data generation], [UI-Oceanus]
    - 📖 TLDR: UI-Oceanus shifts learning from mimicking trajectories to mastering interaction physics via forward dynamics prediction. Using synthetic environmental dynamics as supervision, it improves GUI agents by 7% on offline benchmarks and 16.8% in online navigation, with performance scaling log-linearly with data volume.

- [OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution](https://arxiv.org/abs/2601.20380)
    - Le Zhang, Yixiong Xiao, Xinjiang Lu, Jingjia Cao, Yusai Zhao, Jingbo Zhou, Lang An, Zikan Feng, Wanxiang Sha, Yu Shi, Congxi Xiao, Jian Xiong, Yankai Zhang, Hua Wu, Haifeng Wang
    - 🏛️ Institutions: Baidu Frontier Research Department
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [model], [synthetic data], [Mixture-of-Experts], [GRPO], [OS-Nav], [ChiM-Nav], [Ubu-Nav], [OmegaUse]
    - 📖 TLDR: OmegaUse is a general-purpose GUI agent for both phone-use and computer-use settings trained with a curated-plus-synthetic data pipeline and a two-stage SFT-then-GRPO recipe on an MoE backbone. It also introduces the OS-Nav suite and reports strong cross-terminal results on ScreenSpot-v2, AndroidControl, ChiM-Nav, and Ubu-Nav.

- [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)
    - Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu
    - 🏛️ Institutions: Meituan, Fudan, Tongji University, HKUST
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [synthetic experience], [verifiable synthesis], [OSWorld], [EvoCUA]
    - 📖 TLDR: EvoCUA replaces static imitation with an evolving training loop built on verifiable task synthesis, high-throughput sandbox rollouts, and iterative policy optimization from both successful and failed trajectories. On OSWorld it reaches 56.7% success, outperforming prior open-source computer-use agents and even some leading closed-weight systems.

- [ShowUI-π: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965)
    - Siyuan Hu, Kevin Qinghong Lin, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS
    - 📅 Date: December 31, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [benchmark], [model], [drag interaction], [flow-based model], [continuous action], [ScreenDrag], [ShowUI-π]
    - 📖 TLDR: ShowUI-π treats GUI dragging as a continuous dexterous-control problem rather than only discrete point prediction, while still supporting ordinary click actions in the same model. It also introduces ScreenDrag with 20K trajectories across five domains, and the 450M-parameter model outperforms much larger proprietary GUI agents on this benchmark.

- [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047)
    - Hanzhang Zhou, Xu Zhang, Panrong Tong, Jianan Zhang, Liangyu Chen, Quyu Kong, Chenglin Cai, Chen Liu, Yue Wang, Jingren Zhou, Steven Hoi
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [model], [agent-user interaction], [MCP], [device-cloud collaboration], [online reinforcement learning], [MAI-UI]
    - 📖 TLDR: MAI-UI is a foundation GUI-agent family aimed at realistic deployment rather than benchmark-only optimization. It extends pure UI control with agent-user interaction, MCP tool calls, native device-cloud collaboration, and long-horizon online reinforcement learning, and sets strong results on grounding, AndroidWorld, and MobileWorld.

- [Step-GUI Technical Report](https://arxiv.org/abs/2512.15431)
    - Haolong Yan, Jia Wang, Xin Huang, Yeqing Shen, Ziyang Meng, Zhimin Fan, Kaijun Tan, Jin Gao, Lieyu Shi, Mi Yang, Shiliang Yang, Zhirui Wang, Brian Li, Kang An, Chenyang Li, Lei Lei, Mengmeng Duan, Danxun Liang, Guodong Liu, Hang Cheng, Hao Wu, Jie Dong, Junhao Huang, Mei Chen, Renjie Yu, Shunshan Li, Xu Zhou, Yiting Dai, Yineng Deng, Yingdan Liang, Zelin Chen, Wen Sun, Chengxu Yan, Chunqin Xu, Dong Li, Fengqiong Xiao, Guanghao Fan, Guopeng Li, Guozhen Peng, Hongbing Li, Hang Li, Hongming Chen, Jingjing Xie, Jianyong Li, Jingyang Zhang, Jiaju Ren, Jiayu Yuan, Jianpeng Yin, Kai Cao, Liang Zhao, Liguo Tan, Liying Shi, Mengqiang Ren, Min Xu, Manjiao Liu, Mao Luo, Mingxin Wan, Na Wang, Nan Wu, Ning Wang, Peiyao Ma, Qingzhou Zhang, Qiao Wang, Qinlin Zeng, Qiong Gao, Qiongyao Li, Shangwu Zhong, Shuli Gao, Shaofan Liu, Shisi Gao, Shuang Luo, Xingbin Liu, Xiaojia Liu, Xiaojie Hou, Xin Liu, Xuanti Feng, Xuedan Cai, Xuan Wen, Xianwei Zhu, Xin Liang, Xin Zhou, Yifan Sui, Yingxiu Zhao, Yukang Shi, Yunfang Xu, Yuqing Zeng, Yixun Zhang, Zejia Weng, Zhonghao Yan, Zhiguo Huang, Zhuoyu Wang, Zihan Yan, Zheng Ge, Jing Li, Yibo Zhu, Binxing Jiao, Xiangyu Zhang, Daxin Jiang
    - 🏛️ Institutions: StepFun
    - 📅 Date: December 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [model], [Calibrated Step Reward System], [self-evolving training], [GUI-MCP], [AndroidDaily], [Step-GUI]
    - 📖 TLDR: Step-GUI centers on a self-evolving training pipeline built around the Calibrated Step Reward System, which calibrates model-generated GUI trajectories against trajectory-level signals to produce high-quality supervision at much lower annotation cost. On top of that pipeline, the paper introduces 4B and 8B GUI specialist models, the GUI-MCP protocol, and the AndroidDaily benchmark.

- [AFRAgent : An Adaptive Feature Renormalization Based High Resolution Aware GUI agent](https://arxiv.org/abs/2512.00846)
    - Neeraj Anand, Rishabh Jain, Sohan Patnaik, Balaji Krishnamurthy, Mausoom Sarkar
    - 🏛️ Institutions: Adobe
    - 📅 Date: November 30, 2025
    - 📑 Publisher: WACV 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [GUI grounding], [smartphone automation], [adaptive feature renormalization], [instruct-BLIP], [AFRAgent]
    - 📖 TLDR: AFRAgent targets the loss of spatial detail that hurts mobile GUI automation models built on low-resolution vision features. It adds an adaptive feature renormalization module to enrich instruct-BLIP image embeddings with high-resolution information, and reports state-of-the-art results on Meta-GUI and AITW with a much smaller model than prior baselines.

- [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790)
    - Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple, HKU
    - 📅 Date: October 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [hybrid action], [tool calls], [synthetic tasks], [online reinforcement learning], [UltraCUA]
    - 📖 TLDR: UltraCUA bridges low-level GUI actions and higher-level tool use in one computer-use model instead of forcing every task through clicks, typing, and scrolling alone. Its pipeline combines automated tool extraction, synthetic verifiable tasks, supervised fine-tuning, and online RL, and the resulting hybrid-action models improve both OSWorld performance and transfer to WindowsAgentArena.

- [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221)
    - Zhaoyang Liu, Jingjing Xie, Zichen Ding, Zehao Li, Bowen Yang, Zhenyu Wu, Xuehui Wang, Qiushi Sun, Shi Liu, Weiyun Wang, Shenglong Ye, Qingyun Li, Xuan Dong, Yue Yu, Chenyu Lu, YunXiang Mo, Yao Yan, Zeyue Tian, Xiao Zhang, Yuan Huang, Yiqian Liu, Weijie Su, Gen Luo, Xiangyu Yue, Biqing Qi, Kai Chen, Bowen Zhou, Yu Qiao, Qifeng Chen, Wenhai Wang
    - 🏛️ Institutions: Shanghai AI Laboratory
    - 📅 Date: September 18, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [cross-platform data], [closed-loop data pipeline], [six operating systems], [grounding mode], [reasoned action], [ScaleCUA]
    - 📖 TLDR: ScaleCUA builds an open computer-use dataset across six operating systems and three GUI task families through a closed-loop pipeline that combines automated agents with human experts. Models trained on this corpus support grounding, direct-action, and reasoned-action inference modes and reach strong cross-platform results on WebArena-Lite-v2, OSWorld-G, and MMBench-GUI.

- [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)
    - Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, Zhengxi Lu, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: August 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [model], [GUI-Owl], [self-evolving trajectory production], [trajectory correctness judgment], [TRPO], [multi-agent framework], [Mobile-Agent-v3]
    - 📖 TLDR: This paper introduces GUI-Owl as a foundation model for GUI automation and builds Mobile-Agent-v3 as a multi-agent framework on top of it. The work combines cross-OS trajectory production, diverse GUI data synthesis, reasoning enhancement, and trajectory-aware RL, and reports stronger open-source results on both AndroidWorld and OSWorld.

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua, Zhipu, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [reinforcement learning], [API-GUI paradigm], [distributed RL infrastructure], [parallel virtual desktops], [Entropulse], [OSWorld], [ComputerRL]
    - 📖 TLDR: ComputerRL is a desktop-agent training framework that combines direct GUI interaction with programmatic APIs and scales online RL through a distributed infrastructure over thousands of parallel virtual desktops. Its Entropulse schedule alternates RL and supervised fine-tuning to stabilize long training runs, and the resulting GLM-ComputerRL-9B reaches 48.9% on OSWorld.

- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
    - Zhangxuan Gu, Zhengwen Zeng, Zhenyu Xu, Xingran Zhou, Shuheng Shen, Yunfei Liu, Beitong Zhou, Changhua Meng, Tianyu Xia, Weizhi Chen, Yue Wen, Jingya Dou, Fei Tang, Jinzhen Lin, Yulin Liu, Zhenlin Guo, Yichen Gong, Heng Jia, Changlong Gao, Yuan Guo, Yong Deng, Zhenyu Guo, Liang Chen, Weiqiang Wang
    - 🏛️ Institutions: Ant Group
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [reinforcement fine-tuning], [trajectory history alignment], [sparse action enhancement], [Qwen2.5-VL], [UI-Venus]
    - 📖 TLDR: UI-Venus is a screenshot-only UI agent built on Qwen2.5-VL and trained with reinforcement fine-tuning plus data-cleaning pipelines for both grounding and navigation. The report attributes its gains to reward design and a self-evolving history-alignment and sparse-action mechanism, and reports strong results on ScreenSpot benchmarks and AndroidWorld.

- [DPO Learning with LLMs-Judge Signal for Computer Use Agents](https://arxiv.org/abs/2506.03095)
    - Man Luo, David Cobbley, Xin Su, Shachar Rosenman, Vasudev Lal, Shao-Yen Tseng, Phillip Howard
    - 🏛️ Institutions: Intel, Thoughtworks
    - 📅 Date: June 03, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [reinforcement learning], [DPO], [LLM-as-Judge], [local inference], [synthetic trajectories]
    - 📖 TLDR: This paper targets privacy and compute constraints in computer-use agents by training a lightweight VLM that runs entirely on local machines. It uses an LLM-as-Judge pipeline to score synthetic GUI trajectories and construct DPO preference pairs, then shows that the resulting local agent outperforms baselines on OSWorld.

- [AgentCPM‑GUI: Building Mobile‑Use Agents with Reinforcement Fine‑Tuning](https://aclanthology.org/2025.emnlp-demos.12/)
    - Zhong Zhang, Yaxi Lu, Yikun Fu, Yupeng Huo, Shenzhi Yang, Yesai Wu, Han Si, Xin Cong, Haotian Chen, Yankai Lin, Jie Xie, Wei Zhou, Wang Xu, Yuanheng Zhang, Zhou Su, Zhongwu Zhai, Xiaoming Liu, Yudong Mei, Jianming Xu, Hongyan Tian, Chongyi Wang, Chi Chen, Yuan Yao, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Tsinghua, Renmin University of China, ModelBest
    - 📅 Date: June 02, 2025
    - 📑 Publisher: EMNLP 2025 System Demonstrations
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [benchmark], [reinforcement learning], [GRPO], [grounding-aware pre-training], [CAGUI], [AgentCPM-GUI]
    - 📖 TLDR: AgentCPM-GUI is an 8B mobile GUI model aimed at robust on-device interaction, especially for Chinese and English interfaces. It combines grounding-aware pre-training, supervised trajectory imitation, and GRPO-based reinforcement fine-tuning, and reports strong results on five public benchmarks plus the newly proposed Chinese benchmark CAGUI.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [reward model], [self-improvement], [outcome verification], [UI-Genie]
    - 📖 TLDR: UI-Genie targets two mobile-agent bottlenecks: reliable outcome verification and scalable high-quality training data. It combines an interleaved reward model with a reward-guided self-improvement loop, releases reward-specific GUI datasets, and reports stronger mobile-agent performance across multiple rounds of self-improvement.

- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277)
    - Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
    - 🏛️ Institutions: Yonsei University, CMU
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [dataset], [benchmark], [reward model], [WebRewardBench], [Web-Shepherd]
    - 📖 TLDR: Web-Shepherd introduces the first process reward model specialized for web navigation, along with the WebPRM Collection of 40K step-level preference pairs and the WebRewardBench meta-evaluation benchmark. It substantially outperforms generic frontier-model verifiers on web trajectories while reducing verification cost enough for both RL training and test-time use.

- [Efficient Agent Training for Computer Use](https://arxiv.org/abs/2505.13909)
    - Yanheng He, Jiahe Jin, Pengfei Liu
    - 🏛️ Institutions: SJTU, SII, Generative AI Research Lab (GAIR)
    - 📅 Date: May 20, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [dataset], [benchmark], [trajectory augmentation], [WindowsAgentArena-V2], [PC Agent-E]
    - 📖 TLDR: This paper studies data-efficient training for desktop computer-use agents, starting from only 312 human trajectories and augmenting them with diversified action decisions sampled from Claude 3.7 Sonnet. The resulting PC Agent-E model improves strongly over the base model, surpasses Claude 3.7 Sonnet on WindowsAgentArena-V2, and releases the improved benchmark alongside the training recipe.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: MSR, NTU, AIR, Tsinghua, HKUST
    - 📅 Date: March 20, 2025
    - 📑 Publisher: MobiCom 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [verifier-driven], [discretized action space], [prefilling-only workflow], [pair-wise progress preference training], [V-Droid]
    - 📖 TLDR: V-Droid is a mobile GUI agent that uses LLMs as verifiers to score candidate actions instead of generating actions autoregressively. The paper pairs that design with a discretized action space, prefilling-only verification, and pair-wise progress preference training, reaching strong benchmark performance at 4.3 seconds per step.

- [STEVE: A Step Verification Pipeline for Computer-use Agent Training](https://arxiv.org/abs/2503.12532)
    - Fanbin Lu, Zhisheng Zhong, Ziqin Wei, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: CUHK, SmartMore, HKUST
    - 📅 Date: March 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [model], [step verification], [binary stepwise labels], [KTO], [STEVE]
    - 📖 TLDR: STEVE trains desktop computer-use agents from suboptimal trajectories by verifying each step against before-and-after screenshots instead of relying on expensive gold trajectories. The resulting binary step labels support KTO training of a 7B agent that outperforms supervised fine-tuning on WinAgentArena.

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: ZJU, MSR Asia
    - 📅 Date: March 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [dual-system cognition], [adaptive system switching], [progressive decomposition], [Focus]
    - 📖 TLDR: Focus is a GUI grounding model that switches between fast prediction and slower analysis depending on task complexity. It decomposes grounding into summarization, focused visual analysis, and coordinate prediction, and reaches strong ScreenSpot and ScreenSpot-Pro performance with a 2B model trained on 300K examples.

- [SpiritSight Agent: Advanced GUI Agent with One Look](https://arxiv.org/abs/2503.03196)
    - Zhiyuan Huang, Ziming Cheng, Junting Pan, Zhaohui Hou, Mingjie Zhan
    - 🏛️ Institutions: SenseTime Research, Beijing University of Posts and Telecommunications, MMLab, CUHK
    - 📅 Date: March 05, 2025
    - 📑 Publisher: CVPR 2025 (Poster)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI-Lasagne], [Universal Block Parsing], [single-screenshot inference], [SpiritSight]
    - 📖 TLDR: SpiritSight is an end-to-end GUI agent designed to act from a single screenshot while retaining strong cross-platform grounding accuracy. The paper pairs the GUI-Lasagne dataset with Universal Block Parsing to reduce dynamic-resolution ambiguity and reports gains across web, mobile, and desktop benchmarks.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, UCL
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [lightweight VLM], [offline-to-online training], [AndroidControl], [AndroidWorld], [AppVLM]
    - 📖 TLDR: AppVLM is a lightweight vision-language model for mobile app control that is trained first on AndroidControl and then refined with trajectories collected in AndroidWorld. It achieves the best offline action prediction among the compared baselines and matches GPT-4o on online AndroidWorld success rate while running much faster.

- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)
    - Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng, Xin Liu, Guang Shi
    - 🏛️ Institutions: ByteDance Seed, Tsinghua
    - 📅 Date: January 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [GUI grounding], [unified action modeling], [system-2 reasoning], [reflective online traces], [UI-TARS]
    - 📖 TLDR: UI-TARS is an end-to-end GUI agent model that acts directly from screenshots instead of relying on wrapper-style prompting workflows around proprietary models. It combines enhanced perception, unified cross-platform action modeling, deliberate multi-step reasoning, and iterative training on reflective online traces, and reports strong performance across ten-plus GUI benchmarks.

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: HKU, Salesforce AI Research, Alibaba Group, Australian National University, Independent Researcher
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [pure vision], [instruction synthesis], [context-aware grounding], [Aria-UI]
    - 📖 TLDR: Aria-UI is a GUI-grounding model that deliberately avoids HTML or AXTree inputs and instead works from pure visual observations. It pairs a scalable instruction-synthesis pipeline with interleaved textual and text-image action histories for context-aware grounding, and reports state-of-the-art results across offline and online grounding benchmarks.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: ZJU, NUS
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [GUI grounding], [information-sensitive cropping], [self-refining dual learning], [visual grounding], [Iris]
    - 📖 TLDR: Iris targets the visual-perception bottleneck of GUI agents in high-resolution, visually complex interfaces. It combines information-sensitive cropping with a self-refining dual-learning loop between referring and grounding, and the resulting gains transfer to both web and OS downstream tasks.

- [Falcon-UI: Understanding GUI Before Following User Instructions](https://arxiv.org/abs/2412.09362)
    - Huawen Shen, Chang Liu, Gengluo Li, Xinlong Wang, Yu Zhou, Can Ma, Xiangyang Ji
    - 🏛️ Institutions: Institute of Information Engineering, CAS, Nankai University, Tsinghua, Beijing Academy of Artificial Intelligence, University of Chinese Academy of Sciences
    - 📅 Date: December 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [Insight-UI Dataset], [GUI understanding], [instruction-free pretraining], [Falcon-UI]
    - 📖 TLDR: Falcon-UI studies whether GUI-context understanding should be learned before instruction following. It introduces the large instruction-free Insight-UI Dataset for GUI pretraining and shows that this staged training improves a 7B model enough to approach much larger baselines.

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: HKU, Salesforce AI Research
    - 📅 Date: December 05, 2024
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [pure vision], [inner monologue], [two-stage training], [Aguvis]
    - 📖 TLDR: Aguvis is a pure-vision GUI agent that removes textual interface representations and operates directly on screen images. It combines a large grounding-and-reasoning dataset with a two-stage training pipeline and inner-monologue reasoning, reporting strong offline and online performance without relying on closed-source models.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://aclanthology.org/2025.findings-acl.76/)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Shenzhen International Graduate School, Tsinghua
    - 📅 Date: December 02, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [pure vision], [GUI grounding], [interpreter-locator], [ScreenSpot], [Ponder & Press]
    - 📖 TLDR: Ponder & Press is a pure-vision divide-and-conquer GUI-control framework that separates high-level instruction interpretation from element localization. It pairs a general-purpose MLLM interpreter with a GUI-specific locator, improves ScreenSpot grounding by 22.5%, and reports strong performance across web, desktop, and mobile GUI benchmarks.

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025 (Poster)
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [UI-guided visual token selection], [interleaved vision-language-action streaming], [screenshot grounding], [ShowUI]
    - 📖 TLDR: ShowUI is a lightweight vision-language-action model for GUI visual agents that targets efficient screenshot perception and action-history modeling. It introduces UI-guided visual token selection and interleaved vision-language-action streaming, reaching 75.1% zero-shot screenshot grounding while remaining competitive on web and mobile GUI tasks.

- [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Laboratory, SJTU, HKU, MIT
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform corpus], [OS-Atlas]
    - 📖 TLDR: OS-Atlas is a foundation action model for GUI agents built on a multi-platform grounding-data synthesis toolkit and a corpus with more than 13 million GUI elements. It improves GUI grounding and zero-shot out-of-distribution agent performance across desktop, mobile, and web benchmarks.

- [AutoGLM: Autonomous Foundation Agents for GUIs](https://arxiv.org/abs/2411.00820)
    - Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long Iong, Jiadai Sun, Jiaqi Wang, Junjie Gao, Junjun Shan, Kangning Liu, Shudan Zhang, Shuntian Yao, Siyi Cheng, Wentao Yao, Wenyi Zhao, Xinghan Liu, Xinyi Liu, Xinying Chen, Xinyue Yang, Yang Yang, Yifan Xu, Yu Yang, Yujia Wang, Yulin Xu, Zehan Qi, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu, Tsinghua
    - 📅 Date: October 28, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [model], [foundation agent], [intermediate interface], [progressive reinforcement learning], [AutoGLM]
    - 📖 TLDR: AutoGLM is a foundation-agent system for browser and phone control that emphasizes an intermediate interface separating planning from grounding. The paper pairs that design with progressive self-evolving reinforcement learning and reports strong performance on both web and Android evaluations.

- [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://aclanthology.org/2024.findings-emnlp.599/)
    - Qinzhuo Wu, Weikai Xu, Wei Liu, Tao Tan, Jianfeng Liu, Ang Li, Jian Luan, Bin Wang, Shuo Shang
    - 🏛️ Institutions: XiaoMi AI Lab, University of Electronic Science and Technology of China, Renmin University of China
    - 📅 Date: September 23, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [Mobile3M], [intra-UI understanding], [inter-UI understanding], [MobileVLM]
    - 📖 TLDR: MobileVLM is a mobile-focused vision-language model trained with two extra UI-specific pretraining stages designed to improve both intra-UI element understanding and inter-UI transition understanding. The paper also introduces the 3M-page Chinese mobile corpus Mobile3M with real transition-action graphs, and reports stronger performance than prior VLMs on in-house and public mobile benchmarks.

- [MobileFlow: A Multimodal LLM for Mobile GUI Agent](https://arxiv.org/abs/2407.04346)
    - Songqin Nong, Jiali Zhu, Rui Wu, Jiongchao Jin, Shuo Shan, Xiutian Huang, Wenhao Xu
    - 🏛️ Institutions: Ant Group
    - 📅 Date: July 05, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [hybrid visual encoders], [multilingual GUI], [Mixture of Experts], [GUI alignment], [MobileFlow]
    - 📖 TLDR: MobileFlow adapts Qwen-VL-Chat into a 21B mobile GUI model with hybrid visual encoders, MoE expansion, and GUI-specific alignment and chain-of-thought training. The model is built to handle variable-resolution screens and multilingual interfaces without depending on system APIs for page layout access.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://dl.acm.org/doi/10.1145/3637528.3671620)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua, Zhipu, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences
    - 📅 Date: April 04, 2024
    - 📑 Publisher: KDD 2024
    - 💻 Env: [Web]
    - 🔑 Key: [model], [benchmark], [AutoWebBench], [HTML simplification], [curriculum training], [reinforcement learning]
    - 📖 TLDR: AutoWebGLM is a web-navigation agent built on ChatGLM3-6B that combines HTML simplification, hybrid human-AI trajectory construction, and reinforcement learning with rejection sampling. The paper also introduces the bilingual AutoWebBench benchmark for real-world web navigation and uses it together with other benchmarks to evaluate the system.

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://www.ijcai.org/proceedings/2024/339)
    - Gilles Baechler, Srinivas Sunkara, Maria Wang, Fedir Zubach, Hassan Mansoor, Vincent Etter, Victor Cărbune, Jason Lin, Jindong Chen, Abhanshu Sharma
    - 🏛️ Institutions: Google Research
    - 📅 Date: February 07, 2024
    - 📑 Publisher: IJCAI 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [screen annotation], [UI understanding], [ScreenAI]
    - 📖 TLDR: ScreenAI is a vision-language model for UI and infographics understanding that combines a PaLI-style architecture with pix2struct-style flexible patching. It introduces a screen-annotation task, uses it to generate large-scale UI training data, and releases three datasets for screen annotation and screen question answering.

- [CogAgent: A Visual Language Model for GUI Agents](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_CogAgent_A_Visual_Language_Model_for_GUI_Agents_CVPR_2024_paper.html)
    - Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhui Ji, Yan Wang, Zihan Wang, Yuxiao Dong, Ming Ding, Jie Tang
    - 🏛️ Institutions: Tsinghua, Zhipu
    - 📅 Date: December 14, 2023
    - 📑 Publisher: CVPR 2024 (Highlight)
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [high-resolution GUI understanding], [dual-resolution encoders], [Mind2Web], [AITW], [CogAgent]
    - 📖 TLDR: CogAgent is an 18B visual language model specialized for GUI understanding and navigation. It combines low- and high-resolution image encoders, trains on a large GUI-and-OCR dataset, and outperforms HTML-consuming baselines on Mind2Web and AITW using screenshots alone.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: MSR Asia
    - 📅 Date: October 07, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [instruction grounding], [pixel-to-sequence], [reinforced decoding], [RUIG]
    - 📖 TLDR: RUIG is a metadata-free grounding model that maps natural-language instructions to coordinates on UI screenshots with a pixel-to-sequence decoder. Its main contribution is an RL-style supervision method that strengthens coordinate decoding and positions the model as a generic UI automation executor rather than a full agent framework.

- [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7ef7d8359036afd8c2378d82c21058a4-Abstract-Conference.html)
    - Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu, Izzeddin Gur
    - 🏛️ Institutions: University of Tokyo, Google DeepMind
    - 📅 Date: May 19, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [model], [dataset], [WebGUM], [offline training], [demonstration learning], [cross-benchmark transfer]
    - 📖 TLDR: This paper studies offline multimodal web-agent training with WebGUM, which takes both webpage screenshots and HTML as input. It also releases 347K demonstrations and shows strong gains on MiniWoB and WebShop, with positive transfer to Mind2Web.

- [Spotlight: Mobile UI Understanding using Vision-Language Models with a Focus](https://proceedings.iclr.cc/paper_files/paper/2023/hash/0f4145fde6f5ae66745ef2a16bd1a7cd-Abstract-Conference.html)
    - Gang Li, Yang Li
    - 🏛️ Institutions: Google Research
    - 📅 Date: September 29, 2022
    - 📑 Publisher: ICLR 2023 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [Spotlight], [focus region], [vision-only UI understanding]
    - 📖 TLDR: Spotlight is a vision-only mobile UI understanding model that takes a screenshot plus a region of interest instead of relying on view hierarchy input. It is pretrained on about 2.5 million mobile UI screens and then used for widget captioning, screen summarization, command grounding, and related UI modeling tasks.

- [UIBert: Learning Generic Multimodal Representations for UI Understanding](https://www.ijcai.org/proceedings/2021/235)
    - Chongyang Bai, Xiaoxue Zang, Ying Xu, Srinivas Sunkara, Abhinav Rastogi, Jindong Chen, Blaise Agüera y Arcas
    - 🏛️ Institutions: Dartmouth College, Google Research
    - 📅 Date: July 29, 2021
    - 📑 Publisher: IJCAI 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [pretraining], [multimodal representation learning], [self-alignment], [UIBert]
    - 📖 TLDR: UIBert is a transformer model for UI understanding trained with five UI-specific pretraining tasks over screenshots, text, and structural metadata. Its core idea is that the heterogeneous modalities inside a UI are self-aligned and can supervise one another to learn generic UI representations.
