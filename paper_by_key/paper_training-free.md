# Papers with Keyword: training-free

- [GPA: Learning GUI Process Automation from Demonstrations](https://arxiv.org/abs/2604.01676)
    - Zirui Zhao, Jun Hao Liew, Yan Yang, Wenzhuo Yang, Ziyang Luo, Doyen Sahoo, Silvio Savarese, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: April 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [training-free], [process automation], [long-horizon tasks], [GPA], [robotic process automation]
    - 📖 TLDR: GPA is a vision-based GUI process automation system that enables fast and stable process replay from a single demonstration. Using Sequential Monte Carlo-based localization and readiness calibration, it achieves higher success rates with 10x faster execution than Gemini 3 Pro on long-horizon GUI tasks, running entirely locally without cloud LLMs.

- [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/abs/2603.26266)
    - Rui Xie, Zhi Gao, Chenrui Shi, Zirui Shang, Lu Chen, Qing Li
    - 🏛️ Institutions: SJTU, State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing Institute of Technology
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [video retrieval], [automatic annotation], [domain bias], [training-free], [OSWorld], [GUIDE]
    - 📖 TLDR: GUIDE is a training-free add-on for desktop GUI agents that retrieves relevant tutorial videos, turns them into planning and grounding annotations, and injects that expertise into existing agents without changing model parameters. On OSWorld, it improves multiple agent families while also reducing execution steps.

- [Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements](https://arxiv.org/abs/2603.14448)
    - Ziwei Liu, Tao Feng, Borui Kang, Yanbing Yang, Jun Luo
    - 🏛️ Institutions: Sichuan University, Tsinghua, NJU, NTU
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [inference scaling], [ZoomUI], [instruction rewriting], [progressive zooming]
    - 📖 TLDR: ZoomUI is a training-free GUI grounding method built on the idea that complex interfaces can be decomposed into simpler visual elements that generic MLLMs already understand. It rewrites instructions into element-level visual descriptions and progressively zooms onto candidate UI regions, reaching or surpassing fine-tuned baselines without additional training.

- [M^2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval](https://arxiv.org/abs/2603.00503)
    - Dawei Yan, Haokui Zhang, Guangda Huzhang, Yang Li, Yibo Wang, Qing-Guo Chen, Zhao Xu, Weihua Luo, Ying Li, Wei Dong, Chunhua Shen
    - 🏛️ Institutions: Northwestern Polytechnical University, Alibaba Group, Xi'an University of Architecture and Technology, ZJU
    - 📅 Date: February 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [memory augmentation], [trajectory summarization], [insight retrieval], [training-free], [long-horizon tasks], [M^2]
    - 📖 TLDR: M^2 is a training-free memory augmentation method for long-horizon web agents that combines dynamic trajectory summarization with offline insight retrieval. It improves success rates on WebVoyager and OnlineMind2Web while substantially reducing token usage.

- [Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion](https://arxiv.org/abs/2602.06351)
    - Longhui Ma, Di Zhao, Siwei Wang, Zhao Lv, Miao Wang
    - 🏛️ Institutions: National University of Defense Technology, Academy of Military Sciences
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [multimodal fusion], [attention mechanism], [training-free], [OCR], [Trifuse]
    - 📖 TLDR: Trifuse is a training-free GUI grounding method that fuses MLLM attention, OCR text, and icon caption signals through a consensus-based fusion strategy. It improves grounding across multiple benchmarks without task-specific fine-tuning.

- [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528)
    - Hongze Mi, Yibo Feng, WenJie Lu, Song Cao, Jinyuan Li, Yanming Li, Xuelin Zhang, Haotian Luo, Songyang Peng, He Cui, Tengfei Tian, Jun Fang, Hua Chai, Naiqiang Tan
    - 🏛️ Institutions: Didichuxing Co. Ltd, CUHK-Shenzhen, Tianjin University, Sun Yat-sen University, Fudan
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [memory system], [training-free], [self-regulating memory], [multi-app], [Darwinian Memory], [trajectory pruning]
    - 📖 TLDR: Darwinian Memory is a training-free memory system that treats agent memories as an evolving ecosystem, selecting and pruning trajectories through utility-driven competition. It improves success rate and execution stability on real-world multi-app GUI benchmarks.

- [MVP: Multiple View Prediction Improves GUI Grounding](https://arxiv.org/abs/2512.08529)
    - Yunzhu Zhang, Zeyu Pan, Zhengwen Zeng, Shuheng Shen, Changhua Meng, Linchao Zhu
    - 🏛️ Institutions: ZJU, Hangzhou Dianzi University, Ant Group
    - 📅 Date: December 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [multi-view inference], [prediction instability], [coordinate clustering], [MVP]
    - 📖 TLDR: MVP studies prediction instability in GUI grounding, where tiny visual perturbations can flip coordinate predictions between correct and incorrect. It improves training-free grounding by proposing attention-guided cropped views and clustering the resulting coordinate predictions, yielding consistent gains on ScreenSpot-Pro, UI-Vision, and OS-World-G.

- [Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding](https://arxiv.org/abs/2512.05941)
    - Zhiyuan Jiang, Shenghao Xie, Wenyi Li, Wenqiang Zu, Peihang Li, Jiahao Qiu, Siqi Pei, Lei Ma, Tiejun Huang, Mengdi Wang, Shilong Liu
    - 🏛️ Institutions: Xi’an Jiaotong University, Princeton, PKU, University of Chinese Academy of Sciences, HKU, Michigan State University
    - 📅 Date: December 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [zoom], [test-time scaling], [ZoomClick], [GUIZoom-Bench]
    - 📖 TLDR: This paper studies zooming as a test-time prior for GUI grounding and proposes ZoomClick, which decides when to zoom, how far to zoom, and when to return to the original view during localization. It also introduces GUIZoom-Bench and reports stronger grounding results across several mainstream benchmarks.

- [WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation](https://arxiv.org/abs/2510.22732)
    - Jiali Cheng, Anjishnu Kumar, Roshan Lal, Rishi Rajasekaran, Hani Ramezani, Omar Zia Khan, Oleg Rokhlenko, Sunny Chiu-Webster, Gang Hua, Hadi Amiri
    - 🏛️ Institutions: University of Massachusetts Lowell, Amazon Alexa AI
    - 📅 Date: October 26, 2025
    - 📑 Publisher: NeurIPS 2025 Workshop on Language Agents and World Models
    - 💻 Env: [Web]
    - 🔑 Key: [training-free], [framework], [memory], [planning], [action simulation], [WebArena-Lite], [WebATLAS]
    - 📖 TLDR: WebATLAS is a training-free web agent that reuses past interaction outcomes as persistent experience memory and simulates candidate actions before executing them. Its planner-simulator-critic loop is designed to improve long-horizon behavior on unseen websites, and it reports 63% success on WebArena-Lite without site-specific fine-tuning.

- [GUI-KV: Efficient GUI Agents via KV Cache with Spatio-Temporal Awareness](https://arxiv.org/abs/2510.00536)
    - Kung-Hsiang Huang, Haoyi Qiu, Yutong Dai, Caiming Xiong, Chien-Sheng Wu
    - 🏛️ Institutions: Salesforce AI Research, UCLA
    - 📅 Date: October 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [training-free], [KV cache compression], [spatio-temporal redundancy], [spatial saliency], [AgentNetBench], [GUI-KV]
    - 📖 TLDR: GUI-KV is a training-free KV-cache compression method for GUI agents that exploits two GUI-specific signals: spatial saliency within a frame and temporal redundancy across frames. It closely matches or beats full-cache performance on standard benchmarks, and in a 5-screenshot AgentNetBench setting cuts decoding FLOPs by 38.9% while improving step accuracy.

- [GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://aclanthology.org/2025.acl-long.282/)
    - Bin Xie, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Jie Liu, Min Zhang, Liqiang Nie
    - 🏛️ Institutions: HIT-Shenzhen, Huawei Noah’s Ark Lab
    - 📅 Date: May 22, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [training-free], [framework], [benchmark], [autonomous exploration], [transition-aware knowledge], [GUI-KRB], [GUI-explorer]
    - 📖 TLDR: GUI-explorer is a training-free mobile GUI agent that automatically explores app functionality and mines transition-aware knowledge from observed state changes. It also introduces the GUI-KRB benchmark for mobile GUI reasoning, and shows strong gains on SPA-Bench and AndroidWorld without parameter updates for new apps.

- [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)
    - Anthony Nguyen
    - 🏛️ Institutions: Algoma University
    - 📅 Date: November 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [training-free], [GUI grounding], [visual prompting], [iterative narrowing]
    - 📖 TLDR: Iterative Narrowing is a visual-prompting framework for GUI grounding that repeatedly zooms into smaller image regions to refine predictions. The paper shows that this simple test-time strategy improves both general and fine-tuned VLMs on one-shot grounding across multiple UI platforms.

- [Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/abs/2410.22552)
    - Jaekyeom Kim, Dong-Ki Kim, Lajanugen Logeswaran, Sungryull Sohn, Honglak Lee
    - 🏛️ Institutions: LG AI Research, Field AI, University of Michigan
    - 📅 Date: October 29, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [Web]
    - 🔑 Key: [training-free], [auto-intent], [intent discovery], [self-exploration]
    - 📖 TLDR: Proposes Auto-Intent, a web-agent adaptation method that discovers latent intents from demonstrations and uses predicted intents as hints during self-exploration. Without direct fine-tuning of the base agent, it improves GPT and Llama agents on Mind2Web and WebArena.
