- [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235)
    - Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, LawZero, Mila - Quebec AI Institute, Universite de Montreal, University of California, Berkeley
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [safety], [red teaming], [unintended behavior], [computer-use agent], [AutoElicit]
    - 📖 TLDR: This paper studies unsafe unintended behaviors in computer-use agents under benign user inputs rather than adversarial prompts. It introduces AutoElicit, an agentic framework that iteratively perturbs realistic benign instructions using execution feedback to surface severe harmful behaviors in frontier CUAs. The results show that even strong CUAs remain broadly susceptible to harmful deviations, establishing a concrete framework for systematically probing unintended safety failures in realistic computer-use settings.

- [GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding](https://arxiv.org/abs/2510.04039)
    - Bin Lei, Nuo Xu, Ali Payani, Mingyi Hong, Chunhua Liao, Yu Cao, Caiwen Ding
    - 🏛️ Institutions: UMN, Cisco Research, LLNL
    - 📅 Date: October 5, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [tool coordination], [iterative refinement], [visual grounding]
    - 📖 TLDR: This paper proposes GUI-Spotlight, a model for GUI visual grounding that iteratively refines its focus using specialized tools like crop, extract, and find_color. Trained with a hybrid of supervised learning and reinforcement learning, the method dynamically invokes tools over multiple rounds, improving accuracy and efficiency. It significantly outperforms previous methods on benchmarks like ScreenSpot-Pro and UI-Vision with less training data.

- [GUI‑KV: Efficient GUI Agents via KV Cache with Spatio‑Temporal Awareness](https://arxiv.org/abs/2510.00536)
    - Kung‑Hsiang Huang, Haoyi Qiu, Yutong Dai, Caiming Xiong, Chien‑Sheng Wu
    - 🏛️ Institutions: Salesforce AI Research, UCLA
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

- [SCUBA: Salesforce Computer Use Benchmark](https://sfrcua.github.io/SCUBA/)
    - Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: Sep 30, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [enterprise automation], [demonstration augmentation], [process rewards], [SCUBA]
    - 📖 TLDR: This paper introduces **SCUBA**, a benchmark for evaluating computer-use agents on 300 enterprise-critical CRM tasks within Salesforce. Tasks span personas like admins and service agents, testing UI navigation, automation, data handling, and troubleshooting. SCUBA includes sandbox environments, milestone-based evaluations, and supports parallel execution. Baseline results show large performance gaps across agent designs, especially between open- and closed-source models, with success rates ranging from 5% to 50% depending on demonstration usage.

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
    - 🏛️ Institutions: DeepWisdom, Fudan Univ., HKUST(GZ), UC San Diego, KAUST, Westlake Univ., Stanford Univ., Yale Univ., NUS
    - 📅 Date: August 17, 2025
    - 📑 Publisher: SEA @ NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-as-a-judge], [RealDevWorld], [RealDevBench], [AppEvalPilot], [multimodal]
    - 📖 TLDR: This paper presents **RealDevWorld**, a novel framework to automatically evaluate production-ready GUI software generated by LLMs. It includes **RealDevBench**, a suite of 194 open-ended, multimodal software engineering tasks, and **AppEvalPilot**, an “agent-as-judge” system that simulates realistic GUI interactions to assess functional correctness, visual fidelity, and runtime behavior. It achieves high alignment with human judgment (accuracy 0.92, correlation 0.85), reducing the need for manual review and offering scalable, human-aligned evaluation. Code is available on GitHub.

- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
    - Zhangxuan Gu, Zhengwen Zeng, Zhenyu Xu, Xingran Zhou, Shuheng Shen, Yunfei Liu, Beitong Zhou, Changhua Meng, Tianyu Xia, Weizhi Chen, Yue Wen, Jingya Dou, Fei Tang, Jinzhen Lin, Yulin Liu, Zhenlin Guo, Yichen Gong, Heng Jia, Changlong Gao, Yuan Guo, Yong Deng, Zhenyu Guo, Liang Chen, Weiqiang Wang
    - 🏛️ Institutions: Ant Group
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [grounding], [navigation], [data cleaning], [Qwen2.5-VL], [UI-Venus]
    - 📖 TLDR: This technical report introduces **UI-Venus**, a screenshot-based UI agent built on the multimodal Qwen2.5-VL model and fine-tuned via **reinforcement fine-tuning (RFT)**. It achieves state-of-the-art performance on UI grounding and navigation benchmarks—e.g., Screenspot-V2/Pro (up to 95.3% / 61.9%) and AndroidWorld navigation (up to 65.9%)—by leveraging carefully crafted reward functions, efficient data cleaning pipelines, and a novel **self-evolving framework** (trajectory alignment and sparse action enhancement) to enhance reasoning coherence and handle rare actions. The code and checkpoints are open-sourced to encourage further development.

- [Test‑Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615)
    - Yong Du, Yuchen Yan, Fei Tang, Zhengxi Lu, Chang Zong, Weiming Lu, Shengpei Jiang, Yongliang Shen
    - 🏛️ Institutions: Zhejiang University (ZJU), Central South University (CSU), Zhejiang University of Science and Technology (ZUST), SF Technology
    - 📅 Date: August 7, 2025
    - 📑 Publisher: AAAI 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [test‑time scaling], [reinforcement learning], [self‑supervised], [GUI‑RC], [GUI‑RCPO], [benchmark], [Region Consistency], [GUI grounding]
    - 📖 TLDR: This paper introduces **GUI‑RC (Region Consistency)**, a test-time method that aggregates multiple model predictions via spatial voting to derive a consensus region—achieving 2–3% accuracy improvements on ScreenSpot benchmarks without any additional training. It extends this idea with **GUI‑RCPO (Region Consistency Policy Optimization)**, which turns region-consistency patterns into self-supervised rewards for reinforcement learning at inference time, refining model predictions on unlabeled data and yielding further improvements (e.g., from 83.57% to 85.14% on ScreenSpot‑v2). The approach demonstrates a novel and effective use of test-time optimization for more robust, data-efficient GUI grounding.

- [NatureGAIA: Pushing the Frontiers of GUI Agents with a Challenging Benchmark and High-Quality Trajectory Dataset](https://arxiv.org/abs/2508.01330)
    - Zihan Zheng, Tianle Cui, Chuwen Xie, Jiahui Zhang, Jiahui Pan, Lewei He, Qianglong Chen
    - 🏛️ Institutions: South China Normal University, Zhejiang University
    - 📅 Date: August 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [hierarchical agent], [reinforcement learning], [causal pathways], [WPSR], [NatureGAIA]
    - 📖 TLDR: This paper introduces **NatureGAIA**, a new benchmark based on the principle of **Causal Pathways**, which decomposes complex GUI tasks into programmatically verifiable atomic steps for rigorous and reproducible evaluation. A hierarchical agent architecture called **LightManus** was used to generate a human-verified trajectory dataset representing diverse and self-correcting interaction patterns. This dataset was used to conduct Reinforcement Fine-Tuning (RFT) on the Qwen2.5-VL-7B model. Even top-performing models like Claude-sonnet-4 only reached a Weighted Pathway Success Rate (WPSR) of 34.6%, while RFT improved the smaller model from 3.3% to 10.8%, yet performance dropped significantly in complex scenarios, highlighting current limitations in GUI agent capabilities.

- [GTA1: GUI Test-time Scaling Agent](https://arxiv.org/abs/2507.05791)
    - Yan Yang, Dongxu Li, Yutong Dai, Yuhao Yang, Ziyang Luo, Zirui Zhao, Zhiyuan Hu, Junzhe Huang, Amrita Saha, Zeyuan Chen, Ran Xu, Liyuan Pan, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research, ANU, HKU
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
    - 🔑 Key: [model], [reinforcement learning], [RLCS], [multimodal], [vision language model], [grounding], [GLM-4.1V-Thinking], [GLM-4.5V]
    - 📖 TLDR: Introduces two vision-language models—**GLM-4.1V-9B-Thinking**, a 9B-parameter model designed for multimodal reasoning, and **GLM-4.5V**, a larger version based on GLM-4.5-Air (106B parameters, 12B active). The authors propose a reasoning-centric training pipeline including large-scale pretraining and a novel **Reinforcement Learning with Curriculum Sampling (RLCS)** framework. The models show state-of-the-art performance across 42 (GLM-4.5V) and 28 (GLM-4.1V-Thinking) public multimodal benchmarks, often outperforming much larger models (e.g., Qwen-2.5-VL-72B and Gemini-2.5-Flash), especially in tasks like STEM reasoning, video/document understanding, coding, GUI agents, and grounding. Both models and training code are open-sourced.

- [LPO: Towards Accurate GUI Agent Interaction via Location Preference Optimization](https://arxiv.org/abs/2506.09373)
    - Jiaqi Tang, Yu Xia, Yi‑Feng Wu, Yuwei Hu, Yuhui Chen, Qing‑Guo Chen, Xiaogang Xu, Xiangyu Wu, Hao Lu, Yanqing Ma, Shiyin Lu, Qifeng Chen
    - 🏛️ Institutions: HKUST, Alibaba Group, CUHK, Nanjing University of Science and Technology
    - 📅 Date: June 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [grounding], [navigation], [location reward], [GRPO], [LPO]
    - 📖 TLDR: The paper introduces **Location Preference Optimization (LPO)** to improve GUI agent interaction accuracy. It uses information-entropy-driven zones of interest and a dynamic distance-based reward function. Built atop Group Relative Preference Optimization (GRPO), it enables more precise spatial grounding. Results show SOTA performance on offline benchmarks and real-world online GUI tasks.

- [GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents](https://arxiv.org/abs/2506.03143)
    - Qianhui Wu, Kanzhi Cheng, Rui Yang, Chaoyun Zhang, Jianwei Yang, Huiqiang Jiang, Jian Mu, Baolin Peng, Bo Qiao, Reuben Tan, Si Qin, Lars Liden, Qingwei Lin, Huan Zhang, Tong Zhang, Jianbing Zhang, Dongmei Zhang, Jianfeng Gao
    - 🏛️ Institutions: Microsoft, Nanjing Univ., UIUC
    - 📅 Date: June 3, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [grounding verifier], [attention mechanism], [coordinate‑free grounding], [GUI‑Actor]
    - 📖 TLDR: GUI‑Actor introduces a coordinate‑free visual grounding approach for GUI agents by adding an attention‑based “<ACTOR>” action head atop a frozen vision‑language model. It learns to align with relevant visual patches and produces multiple candidate regions per forward pass. An optional grounding verifier scores candidates to select the best. The method improves spatial‑semantic alignment and generalizes well across unseen resolutions. On benchmarks like ScreenSpot‑Pro, GUI‑Actor‑7B outperforms prior SOTA UI‑TARS‑72B, with verifier‑augmented versions achieving even higher accuracy—while only fine‑tuning ~100 M parameters.

- [ZeroGUI: Automating Online GUI Learning at Zero Human Cost](https://arxiv.org/abs/2505.23762)
    - Chenyu Yang, Shiqian Su, Shi Liu, Xuan Dong, Yue Yu, Weijie Su, Xuehui Wang, Zhaoyang Liu, Jinguo Zhu, Hao Li, Wenhai Wang, Yu Qiao, Xizhou Zhu, Jifeng Dai
    - 🏛️ Institutions: Shanghai Artificial Intelligence Lab, Tsinghua Univ, SJTU, HKUST, CUHK
    - 📅 Date: May 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [model-free], [VLM-task-generation], [VLM-reward-estimation], [ZeroGUI]
    - 📖 TLDR: Introduces **ZeroGUI**, a novel online learning framework that enables GUI agents (based on VLMs) to learn by autonomous interaction without human labels. It uses vision-language models to (i) generate diverse task instructions, (ii) evaluate task success, and (iii) apply a two-stage RL strategy (task-generated training + test-time adaptation). The method shows strong performance gains (e.g., +14% on UI-TARS, +63% on Aguvis) in desktop (OSWorld) and mobile (AndroidLab) GUI benchmarks, proving scalable, human-free GUI-agent training.  

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://arxiv.org/abs/2505.21936)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: OSU
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [CUA], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, SJTU AI Institute, Shanghai Jiao Tong University, Jiangsu Key Lab of Language Computing, Suzhou Laboratory
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [reward model], [progress reward], [LCS], [ProgRM]
    - 📖 TLDR: Introduces **ProgRM**, a novel framework giving dense intermediate rewards to GUI agents by estimating per‑step task progress. Labels are generated through an LCS‑based self‑annotation algorithm that identifies key steps in successful trajectories. Agents trained with ProgRM outperform outcome‑based reward models and proprietary LLMs like Claude‑3.7‑Sonnet across benchmarks.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://osworld-grounding.github.io/)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
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

- [A Summary on GUI Agents with Foundation Models Enhanced by Reinforcement Learning](https://arxiv.org/abs/2504.20464)
    - Jiahao Li, Kaer Huang
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: April 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [framework], [reinforcement learning], [multimodal], [training taxonomy]
    - 📖 TLDR: This paper presents a structured summary of recent advances in GUI agents powered by Multi-modal Large Language Models (MLLMs) and enhanced through Reinforcement Learning (RL). It formalizes GUI agent tasks as Markov Decision Processes and reviews modular architectures comprising Perception, Planning, and Acting modules. The study categorizes training methodologies into Prompt-based, Supervised Fine-Tuning (SFT), and RL-based approaches, highlighting the progression towards dynamic policy learning. The paper concludes by identifying key challenges and future directions for developing more capable and reliable GUI agents.

- [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)
    - Yuhang Liu, Pengxiang Li, Congkai Xie, Xavier Hu, Xiaotian Han, Shengyu Zhang, Hongxia Yang, Fei Wu
    - 🏛️ Institutions: Zhejiang Univ., Dalian Univ. of Tech., Reallm Labs, HK PolyU
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [model], [reinforcement learning], [planning], [reasoning], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: This paper introduces **InfiGUI-R1**, a multimodal GUI agent developed through the **Actor2Reasoner** framework, aiming to transition agents from reactive behaviors to deliberative reasoning. The framework comprises two stages: *Reasoning Injection*, which employs Spatial Reasoning Distillation to integrate GUI visual-spatial information with logical reasoning, and *Deliberation Enhancement*, which uses Reinforcement Learning with Sub-goal Guidance and Error Recovery Scenario Construction to refine the agent's planning and error correction capabilities. Evaluations on benchmarks like AndroidControl and ScreenSpot demonstrate that InfiGUI-R1-3B achieves state-of-the-art performance in GUI grounding and trajectory tasks, outperforming larger models in several categories.

- [TongUI: Building Generalized GUI Agents by Learning from Multimodal Web Tutorials](https://tongui-agent.github.io/)
    - Bofei Zhang, Zirui Shang, Zhi Gao, Wang Zhang, Rui Xie, Xiaojian Ma, Tao Yuan, Xinxiao Wu, Song-Chun Zhu, Qing Li
    - 🏛️ Institutions: BIGAI, BIT, PKU, SJTU, THU
    - 📅 Date: April 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [Qwen2.5-VL], [GUI-Net], [multimodal], [trajectory generation]
    - 📖 TLDR: This paper introduces **TongUI**, a framework for building generalized GUI agents by learning from multimodal web tutorials. By crawling and processing online tutorials into GUI agent trajectory data, the authors construct the **GUI-Net** dataset containing 143K trajectories across five operating systems and over 200 applications. Fine-tuning Qwen2.5-VL-3B/7B models on GUI-Net leads to significant performance improvements on grounding and navigation benchmarks, demonstrating the effectiveness of the TongUI framework.

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

- [GUI-R1: A Generalist R1-Style Vision-Language Action Model for GUI Agents](https://arxiv.org/abs/2504.10458)
    - Run Luo, Lu Wang, Wanwei He, Longze Chen, Jiaming Li, Min Yang, Xiaobo Xia
    - 🏛️ Institutions: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences, National University of Singapore
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [GRPO], [GUI-R1]
    - 📖 TLDR: GUI-R1 introduces a reinforcement learning framework that enhances the capabilities of Large Vision-Language Models (LVLMs) for GUI agents. By employing a unified action space and a rule-based reward function, the model efficiently learns to perform high-level tasks across multiple platforms, including Windows, Linux, MacOS, Android, and Web. Utilizing only 0.02% of the data compared to previous methods, GUI-R1 demonstrates superior performance on eight benchmarks, showcasing the potential of reinforcement learning in GUI agent tasks.

- [On the Robustness of GUI Grounding Models Against Image Attacks](https://arxiv.org/abs/2504.04716)
    - Haoren Zhao, Tianyi Chen, Zhen Wang
    - 🏛️ Institutions: HDU, Microsoft
    - 📅 Date: April 7, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [robustness], [adversarial attacks], [UGround], [ScreenSpot-V2]
    - 📖 TLDR: This paper systematically evaluates the robustness of GUI grounding models, such as UGround, against natural noise, untargeted adversarial attacks, and targeted adversarial attacks. Experiments conducted across mobile, desktop, and web interfaces reveal that these models are highly sensitive to adversarial perturbations and low-resolution conditions. The findings highlight vulnerabilities in current GUI grounding models and establish a benchmark for future research aimed at enhancing their robustness in practical applications.

- [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://arxiv.org/abs/2504.00906)
    - Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: April 1, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [Mixture-of-Grounding], [Proactive Hierarchical Planning], [benchmark], [OSWorld], [WindowsAgentArena], [AndroidWorld]
    - 📖 TLDR: This paper introduces *Agent S2*, a compositional framework for computer use agents that combines generalist and specialist models to address challenges in GUI element grounding and long-horizon task planning. The framework employs a novel Mixture-of-Grounding technique for precise GUI localization and Proactive Hierarchical Planning to dynamically refine action plans. Evaluations demonstrate that Agent S2 achieves state-of-the-art performance on benchmarks like OSWorld, WindowsAgentArena, and AndroidWorld, outperforming existing agents such as Claude Computer Use and UI-TARS.

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: March 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [dual-system cognition], [FOCUS], [ScreenSpot], [ScreenSpot-Pro]
    - 📖 TLDR: This paper introduces **FOCUS**, a novel GUI grounding framework inspired by human dual-system cognition. FOCUS dynamically switches between a fast, intuitive system and a slow, analytical system based on task complexity. The framework decomposes GUI grounding into three stages: interface summarization, focused analysis, and precise coordinate prediction. Trained on a synthesized dataset of 300,000 samples, FOCUS achieves state-of-the-art performance on the ScreenSpot and ScreenSpot-Pro benchmarks, demonstrating significant improvements in both efficiency and accuracy for complex GUI interactions.

- [Magma: A Foundation Model for Multimodal AI Agents](https://microsoft.github.io/Magma/)
    - Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai, Seonghyeon Ye, Joel Jang, Yuquan Deng, Lars Liden, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research, Univ. of Maryland, Univ. of Wisconsin-Madison, KAIST, Univ. of Washington
    - 📅 Date: Feb 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI], [Robotics]
    - 🔑 Key: [model], [framework], [SoM], [ToM], [robotics], [UI navigation]
    - 📖 TLDR: This paper introduces **Magma**, a foundation model designed for multimodal AI agents operating in both digital and physical environments. Magma extends traditional vision-language models by incorporating planning and action capabilities, enabling tasks from UI navigation to robotic manipulation. The model is pretrained on diverse datasets, including images, videos, and robotics data, utilizing **Set-of-Mark (SoM)** for action grounding and **Trace-of-Mark (ToM)** for action planning. Experiments demonstrate that SoM and ToM synergistically enhance Magma's spatial-temporal intelligence, achieving state-of-the-art performance in UI navigation and robotic manipulation tasks.

- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)
    - Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng, Xin Liu, Guang Shi
    - 🏛️ Institutions: ByteDance, Tsinghua University
    - 📅 Date: January 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [UI-TARS]
    - 📖 TLDR: This paper introduces **UI-TARS**, a native GUI agent model that processes screenshots to perform human-like interactions such as keyboard and mouse operations. Unlike traditional frameworks relying on commercial models with handcrafted prompts, UI-TARS is an end-to-end model demonstrating superior performance across over 10 GUI agent benchmarks. Key innovations include enhanced perception through large-scale GUI screenshot datasets, unified action modeling across platforms, incorporation of deliberate multi-step reasoning (System-2 Reasoning), and iterative training with reflective online traces, enabling continuous learning and adaptation with minimal human intervention.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://qiushisun.github.io/OS-Genesis-Home/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Lab, HKU, Johns Hopkins University, SJTU, Oxford, HKUST
    - 📅 Date: Dec 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [trajectory data], [reward model], [e2e model], [data synthesis], [OS-Genesis]
    - 📖 TLDR: This paper introduces *OS-Genesis*, an interaction-driven pipeline that automates the construction of high-quality and diverse GUI agent trajectory data without human supervision. By employing reverse task synthesis and a trajectory reward model, OS-Genesis enables effective end-to-end training of GUI agents, significantly enhancing their performance on online benchmarks.

- [Aria-UI: Visual Grounding for GUI Instructions](https://ariaui.github.io/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: HKU, Rhymes AI
    - 📅 Date: Dec 20, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [grounding], [visual grounding], [Aria-UI]
    - 📖 TLDR: This paper introduces *Aria-UI*, a large multimodal model specifically designed for GUI grounding. Aria-UI employs a pure-vision approach, avoiding reliance on auxiliary inputs like HTML or AXTree. It utilizes a scalable data pipeline to synthesize diverse and high-quality instruction samples and incorporates textual and text-image interleaved action histories for robust context-aware reasoning. Aria-UI achieves state-of-the-art results across offline and online agent benchmarks, outperforming both vision-only and AXTree-reliant baselines.

- [OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://github.com/OS-Agent-Survey/OS-Agent-Survey)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shawn Wang, Xinchen Xu, Shuofei Qiao , Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao, Hongxia Yang, Fan Wu, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Fudan University, OPPO AI Center, University of Chinese Academy of Sciences, Chinese Academy of Sciences, The Chinese HKU, Tsinghua University, 01.AI, The Hong Kong Polytechnic University, SJTU
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Github Repo
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This paper conducts a comprehensive survey on OS Agents, which are (M)LLM-based agents that use computing devices (e.g., computers and mobile phones) by operating within the environments and interfaces (e.g., Graphical User Interface (GUI)) provided by operating systems (OS) to automate tasks. The survey begins by elucidating the fundamentals of OS Agents, exploring their key components including the environment, observation space, and action space, and outlining essential capabilities such as understanding, planning, and grounding. Methodologies for constructing OS Agents are examined, with a focus on domain-specific foundation models and agent frameworks. A detailed review of evaluation protocols and benchmarks highlights how OS Agents are assessed across diverse tasks. Finally, current challenges and promising future research directions, including safety and privacy, personalization and self-evolution, are discussed. 

- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501)
    - Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen, Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Branislav Kveton, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, Franck Dernoncourt
    - 🏛️ Institutions: UMD, SUNY Buffalo, University of Oregon, Adobe Research, Meta AI, University of Rochester, UCSD, CMU, Dolby Labs, Intel AI Research, UNSW
    - 📅 Date: December 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This survey provides a comprehensive overview of GUI agents powered by Large Foundation Models, detailing their benchmarks, evaluation metrics, architectures, and training methods. It introduces a unified framework outlining their perception, reasoning, planning, and acting capabilities, identifies open challenges, and discusses future research directions, serving as a resource for both practitioners and researchers in the field.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, NUS
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [Information-Sensitive Cropping], [Self-Refining Dual Learning], [visual grounding], [model]
    - 📖 TLDR: This paper introduces *Iris*, a visual agent designed to enhance GUI automation by addressing challenges in high-resolution, complex digital environments. It employs two key innovations: **Information-Sensitive Cropping (ISC)**, which dynamically identifies and prioritizes visually dense regions using an edge detection algorithm for efficient processing, and **Self-Refining Dual Learning (SRDL)**, which enhances the agent's ability to handle complex tasks through a dual-learning loop that iteratively refines its performance without requiring additional annotated data. Empirical evaluations demonstrate that Iris achieves state-of-the-art performance across multiple benchmarks with only 850K GUI annotations, outperforming methods using ten times more training data.

- [Falcon-UI: Understanding GUI Before Following User Instructions](https://arxiv.org/abs/2412.09362)
    - Huawen Shen, Chang Liu, Gengluo Li, Xinlong Wang, Yu Zhou, Can Ma, Xiangyang Ji
    - 🏛️ Institutions: Chinese Academy of Sciences, Tsinghua University, Nankai University, BAAI
    - 📅 Date: Dec 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [Falcon-UI], [GUI understanding]
    - 📖 TLDR: This paper introduces *Falcon-UI*, a GUI agent model that emphasizes understanding GUI contexts before following user instructions. The authors present the *Insight-UI Dataset*, an instruction-free GUI navigation dataset generated from the Common Crawl corpus, simulating various platforms like iOS, Android, Windows, and Linux across multiple resolutions on 312K domains. Falcon-UI is pretrained on this dataset and fine-tuned on Android and Web GUI datasets, achieving performance comparable to larger models, highlighting the importance of decoupling GUI understanding from instruction following in agent performance. 

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://aguvis-project.github.io/)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: HKU, NTU, Salesforce
    - 📅 Date: Dec 5, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [planning], [reasoning], [Aguvis], [visual grounding]
    - 📖 TLDR: This paper introduces *Aguvis*, a unified pure vision-based framework for autonomous GUI agents that operates across various platforms. It leverages image-based observations and grounds natural language instructions to visual elements, employing a consistent action space to ensure cross-platform generalization. The approach integrates explicit planning and reasoning within the model, enhancing its ability to autonomously navigate and interact with complex digital environments. A large-scale dataset of GUI agent trajectories is constructed, incorporating multimodal reasoning and grounding. Comprehensive experiments demonstrate that Aguvis surpasses previous state-of-the-art methods in both offline and real-world online scenarios, achieving the first fully autonomous pure vision GUI agent capable of performing tasks independently without collaboration with external closed-source models. All datasets, models, and training recipes are open-sourced to facilitate future research.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: December 2, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [reinforcement learning], [Ponder & Press]
    - 📖 TLDR: This paper introduces *Ponder & Press*, a divide-and-conquer framework for general computer control using only visual input. The approach combines a general-purpose multimodal large language model (MLLM) as an 'interpreter' to translate high-level user instructions into detailed action descriptions, with a GUI-specific MLLM as a 'locator' that precisely identifies GUI elements for action execution. By relying solely on visual inputs, the agent offers a versatile, human-like interaction paradigm applicable across various platforms, achieving state-of-the-art performance in GUI grounding and control tasks.

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://arxiv.org/abs/2411.17465)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: NUS, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [UI-Guided Visual Token Selection], [Interleaved Vision-Language-Action Streaming], [ShowUI]
    - 📖 TLDR: This paper introduces *ShowUI*, a vision-language-action model designed to enhance GUI automation by addressing challenges in UI visual perception and action modeling. It features innovations like UI-Guided Visual Token Selection to reduce computational costs and Interleaved Vision-Language-Action Streaming for effective management of visual-action history. Trained on a curated dataset, ShowUI achieves 75.1% accuracy in zero-shot screenshot grounding and demonstrates competitive performance across web, mobile, and online environments.

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
    - 🔑 Key: [survey], [Generalist Virtual Agent], [GVA], [autonomous agents], [digital platforms]
    - 📖 TLDR: This survey introduces the concept of Generalist Virtual Agents (GVAs), autonomous entities designed to operate across various digital platforms and environments to assist users in performing diverse tasks. It traces the evolution of GVAs from early intelligent assistants to modern implementations incorporating large-scale models, discussing their philosophical foundations, development challenges, and current methodologies. The paper provides a detailed taxonomy of GVA environments, tasks, and capabilities, aiming to bridge theoretical and practical aspects and suggesting that agents operating in environments closely mirroring the real world are more likely to exhibit human-like intelligence.

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890)
    - Shuai Wang, Weiwen Liu, Jingxuan Chen, Weinan Gan, Xingshan Zeng, Shuai Yu, Xinlong Hao, Kun Shao, Yasheng Wang, Ruiming Tang
    - 🏛️ Institutions: Huawei Noah’s Ark Lab
    - 📅 Date: November 7, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey]
    - 📖 TLDR: This survey consolidates recent research on GUI agents powered by foundation models, particularly Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs). It discusses representative datasets and benchmarks, summarizes a unified framework capturing essential components from prior studies, and explores commercial applications. The paper identifies key challenges and proposes future research directions to inspire further developments in (M)LLM-based GUI agents.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Tech, HKU, Stanford
    - 📅 Date: Nov 4, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [attack], [adversarial pop-ups], [VLM agents], [safety]
    - 📖 TLDR: This paper demonstrates that vision-language model (VLM) agents can be easily deceived by carefully designed adversarial pop-ups, leading them to perform unintended actions such as clicking on these pop-ups instead of completing their assigned tasks. Integrating these pop-ups into environments like OSWorld and VisualWebArena resulted in an average attack success rate of 86% and a 47% decrease in task success rate. Basic defense strategies, such as instructing the agent to ignore pop-ups or adding advertisement notices, were found to be ineffective against these attacks.

- [OS-ATLAS: A Foundation Action Model For Generalist GUI Agents](https://osatlas.github.io/)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Lab, SJTU, HKU, MIT
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [OS-Atlas]
    - 📖 TLDR: This paper introduces OS-Atlas, a foundational GUI action model designed to enhance GUI grounding and out-of-distribution tasks. The authors developed a toolkit to synthesize multi-platform GUI grounding data, resulting in a cross-platform corpus of over 13 million GUI elements. OS-Atlas demonstrates significant performance improvements across six benchmarks spanning mobile, desktop, and web platforms.

- [AutoGLM: Autonomous Foundation Agents for GUIs](https://xiao9905.github.io/AutoGLM/)
    - Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long Iong, Jiadai Sun, Jiaqi Wang, Junjie Gao, Junjun Shan, Kangning Liu, Shudan Zhang, Shuntian Yao, Siyi Cheng, Wentao Yao, Wenyi Zhao, Xinghan Liu, Xinyi Liu, Xinying Chen, Xinyue Yang, Yang Yang, Yifan Xu, Yu Yang, Yujia Wang, Yulin Xu, Zehan Qi, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu AI, Tsinghua University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [model], [learning], [AutoGLM]
    - 📖 TLDR: This paper introduces AutoGLM, a new series in the ChatGLM family, designed as foundation agents for autonomous control of digital devices through GUIs. It addresses the challenges foundation models face in decision-making within dynamic environments by developing agents capable of learning through autonomous interactions. Focusing on web browsers and Android devices, AutoGLM integrates various techniques to create deployable agent systems. Key insights include the importance of designing an appropriate "intermediate interface" for GUI control and a novel progressive training framework for self-evolving online curriculum reinforcement learning. Evaluations demonstrate AutoGLM's effectiveness across multiple domains, achieving notable success rates in web browsing and Android device control tasks.

- [EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data](https://doi.org/10.48550/arXiv.2410.19461)
    - Xuetian Chen, Hangcheng Li, Jiaqing Liang, Sihang Jiang, Deqing Yang
    - 🏛️ Institutions: Fudan University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [framework], [synthetic data]
    - 📖 TLDR: The *EDGE* framework proposes an innovative approach to improve GUI understanding and interaction capabilities in vision-language models through large-scale, multi-granularity synthetic data generation. By leveraging webpage data, EDGE minimizes the need for manual annotations and enhances the adaptability of models across desktop and mobile GUI environments. Evaluations show its effectiveness in diverse GUI-related tasks, contributing significantly to autonomous agent development in GUI navigation and interaction.

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: XJTU, Shanghai AI Lab, HKU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [multi-agent systems], [specialized generalist agent], [OSWorld benchmark]
    - 📖 TLDR: AgentStore introduces a scalable platform to integrate and manage heterogeneous agents, designed to enhance generalist assistant capabilities for diverse computer tasks. Using a MetaAgent and AgentToken strategy, AgentStore shows improved generalization on the OSWorld benchmark.

- [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164)
    - Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang
    - 🏛️ Institutions: Simular Research
    - 📅 Date: October 10, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [autonomous GUI interaction], [experience-augmented hierarchical planning]
    - 📖 TLDR: This paper introduces Agent S, an open agentic framework that enables autonomous interaction with computers through a Graphical User Interface (GUI). The system addresses key challenges in automating computer tasks through experience-augmented hierarchical planning and an Agent-Computer Interface (ACI). Agent S demonstrates significant improvements over baselines on the OSWorld benchmark, achieving a 20.58% success rate (83.6% relative improvement). The framework shows generalizability across different operating systems and provides insights for developing more effective GUI agents.

- [TinyClick: Single-Turn Agent for Empowering GUI Automation](https://arxiv.org/abs/2410.11871)
    - Pawel Pawlowski, Krystian Zawistowski, Wojciech Lapacz, Marcin Skorupa, Adam Wiacek, Sebastien Postansque, Jakub Hoscilowicz
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 9, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [vision language model], [Screenspot], [OmniAct]
    - 📖 TLDR: TinyClick is a compact, single-turn agent designed to automate GUI tasks by precisely locating screen elements via the Vision-Language Model Florence-2-Base. Trained with multi-task strategies and MLLM-based data augmentation, TinyClick achieves high accuracy on Screenspot and OmniAct, outperforming specialized GUI interaction models and general MLLMs like GPT-4V. The model's lightweight design (0.27B parameters) ensures fast processing and minimal latency, making it efficient for real-world applications on multiple platforms.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://osu-nlp-group.github.io/UGround/)
    - Boyu Gou, Ruochen Wang, Boyuan Zheng, Yucheng Xie, Cheng Chang, Yiheng Shu, Haotian Sun, Yu Su
    - 🏛️ Institutions: OSU, Orby AI
    - 📅 Date: October 7, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [model], [dataset], [visual grounding], [GUI agents], [cross-platform generalization], [UGround], [SeeAct-V], [synthetic data]
    - 📖 TLDR: This paper introduces UGround, a universal visual grounding model for GUI agents that enables human-like navigation of digital interfaces. The authors advocate for GUI agents with human-like embodiment that perceive the environment entirely visually and take pixel-level actions. UGround is trained on a large-scale synthetic dataset of 10M GUI elements across 1.3M screenshots. Evaluated on six benchmarks spanning grounding, offline, and online agent tasks, UGround significantly outperforms existing visual grounding models by up to 20% absolute. Agents using UGround achieve comparable or better performance than state-of-the-art agents that rely on additional textual input, demonstrating the feasibility of vision-only GUI agents.

- [Turn Every Application into an Agent: Towards Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://arxiv.org/abs/2409.17140)
    - Junting Lu, Zhiyang Zhang, Fangkai Yang, Jue Zhang, Lu Wang, Chao Du, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Peking University, Microsoft
    - 📅 Date: September 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [API interaction], [HACI], [Agent OS]
    - 📖 TLDR: This paper proposes an API-centered framework called **AXIS**, enhancing the efficiency and reliability of LLM-based agents by prioritizing API interactions over UI-based actions. This approach aims to reduce the high latency and error rates of traditional UI-interaction models. AXIS not only supports the rapid creation and extension of APIs through automated application exploration but also contributes to a new **Human-Agent-Computer Interaction (HACI)** framework. The paper outlines the development of an agent-centric operating system (Agent OS), which improves task completion times by up to 70% and reduces cognitive load on users while maintaining high accuracy across complex multi-application tasks.

- [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://arxiv.org/abs/2408.06327)
    - Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Yifan Xu, Xixuan Song, Shudan Zhang, Hanyu Lai, Xinyi Liu, Hanlin Zhao, Jiadai Sun, Xinyue Yang, Yu Yang, Zehan Qi, Shuntian Yao, Xueqiao Sun, Siyi Cheng, Qinkai Zheng, Hao Yu, Hanchen Zhang, Wenyi Hong, Ming Ding, Lihang Pan, Xiaotao Gu, Aohan Zeng, Zhengxiao Du, Chan Hee Song, Yu Su, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, MSRA, The Ohio State University
    - 📅 Date: August 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [VisualAgentBench], [VAB]
    - 📖 TLDR: The authors introduce *VisualAgentBench (VAB)*, a comprehensive benchmark designed to train and evaluate large multimodal models (LMMs) as visual foundation agents across diverse scenarios, including embodied tasks, graphical user interfaces, and visual design. VAB comprises five distinct environments that systematically challenge LMMs' understanding and interaction capabilities. Additionally, the benchmark offers supervised fine-tuning trajectory data for behavior cloning training, demonstrating the potential to improve open LMMs for serving as visual foundation agents.

- [OmniParser for Pure Vision Based GUI Agent](https://microsoft.github.io/OmniParser/)
    - Yadong Lu, Jianwei Yang, Yelong Shen, Ahmed Awadallah
    - 🏛️ Institutions: MSR, Microsoft Gen AI
    - 📅 Date: August 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [OmniParser]
    - 📖 TLDR: This paper introduces **OmniParser**, a method for parsing user interface screenshots into structured elements, enhancing the ability of models like GPT-4V to generate actions accurately grounded in corresponding UI regions. The authors curated datasets for interactable icon detection and icon description, fine-tuning models to parse interactable regions and extract functional semantics of UI elements.

- [CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents](https://arxiv.org/abs/2407.01511)
    - Tianqi Xu, Linyao Chen, Dai-Jie Wu, Yanjun Chen, Zecheng Zhang, Xiang Yao, Zhiqiang Xie, Yongchao Chen, Shilong Liu, Bochen Qian, Philip Torr, Bernard Ghanem, Guohao Li
    - 🏛️ Institutions: KAUST, UTokyo, CMU, Stanford, Harvard, Tsinghua University, SUSTech, Oxford
    - 📅 Date: July 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [framework], [evaluation], [CRAB]
    - 📖 TLDR: The authors present *CRAB*, a benchmark framework designed to evaluate Multimodal Language Model agents across multiple environments. It features a graph-based fine-grained evaluation method and supports automatic task generation, addressing limitations in existing benchmarks.

- [Read Anywhere Pointed: Layout-aware GUI Screen Reading with Tree-of-Lens Grounding](https://screen-point-and-read.github.io/)
    - Yue Fan, Lei Ding, Ching-Chen Kuo, Shan Jiang, Yang Zhao, Xinze Guan, Jie Yang, Yi Zhang, Xin Eric Wang
    - 🏛️ Institutions: UCSC, MSR
    - 📅 Date: June 27, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [ToL], [screen reading], [accessibility]
    - 📖 TLDR: The authors propose the Tree-of-Lens (ToL) agent to address the Screen Point-and-Read (ScreenPR) task, which involves generating natural language descriptions of screen regions based on user-indicated points. The ToL agent constructs a Hierarchical Layout Tree to comprehend the content and articulate the layout and spatial relationships between elements. The authors also introduce the ScreenPR benchmark, consisting of 650 screenshots from web, mobile, and operating system GUIs, manually annotated with 1,500 target points and regions.

- [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://arxiv.org/abs/2406.14056)
    - Ziyang Meng, Yu Dai, Zezheng Gong, Shaoxiong Guo, Minglong Tang, Tongquan Wei
    - 🏛️ Institutions: SJTU
    - 📅 Date: June 20, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [framework], [VGA], [hallucination]
    - 📖 TLDR: This paper introduces VGA, a fine-tuned model designed to enhance GUI comprehension by reducing hallucinations. The authors constructed a Vision Question Answering (VQA) dataset of 63.8k high-quality examples using a Referent Method, ensuring model responses are highly dependent on visual content. They also propose a two-stage fine-tuning method called Foundation and Advanced Comprehension (FAC) to improve the model's ability to extract information from images and align with human intent.

- [Identifying User Goals from UI Trajectories](https://arxiv.org/abs/2406.14314)
    - Omri Berkovitch, Sapir Caduri, Noam Kahlon, Anatoly Efros, Avi Caciularu, Ido Dagan
    - 🏛️ Institutions: Google Research, Bar-Ilan University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [evaluation metric], [intent identification]
    - 📖 TLDR: This paper introduces the task of goal identification from observed UI trajectories, aiming to infer the user's intended task based on their GUI interactions. It proposes a novel evaluation metric to assess whether two task descriptions are paraphrases within a specific UI environment. Experiments utilizing the Android-In-The-Wild and Mind2Web datasets reveal that state-of-the-art models, such as GPT-4 and Gemini-1.5 Pro, underperform compared to humans, indicating significant room for improvement.

- [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://ical-learning.github.io/)
    - Gabriel Sarch, Lawrence Jang, Michael J. Tarr, William W. Cohen, Kenneth Marino, Katerina Fragkiadaki
    - 🏛️ Institutions: CMU, Google DeepMind
    - 📅 Date: June 20, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [memory], [in-context learning], [ICAL]
    - 📖 TLDR: This paper introduces *In-Context Abstraction Learning (ICAL)*, a method enabling Vision-Language Models (VLMs) to generate their own examples from sub-optimal demonstrations and human feedback. By abstracting trajectories into generalized programs of thought, ICAL enhances decision-making in retrieval-augmented LLM and VLM agents, reducing reliance on manual prompt engineering and improving performance across various tasks.

- [GUICourse: From General Vision Language Models to Versatile GUI Agents](https://github.com/yiye3/GUICourse)
    - Wentong Chen, Junbo Cui, Jinyi Hu, Yujia Qin, Junjie Fang, Yue Zhao, Chongyi Wang, Jun Liu, Guirong Chen, Yupeng Huo, Yuan Yao, Yankai Lin, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Tsinghua University, Rhapsody AI, University of Electronic Science and Technology of China
    - 📅 Date: June 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [framework], [GUICourse]
    - 📖 TLDR: This paper introduces *GUICourse*, a suite of datasets aimed at training visual-based GUI agents from general vision-language models. It addresses challenges in OCR, grounding, and GUI knowledge, enhancing the models' capabilities in GUI navigation tasks.

- [GUI-WORLD: A Dataset for GUI-oriented Multimodal LLM-based Agents](https://arxiv.org/abs/2406.10819)
    - Dongping Chen, Yue Huang, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan, Pan Zhou, Jianfeng Gao, Lichao Sun
    - 🏛️ Institutions: Huazhong University of Science and Technology (HUST), MSR, University of Illinois at Chicago (UIC)
    - 📅 Date: June 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [GUI-World], [GUI-Vid]
    - 📖 TLDR: This paper introduces *GUI-World*, a comprehensive dataset designed to evaluate Multimodal Large Language Models (MLLMs) in dynamic and complex GUI environments. It includes over 12,000 annotated GUI interaction videos covering diverse applications and scenarios. The study highlights the limitations of current MLLMs in handling dynamic and multi-step tasks and presents *GUI-Vid*, a fine-tuned VideoLLM, demonstrating improved understanding of various GUI tasks.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: CMU, UCSB
    - 📅 Date: June 2024
    - 📑 Publisher: NAACL 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [UI element localization], [LVG]
    - 📖 TLDR: This work introduces the task of visual UI grounding, which unifies detection and grounding by enabling models to identify UI elements referenced by natural language commands solely from visual input. The authors propose **LVG**, a model that outperforms baselines pre-trained on larger datasets by over 4.9 points in top-1 accuracy, demonstrating its effectiveness in localizing referenced UI elements without relying on UI metadata.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://arxiv.org/abs/2406.10227)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen WU, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: NUS, Microsoft Gen AI
    - 📅 Date: June 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [instructional videos], [visual planning], [hierarchical task decomposition], [complex software interaction]
    - 📖 TLDR: VideoGUI presents a benchmark for evaluating GUI automation on tasks derived from instructional videos, focusing on visually intensive applications like Adobe Photoshop and video editing software. The benchmark includes 178 tasks, with a hierarchical evaluation method distinguishing high-level planning, mid-level procedural steps, and precise action execution. VideoGUI reveals current model limitations in complex visual tasks, marking a significant step toward improved visual planning in GUI automation.

- [UIClip: A Data-driven Model for Assessing User Interface Design](https://arxiv.org/abs/2404.12500)
    - Jason Wu, Yi-Hao Peng, Amanda Li, Amanda Swearngin, Jeffrey P. Bigham, Jeffrey Nichols
    - 🏛️ Institutions: CMU, Apple
    - 📅 Date: Apr 18, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [UIClip], [vision foundation model], [foundation model]
    - 📖 TLDR: This paper introduces *UIClip*, a machine-learned model that evaluates the design quality and visual relevance of user interfaces by analyzing screenshots and corresponding natural language descriptions. Trained on a large-scale dataset combining automated crawling, synthetic augmentation, and human ratings, UIClip assigns numerical scores representing a UI's relevance and quality, and offers design suggestions. Evaluations show that UIClip's assessments align closely with human designer rankings. The paper also demonstrates UIClip's utility in applications like UI code generation, design tips generation, and quality-aware UI example search.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: HKU, CMU, Salesforce, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [real computer tasks], [online environment], [online benchmark]
    - 📖 TLDR: OSWorld introduces a groundbreaking benchmark for multimodal agents to perform open-ended tasks within real computer environments across platforms like Ubuntu, Windows, and macOS. It includes 369 real-world tasks involving web and desktop apps, file management, and multi-app workflows, with custom evaluation scripts for reproducibility. The results reveal current agents’ limitations in GUI interaction and operational knowledge, as they achieve just 12.24% task success compared to humans' 72.36%, highlighting critical gaps for future model improvement.

- [Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)
    - Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
    - 🏛️ Institutions: UCB, UMich
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [evaluation model], [domain transfer]
    - 📖 TLDR: This paper presents an autonomous evaluation framework for digital agents to enhance performance on web navigation and device control. The study introduces modular, cost-effective evaluators achieving up to 92.9% accuracy in benchmarks like WebArena and outlines their use in fine-tuning agents, improving state-of-the-art by 29% without additional supervision.

- [Improving Language Understanding from Screenshots](https://arxiv.org/abs/2402.14073)
    - Tianyu Gao, Zirui Wang, Adithya Bhaskar, Danqi Chen
    - 🏛️ Institutions: Princeton
    - 📅 Date: February 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [screenshot language models], [patch-and-text prediction]
    - 📖 TLDR: This paper introduces a novel approach to improve the language understanding capabilities of screenshot language models (LMs). The authors propose a Patch-and-Text Prediction (PTP) objective, which masks and recovers both image patches and text within screenshots. The method significantly narrows the performance gap between screenshot LMs and text-only models on language understanding tasks, achieving comparable results to BERT on most GLUE tasks. The research also extends PTP to train autoregressive screenshot LMs, demonstrating improved perplexity by utilizing screenshot context.

- [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://arxiv.org/abs/2402.11208)
    - Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
    - 🏛️ Institutions: Renming University of China, PKU, Tencent
    - 📅 Date: Feb 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI], [Misc]
    - 🔑 Key: [attack], [backdoor], [safety]
    - 📖 TLDR: This paper investigates backdoor attacks on LLM-based agents, introducing a framework that categorizes attacks based on outcomes and trigger locations. The study demonstrates the vulnerability of such agents to backdoor attacks and emphasizes the need for targeted defenses.

- [ScreenAgent: A Computer Control Agent Driven by Visual Language Large Model](https://arxiv.org/abs/2402.07945)
    - Runliang Niu, Jindong Li, Shiqi Wang, Yali Fu, Xiyu Hu, Xueyuan Leng, He Kong, Yi Chang, Qi Wang
    - 🏛️ Institutions: Jilin University
    - 📅 Date: February 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual language model], [computer control agent]
    - 📖 TLDR: This paper introduces ScreenAgent, a computer control agent powered by a visual language large model. The system can interpret natural language instructions and execute them on various computer applications by analyzing screen content. ScreenAgent employs a novel action grounding mechanism to map high-level instructions to specific UI interactions. Evaluated on a diverse set of tasks across different applications, ScreenAgent demonstrates superior performance in task completion and generalization compared to existing methods.

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://arxiv.org/abs/2402.04615)
    - Gilles Baechler, Srinivas Sunkara, Maria Wang, Fedir Zubach, Hassan Mansoor, Vincent Etter, Victor Cărbune, Jason Lin, Jindong Chen, Abhanshu Sharma
    - 🏛️ Institutions: Google DeepMind
    - 📅 Date: February 7, 2024
    - 📑 Publisher: IJCAI 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [UI understanding], [infographics understanding], [vision language model]
    - 📖 TLDR: This paper introduces ScreenAI, a vision-language model specializing in UI and infographics understanding. The model combines the PaLI architecture with the flexible patching strategy of pix2struct and is trained on a unique mixture of datasets. ScreenAI achieves state-of-the-art results on several UI and infographics-based tasks, outperforming larger models. The authors also release three new datasets for screen annotation and question answering tasks.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Yantao Li, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: Nanjing University, Shanghai AI Lab
    - 📅 Date: January 19, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [benchmark], [GUI grounding], [visual grounding]
    - 📖 TLDR: TBD.

- [AgentBench: Evaluating LLMs as Agents](https://llmbench.ai/agent)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU, ByteDance
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI], [General]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.

- [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914)
    - Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhao Chen, Yuxuan Wang, Yining Ye, Jiayi Zhang, Hao Dong, Wenhu Chen, Yizhou Wang, Kai-Wei Chang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI
    - 📅 Date: December 15, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [visual language model], [GUI agent]
    - 📖 TLDR: This paper presents CogAgent, a visual language model designed for GUI agents. The authors introduce a new dataset, CogBench, featuring 1,430 GUI tasks across various applications. CogAgent employs a novel training approach combining supervised fine-tuning and decision-making fine-tuning. The model demonstrates superior performance on CogBench and generalizes well to unseen applications, outperforming existing models like GPT-4V in GUI task completion.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: MSRA
    - 📅 Date: October 7, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [reinforcement learning], [UI task automation], [instruction grounding]
    - 📖 TLDR: This paper introduces a multimodal model, termed RUIG (Reinforced UI Instruction Grounding), for automating UI tasks through natural language instructions. By leveraging a pixel-to-sequence approach, the model directly decodes UI element locations from screenshots based on user commands, removing the need for metadata like element coordinates. The framework uses a transformer-based encoder-decoder setup optimized through reinforcement learning to improve spatial accuracy. This novel approach outperforms prior methods, offering a generalized solution for UI task automation.

- [You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/abs/2309.11436)
    - Zhuosheng Zhang, Aston Zhang
    - 🏛️ Institutions: SJTU
    - 📅 Date: September 20, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [multimodal agent], [chain-of-action technique]
    - 📖 TLDR: This paper presents Auto-GUI, a multimodal agent capable of directly interacting with graphical user interfaces without relying on environment parsing or application-specific APIs. The authors introduce a novel chain-of-action technique that leverages previous action histories and future action plans to improve decision-making. Auto-GUI is evaluated on a new device-control benchmark, AITW, demonstrating state-of-the-art performance in action prediction and task completion across various applications and web-based tasks.

- [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://arxiv.org/abs/2305.19308)
    - Hongxin Li, Jingran Su, Yuntao Chen, Qing Li, Zhaoxiang Zhang
    - 🏛️ Institutions: UCAS, HKISI-CAS, PolyU, Shanghai AI Lab
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
