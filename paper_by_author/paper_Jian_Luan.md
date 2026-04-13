# Jian Luan's Papers

- [MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment](https://arxiv.org/abs/2601.20335)
    - Qinzhuo Wu, Zhizhuo Yang, Hanhao Li, Pengzhi Gao, Wei Liu, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi, Peking University, CUHK
    - 📅 Date: January 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [chinese benchmark], [long-horizon tasks], [noise robustness], [auto-evaluation], [MobileBench-OL]
    - 📖 TLDR: MobileBench-OL benchmarks mobile GUI agents on 1,080 online tasks from 80 Chinese apps. It extends evaluation beyond instruction following to long-horizon execution, reasoning and exploration, and robustness to real-world noise, and pairs the benchmark with an automatic evaluation pipeline that supports environment reset.

- [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197)
    - Shaokang Wang, Pei Fu, Ruoceng Zhang, Shaojie Zhang, Xiuwen Xi, Jiahui Yang, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [critic model], [test-time scaling], [data flywheel], [Intuitive Critic Model], [GAIA]
    - 📖 TLDR: GAIA trains an Intuitive Critic Model that judges the immediate correctness of candidate GUI actions before execution. It then uses a data flywheel that recycles agent-generated positive and negative action samples to iteratively improve the critic, yielding better test-time performance for both open-source and closed-source GUI agents.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yunxin Liu, Yuanchun Li, Bin Wang, Bo An
    - 🏛️ Institutions: NTU, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence, Renmin University of China, MiLM Plus, Xiaomi, Institute for AI Industry Research, Tsinghua
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [multi-path evaluation], [ambiguous instructions], [noisy environment], [SMAN-Bench]
    - 📖 TLDR: SMAN-Bench evaluates mobile agents under single-path, multi-path, ambiguous, and noisy task settings that are poorly covered by prior benchmarks. It builds these splits from a graph-structured unlabeled mobile corpus, adds offline multi-path reward evaluation, and includes both contaminated noisy environments and preset Q&A interactions for ambiguous instructions.

- [BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent](https://arxiv.org/abs/2509.15566)
    - Shaojie Zhang, Ruoceng Zhang, Pei Fu, Shaokang Wang, Jiahui Yang, Xin Du, Shiqi Cui, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi
    - 📅 Date: September 19, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [blink-think-link], [blink data generation], [BTL Reward], [process-and-outcome reward], [human-GUI interaction], [BTL-UI]
    - 📖 TLDR: BTL-UI models GUI interaction as Blink, Think, and Link phases inspired by human visual attention, planning, and action. It adds a blink-oriented data generation pipeline and a rule-based reward that supervises both process and outcome, and reports competitive results on both static GUI understanding and dynamic interaction benchmarks.

- [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660)
    - Qinzhuo Wu, Pengzhi Gao, Wei Liu, Jian Luan
    - 🏛️ Institutions: MiLM Plus, Xiaomi
    - 📅 Date: May 27, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [error detection], [backtracking], [judgment reward], [BacktrackAgent]
    - 📖 TLDR: BacktrackAgent addresses the lack of error recovery in mobile GUI agents by adding verifier, judger, and reflector modules plus an explicit backtracking mechanism. It also builds training data for judgment and reflection over post-action outcome pages, improving both task success and step accuracy on Mobile3M and Auto-UI.

- [MobileIPL: Enhancing Mobile Agents Thinking Process via Iterative Preference Learning](https://arxiv.org/abs/2505.12299)
    - Kun Huang, Weikai Xu, Yuxuan Liu, Quandong Wang, Pengzhi Gao, Wei Liu, Jian Luan, Bin Wang, Bo An
    - 🏛️ Institutions: XiaoMi AI Lab, NTU, Gaoling School of Artificial Intelligence, Renmin University of China
    - 📅 Date: May 18, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [DPO], [iterative preference learning], [CoAT], [instruction evolution], [MobileIPL]
    - 📖 TLDR: MobileIPL improves the reasoning process of mobile agents by constructing Chain-of-Action-Planning-Thought trees, scoring sampled outcomes with rule-based rewards, and deriving thinking-level DPO preferences. It also adds staged instruction evolution to improve layout understanding and reports state-of-the-art results on standard mobile GUI benchmarks.

- [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493)
    - Longxi Gao, Li Zhang, Pengzhi Gao, Wei Liu, Jian Luan, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications
    - 📅 Date: May 18, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [self-supervised learning], [K-step GUI Transition], [inverse dynamics], [GUI-Shift]
    - 📖 TLDR: GUI-Shift studies how to train GUI agents from unlabeled trajectories instead of expensive instruction annotations. It introduces the K-step GUI Transition inverse-dynamics task and a self-supervised RL pipeline, improving both mobile GUI automation and grounding performance across multiple benchmarks.

- [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: NTU, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence, Renmin University of China, XiaoMi AI Lab, Institute for AI Industry Research (AIR), Tsinghua
    - 📅 Date: May 17, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [multi-path evaluation], [noisy environments], [ambiguous instructions], [Mobile-Bench-v2]
    - 📖 TLDR: Mobile-Bench-v2 is a more realistic mobile-agent benchmark that fixes three weaknesses of earlier evaluation: single-path scoring, unrealistically clean environments, and over-specified instructions. It adds multi-path offline evaluation, noisy app settings with pop-ups and ads, and ambiguous-instruction splits for testing proactive interaction.

- [ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation](https://aclanthology.org/2025.naacl-long.244/)
    - Qinzhuo Wu, Wei Liu, Jian Luan, Bin Wang
    - 🏛️ Institutions: XiaoMi AI Lab
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [page reaching], [page operation], [MobileReach], [ReachAgent]
    - 📖 TLDR: ReachAgent addresses the tendency of mobile agents to optimize for the next local action while ignoring the larger GUI flow. It introduces the MobileReach training dataset, which decomposes tasks into page-reaching and page-operation subtasks, and uses those subtasks together with reward-based preference GUI flows to train a two-stage mobile agent.

- [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://aclanthology.org/2024.findings-emnlp.599/)
    - Qinzhuo Wu, Weikai Xu, Wei Liu, Tao Tan, Jianfeng Liu, Ang Li, Jian Luan, Bin Wang, Shuo Shang
    - 🏛️ Institutions: XiaoMi AI Lab, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence, Renmin University of China
    - 📅 Date: September 23, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [Mobile3M], [intra-UI understanding], [inter-UI understanding], [MobileVLM]
    - 📖 TLDR: MobileVLM is a mobile-focused vision-language model trained with two extra UI-specific pretraining stages designed to improve both intra-UI element understanding and inter-UI transition understanding. The paper also introduces the 3M-page Chinese mobile corpus Mobile3M with real transition-action graphs, and reports stronger performance than prior VLMs on in-house and public mobile benchmarks.

- [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337)
    - Longxi Gao, Li Zhang, Shihe Wang, Pengzhi Gao, Wei Liu, Jian Luan, Shangguang Wang, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [GUI grounding], [data collection], [MobileViews]
    - 📖 TLDR: MobileViews is a mobile GUI dataset with more than 1.2 million screenshot-view hierarchy pairs collected from over 30K Android apps using VLM-enhanced automatic traversal on mobile SoC clusters. The paper shows that training on MobileViews improves GUI grounding accuracy by up to 6.1% on representative mobile grounding benchmarks.
