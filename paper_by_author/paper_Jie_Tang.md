# Jie Tang's Papers

- [Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification](https://arxiv.org/abs/2603.26648)
    - Zehai He, Wenyi Hong, Zhen Yang, Ziyang Pan, Mingdao Liu, Xiaotao Gu, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI
    - 📅 Date: March 27, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web development], [GUI agent], [code generation], [VLM], [evaluation]
    - 📖 TLDR: Vision2Web is a hierarchical benchmark for visual website development spanning static UI-to-code, interactive frontend reproduction, and full-stack development, with a workflow-based agent verification paradigm using GUI agent verifiers and VLM judges to evaluate coding agents across 193 tasks.

- [UI‑TARS‑2 Technical Report: Advancing GUI Agent with Multi‑Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)
    - Haoming Wang, Haoyang Zou, Huatong Song, Jiazhan Feng, Junjie Fang, Junting Lu, Longxiang Liu, Qinyu Luo, Shihao Liang, Shijue Huang, Wanjun Zhong, Yining Ye, Yujia Qin, Yuwen Xiong, Yuxin Song, Zhiyong Wu, Aoyan Li, Bo Li, Chen Dun, Chong Liu, Daoguang Zan, Fuxing Leng, Hanbin Wang, Hao Yu, Haobin Chen, Hongyi Guo, Jing Su, Jingjia Huang, Kai Shen, Kaiyu Shi, Lin Yan, Peiyao Zhao, Pengfei Liu, Qinghao Ye, Renjie Zheng, Shulin Xin, Wayne Xin Zhao, Wen Heng, Wenhao Huang, Wenqian Wang, Xiaobo Qin, Yi Lin, Youbin Wu, Zehui Chen, Zihao Wang, Baoquan Zhong, Xinchun Zhang, Xujing Li, Yuanfan Li, Zhongkai Zhao, Chengquan Jiang, Faming Wu, Haotian Zhou, Jinlin Pang, Li Han, Qi Liu, Qianli Ma, Siyao Liu, Songhua Cai, Wenqi Fu, Xin Liu, Yaohui Wang, Zhi Zhang, Bo Zhou, Guoliang Li, Jiajun Shi, Jiale Yang, Jie Tang, Li Li, Qihua Han, Taoran Lu, Woyu Lin, Xiaokang Tong, Xinyao Li, Yichi Zhang, Yu Miao, Zhengxuan Jiang, Zili Li, Ziyuan Zhao, Chenxin Li, Dehua Ma, Feng Lin, Ge Zhang, Haihua Yang, Hangyu Guo, Hongda Zhu, Jiaheng Liu, Junda Du, Kai Cai, Kuanye Li, Lichen Yuan, Meilan Han, Minchao Wang, Shuyue Guo, Tianhao Cheng, Xiaobo Ma, Xiaojun Xiao, Xiaolong Huang, Xinjie Chen, Yidi Du, Yilin Chen, Yiwen Wang, Zhaojian Li, Zhenzhu Yang, Zhiyuan Zeng, Chaolin Jin, Chen Li, Hao Chen, Haoli Chen, Jian Chen, Qinghao Zhao, Guang Shi
    - 🏛️ Institutions: ByteDance Seed
    - 📅 Date: September 02, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [reinforcement learning], [UI‑TARS‑2]
    - 📖 TLDR: UI‑TARS‑2 is a newly trained native GUI‑centered agent that uses a scalable data flywheel, stabilized multi‑turn reinforcement learning, hybrid GUI + terminal environments, and a unified sandbox. It achieves leading performance across diverse GUI benchmarks (e.g., 88.2 on Online‑Mind2Web), game tasks (~60% human-level), and generalizes to information-seeking and software engineering tasks. Training dynamics and parameter interpolation offer insights into robust, efficient agent RL at scale.

- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
    - Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Z.AI, University of Chinese Academy of Sciences
    - 📅 Date: August 19, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [framework], [model], [benchmark], [API-GUI paradigm], [dataset], [distributed RL], [entropulse]
    - 📖 TLDR: This paper presents **ComputerRL**, a large-scale end-to-end reinforcement learning framework enabling agents to operate complex desktop tasks. It introduces the **API-GUI paradigm**, combining programmatic API calls with GUI actions, and a **distributed RL infrastructure** managing thousands of parallel virtual Ubuntu desktops for scalable training. A novel **Entropulse** training strategy alternates between reinforcement learning and supervised fine-tuning to prevent entropy collapse over long training runs. Applied to open models like GLM-4-9B-0414, ComputerRL achieves a new state-of-the-art success rate of **48.9%** on the OSWorld benchmark via the GLM-ComputerRL-9B model.

- [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://openreview.net/forum?id=oVKEAFjEqv)
    - Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Jiadai Sun, Xinyue Yang, Yu Yang, Shuntian Yao, Wei Xu, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Shanghai Qi Zhi Institute
    - 📅 Date: November 04, 2024
    - 📑 Publisher: ICLR 2025 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [reinforcement learning], [self-evolving curriculum], [WebRL], [outcome-supervised reward model]
    - 📖 TLDR: This paper introduces *WebRL*, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open large language models (LLMs). WebRL addresses challenges such as the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. It incorporates a self-evolving curriculum that generates new tasks from unsuccessful attempts, a robust outcome-supervised reward model (ORM), and adaptive reinforcement learning strategies to ensure consistent improvements. Applied to Llama-3.1 and GLM-4 models, WebRL significantly enhances their performance on web-based tasks, surpassing existing state-of-the-art web agents.

- [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://aclanthology.org/2025.acl-long.107/)
    - Yifan Xu, Xiao Liu, Xueqiao Sun, Siyi Cheng, Hao Yu, Hanyu Lai, Shudan Zhang, Dan Zhang, Jie Tang, Yuxiao Dong
    - 🏛️ Institutions: Tsinghua University, Peking University, Zhipu AI
    - 📅 Date: October 31, 2024
    - 📑 Publisher: ACL 2025
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [benchmark], [AndroidLab]
    - 📖 TLDR: This paper introduces **AndroidLab**, a comprehensive framework for training and systematically benchmarking Android autonomous agents. It provides an operational environment with diverse modalities and action spaces, supporting both large language models (LLMs) and multimodal models (LMMs). The benchmark includes 138 tasks across nine apps on predefined Android virtual devices. Utilizing AndroidLab, the authors developed an Android Instruction dataset and trained six open-source LLMs and LMMs, significantly improving their average success rates.

- [AutoGLM: Autonomous Foundation Agents for GUIs](https://arxiv.org/abs/2411.00820)
    - Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long Iong, Jiadai Sun, Jiaqi Wang, Junjie Gao, Junjun Shan, Kangning Liu, Shudan Zhang, Shuntian Yao, Siyi Cheng, Wentao Yao, Wenyi Zhao, Xinghan Liu, Xinyi Liu, Xinying Chen, Xinyue Yang, Yang Yang, Yifan Xu, Yu Yang, Yujia Wang, Yulin Xu, Zehan Qi, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu AI, Tsinghua University
    - 📅 Date: October 25, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [model], [learning], [AutoGLM]
    - 📖 TLDR: This paper introduces AutoGLM, a new series in the ChatGLM family, designed as foundation agents for autonomous control of digital devices through GUIs. It addresses the challenges foundation models face in decision-making within dynamic environments by developing agents capable of learning through autonomous interactions. Focusing on web browsers and Android devices, AutoGLM integrates various techniques to create deployable agent systems. Key insights include the importance of designing an appropriate "intermediate interface" for GUI control and a novel progressive training framework for self-evolving online curriculum reinforcement learning. Evaluations demonstrate AutoGLM's effectiveness across multiple domains, achieving notable success rates in web browsing and Android device control tasks.

- [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/eea71dc576381b88f2a0ca4dedc2140d-Abstract-Conference.html)
    - Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Song XiXuan, Yifan Xu, Shudan Zhang, Hanyu Lai, Jiadai Sun, Xinyue Yang, Yu Yang, Zehan Qi, Shuntian Yao, Xueqiao Sun, Siyi Cheng, Qinkai Zheng, Hao Yu, Hanchen Zhang, Wenyi Hong, Ming Ding, Lihang Pan, Xiaotao Gu, Aohan Zeng, Zhengxiao Du, Chan Hee Song, Yu Su, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Microsoft Research Asia, The Ohio State University
    - 📅 Date: August 12, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [dataset], [GUI], [embodied], [visual design], [VisualAgentBench], [VAB]
    - 📖 TLDR: The authors introduce *VisualAgentBench (VAB)*, a comprehensive benchmark designed to train and evaluate large multimodal models (LMMs) as visual foundation agents across diverse scenarios, including embodied tasks, graphical user interfaces, and visual design. VAB comprises five distinct environments that systematically challenge LMMs' understanding and interaction capabilities. Additionally, the benchmark offers supervised fine-tuning trajectory data for behavior cloning training, demonstrating the potential to improve open LMMs for serving as visual foundation agents.

- [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://dl.acm.org/doi/10.1145/3637528.3671620)
    - Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences
    - 📅 Date: April 04, 2024
    - 📑 Publisher: KDD 2024
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [benchmark], [reinforcement learning], [web navigation], [AutoWebBench], [ChatGLM3-6B]
    - 📖 TLDR: AutoWebGLM introduces a web navigation agent based on ChatGLM3-6B, designed to autonomously navigate and interact with webpages for complex tasks. The paper highlights a two-phase data construction approach using a hybrid human-AI methodology for diverse, curriculum-based web task training. It also presents AutoWebBench, a benchmark for evaluating agent performance in web tasks, and uses reinforcement learning to fine-tune operations, addressing complex webpage interaction and grounding.

- [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html)
    - Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Tsinghua University, The Ohio State University, ByteDance
    - 📅 Date: January 01, 2024
    - 📑 Publisher: ICLR 2024
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [evaluation]
    - 📖 TLDR: AgentBench provides a comprehensive benchmark for evaluating LLMs as autonomous agents in various environments. It includes eight distinct scenarios, testing the LLMs' reasoning and decision-making capabilities in tasks such as OS interaction, database querying, knowledge graph traversal, and more. This benchmark compares the effectiveness of multiple commercial and open-source LLMs, revealing areas of improvement in instruction-following and long-term reasoning, essential for practical agent development.
