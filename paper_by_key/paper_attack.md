# Papers with Keyword: attack

- [Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?](https://arxiv.org/abs/2601.12349)
    - Yi Qian, Kunwei Qian, Xingbang He, Ligeng Chen, Jikang Zhang, Tiantai Zhang, Haiyang Wei, Linzhang Wang, Hao Wu, Bing Mao
    - 🏛️ Institutions: State Key Laboratory for Novel Software Technology, Nanjing University, Honor Device Co., Ltd., Institute of Dataspace, Hefei Comprehensive National Science Center
    - 📅 Date: January 18, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [security], [attack], [Android], [Action Rebinding], [verification gates]
    - 📖 TLDR: This paper introduces Action Rebinding, a zero-permission Android attack that exploits the observation-to-action gap in multimodal GUI agents by changing foreground UI state before the planned action executes. Across six agents and 15 tasks it achieves 100% atomic rebinding success, and with intent alignment can also bypass confirmation-style verification gates.

- [Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming](https://arxiv.org/abs/2510.18314)
    - Zheng Zhang, Jiarui He, Yuchen Cai, Deheng Ye, Peilin Zhao, Ruili Feng, Hao Wang
    - 🏛️ Institutions: The Hong Kong University of Science and Technology (Guangzhou), Tencent, Shanghai Jiao Tong University, Alibaba Group
    - 📅 Date: October 21, 2025
    - 📑 Publisher: ICME 2026
    - 💻 Env: [Web]
    - 🔑 Key: [safety], [attack], [prompt injection], [genetic algorithm], [red-teaming], [Genesis]
    - 📖 TLDR: Genesis studies automated red-teaming for web agents by evolving attack strategies over repeated interactions instead of relying on fixed prompts or manually designed attacks. Its attacker-scorer-strategist loop builds and reuses a growing strategy library, yielding stronger adversarial injections across web tasks.

- [VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents](https://arxiv.org/abs/2506.02456)
    - Tri Cao, Bennett Lim, Yue Liu, Yuan Sui, Yuexin Li, Shumin Deng, Lin Lu, Nay Oo, Shuicheng Yan, Bryan Hooi
    - 🏛️ Institutions: National University of Singapore, Cyber Emerging Tech and R&D
    - 📅 Date: June 03, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [visual prompt injection], [security], [attack], [browser-use agents], [VPI-Bench]
    - 📖 TLDR: VPI-Bench studies visual prompt injection attacks on computer-use agents, where malicious instructions are embedded directly into rendered user interfaces rather than hidden in HTML. Across 306 cases on five platforms, it shows that both full-system-access CUAs and browser-use agents remain highly vulnerable, and that prompt-only defenses offer limited protection.

- [WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)
    - Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, Neil Zhenqiang Gong
    - 🏛️ Institutions: Duke University
    - 📅 Date: May 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [prompt injection], [attack], [adversarial attack], [multimodal LLM], [security]
    - 📖 TLDR: WebInject proposes a prompt injection attack against MLLM-based web agents by adding optimized pixel-level perturbations to rendered webpages, using a neural network to approximate the non-differentiable webpage-to-screenshot mapping and projected gradient descent to find perturbations that induce attacker-specified actions.

- [sudo rm -rf agentic_security](https://arxiv.org/abs/2503.20279)
    - Sejin Lee, Jian Kim, Haon Park, Ashkan Yousefpour, Sangyoon Yu, Min Song
    - 🏛️ Institutions: Aim Intelligence, Yonsei University, SNU
    - 📅 Date: March 26, 2025
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop]
    - 🔑 Key: [security], [attack], [jailbreaking], [safety]
    - 📖 TLDR: SUDO (Screen-based Universal Detox2Tox Offense) is a novel attack framework that bypasses refusal-trained safeguards in commercial CUAs (e.g., Claude Computer Use) by transforming harmful requests into seemingly benign ones via a Detox2Tox mechanism, exposing critical vulnerabilities in CUA safety.

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
    - Yanzhe Zhang, Tao Yu, Diyi Yang
    - 🏛️ Institutions: Georgia Institute of Technology, The University of Hong Kong, Stanford University
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [attack], [adversarial pop-ups], [safety], [OSWorld], [VisualWebArena]
    - 📖 TLDR: Shows that vision-language computer agents can be reliably distracted by adversarial pop-ups that human users would typically ignore. On OSWorld and VisualWebArena, these pop-ups achieve high attack success rates and sharply reduce task completion, while simple defenses like warning prompts remain ineffective.

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

- [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Abstract-Conference.html)
    - Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
    - 🏛️ Institutions: Renmin University of China, Peking University, Tencent
    - 📅 Date: February 17, 2024
    - 📑 Publisher: NeurIPS 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [attack], [backdoor], [agent security], [trigger placement]
    - 📖 TLDR: Studies backdoor attacks against LLM-based agents by categorizing them according to trigger placement and attack outcome. The paper shows that agent pipelines introduce distinct backdoor surfaces that are not captured by standard single-model safety evaluation.
