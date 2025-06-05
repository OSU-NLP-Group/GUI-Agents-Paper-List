- [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897)
    - Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiachong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu
    - 🏛️ Institutions: HKU, Shanghai AI Lab, Fudan University, Peking University, Nanjing University, Yale University
    - 📅 Date: May 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [grounding], [Qwen2.5-VL], [UI-TARS], [UGround], [OS-Atlas]
    - 📖 TLDR: This paper introduces *ScienceBoard*, a dynamic multimodal environment for evaluating autonomous agents in realistic scientific workflows. Built on an Ubuntu-based VM with integrated scientific software supporting both GUI and CLI interactions, the environment enables agents to operate like human researchers. Based on this infrastructure, ScienceBoard curates a benchmark of 169 human-validated tasks spanning six domains, including biochemistry, astronomy, GIS, and theorem proving. Evaluations of both general-purpose LLMs and GUI action models show that even state-of-the-art agents achieve only ~15% success, highlighting the substantial gap between current agent capabilities and real-world scientific demands.

- [UFO2: The Desktop AgentOS](https://arxiv.org/abs/2504.14603)
    - Chaoyun Zhang, He Huang, Chiming Ni, Jian Mu, Si Qin, Shilin He, Lu Wang, Fangkai Yang, Pu Zhao, Chao Du, Liqun Li, Yu Kang, Zhao Jiang, Suzhen Zheng, Rujia Wang, Jiaxu Qian, Minghua Ma, Jian-Guang Lou, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
    - 🏛️ Institutions: Microsoft Research, ZJU-UIUC Institute, Nanjing University, Peking University
    - 📅 Date: April 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [hybrid control], [multi-agent], [speculative execution], [knowledge substrate], [UFO2]
    - 📖 TLDR: UFO2 introduces a multi-agent AgentOS for Windows desktops, aiming to transform Computer-Using Agents (CUAs) from fragile prototypes into robust, system-level automation tools. It features a centralized HostAgent for task decomposition and coordination, along with specialized AppAgents equipped with native APIs and domain-specific knowledge. The system employs a hybrid control detection pipeline combining Windows UI Automation with vision-based parsing, and enhances runtime efficiency through speculative multi-action planning. A Picture-in-Picture interface allows agents and users to operate concurrently without interference. Evaluated across over 20 real-world Windows applications, UFO2 demonstrates significant improvements in robustness and execution accuracy over prior CUAs.

- [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661)
    - Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Juan A. Rodriguez, Montek Kalsi, Rabiul Awal, Nicolas Chapados, M. Tamer Özsu, Aishwarya Agrawal, David Vazquez, Christopher Pal, Perouz Taslakian, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [framework], [UI-Vision], [UI-TARS-72B], [spatial reasoning], [drag-and-drop], [element grounding], [layout grounding], [action prediction]
    - 📖 TLDR: This paper introduces *UI-Vision*, a comprehensive, license-permissive benchmark designed for evaluating autonomous agents in real-world desktop GUI environments. It encompasses 83 software applications with dense annotations of human demonstrations, including bounding boxes, UI labels, and action trajectories. The benchmark defines three tasks—Element Grounding, Layout Grounding, and Action Prediction—to assess agents' performance. Evaluations reveal limitations in state-of-the-art models like UI-TARS-72B, particularly in understanding professional software, spatial reasoning, and complex actions such as drag-and-drop. By releasing UI-Vision as open-source, the authors aim to advance the development of more capable agents for desktop tasks.

- [STEVE: A Step Verification Pipeline for Computer-use Agent Training](https://github.com/FanbinLu/STEVE)
    - Fanbin Lu, Zhisheng Zhong, Ziqin Wei, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: CUHK, SmartMore, HKUST
    - 📅 Date: March 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [model], [UI grounding], [KTO], [GPT-4o], [WinAgentArena]
    - 📖 TLDR: This paper introduces **STEVE**, a step verification pipeline designed to enhance the training of computer-use agents. The approach involves creating a large instruction set and collecting trajectory data using suboptimal agents. GPT-4o is employed to verify the correctness of each action step by comparing pre- and post-action screenshots, assigning binary labels. The agent is then optimized using Kahneman and Tversky Optimization (KTO) based on these labels. The result is a 7B vision-language model that achieves state-of-the-art performance in the WinAgentArena desktop environment, outperforming supervised fine-tuning methods by effectively leveraging both positive and negative action data.

- [DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents](https://arxiv.org/abs/2503.11170)
    - Yibin Xu, Liang Yang, Hao Chen, Hua Wang, Zhi Chen, Yaohua Tang
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [model], [AutoCaptioner], [DeskVision], [DeskVision-Eval], [GUIExplorer]
    - 📖 TLDR: This paper introduces *AutoCaptioner*, an automated pipeline for generating richly annotated GUI data with minimal human effort. Utilizing AutoCaptioner, the authors created *DeskVision*, a large-scale desktop GUI dataset comprising 54,855 images and over 303,622 annotations across various operating systems. They also developed *DeskVision-Eval*, the largest desktop benchmark reflecting daily usage scenarios. Leveraging DeskVision, the authors trained *GUIExplorer*, a GUI understanding model that achieves state-of-the-art performance in grounding visual elements without complex architectural designs. The effectiveness of DeskVision was further validated through ablation studies on various large visual language models (LVLMs).

- [In-Context Defense in Computer Agents: An Empirical Study](https://arxiv.org/abs/2503.09241)
    - Pei Yang, Hai Ci, Mike Zheng Shou
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [defense], [in-context learning], [chain-of-thought], [context deception], [security]
    - 📖 TLDR: This paper introduces an in-context defense strategy for computer agents powered by vision-language models (VLMs), targeting context deception attacks such as malicious pop-ups and deceptive HTML elements. By incorporating a small set of curated exemplars and employing chain-of-thought reasoning, the approach guides agents to perform explicit defensive reasoning before action planning. Experiments demonstrate significant reductions in attack success rates across various attack types, highlighting the effectiveness of the method in enhancing agent reliability without requiring model fine-tuning.

- [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://likaixin2000.github.io/papers/ScreenSpot_Pro.pdf)
    - Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, Tat-Seng Chua
    - 🏛️ Institutions: NUS, ECNU, HKBU
    - 📅 Date: January 3, 2025
    - 📑 Publisher: GitHub
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [GUI grounding], [high-resolution], [ScreenSpot-Pro]
    - 📖 TLDR: ScreenSpot-Pro introduces a benchmark designed to evaluate GUI grounding models in professional, high-resolution environments. It encompasses 1,581 tasks across 23 applications in various industries, highlighting the challenges models face with complex software interfaces. Current models achieve low accuracy, underscoring the need for further research in this domain.

- [PC Agent: While You Sleep, AI Works -- A Cognitive Journey into Digital World](https://arxiv.org/abs/2412.17589)
    - Yanheng He, Jiahe Jin, Shijie Xia, Jiadi Su, Runze Fan, Haoyang Zou, Xiangkun Hu, Pengfei Liu
    - 🏛️ Institutions: SJTU
    - 📅 Date: Dec 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [PC Agent], [human cognition transfer], [PC Tracker], [Cognition Completion], [multi-agent system]
    - 📖 TLDR: This paper introduces *PC Agent*, an AI system designed to autonomously perform complex computer-based tasks by emulating human cognitive processes. The system comprises three key components: **PC Tracker**, a lightweight infrastructure for collecting high-quality human-computer interaction data; a **Cognition Completion** pipeline that enriches raw interaction data into detailed cognitive trajectories; and a **multi-agent system** combining a planning agent for decision-making with a grounding agent for precise visual grounding. This approach represents a significant advancement toward AI systems capable of handling intricate real-world work autonomously.

- [The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](https://arxiv.org/abs/2411.10323)
    - Siyuan Hu, Mingyu Ouyang, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: NUS
    - 📅 Date: Nov 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [Claude 3.5 Computer Use], [GUI automation], [planning], [action], [critic]
    - 📖 TLDR: This study evaluates Claude 3.5 Computer Use, an AI model enabling end-to-end language-to-desktop actions, through curated tasks across various domains. It introduces an out-of-the-box framework for deploying API-based GUI automation models, analyzing the model's planning, action execution, and adaptability to dynamic environments.

- [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://microsoft.github.io/WindowsAgentArena/)
    - Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, Yadong Lu, Justin Wagle, Kazuhito Koishida, Arthur Bucker, Lawrence Jang, Zack Hui
    - 🏛️ Institutions: Microsoft
    - 📅 Date: September 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [Navi]
    - 📖 TLDR: This paper introduces the *Windows Agent Arena (WAA)*, a scalable platform for testing and benchmarking multi-modal AI agents within a realistic Windows OS environment. WAA enables researchers to evaluate agentic workflows across diverse tasks and supports large-scale deployment using Azure ML. The study also presents *Navi*, a multi-modal agent achieving a 19.5% success rate on Windows tasks, highlighting the platform's potential for advancing AI agent development.

- [TinyAgent: Function Calling at the Edge](https://github.com/SqueezeAILab/TinyAgent)
    - Lutfi Eren Erdogan, Nicholas Lee, Siddharth Jha, Sehoon Kim, Ryan Tabrizi, Suhong Moon, Coleman Hooper, Gopala Anumanchipalli, Kurt Keutzer, Amir Gholami
    - 🏛️ Institutions: UC Berkeley, ICSI
    - 📅 Date: September 1, 2024
    - 📑 Publisher: EMNLP 2024
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [quantization], [LLMCompiler], [TinyAgent-1.1B], [TinyAgent-7B]
    - 📖 TLDR: This paper introduces TinyAgent, an end-to-end framework for training and deploying task-specific small language model agents capable of function calling at the edge. By fine-tuning small models with curated datasets and employing techniques like quantization and a novel tool retrieval method, TinyAgent enables efficient, real-time execution of user commands on local devices without relying on cloud infrastructure. The framework demonstrates that these small models can match or even surpass the function-calling capabilities of larger models like GPT-4-Turbo while operating entirely on edge devices.

- [OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation](https://arxiv.org/abs/2407.19056)
    - Zilong Wang, Yuedong Cui, Li Zhong, Zimin Zhang, Da Yin, Bill Yuchen Lin, Jingbo Shang
    - 🏛️ Institutions: UCSD, UCLA, AI2
    - 📅 Date: July 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multi-application], [office automation]
    - 📖 TLDR: OfficeBench introduces a benchmark that evaluates language models' ability to automate office tasks across a range of applications like Word, Excel, and email. The benchmark tests agents’ skills in task-switching, planning, and decision-making by simulating realistic office workflows. Current models, including GPT-4, demonstrate significant gaps in task accuracy and efficiency, revealing areas for improvement in managing complex, multi-application tasks in office environments.

- [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://spider2-v.github.io/)
    - Ruisheng Cao, Fangyu Lei, Haoyuan Wu, Jixuan Chen, Yeqiao Fu, Hongcheng Gao, Xinzhuang Xiong, Hanchong Zhang, Yuchen Mao, Wenjing Hu, Tianbao Xie, Hongsheng Xu, Danyang Zhang, Sida Wang, Ruoxi Sun, Pengcheng Yin, Caiming Xiong, Ansong Ni, Qian Liu, Victor Zhong, Lu Chen, Kai Yu, Tao Yu
    - 🏛️ Institutions: HKU, SJTU, Google Cloud AI Research, Google DeepMind, Salesforce Research, Yale University, Sea AI Lab, University of Waterloo
    - 📅 Date: July 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [data science], [engineering workflows], [Spider2-V]
    - 📖 TLDR: This paper introduces **Spider2-V**, a multimodal agent benchmark designed to evaluate the capability of agents in automating professional data science and engineering workflows. It comprises 494 real-world tasks across 20 enterprise-level applications, assessing agents' proficiency in code generation and GUI operations within authentic computer environments.

- [GUI Action Narrator: Where and When Did That Action Take Place?](https://showlab.github.io/GUI-Narrator/)
    - Qinchen Wu, Difei Gao, Kevin Qinghong Lin, Zhuoyu Wu, Xiangwu Guo, Peiran Li, Weichen Zhang, Hengxu Wang, Mike Zheng Shou
    - 🏛️ Institutions: NUS, Chinese Academy of Sciences
    - 📅 Date: June 19, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [framework], [Act2Cap], [GUI Narrator]
    - 📖 TLDR: The authors present **Act2Cap**, a GUI action dataset containing 4,189 video-caption pairs depicting various GUI actions such as clicks, drags, and typing across multiple software environments. They also propose **GUI Narrator**, a framework that leverages cursor detection as a visual prompt to enhance the interpretation of high-resolution screenshots for GUI video captioning. Evaluations reveal that even advanced multimodal models face challenges in this domain, highlighting the need for specialized approaches to improve performance.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://arxiv.org/abs/2406.10227)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen WU, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: NUS, Microsoft Gen AI
    - 📅 Date: June 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [Desktop, Web]
    - 🔑 Key: [benchmark], [instructional videos], [visual planning], [hierarchical task decomposition], [complex software interaction]
    - 📖 TLDR: VideoGUI presents a benchmark for evaluating GUI automation on tasks derived from instructional videos, focusing on visually intensive applications like Adobe Photoshop and video editing software. The benchmark includes 178 tasks, with a hierarchical evaluation method distinguishing high-level planning, mid-level procedural steps, and precise action execution. VideoGUI reveals current model limitations in complex visual tasks, marking a significant step toward improved visual planning in GUI automation.

- [AgentStudio: A Toolkit for Building General Virtual Agents](https://arxiv.org/abs/2403.17918)
    - Longtao Zheng, Zhiyuan Huang, Zhenghai Xue, Xinrun Wang, Bo An, Shuicheng Yan
    - 🏛️ Institutions: NTU, Skywork AI, ETH Zurich
    - 📅 Date: March 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [general virtual agents], [open-ended learning], [tool creation], [GroundUI], [benchmark]
    - 📖 TLDR: AgentStudio is a robust toolkit for developing virtual agents with versatile actions, such as GUI automation and code execution. It unifies real-world human-computer interactions across OS platforms and includes diverse observation and action spaces, facilitating comprehensive training and benchmarking in complex settings. The toolkit's flexibility promotes agent generalization across varied tasks, supporting tool creation and a multimodal interaction interface to advance agent adaptability and learning.

- [Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II as a Case Study](https://arxiv.org/abs/2403.03186)
    - Weihao Tan, Ziluo Ding, Wentao Zhang, Boyu Li, Bohan Zhou, Junpeng Yue, Haochong Xia, Jiechuan Jiang, Longtao Zheng, Xinrun Xu, Yifei Bi, Pengjie Gu, Xinrun Wang, Börje F. Karlsson, Bo An, Zongqing Lu
    - 🏛️ Institutions: NTU, BAAI, PKU
    - 📅 Date: March 5, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [Cradle], [General Computer Control], [multimodal], [keyboard and mouse control], [long-term memory], [reasoning], [self-improvement]
    - 📖 TLDR: This paper introduces *Cradle*, a framework designed to achieve General Computer Control (GCC) by enabling agents to perform any computer task using only screen images (and possibly audio) as input and producing keyboard and mouse operations as output. The authors deploy Cradle in the complex AAA game Red Dead Redemption II, demonstrating its capability to follow the main storyline and complete real missions with minimal reliance on prior knowledge or resources.

- [Cradle: Empowering Foundation Agents Towards General Computer Control](https://arxiv.org/abs/2403.03186)
    - Weihao Tan, Wentao Zhang, Xinrun Xu, Haochong Xia, Ziluo Ding, Boyu Li, Bohan Zhou, Junpeng Yue, Jiechuan Jiang, Yewen Li, Ruyi An, Molei Qin, Chuqiao Zong, Longtao Zheng, Yujie Wu, Xiaoqiang Chai, Yifei Bi, Tianbao Xie, Pengjie Gu, Xiyun Li, Ceyao Zhang, Long Tian, Chaojie Wang, Xinrun Wang, Börje F. Karlsson, Bo An, Shuicheng Yan, Zongqing Lu
    - 🏛️ Institutions: Skywork AI, BAAI, NTU, PKU, Institute of Software - Chinese Academy of Sciences, HKU, CUHK
    - 📅 Date: March 5, 2024
    - 📑 Publisher: TBD
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [general computer control], [skill curation], [self-improvement]
    - 📖 TLDR: This paper introduces the Cradle framework, designed to enable general computer control (GCC) through multimodal input (e.g., screen images and optional audio) and outputs (keyboard and mouse). Cradle’s six core modules, including self-reflection, skill curation, and memory, allow for generalized task handling in complex environments like AAA games. Demonstrated in *Red Dead Redemption II*, the framework exhibits adaptability by performing real missions and following the storyline with minimal prior knowledge, showcasing its potential as a generalist agent for diverse computer tasks.

- [UFO: A UI-Focused Agent for Windows OS Interaction](https://arxiv.org/abs/2402.07939)
    - Chaoyun Zhang, Liqun Li, Shilin He, Xu Zhang, Bo Qiao, Si Qin, Minghua Ma, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Microsoft
    - 📅 Date: February 14, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [UI automation], [Windows], [UFO]
    - 📖 TLDR: This paper presents UFO, a pioneering multimodal LLM-based agent designed to fulfill user requests on Windows OS. UFO employs a dual-agent architecture—comprising AppAgent and ActAgent—that can interpret and execute complex tasks across multiple Windows applications by observing UI elements and utilizing control interactions. The framework allows UFO to handle intricate, cross-application workflows and execute commands seamlessly based on natural language prompts. It integrates GPT-Vision to recognize and interact with graphical elements, enabling flexible, autonomous task completion within and across diverse Windows applications.

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)
    - Zhiyong Wu, Chengcheng Han, Zichen Ding, Zhenmin Weng, Zhoumianze Liu, Shunyu Yao, Tao Yu, Lingpeng Kong
    - 🏛️ Institutions: Shanghai AI Lab, East China Normal University, Princeton, HKU
    - 📅 Date: February 12, 2024
    - 📑 Publisher: ICLR 2024 Workshop LLMAgents
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [self-directed learning], [GAIA], [FRIDAY], [OS-Copilot]
    - 📖 TLDR: The OS-Copilot framework supports building generalist agents capable of performing diverse tasks across an operating system (OS). This work introduces FRIDAY, an embodied agent using OS-Copilot to self-improve by learning from task outcomes. It operates with a memory-based architecture to tackle OS-level tasks across applications like terminals, web browsers, and third-party tools. Tested on the GAIA benchmark, FRIDAY achieved 35% higher performance than prior methods, proving effective in adapting to unfamiliar applications and refining its capabilities with minimal guidance.

- [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553)
    - Raghav Kapoor, Yash Parag Butala, Melisa Russak, Jing Yu Koh, Kiran Kamble, Waseem Alshikh, Ruslan Salakhutdinov
    - 🏛️ Institutions: CMU
    - 📅 Date: February 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [benchmark]
    - 📖 TLDR: OmniACT introduces a dataset and benchmark to train and evaluate multimodal agents capable of autonomously performing diverse tasks across desktop and web environments. Using annotated UI elements across applications, it combines visual grounding with natural language instructions, providing 9,802 data points for developing agents that integrate high-level reasoning with UI interactions. The study highlights the limited proficiency of current models, with baselines like GPT-4 only achieving 15% of human performance on executable scripts, emphasizing OmniACT's potential as a testbed for advancing multimodal AI.

- [AssistGUI: Task-Oriented Desktop Graphical User Interface Automation](https://arxiv.org/abs/2312.13108)
    - Difei Gao, Lei Ji, Zechen Bai, Mingyu Ouyang, Peiran Li, Dongxing Mao, Qinchen Wu, Weichen Zhang, Peiyi Wang, Xiangwu Guo, Hengxu Wang, Luowei Zhou, Mike Zheng Shou
    - 🏛️ Institutions: NUS
    - 📅 Date: December 20, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [desktop productivity tasks]
    - 📖 TLDR: This study presents *AssistGUI*, a benchmark and framework for desktop GUI automation, featuring an LLM-based agent capable of completing complex user requests by analyzing instructional videos and performing actions on the desktop. Utilizing a novel Actor-Critic framework and GUI parser, *AssistGUI* was tested on 100 tasks across nine applications, such as MS Word and After Effects. Despite advances, the top-performing model achieved only a 46% success rate, illustrating the challenge of comprehensive desktop automation and underscoring areas for future research in agent-driven GUI tasks.

- [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863)
    - Longtao Zheng, Rundong Wang, Xinrun Wang, Bo An
    - 🏛️ Institutions: NTU
    - 📅 Date: June 13, 2023
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [trajectory prompting], [state abstraction], [memory retrieval]
    - 📖 TLDR: Synapse introduces a novel framework for computer control tasks, leveraging trajectory-as-exemplar prompting and memory to enhance LLM performance in complex, multi-step computer tasks. The system combines state abstraction, trajectory-based prompts, and memory retrieval, overcoming LLM limitations by filtering task-irrelevant data, storing exemplar trajectories, and retrieving relevant instances for improved decision-making. Synapse achieves significant performance gains on benchmarks such as MiniWoB++ and Mind2Web, demonstrating enhanced task success rates and generalization across diverse web-based tasks.

- [Language Models can Solve Computer Tasks](https://arxiv.org/abs/2303.17491)
    - Geunwoo Kim, Pierre Baldi, Stephen McAleer
    - 🏛️ Institutions: UCI
    - 📅 Date: March 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [Recursive Critique and Improve], [RCI], [MiniWoB++], [general computer tasks]
    - 📖 TLDR: This study demonstrates that large language models (LLMs) can effectively automate computer tasks using a Recursive Critique and Improve (RCI) prompting method, enabling agents to handle complex desktop tasks like email and file management. By combining RCI with existing Chain of Thought (CoT) prompting, the method outperforms prior LLM approaches and traditional supervised and reinforcement learning models on the **MiniWoB++** benchmark, showing potential for broad computer task automation.

- [A Data-Driven Approach for Learning to Control Computers](https://arxiv.org/abs/2202.08137)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - 🏛️ Institutions: DeepMind
    - 📅 Date: February 16, 2022
    - 📑 Publisher: ICML 2022
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [framework], [computer control], [reinforcement learning], [multimodal transformer]
    - 📖 TLDR: This study presents a reinforcement learning-based approach to train agents for computer control tasks, using keyboard and mouse interactions guided by natural language. By leveraging human demonstration data, agents trained in this environment achieved strong cross-task generalization across the MiniWob++ benchmark. This framework demonstrates how agents can control computers as humans would, enabling enhanced performance in complex computer tasks with high transferability.
