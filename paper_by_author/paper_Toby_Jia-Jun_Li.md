# Toby Jia-Jun Li's Papers

- [UI Layout Generation with LLMs Guided by UI Grammar](https://arxiv.org/abs/2310.15455)
    - Yuwen Lu, Ziang Tong, Qinyi Zhao, Chengzhi Zhang, Toby Jia-Jun Li
    - 🏛️ Institutions: ICML 2023 Workshop on AI and HCI
    - 📅 Date: October 24, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [UI grammar], [UI Layout Generation]
    - 📖 TLDR: This position paper explores the use of Large Language Models (LLMs) for generating mobile user interface (UI) layouts. It introduces *UI grammar*, a novel approach to represent the hierarchical structure of UI screens, aiming to guide LLMs' generative capabilities more effectively and enhance the explainability and controllability of the process. Initial experiments with GPT-4 demonstrate the potential of LLMs to produce high-quality UIs through in-context learning, with the grammar-based approach improving certain aspects of generation quality.

- [AutoDroid: LLM-powered Task Automation in Android](https://arxiv.org/abs/2308.15272)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - 🏛️ Institutions: Tsinghua University, Shanghai AI Lab, University of Notre Dame, MSR
    - 📅 Date: August 29, 2023
    - 📑 Publisher: MobiCom 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [Android task automation], [LLM-powered agent]
    - 📖 TLDR: This paper introduces AutoDroid, a novel mobile task automation system capable of handling arbitrary tasks on any Android application without manual efforts. The framework combines the commonsense knowledge of LLMs with domain-specific knowledge of apps through automated dynamic analysis. AutoDroid features a functionality-aware UI representation method, exploration-based memory injection techniques, and a multi-granularity query optimization module. Evaluated on a new benchmark with 158 common tasks, AutoDroid achieves a 90.9% action generation accuracy and a 71.3% task completion rate, significantly outperforming GPT-4-powered baselines.

- [Interactive Task Learning from GUI-Grounded Natural Language Instructions and Demonstrations](https://aclanthology.org/2020.acl-demos.25/)
    - Toby Jia-Jun Li, Tom Mitchell, Brad Myers
    - 🏛️ Institutions: CMU
    - 📅 Date: July 2020
    - 📑 Publisher: ACL 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [Sugilite], [programming-by-demonstration]
    - 📖 TLDR: This paper introduces *Sugilite*, an intelligent task automation agent that learns new tasks and associated concepts interactively from users' natural language instructions and demonstrations on third-party mobile app GUIs. The system allows users to teach procedures and concepts through verbal instructions combined with GUI demonstrations, supports intent clarification for demonstrated actions, infers task parameters using hierarchical app GUI structures, and generalizes taught concepts across different contexts and domains. A prototype is presented as a conversational assistant on Android. [oai_citation_attribution:0‡ACL Anthology](https://aclanthology.org/2020.acl-demos.25/?utm_source=chatgpt.com)

- [PUMICE: A Multi-Modal Agent that Learns Concepts and Conditionals from Natural Language and Demonstrations](https://arxiv.org/abs/1909.00031)
    - Toby Jia-Jun Li, Marissa Radensky, Justin Jia, Kirielle Singarajah, Tom M. Mitchell, Brad A. Myers
    - 🏛️ Institutions: CMU, Amherst College
    - 📅 Date: August 30, 2019
    - 📑 Publisher: UIST 2019
    - 💻 Env: [Mobile]
    - 🔑 Key: [programming-by-demonstration], [PUMICE]
    - 📖 TLDR: This paper introduces *PUMICE*, a multi-modal agent that combines natural language programming and programming-by-demonstration to enable end users to instruct intelligent agents in performing new tasks. By allowing users to describe tasks and conditions naturally and then collaboratively resolving ambiguities through conversation and demonstration, PUMICE facilitates the teaching of new concepts and procedures within existing mobile app GUIs. A lab study with 10 users demonstrated its usability and effectiveness.

- [SUGILITE: Creating Multimodal Smartphone Automation by Demonstration](https://dl.acm.org/doi/abs/10.1145/3025453.3025483)
    - Toby Jia-Jun Li, Amos Azaria, Brad A. Myers
    - 🏛️ Institutions: CMU, Ariel University
    - 📅 Date: May 6, 2017
    - 📑 Publisher: CHI 2017
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [PBD], [multimodal interaction], [SUGILITE], [programming-by-demonstration], [demonstration]
    - 📖 TLDR: This paper introduces *SUGILITE*, a programming-by-demonstration (PBD) system that enables users to automate tasks on smartphones through multimodal interactions. By leveraging Android's accessibility API, SUGILITE allows users to create generalized automation scripts for arbitrary third-party apps by demonstrating tasks using the regular app UI. The system combines verbal instructions, user demonstrations, and app UI hierarchies to generalize scripts from single demonstrations, facilitating task variations and parameterization. Extensive error handling and context checking enhance robustness against app UI changes. A lab study indicates that users with minimal programming knowledge can successfully automate smartphone tasks using SUGILITE.
