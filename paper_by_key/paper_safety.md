# Papers with Keyword: safety

- [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707)
    - Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
    - 🏛️ Institutions: McGill University, AMD, Red Hat
    - 📅 Date: March 16, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [security], [safety], [visual grounding], [guardrail], [adversarial attacks], [TOCTOU], [visual confused deputy]
    - 📖 TLDR: This paper reframes perception failures in GUI agents as a security problem rather than just a performance issue, formalizing the visual confused deputy where misperceived UI state causes privileged actions on the wrong target. It then proposes a dual-channel guardrail that separately checks the visual target and the agent's textual reasoning to block unsafe executions.

- [You Told Me to Do It: Measuring Instructional Text-induced Private Data Leakage in LLM Agents](https://arxiv.org/abs/2603.11862)
    - Ching-Yu Kao, Xinfeng Li, Shenyu Dai, Tianze Qiu, Pengcheng Zhou, Eric Hanchen Jiang, Philip Sperl
    - 🏛️ Institutions: Fraunhofer AISEC, NTU, KTH, NUS, UCLA
    - 📅 Date: March 12, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [security], [LLM agent], [prompt injection], [privacy], [data leakage], [safety]
    - 📖 TLDR: Identifies and measures the "Trusted Executor Dilemma"—where LLM agents execute adversarial instructions embedded in documentation because they cannot distinguish malicious directives from legitimate guidance—formalizing a three-dimensional taxonomy of instructional text-induced private data leakage attacks.

- [LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios](https://arxiv.org/abs/2602.03255)
    - Tianyu Chen, Chujia Hu, Ge Gao, Ruofeng Yu, Yao Lu
    - 🏛️ Institutions: ShanghaiTech University, Shanghai Artificial Intelligence Laboratory, Rice University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [MCP], [long-horizon planning], [LLM agent]
    - 📖 TLDR: LPS-Bench is a benchmark evaluating the planning-time safety awareness of MCP-based computer-use agents under long-horizon tasks, covering 65 scenarios across 7 task domains and 9 risk types with both benign and adversarial interactions, revealing substantial safety deficiencies in existing agents.

- [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725)
    - Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, The Chinese University of Hong Kong, Shenzhen
    - 📅 Date: February 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [guardrail], [world model], [risk prediction], [safety], [long-horizon risk]
    - 📖 TLDR: SafePred is a predictive guardrail for computer-use agents that uses a world model to simulate future states and align current actions with delayed risk, targeting long-horizon hazards that reactive guardrails miss because the danger only emerges after later state transitions.

- [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)
    - Hanna Foerster, Tom Blanchard, Kristina Nikolić, Ilia Shumailov, Cheng Zhang, Robert Mullins, Nicolas Papernot, Florian Tramèr, Yiren Zhao
    - 🏛️ Institutions: University of Cambridge, University of Toronto, Vector Institute, ETH Zurich, AI Sequrity Company
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [single-shot planning], [branch steering], [OSWorld]
    - 📖 TLDR: This paper studies system-level security for computer-use agents under prompt injection attacks. It introduces Single-Shot Planning, where a trusted planner produces a full execution graph with conditional branches before the agent observes potentially malicious content, giving provable control-flow integrity against injected instructions. The paper also identifies Branch Steering as an additional attack surface and shows on OSWorld that strong security guarantees can be achieved while retaining meaningful utility.

- [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/abs/2601.08406)
    - Xinyi Wu, Jiagui Chen, Geng Hong, Jiayi Dong, Xudong Pan, Jiarun Dai, Min Yang
    - 🏛️ Institutions: Fudan University, Shanghai Innovation Institute
    - 📅 Date: January 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [agent framework], [security evaluation], [attack]
    - 📖 TLDR: WebTrap Park is an automated platform for systematic security evaluation of web agents that instantiates three major security risk sources into 1,226 executable tasks on live web pages, revealing that agent architecture matters more than the underlying model for security robustness.

- [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](https://arxiv.org/abs/2512.23128)
    - Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H. S. Torr, Adam Mahdi, Adel Bibi
    - 🏛️ Institutions: University of Oxford, SoftServe, Independent, Johannes Kepler University Linz
    - 📅 Date: December 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [security], [LLM]
    - 📖 TLDR: TRAP is a benchmark for evaluating how persuasion-based prompt injection attacks can redirect LLM-powered web agents from their intended tasks, finding that across six frontier models agents are susceptible to such attacks in 25% of tasks on average, with psychologically-driven social engineering techniques and small interface changes often doubling attack success rates.

- [DECEPTICON: How Dark Patterns Manipulate Web Agents](https://arxiv.org/abs/2512.22894)
    - Phil Cuvin, Hao Zhu, Diyi Yang
    - 🏛️ Institutions: Stanford University
    - 📅 Date: December 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [robustness], [dark patterns], [adversarial attack]
    - 📖 TLDR: Introduces DECEPTICON, a benchmark of 700 web navigation tasks with dark patterns, showing that deceptive UI designs successfully steer state-of-the-art web agents toward malicious outcomes in over 70% of tasks -- with larger models being more susceptible -- and that existing countermeasures fail to mitigate this risk.

- [Permission Manifests for Web Agents](https://arxiv.org/abs/2601.02371)
    - Samuele Marro, Alan Chan, Xinxing Ren, Lewis Hammond, Jesse Wright, Gurjyot Wanga, Tiziano Piccardi, Nuno Campos, Tobin South, Jialin Yu, Sunando Sengupta, Eric Sommerlade, Alex Pentland, Philip Torr, Jiaxin Pei
    - 🏛️ Institutions: University of Oxford, Institute for Decentralized AI, Centre for the Governance of AI, Coral Protocol, Cooperative AI Foundation, Webair, Johns Hopkins University, Witan Labs, Anthropic, Stanford University, The University of Texas at Austin
    - 📅 Date: December 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [framework], [LLM agent], [permission control], [governance]
    - 📖 TLDR: This paper introduces agent-permissions.json, a lightweight robots.txt-style permission manifest that allows website owners to declaratively specify interaction policies for LLM-based web agents, enabling beneficial automated interactions while respecting site owners' preferences and reducing reliance on blanket blocking.

- [Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming](https://arxiv.org/abs/2510.18314)
    - Zheng Zhang, Jiarui He, Yuchen Cai, Deheng Ye, Peilin Zhao, Ruili Feng, Hao Wang
    - 🏛️ Institutions: The Hong Kong University of Science and Technology (Guangzhou), Tencent, Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: October 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [benchmark], [attack], [LLM], [red-teaming]
    - 📖 TLDR: Genesis is an agentic red-teaming framework for LLM web agents that uses genetic algorithms and a dynamic strategy library (Attacker, Scorer, Strategist modules) to automatically evolve and discover adversarial injection attacks, consistently outperforming existing attack baselines across diverse web tasks.

- [Investigating the Impact of Dark Patterns on LLM-Based Web Agents](https://arxiv.org/abs/2510.18113)
    - Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik
    - 🏛️ Institutions: Purdue University, Florida International University, Georgia Institute of Technology
    - 📅 Date: October 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [LLM agent], [dark patterns], [evaluation]
    - 📖 TLDR: This paper presents the first study on how dark patterns (deceptive UI designs) affect LLM-based web agents, introducing TrickyArena as a controlled benchmark environment and finding that agents are susceptible to dark patterns an average of 41% of the time across six popular web agent frameworks and three LLMs.

- [SusBench: An Online Benchmark for Evaluating Dark Pattern Susceptibility of Computer-Use Agents](https://arxiv.org/abs/2510.11035)
    - Longjie Guo, Chenjie Yuan, Mingyuan Zhong, Robert Wolfe, Ruican Zhong, Yue Xu, Bingbing Wen, Hua Shen, Lucy Lu Wang, Alexis Hiniker
    - 🏛️ Institutions: University of Washington, Rutgers University, Carnegie Mellon University, New York University Shanghai
    - 📅 Date: October 13, 2025
    - 📑 Publisher: IUI 2026
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dark pattern], [safety]
    - 📖 TLDR: SusBench is an online benchmark evaluating CUA susceptibility to 9 types of UI dark patterns, featuring 313 realistic tasks across 55 consumer websites with dark patterns injected via code modifications, finding that frontier CUAs are significantly more susceptible to manipulative designs than human users.

- [SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)
    - Zonghao Ying, Yangguang Shao, Jianle Gan, Gan Xu, Junjie Shen, Wenxin Zhang, Quanchen Zou, Junzheng Shi, Zhenfei Yin, Mingchuan Zhang, Aishan Liu, Xianglong Liu
    - 🏛️ Institutions: SKLCCSE, Beihang University, Institute of Information Engineering, Chinese Academy of Sciences, China University of Petroleum (East China), Zhejiang University of Technology, University of Chinese Academy of Science, 360 AI Security Lab, The University of Sydney, Henan University of Science and Technology, Zhongguancun Laboratory, Institute of Dataspace
    - 📅 Date: October 11, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [attack], [VLM], [evaluation]
    - 📖 TLDR: SecureWebArena is a security benchmark for LVLM-based web agents that expands beyond narrow prompt-manipulation settings to six realistic web environments, 2,970 trajectories, and six attack vectors spanning both user-level and environment-level manipulations. Its evaluation protocol separates failures in reasoning, behavior, and task outcome, and the benchmark shows that all tested agents remain vulnerable to subtle adversarial attacks.

- [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670)
    - Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
    - 🏛️ Institutions: Microsoft Research AI Frontiers, Microsoft AI Red Team, University of California, Riverside, NVIDIA
    - 📅 Date: October 02, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [safety], [blind goal-directedness], [BLIND-ACT], [risk evaluation]
    - 📖 TLDR: This paper identifies Blind Goal-Directedness as a recurring failure mode in computer-use agents, where agents keep pursuing user goals despite infeasibility, ambiguity, or unsafe context. It introduces BLIND-ACT, a benchmark built on OSWorld to evaluate these subtle safety failures in realistic desktop environments. The results show high rates of blind goal pursuit across frontier CUAs, making the paper directly relevant to safety evaluation of GUI agents beyond prompt injection alone.

- [WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents](https://arxiv.org/abs/2510.01354)
    - Yinuo Liu, Ruohan Xu, Xilong Wang, Yuqi Jia, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: October 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [security], [prompt injection], [attack detection], [safety]
    - 📖 TLDR: WAInjectBench presents the first comprehensive benchmark for evaluating prompt injection detection methods targeting web agents, finding that while some detectors handle explicit textual attacks or visible image perturbations reasonably well, they largely fail against attacks that omit explicit instructions or use imperceptible perturbations.

- [Secure and Efficient Access Control for Computer-Use Agents via Context Space](https://arxiv.org/abs/2509.22256)
    - Haochen Gong, Chenxiao Li, Rui Chang, Wenbo Shen
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: September 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [access control], [safety], [framework]
    - 📖 TLDR: CSAgent is a system-level, static policy-based access control framework for CUAs that uses "context space"—a representation of the agent operational context—to enforce fine-grained permissions and prevent LLM uncertainty from causing irreversible harmful actions.

- [AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents](https://arxiv.org/abs/2509.07764)
    - Haitao Hu, Peng Chen, Yanpeng Zhao, Yuqi Chen
    - 🏛️ Institutions: ShanghaiTech University, Independent Researcher
    - 📅 Date: September 09, 2025
    - 📑 Publisher: CCS 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [defense], [safety], [framework]
    - 📖 TLDR: AgentSentinel is an end-to-end, real-time security defense framework for CUAs that monitors LLM-driven tool commands across all agent components to detect and prevent unintended or harmful operations arising from LLM non-determinism, spanning vulnerabilities beyond insecure user prompts.

- [Throttling Web Agents Using Reasoning Gates](https://arxiv.org/abs/2509.01619)
    - Abhinav Kumar, Jaechul Roh, Ali Naseh, Amir Houmansadr, Eugene Bagdasarian
    - 🏛️ Institutions: University of Massachusetts Amherst
    - 📅 Date: September 01, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [access control], [defense], [reasoning]
    - 📖 TLDR: Proposes Reasoning Gates, a framework imposing tunable computational costs on web agents before granting resource access, protecting content providers from denial-of-service, excessive scraping, and CAPTCHA bypass while preserving service availability for legitimate users.

- [Reliable Weak-to-Strong Monitoring of LLM Agents](https://arxiv.org/abs/2508.19461)
    - Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Scale Red Team, Christina Q. Knight, Zifan Wang
    - 🏛️ Institutions: Scale AI, Carnegie Mellon University, Massachusetts Institute of Technology
    - 📅 Date: August 26, 2025
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [LLM agent], [monitoring], [red-teaming]
    - 📖 TLDR: Stress-tests LLM agent monitoring systems for detecting covert misbehavior using a monitor red-teaming (MRT) workflow varying agent/monitor awareness and adversarial evasion strategies, evaluated on SHADE-Arena for tool-calling agents and CUA-SHADE-Arena for computer-use agents.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: June 04, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multilingual], [safety], [macOSWorld]
    - 📖 TLDR: Introduces **macOSWorld**, the first interactive benchmark for GUI agents on macOS, with 202 tasks across 30 apps (28 macOS-exclusive) in 5 languages plus a safety subset for deception attacks; evaluates 6 agents, showing proprietary CUAs outperform open-source and VLM-based agents, significant language gaps (Arabic –27.5%), and both grounding and safety challenges.

- [DPO Learning with LLMs-Judge Signal for Computer Use Agents](https://arxiv.org/abs/2506.03095)
    - Man Luo, David Cobbley, Xin Su, Shachar Rosenman, Vasudev Lal, Shao-Yen Tseng, Phillip Howard
    - 🏛️ Institutions: Intel, Thoughtworks
    - 📅 Date: June 03, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [memory], [safety], [alignment], [framework]
    - 📖 TLDR: VerificAgent is a scalable oversight framework for CUAs treating persistent memory as an explicit alignment surface, combining expert-curated domain seeds, trajectory-based memory growth, and human fact-checking to prevent domain-inappropriate or unsafe heuristics from accumulating in agent memory.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory, University of Science and Technology of China, Shanghai Jiao Tong University
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [safety], [risk evaluation], [harmful task completion], [OSWorld], [RiOSWorld]
    - 📖 TLDR: RiOSWorld measures misuse risk for multimodal desktop and web agents in realistic interactive settings rather than ordinary chat-style safety probes. Its 492 risky tasks score both harmful intent and harmful task completion, showing that current agents remain highly exposed to real-world misuse despite strong task-solving abilities.

- [GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents](https://arxiv.org/abs/2505.12842)
    - Zheng Wu, Pengzhou Cheng, Zongru Wu, Lingzhong Dong, Zhuosheng Zhang
    - 🏛️ Institutions: School of Electronic Information and Electrical Engineering, Shanghai Jiao Tong University
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [out-of-distribution detection], [safety], [gaussian mixture model], [MLLM], [robustness]
    - 📖 TLDR: GEM proposes a Gaussian mixture model-based method for detecting out-of-distribution instructions in GUI agents by modeling input embedding distances, achieving a 23.70% average accuracy improvement over baselines across eight datasets spanning smartphones, computers, and web browsers.

- [A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?](https://arxiv.org/abs/2505.10924)
    - Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
    - 🏛️ Institutions: Carnegie Mellon University, The Chinese University of Hong Kong, KAUST, Johns Hopkins University, Nanyang Technological University, The Hong Kong University of Science and Technology
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [safety], [security]
    - 📖 TLDR: A comprehensive survey of safety and security threats to computer-using agents, covering vulnerabilities in LLM-driven reasoning, multi-component integration, and GUI interaction, analyzing novel risks as CUAs evolve from prototype tools to sophisticated autonomous systems.

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
    - Ivan Evtimov, Arman Zharmagambetov, Aaron Grattafiori, Chuan Guo, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta
    - 📅 Date: April 22, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [security], [WASP]
    - 📖 TLDR: Evaluates web-agent security under realistic multi-step prompt injection attacks instead of simplified single-step setups. WASP shows that even strong agents can be partially deceived at very high rates by low-effort human-written injections, while also revealing a security-by-incompetence pattern where agents are unsafe but often too weak to fully realize the attacker’s goal.

- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434)
    - Yucheng Shi, Wenhao Yu, Jingyuan Huang, Wenlin Yao, Wenhu Chen, Ninghao Liu
    - 🏛️ Institutions: University of Georgia, Tencent AI Seattle Lab, Microsoft Research, University of Waterloo, Hong Kong Polytechnic University
    - 📅 Date: March 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [survey], [trustworthiness], [safety], [security], [benchmark]
    - 📖 TLDR: A survey on trustworthy GUI agents that introduces a workflow-aligned taxonomy decomposing trust into Perception Trust, Reasoning Trust, and Interaction Trust, systematically reviewing failure modes, adversarial attacks, defense mechanisms, and evaluation practices for deploying GUI agents safely.

- [sudo rm -rf agentic_security](https://arxiv.org/abs/2503.20279)
    - Sejin Lee, Jian Kim, Haon Park, Ashkan Yousefpour, Sangyoon Yu, Min Song
    - 🏛️ Institutions: Aim Intelligence, Yonsei University, SNU
    - 📅 Date: March 26, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [attack], [jailbreaking], [safety]
    - 📖 TLDR: SUDO (Screen-based Universal Detox2Tox Offense) is a novel attack framework that bypasses refusal-trained safeguards in commercial CUAs (e.g., Claude Computer Use) by transforming harmful requests into seemingly benign ones via a Detox2Tox mechanism, exposing critical vulnerabilities in CUA safety.

- [VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification](https://arxiv.org/abs/2503.18492)
    - Jungjae Lee, Dongjae Lee, Chihun Choi, Youngmin Im, Jaeyoung Wi, Kihong Heo, Sangeun Oh, Sunjae Lee, Insik Shin
    - 🏛️ Institutions: KAIST, Korea University, SKKU
    - 📅 Date: March 24, 2025
    - 📑 Publisher: MobiCom 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [safety], [verification], [formal verification], [framework]
    - 📖 TLDR: VeriSafe Agent (VSA) is a formal logic-based action verification system for mobile GUI agents that checks LFM-proposed actions against predefined safety constraints before execution, preventing unreliable automation caused by the probabilistic nature of large foundation models.

- [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)
    - Lukas Aichberger, Alasdair Paren, Guohao Li, Philip Torr, Yarin Gal, Adel Bibi
    - 🏛️ Institutions: Johannes Kepler University Linz, University of Oxford
    - 📅 Date: March 13, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [security], [adversarial attacks], [OS agent], [MIP against agent]
    - 📖 TLDR: This paper identifies Malicious Image Patches as a new attack vector against multimodal OS agents, where adversarially perturbed visual regions on the screen can trigger harmful actions when captured by the agent. The attack generalizes across prompts and screen setups, showing that benign-looking visual content such as wallpapers or social media images can hijack computer-use agents. The paper exposes a concrete security weakness in OS-level agents that goes beyond text-only prompt injection.

- [AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780)
    - Arman Zharmagambetov, Chuan Guo, Ivan Evtimov, Maya Pavlova, Ruslan Salakhutdinov, Kamalika Chaudhuri
    - 🏛️ Institutions: FAIR at Meta, Meta
    - 📅 Date: March 12, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [privacy], [data minimization], [safety], [AgentDAM]
    - 📖 TLDR: Evaluates whether autonomous web agents obey the privacy principle of data minimization, meaning they access sensitive user information only when it is genuinely necessary for task completion. AgentDAM provides an end-to-end web benchmark for this question and shows that strong current agents frequently consume unnecessary private information, even though a prompting-based defense can reduce leakage.

- [Evaluating the Robustness of Multimodal Agents Against Active Environmental Injection Attacks](https://arxiv.org/abs/2502.13053)
    - Yurun Chen, Xueyu Hu, Keting Yin, Juncheng Li, Shengyu Zhang
    - 🏛️ Institutions: Zhejiang University
    - 📅 Date: February 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [safety], [AEIA-MN]
    - 📖 TLDR: This paper introduces the concept of Active Environment Injection Attack (AEIA), where attackers disguise malicious actions as environmental elements to disrupt AI agents' decision-making processes. The authors propose AEIA-MN, an attack scheme leveraging mobile notifications to evaluate the robustness of multimodal large language model-based mobile agents. Experimental results demonstrate that even advanced models are highly vulnerable to such attacks, with success rates reaching up to 93% in the AndroidWorld benchmark.

- [Language Agents: Foundations, Prospects, and Risks](https://aclanthology.org/2024.emnlp-tutorials.3/)
    - Yu Su, Diyi Yang, Shunyu Yao, Tao Yu
    - 🏛️ Institutions: The Ohio State University, Stanford University, Princeton University, The University of Hong Kong
    - 📅 Date: November 30, 2024
    - 📑 Publisher: EMNLP 2024 Tutorial Abstracts
    - 💻 Env: [Misc]
    - 🔑 Key: [survey], [tutorial], [reasoning], [planning], [memory], [multi-agent systems], [safety]
    - 📖 TLDR: This tutorial provides a comprehensive exploration of language agents—autonomous systems powered by large language models capable of executing complex tasks through language instructions. It delves into their theoretical foundations, potential applications, associated risks, and future directions, covering topics such as reasoning, memory, planning, tool augmentation, grounding, multi-agent systems, and safety considerations.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Institute of Technology, The University of Hong Kong, Stanford University
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [attack], [adversarial pop-ups], [safety], [OSWorld], [VisualWebArena]
    - 📖 TLDR: Shows that vision-language computer agents can be reliably distracted by adversarial pop-ups that human users would typically ignore. On OSWorld and VisualWebArena, these pop-ups achieve high attack success rates and sharply reduce task completion, while simple defenses like warning prompts remain ineffective.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, The University of Texas at Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [Android emulator], [MobileSafetyBench]
    - 📖 TLDR: Introduces MobileSafetyBench, a benchmark for measuring safety failures of mobile-control agents in realistic Android tasks involving apps like messaging and banking. It evaluates both ordinary safety behavior and robustness to indirect prompt injection, and shows that current agents still struggle to avoid harmful actions.

- [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://arxiv.org/abs/2410.17401)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: University of Illinois Urbana-Champaign, University of Chicago, The Ohio State University, University of Science and Technology of China
    - 📅 Date: October 22, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [attack], [black-box attack], [adversarial prompt injection], [DPO], [AdvAgent]
    - 📖 TLDR: AdvAgent is a black-box red-teaming framework for web agents that trains an adversarial prompter with DPO to craft stealthy, controllable attacks against VLM-powered agents. It achieves high attack success rates on realistic web tasks and shows that existing prompt-based defenses remain insufficient.

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
    - 📅 Date: October 09, 2024
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
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [EIA]
    - 📖 TLDR: This paper introduces the Environmental Injection Attack (EIA), a privacy attack targeting generalist web agents by embedding malicious yet concealed web elements to trick agents into leaking users' PII. Utilizing 177 action steps within realistic web scenarios, EIA demonstrates a high success rate in extracting specific PII and whole user requests. Through its detailed threat model and defense suggestions, the work underscores the challenge of detecting and mitigating privacy risks in autonomous web agents.

- [Caution for the Environment: Multimodal LLM Agents are Susceptible to Environmental Distractions](https://aclanthology.org/2025.acl-long.1087/)
    - Xinbei Ma, Yiting Wang, Yao Yao, Tongxin Yuan, Aston Zhang, Zhuosheng Zhang, Hai Zhao
    - 🏛️ Institutions: Shanghai Jiao Tong University, Meta
    - 📅 Date: August 05, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [robustness], [environmental distraction], [multimodal LLM agent]
    - 📖 TLDR: This paper highlights the vulnerability of multimodal agents to environmental distractions. The researchers demonstrate that these agents, which process multiple types of input (e.g., text, images, audio), can be significantly impacted by irrelevant or misleading environmental cues. The study provides insights into the limitations of current multimodal systems and emphasizes the need for more robust architectures that can filter out distractions and maintain focus on relevant information in complex, real-world environments.

- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://arxiv.org/abs/2402.10196)
    - Lingbo Mo, Zeyi Liao, Boyuan Zheng, Yu Su, Chaowei Xiao, Huan Sun
    - 🏛️ Institutions: The Ohio State University, University of Wisconsin-Madison
    - 📅 Date: February 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Misc]
    - 🔑 Key: [safety], [adversarial attacks], [security risks], [language agents], [perception-brain-action]
    - 📖 TLDR: Maps adversarial attacks on language agents through a Perception-Brain-Action decomposition and surveys 12 attack types across those layers. The paper is mainly a threat-modeling taxonomy, useful as a security lens for later web and computer-use agents.
