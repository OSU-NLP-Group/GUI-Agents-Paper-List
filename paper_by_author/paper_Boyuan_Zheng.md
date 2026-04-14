# Boyuan Zheng's Papers

- [CocoaBench: Evaluating Unified Digital Agents in the Wild](https://arxiv.org/abs/2604.11201)
    - Shibo Hao, Zhining Zhang, Zhiqi Liang, Tianyang Liu, Yuheng Zha, Qiyue Gao, Jixuan Chen, Zilong Wang, Zhoujun Cheng, Haoxiang Zhang, Junli Wang, Hexi Jin, Boyuan Zheng, Kun Zhou, Yu Wang, Feng Yao, Licheng Liu, Yijiang Li, Zhifei Li, Zhengtao Han, Pracha Promthaw, Tommaso Cerruti, Xiaohan Fu, Ziqiao Ma, Jingbo Shang, Lianhui Qin, Julian McAuley, Eric P. Xing, Zhengzhong Liu, Rupesh Kumar Srivastava, Zhiting Hu
    - 🏛️ Institutions: UC San Diego, OSU, CMU, MBZUAI
    - 📅 Date: April 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [unified digital agents], [long-horizon tasks], [visual grounding], [CocoaBench], [CocoaAgent]
    - 📖 TLDR: CocoaBench evaluates unified digital agents on long-horizon tasks requiring flexible composition of vision, search, and coding. Tasks are specified by an instruction and an automatic evaluation function, enabling reliable scalable evaluation across agent infrastructures. The best-evaluated system reaches only 45.1%, exposing gaps in reasoning, tool use, and visual grounding.

- [MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516)
    - Tanmay Gupta, Piper Wolters, Zixian Ma, Peter Sushko, Rock Yuren Pang, Diego Llanes, Yue Yang, Taira Anderson, Boyuan Zheng, Zhongzheng Ren, Harsh Trivedi, Taylor Blanton, Caleb Ouellette, Winson Han, Ali Farhadi, Ranjay Krishna
    - 🏛️ Institutions: AI2, UW, UNC
    - 📅 Date: April 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [model], [dataset], [MolmoWeb], [open-source]
    - 📖 TLDR: MolmoWeb is a family of fully open multimodal web agents (4B and 8B) trained on MolmoWebMix (100K+ synthetic trajectories and 30K+ human demonstrations). Operating as screenshot-only visual-language action policies without HTML or accessibility tree access, it achieves SOTA on WebVoyager, Online-Mind2Web, and DeepShop, outperforming larger closed models like GPT-4o.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets & Benchmarks Track (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [agentic search], [agent-as-a-judge], [tree-structured rubric], [source attribution], [human evaluation], [Mind2Web 2]
    - 📖 TLDR: Mind2Web 2 benchmarks long-horizon agentic search with 130 human-crafted tasks that require real-time browsing and citation-backed synthesis. It evaluates systems with task-specific judge agents built from tree-structured rubrics that score both answer correctness and source attribution, and compares ten frontier systems against human performance.

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y.Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: XLANG Lab, HKU, Moonshot AI, Stanford, University of Waterloo, CMU
    - 📅 Date: August 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [AgentNet], [AgentNet Tool], [reflective long CoT], [OSWorld-Verified], [OpenCUA]
    - 📖 TLDR: OpenCUA is an open-source computer-use stack centered on AgentNet Tool for demonstration capture, AgentNet for large-scale cross-platform trajectories, and a training pipeline that adds reflective long chain-of-thought supervision. The paper reports strong open-model results on OSWorld-Verified and argues that cross-platform data and test-time reasoning both materially improve agent performance.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: OSU, CMU, University of Virginia, Purdue University, Cisco Research
    - 📅 Date: April 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [practice-and-distill], [transferable skills], [SkillWeaver]
    - 📖 TLDR: SkillWeaver is a skill-centric self-improvement framework for web agents that discovers website-specific skills, practices them, and distills the resulting experience into reusable APIs. Its iterative exploration grows a library of lightweight skills that improve performance on WebArena and real websites, and those APIs can also be transferred to weaker agents.

- [WebOlympus: An Open Platform for Web Agents on Live Websites](https://aclanthology.org/2024.emnlp-demo.20/)
    - Boyuan Zheng, Boyu Gou, Scott Salisbury, Zheng Du, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: November 12, 2024
    - 📑 Publisher: EMNLP 2024 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [platform], [WebOlympus], [Chrome extension], [live websites], [safety monitor]
    - 📖 TLDR: Presents WebOlympus, an open platform for running web agents directly on live websites through a Chrome extension interface. The system is designed to support research and deployment workflows while adding a safety monitor for human- or model-mediated intervention and supporting applications like trajectory annotation and data collection.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://openreview.net/forum?id=c6l7yA0HSq)
    - Yu Gu, Kai Zhang, Yuting Ning, Boyuan Zheng, Boyu Gou, Tianci Xue, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Uniphore, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [WebDreamer], [model-based planning], [world model], [irreversible actions]
    - 📖 TLDR: This paper argues that web agents should use model-based planning instead of relying heavily on backtracking search in irreversible web environments. The proposed WebDreamer framework uses an LLM world model to simulate candidate action outcomes before acting, improving over reactive baselines on benchmarks such as VisualWebArena, Online-Mind2Web, and Mind2Web-Live.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4ca0e369689dadb25a5345ba9755ad6f-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Orby AI
    - 📅 Date: October 07, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [dataset], [GUI grounding], [vision-only agents], [cross-platform grounding], [UGround], [synthetic data]
    - 📖 TLDR: This paper introduces UGround, a universal GUI visual grounding model trained on 10M element-expression pairs over 1.3M screenshots from web, mobile, and desktop interfaces. It argues for vision-only GUI agents with pixel-level actions and shows that UGround improves grounding, offline-agent, and online-agent performance across six benchmarks.

- [Dual-View Visual Contextualization for Web Navigation](https://doi.org/10.1109/CVPR52733.2024.01369)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - 🏛️ Institutions: OSU
    - 📅 Date: February 06, 2024
    - 📑 Publisher: CVPR 2024 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [GUI grounding], [dual-view contextualization], [visual grounding], [web element neighborhood], [Mind2Web]
    - 📖 TLDR: This paper contextualizes each HTML element with its corresponding screenshot region and nearby elements, combining textual and visual features to represent webpage elements more informatively. It evaluates the approach on Mind2Web and reports consistent gains in cross-task, cross-website, and cross-domain settings.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: January 03, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [grounding], [SeeAct], [live website evaluation], [Mind2Web]
    - 📖 TLDR: SeeAct studies GPT-4V as a generalist web agent and adds an online evaluation setup for running agents on live websites. It shows that GPT-4V is strong when grounding is handled manually, and identifies grounding as the main remaining bottleneck.

- [Mind2Web: Towards a Generalist Agent for the Web](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5950bf290a1570ea401bf98882128160-Abstract-Datasets_and_Benchmarks.html)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: June 09, 2023
    - 📑 Publisher: NeurIPS 2023 Datasets and Benchmarks Track
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [Mind2Web], [MindAct], [generalist web agents]
    - 📖 TLDR: Introduces Mind2Web, a benchmark of realistic language-guided web tasks across 137 websites and 31 domains. The companion MindAct framework uses smaller models for element ranking to help larger models operate on messy real-world HTML, making the paper a cornerstone for modern web-agent evaluation.
