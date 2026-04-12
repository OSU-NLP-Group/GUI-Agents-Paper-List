# Huan Sun's Papers

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL], [curriculum learning]
    - 📖 TLDR: ACuRL studies continual adaptation for computer-use agents in changing environments without human demonstrations. It combines autonomous curriculum generation with CUAJudge-based evaluation to improve both within-environment and cross-environment adaptation while limiting forgetting.

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Zeyi Liao, Yadong Lu, Boyu Gou, Huan Sun, Ahmed Awadallah
    - 🏛️ Institutions: The Ohio State University, Microsoft Research, Redmond
    - 📅 Date: November 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [dataset], [benchmark], [text dragging], [GUI-Drag], [ScreenDrag]
    - 📖 TLDR: This paper expands GUI grounding beyond click actions by focusing on text dragging, a common but previously underexplored mouse interaction. It introduces the GUI-Drag training set and the ScreenDrag benchmark, and shows that continual training for dragging can improve drag performance without sacrificing click grounding.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets & Benchmarks Track (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [agentic search], [agent-as-a-judge], [tree-structured rubric], [source attribution], [human evaluation], [Mind2Web 2]
    - 📖 TLDR: Mind2Web 2 benchmarks long-horizon agentic search with 130 human-crafted tasks that require real-time browsing and citation-backed synthesis. It evaluates systems with task-specific judge agents built from tree-structured rubrics that score both answer correctness and source attribution, and compares ten frontier systems against human performance.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [indirect prompt injection], [hybrid web-OS sandbox], [RTC-Bench], [RedTeamCUA]
    - 📖 TLDR: RedTeamCUA introduces a hybrid OS-and-web sandbox for realistic adversarial testing of computer-use agents under indirect prompt injection. Its RTC-Bench benchmark contains 864 hybrid attack scenarios and shows that current frontier agents still exhibit substantial attack success rates in both initialized and end-to-end settings.

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://openreview.net/forum?id=6jZi4HSs6o)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: April 02, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [online-Mind2Web], [WebJudge], [LLM-as-a-judge]
    - 📖 TLDR: This paper argues that reported web-agent progress is overstated once agents are evaluated on more realistic online tasks. It introduces Online-Mind2Web with 300 tasks across 136 live websites, pairs it with the WebJudge automatic evaluation method, and uses that setup to show a much weaker picture of current web-agent capability than prior benchmarks suggest.

- [WebOlympus: An Open Platform for Web Agents on Live Websites](https://aclanthology.org/2024.emnlp-demo.20/)
    - Boyuan Zheng, Boyu Gou, Scott Salisbury, Zheng Du, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: November 12, 2024
    - 📑 Publisher: EMNLP 2024 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [platform], [WebOlympus], [Chrome extension], [live websites], [safety monitor]
    - 📖 TLDR: Presents WebOlympus, an open platform for running web agents directly on live websites through a Chrome extension interface. The system is designed to support research and deployment workflows while adding a safety monitor for human- or model-mediated intervention and supporting applications like trajectory annotation and data collection.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://openreview.net/forum?id=c6l7yA0HSq)
    - Yu Gu, Kai Zhang, Yuting Ning, Boyuan Zheng, Boyu Gou, Tianci Xue, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Uniphore, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [WebDreamer], [model-based planning], [world model], [irreversible actions]
    - 📖 TLDR: This paper argues that web agents should use model-based planning instead of relying heavily on backtracking search in irreversible web environments. The proposed WebDreamer framework uses an LLM world model to simulate candidate action outcomes before acting, improving over reactive baselines on benchmarks such as VisualWebArena, Online-Mind2Web, and Mind2Web-Live.

- [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://proceedings.mlr.press/v267/xu25m.html)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, University of Chicago, The Ohio State University
    - 📅 Date: October 22, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [red teaming], [black-box attack], [DPO], [AdvAgent]
    - 📖 TLDR: AdvAgent is a black-box red-teaming method for web agents that trains an adversarial prompter with DPO to generate stealthy, controllable attacks against frontier browser agents. The paper shows high attack success rates across realistic web tasks and finds that existing prompt-based defenses provide limited protection.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0faa4bc5f522076947a030273629d4fe-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: October 07, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform generalization], [UGround], [synthetic data]
    - 📖 TLDR: Introduces UGround, a universal visual grounding model for GUI agents trained on a 10M-element synthetic dataset spanning 1.3M screenshots. The paper shows that a vision-only grounding module can generalize across desktop, mobile, and web interfaces and can match or exceed agents that rely on extra textual inputs.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Los Angeles, The University of Chicago, University of Illinois Urbana-Champaign, University of Wisconsin-Madison
    - 📅 Date: September 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [EIA]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: January 01, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [grounding], [SeeAct], [Mind2Web], [online evaluation]
    - 📖 TLDR: Shows that GPT-4V can act as a strong generalist web agent when the grounding problem is handled carefully. The paper introduces the SeeAct framework and demonstrates that better grounding of webpage elements is the main bottleneck between frontier multimodal models and reliable web control.

- [Mind2Web: Towards a Generalist Agent for the Web](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5950bf290a1570ea401bf98882128160-Abstract-Datasets_and_Benchmarks.html)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: June 09, 2023
    - 📑 Publisher: NeurIPS 2023 Datasets and Benchmarks Track
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [Mind2Web], [MindAct], [generalist web agents]
    - 📖 TLDR: Introduces Mind2Web, a benchmark of realistic language-guided web tasks across 137 websites and 31 domains. The companion MindAct framework uses smaller models for element ranking to help larger models operate on messy real-world HTML, making the paper a cornerstone for modern web-agent evaluation.
