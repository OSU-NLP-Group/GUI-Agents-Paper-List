# Graham Neubig's Papers

- [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588)
    - Faria Huq, Zora Zhiruo Wang, Zhanqiu Guo, Venu Arvind Arangarajan, Tianyue Ou, Frank Xu, Shuyan Zhou, Graham Neubig, Jeffrey P. Bigham
    - 🏛️ Institutions: Carnegie Mellon University, Duke University
    - 📅 Date: 2026-02-27
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [framework], [web agent], [human-agent interaction], [intervention prediction], [CowCorpus]
    - 📖 TLDR: This paper introduces CowCorpus, a dataset of 400 real-user web navigation trajectories with interleaved human-agent actions, and identifies four distinct human interaction patterns to train language models that predict user interventions, achieving 61.4-63.4% improvement in prediction accuracy and a 26.5% increase in user-rated agent usefulness.

- [Go-Browse: Training Web Agents with Structured Exploration](https://arxiv.org/abs/2506.03533)
    - Apurva Gandhi, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: June 4, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [web agent], [structured exploration], [task generation], [WebArena], [go-browse]
    - 📖 TLDR: This paper frames web-agent data collection as structured exploration over website graphs so agents can reuse information gathered across trajectories instead of exploring each task from scratch. On WebArena, Go-Browse collects 10K successful trajectories and 40K interaction steps across 100 URLs, then uses them to fine-tune a 7B model that surpasses GPT-4o mini and sets a new sub-10B result on the benchmark.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, Carnegie Mellon University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [human-agent collaboration], [web navigation], [evaluation], [CowPilot]
    - 📖 TLDR: This paper introduces CowPilot, a Chrome-extension framework for mixed-initiative web navigation where an agent proposes actions while a human can pause, reject, override, or resume control during the same task. It is designed both as a collaboration interface and as an evaluation/data-collection platform for web agents. In case studies across five websites, the collaborative setting reaches the highest success rate while substantially reducing the number of steps humans must perform themselves.

- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University, Microsoft
    - 📅 Date: April 9, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [model], [benchmark], [learning], [reasoning], [planning], [ASI], [WebArena]
    - 📖 TLDR: This paper introduces Agent Skill Induction (ASI), a framework enabling web agents to learn and apply programmatic skills dynamically. By representing skills as executable programs, ASI allows agents to verify and reuse these skills across tasks, enhancing adaptability and efficiency. Evaluated on the WebArena benchmark, ASI outperforms static and text-based skill agents in success rate and step efficiency, demonstrating improved generalization and adaptability to new web environments.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: The Ohio State University, Carnegie Mellon University, University of Virginia, Purdue University, Cisco Research
    - 📅 Date: April 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [transfer learning], [WebArena]
    - 📖 TLDR: SkillWeaver is a framework that enables web agents to autonomously improve by discovering, practicing, and refining reusable skills, encapsulated as APIs. Through iterative exploration, agents build a library of plug-and-play APIs, enhancing their capabilities. Experiments on WebArena and real-world websites demonstrate significant performance improvements, and the synthesized APIs can be shared among agents to boost overall performance.

- [The BrowserGym Ecosystem for Web Agent Research](https://openreview.net/forum?id=5298fKGmv3)
    - Thibault Le Sellier De Chezelles, Maxime Gasse, Alexandre Drouin, Massimo Caccia, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Quentin Cappart, Graham Neubig, Ruslan Salakhutdinov, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Carnegie Mellon University, McGill University, Tel Aviv University, Université de Montréal, iMean AI
    - 📅 Date: December 6, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [LLM], [automation], [BrowserGym], [AgentLab]
    - 📖 TLDR: This paper presents *BrowserGym*, an ecosystem designed to standardize the evaluation and benchmarking of web agents, particularly those leveraging Large Language Models (LLMs). It addresses the challenges posed by fragmented benchmarks and inconsistent methodologies in web agent research. BrowserGym provides a unified, gym-like environment with clearly defined observation and action spaces, enabling reproducible comparisons across various benchmarks. Additionally, *AgentLab*, a complementary framework, supports agent creation, testing, and analysis. The paper also features a large-scale experiment comparing the performance of 6 leading LLMs, highlighting the strengths and weaknesses of different models in real-world web tasks, while emphasizing the ongoing challenges in building efficient and robust web agents.

- [Beyond Browsing: API-Based Web Agents](https://aclanthology.org/2025.findings-acl.577/)
    - Yueqi Song, Frank Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [benchmark], [WebArena], [SOTA performance]
    - 📖 TLDR: This paper introduces API-based and hybrid agents designed to execute online tasks by accessing both APIs and traditional web browsing interfaces. In evaluations using WebArena, a benchmark for web navigation, the API-based agent achieves higher performance than browser-based agents, and the hybrid model achieves a success rate of 35.8%, setting a new state-of-the-art (SOTA) in task-agnostic web navigation. The findings highlight the efficiency and reliability gains of API interactions for web agents.

- [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2da53cd1abdae59150e35f4693834f32-Abstract-Conference.html)
    - Junpeng Liu, Tianyue Ou, Yifan Song, Yuxiao Qu, Wai Lam, Chenyan Xiong, Wenhu Chen, Graham Neubig, Xiang Yue
    - 🏛️ Institutions: Carnegie Mellon University, The Chinese University of Hong Kong, Peking University, University of Waterloo
    - 📅 Date: October 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [multimodal instruction tuning], [text-rich visual understanding], [web UI], [MultiUI]
    - 📖 TLDR: This paper introduces *MultiUI*, a large-scale dataset containing 7.3 million annotated samples from 1 million websites, specifically designed to enhance multimodal large language models’ (MLLMs) capabilities in text-rich visual understanding. Utilizing webpage UI structures as a training resource, MultiUI provides robust accessibility tree data paired with UI screenshots, significantly improving MLLMs’ grounding, OCR, and interaction performance. Models trained with MultiUI achieve up to a 48% performance boost on VisualWebBench and demonstrate enhanced generalization across non-web tasks, setting a new standard for structured, visually integrated web data modeling.

- [Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a6a6891cf1dfc64d664f086cf5976e93-Abstract-Conference.html)
    - Tianyue Ou, Frank F. Xu, Aman Madaan, Jiarui Liu, Robert Lo, Abishek Sridhar, Sudipta Sengupta, Dan Roth, Graham Neubig, Shuyan Zhou
    - 🏛️ Institutions: Carnegie Mellon University, Amazon Web Services AI
    - 📅 Date: September 24, 2024
    - 📑 Publisher: NeurIPS 2024 (Main Conference Track)
    - 💻 Env: [Web]
    - 🔑 Key: [synthetic data], [synthetic demonstrations], [web navigation], [synatra]
    - 📖 TLDR: Synatra introduces a scalable framework for digital agents, enabling them to convert indirect knowledge sources into actionable demonstrations. This approach enhances the ability of agents to learn tasks without extensive labeled data, leveraging insights from indirect observations to scale practical implementations in digital environments.

- [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
    - Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University, Massachusetts Institute of Technology
    - 📅 Date: September 11, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [memory], [workflow induction], [web navigation], [AWM]
    - 📖 TLDR: The paper proposes *Agent Workflow Memory (AWM)*, a method enabling language model-based agents to induce and utilize reusable workflows from past experiences to guide future actions in web navigation tasks. AWM operates in both offline and online settings, significantly improving performance on benchmarks like Mind2Web and WebArena, and demonstrating robust generalization across tasks, websites, and domains.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web page understanding], [grounding]
    - 📖 TLDR: VisualWebBench introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on web-based tasks. It includes 1.5K human-curated instances across 139 websites in 87 sub-domains. The benchmark spans seven tasks—such as OCR, grounding, and web-based QA—aiming to test MLLMs' capabilities in fine-grained web page understanding. Results reveal significant performance gaps, particularly in grounding tasks, highlighting the need for advancement in MLLM web understanding.

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
