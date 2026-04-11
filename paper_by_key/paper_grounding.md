# Papers with Keyword: grounding

- [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](https://arxiv.org/abs/2603.14248)
    - Mohamed Aghzal, Gregory J. Stein, Ziyu Yao
    - 🏛️ Institutions: Department of Computer Science, George Mason University
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [failure analysis], [hierarchical planning], [PDDL], [replanning], [grounding]
    - 📖 TLDR: This paper analyzes web-agent failures through a three-layer hierarchy of high-level planning, low-level execution, and replanning rather than relying only on end-to-end success. It finds that structured PDDL plans improve strategic planning over natural-language plans, but that execution and grounding remain the dominant reliability bottlenecks.

- [Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization](https://arxiv.org/abs/2602.13653)
    - Yibo Wang, Guangda Huzhang, Yuwei Hu, Yu Xia, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Lijun Zhang
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, Nanjing University, Ovis Team, Alibaba Group
    - 📅 Date: February 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [agentic-Q estimation], [step-wise policy optimization], [Ovis2.5-9B], [GUI navigation], [grounding]
    - 📖 TLDR: This paper trains GUI agents with an agentic-Q model that estimates each action's contribution to task completion and a step-wise policy optimization routine decoupled from online interaction. The design keeps data collection manageable while stabilizing updates and improving navigation and grounding performance.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: University of Michigan, LG AI Research
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [RegionFocus], [test-time scaling], [grounding], [zoom-in reasoning]
    - 📖 TLDR: Presents RegionFocus, a test-time scaling method that repeatedly zooms into promising GUI regions instead of relying on a single full-screen pass. The paper treats grounding as an iterative visual search problem and shows strong gains on ScreenSpot-Pro and WebVoyager without retraining the base model.

- [ScaleTrack: Scaling and back-tracking Automated GUI Agents](https://arxiv.org/abs/2505.00416)
    - Jing Huang, Zhixiong Zeng, Wenkang Han, Yufeng Zhong, Liming Zheng, Shuai Fu, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, University of Adelaide
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [framework], [training strategy], [back-tracking], [grounding], [ScaleTrack]
    - 📖 TLDR: Presents ScaleTrack, a training framework that tackles GUI-agent weaknesses at both the data and planning levels. It scales grounding data through unified sample aggregation and explicitly trains back-tracking behavior so agents can recover from wrong turns instead of only moving forward.

- [DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents](https://arxiv.org/abs/2503.11170)
    - Yibin Xu, Liang Yang, Hao Chen, Hua Wang, Zhi Chen, Yaohua Tang
    - 🏛️ Institutions: Moore Threads AI
    - 📅 Date: March 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [GUI understanding], [grounding], [data pipeline], [benchmark]
    - 📖 TLDR: DeskVision introduces an automated data pipeline (AutoCaptioner) and a large-scale desktop GUI dataset with 54,855 images and 303,622 annotations across Windows, macOS, and Linux, along with the DeskVision-Eval benchmark, and trains a GUI understanding model (GUIExplorer) that achieves state-of-the-art performance on visual element understanding and grounding tasks.

- [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
    - Junpeng Liu, Yifan Song, Bill Yuchen Lin, Wai Lam, Graham Neubig, Yuanzhi Li, Xiang Yue
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: April 09, 2024
    - 📑 Publisher: COLM 2024
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [web page understanding], [grounding]
    - 📖 TLDR: VisualWebBench introduces a comprehensive benchmark for evaluating multimodal large language models (MLLMs) on web-based tasks. It includes 1.5K human-curated instances across 139 websites in 87 sub-domains. The benchmark spans seven tasks—such as OCR, grounding, and web-based QA—aiming to test MLLMs' capabilities in fine-grained web page understanding. Results reveal significant performance gaps, particularly in grounding tasks, highlighting the need for advancement in MLLM web understanding.

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://eccv.ecva.net/virtual/2024/poster/749)
    - Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeff Nichols, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: April 08, 2024
    - 📑 Publisher: ECCV 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [benchmark], [grounding], [reasoning], [mobile UI understanding], [ferret-UI]
    - 📖 TLDR: This paper presents **Ferret-UI**, a multimodal large language model (MLLM) designed to understand and interact with mobile user interfaces. The model incorporates advanced capabilities for referring, grounding, and reasoning about UI elements. By training on a variety of UI tasks, Ferret-UI achieves high performance in tasks such as icon recognition and text extraction. The authors introduce a unique architecture that allows for improved visual feature extraction from mobile screens, paving the way for applications in accessibility and user interaction.

- [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
    - Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: January 01, 2024
    - 📑 Publisher: ICML 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [grounding], [SeeAct], [Mind2Web], [online evaluation]
    - 📖 TLDR: Shows that GPT-4V can act as a strong generalist web agent when the grounding problem is handled carefully. The paper introduces the SeeAct framework and demonstrates that better grounding of webpage elements is the main bottleneck between frontier multimodal models and reliable web control.

- [Grounding Open-Domain Instructions to Automate Web Support Tasks](https://aclanthology.org/2021.naacl-main.80/)
    - Nancy Xu, Sam Masling, Michael Du, Giovanni Campagna, Larry Heck, James Landay, Monica Lam
    - 🏛️ Institutions: Stanford University, Samsung Research
    - 📅 Date: March 30, 2021
    - 📑 Publisher: NAACL 2021
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [framework], [grounding], [task automation], [open-domain instructions], [RUSS]
    - 📖 TLDR: Introduces RUSS, a framework for grounding open-domain web support instructions into executable actions. The system uses semantic parsing into ThingTalk to map natural-language troubleshooting instructions onto web interactions.
