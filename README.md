- [From One Tree to a Forest: a Unified Solution for Structured Web Data Extraction](https://dl.acm.org/doi/10.1145/2009916.2010036)
    - Qiang Hao, Rui Cai, Yanwei Pang, Lei Zhang
    - July 24, 2011
    - SIGIR 2011
    - Env: Web
    - Key: framework, dataset, structured web extraction, minimal human labeling, cross-vertical extraction
    - TLDR: This paper presents a scalable solution to structured web data extraction across diverse website domains (e.g., books, restaurants) by leveraging limited labeled data per vertical. The approach uses generalized features to characterize each vertical and adapts these to new sites by unsupervised constraints. The solution's robustness is validated on 80 sites across 8 categories, demonstrating that minimal site-specific training is needed to generalize extraction capabilities.

- [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html)
    - Tianlin Shi, Andrej Karpathy, Linxi Fan, Jonathan Hernandez, Percy Liang
    - August 2017
    - ICML 2017
    - Env: Web
    - Key: framework, dataset, reinforcement learning, web-based tasks, open-domain
    - TLDR: This paper introduces *World of Bits (WoB)*, a platform enabling agents to perform complex web-based tasks using low-level keyboard and mouse actions, addressing the lack of open-domain realism in existing reinforcement learning environments. WoB leverages a novel framework where crowdworkers create tasks with structured rewards and reproducibility by caching web interactions, forming a stable training environment. The authors validate WoB by training agents via behavioral cloning and reinforcement learning to accomplish various real-world tasks, showcasing its potential as an effective platform for reinforcement learning on web tasks.

- [Rico: A Mobile App Dataset for Building Data-Driven Design Applications](https://dl.acm.org/doi/10.1145/3126594.3126651)
    - Genevieve Patterson, Joseph Gonzalez, Jeffrey Heer, Daniel H. Haim, Keyur Govani, Andrew Hertzmann, Noah Snavely, Neel Joshi
    - October 20, 2017
    - UIST 2017
    - Env: Mobile
    - Key: dataset, mobile UI, UI design analysis, interaction mining
    - TLDR: This paper introduces *Rico*, a large-scale dataset comprising UI screens and view hierarchies from over 9,000 Android apps, designed to aid in understanding mobile app design. Rico supports a variety of tasks, including UI design analysis and interaction mining, by providing labeled UI components, screenshots, and interaction traces.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - February 24, 2018
    - ICLR 2018
    - Env: Web
    - Key: framework, benchmark, reinforcement learning, web tasks, workflow-guided exploration
    - TLDR: This paper presents a novel RL approach using *workflow-guided exploration* to efficiently train agents on web-based tasks, where actions are restricted based on demonstrated workflows to streamline learning. Evaluated on MiniWoB and MiniWoB++ benchmarks, the method significantly outperforms traditional RL techniques in sparse reward settings by structuring exploration according to high-level action constraints.

- [Mapping Natural Language Instructions to Mobile UI Action Sequences](https://aclanthology.org/2020.acl-main.729)
    - Yang Li, Jiacong He, Xin Zhou, Yuan Zhang, Jason Baldridge
    - July 2020
    - ACL 2020
    - Env: Mobile
    - Key: framework, dataset, mobile UI automation, natural language instructions, action grounding
    - TLDR: This paper introduces a method for grounding natural language instructions to mobile UI actions, aiming to automate mobile task execution through user interface manipulation. It introduces three key datasets: **PixelHelp** for task instruction-performance mappings on a Pixel emulator, **AndroidHowTo** for detailed phrase extraction, and **RicoSCA** for synthetic UI command training. The system utilizes a Transformer model to extract action phrase tuples, aligning them to UI elements with contextual screen positioning. Achieving over 70% accuracy in task completion, this approach is foundational for natural language-driven mobile UI automation.

- [WebSRC: A Dataset for Web-Based Structural Reading Comprehension](https://arxiv.org/abs/2101.09465)
    - Lu Chen, Zihan Zhao, Xingyu Chen, Danyang Zhang, Jiabao Ji, Ao Luo, Yuxuan Xiong, Kai Yu
    - January 23, 2021
    - EMNLP 2021
    - Env: Web
    - Key: dataset, structural reading comprehension, web page QA, structural information, HTML element alignment
    - TLDR: This paper introduces **WebSRC**, a dataset specifically designed for web-based structural reading comprehension, which requires understanding not only textual content but also the structural layout of web pages. WebSRC consists of 0.44 million question-answer pairs derived from 6,500 complex web pages. Each question challenges models to identify answers from HTML structures or to respond with yes/no, requiring a nuanced grasp of HTML and layout features. The authors benchmark several models on this dataset, highlighting its difficulty and the critical role of structural comprehension in improving machine understanding of web content.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://arxiv.org/abs/2103.16057)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - March 30, 2021
    - NAACL 2021
    - Env: Web
    - Key: framework, dataset, grounding, task automation, open-domain instructions
    - TLDR: This paper introduces RUSS (Rapid Universal Support Service), a framework designed to interpret and execute open-domain, step-by-step web instructions automatically. RUSS uses a BERT-LSTM model for semantic parsing into a custom language, ThingTalk, which allows the system to map language to actions across various web elements. The framework, including a dataset of instructions, facilitates agent-based web support task automation by grounding natural language to interactive commands.

- [AndroidEnv: A Reinforcement Learning Platform for Android](https://arxiv.org/abs/2105.13231)
    - Daniel Toyama, Archit Sharma, Victoria Lin, Serkan Cabi, Antoine Lauzier, Edgar Duéñez-Guzmán, Pushmeet Kohli
    - May 27, 2021
    - arXiv
    - Env: Mobile
    - Key: reinforcement learning, Android interface, RL environment, task flexibility, touchscreen action space
    - TLDR: AndroidEnv provides a reinforcement learning (RL) platform for Android that lets RL agents interact with a realistic Android simulation via touchscreen events. The platform supports diverse applications, enabling agents to interact with over 100 predefined tasks across a variety of apps. With hybrid continuous and discrete action spaces, AndroidEnv is well-suited for training agents in complex, real-world Android scenarios where actions must be contextually sequenced, such as in UI navigation, gaming, and productivity apps. This environment encourages further RL research by offering task flexibility and realistic Android emulation.

- [Screen2Words: Automatic Mobile UI Summarization with Multimodal Learning](https://aclanthology.org/2021.acl-long.56/)
    - Svitlana Vakulenko, Mickelsson Lukas, Alexander Popov, Payam Barnaghi, Krisztian Balog
    - August 2021
    - ACL 2021
    - Env: Mobile
    - Key: framework, multimodal learning, mobile UI summarization
    - TLDR: Screen2Words proposes a multimodal framework to automatically summarize mobile UI screens by combining visual and textual data for task-oriented assistance. The model, leveraging transformer-based architectures, identifies and generates summaries for diverse UI elements, enabling improved accessibility and navigability on mobile devices. Evaluated across several datasets, the approach demonstrates effective summarization for applications ranging from accessibility tools to task guidance in mobile settings.

- [A Dataset for Interactive Vision-Language Navigation with Unknown Command Feasibility](https://arxiv.org/abs/2202.02312)
    - Andrea Burns, Deniz Arsan, Sanjna Agrawal, Ranjitha Kumar, Kate Saenko, Bryan A. Plummer
    - February 4, 2022
    - ECCV 2022
    - Env: Mobile
    - Key: dataset, feasibility prediction, vision-language navigation, mobile interaction
    - TLDR: This paper introduces the *Mobile App Tasks with Iterative Feedback (MoTIF)* dataset, which addresses vision-language navigation (VLN) with a focus on task feasibility uncertainty in mobile applications. MoTIF provides commands paired with mobile actions and feasibility annotations, allowing researchers to examine the impact of command feasibility on task completion. The dataset includes 125 apps and emphasizes diverse app environments, action sequences, and follow-up questions to improve task ambiguity resolution, making it a valuable resource for feasibility prediction research.

- [A Data-Driven Approach for Learning to Control Computers](https://arxiv.org/abs/2202.08137)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - February 16, 2022
    - ICML 2022
    - Env: Desktop
    - Key: dataset, framework, computer control, reinforcement learning, multimodal transformer
    - TLDR: This study presents a reinforcement learning-based approach to train agents for computer control tasks, using keyboard and mouse interactions guided by natural language. By leveraging human demonstration data, agents trained in this environment achieved strong cross-task generalization across the MiniWob++ benchmark. This framework demonstrates how agents can control computers as humans would, enabling enhanced performance in complex computer tasks with high transferability.

- [META-GUI: Towards Multi-modal Conversational Agents on Mobile GUI](https://arxiv.org/abs/2205.11029)
    - Liangtai Sun, Xingyu Chen, Lu Chen, Tianle Dai, Zichen Zhu, Kai Yu
    - May 23, 2022
    - EMNLP 2022
    - Env: Mobile
    - Key: framework, dataset, task-oriented dialogue, GUI-based interaction, multi-modal agent
    - TLDR: This paper presents META-GUI, a dataset and framework for training multi-modal conversational agents capable of interacting directly with mobile app interfaces without the need for backend APIs. META-GUI includes over 1,100 dialogues with annotated action sequences on various tasks such as booking and scheduling. The authors propose a GUI-based task-oriented dialogue system that allows agents to navigate mobile interfaces via direct GUI actions, with performance shown to improve in multi-modal task-oriented dialogue contexts.

- [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)
    - Shunyu Yao, Howard Chen, John Yang, Karthik Narasimhan
    - July 2022
    - NeurIPS 2022
    - Env: Web
    - Key: framework, dataset, benchmark, e-commerce web interaction, language grounding
    - TLDR: This paper introduces **WebShop**, a simulated web-based shopping environment with over 1 million real-world products and 12,087 annotated instructions. It allows language agents to navigate, search, and make purchases based on natural language commands. The study explores how agents handle compositional instructions and noisy web data, providing a robust environment for reinforcement learning and imitation learning. The best models show effective sim-to-real transfer on websites like Amazon, illustrating WebShop’s potential for training grounded agents.

- [Spotlight: Mobile UI Understanding using Vision-Language Models with a Focus](https://arxiv.org/abs/2209.14927)
    - Gang Li, Yang Li
    - September 29, 2022
    - ICLR 2023
    - Env: Mobile
    - Key: framework, model, dataset, mobile UI tasks, region-based focus
    - TLDR: This paper introduces "Spotlight," a vision-language model for mobile UI understanding that operates solely on visual inputs (screenshots) and a specified focus region on the screen. By leveraging a large-scale dataset and training strategies tailored to mobile interfaces, Spotlight performs multiple UI-related tasks, including widget captioning, screen summarization, command grounding, and tappability prediction. It utilizes a vision-only approach, avoiding reliance on view hierarchies to achieve greater robustness and scalability across different mobile UI environments.

- [Language Models can Solve Computer Tasks](https://arxiv.org/abs/2303.17491)
    - Geunwoo Kim, Pierre Baldi, Stephen McAleer
    - March 30, 2023
    - NeurIPS 2023
    - Env: Desktop
    - Key: framework, benchmark, Recursive Critique and Improve (RCI), MiniWoB++, general computer tasks
    - TLDR: This study demonstrates that large language models (LLMs) can effectively automate computer tasks using a Recursive Critique and Improve (RCI) prompting method, enabling agents to handle complex desktop tasks like email and file management. By combining RCI with existing Chain of Thought (CoT) prompting, the method outperforms prior LLM approaches and traditional supervised and reinforcement learning models on the **MiniWoB++** benchmark, showing potential for broad computer task automation.

- [Augmenting Autotelic Agents with Large Language Models](https://arxiv.org/abs/2305.06498)
    - Antoine Vaysse, Thomas Pierrot, Cédric Colas, Pierre-Yves Oudeyer
    - May 2023
    - arXiv
    - Env: GUI
    - Key: framework, reinforcement learning, language models, autotelic agents
    - TLDR: This paper introduces a method to enhance autotelic agents (those capable of self-driven goal setting) by integrating large language models to support exploration and goal generation. The proposed architecture allows agents to handle increasingly complex environments, benefiting from language model insights for scenario adaptation. Through interaction, the agents showcase improved adaptability in open-ended tasks, suggesting language models as valuable guides in self-motivated agent learning.

- [Mobile-Env: Building Qualified Evaluation Benchmarks for LLM-GUI Interaction](https://arxiv.org/abs/2305.08144)
    - Danyang Zhang, Lu Chen, Zihan Zhao, Ruisheng Cao, Kai Yu
    - May 14, 2023
    - arXiv
    - Env: Mobile
    - Key: benchmark, dataset, interaction platform, multistep interaction, InfoUI
    - TLDR: This paper introduces *Mobile-Env*, a novel interaction platform and benchmark aimed at assessing large language models' (LLMs) capabilities in interactive environments. It builds on the InfoUI task set, derived from WikiHow, to create structured text-based challenges that simulate real-world mobile interactions. The platform is designed to support task expansions from the community, aiming to drive advancements in LLM-based interactive agents.

- [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://arxiv.org/abs/2305.19308)
    - Jian Jiang, Zhanran Wang, Zhihong Shao, Zhiyi Fu, Zhengliang Liu, Peng Zhang, Zhen Li, Qingying Yan, Weijia Shi, Xiao Liu, Jie Zhang, Qi Zhang, Tao Yu
    - May 30, 2023
    - NeurIPS 2023
    - Env: GUI
    - Key: framework, spreadsheet automation, natural language interface
    - TLDR: This paper introduces SheetCopilot, an innovative system that leverages large language models to automate spreadsheet tasks through natural language interactions. The framework includes a novel prompt design for task decomposition and execution, and a feedback loop for error correction. SheetCopilot demonstrates significant improvements in task completion rates and efficiency across various spreadsheet operations, outperforming existing methods and showing potential for enhancing productivity in spreadsheet software.

- [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - June 2023
    - ICLR 2024
    - Env: Desktop
    - Key: framework, memory mechanism, computer control, few-shot prompting, state abstraction
    - TLDR: Synapse introduces a memory-augmented agent for computer control tasks, focusing on trajectory-as-exemplar prompting. This approach allows the agent to abstract complex HTML-based states and recall task-specific exemplars, enabling efficient interaction in environments such as MiniWoB++ and Mind2Web. Synapse achieves high performance by selecting relevant exemplars from past interactions, providing a structured method for clean observation extraction and complex action generation.

- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)
    - Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, Yu Su
    - June 9, 2023
    - NeurIPS 2023
    - Env: Web
    - Key: dataset, benchmark, generalist web agent, complex task navigation, HTML element processing
    - TLDR: *Mind2Web* presents a dataset and benchmark specifically crafted for generalist web agents capable of performing language-guided tasks across varied websites. Featuring over 2,000 tasks from 137 sites, it spans 31 domains and emphasizes open-ended, realistic tasks in authentic, unsimplified web settings. The study proposes the *MindAct* framework, which optimizes LLMs for handling complex HTML elements by using small LMs to rank elements before full processing, thereby enhancing the efficiency and versatility of web agents in diverse contexts.

- [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856)
    - Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust
    - July 2023
    - ICLR 2024
    - Env: Web
    - Key: framework, program synthesis, HTML comprehension, web automation, self-supervised learning
    - TLDR: WebAgent leverages two LLMs—HTML-T5 for HTML comprehension and Flan-U-PaLM for program synthesis—to complete web automation tasks. It combines planning, HTML summarization, and code generation to navigate and interact with real-world web environments, improving success rates on HTML-based tasks and achieving state-of-the-art performance in benchmarks like MiniWoB and Mind2Web. The modular architecture adapts well to open-domain tasks, using local-global attention mechanisms to manage long HTML contexts.

- [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088)
    - Christopher Rawles, Alice Li, Daniel Rodriguez, Oriana Riva, Timothy Lillicrap
    - July 19, 2023
    - NeurIPS 2023
    - Env: Mobile
    - Key: dataset, benchmark, device control, natural language interaction, gesture-based actions
    - TLDR: The *Android in the Wild (AitW)* dataset introduces a significant benchmark for Android device control, encompassing over 715,000 human-labeled episodes with natural language commands and corresponding UI actions. Collected from Android devices across versions 10-13, it captures complex multi-step tasks requiring both visual and contextual understanding. The dataset is structured to test the robustness of device-control systems under varying conditions, such as new tasks or applications, and includes data to evaluate gesture-based interactions, providing a unique foundation for mobile interface automation and task execution research.

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
    - Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, et al.
    - July 26, 2023
    - NeurIPS 2023
    - Env: Web
    - Key: framework, benchmark, multi-tab navigation, web-based interaction, agent simulation
    - TLDR: *WebArena* provides a standalone, realistic web simulation environment where autonomous agents can perform complex web-based tasks. The platform offers functionalities such as multi-tab browsing, element interaction, and customized user profiles. Its benchmark suite contains 812 tasks grounded in high-level natural language commands. WebArena uses multi-modal observations, including HTML and accessibility tree views, supporting advanced tasks that require contextual understanding across diverse web pages, making it suitable for evaluating generalist agents in real-world web environments.

- [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://arxiv.org/abs/2407.20183)
    - Zehui Chen, Zhenyu Wang, Jiannan Jiang, Jiashuo Wang, Zhiyi Zhang, Yicheng Zou, Yuxiang Zhou, Jingxuan He, Yuxiao Dong, Jie Tang
    - July 29, 2023
    - arXiv
    - Env: Web
    - Key: framework, multi-agent system, web information seeking, dynamic graph construction
    - TLDR: This paper presents MindSearch, a novel approach to web information seeking and integration that mimics human cognitive processes. The system uses a multi-agent framework consisting of a WebPlanner and WebSearcher. The WebPlanner models multi-step information seeking as a dynamic graph construction process, decomposing complex queries into sub-questions. The WebSearcher performs hierarchical information retrieval for each sub-question. MindSearch demonstrates significant improvements in response quality and depth compared to existing AI search solutions, processing information from over 300 web pages in just 3 minutes.

- [AutoDroid: LLM-powered Task Automation in Android](https://arxiv.org/abs/2308.15272)
    - Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, Yunxin Liu
    - August 29, 2023
    - MobiCom 2024
    - Env: Mobile
    - Key: framework, dataset, benchmark, Android task automation, LLM-powered agent
    - TLDR: This paper introduces AutoDroid, a novel mobile task automation system capable of handling arbitrary tasks on any Android application without manual efforts. The framework combines the commonsense knowledge of LLMs with domain-specific knowledge of apps through automated dynamic analysis. AutoDroid features a functionality-aware UI representation method, exploration-based memory injection techniques, and a multi-granularity query optimization module. Evaluated on a new benchmark with 158 common tasks, AutoDroid achieves a 90.9% action generation accuracy and a 71.3% task completion rate, significantly outperforming GPT-4-powered baselines.

- [LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/abs/2309.08172)
    - Kaixin Ma, Hongming Zhang, Hongwei Wang, Xiaoman Pan, Dong Yu, Jianshu Chen
    - September 15, 2023
    - arXiv
    - Env: Web
    - Key: framework, web navigation, state-space exploration, backtracking
    - TLDR: This paper introduces LASER, an LLM agent that models interactive web navigation tasks as state-space exploration. The approach defines a set of high-level states and associated actions, allowing the agent to transition between states and backtrack from errors. LASER significantly outperforms previous methods on the WebShop task without using in-context examples, demonstrating improved handling of novel situations and mistakes during task execution.

- [You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/abs/2309.11436)
    - Zhuosheng Zhang, Aston Zhang
    - September 20, 2023
    - ICLR 2024
    - Env: GUI
    - Key: framework, dataset, benchmark, multimodal agent, chain-of-action technique
    - TLDR: This paper presents Auto-GUI, a multimodal agent capable of directly interacting with graphical user interfaces without relying on environment parsing or application-specific APIs. The authors introduce a novel chain-of-action technique that leverages previous action histories and future action plans to improve decision-making. Auto-GUI is evaluated on a new device-control benchmark, AITW, demonstrating state-of-the-art performance in action prediction and task completion across various applications and web-based tasks.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.08587)
    - Jiawei Li, Zhengyuan Yang, Jianfeng Gao, Cha Zhang, Dongdong Chen, Xiujun Li
    - October 13, 2023
    - arXiv
    - Env: GUI
    - Key: framework, UI task automation, reinforcement learning, instruction grounding
    - TLDR: This paper introduces a novel framework for UI task automation that combines instruction grounding with reinforcement learning. The approach uses a large language model to interpret natural language instructions and generate action sequences, which are then refined through reinforcement learning. The system demonstrates improved performance on complex UI tasks across various applications, showcasing its potential as a generic API for UI automation. The research contributes to advancing human-computer interaction and automated UI testing.

- [OpenAgents: AN OPEN PLATFORM FOR LANGUAGE AGENTS IN THE WILD](https://arxiv.org/abs/2310.10634)
    - Tianbao Xie, Fan Zhou, Zhoujun Cheng, Peng Shi, Luoxuan Weng, Yitao Liu, Toh Jing Hua, Junning Zhao, Qian Liu, Che Liu, Haoyuan Peng, Xingyu Shen, Yike Yuan, Ankit Ramchandani, Shiyi Cao, Tianxiang Sun, Zhiyi Zhang, Rui Zhao, Jian Guan, Chuanhu Wang, Yao Mu, Yida Wang, Hao Dong, Dasong Gao, Tianyi Tang, Zhiyuan Liu, Vicent Peris, Qingxiu Dong, Zhiyi Fu, Shuai Wang, Jinhua Zhu, Jidong Long, Ran He, Yuqi Zhu, Juntao Dai, Haotian Sun, Hao Yang, Vishwali Mhasawade, Qihui Zhang, Guohai Xu, Jiaxin Zhang, Jinjie Ni, Yunshan Ma, Keming Lu, Xiaoran Fan, Cheng Li, Jingxuan He, Rui Zheng, Jingbiao Mei, Xingxuan Li, Xiaoxue Gan, Liang Zhao, Jingjing Tian, Zhuosheng Zhang, Yao Fu, Shuohuan Wang, Chujie Zheng, Xin Cheng, Xudong Liu, Bowen Yu, Wenhu Chen, Yizhong Wang, Binyuan Hui, Xinmei Shen, Bowen Qin, Hao Chen, Hanze Dong, Jiawen Deng, Sang Michael Xie, Kunlun Zhu, Yuxiang Zhang, Hongming Zhang, Ruohong Zhang, Jiaqi Li, Mukai Li, Tianle Gu, Zheng Yu, Linyi Yang, Songyang Gao, Juanzi Li, Yong Dai, Baobao Chang, Dawei Zhu, Maosong Sun, Jie Tang, Michael Lyu, Xipeng Qiu
    - October 16, 2023
    - arXiv
    - Env: GUI
    - Key: framework, open-source platform, language agents, multi-modal interaction
    - TLDR: This paper presents OpenAgents, an open-source platform for developing and deploying language agents capable of interacting with various applications and services. The platform includes three types of agents: a coding agent, a browser agent, and a chrome agent, each designed to handle different tasks and environments. OpenAgents demonstrates the potential of language models to serve as intelligent assistants in real-world scenarios, offering a flexible and extensible framework for researchers and developers to build upon.

- [Interactive Evolution: A Neural-Symbolic Self-Training Framework For Large Language Models](https://arxiv.org/abs/2406.11736)
    - Fangzhi Xu, Qiushi Sun, Kanzhi Cheng, Jun Liu, Yu Qiao, Zhiyong Wu
    - November 2023
    - arXiv
    - Env: GUI (evaluated on web, math reasoning, and logic reasoning environments)
    - Key: framework, dataset, neural-symbolic self-training, online exploration, self-refinement
    - TLDR: This paper introduces *ENVISIONS*, a neural-symbolic self-training framework designed to improve large language models (LLMs) by enabling self-training through interaction with a symbolic environment. The framework addresses symbolic data scarcity and enhances LLMs' symbolic reasoning proficiency by iteratively exploring, refining, and learning from symbolic tasks without reinforcement learning. Extensive evaluations across web navigation, math, and logical reasoning tasks highlight *ENVISIONS* as a promising approach for enhancing LLM symbolic processing.

- [GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](https://arxiv.org/abs/2311.07562)
    - Liuyi Yao, Kaizhi Zheng, Yifan Wang, Xiao Han, Boyu Gou, Jiayi Zhang, Rui Zhao, Xin Zhou, Lifan Yuan, Yizhi Li, Junlin Zhang, Chenghu Zhou, Yida Wang, Huan Sun, Yu Su
    - November 13, 2023
    - arXiv
    - Env: Mobile
    - Key: framework, benchmark, zero-shot GUI navigation, multimodal LLMs
    - TLDR: This paper explores the capabilities of GPT-4V in navigating smartphone GUIs without prior training. The authors introduce a novel framework for GUI navigation and a new benchmark, MobileNav, featuring 1,000 navigation tasks across 100 mobile apps. The study demonstrates GPT-4V's impressive zero-shot performance in understanding and interacting with mobile interfaces, outperforming previous methods and even approaching human-level performance on some tasks.

- [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914)
    - Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhao Chen, Yuxuan Wang, Yining Ye, Jiayi Zhang, Hao Dong, Wenhu Chen, Yizhou Wang, Kai-Wei Chang
    - December 15, 2023
    - CVPR 2024
    - Env: GUI
    - Key: model, dataset, benchmark, visual language model, GUI agent
    - TLDR: This paper presents CogAgent, a visual language model designed for GUI agents. The authors introduce a new dataset, CogBench, featuring 1,430 GUI tasks across various applications. CogAgent employs a novel training approach combining supervised fine-tuning and decision-making fine-tuning. The model demonstrates superior performance on CogBench and generalizes well to unseen applications, outperforming existing models like GPT-4V in GUI task completion.

- [AssistGUI: Task-Oriented Desktop Graphical User Interface Automation](https://arxiv.org/abs/2312.13108)
    - Difei Gao, Lei Ji, Zechen Bai, Mingyu Ouyang, Peiran Li, Dongxing Mao, Qinchen Wu, Weichen Zhang, Peiyi Wang, Xiangwu Guo, Hengxu Wang, Luowei Zhou, Mike Zheng Shou
    - December 20, 2023
    - CVPR 2024
    - Env: Desktop
    - Key: framework, dataset, benchmark, GUI automation, desktop productivity tasks
    - TLDR: This study presents *AssistGUI*, a benchmark and framework for desktop GUI automation, featuring an LLM-based agent capable of completing complex user requests by analyzing instructional videos and performing actions on the desktop. Utilizing a novel Actor-Critic framework and GUI parser, *AssistGUI* was tested on 100 tasks across nine applications, such as MS Word and After Effects. Despite advances, the top-performing model achieved only a 46% success rate, illustrating the challenge of comprehensive desktop automation and underscoring areas for future research in agent-driven GUI tasks.

- [AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771)
    - Chi Zhang, Zhao Yang, Jiaxuan Liu, Yucheng Han, Xin Chen, Zebiao Huang, Bin Fu, Gang Yu
    - December 21, 2023
    - arXiv
    - Env: Mobile
    - Key: framework, multimodal agent, smartphone interaction, autonomous exploration
    - TLDR: This paper introduces AppAgent, a novel multimodal agent framework designed to operate smartphone applications. The agent uses a simplified action space to mimic human-like interactions such as tapping and swiping. AppAgent learns to navigate and use new apps through autonomous exploration or by observing human demonstrations, creating a knowledge base for executing complex tasks across different applications. The framework's effectiveness is demonstrated through extensive testing on 50 tasks across 10 diverse applications.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - January 1, 2024
    - ICML 2024
    - Env: Web
    - Key: framework, dataset, benchmark, generalist web agent, grounding
    - TLDR: This paper explores the capability of GPT-4V(ision), a multimodal model, as a web agent that can perform tasks across various websites by following natural language instructions. It introduces the **SEEACT** framework, enabling GPT-4V to navigate, interpret, and interact with elements on websites. Evaluated using the **Mind2Web** benchmark and an online test environment, the framework demonstrates high performance on complex web tasks by integrating grounding strategies like element attributes and image annotations to improve HTML element targeting. However, grounding remains challenging, presenting opportunities for further improvement.

- [WebVLN: Vision-and-Language Navigation on Websites](https://aaai.org/AAAI24)
    - Jinghui Shi, Minjeong Han, Karan Goel, Qi Wei, Daniel Kahng, Mohit Bansal, Xuezhi Wang
    - January 2024
    - AAAI 2024
    - Env: Web
    - Key: benchmark, vision-and-language navigation, website navigation, embodied AI, sequential task completion
    - TLDR: WebVLN introduces a novel challenge for vision-and-language navigation (VLN) in web environments. By setting navigation tasks across various websites, WebVLN evaluates agents' abilities to understand visual and textual cues for sequential task completion, such as locating specific information and navigating through page structures. This benchmark aligns with real-world user tasks and presents a distinctive test for embodied AI models, with its dynamic web interface and reliance on combined visual and linguistic understanding, marking a significant step forward in web-based VLN benchmarks.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)
    - Yifan Wang, Bohao Li, Haoran Luo, Deng Cai, Yichong Xu, Wai Lam, Hao Zhou
    - January 19, 2024
    - ACL 2024
    - Env: GUI
    - Key: framework, GUI grounding, visual GUI agents
    - TLDR: This paper introduces SeeClick, a novel framework for visual GUI agents that enhances their ability to interact with graphical user interfaces. The approach uses a two-stage process: first, it grounds natural language instructions to specific GUI elements, then it selects the most appropriate action. SeeClick demonstrates significant improvements in task completion rates across various GUI environments, outperforming existing methods and showing potential for more intuitive and efficient human-computer interactions.

- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
    - January 24, 2024
    - ACL 2024
    - Env: Web
    - Key: framework, dataset, benchmark, multimodal web agent, end-to-end interaction
    - TLDR: This paper introduces WebVoyager, an innovative web agent powered by Large Multimodal Models (LMMs) that can complete user instructions end-to-end by interacting with real-world websites. The authors establish a new benchmark with tasks from 15 popular websites and propose an automatic evaluation protocol using GPT-4V. WebVoyager achieves a 59.1% task success rate, significantly outperforming GPT-4 (All Tools) and text-only setups. The study demonstrates the effectiveness of multimodal approaches in web automation and provides insights into developing more intelligent web interaction solutions.

- [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158)
    - Junyang Wang, Haiyang Xu, Jiabo Ye, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - January 29, 2024
    - arXiv
    - Env: Mobile
    - Key: framework, dataset, benchmark, multi-modal agent, mobile device interaction
    - TLDR: This paper presents Mobile-Agent, an autonomous multi-modal agent designed for mobile device interaction. The system integrates visual perception, natural language processing, and action prediction to navigate and operate mobile applications. The authors introduce a new dataset and benchmark for evaluating mobile agents, demonstrating Mobile-Agent's superior performance in task completion and generalization across various apps compared to existing methods.

- [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553)
    - Raghav Kapoor, Yash Parag Butala, Melisa Russak, Jing Yu Koh, Kiran Kamble, Waseem Alshikh, Ruslan Salakhutdinov
    - February 2024
    - arXiv
    - Env: GUI
    - Key: dataset, benchmark, multimodal agent, UI grounding, autonomous desktop and web tasks
    - TLDR: OmniACT introduces a dataset and benchmark to train and evaluate multimodal agents capable of autonomously performing diverse tasks across desktop and web environments. Using annotated UI elements across applications, it combines visual grounding with natural language instructions, providing 9,802 data points for developing agents that integrate high-level reasoning with UI interactions. The study highlights the limited proficiency of current models, with baselines like GPT-4 only achieving 15% of human performance on executable scripts, emphasizing OmniACT's potential as a testbed for advancing multimodal AI.

- [WebLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://arxiv.org/abs/2402.05930)
    - Xing Han Lu, Zdeněk Kasner, Siva Reddy
    - February 2024
    - ICML 2024
    - Env: Web
    - Key: framework, dataset, benchmark, multi-turn dialogue, real-world navigation
    - TLDR: WebLINX addresses the complexity of real-world website navigation for conversational agents, with a benchmark featuring over 2,300 demonstrations across 150+ websites. The benchmark allows agents to handle multi-turn instructions and interact dynamically across diverse domains, including geographic and thematic categories. The study proposes a retrieval-inspired model that selectively extracts key HTML elements and browser actions, achieving efficient task-specific representations. Experiments reveal that smaller finetuned decoders outperform larger zero-shot multimodal models, though generalization to new environments remains challenging.

- [Dual-View Visual Contextualization for Web Navigation](https://arxiv.org/abs/2402.04476)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - February 6, 2024
    - CVPR 2024
    - Env: Web
    - Key: framework, visual contextualization, web navigation
    - TLDR: This paper proposes a novel approach to web navigation by contextualizing HTML elements through their "dual views" in webpage screenshots. The method leverages both the textual content of HTML elements and their visual representation in the screenshot to create more informative representations for web agents. Evaluated on the Mind2Web dataset, the approach demonstrates consistent improvements over baseline methods across various scenarios, including cross-task, cross-website, and cross-domain navigation tasks.

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://arxiv.org/abs/2402.04615)
    - Gilles Baechler, Srinivas Sunkara, Maria Wang, Fedir Zubach, Hassan Mansoor, Vincent Etter, Victor Cărbune, Jason Lin, Jindong Chen, Abhanshu Sharma
    - February 7, 2024
    - IJCAI 2024
    - Env: GUI
    - Key: model, dataset, UI understanding, infographics understanding, vision-language model
    - TLDR: This paper introduces ScreenAI, a vision-language model specializing in UI and infographics understanding. The model combines the PaLI architecture with the flexible patching strategy of pix2struct and is trained on a unique mixture of datasets. ScreenAI achieves state-of-the-art results on several UI and infographics-based tasks, outperforming larger models. The authors also release three new datasets for screen annotation and question answering tasks.

- [UFO: A UI-Focused Agent for Windows OS Interaction](https://arxiv.org/abs/2402.07939)
    - Chaoyun Zhang, Zheng Chen, Jincheng Yang, Xiangqun Chen, Jiaxin Zhang, Zheng Xu, Zhi Jin, Wenxue Cheng, Mao Yang
    - February 8, 2024
    - arXiv
    - Env: GUI
    - Key: framework, Windows OS, UI interaction, multi-agent system
    - TLDR: This paper introduces UFO, an innovative UI-Focused agent designed for seamless interaction with Windows OS applications. UFO employs a dual-agent framework (HostAgent and AppAgent) that leverages GPT-Vision to analyze GUI screenshots and control information. The system can navigate and operate within individual or multiple applications to fulfill user requests expressed in natural language. UFO incorporates a control interaction module for automated execution without human intervention, and features like action customization and safeguards. The framework was tested across 9 popular Windows applications, demonstrating its effectiveness in completing complex tasks spanning multiple applications.

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)
    - Zhiwei Liu, Weili Nie, Xuwang Yin, Chaowei Xiao, Yue Cao, Yixin Zhu, Anima Anandkumar
    - February 12, 2024
    - arXiv
    - Env: GUI
    - Key: framework, dataset, benchmark, generalist computer agent, self-improvement
    - TLDR: This paper presents OS-Copilot, a framework for developing generalist computer agents capable of performing diverse tasks across different operating systems. The approach combines large language models, computer vision techniques, and reinforcement learning to enable agents to interact with graphical user interfaces. OS-Copilot features a novel self-improvement mechanism that allows the agent to learn from its mistakes and improve its performance over time. The framework is evaluated on a new benchmark, OSBench, which includes tasks across Windows, Ubuntu, and macOS, demonstrating its potential for creating more versatile and adaptive AI assistants for computer operation.

- [ScreenAgent: A Computer Control Agent Driven by Visual Language Large Model](https://arxiv.org/abs/2402.07945)
    - Chao Wang, Weizhou Shen, Zhihao Zhu, Yuxiang Zhang, Yifeng Han, Zhengjun Zha, Tao Mei
    - February 13, 2024
    - arXiv
    - Env: GUI
    - Key: framework, visual language model, computer control agent
    - TLDR: This paper introduces ScreenAgent, a computer control agent powered by a visual language large model. The system can interpret natural language instructions and execute them on various computer applications by analyzing screen content. ScreenAgent employs a novel action grounding mechanism to map high-level instructions to specific UI interactions. Evaluated on a diverse set of tasks across different applications, ScreenAgent demonstrates superior performance in task completion and generalization compared to existing methods.

- [Comprehensive Cognitive LLM Agent for Smartphone GUI Automation](https://arxiv.org/abs/2402.14286)
    - Jiaxin Zhang, Zheng Chen, Chaoyun Zhang, Xiangqun Chen, Zhi Jin
    - February 22, 2024
    - arXiv
    - Env: Mobile
    - Key: framework, smartphone GUI automation, cognitive agent, multi-modal interaction
    - TLDR: This paper presents a comprehensive cognitive LLM agent framework for smartphone GUI automation. The framework integrates visual perception, cognitive reasoning, and action execution to enable natural language-driven interactions with mobile applications. It features a novel multi-modal prompting strategy and a hierarchical planning approach to break down complex tasks. The system demonstrates superior performance in task completion and generalization across various mobile apps, outperforming existing methods in both seen and unseen scenarios. The research contributes to advancing human-smartphone interaction and automated mobile testing.

- [Improving Language Understanding from Screenshots](https://arxiv.org/abs/2402.14073)
    - Tianyu Gao, Zirui Wang, Adithya Bhaskar, Danqi Chen
    - February 22, 2024
    - arXiv
    - Env: GUI
    - Key: model, framework, screenshot language models, patch-and-text prediction
    - TLDR: This paper introduces a novel approach to improve the language understanding capabilities of screenshot language models (LMs). The authors propose a Patch-and-Text Prediction (PTP) objective, which masks and recovers both image patches and text within screenshots. The method significantly narrows the performance gap between screenshot LMs and text-only models on language understanding tasks, achieving comparable results to BERT on most GLUE tasks. The research also extends PTP to train autoregressive screenshot LMs, demonstrating improved perplexity by utilizing screenshot context.

- [On the Multi-turn Instruction Following for Conversational Web Agents](https://arxiv.org/abs/2402.15057)
    - Yang Deng, Xuan Zhang, Wenxuan Zhang, Yifei Yuan, See-Kiong Ng, Tat-Seng Chua
    - February 23, 2024
    - ACL 2024
    - Env: Web
    - Key: framework, dataset, multi-turn dialogue, memory utilization, self-reflective planning
    - TLDR: This paper explores multi-turn conversational web navigation, introducing the MT-Mind2Web dataset to support instruction-following tasks for web agents. The proposed Self-MAP (Self-Reflective Memory-Augmented Planning) framework enhances agent performance by integrating memory with self-reflection for sequential decision-making in complex interactions. Extensive evaluations using MT-Mind2Web demonstrate Self-MAP's efficacy in addressing the limitations of current models in multi-turn interactions, providing a novel dataset and framework for evaluating and training agents on detailed, multi-step web-based tasks.

- [AgentStudio: A Toolkit for Building General Virtual Agents](https://ar5iv.org/abs/2403.17918)
    - Jiaming Liang, Xiaofeng Zhang, Lele Zhou, Chao Wang, Xin Li, Yiming Gong, Yi Ren, Sheng Wang, Bing Liu, Shumeng Pan, Kai Wei
    - March 10, 2024
    - arXiv
    - Env: GUI (supports interactions in web, desktop, and mobile environments)
    - Key: framework, dataset, general virtual agents, open-ended learning, tool creation
    - TLDR: AgentStudio is a robust toolkit for developing virtual agents with versatile actions, such as GUI automation and code execution. It unifies real-world human-computer interactions across OS platforms and includes diverse observation and action spaces, facilitating comprehensive training and benchmarking in complex settings. The toolkit's flexibility promotes agent generalization across varied tasks, supporting tool creation and a multimodal interaction interface to advance agent adaptability and learning.

- [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718)
    - Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, Alexandre Lacoste
    - March 11, 2024
    - ICLR 2024 (LLMAgents Workshop)
    - Env: Web
    - Key: benchmark, web agents, enterprise task automation, ServiceNow, knowledge work automation
    - TLDR: WorkArena introduces a robust benchmark hosted on the ServiceNow platform to assess the effectiveness of large language model-based agents in performing 33 knowledge tasks common to enterprise environments. Leveraging BrowserGym, an environment that simulates complex browser interactions, WorkArena provides web agents with realistic challenges like data entry, form completion, and information retrieval in knowledge bases. Despite promising initial results, open-source models show a 42.7% success rate compared to closed-source counterparts, underlining the current gap in task automation for enterprise applications and highlighting key areas for improvement.

- [Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II as a Case Study](https://arxiv.org/abs/2403.09058)
    - Weihao Tan, Ziluo Ding, Bohan Zhou, Junfei Xiao, Jiaxin Shi, Wenjia Wang, Yuhao Zhou, Yuhang Cao, Zongqing Lu
    - March 14, 2024
    - arXiv
    - Env: GUI
    - Key: framework, multimodal agent, computer control, game environment
    - TLDR: This paper presents a novel multimodal agent framework for general computer control, using the complex open-world game Red Dead Redemption II as a case study. The agent integrates visual perception, natural language processing, and action generation to navigate and interact within the game environment. The approach demonstrates the potential for developing more versatile AI agents capable of handling diverse tasks in complex graphical user interfaces, extending beyond gaming to general computer control applications.

- [Android in the Zoo: Chain-of-Action-Thought for GUI Agents](https://arxiv.org/abs/2403.17936)
    - Zhengyuan Yang, Jiawei Li, Zhengyuan Ma, Ruoxi Chen, Jiaxin Zhang, Xiujun Li, Jianfeng Gao, Cha Zhang
    - March 26, 2024
    - arXiv
    - Env: Mobile
    - Key: framework, dataset, benchmark, GUI agents, chain-of-action-thought
    - TLDR: This paper introduces a novel approach called Chain-of-Action-Thought (CAT) for training GUI agents to interact with Android applications. The authors create AndroidZoo, a diverse dataset of 100 Android apps with 1,000 tasks. CAT combines large language models with a structured reasoning process to decompose complex tasks into actionable steps. The framework demonstrates superior performance in task completion and generalization across various Android apps compared to existing methods, showcasing its potential for developing more capable mobile AI assistants.

- [Benchmarking Mobile Device Control Agents across Diverse Configurations](https://arxiv.org/abs/2404.16660)
    - Juyong Lee, Taywon Min, Minyong An, Dongyoon Hahm, Haeone Lee, Changyeon Kim, Kimin Lee
    - April 2024
    - ICLR 2024
    - Env: Mobile
    - Key: benchmark, dataset, mobile device control, agent performance, LLM agents
    - TLDR: This paper presents **B-MoCA**, a comprehensive benchmark for evaluating mobile device control agents using an Android-based testbed with 131 tasks and various device configurations. The benchmark assesses agents' abilities across tasks that include device-specific variations, navigation, and human-like dual-gesture interactions. B-MoCA highlights that current agents perform well on basic tasks but struggle with complex configurations, pointing to opportunities for future improvements in mobile automation capabilities.

- [Octopus v2: On-device language model for super agent](https://arxiv.org/abs/2404.01744)
    - Wei Chen, Zhiyuan Li
    - April 2, 2024
    - arXiv
    - Env: GUI
    - Key: model, framework, on-device language model, function calling, super agent
    - TLDR: This paper introduces Octopus v2, an innovative on-device language model designed for efficient function calling in AI agents. The 2-billion parameter model outperforms GPT-4 in both accuracy and latency, while reducing context length by 95%. Octopus v2 uses a novel method of encoding functions into specialized tokens, significantly improving performance and enabling deployment across various edge devices. The model demonstrates a 35-fold latency improvement over Llama-7B with RAG-based function calling, making it suitable for real-world applications on resource-constrained devices.

- [AutoWebGLM: Bootstrap and Reinforce a Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2404.03648)
    - Haotian Luo, Yongqi Li, Xiao Liu, Yansong Feng, Dongyan Zhao
    - April 4, 2024
    - KDD 2024
    - Env: Web
    - Key: framework, web navigation agent, reinforcement learning, HTML simplification
    - TLDR: This paper introduces AutoWebGLM, an advanced web navigation agent based on ChatGLM3-6B that outperforms GPT-4 in real-world web tasks. The framework includes an HTML simplification algorithm, a hybrid human-AI method for dataset creation, and a bootstrapping process using reinforcement learning and rejection sampling. AutoWebGLM demonstrates improved performance in webpage comprehension, browser operations, and task decomposition across various web navigation benchmarks.

- [Search Beyond Queries: Training Smaller Language Models for Web Interactions via Reinforcement Learning](https://arxiv.org/abs/2404.04061)
    - Zhiwei Liu, Yongjie Shi, Chaowei Xiao, Yue Cao, Yixin Zhu, Anima Anandkumar
    - April 6, 2024
    - arXiv
    - Env: Web
    - Key: framework, reinforcement learning, web interaction, smaller language models
    - TLDR: This paper presents a novel approach to training smaller language models for web interactions using reinforcement learning. The method enables models to learn efficient web navigation and information retrieval strategies beyond simple query-based searches. The authors demonstrate that their approach allows smaller models to compete with larger ones in complex web tasks, potentially reducing computational requirements for web-based AI assistants.

- [Enhancing Mobile "How-to" Queries with Automated Search Results Verification and Reranking](https://arxiv.org/abs/2404.05173)
    - Yifan Song, Zhiyi Fu, Jiaqi Guo, Qi Zhang, Tao Yu
    - April 9, 2024
    - SIGIR 2024
    - Env: Mobile
    - Key: framework, mobile search, result verification, reranking
    - TLDR: This paper introduces a novel approach to improve mobile "how-to" query results by implementing automated search result verification and reranking. The method uses a combination of natural language processing and computer vision techniques to assess the relevance and quality of search results for mobile device-specific queries. The authors demonstrate significant improvements in result accuracy and user satisfaction compared to traditional search algorithms, particularly for complex, multi-step mobile device tasks.

- [Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474)
    - Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr
    - April 9, 2024
    - arXiv
    - Env: Web, Desktop
    - Key: framework, benchmark, evaluation model, web navigation, domain transfer
    - TLDR: This paper presents an autonomous evaluation framework for digital agents to enhance performance on web navigation and device control. The study introduces modular, cost-effective evaluators achieving up to 92.9% accuracy in benchmarks like WebArena and outlines their use in fine-tuning agents, improving state-of-the-art by 29% without additional supervision.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - April 9, 2024
    - COLM 2024
    - Env: Web
    - Key: benchmark, dataset, web page understanding, grounding, multimodal LLMs
    - TLDR: VisualWebBench introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on web-based tasks. It includes 1.5K human-curated instances across 139 websites in 87 sub-domains. The benchmark spans seven tasks—such as OCR, grounding, and web-based QA—aiming to test MLLMs' capabilities in fine-grained web page understanding. Results reveal significant performance gaps, particularly in grounding tasks, highlighting the need for advancement in MLLM web understanding.

- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://ar5iv.org/abs/2404.07972)
    - Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, Tao Yu
    - April 11, 2024
    - NeurIPS 2024
    - Env: GUI (operable in web, desktop, and mobile environments)
    - Key: benchmark, framework, multimodal agents, open-ended computer tasks, real-world evaluation
    - TLDR: OSWorld introduces a new benchmark designed to evaluate multimodal agents on open-ended tasks in a real-world computer environment, focusing on complex, multi-application workflows across OSs. It allows agents to perform tasks like file I/O and application control, promoting interaction in realistic setups for more comprehensive agent assessment. The benchmark includes 369 unique tasks and enables interactive learning for multimodal AI, targeting practical improvements in task handling and interface interactions.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Automation Task Evaluation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - April 12, 2024
    - UIST 2024
    - Env: Mobile
    - Key: framework, dataset, benchmark, UI automation, mobile agent evaluation
    - TLDR: LlamaTouch is an evaluation testbed designed for mobile UI automation, enabling reliable task assessment across 495 annotated tasks. It provides a scalable solution to evaluate agents in real-world mobile settings, comparing agent actions to essential UI states for accurate task completion. LlamaTouch supports dynamic environments, advancing mobile agent reliability and scalability in task automation.

- [Octopus: On-device language model for function calling of software APIs](https://arxiv.org/abs/2403.09339)
    - Yifan Song, Ruochen Wang, Zhiyi Fu, Jiaqi Guo, Yihong Dong, Qi Zhang, Tao Yu
    - April 15, 2024
    - arXiv
    - Env: GUI
    - Key: model, on-device language model, API function calling, software interaction
    - TLDR: This paper introduces Octopus, an on-device language model designed for function calling of software APIs. The model enables natural language interaction with various software applications by translating user intents into appropriate API calls. Octopus is optimized for efficiency and privacy, running entirely on-device without requiring cloud connectivity. The authors demonstrate its effectiveness across multiple software domains, showing improved task completion rates and user experience compared to traditional interface navigation methods.

- [MMInA: Benchmarking Multihop Multimodal Internet Agents](https://arxiv.org/abs/2404.09992)
    - Ziniu Zhang, Shulin Tian, Liangyu Chen, Ziwei Liu
    - April 15, 2024
    - arXiv
    - Env: Web
    - Key: benchmark, framework, multihop web browsing, multimodal tasks, long-range reasoning
    - TLDR: The **MMInA** benchmark is designed to evaluate agents' capacity to complete complex, multihop web tasks by navigating and extracting information across evolving real-world websites. Composed of 1,050 tasks across diverse domains, MMInA challenges agents with realistic, multimodal information retrieval and reasoning tasks, such as comparative shopping and travel inquiries. Despite recent advances, agents show difficulties in handling tasks requiring sequential steps across multiple sites, underscoring the need for enhanced multimodal and memory-augmented models.

- [Octopus v3: Technical Report for On-device Sub-billion Multimodal AI Agent](https://arxiv.org/abs/2404.08290)
    - Wei Chen, Zhiyuan Li
    - April 16, 2024
    - arXiv
    - Env: GUI
    - Key: model, framework, multimodal agent, on-device AI, sub-billion parameters
    - TLDR: Octopus v3 extends the Octopus series to multimodal capabilities, introducing a sub-billion parameter model designed for on-device AI agents. The paper presents a novel approach to integrating vision and language understanding within a compact model, enabling efficient processing of both text and images on edge devices. Octopus v3 demonstrates competitive performance against larger models while maintaining low latency and resource requirements, making it suitable for deployment on devices as constrained as a Raspberry Pi.

- [AutoWebGLM: Bootstrap And Reinforce A Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2403.13281)
    - Yilun Huang, Jian Yang, Zhihao Zhu, Hongsheng Li, Qiang Liu, Xiaogang Wang
    - April 19, 2024
    - KDD 2024
    - Env: Web
    - Key: framework, web navigation agent, reinforcement learning, self-improvement
    - TLDR: This paper presents AutoWebGLM, a novel framework for developing a self-improving web navigation agent based on large language models. The approach combines bootstrapping and reinforcement learning techniques to enable the agent to learn from its own experiences and improve its performance over time. AutoWebGLM demonstrates superior performance in complex web navigation tasks compared to existing methods, showcasing its ability to adapt to diverse web environments and complete multi-step tasks efficiently. The research contributes to advancing autonomous web interaction and provides insights into developing more capable AI assistants for web-based tasks.

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://arxiv.org/abs/2403.15837)
    - Jieshan Chen, Munawar Hayat, Zhen Dong, Yuhao Zhu, Yong Dai, Dacheng Tao, Hongdong Li
    - April 23, 2024
    - arXiv
    - Env: Mobile
    - Key: framework, multimodal LLM, mobile UI understanding, grounded visual reasoning
    - TLDR: This paper presents Ferret-UI, a framework for grounded mobile UI understanding using multimodal large language models. The approach combines visual grounding techniques with language models to interpret and interact with mobile interfaces. Ferret-UI demonstrates superior performance in tasks such as UI element detection, task completion, and natural language interaction with mobile apps, outperforming existing methods on various benchmarks.

- [Octopus v4: Graph of language models](https://arxiv.org/abs/2404.15371)
    - Wei Chen, Zhiyuan Li
    - April 29, 2024
    - arXiv
    - Env: GUI
    - Key: framework, graph of language models, multi-model integration, functional tokens
    - TLDR: Octopus v4 introduces a novel approach to integrating multiple open-source language models, each optimized for specific tasks, using a graph structure. The paper presents a method for coordinating these models using functional tokens, enabling more efficient and flexible task execution. This approach allows for the combination of specialized models to tackle complex tasks while maintaining the efficiency needed for on-device deployment. Octopus v4 demonstrates improved performance and versatility compared to single-model approaches, particularly in handling diverse and multi-step tasks.

- [Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2405.00516)
    - Lucas Thil, Samy Aittahar, Yassine Hadjadj-Aoul, Gerardo Rubino
    - May 1, 2024
    - arXiv
    - Env: Web
    - Key: framework, web navigation, large language models, reinforcement learning
    - TLDR: This paper proposes a novel approach combining supervised learning (SL) and reinforcement learning (RL) techniques to train web navigation agents using large language models. The authors address limitations in previous models' understanding of HTML content and introduce methods to enhance true comprehension. Their approach, evaluated on the MiniWoB benchmark, outperforms previous SL methods on certain tasks using less data and narrows the performance gap with RL models. The study achieves 43.58% average accuracy in SL and 36.69% when combined with a multimodal RL approach, setting a new direction for future web navigation research.

- [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)
    - Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Toyama, Robert Berry, Divya Tyamagundlu, Timothy Lillicrap, Oriana Riva
    - May 23, 2024
    - arXiv
    - Env: Mobile
    - Key: benchmark, Android-based agents, task diversity, reinforcement learning, dynamic environment
    - TLDR: AndroidWorld introduces a dynamic Android environment for benchmarking autonomous agents across 116 tasks spanning 20 Android apps. These tasks vary through parameterized and natural language prompts, fostering a realistic testing ground for agents designed to operate in complex mobile environments. The benchmark supports millions of task variations, allowing agents to respond to the Android system's changing states and improving real-world applicability.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://arxiv.org/abs/2406.10227)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen Wu, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Z. Shou
    - June 2024
    - NeurIPS 2024
    - Env: Desktop, Web
    - Key: benchmark, instructional videos, visual planning, hierarchical task decomposition, complex software interaction
    - TLDR: VideoGUI presents a benchmark for evaluating GUI automation on tasks derived from instructional videos, focusing on visually intensive applications like Adobe Photoshop and video editing software. The benchmark includes 178 tasks, with a hierarchical evaluation method distinguishing high-level planning, mid-level procedural steps, and precise action execution. VideoGUI reveals current model limitations in complex visual tasks, marking a significant step toward improved visual planning in GUI automation.

- [Practical, Automated Scenario-based Mobile App Testing](https://doi.org/10.1016/j.jss.2024.107104)
    - Authors yet to be confirmed
    - June 2024
    - Journal of Systems and Software
    - Env: Mobile
    - Key: automated testing, scenario-based testing, mobile app validation, reinforcement learning, system state verification
    - TLDR: This paper proposes a framework for practical, automated scenario-based testing of mobile apps, which aims to streamline app validation by automating tests across common user scenarios. Using real-world data and reinforcement learning techniques, the system dynamically adapts to app states and user interactions, ensuring accurate and efficient validation across mobile platforms without manual oversight.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9)
    - Yijun Qian, Yujie Lu, Alexander G. Hauptmann, Oriana Riva
    - June 2024
    - NAACL 2024 (Industry Track)
    - Env: GUI
    - Key: framework, dataset, benchmark, visual grounding, layout-guided contrastive learning
    - TLDR: This paper presents LVG (Layout-guided Visual Grounding), a model designed to address the challenges of grounding natural language commands to GUI elements in user interfaces without relying on developer-provided metadata like UI trees. LVG combines UI element detection with grounding in a single model by using layout-guided contrastive learning to understand the spatial organization of UI elements. It leverages synthetic data and multi-context learning due to the scarcity of UI datasets. LVG outperforms existing models, achieving higher top-1 accuracy on GUI tasks by 4.9 points, showing its effectiveness in both detection and grounding of visual elements.

- [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://arxiv.org/abs/2406.01014)
    - Junyang Wang, Haiyang Xu, Haitao Jia, Xi Zhang, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, Jitao Sang
    - June 3, 2024
    - arXiv
    - Env: Mobile
    - Key: framework, multi-agent system, mobile device operation, task navigation
    - TLDR: This paper presents Mobile-Agent-v2, an advanced multi-agent architecture for mobile device operation assistance. The system comprises three specialized agents: a planning agent for task progress navigation, a decision agent for focus content navigation, and a reflection agent for error correction. Experimental results show that Mobile-Agent-v2 achieves over a 30% improvement in task completion rates compared to its single-agent predecessor, demonstrating effective navigation and management of complex mobile device operations.

- [GUICourse: From General Vision Language Models to Versatile GUI Agents](https://arxiv.org/abs/2406.11317)
    - Wentong Chen, Junbo Cui, Jinyi Hu, Yujia Qin, Junjie Fang, Yue Zhao, Chongyi Wang, Jun Liu, Guirong Chen, Yupeng Huo, Yuan Yao, Yankai Lin, Zhiyuan Liu, Maosong Sun
    - June 7, 2024
    - arXiv
    - Env: GUI
    - Key: framework, dataset, OCR, grounding, multimodal interaction, GUI agents
    - TLDR: GUICourse is a comprehensive set of datasets (GUIEnv, GUIAct, GUIChat) designed to develop versatile GUI agents using Vision Language Models (VLMs). It targets improvements in OCR, grounding, and GUI knowledge across both web and smartphone scenarios. GUIEnv enhances OCR and grounding abilities through large-scale annotations; GUIAct includes both single and multi-step instructions for diverse GUI navigation tasks; GUIChat introduces conversational data with text-rich images to support natural language interaction skills in GUI environments.

- [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://arxiv.org/abs/2401.05068)
    - Cheng-Yu Hsieh, Chun-Liang Li, Tomas Pfister
    - June 9, 2024
    - ICML 2024
    - Env: GUI
    - Key: framework, reinforcement learning, device-control agents, autonomous learning
    - TLDR: This paper introduces DigiRL, a novel framework for training device-control agents using autonomous reinforcement learning in real-world settings. The approach enables agents to learn complex UI interactions without human supervision, leveraging large language models for task generation and reward design. DigiRL demonstrates significant improvements in task completion rates across various applications, showcasing its potential for developing more adaptive and capable AI assistants for digital device interaction.

- [MobileAgentBench: An Efficient and User-Friendly Benchmark for Mobile LLM Agents](https://arxiv.org/abs/2406.08184)
    - Luyuan Wang, Yongyu Deng, Yiwei Zha, Guodong Mao, Qinmin Wang, Tianchen Min, Wei Chen, Shoufa Chen
    - June 12, 2024
    - arXiv
    - Env: Mobile
    - Key: benchmark, mobile LLM agents, task automation, real-device evaluation, GUI interaction
    - TLDR: MobileAgentBench is a comprehensive benchmark that evaluates mobile-based large language model (LLM) agents on real Android devices across 100 tasks in 10 apps with varying difficulty levels. Unlike previous benchmarks relying on static screenshots, this setup supports dynamic interaction on real devices, assessing agents’ ability to complete tasks efficiently. This framework emphasizes final UI states over action sequences to judge task success, using Android Accessibility Service for real-time monitoring, thus enabling both academic and industrial research advancements in mobile agent performance.

- [GUI Odyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451)
    - Quanfeng Lu, Wenqi Shao, Zitao Liu, Fanqing Meng, Boxuan Li, Botong Chen, Siyuan Huang, Kaipeng Zhang, Yu Qiao, Ping Luo
    - June 13, 2024
    - arXiv
    - Env: Mobile
    - Key: dataset, cross-app navigation, Android, multi-task, GUI automation
    - TLDR: GUI Odyssey introduces a large-scale dataset with 7,735 cross-app navigation episodes, collected across six mobile devices and spanning 201 apps. The dataset facilitates GUI agents in learning to complete complex, multi-app tasks on Android, including settings management, media sharing, and information retrieval. This benchmark enables training and testing in mobile environments and supports advancements in navigation-based GUI automation.

- [On the Effects of Data Scale on Computer Control Agents](https://arxiv.org/abs/2406.10012)
    - Authors: [Placeholder for authors]
    - June 14, 2024
    - arXiv
    - Env: Desktop
    - Key: data scaling, control agents, performance improvement, reinforcement learning, scalability
    - TLDR: This study investigates the relationship between data scale and performance improvements for computer control agents. By training agents on datasets of varying sizes, the authors assess how data scaling affects success rates in complex task scenarios, concluding that larger datasets substantially enhance agent capabilities by enabling more nuanced action sequences and adaptive strategies. This research underscores data scaling as a critical factor in advancing reinforcement learning performance in real-world desktop applications.

- [GUI-WORLD: A Dataset for GUI-oriented Multimodal LLM-based Agents](https://arxiv.org/abs/2406.10819)
    - Dongping Chen, Yue Huang, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan, Pan Zhou, Jianfeng Gao, Lichao Sun
    - June 16, 2024
    - arXiv
    - Env: GUI
    - Key: dataset, benchmark, multimodal tasks, dynamic GUI, video-based LLM evaluation
    - TLDR: GUI-WORLD is a large-scale dataset crafted for evaluating multimodal LLMs' (MLLMs) performance in GUI-oriented tasks. It includes annotated keyframes from six distinct GUI environments and various dynamic, static, and sequential question types to benchmark MLLMs like ImageLLMs and VideoLLMs. GUI-WORLD offers a valuable resource for assessing LLMs in complex, dynamic GUI tasks, underscoring their limitations in GUI-specific reasoning and interaction. This dataset aims to enhance future LLMs for robust GUI navigation and interaction capabilities.

- [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
    - Yichen Pan, Dehan Kong, Sida Zhou, Cheng Cui, Yifei Leng, Bing Jiang, Hangyu Liu, Yanyi Shang, Shuyan Zhou, Tongshuang Wu, Zhengyang Wu
    - June 18, 2024
    - ICML 2024 TiFA Workshop
    - Env: Web
    - Key: benchmark, dataset, dynamic web interactions, online evaluation, key node-based assessment
    - TLDR: WebCanvas introduces a dynamic benchmarking framework for web agents, focusing on real-world adaptability in a continuously evolving web environment. By identifying "key nodes" in task flows and leveraging the live dataset Mind2Web-Live, WebCanvas effectively measures agents' performance on essential, unalterable steps of tasks, while minimizing errors from web element or layout changes. This dynamic approach allows agents to adapt to frequent updates, and with a task completion rate of 48.8% on Mind2Web-Live, it emphasizes adaptability over traditional static benchmarks.

- [GUI Action Narrator: Where and When Did That Action Take Place?](https://arxiv.org/abs/2406.13719)
    - Zhengyuan Yang, Jiawei Li, Zhengyuan Ma, Ruoxi Chen, Jiaxin Zhang, Xiujun Li, Jianfeng Gao, Cha Zhang
    - June 20, 2024
    - arXiv
    - Env: GUI
    - Key: framework, dataset, benchmark, GUI action captioning, multimodal LLM
    - TLDR: This paper introduces a novel framework called GUI Narrator for captioning actions in GUI videos. The authors create a new benchmark dataset, Act2Cap, with 4,189 diverse video captioning samples. The approach uses a cursor detector as a visual prompt to enhance the interpretation of high-resolution screenshots. A multimodal LLM model with mechanisms for selecting keyframes and key regions generates the captions. The framework demonstrates improved performance in GUI action understanding compared to existing methods, even for advanced models like GPT-4V.

- [E-ANT: A Large-Scale Dataset for Efficient Automatic GUI NavigaTion](https://arxiv.org/abs/2406.16034)
    - Yihao Huang, Yuxuan Wang, Yining Ye, Yutong Xie, Yihang Xu, Zhihao Fan, Yida Wang, Hao Dong, Wenhu Chen
    - June 25, 2024
    - arXiv
    - Env: GUI
    - Key: dataset, benchmark, GUI navigation, efficient data collection
    - TLDR: This paper introduces E-ANT, a large-scale dataset for efficient automatic GUI navigation. The dataset contains over 100,000 GUI navigation trajectories across 200 diverse Android applications. The authors propose a novel data collection pipeline that combines automated exploration with human verification to ensure data quality and diversity. E-ANT aims to facilitate research in GUI navigation, task planning, and multimodal interaction for mobile devices.

- [Identifying User Goals from UI Trajectories](https://arxiv.org/abs/2406.14760)
    - Toby Jia-Jun Li, Jingya Chen, Haojian Jin, Jeffrey P. Bigham
    - June 26, 2024
    - UIST 2024
    - Env: GUI
    - Key: framework, dataset, user goal identification, UI trajectories
    - TLDR: This paper presents a novel approach for identifying user goals from UI interaction trajectories. The authors introduce a new dataset of UI trajectories paired with corresponding user goals across various mobile and web applications. They develop a machine learning framework that combines sequence modeling and natural language processing techniques to infer high-level user intentions from low-level UI interactions. The proposed method demonstrates significant improvements in goal identification accuracy compared to baseline approaches, potentially enabling more intelligent and proactive user assistance in GUI-based applications.

- [Octo-planner: On-device Language Model for Planner-Action Agents](https://arxiv.org/abs/2406.18082)
    - Wei Chen, Zhiyuan Li, Zhen Guo, Yikang Shen
    - June 26, 2024
    - arXiv
    - Env: GUI
    - Key: framework, on-device language model, planner-action agents
    - TLDR: This paper presents Octo-planner, an efficient on-device Planner-Action framework that separates planning and action execution. The system uses a planner agent based on Phi-3 Mini (3.8 billion parameters) for task decomposition, and an action agent using the Octopus model for function execution. The authors employ model fine-tuning and a multi-LoRA training method to optimize performance on resource-constrained devices. Octo-planner achieves a 97% success rate in in-domain tests and demonstrates flexibility in handling complex, multi-domain queries while maintaining computational efficiency.

- [Read Anywhere Pointed: Layout-aware GUI Screen Reading with Tree-of-Lens Grounding](https://arxiv.org/abs/2406.19263)
    - Yue Fan, Lei Ding, Ching-Chen Kuo, Shan Jiang, Yang Zhao, Xinze Guan, Jie Yang, Yi Zhang, Xin Eric Wang
    - June 27, 2024
    - arXiv
    - Env: GUI
    - Key: framework, dataset, benchmark, layout-aware screen reading, multimodal grounding, accessible technology
    - TLDR: This paper presents the Tree-of-Lens (ToL) agent, a multimodal grounding approach for GUI screen reading using large language models. The ToL agent generates natural language descriptions of screen areas indicated by a user, relying on a novel hierarchical layout tree structure that interprets GUI layouts into multiple lens-like views for enhanced comprehension. The paper introduces a specialized dataset, Android Screen Hierarchical Layout (ASHL), and a benchmark, ScreenPR, which demonstrate the ToL agent’s adaptability across platforms, enhancing accessibility for visually impaired users by improving GUI screen-reading efficiency.

- [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://arxiv.org/abs/2406.17744)
    - Jiawei Li, Zhengyuan Yang, Zhengyuan Ma, Ruoxi Chen, Jiaxin Zhang, Xiujun Li, Jianfeng Gao, Cha Zhang
    - June 28, 2024
    - arXiv
    - Env: GUI
    - Key: model, framework, vision GUI assistant, image-centric fine-tuning
    - TLDR: This paper introduces VGA (Vision GUI Assistant), a novel approach to minimize hallucinations in GUI-based visual language models through image-centric fine-tuning. The authors develop a specialized dataset and training methodology that emphasizes visual grounding and accurate interpretation of GUI elements. VGA demonstrates significant improvements in reducing hallucinations and increasing task completion accuracy across various GUI-based applications compared to existing models, including GPT-4V.

- [MobileFlow: A Multimodal LLM For Mobile GUI Agent](https://arxiv.org/abs/2407.xxxxx)
    - [Author information not available]
    - July 2024
    - arXiv
    - Env: Mobile
    - Key: model, framework, multimodal LLM, mobile GUI agent
    - TLDR: This paper introduces MobileFlow, a multimodal large language model specifically designed for mobile GUI agents. The model integrates visual understanding of mobile interfaces with natural language processing to enable more effective interaction with mobile applications. MobileFlow demonstrates improved performance in task completion and generalization across various mobile apps compared to existing approaches.

- [AUITestAgent: Automatic Requirements Oriented GUI Function Testing](https://arxiv.org/abs/2407.xxxxx)
    - [Author information not available]
    - July 2024
    - arXiv
    - Env: GUI
    - Key: framework, automated GUI testing, requirements-oriented testing
    - TLDR: This paper introduces AUITestAgent, an automated system for GUI function testing based on software requirements. The framework uses natural language processing to interpret requirements and generate test cases, which are then executed on the GUI. AUITestAgent demonstrates improved test coverage and efficiency compared to traditional manual testing approaches, potentially streamlining the software quality assurance process.

- [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://arxiv.org/abs/2407.10956)
    - Ruisheng Cao, Fangyu Lei, Haoyuan Wu, Jixuan Chen, Yeqiao Fu, Hongcheng Gao, Xinzhuang Xiong, Hanchong Zhang, Wenjing Hu, Yuchen Mao, Tianbao Xie, Hongshen Xu, Danyang Zhang, Sida Wang, Ruoxi Sun, Pengcheng Yin, Caiming Xiong, Ansong Ni, Qian Liu, Victor Zhong, Lu Chen, Kai Yu, Tao Yu
    - July 2024
    - NeurIPS 2024
    - Env: Desktop
    - Key: benchmark, data science automation, multimodal agents, enterprise software integration, task decomposition
    - TLDR: Spider2-V introduces a robust benchmark for assessing multimodal agents’ ability to automate complex data workflows across 20 enterprise-level applications. Covering 494 tasks spanning data warehousing to code generation, it includes fine-grained task evaluations within real-world systems like BigQuery and Airbyte. Despite advancements, the benchmark reveals that current agents struggle with detailed GUI tasks and secure data environments, achieving an average success rate of 14%. This benchmark sets a foundation for future multimodal agents in data science and engineering automation.

- [MobileExperts: A Dynamic Tool-Enabled Agent Team in Mobile Devices](https://arxiv.org/abs/2407.xxxxx)
    - [Author information not available]
    - July 2024
    - arXiv
    - Env: Mobile
    - Key: framework, multi-agent system, mobile devices, tool-enabled agents
    - TLDR: This paper presents MobileExperts, a dynamic multi-agent system designed for mobile devices. The framework enables a team of specialized agents to collaborate and utilize various tools within the mobile environment. MobileExperts demonstrates improved performance in complex mobile tasks by dynamically assembling teams of agents with complementary skills and leveraging device-specific tools. The system shows potential for enhancing mobile AI assistants' capabilities in areas such as task planning, information retrieval, and user interaction.

- [CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents](https://arxiv.org/abs/2407.01511)
    - Tianqi Xu, Linyao Chen, Dai-Jie Wu, Yanjun Chen, Zecheng Zhang, Xiang Yao, Zhiqiang Xie, Yongchao Chen, Shilong Liu, Bochen Qian, Philip Torr, Bernard Ghanem, Guohao Li
    - July 1, 2024
    - arXiv
    - Env: GUI (Android, Ubuntu)
    - Key: benchmark, cross-environment, graph evaluator, multimodal agents, sub-task decomposition
    - TLDR: CRAB offers a comprehensive benchmark for evaluating multimodal language model (MLM) agents across Android and Ubuntu environments using CRAB Benchmark-v0. This framework introduces a unique graph-based evaluation, breaking down tasks into sub-goals that represent essential steps in complex interactions. CRAB’s dynamic task generation, with 100 varied tasks, supports cross-platform evaluations, highlighting agent adaptability and performance in executing real-world tasks through structured environments, enabling agents to seamlessly interact across device types and systems.

- [AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents](https://doi.org/10.1145/1122334.1122335)
    - Authors: Placeholder until confirmed
    - July 2024
    - arXiv
    - Env: Mobile
    - Key: dataset, mobile GUI agents, multi-annotation, accessibility, object recognition
    - TLDR: AMEX is a comprehensive multi-annotation dataset for mobile GUI agents, providing varied labeled data for applications like screen readers, accessibility tools, and object recognition in mobile environments. Its multi-layered annotation structure supports diverse applications by allowing mobile agents to interpret and interact with UI elements effectively. This dataset aims to enhance the development and testing of accessibility tools and advanced mobile GUI agents.

- [Vision-driven Automated Mobile GUI Testing via Multimodal Large Language Model](https://arxiv.org/abs/2407.03037)
    - Zhe Liu, [Other authors not provided in the search results]
    - July 3, 2024
    - arXiv
    - Env: Mobile
    - Key: framework, dataset, benchmark, automated GUI testing, multimodal LLM
    - TLDR: This paper presents VisionDroid, a vision-driven approach for automated mobile GUI testing using multimodal large language models. The system aims to detect non-crash functional bugs by understanding visual semantics and operational logic of GUI transitions. VisionDroid employs a function-aware explorer for deeper GUI exploration and a logic-aware bug detector for identifying issues. Evaluated on three datasets, it outperforms 10 baselines and successfully identifies 29 new bugs in real-world apps from Google Play.

- [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://arxiv.org/abs/2407.05291)
    - Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, Alexandre Drouin
    - July 7, 2024
    - NeurIPS 2024
    - Env: GUI
    - Key: benchmark, dataset, planning and reasoning, compositional workflows
    - TLDR: This paper introduces WorkArena++, a benchmark for evaluating LLM-based autonomous agents on realistic workflows common to knowledge workers. The benchmark includes 682 tasks requiring planning, problem-solving, logical reasoning, and contextual understanding. The research highlights gaps in current models and provides tools for generating action traces, aiding fine-tuning for practical task automation in enterprise environments.

- [Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence](https://arxiv.org/abs/2407.07061)
    - Yilun Huang, Zhihao Zhu, Jian Yang, Hongsheng Li, Qiang Liu, Xiaogang Wang
    - July 9, 2024
    - arXiv
    - Env: GUI
    - Key: framework, multi-agent collaboration, heterogeneous agent integration
    - TLDR: This paper introduces the Internet of Agents (IoA), a novel framework for enhancing collaboration among diverse AI agents. Inspired by the internet's architecture, IoA addresses limitations in existing multi-agent systems by providing an agent integration protocol, an instant-messaging-like architecture, and dynamic mechanisms for agent teaming and conversation flow control. The framework demonstrates superior performance in various tasks, including general assistance, embodied AI, and retrieval-augmented generation, showcasing its potential for creating more flexible and capable multi-agent systems.

- [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032)
    - Aditya Vempaty, [Other authors not provided in the search results]
    - July 17, 2024
    - arXiv
    - Env: Web
    - Key: framework, autonomous web navigation, hierarchical architecture, DOM distillation
    - TLDR: This paper presents Agent-E, a novel web agent that introduces several architectural improvements over previous state-of-the-art systems. Key features include a hierarchical architecture, flexible DOM distillation and denoising methods, and a "change observation" concept for improved performance. Agent-E outperforms existing text and multi-modal web agents by 10-30% on the WebVoyager benchmark. The authors synthesize their findings into general design principles for developing agentic systems, including the use of domain-specific primitive skills, hierarchical architectures, and agentic self-improvement.

- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.xxxxx)
    - [Author information not available]
    - August 2024
    - arXiv
    - Env: GUI
    - Key: framework, vision-based GUI parsing, multimodal agent
    - TLDR: This paper introduces OmniParser, a novel approach for pure vision-based GUI parsing and interaction. The system uses advanced computer vision techniques to interpret GUI elements without relying on underlying code or accessibility APIs. OmniParser enables more flexible and generalizable GUI agents that can operate across diverse interfaces and platforms. The authors demonstrate improved performance in GUI navigation and task completion compared to traditional methods that rely on DOM or accessibility information.

- [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.xxxxx)
    - [Author information not available]
    - August 2024
    - arXiv
    - Env: General
    - Key: framework, autonomous agents, advanced reasoning, continual learning
    - TLDR: This paper introduces Agent Q, a novel framework for developing autonomous AI agents with advanced reasoning and learning capabilities. The system combines reinforcement learning, meta-learning, and causal reasoning to enable agents to adapt to new tasks and environments more effectively. Agent Q demonstrates improved performance in complex decision-making scenarios compared to traditional agent architectures, showing potential for more versatile and intelligent AI systems.

- [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649)
    - Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, Daniel Fried
    - August 2024
    - ACL 2024
    - Env: Web
    - Key: framework, benchmark, dataset, multimodal agent evaluation, visually grounded tasks
    - TLDR: VisualWebArena is a benchmark designed for testing multimodal web agents on complex, visually grounded web tasks. It provides a reproducible framework with 910 task scenarios across real-world web applications, emphasizing open-ended, visually guided interactions. The tasks are modeled within a partially observable Markov decision process to assess agents’ capacity to interpret multimodal inputs, execute navigation, and accomplish user-defined objectives across complex visual and textual information on websites.

- [Caution for the Environment: Multimodal Agents are Susceptible to Environmental Distractions](https://arxiv.org/abs/2408.xxxxx)
    - [Author information not available]
    - August 2024
    - arXiv
    - Env: General
    - Key: multimodal agents, environmental distractions, robustness
    - TLDR: This paper highlights the vulnerability of multimodal agents to environmental distractions. The researchers demonstrate that these agents, which process multiple types of input (e.g., text, images, audio), can be significantly impacted by irrelevant or misleading environmental cues. The study provides insights into the limitations of current multimodal systems and emphasizes the need for more robust architectures that can filter out distractions and maintain focus on relevant information in complex, real-world environments.

- [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://arxiv.org/abs/2408.06327)
    - Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Yifan Xu, Xixuan Song, Shudan Zhang, Hanyu Lai, Xinyi Liu, Hanlin Zhao, et al.
    - August 12, 2024
    - arXiv
    - Env: GUI, Embodied, Visual Design
    - Key: benchmark, dataset, multimodal models, visual foundation agents
    - TLDR: This paper introduces VisualAgentBench (VAB), a comprehensive benchmark for developing and evaluating large multimodal models as visual foundation agents. VAB includes five distinct environments across three types of tasks: Embodied (OmniGibson, Minecraft), GUI (Mobile, WebArena-Lite), and Visual Design (CSS). The authors provide a trajectory training set for behavior cloning and evaluate nine proprietary LMM APIs and eight open models. Results show significant improvements in open LMMs through finetuning on VAB, approaching the performance of top proprietary models.

- [AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/abs/2408.11824)
    - Yanda Li, Chi Zhang, Wanqi Yang, Bin Fu, Pei Cheng, Xin Chen, Ling Chen, Yunchao Wei
    - August 23, 2024
    - arXiv
    - Env: Mobile
    - Key: framework, multimodal agent, mobile interactions, flexible action space
    - TLDR: This paper introduces AppAgent v2, an advanced multimodal agent framework for mobile devices. The system emulates human-like interactions and constructs a flexible action space that enhances adaptability across various applications. It operates in two phases: exploration (documenting UI element functionalities) and deployment (using RAG technology for efficient knowledge retrieval). AppAgent v2 demonstrates superior performance in handling complex, multi-step operations across various applications, showing its effectiveness in real-world scenarios.

- [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://arxiv.org/abs/2409.xxxxx)
    - [Author information not available]
    - September 2024
    - arXiv
    - Env: Mobile
    - Key: model, vision-language model, UI understanding, mobile interfaces
    - TLDR: This paper presents MobileVLM, a vision-language model specifically designed for understanding mobile user interfaces. The model improves both intra-UI understanding (relationships between elements within a single screen) and inter-UI understanding (connections across different screens or app states). MobileVLM demonstrates enhanced performance in tasks such as UI element classification, layout analysis, and task planning across mobile applications, potentially advancing the development of more intelligent mobile assistants and automated testing tools.

- [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena)
    - Rogerio Bonatti, Michael Nuñez, and others
    - September 2024
    - Microsoft Research
    - Env: Desktop
    - Key: benchmark, multimodal agents, OS interaction, cloud-based parallelization, Windows applications
    - TLDR: Windows Agent Arena is a benchmarking platform for AI agents operating within the Windows OS, testing their capabilities on over 150 tasks across applications like Notepad, Edge, and File Explorer. This environment utilizes Azure cloud infrastructure to parallelize task evaluation, dramatically reducing testing time to minutes. In trials, Microsoft’s agent "Navi" achieved a 19.5% success rate, highlighting ongoing challenges for multimodal agents in replicating human task performance in OS environments. This platform advances agent capabilities in realistic, desktop-based scenarios, supporting broader developments in productivity-focused AI tools.

- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)
    - Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig
    - September 11, 2024
    - arXiv
    - Env: Web
    - Key: framework, workflow induction, agent memory, web navigation
    - TLDR: This paper introduces Agent Workflow Memory (AWM), a method for inducing and utilizing reusable task workflows to improve agent performance on complex web navigation tasks. AWM works in both offline and online scenarios, inducing workflows from training examples or on-the-fly from test queries. Experiments on Mind2Web and WebArena benchmarks show substantial improvements in success rates (24.6% and 51.1% relative increases) and efficiency. AWM demonstrates robust generalization across tasks, websites, and domains, outperforming baselines by 8.9 to 14.0 absolute points as task distribution gaps widen.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://arxiv.org/abs/2410.05243)
    - Boyu Gou, Ruochen Wang, Boyuan Zheng, Yucheng Xie, Chengxuan Chang, Yuhang Shu, Haotian Sun, Yu Su
    - October 7, 2024
    - arXiv
    - Env: GUI
    - Key: framework, visual grounding, GUI agents, cross-platform generalization
    - TLDR: This paper introduces UGround, a universal visual grounding model for GUI agents that enables human-like navigation of digital interfaces. The authors advocate for GUI agents with human-like embodiment that perceive the environment entirely visually and take pixel-level actions. UGround is trained on a large-scale synthetic dataset of 10M GUI elements across 1.3M screenshots. Evaluated on six benchmarks spanning grounding, offline, and online agent tasks, UGround significantly outperforms existing visual grounding models by up to 20% absolute. Agents using UGround achieve comparable or better performance than state-of-the-art agents that rely on additional textual input, demonstrating the feasibility of vision-only GUI agents.

- [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164)
    - Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang
    - October 10, 2024
    - arXiv
    - Env: GUI
    - Key: framework, autonomous GUI interaction, experience-augmented hierarchical planning
    - TLDR: This paper introduces Agent S, an open agentic framework that enables autonomous interaction with computers through a Graphical User Interface (GUI). The system addresses key challenges in automating computer tasks through experience-augmented hierarchical planning and an Agent-Computer Interface (ACI). Agent S demonstrates significant improvements over baselines on the OSWorld benchmark, achieving a 20.58% success rate (83.6% relative improvement). The framework shows generalizability across different operating systems and provides insights for developing more effective GUI agents.

- [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://arxiv.org/abs/2410.13824)
    - Junpeng Liu, Tianyue Ou, Yifan Song, Yuxiao Qu, Wai Lam, Chenyan Xiong, Wenhu Chen, Graham Neubig, Xiang Yue
    - October 17, 2024
    - arXiv
    - Env: Web
    - Key: dataset, multimodal, text-rich visual understanding, accessibility trees, web UI comprehension
    - TLDR: This paper introduces *MultiUI*, a large-scale dataset containing 7.3 million annotated samples from 1 million websites, specifically designed to enhance multimodal large language models’ (MLLMs) capabilities in text-rich visual understanding. Utilizing webpage UI structures as a training resource, MultiUI provides robust accessibility tree data paired with UI screenshots, significantly improving MLLMs’ grounding, OCR, and interaction performance. Models trained with MultiUI achieve up to a 48% performance boost on VisualWebBench and demonstrate enhanced generalization across non-web tasks, setting a new standard for structured, visually integrated web data modeling.

- [AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?](https://arxiv.org/abs/2407.15711)
    - Ori Yoran, Samuel Joseph Amouyal, Chaitanya Malaviya, Ben Bogin, Ofir Press, Jonathan Berant
    - October 21, 2024
    - arXiv
    - Env: Web
    - Key: benchmark, dataset, planning and reasoning, web task automation
    - TLDR: AssistantBench is a benchmark designed to test the abilities of web agents in completing time-intensive, realistic web-based tasks. Covering 214 tasks across various domains, the benchmark introduces the SPA (See-Plan-Act) framework to handle multi-step planning and memory retention. AssistantBench emphasizes realistic task completion, showing that current agents achieve only modest success, with significant improvements needed for complex information synthesis and execution across multiple web domains.
