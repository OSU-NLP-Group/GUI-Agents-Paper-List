# Papers with Keyword: chain-of-thought

- [Say One Thing, Do Another? Diagnosing Reasoning‑Execution Gaps in VLM‑Powered Mobile‑Use Agents](https://arxiv.org/abs/2510.02204)
    - Lingzhong Dong, Ziqi Zhou, Shuaibo Yang, Haiyue Sheng, Pengzhou Cheng, Zongru Wu, Zheng Wu, Gongshen Liu, Zhuosheng Zhang
    - 🏛️ Institutions: SJTU, BIT
    - 📅 Date: October 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [mobile]
    - 🔑 Key: [evaluation framework], [Ground-Truth Alignment], [reasoning-execution gap], [chain-of-thought], [VLM]
    - 📖 TLDR: This paper investigates reasoning-execution mismatches in VLM-powered mobile agents, revealing that models often generate correct reasoning but fail in execution. It introduces an evaluation framework combining execution accuracy and a new metric called Ground-Truth Alignment (GTA). The authors identify two types of errors—Execution Gap and Reasoning Gap—and show that model scaling alleviates but does not resolve these issues.

- [Ferret-UI Lite: Lessons from Building Small On-Device GUI Agents](https://arxiv.org/abs/2509.26539)
    - Zhen Yang, Zi-Yi Dou, Di Feng, Forrest Huang, Anh Nguyen, Keen You, Omar Attia, Yuhao Yang, Michael Feng, Haotian Zhang, Ram Ramrakhya, Chao Jia, Jeffrey Nichols, Alexander Toshev, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: September 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [reinforcement learning], [chain-of-thought], [visual tool-use]
    - 📖 TLDR: This paper presents **Ferret-UI Lite**, a compact 3B end-to-end GUI agent designed for on-device deployment across mobile, web, and desktop. It introduces a mixed real and synthetic GUI dataset, a two-stage training pipeline combining supervised fine-tuning and reinforcement learning with verifiable rewards, and inference-time reasoning and visual cropping strategies. Ferret-UI Lite achieves strong grounding accuracy (91.6% on ScreenSpot-V2) and promising task success rates (28.0% on AndroidWorld, 19.8% on OSWorld), illustrating both the opportunities and challenges of building efficient on-device GUI agents.

- [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123)
    - Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole Guo, Yiheng Xu, Chen Henry Wu, Zhennan Shen, Zhuokai Li, Ryan Li, Xiaochuan Li, Junda Chen, Boyuan Zheng, Peihang Li, Fangyu Lei, Ruisheng Cao, Yeqiao Fu, Dongchan Shin, Martin Shin, Jiarui Hu, Yuyan Wang, Jixuan Chen, Yuxiao Ye, Danyang Zhang, Dikang Du, Hao Hu, Huarong Chen, Zaida Zhou, Haotian Yao, Ziwei Chen, Qizheng Gu, Yipu Wang, Heng Wang, Diyi Yang, Victor Zhong, Flood Sung, Y. Charles, Zhilin Yang, Tao Yu
    - 🏛️ Institutions: XLANG Lab (HKU), Moonshot AI, Stanford, University of Waterloo, Carnegie Mellon University
    - 📅 Date: August 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [dataset], [benchmark], [chain-of-thought], [vision-language-model], [AgentNet]
    - 📖 TLDR: Introduces **OpenCUA**, an open-source framework to train computer-use agents (CUAs) using vision-language models. It includes a cross-platform annotation tool (AgentNet Tool), a large-scale dataset covering 3 OSes and 200+ apps/websites (AgentNet), and a data processing pipeline that builds state–action pairs enhanced with reflective long chain-of-thought reasoning. The resulting models—especially OpenCUA-32B—achieve SOTA performance on the OSWorld-Verified benchmark (34.8% success), surpassing OpenAI’s GPT-4o CUA and demonstrating strong generalization and scalability. All tools, models, and data are publicly released. :contentReference[oaicite:4]{index=4}

- [In-Context Defense in Computer Agents: An Empirical Study](https://arxiv.org/abs/2503.09241)
    - Pei Yang, Hai Ci, Mike Zheng Shou
    - 🏛️ Institutions: Unknown
    - 📅 Date: March 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [defense], [in-context learning], [chain-of-thought], [context deception], [security]
    - 📖 TLDR: This paper introduces an in-context defense strategy for computer agents powered by vision-language models (VLMs), targeting context deception attacks such as malicious pop-ups and deceptive HTML elements. By incorporating a small set of curated exemplars and employing chain-of-thought reasoning, the approach guides agents to perform explicit defensive reasoning before action planning. Experiments demonstrate significant reductions in attack success rates across various attack types, highlighting the effectiveness of the method in enhancing agent reliability without requiring model fine-tuning.
