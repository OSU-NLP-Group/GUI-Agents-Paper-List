# Yuxiang Chai's Papers

- [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832)
    - Han Xiao, Guozhi Wang, Hao Wang, Shilong Liu, Yuxiang Chai, Yue Pan, Yufeng Zhou, Xiaoxin Chen, Yafei Wen, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, Princeton University, Shenzhen Loop Area Institute, Shanghai AI Lab
    - 📅 Date: February 5, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [memory], [reinforcement learning], [online RL], [mobile GUI agent], [UI-mem]
    - 📖 TLDR: This paper proposes UI-Mem, a mobile GUI agent training framework that augments online reinforcement learning with a hierarchical experience memory storing reusable workflows, subtask skills, and failure patterns. It introduces stratified group sampling to mix strong, weak, and unguided rollouts, plus a self-evolving loop that continually abstracts new successful plans and error diagnoses back into memory. Experiments on AndroidWorld and AndroidLab show strong gains over standard online RL and static reuse baselines, especially on unseen applications.

- [EntWorld: A Holistic Environment and Benchmark for Verifiable Enterprise GUI Agents](https://arxiv.org/abs/2601.17722)
    - Haotian Zhao, Yuxiang Chai, Pengxiang Zhao, Wendi Yu, Difei Gao
    - 🏛️ Institutions: Zhongguancun Laboratory, Tsinghua University
    - 📅 Date: January 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [web agent], [enterprise], [evaluation], [dataset], [GUI agent]
    - 📖 TLDR: EntWorld is a large-scale benchmark of 1,756 tasks across six enterprise domains (CRM, ITIL, ERP, etc.) with SQL-based deterministic verification, revealing that state-of-the-art models like GPT-4.1 achieve only 47.61% success rate compared to human performance, highlighting a significant enterprise gap in current GUI agent capabilities.

- [GraphPilot: GUI Task Automation with One-Step LLM Reasoning Powered by Knowledge Graph](https://arxiv.org/abs/2601.17418)
    - Pengxiang Zhao, Yuxiang Chai, Haotian Zhao, Yiyuan Liu, Shuai Ren
    - 🏛️ Institutions: Sun Yat-sen University
    - 📅 Date: January 17, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [GUI agent], [mobile], [knowledge graph], [LLM], [task automation], [efficiency]
    - 📖 TLDR: GraphPilot constructs app-specific knowledge graphs offline to encode page functions, element roles, and transition rules, then uses these graphs to guide LLM reasoning online so that a mobile GUI agent can plan a complete action sequence in nearly one LLM query, improving task completion rate on DroidTask while substantially reducing latency and the number of LLM calls compared to stepwise approaches.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [reward model], [self-improvement], [synthetic data], [mobile GUI agent], [UI-genie-RM], [UI-genie-agent]
    - 📖 TLDR: This paper introduces UI-Genie, a self-improving mobile GUI-agent framework that tackles two bottlenecks at once: outcome verification and scalable high-quality trajectory generation. It builds a dedicated reward model, UI-Genie-RM, plus a reward-guided self-improvement loop that iteratively upgrades both the agent and the reward model in dynamic environments. The paper also releases the first reward-specific GUI-agent dataset and reports state-of-the-art performance across multiple mobile GUI benchmarks after several generations of self-improvement.

- [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, Wenhao Wang, Tianze Wu, Linghao Li, Guanjing Xiong, Yong Liu, Hongsheng Li
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab, The Chinese University of Hong Kong MMLab
    - 📅 Date: April 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [survey], [framework], [dataset], [benchmark], [planning], [multimodal], [taxonomy]
    - 📖 TLDR: This comprehensive survey examines the evolution of LLM-powered GUI agents in mobile phone automation, transitioning from static scripts to intelligent, adaptive systems. It presents a taxonomy encompassing agent frameworks (single-agent, multi-agent, plan-then-act), modeling approaches (prompt engineering, training-based), and essential datasets and benchmarks. The paper discusses how LLMs enhance language understanding, multimodal perception, and decision-making in GUI tasks, and addresses challenges such as dataset diversity, on-device deployment efficiency, user-centric adaptation, and security concerns. It serves as a definitive reference for researchers and practitioners aiming to leverage LLMs in designing scalable, user-friendly phone GUI agents.

- [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805)
    - Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, Shibo He, Wenchao Meng
    - 🏛️ Institutions: Zhejiang University, vivo AI Lab
    - 📅 Date: April 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [few-shot learning], [LearnAct], [LearnGUI], [DemoParser], [KnowSeeker], [ActExecutor]
    - 📖 TLDR: This paper introduces **LearnAct**, a multi-agent framework designed to enhance mobile GUI agents through few-shot demonstration learning. Accompanied by **LearnGUI**, a dataset comprising 2,252 offline and 101 online tasks with high-quality human demonstrations, the framework integrates three specialized agents—DemoParser, KnowSeeker, and ActExecutor—to extract, retrieve, and apply knowledge from demonstrations. Experimental results show significant performance improvements in both offline and online evaluations, establishing demonstration-based learning as a promising direction for developing adaptable and personalized mobile GUI agents.

- [UI-R1: Enhancing Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)
    - Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Guanjing Xiong, Hongsheng Li
    - 🏛️ Institutions: vivo AI Lab, MMLab, The Chinese University of Hong Kong
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [reinforcement learning], [UI-R1-3B], [GRPO], [AndroidControl], [ScreenSpot-pro]
    - 📖 TLDR: This paper introduces **UI-R1**, a framework that enhances the reasoning capabilities of multimodal large language models (MLLMs) for GUI action prediction tasks through rule-based reinforcement learning. Utilizing a small, high-quality dataset of 136 challenging mobile tasks, the authors design a unified rule-based action reward function and optimize the model using Group Relative Policy Optimization (GRPO). The resulting model, **UI-R1-3B**, demonstrates significant improvements over the base model (Qwen2.5-VL-3B) on both in-domain (AndroidControl) and out-of-domain (ScreenSpot-Pro) benchmarks, showcasing the effectiveness of rule-based RL in advancing GUI understanding and control.

- [A3: Android Agent Arena for Mobile GUI Agents with Essential-State Procedural Evaluation](https://arxiv.org/abs/2501.01149)
    - Yuxiang Chai, Shunye Tang, Han Xiao, Weifeng Lin, Hanhao Li, Jiayu Zhang, Liang Liu, Pengxiang Zhao, Guangyi Liu, Guozhi Wang, Shuai Ren, Rongduo Han, Haining Zhang, Siyuan Huang, Hongsheng Li
    - 🏛️ Institutions: The Chinese University of Hong Kong, Nankai University, vivo AI Lab, Shanghai Jiao Tong University
    - 📅 Date: January 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [Android], [mobile agent], [GUI agent], [evaluation], [LLM-based evaluation]
    - 📖 TLDR: A3 (Android Agent Arena) introduces a benchmark of 100 tasks across 20 popular online Android apps with a novel "essential-state" procedural evaluation method that uses MLLMs as reward models to progressively verify task completion, addressing the limitations of static or offline-only benchmarks for mobile GUI agents.

- [AMEX: Android Multi-annotation Expo Dataset for Mobile GUI Agents](https://aclanthology.org/2025.findings-acl.110/)
    - Yuxiang Chai, Siyuan Huang, Yazhe Niu, Han Xiao, Liang Liu, Guozhi Wang, Dingyu Zhang, Shuai Ren, Hongsheng Li
    - 🏛️ Institutions: The Chinese University of Hong Kong, Shanghai Jiao Tong University, Shanghai AI Laboratory, vivo AI Lab
    - 📅 Date: July 3, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [AMEX]
    - 📖 TLDR: This paper introduces the **Android Multi-annotation EXpo (AMEX)**, a comprehensive dataset designed for training and evaluating mobile GUI-control agents. AMEX comprises over 104K high-resolution screenshots from 110 popular mobile applications, annotated at multiple levels, including GUI interactive element grounding, functionality descriptions, and complex natural language instructions. The dataset aims to advance research on AI agents capable of completing complex tasks by interacting directly with mobile device GUIs.
