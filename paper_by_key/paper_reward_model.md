# Papers with Keyword: reward model

- [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191)
    - Zehao Li, Zhenyu Wu, Yibo Zhao, Bowen Yang, Jingjing Xie, Zhaoyang Liu, Zhoumianze Liu, Kaiming Jin, Jianze Liang, Zonglin Li, Feng Wu, Bowen Zhou, Zun Wang, Zichen Ding
    - 🏛️ Institutions: University of Science and Technology of China, Shanghai AI Laboratory, CUHK MMLab, HKUST, NUS
    - 📅 Date: March 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [reinforcement learning], [critic framework], [OmniGUIRewardBench], [milestone decomposition], [OS-Themis]
    - 📖 TLDR: OS-Themis is a scalable critic framework for GUI reward modeling that breaks trajectories into verifiable milestones and audits the evidence chain before issuing a verdict. It improves AndroidWorld training and filtering loops and introduces OmniGUIRewardBench as a cross-platform benchmark for GUI outcome rewards.

- [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178)
    - Linxin Song, Jieyu Zhang, Huanxin Sheng, Taiwei Shi, Gupta Rahul, Yang Liu, Ranjay Krishna, Jian Kang, Jieyu Zhao
    - 🏛️ Institutions: University of Southern California, University of Washington, MBZUAI, Amazon AGI
    - 📅 Date: March 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [reward model], [execution video], [trajectory evaluation], [spatiotemporal token pruning], [ExeVR-53k], [ExeVRM]
    - 📖 TLDR: This paper studies reward modeling from execution video rather than agent internals, introducing the ExeVR-53k dataset and an execution-video reward model that predicts success from keyframes plus the user instruction. The model scales evaluation across Ubuntu, macOS, Windows, and Android, outperforming strong proprietary models while providing finer temporal attribution.

- [MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux](https://arxiv.org/abs/2601.13060)
    - Zecheng Li, Zhihui Cao, Wenke Huang, Yudong Zhang, Keying Qi, Rui Wang, Zeyu Zheng, Jian Zhao, Hao Zhu, Hengxin Wu, Yuran Wang, Guitao Fan, Guokun Wu, Yicong Liu, Zhilin Gao, Haikun Xu, He Yang, Minqi Xiang, Xingyu Liu, Zuojian Wang
    - 🏛️ Institutions: Honor Device Co., Ltd.
    - 📅 Date: January 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [multi-agent system], [data construction], [data reflux], [MagicGUI-RMS]
    - 📖 TLDR: MagicGUI-RMS combines a domain-specific reward model with a general-purpose reward model to score GUI trajectories, propose corrections, and feed improved data back into later training rounds. It also introduces an automated reward-data construction pipeline and reports gains in task accuracy and behavioral robustness.

- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596)
    - Haojia Lin, Xiaoyu Tan, Yulei Qin, Zihan Xu, Yuchen Shi, Zongyi Li, Gang Li, Shaofei Cai, Siqi Cai, Chaoyou Fu, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, PKU, Nanjing University
    - 📅 Date: October 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [reward model], [outcome reward model], [process reward model], [expert annotation], [CUARewardBench], [UPE]
    - 📖 TLDR: CUARewardBench benchmarks both outcome and process reward models for desktop computer-use evaluation using expert-annotated trajectories from 10 software categories and 7 agent architectures. It shows that current reward models are still unreliable and introduces Unanimous Prompt Ensemble (UPE) to improve reward-model precision.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [reward model], [self-improvement], [outcome verification], [UI-Genie]
    - 📖 TLDR: UI-Genie targets two mobile-agent bottlenecks: reliable outcome verification and scalable high-quality training data. It combines an interleaved reward model with a reward-guided self-improvement loop, releases reward-specific GUI datasets, and reports stronger mobile-agent performance across multiple rounds of self-improvement.

- [ProgRM: Build Better GUI Agents with Progress Rewards](https://arxiv.org/abs/2505.18121)
    - Danyang Zhang, Situo Zhang, Ziyue Yang, Zichen Zhu, Zihan Zhao, Ruisheng Cao, Lu Chen, Kai Yu
    - 🏛️ Institutions: X-LANCE Lab, School of Computer Science, MoE Key Lab of Artificial Intelligence, SJTU AI Institute, Shanghai Jiao Tong University, Jiangsu Key Lab of Language Computing, Suzhou Laboratory
    - 📅 Date: May 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [reward model], [progress reward], [dense rewards], [LCS self-annotation], [ProgRM]
    - 📖 TLDR: ProgRM studies how to replace coarse outcome-only rewards with dense step-level progress signals for GUI-agent reinforcement learning. It uses an LCS-based self-annotation method to assign progress labels from successful trajectories and shows that progress rewards outperform outcome reward models across GUI benchmarks.

- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277)
    - Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
    - 🏛️ Institutions: Yonsei University, CMU
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [dataset], [benchmark], [reward model], [WebRewardBench], [Web-Shepherd]
    - 📖 TLDR: Web-Shepherd introduces the first process reward model specialized for web navigation, along with the WebPRM Collection of 40K step-level preference pairs and the WebRewardBench meta-evaluation benchmark. It substantially outperforms generic frontier-model verifiers on web trajectories while reducing verification cost enough for both RL training and test-time use.

- [A3: Android Agent Arena for Mobile GUI Agents with Essential-State Procedural Evaluation](https://arxiv.org/abs/2501.01149)
    - Yuxiang Chai, Shunye Tang, Han Xiao, Weifeng Lin, Hanhao Li, Jiayu Zhang, Liang Liu, Pengxiang Zhao, Guangyi Liu, Guozhi Wang, Shuai Ren, Rongduo Han, Haining Zhang, Siyuan Huang, Hongsheng Li
    - 🏛️ Institutions: MMLab @ CUHK, EE department @ CUHK, vivo AI Lab, Shanghai Jiao Tong University
    - 📅 Date: January 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [essential-state evaluation], [procedural evaluation], [reward model], [A3]
    - 📖 TLDR: A3 is a mobile GUI benchmark built from 100 tasks over 20 dynamic online Android apps to evaluate agents beyond static or offline settings. Its essential-state procedural evaluation uses MLLMs as reward models to verify both intermediate progress and final completion on real online apps.

- [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://aclanthology.org/2025.acl-long.277/)
    - Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu
    - 🏛️ Institutions: Shanghai AI Laboratory, HKU, Johns Hopkins University, Shanghai Jiao Tong University, Oxford, HKUST
    - 📅 Date: December 27, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [dataset], [trajectory synthesis], [reverse task synthesis], [reward model], [OS-Genesis]
    - 📖 TLDR: OS-Genesis tackles the lack of high-quality GUI trajectories by synthesizing them without preset tasks or human demonstrations. It first explores with step-level interactions, then retrospectively derives tasks and filters the resulting trajectories with a reward model, producing more diverse training data for GUI agents.
