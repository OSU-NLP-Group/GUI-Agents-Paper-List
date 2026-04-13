# Papers with Keyword: reinforcement learning

- [UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience](https://arxiv.org/abs/2603.24533)
    - Zichuan Lin, Feiyu Liu, Yijun Yang, Jiafei Lyu, Yiming Gao, Yicheng Liu, Zhicong Lu, Yangbin Yu, Mingyu Yang, Junyou Li, Deheng Ye, Jie Jiang
    - 🏛️ Institutions: Tencent Hunyuan
    - 📅 Date: March 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [self-evolving], [failed trajectory learning], [RFT], [GRSD], [AndroidWorld], [UI-Voyager]
    - 📖 TLDR: UI-Voyager is a self-evolving mobile GUI agent that learns from failed trajectories instead of manual annotations. Its two-stage training combines rejection fine-tuning with group-relative self-distillation to turn successful rollouts into dense corrective supervision, yielding 81.0% Pass@1 on AndroidWorld with a 4B model.

- [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191)
    - Zehao Li, Zhenyu Wu, Yibo Zhao, Bowen Yang, Jingjing Xie, Zhaoyang Liu, Zhoumianze Liu, Kaiming Jin, Jianze Liang, Zonglin Li, Feng Wu, Bowen Zhou, Zun Wang, Zichen Ding
    - 🏛️ Institutions: USTC, Shanghai AI Laboratory, CUHK MMLab, HKUST, NUS
    - 📅 Date: March 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [reinforcement learning], [critic framework], [OmniGUIRewardBench], [milestone decomposition], [OS-Themis]
    - 📖 TLDR: OS-Themis is a scalable critic framework for GUI reward modeling that breaks trajectories into verifiable milestones and audits the evidence chain before issuing a verdict. It improves AndroidWorld training and filtering loops and introduces OmniGUIRewardBench as a cross-platform benchmark for GUI outcome rewards.

- [Generalization in Online Reinforcement Learning for Mobile Agents](https://arxiv.org/abs/2603.07432)
    - Li Gu, Zihuan Jiang, Zhixiang Chi, Huan Liu, Ziqiang Wang, Yuanhao Yu, Glen Berseth, Yang Wang
    - 🏛️ Institutions: Mila, Concordia University, Université de Montréal, CIFAR AI Chair, University of Toronto, McMaster University
    - 📅 Date: March 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [benchmark], [generalization], [AndroidWorld-Generalization], [GRPO], [test-time adaptation]
    - 📖 TLDR: This paper studies generalization in online RL for mobile agents, introducing AndroidWorld-Generalization to measure transfer to unseen instances, templates, and applications. Its open RL training system shows gains over supervised fine-tuning on unseen instances, but also highlights that unseen templates and apps remain much harder without additional adaptation.

- [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)
    - Sicheng Fan, Qingyun Shi, Shengze Xu, Shengbo Cai, Tieyong Zeng, Li Ling, Yanyi Shang, Dehan Kong
    - 🏛️ Institutions: Fudan, IMean AI, CUHK, Tsinghua
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [reinforcement learning], [synthetic data], [environment synthesis], [task generation], [embodiment potential], [WebFactory]
    - 📖 TLDR: WebFactory presents a closed-loop training pipeline that compresses LLM latent internet knowledge into grounded web-agent behavior through synthetic environment generation, task generation, trajectory collection, and decomposed-reward RL. It matches agents trained on comparable amounts of human data while using synthetic data from only 10 websites.

- [CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning](https://arxiv.org/abs/2603.02951)
    - Zhenquan Yao, Zitong Huang, Yihan Zeng, Jianhua Han, Hang Xu, Chun-Mei Feng, Jianwei Ma, Wangmeng Zuo
    - 🏛️ Institutions: Harbin Institute of Technology, Huawei Noah's Ark Lab, University College Dublin, PKU
    - 📅 Date: March 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [gradient surgery], [policy entropy], [AndroidControl-CL], [CGL]
    - 📖 TLDR: CGL studies continual GUI learning under app updates, combining supervised adaptation with reinforcement fine-tuning to retain prior interaction skills. It uses policy-entropy-guided SFT weighting and gradient surgery against GRPO anchor gradients, and introduces AndroidControl-CL to benchmark continual adaptation without catastrophic forgetting.

- [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190)
    - Rui Yang, Qianhui Wu, Zhaoyang Wang, Hanyang Chen, Ke Yang, Hao Cheng, Huaxiu Yao, Baoling Peng, Huan Zhang, Jianfeng Gao, Tong Zhang
    - 🏛️ Institutions: UIUC, Microsoft, UNC
    - 📅 Date: February 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [post-training], [reinforcement learning], [action-aware supervision], [partial verifiability], [GUI reasoning dataset], [GUI-Libra]
    - 📖 TLDR: GUI-Libra is a post-training recipe for native GUI agents that combines curated reasoning data, action-aware supervised fine-tuning, and partially verifiable RL. It targets the mismatch between chain-of-thought reasoning and grounding, and improves both step-level accuracy and end-to-end task completion on web and mobile benchmarks.

- [OpAgent: Operator Agent for Web Navigation](https://arxiv.org/abs/2602.13559)
    - Yuyu Guo, Wenjie Yang, Siyuan Yang, Ziyang Liu, Cheng Chen, Yuan Wei, Yun Hu, Yang Huang, Guoliang Hao, Dongsheng Yuan, Jianming Wang, Xin Chen, Hang Yu, Lei Lei, Peng Di
    - 🏛️ Institutions: Ant Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [reinforcement learning], [planner-grounder-reflector-summarizer], [hierarchical multitask fine-tuning], [WebArena], [OpAgent]
    - 📖 TLDR: OpAgent combines a modular planner-grounder-reflector-summarizer design with online reinforcement learning on unconstrained web environments. The paper reports strong WebArena performance and studies how modular coordination and RL improve web navigation.

- [Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization](https://arxiv.org/abs/2602.13653)
    - Yibo Wang, Guangda Huzhang, Yuwei Hu, Yu Xia, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Lijun Zhang
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, NJU, Ovis Team, Alibaba Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [agentic-Q estimation], [step-wise policy optimization], [Ovis2.5-9B], [GUI navigation], [grounding]
    - 📖 TLDR: This paper trains GUI agents with an agentic-Q model that estimates each action's contribution to task completion and a step-wise policy optimization routine decoupled from online interaction. The design keeps data collection manageable while stabilizing updates and improving navigation and grounding performance.

- [Adaptive Milestone Reward for GUI Agents](https://arxiv.org/abs/2602.11524)
    - Congmin Zheng, Xiaoyun Mo, Xinbei Ma, Qiqiang Lin, Yin Zhao, Jiachen Zhu, Xingyu Lou, Jun Wang, Zhaoxiang Wang, Weiwen Liu, Zhuosheng Zhang, Yong Yu, Weinan Zhang
    - 🏛️ Institutions: SJTU, OPPO Research Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [reward shaping], [credit assignment], [milestone reward], [ADMIRE], [AndroidWorld]
    - 📖 TLDR: ADMIRE is a reinforcement-learning reward design for GUI agents that distills adaptive, verifiable milestones from successful trajectories and pairs them with asymmetric credit assignment. It improves AndroidWorld performance by more than 10 absolute points and transfers to other RL algorithms and environments.

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: OSU, UC Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL], [curriculum learning]
    - 📖 TLDR: ACuRL studies continual adaptation for computer-use agents in changing environments without human demonstrations. It combines autonomous curriculum generation with CUAJudge-based evaluation to improve both within-environment and cross-environment adaptation while limiting forgetting.

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: Multimedia Laboratory (MMLab), CUHK, vivo AI Lab, Princeton, Shenzhen Loop Area Institute, Shanghai AI Laboratory
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [memory], [reinforcement learning], [online RL], [hierarchical experience memory], [stratified group sampling], [UI-Mem]
    - 📖 TLDR: UI-Mem augments online RL for mobile GUI agents with a hierarchical experience memory that stores reusable workflows, subtask skills, and failure patterns as transferable templates. Its stratified group sampling lets the policy absorb memory-informed behavior and improves over standard online RL baselines.

- [SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization](https://arxiv.org/abs/2601.22491)
    - Jinyang Wu, Changpeng Yang, Yuhao Shen, Fangzhi Xu, Bolin Ni, Chonghua Liao, Yuchen Liu, Hongzhen Wang, Shuai Nie, Shuai Zhang, Haoran Luo, Jiaming Xu
    - 🏛️ Institutions: Tsinghua, Xiaomi, ZJU, NTU, Institute of Automation, CAS
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [tiered rewards], [reward shaping], [GUI grounding], [planning], [SSL]
    - 📖 TLDR: SSL replaces binary verifier rewards with progressively amplified tiered rewards that distinguish higher- and lower-quality successful trajectories. Across GUI perception, short- and long-horizon planning, and reasoning benchmarks, it improves optimization stability and reaches up to 2.5x better sample efficiency than binary-reward baselines.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: USTC, Institute of Artificial Intelligence (TeleAI), China Telecom, Shanghai Innovation Institute, SJTU
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [active perception], [tool-augmented perception], [ScreenSpot-pro], [GUI-Eyes]
    - 📖 TLDR: GUI-Eyes frames GUI grounding as active perception, letting the agent learn when and how to call tools such as cropping and zooming inside a two-stage reasoning process. It pairs that policy with a spatially continuous reward for tool use and reaches 44.8% grounding accuracy on ScreenSpot-Pro using only 3k labeled samples.

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu
    - 🏛️ Institutions: NJU, PKU, Microsoft Research Asia
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [RLVR], [off-policy assimilation], [BEPA], [OSWorld]
    - 📖 TLDR: BEPA improves end-to-end GUI-agent training with verifiable rewards by turning scarce off-policy expert traces into policy-aligned guidance through self-rolled reachable trajectories and a dynamically updated per-task cache. On OSWorld-Verified it raises UI-TARS-1.5-7B from 22.87% to 32.13%, with additional gains on MMBench-GUI and Online-Mind2Web.

- [WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks](https://arxiv.org/abs/2601.02439)
    - Hao Bai, Alexey Taymanov, Tong Zhang, Aviral Kumar, Spencer Whitehead
    - 🏛️ Institutions: Microsoft, UIUC, CMU
    - 📅 Date: January 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [training environment], [reinforcement learning], [asynchronous rollouts], [WebGym]
    - 📖 TLDR: WebGym provides a large-scale open training environment for visual web agents with nearly 300,000 rubric-evaluated tasks on realistic websites. It also includes a high-throughput asynchronous rollout system, and agents fine-tuned on WebGym improve from 26.2% to 42.9% on out-of-distribution websites, outperforming GPT-4o and GPT-5-Thinking.

- [SmartSnap: Proactive Evidence Seeking for Self-Verifying Agents](https://arxiv.org/abs/2512.22322)
    - Shaofei Cai, Yulei Qin, Haojia Lin, Zihan Xu, Gang Li, Yuchen Shi, Zongyi Li, Yong Mao, Siqi Cai, Xiaoyu Tan, Yitao Liang, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, Institute for Artificial Intelligence, PKU
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [self-verification], [evidence seeking], [LLM-as-a-judge], [AndroidLab]
    - 📖 TLDR: SmartSnap turns task verification from a passive post-hoc check into proactive evidence seeking, training mobile GUI agents to collect a minimal set of decisive snapshots under the 3C principles so an LLM judge can verify success more reliably, yielding large gains on AndroidLab across 8B and 30B agents.

- [GUI Exploration Lab: Enhancing Screen Navigation in Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2512.02423)
    - Haolong Yan, Yeqing Shen, Xin Huang, Jia Wang, Kaijun Tan, Zhixuan Liang, Hongxin Li, Zheng Ge, Osamu Yoshie, Si Li, Xiangyu Zhang, Daxin Jiang
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, StepFun, Waseda University, Institute of Automation, CAS
    - 📅 Date: December 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [screen navigation], [simulation environment], [reinforcement learning], [exploration strategy], [GUI Exploration Lab]
    - 📖 TLDR: GUI Exploration Lab is a simulation engine for studying screen navigation, exposing full screen and navigation-graph structure so agents can be trained and evaluated without proprietary GUI environments. The paper compares supervised fine-tuning, single-turn RL, and multi-turn RL, and finds that multi-turn RL is what most clearly induces exploratory navigation behavior.

- [HiconAgent: History Context-aware Policy Optimization for GUI Agents](https://arxiv.org/abs/2512.01763)
    - Xurui Zhou, Gongwei Chen, Yuquan Xie, Zaijing Li, Kaiwen Zhou, Shuai Wang, Shuo Yang, Zhuotao Tian, Rui Shao
    - 🏛️ Institutions: HIT-Shenzhen, Huawei Noah’s Ark Lab
    - 📅 Date: December 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [history usage], [Dynamic Context Sampling], [Anchor-guided History Compression], [HiconAgent]
    - 📖 TLDR: HiconAgent studies how GUI agents should use historical context during sequential navigation instead of always keeping a fixed full history. Its HCPO training recipe combines Dynamic Context Sampling with Anchor-guided History Compression, and the resulting 3B model improves GUI-Odyssey while matching or approaching larger baselines on AndroidControl and AITW at lower compute cost.

- [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235)
    - Zehao Deng, Tianjie Ju, Zheng Wu, Zhuosheng Zhang, Gongshen Liu
    - 🏛️ Institutions: Soochow University, SJTU
    - 📅 Date: November 27, 2025
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [long-horizon tasks], [state tracking], [task decomposition], [CES]
    - 📖 TLDR: This paper targets long-horizon GUI automation by training high-level scheduling modules instead of a single end-to-end executor. Its CES framework separates coordination, execution, and state tracking, and uses execution-feedback reinforcement learning to improve planning and task-state management across different low-level executors.

- [WebServ: A Browser-Server Environment for Efficient Training of Reinforcement Learning-based Web Agents at Scale](https://arxiv.org/abs/2510.16252)
    - Yuxuan Lu, Jing Huang, Hui Liu, Jiri Gesi, Yan Han, Shihan Fu, Tianqi Zheng, Dakuo Wang
    - 🏛️ Institutions: Northeastern University, Amazon
    - 📅 Date: October 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [reinforcement learning], [training environment], [browser-server architecture], [scalability], [WebServ]
    - 📖 TLDR: WebServ is a full-stack environment for large-scale RL training of web agents that combines a compact browser-side interface with efficient isolated server-side state management. It is designed to make parallel rollouts practical, and the paper reports faster launches, lower storage cost, and strong WebArena performance.

- [Efficient Multi-turn RL for GUI Agents via Decoupled Training and Adaptive Data Curation](https://arxiv.org/abs/2509.23866)
    - Pengxiang Li, Zechen Hu, Zirui Shang, Jingrong Wu, Yang Liu, Hui Liu, Zhi Gao, Chenrui Shi, Bofei Zhang, Zihao Zhang, Xiaochuan Shi, Zedong YU, Yuwei Wu, Xinxiao Wu, Yunde Jia, Liuyu Xiang, Zhaofeng He, Qing Li
    - 🏛️ Institutions: Beijing Institute of Technology, State Key Laboratory of General Artificial Intelligence, BIGAI, DataCanvas, Beijing University of Posts and Telecommunications, Shenzhen MSU-BIT University
    - 📅 Date: September 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [reinforcement learning], [decoupled training], [adaptive data curation], [asynchronous modules], [OSWorld], [DART]
    - 📖 TLDR: DART is a decoupled RL training framework for GUI agents that separates environment execution, rollout service, data management, and training into asynchronous modules to improve multi-turn learning efficiency. It pairs that system design with adaptive data curation, including difficulty-aware rollout control and high-entropy step selection, and substantially improves OSWorld performance over the base model.

- [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)
    - Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: May 28, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [information seeking], [browsing data construction], [trajectory sampling], [reinforcement learning], [WebDancer]
    - 📖 TLDR: WebDancer studies end-to-end training for long-horizon web information-seeking agents rather than short templated browser tasks. It presents a four-stage data and training pipeline covering browsing data construction, trajectory sampling, supervised fine-tuning, and reinforcement learning, and reports strong results on GAIA and WebWalkerQA.

- [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2505.16421)
    - Zhepei Wei, Wenlin Yao, Yao Liu, Weizhi Zhang, Qin Lu, Liang Qiu, Changlong Yu, Puyang Xu, Chao Zhang, Bing Yin, Hyokun Yun, Lihong Li
    - 🏛️ Institutions: University of Virginia, Amazon, Georgia Tech
    - 📅 Date: May 22, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Web]
    - 🔑 Key: [reinforcement learning], [multi-turn interaction], [WebArena-Lite], [test-time scaling], [WebAgent-R1]
    - 📖 TLDR: WebAgent-R1 studies end-to-end multi-turn reinforcement learning for web agents rather than single-turn reasoning tasks. It learns directly from online browser interactions with binary success rewards and substantially improves small open models on WebArena-Lite, surpassing prior methods and some proprietary baselines.

- [ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282)
    - Fanbin Lu, Zhisheng Zhong, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: CUHK, SmartMore, HKUST
    - 📅 Date: May 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [reinforcement learning], [experience replay], [GRPO], [task selection], [ARPO]
    - 📖 TLDR: ARPO studies end-to-end reinforcement learning for GUI agents in long-horizon desktop environments where sparse rewards and rollout cost make optimization difficult. It augments GRPO with replayed successful experience and task selection, establishing a stronger OSWorld training baseline than prior policy-optimization approaches.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [reinforcement learning], [fast thinking template], [difficulty-aware scaling], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: NKU, vivo Mobile Communication Co., Ltd, NUS, Fudan, East China University of Science and Technology
    - 📅 Date: May 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [GUI grounding], [dense policy gradient], [self-evolutionary finetuning], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications
    - 📅 Date: May 18, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [self-supervised learning], [K-step GUI Transition], [inverse dynamics], [GUI-Shift]
    - 📖 TLDR: GUI-Shift studies how to train GUI agents from unlabeled trajectories instead of expensive instruction annotations. It introduces the K-step GUI Transition inverse-dynamics task and a self-supervised RL pipeline, improving both mobile GUI automation and grounding performance across multiple benchmarks.

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
    - 🏛️ Institutions: ZJU, Dalian University of Technology, Reallm Labs, PolyU
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [reasoning injection], [sub-goal guidance], [error recovery], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: InfiGUI-R1 is trained to shift GUI agents from reactive action prediction toward explicit deliberative reasoning. Its Actor2Reasoner pipeline first distills cross-modal spatial reasoning into the model, then uses reinforcement learning with sub-goal guidance and failure-recovery scenarios to strengthen planning and recovery.

- [GUI-R1: A Generalist R1-Style Vision-Language Action Model for GUI Agents](https://arxiv.org/abs/2504.10458)
    - Run Luo, Lu Wang, Wanwei He, Longze Chen, Jiaming Li, Min Yang, Xiaobo Xia
    - 🏛️ Institutions: Shenzhen Institute of Advanced Technology, CAS, University of Chinese Academy of Sciences, NUS
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [reinforcement learning], [unified action space], [GRPO], [data efficiency], [GUI-R1]
    - 📖 TLDR: GUI-R1 applies R1-style reinforcement learning to GUI action modeling by training a vision-language agent with unified action-space rules across Windows, Linux, macOS, Android, and Web. Using only a small curated cross-platform dataset, it reports stronger performance than prior methods across eight benchmarks and highlights RL's data-efficiency benefits for GUI agents.

- [UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Han Xiao, Shuai Ren, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, CUHK
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [reinforcement learning], [rule-based action reward], [GRPO], [UI-R1-3B], [AndroidControl], [ScreenSpot-pro]
    - 📖 TLDR: UI-R1 studies whether rule-based reinforcement learning can improve efficient GUI action prediction for multimodal mobile agents. It trains UI-R1-3B with GRPO on a curated set of 136 challenging mobile tasks using a rule-based action reward, and reports gains on ScreenSpot, ScreenSpot-Pro, and AndroidControl over the base model.

- [Advancing Autonomous VLM Agents via Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Liverpool, University of Southampton, Huawei Noah's Ark Lab, Tianjin University, UCL
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [reinforcement learning], [subgoal-conditioned RL], [SGC-ELBO], [learning efficiency], [VSC-RL]
    - 📖 TLDR: This paper reformulates long-horizon VLM-agent training as a variational subgoal-conditioned reinforcement learning problem with the SGC-ELBO objective. Across mobile-device and web-control benchmarks, VSC-RL improves both learning efficiency and final performance over prior RL methods.

- [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://proceedings.mlr.press/v267/zhou25ah.html)
    - Yifei Zhou, Qianlan Yang, Kaixiang Lin, Min Bai, Xiong Zhou, Yu-Xiong Wang, Sergey Levine, Li Erran Li
    - 🏛️ Institutions: UC Berkeley, UIUC, Amazon
    - 📅 Date: December 17, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [skill discovery], [autonomous task proposal], [VLM-based success evaluator], [PAE]
    - 📖 TLDR: PAE is a web-agent learning system that lets foundation-model agents autonomously propose tasks, attempt them, and score the resulting trajectories with a VLM-based evaluator. By turning those evaluations into RL signals, it improves zero-shot generalization on unseen websites and tasks for vision-based internet agents.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://openreview.net/forum?id=oVKEAFjEqv)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Jiadai Sun, Xinyue Yang, Yu Yang, Shuntian Yao, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua, Zhipu
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Web]
    - 🔑 Key: [reinforcement learning], [self-evolving curriculum], [outcome-supervised reward model], [online learning], [WebRL]
    - 📖 TLDR: WebRL trains open web agents with online reinforcement learning rather than static supervised data, combining self-evolving task generation, an outcome-supervised reward model, and adaptive policy updates. It substantially improves Llama-3.1-based and GLM-4-based agents on WebArena-Lite and narrows the gap to proprietary systems.

- [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html)
    - Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, Aviral Kumar
    - 🏛️ Institutions: UC Berkeley, UIUC, CMU, Google DeepMind
    - 📅 Date: June 14, 2024
    - 📑 Publisher: NeurIPS 2024 Main Conference Track
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [offline-to-online RL], [AITW], [automatic curriculum], [DigiRL]
    - 📖 TLDR: DigiRL trains mobile device-control agents with a two-stage reinforcement learning pipeline that starts from offline RL and continues with offline-to-online RL on real Android interactions. It pairs that training loop with a scalable Android learning environment and a VLM-based evaluator, and reports a large gain over supervised fine-tuning on AitW.

- [Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2405.00516)
    - Lucas-Andreï Thil, Mirela Popa, Gerasimos Spanakis
    - 🏛️ Institutions: Maastricht University
    - 📅 Date: May 01, 2024
    - 📑 Publisher: SAC 2024
    - 💻 Env: [Web]
    - 🔑 Key: [MiniWoB], [supervised learning], [reinforcement learning], [HTML understanding], [WebAI]
    - 📖 TLDR: Navigating WebAI studies web-task completion on MiniWoB with a training recipe that combines supervised learning and reinforcement learning. It also diagnoses that prior models often memorize shallow HTML cues instead of understanding structure, and reports stronger supervised baselines with less data while narrowing the gap to RL approaches.

- [Grounded Language Agent for Product Search via Intelligent Web Interactions](https://arxiv.org/abs/2404.10887)
    - Moghis Fereidouni, Adib Mosharrof, A.B. Siddique
    - 🏛️ Institutions: University of Kentucky
    - 📅 Date: April 16, 2024
    - 📑 Publisher: CustomNLP4U @ NAACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [GLAINTEL], [product search], [reinforcement learning], [Flan-T5], [unsupervised domain adaptation]
    - 📖 TLDR: GLAINTEL is a grounded language agent for product-search interactions on the web built on top of Flan-T5 with a language-modeling head and value head. It studies unsupervised training, supervised training, and unsupervised domain adaptation, and finds that combining human demonstrations with reinforcement learning works better than straightforward behavior cloning alone.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://dl.acm.org/doi/10.1145/3637528.3671620)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua, Zhipu, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences
    - 📅 Date: April 04, 2024
    - 📑 Publisher: KDD 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [AutoWebBench], [HTML simplification], [curriculum training], [reinforcement learning]
    - 📖 TLDR: AutoWebGLM is a web-navigation agent built on ChatGLM3-6B that combines HTML simplification, hybrid human-AI trajectory construction, and reinforcement learning with rejection sampling. The paper also introduces the bilingual AutoWebBench benchmark for real-world web navigation and uses it together with other benchmarks to evaluate the system.

- [A Data-Driven Approach for Learning to Control Computers](https://proceedings.mlr.press/v162/humphreys22a.html)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - 🏛️ Institutions: Google DeepMind
    - 📅 Date: February 16, 2022
    - 📑 Publisher: ICML 2022
    - 💻 Env: [Desktop]
    - 🔑 Key: [computer control], [behavioral cloning], [reinforcement learning], [demonstration data], [MiniWoB++]
    - 📖 TLDR: Studies computer control as a data-driven learning problem using natural-language goals plus low-level mouse and keyboard actions. The work combines human demonstrations with RL-style training and shows strong cross-task generalization on desktop-style control tasks.

- [AndroidEnv: A Reinforcement Learning Platform for Android](https://arxiv.org/abs/2105.13231)
    - Daniel Toyama, Philippe Hamel, Anita Gergely, Gheorghe Comanici, Amelia Glaese, Zafarali Ahmed, Tyler Jackson, Shibl Mourad, Doina Precup
    - 🏛️ Institutions: Google DeepMind
    - 📅 Date: May 27, 2021
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [environment], [reinforcement learning], [AndroidEnv], [touchscreen interface], [Android platform]
    - 📖 TLDR: AndroidEnv is an open-source research platform that exposes Android apps through a realistic touchscreen interaction loop for reinforcement learning. The paper frames Android device use as a unified environment family rather than a single fixed benchmark task.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://openreview.net/forum?id=ryTp3f-0-)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Stanford
    - 📅 Date: February 24, 2018
    - 📑 Publisher: ICLR 2018 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [workflow-guided exploration], [MiniWoB]
    - 📖 TLDR: This paper introduces workflow-guided exploration, where demonstrations are converted into high-level workflows that constrain web-agent exploration during RL. It shows that this makes sparse-reward web interaction much more sample-efficient than pure behavioral cloning on World of Bits style tasks.

- [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html)
    - Tianlin Shi, Andrej Karpathy, Linxi Fan, Jonathan Hernandez, Percy Liang
    - 🏛️ Institutions: Stanford, OpenAI
    - 📅 Date: August 31, 2017
    - 📑 Publisher: ICML 2017
    - 💻 Env: [Web]
    - 🔑 Key: [environment], [reinforcement learning], [World of Bits], [MiniWoB], [QAWoB]
    - 📖 TLDR: World of Bits is an open-domain web environment where agents observe rendered webpages and DOM structure, then act with low-level keyboard and mouse commands. The paper also defines a methodology for building reproducible web tasks from real websites, including MiniWoB and QAWoB.
