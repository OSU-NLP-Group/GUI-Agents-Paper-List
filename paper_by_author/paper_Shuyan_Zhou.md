# Shuyan Zhou's Papers

- [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588)
    - Faria Huq, Zora Zhiruo Wang, Zhanqiu Guo, Venu Arvind Arangarajan, Tianyue Ou, Frank Xu, Shuyan Zhou, Graham Neubig, Jeffrey P. Bigham
    - 🏛️ Institutions: Carnegie Mellon University, Duke University
    - 📅 Date: February 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [framework], [web agent], [human-agent interaction], [intervention prediction], [CowCorpus]
    - 📖 TLDR: This paper introduces CowCorpus, a dataset of 400 real-user web navigation trajectories with interleaved human-agent actions, and identifies four distinct human interaction patterns to train language models that predict user interventions, achieving 61.4-63.4% improvement in prediction accuracy and a 26.5% increase in user-rated agent usefulness.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: October 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [prompt injection], [attack], [adversarial attack], [multimodal LLM], [security]
    - 📖 TLDR: WebInject proposes a prompt injection attack against MLLM-based web agents by adding optimized pixel-level perturbations to rendered webpages, using a neural network to approximate the non-differentiable webpage-to-screenshot mapping and projected gradient descent to find perturbations that induce attacker-specified actions.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, Carnegie Mellon University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [human-agent collaboration], [web navigation], [evaluation], [CowPilot]
    - 📖 TLDR: This paper introduces CowPilot, a Chrome-extension framework for mixed-initiative web navigation where an agent proposes actions while a human can pause, reject, override, or resume control during the same task. It is designed both as a collaboration interface and as an evaluation/data-collection platform for web agents. In case studies across five websites, the collaborative setting reaches the highest success rate while substantially reducing the number of steps humans must perform themselves.

- [Beyond Browsing: API-Based Web Agents](https://aclanthology.org/2025.findings-acl.577/)
    - Yueqi Song, Frank Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [benchmark], [WebArena], [SOTA performance]
    - 📖 TLDR: This paper introduces API-based and hybrid agents designed to execute online tasks by accessing both APIs and traditional web browsing interfaces. In evaluations using WebArena, a benchmark for web navigation, the API-based agent achieves higher performance than browser-based agents, and the hybrid model achieves a success rate of 35.8%, setting a new state-of-the-art (SOTA) in task-agnostic web navigation. The findings highlight the efficiency and reliability gains of API interactions for web agents.

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
    - 🔑 Key: [synthetic data], [synthetic demonstrations], [web navigation], [synatra]
    - 📖 TLDR: Synatra introduces a scalable framework for digital agents, enabling them to convert indirect knowledge sources into actionable demonstrations. This approach enhances the ability of agents to learn tasks without extensive labeled data, leveraging insights from indirect observations to scale practical implementations in digital environments.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: iMean AI, Carnegie Mellon University
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [Mind2Web-live], [key-node evaluation]
    - 📖 TLDR: This paper presents WebCanvas, an online evaluation framework for web agents designed to address the dynamic nature of web interactions. It introduces a key-node-based evaluation metric to capture critical actions or states necessary for task completion while disregarding noise from insignificant events or changed web elements. The framework includes the Mind2Web-Live dataset, a refined version of the original Mind2Web static dataset, containing 542 tasks with 2,439 intermediate evaluation states. Despite advancements, the best-performing model achieves a task success rate of 23.1%, highlighting substantial room for improvement.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Jing Hua Toh, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Carnegie Mellon University, Salesforce Research, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [GUI]
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
    - 📅 Date: July 26, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [multi-tab navigation], [web-based interaction], [agent simulation]
    - 📖 TLDR: *WebArena* provides a standalone, realistic web simulation environment where autonomous agents can perform complex web-based tasks. The platform offers functionalities such as multi-tab browsing, element interaction, and customized user profiles. Its benchmark suite contains 812 tasks grounded in high-level natural language commands. WebArena uses multi-modal observations, including HTML and accessibility tree views, supporting advanced tasks that require contextual understanding across diverse web pages, making it suitable for evaluating generalist agents in real-world web environments.
