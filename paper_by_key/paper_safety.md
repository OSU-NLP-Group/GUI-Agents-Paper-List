# Papers with Keyword: safety

- [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235)
    - Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun
    - 🏛️ Institutions: OSU, LawZero, Mila, UdeM, UC Berkeley
    - 📅 Date: February 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [unintended behaviors], [AutoElicit], [benchmark], [red teaming]
    - 📖 TLDR: AutoElicit is an agentic framework that iteratively perturbs benign instructions using CUA execution feedback to surface unintended harmful behaviors while keeping inputs realistic. It elicits severe harms from frontier CUAs like Claude 4.5 and Operator in up to 72.5% of OS-domain seeds, and evaluates cross-model transferability of verified perturbations.

- [When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents](https://arxiv.org/abs/2602.08995)
    - Yuting Ning, Jaylen Jones, Zhehao Zhang, Chentao Ye, Weitong Ruan, Junyi Li, Rahul Gupta, Huan Sun
    - 🏛️ Institutions: OSU, Amazon AGI
    - 📅 Date: February 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [guardrail], [misaligned actions], [benchmark], [dataset], [MisActBench], [DeAction]
    - 📖 TLDR: This paper introduces MisActBench, a benchmark of 2,264 human-annotated action-level alignment labels covering malicious instruction following, harmful unintended behavior, and task-irrelevant actions. It proposes DeAction, a two-stage guardrail that detects misaligned actions before execution and iteratively corrects them, improving F1 by 15%+ over baselines and reducing attack success rate by over 90%.

- [LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios](https://arxiv.org/abs/2602.03255)
    - Tianyu Chen, Chujia Hu, Ge Gao, Ruofeng Yu, Yao Lu
    - 🏛️ Institutions: ShanghaiTech University, Shanghai AI Laboratory, Rice University
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [safety], [MCP], [long-horizon planning], [LLM agent]
    - 📖 TLDR: LPS-Bench is a benchmark evaluating the planning-time safety awareness of MCP-based computer-use agents under long-horizon tasks, covering 65 scenarios across 7 task domains and 9 risk types with both benign and adversarial interactions, revealing substantial safety deficiencies in existing agents.

- [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725)
    - Yurun Chen, Zeyi Liao, Ping Yin, Taotao Xie, Keting Yin, Shengyu Zhang
    - 🏛️ Institutions: Tsinghua, OSU, CUHK-Shenzhen
    - 📅 Date: February 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [guardrail], [world model], [risk prediction], [safety], [long-horizon risk], [SafePred]
    - 📖 TLDR: SafePred is a predictive guardrail that uses a world model to simulate future states and assess delayed risk before a computer-use agent acts. It targets long-horizon hazards that reactive safety filters tend to miss.

- [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)
    - Hanna Foerster, Tom Blanchard, Kristina Nikolić, Ilia Shumailov, Cheng Zhang, Robert Mullins, Nicolas Papernot, Florian Tramèr, Yiren Zhao
    - 🏛️ Institutions: University of Cambridge, University of Toronto, Vector Institute, ETH, AI Sequrity Company
    - 📅 Date: January 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [safety], [prompt injection], [control flow integrity], [Single-Shot Planning], [Branch Steering], [OSWorld], [CaMeLs]
    - 📖 TLDR: This paper adapts the Dual-LLM security paradigm to computer-use agents through Single-Shot Planning, where a trusted planner writes a full branching execution graph before seeing untrusted UI content. That gives control-flow integrity against injected instructions, but the paper also identifies Branch Steering as a remaining data-flow threat and studies its tradeoff with utility on OSWorld.

- [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/abs/2601.08406)
    - Xinyi Wu, Jiagui Chen, Geng Hong, Jiayi Dong, Xudong Pan, Jiarun Dai, Min Yang
    - 🏛️ Institutions: Fudan, Shanghai Innovation Institute
    - 📅 Date: January 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [security evaluation], [behavioral evaluation], [WebTrap Park]
    - 📖 TLDR: WebTrap Park is an automated platform for evaluating web-agent security by directly observing actions on live web pages rather than relying on internal logs. It instantiates malicious user prompts, prompt injections, and deceptive website designs into 1,226 executable tasks and shows clear security differences across agent frameworks.

- [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](https://arxiv.org/abs/2512.23128)
    - Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H.S. Torr, Adam Mahdi, Adel Bibi
    - 🏛️ Institutions: Oxford, SoftServe, Independent, Johannes Kepler University Linz
    - 📅 Date: December 29, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [social engineering], [TRAP]
    - 📖 TLDR: TRAP studies persuasion-style prompt injection on realistic cloned websites, varying factors such as injection interface, persuasion principle, placement, and tailoring. Across six frontier models, it finds web agents are redirected in 25% of tasks on average, and small interface or contextual changes often double attack success.

- [DECEPTICON: How Dark Patterns Manipulate Web Agents](https://arxiv.org/abs/2512.22894)
    - Phil Cuvin, Hao Zhu, Diyi Yang
    - 🏛️ Institutions: Stanford
    - 📅 Date: December 28, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [dark patterns], [human benchmark], [DECEPTICON]
    - 📖 TLDR: DECEPTICON isolates individual dark patterns in 700 web-navigation tasks, including 600 generated tasks and 100 real-world ones, to measure both task success and manipulation effectiveness. It finds dark patterns steer state-of-the-art web agents toward malicious outcomes in over 70% of tested tasks, exceed human susceptibility, and remain hard to mitigate with current defenses.

- [Permission Manifests for Web Agents](https://arxiv.org/abs/2601.02371)
    - Samuele Marro, Alan Chan, Xinxing Ren, Lewis Hammond, Jesse Wright, Gurjyot Wanga, Tiziano Piccardi, Nuno Campos, Tobin South, Jialin Yu, Sunando Sengupta, Eric Sommerlade, Alex Pentland, Philip Torr, Jiaxin Pei
    - 🏛️ Institutions: Oxford, Institute for Decentralized AI, Centre for the Governance of AI, Coral Protocol, Cooperative AI Foundation, Webair, JHU, Witan Labs, Anthropic, Stanford, UT Austin
    - 📅 Date: December 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [agent-permissions.json], [permission manifest], [robots.txt-style governance], [web governance]
    - 📖 TLDR: This paper proposes agent-permissions.json, a lightweight robots.txt-style manifest for web agents that lets site owners specify which resources and interactions are allowed, optionally pointing agents to preferred APIs. The goal is to replace blanket blocking with a lower-friction compliance mechanism for browser-based agent traffic.

- [Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming](https://arxiv.org/abs/2510.18314)
    - Zheng Zhang, Jiarui He, Yuchen Cai, Deheng Ye, Peilin Zhao, Ruili Feng, Hao Wang
    - 🏛️ Institutions: HKUST(GZ), Tencent, SJTU, Alibaba Group
    - 📅 Date: October 21, 2025
    - 📑 Publisher: ICME 2026
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [attack], [prompt injection], [genetic algorithm], [red-teaming], [Genesis]
    - 📖 TLDR: Genesis studies automated red-teaming for web agents by evolving attack strategies over repeated interactions instead of relying on fixed prompts or manually designed attacks. Its attacker-scorer-strategist loop builds and reuses a growing strategy library, yielding stronger adversarial injections across web tasks.

- [Investigating the Impact of Dark Patterns on LLM-Based Web Agents](https://arxiv.org/abs/2510.18113)
    - Devin Ersoy, Brandon Lee, Ananth Shreekumar, Arjun Arunasalam, Muhammad Ibrahim, Antonio Bianchi, Z. Berkay Celik
    - 🏛️ Institutions: Purdue University, Florida International University, Georgia Tech
    - 📅 Date: October 20, 2025
    - 📑 Publisher: IEEE S&P 2026
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [dark patterns], [TrickyArena], [LiteAgent]
    - 📖 TLDR: This paper studies how deceptive interface designs affect web agents, introducing LiteAgent for controlled execution and TrickyArena as a dark-pattern test environment. Across six agent frameworks and three underlying models, it finds that agents are frequently steered by dark patterns and that both visual and HTML-level manipulations can change susceptibility.

- [macOSWorld: A Multilingual Interactive Benchmark for GUI Agents](https://arxiv.org/abs/2506.04135)
    - Pei Yang, Hai Ci, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS
    - 📅 Date: June 04, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [multilingual], [safety], [macOSWorld]
    - 📖 TLDR: macOSWorld is the first interactive benchmark for GUI agents on macOS, covering 202 multilingual tasks across 30 applications and a dedicated safety subset for deception attacks. The evaluation shows large performance gaps between proprietary and open-source agents, substantial multilingual degradation, and unresolved safety weaknesses on macOS-specific workflows.

- [RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents](https://arxiv.org/abs/2506.00618)
    - Jingyi Yang, Shuai Shao, Dongrui Liu, Jing Shao
    - 🏛️ Institutions: Shanghai AI Laboratory, USTC, SJTU
    - 📅 Date: May 31, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [safety], [misuse risk], [harmful intent], [harmful task completion], [RiOSWorld]
    - 📖 TLDR: RiOSWorld measures misuse risk for multimodal desktop and web agents in realistic interactive settings rather than ordinary chat-style safety probes. Its 492 risky tasks score both harmful intent and harmful task completion, showing that current computer-use agents remain highly exposed to real-world misuse despite strong task-solving ability.

- [GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents](https://arxiv.org/abs/2505.12842)
    - Zheng Wu, Pengzhou Cheng, Zongru Wu, Lingzhong Dong, Zhuosheng Zhang
    - 🏛️ Institutions: School of Electronic Information and Electrical Engineering, SJTU
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [out-of-distribution detection], [gaussian embedding modeling], [capability boundary], [safety], [GEM]
    - 📖 TLDR: GEM studies out-of-distribution instruction detection for GUI agents whose capability boundaries are hard to characterize in evolving interfaces. It models embedding-distance clusters with a Gaussian mixture and improves OOD detection accuracy across mobile, desktop, and web settings, while also boosting step-wise success by escalating OOD cases to a stronger cloud model.

- [A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?](https://arxiv.org/abs/2505.10924)
    - Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, Shuai Wang
    - 🏛️ Institutions: CMU, CUHK, KAUST, JHU, NTU, HKUST
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [safety], [security], [threat taxonomy], [defense taxonomy]
    - 📖 TLDR: This survey systematizes safety and security risks in computer-using agents, from reasoning failures and multimodal vulnerabilities to risks introduced by multi-component agent stacks. It organizes the field around threat categories, defensive strategies, and the benchmarks and datasets currently used to study secure CUA deployment.

- [VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification](https://arxiv.org/abs/2503.18492)
    - Jungjae Lee, Dongjae Lee, Chihun Choi, Youngmin Im, Jaeyoung Wi, Kihong Heo, Sangeun Oh, Sunjae Lee, Insik Shin
    - 🏛️ Institutions: KAIST, Korea University, SKKU
    - 📅 Date: March 24, 2025
    - 📑 Publisher: MobiCom 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [safety], [formal verification], [autoformalization], [runtime verification], [VSA]
    - 📖 TLDR: VeriSafe Agent is a mobile GUI safeguard that translates user instructions into formal specifications and verifies each proposed action against them before execution. Across 300 instructions on 18 apps, it improves verification accuracy over LFM-based baselines and raises downstream task completion.

- [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/)
    - Xueyu Hu, Tao Xiong, Biao Yi, Zishu Wei, Ruixuan Xiao, Yurun Chen, Jiasheng Ye, Meiling Tao, Xiangxin Zhou, Ziyu Zhao, Yuhuai Li, Shengze Xu, Shenzhi Wang, Xinchen Xu, Shuofei Qiao, Zhaokai Wang, Kun Kuang, Tieyong Zeng, Liang Wang, Jiwei Li, Yuchen Eleanor Jiang, Wangchunshu Zhou, Guoyin Wang, Keting Yin, Zhou Zhao, Hongxia Yang, Fan Wu, Shengyu Zhang, Fei Wu
    - 🏛️ Institutions: ZJU, Fudan, OPPO AI Center, University of Chinese Academy of Sciences, Institute of Automation, CAS, CUHK, Tsinghua, SJTU, 01.AI, PolyU
    - 📅 Date: December 20, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [survey], [architectures], [benchmarks], [training], [safety]
    - 📖 TLDR: This survey reviews MLLM-based OS agents across computers, phones, and browsers, covering their environments, observation and action spaces, capabilities, and system designs. It also organizes the benchmark landscape and highlights open problems such as safety, privacy, personalization, and self-evolution.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Tech, HKU, Stanford
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [attack], [adversarial pop-ups], [safety], [OSWorld], [VisualWebArena]
    - 📖 TLDR: Shows that vision-language computer agents can be reliably distracted by adversarial pop-ups that human users would typically ignore. On OSWorld and VisualWebArena, these pop-ups achieve high attack success rates and sharply reduce task completion, while simple defenses like warning prompts remain ineffective.

- [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520)
    - Juyong Lee, Dongyoon Hahm, June Suk Choi, W. Bradley Knox, Kimin Lee
    - 🏛️ Institutions: KAIST, UT Austin
    - 📅 Date: October 23, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [safety], [prompt injection], [Android emulator], [MobileSafetyBench]
    - 📖 TLDR: Introduces MobileSafetyBench, a benchmark for measuring safety failures of mobile-control agents in realistic Android tasks involving apps like messaging and banking. It evaluates both ordinary safety behavior and robustness to indirect prompt injection, and shows that current agents still struggle to avoid harmful actions.

- [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://proceedings.mlr.press/v267/xu25m.html)
    - Chejian Xu, Mintong Kang, Jiawei Zhang, Zeyi Liao, Lingbo Mo, Mengqi Yuan, Huan Sun, Bo Li
    - 🏛️ Institutions: UIUC, University of Chicago, OSU
    - 📅 Date: October 22, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [red teaming], [black-box attack], [DPO], [AdvAgent]
    - 📖 TLDR: AdvAgent is a black-box red-teaming method for web agents that trains an adversarial prompter with DPO to generate stealthy, controllable attacks against frontier browser agents. The paper shows high attack success rates across realistic web tasks and finds that existing prompt-based defenses provide limited protection.

- [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886)
    - Priyanshu Kumar, Elaine Lau, Saranya Vijayakumar, Tu Trinh, Scale Red Team, Elaine Chang, Vaughn Robinson, Sean Hendryx, Shuyan Zhou, Matt Fredrikson, Summer Yue, Zifan Wang
    - 🏛️ Institutions: CMU, Scale AI, GraySwan AI
    - 📅 Date: October 11, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [red teaming], [jailbreaking], [BrowserART]
    - 📖 TLDR: The paper introduces BrowserART, a red-teaming benchmark with 100 harmful browser-agent behaviors spanning synthetic and real websites. It shows that refusal-trained backbone LLMs may still execute harmful instructions once embedded in browser agents, and that chat jailbreaks transfer effectively to that agent setting.

- [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://openreview.net/forum?id=MuCDzH0ctf)
    - Ido Levy, Ben Wiesel, Sami Marreed, Alon Oved, Avi Yaeli, Nir Mashkif, Segev Shlomov
    - 🏛️ Institutions: IBM Research
    - 📅 Date: October 09, 2024
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [safety], [trustworthiness], [policy compliance], [CuP], [ST-WebAgentBench]
    - 📖 TLDR: ST-WebAgentBench is a benchmark for enterprise-style web-agent evaluation that pairs 375 tasks with 3,057 safety and trustworthiness policies and introduces policy-aware metrics such as Completion Under Policy (CuP) and Risk Ratio. The paper shows that strong agents lose a large fraction of their nominal completion rate once policy compliance is required.

- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk)
    - Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun
    - 🏛️ Institutions: OSU, Amazon, UIUC, University of Chicago, JHU, University of Virginia
    - 📅 Date: September 17, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [privacy attack], [prompt injection], [environmental injection], [EIA]
    - 📖 TLDR: EIA studies privacy leakage in generalist web agents under adversarial webpages and introduces Environmental Injection Attack, which hides malicious content in the environment to steal user information. Using 177 action steps built from realistic Mind2Web scenarios, the paper reports up to 70% attack success for stealing specific PII and 16% for stealing a full user request at a step, while also arguing that well-adapted attacks are difficult to detect or mitigate.

- [Dissecting Adversarial Robustness of Multimodal LM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/460a1d8eac34125dad453b28d6d64446-Abstract-Conference.html)
    - Chen Henry Wu, Rishi Shah, Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried, Aditi Raghunathan
    - 🏛️ Institutions: CMU
    - 📅 Date: June 18, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [attack], [ARE], [VisualWebArena], [safety]
    - 📖 TLDR: The paper builds an adversarial extension of VisualWebArena with 200 targeted tasks and introduces the Agent Robustness Evaluation (ARE) framework for analyzing how attacks propagate through compound agent systems. It shows that small visual or textual perturbations can reliably hijack strong multimodal web agents, including variants that use reflection or tree search.
