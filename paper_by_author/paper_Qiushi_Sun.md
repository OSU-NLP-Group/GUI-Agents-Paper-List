# Qiushi Sun's Papers

- [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221)
    - Zhaoyang Liu, JingJing Xie, Zichen Ding, Zehao Li, Bowen Yang, Zhenyu Wu, Xuehui Wang, Qiushi Sun, Shi Liu, Weiyun Wang, Shenglong Ye, Qingyun Li, Zeyue Tian, Gen Luo, Xiangyu Yue, Biqing Qi, Kai Chen, Bowen Zhou, Yu Qiao, Qifeng Chen, Wenhai Wang
    - 🏛️ Institutions:Shanghai AI Lab
    - 📅 Date: September 18, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [dataset], [model], [ScaleCUA]
    - 📖 TLDR: This paper presents **ScaleCUA**, a large-scale open-source project for training general-purpose computer use agents (CUAs). The dataset spans 6 operating systems and 3 task domains, built using a hybrid pipeline combining automated agents with human experts. ScaleCUA supports tasks like GUI understanding, grounding, and full interaction. The trained models outperform baselines and set new SOTA on key benchmarks like WebArena-Lite-v2 and MMBench-GUI. The authors also release the full dataset, models, and codebase to promote further research in GUI-based agents.



- [UI‑TARS‑2 Technical Report: Advancing GUI Agent with Multi‑Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)
    - Haoming Wang, Haoyang Zou, Huatong Song, Jiazhan Feng, Junjie Fang, Junting Lu, Longxiang Liu, Qinyu Luo, Shihao Liang, Shijue Huang, Wanjun Zhong, Yining Ye, Yujia Qin, Yuwen Xiong, Yuxin Song, Zhiyong Wu, Aoyan Li, Bo Li, Chen Dun, Chong Liu, Daoguang Zan, Fuxing Leng, Hanbin Wang, Hao Yu, Haobin Chen, Hongyi Guo, Jing Su, Jingjia Huang, Kai Shen, Kaiyu Shi, Lin Yan, Peiyao Zhao, Pengfei Liu, Qinghao Ye, Renjie Zheng, Shulin Xin, Wayne Xin Zhao, Wen Heng, Wenhao Huang, Wenqian Wang, Xiaobo Qin, Yi Lin, Youbin Wu, Zehui Chen, Zihao Wang, Baoquan Zhong, Xinchun Zhang, Xujing Li, Yuanfan Li, Zhongkai Zhao, Chengquan Jiang, Faming Wu, Haotian Zhou, Jinlin Pang, Li Han, Qi Liu, Qianli Ma, Siyao Liu, Songhua Cai, Wenqi Fu, Xin Liu, Yaohui Wang, Zhi Zhang, Bo Zhou, Guoliang Li, Jiajun Shi, Jiale Yang, Jie Tang, Li Li, Qihua Han, Taoran Lu, Woyu Lin, Xiaokang Tong, Xinyao Li, Yichi Zhang, Yu Miao, Zhengxuan Jiang, Zili Li, Ziyuan Zhao, Chenxin Li, Dehua Ma, Feng Lin, Ge Zhang, Haihua Yang, Hangyu Guo, Hongda Zhu, Jiaheng Liu, Junda Du, Kai Cai, Kuanye Li, Lichen Yuan, Meilan Han, Minchao Wang, Shuyue Guo, Tianhao Cheng, Xiaobo Ma, Xiaojun Xiao, Xiaolong Huang, Xinjie Chen, Yidi Du, Yilin Chen, Yiwen Wang, Zhaojian Li, Zhenzhu Yang, Zhiyuan Zeng, Chaolin Jin, Chen Li, Hao Chen, Haoli Chen, Jian Chen, Qinghao Zhao, Guang Shi
    - 🏛️ Institutions: ByteDance Seed
    - 📅 Date: September 2, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [UI‑TARS‑2]
    - 📖 TLDR: UI‑TARS‑2 is a newly trained native GUI‑centered agent that uses a scalable data flywheel, stabilized multi‑turn reinforcement learning, hybrid GUI + terminal environments, and a unified sandbox. It achieves leading performance across diverse GUI benchmarks (e.g., 88.2 on Online‑Mind2Web), game tasks (~60% human-level), and generalizes to information-seeking and software engineering tasks. Training dynamics and parameter interpolation offer insights into robust, efficient agent RL at scale.

- [Breaking the Data Barrier -- Building GUI Agents Through Task Generalization](https://arxiv.org/abs/2504.10127)
    - Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, Qiushi Sun, Zhenzhong Lan, Junxian He
    - 🏛️ Institutions: ZJU, WestlakeU, Shanghai AI Lab, HKU, HKUST
    - 📅 Date: April 14, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [dataset], [benchmark], [mid-training], [reasoning], [GUIMid]
    - 📖 TLDR: This paper introduces a mid-training approach to enhance GUI agents by leveraging diverse, reasoning-intensive datasets such as mathematical and coding tasks. The authors demonstrate that training Vision Language Models (VLMs) on these data-rich tasks before fine-tuning on limited GUI trajectory data significantly improves performance on GUI benchmarks like WebArena and AndroidWorld. Notably, text-only mathematical reasoning data led to substantial cross-modal gains, highlighting the effectiveness of task generalization in overcoming data scarcity challenges in GUI agent development.

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

- [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603)
    - Chengyou Jia, Minnan Luo, Zhuohang Dang, Qiushi Sun, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu
    - 🏛️ Institutions: XJTU, Shanghai AI Lab, HKU
    - 📅 Date: October 24, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [multi-agent systems], [specialized generalist agent], [OSWorld benchmark]
    - 📖 TLDR: AgentStore introduces a scalable platform to integrate and manage heterogeneous agents, designed to enhance generalist assistant capabilities for diverse computer tasks. Using a MetaAgent and AgentToken strategy, AgentStore shows improved generalization on the OSWorld benchmark.

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
