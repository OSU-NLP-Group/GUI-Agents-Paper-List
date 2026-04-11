# Graham Neubig's Papers

- [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588)
    - Faria Huq, Zora Zhiruo Wang, Zhanqiu Guo, Venu Arvind Arangarajan, Tianyue Ou, Frank Xu, Shuyan Zhou, Graham Neubig, Jeffrey P. Bigham
    - 🏛️ Institutions: Carnegie Mellon University, Duke University
    - 📅 Date: February 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [human-agent interaction], [intervention prediction], [interaction styles], [CowCorpus], [collaborative web agents]
    - 📖 TLDR: This paper studies collaborative web agents through human intervention patterns, introducing CowCorpus with 400 real-user trajectories that mix human and agent actions. Modeling four distinct interaction styles substantially improves intervention prediction and raises user-rated usefulness in live agents.

- [Go-Browse: Training Web Agents with Structured Exploration](https://arxiv.org/abs/2506.03533)
    - Apurva Gandhi, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: June 04, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [structured exploration], [graph search], [WebArena], [Go-Browse]
    - 📖 TLDR: This paper frames web-agent data collection as structured exploration over website graphs so agents can reuse information gathered across trajectories instead of exploring each task from scratch. On WebArena, Go-Browse collects 10K successful trajectories and 40K interaction steps across 100 URLs, then uses them to fine-tune a 7B model that surpasses GPT-4o mini and sets a new sub-10B result on the benchmark.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, Carnegie Mellon University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-agent collaboration], [mixed-initiative web navigation], [data collection], [CowPilot]
    - 📖 TLDR: CowPilot is a mixed-initiative web-navigation framework where an agent proposes next steps while the user can pause, reject, override, or hand control back at any time. Across five websites, the collaborative mode reaches the highest success rate while requiring humans to perform only a small fraction of the total steps, and the system is also positioned as a data-collection and evaluation tool.

- [Inducing Programmatic Skills for Agentic Tasks](https://openreview.net/forum?id=lsAY6fWsog)
    - Zora Zhiruo Wang, Apurva Gandhi, Graham Neubig, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University, Microsoft
    - 📅 Date: April 09, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [model], [benchmark], [learning], [reasoning], [planning], [ASI], [WebArena]
    - 📖 TLDR: Proposes Agent Skill Induction (ASI), which induces executable program skills from web interaction experience and reuses them online as tasks evolve. Program-based skills make verification possible during induction, improving both WebArena success rate and step efficiency over static agents and text-skill alternatives while also transferring better across websites.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: The Ohio State University, Carnegie Mellon University, University of Virginia, Purdue University, Cisco Research
    - 📅 Date: April 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [transfer learning], [WebArena]
    - 📖 TLDR: SkillWeaver is a framework that enables web agents to autonomously improve by discovering, practicing, and refining reusable skills, encapsulated as APIs. Through iterative exploration, agents build a library of plug-and-play APIs, enhancing their capabilities. Experiments on WebArena and real-world websites demonstrate significant performance improvements, and the synthesized APIs can be shared among agents to boost overall performance.

- [The BrowserGym Ecosystem for Web Agent Research](https://openreview.net/forum?id=5298fKGmv3)
    - Thibault Le Sellier de Chezelles, Maxime Gasse, Alexandre Lacoste, Massimo Caccia, Alexandre Drouin, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Graham Neubig, Quentin Cappart, Russ Salakhutdinov, Nicolas Chapados
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Carnegie Mellon University, McGill University, Tel Aviv University, Université de Montréal, iMean AI
    - 📅 Date: December 06, 2024
    - 📑 Publisher: TMLR
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [BrowserGym], [AgentLab], [evaluation ecosystem]
    - 📖 TLDR: BrowserGym is a unified ecosystem for web-agent research that standardizes observation/action spaces and wraps multiple existing benchmarks under a common interface. The paper also introduces AgentLab for agent creation and experiment analysis, and uses the ecosystem to run a large cross-benchmark comparison of six frontier LLMs.

- [Beyond Browsing: API-Based Web Agents](https://aclanthology.org/2025.findings-acl.577/)
    - Yueqi Song, Frank Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: October 24, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [WebArena], [API access]
    - 📖 TLDR: Studies what happens when web-agent tasks are solved through APIs instead of only through browsers. The paper proposes both API-only and hybrid agents, and shows that hybrid access to APIs plus browsing substantially outperforms browsing alone on WebArena.

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
    - 🔑 Key: [synthetic data], [synthetic demonstrations], [indirect knowledge], [Synatra]
    - 📖 TLDR: Introduces Synatra, a pipeline for converting indirect knowledge sources such as tutorials into direct demonstrations for digital agents. Using 100k synthetic demonstrations, the paper trains a 7B web agent that outperforms similarly sized models on Mind2Web, MiniWoB++, and WebArena at a small fraction of the cost of human demonstrations.

- [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
    - Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University, Massachusetts Institute of Technology
    - 📅 Date: September 11, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [memory], [workflow induction], [AWM]
    - 📖 TLDR: The paper proposes *Agent Workflow Memory (AWM)*, a method enabling language model-based agents to induce and utilize reusable workflows from past experiences to guide future actions in web navigation tasks. AWM operates in both offline and online settings, significantly improving performance on benchmarks like Mind2Web and WebArena, and demonstrating robust generalization across tasks, websites, and domains.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: April 09, 2024
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
    - 📅 Date: July 25, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [environment], [benchmark], [multi-tab navigation], [realistic web tasks], [WebArena]
    - 📖 TLDR: Introduces WebArena, a realistic and reproducible web environment built from fully functional sites across several common domains. It helped establish the modern web-agent evaluation stack by pairing realistic websites, external tools and knowledge sources, and long-horizon benchmark tasks with functional correctness checks.
