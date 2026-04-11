# Papers with Keyword: evaluation

- [CUAAudit: Meta-Evaluation of Vision-Language Models as Auditors of Autonomous Computer-Use Agents](https://arxiv.org/abs/2603.10577)
    - Marta Sumyk, Oleksandr Kosovan
    - 🏛️ Institutions: Ukrainian Catholic University
    - 📅 Date: March 11, 2026
    - 📑 Publisher: HEAL @ CHI 2026 Workshop
    - 💻 Env: [Desktop]
    - 🔑 Key: [evaluation], [VLM judge], [agent-as-a-judge], [calibration], [meta-evaluation], [CUAAudit]
    - 📖 TLDR: CUAAudit studies vision-language models as autonomous judges of desktop-agent task success from observable interactions alone. Across multiple operating-system benchmarks, it finds that even strong VLM auditors degrade on harder environments and disagree substantially with one another, highlighting limits of model-based auditing.

- [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075)
    - Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Qinyi Luo, Shunye Tang, Yuxiang Chai, Weifeng Lin, Han Xiao, WenHao Wang, Siheng Chen, Zhengxi Lu, Gao Wu, Hao Wang, Liang Liu, Yong Liu
    - 🏛️ Institutions: Zhejiang University, Nankai University, The Chinese University of Hong Kong, Shanghai Jiao Tong University, vivo AI Lab
    - 📅 Date: February 03, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [memory], [evaluation], [MemGUI-Eval], [MemGUI-Bench]
    - 📖 TLDR: MemGUI-Bench is a memory-focused benchmark for mobile GUI agents covering dynamic tasks that require cross-temporal and cross-spatial retention. Paired with MemGUI-Eval, it reveals large hidden memory deficits in current agents that standard benchmarks miss.

- [WebGraphEval: Multi-Turn Trajectory Evaluation for Web Agents using Graph Representation](https://arxiv.org/abs/2510.19205)
    - Yaoyao Qian, Yuanli Wang, Jinda Zhang, Yun Zong, Meixu Chen, Hanhan Zhou, Jindan Huang, Yifan Zeng, Xinyu Hu, Chan Hee Song, Danqing Zhang
    - 🏛️ Institutions: Northeastern University, Boston University, University of Victoria, University of Minnesota, George Washington University, Tufts University, Oregon State University, University of Texas at San Antonio, The Ohio State University, PathOnAI.org
    - 📅 Date: October 22, 2025
    - 📑 Publisher: NeurIPS 2025 Workshop on Multi-Turn Interactions in Large Language Models
    - 💻 Env: [Web]
    - 🔑 Key: [evaluation], [trajectory analysis], [weighted action graph], [multi-path evaluation], [WebGraphEval]
    - 📖 TLDR: WebGraphEval evaluates web agents by converting many interaction trajectories into a unified weighted action graph instead of scoring only final success or conformity to one reference path. This graph view highlights redundancy, inefficiency, and critical decision points across agents and benchmark runs.

- [AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://arxiv.org/abs/2504.08942)
    - Xing Han Lù, Amirhossein Kazemnejad, Nicholas Meade, Arkil Patel, Dongchan Shin, Alejandra Zambrano, Karolina Stańczak, Peter Shaw, Christopher J. Pal, Siva Reddy
    - 🏛️ Institutions: McGill, Mila, Google DeepMind, Polytechnique Montréal, ServiceNow Research
    - 📅 Date: April 11, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation], [LLM judges], [AgentRewardBench]
    - 📖 TLDR: Benchmarks automatic evaluation of web-agent trajectories rather than agent performance itself, collecting 1,302 expert-annotated trajectories across five web benchmarks with labels for success, side effects, and repetitiveness. The study shows no single LLM judge dominates across settings and that common rule-based evaluators often underreport true agent success.

- [An Illusion of Progress? Assessing the Current State of Web Agents](https://openreview.net/forum?id=6jZi4HSs6o)
    - Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, Yu Su
    - 🏛️ Institutions: The Ohio State University, University of California, Berkeley
    - 📅 Date: April 02, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [evaluation], [online-Mind2Web], [WebJudge], [operator], [LLM-as-a-judge]
    - 📖 TLDR: This paper critically evaluates the performance of current web agents, revealing that many underperform on the newly introduced **Online-Mind2Web** benchmark, which comprises 300 realistic tasks across 136 websites. The study highlights a discrepancy between reported successes and actual capabilities, attributing this to shortcomings in existing benchmarks. To address evaluation scalability, the authors propose **WebJudge**, an automatic LLM-based evaluation method achieving approximately 85% agreement with human judgments. The comprehensive analysis underscores the need for more robust assessment frameworks in web agent research.

- [BEARCUBS: A benchmark for computer-using web agents](https://arxiv.org/abs/2503.07919)
    - Yixiao Song, Katherine Thai, Chau Minh Pham, Yapei Chang, Mazin Nadaf, Mohit Iyyer
    - 🏛️ Institutions: UMass Amherst, UMD
    - 📅 Date: March 10, 2025
    - 📑 Publisher: COLM 2025
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [information seeking], [computer use], [evaluation]
    - 📖 TLDR: BEARCUBS is a benchmark of 111 information-seeking questions requiring web agents to access live websites, handle authentication, interact with dynamic content, and identify factual information in real-world settings without relying on static cached content.

- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis](https://arxiv.org/abs/2502.20383)
    - Jeffrey Yang Fan Chiang, Seungjae Lee, Jia-Bin Huang, Furong Huang, Yizheng Chen
    - 🏛️ Institutions: University of Maryland
    - 📅 Date: February 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [security], [jailbreaking], [evaluation], [OpenHands]
    - 📖 TLDR: This paper investigates why Web AI agents are significantly more susceptible to executing harmful commands compared to standalone LLMs, despite sharing the same underlying models. Through a fine-grained evaluation, the authors identify three critical factors contributing to this vulnerability: embedding user goals into system prompts, multi-step action generation, and processing of event streams from web navigation. The study introduces a five-level harmfulness evaluation framework and utilizes the OpenHands platform to systematically assess these vulnerabilities, revealing a 46.6% success rate in malicious task execution by Web AI agents versus 0% for standalone LLMs.

- [The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use](https://arxiv.org/abs/2411.10323)
    - Siyuan Hu, Mingyu Ouyang, Difei Gao, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: November 15, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [case study], [Claude 3.5 Computer Use], [desktop automation], [evaluation]
    - 📖 TLDR: Studies Claude 3.5 Computer Use through curated desktop tasks spanning multiple software domains and provides a simple deployment framework for API-based GUI automation. The analysis focuses on what the model can already do well and where planning, action execution, and critic behavior still break down in real-world settings.

- [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation](https://arxiv.org/abs/2404.16054)
    - Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu
    - 🏛️ Institutions: Beijing University of Posts and Telecommunications, Tsinghua University
    - 📅 Date: April 12, 2024
    - 📑 Publisher: UIST 2024
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [dataset], [mobile UI automation], [evaluation], [state matching], [LlamaTouch]
    - 📖 TLDR: LlamaTouch is a mobile UI task-automation testbed that replaces brittle action-sequence matching with evaluation based on whether an agent traverses manually annotated essential application and system states. It combines on-device execution, fine-grained UI component annotation, and multi-level state matching to deliver more faithful and scalable evaluation across 496 tasks.

- [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://aclanthology.org/2024.acl-long.371/)
    - Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu
    - 🏛️ Institutions: Zhejiang University, Tencent AI Lab, Westlake University
    - 📅 Date: January 24, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [evaluation], [WebVoyager], [automatic judging]
    - 📖 TLDR: Presents WebVoyager, an end-to-end multimodal web agent evaluated on realistic tasks across 15 live websites. The paper is notable both for the agent itself and for proposing an automatic GPT-4V-based evaluation protocol for live web-agent execution.
