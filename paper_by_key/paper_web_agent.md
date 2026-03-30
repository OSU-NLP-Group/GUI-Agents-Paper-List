# Papers with Keyword: web agent

- [WARC-Bench: Web Archive based Benchmark for GUI Subtask Executions](https://arxiv.org/abs/2510.09872)
    - Sanjari Srivastava, Gang Li, Cheng Chang, Rishu Garg, Manpreet Kaur, Charlene Y. Lee, Yuezhang Li, Yining Mao, Ignacio Cases, Yanan Xie, Peng Qi
    - 🏛️ Institutions: Uniphore
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web agent], [GUI subtask], [reinforcement learning], [WebArchive], [WARC-Bench]
    - 📖 TLDR: This paper introduces WARC-Bench, a web-agent benchmark focused on short-horizon GUI subtasks such as date pickers, scroll containers, and other interface widgets that are essential for larger web workflows. It builds 438 tasks on realistic archived webpages using WARC files and shows that even strong computer-use models struggle on these subtasks. The paper also studies supervised fine-tuning and RL with verifiable rewards, showing that targeted subtask training materially improves open models.

- [How to Train Your LLM Web Agent: A Statistical Diagnosis](https://arxiv.org/abs/2507.04103)
    - Dheeraj Vattikonda, Santhoshi Ravichandran, Emiliano Penaloza, Hadi Nekoei, Megh Thakkar, Thibault Le Sellier de Chezelles, Nicolas Gontier, Miguel Munoz-Marmol, Sahar Omidi Shayegan, Stefania Raimondo, Xue Liu, Alexandre Drouin, Laurent Charlin, Alexandre Piche, Alexandre Lacoste, Massimo Caccia
    - 🏛️ Institutions: ServiceNow AI Research, Mila - Quebec AI Institute, Polytechnique Montreal, HEC Montreal, McGill University, Universite de Montreal
    - 📅 Date: July 5, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [reinforcement learning], [imitation learning], [training analysis], [WorkArena]
    - 📖 TLDR: This paper studies how to post-train open web agents under a strict compute budget, combining supervised imitation from a stronger teacher with on-policy reinforcement learning. Using large hyperparameter sweeps and bootstrapped sensitivity analysis, it provides one of the first statistically grounded compute-allocation studies for LLM web-agent training. The main result is that a mixed SFT-plus-RL pipeline is both more compute efficient and more effective than using either approach alone on WorkArena and MiniWoB++.

- [Go-Browse: Training Web Agents with Structured Exploration](https://arxiv.org/abs/2506.03533)
    - Apurva Gandhi, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: June 4, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [web agent], [structured exploration], [task generation], [WebArena], [Go-Browse]
    - 📖 TLDR: This paper frames web-agent data collection as structured exploration over website graphs so agents can reuse information gathered across trajectories instead of exploring each task from scratch. On WebArena, Go-Browse collects 10K successful trajectories and 40K interaction steps across 100 URLs, then uses them to fine-tune a 7B model that surpasses GPT-4o mini and sets a new sub-10B result on the benchmark.

- [Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents](https://arxiv.org/abs/2505.24878)
    - Yaxin Luo, Zhaoyi Li, Jiacheng Liu, Jiacheng Cui, Xiaohan Zhao, Zhiqiang Shen
    - 🏛️ Institutions: VILA Lab, MBZUAI, MetaAgentX
    - 📅 Date: May 30, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [multimodal agent], [CAPTCHA], [reasoning], [Open CaptchaWorld]
    - 📖 TLDR: This paper introduces Open CaptchaWorld, a web-based benchmark designed to test whether multimodal LLM agents can solve realistic CAPTCHA challenges that block end-to-end web automation. It spans 20 CAPTCHA types and measures both performance and CAPTCHA reasoning depth, capturing the multi-step perceptual and interaction burden of these tasks. The benchmark shows that even strong multimodal agents remain far from human performance on CAPTCHA-heavy web workflows.

- [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)
    - Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: May 28, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [information seeking], [reinforcement learning], [GAIA], [WebDancer]
    - 📖 TLDR: This paper presents WebDancer, an end-to-end web agent for autonomous information seeking built through a data-centric four-stage training pipeline: browsing data construction, trajectory sampling, supervised fine-tuning, and reinforcement learning. It targets long-horizon information-seeking problems rather than short templated web tasks. The resulting system achieves strong performance on GAIA and WebWalkerQA and offers a concrete recipe for training more capable research-style web agents.

- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277)
    - Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
    - 🏛️ Institutions: Georgia Institute of Technology, Yonsei University, Carnegie Mellon University
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [reward model], [web agent], [benchmark], [WebRewardBench], [Web-Shepherd]
    - 📖 TLDR: This paper introduces Web-Shepherd, the first process reward model specialized for web navigation, together with WebPRM Collection and WebRewardBench for training and meta-evaluating web-agent reward models. It shows that a compact specialized verifier can substantially outperform generic frontier models as web-trajectory evaluators while costing much less. The work is directly relevant to reinforcing web agents because it provides both the reward model and the evaluation infrastructure needed for scalable RL or test-time verification.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, Carnegie Mellon University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [human-agent collaboration], [web navigation], [evaluation], [CowPilot]
    - 📖 TLDR: This paper introduces CowPilot, a Chrome-extension framework for mixed-initiative web navigation where an agent proposes actions while a human can pause, reject, override, or resume control during the same task. It is designed both as a collaboration interface and as an evaluation/data-collection platform for web agents. In case studies across five websites, the collaborative setting reaches the highest success rate while substantially reducing the number of steps humans must perform themselves.

- [Infogent: An Agent-Based Framework for Web Information Aggregation](https://aclanthology.org/2025.findings-naacl.318/)
    - Revanth Gangi Reddy, Sagnik Mukherjee, Jeonghwan Kim, Zhenhailong Wang, Dilek Hakkani-Tur, Heng Ji
    - 🏛️ Institutions: University of Illinois at Urbana-Champaign
    - 📅 Date: April 29, 2025
    - 📑 Publisher: Findings of NAACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [information aggregation], [browser navigation], [AssistantBench], [Infogent]
    - 📖 TLDR: This paper targets web information aggregation rather than single-site task completion, asking agents to explore multiple websites and decide when enough evidence has been gathered for a complex query. It introduces Infogent, a modular framework with Navigator, Extractor, and Aggregator components, plus enhanced actions for backtracking and feedback-driven navigation. The framework improves over prior baselines in both API-driven and interactive visual web-access settings, including gains on AssistantBench.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Chuan Guo, Aaron Grattafiori, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Independent Researcher
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [web agent], [prompt injection], [security], [WASP]
    - 📖 TLDR: This paper introduces WASP, a benchmark for end-to-end evaluation of web-agent security against prompt injection attacks in realistic multi-step web tasks. It shows that even strong web agents can be partially deceived at very high rates by simple human-written injections, while also revealing a more nuanced failure mode where agents are often insecure yet too incompetent to fully execute the attacker's goal. The benchmark is designed to measure security under realistic web-agent deployment conditions rather than simplified single-step attacks.

- [AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780)
    - Arman Zharmagambetov, Chuan Guo, Ivan Evtimov, Maya Pavlova, Ruslan Salakhutdinov, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Meta
    - 📅 Date: March 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [privacy], [web agent], [data minimization], [safety], [AgentDAM]
    - 📖 TLDR: This paper introduces AgentDAM, a benchmark for evaluating whether autonomous web agents respect data minimization when using sensitive user information. It measures whether an agent accesses private information only when it is necessary to complete a task, and shows that current web agents frequently leak unnecessary sensitive data. The paper also studies a prompting-based defense, but the main contribution is a realistic end-to-end privacy evaluation setup for autonomous web agents.

- [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents](https://aclanthology.org/2025.findings-acl.326/)
    - Vardaan Pahuja, Yadong Lu, Corby Rosset, Boyu Gou, Arindam Mitra, Spencer Whitehead, Yu Su, Ahmed Hassan Awadallah
    - 🏛️ Institutions: Microsoft Research, The Ohio State University
    - 📅 Date: February 17, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [web agents], [reinforcement learning], [Explorer]
    - 📖 TLDR: This paper introduces *Explorer*, a multimodal web agent trained on a newly synthesized dataset comprising over 94,000 successful web trajectories. The dataset, generated through scalable exploration and refinement techniques, spans 49,000 unique URLs and includes 720,000 screenshots and 33 million web elements. *Explorer* demonstrates strong performance on benchmarks like Mind2Web-Live, Multimodal-Mind2Web, and MiniWob++, highlighting the importance of data scaling in enhancing web agent capabilities.

- [Large Language Models Empowered Personalized Web Agents](https://openreview.net/forum?id=kAzqfqsCC5)
    - Hongru Cai, Yongqi Li, Wenjie Wang, Fengbin Zhu, Xiaoyu Shen, Wenjie Li, Tat-Seng Chua
    - 🏛️ Institutions: The Hong Kong Polytechnic University, Nanyang Technological University
    - 📅 Date: Oct 22, 2024
    - 📑 Publisher: WWW 2025 (Oral)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [personalized web agent], [user behavior alignment], [memory-enhanced alignment]
    - 📖 TLDR: This paper proposes a novel framework, *Personalized User Memory-enhanced Alignment (PUMA)*, enabling large language models to serve as personalized web agents by incorporating user-specific data and historical web interactions. The authors also introduce a benchmark, *PersonalWAB*, to evaluate these agents on various personalized web tasks. Results show that PUMA improves web agent performance by optimizing action execution based on user-specific preferences.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Los Angeles, The University of Chicago, University of Illinois Urbana-Champaign, University of Wisconsin-Madison
    - 📅 Date: September 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [web agent], [EIA]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [OpenAgents: An Open Platform for Language Agents in the Wild](https://openreview.net/forum?id=sKATR2O1Y0)
    - Tianbao Xie, Fan Zhou, Zhoujun Cheng, Peng Shi, Luoxuan Weng, Yitao Liu, Toh Jing Hua, Junning Zhao, Qian Liu, Che Liu, Zeyu Liu, Yiheng Xu, Hongjin Su, Dongchan Shin, Caiming Xiong, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Sea AI Lab, Salesforce Research
    - 📅 Date: October 16, 2023
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [data analysis], [API tools], [web agent], [OpenAgents]
    - 📖 TLDR: This paper introduces OpenAgents, an open-source platform designed to facilitate the use and hosting of language agents in real-world scenarios. It features three agents: Data Agent for data analysis using Python and SQL, Plugins Agent with access to over 200 daily API tools, and Web Agent for autonomous web browsing. OpenAgents aims to provide a user-friendly web interface for general users and a seamless deployment experience for developers and researchers, promoting the development and evaluation of innovative language agents in practical applications.
