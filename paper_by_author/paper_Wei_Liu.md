# Wei Liu's Papers

- [MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment](https://arxiv.org/abs/2601.20335)
    - Qinzhuo Wu, Zhizhuo Yang, Hanhao Li, Pengzhi Gao, Wei Liu, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc, Peking University, Chinese University of Hong Kong
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [chinese benchmark], [long-horizon tasks], [noise robustness], [auto-evaluation], [MobileBench-OL]
    - 📖 TLDR: MobileBench-OL benchmarks mobile GUI agents on 1,080 online tasks from 80 Chinese apps. It extends evaluation beyond instruction following to long-horizon execution, reasoning and exploration, and robustness to real-world noise, and pairs the benchmark with an automatic evaluation pipeline that supports environment reset.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yunxin Liu, Yuanchun Li, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence, Renmin University of China, MiLM Plus, Xiaomi Inc., Institute for AI Industry Research, Tsinghua University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [multi-path evaluation], [ambiguous instructions], [noisy environment], [SMAN-Bench]
    - 📖 TLDR: SMAN-Bench evaluates mobile agents under single-path, multi-path, ambiguous, and noisy task settings that are poorly covered by prior benchmarks. It builds these splits from a graph-structured unlabeled mobile corpus, adds offline multi-path reward evaluation, and includes both contaminated noisy environments and preset Q&A interactions for ambiguous instructions.

- [Agent-SAMA: State-Aware Mobile Assistant](https://arxiv.org/abs/2505.23596)
    - Linqiang Guo, Wei Liu, Yi Wen Heng, Tse-Hsun, Chen, Yang Wang
    - 🏛️ Institutions: Software PErformance, Analysis, and Reliability (SPEAR) lab, Concordia University, Concordia University
    - 📅 Date: May 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [multi-agent framework], [finite state machine], [error recovery], [Android], [benchmark]
    - 📖 TLDR: Agent-SAMA is a state-aware multi-agent framework that models mobile app execution as a Finite State Machine (FSM), using four specialized agents to collaboratively construct FSMs in real time for task planning, execution verification, and error recovery, achieving up to 84% task success rate and 71.9% recovery rate on cross-app benchmarks.

- [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660)
    - Qinzhuo Wu, Pengzhi Gao, Wei Liu, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi Inc
    - 📅 Date: May 27, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [error detection], [backtracking], [Mobile3M], [Auto‑UI]
    - 📖 TLDR: BacktrackAgent introduces a novel GUI‑agent framework that embeds four components—generator, verifier, judger, and reflector—to detect when actions go wrong, evaluate their effects, and backtrack to recover. It also constructs specialized datasets for training these “judgment” and “reflection” modules. On Mobile3M and Auto‑UI benchmarks, it boosts task success rate by ~7.6% and step accuracy by ~1.6%, outperforming prior SOTA like MobileVLM and ReachAgent.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications
    - 📅 Date: May 18, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [self-supervised learning], [GUI grounding], [GUI-shift]
    - 📖 TLDR: Learns GUI dynamics from unlabeled trajectories through a self-supervised inverse-dynamics task called K-step GUI Transition, avoiding dependence on natural-language annotations. Built on top of that task, GUI-Shift combines rule-based optimization with data filtering and improves both GUI automation and grounding across AndroidControl, GUI Odyssey, ScreenSpot-v2, and ScreenSpot-Pro.

- [MobileIPL: Enhancing Mobile Agents Thinking Process via Iterative Preference Learning](https://arxiv.org/abs/2505.12299)
    - Kun Huang, Weikai Xu, Yuxuan Liu, Quandong Wang, Pengzhi Gao, Wei Liu, Jian Luan, Bin Wang, Bo An
    - 🏛️ Institutions: XiaoMi AI Lab, Nanyang Technological University, Gaoling School of Artificial Intelligence, Renmin University of China
    - 📅 Date: May 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [training], [DPO], [preference learning], [chain-of-thought]
    - 📖 TLDR: MobileIPL proposes an Iterative Preference Learning framework that constructs CoaT-trees via iterative sampling and derives thinking-level DPO pairs with rule-based rewards, combined with a three-stage instruction evolution to prevent SFT overfitting, achieving state-of-the-art performance on three standard mobile GUI agent benchmarks while outperforming models like OS-ATLAS and UI-TARS.

- [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence, Renmin University of China, XiaoMi AI Lab, Institute for AI Industry Research (AIR), Tsinghua University
    - 📅 Date: May 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [evaluation], [dataset], [GUI testing], [multimodal]
    - 📖 TLDR: Mobile-Bench-v2 is a more realistic benchmark for VLM-based mobile agents that introduces multi-path offline evaluation, noisy environments with pop-ups and ads, and ambiguous instruction splits to test proactive interaction capabilities, addressing key limitations of existing mobile agent benchmarks.

- [ReachAgent: Enhancing Mobile Agent via Page Reaching and Page Operation](https://aclanthology.org/2025.naacl-long.244/)
    - Qinzhuo Wu, Wei Liu, Jian Luan, Bin Wang
    - 🏛️ Institutions: XiaoMi AI Lab
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [page reaching], [task decomposition], [ReachAgent], [MobileReach]
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
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [GUI grounding], [data collection], [MobileViews]
    - 📖 TLDR: MobileViews is a million-scale mobile GUI dataset comprising over 1.2 million screenshot-view hierarchy pairs from 30K+ Android apps, collected via an automated VLM-enhanced traversal framework on mobile SoC clusters, which improves GUI grounding accuracy by up to 6.1% when used to train visual language models.
