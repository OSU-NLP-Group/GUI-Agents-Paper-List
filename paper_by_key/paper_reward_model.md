# Papers with Keyword: reward model

- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596)
    - Haojia Lin, Xiaoyu Tan, Yulei Qin, Zihan Xu, Yuchen Shi, Zongyi Li, Gang Li, Shaofei Cai, Siqi Cai, Chaoyou Fu, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, PKU, NJU
    - 📅 Date: October 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [reward model], [computer-using agent], [CUARewardBench], [Unanimous Prompt Ensemble (UPE)]
    - 📖 TLDR: This paper introduces CUARewardBench, the first benchmark for evaluating reward models tailored to computer-using agents. It includes step-level and trajectory-level annotations from tasks across 10 software types and 7 agent architectures. The study identifies the limitations of current reward models and proposes UPE, a prompting-based method that significantly improves evaluation accuracy.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, SJTU AI Institute, Shanghai Jiao Tong University, Jiangsu Key Lab of Language Computing, Suzhou Laboratory
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [reinforcement learning], [reward model], [progress reward], [LCS], [ProgRM]
    - 📖 TLDR: Introduces **ProgRM**, a novel framework giving dense intermediate rewards to GUI agents by estimating per‑step task progress. Labels are generated through an LCS‑based self‑annotation algorithm that identifies key steps in successful trajectories. Agents trained with ProgRM outperform outcome‑based reward models and proprietary LLMs like Claude‑3.7‑Sonnet across benchmarks.

- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277)
    - Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
    - 🏛️ Institutions: Georgia Institute of Technology, Yonsei University, Carnegie Mellon University
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [reward model], [web agent], [benchmark], [WebRewardBench], [Web-Shepherd]
    - 📖 TLDR: This paper introduces Web-Shepherd, the first process reward model specialized for web navigation, together with WebPRM Collection and WebRewardBench for training and meta-evaluating web-agent reward models. It shows that a compact specialized verifier can substantially outperform generic frontier models as web-trajectory evaluators while costing much less. The work is directly relevant to reinforcing web agents because it provides both the reward model and the evaluation infrastructure needed for scalable RL or test-time verification.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://qiushisun.github.io/OS-Genesis-Home/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Lab, HKU, Johns Hopkins University, SJTU, Oxford, HKUST
    - 📅 Date: Dec 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [trajectory data], [reward model], [e2e model], [data synthesis], [OS-Genesis]
    - 📖 TLDR: This paper introduces *OS-Genesis*, an interaction-driven pipeline that automates the construction of high-quality and diverse GUI agent trajectory data without human supervision. By employing reverse task synthesis and a trajectory reward model, OS-Genesis enables effective end-to-end training of GUI agents, significantly enhancing their performance on online benchmarks.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337v1)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Xinyue Yang, Jiadai Sun, Yu Yang, Shuntian Yao, Tianjie Zhang, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, BAAI
    - 📅 Date: November 4, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [self-evolving curriculum], [WebRL], [outcome-supervised reward model]
    - 📖 TLDR: This paper introduces *WebRL*, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open large language models (LLMs). WebRL addresses challenges such as the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. It incorporates a self-evolving curriculum that generates new tasks from unsuccessful attempts, a robust outcome-supervised reward model (ORM), and adaptive reinforcement learning strategies to ensure consistent improvements. Applied to Llama-3.1 and GLM-4 models, WebRL significantly enhances their performance on web-based tasks, surpassing existing state-of-the-art web agents.
