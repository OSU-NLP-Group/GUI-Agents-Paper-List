# Wei Liu's Papers

- [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)
    - Xiao Liu, Ziyang Luo, Jiawei Liu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web], [GUI]
    - 🔑 Key: [framework]
    - 📖 TLDR: An automated closed-loop RL pipeline that systematically compresses LLM knowledge into grounded web agent actions through scalable environment synthesis and knowledge-aware task generation.

- [WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces](https://arxiv.org/abs/2603.05295)
    - Xiao Liu, Ziyang Luo, Jiawei Liu, Kaizhe Hu, Yeye He
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web], [GUI]
    - 🔑 Key: [dataset]
    - 📖 TLDR: The largest open-source dataset of human-annotated web trajectories with 31,725 sequences and 318k steps featuring multi-modal visual, structural, and action alignment.

- [Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855)
    - Haiyang Xu, Xi Zhang, Haowei Liu, Junyang Wang, Zhaozai Zhu, Shengjie Zhou, Xuhao Hu, Feiyu Gao, Junjie Cao, Zihua Wang, Zhiyuan Chen, Jitong Liao, Qi Zheng, Jiahui Zeng, Ze Xu, Shuai Bai, Junyang Lin, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: February 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [multi-platform], [MCP], [memory], [GUI-Owl-1.5], [Mobile-Agent-v3.5]
    - 📖 TLDR: This paper introduces Mobile-Agent-v3.5, a family of native multi-platform GUI agents centered on the GUI-Owl-1.5 models, with support for desktop, mobile, browser, and tool-calling settings. The work combines a hybrid data flywheel, unified capability enhancement for reasoning, MCP/tool use, memory, and multi-agent adaptation, and a new multi-platform RL algorithm called MRPO. It reports strong open-source results across more than 20 GUI benchmarks, including OSWorld, AndroidWorld, WebArena, ScreenSpotPro, OSWorld-MCP, MobileWorld, and GUI-Knowledge Bench.

- [Where Not to Learn: Prior-Aligned Training with Subset-based Attribution Constraints for Reliable Decision-Making](https://arxiv.org/abs/2602.07008)
    - Ruoyu Chen, Shangquan Sun, Xiaoqing Guo, Chen Lin, Ziwei Liu
    - 🏛️ Institutions: Unknown
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework]
    - 📖 TLDR: An attribution-based training method aligning MLLM models with human priors by constraining learned representations to match human perception patterns for reliability.

- [Continual GUI Agents](https://arxiv.org/abs/2601.20732)
    - Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng
    - 🏛️ Institutions: Tsinghua University, Zhejiang University, ETH Zurich, Beijing University of Posts and Telecommunications
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [continual learning], [reinforcement learning], [GUI grounding], [domain shift], [GUI-AiF], [Continual GUI Agents]
    - 📖 TLDR: This paper introduces Continual GUI Agents as a continual learning setting where GUI agents must adapt to domain and resolution shifts over time without losing stable grounding. It proposes GUI-AiF, a reinforcement fine-tuning framework with anchoring-point and anchoring-region rewards that keep agents aligned to changing interaction targets instead of overfitting to static cues. Experiments show the method outperforms prior baselines and frames continual adaptation as a core systems challenge for GUI agents.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence Renmin University of China, MiLM Plus Xiaomi Inc., Institute for AI Industry Research Tsinghua University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile GUI agent], [multi-path evaluation], [ambiguous instruction], [noisy environment], [SMAN-Bench]
    - 📖 TLDR: This paper introduces SMAN-Bench, a mobile-agent benchmark that moves beyond single golden trajectories by evaluating single-path, multi-path, ambiguous, and noisy task settings in one framework. It builds instructions from an existing graph-structured mobile corpus, adds offline multi-path reward evaluation, and explicitly includes noisy pop-up-heavy environments plus clarification-style ambiguous tasks. The benchmark is designed to better reflect realistic mobile-agent deployment conditions than cleaner or purely online settings.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Unaffiliated
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [mobile GUI agent], [GUI-Shift]
    - 📖 TLDR: This paper introduces GUI-Shift, a self-supervised reinforcement learning framework for VLM-based GUI agents built around the K-step GUI Transition task, which learns GUI dynamics from unlabeled trajectories without natural-language instruction annotation. The method combines rule-based optimization with data filtering and improves both GUI automation and grounding performance across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro. The paper shows a scalable path to training stronger mobile GUI agents from large amounts of unlabeled interaction data.

- [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)
    - Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, Zhengxi Lu, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: August 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [multi-agent], [GUI automation], [trajectory production], [TRPO]
    - 📖 TLDR: The paper introduces **GUI-Owl**, a foundational multimodal GUI agent model built on Qwen2.5-VL, integrating perception, grounding, reasoning, planning, and action execution into one policy network. GUI-Owl-7B achieves strong baseline performance (66.4 on AndroidWorld, 29.4 on OSWorld). The authors further propose **Mobile-Agent-v3**, a general-purpose, multi-agent GUI automation framework that builds on GUI-Owl and achieves state-of-the-art open-source results (73.3 on AndroidWorld, 37.7 on OSWorld). Core innovations include: a large-scale cross-platform cloud-based environment infrastructure with Self-Evolving GUI Trajectory Production; modular foundational agent capabilities; and scalable, asynchronous reinforcement learning using Trajectory-aware Relative Policy Optimization (TRPO). The framework is open-sourced at the X-PLUG MobileAgent GitHub repository.

- [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://arxiv.org/abs/2506.08012)
    - Penghao Wu, Shengnan Ma, Bo Wang, Jiaheng Yu, Lewei Lu, Ziwei Liu
    - 🏛️ Institutions: Nanyang Technological University, SenseTime Research
    - 📅 Date: June 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [model], [benchmark], [self-reflection], [GUI‑Reflection Task Suite]
    - 📖 TLDR: Introduces **GUI‑Reflection**, a framework that enhances multimodal GUI agents with self-reflection and error correction. It spans three training stages—pre‑training with reflection tasks, offline supervised fine‑tuning with autogenerated error scenarios, and online iterative reflection tuning—resulting in improved robustness on AndroidWorld and the novel GUI‑Reflection Task Suite using entirely automated pipelines.

- [Agent-SAMA: State-Aware Mobile Assistant](https://arxiv.org/abs/2505.23596)
    - Linqiang Guo, Wei Liu, Yi Wen Heng, Tse-Hsun, Chen, Yang Wang
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-29
    - 📑 Publisher: arXiv
    - 💻 Env: [Web], [Desktop], [Mobile], [GUI]
    - 🔑 Key: [model], [state-aware], [finite state machine], [error recovery], [mobile agent]
    - 📖 TLDR: State-aware mobile agent framework modeling app execution as Finite State Machines (FSM) with four specialized agents for planning, verification, and recovery, achieving 84% success and 71.9% recovery rates.

- [MobileIPL: Enhancing Mobile Agents Thinking Process via Iterative Preference Learning](https://arxiv.org/abs/2505.12299)
    - Kun Huang, Weikai Xu, Yuxuan Liu, Quandong Wang, Pengzhi Gao, Wei Liu, Jian Luan, Bin Wang, Bo An
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-18
    - 📑 Publisher: arXiv
    - 💻 Env: [Web], [Desktop], [Mobile], [GUI]
    - 🔑 Key: [model], [preference learning], [chain-of-thought], [DPO], [reasoning]
    - 📖 TLDR: MobileIPL framework enhancing mobile agent reasoning via iterative preference learning with CoaT-trees, rule-based rewards, and Thinking-level DPO pairs, with three-stage instruction evolution for improved generalization.

- [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2025-05-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Web], [Desktop], [Mobile], [GUI]
    - 🔑 Key: [benchmark], [mobile agent], [multi-path evaluation], [realistic scenario], [robustness]
    - 📖 TLDR: Realistic mobile agent benchmark with offline multi-path evaluation, noisy apps (pop-ups/ads) splits, and ambiguous instructions to assess robustness under real-world conditions and noisy environments.

- [ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation](https://aclanthology.org/2025.naacl-long.244/)
    - Qinzhuo Wu, Wei Liu, Jian Luan, Bin Wang
    - 🏛️ Institutions: XiaoMi AI Lab
    - 📅 Date: April 2025
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile GUI agent], [page reaching], [task decomposition], [ReachAgent], [MobileReach]
    - 📖 TLDR: This paper argues that mobile agents often optimize locally for the next UI action while missing the larger GUI flow needed to finish a task. It introduces MobileReach, a dataset that decomposes tasks into page-reaching and page-operation subtasks, and trains ReachAgent as a two-stage framework over those subtasks plus reward-based preference flows. The result is stronger step-level and task-level accuracy than prior mobile-agent baselines.

- [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://aclanthology.org/2024.findings-emnlp.599/)
    - Qinzhuo Wu, Weikai Xu, Wei Liu, Tao Tan, Jianfeng Liu, Ang Li, Jian Luan, Bin Wang, Shuo Shang
    - 🏛️ Institutions: Xiaomi AI Lab, University of Electronic Science and Technology of China, Renmin University of China
    - 📅 Date: September 23, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [MobileVLM], [Mobile3M], [UI understanding]
    - 📖 TLDR: This paper introduces *MobileVLM*, a vision-language model designed to enhance both intra- and inter-UI understanding for mobile applications. The authors propose two additional pre-training stages with four specific UI-based tasks to improve the model's perception of fine-grained elements and capture page transition actions. To support this, they constructed *Mobile3M*, a large-scale Chinese mobile dataset comprising 3 million UI pages and real-world transition actions, organized into directed graphs. Experimental results demonstrate that MobileVLM outperforms existing vision-language models on both in-house test sets and public mobile benchmarks.

- [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337)
    - Longxi Gao, Li Zhang, Shihe Wang, Pengzhi Gao, Wei Liu, Jian Luan, Shangguang Wang, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Unknown
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI], [Mobile]
    - 🔑 Key: [dataset]
    - 📖 TLDR: A million-scale mobile GUI dataset with 1.2M+ screenshot-view hierarchy pairs from 30K Android applications, enabling training of visual language models for mobile agent GUI grounding and interaction.

- [MMInA: Benchmarking Multihop Multimodal Internet Agents](https://aclanthology.org/2025.findings-acl.703/)
    - Shulin Tian, Ziniu Zhang, Liangyu Chen, Ziwei Liu
    - 🏛️ Institutions: Nanyang Technological University
    - 📅 Date: April 15, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [multihop web browsing], [multimodal tasks], [long-range reasoning]
    - 📖 TLDR: The **MMInA** benchmark is designed to evaluate agents' capacity to complete complex, multihop web tasks by navigating and extracting information across evolving real-world websites. Composed of 1,050 tasks across diverse domains, MMInA challenges agents with realistic, multimodal information retrieval and reasoning tasks, such as comparative shopping and travel inquiries. Despite recent advances, agents show difficulties in handling tasks requiring sequential steps across multiple sites, underscoring the need for enhanced multimodal and memory-augmented models.
