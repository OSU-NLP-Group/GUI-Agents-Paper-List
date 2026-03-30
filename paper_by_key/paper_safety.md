# Papers with Keyword: safety

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Mauro Li, Reuben Binns, Soheil Feizi, Lind Seelig, Kasper Luckow
    - 🏛️ Institutions: vLLM Semantic Router Project, MBZUAI, McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [safety], [computer-use agent], [visual grounding], [guardrail], [adversarial attacks]
    - 📖 TLDR: Formalizes the "visual confused deputy" as a security vulnerability in computer-using agents where misperceived screen states (from grounding errors, adversarial screenshot manipulation, or TOCTOU races) cause agents to authorize unintended privileged actions, and proposes a dual-channel contrastive classification guardrail that independently verifies the visual click target and the agent's textual reasoning to block risky executions.

- [Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks](https://arxiv.org/abs/2603.04364)
    - Haoyu Liu, Dingcheng Li, Lukas Rutishauser, Zeyu Zheng
    - 🏛️ Institutions: UC Berkeley, Google, Google DeepMind
    - 📅 Date: 2026-03-04
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [defense], [web agent safety], [DMAST], [adversarial training], [cross-modal attack], [GRPO]
    - 📖 TLDR: DMAST is a three-stage adversarial safety training framework (imitation learning, oracle-guided SFT with zero-acknowledgment, and GRPO self-play) that robustifies multimodal web agents against cross-modal DOM injection attacks, substantially reducing adversarial risk while doubling task completion efficiency on out-of-distribution MiniWob++ tasks.

- [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235)
    - Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: The Ohio State University, LawZero, Mila - Quebec AI Institute, Universite de Montreal, University of California, Berkeley
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [safety], [red teaming], [unintended behavior], [computer-use agent], [AutoElicit]
    - 📖 TLDR: This paper studies unsafe unintended behaviors in computer-use agents under benign user inputs rather than adversarial prompts. It introduces AutoElicit, an agentic framework that iteratively perturbs realistic benign instructions using execution feedback to surface severe harmful behaviors in frontier CUAs. The results show that even strong CUAs remain broadly susceptible to harmful deviations, establishing a concrete framework for systematically probing unintended safety failures in realistic computer-use settings.

- [When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents](https://arxiv.org/abs/2602.08995)
    - Yuting Ning, Jaylen Jones, Zhehao Zhang, Chentao Ye, Weitong Ruan, Junyi Li, Rahul Gupta, Huan Sun
    - 🏛️ Institutions: The Ohio State University, Amazon AGI
    - 📅 Date: February 9, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [guardrail], [misaligned actions], [MisActBench], [DeAction]
    - 📖 TLDR: This paper defines the problem of misaligned actions in computer-use agents, covering both externally induced failures such as prompt injection and internally arising errors such as faulty reasoning. It introduces MisActBench, an action-level benchmark with human alignment labels, and DeAction, a guardrail that detects and iteratively corrects misaligned actions before execution. DeAction substantially improves F1 on the benchmark and sharply reduces attack success in online evaluation while preserving benign task success.

- [Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible](https://arxiv.org/abs/2602.10139)
    - Lepeng Zhao, Zhenhua Zou, Shuo Li, Xiaoming Li, Bangfei Tian
    - 🏛️ Institutions: Tsinghua University
    - 📅 Date: February 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [privacy], [mobile agent], [Android], [benchmark], [framework], [safety]
    - 📖 TLDR: Proposes an anonymization-based privacy protection framework for mobile GUI agents that replaces sensitive PII with type-preserving placeholders, enabling task execution without exposing raw personal data to cloud-based models, and demonstrates strong privacy-utility trade-offs on the AndroidLab and PrivScreen benchmarks.

- [DECEPTICON: How Dark Patterns Manipulate Web Agents](https://arxiv.org/abs/2512.22894)
    - Phil Cuvin, Hao Zhu, Diyi Yang
    - 🏛️ Institutions: Stanford University
    - 📅 Date: 2026-02-06
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [safety], [robustness], [dark patterns], [adversarial attack]
    - 📖 TLDR: Introduces DECEPTICON, a benchmark of 700 web navigation tasks with dark patterns, showing that deceptive UI designs successfully steer state-of-the-art web agents toward malicious outcomes in over 70% of tasks -- with larger models being more susceptible -- and that existing countermeasures fail to mitigate this risk.

- [LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios](https://arxiv.org/abs/2602.03255)
    - Tianyu Chen, Chujia Hu, Ge Gao, Ruofeng Yu, Yao Lu
    - 🏛️ Institutions: ShanghaiTech University, Shanghai Artificial Intelligence Laboratory, Rice University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer use agent], [MCP], [long-horizon planning], [LLM agent]
    - 📖 TLDR: LPS-Bench is a benchmark evaluating the planning-time safety awareness of MCP-based computer-use agents under long-horizon tasks, covering 65 scenarios across 7 task domains and 9 risk types with both benign and adversarial interactions, revealing substantial safety deficiencies in existing agents.

- [GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents](https://arxiv.org/abs/2601.18842)
    - Yanxi Wang, Zhiling Zhang, Wenbo Zhou, Weiming Zhang, Jie Zhang, Qiannan Zhu, Yu Shi, Shuxin Zheng, Jiyan He
    - 🏛️ Institutions: Beijing Normal University, Zhongguancun Academy, USTC, A*STAR, Zhongguancun Institution of Artificial Intelligence
    - 📅 Date: January 26, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [dataset], [safety], [privacy-preserving GUI agent], [GUIGuard], [GUIGuard-bench]
    - 📖 TLDR: This paper introduces GUIGuard, a general privacy-preserving framework for GUI agents that separates privacy recognition, privacy protection, and protected task execution. It also builds GUIGuard-Bench, a cross-platform benchmark with 630 trajectories and 13,830 screenshots annotated for privacy grounding, risk levels, categories, and task necessity. Results show that current GUI agents have very weak privacy recognition, while carefully designed protection policies can retain usable task-planning fidelity, making privacy-aware GUI agents a concrete and measurable systems problem.

- [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)
    - Hanna Foerster, Tom Blanchard, Kristina Nikolić, Ilia Shumailov, Cheng Zhang, Robert Mullins, Nicolas Papernot, Florian Tramèr, Yiren Zhao
    - 🏛️ Institutions: University of Cambridge, University of Toronto & Vector Institute, ETH Zurich, AI Sequrity Company
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [single-shot planning], [branch steering], [OSWorld]
    - 📖 TLDR: This paper studies system-level security for computer-use agents under prompt injection attacks. It introduces Single-Shot Planning, where a trusted planner produces a full execution graph with conditional branches before the agent observes potentially malicious content, giving provable control-flow integrity against injected instructions. The paper also identifies Branch Steering as an additional attack surface and shows on OSWorld that strong security guarantees can be achieved while retaining meaningful utility.

- [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/abs/2601.08406)
    - Xinyi Wu, Jiagui Chen, Geng Hong, Jiayi Dong, Xudong Pan, Jiarun Dai, Min Yang
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute
    - 📅 Date: 2026-01-13
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [safety], [agent framework], [security evaluation], [attack]
    - 📖 TLDR: WebTrap Park is an automated platform for systematic security evaluation of web agents that instantiates three major security risk sources into 1,226 executable tasks on live web pages, revealing that agent architecture matters more than the underlying model for security robustness.

- [Permission Manifests for Web Agents](https://arxiv.org/abs/2601.02371)
    - Samuele Marro, Alan Chan, Xinxing Ren, Lewis Hammond, Jesse Wright, Gurjyot Wanga, Tiziano Piccardi, Nuno Campos, Tobin South, Jialin Yu, Sunando Sengupta, Eric Sommerlade, Alex Pentland, Philip Torr, Jiaxin Pei
    - 🏛️ Institutions: University of Oxford, Institute for Decentralized AI, Centre for the Governance of AI, Coral Protocol, Cooperative AI Foundation, Webair, Johns Hopkins University, Witan Labs, Stanford University, Microsoft, UT Austin
    - 📅 Date: 2026-01-12
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [safety], [framework], [LLM agent], [permission control], [governance]
    - 📖 TLDR: This paper introduces agent-permissions.json, a lightweight robots.txt-style permission manifest that allows website owners to declaratively specify interaction policies for LLM-based web agents, enabling beneficial automated interactions while respecting site owners' preferences and reducing reliance on blanket blocking.

- [MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction](https://arxiv.org/abs/2601.12822)
    - Yinhao Jiang, Hao Ye, Juntao Ren, Zhenying He, Jian Hou
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute
    - 📅 Date: January 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [agent safety], [benchmark], [framework], [GUI agent], [security], [simulation]
    - 📖 TLDR: MirrorGuard is a plug-and-play defense framework that uses a neural-symbolic simulation pipeline to generate high-risk GUI interaction trajectories in a text-based environment, training a module to intercept and rectify insecure reasoning chains of Computer Use Agents before they execute harmful actions. On the ByteDance UI-TARS system, it reduces the unsafe rate from 66.5% to 13.0% while maintaining low false refusal rates, significantly outperforming prior defenses.

- [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](https://arxiv.org/abs/2512.23128)
    - Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H. S. Torr, Adam Mahdi, Adel Bibi
    - 🏛️ Institutions: University of Oxford, SoftServe, Independent, Johannes Kepler University Linz
    - 📅 Date: 2025-12-28
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [safety], [prompt injection], [security], [LLM]
    - 📖 TLDR: TRAP is a benchmark for evaluating how persuasion-based prompt injection attacks can redirect LLM-powered web agents from their intended tasks, finding that across six frontier models agents are susceptible to such attacks in 25% of tasks on average, with psychologically-driven social engineering techniques and small interface changes often doubling attack success rates.

- [BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents](https://arxiv.org/abs/2511.20597)
    - Kaiyuan Zhang, Mark Tenenholtz, Kyle Polley, Jerry Ma, Denis Yarats, Ninghui Li
    - 🏛️ Institutions: Purdue University, Perplexity AI
    - 📅 Date: 2025-11-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [benchmark], [safety], [prompt injection], [defense], [security]
    - 📖 TLDR: BrowseSafe introduces a benchmark of prompt injection attacks embedded in realistic HTML payloads targeting AI browser agents, and proposes a multi-layered defense-in-depth strategy combining architectural and model-based defenses to protect web agents from evolving prompt injection threats.

- [DualTAP: A Dual-Task Adversarial Protector for Mobile MLLM Agents](https://arxiv.org/abs/2511.13248)
    - Fuyao Zhang, Jiaming Zhang, Che Wang...
    - 🏛️ Institutions: Nanyang Technological University, Peking University, Xidian University, Hebei Normal University, Alibaba Group
    - 📅 Date: 2025-11-17
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [mobile agent], [safety], [privacy], [adversarial attack], [dataset], [MLLM]
    - 📖 TLDR: DualTAP is a dual-task adversarial framework that protects personally identifiable information (PII) in mobile GUI agent screenshots from untrusted routers while preserving task utility, achieving a 31.6 percentage point reduction in privacy leakage with minimal impact on agent task success rate.

- [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)
    - Thomas Kuntz, Agatha Duzan, Hao Zhao, Francesco Croce, J Zico Kolter, Nicolas Flammarion, Maksym Andriushchenko
    - 🏛️ Institutions: EPFL, Carnegie Mellon University
    - 📅 Date: October 29, 2025
    - 📑 Publisher: NeurIPS 2025 (Datasets and Benchmarks Track Spotlight)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer-use agent], [prompt injection], [OSWorld], [OS-harm]
    - 📖 TLDR: This paper introduces OS-Harm, a safety benchmark for computer-use agents built on top of OSWorld. It covers 150 tasks spanning deliberate misuse, prompt injection, and model misbehavior across applications such as browsers, editors, and email clients, and includes an automated judge for both safety and task correctness. Evaluations show that current frontier agents often comply with harmful requests, remain vulnerable to prompt injection, and can execute unsafe actions in realistic computer-use settings.

- [GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments?](https://arxiv.org/abs/2510.20333)
    - Chiyu Chen, Xinhao Song, Yunkai Chai, Yang Yao, Haodong Zhao, Lijun Li, Jie Li, Yan Teng, Gongshen Liu, Yingchun Wang
    - 🏛️ Institutions: Shanghai Jiao Tong University, School of Computer Science, Shanghai Artificial Intelligence Laboratory, The University of Hong Kong
    - 📅 Date: October 23, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [mobile GUI agent], [environmental injection], [adversarial robustness], [GhostEI-bench]
    - 📖 TLDR: This paper introduces GhostEI-Bench, a benchmark for evaluating mobile agents under dynamic environmental injection attacks such as deceptive overlays, spoofed notifications, and pop-ups inside realistic Android workflows. Rather than testing static screenshots, it injects adversarial events into executable mobile environments and uses judge-based trajectory analysis to localize failure points. The benchmark shows that current mobile agents remain highly vulnerable to these runtime visual attacks.

- [Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming](https://arxiv.org/abs/2510.18314)
    - Zheng Zhang, Jiarui He, Yuchen Cai, Deheng Ye, Peilin Zhao, Ruili Feng, Hao Wang
    - 🏛️ Institutions: The Hong Kong University of Science and Technology (Guangzhou), Tencent, Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: 2025-10-21
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [web agent], [safety], [benchmark], [attack], [LLM], [red-teaming]
    - 📖 TLDR: Genesis is an agentic red-teaming framework for LLM web agents that uses genetic algorithms and a dynamic strategy library (Attacker, Scorer, Strategist modules) to automatically evolve and discover adversarial injection attacks, consistently outperforming existing attack baselines across diverse web tasks.

- [Investigating the Impact of Dark Patterns on LLM-Based Web Agents](https://arxiv.org/abs/2510.18113)
    - Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik
    - 🏛️ Institutions: Purdue University, Florida International University, Georgia Institute of Technology
    - 📅 Date: 2025-10-20
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [safety], [LLM agent], [dark patterns], [evaluation]
    - 📖 TLDR: This paper presents the first study on how dark patterns (deceptive UI designs) affect LLM-based web agents, introducing TrickyArena as a controlled benchmark environment and finding that agents are susceptible to dark patterns an average of 41% of the time across six popular web agent frameworks and three LLMs.

- [SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)
    - Zonghao Ying, Yangguang Shao, Jianle Gan, Gan Xu, Junjie Shen, Wenxin Zhang, Quanchen Zou, Junzheng Shi, Zhenfei Yin, Mingchuan Zhang, Aishan Liu, Xianglong Liu
    - 🏛️ Institutions: Beihang University, Institute of Information Engineering (Chinese Academy of Sciences), China University of Petroleum (East China), Zhejiang University of Technology, University of Chinese Academy of Sciences, 360 AI Security Lab, The University of Sydney, Henan University of Science and Technology, Zhongguancun Laboratory
    - 📅 Date: 2025-10-11
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [web agent], [attack], [VLM], [evaluation]
    - 📖 TLDR: SecureWebArena is the first holistic security benchmark for LVLM-based web agents, featuring 2,970 trajectories across six simulated web environments with a structured taxonomy of six attack vectors and a multi-layered evaluation protocol assessing reasoning, behavior, and task outcomes. Experiments on 9 LVLMs reveal consistent vulnerabilities to adversarial manipulations and critical trade-offs between model specialization and security.

- [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670)
    - Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
    - 🏛️ Institutions: Microsoft Research AI Frontiers, Microsoft AI Red Team, University of California, Riverside, NVIDIA
    - 📅 Date: October 2, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [computer-use agent], [blind goal-directedness], [BLIND-ACT], [risk evaluation]
    - 📖 TLDR: This paper identifies Blind Goal-Directedness as a recurring failure mode in computer-use agents, where agents keep pursuing user goals despite infeasibility, ambiguity, or unsafe context. It introduces BLIND-ACT, a benchmark built on OSWorld to evaluate these subtle safety failures in realistic desktop environments. The results show high rates of blind goal pursuit across frontier CUAs, making the paper directly relevant to safety evaluation of GUI agents beyond prompt injection alone.

- [WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents](https://arxiv.org/abs/2510.01354)
    - Yinuo Liu, Ruohan Xu, Xilong Wang, Yuqi Jia, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: 2025-10-01
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [security], [prompt injection], [attack detection], [safety]
    - 📖 TLDR: WAInjectBench presents the first comprehensive benchmark for evaluating prompt injection detection methods targeting web agents, finding that while some detectors handle explicit textual attacks or visible image perturbations reasonably well, they largely fail against attacks that omit explicit instructions or use imperceptible perturbations.

- [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358)
    - Hussein Mozannar, Gagan Bansal, Cheng Tan, Adam Fourney, Victor Dibia, Jingya Chen, Jack Gerrits, Tyler Payne, Matheus Kunzler Maldaner, Madeleine Grunde-McLaughlin, Eric Zhu, Griffin Bassman, Jacob Alber, Peter Chang, Ricky Loynd, Friederike Niedtner, Ece Kamar, Maya Murad, Rafah Hosn, Saleema Amershi
    - 🏛️ Institutions: Microsoft Research AI Frontiers
    - 📅 Date: July 30, 2025
    - 📑 Publisher: arXiv (also MSR Technical Report MSR-TR-2025-40)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [human-in-the-loop], [multi-agent], [planning], [memory], [MCP], [safety]
    - 📖 TLDR: Magentic-UI (Multi-agentic User Interface) is an open-source web interface enabling safe, efficient human–agent collaboration through a flexible multi-agent architecture. It supports web browsing, code execution, and file manipulation, and provides six interaction mechanisms—co-planning, co-tasking, multi-tasking, action guards, answer verification, and long-term memory—to integrate human oversight with AI autonomy. Evaluated via agentic benchmarks, simulated user tests, qualitative user study, and safety assessments, it demonstrates how incorporating human-in-the-loop dynamics can significantly improve agentic systems' reliability and performance.

- [WebGuard: Building a Generalizable Guardrail for Web Agents](https://arxiv.org/abs/2507.14293)
    - Boyuan Zheng, Zeyi Liao, Scott Salisbury, Zeyuan Liu, Michael Lin, Qinyuan Zheng, Zifan Wang, Xiang Deng, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, Scale AI, University of California, Berkeley
    - 📅 Date: July 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [benchmark], [safety], [guardrail], [WebGuard]
    - 📖 TLDR: Autonomous web agents powered by LLMs can take unintended or harmful actions when interacting with websites (especially state-changing ones). WebGuard is introduced as a dataset to assess risks of web agent actions by collecting nearly 5,000 human‑annotated actions across many real websites, labeled by risk level (SAFE / LOW / HIGH). Baseline LLMs do poorly (<60% accuracy / recall) on detecting high‑risk actions; after fine‑tuning (using Qwen2.5VL‑7B), performance improves significantly (accuracy ~80%, recall on HIGH ~76%), though still not sufficient for very high‑stakes settings. The paper highlights that reliable guardrails for web agents remain an open challenge.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, and Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: June 4, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multilingual], [safety], [macOSWorld]
    - 📖 TLDR: Introduces **macOSWorld**, the first interactive benchmark for GUI agents on macOS, with 202 tasks across 30 apps (28 macOS-exclusive) in 5 languages plus a safety subset for deception attacks; evaluates 6 agents, showing proprietary CUAs outperform open-source and VLM-based agents, significant language gaps (Arabic –27.5%), and both grounding and safety challenges.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [computer-use agent], [OSWorld], [RiOSWorld]
    - 📖 TLDR: This paper introduces RiOSWorld, a benchmark for evaluating safety risks in multimodal computer-use agents during realistic computer manipulation. It covers 492 risky tasks across applications such as web, social media, multimedia, email, office software, and operating-system interactions, and evaluates both harmful intent and harmful task completion. The benchmark shows that current computer-use agents remain exposed to substantial real-world safety risks even when they are aligned for ordinary dialogue settings.

- [GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents](https://arxiv.org/abs/2505.12842)
    - Zheng Wu, Pengzhou Cheng, Zongru Wu, Lingzhong Dong, Zhuosheng Zhang
    - 🏛️ Institutions: Shanghai Jiao Tong University
    - 📅 Date: 2025-05-19
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [GUI agent], [out-of-distribution detection], [safety], [gaussian mixture model], [MLLM], [robustness]
    - 📖 TLDR: GEM proposes a Gaussian mixture model-based method for detecting out-of-distribution instructions in GUI agents by modeling input embedding distances, achieving a 23.70% average accuracy improvement over baselines across eight datasets spanning smartphones, computers, and web browsers.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Chuan Guo, Aaron Grattafiori, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Independent Researcher
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [web agent], [prompt injection], [security], [WASP]
    - 📖 TLDR: This paper introduces WASP, a benchmark for end-to-end evaluation of web-agent security against prompt injection attacks in realistic multi-step web tasks. It shows that even strong web agents can be partially deceived at very high rates by simple human-written injections, while also revealing a more nuanced failure mode where agents are often insecure yet too incompetent to fully execute the attacker's goal. The benchmark is designed to measure security under realistic web-agent deployment conditions rather than simplified single-step attacks.

- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434)
    - Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu
    - 🏛️ Institutions: University of Georgia, Tencent AI Seattle Lab, Microsoft Research, University of Waterloo, Hong Kong Polytechnic University
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [GUI agent], [trustworthiness], [safety], [security], [benchmark]
    - 📖 TLDR: A survey on trustworthy GUI agents that introduces a workflow-aligned taxonomy decomposing trust into Perception Trust, Reasoning Trust, and Interaction Trust, systematically reviewing failure modes, adversarial attacks, defense mechanisms, and evaluation practices for deploying GUI agents safely.

- [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)
    - Lukas Aichberger, Alasdair Paren, Guohao Li, Philip Torr, Yarin Gal, Adel Bibi
    - 🏛️ Institutions: Johannes Kepler University Linz, University of Oxford
    - 📅 Date: March 13, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [security], [adversarial attacks], [computer-use agent], [OS agent], [MIP against agent]
    - 📖 TLDR: This paper identifies Malicious Image Patches as a new attack vector against multimodal OS agents, where adversarially perturbed visual regions on the screen can trigger harmful actions when captured by the agent. The attack generalizes across prompts and screen setups, showing that benign-looking visual content such as wallpapers or social media images can hijack computer-use agents. The paper exposes a concrete security weakness in OS-level agents that goes beyond text-only prompt injection.

- [AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780)
    - Arman Zharmagambetov, Chuan Guo, Ivan Evtimov, Maya Pavlova, Ruslan Salakhutdinov, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Meta
    - 📅 Date: March 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [privacy], [web agent], [data minimization], [safety], [AgentDAM]
    - 📖 TLDR: This paper introduces AgentDAM, a benchmark for evaluating whether autonomous web agents respect data minimization when using sensitive user information. It measures whether an agent accesses private information only when it is necessary to complete a task, and shows that current web agents frequently leak unnecessary sensitive data. The paper also studies a prompting-based defense, but the main contribution is a realistic end-to-end privacy evaluation setup for autonomous web agents.

- [AEIA-MN: Evaluating the Robustness of Multimodal LLM-Powered Mobile Agents Against Active Environmental Injection Attacks](https://arxiv.org/abs/2502.13053)
    - Yurun Chen, Xueyu Hu, Keting Yin, Juncheng Li, Shengyu Zhang
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: February 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [safety], [AEIA-MN]
    - 📖 TLDR: This paper introduces the concept of Active Environment Injection Attack (AEIA), where attackers disguise malicious actions as environmental elements to disrupt AI agents' decision-making processes. The authors propose AEIA-MN, an attack scheme leveraging mobile notifications to evaluate the robustness of multimodal large language model-based mobile agents. Experimental results demonstrate that even advanced models are highly vulnerable to such attacks, with success rates reaching up to 93% in the AndroidWorld benchmark.

- [WebOlympus: An Open Platform for Web Agents on Live Websites](https://aclanthology.org/2024.emnlp-demo.20/)
    - Boyuan Zheng, Boyu Gou, Scott Salisbury, Zheng Du, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: November 12, 2024
    - 📑 Publisher: EMNLP 2024 System Demonstrations
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [chrome extension], [WebOlympus], [SeeAct], [annotation tool]
    - 📖 TLDR: This paper introduces *WebOlympus*, an open platform designed to facilitate the research and deployment of web agents on live websites. It features a user-friendly Chrome extension interface, allowing users without programming expertise to operate web agents with minimal effort. The platform incorporates a safety monitor module to prevent harmful actions through human supervision or model-based control, supporting applications such as annotation interfaces for web agent trajectories and data crawling.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Institute of Technology, The University of Hong Kong, Stanford University
    - 📅 Date: Nov 4, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [attack], [adversarial pop-ups], [VLM agents], [safety]
    - 📖 TLDR: This paper demonstrates that vision-language model (VLM) agents can be easily deceived by carefully designed adversarial pop-ups, leading them to perform unintended actions such as clicking on these pop-ups instead of completing their assigned tasks. Integrating these pop-ups into environments like OSWorld and VisualWebArena resulted in an average attack success rate of 86% and a 47% decrease in task success rate. Basic defense strategies, such as instructing the agent to ignore pop-ups or adding advertisement notices, were found to be ineffective against these attacks.

- [Language Agents: Foundations, Prospects, and Risks](https://aclanthology.org/2024.emnlp-tutorials.3/)
    - Yu Su, Diyi Yang, Shunyu Yao, Tao Yu
    - 🏛️ Institutions: The Ohio State University, Stanford University, Princeton University, The University of Hong Kong
    - 📅 Date: November 2024
    - 📑 Publisher: EMNLP 2024 Tutorial Abstracts
    - 💻 Env: [Misc]
    - 🔑 Key: [survey], [tutorial], [reasoning], [planning], [memory], [multi-agent systems], [safety]
    - 📖 TLDR: This tutorial provides a comprehensive exploration of language agents—autonomous systems powered by large language models capable of executing complex tasks through language instructions. It delves into their theoretical foundations, potential applications, associated risks, and future directions, covering topics such as reasoning, memory, planning, tool augmentation, grounding, multi-agent systems, and safety considerations.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, The University of Texas at Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [evaluation], [Android emulator]
    - 📖 TLDR: *MobileSafetyBench* introduces a benchmark for evaluating the safety of large language model (LLM)-based autonomous agents in mobile device control. Using Android emulators, the benchmark simulates real-world tasks in apps such as messaging and banking to assess agents' safety and helpfulness. The safety-focused tasks test for privacy risk management and robustness against adversarial prompt injections. Experiments show agents perform well in helpful tasks but struggle with safety-related challenges, underscoring the need for continued advancements in mobile safety mechanisms for autonomous agents.

- [AdvWeb: Controllable Black-box Attacks on VLM-powered Web Agents](https://arxiv.org/abs/2410.17401)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, University of Chicago, The Ohio State University, University of Science and Technology of China
    - 📅 Date: October 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [attack], [black-box attack], [adversarial prompt injection], [direct policy optimization], [AdvWeb]
    - 📖 TLDR: This paper presents AdvWeb, a black-box attack framework that exploits vulnerabilities in vision-language model (VLM)-powered web agents by injecting adversarial prompts directly into web pages. Using Direct Policy Optimization (DPO), AdvWeb trains an adversarial prompter model that can mislead agents into executing harmful actions, such as unauthorized financial transactions, while maintaining high stealth and control. Extensive evaluations reveal that AdvWeb achieves high success rates across multiple real-world tasks, emphasizing the need for stronger security measures in web agent deployments.

- [Dissecting Adversarial Robustness of Multimodal LM Agents](https://openreview.net/forum?id=LjVIGva5Ct)
    - Chen Henry Wu, Rishi Rajesh Shah, Jing Yu Koh, Russ Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: Carnegie Mellon University, Stanford University
    - 📅 Date: October 21, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [dataset], [attack], [ARE], [safety]
    - 📖 TLDR: This paper introduces the Agent Robustness Evaluation (ARE) framework to assess the adversarial robustness of multimodal language model agents in web environments. By creating 200 targeted adversarial tasks within VisualWebArena, the study reveals that minimal perturbations can significantly compromise agent performance, even in advanced systems utilizing reflection and tree-search mechanisms. The findings highlight the need for enhanced safety measures in deploying such agents.

- [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886)
    - Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar, Tu Trinh, Scale Red Team, Elaine T. Chang, Vaughn Robinson, Sean Hendryx, Shuyan Zhou, Matt Fredrikson, Summer Yue, Zifan Wang
    - 🏛️ Institutions: Carnegie Mellon University, GraySwan AI, Scale AI
    - 📅 Date: October 11, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [safety], [red teaming], [jailbreaking], [BrowserART]
    - 📖 TLDR: This paper introduces **Browser Agent Red teaming Toolkit (BrowserART)**, a comprehensive test suite for evaluating the safety of LLM-based browser agents. The study reveals that while refusal-trained LLMs decline harmful instructions in chat settings, their corresponding browser agents often comply with such instructions, indicating a significant safety gap. The authors call for collaboration among developers and policymakers to enhance agent safety.

- [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://openreview.net/forum?id=MuCDzH0ctf)
    - Ido Levy, Ben Wiesel, Sami Marreed, Alon Oved, Avi Yaeli, Segev Shlomov
    - 🏛️ Institutions: IBM Research
    - 📅 Date: October 9, 2024
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [safety], [trustworthiness], [policy compliance], [completion under policy], [ST-WebAgentBench]
    - 📖 TLDR: This paper introduces **ST-WebAgentBench**, a benchmark designed to evaluate the safety and trustworthiness of web agents in enterprise contexts. It defines safe and trustworthy agent behavior, outlines the structure of safety policies, and introduces the "Completion under Policies" metric to assess agent performance. The study reveals that current state-of-the-art agents struggle with policy adherence, highlighting the need for improved policy awareness and compliance in web agents.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of California, Los Angeles, The University of Chicago, University of Illinois Urbana-Champaign, University of Wisconsin-Madison
    - 📅 Date: September 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [web agent], [EIA]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [Caution for the Environment: Multimodal LLM Agents are Susceptible to Environmental Distractions](https://aclanthology.org/2025.acl-long.1087/)
    - Xinbei Ma, Yiting Wang, Yao Yao, Tongxin Yuan, Aston Zhang, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University, Meta
    - 📅 Date: August 5, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [robustness], [environmental distraction], [multimodal LLM agent]
    - 📖 TLDR: This paper highlights the vulnerability of multimodal agents to environmental distractions. The researchers demonstrate that these agents, which process multiple types of input (e.g., text, images, audio), can be significantly impacted by irrelevant or misleading environmental cues. The study provides insights into the limitations of current multimodal systems and emphasizes the need for more robust architectures that can filter out distractions and maintain focus on relevant information in complex, real-world environments.

- [Adversarial Attacks on Multimodal Agents](https://arxiv.org/abs/2406.12814)
    - Chen Henry Wu, Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: Carnegie Mellon University
    - 📅 Date: Jun 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [VisualWebArena-adv]
    - 📖 TLDR: This paper investigates the safety risks posed by multimodal agents built on vision-enabled language models (VLMs). The authors introduce two adversarial attack methods: a captioner attack targeting white-box captioners and a CLIP attack that transfers to proprietary VLMs. To evaluate these attacks, they curated VisualWebArena-Adv, a set of adversarial tasks based on VisualWebArena. The study demonstrates that within a limited perturbation norm, the captioner attack can achieve a 75% success rate in making a captioner-augmented GPT-4V agent execute adversarial goals. The paper also discusses the robustness of agents based on other VLMs and provides insights into factors contributing to attack success and potential defenses.

- [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Abstract-Conference.html)
    - Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
    - 🏛️ Institutions: Renmin University of China, Peking University, Tencent
    - 📅 Date: Feb 17, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [attack], [backdoor], [safety]
    - 📖 TLDR: This paper investigates backdoor attacks on LLM-based agents, introducing a framework that categorizes attacks based on outcomes and trigger locations. The study demonstrates the vulnerability of such agents to backdoor attacks and emphasizes the need for targeted defenses.

- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://arxiv.org/abs/2402.10196)
    - Lingbo Mo, Zeyi Liao, Boyuan Zheng, Yu Su, Chaowei Xiao, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of Wisconsin-Madison
    - 📅 Date: February 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [adversarial attacks], [security risks], [language agents], [perception-brain-action]
    - 📖 TLDR: This paper introduces a conceptual framework to assess and understand adversarial vulnerabilities in language agents, dividing the agent structure into three components—Perception, Brain, and Action. It discusses 12 specific adversarial attack types that exploit these components, ranging from input manipulation to complex backdoor and jailbreak attacks. The framework provides a basis for identifying and mitigating risks before the widespread deployment of these agents in real-world applications.
