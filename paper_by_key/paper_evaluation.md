# Papers with Keyword: evaluation

- [AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild](https://arxiv.org/abs/2602.11750)
    - Jiazheng Sun, Mingxuan Li, Yingying Zhang, Jiayang Niu, Yachen Wu, Ruihan Jin, Shuyu Lei, Pengrongrui Tan, Zongyu Zhang, Ruoyi Wang, Jiachen Yang, Boyu Yang, Jiacheng Liu, Xin Peng
    - 🏛️ Institutions: Fudan University, Jilin University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [mobile GUI agent], [agent-user interaction], [MUSE], [AmbiBench]
    - 📖 TLDR: This paper introduces AmbiBench, a mobile GUI agent benchmark designed to move beyond idealized one-shot instructions toward realistic intent alignment. It organizes tasks by instruction clarity, includes 240 tasks across 25 applications, and evaluates not only execution success but also interaction quality through the MUSE judge framework. The benchmark highlights how current mobile agents struggle when users are ambiguous or incomplete, and reframes mobile agent evaluation around bidirectional interaction rather than pure instruction following.

- [SMAN-Bench: A Cross-System Benchmark for Mobile Agents under Single- and Multi-path, Ambiguous, and Noisy Tasks](https://openreview.net/forum?id=IWDpCaSF9Q)
    - Weikai Xu, Zhizheng Jiang, Yuxuan Liu, Pengzhi Gao, Wei Liu, Jian Luan, Yuanchun Li, Yunxin Liu, Bin Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, University of Electronic Science and Technology of China, Gaoling School of Artificial Intelligence Renmin University of China, MiLM Plus Xiaomi Inc., Institute for AI Industry Research Tsinghua University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile GUI agent], [multi-path evaluation], [ambiguous instruction], [noisy environment], [SMAN-Bench]
    - 📖 TLDR: This paper introduces SMAN-Bench, a mobile-agent benchmark that moves beyond single golden trajectories by evaluating single-path, multi-path, ambiguous, and noisy task settings in one framework. It builds instructions from an existing graph-structured mobile corpus, adds offline multi-path reward evaluation, and explicitly includes noisy pop-up-heavy environments plus clarification-style ambiguous tasks. The benchmark is designed to better reflect realistic mobile-agent deployment conditions than cleaner or purely online settings.

- [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)
    - Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir, Zachary S. Siegel, Boyi Wei, Tianci Xue, Ziru Chen, Felix Chen, Saiteja Utpala, Franck Ndzomga, Dheeraj Oruganty, Sophie Luskin, Kangheng Liu, Botao Yu, Amit Arora, Dongyoon Hahm, Harsh Trivedi, Huan Sun, Juyong Lee, Tengjun Jin, Yifan Mai, Yifei Zhou, Yuxuan Zhu, Rishi Bommasani, Daniel Kang, Dawn Song, Peter Henderson, Yu Su, Percy Liang, Arvind Narayanan
    - 🏛️ Institutions: Princeton University, The Ohio State University, Stanford University, University of California, Berkeley
    - 📅 Date: October 13, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [evaluation], [leaderboard], [evaluation harness], [web navigation], [HAL]
    - 📖 TLDR: This paper introduces HAL, an evaluation harness and leaderboard infrastructure for AI agents that standardizes large-scale, distributed benchmarking across models, scaffolds, and benchmarks. Beyond aggregate scores, it also tracks costs and uses LLM-aided log inspection to uncover failure modes and benchmark gaming behaviors. Although broader than GUI agents alone, it is directly relevant to computer-use evaluation because it includes web-navigation-style agent benchmarks and focuses on reliable real-world agent assessment.

- [Say One Thing, Do Another? Diagnosing Reasoning‑Execution Gaps in VLM‑Powered Mobile‑Use Agents](https://arxiv.org/abs/2510.02204)
    - Lingzhong Dong, Ziqi Zhou, Shuaibo Yang, Haiyue Sheng, Pengzhou Cheng, Zongru Wu, Zheng Wu, Gongshen Liu, Zhuosheng Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University, Beijing Institute of Technology
    - 📅 Date: October 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [evaluation framework], [Ground-Truth Alignment], [reasoning-execution gap], [chain-of-thought], [VLM]
    - 📖 TLDR: This paper investigates reasoning-execution mismatches in VLM-powered mobile agents, revealing that models often generate correct reasoning but fail in execution. It introduces an evaluation framework combining execution accuracy and a new metric called Ground-Truth Alignment (GTA). The authors identify two types of errors—Execution Gap and Reasoning Gap—and show that model scaling alleviates but does not resolve these issues.

- [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670)
    - Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
    - 🏛️ Institutions: Microsoft Research AI Frontiers, Microsoft AI Red Team, University of California, Riverside, NVIDIA
    - 📅 Date: October 2, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer-use agent], [blind goal-directedness], [BLIND-ACT], [risk evaluation]
    - 📖 TLDR: This paper identifies Blind Goal-Directedness as a recurring failure mode in computer-use agents, where agents keep pursuing user goals despite infeasibility, ambiguity, or unsafe context. It introduces BLIND-ACT, a benchmark built on OSWorld to evaluate these subtle safety failures in realistic desktop environments. The results show high rates of blind goal pursuit across frontier CUAs, making the paper directly relevant to safety evaluation of GUI agents beyond prompt injection alone.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: September 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets & Benchmarks Track)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agentic search], [Agent-as-a-Judge], [evaluation], [Mind2Web 2]
    - 📖 TLDR: This paper introduces **Mind2Web 2**, a benchmark of 130 long-horizon, real-world tasks requiring web browsing and extensive information synthesis. It proposes an **Agent-as-a-Judge** framework to automatically and rigorously evaluate the correctness and source attribution of answers for agentic search systems. Through a detailed evaluation of nine frontier systems, the paper highlights OpenAI’s Deep Research system as the best performer, achieving 50-70% of human performance while reducing time consumption by half. Mind2Web 2 offers a foundation for benchmarking next-generation agentic search systems.

- [MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers](https://arxiv.org/abs/2508.14704)
    - Ziyang Luo, Zhiqi Shen, Wenzhuo Yang, Zirui Zhao, Prathyusha Jwalapuram, Amrita Saha, Doyen Sahoo, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: August 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [benchmark], [dataset], [framework], [long-horizon reasoning], [unknown-tools challenge], [execution-based evaluation], [MCP-Universe]
    - 📖 TLDR: MCP-Universe introduces the first comprehensive benchmark for evaluating large language models (LLMs) through interactions with real-world Model Context Protocol (MCP) servers. It spans six core domains—Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, and Web Searching—across 11 MCP servers. The benchmark employs execution-based evaluators (format, static, dynamic) to rigorously assess agent performance. Despite progress, state-of-the-art models like GPT-5 (43.72% success), Grok-4 (33.33%), and Claude-4.0-Sonnet (29.44%) show significant limitations. The benchmark highlights challenges in long-context reasoning and unfamiliar tool handling, and provides an open-source extensible evaluation framework with UI support to accelerate future research. 

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [computer-use agent], [OSWorld], [RiOSWorld]
    - 📖 TLDR: This paper introduces RiOSWorld, a benchmark for evaluating safety risks in multimodal computer-use agents during realistic computer manipulation. It covers 492 risky tasks across applications such as web, social media, multimedia, email, office software, and operating-system interactions, and evaluates both harmful intent and harmful task completion. The benchmark shows that current computer-use agents remain exposed to substantial real-world safety risks even when they are aligned for ordinary dialogue settings.

- [DeepShop: A Benchmark for Deep Research Shopping Agents](https://arxiv.org/abs/2506.02839)
    - Yougang Lyu, Xiaoyu Zhang, Lingyong Yan, Maarten de Rijke, Zhaochun Ren, Xiuying Chen
    - 🏛️ Institutions: U Amsterdam, Shandong U, Baidu Inc., Leiden U, MBZUAI
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation framework], [RAG], [query complexity], [DeepShop]
    - 📖 TLDR: DeepShop introduces a comprehensive benchmark for web shopping agents, mirroring the real first-use complexity of online shopping scenarios. It features diversified query evolution across five domains, complexity-tier classification (easy/medium/hard), and a fine‐grained scoring system analyzing attribute matching, filters, and sorting. Evaluations across RAG and agentic systems reveal significant shortcomings, especially in handling filters and sorting, underscoring gaps in current research capabilities.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [computer-use agent], [OSWorld], [RiOSWorld]
    - 📖 TLDR: This paper introduces RiOSWorld, a benchmark for evaluating safety risks in multimodal computer-use agents during realistic computer manipulation. It covers 492 risky tasks across applications such as web, social media, multimedia, email, office software, and operating-system interactions, and evaluates both harmful intent and harmful task completion. The benchmark shows that current computer-use agents remain exposed to substantial real-world safety risks even when they are aligned for ordinary dialogue settings.

- [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://aclanthology.org/2025.naacl-demo.17/)
    - Faria Huq, Zora Zhiruo Wang, Frank F. Xu, Tianyue Ou, Shuyan Zhou, Jeffrey P. Bigham, Graham Neubig
    - 🏛️ Institutions: School of Computer Science, Carnegie Mellon University
    - 📅 Date: April 30, 2025
    - 📑 Publisher: NAACL 2025 (System Demonstrations)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [web agent], [human-agent collaboration], [web navigation], [evaluation], [CowPilot]
    - 📖 TLDR: This paper introduces CowPilot, a Chrome-extension framework for mixed-initiative web navigation where an agent proposes actions while a human can pause, reject, override, or resume control during the same task. It is designed both as a collaboration interface and as an evaluation/data-collection platform for web agents. In case studies across five websites, the collaborative setting reaches the highest success rate while substantially reducing the number of steps humans must perform themselves.

- [REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)
    - Divyansh Garg, Shaun VanWeelden, Diego Caples, Andis Draguns, Nikil Ravi, Pranav Putta, Naman Garg, Tomas Abraham, Michael Lara, Federico Lopez, James Liu, Atharva Gundawar, Prannay Hebbar, Youngchul Joo, Jindong Gu, Charles London, Christian Schroeder de Witt, Sumeet Motwani
    - 🏛️ Institutions: The AGI Company, Stanford University, University of Oxford, Mercor, Contramont Research, Plato, Independent
    - 📅 Date: April 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [dataset], [evaluation], [reproducibility], [multi-turn tasks], [REAL]
    - 📖 TLDR: This paper introduces **REAL**, a benchmark and framework designed for evaluating autonomous agents through deterministic simulations of real-world websites. REAL encompasses high-fidelity replicas of 11 widely-used websites across domains like e-commerce, travel, communication, and professional networking. It includes 112 practical tasks that mirror complex user interactions requiring both accurate information retrieval and state-changing actions. The controlled environment ensures safety and reproducibility, combining programmatic checks for action-based tasks with rubric-guided LLM-based judgments for information retrieval. Empirical results reveal that current frontier language models achieve at most a 41% success rate on REAL, highlighting significant gaps in autonomous web navigation and task completion capabilities.

- [AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://arxiv.org/abs/2504.08942)
    - Xing Han Lù, Amirhossein Kazemnejad, Nicholas Meade, Arkil Patel, Dongchan Shin, Alejandra Zambrano, Karolina Stańczak, Peter Shaw, Christopher J. Pal, Siva Reddy
    - 🏛️ Institutions: McGill, Mila, Google DeepMind, Polytechnique Montréal, ServiceNow Research
    - 📅 Date: April 11, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [LLM judges], [AgentRewardBench]
    - 📖 TLDR: This paper introduces *AgentRewardBench*, a benchmark designed to assess the effectiveness of large language model (LLM) judges in evaluating web agent trajectories. The benchmark comprises 1,302 trajectories across five web benchmarks, each annotated by experts for success, side effects, and repetitiveness. Evaluations of 12 LLM judges reveal that no single model excels across all benchmarks, and that rule-based evaluations often underreport agent success rates, highlighting the need for more adaptable automatic evaluation methods.

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://openreview.net/forum?id=6jZi4HSs6o)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: April 2, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [Online-Mind2Web], [WebJudge], [Operator], [LLM-as-a-Judge]
    - 📖 TLDR: This paper critically evaluates the performance of current web agents, revealing that many underperform on the newly introduced **Online-Mind2Web** benchmark, which comprises 300 realistic tasks across 136 websites. The study highlights a discrepancy between reported successes and actual capabilities, attributing this to shortcomings in existing benchmarks. To address evaluation scalability, the authors propose **WebJudge**, an automatic LLM-based evaluation method achieving approximately 85% agreement with human judgments. The comprehensive analysis underscores the need for more robust assessment frameworks in web agent research.

- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis](https://arxiv.org/abs/2502.20383)
    - Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
    - 🏛️ Institutions: University of Maryland
    - 📅 Date: March 4, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [security], [jailbreaking], [evaluation], [OpenHands]
    - 📖 TLDR: This paper investigates why Web AI agents are significantly more susceptible to executing harmful commands compared to standalone LLMs, despite sharing the same underlying models. Through a fine-grained evaluation, the authors identify three critical factors contributing to this vulnerability: embedding user goals into system prompts, multi-step action generation, and processing of event streams from web navigation. The study introduces a five-level harmfulness evaluation framework and utilizes the OpenHands platform to systematically assess these vulnerabilities, revealing a 46.6% success rate in malicious task execution by Web AI agents versus 0% for standalone LLMs.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: University of Cambridge, Huawei Noah's Ark Lab, University College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [evaluation], [AppVLM], [on-device control]
    - 📖 TLDR: This paper introduces **AppVLM**, a lightweight Vision-Language Model designed for efficient on-device control of smartphone applications. AppVLM is fine-tuned on the AndroidControl dataset and further refined through interactions within the AndroidWorld environment. It achieves superior action prediction accuracy in offline evaluations and matches GPT-4o in online task completion success rates, while operating up to ten times faster, making it a practical solution for real-world deployment.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, The University of Texas at Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [evaluation], [Android emulator]
    - 📖 TLDR: *MobileSafetyBench* introduces a benchmark for evaluating the safety of large language model (LLM)-based autonomous agents in mobile device control. Using Android emulators, the benchmark simulates real-world tasks in apps such as messaging and banking to assess agents' safety and helpfulness. The safety-focused tasks test for privacy risk management and robustness against adversarial prompt injections. Experiments show agents perform well in helpful tasks but struggle with safety-related challenges, underscoring the need for continued advancements in mobile safety mechanisms for autonomous agents.

- [CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents](https://aclanthology.org/2025.findings-acl.1113/)
    - Tianqi Xu, Linyao Chen, Dai-Jie Wu, Yanjun Chen, Zecheng Zhang, Xiang Yao, Zhiqiang Xie, Yongchao Chen, Shilong Liu, Bochen Qian, Anjie Yang, Zhaoxuan Jin, Jianbo Deng, Philip Torr, Bernard Ghanem, Guohao Li
    - 🏛️ Institutions: King Abdullah University of Science and Technology, The University of Tokyo, Carnegie Mellon University, Stanford University, Harvard University, Tsinghua University, Southern University of Science and Technology, University of Oxford
    - 📅 Date: July 3, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [cross-environment], [graph-based evaluation], [task generation], [CRAB]
    - 📖 TLDR: The authors present *CRAB*, a benchmark framework designed to evaluate Multimodal Language Model agents across multiple environments. It features a graph-based fine-grained evaluation method and supports automatic task generation, addressing limitations in existing benchmarks.

- [Identifying User Goals from UI Trajectories](https://arxiv.org/abs/2406.14314)
    - Omri Berkovitch, Sapir Caduri, Noam Kahlon, Anatoly Efros, Avi Caciularu, Ido Dagan
    - 🏛️ Institutions: Google Research, Bar-Ilan University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [evaluation metric], [intent identification]
    - 📖 TLDR: This paper introduces the task of goal identification from observed UI trajectories, aiming to infer the user's intended task based on their GUI interactions. It proposes a novel evaluation metric to assess whether two task descriptions are paraphrases within a specific UI environment. Experiments utilizing the Android-In-The-Wild and Mind2Web datasets reveal that state-of-the-art models, such as GPT-4 and Gemini-1.5 Pro, underperform compared to humans, indicating significant room for improvement.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: iMean AI, Carnegie Mellon University
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [Mind2Web-Live], [key-node evaluation]
    - 📖 TLDR: This paper presents WebCanvas, an online evaluation framework for web agents designed to address the dynamic nature of web interactions. It introduces a key-node-based evaluation metric to capture critical actions or states necessary for task completion while disregarding noise from insignificant events or changed web elements. The framework includes the Mind2Web-Live dataset, a refined version of the original Mind2Web static dataset, containing 542 tasks with 2,439 intermediate evaluation states. Despite advancements, the best-performing model achieves a task success rate of 23.1%, highlighting substantial room for improvement.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Automation Task Evaluation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: April 12, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [UI automation], [mobile agent evaluation]
    - 📖 TLDR: LlamaTouch is an evaluation testbed designed for mobile UI automation, enabling reliable task assessment across 495 annotated tasks. It provides a scalable solution to evaluate agents in real-world mobile settings, comparing agent actions to essential UI states for accurate task completion. LlamaTouch supports dynamic environments, advancing mobile agent reliability and scalability in task automation.

- [Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)
    - Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
    - 🏛️ Institutions: University of California, Berkeley, University of Michigan
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [evaluation model], [domain transfer]
    - 📖 TLDR: This paper presents an autonomous evaluation framework for digital agents to enhance performance on web navigation and device control. The study introduces modular, cost-effective evaluators achieving up to 92.9% accuracy in benchmarks like WebArena and outlines their use in fine-tuning agents, improving state-of-the-art by 29% without additional supervision.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://aclanthology.org/2024.acl-long.50/)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [dataset], [multimodal agent evaluation], [visually grounded tasks]
    - 📖 TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://aclanthology.org/2024.acl-long.371/)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab, Westlake University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: This paper introduces WebVoyager, an innovative web agent powered by Large Multimodal Models (LMMs) that can complete user instructions end-to-end by interacting with real-world websites. The authors establish a new benchmark with tasks from 15 popular websites and propose an automatic evaluation protocol using GPT-4V. WebVoyager achieves a 59.1% task success rate, significantly outperforming GPT-4 (All Tools) and text-only setups. The study demonstrates the effectiveness of multimodal approaches in web automation and provides insights into developing more intelligent web interaction solutions.

- [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, ByteDance
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI], [General]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.
