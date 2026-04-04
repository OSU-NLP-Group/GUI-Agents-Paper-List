# Papers with Keyword: grounding

- [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](https://arxiv.org/abs/2603.14248)
    - Mohamed Aghzal, Gregory J. Stein, Ziyu Yao
    - 🏛️ Institutions: George Mason University
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [failure analysis], [hierarchical planning], [PDDL], [grounding]
    - 📖 TLDR: This paper analyzes web-agent failures through a three-layer hierarchy of high-level planning, low-level execution, and replanning rather than relying only on end-to-end success. It finds that structured PDDL plans improve strategic planning over natural-language plans, but that execution and grounding remain the dominant reliability bottlenecks.

- [WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces](https://arxiv.org/abs/2603.05295)
    - Sicheng Fan, Rui Wan, Yifei Leng, Gaoning Liang, Li Ling
    - 🏛️ Institutions: Fudan University, IMean AI
    - 📅 Date: March 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [grounding], [training data], [multimodal]
    - 📖 TLDR: WebChain is the largest open-source dataset of 31,725 human-annotated web interaction trajectories (318k steps) on real-world websites, featuring triple-aligned visual, structural, and action data. Leveraging this dataset, the authors propose a Dual Mid-Training recipe that decouples spatial grounding from planning, achieving state-of-the-art performance on their WebChainBench and other public GUI benchmarks.

- [GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection](https://arxiv.org/abs/2512.09396)
    - Zishu Wei, Qixiang Ma, Xavier Hu, Yuhang Liu, Hui Zang, Yudong Zhao, Tao Wang, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: Zhejiang University, Huawei Technologies Ltd.
    - 📅 Date: December 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multi-agent], [grounding], [reasoning], [reflection], [benchmark]
    - 📖 TLDR: GAIR is a multi-agent GUI automation framework that uses a general-purpose MLLM to jointly reason over information gathered by multiple GUI-specific models, with a group reflection mechanism that drives specialized models to collect more targeted information when the decision-maker determines insufficient evidence, achieving state-of-the-art results on GUI benchmarks like ScreenSpot and UI-I2E-Bench with only 7B models.

- [Prune4Web: DOM Tree Pruning Programming for Web Agent](https://arxiv.org/abs/2511.21398)
    - Jiayuan Zhang, Kaiquan Chen, Zhihao Lu, Enshen Zhou, Qian Yu, Jing Zhang
    - 🏛️ Institutions: School of Software & QRI, Beihang University
    - 📅 Date: November 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [DOM pruning], [grounding], [LLM], [code generation], [observation simplification]
    - 📖 TLDR: Prune4Web introduces DOM Tree Pruning Programming, where an LLM generates executable Python scoring scripts to programmatically filter DOM elements based on sub-task semantics, achieving 25-50x reduction in candidate elements and improving web grounding accuracy from 46.8% to 88.28%.

- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
    - Zhangxuan Gu, Zhengwen Zeng, Zhenyu Xu, Xingran Zhou, Shuheng Shen, Yunfei Liu, Beitong Zhou, Changhua Meng, Tianyu Xia, Weizhi Chen, Yue Wen, Jingya Dou, Fei Tang, Jinzhen Lin, Yulin Liu, Zhenlin Guo, Yichen Gong, Heng Jia, Changlong Gao, Yuan Guo, Yong Deng, Zhenyu Guo, Liang Chen, Weiqiang Wang
    - 🏛️ Institutions: Ant Group
    - 📅 Date: August 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [grounding], [navigation], [data cleaning], [Qwen2.5-VL], [UI-venus]
    - 📖 TLDR: This technical report introduces **UI-Venus**, a screenshot-based UI agent built on the multimodal Qwen2.5-VL model and fine-tuned via **reinforcement fine-tuning (RFT)**. It achieves state-of-the-art performance on UI grounding and navigation benchmarks—e.g., Screenspot-V2/Pro (up to 95.3% / 61.9%) and AndroidWorld navigation (up to 65.9%)—by leveraging carefully crafted reward functions, efficient data cleaning pipelines, and a novel **self-evolving framework** (trajectory alignment and sparse action enhancement) to enhance reasoning coherence and handle rare actions. The code and checkpoints are open-sourced to encourage further development.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: University of Michigan, LG AI Research
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [RegionFocus], [test-time scaling], [grounding], [zoom-in reasoning]
    - 📖 TLDR: Presents RegionFocus, a test-time scaling method that repeatedly zooms into promising GUI regions instead of relying on a single full-screen pass. The paper treats grounding as an iterative visual search problem and shows strong gains on ScreenSpot-Pro and WebVoyager without retraining the base model.

- [ScaleTrack: Scaling and back-tracking Automated GUI Agents](https://arxiv.org/abs/2505.00416)
    - Jing Huang, Zhixiong Zeng, Wenkang Han, Yufeng Zhong, Liming Zheng, Shuai Fu, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, Zhejiang University, University of Adelaide
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
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
