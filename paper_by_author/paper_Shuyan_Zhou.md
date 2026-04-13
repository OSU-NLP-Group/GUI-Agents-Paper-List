# Shuyan Zhou's Papers

- [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588)
    - Faria Huq, Zora Zhiruo Wang, Zhanqiu Guo, Venu Arvind Arangarajan, Tianyue Ou, Frank Xu, Shuyan Zhou, Graham Neubig, Jeffrey P. Bigham
    - 🏛️ Institutions: CMU, Duke University
    - 📅 Date: February 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [human-agent interaction], [intervention prediction], [interaction styles], [CowCorpus], [collaborative web agents]
    - 📖 TLDR: This paper studies collaborative web agents through human intervention patterns, introducing CowCorpus with 400 real-user trajectories that mix human and agent actions. Modeling four distinct interaction styles substantially improves intervention prediction and raises user-rated usefulness in live agents.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: May 16, 2025
    - 📑 Publisher: EMNLP 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [security], [prompt injection], [pixel perturbation], [screenshot attack], [neural rendering approximation], [WebInject]
    - 📖 TLDR: WebInject attacks screenshot-based web agents by perturbing the raw pixels of a rendered webpage so the resulting screenshot steers the agent toward an attacker-chosen action. To optimize that attack despite the non-differentiable render-to-screenshot pipeline, it learns a neural approximation of the mapping and then applies projected gradient descent.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: CMU
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-agent collaboration], [mixed-initiative web navigation], [data collection], [CowPilot]
    - 📖 TLDR: CowPilot is a mixed-initiative web-navigation framework where an agent proposes next steps while the user can pause, reject, override, or hand control back at any time. Across five websites, the collaborative mode reaches the highest success rate while requiring humans to perform only a small fraction of the total steps, and the system is also positioned as a data-collection and evaluation tool.

- [Beyond Browsing: API-Based Web Agents](https://aclanthology.org/2025.findings-acl.577/)
    - Yueqi Song, Frank F. Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: CMU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [WebArena], [API access]
    - 📖 TLDR: Studies what happens when web-agent tasks are solved through APIs instead of only through browsers. The paper proposes both API-only and hybrid agents, and shows that hybrid access to APIs plus browsing substantially outperforms browsing alone on WebArena.

- [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886)
    - Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar, Tu Trinh, Scale Red Team, Elaine Chang, Vaughn Robinson, Sean Hendryx, Shuyan Zhou, Matt Fredrikson, Summer Yue, Zifan Wang
    - 🏛️ Institutions: CMU, Scale AI, GraySwan AI
    - 📅 Date: October 11, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [red teaming], [jailbreaking], [BrowserART]
    - 📖 TLDR: The paper introduces BrowserART, a red-teaming benchmark with 100 harmful browser-agent behaviors spanning synthetic and real websites. It shows that refusal-trained backbone LLMs may still execute harmful instructions once embedded in browser agents, and that chat jailbreaks transfer effectively to that agent setting.

- [Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a6a6891cf1dfc64d664f086cf5976e93-Abstract-Conference.html)
    - Tianyue Ou, Frank F. Xu, Aman Madaan, Jiarui Liu, Robert Lo, Abishek Sridhar, Sudipta Sengupta, Dan Roth, Graham Neubig, Shuyan Zhou
    - 🏛️ Institutions: CMU, Amazon AWS AI, xAI
    - 📅 Date: September 24, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [synthetic demonstrations], [tutorial-to-demo synthesis], [indirect knowledge], [Synatra]
    - 📖 TLDR: Synatra turns indirect knowledge sources such as online tutorials into direct demonstrations for digital agents and uses 100k such synthetic demonstrations to train a 7B web agent. The paper reports stronger results than comparably sized models on Mind2Web, MiniWoB++, and WebArena, while synthetic demonstrations cost about 3% as much as human-collected ones.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: iMean AI, CMU
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [Mind2Web-Live], [key-node evaluation], [WebCanvas]
    - 📖 TLDR: WebCanvas is an online web-agent benchmark built to evaluate agents against live websites rather than static snapshots. It introduces key-node evaluation for progress-aware scoring, releases Mind2Web-Live with 542 tasks and 2,439 intermediate evaluation states, and provides tooling to annotate and maintain those tasks as the web changes.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Jing Hua Toh, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: HKU, CMU, Salesforce AI Research, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [OSWorld], [real computer environment], [execution-based evaluation], [multi-app workflows]
    - 📖 TLDR: OSWorld provides a real computer environment and benchmark for open-ended tasks across Ubuntu, Windows, and macOS, with 369 tasks spanning real web apps, desktop apps, file I/O, and multi-application workflows. Its execution-based evaluation setup exposes a large gap between humans and current multimodal agents, with the best reported model reaching 12.24% task success versus 72.36% for humans.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://aclanthology.org/2024.acl-long.50/)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: CMU
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [VisualWebArena], [visually grounded web tasks], [self-hosted environments], [multimodal agent evaluation]
    - 📖 TLDR: VisualWebArena is a benchmark of 910 visually grounded web tasks across Classifieds, Shopping, and Reddit environments. Built on WebArena's self-hosted setup, it targets multimodal web agents that must use image-text inputs rather than text alone.

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
    - 🏛️ Institutions: CMU, Inspired Cognition
    - 📅 Date: July 25, 2023
    - 📑 Publisher: NeurIPS 2024 (Oral)
    - 💻 Env: [Web]
    - 🔑 Key: [environment], [benchmark], [functional correctness], [realistic web tasks], [WebArena]
    - 📖 TLDR: Introduces WebArena, a realistic and reproducible web environment built from fully functional sites across several common domains. It helped establish the modern web-agent evaluation stack by pairing realistic websites, external tools and knowledge sources, and long-horizon benchmark tasks with functional correctness checks.
