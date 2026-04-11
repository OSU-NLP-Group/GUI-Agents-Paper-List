# Adjacent Papers for GUI Agent Research

This file tracks papers that are important to the GUI-agent ecosystem but are **not** part of the canonical direct-GUI paper list in `ALL_PAPERS.md`.

Typical examples include:
- general-purpose foundation models later reused in GUI work
- non-GUI agent benchmarks, infrastructure, and evaluation papers
- general multimodal or prompting methods later adopted by GUI papers
- Search-API or agentic-search papers that are not primarily browser-based GUI-agent research

These entries are kept for reference only. The main list and generated environment pages are sourced only from `ALL_PAPERS.md`.

- [Seed1.8 Model Card: Towards Generalized Real-World Agency](https://arxiv.org/abs/2603.20633)
    - Bytedance Seed
    - 🏛️ Institutions: ByteDance Seed
    - 📅 Date: March 21, 2026
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [foundation model], [generalist agency], [tool use], [code execution], [GUI interaction], [Seed1.8]
    - 📖 TLDR: Seed1.8 is a foundation model for generalized real-world agency that unifies search, code generation and execution, and GUI interaction under one agentic interface. The model card emphasizes strong language-vision performance plus latency- and cost-aware inference modes for deployment.

- [MM-CondChain: A Programmatically Verified Benchmark for Visually Grounded Deep Compositional Reasoning](https://arxiv.org/abs/2603.12266)
    - Haozhan Shen, Shilin Yan, Hongwei Xue, Shuaiqi Lu, Xiaojun Tang, Guannan Zhang, Tiancheng Zhao, Jianwei Yin
    - 🏛️ Institutions: Accio Team, Alibaba Group, Zhejiang University, ZJU-BJ
    - 📅 Date: March 12, 2026
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [benchmark], [compositional reasoning], [visual grounding], [VPIR], [programmatic verification], [MM-CondChain]
    - 📖 TLDR: MM-CondChain is a benchmark for visually grounded deep compositional reasoning built from multi-layer conditional chains whose steps are programmatically verified through VPIR. It spans natural images, charts, and GUI trajectories, and shows that even the strongest MLLMs remain weak on deep chained reasoning.

- [You Told Me to Do It: Measuring Instructional Text-induced Private Data Leakage in LLM Agents](https://arxiv.org/abs/2603.11862)
    - Ching-Yu Kao, Xinfeng Li, Shenyu Dai, Tianze Qiu, Pengcheng Zhou, Eric Hanchen Jiang, Philip Sperl
    - 🏛️ Institutions: Fraunhofer AISEC, NTU, KTH, NUS, UCLA
    - 📅 Date: March 12, 2026
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [security], [documentation injection], [privacy], [data leakage], [ReadSecBench], [Trusted Executor Dilemma]
    - 📖 TLDR: This paper studies documentation-embedded instruction injection in high-privilege LLM agents and frames the failure mode as the Trusted Executor Dilemma. It introduces ReadSecBench, shows exfiltration success up to 85%, and finds that both rule-based and LLM-based defenses still fail to catch the attacks reliably.

- [OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/abs/2603.10165)
    - Yinjie Wang, Xuyang Chen, Xiaolong Jin, Mengdi Wang, Ling Yang
    - 🏛️ Institutions: University of Chicago, Princeton University, Peking University
    - 📅 Date: March 10, 2026
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [reinforcement learning], [agent training], [next-state signals], [process reward model], [on-policy distillation], [OpenClaw-RL]
    - 📖 TLDR: OpenClaw-RL is an asynchronous RL framework that treats next-state signals from live interactions as a universal learning source. It combines scalar rewards from a process-reward judge with hindsight-guided on-policy distillation, and trains agents across conversations, terminals, GUI tasks, SWE, and tool use in one online loop.

- [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430)
    - Renjun Xu, Yang Yan
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: February 12, 2026
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [survey], [agent skills], [SKILL.md], [MCP], [skill acquisition], [agent security]
    - 📖 TLDR: This survey reviews the emerging agent-skills ecosystem for LLMs, covering architectural foundations such as SKILL.md and MCP, methods for acquiring and refining skills, deployment patterns for agent systems, and the security problems introduced by portable, dynamically loaded capabilities.

- [Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning](https://arxiv.org/abs/2512.09706)
    - Kaichen He, Zihao Wang, Muyao Li, Anji Liu, Yitao Liang
    - 🏛️ Institutions: Peking University, National University of Singapore
    - 📅 Date: December 10, 2025
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [reinforcement learning], [heterogeneous action space], [multi-turn GRPO], [Minecraft agent], [cross-level actions], [CrossAgent]
    - 📖 TLDR: CrossAgent studies how a single agent model can switch among heterogeneous action spaces, including APIs, GUI events, and lower-level commands, without hand-written routing rules. Its training pipeline combines supervised fine-tuning with multi-turn GRPO and reports state-of-the-art results on 800+ Minecraft tasks, making it relevant to GUI work as a broader action-space unification result rather than a direct GUI paper.

- [Single-Agent Scaling Fails Multi-Agent Intelligence: Towards Foundation Models with Native Multi-Agent Intelligence](https://arxiv.org/abs/2512.08743)
    - Shuyue Hu, Haoyang Yan, Yiqun Zhang, Yang Chen, Dongzhan Zhou, Lei Bai
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory
    - 📅 Date: December 09, 2025
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [multi-agent systems], [foundation models], [multi-agent intelligence], [evaluation], [scaling], [survey]
    - 📖 TLDR: This paper argues that stronger single-agent foundation models do not automatically become strong multi-agent systems, and evaluates 41 open models on seven single-agent and multi-agent benchmarks to show the gap directly. It uses GUI interaction as one example of native single-agent capability, but its main contribution is a broader multi-agent intelligence agenda rather than GUI research itself.

- [Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents](https://arxiv.org/abs/2510.24702)
    - Yueqi Song, Ketan Ramaneti, Zaid Sheikh, Ziru Chen, Boyu Gou, Tianbao Xie, Yiheng Xu, Danyang Zhang, Apurva Gandhi, Fan Yang, Joseph Liu, Tianyue Ou, Zhihao Yuan, Frank Xu, Shuyan Zhou, Xingyao Wang, Xiang Yue, Tao Yu, Huan Sun, Yu Su, Graham Neubig
    - 🏛️ Institutions: Carnegie Mellon University, The Ohio State University, University of Hong Kong, Duke University, Fujitsu Research, All Hands AI
    - 📅 Date: October 28, 2025
    - 📑 Publisher: ICLR 2026 (Oral)
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [framework], [data protocol], [training data], [supervised fine-tuning], [dataset unification], [ADP]
    - 📖 TLDR: Agent Data Protocol (ADP) standardizes heterogeneous agent trajectories into a lightweight schema and conversion pipeline so diverse agent datasets can plug into multiple SFT pipelines without per-dataset engineering. Converting 13 existing datasets into ADP and fine-tuning on the unified corpus improves base models by about 20% on average across coding, browsing, tool-use, and research benchmarks.

- [Synthesizing Agentic Data for Web Agents with Progressive Difficulty Enhancement Mechanisms](https://arxiv.org/abs/2510.13913)
    - Shrey Pandit, Xuan-Phi Nguyen, Yifei Ming, Austin Xu, Jiayu Wang, Caiming Xiong, Shafiq Joty
    - 🏛️ Institutions: Salesforce AI Research, University of Wisconsin-Madison
    - 📅 Date: October 15, 2025
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [training data], [data synthesis], [progressive difficulty], [deep research], [tool-use diversity]
    - 📖 TLDR: This paper synthesizes training data for deep-research web agents by progressively increasing question difficulty until a baseline agent fails, then using that agent again for validation and filtering. The resulting corpus is aimed at long-horizon online-tool use rather than browser-native GUI interaction, but it is relevant as adjacent training-data work for agent systems.

- [Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation](https://arxiv.org/abs/2510.11977)
    - Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir, Zachary S. Siegel, Boyi Wei, Tianci Xue, Ziru Chen, Felix Chen, Saiteja Utpala, Franck Ndzomga, Dheeraj Oruganty, Sophie Luskin, Kangheng Liu, Botao Yu, Amit Arora, Dongyoon Hahm, Harsh Trivedi, Huan Sun, Juyong Lee, Tengjun Jin, Yifan Mai, Yifei Zhou, Yuxuan Zhu, Rishi Bommasani, Daniel Kang, Dawn Song, Peter Henderson, Yu Su, Percy Liang, Arvind Narayanan
    - 🏛️ Institutions: Princeton University, Independent Researcher, The Ohio State University, Microsoft Research, Amazon, Georgetown University, KAIST, Stony Brook University, University of Illinois Urbana-Champaign, Stanford University, xAI, University of California, Berkeley
    - 📅 Date: October 13, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [evaluation infrastructure], [leaderboard], [evaluation harness], [cost tracking], [log inspection], [agent traces], [HAL]
    - 📖 TLDR: HAL provides standardized infrastructure for evaluating agents across models, scaffolds, and benchmarks rather than introducing a new agent. It reports results from 21,730 rollouts across 9 models and 9 benchmarks, tracks costs and full traces, and uses LLM-aided log inspection to surface behaviors such as benchmark gaming and unsafe actions.

- [Reliable Weak-to-Strong Monitoring of LLM Agents](https://arxiv.org/abs/2508.19461)
    - Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang
    - 🏛️ Institutions: Scale AI, Carnegie Mellon University, Massachusetts Institute of Technology
    - 📅 Date: August 26, 2025
    - 📑 Publisher: ICLR 2025
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [safety], [LLM agent], [monitoring], [red-teaming]
    - 📖 TLDR: Stress-tests LLM agent monitoring systems for detecting covert misbehavior using a monitor red-teaming (MRT) workflow varying agent/monitor awareness and adversarial evasion strategies, evaluated on SHADE-Arena for tool-calling agents and CUA-SHADE-Arena for computer-use agents.

- [BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent](https://arxiv.org/abs/2508.06600)
    - Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Andrew Liu, Joshua Green, Kshama Patel, Ruoxi Meng, Mingyi Su, Sahel Sharifymoghaddam, Yanxi Li, Haoran Hong, Xinyu Shi, Xuye Liu, Nandan Thakur, Crystina Zhang, Luyu Gao, Wenhu Chen, Jimmy Lin
    - 🏛️ Institutions: University of Waterloo, CSIRO, Independent, Carnegie Mellon University, The University of Queensland
    - 📅 Date: August 08, 2025
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [benchmark], [dataset], [agentic search], [deep research], [BrowseComp-plus]
    - 📖 TLDR: Introduces **BrowseComp-Plus**, a fixed-corpus benchmark for evaluating deep-research agents. It enables controlled, fair, and transparent comparisons by providing human-verified supporting and challenging negative documents for each query. Results reveal significant performance variation—for example, an open-source model (Search-R1 + BM25) only achieves 3.86% accuracy, while GPT-5 reaches 55.9%, and GPT-5 with Qwen3-Embedding-8B retriever achieves 70.1% with fewer queries—highlighting the critical importance of retrieval quality and enabling disentangled analysis of retrieval vs. reasoning components.

- [MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers](https://arxiv.org/abs/2508.14704)
    - Ziyang Luo, Zhiqi Shen, Wenzhuo Yang, Zirui Zhao, Prathyusha Jwalapuram, Amrita Saha, Doyen Sahoo, Silvio Savarese, Caiming Xiong, Junnan Li
    - 🏛️ Institutions: Salesforce AI Research
    - 📅 Date: August 20, 2025
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [benchmark], [dataset], [framework], [long-horizon reasoning], [unknown-tools challenge], [execution-based evaluation], [MCP-universe]
    - 📖 TLDR: MCP-Universe introduces the first comprehensive benchmark for evaluating large language models (LLMs) through interactions with real-world Model Context Protocol (MCP) servers. It spans six core domains—Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, and Web Searching—across 11 MCP servers. The benchmark employs execution-based evaluators (format, static, dynamic) to rigorously assess agent performance. Despite progress, state-of-the-art models like GPT-5 (43.72% success), Grok-4 (33.33%), and Claude-4.0-Sonnet (29.44%) show significant limitations. The benchmark highlights challenges in long-context reasoning and unfamiliar tool handling, and provides an open-source extensible evaluation framework with UI support to accelerate future research.

- [Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training](https://arxiv.org/abs/2508.00414)
    - Tianqing Fang, Zhisong Zhang, Xiaoyang Wang, Rui Wang, Can Qin, Yuxuan Wan, Jun-Yu Ma, Ce Zhang, Jiaqi Chen, Xiyun Li, Hongming Zhang, Haitao Mi, Dong Yu
    - 🏛️ Institutions: Tencent AI Lab
    - 📅 Date: August 01, 2025
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [framework], [dataset], [model], [deep research], [reflection], [voting], [agent foundation models]
    - 📖 TLDR: This work introduces **Cognitive Kernel-Pro**, a fully open-source, multi-module agent framework designed to democratize advanced AI agent development. It curates high-quality training data across four domains—web, files, code, and general reasoning—and introduces test-time strategies like reflection and voting to enhance robustness. Evaluated on the GAIA benchmark, its open 8B-parameter model outperforms previous open-source agents such as WebDancer and WebSailor, setting a new performance standard. Code is publicly available.

- [Talk to Your Slides: High-Efficiency Slide Editing via Language-Driven Structured Data Manipulation](https://arxiv.org/abs/2505.11604)
    - Kyudan Jung, Hojun Cho, Jooyeol Yun, Soyoung Yang, Jaehyeok Jang, Jaegul Choo
    - 🏛️ Institutions: Chung-ang University, KAIST AI
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [benchmark], [structured data manipulation], [slide editing], [object model editing], [TSBench]
    - 📖 TLDR: Talk to Your Slides targets slide editing through language-driven manipulation of the underlying document object model rather than GUI-native visual interaction. It is relevant to GUI work because it compares against GUI-based baselines and introduces the TSBench benchmark, but its primary interaction mechanism is structured document editing rather than direct GUI control.

- [Language Agents: Foundations, Prospects, and Risks](https://aclanthology.org/2024.emnlp-tutorials.3/)
    - Yu Su, Diyi Yang, Shunyu Yao, Tao Yu
    - 🏛️ Institutions: The Ohio State University, Stanford University, Princeton University, The University of Hong Kong
    - 📅 Date: November 30, 2024
    - 📑 Publisher: EMNLP 2024 Tutorial Abstracts
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [survey], [tutorial], [reasoning], [planning], [memory], [multi-agent systems], [safety]
    - 📖 TLDR: This tutorial provides a comprehensive exploration of language agents—autonomous systems powered by large language models capable of executing complex tasks through language instructions. It delves into their theoretical foundations, potential applications, associated risks, and future directions, covering topics such as reasoning, memory, planning, tool augmentation, grounding, multi-agent systems, and safety considerations.

- [MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a2c3c86679300047c740c9900f19ddac-Abstract-Conference.html)
    - Haotian Zhang, Mingfei Gao, Zhe Gan, Philipp Dufter, Nina Wenzel, Forrest Huang, Dhruti Shah, Xianzhi Du, Bowen Zhang, Yanghao Li, Sam Dodge, Keen You, Zhen Yang, Aleksei Timofeev, Mingze Xu, Hong-You Chen, Jean-Philippe Fauconnier, Zhengfeng Lai, Haoxuan You, Zirui Wang, Afshin Dehghan, Peter Grasch, Yinfei Yang
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [model], [MM1.5], [vision language model], [visual grounding], [reasoning], [data-centric], [analysis]
    - 📖 TLDR: This paper introduces MM1.5, a family of multimodal large language models (MLLMs) ranging from 1B to 30B parameters, including dense and mixture-of-experts variants. MM1.5 enhances capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning. The authors employ a data-centric training approach, utilizing high-quality OCR data and synthetic captions for continual pre-training, alongside an optimized visual instruction-tuning data mixture for supervised fine-tuning. Specialized variants, MM1.5-Video and MM1.5-UI, are designed for video understanding and mobile UI comprehension, respectively. Extensive empirical studies provide insights into the training processes, offering guidance for future MLLM development.

- [Caution for the Environment: Multimodal LLM Agents are Susceptible to Environmental Distractions](https://aclanthology.org/2025.acl-long.1087/)
    - Xinbei Ma, Yiting Wang, Yao Yao, Tongxin Yuan, Aston Zhang, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University, Meta
    - 📅 Date: August 05, 2024
    - 📑 Publisher: ACL 2025
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [safety], [robustness], [environmental distraction], [multimodal LLM agent]
    - 📖 TLDR: This paper highlights the vulnerability of multimodal agents to environmental distractions. The researchers demonstrate that these agents, which process multiple types of input (e.g., text, images, audio), can be significantly impacted by irrelevant or misleading environmental cues. The study provides insights into the limitations of current multimodal systems and emphasizes the need for more robust architectures that can filter out distractions and maintain focus on relevant information in complex, real-world environments.

- [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://openreview.net/forum?id=xgtXkyqw1f)
    - Zehui Chen, Kuikun Liu, Qiuchen Wang, Jiangning Liu, Wenwei Zhang, Kai Chen, Feng Zhao
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory
    - 📅 Date: July 29, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [framework], [information seeking], [planning], [AI search], [MindSearch]
    - 📖 TLDR: This paper presents MindSearch, a novel approach to web information seeking and integration that mimics human cognitive processes. The system uses a multi-agent framework consisting of a WebPlanner and WebSearcher. The WebPlanner models multi-step information seeking as a dynamic graph construction process, decomposing complex queries into sub-questions. The WebSearcher performs hierarchical information retrieval for each sub-question. MindSearch demonstrates significant improvements in response quality and depth compared to existing AI search solutions, processing information from over 300 web pages in just 3 minutes.

- [Octo-planner: On-device Language Model for Planner-Action Agents](https://arxiv.org/abs/2406.18082)
    - Nexa AI Team
    - 🏛️ Institutions: Nexa AI
    - 📅 Date: June 26, 2024
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [model], [planner-action framework], [Octo-planner], [on-device planning]
    - 📖 TLDR: Presents Octo-planner, an on-device planner for a planner-action agent framework that separates task decomposition from action execution. Built on Phi-3 Mini and paired with an Octopus action model, it targets low-latency planning and execution on resource-constrained devices.

- [Enhancing Mobile "How-to" Queries with Automated Search Results Verification and Reranking](https://arxiv.org/abs/2404.08860)
    - Lei Ding, Jeshwanth Bheemanpally, Yi Zhang
    - 🏛️ Institutions: University of California, Santa Cruz
    - 📅 Date: April 13, 2024
    - 📑 Publisher: SIGIR 2024
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [framework], [reranking], [verification], [technical support search], [instruction execution]
    - 📖 TLDR: Targets mobile "how-to" search by automatically executing step-by-step instructions from retrieved pages in a controlled Android environment and reranking results based on actual success. The paper frames this as a verification-driven ranking pipeline for technical-support search rather than a pure mobile-control benchmark.

- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://arxiv.org/abs/2402.10196)
    - Lingbo Mo, Zeyi Liao, Boyuan Zheng, Yu Su, Chaowei Xiao, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of Wisconsin-Madison
    - 📅 Date: February 15, 2024
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [safety], [adversarial attacks], [security risks], [language agents], [perception-brain-action]
    - 📖 TLDR: Maps adversarial attacks on language agents through a Perception-Brain-Action decomposition and surveys 12 attack types across those layers. The paper is mainly a threat-modeling taxonomy, useful as a security lens for later web and computer-use agents.

- [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, ByteDance
    - 📅 Date: January 01, 2024
    - 📑 Publisher: ICLR 2024
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [benchmark], [evaluation], [multi-environment agents], [AgentBench]
    - 📖 TLDR: Introduces AgentBench, a broad benchmark suite for evaluating LLMs as agents across eight environments, including but not limited to OS interaction. It belongs in this repo mainly as a general agent-evaluation reference rather than a pure GUI benchmark.

- [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25ae35b5b1738d80f1f03a8713e405ec-Abstract-Conference.html)
    - Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, Thomas Scialom
    - 🏛️ Institutions: Meta AI, Hugging Face, AutoGPT
    - 📅 Date: November 21, 2023
    - 📑 Publisher: ICLR 2024
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [benchmark], [multi-modality], [tool use], [reasoning]
    - 📖 TLDR: GAIA is a benchmark developed for evaluating general-purpose AI assistants. It aims to test assistant models across multiple modalities and complex reasoning tasks in real-world settings, including scenarios that require tool usage and open-ended question answering. With a dataset comprising 466 questions across various domains, GAIA highlights gaps between current AI performance and human capability, presenting a significant challenge for large language models such as GPT-4.

- [Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V](https://arxiv.org/abs/2310.11441)
    - Jianwei Yang, Hao Zhang, Feng Li, Xueyan Zou, Chunyuan Li, Jianfeng Gao
    - 🏛️ Institutions: Microsoft Research
    - 📅 Date: October 17, 2023
    - 📑 Publisher: arXiv
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [visual prompting], [Set-of-Mark], [visual grounding], [zero-shot], [region marking]
    - 📖 TLDR: Introduces Set-of-Mark prompting, where segmented image regions are overlaid with explicit marks before being passed to a multimodal model. The paper shows that simple region marking can unlock much stronger zero-shot grounding from GPT-4V without fine-tuning.

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)
    - Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
    - 🏛️ Institutions: Northeastern University, Massachusetts Institute of Technology, Princeton University
    - 📅 Date: March 20, 2023
    - 📑 Publisher: NeurIPS 2023
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [framework], [learning], [verbal reinforcement learning], [reflexion]
    - 📖 TLDR: Introduces Reflexion, a framework where language agents learn from feedback by writing verbal reflections into episodic memory instead of updating model weights. The method is broad rather than GUI-specific, but it matters here because many later web and computer-use agents inherit its reflection-and-memory pattern.

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://openreview.net/forum?id=WE_vluYUL-X)
    - Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
    - 🏛️ Institutions: Princeton University, Google Research
    - 📅 Date: October 06, 2022
    - 📑 Publisher: ICLR 2023
    - 📌 Relation: Adjacent to GUI research (not part of the canonical direct-GUI main list)
    - 🔑 Key: [framework], [reasoning], [ReAct]
    - 📖 TLDR: Introduces ReAct, the now-standard prompting pattern that interleaves reasoning traces with actions. It is not a GUI paper, but it is foundational because many later web and computer-use agents build directly on this reasoning-action decomposition.
