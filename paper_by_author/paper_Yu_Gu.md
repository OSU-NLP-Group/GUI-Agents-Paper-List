# Yu Gu's Papers

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://arxiv.org/abs/2506.21506)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Amazon AGI
    - 📅 Date: June 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agentic search], [Agent-as-a-Judge], [evaluation], [Mind2Web 2]
    - 📖 TLDR: This paper introduces **Mind2Web 2**, a benchmark of 130 long-horizon, real-world tasks requiring web browsing and extensive information synthesis. It proposes an **Agent-as-a-Judge** framework to automatically and rigorously evaluate the correctness and source attribution of answers for agentic search systems. Through a detailed evaluation of nine frontier systems, the paper highlights OpenAI’s Deep Research system as the best performer, achieving 50-70% of human performance while reducing time consumption by half. Mind2Web 2 offers a foundation for benchmarking next-generation agentic search systems.

- [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079)
    - Boyuan Zheng, Michael Y. Fatemi, Xiaolong Jin, Zora Zhiruo Wang, Apurva Gandhi, Yueqi Song, Yu Gu, Jayanth Srinivasa, Gaowen Liu, Graham Neubig, Yu Su
    - 🏛️ Institutions: OSU, CMU, UVA, Purdue, Cisco Research
    - 📅 Date: April 9, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [API synthesis], [skill discovery], [transfer learning], [WebArena]
    - 📖 TLDR: SkillWeaver is a framework that enables web agents to autonomously improve by discovering, practicing, and refining reusable skills, encapsulated as APIs. Through iterative exploration, agents build a library of plug-and-play APIs, enhancing their capabilities. Experiments on WebArena and real-world websites demonstrate significant performance improvements, and the synthesized APIs can be shared among agents to boost overall performance.

- [Magma: A Foundation Model for Multimodal AI Agents](https://microsoft.github.io/Magma/)
    - Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai, Seonghyeon Ye, Joel Jang, Yuquan Deng, Lars Liden, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research, Univ. of Maryland, Univ. of Wisconsin-Madison, KAIST, Univ. of Washington
    - 📅 Date: Feb 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI], [Robotics]
    - 🔑 Key: [model], [framework], [SoM], [ToM], [robotics], [UI navigation]
    - 📖 TLDR: This paper introduces **Magma**, a foundation model designed for multimodal AI agents operating in both digital and physical environments. Magma extends traditional vision-language models by incorporating planning and action capabilities, enabling tasks from UI navigation to robotic manipulation. The model is pretrained on diverse datasets, including images, videos, and robotics data, utilizing **Set-of-Mark (SoM)** for action grounding and **Trace-of-Mark (ToM)** for action planning. Experiments demonstrate that SoM and ToM synergistically enhance Magma's spatial-temporal intelligence, achieving state-of-the-art performance in UI navigation and robotic manipulation tasks.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559)
    - Yu Gu, Boyuan Zheng, Boyu Gou, Kai Zhang, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [WebDreamer], [model-based planning], [world model]
    - 📖 TLDR: This paper investigates whether Large Language Models (LLMs) can function as world models within web environments, enabling model-based planning for web agents. Introducing **WebDreamer**, a framework that leverages LLMs to simulate potential action sequences in web environments, the study demonstrates significant performance improvements over reactive baselines on benchmarks like VisualWebArena and Mind2Web-live. The findings suggest that LLMs possess the capability to model the dynamic nature of the internet, paving the way for advancements in automated web interaction and opening new research avenues in optimizing LLMs for complex, evolving environments.

- [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://arxiv.org/abs/2408.06327)
    - Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Yifan Xu, Xixuan Song, Shudan Zhang, Hanyu Lai, Xinyi Liu, Hanlin Zhao, Jiadai Sun, Xinyue Yang, Yu Yang, Zehan Qi, Shuntian Yao, Xueqiao Sun, Siyi Cheng, Qinkai Zheng, Hao Yu, Hanchen Zhang, Wenyi Hong, Ming Ding, Lihang Pan, Xiaotao Gu, Aohan Zeng, Zhengxiao Du, Chan Hee Song, Yu Su, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, MSRA, The Ohio State University
    - 📅 Date: August 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [VisualAgentBench], [VAB]
    - 📖 TLDR: The authors introduce *VisualAgentBench (VAB)*, a comprehensive benchmark designed to train and evaluate large multimodal models (LMMs) as visual foundation agents across diverse scenarios, including embodied tasks, graphical user interfaces, and visual design. VAB comprises five distinct environments that systematically challenge LMMs' understanding and interaction capabilities. Additionally, the benchmark offers supervised fine-tuning trajectory data for behavior cloning training, demonstrating the potential to improve open LMMs for serving as visual foundation agents.

- [AUITestAgent: Automatic Requirements Oriented GUI Function Testing](https://github.com/bz-lab/AUITestAgent)
    - Yongxiang Hu, Xuan Wang, Yingchuan Wang, Yu Zhang, Shiyu Guo, Chaoyi Chen, Xin Wang, Yangfan Zhou
    - 🏛️ Institutions: Fudan University, Meituan
    - 📅 Date: July 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI testing], [AUITestAgent]
    - 📖 TLDR: This paper presents **AUITestAgent**, the first automatic, natural language-driven GUI testing tool for mobile apps. It automates the entire process of GUI interaction and function verification by extracting GUI interactions from test requirements via dynamically organized agents and employing a multi-dimensional data extraction strategy for verification.

- [AgentBench: Evaluating LLMs as Agents](https://llmbench.ai/agent)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU, ByteDance
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI], [General]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.

- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: June 9, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [model], [Mind2Web], [MindAct]
    - 📖 TLDR: *Mind2Web* presents a dataset and benchmark specifically crafted for generalist web agents capable of performing language-guided tasks across varied websites. Featuring over 2,000 tasks from 137 sites, it spans 31 domains and emphasizes open-ended, realistic tasks in authentic, unsimplified web settings. The study proposes the *MindAct* framework, which optimizes LLMs for handling complex HTML elements by using small LMs to rank elements before full processing, thereby enhancing the efficiency and versatility of web agents in diverse contexts.
