- [IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/abs/2602.17049)
    - Seoyoung Lee, Seobin Yoon, Seongbeen Lee, Yoojung Chun, Dayoung Park, Doyeon Kim, Joo Yong Sim
    - 🏛️ Institutions: Sookmyung Women's University
    - 📅 Date: February 19, 2026
    - 📑 Publisher: AAMAS 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [multi-agent], [memory], [planning], [skill abstraction], [intent representation], [IntentCUA]
    - 📖 TLDR: This paper introduces IntentCUA, a multi-agent computer-use framework for stabilizing long-horizon desktop automation through intent-aligned plan memory. It learns intent-level representations from interaction traces, abstracts reusable skills, and coordinates a Planner, Plan-Optimizer, and Critic over shared memory to reduce redundant replanning and error accumulation. On end-to-end evaluations over desktop applications, IntentCUA outperforms RL-based and trajectory-centric baselines, highlighting intent abstraction and memory-grounded multi-agent planning as an effective systems design for computer-use agents.

- [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://openreview.net/forum?id=bJvwJahJeF)
    - Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiaochong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu
    - 🏛️ Institutions: The University of Hong Kong, Shanghai AI Laboratory, Fudan University, Peking University, Nanjing University, East China Normal University, Yale University
    - 📅 Date: January 26, 2026
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [environment], [POMDP], [GUI/CLI agents], [multimodal], [modular design], [ScienceBoard]
    - 📖 TLDR: Introduces **ScienceBoard**, a first-of-its-kind realistic multimodal environment and benchmark (169 tasks across six scientific domains) for evaluating agents that operate GUI and CLI workflows. Agents like GPT‑4o and Claude reach only ~15% success, revealing limitations in visual grounding and domain reasoning. Modular agent designs (separating planning and action) improve performance. Environment integrates real scientific tools via VM, accessibility trees, and screenshot inputs, setting the stage for more capable AI co‑scientists.

- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596)
    - Haojia Lin, Xiaoyu Tan, Yulei Qin, Zihan Xu, Yuchen Shi, Zongyi Li, Gang Li, Shaofei Cai, Siqi Cai, Chaoyou Fu, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, Peking University, Nanjing University
    - 📅 Date: October 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [reward model], [computer-using agent], [CUARewardBench], [Unanimous Prompt Ensemble (UPE)]
    - 📖 TLDR: This paper introduces CUARewardBench, the first benchmark for evaluating reward models tailored to computer-using agents. It includes step-level and trajectory-level annotations from tasks across 10 software types and 7 agent architectures. The study identifies the limitations of current reward models and proposes UPE, a prompting-based method that significantly improves evaluation accuracy.

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Z.AI, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [benchmark], [API-GUI paradigm], [dataset], [distributed RL], [Entropulse]
    - 📖 TLDR: This paper presents **ComputerRL**, a large-scale end-to-end reinforcement learning framework enabling agents to operate complex desktop tasks. It introduces the **API-GUI paradigm**, combining programmatic API calls with GUI actions, and a **distributed RL infrastructure** managing thousands of parallel virtual Ubuntu desktops for scalable training. A novel **Entropulse** training strategy alternates between reinforcement learning and supervised fine-tuning to prevent entropy collapse over long training runs. Applied to open models like GLM-4-9B-0414, ComputerRL achieves a new state-of-the-art success rate of **48.9%** on the OSWorld benchmark via the GLM-ComputerRL-9B model.

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y. Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Moonshot AI, Stanford University, University of Waterloo, Carnegie Mellon University
    - 📅 Date: August 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [chain-of-thought], [vision language model], [AgentNet]
    - 📖 TLDR: Introduces **OpenCUA**, an open-source framework to train computer-use agents (CUAs) using vision-language models. It includes a cross-platform annotation tool (AgentNet Tool), a large-scale dataset covering 3 OSes and 200+ apps/websites (AgentNet), and a data processing pipeline that builds state-action pairs enhanced with reflective long chain-of-thought reasoning. The resulting models—especially OpenCUA-72B—achieve SOTA performance on the OSWorld-Verified benchmark (45.0% success), surpassing prior open-source baselines and demonstrating strong generalization and scalability. All tools, models, and data are publicly released.

- [CoAct‑1: Computer‑using Multi-agent System with Coding Actions](https://arxiv.org/abs/2508.03923)
    - Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese, Zeyuan Chen, Jieyu Zhao, Ran Xu, Caiming Xiong
    - 🏛️ Institutions: University of Southern California, Salesforce Research, University of Washington
    - 📅 Date: August 5, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [hybrid agent], [coding action], [multi-agent system], [OSWorld]
    - 📖 TLDR: This paper introduces **CoAct‑1**, a multi-agent system where an Orchestrator coordinates between a GUI Operator and a Programmer agent that can execute code (Python/Bash) directly. This hybrid design allows the agent to perform complex desktop tasks more efficiently than GUI-only agents. Evaluated on OSWorld and WindowsAgentArena, CoAct‑1 achieves state-of-the-art success rates of 60.8% and 52.5% respectively, while reducing average steps to 10.15.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, and Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: June 4, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multilingual], [safety], [macOSWorld]
    - 📖 TLDR: Introduces **macOSWorld**, the first interactive benchmark for GUI agents on macOS, with 202 tasks across 30 apps (28 macOS-exclusive) in 5 languages plus a safety subset for deception attacks; evaluates 6 agents, showing proprietary CUAs outperform open-source and VLM-based agents, significant language gaps (Arabic –27.5%), and both grounding and safety challenges.

- [UI-Evol: Automatic Knowledge Evolving for Computer Use Agents](https://arxiv.org/abs/2505.21964)
    - Ziyun Zhang, Xinyi Liu, Xiaoyi Zhang, Jun Wang, Gang Chen, Yan Lu
    - 🏛️ Institutions: Peking University, Microsoft Research Asia
    - 📅 Date: May 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [knowledge-execution gap], [Critique Stage], [Retrace Stage], [OSWorld], [self‑evolution]
    - 📖 TLDR: The paper identifies a “knowledge‑execution gap” where even highly accurate external knowledge (90%) only yields a 41% execution success rate. To bridge this, the authors introduce **UI‑Evol**, a plug‑and‑play two‑stage module for GUI agents—**Retrace** recovers actual action sequences from real agent–environment interactions, and **Critique** refines knowledge by comparing these sequences with external references. Experiments using Agent S2 on the OSWorld benchmark show significant gains in task performance and reduced behavioral variance, improving agent reliability.

- [LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS](https://arxiv.org/abs/2505.18829)
    - Kai Mei, Xi Zhu, Hang Gao, Shuhang Lin, and Yongfeng Zhang
    - 🏛️ Institutions: Rutgers University, AIOS Foundation
    - 📅 Date: May 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [model context protocol], [MCP], [OSWorld], [LiteCUA]
    - 📖 TLDR: Introduces AIOS 1.0, which contextualizes desktop computer states via an MCP server so LLM-powered agents can better understand and operate GUIs. Built on top, LiteCUA—a lightweight agent—achieves 14.66 % success on the OSWorld benchmark, outperforming several heavier agent frameworks, showing the benefits of environment contextualization.

- [UFO2: The Desktop AgentOS](https://arxiv.org/abs/2504.14603)
    - Chaoyun Zhang, He Huang, Chiming Ni, Jian Mu, Si Qin, Shilin He, Lu Wang, Fangkai Yang, Pu Zhao, Chao Du, Liqun Li, Yu Kang, Zhao Jiang, Suzhen Zheng, Rujia Wang, Jiaxu Qian, Minghua Ma, Jian-Guang Lou, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
    - 🏛️ Institutions: Microsoft Research, Zhejiang University-University of Illinois Urbana-Champaign Institute, Nanjing University, Peking University
    - 📅 Date: April 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [hybrid control], [multi-agent], [speculative execution], [knowledge substrate], [UFO2]
    - 📖 TLDR: UFO2 introduces a multi-agent AgentOS for Windows desktops, aiming to transform Computer-Using Agents (CUAs) from fragile prototypes into robust, system-level automation tools. It features a centralized HostAgent for task decomposition and coordination, along with specialized AppAgents equipped with native APIs and domain-specific knowledge. The system employs a hybrid control detection pipeline combining Windows UI Automation with vision-based parsing, and enhances runtime efficiency through speculative multi-action planning. A Picture-in-Picture interface allows agents and users to operate concurrently without interference. Evaluated across over 20 real-world Windows applications, UFO2 demonstrates significant improvements in robustness and execution accuracy over prior CUAs.

- [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661)
    - Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Juan A. Rodriguez, Montek Kalsi, Rabiul Awal, Nicolas Chapados, M. Tamer Özsu, Aishwarya Agrawal, David Vazquez, Christopher Pal, Perouz Taslakian, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, Universite de Montreal, ServiceNow, University of Waterloo, National University of Singapore, Ecole de Technologie Superieure, CIFAR AI Chair, Polytechnique Montreal
    - 📅 Date: March 19, 2025
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [framework], [UI-Vision], [UI-TARS-72B], [spatial reasoning], [drag-and-drop], [element grounding], [layout grounding], [action prediction]
    - 📖 TLDR: This paper introduces *UI-Vision*, a comprehensive, license-permissive benchmark designed for evaluating autonomous agents in real-world desktop GUI environments. It encompasses 83 software applications with dense annotations of human demonstrations, including bounding boxes, UI labels, and action trajectories. The benchmark defines three tasks—Element Grounding, Layout Grounding, and Action Prediction—to assess agents' performance. Evaluations reveal limitations in state-of-the-art models like UI-TARS-72B, particularly in understanding professional software, spatial reasoning, and complex actions such as drag-and-drop. By releasing UI-Vision as open-source, the authors aim to advance the development of more capable agents for desktop tasks.

- [STEVE: A Step Verification Pipeline for Computer-use Agent Training](https://arxiv.org/abs/2503.12532)
    - Fanbin Lu, Zhisheng Zhong, Ziqin Wei, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: The Chinese University of Hong Kong, SmartMore, Hong Kong University of Science and Technology
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
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: March 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [defense], [in-context learning], [chain-of-thought], [context deception], [security]
    - 📖 TLDR: This paper introduces an in-context defense strategy for computer agents powered by vision-language models (VLMs), targeting context deception attacks such as malicious pop-ups and deceptive HTML elements. By incorporating a small set of curated exemplars and employing chain-of-thought reasoning, the approach guides agents to perform explicit defensive reasoning before action planning. Experiments demonstrate significant reductions in attack success rates across various attack types, highlighting the effectiveness of the method in enhancing agent reliability without requiring model fine-tuning.

- [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981)
    - Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, Tat-Seng Chua
    - 🏛️ Institutions: National University of Singapore, East China Normal University, Hong Kong Baptist University
    - 📅 Date: January 3, 2025
    - 📑 Publisher: ACM Multimedia 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [GUI grounding], [high-resolution], [ScreenSpot-Pro]
    - 📖 TLDR: ScreenSpot-Pro introduces a benchmark designed to evaluate GUI grounding models in professional, high-resolution environments. It encompasses 1,581 tasks across 23 applications in various industries, highlighting the challenges models face with complex software interfaces. Current models achieve low accuracy, underscoring the need for further research in this domain.

- [PC Agent: While You Sleep, AI Works -- A Cognitive Journey into Digital World](https://arxiv.org/abs/2412.17589)
    - Yanheng He, Jiahe Jin, Shijie Xia, Jiadi Su, Runze Fan, Haoyang Zou, Xiangkun Hu, Pengfei Liu
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: Dec 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [PC Agent], [human cognition transfer], [PC Tracker], [Cognition Completion], [multi-agent system]
    - 📖 TLDR: This paper introduces *PC Agent*, an AI system designed to autonomously perform complex computer-based tasks by emulating human cognitive processes. The system comprises three key components: **PC Tracker**, a lightweight infrastructure for collecting high-quality human-computer interaction data; a **Cognition Completion** pipeline that enriches raw interaction data into detailed cognitive trajectories; and a **multi-agent system** combining a planning agent for decision-making with a grounding agent for precise visual grounding. This approach represents a significant advancement toward AI systems capable of handling intricate real-world work autonomously.

- [The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](https://arxiv.org/abs/2411.10323)
    - Siyuan Hu, Mingyu Ouyang, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: Nov 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [Claude 3.5 Computer Use], [GUI automation], [planning], [action], [critic]
    - 📖 TLDR: This study evaluates Claude 3.5 Computer Use, an AI model enabling end-to-end language-to-desktop actions, through curated tasks across various domains. It introduces an out-of-the-box framework for deploying API-based GUI automation models, analyzing the model's planning, action execution, and adaptability to dynamic environments.

- [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://proceedings.mlr.press/v267/bonatti25a.html)
    - Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, Yadong Lu, Justin Wagle, Kazuhito Koishida, Arthur Bucker, Lawrence Keunho Jang, Zheng Hui
    - 🏛️ Institutions: Microsoft
    - 📅 Date: September 13, 2024
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [desktop agent], [Windows OS], [Navi], [Windows Agent Arena]
    - 📖 TLDR: This paper introduces the *Windows Agent Arena (WAA)*, a scalable platform for testing and benchmarking multi-modal AI agents within a realistic Windows OS environment. WAA enables researchers to evaluate agentic workflows across diverse tasks and supports large-scale deployment using Azure ML. The study also presents *Navi*, a multi-modal agent achieving a 19.5% success rate on Windows tasks, highlighting the platform's potential for advancing AI agent development.

- [TinyAgent: Function Calling at the Edge](https://aclanthology.org/2024.emnlp-demo.9/)
    - Lutfi Eren Erdogan, Nicholas Lee, Siddharth Jha, Sehoon Kim, Ryan Tabrizi, Suhong Moon, Coleman Richard Charles Hooper, Gopala Anumanchipalli, Kurt Keutzer, Amir Gholami
    - 🏛️ Institutions: UC Berkeley, ICSI
    - 📅 Date: September 1, 2024
    - 📑 Publisher: EMNLP 2024 System Demonstrations
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [function calling], [quantization], [LLMCompiler], [TinyAgent-1.1B], [TinyAgent-7B]
    - 📖 TLDR: This paper introduces TinyAgent, an end-to-end framework for training and deploying task-specific small language model agents capable of function calling at the edge. By fine-tuning small models with curated datasets and employing techniques like quantization and a novel tool retrieval method, TinyAgent enables efficient, real-time execution of user commands on local devices without relying on cloud infrastructure. The framework demonstrates that these small models can match or even surpass the function-calling capabilities of larger models like GPT-4-Turbo while operating entirely on edge devices.

- [OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation](https://arxiv.org/abs/2407.19056)
    - Zilong Wang, Yuedong Cui, Li Zhong, Zimin Zhang, Da Yin, Bill Yuchen Lin, Jingbo Shang
    - 🏛️ Institutions: University of California San Diego, University of California Los Angeles, Allen Institute for AI
    - 📅 Date: July 26, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multi-application], [office automation]
    - 📖 TLDR: OfficeBench introduces a benchmark that evaluates language models' ability to automate office tasks across a range of applications like Word, Excel, and email. The benchmark tests agents’ skills in task-switching, planning, and decision-making by simulating realistic office workflows. Current models, including GPT-4, demonstrate significant gaps in task accuracy and efficiency, revealing areas for improvement in managing complex, multi-application tasks in office environments.

- [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c2f71567cd53464161cab3336e8fc865-Abstract-Datasets_and_Benchmarks_Track.html)
    - Ruisheng Cao, Fangyu Lei, Haoyuan Wu, Jixuan Chen, Yeqiao Fu, Hongcheng Gao, Xinzhuang Xiong, Hanchong Zhang, Yuchen Mao, Wenjing Hu, Tianbao Xie, Hongsheng Xu, Danyang Zhang, Sida Wang, Ruoxi Sun, Pengcheng Yin, Caiming Xiong, Ansong Ni, Qian Liu, Victor Zhong, Lu Chen, Kai Yu, Tao Yu
    - 🏛️ Institutions: The University of Hong Kong, Shanghai Jiao Tong University, Google Cloud AI Research, Google DeepMind, Salesforce Research, Yale University, Sea AI Lab, University of Waterloo
    - 📅 Date: July 15, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [data science], [engineering workflows], [Spider2-V]
    - 📖 TLDR: This paper introduces **Spider2-V**, a multimodal agent benchmark designed to evaluate the capability of agents in automating professional data science and engineering workflows. It comprises 494 real-world tasks across 20 enterprise-level applications, assessing agents' proficiency in code generation and GUI operations within authentic computer environments.

- [GUI Action Narrator: Where and When Did That Action Take Place?](https://arxiv.org/abs/2406.13719)
    - Qinchen Wu, Difei Gao, Kevin Qinghong Lin, Zhuoyu Wu, Xiangwu Guo, Peiran Li, Weichen Zhang, Hengxu Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore, Chinese Academy of Sciences, Shenzhen
    - 📅 Date: June 19, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [framework], [Act2Cap], [GUI Narrator]
    - 📖 TLDR: The authors present **Act2Cap**, a GUI action dataset containing 4,189 video-caption pairs depicting various GUI actions such as clicks, drags, and typing across multiple software environments. They also propose **GUI Narrator**, a framework that leverages cursor detection as a visual prompt to enhance the interpretation of high-resolution screenshots for GUI video captioning. Evaluations reveal that even advanced multimodal models face challenges in this domain, highlighting the need for specialized approaches to improve performance.

- [AgentStudio: A Toolkit for Building General Virtual Agents](https://openreview.net/forum?id=axUf8BOjnH)
    - Longtao Zheng, Zhiyuan Huang, Zhenghai Xue, Xinrun Wang, Bo An, Shuicheng Yan
    - 🏛️ Institutions: Nanyang Technological University, Skywork AI, ETH Zurich
    - 📅 Date: March 26, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [general virtual agents], [open-ended learning], [tool creation], [GroundUI], [benchmark]
    - 📖 TLDR: AgentStudio is a robust toolkit for developing virtual agents with versatile actions, such as GUI automation and code execution. It unifies real-world human-computer interactions across OS platforms and includes diverse observation and action spaces, facilitating comprehensive training and benchmarking in complex settings. The toolkit's flexibility promotes agent generalization across varied tasks, supporting tool creation and a multimodal interaction interface to advance agent adaptability and learning.

- [Cradle: Empowering Foundation Agents Towards General Computer Control](https://proceedings.mlr.press/v267/tan25h.html)
    - Weihao Tan, Wentao Zhang, Xinrun Xu, Haochong Xia, Ziluo Ding, Boyu Li, Bohan Zhou, Junpeng Yue, Jiechuan Jiang, Yewen Li, Ruyi An, Molei Qin, Chuqiao Zong, Longtao Zheng, Yujie Wu, Xiaoqiang Chai, Yifei Bi, Tianbao Xie, Pengjie Gu, Xiyun Li, Ceyao Zhang, Long Tian, Chaojie Wang, Xinrun Wang, Börje F. Karlsson, Bo An, Shuicheng Yan, Zongqing Lu
    - 🏛️ Institutions: Skywork AI, Beijing Academy of Artificial Intelligence, Nanyang Technological University, Peking University, Institute of Software, Chinese Academy of Sciences, The University of Hong Kong, The Chinese University of Hong Kong
    - 📅 Date: March 5, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [general computer control], [skill curation], [self-improvement]
    - 📖 TLDR: This paper introduces the Cradle framework, designed to enable general computer control (GCC) through multimodal input (e.g., screen images and optional audio) and outputs (keyboard and mouse). Cradle’s six core modules, including self-reflection, skill curation, and memory, allow for generalized task handling in complex environments like AAA games. Demonstrated in *Red Dead Redemption II*, the framework exhibits adaptability by performing real missions and following the storyline with minimal prior knowledge, showcasing its potential as a generalist agent for diverse computer tasks.

- [Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II as a Case Study](https://arxiv.org/abs/2403.03186)
    - Weihao Tan, Ziluo Ding, Wentao Zhang, Boyu Li, Bohan Zhou, Junpeng Yue, Haochong Xia, Jiechuan Jiang, Longtao Zheng, Xinrun Xu, Yifei Bi, Pengjie Gu, Xinrun Wang, Börje F. Karlsson, Bo An, Zongqing Lu
    - 🏛️ Institutions: Nanyang Technological University, Beijing Academy of Artificial Intelligence, Peking University
    - 📅 Date: March 5, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [Cradle], [General Computer Control], [multimodal], [keyboard and mouse control], [long-term memory], [reasoning], [self-improvement]
    - 📖 TLDR: This paper introduces *Cradle*, a framework designed to achieve General Computer Control (GCC) by enabling agents to perform any computer task using only screen images (and possibly audio) as input and producing keyboard and mouse operations as output. The authors deploy Cradle in the complex AAA game Red Dead Redemption II, demonstrating its capability to follow the main storyline and complete real missions with minimal reliance on prior knowledge or resources.

- [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26/)
    - Chaoyun Zhang, Liqun Li, Shilin He, Xu Zhang, Bo Qiao, Si Qin, Minghua Ma, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
    - 🏛️ Institutions: Microsoft
    - 📅 Date: February 14, 2024
    - 📑 Publisher: NAACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [UI automation], [Windows], [UFO]
    - 📖 TLDR: This paper presents UFO, a pioneering multimodal LLM-based agent designed to fulfill user requests on Windows OS. UFO employs a dual-agent architecture—comprising AppAgent and ActAgent—that can interpret and execute complex tasks across multiple Windows applications by observing UI elements and utilizing control interactions. The framework allows UFO to handle intricate, cross-application workflows and execute commands seamlessly based on natural language prompts. It integrates GPT-Vision to recognize and interact with graphical elements, enabling flexible, autonomous task completion within and across diverse Windows applications.

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456)
    - Zhiyong Wu, Chengcheng Han, Zichen Ding, Zhenmin Weng, Zhoumianze Liu, Shunyu Yao, Tao Yu, Lingpeng Kong
    - 🏛️ Institutions: Shanghai AI Laboratory, East China Normal University, Princeton University, The University of Hong Kong
    - 📅 Date: February 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [self-directed learning], [GAIA], [FRIDAY], [OS-Copilot]
    - 📖 TLDR: The OS-Copilot framework supports building generalist agents capable of performing diverse tasks across an operating system (OS). This work introduces FRIDAY, an embodied agent using OS-Copilot to self-improve by learning from task outcomes. It operates with a memory-based architecture to tackle OS-level tasks across applications like terminals, web browsers, and third-party tools. Tested on the GAIA benchmark, FRIDAY achieved 35% higher performance than prior methods, proving effective in adapting to unfamiliar applications and refining its capabilities with minimal guidance.

- [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://eccv.ecva.net/virtual/2024/poster/1107)
    - Raghav Kapoor, Yash Parag Butala, Melisa Russak, Jing Yu Koh, Kiran Kamble, Waseem Alshikh, Ruslan Salakhutdinov
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: February 2024
    - 📑 Publisher: ECCV 2024 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [benchmark]
    - 📖 TLDR: OmniACT introduces a dataset and benchmark to train and evaluate multimodal agents capable of autonomously performing diverse tasks across desktop and web environments. Using annotated UI elements across applications, it combines visual grounding with natural language instructions, providing 9,802 data points for developing agents that integrate high-level reasoning with UI interactions. The study highlights the limited proficiency of current models, with baselines like GPT-4 only achieving 15% of human performance on executable scripts, emphasizing OmniACT's potential as a testbed for advancing multimodal AI.

- [AssistGUI: Task-Oriented Desktop Graphical User Interface Automation](https://arxiv.org/abs/2312.13108)
    - Difei Gao, Lei Ji, Zechen Bai, Mingyu Ouyang, Peiran Li, Dongxing Mao, Qinchen Wu, Weichen Zhang, Peiyi Wang, Xiangwu Guo, Hengxu Wang, Luowei Zhou, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore
    - 📅 Date: December 20, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [desktop productivity tasks]
    - 📖 TLDR: This study presents *AssistGUI*, a benchmark and framework for desktop GUI automation, featuring an LLM-based agent capable of completing complex user requests by analyzing instructional videos and performing actions on the desktop. Utilizing a novel Actor-Critic framework and GUI parser, *AssistGUI* was tested on 100 tasks across nine applications, such as MS Word and After Effects. Despite advances, the top-performing model achieved only a 46% success rate, illustrating the challenge of comprehensive desktop automation and underscoring areas for future research in agent-driven GUI tasks.

- [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://openreview.net/forum?id=Pc8AU1aF5e)
    - Longtao Zheng, Rundong Wang, Xinrun Wang, Bo An
    - 🏛️ Institutions: Nanyang Technological University, Skywork AI
    - 📅 Date: June 13, 2023
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [trajectory prompting], [state abstraction], [memory retrieval]
    - 📖 TLDR: Synapse introduces a novel framework for computer control tasks, leveraging trajectory-as-exemplar prompting and memory to enhance LLM performance in complex, multi-step computer tasks. The system combines state abstraction, trajectory-based prompts, and memory retrieval, overcoming LLM limitations by filtering task-irrelevant data, storing exemplar trajectories, and retrieving relevant instances for improved decision-making. Synapse achieves significant performance gains on benchmarks such as MiniWoB++ and Mind2Web, demonstrating enhanced task success rates and generalization across diverse web-based tasks.

- [Language Models can Solve Computer Tasks](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7cc1005ec73cfbaac9fa21192b622507-Abstract-Conference.html)
    - Geunwoo Kim, Pierre Baldi, Stephen McAleer
    - 🏛️ Institutions: University of California, Irvine, Carnegie Mellon University
    - 📅 Date: March 30, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [benchmark], [Recursive Critique and Improve], [RCI], [MiniWoB++], [general computer tasks]
    - 📖 TLDR: This study demonstrates that large language models (LLMs) can effectively automate computer tasks using a Recursive Critique and Improve (RCI) prompting method, enabling agents to handle complex desktop tasks like email and file management. By combining RCI with existing Chain of Thought (CoT) prompting, the method outperforms prior LLM approaches and traditional supervised and reinforcement learning models on the **MiniWoB++** benchmark, showing potential for broad computer task automation.

- [A Data-Driven Approach for Learning to Control Computers](https://proceedings.mlr.press/v162/humphreys22a.html)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - 🏛️ Institutions: DeepMind
    - 📅 Date: February 16, 2022
    - 📑 Publisher: ICML 2022
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [computer control], [reinforcement learning], [behavioral cloning], [MiniWoB++]
    - 📖 TLDR: This study presents a reinforcement learning-based approach to train agents for computer control tasks, using keyboard and mouse interactions guided by natural language. By leveraging human demonstration data, agents trained in this environment achieved strong cross-task generalization across the MiniWob++ benchmark. This framework demonstrates how agents can control computers as humans would, enabling enhanced performance in complex computer tasks with high transferability.
