# Tao Yu's Papers

- [Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System](https://arxiv.org/abs/2602.10915)
    - Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Tao Yu, Kun Zhang
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: February 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile agent], [agent security], [prompt injection], [access control], [operating system], [benchmark]
    - 📖 TLDR: This paper conducts a systematic security analysis of GUI-based mobile agents (using Doubao Mobile Assistant as a case study), identifying vulnerabilities across identity, perception, cognition, and execution dimensions, and proposes Aura, an Agent Universal Runtime Architecture that replaces GUI scraping with a structured intent-driven interaction model secured by cryptographic identity, semantic firewalls, taint-aware memory, and granular access control, achieving 94.3% task success rate while reducing attack success rate to 4.4% on MobileSafetyBench.

- [VideoAgentTrek: Computer Use Pretraining from Unlabeled Videos](https://arxiv.org/abs/2510.19488)
    - Dunjie Lu, Yiheng Xu, Junli Wang, Haoyuan Wu, Xinyuan Wang, Zekun Wang, Junlin Yang, Hongjin Su, Jixuan Chen, Junda Chen, Yuchen Mao, Jingren Zhou, Junyang Lin, Binyuan Hui, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Qwen Team, Alibaba Group
    - 📅 Date: October 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [pretraining], [computer-use agent], [video mining], [inverse dynamics], [OSWorld-verified], [VideoAgentTrek], [Video2Action]
    - 📖 TLDR: This paper introduces VideoAgentTrek, a scalable pipeline that converts unlabeled screen-recorded videos into structured computer-use trajectories for pretraining GUI agents. Its Video2Action inverse-dynamics module first localizes GUI actions in time and then recovers structured action parameters such as click coordinates and typed text. Mining 39,000 YouTube tutorials yields 1.52 million interaction steps, and using this data for continued pretraining substantially improves downstream performance on OSWorld-Verified and AgentNetBench.

- [BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions](https://arxiv.org/abs/2510.10666)
    - Tao Yu, Zhengbo Zhang, Zhiheng Lyu, Junhao Gong, Hongzhu Yi, Xinming Wang, Yuxuan Zhou, Jiabing Yang, Ping Nie, Yan Huang, Wenhu Chen
    - 🏛️ Institutions: CASIA, University of Chinese Academy of Sciences (UCAS), University of Waterloo, Peking University, Tsinghua University
    - 📅 Date: 2025-10-14
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [browser automation], [SFT], [rejection fine-tuning], [memory mechanism], [open-domain QA]
    - 📖 TLDR: BrowserAgent is a web agent framework that uses human-inspired browser actions (scrolling, clicking, typing) via Playwright to solve complex tasks, trained with a two-stage SFT+RFT pipeline and an explicit memory mechanism, achieving ~20% improvement over Search-R1 on multi-hop QA benchmarks.

- [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)
    - Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir, Zachary S. Siegel, Boyi Wei, Tianci Xue, Ziru Chen, Felix Chen, Saiteja Utpala, Franck Ndzomga, Dheeraj Oruganty, Sophie Luskin, Kangheng Liu, Botao Yu, Amit Arora, Dongyoon Hahm, Harsh Trivedi, Huan Sun, Juyong Lee, Tengjun Jin, Yifan Mai, Yifei Zhou, Yuxuan Zhu, Rishi Bommasani, Daniel Kang, Dawn Song, Peter Henderson, Yu Su, Percy Liang, Arvind Narayanan
    - 🏛️ Institutions: Princeton University, The Ohio State University, Stanford University, University of California, Berkeley
    - 📅 Date: October 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [evaluation], [leaderboard], [evaluation harness], [web navigation], [HAL]
    - 📖 TLDR: This paper introduces HAL, an evaluation harness and leaderboard infrastructure for AI agents that standardizes large-scale, distributed benchmarking across models, scaffolds, and benchmarks. Beyond aggregate scores, it also tracks costs and uses LLM-aided log inspection to uncover failure modes and benchmark gaming behaviors. Although broader than GUI agents alone, it is directly relevant to computer-use evaluation because it includes web-navigation-style agent benchmarks and focuses on reliable real-world agent assessment.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets & Benchmarks Track)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agentic search], [agent-as-a-judge], [evaluation], [Mind2Web 2]
    - 📖 TLDR: This paper introduces **Mind2Web 2**, a benchmark of 130 long-horizon, real-world tasks requiring web browsing and extensive information synthesis. It proposes an **Agent-as-a-Judge** framework to automatically and rigorously evaluate the correctness and source attribution of answers for agentic search systems. Through a detailed evaluation of nine frontier systems, the paper highlights OpenAI’s Deep Research system as the best performer, achieving 50-70% of human performance while reducing time consumption by half. Mind2Web 2 offers a foundation for benchmarking next-generation agentic search systems.

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y. Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Moonshot AI, Stanford University, University of Waterloo, Carnegie Mellon University
    - 📅 Date: August 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [chain-of-thought], [vision language model], [AgentNet]
    - 📖 TLDR: Introduces **OpenCUA**, an open-source framework to train computer-use agents (CUAs) using vision-language models. It includes a cross-platform annotation tool (AgentNet Tool), a large-scale dataset covering 3 OSes and 200+ apps/websites (AgentNet), and a data processing pipeline that builds state-action pairs enhanced with reflective long chain-of-thought reasoning. The resulting models—especially OpenCUA-72B—achieve SOTA performance on the OSWorld-Verified benchmark (45.0% success), surpassing prior open-source baselines and demonstrating strong generalization and scalability. All tools, models, and data are publicly released.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Salesforce Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets and Benchmarks Track (Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [benchmark], [framework], [jedi], [OSWorld‑G], [GUI grounding], [compositional generalization], [fine‑grained manipulation]
    - 📖 TLDR: This work tackles limitations in GUI grounding by introducing **OSWorld‑G**, a 564‑sample benchmark covering text matching, element recognition, layout understanding, fine‑grained manipulation, and refusal detection. They also synthesize **Jedi**, a massive 4 M‑example dataset generated via UI decomposition and synthesis. Training multi‑scale models on Jedi achieves state‑of‑the‑art grounding across benchmarks (ScreenSpot‑v2/Pro and OSWorld‑G), boosting agentic task performance from 5 % to ~27 % success. Ablations demonstrate compositional benefits. All artifacts are publicly released.

- [TongUI: Building Generalized GUI Agents by Learning from Multimodal Web Tutorials](https://arxiv.org/abs/2504.12679)
    - Bofei Zhang, Zirui Shang, Zhi Gao, Wang Zhang, Rui Xie, Xiaojian Ma, Tao Yuan, Xinxiao Wu, Song-Chun Zhu, Qing Li
    - 🏛️ Institutions: Beijing Institute for General Artificial Intelligence, Beijing Institute of Technology, Peking University, Shanghai Jiao Tong University, Tsinghua University
    - 📅 Date: April 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [Qwen2.5-VL], [GUI-net], [multimodal], [trajectory generation]
    - 📖 TLDR: This paper introduces **TongUI**, a framework for building generalized GUI agents by learning from multimodal web tutorials. By crawling and processing online tutorials into GUI agent trajectory data, the authors construct the **GUI-Net** dataset containing 143K trajectories across five operating systems and over 200 applications. Fine-tuning Qwen2.5-VL-3B/7B models on GUI-Net leads to significant performance improvements on grounding and navigation benchmarks, demonstrating the effectiveness of the TongUI framework.

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: The University of Hong Kong, Nanyang Technological University, Salesforce
    - 📅 Date: Dec 5, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [planning], [reasoning], [aguvis], [visual grounding]
    - 📖 TLDR: This paper introduces *Aguvis*, a unified pure vision-based framework for autonomous GUI agents that operates across various platforms. It leverages image-based observations and grounds natural language instructions to visual elements, employing a consistent action space to ensure cross-platform generalization. The approach integrates explicit planning and reasoning within the model, enhancing its ability to autonomously navigate and interact with complex digital environments. A large-scale dataset of GUI agent trajectories is constructed, incorporating multimodal reasoning and grounding. Comprehensive experiments demonstrate that Aguvis surpasses previous state-of-the-art methods in both offline and real-world online scenarios, achieving the first fully autonomous pure vision GUI agent capable of performing tasks independently without collaboration with external closed-source models. All datasets, models, and training recipes are open-sourced to facilitate future research.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Institute of Technology, The University of Hong Kong, Stanford University
    - 📅 Date: Nov 4, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [attack], [adversarial pop-ups], [VLM agents], [safety]
    - 📖 TLDR: This paper demonstrates that vision-language model (VLM) agents can be easily deceived by carefully designed adversarial pop-ups, leading them to perform unintended actions such as clicking on these pop-ups instead of completing their assigned tasks. Integrating these pop-ups into environments like OSWorld and VisualWebArena resulted in an average attack success rate of 86% and a 47% decrease in task success rate. Basic defense strategies, such as instructing the agent to ignore pop-ups or adding advertisement notices, were found to be ineffective against these attacks.

- [Language Agents: Foundations, Prospects, and Risks](https://aclanthology.org/2024.emnlp-tutorials.3/)
    - Yu Su, Diyi Yang, Shunyu Yao, Tao Yu
    - 🏛️ Institutions: The Ohio State University, Stanford University, Princeton University, The University of Hong Kong
    - 📅 Date: November 2024
    - 📑 Publisher: EMNLP 2024 Tutorial Abstracts
    - 💻 Env: [Misc]
    - 🔑 Key: [survey], [tutorial], [reasoning], [planning], [memory], [multi-agent systems], [safety]
    - 📖 TLDR: This tutorial provides a comprehensive exploration of language agents—autonomous systems powered by large language models capable of executing complex tasks through language instructions. It delves into their theoretical foundations, potential applications, associated risks, and future directions, covering topics such as reasoning, memory, planning, tool augmentation, grounding, multi-agent systems, and safety considerations.

- [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c2f71567cd53464161cab3336e8fc865-Abstract-Datasets_and_Benchmarks_Track.html)
    - Ruisheng Cao, Fangyu Lei, Haoyuan Wu, Jixuan Chen, Yeqiao Fu, Hongcheng Gao, Xinzhuang Xiong, Hanchong Zhang, Yuchen Mao, Wenjing Hu, Tianbao Xie, Hongsheng Xu, Danyang Zhang, Sida Wang, Ruoxi Sun, Pengcheng Yin, Caiming Xiong, Ansong Ni, Qian Liu, Victor Zhong, Lu Chen, Kai Yu, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Shanghai Jiao Tong University, Google Cloud AI Research, Google DeepMind, Salesforce Research, Yale University, Sea AI Lab, University of Waterloo
    - 📅 Date: July 15, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [data science], [engineering workflows], [Spider2-v]
    - 📖 TLDR: This paper introduces **Spider2-V**, a multimodal agent benchmark designed to evaluate the capability of agents in automating professional data science and engineering workflows. It comprises 494 real-world tasks across 20 enterprise-level applications, assessing agents' proficiency in code generation and GUI operations within authentic computer environments.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Jing Hua Toh, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Carnegie Mellon University, Salesforce Research, University of Waterloo
    - 📅 Date: April 11, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [real computer tasks], [online environment], [online benchmark]
    - 📖 TLDR: OSWorld introduces a groundbreaking benchmark for multimodal agents to perform open-ended tasks within real computer environments across platforms like Ubuntu, Windows, and macOS. It includes 369 real-world tasks involving web and desktop apps, file management, and multi-app workflows, with custom evaluation scripts for reproducibility. The results reveal current agents’ limitations in GUI interaction and operational knowledge, as they achieve just 12.24% task success compared to humans' 72.36%, highlighting critical gaps for future model improvement.

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)
    - Zhiyong Wu, Chengcheng Han, Zichen Ding, Zhenmin Weng, Zhoumianze Liu, Shunyu Yao, Tao Yu, Lingpeng Kong
    - 🏛️ Institutions: Shanghai AI Laboratory, East China Normal University, Princeton University, The University of Hong Kong
    - 📅 Date: February 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [self-directed learning], [GAIA], [FRIDAY], [OS-copilot]
    - 📖 TLDR: The OS-Copilot framework supports building generalist agents capable of performing diverse tasks across an operating system (OS). This work introduces FRIDAY, an embodied agent using OS-Copilot to self-improve by learning from task outcomes. It operates with a memory-based architecture to tackle OS-level tasks across applications like terminals, web browsers, and third-party tools. Tested on the GAIA benchmark, FRIDAY achieved 35% higher performance than prior methods, proving effective in adapting to unfamiliar applications and refining its capabilities with minimal guidance.

- [OpenAgents: An Open Platform for Language Agents in the Wild](https://openreview.net/forum?id=sKATR2O1Y0)
    - Tianbao Xie, Fan Zhou, Zhoujun Cheng, Peng Shi, Luoxuan Weng, Yitao Liu, Toh Jing Hua, Junning Zhao, Qian Liu, Che Liu, Zeyu Liu, Yiheng Xu, Hongjin Su, Dongchan Shin, Caiming Xiong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Sea AI Lab, Salesforce Research
    - 📅 Date: October 16, 2023
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [data analysis], [API tools], [web agent], [OpenAgents]
    - 📖 TLDR: This paper introduces OpenAgents, an open-source platform designed to facilitate the use and hosting of language agents in real-world scenarios. It features three agents: Data Agent for data analysis using Python and SQL, Plugins Agent with access to over 200 daily API tools, and Web Agent for autonomous web browsing. OpenAgents aims to provide a user-friendly web interface for general users and a seamless deployment experience for developers and researchers, promoting the development and evaluation of innovative language agents in practical applications.

- [AutoDroid: LLM-powered Task Automation in Android](https://doi.org/10.1145/3636534.3649379)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - 🏛️ Institutions: Tsinghua University, Shanghai AI Laboratory, University of Notre Dame, Microsoft Research
    - 📅 Date: August 29, 2023
    - 📑 Publisher: MobiCom 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [Android task automation], [LLM-powered agent]
    - 📖 TLDR: This paper introduces AutoDroid, a novel mobile task automation system capable of handling arbitrary tasks on any Android application without manual efforts. The framework combines the commonsense knowledge of LLMs with domain-specific knowledge of apps through automated dynamic analysis. AutoDroid features a functionality-aware UI representation method, exploration-based memory injection techniques, and a multi-granularity query optimization module. Evaluated on a new benchmark with 158 common tasks, AutoDroid achieves a 90.9% action generation accuracy and a 71.3% task completion rate, significantly outperforming GPT-4-powered baselines.
