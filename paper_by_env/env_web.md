- [The BrowserGym Ecosystem for Web Agent Research](https://arxiv.org/abs/2412.05467)
    - Thibault Le Sellier De Chezelles, Maxime Gasse, Alexandre Drouin, Massimo Caccia, Léo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Quentin Cappart, Graham Neubig, Ruslan Salakhutdinov, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal ,CMU, McGill University, Tel Aviv University,Université de Montréal, iMean AI
    - 📅 Date: December 6, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [LLM], [automation], [BrowserGym], [AgentLab]
    - 📖 TLDR: This paper presents *BrowserGym*, an ecosystem designed to standardize the evaluation and benchmarking of web agents, particularly those leveraging Large Language Models (LLMs). It addresses the challenges posed by fragmented benchmarks and inconsistent methodologies in web agent research. BrowserGym provides a unified, gym-like environment with clearly defined observation and action spaces, enabling reproducible comparisons across various benchmarks. Additionally, *AgentLab*, a complementary framework, supports agent creation, testing, and analysis. The paper also features a large-scale experiment comparing the performance of 6 leading LLMs, highlighting the strengths and weaknesses of different models in real-world web tasks, while emphasizing the ongoing challenges in building efficient and robust web agents.

- [AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://arxiv.org/abs/2411.13451)
    - Gaurav Verma, Rachneet Kaur, Nishan Srishankar, Zhen Zeng, Tucker Balch, Manuela Veloso
    - 🏛️ Institutions: J.P. Morgan AI Research
    - 📅 Date: November 24, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [few-shot learning], [meta-learning], [AdaptAgent]
    - 📖 TLDR: This paper introduces **AdaptAgent**, a framework that enables multimodal web agents to adapt to new websites and domains using few human demonstrations (up to 2). The approach enhances agents' adaptability beyond large-scale pre-training and fine-tuning by leveraging in-context learning and meta-learning techniques. Experiments on benchmarks like Mind2Web and VisualWebArena show that incorporating minimal human demonstrations boosts task success rates significantly, highlighting the effectiveness of multimodal demonstrations over text-only ones and the impact of data selection strategies during meta-learning on agent generalization.

- [WebOlympus: An Open Platform for Web Agents on Live Websites](https://aclanthology.org/2024.emnlp-demo.20/)
    - Boyuan Zheng, Boyu Gou, Scott Salisbury, Zheng Du, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: November 12, 2024
    - 📑 Publisher: EMNLP 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [safety], [Chrome extension], [WebOlympus]
    - 📖 TLDR: This paper introduces *WebOlympus*, an open platform designed to facilitate the research and deployment of web agents on live websites. It features a user-friendly Chrome extension interface, allowing users without programming expertise to operate web agents with minimal effort. The platform incorporates a safety monitor module to prevent harmful actions through human supervision or model-based control, supporting applications such as annotation interfaces for web agent trajectories and data crawling.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559)
    - Yu Gu, Boyuan Zheng, Boyu Gou, Kai Zhang, Cheng Chang, Sanjari Srivastava, Yanan Xie, Peng Qi, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Orby AI
    - 📅 Date: November 10, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [WebDreamer], [model-based planning], [world model], [web agents]
    - 📖 TLDR: This paper investigates whether Large Language Models (LLMs) can function as world models within web environments, enabling model-based planning for web agents. Introducing **WebDreamer**, a framework that leverages LLMs to simulate potential action sequences in web environments, the study demonstrates significant performance improvements over reactive baselines on benchmarks like VisualWebArena and Mind2Web-live. The findings suggest that LLMs possess the capability to model the dynamic nature of the internet, paving the way for advancements in automated web interaction and opening new research avenues in optimizing LLMs for complex, evolving environments.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337v1)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Xinyue Yang, Jiadai Sun, Yu Yang, Shuntian Yao, Tianjie Zhang, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, BAAI
    - 📅 Date: November 4, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [RL], [self-evolving curriculum], [WebRL], [outcome-supervised reward model]
    - 📖 TLDR: This paper introduces *WebRL*, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open large language models (LLMs). WebRL addresses challenges such as the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. It incorporates a self-evolving curriculum that generates new tasks from unsuccessful attempts, a robust outcome-supervised reward model (ORM), and adaptive reinforcement learning strategies to ensure consistent improvements. Applied to Llama-3.1 and GLM-4 models, WebRL significantly enhances their performance on web-based tasks, surpassing existing state-of-the-art web agents.

- [From Context to Action: Analysis of the Impact of State Representation and Context on the Generalization of Multi-Turn Web Navigation Agents](https://arxiv.org/abs/2409.13701)
    - Nalin Tiwary, Vardhan Dongre, Sanil Arun Chawla, Ashwin Lamani, Dilek Hakkani-Tür
    - 🏛️ Institutions: UIUC
    - 📅 Date: October 31, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [context management], [generalization], [multi-turn navigation], [CWA]
    - 📖 TLDR: This study examines how different contextual elements affect the performance and generalization of Conversational Web Agents (CWAs) in multi-turn web navigation tasks. By optimizing context management—specifically interaction history and web page representation—the research demonstrates enhanced agent performance across various out-of-distribution scenarios, including unseen websites, categories, and geographic locations.

- [Evaluating Cultural and Social Awareness of LLM Web Agents](https://arxiv.org/abs/2410.23252)
    - Haoyi Qiu, Alexander R. Fabbri, Divyansh Agarwal, Kung-Hsiang Huang, Sarah Tan, Nanyun Peng, Chien-Sheng Wu
    - 🏛️ Institutions: UCLA, Salesforce AI Research
    - 📅 Date: October 30, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [CASA], [cultural awareness], [social awareness], [fine-tuning], [prompting]
    - 📖 TLDR: This paper introduces CASA, a benchmark designed to assess the cultural and social awareness of LLM web agents in tasks like online shopping and social discussion forums. It evaluates agents' abilities to detect and appropriately respond to norm-violating user queries and observations. The study finds that current LLM agents have limited cultural and social awareness, with less than 10% awareness coverage and over 40% violation rates. To enhance performance, the authors explore prompting and fine-tuning methods, demonstrating that combining both can offer complementary advantages.

- [Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/abs/2410.22552)
    - Jaekyeom Kim, Dong-Ki Kim, Lajanugen Logeswaran, Sungryull Sohn, Honglak Lee
    - 🏛️ Institutions: LG AI Research, Field AI, University of Michigan
    - 📅 Date: October 29, 2024
    - 📑 Publisher: EMNLP 2024 (Findings)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [Auto-Intent]
    - 📖 TLDR: The paper presents Auto-Intent, a method to adapt pre-trained large language models for web navigation tasks without direct fine-tuning. It discovers underlying intents from domain demonstrations and trains an intent predictor to enhance decision-making. Auto-Intent improves the performance of GPT-3.5, GPT-4, and Llama-3.1 agents on benchmarks like Mind2Web and WebArena.

- [OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization](https://doi.org/10.48550/arXiv.2410.19609)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Hongming Zhang, Tianqing Fang, Zhenzhong Lan, Dong Yu
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab, Westlake University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [learning], [imitation learning], [exploration], [AI feedback]
    - 📖 TLDR: The paper presents **OpenWebVoyager**, an open-source framework for training web agents that explore real-world online environments autonomously. The framework employs a cycle of exploration, feedback, and optimization, enhancing agent capabilities through multimodal perception and iterative learning. Initial skills are acquired through imitation learning, followed by real-world exploration, where the agent’s performance is evaluated and refined through feedback loops.

- [Beyond Browsing: API-Based Web Agents](https://arxiv.org/pdf/2410.16464)
    - Yueqi Song, Frank Xu, Shuyan Zhou, Graham Neubig
    - 🏛️ Institutions: CMU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [API-based agent], [hybrid agent], [benchmark], [WebArena], [SOTA performance]
    - 📖 TLDR: This paper introduces API-based and hybrid agents designed to execute online tasks by accessing both APIs and traditional web browsing interfaces. In evaluations using WebArena, a benchmark for web navigation, the API-based agent achieves higher performance than browser-based agents, and the hybrid model achieves a success rate of 35.8%, setting a new state-of-the-art (SOTA) in task-agnostic web navigation. The findings highlight the efficiency and reliability gains of API interactions for web agents.

- [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://doi.org/10.48550/arXiv.2410.19100)
    - Lawrence Jang, Yinheng Li, Charles Ding, Justin Lin, Paul Pu Liang, Dan Zhao, Rogerio Bonatti, Kazuhito Koishida
    - 🏛️ Institutions: CMU, MIT, NYU, Microsoft
    - 📅 Date: October 24, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [video understanding], [long-context], [VideoWA]
    - 📖 TLDR: This paper introduces **VideoWebArena (VideoWA)**, a benchmark assessing multimodal agents in video-based tasks. It features over 2,000 tasks focused on skill and factual retention, using video tutorials to simulate long-context environments. Results highlight current challenges in agentic abilities, providing a critical testbed for long-context video understanding improvements.

- [Large Language Models Empowered Personalized Web Agents](https://ar5iv.org/abs/2410.17236)
    - Hongru Cai, Yongqi Li, Wenjie Wang, Fengbin Zhu, Xiaoyu Shen, Wenjie Li, Tat-Seng Chua
    - 🏛️ Institutions: HK PolyU, NTU Singapore
    - 📅 Date: Oct 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [personalized web agent], [user behavior alignment], [memory-enhanced alignment]
    - 📖 TLDR: This paper proposes a novel framework, *Personalized User Memory-enhanced Alignment (PUMA)*, enabling large language models to serve as personalized web agents by incorporating user-specific data and historical web interactions. The authors also introduce a benchmark, *PersonalWAB*, to evaluate these agents on various personalized web tasks. Results show that PUMA improves web agent performance by optimizing action execution based on user-specific preferences.

- [AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://arxiv.org/abs/2407.15711)
    - Ori Yoran, Samuel Joseph Amouyal, Chaitanya Malaviya, Ben Bogin, Ofir Press, Jonathan Berant
    - 🏛️ Institutions: Tel Aviv University
    - 📅 Date: October 21, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [planning and reasoning]
    - 📖 TLDR: AssistantBench is a benchmark designed to test the abilities of web agents in completing time-intensive, realistic web-based tasks. Covering 214 tasks across various domains, the benchmark introduces the SPA (See-Plan-Act) framework to handle multi-step planning and memory retention. AssistantBench emphasizes realistic task completion, showing that current agents achieve only modest success, with significant improvements needed for complex information synthesis and execution across multiple web domains.

- [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://arxiv.org/abs/2410.13824)
    - Junpeng Liu, Tianyue Ou, Yifan Song, Yuxiao Qu, Wai Lam, Chenyan Xiong, Wenhu Chen, Graham Neubig, Xiang Yue
    - 🏛️ Institutions: CMU
    - 📅 Date: October 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [model], [text-rich visual understanding], [web UI comprehension]
    - 📖 TLDR: This paper introduces *MultiUI*, a large-scale dataset containing 7.3 million annotated samples from 1 million websites, specifically designed to enhance multimodal large language models’ (MLLMs) capabilities in text-rich visual understanding. Utilizing webpage UI structures as a training resource, MultiUI provides robust accessibility tree data paired with UI screenshots, significantly improving MLLMs’ grounding, OCR, and interaction performance. Models trained with MultiUI achieve up to a 48% performance boost on VisualWebBench and demonstrate enhanced generalization across non-web tasks, setting a new standard for structured, visually integrated web data modeling.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2404.03648)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU
    - 📅 Date: October 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [reinforcement learning], [web-based tasks]
    - 📖 TLDR: AutoWebGLM introduces a web navigation agent based on ChatGLM3-6B, designed to autonomously navigate and interact with webpages for complex tasks. The paper highlights a two-phase data construction approach using a hybrid human-AI methodology for diverse, curriculum-based web task training. It also presents AutoWebBench, a benchmark for evaluating agent performance in web tasks, and uses reinforcement learning to fine-tune operations, addressing complex webpage interaction and grounding.

- [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://sites.google.com/view/st-webagentbench/home)
    - Ido Levy, Ben Wiesel, Sami Marreed, Alon Oved, Avi Yaeli, Segev Shlomov
    - 🏛️ Institutions: IBM Research
    - 📅 Date: October 9, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [trustworthiness], [ST-WebAgentBench]
    - 📖 TLDR: This paper introduces **ST-WebAgentBench**, a benchmark designed to evaluate the safety and trustworthiness of web agents in enterprise contexts. It defines safe and trustworthy agent behavior, outlines the structure of safety policies, and introduces the "Completion under Policies" metric to assess agent performance. The study reveals that current state-of-the-art agents struggle with policy adherence, highlighting the need for improved policy awareness and compliance in web agents.

- [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://agent-e3.github.io/ExACT/)
    - Xiao Yu, Baolin Peng, Vineeth Vajipey, Hao Cheng, Michel Galley, Jianfeng Gao, Zhou Yu
    - 🏛️ Institutions: Columbia Univ., Microsoft Research
    - 📅 Date: Oct 2, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [learning], [R-MCTS], [Exploratory Learning], [VisualWebArena]
    - 📖 TLDR: This paper introduces ExACT, an approach that combines Reflective Monte Carlo Tree Search (R-MCTS) and Exploratory Learning to enhance AI agents' exploration and decision-making capabilities in complex web environments. R-MCTS incorporates contrastive reflection and multi-agent debate for improved search efficiency and reliable state evaluation. Evaluated on the VisualWebArena benchmark, the GPT-4o-based R-MCTS agent demonstrates significant performance improvements over previous state-of-the-art methods. Additionally, knowledge gained from test-time search is effectively transferred back to GPT-4o through fine-tuning, enabling the model to explore, evaluate, and backtrack without external search algorithms, achieving 87% of R-MCTS's performance with reduced computational resources.

- [AdvWeb: Controllable Black-box Attacks on VLM-powered Web Agents](https://ai-secure.github.io/AdvWeb/)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: UIUC, OSU
    - 📅 Date: September 27, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safty], [black-box attack], [adversarial prompter model], [Direct Policy Optimization]
    - 📖 TLDR: This paper presents AdvWeb, a black-box attack framework that exploits vulnerabilities in vision-language model (VLM)-powered web agents by injecting adversarial prompts directly into web pages. Using Direct Policy Optimization (DPO), AdvWeb trains an adversarial prompter model that can mislead agents into executing harmful actions, such as unauthorized financial transactions, while maintaining high stealth and control. Extensive evaluations reveal that AdvWeb achieves high success rates across multiple real-world tasks, emphasizing the need for stronger security measures in web agent deployments.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://arxiv.org/abs/2409.11295)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: OSU, UCLA, UChicago, UIUC, UW-Madison
    - 📅 Date: September 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [environmental injection], [stealth attack]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)
    - Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig
    - 🏛️ Institutions: CMU, MIT
    - 📅 Date: September 11, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [memory], [AWM]
    - 📖 TLDR: The paper proposes *Agent Workflow Memory (AWM)*, a method enabling language model-based agents to induce and utilize reusable workflows from past experiences to guide future actions in web navigation tasks. AWM operates in both offline and online settings, significantly improving performance on benchmarks like Mind2Web and WebArena, and demonstrating robust generalization across tasks, websites, and domains.

- [From Grounding to Planning: Benchmarking Bottlenecks in Web Agents](https://arxiv.org/abs/2409.01927)
    - Segev Shlomov, Ben Wiesel, Aviad Sela, Ido Levy, Liane Galanti, Roy Abitbol
    - 🏛️ Institutions: IBM
    - 📅 Date: September 3, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [planning], [grounding], [Mind2Web dataset], [web navigation]
    - 📖 TLDR: This paper analyzes performance bottlenecks in web agents by separately evaluating grounding and planning tasks, isolating their individual impacts on navigation efficacy. Using an enhanced version of the Mind2Web dataset, the study reveals planning as a significant bottleneck, with advancements in grounding and task-specific benchmarking for elements like UI component recognition. Through experimental adjustments, the authors propose a refined evaluation framework, aiming to enhance web agents' contextual adaptability and accuracy in complex web environments.

- [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199)
    - Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
    - 🏛️ Institutions: MultiOn, Stanford
    - 📅 Date: August 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [MCTS], [Tree Search], [DPO], [Reinforcement Learning]. [RL]
    - 📖 TLDR: TBD

- [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032)
    - Aditya Vempaty, [Other authors not provided in the search results]
    - 🏛️ Institutions: Emergence AI
    - 📅 Date: July 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [autonomous web navigation], [hierarchical architecture], [DOM distillation]
    - 📖 TLDR: This paper presents Agent-E, a novel web agent that introduces several architectural improvements over previous state-of-the-art systems. Key features include a hierarchical architecture, flexible DOM distillation and denoising methods, and a "change observation" concept for improved performance. Agent-E outperforms existing text and multi-modal web agents by 10-30% on the WebVoyager benchmark. The authors synthesize their findings into general design principles for developing agentic systems, including the use of domain-specific primitive skills, hierarchical architectures, and agentic self-improvement.

- [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://arxiv.org/abs/2407.05291)
    - Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, Alexandre Drouin
    - 🏛️ Institutions: ServiceNow Research, Mila, Polytechnique Montréal, Université de Montréal
    - 📅 Date: July 7, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [planning], [reasoning], [WorkArena++]
    - 📖 TLDR: This paper introduces **WorkArena++**, a benchmark comprising 682 tasks that simulate realistic workflows performed by knowledge workers. It evaluates web agents' capabilities in planning, problem-solving, logical/arithmetic reasoning, retrieval, and contextual understanding. The study reveals challenges faced by current large language models and vision-language models in serving as effective workplace assistants, providing a resource to advance autonomous agent development. [oai_citation_attribution:0‡arXiv](https://arxiv.org/abs/2407.05291?utm_source=chatgpt.com)

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - 🏛️ Institutions: Zhejiang University, iMean AI, University of Washington
    - 📅 Date: June 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [Mind2Web-Live], [key-node evaluation]
    - 📖 TLDR: This paper presents WebCanvas, an online evaluation framework for web agents designed to address the dynamic nature of web interactions. It introduces a key-node-based evaluation metric to capture critical actions or states necessary for task completion while disregarding noise from insignificant events or changed web elements. The framework includes the Mind2Web-Live dataset, a refined version of the original Mind2Web static dataset, containing 542 tasks with 2,439 intermediate evaluation states. Despite advancements, the best-performing model achieves a task success rate of 23.1%, highlighting substantial room for improvement.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://arxiv.org/abs/2406.10227)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen Wu, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Z. Shou
    - 🏛️ Institutions: Unknown
    - 📅 Date: June 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [Desktop, Web]
    - 🔑 Key: [benchmark], [instructional videos], [visual planning], [hierarchical task decomposition], [complex software interaction]
    - 📖 TLDR: VideoGUI presents a benchmark for evaluating GUI automation on tasks derived from instructional videos, focusing on visually intensive applications like Adobe Photoshop and video editing software. The benchmark includes 178 tasks, with a hierarchical evaluation method distinguishing high-level planning, mid-level procedural steps, and precise action execution. VideoGUI reveals current model limitations in complex visual tasks, marking a significant step toward improved visual planning in GUI automation.

- [WebSuite: Systematically Evaluating Why Web Agents Fail](https://arxiv.org/abs/2406.01623)
    - Eric Li, Jim Waldo
    - 🏛️ Institutions: Harvard
    - 📅 Date: June 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [web agents], [failure analysis], [analysis], [task disaggregation]
    - 📖 TLDR: This paper introduces *WebSuite*, a diagnostic benchmark to investigate the causes of web agent failures. By categorizing agent tasks using a taxonomy of operational, informational, and navigational actions, WebSuite offers granular insights into the specific actions where agents struggle, like filtering or form completion. It enables detailed comparison across agents, identifying areas for architectural and UX adaptation to improve agent reliability and task success on the web.

- [Large Language Models Can Self-Improve At Web Agent Tasks](https://arxiv.org/abs/2405.20309)
    - Ajay Patel, Markus Hofmarcher, Claudiu Leoveanu-Condrei, Marius-Constantin Dinu, Chris Callison-Burch, Sepp Hochreiter
    - 🏛️ Institutions: University of Pennsylvania, ExtensityAI, Johannes Kepler University Linz, NXAI
    - 📅 Date: May 30, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [self-improvement], [self-improve]
    - 📖 TLDR: This paper investigates the ability of large language models (LLMs) to enhance their performance as web agents through self-improvement. Utilizing the WebArena benchmark, the authors fine-tune LLMs on synthetic training data, achieving a 31% improvement in task completion rates. They also introduce novel evaluation metrics to assess the performance, robustness, and quality of the fine-tuned agents' trajectories.

- [Unveiling Disparities in Web Task Handling Between Human and Web Agent](https://arxiv.org/abs/2405.04497)
    - Kihoon Son, Jinhyeon Kwon, DaEun Choi, Tae Soo Kim, Young-Ho Kim, Sangdoo Yun, Juho Kim
    - 🏛️ Institutions: KAIST, Seoul National University
    - 📅 Date: May 7, 2024
    - 📑 Publisher: CHI 2024 Workshop
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [cognitive comparison], [task analysis]
    - 📖 TLDR: This paper examines how humans and web agents differ in handling web-based tasks, focusing on key aspects such as planning, action-taking, and reflection. Using a think-aloud protocol, the study highlights the cognitive processes humans employ, like exploration and adjustment, versus the more rigid task execution patterns observed in web agents. The authors identify several limitations in current web agents, proposing the need for improved frameworks to enhance adaptability and knowledge update mechanisms in agent-based systems.

- [Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2405.00516)
    - Lucas Thil, Samy Aittahar, Yassine Hadjadj-Aoul, Gerardo Rubino
    - 🏛️ Institutions: Unknown
    - 📅 Date: May 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [large language models], [reinforcement learning]
    - 📖 TLDR: This paper proposes a novel approach combining supervised learning (SL) and reinforcement learning (RL) techniques to train web navigation agents using large language models. The authors address limitations in previous models' understanding of HTML content and introduce methods to enhance true comprehension. Their approach, evaluated on the MiniWoB benchmark, outperforms previous SL methods on certain tasks using less data and narrows the performance gap with RL models. The study achieves 43.58% average accuracy in SL and 36.69% when combined with a multimodal RL approach, setting a new direction for future web navigation research.

- [Search Beyond Queries: Training Smaller Language Models for Web Interactions via Reinforcement Learning](https://arxiv.org/abs/2404.10887)
    - Moghis Fereidouni, A.B. Siddique
    - 🏛️ Institutions: Unknown
    - 📅 Date: April 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [grounded language agent], [Flan-T5], [unsupervised domain adaptation]
    - 📖 TLDR: This paper introduces GLAINTEL, a grounded language agent framework designed to enhance web interaction using instruction-finetuned language models, particularly Flan-T5, with reinforcement learning (PPO) to tackle interactive web navigation challenges. The study explores unsupervised and supervised training methods, evaluating the effects of human demonstration on agent performance. Results indicate that combining human feedback with reinforcement learning yields effective outcomes, rivaling larger models like GPT-4 on web navigation tasks.

- [MMInA: Benchmarking Multihop Multimodal Internet Agents](https://arxiv.org/abs/2404.09992)
    - Ziniu Zhang, Shulin Tian, Liangyu Chen, Ziwei Liu
    - 🏛️ Institutions: Unknown
    - 📅 Date: April 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [multihop web browsing], [multimodal tasks], [long-range reasoning]
    - 📖 TLDR: The **MMInA** benchmark is designed to evaluate agents' capacity to complete complex, multihop web tasks by navigating and extracting information across evolving real-world websites. Composed of 1,050 tasks across diverse domains, MMInA challenges agents with realistic, multimodal information retrieval and reasoning tasks, such as comparative shopping and travel inquiries. Despite recent advances, agents show difficulties in handling tasks requiring sequential steps across multiple sites, underscoring the need for enhanced multimodal and memory-augmented models.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - 🏛️ Institutions: CMU
    - 📅 Date: April 9, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web page understanding], [grounding]
    - 📖 TLDR: VisualWebBench introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on web-based tasks. It includes 1.5K human-curated instances across 139 websites in 87 sub-domains. The benchmark spans seven tasks—such as OCR, grounding, and web-based QA—aiming to test MLLMs' capabilities in fine-grained web page understanding. Results reveal significant performance gaps, particularly in grounding tasks, highlighting the need for advancement in MLLM web understanding.

- [WebVLN: Vision-and-Language Navigation on Websites](https://arxiv.org/abs/2312.15820)
    - Qi Chen, Dileepa Pitawela, Chongyang Zhao, Gengze Zhou, Hsiang-Ting Chen, Qi Wu
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 24, 2024
    - 📑 Publisher: AAAI 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [web-based VLN], [HTML content integration], [multimodal navigation]
    - 📖 TLDR: This paper introduces the *WebVLN* task, where agents navigate websites by following natural language instructions that include questions and descriptions. Aimed at emulating real-world browsing behavior, the task allows the agent to interact with elements not directly visible in the rendered content by integrating HTML-specific information. A new *WebVLN-Net* model, based on the VLN BERT framework, is introduced alongside the *WebVLN-v1* dataset, supporting question-answer navigation across web pages. This framework demonstrated significant improvement over existing web-based navigation methods, marking a new direction in vision-and-language navigation research.

- [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718)
    - Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, Alexandre Lacoste
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 11, 2024
    - 📑 Publisher: ICLR 2024 (LLMAgents Workshop)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agents], [enterprise task automation], [ServiceNow], [knowledge work automation]
    - 📖 TLDR: WorkArena introduces a robust benchmark hosted on the ServiceNow platform to assess the effectiveness of large language model-based agents in performing 33 knowledge tasks common to enterprise environments. Leveraging BrowserGym, an environment that simulates complex browser interactions, WorkArena provides web agents with realistic challenges like data entry, form completion, and information retrieval in knowledge bases. Despite promising initial results, open-source models show a 42.7% success rate compared to closed-source counterparts, underlining the current gap in task automation for enterprise applications and highlighting key areas for improvement.

- [On the Multi-turn Instruction Following for Conversational Web Agents](https://arxiv.org/abs/2402.15057)
    - Yang Deng, Xuan Zhang, Wenxuan Zhang, Yifei Yuan, See-Kiong Ng, Tat-Seng Chua
    - 🏛️ Institutions: Unknown
    - 📅 Date: February 23, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [multi-turn dialogue], [memory utilization], [self-reflective planning]
    - 📖 TLDR: This paper explores multi-turn conversational web navigation, introducing the MT-Mind2Web dataset to support instruction-following tasks for web agents. The proposed Self-MAP (Self-Reflective Memory-Augmented Planning) framework enhances agent performance by integrating memory with self-reflection for sequential decision-making in complex interactions. Extensive evaluations using MT-Mind2Web demonstrate Self-MAP's efficacy in addressing the limitations of current models in multi-turn interactions, providing a novel dataset and framework for evaluating and training agents on detailed, multi-step web-based tasks.

- [Dual-View Visual Contextualization for Web Navigation](https://arxiv.org/abs/2402.04476)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - 🏛️ Institutions: OSU
    - 📅 Date: February 6, 2024
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [visual contextualization]
    - 📖 TLDR: This paper proposes a novel approach to web navigation by contextualizing HTML elements through their "dual views" in webpage screenshots. The method leverages both the textual content of HTML elements and their visual representation in the screenshot to create more informative representations for web agents. Evaluated on the Mind2Web dataset, the approach demonstrates consistent improvements over baseline methods across various scenarios, including cross-task, cross-website, and cross-domain navigation tasks.

- [WebLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://arxiv.org/abs/2402.05930)
    - Xing Han Lu, Zdeněk Kasner, Siva Reddy
    - 🏛️ Institutions: Mila, McGill University
    - 📅 Date: February 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [multi-turn dialogue], [real-world navigation]
    - 📖 TLDR: WebLINX addresses the complexity of real-world website navigation for conversational agents, with a benchmark featuring over 2,300 demonstrations across 150+ websites. The benchmark allows agents to handle multi-turn instructions and interact dynamically across diverse domains, including geographic and thematic categories. The study proposes a retrieval-inspired model that selectively extracts key HTML elements and browser actions, achieving efficient task-specific representations. Experiments reveal that smaller finetuned decoders outperform larger zero-shot multimodal models, though generalization to new environments remains challenging.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - 🏛️ Institutions: Unknown
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

- [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://huggingface.co/papers/2305.11854)
    - Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu, Izzeddin Gur
    - 🏛️ Institutions: Univ. of Tokyo, Google DeepMind
    - 📅 Date: Jan 1, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [model], [dataset], [web navigation], [instruction-following]
    - 📖 TLDR: This paper introduces WebGUM, an instruction-following multimodal agent for autonomous web navigation that leverages both visual (webpage screenshots) and textual (HTML) inputs to perform actions such as click and type. The model is trained on a vast corpus of demonstrations and shows improved capabilities in visual perception, HTML comprehension, and multi-step decision-making, achieving state-of-the-art performance on benchmarks like MiniWoB and WebShop. WebGUM provides a scalable approach to web-based tasks without task-specific architectures, enabling high-performance web navigation with generalizable, multimodal foundation models.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://osu-nlp-group.github.io/SeeAct/)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: January 1, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [grounding], [seeact], [multimodal-mind2web]
    - 📖 TLDR: This paper explores the capability of GPT-4V(ision), a multimodal model, as a web agent that can perform tasks across various websites by following natural language instructions. It introduces the **SEEACT** framework, enabling GPT-4V to navigate, interpret, and interact with elements on websites. Evaluated using the **Mind2Web** benchmark and an online test environment, the framework demonstrates high performance on complex web tasks by integrating grounding strategies like element attributes and image annotations to improve HTML element targeting. However, grounding remains challenging, presenting opportunities for further improvement.

- [Interactive Evolution: A Neural-Symbolic Self-Training Framework For Large Language Models](https://arxiv.org/abs/2406.11736)
    - Fangzhi Xu, Qiushi Sun, Kanzhi Cheng, Jun Liu, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Unknown
    - 📅 Date: November 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI (evaluated on web, math reasoning, and logic reasoning environments)]
    - 🔑 Key: [framework], [dataset], [neural-symbolic self-training], [online exploration], [self-refinement]
    - 📖 TLDR: This paper introduces *ENVISIONS*, a neural-symbolic self-training framework designed to improve large language models (LLMs) by enabling self-training through interaction with a symbolic environment. The framework addresses symbolic data scarcity and enhances LLMs' symbolic reasoning proficiency by iteratively exploring, refining, and learning from symbolic tasks without reinforcement learning. Extensive evaluations across web navigation, math, and logical reasoning tasks highlight *ENVISIONS* as a promising approach for enhancing LLM symbolic processing.

- [OpenAgents: An Open Platform for Language Agents in the Wild](https://github.com/xlang-ai/OpenAgents)
    - Tianbao Xie, Fan Zhou, Zhoujun Cheng, Peng Shi, Luoxuan Weng, Yitao Liu, Toh Jing Hua, Junning Zhao, Qian Liu, Che Liu, Leo Z. Liu, Yiheng Xu, Hongjin Su, Dongchan Shin, Caiming Xiong, Tao Yu
    - 🏛️ Institutions: HKU, XLang Lab, Sea AI Lab, Salesforce Research
    - 📅 Date: October 16, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [Data Agent], [Plugins Agent], [Web Agent]
    - 📖 TLDR: This paper introduces OpenAgents, an open-source platform designed to facilitate the use and hosting of language agents in real-world scenarios. It features three agents: Data Agent for data analysis using Python and SQL, Plugins Agent with access to over 200 daily API tools, and Web Agent for autonomous web browsing. OpenAgents aims to provide a user-friendly web interface for general users and a seamless deployment experience for developers and researchers, promoting the development and evaluation of innovative language agents in practical applications.

- [SteP: Stacked LLM Policies for Web Actions](https://asappresearch.github.io/webagents-step/)
    - Paloma Sodhi, S.R.K. Branavan, Yoav Artzi, Ryan McDonald
    - 🏛️ Institutions: ASAPP Research, Cornell University
    - 📅 Date: October 5, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [policy composition], [dynamic control], [SteP]
    - 📖 TLDR: This paper introduces **SteP (Stacked LLM Policies)**, a framework that dynamically composes policies to tackle diverse web tasks. By defining a Markov Decision Process where the state is a stack of policies, SteP enables adaptive control that adjusts to task complexity. Evaluations on WebArena, MiniWoB++, and a CRM simulator demonstrate that SteP significantly outperforms existing methods, achieving a success rate improvement from 14.9% to 35.8% over state-of-the-art GPT-4 policies.

- [LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/abs/2309.08172)
    - Kaixin Ma, Hongming Zhang, Hongwei Wang, Xiaoman Pan, Dong Yu, Jianshu Chen
    - 🏛️ Institutions: Unknown
    - 📅 Date: September 15, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [state-space exploration], [backtracking]
    - 📖 TLDR: This paper introduces LASER, an LLM agent that models interactive web navigation tasks as state-space exploration. The approach defines a set of high-level states and associated actions, allowing the agent to transition between states and backtrack from errors. LASER significantly outperforms previous methods on the WebShop task without using in-context examples, demonstrating improved handling of novel situations and mistakes during task execution.

- [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://arxiv.org/abs/2407.20183)
    - Zehui Chen, Zhenyu Wang, Jiannan Jiang, Jiashuo Wang, Zhiyi Zhang, Yicheng Zou, Yuxiang Zhou, Jingxuan He, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Unknown
    - 📅 Date: July 29, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [multi-agent system], [web information seeking], [dynamic graph construction]
    - 📖 TLDR: This paper presents MindSearch, a novel approach to web information seeking and integration that mimics human cognitive processes. The system uses a multi-agent framework consisting of a WebPlanner and WebSearcher. The WebPlanner models multi-step information seeking as a dynamic graph construction process, decomposing complex queries into sub-questions. The WebSearcher performs hierarchical information retrieval for each sub-question. MindSearch demonstrates significant improvements in response quality and depth compared to existing AI search solutions, processing information from over 300 web pages in just 3 minutes.

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, et al.
    - 🏛️ Institutions: Unknown
    - 📅 Date: July 26, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [multi-tab navigation], [web-based interaction], [agent simulation]
    - 📖 TLDR: *WebArena* provides a standalone, realistic web simulation environment where autonomous agents can perform complex web-based tasks. The platform offers functionalities such as multi-tab browsing, element interaction, and customized user profiles. Its benchmark suite contains 812 tasks grounded in high-level natural language commands. WebArena uses multi-modal observations, including HTML and accessibility tree views, supporting advanced tasks that require contextual understanding across diverse web pages, making it suitable for evaluating generalist agents in real-world web environments.

- [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856)
    - Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust
    - 🏛️ Institutions: Unknown
    - 📅 Date: July 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [program synthesis], [HTML comprehension], [web automation], [self-supervised learning]
    - 📖 TLDR: WebAgent leverages two LLMs—HTML-T5 for HTML comprehension and Flan-U-PaLM for program synthesis—to complete web automation tasks. It combines planning, HTML summarization, and code generation to navigate and interact with real-world web environments, improving success rates on HTML-based tasks and achieving state-of-the-art performance in benchmarks like MiniWoB and Mind2Web. The modular architecture adapts well to open-domain tasks, using local-global attention mechanisms to manage long HTML contexts.

- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU
    - 📅 Date: June 9, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [model], [mind2web], [mindact]
    - 📖 TLDR: *Mind2Web* presents a dataset and benchmark specifically crafted for generalist web agents capable of performing language-guided tasks across varied websites. Featuring over 2,000 tasks from 137 sites, it spans 31 domains and emphasizes open-ended, realistic tasks in authentic, unsimplified web settings. The study proposes the *MindAct* framework, which optimizes LLMs for handling complex HTML elements by using small LMs to rank elements before full processing, thereby enhancing the efficiency and versatility of web agents in diverse contexts.

- [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://arxiv.org/abs/2210.03347)
    - Kenton Lee, Mandar Joshi, Iulia Raluca Turc, Hexiang Hu, Fangyu Liu, Julian Martin Eisenschlos, Urvashi Khandelwal, Peter Shaw, Ming-Wei Chang, Kristina Toutanova
    - 🏛️ Institutions: Google
    - 📅 Date: February 1, 2023
    - 📑 Publisher: ICML 2023
    - 💻 Env: [Web], [Doc]
    - 🔑 Key: [model], [framework], [vision encoder], [visual language understanding], [screenshot parsing], [image-to-text]
    - 📖 TLDR: This paper introduces Pix2Struct, a model pre-trained to parse masked screenshots into simplified HTML for tasks requiring visual language understanding. By leveraging the structure of HTML and diverse web page elements, Pix2Struct captures pretraining signals like OCR and image captioning, achieving state-of-the-art performance across tasks in domains including documents, user interfaces, and illustrations.

- [WebUI: A Dataset for Enhancing Visual UI Understanding with Web Semantics](https://arxiv.org/abs/2301.13280)
    - Jason Wu, Siyan Wang, Siman Shen, Yi-Hao Peng, Jeffrey Nichols, Jeffrey P. Bigham
    - 🏛️ Institutions: CMU, Wellesley College, Grinnell College, Snooty Bird LLC
    - 📅 Date: January 30, 2023
    - 📑 Publisher: CHI 2023
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [element detection], [screen classification], [screen similarity], [UI modeling]
    - 📖 TLDR: The WebUI dataset includes 400,000 web UIs captured to enhance UI modeling by integrating visual UI metadata. This dataset supports tasks such as element detection, screen classification, and screen similarity, especially for accessibility, app automation, and testing applications. Through transfer learning and semi-supervised methods, WebUI addresses the challenge of training robust models with limited labeled mobile data, proving effective in tasks beyond web contexts, such as mobile UIs.

- [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)
    - Shunyu Yao, Howard Chen, John Yang, Karthik Narasimhan
    - 🏛️ Institutions: Unknown
    - 📅 Date: July 2022
    - 📑 Publisher: NeurIPS 2022
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [e-commerce web interaction], [language grounding]
    - 📖 TLDR: This paper introduces **WebShop**, a simulated web-based shopping environment with over 1 million real-world products and 12,087 annotated instructions. It allows language agents to navigate, search, and make purchases based on natural language commands. The study explores how agents handle compositional instructions and noisy web data, providing a robust environment for reinforcement learning and imitation learning. The best models show effective sim-to-real transfer on websites like Amazon, illustrating WebShop’s potential for training grounded agents.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://arxiv.org/abs/2103.16057)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 30, 2021
    - 📑 Publisher: NAACL 2021
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [grounding], [task automation], [open-domain instructions]
    - 📖 TLDR: This paper introduces RUSS (Rapid Universal Support Service), a framework designed to interpret and execute open-domain, step-by-step web instructions automatically. RUSS uses a BERT-LSTM model for semantic parsing into a custom language, ThingTalk, which allows the system to map language to actions across various web elements. The framework, including a dataset of instructions, facilitates agent-based web support task automation by grounding natural language to interactive commands.

- [WebSRC: A Dataset for Web-Based Structural Reading Comprehension](https://arxiv.org/abs/2101.09465)
    - Lu Chen, Zihan Zhao, Xingyu Chen, Danyang Zhang, Jiabao Ji, Ao Luo, Yuxuan Xiong, Kai Yu
    - 🏛️ Institutions: Unknown
    - 📅 Date: January 23, 2021
    - 📑 Publisher: EMNLP 2021
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [structural reading comprehension], [web page QA], [structural information], [HTML element alignment]
    - 📖 TLDR: This paper introduces **WebSRC**, a dataset specifically designed for web-based structural reading comprehension, which requires understanding not only textual content but also the structural layout of web pages. WebSRC consists of 0.44 million question-answer pairs derived from 6,500 complex web pages. Each question challenges models to identify answers from HTML structures or to respond with yes/no, requiring a nuanced grasp of HTML and layout features. The authors benchmark several models on this dataset, highlighting its difficulty and the critical role of structural comprehension in improving machine understanding of web content.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Unknown
    - 📅 Date: February 24, 2018
    - 📑 Publisher: ICLR 2018
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [web tasks], [workflow-guided exploration]
    - 📖 TLDR: This paper presents a novel RL approach using *workflow-guided exploration* to efficiently train agents on web-based tasks, where actions are restricted based on demonstrated workflows to streamline learning. Evaluated on MiniWoB and MiniWoB++ benchmarks, the method significantly outperforms traditional RL techniques in sparse reward settings by structuring exploration according to high-level action constraints.

- [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html)
    - Tianlin Shi, Andrej Karpathy, Linxi Fan, Jonathan Hernandez, Percy Liang
    - 🏛️ Institutions: Stanford, OpenAI
    - 📅 Date: August 2017
    - 📑 Publisher: ICML 2017
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [web-based tasks], [open-domain]
    - 📖 TLDR: This paper introduces *World of Bits (WoB)*, a platform enabling agents to perform complex web-based tasks using low-level keyboard and mouse actions, addressing the lack of open-domain realism in existing reinforcement learning environments. WoB leverages a novel framework where crowdworkers create tasks with structured rewards and reproducibility by caching web interactions, forming a stable training environment. The authors validate WoB by training agents via behavioral cloning and reinforcement learning to accomplish various real-world tasks, showcasing its potential as an effective platform for reinforcement learning on web tasks.

- [From One Tree to a Forest: a Unified Solution for Structured Web Data Extraction](https://dl.acm.org/doi/abs/10.1145/2009916.2010020?casa_token=_yhpn25Od9kAAAAA:5ANOavO4-9WJc1yi7Sz2EalB69XPN8kAUi8JqeMy3ws0aKHInvglGZ9gEWbgoBS-o_SYyXgP4mhw)
    - Qiang Hao, Rui Cai, Yanwei Pang, Lei Zhang
    - 🏛️ Institutions: Unknown
    - 📅 Date: July 24, 2011
    - 📑 Publisher: SIGIR 2011
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [structured web extraction], [minimal human labeling], [cross-vertical extraction]
    - 📖 TLDR: This paper presents a scalable solution to structured web data extraction across diverse website domains (e.g., books, restaurants) by leveraging limited labeled data per vertical. The approach uses generalized features to characterize each vertical and adapts these to new sites by unsupervised constraints. The solution's robustness is validated on 80 sites across 8 categories, demonstrating that minimal site-specific training is needed to generalize extraction capabilities.
