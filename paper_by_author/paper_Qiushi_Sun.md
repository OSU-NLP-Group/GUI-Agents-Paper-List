# Qiushi Sun's Papers

- [OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models](https://arxiv.org/abs/2512.16295)
    - Zhenyu Wu, Jingjing Xie, Zehao Li, Bowen Yang, Qiushi Sun, Zhaoyang Liu, Zhoumianze Liu, Yu Qiao, Xiangyu Yue, Zun Wang, Zichen Ding
    - 🏛️ Institutions: Shanghai Jiao Tong University, Shanghai AI Laboratory, CUHK MMLab, HKU, HKUST
    - 📅 Date: December 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [critic model], [benchmark], [step-level evaluation], [CP-GRPO], [OS-Critic Bench], [OS-Oracle]
    - 📖 TLDR: OS-Oracle targets step-level action criticism for computer-use agents with a 310k-sample cross-platform training pipeline, a two-stage SFT plus CP-GRPO recipe, and the OS-Critic Bench benchmark. The resulting 7B critic reaches state of the art among open-source VLM critics and improves downstream GUI agents when used as a pre-critic.

- [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221)
    - Zhaoyang Liu, Jingjing Xie, Zichen Ding, Zehao Li, Bowen Yang, Zhenyu Wu, Xuehui Wang, Qiushi Sun, Shi Liu, Weiyun Wang, Shenglong Ye, Qingyun Li, Xuan Dong, Yue Yu, Chenyu Lu, YunXiang Mo, Yao Yan, Zeyue Tian, Xiao Zhang, Yuan Huang, Yiqian Liu, Weijie Su, Gen Luo, Xiangyu Yue, Biqing Qi, Kai Chen, Bowen Zhou, Yu Qiao, Qifeng Chen, Wenhai Wang
    - 🏛️ Institutions: Shanghai AI Laboratory
    - 📅 Date: September 18, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [cross-platform data], [closed-loop data pipeline], [six operating systems], [grounding mode], [reasoned action], [ScaleCUA]
    - 📖 TLDR: ScaleCUA builds an open computer-use dataset across six operating systems and three GUI task families through a closed-loop pipeline that combines automated agents with human experts. Models trained on this corpus support grounding, direct-action, and reasoned-action inference modes and reach strong cross-platform results on WebArena-Lite-v2, OSWorld-G, and MMBench-GUI.

- [CODA: Coordinating the Cerebrum and Cerebellum for a Dual-Brain Computer Use Agent with Decoupled Reinforcement Learning](https://arxiv.org/abs/2508.20096)
    - Zeyi Sun, Yuhang Cao, Jianze Liang, Qiushi Sun, Ziyu Liu, Zhixiong Zhang, Yuhang Zang, Xiaoyi Dong, Kai Chen, Dahua Lin, Jiaqi Wang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Shanghai AI Laboratory, CUHK, HKU
    - 📅 Date: August 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dual-brain architecture], [decoupled GRPO], [planner-executor coordination], [ScienceBoard], [specialization-to-generalization], [CODA]
    - 📖 TLDR: CODA is a trainable planner-executor composition for specialized computer-use tasks, where a generalist planner is paired with a specialist executor and improved through a two-stage specialization-then-generalization pipeline. On ScienceBoard's scientific software tasks, it uses decoupled GRPO to train application-specific planners and then consolidates successful trajectories into a stronger cross-domain planner.

- [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897)
    - Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiachong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu
    - 🏛️ Institutions: HKU, Shanghai AI Laboratory, Fudan University, Peking University, Nanjing University, East China Normal University, Yale University
    - 📅 Date: May 26, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [environment], [scientific workflows], [scientific discovery], [ScienceBoard]
    - 📖 TLDR: ScienceBoard introduces a realistic scientific environment and a 169-task benchmark spanning six domains with integrated professional software and mixed-interface workflows. Evaluations with current multimodal agents reach only about 15% overall success, showing that autonomous scientific assistance remains far from reliable.

- [Breaking the Data Barrier -- Building GUI Agents Through Task Generalization](https://openreview.net/forum?id=QDtORaZt8K)
    - Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, Qiushi Sun, Zhenzhong Lan, Junxian He
    - 🏛️ Institutions: Zhejiang University, Westlake University, Shanghai AI Laboratory, HKU, HKUST
    - 📅 Date: April 14, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [mid-training], [task generalization], [multimodal reasoning], [textual reasoning], [GUIMid]
    - 📖 TLDR: This paper studies whether GUI agents benefit from a dedicated mid-training stage on non-GUI but reasoning-intensive tasks before GUI tuning. Across 11 mid-training tasks, it finds that multimodal and even text-only reasoning data can transfer strongly to downstream GUI performance on WebArena and AndroidWorld, motivating optimized non-GUI mixture design for GUI-agent training.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://aclanthology.org/2025.acl-long.277/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Laboratory, HKU, Johns Hopkins University, Shanghai Jiao Tong University, University of Oxford, HKUST
    - 📅 Date: December 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [trajectory synthesis], [reverse task synthesis], [reward model], [OS-Genesis]
    - 📖 TLDR: OS-Genesis tackles the lack of high-quality GUI trajectories by synthesizing them without preset tasks or human demonstrations. It first explores with step-level interactions, then retrospectively derives tasks and filters the resulting trajectories with a reward model, producing more diverse training data for GUI agents.

- [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Laboratory, Shanghai Jiao Tong University, HKU, MIT
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform corpus], [OS-Atlas]
    - 📖 TLDR: OS-Atlas is a foundation action model for GUI agents built on a multi-platform grounding-data synthesis toolkit and a corpus with more than 13 million GUI elements. It improves GUI grounding and zero-shot out-of-distribution agent performance across desktop, mobile, and web benchmarks.

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Shanghai AI Laboratory, HKU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [multi-agent system], [MetaAgent], [AgentToken], [AgentStore]
    - 📖 TLDR: Proposes AgentStore, a platform for integrating heterogeneous third-party agents into a single computer assistant. Its MetaAgent and AgentToken design lets the system coordinate specialized and generalist capabilities, substantially improving performance on challenging desktop-computing benchmarks such as OSWorld.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Yantao Li, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, Nanjing University, Shanghai AI Laboratory
    - 📅 Date: January 17, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [benchmark], [dataset], [GUI grounding], [grounding pre-training], [ScreenSpot], [SeeClick]
    - 📖 TLDR: SeeClick is a screenshot-only GUI agent built around the GUI grounding problem rather than structured trees such as HTML. The paper adds automated GUI-grounding data curation and introduces ScreenSpot, a grounding benchmark spanning mobile, desktop, and web environments.
