# Boyuan Zheng's Papers

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets & Benchmarks Track (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [agentic search], [agent-as-a-judge], [tree-structured rubric], [source attribution], [human evaluation], [Mind2Web 2]
    - 📖 TLDR: Mind2Web 2 benchmarks long-horizon agentic search with 130 human-crafted tasks that require real-time browsing and citation-backed synthesis. It evaluates systems with task-specific judge agents built from tree-structured rubrics that score both answer correctness and source attribution, and compares ten frontier systems against human performance.

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y.Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: XLANG Lab, University of Hong Kong, Moonshot AI, Stanford University, University of Waterloo, Carnegie Mellon University
    - 📅 Date: August 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [chain-of-thought], [vision language model], [AgentNet]
    - 📖 TLDR: Introduces **OpenCUA**, an open-source framework to train computer-use agents (CUAs) using vision-language models. It includes a cross-platform annotation tool (AgentNet Tool), a large-scale dataset covering 3 OSes and 200+ apps/websites (AgentNet), and a data processing pipeline that builds state-action pairs enhanced with reflective long chain-of-thought reasoning. The resulting models—especially OpenCUA-72B—achieve SOTA performance on the OSWorld-Verified benchmark (45.0% success), surpassing prior open-source baselines and demonstrating strong generalization and scalability. All tools, models, and data are publicly released.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: The Ohio State University, Carnegie Mellon University, University of Virginia, Purdue University, Cisco Research
    - 📅 Date: April 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [transfer learning], [WebArena]
    - 📖 TLDR: SkillWeaver is a framework that enables web agents to autonomously improve by discovering, practicing, and refining reusable skills, encapsulated as APIs. Through iterative exploration, agents build a library of plug-and-play APIs, enhancing their capabilities. Experiments on WebArena and real-world websites demonstrate significant performance improvements, and the synthesized APIs can be shared among agents to boost overall performance.

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

- [Dual-View Visual Contextualization for Web Navigation](https://arxiv.org/abs/2402.04476)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: February 06, 2024
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [visual contextualization], [dual-view representation], [Mind2Web]
    - 📖 TLDR: Proposes dual-view visual contextualization, where a web element is represented jointly by its HTML-side attributes and its rendered screenshot context. The paper targets the disconnect between DOM text and visual layout in web navigation and reports gains on Mind2Web.

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
