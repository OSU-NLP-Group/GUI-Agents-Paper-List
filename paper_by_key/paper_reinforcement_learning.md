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
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory, CUHK MMLab, The Hong Kong University of Science and Technology, National University of Singapore
    - 📅 Date: March 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [reinforcement learning], [critic framework], [OmniGUIRewardBench], [milestone decomposition], [OS-Themis]
    - 📖 TLDR: OS-Themis is a scalable critic framework for GUI reward modeling that breaks trajectories into verifiable milestones and audits the evidence chain before issuing a verdict. It improves AndroidWorld training and filtering loops and introduces OmniGUIRewardBench as a cross-platform benchmark for GUI outcome rewards.

- [Generalization in Online Reinforcement Learning for Mobile Agents](https://arxiv.org/abs/2603.07432)
    - Li Gu, Zihuan Jiang, Zhixiang Chi, Huan Liu, Ziqiang Wang, Yuanhao Yu, Glen Berseth, Yang Wang
    - 🏛️ Institutions: Mila - Quebec AI Institute, Concordia University, Universite de Montreal, CIFAR AI Chair, University of Toronto, McMaster University
    - 📅 Date: March 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [benchmark], [generalization], [AndroidWorld-Generalization], [GRPO], [test-time adaptation]
    - 📖 TLDR: This paper studies generalization in online RL for mobile agents, introducing AndroidWorld-Generalization to measure transfer to unseen instances, templates, and applications. Its open RL training system shows gains over supervised fine-tuning on unseen instances, but also highlights that unseen templates and apps remain much harder without additional adaptation.

- [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)
    - Sicheng Fan, Qingyun Shi, Shengze Xu, Shengbo Cai, Tieyong Zeng, Li Ling, Yanyi Shang, Dehan Kong
    - 🏛️ Institutions: Fudan University, IMean AI, The Chinese University of Hong Kong, Tsinghua University
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [reinforcement learning], [synthetic data], [environment synthesis], [task generation], [embodiment potential], [WebFactory]
    - 📖 TLDR: WebFactory presents a closed-loop training pipeline that compresses LLM latent internet knowledge into grounded web-agent behavior through synthetic environment generation, task generation, trajectory collection, and decomposed-reward RL. It matches agents trained on comparable amounts of human data while using synthetic data from only 10 websites.

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
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, Nanjing University, Ovis Team, Alibaba Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [agentic-Q estimation], [step-wise policy optimization], [Ovis2.5-9B], [GUI navigation], [grounding]
    - 📖 TLDR: This paper trains GUI agents with an agentic-Q model that estimates each action's contribution to task completion and a step-wise policy optimization routine decoupled from online interaction. The design keeps data collection manageable while stabilizing updates and improving navigation and grounding performance.

- [Adaptive Milestone Reward for GUI Agents](https://arxiv.org/abs/2602.11524)
    - Congmin Zheng, Xiaoyun Mo, Xinbei Ma, Qiqiang Lin, Yin Zhao, Jiachen Zhu, Xingyu Lou, Jun Wang, Zhaoxiang Wang, Weiwen Liu, Zhuosheng Zhang, Yong Yu, Weinan Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, OPPO Research Institute
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [reward shaping], [credit assignment], [milestone reward], [ADMIRE], [AndroidWorld]
    - 📖 TLDR: ADMIRE is a reinforcement-learning reward design for GUI agents that distills adaptive, verifiable milestones from successful trajectories and pairs them with asymmetric credit assignment. It improves AndroidWorld performance by more than 10 absolute points and transfers to other RL algorithms and environments.

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL], [curriculum learning]
    - 📖 TLDR: ACuRL studies continual adaptation for computer-use agents in changing environments without human demonstrations. It combines autonomous curriculum generation with CUAJudge-based evaluation to improve both within-environment and cross-environment adaptation while limiting forgetting.

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: Multimedia Laboratory (MMLab), The Chinese University of Hong Kong, vivo AI Lab, Princeton University, Shenzhen Loop Area Institute, Shanghai AI Lab
    - 📅 Date: February 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [memory], [reinforcement learning], [online RL], [hierarchical experience memory], [stratified group sampling], [UI-Mem]
    - 📖 TLDR: UI-Mem augments online RL for mobile GUI agents with a hierarchical experience memory that stores reusable workflows, subtask skills, and failure patterns as transferable templates. Its stratified group sampling lets the policy absorb memory-informed behavior and improves over standard online RL baselines.

- [SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization](https://arxiv.org/abs/2601.22491)
    - Jinyang Wu, Changpeng Yang, Yuhao Shen, Fangzhi Xu, Bolin Ni, Chonghua Liao, Yuchen Liu, Hongzhen Wang, Shuai Nie, Shuai Zhang, Haoran Luo, Jiaming Xu
    - 🏛️ Institutions: Tsinghua University, Xiaomi Corporation, Zhejiang University, Nanyang Technological University, Institute of Automation, Chinese Academy of Sciences
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [tiered rewards], [reward shaping], [GUI grounding], [planning], [SSL]
    - 📖 TLDR: SSL replaces binary verifier rewards with progressively amplified tiered rewards that distinguish higher- and lower-quality successful trajectories. Across GUI perception, short- and long-horizon planning, and reasoning benchmarks, it improves optimization stability and reaches up to 2.5x better sample efficiency than binary-reward baselines.

- [GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents](https://arxiv.org/abs/2601.09770)
    - Chen Chen, Jiawei Shao, Dakuan Lu, Haoyi Hu, Xiangcheng Liu, Hantao Yao, Wu Liu
    - 🏛️ Institutions: University of Science and Technology of China, Institute of Artificial Intelligence (TeleAI), China Telecom, Shanghai Innovation Institute, Shanghai Jiao Tong University
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [active perception], [tool-augmented perception], [ScreenSpot-pro], [GUI-Eyes]
    - 📖 TLDR: GUI-Eyes frames GUI grounding as active perception, letting the agent learn when and how to call tools such as cropping and zooming inside a two-stage reasoning process. It pairs that policy with a spatially continuous reward for tool use and reaches 44.8% grounding accuracy on ScreenSpot-Pro using only 3k labeled samples.

- [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/abs/2601.05787)
    - Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu
    - 🏛️ Institutions: Nanjing University, Peking University, Microsoft Research Asia
    - 📅 Date: January 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [RLVR], [off-policy assimilation], [BEPA], [OSWorld]
    - 📖 TLDR: BEPA improves end-to-end GUI-agent training with verifiable rewards by turning scarce off-policy expert traces into policy-aligned guidance through self-rolled reachable trajectories and a dynamically updated per-task cache. On OSWorld-Verified it raises UI-TARS-1.5-7B from 22.87% to 32.13%, with additional gains on MMBench-GUI and Online-Mind2Web.

- [WebGym: Scaling Training Environments for Visual Web Agents with Realistic Tasks](https://arxiv.org/abs/2601.02439)
    - Hao Bai, Alexey Taymanov, Tong Zhang, Aviral Kumar, Spencer Whitehead
    - 🏛️ Institutions: Microsoft, University of Illinois Urbana-Champaign, Carnegie Mellon University
    - 📅 Date: January 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [training environment], [reinforcement learning], [asynchronous rollouts], [WebGym]
    - 📖 TLDR: WebGym provides a large-scale open training environment for visual web agents with nearly 300,000 rubric-evaluated tasks on realistic websites. It also includes a high-throughput asynchronous rollout system, and agents fine-tuned on WebGym improve from 26.2% to 42.9% on out-of-distribution websites, outperforming GPT-4o and GPT-5-Thinking.

- [SmartSnap: Proactive Evidence Seeking for Self-Verifying Agents](https://arxiv.org/abs/2512.22322)
    - Shaofei Cai, Yulei Qin, Haojia Lin, Zihan Xu, Gang Li, Yuchen Shi, Zongyi Li, Yong Mao, Siqi Cai, Xiaoyu Tan, Yitao Liang, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, Institute for Artificial Intelligence, Peking University
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [self-verification], [evidence seeking], [LLM-as-a-judge], [AndroidLab]
    - 📖 TLDR: SmartSnap turns task verification from a passive post-hoc check into proactive evidence seeking, training mobile GUI agents to collect a minimal set of decisive snapshots under the 3C principles so an LLM judge can verify success more reliably, yielding large gains on AndroidLab across 8B and 30B agents.

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

- [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235)
    - Zehao Deng, Tianjie Ju, Zheng Wu, Zhuosheng Zhang, Gongshen Liu
    - 🏛️ Institutions: Soochow University, Shanghai Jiao Tong University
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

- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
    - Zhangxuan Gu, Zhengwen Zeng, Zhenyu Xu, Xingran Zhou, Shuheng Shen, Yunfei Liu, Beitong Zhou, Changhua Meng, Tianyu Xia, Weizhi Chen, Yue Wen, Jingya Dou, Fei Tang, Jinzhen Lin, Yulin Liu, Zhenlin Guo, Yichen Gong, Heng Jia, Changlong Gao, Yuan Guo, Yong Deng, Zhenyu Guo, Liang Chen, Weiqiang Wang
    - 🏛️ Institutions: Ant Group
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [reinforcement learning], [grounding], [navigation], [data cleaning], [Qwen2.5-VL], [UI-venus]
    - 📖 TLDR: This technical report introduces **UI-Venus**, a screenshot-based UI agent built on the multimodal Qwen2.5-VL model and fine-tuned via **reinforcement fine-tuning (RFT)**. It achieves state-of-the-art performance on UI grounding and navigation benchmarks—e.g., Screenspot-V2/Pro (up to 95.3% / 61.9%) and AndroidWorld navigation (up to 65.9%)—by leveraging carefully crafted reward functions, efficient data cleaning pipelines, and a novel **self-evolving framework** (trajectory alignment and sparse action enhancement) to enhance reasoning coherence and handle rare actions. The code and checkpoints are open-sourced to encourage further development.

- [Test‑Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615)
    - Yong Du, Yuchen Yan, Fei Tang, Zhengxi Lu, Chang Zong, Weiming Lu, Shengpei Jiang, Yongliang Shen
    - 🏛️ Institutions: Zhejiang University, Central South University, Zhejiang University of Science and Technology, SF Technology
    - 📅 Date: August 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [test-time scaling], [reinforcement learning], [self‑supervised], [GUI‑RC], [GUI‑RCPO], [benchmark], [region consistency], [GUI grounding]
    - 📖 TLDR: This paper introduces **GUI‑RC (Region Consistency)**, a test-time method that aggregates multiple model predictions via spatial voting to derive a consensus region—achieving 2–3% accuracy improvements on ScreenSpot benchmarks without any additional training. It extends this idea with **GUI‑RCPO (Region Consistency Policy Optimization)**, which turns region-consistency patterns into self-supervised rewards for reinforcement learning at inference time, refining model predictions on unlabeled data and yielding further improvements (e.g., from 83.57% to 85.14% on ScreenSpot‑v2). The approach demonstrates a novel and effective use of test-time optimization for more robust, data-efficient GUI grounding.

- [GuirlVG: Incentivize GUI Visual Grounding via Empirical Exploration on Reinforcement Learning](https://arxiv.org/abs/2508.04389)
    - Weitai Kang, Bin Lei, Gaowen Liu, Caiwen Ding, Yan Yan
    - 🏛️ Institutions: University of Illinois Chicago, University of Minnesota, Cisco Research
    - 📅 Date: August 06, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [GUI grounding], [reinforcement learning], [reinforcement fine-tuning], [ScreenSpot], [GuirlVG]
    - 📖 TLDR: This paper studies reinforcement fine-tuning for GUI visual grounding and argues that naive rule-based RL underperforms strong supervised baselines without careful formulation. It introduces GuirlVG, which systematically redesigns the reward, training setup, and stabilization mechanism, including an Adversarial KL Factor to reduce reward over-optimization. With only 5.2K training samples, the method surpasses prior GUI grounding approaches trained on much larger datasets across ScreenSpot, ScreenSpot-Pro, and ScreenSpot-V2.

- [Evolving in Tasks: Empowering the Multi-modality Large Language Model as the Computer Use Agent](https://arxiv.org/abs/2508.04037)
    - Yuhao Cheng, Liang Tang, Shuxian Li, Yukang Huo, Tiaonan Duan, Kaer Huang, Yanzhe Jing, Yiqiang Yan
    - 🏛️ Institutions: Lenovo, College of Information and Electrical Engineering, China Agricultural University
    - 📅 Date: August 06, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [self-evolving], [reinforcement learning], [data generation], [framework]
    - 📖 TLDR: Proposes the Self-Evolution Agent (SEA) for computer operation with three core innovations: an automatic verifiable trajectory generation pipeline, multi-turn RL-based policy optimization, and continual model enhancement to iteratively improve performance on diverse computer-use tasks.

- [NaviMaster: Learning a Unified Policy for GUI and Embodied Navigation Tasks](https://arxiv.org/abs/2508.02046)
    - Zhihao Luo, Wentao Yan, Jingyu Gong, Min Wang, Zhizhong Zhang, Xuhong Wang, Yuan Xie, Xin Tan
    - 🏛️ Institutions: East China Normal University, Shanghai AI Laboratory, SenseTime Research
    - 📅 Date: August 04, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI navigation], [embodied navigation], [reinforcement learning], [unified agent]
    - 📖 TLDR: NaviMaster is the first unified agent that combines GUI navigation (mobile/web/desktop) and embodied navigation within a single reinforcement learning framework, using a visual-target trajectory collection pipeline and distance-aware reward to outperform state-of-the-art agents on out-of-domain benchmarks across both domains.

- [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976)
    - Junhong Shen, Hao Bai, Lunjun Zhang, Yifei Zhou, Amrith Setlur, Shengbang Tong, Diego Caples, Nan Jiang, Tong Zhang, Ameet Talwalkar, Aviral Kumar
    - 🏛️ Institutions: Carnegie Mellon University, Scribe, University of Illinois Urbana-Champaign, University of Toronto, University of California, Berkeley, The AGI Company, New York University
    - 📅 Date: June 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [test-time scaling], [exploration], [planning], [reinforcement learning]
    - 📖 TLDR: Proposes test-time interaction scaling—increasing agent interaction horizons rather than reasoning trace length—showing that richer behaviors including exploration, backtracking, and dynamic adaptation from more interactions outperform extended pre-action thinking for GUI-based computer tasks.

- [ZeroGUI: Automating Online GUI Learning at Zero Human Cost](https://arxiv.org/abs/2505.23762)
    - Chenyu Yang, Shiqian Su, Shi Liu, Xuan Dong, Yue Yu, Weijie Su, Xuehui Wang, Zhaoyang Liu, Jinguo Zhu, Hao Li, Wenhai Wang, Yu Qiao, Xizhou Zhu, Jifeng Dai
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, Tsinghua University, Shanghai Jiao Tong University, Hong Kong University of Science and Technology, The Chinese University of Hong Kong
    - 📅 Date: May 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [model-free], [VLM-task-generation], [VLM-reward-estimation], [ZeroGUI]
    - 📖 TLDR: Introduces **ZeroGUI**, a novel online learning framework that enables GUI agents (based on VLMs) to learn by autonomous interaction without human labels. It uses vision-language models to (i) generate diverse task instructions, (ii) evaluate task success, and (iii) apply a two-stage RL strategy (task-generated training + test-time adaptation). The method shows strong performance gains (e.g., +14% on UI-TARS, +63% on Aguvis) in desktop (OSWorld) and mobile (AndroidLab) GUI benchmarks, proving scalable, human-free GUI-agent training.

- [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)
    - Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: May 28, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [information seeking], [reinforcement learning], [GAIA], [WebDancer]
    - 📖 TLDR: This paper presents WebDancer, an end-to-end web agent for autonomous information seeking built through a data-centric four-stage training pipeline: browsing data construction, trajectory sampling, supervised fine-tuning, and reinforcement learning. It targets long-horizon information-seeking problems rather than short templated web tasks. The resulting system achieves strong performance on GAIA and WebWalkerQA and offers a concrete recipe for training more capable research-style web agents.

- [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660)
    - Qinzhuo Wu, Pengzhi Gao, Wei Liu, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: May 27, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [error detection], [backtracking], [Mobile3M], [Auto‑UI]
    - 📖 TLDR: BacktrackAgent introduces a novel GUI‑agent framework that embeds four components—generator, verifier, judger, and reflector—to detect when actions go wrong, evaluate their effects, and backtrack to recover. It also constructs specialized datasets for training these “judgment” and “reflection” modules. On Mobile3M and Auto‑UI benchmarks, it boosts task success rate by ~7.6% and step accuracy by ~1.6%, outperforming prior SOTA like MobileVLM and ReachAgent.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, School of Computer Science, MoE Key Lab of Artificial Intelligence, SJTU AI Institute, Shanghai Jiao Tong University, Jiangsu Key Lab of Language Computing, Suzhou Laboratory
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [reward model], [progress reward], [LCS], [ProgRM]
    - 📖 TLDR: Introduces **ProgRM**, a novel framework giving dense intermediate rewards to GUI agents by estimating per‑step task progress. Labels are generated through an LCS‑based self‑annotation algorithm that identifies key steps in successful trajectories. Agents trained with ProgRM outperform outcome‑based reward models and proprietary LLMs like Claude‑3.7‑Sonnet across benchmarks.

- [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2505.16421)
    - Zhepei Wei, Wenlin Yao, Yao Liu, Weizhi Zhang, Qin Lu, Liang Qiu, Changlong Yu, Puyang Xu, Chao Zhang, Bing Yin, Hyokun Yun, Lihong Li
    - 🏛️ Institutions: University of Virginia, Amazon, Georgia Institute of Technology
    - 📅 Date: May 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [reinforcement learning], [multi-turn interaction], [WebArena], [chain-of-thought], [test-time scaling]
    - 📖 TLDR: WebAgent-R1 is an end-to-end multi-turn reinforcement learning framework for training web agents that learns from online interactions with web environments using binary task-success rewards, boosting Llama-3.1-8B's success rate on WebArena-Lite from 8.5% to 44.8% and surpassing proprietary models like OpenAI o3.

- [ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282)
    - Fanbin Lu, Zhisheng Zhong, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: The Chinese University of Hong Kong, SmartMore, Hong Kong University of Science and Technology
    - 📅 Date: May 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [policy optimization], [training], [multi-turn]
    - 📖 TLDR: ARPO (End-to-End Policy Optimization for GUI Agents with Experience Replay) addresses multi-turn RL for VLM-based GUI agents through experience replay to mitigate sparse rewards, delayed feedback, and high rollout costs, enabling efficient optimization of long-horizon GUI action sequences.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Gaoling School of Artificial Intelligence, Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [GUI grounding], [visual grounding], [reinforcement learning], [ScreenSpot], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications
    - 📅 Date: May 18, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [GUI-shift]
    - 📖 TLDR: Learns GUI dynamics from unlabeled trajectories through a self-supervised inverse-dynamics task called K-step GUI Transition, avoiding dependence on natural-language annotations. Built on top of that task, GUI-Shift combines rule-based optimization with data filtering and improves both GUI automation and grounding across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro.

- [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: VCIP, School of Computer Science, NKU, vivo Mobile Communication Co., Ltd, National University of Singapore, Fudan University, East China University of Science and Technology
    - 📅 Date: May 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [visual grounding], [ScreenSpot-pro], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [A Survey on GUI Agents with Foundation Models Enhanced by Reinforcement Learning](https://arxiv.org/abs/2504.20464)
    - Jiahao Li, Kaer Huang
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: April 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [reinforcement learning], [multimodal], [training taxonomy], [MDP formulation]
    - 📖 TLDR: Surveys GUI agents through the lens of reinforcement learning, framing GUI interaction as an MDP and organizing the field around perception, planning, and acting modules. Its main value is a training-oriented taxonomy that connects prompting, supervised fine-tuning, and RL-style policy optimization.

- [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)
    - Yuhang Liu, Pengxiang Li, Congkai Xie, Xavier Hu, Xiaotian Han, Shengyu Zhang, Hongxia Yang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Dalian University of Technology, Reallm Labs, The Hong Kong Polytechnic University
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [planning], [reasoning], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: Presents InfiGUI-R1 as a GUI agent designed to move from reactive action prediction toward explicit deliberative reasoning. The Actor2Reasoner pipeline first injects spatial reasoning and then strengthens planning and recovery through RL with sub-goal guidance and error-recovery scenarios.

- [GUI-R1: A Generalist R1-Style Vision-Language Action Model for GUI Agents](https://arxiv.org/abs/2504.10458)
    - Run Luo, Lu Wang, Wanwei He, Longze Chen, Jiaming Li, Min Yang, Xiaobo Xia
    - 🏛️ Institutions: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences, National University of Singapore
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [reinforcement learning], [unified action space], [GRPO], [data efficiency], [GUI-R1]
    - 📖 TLDR: GUI-R1 is an R1-style reinforcement learning framework for GUI agents that trains vision-language action models with a unified action space and rule-based rewards across Windows, Linux, macOS, Android, and Web. Using only a small curated dataset, it achieves stronger results than prior methods across eight benchmarks, showing that RL can substantially improve data efficiency for GUI-agent training.

- [UI-R1: Enhancing Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, The Chinese University of Hong Kong
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [UI-R1-3B], [GRPO], [AndroidControl], [ScreenSpot-pro]
    - 📖 TLDR: Explores whether R1-style rule-based reinforcement learning can improve multimodal GUI action prediction with very little data. UI-R1 uses a unified action reward and only 136 high-quality mobile tasks to train UI-R1-3B with GRPO, yielding large gains on AndroidControl, ScreenSpot, and ScreenSpot-Pro relative to the base model.

- [Advancing Autonomous VLM Agents via Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, University College London
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [VLM agent], [subgoal-conditioned RL], [learning efficiency], [VSC-RL]
    - 📖 TLDR: This paper reformulates long-horizon VLM-agent training as a variational subgoal-conditioned reinforcement learning problem, introducing the SGC-ELBO objective to balance subgoal-conditioned return maximization against divergence from a reference policy. Across mobile and web control benchmarks, VSC-RL improves both learning efficiency and final performance over prior RL methods.

- [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://proceedings.mlr.press/v267/zhou25ah.html)
    - Yifei Zhou, Qianlan Yang, Kaixiang Lin, Min Bai, Xiong Zhou, Yu-Xiong Wang, Sergey Levine, Li Erran Li
    - 🏛️ Institutions: University of California, Berkeley, University of Illinois Urbana-Champaign, Amazon
    - 📅 Date: December 17, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [skill discovery], [PAE]
    - 📖 TLDR: This paper introduces the Proposer-Agent-Evaluator (PAE) system, enabling foundation model agents to autonomously discover and practice skills in real-world web environments. PAE comprises a context-aware task proposer, an agent policy for task execution, and a vision-language model-based success evaluator. Validated on vision-based web navigation tasks, PAE significantly enhances zero-shot generalization capabilities of vision-language model Internet agents, achieving over 30% relative improvement on unseen tasks and websites, and surpassing state-of-the-art open-source agents by more than 10%.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://openreview.net/forum?id=oVKEAFjEqv)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Jiadai Sun, Xinyue Yang, Yu Yang, Shuntian Yao, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Shanghai Qi Zhi Institute
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [self-evolving curriculum], [WebRL], [outcome-supervised reward model]
    - 📖 TLDR: Introduces WebRL, an online reinforcement learning framework for training open web agents through self-evolving task generation, outcome-supervised rewards, and adaptive policy optimization. Applied to Llama-3.1 and GLM-4 style models, it substantially improves web-agent performance and narrows the gap with proprietary systems.

- [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b9e472cd579c83e2f6aa3459f46aac28-Abstract-Conference.html)
    - Taiyi Wang, Zhihao Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Huawei Noah's Ark Lab, University College London
    - 📅 Date: October 18, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [distributed training], [a-RIDE], [on-device control]
    - 📖 TLDR: This paper introduces **DistRL**, a novel framework designed to enhance the efficiency of online reinforcement learning fine-tuning for mobile device control agents. DistRL employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in dynamic online interactions. The framework is supported by a custom RL algorithm, A-RIDE, which balances exploration with prioritized data utilization to ensure stable and robust training. Experiments demonstrate that DistRL improves training efficiency by 3× and accelerates data collection by 2.4× compared to leading synchronous multi-machine methods. Notably, after training, DistRL achieves a 20% relative improvement in success rate on general Android tasks from an open benchmark, outperforming existing approaches while maintaining the same training time.

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
    - 🔑 Key: [framework], [MCTS], [DPO], [reinforcement learning], [WebShop], [Agent Q]
    - 📖 TLDR: Agent Q combines guided MCTS, self-critique, and off-policy DPO to train web agents from both successful and failed trajectories. It substantially improves LLM agent performance on WebShop and real-world booking tasks, especially when paired with online search.

- [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html)
    - Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, Aviral Kumar
    - 🏛️ Institutions: University of California, Berkeley, University of Illinois Urbana-Champaign, Carnegie Mellon University, Google DeepMind
    - 📅 Date: June 14, 2024
    - 📑 Publisher: NeurIPS 2024 Main Conference Track
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [Android in the Wild], [AITW], [DigiRL]
    - 📖 TLDR: Presents DigiRL, an autonomous reinforcement learning approach for training in-the-wild device-control agents with offline and offline-to-online RL stages. The method uses a scalable Android learning environment, automatic curriculum design, and a VLM-based evaluator to improve device-control performance.

- [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/01a83bc2f2732a58e6aa731e659e7101-Abstract-Conference.html)
    - Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William E Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Kenji Toyama, Robert James Berry, Divya Tyamagundlu, Timothy P Lillicrap, Oriana Riva
    - 🏛️ Institutions: Google DeepMind, Google
    - 📅 Date: May 23, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [Android-based agents], [task diversity], [reinforcement learning], [dynamic environment]
    - 📖 TLDR: AndroidWorld introduces a dynamic Android environment for benchmarking autonomous agents across 116 tasks spanning 20 Android apps. These tasks vary through parameterized and natural language prompts, fostering a realistic testing ground for agents designed to operate in complex mobile environments. The benchmark supports millions of task variations, allowing agents to respond to the Android system's changing states and improving real-world applicability.

- [Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2405.00516)
    - Lucas-Andreï Thil, Mirela Popa, Gerasimos Spanakis
    - 🏛️ Institutions: Maastricht University the Netherlands
    - 📅 Date: May 01, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [MiniWoB], [supervised learning], [reinforcement learning], [HTML understanding]
    - 📖 TLDR: Combines supervised learning and reinforcement learning for web navigation on MiniWoB while explicitly targeting shallow HTML memorization. The paper shows stronger supervised baselines with less data and narrows the gap to RL-based web agents by improving structural understanding of HTML content.

- [Grounded Language Agent for Product Search via Intelligent Web Interactions](https://arxiv.org/abs/2404.10887)
    - Moghis Fereidouni, Adib Mosharrof, A.B. Siddique
    - 🏛️ Institutions: University of Kentucky
    - 📅 Date: April 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [GLAINTEL], [Flan-T5], [unsupervised domain adaptation]
    - 📖 TLDR: This paper introduces GLAINTEL, a grounded language agent framework designed to enhance web interaction using instruction-finetuned language models, particularly Flan-T5, with reinforcement learning (PPO) to tackle interactive web navigation challenges. The study explores unsupervised and supervised training methods, evaluating the effects of human demonstration on agent performance. Results indicate that combining human feedback with reinforcement learning yields effective outcomes, rivaling larger models like GPT-4 on web navigation tasks.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://dl.acm.org/doi/10.1145/3637528.3671620)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences
    - 📅 Date: April 04, 2024
    - 📑 Publisher: KDD 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [AutoWebBench], [ChatGLM3-6B]
    - 📖 TLDR: AutoWebGLM introduces a web navigation agent based on ChatGLM3-6B, designed to autonomously navigate and interact with webpages for complex tasks. The paper highlights a two-phase data construction approach using a hybrid human-AI methodology for diverse, curriculum-based web task training. It also presents AutoWebBench, a benchmark for evaluating agent performance in web tasks, and uses reinforcement learning to fine-tune operations, addressing complex webpage interaction and grounding.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia
    - 📅 Date: October 07, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [instruction grounding], [pixel-to-sequence], [reinforcement learning], [RUIG]
    - 📖 TLDR: Presents RUIG, a metadata-free grounding model that maps natural-language instructions to coordinates on UI screenshots using a pixel-to-sequence decoder. The main contribution is an RL-style training objective that strengthens spatial decoding quality, positioning RUIG as a generic UI-grounding API rather than a full agent stack.

- [A Data-Driven Approach for Learning to Control Computers](https://proceedings.mlr.press/v162/humphreys22a.html)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - 🏛️ Institutions: DeepMind
    - 📅 Date: February 16, 2022
    - 📑 Publisher: ICML 2022
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [computer control], [behavioral cloning], [reinforcement learning], [demonstration data]
    - 📖 TLDR: Studies computer control as a data-driven learning problem using natural-language goals plus low-level mouse and keyboard actions. The work combines human demonstrations with RL-style training and shows strong cross-task generalization on desktop-style control tasks.

- [AndroidEnv: A Reinforcement Learning Platform for Android](https://arxiv.org/abs/2105.13231)
    - Daniel Toyama, Philippe Hamel, Anita Gergely, Gheorghe Comanici, Amelia Glaese, Zafarali Ahmed, Tyler Jackson, Shibl Mourad, Doina Precup
    - 🏛️ Institutions: DeepMind
    - 📅 Date: May 27, 2021
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [environment], [reinforcement learning], [AndroidEnv], [touchscreen control], [Android tasks]
    - 📖 TLDR: Introduces AndroidEnv, an open-source RL platform that lets agents interact with realistic Android apps and services through a universal touchscreen interface. Its main contribution is to make Android device control a reusable research environment rather than a single benchmark task.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://openreview.net/forum?id=ryTp3f-0-)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Stanford University
    - 📅 Date: February 24, 2018
    - 📑 Publisher: ICLR 2018 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [workflow-guided exploration], [MiniWoB]
    - 📖 TLDR: Introduces workflow-guided exploration, an RL training strategy that constrains web-agent exploration with abstract workflows extracted from demonstrations. The paper is an early milestone showing how to make sparse-reward web interaction tractable on MiniWoB-style tasks.

- [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html)
    - Tianlin Shi, Andrej Karpathy, Linxi Fan, Jonathan Hernandez, Percy Liang
    - 🏛️ Institutions: Stanford University, OpenAI
    - 📅 Date: August 31, 2017
    - 📑 Publisher: ICML 2017
    - 💻 Env: [Web]
    - 🔑 Key: [environment], [reinforcement learning], [World of Bits], [MiniWoB], [QAWoB]
    - 📖 TLDR: Introduces World of Bits, an open-domain web environment where agents interact with live or cached websites through keyboard and mouse actions. The paper contributes both the platform and a task-construction methodology, including MiniWoB and QAWoB, to make web-based RL tasks diverse yet reproducible.
