# Yuanchun Li's Papers

- [Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training](https://arxiv.org/abs/2601.22781)
    - Linjia Kang, Zhimin Wang, Yongkang Zhang, Yuanchun Li, Gang Yin
    - 🏛️ Institutions: Tsinghua University, Huazhong Agricultural University, Kuaishou Technology
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [data generation], [curriculum learning], [multi-agent], [VLM], [training data]
    - 📖 TLDR: MobileGen is an adaptive data generation framework for mobile GUI agent training that decouples task difficulty into structural and semantic dimensions, profiles the agent's capability frontier, and uses a multi-agent controllable generator to synthesize difficulty-aligned interaction trajectories, improving average agent performance by 1.57x over baselines across multiple benchmarks.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence, Renmin University of China, MiLM Plus, Xiaomi Inc., Institute for AI Industry Research, Tsinghua University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [multi-path evaluation], [ambiguous instructions], [noisy environment], [SMAN-Bench]
    - 📖 TLDR: Evaluates mobile agents under four settings that cleaner benchmarks usually miss: single-path, multi-path, ambiguous, and noisy tasks. SMAN-Bench builds these splits from a graph-structured mobile corpus, adds offline multi-path reward evaluation, and includes both pop-up-heavy noisy apps and clarification-style ambiguous tasks to better approximate real deployment conditions.

- [AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management](https://arxiv.org/abs/2512.10371)
    - Shizuo Tian, Hao Wen, Yuxuan Chen, Jiacheng Liu, Shanhui Zhao, Guohong Liu, Ju Ren, Yunxin Liu, Yuanchun Li
    - 🏛️ Institutions: Tsinghua University, Peking University
    - 📅 Date: December 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [context management], [long-horizon task], [Android], [program-guided]
    - 📖 TLDR: AgentProg is a program-guided context management approach for mobile GUI agents that reframes interaction history as a program with variables and control flow, integrating a belief state mechanism inspired by Belief MDP to handle partial observability, achieving state-of-the-art success rates on AndroidWorld and extended long-horizon task benchmarks while baseline methods suffer catastrophic degradation.

- [ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration](https://arxiv.org/abs/2509.21823)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuqing Yang, Yuanchun Li, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Nanyang Technological University, Microsoft Research, Institute for AI Industry Research (AIR), Tsinghua University, Hong Kong University of Science and Technology
    - 📅 Date: September 26, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reward system], [agentic evaluation], [state probing], [ProRe]
    - 📖 TLDR: ProRe is a reward system for GUI agents that replaces purely static trajectory judging with active state probing: a reasoner schedules targeted checks and evaluator agents interact with the environment to collect missing evidence before assigning rewards. This proactive setup improves reward accuracy and F1 on more than 3,000 trajectories and also improves downstream policy performance.

- [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence, Renmin University of China, XiaoMi AI Lab, Institute for AI Industry Research (AIR), Tsinghua University
    - 📅 Date: May 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [evaluation], [dataset], [GUI testing], [multimodal]
    - 📖 TLDR: Mobile-Bench-v2 is a more realistic benchmark for VLM-based mobile agents that introduces multi-path offline evaluation, noisy environments with pop-ups and ads, and ambiguous instruction splits to test proactive interaction capabilities, addressing key limitations of existing mobile agent benchmarks.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Microsoft Research, Nanyang Technological University, Institute for AI Industry Research (AIR), Tsinghua University, Hong Kong University of Science and Technology
    - 📅 Date: March 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [benchmark], [v-droid], [verifier-driven], [pair-wise preference training], [human-agent joint annotation], [low-latency]
    - 📖 TLDR: V-Droid is a verifier-driven mobile GUI agent that uses LLMs to score candidate actions before execution rather than generating actions autoregressively. It combines a discretized action space, prefilling-only inference, pair-wise preference training, and human-agent joint annotation, yielding strong AndroidWorld, AndroidLab, and MobileAgentBench performance with much lower latency.

- [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337)
    - Longxi Gao, Li Zhang, Shihe Wang, Pengzhi Gao, Wei Liu, Jian Luan, Shangguang Wang, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [GUI grounding], [data collection], [MobileViews]
    - 📖 TLDR: MobileViews is a million-scale mobile GUI dataset comprising over 1.2 million screenshot-view hierarchy pairs from 30K+ Android apps, collected via an automated VLM-enhanced traversal framework on mobile SoC clusters, which improves GUI grounding accuracy by up to 6.1% when used to train visual language models.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: April 12, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile UI automation], [evaluation], [state matching], [LlamaTouch]
    - 📖 TLDR: LlamaTouch is a mobile UI task-automation testbed that replaces brittle action-sequence matching with evaluation based on whether an agent traverses manually annotated essential application and system states. It combines on-device execution, fine-grained UI component annotation, and multi-level state matching to deliver more faithful and scalable evaluation across 496 tasks.

- [AutoDroid: LLM-powered Task Automation in Android](https://doi.org/10.1145/3636534.3649379)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - 🏛️ Institutions: Tsinghua University, Shanghai AI Laboratory, University of Notre Dame, Microsoft Research
    - 📅 Date: August 29, 2023
    - 📑 Publisher: MobiCom 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [Android task automation], [dynamic analysis], [memory injection], [AutoDroid]
    - 📖 TLDR: Presents AutoDroid, an Android automation system that combines LLM priors with app-specific knowledge gathered through dynamic analysis. The paper emphasizes functionality-aware UI representations and exploration-driven memory injection so the agent can handle previously unseen apps with less manual setup.
