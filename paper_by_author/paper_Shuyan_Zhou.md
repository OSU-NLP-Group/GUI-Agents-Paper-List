# Shuyan Zhou's Papers

- [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588)
    - Faria Huq, Zora Zhiruo Wang, Zhanqiu Guo, Venu Arvind Arangarajan, Tianyue Ou, Frank Xu, Shuyan Zhou, Graham Neubig, Jeffrey P. Bigham
    - 🏛️ Institutions: Carnegie Mellon University, Duke University
    - 📅 Date: February 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [human-agent interaction], [intervention prediction], [interaction styles], [CowCorpus], [collaborative web agents]
    - 📖 TLDR: This paper studies collaborative web agents through human intervention patterns, introducing CowCorpus with 400 real-user trajectories that mix human and agent actions. Modeling four distinct interaction styles substantially improves intervention prediction and raises user-rated usefulness in live agents.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: May 16, 2025
    - 📑 Publisher: EMNLP 2025
    - 💻 Env: [Web]
    - 🔑 Key: [security], [prompt injection], [pixel perturbation], [screenshot attack], [neural rendering approximation], [WebInject]
    - 📖 TLDR: WebInject attacks screenshot-based web agents by perturbing the raw pixels of a rendered webpage so the resulting screenshot steers the agent toward an attacker-chosen action. To optimize that attack despite the non-differentiable render-to-screenshot pipeline, it learns a neural approximation of the mapping and then applies projected gradient descent.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, Carnegie Mellon University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-agent collaboration], [mixed-initiative web navigation], [data collection], [CowPilot]
    - 📖 TLDR: CowPilot is a mixed-initiative web-navigation framework where an agent proposes next steps while the user can pause, reject, override, or hand control back at any time. Across five websites, the collaborative mode reaches the highest success rate while requiring humans to perform only a small fraction of the total steps, and the system is also positioned as a data-collection and evaluation tool.

- [Beyond Browsing: API-Based Web Agents](https://aclanthology.org/2025.findings-acl.577/)
    - Yueqi Song, Frank F. Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [WebArena], [API access]
    - 📖 TLDR: Studies what happens when web-agent tasks are solved through APIs instead of only through browsers. The paper proposes both API-only and hybrid agents, and shows that hybrid access to APIs plus browsing substantially outperforms browsing alone on WebArena.

- [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886)
    - Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar, Tu Trinh, Scale Red Team, Elaine T. Chang, Vaughn Robinson, Sean Hendryx, Shuyan Zhou, Matt Fredrikson, Summer Yue, Zifan Wang
    - 🏛️ Institutions: Carnegie Mellon University, GraySwan AI, Scale AI
    - 📅 Date: October 11, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [safety], [red teaming], [jailbreaking], [BrowserART]
    - 📖 TLDR: This paper introduces **Browser Agent Red teaming Toolkit (BrowserART)**, a comprehensive test suite for evaluating the safety of LLM-based browser agents. The study reveals that while refusal-trained LLMs decline harmful instructions in chat settings, their corresponding browser agents often comply with such instructions, indicating a significant safety gap. The authors call for collaboration among developers and policymakers to enhance agent safety.

- [Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a6a6891cf1dfc64d664f086cf5976e93-Abstract-Conference.html)
    - Tianyue Ou, Frank F. Xu, Aman Madaan, Jiarui Liu, Robert Lo, Abishek Sridhar, Sudipta Sengupta, Dan Roth, Graham Neubig, Shuyan Zhou
    - 🏛️ Institutions: Carnegie Mellon University, Amazon Web Services AI
    - 📅 Date: September 24, 2024
    - 📑 Publisher: NeurIPS 2024 (Main Conference Track)
    - 💻 Env: [Web]
    - 🔑 Key: [synthetic data], [synthetic demonstrations], [indirect knowledge], [Synatra]
    - 📖 TLDR: Introduces Synatra, a pipeline for converting indirect knowledge sources such as tutorials into direct demonstrations for digital agents. Using 100k synthetic demonstrations, the paper trains a 7B web agent that outperforms similarly sized models on Mind2Web, MiniWoB++, and WebArena at a small fraction of the cost of human demonstrations.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: iMean AI, Carnegie Mellon University
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [Mind2Web-Live], [key-node evaluation], [WebCanvas]
    - 📖 TLDR: Presents WebCanvas, an online evaluation framework for web agents that explicitly targets the instability of real websites. It introduces key-node evaluation, releases Mind2Web-Live as an online benchmark derived from Mind2Web, and provides tooling for annotation and continual maintenance.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Jing Hua Toh, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Carnegie Mellon University, Salesforce Research, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [real computer tasks], [online environment], [online benchmark]
    - 📖 TLDR: OSWorld introduces a groundbreaking benchmark for multimodal agents to perform open-ended tasks within real computer environments across platforms like Ubuntu, Windows, and macOS. It includes 369 real-world tasks involving web and desktop apps, file management, and multi-app workflows, with custom evaluation scripts for reproducibility. The results reveal current agents’ limitations in GUI interaction and operational knowledge, as they achieve just 12.24% task success compared to humans' 72.36%, highlighting critical gaps for future model improvement.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://aclanthology.org/2024.acl-long.50/)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [dataset], [multimodal agent evaluation], [visually grounded tasks]
    - 📖 TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: July 25, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [environment], [benchmark], [multi-tab navigation], [realistic web tasks], [WebArena]
    - 📖 TLDR: Introduces WebArena, a realistic and reproducible web environment built from fully functional sites across several common domains. It helped establish the modern web-agent evaluation stack by pairing realistic websites, external tools and knowledge sources, and long-horizon benchmark tasks with functional correctness checks.
