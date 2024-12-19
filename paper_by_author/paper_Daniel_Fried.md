# Daniel Fried's Papers

- [Dissecting Adversarial Robustness of Multimodal LM Agents](https://openreview.net/forum?id=LjVIGva5Ct)
    - Chen Henry Wu, Rishi Rajesh Shah, Jing Yu Koh, Russ Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: CMU, Stanford
    - 📅 Date: October 21, 2024
    - 📑 Publisher: NeurIPS 2024 Workshop
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [attack], [ARE], [safety]
    - 📖 TLDR: This paper introduces the Agent Robustness Evaluation (ARE) framework to assess the adversarial robustness of multimodal language model agents in web environments. By creating 200 targeted adversarial tasks within VisualWebArena, the study reveals that minimal perturbations can significantly compromise agent performance, even in advanced systems utilizing reflection and tree-search mechanisms. The findings highlight the need for enhanced safety measures in deploying such agents.

- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)
    - Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig
    - 🏛️ Institutions: CMU, MIT
    - 📅 Date: September 11, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [memory], [AWM]
    - 📖 TLDR: The paper proposes *Agent Workflow Memory (AWM)*, a method enabling language model-based agents to induce and utilize reusable workflows from past experiences to guide future actions in web navigation tasks. AWM operates in both offline and online settings, significantly improving performance on benchmarks like Mind2Web and WebArena, and demonstrating robust generalization across tasks, websites, and domains.

- [Adversarial Attacks on Multimodal Agents](https://chenwu.io/attack-agent/)
    - Chen Henry Wu, Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: CMU
    - 📅 Date: Jun 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [VisualWebArena-Adv]
    - 📖 TLDR: This paper investigates the safety risks posed by multimodal agents built on vision-enabled language models (VLMs). The authors introduce two adversarial attack methods: a captioner attack targeting white-box captioners and a CLIP attack that transfers to proprietary VLMs. To evaluate these attacks, they curated VisualWebArena-Adv, a set of adversarial tasks based on VisualWebArena. The study demonstrates that within a limited perturbation norm, the captioner attack can achieve a 75% success rate in making a captioner-augmented GPT-4V agent execute adversarial goals. The paper also discusses the robustness of agents based on other VLMs and provides insights into factors contributing to attack success and potential defenses. [oai_citation_attribution:0‡ArXiv](https://arxiv.org/abs/2406.12814?utm_source=chatgpt.com)

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: CMU
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [dataset], [multimodal agent evaluation], [visually grounded tasks]
    - 📖 TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
    - 🏛️ Institutions: CMU
    - 📅 Date: July 26, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [multi-tab navigation], [web-based interaction], [agent simulation]
    - 📖 TLDR: *WebArena* provides a standalone, realistic web simulation environment where autonomous agents can perform complex web-based tasks. The platform offers functionalities such as multi-tab browsing, element interaction, and customized user profiles. Its benchmark suite contains 812 tasks grounded in high-level natural language commands. WebArena uses multi-modal observations, including HTML and accessibility tree views, supporting advanced tasks that require contextual understanding across diverse web pages, making it suitable for evaluating generalist agents in real-world web environments.
