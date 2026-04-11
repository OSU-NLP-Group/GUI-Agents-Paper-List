# Papers with Keyword: model

- [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)
    - Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu
    - 🏛️ Institutions: Meituan, Fudan University, Tongji University, The Hong Kong University of Science and Technology
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [framework], [synthetic experience], [verifiable synthesis], [OSWorld], [EvoCUA]
    - 📖 TLDR: EvoCUA replaces static imitation with an evolving training loop built on verifiable task synthesis, high-throughput sandbox rollouts, and iterative policy optimization from both successful and failed trajectories. On OSWorld it reaches 56.7% success, outperforming prior open-source computer-use agents and even some leading closed-weight systems.

- [ShowUI-π: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965)
    - Siyuan Hu, Kevin Qinghong Lin, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: December 31, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [drag interaction], [flow-based model], [continuous action], [ScreenDrag], [ShowUI-π]
    - 📖 TLDR: ShowUI-π treats GUI dragging as a continuous dexterous-control problem rather than only discrete point prediction, while still supporting ordinary click actions in the same model. It also introduces ScreenDrag with 20K trajectories across five domains, and the 450M-parameter model outperforms much larger proprietary GUI agents on this benchmark.

- [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047)
    - Hanzhang Zhou, Xu Zhang, Panrong Tong, Jianan Zhang, Liangyu Chen, Quyu Kong, Chenglin Cai, Chen Liu, Yue Wang, Jingren Zhou, Steven Hoi
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [model], [agent-user interaction], [MCP], [device-cloud collaboration], [online reinforcement learning], [MAI-UI]
    - 📖 TLDR: MAI-UI is a foundation GUI-agent family aimed at realistic deployment rather than benchmark-only optimization. It extends pure UI control with agent-user interaction, MCP tool calls, native device-cloud collaboration, and long-horizon online reinforcement learning, and sets strong results on grounding, AndroidWorld, and MobileWorld.

- [HiconAgent: History Context-aware Policy Optimization for GUI Agents](https://arxiv.org/abs/2512.01763)
    - Xurui Zhou, Gongwei Chen, Yuquan Xie, Zaijing Li, Kaiwen Zhou, Shuai Wang, Shuo Yang, Zhuotao Tian, Rui Shao
    - 🏛️ Institutions: Harbin Institute of Technology, Shenzhen, Huawei Noah’s Ark Lab
    - 📅 Date: December 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [history modeling], [policy optimization], [GUI navigation], [HiconAgent]
    - 📖 TLDR: This paper studies how GUI agents should use historical context during sequential decision making, arguing that naively including full history is both expensive and distracting. It introduces History Context-aware Policy Optimization, combining dynamic context sampling with anchor-guided history compression to train lightweight agents that use past observations and actions more effectively. The resulting HiconAgent-3B improves performance on benchmarks such as GUI-Odyssey, AndroidControl, and AITW while reducing FLOPs and inference cost.

- [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790)
    - Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple, The University of Hong Kong
    - 📅 Date: October 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [hybrid action], [tool calls], [synthetic tasks], [online reinforcement learning], [OSWorld], [WindowsAgentArena], [UltraCUA]
    - 📖 TLDR: UltraCUA is a foundation computer-use model that combines primitive GUI actions with higher-level tool calls, supported by automated tool extraction, synthetic verifiable tasks, supervised fine-tuning, and online reinforcement learning. This hybrid action setup improves both robustness and efficiency, yielding strong gains on OSWorld and good transfer to WindowsAgentArena.

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

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [benchmark], [API-GUI paradigm], [dataset], [distributed RL], [entropulse]
    - 📖 TLDR: This paper presents **ComputerRL**, a large-scale end-to-end reinforcement learning framework enabling agents to operate complex desktop tasks. It introduces the **API-GUI paradigm**, combining programmatic API calls with GUI actions, and a **distributed RL infrastructure** managing thousands of parallel virtual Ubuntu desktops for scalable training. A novel **Entropulse** training strategy alternates between reinforcement learning and supervised fine-tuning to prevent entropy collapse over long training runs. Applied to open models like GLM-4-9B-0414, ComputerRL achieves a new state-of-the-art success rate of **48.9%** on the OSWorld benchmark via the GLM-ComputerRL-9B model.

- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
    - Zhangxuan Gu, Zhengwen Zeng, Zhenyu Xu, Xingran Zhou, Shuheng Shen, Yunfei Liu, Beitong Zhou, Changhua Meng, Tianyu Xia, Weizhi Chen, Yue Wen, Jingya Dou, Fei Tang, Jinzhen Lin, Yulin Liu, Zhenlin Guo, Yichen Gong, Heng Jia, Changlong Gao, Yuan Guo, Yong Deng, Zhenyu Guo, Liang Chen, Weiqiang Wang
    - 🏛️ Institutions: Ant Group
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [grounding], [navigation], [data cleaning], [Qwen2.5-VL], [UI-venus]
    - 📖 TLDR: This technical report introduces **UI-Venus**, a screenshot-based UI agent built on the multimodal Qwen2.5-VL model and fine-tuned via **reinforcement fine-tuning (RFT)**. It achieves state-of-the-art performance on UI grounding and navigation benchmarks—e.g., Screenspot-V2/Pro (up to 95.3% / 61.9%) and AndroidWorld navigation (up to 65.9%)—by leveraging carefully crafted reward functions, efficient data cleaning pipelines, and a novel **self-evolving framework** (trajectory alignment and sparse action enhancement) to enhance reasoning coherence and handle rare actions. The code and checkpoints are open-sourced to encourage further development.

- [Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training](https://arxiv.org/abs/2508.00414)
    - Tianqing Fang, Zhisong Zhang, Xiaoyang Wang, Rui Wang, Can Qin, Yuxuan Wan, Jun-Yu Ma, Ce Zhang, Jiaqi Chen, Xiyun Li, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: Tencent AI Lab
    - 📅 Date: August 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [dataset], [model], [deep research], [reflection], [voting], [agent foundation models]
    - 📖 TLDR: This work introduces **Cognitive Kernel-Pro**, a fully open-source, multi-module agent framework designed to democratize advanced AI agent development. It curates high-quality training data across four domains—web, files, code, and general reasoning—and introduces test-time strategies like reflection and voting to enhance robustness. Evaluated on the GAIA benchmark, its open 8B-parameter model outperforms previous open-source agents such as WebDancer and WebSailor, setting a new performance standard. Code is publicly available.

- [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://arxiv.org/abs/2506.08012)
    - Penghao Wu, Shengnan Ma, Bo Wang, Jiaheng Yu, Lewei Lu, Ziwei Liu
    - 🏛️ Institutions: S-Lab, Nanyang Technological University, SenseTime Research
    - 📅 Date: June 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [model], [benchmark], [self-reflection], [GUI‑Reflection task suite]
    - 📖 TLDR: Introduces **GUI‑Reflection**, a framework that enhances multimodal GUI agents with self-reflection and error correction. It spans three training stages—pre‑training with reflection tasks, offline supervised fine‑tuning with autogenerated error scenarios, and online iterative reflection tuning—resulting in improved robustness on AndroidWorld and the novel GUI‑Reflection Task Suite using entirely automated pipelines.

- [AgentCPM‑GUI: Building Mobile‑Use Agents with Reinforcement Fine‑Tuning](https://aclanthology.org/2025.emnlp-demos.12/)
    - Zhong Zhang, Yaxi Lu, Yikun Fu, Yupeng Huo, Shenzhi Yang, Yesai Wu, Han Si, Xin Cong, Haotian Chen, Yankai Lin, Jie Xie, Wei Zhou, Wang Xu, Yuanheng Zhang, Zhou Su, Zhongwu Zhai, Xiaoming Liu, Yudong Mei, Jianming Xu, Hongyan Tian, Chongyi Wang, Chi Chen, Yuan Yao, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Tsinghua University, Renmin University of China, ModelBest
    - 📅 Date: June 02, 2025
    - 📑 Publisher: EMNLP 2025 System Demonstrations
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [dataset], [benchmark], [reinforcement fine‑tuning], [compact action space], [CAGUI], [GRPO]
    - 📖 TLDR: Introduces an 8 B Vision–Language GUI agent for on‑device mobile app interaction. Training uses grounding pre-training, supervised fine‑tuning on 55 K Chinese & English trajectories, and reinforcement fine‑tuning (GRPO). A compact JSON action schema enables low-latency inference. Achieves SOTA on five benchmarks including the new Chinese CAGUI (96 %+ TM, 91 % EM). All code, model, and data released.

- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277)
    - Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
    - 🏛️ Institutions: Yonsei University, Carnegie Mellon University
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [reward model], [benchmark], [WebRewardBench], [web-shepherd]
    - 📖 TLDR: Introduces the first process reward model specialized for web navigation, together with a 40K-pair step-level preference dataset and a benchmark for meta-evaluating web-agent reward models. Web-Shepherd substantially outperforms generic frontier-model verifiers on web trajectories while costing far less, making it practical for both RL and test-time verification.

- [WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](https://arxiv.org/abs/2504.11788)
    - Zhisong Zhang, Tianqing Fang, Kaixin Ma, Wenhao Yu, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: City University of Hong Kong, Tencent AI Lab
    - 📅 Date: April 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [planning], [benchmark], [model], [reasoning]
    - 📖 TLDR: WebRollback introduces an explicit rollback mechanism for web agents that allows them to revert to previous states in their navigation trajectory when they encounter errors, replacing the typical greedy one-way search strategy. Evaluated on Mind2Web-Live and WebVoyager benchmarks under both zero-shot and fine-tuning settings, the approach demonstrates improved effectiveness and efficiency in live web navigation tasks.

- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University, Microsoft
    - 📅 Date: April 09, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [model], [benchmark], [learning], [reasoning], [planning], [ASI], [WebArena]
    - 📖 TLDR: Proposes Agent Skill Induction (ASI), which induces executable program skills from web interaction experience and reuses them online as tasks evolve. Program-based skills make verification possible during induction, improving both WebArena success rate and step efficiency over static agents and text-skill alternatives while also transferring better across websites.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Microsoft Research, Nanyang Technological University, Institute for AI Industry Research (AIR), Tsinghua University, Hong Kong University of Science and Technology
    - 📅 Date: March 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [benchmark], [v-droid], [verifier-driven], [pair-wise preference training], [human-agent joint annotation], [low-latency]
    - 📖 TLDR: V-Droid is a verifier-driven mobile GUI agent that uses LLMs to score candidate actions before execution rather than generating actions autoregressively. It combines a discretized action space, prefilling-only inference, pair-wise preference training, and human-agent joint annotation, yielding strong AndroidWorld, AndroidLab, and MobileAgentBench performance with much lower latency.

- [STEVE: A Step Verification Pipeline for Computer-use Agent Training](https://arxiv.org/abs/2503.12532)
    - Fanbin Lu, Zhisheng Zhong, Ziqin Wei, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: The Chinese University of Hong Kong, SmartMore, Hong Kong University of Science and Technology
    - 📅 Date: March 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [model], [UI grounding], [KTO], [GPT-4o], [WinAgentArena]
    - 📖 TLDR: Uses step-level verification rather than expensive gold trajectories to train desktop computer-use agents at scale. STEVE collects trajectories from suboptimal agents, labels each step with GPT-4o by comparing pre/post screenshots, and then optimizes the policy with KTO, producing a 7B agent that beats supervised fine-tuning on WinAgentArena.

- [Magma: A Foundation Model for Multimodal AI Agents](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html)
    - Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai, Seonghyeon Ye, Joel Jang, Yuquan Deng, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research, University of Maryland, University of Wisconsin-Madison, KAIST, University of Washington
    - 📅 Date: February 18, 2025
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [SoM], [ToM], [robotics], [UI navigation]
    - 📖 TLDR: This paper introduces **Magma**, a foundation model designed for multimodal AI agents operating in both digital and physical environments. Magma extends traditional vision-language models by incorporating planning and action capabilities, enabling tasks from UI navigation to robotic manipulation. The model is pretrained on diverse datasets, including images, videos, and robotics data, utilizing **Set-of-Mark (SoM)** for action grounding and **Trace-of-Mark (ToM)** for action planning. Experiments demonstrate that SoM and ToM synergistically enhance Magma's spatial-temporal intelligence, achieving state-of-the-art performance in UI navigation and robotic manipulation tasks.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, University College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [lightweight VLM], [on-device control], [AndroidControl], [AndroidWorld], [AppVLM]
    - 📖 TLDR: AppVLM is a lightweight mobile-control VLM that is first fine-tuned offline on AndroidControl and then refined with data collected from AndroidWorld. It reaches state-of-the-art offline action prediction and matches GPT-4o on online AndroidWorld success rate while running up to 10x faster.

- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)
    - Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng, Xin Liu, Guang Shi
    - 🏛️ Institutions: ByteDance Seed, Tsinghua University
    - 📅 Date: January 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [action modeling], [system-2 reasoning], [reflective online traces], [UI-TARS]
    - 📖 TLDR: UI-TARS is an end-to-end native GUI agent model that operates directly from screenshots rather than wrapping a commercial foundation model with handcrafted prompting workflows. It combines enhanced GUI perception, unified cross-platform action modeling, deliberate multi-step reasoning, and iterative training on reflective online traces, and reports strong results across more than ten GUI-agent benchmarks.

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research, Alibaba Group, Australian National University, Independent Researcher
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [pure vision], [instruction synthesis], [context-aware grounding], [Aria-UI]
    - 📖 TLDR: Aria-UI is a GUI-grounding model that deliberately avoids HTML or AXTree inputs and instead works from pure visual observations. It pairs a scalable instruction-synthesis pipeline with interleaved textual and text-image action histories for context-aware grounding, and reports state-of-the-art results across offline and online grounding benchmarks.

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

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [UI-guided visual token selection], [interleaved vision-language-action streaming], [screenshot grounding], [ShowUI]
    - 📖 TLDR: ShowUI is a lightweight vision-language-action model for GUI visual agents that focuses on efficient screenshot perception and action-history modeling. It introduces UI-guided visual token selection and interleaved vision-language-action streaming, reaching 75.1% zero-shot screenshot-grounding accuracy while remaining competitive on web and mobile GUI tasks.

- [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform training], [OS-Atlas]
    - 📖 TLDR: Introduces OS-Atlas, an open foundation action model for GUI agents built on a cross-platform synthetic grounding toolkit and a corpus of more than 13 million GUI elements. The model improves GUI grounding and out-of-distribution agent performance across mobile, desktop, and web benchmarks.

- [AutoGLM: Autonomous Foundation Agents for GUIs](https://arxiv.org/abs/2411.00820)
    - Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long Iong, Jiadai Sun, Jiaqi Wang, Junjie Gao, Junjun Shan, Kangning Liu, Shudan Zhang, Shuntian Yao, Siyi Cheng, Wentao Yao, Wenyi Zhao, Xinghan Liu, Xinyi Liu, Xinying Chen, Xinyue Yang, Yang Yang, Yifan Xu, Yu Yang, Yujia Wang, Yulin Xu, Zehan Qi, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu AI, Tsinghua University
    - 📅 Date: October 28, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [model], [foundation agent], [intermediate interface], [progressive reinforcement learning], [AutoGLM]
    - 📖 TLDR: Introduces AutoGLM as a foundation-agent family for GUI control, focusing on browser and Android scenarios. The paper argues for separating planning from grounding through an intermediate interface and pairs that design with progressive self-evolving reinforcement learning to improve real-world performance.

- [TinyClick: Single-Turn Agent for Empowering GUI Automation](https://www.isca-archive.org/interspeech_2025/pawlowski25_interspeech.html)
    - Pawel Pawlowski, Krystian Zawistowski, Wojciech Lapacz, Adam Wiacek, Marcin Skorupa, Sebastien Postansque, Jakub Hoscilowicz
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 09, 2024
    - 📑 Publisher: INTERSPEECH 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI grounding], [single-turn agent], [on-device model], [ScreenSpot], [OmniAct], [TinyClick]
    - 📖 TLDR: TinyClick is a compact, single-turn agent designed to automate GUI tasks by precisely locating screen elements via the Vision-Language Model Florence-2-Base. Trained with multi-task strategies and MLLM-based data augmentation, TinyClick achieves high accuracy on Screenspot and OmniAct, outperforming specialized GUI interaction models and general MLLMs like GPT-4V. The model's lightweight design (0.27B parameters) ensures fast processing and minimal latency, making it efficient for real-world applications on multiple platforms.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0faa4bc5f522076947a030273629d4fe-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: October 07, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform generalization], [UGround], [synthetic data]
    - 📖 TLDR: Introduces UGround, a universal visual grounding model for GUI agents trained on a 10M-element synthetic dataset spanning 1.3M screenshots. The paper shows that a vision-only grounding module can generalize across desktop, mobile, and web interfaces and can match or exceed agents that rely on extra textual inputs.

- [MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a2c3c86679300047c740c9900f19ddac-Abstract-Conference.html)
    - Haotian Zhang, Mingfei Gao, Zhe Gan, Philipp Dufter, Nina Wenzel, Forrest Huang, Dhruti Shah, Xianzhi Du, Bowen Zhang, Yanghao Li, Sam Dodge, Keen You, Zhen Yang, Aleksei Timofeev, Mingze Xu, Hong-You Chen, Jean-Philippe Fauconnier, Zhengfeng Lai, Haoxuan You, Zirui Wang, Afshin Dehghan, Peter Grasch, Yinfei Yang
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Misc]
    - 🔑 Key: [model], [MM1.5], [vision language model], [visual grounding], [reasoning], [data-centric], [analysis]
    - 📖 TLDR: This paper introduces MM1.5, a family of multimodal large language models (MLLMs) ranging from 1B to 30B parameters, including dense and mixture-of-experts variants. MM1.5 enhances capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning. The authors employ a data-centric training approach, utilizing high-quality OCR data and synthetic captions for continual pre-training, alongside an optimized visual instruction-tuning data mixture for supervised fine-tuning. Specialized variants, MM1.5-Video and MM1.5-UI, are designed for video understanding and mobile UI comprehension, respectively. Extensive empirical studies provide insights into the training processes, offering guidance for future MLLM development.

- [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://aclanthology.org/2024.findings-emnlp.599/)
    - Qinzhuo Wu, Weikai Xu, Wei Liu, Tao Tan, Jianfeng Liu, Ang Li, Jian Luan, Bin Wang, Shuo Shang
    - 🏛️ Institutions: Xiaomi AI Lab, University of Electronic Science and Technology of China, Renmin University of China
    - 📅 Date: September 23, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [MobileVLM], [Mobile3M], [UI understanding]
    - 📖 TLDR: This paper introduces *MobileVLM*, a vision-language model designed to enhance both intra- and inter-UI understanding for mobile applications. The authors propose two additional pre-training stages with four specific UI-based tasks to improve the model's perception of fine-grained elements and capture page transition actions. To support this, they constructed *Mobile3M*, a large-scale Chinese mobile dataset comprising 3 million UI pages and real-world transition actions, organized into directed graphs. Experimental results demonstrate that MobileVLM outperforms existing vision-language models on both in-house test sets and public mobile benchmarks.

- [CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://aclanthology.org/2024.findings-acl.539)
    - Xinbei Ma, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: August 31, 2024
    - 📑 Publisher: Findings of ACL 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [smartphone automation], [comprehensive environment perception], [conditional action prediction], [CoCo-Agent]
    - 📖 TLDR: Presents CoCo-Agent, a smartphone GUI agent built around comprehensive environment perception and conditional action prediction. The paper reports strong gains on mobile GUI automation benchmarks such as AITW and META-GUI, showing that richer environment modeling improves action selection.

- [MobileFlow: A Multimodal LLM For Mobile GUI Agent](https://arxiv.org/abs/2407.04346)
    - Songqin Nong, Jiali Zhu, Rui Wu, Jiongchao Jin, Shuo Shan, Xiutian Huang, Wenhao Xu
    - 🏛️ Institutions: Ant Group
    - 📅 Date: July 05, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [hybrid visual encoder], [multilingual GUI], [MobileFlow]
    - 📖 TLDR: This paper introduces *MobileFlow*, a multimodal large language model tailored for mobile GUI agents. With approximately 21 billion parameters and hybrid visual encoders, it supports variable image resolutions and multilingual GUIs, enhancing the model's ability to interpret image data and comprehend user instructions for GUI interaction tasks.

- [Octo-planner: On-device Language Model for Planner-Action Agents](https://arxiv.org/abs/2406.18082)
    - Nexa AI Team
    - 🏛️ Institutions: Nexa AI
    - 📅 Date: June 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [model], [planner-action framework], [Octo-planner], [on-device planning]
    - 📖 TLDR: Presents Octo-planner, an on-device planner for a planner-action agent framework that separates task decomposition from action execution. Built on Phi-3 Mini and paired with an Octopus action model, it targets low-latency planning and execution on resource-constrained devices.

- [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://aclanthology.org/2024.findings-emnlp.68/)
    - Ziyang Meng, Yu Dai, Zezheng Gong, Shaoxiong Guo, Minglong Tang, Tongquan Wei
    - 🏛️ Institutions: East China Normal University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [GUI VQA], [hallucination mitigation], [FAC], [referent method], [VGA]
    - 📖 TLDR: Introduces VGA, a GUI-understanding model trained to reduce hallucinations caused by over-reliance on textual priors instead of on-screen evidence. The paper builds a 63.8K GUI VQA dataset with a referent-based construction method and uses a two-stage FAC fine-tuning procedure to improve visually grounded answers.

- [Octopus v3: Technical Report for On-device Sub-billion Multimodal AI Agent](https://arxiv.org/abs/2404.11459)
    - Wei Chen, Zhiyuan Li
    - 🏛️ Institutions: Stanford University
    - 📅 Date: April 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [functional tokens], [on-device agent], [edge deployment], [Octopus v3]
    - 📖 TLDR: Presents Octopus v3, a sub-billion multimodal agent model aimed at on-device deployment on hardware as small as a Raspberry Pi. Its core idea is to introduce functional tokens that map multimodal inputs into action-oriented representations for agent tasks.

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://eccv.ecva.net/virtual/2024/poster/749)
    - Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeff Nichols, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: April 08, 2024
    - 📑 Publisher: ECCV 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [benchmark], [grounding], [reasoning], [mobile UI understanding], [ferret-UI]
    - 📖 TLDR: This paper presents **Ferret-UI**, a multimodal large language model (MLLM) designed to understand and interact with mobile user interfaces. The model incorporates advanced capabilities for referring, grounding, and reasoning about UI elements. By training on a variety of UI tasks, Ferret-UI achieves high performance in tasks such as icon recognition and text extraction. The authors introduce a unique architecture that allows for improved visual feature extraction from mobile screens, paving the way for applications in accessibility and user interaction.

- [Improving Language Understanding from Screenshots](https://arxiv.org/abs/2402.14073)
    - Tianyu Gao, Zirui Wang, Adithya Bhaskar, Danqi Chen
    - 🏛️ Institutions: Princeton Language and Intelligence (PLI), Princeton University
    - 📅 Date: February 21, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [screenshot language model], [PTP], [pretraining objective], [multimodal language understanding]
    - 📖 TLDR: Studies how to make screenshot language models better at text-heavy understanding by pretraining them with a patch-and-text prediction objective that reconstructs both image regions and embedded text. The resulting models close much of the gap to text-only baselines on GLUE-style tasks and also improve autoregressive screenshot language modeling.

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

- [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7ef7d8359036afd8c2378d82c21058a4-Abstract-Conference.html)
    - Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu, Izzeddin Gur
    - 🏛️ Institutions: The University of Tokyo, Google DeepMind
    - 📅 Date: January 01, 2024
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [offline training], [WebGUM], [demonstration learning], [MiniWoB], [WebShop], [Mind2Web]
    - 📖 TLDR: Trains an instruction-following multimodal web agent offline from a large demonstration corpus using both screenshots and HTML as input. WebGUM substantially improves grounded perception and multi-step reasoning, outperforming prior offline methods on MiniWoB, beating PaLM-540B on WebShop, and transferring positively to Mind2Web.

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

- [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://proceedings.mlr.press/v202/lee23g.html)
    - Kenton Lee, Mandar Joshi, Iulia Raluca Turc, Hexiang Hu, Fangyu Liu, Julian Martin Eisenschlos, Urvashi Khandelwal, Peter Shaw, Ming-Wei Chang, Kristina Toutanova
    - 🏛️ Institutions: Google
    - 📅 Date: February 01, 2023
    - 📑 Publisher: ICML 2023
    - 💻 Env: [Web]
    - 🔑 Key: [model], [pretraining], [screenshot parsing], [image-to-text], [Pix2Struct]
    - 📖 TLDR: Presents Pix2Struct, an image-to-text model pretrained by reconstructing simplified HTML from masked webpage screenshots. The paper positions screenshot parsing as a unified pretraining task for visually situated language and shows strong transfer across document, illustration, and UI understanding tasks.

- [Spotlight: Mobile UI Understanding using Vision-Language Models with a Focus](https://proceedings.iclr.cc/paper_files/paper/2023/hash/0f4145fde6f5ae66745ef2a16bd1a7cd-Abstract-Conference.html)
    - Gang Li, Yang Li
    - 🏛️ Institutions: Google Research
    - 📅 Date: September 29, 2022
    - 📑 Publisher: ICLR 2023 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [region-based focus], [mobile UI understanding], [Spotlight]
    - 📖 TLDR: Presents Spotlight, a vision-language model for mobile UI understanding that uses screenshots plus a user-specified focus region instead of relying on view hierarchy metadata. The paper targets multiple UI tasks, including captioning, summarization, grounding, and tappability prediction, under a unified visual-only setup.

- [Screen2Words: Automatic Mobile UI Summarization with Multimodal Learning](https://dl.acm.org/doi/10.1145/3472749.3474765)
    - Bryan Wang, Gang Li, Xin Zhou, Zhourong Chen, Tovi Grossman, Yang Li
    - 🏛️ Institutions: University of Toronto
    - 📅 Date: August 06, 2021
    - 📑 Publisher: UIST 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [mobile UI summarization], [multimodal learning], [Screen2Words]
    - 📖 TLDR: Introduces Screen2Words, a dataset and model for generating high-level natural-language summaries of mobile screens. The paper is important because it turns UI understanding into screen-level semantic summarization rather than only element-level labeling.

- [UIBert: Learning Generic Multimodal Representations for UI Understanding](https://www.ijcai.org/proceedings/2021/235)
    - Chongyang Bai, Xiaoxue Zang, Ying Xu, Srinivas Sunkara, Abhinav Rastogi, Jindong Chen, Blaise Agüera y Arcas
    - 🏛️ Institutions: Google Research
    - 📅 Date: July 29, 2021
    - 📑 Publisher: IJCAI 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [pretraining], [multimodal representation learning], [view hierarchy], [UIBert]
    - 📖 TLDR: Introduces UIBert, a transformer model for UI understanding that jointly models screenshots, text, and structural metadata such as the Android view hierarchy. The paper proposes five UI-specific pretraining tasks built around self-alignment between modalities and reports gains on nine downstream UI tasks.

- [Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements](https://aclanthology.org/2020.emnlp-main.443/)
    - Yang Li, Gang Li, Luheng He, Jingjie Zheng, Hong Li, Zhiwei Guan
    - 🏛️ Institutions: Google Research, Georgia Institute of Technology
    - 📅 Date: November 30, 2020
    - 📑 Publisher: EMNLP 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [model], [accessibility], [natural language generation], [WidgetCaption]
    - 📖 TLDR: Introduces widget captioning as the task of generating accessibility-oriented natural-language descriptions for mobile UI elements. The paper contributes a large captioned dataset and frames element description as a core building block for accessible mobile assistants.
