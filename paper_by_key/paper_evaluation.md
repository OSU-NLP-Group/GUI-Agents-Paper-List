# Papers with Keyword: evaluation

- [REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://realevals.xyz)
    - Divyansh Garg, Shaun VanWeelden, Diego Caples, Andis Draguns, Nikil Ravi, Pranav Putta, Naman Garg, Tomas Abraham, Michael Lara, Federico Lopez, James Liu, Atharva Gundawar, Prannay Hebbar, Youngchul Joo, Charles London, Christian Schroeder de Witt, Sumeet Motwani
    - 🏛️ Institutions: AGI Inc.
    - 📅 Date: April 15, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [dataset], [evaluation], [reproducibility], [multi-turn tasks], [REAL]
    - 📖 TLDR: This paper introduces **REAL**, a benchmark and framework designed for evaluating autonomous agents through deterministic simulations of real-world websites. REAL encompasses high-fidelity replicas of 11 widely-used websites across domains like e-commerce, travel, communication, and professional networking. It includes 112 practical tasks that mirror complex user interactions requiring both accurate information retrieval and state-changing actions. The controlled environment ensures safety and reproducibility, combining programmatic checks for action-based tasks with rubric-guided LLM-based judgments for information retrieval. Empirical results reveal that current frontier language models achieve at most a 41% success rate on REAL, highlighting significant gaps in autonomous web navigation and task completion capabilities.

- [AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://agent-reward-bench.github.io/)
    - Xing Han Lù, Amirhossein Kazemnejad, Nicholas Meade, Arkil Patel, Dongchan Shin, Alejandra Zambrano, Karolina Stańczak, Peter Shaw, Christopher J. Pal, Siva Reddy
    - 🏛️ Institutions: McGill, Mila, Google DeepMind, Polytechnique Montréal, ServiceNow Research
    - 📅 Date: April 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [LLM judges], [AgentRewardBench]
    - 📖 TLDR: This paper introduces *AgentRewardBench*, a benchmark designed to assess the effectiveness of large language model (LLM) judges in evaluating web agent trajectories. The benchmark comprises 1,302 trajectories across five web benchmarks, each annotated by experts for success, side effects, and repetitiveness. Evaluations of 12 LLM judges reveal that no single model excels across all benchmarks, and that rule-based evaluations often underreport agent success rates, highlighting the need for more adaptable automatic evaluation methods.

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://arxiv.org/abs/2504.01382)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, UC Berkeley
    - 📅 Date: April 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [Online-Mind2Web], [WebJudge], [Operator], [LLM-as-a-Judge]
    - 📖 TLDR: This paper critically evaluates the performance of current web agents, revealing that many underperform on the newly introduced **Online-Mind2Web** benchmark, which comprises 300 realistic tasks across 136 websites. The study highlights a discrepancy between reported successes and actual capabilities, attributing this to shortcomings in existing benchmarks. To address evaluation scalability, the authors propose **WebJudge**, an automatic LLM-based evaluation method achieving approximately 85% agreement with human judgments. The comprehensive analysis underscores the need for more robust assessment frameworks in web agent research.

- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis](https://vulnerable-ai-agents.github.io/)
    - Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
    - 🏛️ Institutions: UMD
    - 📅 Date: March 4, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [security], [jailbreaking], [evaluation], [OpenHands]
    - 📖 TLDR: This paper investigates why Web AI agents are significantly more susceptible to executing harmful commands compared to standalone LLMs, despite sharing the same underlying models. Through a fine-grained evaluation, the authors identify three critical factors contributing to this vulnerability: embedding user goals into system prompts, multi-step action generation, and processing of event streams from web navigation. The study introduces a five-level harmfulness evaluation framework and utilizes the OpenHands platform to systematically assess these vulnerabilities, revealing a 46.6% success rate in malicious task execution by Web AI agents versus 0% for standalone LLMs.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Univ. of Cambridge, Huawei Noah's Ark Lab, Univ. College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [framework], [evaluation], [AppVLM], [on-device control]
    - 📖 TLDR: This paper introduces **AppVLM**, a lightweight Vision-Language Model designed for efficient on-device control of smartphone applications. AppVLM is fine-tuned on the AndroidControl dataset and further refined through interactions within the AndroidWorld environment. It achieves superior action prediction accuracy in offline evaluations and matches GPT-4o in online task completion success rates, while operating up to ten times faster, making it a practical solution for real-world deployment.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, UT at Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [evaluation], [Android emulator]
    - 📖 TLDR: *MobileSafetyBench* introduces a benchmark for evaluating the safety of large language model (LLM)-based autonomous agents in mobile device control. Using Android emulators, the benchmark simulates real-world tasks in apps such as messaging and banking to assess agents' safety and helpfulness. The safety-focused tasks test for privacy risk management and robustness against adversarial prompt injections. Experiments show agents perform well in helpful tasks but struggle with safety-related challenges, underscoring the need for continued advancements in mobile safety mechanisms for autonomous agents.

- [CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents](https://arxiv.org/abs/2407.01511)
    - Tianqi Xu, Linyao Chen, Dai-Jie Wu, Yanjun Chen, Zecheng Zhang, Xiang Yao, Zhiqiang Xie, Yongchao Chen, Shilong Liu, Bochen Qian, Philip Torr, Bernard Ghanem, Guohao Li
    - 🏛️ Institutions: KAUST, UTokyo, CMU, Stanford, Harvard, Tsinghua University, SUSTech, Oxford
    - 📅 Date: July 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [framework], [evaluation], [CRAB]
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
    - 🏛️ Institutions: iMean AI, CMU
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [Mind2Web-Live], [key-node evaluation]
    - 📖 TLDR: This paper presents WebCanvas, an online evaluation framework for web agents designed to address the dynamic nature of web interactions. It introduces a key-node-based evaluation metric to capture critical actions or states necessary for task completion while disregarding noise from insignificant events or changed web elements. The framework includes the Mind2Web-Live dataset, a refined version of the original Mind2Web static dataset, containing 542 tasks with 2,439 intermediate evaluation states. Despite advancements, the best-performing model achieves a task success rate of 23.1%, highlighting substantial room for improvement.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Automation Task Evaluation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: BUPT, Tsinghua University
    - 📅 Date: April 12, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [UI automation], [mobile agent evaluation]
    - 📖 TLDR: LlamaTouch is an evaluation testbed designed for mobile UI automation, enabling reliable task assessment across 495 annotated tasks. It provides a scalable solution to evaluate agents in real-world mobile settings, comparing agent actions to essential UI states for accurate task completion. LlamaTouch supports dynamic environments, advancing mobile agent reliability and scalability in task automation.

- [Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)
    - Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
    - 🏛️ Institutions: UCB, UMich
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [evaluation model], [domain transfer]
    - 📖 TLDR: This paper presents an autonomous evaluation framework for digital agents to enhance performance on web navigation and device control. The study introduces modular, cost-effective evaluators achieving up to 92.9% accuracy in benchmarks like WebArena and outlines their use in fine-tuning agents, improving state-of-the-art by 29% without additional supervision.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: CMU
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [dataset], [multimodal agent evaluation], [visually grounded tasks]
    - 📖 TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab, Westlake University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: This paper introduces WebVoyager, an innovative web agent powered by Large Multimodal Models (LMMs) that can complete user instructions end-to-end by interacting with real-world websites. The authors establish a new benchmark with tasks from 15 popular websites and propose an automatic evaluation protocol using GPT-4V. WebVoyager achieves a 59.1% task success rate, significantly outperforming GPT-4 (All Tools) and text-only setups. The study demonstrates the effectiveness of multimodal approaches in web automation and provides insights into developing more intelligent web interaction solutions.

- [AgentBench: Evaluating LLMs as Agents](https://llmbench.ai/agent)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU, ByteDance
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI], [General]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.
