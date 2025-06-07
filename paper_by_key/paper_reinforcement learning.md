# Papers with Keyword: reinforcement learning

- [AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning](https://github.com/OpenBMB/AgentCPM-GUI)
    - Zhong Zhang, Yaxi Lu, Yikun Fu, Yupeng Huo, Shenzhi Yang, Yesai Wu, Han Si, Xin Cong, Haotian Chen, Yankai Lin, Jie Xie, Wei Zhou, Wang Xu, Yuanheng Zhang, Zhou Su, Zhongwu Zhai, Xiaoming Liu, Yudong Mei, Jianming Xu, Hongyan Tian, Chongyi Wang, Chi Chen, Yuan Yao, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: THUNLP, RUC, ModelBest
    - 📅 Date: June 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [benchmark], [reinforcement learning], [grounding], [CAGUI], [mobile use]
    - 📖 TLDR: AgentCPM-GUI is an 8B-parameter on-device GUI agent tailored for Android applications, emphasizing robust multilingual interaction. Built upon MiniCPM-V, it undergoes a three-stage training pipeline: grounding-aware pre-training on a 12M-sample bilingual dataset, supervised fine-tuning with 55K high-quality trajectories from over 30 Chinese apps, and reinforcement fine-tuning using the Group Relative Policy Optimization (GRPO) algorithm to enhance reasoning capabilities. The model introduces a compact JSON-based action space optimized for mobile efficiency. Evaluated across five benchmarks, including the newly introduced Chinese GUI benchmark CAGUI, AgentCPM-GUI achieves state-of-the-art performance, notably 96.9% Type-Match and 91.3% Exact-Match on CAGUI. All code, model checkpoints, and evaluation data are publicly released to support further research.

- [A Summary on GUI Agents with Foundation Models Enhanced by Reinforcement Learning](https://arxiv.org/abs/2504.20464)
    - Jiahao Li, Kaer Huang
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: April 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [framework], [reinforcement learning], [multimodal], [training taxonomy]
    - 📖 TLDR: This paper presents a structured summary of recent advances in GUI agents powered by Multi-modal Large Language Models (MLLMs) and enhanced through Reinforcement Learning (RL). It formalizes GUI agent tasks as Markov Decision Processes and reviews modular architectures comprising Perception, Planning, and Acting modules. The study categorizes training methodologies into Prompt-based, Supervised Fine-Tuning (SFT), and RL-based approaches, highlighting the progression towards dynamic policy learning. The paper concludes by identifying key challenges and future directions for developing more capable and reliable GUI agents.

- [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)
    - Yuhang Liu, Pengxiang Li, Congkai Xie, Xavier Hu, Xiaotian Han, Shengyu Zhang, Hongxia Yang, Fei Wu
    - 🏛️ Institutions: Zhejiang Univ., Dalian Univ. of Tech., Reallm Labs, HK PolyU
    - 📅 Date: April 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [model], [reinforcement learning], [planning], [reasoning], [Actor2Reasoner], [InfiGUI-R1]
    - 📖 TLDR: This paper introduces **InfiGUI-R1**, a multimodal GUI agent developed through the **Actor2Reasoner** framework, aiming to transition agents from reactive behaviors to deliberative reasoning. The framework comprises two stages: *Reasoning Injection*, which employs Spatial Reasoning Distillation to integrate GUI visual-spatial information with logical reasoning, and *Deliberation Enhancement*, which uses Reinforcement Learning with Sub-goal Guidance and Error Recovery Scenario Construction to refine the agent's planning and error correction capabilities. Evaluations on benchmarks like AndroidControl and ScreenSpot demonstrate that InfiGUI-R1-3B achieves state-of-the-art performance in GUI grounding and trajectory tasks, outperforming larger models in several categories.

- [GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents](https://arxiv.org/abs/2504.10458)
    - Xiaobo Xia, Run Luo
    - 🏛️ Institutions: Unknown
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [unified action space], [GRPO], [GUI-R1]
    - 📖 TLDR: GUI-R1 introduces a reinforcement learning framework that enhances the capabilities of Large Vision-Language Models (LVLMs) for GUI agents. By employing a unified action space and a rule-based reward function, the model efficiently learns to perform high-level tasks across multiple platforms, including Windows, Linux, MacOS, Android, and Web. Utilizing only 0.02% of the data compared to previous methods, GUI-R1 demonstrates superior performance on eight benchmarks, showcasing the potential of reinforcement learning in GUI agent tasks.

- [UI-R1: Enhancing Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab @ CUHK
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [UI-R1-3B], [GRPO], [AndroidControl], [ScreenSpot-Pro]
    - 📖 TLDR: This paper introduces **UI-R1**, a framework that enhances the reasoning capabilities of multimodal large language models (MLLMs) for GUI action prediction tasks through rule-based reinforcement learning. Utilizing a small, high-quality dataset of 136 challenging mobile tasks, the authors design a unified rule-based action reward function and optimize the model using Group Relative Policy Optimization (GRPO). The resulting model, **UI-R1-3B**, demonstrates significant improvements over the base model (Qwen2.5-VL-3B) on both in-domain (AndroidControl) and out-of-domain (ScreenSpot-Pro) benchmarks, showcasing the effectiveness of rule-based RL in advancing GUI understanding and control.

- [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents](https://arxiv.org/abs/2502.11357)
    - Vardaan Pahuja, Yadong Lu, Corby Rosset, Boyu Gou, Arindam Mitra, Spencer Whitehead, Yu Su, Ahmed Awadallah
    - 🏛️ Institutions: Microsoft Research, The Ohio State University
    - 📅 Date: February 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [web agents], [reinforcement learning], [Explorer]
    - 📖 TLDR: This paper introduces *Explorer*, a multimodal web agent trained on a newly synthesized dataset comprising over 94,000 successful web trajectories. The dataset, generated through scalable exploration and refinement techniques, spans 49,000 unique URLs and includes 720,000 screenshots and 33 million web elements. *Explorer* demonstrates strong performance on benchmarks like Mind2Web-Live, Multimodal-Mind2Web, and MiniWob++, highlighting the importance of data scaling in enhancing web agent capabilities.

- [VSC-RL: Advancing Autonomous Vision-Language Agents with Variational Subgoal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2502.07949)
    - Qingyuan Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah's Ark Lab, Univ. College London
    - 📅 Date: February 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [subgoal generation], [VSC-RL], [learning efficiency]
    - 📖 TLDR: This paper introduces **VSC-RL**, a novel reinforcement learning framework that enhances learning efficiency for vision-language agents in complex sequential decision-making tasks. By reformulating these tasks as variational goal-conditioned problems, VSC-RL leverages advanced optimization techniques and utilizes vision-language models to autonomously decompose goals into feasible subgoals. Empirical results demonstrate that VSC-RL significantly outperforms state-of-the-art agents, particularly in challenging mobile device control tasks.

- [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://arxiv.org/abs/2412.13194)
    - Yifei Zhou, Qianlan Yang, Kaixiang Lin, Min Bai, Xiong Zhou, Yu-Xiong Wang, Sergey Levine, Erran Li
    - 🏛️ Institutions: UCB, UIUC, Amazon
    - 📅 Date: December 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [skill discovery], [PAE]
    - 📖 TLDR: This paper introduces the Proposer-Agent-Evaluator (PAE) system, enabling foundation model agents to autonomously discover and practice skills in real-world web environments. PAE comprises a context-aware task proposer, an agent policy for task execution, and a vision-language model-based success evaluator. Validated on vision-based web navigation tasks, PAE significantly enhances zero-shot generalization capabilities of vision-language model Internet agents, achieving over 30% relative improvement on unseen tasks and websites, and surpassing state-of-the-art open-source agents by more than 10%.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: December 2, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [reinforcement learning], [Ponder & Press]
    - 📖 TLDR: This paper introduces *Ponder & Press*, a divide-and-conquer framework for general computer control using only visual input. The approach combines a general-purpose multimodal large language model (MLLM) as an 'interpreter' to translate high-level user instructions into detailed action descriptions, with a GUI-specific MLLM as a 'locator' that precisely identifies GUI elements for action execution. By relying solely on visual inputs, the agent offers a versatile, human-like interaction paradigm applicable across various platforms, achieving state-of-the-art performance in GUI grounding and control tasks.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337v1)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Xinyue Yang, Jiadai Sun, Yu Yang, Shuntian Yao, Tianjie Zhang, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, BAAI
    - 📅 Date: November 4, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [self-evolving curriculum], [WebRL], [outcome-supervised reward model]
    - 📖 TLDR: This paper introduces *WebRL*, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open large language models (LLMs). WebRL addresses challenges such as the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. It incorporates a self-evolving curriculum that generates new tasks from unsuccessful attempts, a robust outcome-supervised reward model (ORM), and adaptive reinforcement learning strategies to ensure consistent improvements. Applied to Llama-3.1 and GLM-4 models, WebRL significantly enhances their performance on web-based tasks, surpassing existing state-of-the-art web agents.

- [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://ai-agents-2030.github.io/DistRL/)
    - Taiyi Wang, Zhihao Wu, Jianheng Liu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Univ. of Cambridge, Huawei Noah's Ark Lab, Univ. College London
    - 📅 Date: October 18, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [distributed training], [A-RIDE], [on-device control]
    - 📖 TLDR: This paper introduces **DistRL**, a novel framework designed to enhance the efficiency of online reinforcement learning fine-tuning for mobile device control agents. DistRL employs centralized training and decentralized data acquisition to ensure efficient fine-tuning in dynamic online interactions. The framework is supported by a custom RL algorithm, A-RIDE, which balances exploration with prioritized data utilization to ensure stable and robust training. Experiments demonstrate that DistRL improves training efficiency by 3× and accelerates data collection by 2.4× compared to leading synchronous multi-machine methods. Notably, after training, DistRL achieves a 20% relative improvement in success rate on general Android tasks from an open benchmark, outperforming existing approaches while maintaining the same training time.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2404.03648)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: THU, OSU
    - 📅 Date: October 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [dataset], [benchmark], [reinforcement learning]
    - 📖 TLDR: AutoWebGLM introduces a web navigation agent based on ChatGLM3-6B, designed to autonomously navigate and interact with webpages for complex tasks. The paper highlights a two-phase data construction approach using a hybrid human-AI methodology for diverse, curriculum-based web task training. It also presents AutoWebBench, a benchmark for evaluating agent performance in web tasks, and uses reinforcement learning to fine-tune operations, addressing complex webpage interaction and grounding.

- [WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration](https://arxiv.org/abs/2408.15978)
    - Yao Zhang, Zijian Ma, Yunpu Ma, Zhen Han, Yu Wu, Volker Tresp
    - 🏛️ Institutions: LMU Munich, Technical University of Munich, Munich Center for Machine Learning (MCML)
    - 📅 Date: August 28, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [Monte Carlo Tree Search], [reinforcement learning], [WebPilot]
    - 📖 TLDR: This paper introduces **WebPilot**, a multi-agent system designed to execute complex web tasks requiring dynamic interaction. By employing a dual optimization strategy grounded in Monte Carlo Tree Search (MCTS), WebPilot enhances adaptability in complex web environments. The system's Global Optimization phase generates high-level plans by decomposing tasks into manageable subtasks, while the Local Optimization phase executes each subtask using a tailored MCTS approach. Experimental results on WebArena and MiniWoB++ demonstrate WebPilot's effectiveness, achieving state-of-the-art performance with GPT-4 and marking a significant advancement in autonomous web agent capabilities. :contentReference[oaicite:0]{index=0}

- [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199)
    - Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
    - 🏛️ Institutions: MultiOn, Stanford
    - 📅 Date: August 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [MCTS], [Tree Search], [DPO], [Reinforcement Learning]
    - 📖 TLDR: TBD

- [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://digirl-agent.github.io/)
    - Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, Aviral Kumar
    - 🏛️ Institutions: UC Berkeley, UIUC, Google DeepMind
    - 📅 Date: June 14, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reinforcement learning], [DigiRL]
    - 📖 TLDR: The authors present *DigiRL*, an autonomous reinforcement learning approach for training device-control agents. By fine-tuning a pre-trained vision-language model in two stages—offline and offline-to-online RL—DigiRL achieves a significant improvement in success rates on the Android-in-the-Wild dataset, establishing a new state-of-the-art for digital agents in device control.

- [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)
    - Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Toyama, Robert Berry, Divya Tyamagundlu, Timothy Lillicrap, Oriana Riva
    - 🏛️ Institutions: Google DeepMind, Google
    - 📅 Date: May 23, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [Android-based agents], [task diversity], [reinforcement learning], [dynamic environment]
    - 📖 TLDR: AndroidWorld introduces a dynamic Android environment for benchmarking autonomous agents across 116 tasks spanning 20 Android apps. These tasks vary through parameterized and natural language prompts, fostering a realistic testing ground for agents designed to operate in complex mobile environments. The benchmark supports millions of task variations, allowing agents to respond to the Android system's changing states and improving real-world applicability.

- [Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2405.00516)
    - Lucas-Andreï Thil, Mirela Popa, Gerasimos Spanakis
    - 🏛️ Institutions: Maastricht University the Netherlands
    - 📅 Date: May 1, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [large language models], [reinforcement learning]
    - 📖 TLDR: This paper proposes a novel approach combining supervised learning (SL) and reinforcement learning (RL) techniques to train web navigation agents using large language models. The authors address limitations in previous models' understanding of HTML content and introduce methods to enhance true comprehension. Their approach, evaluated on the MiniWoB benchmark, outperforms previous SL methods on certain tasks using less data and narrows the performance gap with RL models. The study achieves 43.58% average accuracy in SL and 36.69% when combined with a multimodal RL approach, setting a new direction for future web navigation research.

- [Search Beyond Queries: Training Smaller Language Models for Web Interactions via Reinforcement Learning](https://arxiv.org/abs/2404.10887)
    - Moghis Fereidouni, A.B. Siddique
    - 🏛️ Institutions: University of Kentucky
    - 📅 Date: April 16, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [grounded language agent], [Flan-T5], [unsupervised domain adaptation]
    - 📖 TLDR: This paper introduces GLAINTEL, a grounded language agent framework designed to enhance web interaction using instruction-finetuned language models, particularly Flan-T5, with reinforcement learning (PPO) to tackle interactive web navigation challenges. The study explores unsupervised and supervised training methods, evaluating the effects of human demonstration on agent performance. Results indicate that combining human feedback with reinforcement learning yields effective outcomes, rivaling larger models like GPT-4 on web navigation tasks.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: MSRA
    - 📅 Date: October 7, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [reinforcement learning], [UI task automation], [instruction grounding]
    - 📖 TLDR: This paper introduces a multimodal model, termed RUIG (Reinforced UI Instruction Grounding), for automating UI tasks through natural language instructions. By leveraging a pixel-to-sequence approach, the model directly decodes UI element locations from screenshots based on user commands, removing the need for metadata like element coordinates. The framework uses a transformer-based encoder-decoder setup optimized through reinforcement learning to improve spatial accuracy. This novel approach outperforms prior methods, offering a generalized solution for UI task automation.

- [Augmenting Autotelic Agents with Large Language Models](https://arxiv.org/abs/2305.12487)
    - Cédric Colas, Laetitia Teodorescu, Pierre-Yves Oudeyer, Xingdi Yuan, Marc-Alexandre Côté
    - 🏛️ Institutions: MIT, Inria, Microsoft
    - 📅 Date: May 22, 2023
    - 📑 Publisher: CoLLAs 2023
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [goal generation], [large language models], [autotelic learning]
    - 📖 TLDR: This study introduces the *Language Model-Augmented Autotelic Agent (LMA3)*, a framework leveraging large language models to help agents autonomously generate, represent, and learn diverse goals in a task-agnostic, text-based environment. LMA3 integrates pretrained language models to emulate human cultural knowledge, aiming to dynamically relabel goals, generate new goals, and create goal-driven reward functions without manual inputs. This approach supports skill development by autonomously expanding goal repertoires in ways that resemble human open-ended learning, showcasing potential for achieving complex, self-directed learning in AI.

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
    - Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
    - 🏛️ Institutions: Northeastern University, MIT, Princeton
    - 📅 Date: March 20, 2023
    - 📑 Publisher: NeurIPS 2023
    - 💻 Env: [Misc]
    - 🔑 Key: [framework], [learning], [verbal reinforcement learning], [Reflexion]
    - 📖 TLDR: This paper introduces *Reflexion*, a framework that enhances language agents by enabling them to reflect on task feedback linguistically, storing these reflections in an episodic memory to improve decision-making in future trials. Reflexion allows agents to learn from various feedback types without traditional weight updates, achieving significant performance improvements across tasks like decision-making, coding, and reasoning. For instance, Reflexion attains a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4's 80%.

- [A Data-Driven Approach for Learning to Control Computers](https://arxiv.org/abs/2202.08137)
    - Peter C. Humphreys, David Raposo, Tobias Pohlen, Gregory Thornton, Rachita Chhaparia, Alistair Muldal, Josh Abramson, Petko Georgiev, Alex Goldin, Adam Santoro, Timothy Lillicrap
    - 🏛️ Institutions: DeepMind
    - 📅 Date: February 16, 2022
    - 📑 Publisher: ICML 2022
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [framework], [computer control], [reinforcement learning], [multimodal transformer]
    - 📖 TLDR: This study presents a reinforcement learning-based approach to train agents for computer control tasks, using keyboard and mouse interactions guided by natural language. By leveraging human demonstration data, agents trained in this environment achieved strong cross-task generalization across the MiniWob++ benchmark. This framework demonstrates how agents can control computers as humans would, enabling enhanced performance in complex computer tasks with high transferability.

- [AndroidEnv: A Reinforcement Learning Platform for Android](https://arxiv.org/abs/2105.13231)
    - Daniel Toyama, Philippe Hamel, Anita Gergely, Gheorghe Comanici, Amelia Glaese, Zafarali Ahmed, Tyler Jackson, Shibl Mourad, Doina Precup
    - 🏛️ Institutions: DeepMind
    - 📅 Date: May 27, 2021
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [reinforcement learning], [Android interface], [RL environment], [task flexibility], [touchscreen action space]
    - 📖 TLDR: AndroidEnv provides a reinforcement learning (RL) platform for Android that lets RL agents interact with a realistic Android simulation via touchscreen events. The platform supports diverse applications, enabling agents to interact with over 100 predefined tasks across a variety of apps. With hybrid continuous and discrete action spaces, AndroidEnv is well-suited for training agents in complex, real-world Android scenarios where actions must be contextually sequenced, such as in UI navigation, gaming, and productivity apps. This environment encourages further RL research by offering task flexibility and realistic Android emulation.

- [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802)
    - Evan Zheran Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, Percy Liang
    - 🏛️ Institutions: Stanford
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
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [open-domain]
    - 📖 TLDR: This paper introduces *World of Bits (WoB)*, a platform enabling agents to perform complex web-based tasks using low-level keyboard and mouse actions, addressing the lack of open-domain realism in existing reinforcement learning environments. WoB leverages a novel framework where crowdworkers create tasks with structured rewards and reproducibility by caching web interactions, forming a stable training environment. The authors validate WoB by training agents via behavioral cloning and reinforcement learning to accomplish various real-world tasks, showcasing its potential as an effective platform for reinforcement learning on web tasks.
