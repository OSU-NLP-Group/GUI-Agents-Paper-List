# Papers with Keyword: visual grounding

- [Rethinking Token Pruning for Historical Screenshots in GUI Visual Agents: Semantic, Spatial, and Temporal Perspectives](https://arxiv.org/abs/2603.26041)
    - Daiqiang Li, Zihao Pan, Zeyu Zhang, Ronghao Chen, Huacan Wang, Honggang Chen, Haiyun Jiang
    - 🏛️ Institutions: Sichuan University, Sun Yat-sen University, Australian National University, Peking University, University of Chinese Academy of Sciences, Shanghai Jiao Tong University
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [token pruning], [efficiency], [MLLM], [visual grounding], [empirical study]
    - 📖 TLDR: This paper conducts an empirical study on token pruning for historical screenshots in GUI visual agents, revealing three key insights: background regions capture valuable interface-state transitions, random pruning better preserves spatial structure than designed strategies, and a temporal recency effect allows heavy compression of distant screenshots with minimal performance loss.

- [FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair](https://arxiv.org/abs/2603.17826)
    - Ruize Ma, Yilei Jiang, Shilin Zhang, Zheng Ma, Yi Feng
    - 🏛️ Institutions: Nanjing University, SenseTime, The Chinese University of Hong Kong, University of Texas at Dallas
    - 📅 Date: March 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multimodal], [software engineering], [program repair], [memory-augmented], [visual grounding], [benchmark]
    - 📖 TLDR: FailureMem is a multimodal automated program repair framework for settings where repair requires jointly reasoning over code, issue text, and GUI screenshots. It combines a hybrid workflow-agent architecture, localized visual grounding through active perception tools, and a Failure Memory Bank that turns failed repair attempts into reusable guidance, improving resolved rate over GUIRepair on SWE-bench Multimodal.

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
    - 🏛️ Institutions: McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [safety], [visual grounding], [guardrail], [adversarial attacks], [TOCTOU], [visual confused deputy]
    - 📖 TLDR: This paper reframes perception failures in GUI agents as a security problem rather than just a performance issue, formalizing the visual confused deputy where misperceived UI state causes privileged actions on the wrong target. It then proposes a dual-channel guardrail that separately checks the visual target and the agent's textual reasoning to block unsafe executions.

- [Zoom to Essence: Trainless GUI Grounding by Inferring upon Interface Elements](https://arxiv.org/abs/2603.14448)
    - Jingfeng Yang, Yu Tan, Haofeng Gao, Xiaozhi Gao, Jianguo Li
    - 🏛️ Institutions: Sichuan University, Tsinghua University, Nanjing University, Nanyang Technological University
    - 📅 Date: March 15, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [inference scaling], [training-free], [MLLM], [visual grounding], [image pyramid]
    - 📖 TLDR: ZoomUI is a training-free GUI grounding method built on the observation that complex interfaces can be decomposed into simpler visual elements that generic MLLMs already understand. It uses latent reasoning to rewrite instructions into visual feature descriptions and then progressively zooms attention onto candidate UI regions, reaching or surpassing fine-tuned baselines without additional training.

- [MM-CondChain: A Programmatically Verified Benchmark for Visually Grounded Deep Compositional Reasoning](https://arxiv.org/abs/2603.12266)
    - Zhouheng Sun, Yingyao Zhou, Yang Liu, Junlu Tang, Jian Xie
    - 🏛️ Institutions: Alibaba Group, Zhejiang University
    - 📅 Date: March 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [multimodal LLM], [compositional reasoning], [visual grounding], [evaluation]
    - 📖 TLDR: MM-CondChain is a benchmark for evaluating visually grounded deep compositional reasoning in multimodal LLMs, featuring multi-layer conditional chains across natural images, charts, and GUI trajectories, where even the best model achieves only 53.33 Path F1, revealing that deeply chained compositional reasoning remains a fundamental challenge.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548)
    - Xiaoce Wang, Guibin Zhang, Junzhe Li, Fang Li, Chen Zhang
    - 🏛️ Institutions: Tsinghua University, National University of Singapore, Peking University, Shenzhen MSU-BIT University, Guangming Laboratory
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [tool use], [tokenization], [curriculum learning], [visual grounding], [data efficiency]
    - 📖 TLDR: ToolTok introduces a tool tokenization paradigm for GUI agents that models operations as multi-step pathfinding through learnable tool tokens with semantic anchoring and curriculum learning, achieving competitive performance with models 50x larger while using less than 1% of the training data required by other post-training approaches.

- [How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors](https://arxiv.org/abs/2601.21961)
    - Kuai Yu, Naicheng Yu, Han Wang, Rui Yang, Huan Zhang
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, Columbia University, University of California San Diego
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [GUI understanding], [visual grounding], [robustness]
    - 📖 TLDR: Introduces VAF, a controlled evaluation pipeline that systematically measures how webpage visual attribute factors (e.g., background color contrast, item size, position, card clarity) influence web agent decision-making across 48 variants, 5 real-world websites, and 4 representative agents.

- [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009)
    - Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu, Vineeth N Balasubramanian
    - 🏛️ Institutions: Indian Institute of Technology Bombay, Indian Institute of Technology Hyderabad
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [multimodal LLM], [slow-fast reasoning], [visual grounding], [implicit chain-of-thought], [adaptive perception]
    - 📖 TLDR: iSHIFT is a lightweight 2.5B-parameter multimodal GUI agent that integrates latent thinking (implicit chain-of-thought) with a perception control module, enabling adaptive switching between a fast mode for routine actions and a slow mode with detailed visual grounding for precision tasks, matching state-of-the-art performance on multiple GUI benchmarks despite its compact size.

- [Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding](https://arxiv.org/abs/2512.05941)
    - Zhiyuan Jiang, Shenghao Xie, Wenyi Li, Wenqiang Zu, Peihang Li, Jiahao Qiu, Siqi Pei, Lei Ma, Tiejun Huang, Mengdi Wang, Shilong Liu
    - 🏛️ Institutions: Xi’an Jiaotong University, Princeton University, Peking University, University of Chinese Academy of Sciences, The University of Hong Kong, Michigan State University
    - 📅 Date: December 05, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI grounding], [benchmark], [training-free], [zoom], [test-time scaling], [visual grounding]
    - 📖 TLDR: Proposes ZoomClick, a training-free method that leverages zoom as a prior for GUI grounding to dynamically focus on screen regions and switch context, achieving state-of-the-art results on benchmarks like ScreenSpot-Pro, and introduces GUIZoom-Bench for evaluating model adaptability to zoom.

- [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810)
    - Yuqi Zhou, Sunhao Dai, Shuai Wang, Kaiwen Zhou, Qinglin Jia, Jun Xu
    - 🏛️ Institutions: Gaoling School of Artificial Intelligence, Renmin University of China, Huawei Noah's Ark Lab
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [GUI grounding], [visual grounding], [reinforcement learning], [ScreenSpot], [GUI-G1]
    - 📖 TLDR: This paper analyzes why blindly copying R1-Zero-style online RL pipelines into GUI grounding leads to poor behavior, including overlong reasoning, reward hacking on box size, and under-optimization on hard examples. It then proposes targeted fixes in prompt design, reward shaping, and difficulty-aware policy optimization. The resulting GUI-G1 model sets a new state of the art for its scale on ScreenSpot-style GUI grounding benchmarks.

- [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370)
    - Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, Bo Li
    - 🏛️ Institutions: VCIP, School of Computer Science, NKU, vivo Mobile Communication Co., Ltd, National University of Singapore, Fudan University, East China University of Science and Technology
    - 📅 Date: May 18, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [reinforcement learning], [GUI grounding], [visual grounding], [ScreenSpot-pro], [SE-GUI]
    - 📖 TLDR: This paper targets visual grounding for GUI agents in complex, high-resolution interfaces where supervised fine-tuning often generalizes poorly. It introduces SE-GUI, an RL-based framework with seed-data curation, dense policy gradients, and self-evolutionary reinforcement finetuning driven by attention maps. With only 3k training samples, the 7B model reaches state-of-the-art results on multiple grounding benchmarks and substantially improves ScreenSpot-Pro performance.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, National University of Singapore
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [information-sensitive cropping], [self-refining dual learning], [visual grounding], [model]
    - 📖 TLDR: This paper introduces *Iris*, a visual agent designed to enhance GUI automation by addressing challenges in high-resolution, complex digital environments. It employs two key innovations: **Information-Sensitive Cropping (ISC)**, which dynamically identifies and prioritizes visually dense regions using an edge detection algorithm for efficient processing, and **Self-Refining Dual Learning (SRDL)**, which enhances the agent's ability to handle complex tasks through a dual-learning loop that iteratively refines its performance without requiring additional annotated data. Empirical evaluations demonstrate that Iris achieves state-of-the-art performance across multiple benchmarks with only 850K GUI annotations, outperforming methods using ten times more training data.

- [MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a2c3c86679300047c740c9900f19ddac-Abstract-Conference.html)
    - Haotian Zhang, Mingfei Gao, Zhe Gan, Philipp Dufter, Nina Wenzel, Forrest Huang, Dhruti Shah, Xianzhi Du, Bowen Zhang, Yanghao Li, Sam Dodge, Keen You, Zhen Yang, Aleksei Timofeev, Mingze Xu, Hong-You Chen, Jean-Philippe Fauconnier, Zhengfeng Lai, Haoxuan You, Zirui Wang, Afshin Dehghan, Peter Grasch, Yinfei Yang
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Misc]
    - 🔑 Key: [model], [MM1.5], [vision language model], [visual grounding], [reasoning], [data-centric], [analysis]
    - 📖 TLDR: This paper introduces MM1.5, a family of multimodal large language models (MLLMs) ranging from 1B to 30B parameters, including dense and mixture-of-experts variants. MM1.5 enhances capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning. The authors employ a data-centric training approach, utilizing high-quality OCR data and synthetic captions for continual pre-training, alongside an optimized visual instruction-tuning data mixture for supervised fine-tuning. Specialized variants, MM1.5-Video and MM1.5-UI, are designed for video understanding and mobile UI comprehension, respectively. Extensive empirical studies provide insights into the training processes, offering guidance for future MLLM development.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: Carnegie Mellon University, University of California, Santa Barbara
    - 📅 Date: June 30, 2024
    - 📑 Publisher: NAACL 2024 Industry Track
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [visual grounding], [UI element localization], [LVG]
    - 📖 TLDR: This work introduces the task of visual UI grounding, which unifies detection and grounding by enabling models to identify UI elements referenced by natural language commands solely from visual input. The authors propose **LVG**, a model that outperforms baselines pre-trained on larger datasets by over 4.9 points in top-1 accuracy, demonstrating its effectiveness in localizing referenced UI elements without relying on UI metadata.

- [Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V](https://arxiv.org/abs/2310.11441)
    - Jianwei Yang, Hao Zhang, Feng Li, Xueyan Zou, Chunyuan Li, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research
    - 📅 Date: October 17, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [visual prompting], [Set-of-Mark], [visual grounding], [zero-shot], [region marking]
    - 📖 TLDR: Introduces Set-of-Mark prompting, where segmented image regions are overlaid with explicit marks before being passed to a multimodal model. The paper shows that simple region marking can unlock much stronger zero-shot grounding from GPT-4V without fine-tuning.
