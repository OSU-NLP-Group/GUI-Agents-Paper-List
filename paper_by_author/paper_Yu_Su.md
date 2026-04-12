# Yu Su's Papers

- [Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation](https://arxiv.org/abs/2602.10356)
    - Tianci Xue, Zeyi Liao, Tianneng Shi, Zilu Wang, Kai Zhang, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [continual learning], [reinforcement learning], [environment adaptation], [CUAJudge], [ACuRL], [curriculum learning]
    - 📖 TLDR: ACuRL studies continual adaptation for computer-use agents in changing environments without human demonstrations. It combines autonomous curriculum generation with CUAJudge-based evaluation to improve both within-environment and cross-environment adaptation while limiting forgetting.

- [Watch and Learn: Learning to Use Computers from Online Videos](https://arxiv.org/abs/2510.04673)
    - Chan Hee Song, Yiwen Song, Palash Goyal, Yu Su, Oriana Riva, Hamid Palangi, Tomas Pfister
    - 🏛️ Institutions: Google Cloud AI Research, The Ohio State University
    - 📅 Date: October 06, 2025
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [video demonstrations], [inverse dynamics], [trajectory annotation], [OSWorld], [WindowsAgentArena], [Watch & Learn]
    - 📖 TLDR: Watch & Learn converts Internet videos of human computer use into more than 53K executable UI trajectories by framing annotation as an inverse dynamics problem over consecutive screen states. The resulting data improves both general-purpose and specialized CUAs on OSWorld and yields state-of-the-art 7B-scale performance on WindowsAgentArena under the 15-step limit.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets & Benchmarks Track (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [agentic search], [agent-as-a-judge], [tree-structured rubric], [source attribution], [human evaluation], [Mind2Web 2]
    - 📖 TLDR: Mind2Web 2 benchmarks long-horizon agentic search with 130 human-crafted tasks that require real-time browsing and citation-backed synthesis. It evaluates systems with task-specific judge agents built from tree-structured rubrics that score both answer correctness and source attribution, and compares ten frontier systems against human performance.

- [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents](https://aclanthology.org/2025.findings-acl.326/)
    - Vardaan Pahuja, Yadong Lu, Corby Rosset, Boyu Gou, Arindam Mitra, Spencer Whitehead, Yu Su, Ahmed Hassan Awadallah
    - 🏛️ Institutions: Microsoft Research, Redmond, The Ohio State University
    - 📅 Date: July 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [trajectory synthesis], [web exploration], [data scaling], [Explorer]
    - 📖 TLDR: This paper targets the shortage of large, diverse web-agent trajectories by synthesizing a 94K-trajectory multimodal dataset through scalable exploration and refinement over 49K URLs. Training on this dataset yields a strong web agent, Explorer, and shows that data scaling is a major driver of web-agent performance.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: May 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [indirect prompt injection], [hybrid web-OS sandbox], [RTC-Bench], [RedTeamCUA]
    - 📖 TLDR: RedTeamCUA introduces a hybrid OS-and-web sandbox for realistic adversarial testing of computer-use agents under indirect prompt injection. Its RTC-Bench benchmark contains 864 hybrid attack scenarios and shows that current frontier agents still exhibit substantial attack success rates in both initialized and end-to-end settings.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: The Ohio State University, Carnegie Mellon University, University of Virginia, Purdue University, Cisco Research
    - 📅 Date: April 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [practice-and-distill], [transferable skills], [SkillWeaver]
    - 📖 TLDR: SkillWeaver is a skill-centric self-improvement framework for web agents that discovers website-specific skills, practices them, and distills the resulting experience into reusable APIs. Its iterative exploration grows a library of lightweight skills that improve performance on WebArena and real websites, and those APIs can also be transferred to weaker agents.

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

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4ca0e369689dadb25a5345ba9755ad6f-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: October 07, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [dataset], [GUI grounding], [vision-only agents], [cross-platform grounding], [UGround], [synthetic data]
    - 📖 TLDR: This paper introduces UGround, a universal GUI visual grounding model trained on 10M element-expression pairs over 1.3M screenshots from web, mobile, and desktop interfaces. It argues for vision-only GUI agents with pixel-level actions and shows that UGround improves grounding, offline-agent, and online-agent performance across six benchmarks.

- [Dual-View Visual Contextualization for Web Navigation](https://doi.org/10.1109/CVPR52733.2024.01369)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: February 06, 2024
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [dual-view contextualization], [visual grounding], [web element neighborhood], [Mind2Web]
    - 📖 TLDR: This paper contextualizes each HTML element with its corresponding screenshot region and nearby elements, combining textual and visual features to represent webpage elements more informatively. It evaluates the approach on Mind2Web and reports consistent gains in cross-task, cross-website, and cross-domain settings.

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
