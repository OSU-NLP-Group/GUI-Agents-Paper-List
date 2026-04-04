# Boyu Gou's Papers

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Zeyi Liao, Yadong Lu, Boyu Gou, Huan Sun, Ahmed Awadallah
    - 🏛️ Institutions: The Ohio State University, Microsoft Research, Redmond
    - 📅 Date: November 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [dataset], [benchmark], [text dragging], [multimodal LLM]
    - 📖 TLDR: This paper introduces GUI-Drag, a 161K-example dataset for text dragging in GUIs, and ScreenDrag, a benchmark with 5,333 examples, extending GUI grounding beyond click-only actions to support drag-based text selection and manipulation while maintaining click performance.

- [Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents](https://arxiv.org/abs/2510.24702)
    - Yueqi Song, Ketan Ramaneti, Zaid Sheikh, Ziru Chen, Boyu Gou, Tianbao Xie, Yiheng Xu, Danyang Zhang, Apurva Gandhi, Fan Yang, Joseph Liu, Tianyue Ou, Zhihao Yuan, Frank Xu, Shuyan Zhou, Xingyao Wang, Xiang Yue, Tao Yu, Huan Sun, Yu Su, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University, The Ohio State University, University of Hong Kong, Duke University, Fujitsu Research, All Hands AI
    - 📅 Date: October 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [data protocol], [training data], [supervised fine-tuning], [dataset unification], [ADP]
    - 📖 TLDR: Agent Data Protocol (ADP) standardizes heterogeneous agent trajectories into a lightweight schema and conversion pipeline so diverse agent datasets can plug into multiple SFT pipelines without per-dataset engineering. Converting 13 existing datasets into ADP and fine-tuning on the unified corpus improves base models by about 20% on average across coding, browsing, tool-use, and research benchmarks.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets & Benchmarks Track)
    - 💻 Env: [Web], [Search]
    - 🔑 Key: [benchmark], [agentic search], [agent-as-a-judge], [information synthesis], [evaluation], [Mind2Web 2]
    - 📖 TLDR: Mind2Web 2 is a benchmark of 130 realistic long-horizon agentic-search tasks built with more than 1,000 hours of human labor, focusing on real-time browsing plus citation-backed synthesis rather than short static-answer retrieval. Its main technical contribution is Agent-as-a-Judge: task-specific judge agents built from tree-structured rubrics that score both answer correctness and source attribution, enabling large-scale evaluation of frontier deep-research systems against humans.

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://openreview.net/forum?id=6jZi4HSs6o)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: April 02, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [online-Mind2Web], [WebJudge], [operator], [LLM-as-a-judge]
    - 📖 TLDR: This paper critically evaluates the performance of current web agents, revealing that many underperform on the newly introduced **Online-Mind2Web** benchmark, which comprises 300 realistic tasks across 136 websites. The study highlights a discrepancy between reported successes and actual capabilities, attributing this to shortcomings in existing benchmarks. To address evaluation scalability, the authors propose **WebJudge**, an automatic LLM-based evaluation method achieving approximately 85% agreement with human judgments. The comprehensive analysis underscores the need for more robust assessment frameworks in web agent research.

- [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents](https://aclanthology.org/2025.findings-acl.326/)
    - Vardaan Pahuja, Yadong Lu, Corby Rosset, Boyu Gou, Arindam Mitra, Spencer Whitehead, Yu Su, Ahmed Hassan Awadallah
    - 🏛️ Institutions: Microsoft Research, Redmond, The Ohio State University
    - 📅 Date: February 17, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [trajectory synthesis], [web exploration], [data scaling], [Explorer]
    - 📖 TLDR: This paper targets the shortage of large, diverse web-agent trajectories by synthesizing a 94K-trajectory multimodal dataset through scalable exploration and refinement over 49K URLs. Training on this dataset yields a strong web agent, Explorer, and shows that data scaling is a major driver of web-agent performance.

- [WebOlympus: An Open Platform for Web Agents on Live Websites](https://aclanthology.org/2024.emnlp-demo.20/)
    - Boyuan Zheng, Boyu Gou, Scott Salisbury, Zheng Du, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: November 12, 2024
    - 📑 Publisher: EMNLP 2024 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [platform], [WebOlympus], [chrome extension], [live websites], [safety monitor]
    - 📖 TLDR: Presents WebOlympus, an open platform for running web agents directly on live websites through a Chrome extension interface. The system is designed to support research and deployment workflows while adding a safety monitor for human- or model-mediated intervention and supporting applications like trajectory annotation and data collection.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://openreview.net/forum?id=c6l7yA0HSq)
    - Yu Gu, Kai Zhang, Yuting Ning, Boyuan Zheng, Boyu Gou, Tianci Xue, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [WebDreamer], [model-based planning], [world model], [irreversible actions]
    - 📖 TLDR: Argues that web agents should use model-based planning instead of relying heavily on backtracking search in irreversible web environments. The proposed WebDreamer framework uses an LLM world model to simulate candidate action outcomes before acting, improving over reactive baselines on benchmarks such as VisualWebArena and Mind2Web-live.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0faa4bc5f522076947a030273629d4fe-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Orby AI
    - 📅 Date: October 07, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform generalization], [UGround], [synthetic data]
    - 📖 TLDR: Introduces UGround, a universal visual grounding model for GUI agents trained on a 10M-element synthetic dataset spanning 1.3M screenshots. The paper shows that a vision-only grounding module can generalize across desktop, mobile, and web interfaces and can match or exceed agents that rely on extra textual inputs.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: January 01, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [grounding], [SeeAct], [Mind2Web], [online evaluation]
    - 📖 TLDR: Shows that GPT-4V can act as a strong generalist web agent when the grounding problem is handled carefully. The paper introduces the SeeAct framework and demonstrates that better grounding of webpage elements is the main bottleneck between frontier multimodal models and reliable web control.
