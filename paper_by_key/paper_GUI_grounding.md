# Papers with Keyword: GUI grounding

- [What's Missing in Screen-to-Action? Towards a UI-in-the-Loop Paradigm for Multimodal GUI Reasoning](https://arxiv.org/abs/2604.06995)
    - Songze Li, Xiaoke Guo, Tianqi Liu, Biao Yi, Zhaoyan Gong, Zhiqiang Liu, Huajun Chen, Wen Zhang
    - 🏛️ Institutions: ZJU
    - 📅 Date: April 08, 2026
    - 📑 Publisher: Findings of ACL 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [benchmark], [UILoop], [UI comprehension]
    - 📖 TLDR: UILoop treats GUI reasoning as a cyclic Screen-UI elements-Action process, enabling MLLMs to explicitly learn the localization, semantic functions, and usage of key UI elements. It introduces UI Comprehension-Bench (26K samples) and achieves state-of-the-art GUI reasoning performance with improved interpretability.

- [Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding](https://arxiv.org/abs/2603.26211)
    - Shrinidhi Kumbhar, Haofu Liao, Srikar Appalaraju, Kunwar Yashraj Singh
    - 🏛️ Institutions: Arizona State University, Amazon (AWS Agentic AI)
    - 📅 Date: March 27, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [diffusion models], [hybrid masking], [bounding-box prediction], [LLaDA-V], [cross-platform]
    - 📖 TLDR: This paper adapts the discrete diffusion model LLaDA-V to GUI grounding and proposes a hybrid masking schedule for bounding-box prediction. Across web, desktop, and mobile benchmarks, the diffusion model outperforms its linear-masked variant and remains competitive with autoregressive VLMs.

- [AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement](https://arxiv.org/abs/2603.17441)
    - Siqi Pei, Liang Tang, Tiaonan Duan, Long Chen, Shuxian Li, Kaer Huang, Yanzhe Jing, Yiqiang Yan, Bo Zhang, Chenghao Jiang, Borui Zhang, Jiwen Lu
    - 🏛️ Institutions: Lenovo Research
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [instruction refinement], [adaptive zoom], [GRPO], [bounding-box prediction], [AdaZoom-GUI]
    - 📖 TLDR: AdaZoom-GUI targets two concrete GUI-grounding bottlenecks: ambiguous natural-language instructions and tiny UI elements in high-resolution screenshots. It combines instruction rewriting with a conditional second-stage zoom-in pass and reports state-of-the-art grounding performance among comparable model sizes.

- [Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements](https://arxiv.org/abs/2603.14448)
    - Ziwei Liu, Tao Feng, Borui Kang, Yanbing Yang, Jun Luo
    - 🏛️ Institutions: Sichuan University, Tsinghua, NJU, NTU
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [training-free], [inference scaling], [ZoomUI], [instruction rewriting], [progressive zooming]
    - 📖 TLDR: ZoomUI is a training-free GUI grounding method built on the idea that complex interfaces can be decomposed into simpler visual elements that generic MLLMs already understand. It rewrites instructions into element-level visual descriptions and progressively zooms onto candidate UI regions, reaching or surpassing fine-tuned baselines without additional training.

- [Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision](https://arxiv.org/abs/2602.14276)
    - A. Said Gurbuz, Sunghwan Hong, Ahmed Nassar, Marc Pollefeys, Peter Staar
    - 🏛️ Institutions: IBM Research, ETH, KAIST
    - 📅 Date: February 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [dataset], [screen parsing], [dense supervision], [ScreenParse], [UI understanding]
    - 📖 TLDR: This paper argues that sparse grounding supervision is insufficient for GUI understanding and introduces ScreenParse, a large-scale densely annotated screen-parsing dataset. It provides complete UI-element supervision across web screenshots to support richer grounding and UI understanding models.

- [WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements](https://arxiv.org/abs/2602.11724)
    - Xiwen Teoh, Yun Lin, Duc-Minh Nguyen, Ruofei Ren, Wenjie Zhang, Jin Song Dong
    - 🏛️ Institutions: NUS, SJTU
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web testing], [bug detection], [GUI grounding], [test oracle], [symbolized GUI elements], [WebTestPilot]
    - 📖 TLDR: WebTestPilot is an agentic end-to-end web-testing system that symbolizes GUI elements and infers test oracles from natural-language specifications. It achieves high precision and recall on bug-injected web apps and outperforms existing baselines in automated web testing.

- [POINTS-GUI-G: GUI-Grounding Journey](https://arxiv.org/abs/2602.06391)
    - Zhongyin Zhao, Yuan Liu, Yikun Liu, Haicheng Wang, Le Tian, Xiao Zhou, Yangxiu You, Zilin Yu, Yang Yu, Jie Zhou
    - 🏛️ Institutions: WeChat AI
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [data engineering], [vision encoder training], [verifiable rewards], [POINTS-GUI-G-8B], [ScreenSpot-pro]
    - 📖 TLDR: POINTS-GUI-G studies how to build strong GUI grounding from a base model without strong initial spatial grounding. It attributes gains to multi-source data engineering, improved vision-encoder training, and RL with verifiable rewards, producing competitive results across several grounding benchmarks.

- [Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion](https://arxiv.org/abs/2602.06351)
    - Longhui Ma, Di Zhao, Siwei Wang, Zhao Lv, Miao Wang
    - 🏛️ Institutions: National University of Defense Technology, Academy of Military Sciences
    - 📅 Date: February 06, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [multimodal fusion], [attention mechanism], [training-free], [OCR], [Trifuse]
    - 📖 TLDR: Trifuse is a training-free GUI grounding method that fuses MLLM attention, OCR text, and icon caption signals through a consensus-based fusion strategy. It improves grounding across multiple benchmarks without task-specific fine-tuning.

- [SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization](https://arxiv.org/abs/2601.22491)
    - Jinyang Wu, Changpeng Yang, Yuhao Shen, Fangzhi Xu, Bolin Ni, Chonghua Liao, Yuchen Liu, Hongzhen Wang, Shuai Nie, Shuai Zhang, Haoran Luo, Jiaming Xu
    - 🏛️ Institutions: Tsinghua, Xiaomi, ZJU, NTU, Institute of Automation, CAS
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [tiered rewards], [reward shaping], [GUI grounding], [planning], [SSL]
    - 📖 TLDR: SSL replaces binary verifier rewards with progressively amplified tiered rewards that distinguish higher- and lower-quality successful trajectories. Across GUI perception, short- and long-horizon planning, and reasoning benchmarks, it improves optimization stability and reaches up to 2.5x better sample efficiency than binary-reward baselines.

- [V2P: Visual Attention Calibration for GUI Grounding via Background Suppression and Center Peaking](https://arxiv.org/abs/2601.06899)
    - Jikai Chen, Long Chen, Dong Wang, Qinglin Su, Zhixuan Chu, Bingguang Hao, Leilei Gan, Chenyi Zhuang, Jinjie Gu
    - 🏛️ Institutions: ZJU, Inclusion AI, Ant Group
    - 📅 Date: January 11, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [visual attention], [background suppression], [Fitts' law], [V2P]
    - 📖 TLDR: V2P improves attention-based GUI grounding by suppressing irrelevant background regions and using a Fitts’ Law-inspired Gaussian peak to emphasize an element’s actionable center over its edges. The paper reports 92.4% on ScreenSpot-v2 and 52.5% on ScreenSpot-Pro, with ablations confirming both components matter.

- [VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks](https://arxiv.org/abs/2512.16501)
    - Beitong Zhou, Zhexiao Huang, Yuan Guo, Zhangxuan Gu, Tianyu Xia, Zichen Luo, Fei Tang, Dehan Kong, Yanyi Shang, Suling Ou, Zhenlin Guo, Changhua Meng, Shuheng Shen
    - 🏛️ Institutions: Venus Team, Ant Group, iMean AI
    - 📅 Date: December 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [benchmark], [GUI grounding], [bilingual benchmark], [hierarchical evaluation], [VenusBench-GD]
    - 📖 TLDR: VenusBench-GD is a bilingual GUI grounding benchmark spanning mobile, desktop, and web platforms, and organizes evaluation into basic and advanced grounding tasks. The paper uses this hierarchy to show that general-purpose multimodal models have mostly caught up on basic grounding, while advanced tasks still expose substantial reasoning and robustness gaps.

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

- [AFRAgent : An Adaptive Feature Renormalization Based High Resolution Aware GUI agent](https://arxiv.org/abs/2512.00846)
    - Neeraj Anand, Rishabh Jain, Sohan Patnaik, Balaji Krishnamurthy, Mausoom Sarkar
    - 🏛️ Institutions: Adobe
    - 📅 Date: November 30, 2025
    - 📑 Publisher: WACV 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI grounding], [smartphone automation], [adaptive feature renormalization], [instruct-BLIP], [AFRAgent]
    - 📖 TLDR: AFRAgent targets the loss of spatial detail that hurts mobile GUI automation models built on low-resolution vision features. It adds an adaptive feature renormalization module to enrich instruct-BLIP image embeddings with high-resolution information, and reports state-of-the-art results on Meta-GUI and AITW with a much smaller model than prior baselines.

- [Beyond Clicking: A Step Towards Generalist GUI Grounding via Text Dragging](https://arxiv.org/abs/2601.06031)
    - Zeyi Liao, Yadong Lu, Boyu Gou, Huan Sun, Ahmed Awadallah
    - 🏛️ Institutions: OSU, Microsoft Research, Redmond
    - 📅 Date: November 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [dataset], [benchmark], [text dragging], [GUI-Drag], [ScreenDrag]
    - 📖 TLDR: This paper expands GUI grounding beyond click actions by focusing on text dragging, a common but previously underexplored mouse interaction. It introduces the GUI-Drag training set and the ScreenDrag benchmark, and shows that continual training for dragging can improve drag performance without sacrificing click grounding.

- [GUI-Spotlight: Adaptive Iterative Focus Refinement for Enhanced GUI Visual Grounding](https://arxiv.org/abs/2510.04039)
    - Bin Lei, Nuo Xu, Ali Payani, Mingyi Hong, Chunhua Liao, Yu Cao, Caiwen Ding
    - 🏛️ Institutions: University of Minnesota, Cisco Research, Lawrence Livermore National Labs
    - 📅 Date: October 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [image-grounded reasoning], [iterative focus refinement], [ScreenSpot-pro], [GUI-Spotlight]
    - 📖 TLDR: GUI-Spotlight is a GUI grounding model that performs image-grounded reasoning by iteratively invoking specialized tools to narrow attention to the relevant screen region. Trained with only 18.5K examples, it reaches 52.8% accuracy on ScreenSpot-Pro, outperforming prior 7B grounding models trained on much larger datasets.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [reinforcement learning], [fast thinking template], [difficulty-aware scaling], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [ReGUIDE: Data Efficient GUI Grounding via Spatial Reasoning and Search](https://arxiv.org/abs/2505.15259)
    - Hyunseok Lee, Jeonghoon Kim, Beomjun Kim, Jihoon Tack, Chansong Jo, Jaehong Lee, Cheonbok Park, Sookyo In, Jinwoo Shin, Kang Min Yoo
    - 🏛️ Institutions: KAIST, NAVER Cloud
    - 📅 Date: May 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [GUI grounding], [spatial reasoning], [data efficiency], [test-time scaling], [ReGUIDE]
    - 📖 TLDR: ReGUIDE improves web GUI grounding under limited data by combining self-generated reasoning, spatially aware criticism, and test-time spatial search. It substantially outperforms baselines while using only a tiny fraction of the training data required by prior web-grounding approaches.

- [Scaling Computer‑Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227)
    - Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: HKU, Salesforce AI Research
    - 📅 Date: May 19, 2025
    - 📑 Publisher: NeurIPS 2025 Datasets and Benchmarks Track (Spotlight)
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [benchmark], [GUI grounding], [OSWorld-G], [Jedi], [compositional generalization]
    - 📖 TLDR: This paper targets the mismatch between simplified grounding benchmarks and real computer-use grounding. It introduces the OSWorld-G benchmark and the 4M-example Jedi grounding dataset generated by UI decomposition and synthesis, showing that better grounding data transfers into large gains on both grounding benchmarks and downstream agent performance.

- [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: NKU, vivo Mobile Communication Co., Ltd, NUS, Fudan, East China University of Science and Technology
    - 📅 Date: May 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [General GUI]
    - 🔑 Key: [reinforcement learning], [GUI grounding], [dense policy gradient], [self-evolutionary finetuning], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684)
    - Tiange Luo, Lajanugen Logeswaran, Justin Johnson, Honglak Lee
    - 🏛️ Institutions: University of Michigan, LG AI Research
    - 📅 Date: May 01, 2025
    - 📑 Publisher: ICCV 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [RegionFocus], [visual test-time scaling], [image-as-map], [visual search]
    - 📖 TLDR: This paper frames GUI grounding as an iterative visual search process rather than a single full-screen prediction. Its RegionFocus method repeatedly zooms into promising regions and uses an image-as-map view to expose landmarks and action candidates, improving grounding on ScreenSpot-Pro and WebVoyager without retraining the base model.

- [ScaleTrack: Scaling and back-tracking Automated GUI Agents](https://arxiv.org/abs/2505.00416)
    - Jing Huang, Zhixiong Zeng, Wenkang Han, Yufeng Zhong, Liming Zheng, Shuai Fu, Jingyuan Chen, Lin Ma
    - 🏛️ Institutions: Meituan, ZJU, University of Adelaide
    - 📅 Date: May 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [GUI grounding], [backtracking planning], [data scaling], [historical action backtracking], [ScaleTrack]
    - 📖 TLDR: ScaleTrack targets two training bottlenecks in automated GUI agents: weak grounding data coverage and the lack of backtracking behavior during planning. It aggregates GUI samples from heterogeneous sources into a unified grounding corpus and trains agents to predict the next action together with the historical actions that led to the current screen.

- [UI-E2I-Synth: Advancing GUI Grounding with Large-Scale Instruction Synthesis](https://aclanthology.org/2025.findings-acl.809/)
    - Xinyi Liu, Xiaoyi Zhang, Ziyun Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia, PKU
    - 📅 Date: April 15, 2025
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [benchmark], [instruction synthesis], [GUI grounding], [UI-E2I-Synth], [UI-I2E-Bench]
    - 📖 TLDR: UI-E2I-Synth addresses the annotation bottleneck in vision-based GUI grounding by using GPT-4o to synthesize large-scale grounding instructions with varied difficulty and annotation properties. The paper also introduces the UI-I2E-Bench benchmark for evaluating GUI instruction grounding under challenges such as implicit instructions, small elements, and underrepresented element types.

- [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981)
    - Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, Tat-Seng Chua
    - 🏛️ Institutions: NUS, East China Normal University, Hong Kong Baptist University
    - 📅 Date: April 04, 2025
    - 📑 Publisher: ACM Multimedia 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [GUI grounding], [high-resolution], [ScreenSeekeR], [ScreenSpot-pro]
    - 📖 TLDR: ScreenSpot-Pro benchmarks GUI grounding in professional high-resolution computer-use settings with 1,581 tasks across 23 applications, five industries, and three operating systems. The paper also proposes ScreenSeekeR, a cascaded visual search method guided by planner knowledge, and shows that current grounding models remain weak in these professional environments.

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: ZJU, Microsoft Research Asia
    - 📅 Date: March 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [dual-system cognition], [adaptive system switching], [progressive decomposition], [Focus]
    - 📖 TLDR: Focus is a GUI grounding model that switches between fast prediction and slower analysis depending on task complexity. It decomposes grounding into summarization, focused visual analysis, and coordinate prediction, and reaches strong ScreenSpot and ScreenSpot-Pro performance with a 2B model trained on 300K examples.

- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)
    - Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng, Xin Liu, Guang Shi
    - 🏛️ Institutions: ByteDance Seed, Tsinghua
    - 📅 Date: January 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [GUI grounding], [unified action modeling], [system-2 reasoning], [reflective online traces], [UI-TARS]
    - 📖 TLDR: UI-TARS is an end-to-end GUI agent model that acts directly from screenshots instead of relying on wrapper-style prompting workflows around proprietary models. It combines enhanced perception, unified cross-platform action modeling, deliberate multi-step reasoning, and iterative training on reflective online traces, and reports strong performance across ten-plus GUI benchmarks.

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: HKU, Salesforce AI Research, Alibaba Group, Australian National University, Independent Researcher
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [pure vision], [instruction synthesis], [context-aware grounding], [Aria-UI]
    - 📖 TLDR: Aria-UI is a GUI-grounding model that deliberately avoids HTML or AXTree inputs and instead works from pure visual observations. It pairs a scalable instruction-synthesis pipeline with interleaved textual and text-image action histories for context-aware grounding, and reports state-of-the-art results across offline and online grounding benchmarks.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: ZJU, NUS
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [GUI grounding], [information-sensitive cropping], [self-refining dual learning], [visual grounding], [Iris]
    - 📖 TLDR: Iris targets the visual-perception bottleneck of GUI agents in high-resolution, visually complex interfaces. It combines information-sensitive cropping with a self-refining dual-learning loop between referring and grounding, and the resulting gains transfer to both web and OS downstream tasks.

- [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://aclanthology.org/2025.findings-acl.76/)
    - Yiqin Wang, Haoji Zhang, Jingqi Tian, Yansong Tang
    - 🏛️ Institutions: Shenzhen International Graduate School, Tsinghua
    - 📅 Date: December 02, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [pure vision], [GUI grounding], [interpreter-locator], [ScreenSpot], [Ponder & Press]
    - 📖 TLDR: Ponder & Press is a pure-vision divide-and-conquer GUI-control framework that separates high-level instruction interpretation from element localization. It pairs a general-purpose MLLM interpreter with a GUI-specific locator, improves ScreenSpot grounding by 22.5%, and reports strong performance across web, desktop, and mobile GUI benchmarks.

- [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)
    - Anthony Nguyen
    - 🏛️ Institutions: Algoma University
    - 📅 Date: November 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [GUI grounding], [visual prompting], [iterative narrowing]
    - 📖 TLDR: Iterative Narrowing is a visual-prompting framework for GUI grounding that repeatedly zooms into smaller image regions to refine predictions. The paper shows that this simple test-time strategy improves both general and fine-tuned VLMs on one-shot grounding across multiple UI platforms.

- [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Laboratory, SJTU, HKU, MIT
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025 (Spotlight)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform corpus], [OS-Atlas]
    - 📖 TLDR: OS-Atlas is a foundation action model for GUI agents built on a multi-platform grounding-data synthesis toolkit and a corpus with more than 13 million GUI elements. It improves GUI grounding and zero-shot out-of-distribution agent performance across desktop, mobile, and web benchmarks.

- [EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data](https://arxiv.org/abs/2410.19461)
    - Xuetian Chen, Hangcheng Li, Jiaqing Liang, Sihang Jiang, Deqing Yang
    - 🏛️ Institutions: Fudan
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [synthetic data], [GUI grounding], [multi-granularity data], [EDGE]
    - 📖 TLDR: EDGE is a synthetic-data pipeline for GUI understanding that generates large-scale multi-granularity supervision from webpages. Models trained on the resulting dataset improve webpage understanding first and then transfer that gain to previously unseen desktop and mobile GUI environments with much less manual annotation.

- [ClickAgent: Enhancing UI Location Capabilities of Autonomous Agents](https://aclanthology.org/2025.sigdial-1.38/)
    - Jakub Hoscilowicz, Bartosz Maj, Bartosz Kozakiewicz, Oleksii Tymoshchuk, Artur Janicki
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 09, 2024
    - 📑 Publisher: SIGDIAL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [GUI grounding], [AITW], [ClickAgent], [mobile control]
    - 📖 TLDR: Proposes ClickAgent, a mobile agent framework that separates high-level reasoning from precise UI element localization. By pairing an MLLM planner with a dedicated grounding component, it improves task success on AITW and on real-device Android evaluations.

- [TinyClick: Single-Turn Agent for Empowering GUI Automation](https://www.isca-archive.org/interspeech_2025/pawlowski25_interspeech.html)
    - Pawel Pawlowski, Krystian Zawistowski, Wojciech Lapacz, Adam Wiacek, Marcin Skorupa, Sebastien Postansque, Jakub Hoscilowicz
    - 🏛️ Institutions: Samsung R&D Poland, Warsaw University of Technology
    - 📅 Date: October 09, 2024
    - 📑 Publisher: INTERSPEECH 2025
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [GUI grounding], [single-turn agent], [on-device model], [Florence-2], [ScreenSpot], [OmniACT], [TinyClick]
    - 📖 TLDR: TinyClick is a 0.27B single-turn GUI agent built on Florence-2-Base that predicts the target UI element from a screenshot and user command. The paper attributes its gains to vision-specific multitask training and MLLM-based data augmentation, and reports strong results on ScreenSpot and OmniAct annotations while keeping latency and training cost low.

- [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4ca0e369689dadb25a5345ba9755ad6f-Abstract-Conference.html)
    - Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su
    - 🏛️ Institutions: OSU, Orby AI
    - 📅 Date: October 07, 2024
    - 📑 Publisher: ICLR 2025 (Oral)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [dataset], [GUI grounding], [vision-only agents], [cross-platform grounding], [UGround], [synthetic data]
    - 📖 TLDR: This paper introduces UGround, a universal GUI visual grounding model trained on 10M element-expression pairs over 1.3M screenshots from web, mobile, and desktop interfaces. It argues for vision-only GUI agents with pixel-level actions and shows that UGround improves grounding, offline-agent, and online-agent performance across six benchmarks.

- [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337)
    - Longxi Gao, Li Zhang, Shihe Wang, Pengzhi Gao, Wei Liu, Jian Luan, Shangguang Wang, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua
    - 📅 Date: September 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [GUI grounding], [data collection], [MobileViews]
    - 📖 TLDR: MobileViews is a mobile GUI dataset with more than 1.2 million screenshot-view hierarchy pairs collected from over 30K Android apps using VLM-enhanced automatic traversal on mobile SoC clusters. The paper shows that training on MobileViews improves GUI grounding accuracy by up to 6.1% on representative mobile grounding benchmarks.

- [Grounded GUI Understanding for Vision-Based Spatial Intelligent Agent: Exemplified by Extended Reality Apps](https://arxiv.org/abs/2409.10811)
    - Shuqing Li, Binchang Li, Yepang Liu, Cuiyun Gao, Jianping Zhang, Shing-Chi Cheung, Michael R. Lyu
    - 🏛️ Institutions: CUHK, Harbin Institute of Technology, Southern University of Science and Technology, HKUST
    - 📅 Date: September 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [XR apps], [interactable element detection], [zero-shot detection], [Orienter]
    - 📖 TLDR: This paper proposes Orienter, a zero-shot framework for detecting context-sensitive interactable GUI elements in extended-reality apps. It targets XR-specific challenges such as open-vocabulary GUI elements, context-dependent interactability, and spatial perception, and the paper reports stronger performance than prior GUI element detection approaches on VR app data.

- [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203)
    - Yadong Lu, Jianwei Yang, Yelong Shen, Ahmed Awadallah
    - 🏛️ Institutions: Microsoft Research, Microsoft GenAI
    - 📅 Date: August 01, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [screen parsing], [GUI grounding], [icon detection], [icon captioning], [OmniParser]
    - 📖 TLDR: OmniParser parses UI screenshots into structured screen elements by combining interactable icon detection with element captioning. The paper also curates icon-related datasets and shows that this screen parsing layer improves GPT-4V grounding on ScreenSpot, Mind2Web, and AITW.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: CMU, UC Santa Barbara, Google Research
    - 📅 Date: June 16, 2024
    - 📑 Publisher: NAACL 2024 Industry Track
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [visual grounding], [UI element localization], [layout-guided contrastive learning], [multi-context learning], [LVG]
    - 📖 TLDR: This paper defines visual UI grounding, where a model must localize the UI element referenced by a natural-language command directly from a screenshot without relying on UI metadata. It proposes LVG, which combines layout-guided contrastive learning with synthetic-to-real multi-context learning and improves top-1 accuracy by more than 4.9 points over strong baselines.

- [Visual Grounding Methods for Efficient Interaction with Desktop Graphical User Interfaces](https://arxiv.org/abs/2407.01558)
    - El Hassane Ettifouri, Jessica López Espejel, Laura Minkova, Tassnim Dardouri, Walid Dahhane
    - 🏛️ Institutions: Novelis
    - 📅 Date: May 05, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [GUI grounding], [instruction visual grounding], [IVGocr], [IVGdirect], [CPV metric]
    - 📖 TLDR: Studies instruction visual grounding for desktop GUIs, where a model must locate the screen element implied by a natural-language command. The paper proposes both modular and end-to-end grounding methods, introduces dedicated datasets, and adds the CPV metric for relaxed point-based evaluation.

- [Dual-View Visual Contextualization for Web Navigation](https://doi.org/10.1109/CVPR52733.2024.01369)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - 🏛️ Institutions: OSU
    - 📅 Date: February 06, 2024
    - 📑 Publisher: CVPR 2024 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [GUI grounding], [dual-view contextualization], [visual grounding], [web element neighborhood], [Mind2Web]
    - 📖 TLDR: This paper contextualizes each HTML element with its corresponding screenshot region and nearby elements, combining textual and visual features to represent webpage elements more informatively. It evaluates the approach on Mind2Web and reports consistent gains in cross-task, cross-website, and cross-domain settings.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Yantao Li, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: National Key Laboratory for Novel Software Technology, NJU, Shanghai AI Laboratory
    - 📅 Date: January 17, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [benchmark], [dataset], [GUI grounding], [grounding pre-training], [ScreenSpot], [SeeClick]
    - 📖 TLDR: SeeClick is a screenshot-only GUI agent built around the GUI grounding problem rather than structured trees such as HTML. The paper adds automated GUI-grounding data curation and introduces ScreenSpot, a grounding benchmark spanning mobile, desktop, and web environments.
