# Kanzhi Cheng's Papers

- [GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents](https://arxiv.org/abs/2506.03143)
    - Qianhui Wu, Kanzhi Cheng, Rui Yang, Chaoyun Zhang, Jianwei Yang, Huiqiang Jiang, Jian Mu, Baolin Peng, Bo Qiao, Reuben Tan, Si Qin, Lars Liden, Qingwei Lin, Huan Zhang, Tong Zhang, Jianbing Zhang, Dongmei Zhang, Jianfeng Gao
    - 🏛️ Institutions: Microsoft, Nanjing Univ., UIUC
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv (α); (likely under review / not yet accepted)
    - 💻 Env: [GUI] (applies across web/mobile/desktop)
    - 🔑 Key: [model], [framework], [grounding verifier], [attention mechanism], [coordinate‑free grounding], [GUI‑Actor]
    - 📖 TLDR: GUI‑Actor introduces a coordinate‑free visual grounding approach for GUI agents by adding an attention‑based “<ACTOR>” action head atop a frozen vision‑language model. It learns to align with relevant visual patches and produces multiple candidate regions per forward pass. An optional grounding verifier scores candidates to select the best. The method improves spatial‑semantic alignment and generalizes well across unseen resolutions. On benchmarks like ScreenSpot‑Pro, GUI‑Actor‑7B outperforms prior SOTA UI‑TARS‑72B, with verifier‑augmented versions achieving even higher accuracy—while only fine‑tuning ~100 M parameters.


- [DeepShop: A Benchmark for Deep Research Shopping Agents](https://arxiv.org/abs/2506.02839)
    - Yougang Lyu, Xiaoyu Zhang, Lingyong Yan, Maarten de Rijke, Zhaochun Ren, Xiuying Chen
    - 🏛️ Institutions: U Amsterdam, Shandong U, Baidu Inc., Leiden U, MBZUAI
    - 📅 Date: June 3, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [dataset], [evaluation framework], [RAG], [query complexity], [DeepShop]
    - 📖 TLDR: DeepShop introduces a comprehensive benchmark for web shopping agents, mirroring the real first-use complexity of online shopping scenarios. It features diversified query evolution across five domains, complexity-tier classification (easy/medium/hard), and a fine‐grained scoring system analyzing attribute matching, filters, and sorting. Evaluations across RAG and agentic systems reveal significant shortcomings, especially in handling filters and sorting, underscoring gaps in current research capabilities.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://qiushisun.github.io/OS-Genesis-Home/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Lab, HKU, Johns Hopkins University, SJTU, Oxford, HKUST
    - 📅 Date: Dec 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [trajectory data], [reward model], [e2e model], [data synthesis], [OS-Genesis]
    - 📖 TLDR: This paper introduces *OS-Genesis*, an interaction-driven pipeline that automates the construction of high-quality and diverse GUI agent trajectory data without human supervision. By employing reverse task synthesis and a trajectory reward model, OS-Genesis enables effective end-to-end training of GUI agents, significantly enhancing their performance on online benchmarks.

- [OS-ATLAS: A Foundation Action Model For Generalist GUI Agents](https://osatlas.github.io/)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Lab, SJTU, HKU, MIT
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [OS-Atlas]
    - 📖 TLDR: This paper introduces OS-Atlas, a foundational GUI action model designed to enhance GUI grounding and out-of-distribution tasks. The authors developed a toolkit to synthesize multi-platform GUI grounding data, resulting in a cross-platform corpus of over 13 million GUI elements. OS-Atlas demonstrates significant performance improvements across six benchmarks spanning mobile, desktop, and web platforms.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Yantao Li, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: Nanjing University, Shanghai AI Lab
    - 📅 Date: January 19, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [benchmark], [GUI grounding], [visual grounding]
    - 📖 TLDR: TBD.

- [Interactive Evolution: A Neural-Symbolic Self-Training Framework For Large Language Models](https://arxiv.org/abs/2406.11736)
    - Fangzhi Xu, Qiushi Sun, Kanzhi Cheng, Jun Liu, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Xi'an Jiaotong University, Shanghai AI Lab, HKU, Nanjing University
    - 📅 Date: November 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI (evaluated on web, math reasoning, and logic reasoning environments)]
    - 🔑 Key: [framework], [dataset], [neural-symbolic self-training], [online exploration], [self-refinement]
    - 📖 TLDR: This paper introduces *ENVISIONS*, a neural-symbolic self-training framework designed to improve large language models (LLMs) by enabling self-training through interaction with a symbolic environment. The framework addresses symbolic data scarcity and enhances LLMs' symbolic reasoning proficiency by iteratively exploring, refining, and learning from symbolic tasks without reinforcement learning. Extensive evaluations across web navigation, math, and logical reasoning tasks highlight *ENVISIONS* as a promising approach for enhancing LLM symbolic processing.
