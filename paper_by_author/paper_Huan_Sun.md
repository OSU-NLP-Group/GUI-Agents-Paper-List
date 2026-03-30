# Huan Sun's Papers

- [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235)
    - Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, LawZero, Mila - Quebec AI Institute, Universite de Montreal, University of California, Berkeley
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [safety], [red teaming], [unintended behavior], [computer-use agent], [AutoElicit]
    - 📖 TLDR: This paper studies unsafe unintended behaviors in computer-use agents under benign user inputs rather than adversarial prompts. It introduces AutoElicit, an agentic framework that iteratively perturbs realistic benign instructions using execution feedback to surface severe harmful behaviors in frontier CUAs. The results show that even strong CUAs remain broadly susceptible to harmful deviations, establishing a concrete framework for systematically probing unintended safety failures in realistic computer-use settings.

- [WebGuard: Building a Generalizable Guardrail for Web Agents](https://arxiv.org/abs/2507.14293)
    - Boyuan Zheng, Zeyi Liao, Scott Salisbury, Zeyuan Liu, Michael Lin, Qinyuan Zheng, Zifan Wang, Xiang Deng, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU; Scale AI; UCB
    - 📅 Date: July 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [safety], [guardrail], [WebGuard]
    - 📖 TLDR: Autonomous web agents powered by LLMs can take unintended or harmful actions when interacting with websites (especially state-changing ones). WebGuard is introduced as a dataset to assess risks of web agent actions by collecting nearly 5,000 human‑annotated actions across many real websites, labeled by risk level (SAFE / LOW / HIGH). Baseline LLMs do poorly (<60% accuracy / recall) on detecting high‑risk actions; after fine‑tuning (using Qwen2.5VL‑7B), performance improves significantly (accuracy ~80%, recall on HIGH ~76%), though still not sufficient for very high‑stakes settings. The paper highlights that reliable guardrails for web agents remain an open challenge.

- [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://arxiv.org/abs/2506.21506)
    - Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Amazon AGI
    - 📅 Date: June 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [agentic search], [Agent-as-a-Judge], [evaluation], [Mind2Web 2]
    - 📖 TLDR: This paper introduces **Mind2Web 2**, a benchmark of 130 long-horizon, real-world tasks requiring web browsing and extensive information synthesis. It proposes an **Agent-as-a-Judge** framework to automatically and rigorously evaluate the correctness and source attribution of answers for agentic search systems. Through a detailed evaluation of nine frontier systems, the paper highlights OpenAI’s Deep Research system as the best performer, achieving 50-70% of human performance while reducing time consumption by half. Mind2Web 2 offers a foundation for benchmarking next-generation agentic search systems.

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://arxiv.org/abs/2505.21936)
    - Zeyi Liao, Jaylen Jones, Linxi Jiang, Eric Fosler‑Lussier, Yu Su, Zhiqiang Lin, Huan Sun
    - 🏛️ Institutions: OSU
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [indirect prompt injection], [security], [CUA], [RTC‑Bench]
    - 📖 TLDR: Proposes **RedTeamCUA**, a hybrid VM‑OS + Docker‑web sandbox enabling realistic evaluation of computer‑use agents (CUAs) under indirect prompt injection. Introduces **RTC‑Bench**, a benchmark with 864 adversarial scenarios across hybrid web‑OS paths. Testing reveals high attack success rates (up to ~66%) against frontier CUAs like Claude and Operator, even end-to‑end (ASR ~48% on Claude 4). Highlights urgent need for robust defense mechanisms.

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://arxiv.org/abs/2504.01382)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, UC Berkeley
    - 📅 Date: April 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [Online-Mind2Web], [WebJudge], [Operator], [LLM-as-a-Judge]
    - 📖 TLDR: This paper critically evaluates the performance of current web agents, revealing that many underperform on the newly introduced **Online-Mind2Web** benchmark, which comprises 300 realistic tasks across 136 websites. The study highlights a discrepancy between reported successes and actual capabilities, attributing this to shortcomings in existing benchmarks. To address evaluation scalability, the authors propose **WebJudge**, an automatic LLM-based evaluation method achieving approximately 85% agreement with human judgments. The comprehensive analysis underscores the need for more robust assessment frameworks in web agent research.

- [WebOlympus: An Open Platform for Web Agents on Live Websites](https://aclanthology.org/2024.emnlp-demo.20/)
    - Boyuan Zheng, Boyu Gou, Scott Salisbury, Zheng Du, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: November 12, 2024
    - 📑 Publisher: EMNLP 2024
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [Chrome extension], [WebOlympus], [SeeAct], [Annotation Tool]
    - 📖 TLDR: This paper introduces *WebOlympus*, an open platform designed to facilitate the research and deployment of web agents on live websites. It features a user-friendly Chrome extension interface, allowing users without programming expertise to operate web agents with minimal effort. The platform incorporates a safety monitor module to prevent harmful actions through human supervision or model-based control, supporting applications such as annotation interfaces for web agent trajectories and data crawling.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559)
    - Yu Gu, Boyuan Zheng, Boyu Gou, Kai Zhang, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [WebDreamer], [model-based planning], [world model]
    - 📖 TLDR: This paper investigates whether Large Language Models (LLMs) can function as world models within web environments, enabling model-based planning for web agents. Introducing **WebDreamer**, a framework that leverages LLMs to simulate potential action sequences in web environments, the study demonstrates significant performance improvements over reactive baselines on benchmarks like VisualWebArena and Mind2Web-live. The findings suggest that LLMs possess the capability to model the dynamic nature of the internet, paving the way for advancements in automated web interaction and opening new research avenues in optimizing LLMs for complex, evolving environments.

- [AdvWeb: Controllable Black-box Attacks on VLM-powered Web Agents](https://ai-secure.github.io/AdvWeb/)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: UIUC, OSU
    - 📅 Date: September 27, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [black-box attack], [adversarial prompter model], [Direct Policy Optimization]
    - 📖 TLDR: This paper presents AdvWeb, a black-box attack framework that exploits vulnerabilities in vision-language model (VLM)-powered web agents by injecting adversarial prompts directly into web pages. Using Direct Policy Optimization (DPO), AdvWeb trains an adversarial prompter model that can mislead agents into executing harmful actions, such as unauthorized financial transactions, while maintaining high stealth and control. Extensive evaluations reveal that AdvWeb achieves high success rates across multiple real-world tasks, emphasizing the need for stronger security measures in web agent deployments.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://arxiv.org/abs/2409.11295)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: OSU, UCLA, UChicago, UIUC, UW-Madison
    - 📅 Date: September 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [environmental injection], [stealth attack]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://www.catalyzex.com/paper/a-trembling-house-of-cards-mapping)
    - Lingbo Mo, Zeyi Liao, Boyuan Zheng, Yu Su, Chaowei Xiao, Huan Sun
    - 🏛️ Institutions: OSU, UWM
    - 📅 Date: February 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [adversarial attacks], [security risks], [language agents], [Perception-Brain-Action]
    - 📖 TLDR: This paper introduces a conceptual framework to assess and understand adversarial vulnerabilities in language agents, dividing the agent structure into three components—Perception, Brain, and Action. It discusses 12 specific adversarial attack types that exploit these components, ranging from input manipulation to complex backdoor and jailbreak attacks. The framework provides a basis for identifying and mitigating risks before the widespread deployment of these agents in real-world applications.

- [AgentBench: Evaluating LLMs as Agents](https://llmbench.ai/agent)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU, ByteDance
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI], [General]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://osu-nlp-group.github.io/SeeAct/)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [grounding], [SeeAct], [Multimodal-Mind2web]
    - 📖 TLDR: This paper explores the capability of GPT-4V(ision), a multimodal model, as a web agent that can perform tasks across various websites by following natural language instructions. It introduces the **SEEACT** framework, enabling GPT-4V to navigate, interpret, and interact with elements on websites. Evaluated using the **Mind2Web** benchmark and an online test environment, the framework demonstrates high performance on complex web tasks by integrating grounding strategies like element attributes and image annotations to improve HTML element targeting. However, grounding remains challenging, presenting opportunities for further improvement.

- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: June 9, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [model], [Mind2Web], [MindAct]
    - 📖 TLDR: *Mind2Web* presents a dataset and benchmark specifically crafted for generalist web agents capable of performing language-guided tasks across varied websites. Featuring over 2,000 tasks from 137 sites, it spans 31 domains and emphasizes open-ended, realistic tasks in authentic, unsimplified web settings. The study proposes the *MindAct* framework, which optimizes LLMs for handling complex HTML elements by using small LMs to rank elements before full processing, thereby enhancing the efficiency and versatility of web agents in diverse contexts.
