# Yuanchun Li's Papers

- [Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training](https://arxiv.org/abs/2601.22781)
    - Linjia Kang, Zhimin Wang, Yongkang Zhang, Yuanchun Li, Gang Yin
    - 🏛️ Institutions: Tsinghua University, Huazhong Agricultural University, Kuaishou Technology
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: Mobile GUI Agent, Data Generation, Curriculum Learning, Multi-Agent, VLM, Training Data
    - 📖 TLDR: MobileGen is an adaptive data generation framework for mobile GUI agent training that decouples task difficulty into structural and semantic dimensions, profiles the agent's capability frontier, and uses a multi-agent controllable generator to synthesize difficulty-aligned interaction trajectories, improving average agent performance by 1.57x over baselines across multiple benchmarks.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence Renmin University of China, MiLM Plus Xiaomi Inc., Institute for AI Industry Research Tsinghua University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile GUI agent], [multi-path evaluation], [ambiguous instruction], [noisy environment], [SMAN-Bench]
    - 📖 TLDR: This paper introduces SMAN-Bench, a mobile-agent benchmark that moves beyond single golden trajectories by evaluating single-path, multi-path, ambiguous, and noisy task settings in one framework. It builds instructions from an existing graph-structured mobile corpus, adds offline multi-path reward evaluation, and explicitly includes noisy pop-up-heavy environments plus clarification-style ambiguous tasks. The benchmark is designed to better reflect realistic mobile-agent deployment conditions than cleaner or purely online settings.

- [Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?](https://arxiv.org/abs/2601.12349)
    - Chenhao Lin, Zichen Ding, Lingming Zhang, Yuanchun Li, Xuanzhe Liu
    - 🏛️ Institutions: Nanjing University, Honor Device Co. Ltd, Institute of Dataspace Hefei Comprehensive National Science Center
    - 📅 Date: January 07, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: Security, Attack, Android, Mobile, Benchmark, LMM
    - 📖 TLDR: This paper presents "Action Rebinding," a zero-permission attack that exploits the observation-to-action gap in LMM-powered Android GUI agents to hijack their actions, achieving 100% success on atomic rebinding across six agents and 15 tasks while evading all malware scanners, revealing a fundamental architectural flaw in current agent-OS integration.

- [GUITester: Enabling GUI Agents for Exploratory Defect Discovery](https://arxiv.org/abs/2601.04500)
    - Yixuan Yue, Yiming Liu, Tao Xie, Yuanchun Li, Xuanzhe Liu
    - 🏛️ Institutions: Beijing Jiaotong University, Hithink Research, Nanyang Technological University
    - 📅 Date: December 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: GUI Testing, Mobile, Multi-Agent, Benchmark, Defect Detection, MLLM
    - 📖 TLDR: GUITester is a multi-agent framework that enables MLLM-based GUI agents to autonomously discover defects in mobile apps by decoupling navigation from verification through a Planning-Execution Module and a Hierarchical Reflection Module, achieving 48.90% F1-score on the newly introduced GUITestBench benchmark with 143 tasks across 26 defects.

- [ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration](https://arxiv.org/abs/2509.21823)
    - Gaole Dai, Shiqi Jiang, Yuanchun Li, Ting Cao, Rui Tan, Mo Li, Yuqing Yang, Lili Qiu
    - 🏛️ Institutions: Nanyang Technological University, Microsoft Research, Institute for AI Industry Research, Tsinghua University, The Hong Kong University of Science and Technology
    - 📅 Date: September 26, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reward system], [GUI agent], [agentic evaluation], [state probing], [ProRe]
    - 📖 TLDR: This paper introduces ProRe, a proactive reward system for GUI agents that combines a general-purpose reasoner with domain-specific evaluator agents that actively probe the environment before assigning rewards. Instead of judging trajectories statically, ProRe gathers additional observations through targeted interaction, which makes reward assignment more verifiable and accurate. Across more than 3,000 trajectories, it improves reward accuracy and F1, and it also boosts downstream GUI-agent task success when used for policy training.

- [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, Renmin University of China, Xiaomi, Tsinghua University
    - 📅 Date: 2025-05-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: Benchmark, Mobile, Evaluation, Dataset, GUI Testing, Multimodal
    - 📖 TLDR: Mobile-Bench-v2 is a more realistic benchmark for VLM-based mobile agents that introduces multi-path offline evaluation, noisy environments with pop-ups and ads, and ambiguous instruction splits to test proactive interaction capabilities, addressing key limitations of existing mobile agent benchmarks.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Tsinghua University, Nanyang Technological University, The University of Texas at Austin
    - 📅 Date: March 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [benchmark], [V-Droid], [verifier-driven], [pair-wise preference training], [human-agent joint annotation], [low-latency]
    - 📖 TLDR: This paper introduces **V-Droid**, a mobile GUI automation agent that leverages large language models (LLMs) as verifiers rather than generators. By evaluating candidate actions before execution, V-Droid enhances decision-making accuracy and reduces latency. The framework incorporates discretized action space construction, a prefilling-only workflow, pair-wise preference training, and a scalable human-agent joint annotation scheme. Evaluated on benchmarks like AndroidWorld, AndroidLab, and MobileAgentBench, V-Droid achieves state-of-the-art success rates and operates with near-real-time decision-making capabilities.

- [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337)
    - Longxi Gao, Li Zhang, Shihe Wang, Pengzhi Gao, Wei Liu, Jian Luan, Shangguang Wang, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: dataset, mobile, Android, GUI grounding, data collection, benchmark
    - 📖 TLDR: MobileViews is a million-scale mobile GUI dataset comprising over 1.2 million screenshot-view hierarchy pairs from 30K+ Android apps, collected via an automated VLM-enhanced traversal framework on mobile SoC clusters, which improves GUI grounding accuracy by up to 6.1% when used to train visual language models.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Automation Task Evaluation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: April 12, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [UI automation], [mobile agent evaluation]
    - 📖 TLDR: LlamaTouch is an evaluation testbed designed for mobile UI automation, enabling reliable task assessment across 495 annotated tasks. It provides a scalable solution to evaluate agents in real-world mobile settings, comparing agent actions to essential UI states for accurate task completion. LlamaTouch supports dynamic environments, advancing mobile agent reliability and scalability in task automation.

- [AutoDroid: LLM-powered Task Automation in Android](https://doi.org/10.1145/3636534.3649379)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - 🏛️ Institutions: Tsinghua University, Shanghai AI Laboratory, University of Notre Dame, Microsoft Research
    - 📅 Date: August 29, 2023
    - 📑 Publisher: MobiCom 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [Android task automation], [LLM-powered agent]
    - 📖 TLDR: This paper introduces AutoDroid, a novel mobile task automation system capable of handling arbitrary tasks on any Android application without manual efforts. The framework combines the commonsense knowledge of LLMs with domain-specific knowledge of apps through automated dynamic analysis. AutoDroid features a functionality-aware UI representation method, exploration-based memory injection techniques, and a multi-granularity query optimization module. Evaluated on a new benchmark with 158 common tasks, AutoDroid achieves a 90.9% action generation accuracy and a 71.3% task completion rate, significantly outperforming GPT-4-powered baselines.
