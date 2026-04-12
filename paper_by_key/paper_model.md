# Papers with Keyword: model

- [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876)
    - Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang, Xiaocheng Zhang, Xin Yang, Dengchang Zhao, Jinrui Ding, Xiandi Ma, Yuchen Xie, Peng Pei, Xunliang Cai, Xipeng Qiu
    - 🏛️ Institutions: Meituan, Fudan University, Tongji University, The Hong Kong University of Science and Technology
    - 📅 Date: January 22, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [framework], [synthetic experience], [verifiable synthesis], [OSWorld], [EvoCUA]
    - 📖 TLDR: EvoCUA replaces static imitation with an evolving training loop built on verifiable task synthesis, high-throughput sandbox rollouts, and iterative policy optimization from both successful and failed trajectories. On OSWorld it reaches 56.7% success, outperforming prior open-source computer-use agents and even some leading closed-weight systems.

- [ShowUI-π: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965)
    - Siyuan Hu, Kevin Qinghong Lin, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore
    - 📅 Date: December 31, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [drag interaction], [flow-based model], [continuous action], [ScreenDrag], [ShowUI-π]
    - 📖 TLDR: ShowUI-π treats GUI dragging as a continuous dexterous-control problem rather than only discrete point prediction, while still supporting ordinary click actions in the same model. It also introduces ScreenDrag with 20K trajectories across five domains, and the 450M-parameter model outperforms much larger proprietary GUI agents on this benchmark.

- [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047)
    - Hanzhang Zhou, Xu Zhang, Panrong Tong, Jianan Zhang, Liangyu Chen, Quyu Kong, Chenglin Cai, Chen Liu, Yue Wang, Jingren Zhou, Steven Hoi
    - 🏛️ Institutions: Tongyi Lab, Alibaba Group
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile]
    - 🔑 Key: [model], [agent-user interaction], [MCP], [device-cloud collaboration], [online reinforcement learning], [MAI-UI]
    - 📖 TLDR: MAI-UI is a foundation GUI-agent family aimed at realistic deployment rather than benchmark-only optimization. It extends pure UI control with agent-user interaction, MCP tool calls, native device-cloud collaboration, and long-horizon online reinforcement learning, and sets strong results on grounding, AndroidWorld, and MobileWorld.

- [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790)
    - Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple, The University of Hong Kong
    - 📅 Date: October 20, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [hybrid action], [tool calls], [synthetic tasks], [online reinforcement learning], [UltraCUA]
    - 📖 TLDR: UltraCUA bridges low-level GUI actions and higher-level tool use in one computer-use model instead of forcing every task through clicks, typing, and scrolling alone. Its pipeline combines automated tool extraction, synthetic verifiable tasks, supervised fine-tuning, and online RL, and the resulting hybrid-action models improve both OSWorld performance and transfer to WindowsAgentArena.

- [DPO Learning with LLMs-Judge Signal for Computer Use Agents](https://arxiv.org/abs/2506.03095)
    - Man Luo, David Cobbley, Xin Su, Shachar Rosenman, Vasudev Lal, Shao-Yen Tseng, Phillip Howard
    - 🏛️ Institutions: Intel, Thoughtworks
    - 📅 Date: June 03, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [DPO], [LLM-as-Judge], [local inference], [synthetic trajectories]
    - 📖 TLDR: This paper targets privacy and compute constraints in computer-use agents by training a lightweight VLM that runs entirely on local machines. It uses an LLM-as-Judge pipeline to score synthetic GUI trajectories and construct DPO preference pairs, then shows that the resulting local agent outperforms baselines on OSWorld.

- [AgentCPM‑GUI: Building Mobile‑Use Agents with Reinforcement Fine‑Tuning](https://aclanthology.org/2025.emnlp-demos.12/)
    - Zhong Zhang, Yaxi Lu, Yikun Fu, Yupeng Huo, Shenzhi Yang, Yesai Wu, Han Si, Xin Cong, Haotian Chen, Yankai Lin, Jie Xie, Wei Zhou, Wang Xu, Yuanheng Zhang, Zhou Su, Zhongwu Zhai, Xiaoming Liu, Yudong Mei, Jianming Xu, Hongyan Tian, Chongyi Wang, Chi Chen, Yuan Yao, Zhiyuan Liu, Maosong Sun
    - 🏛️ Institutions: Tsinghua University, Renmin University of China, ModelBest
    - 📅 Date: June 02, 2025
    - 📑 Publisher: EMNLP 2025 System Demonstrations
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [benchmark], [GRPO], [grounding-aware pre-training], [CAGUI], [AgentCPM-GUI]
    - 📖 TLDR: AgentCPM-GUI is an 8B mobile GUI model aimed at robust on-device interaction, especially for Chinese and English interfaces. It combines grounding-aware pre-training, supervised trajectory imitation, and GRPO-based reinforcement fine-tuning, and reports strong results on five public benchmarks plus the newly proposed Chinese benchmark CAGUI.

- [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://arxiv.org/abs/2505.21496)
    - Han Xiao, Guozhi Wang, Yuxiang Chai, Zimu Lu, Weifeng Lin, Hao He, Lue Fan, Liuyang Bian, Rui Hu, Liang Liu, Shuai Ren, Yafei Wen, Xiaoxin Chen, Aojun Zhou, Hongsheng Li
    - 🏛️ Institutions: CUHK MMLab, vivo AI Lab, CPII under InnoHK
    - 📅 Date: May 27, 2025
    - 📑 Publisher: NeurIPS 2025 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [reward model], [self-improvement], [outcome verification], [UI-Genie]
    - 📖 TLDR: UI-Genie targets two mobile-agent bottlenecks: reliable outcome verification and scalable high-quality training data. It combines an interleaved reward model with a reward-guided self-improvement loop, releases reward-specific GUI datasets, and reports stronger mobile-agent performance across multiple rounds of self-improvement.

- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277)
    - Hyungjoo Chae, Sunghwan Kim, Junhee Cho, Seungone Kim, Seungjun Moon, Gyeom Hwangbo, Dongha Lim, Minjin Kim, Yeonjun Hwang, Minju Gwak, Dongwook Choi, Minseok Kang, Gwanhoon Im, ByeongUng Cho, Hyojun Kim, Jun Hee Han, Taeyoon Kwon, Minju Kim, Beong-woo Kwak, Dongjin Kang, Jinyoung Yeo
    - 🏛️ Institutions: Yonsei University, Carnegie Mellon University
    - 📅 Date: May 21, 2025
    - 📑 Publisher: NeurIPS 2025 (Spotlight)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [dataset], [benchmark], [reward model], [WebRewardBench], [Web-Shepherd]
    - 📖 TLDR: Web-Shepherd introduces the first process reward model specialized for web navigation, along with the WebPRM Collection of 40K step-level preference pairs and the WebRewardBench meta-evaluation benchmark. It substantially outperforms generic frontier-model verifiers on web trajectories while reducing verification cost enough for both RL training and test-time use.

- [Efficient Agent Training for Computer Use](https://arxiv.org/abs/2505.13909)
    - Yanheng He, Jiahe Jin, Pengfei Liu
    - 🏛️ Institutions: Shanghai Jiao Tong University, SII, Generative AI Research Lab (GAIR)
    - 📅 Date: May 20, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [model], [dataset], [benchmark], [trajectory augmentation], [WindowsAgentArena-V2], [PC Agent-E]
    - 📖 TLDR: This paper studies data-efficient training for desktop computer-use agents, starting from only 312 human trajectories and augmenting them with diversified action decisions sampled from Claude 3.7 Sonnet. The resulting PC Agent-E model improves strongly over the base model, surpasses Claude 3.7 Sonnet on WindowsAgentArena-V2, and releases the improved benchmark alongside the training recipe.

- [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937)
    - Gaole Dai, Shiqi Jiang, Ting Cao, Yuanchun Li, Yuqing Yang, Rui Tan, Mo Li, Lili Qiu
    - 🏛️ Institutions: Microsoft Research, NTU, AIR, Tsinghua University, HKUST
    - 📅 Date: March 20, 2025
    - 📑 Publisher: MobiCom 2026
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [verifier-driven], [discretized action space], [prefilling-only workflow], [pair-wise progress preference training], [V-Droid]
    - 📖 TLDR: V-Droid is a mobile GUI agent that uses LLMs as verifiers to score candidate actions instead of generating actions autoregressively. The paper pairs that design with a discretized action space, prefilling-only verification, and pair-wise progress preference training, reaching strong benchmark performance at 4.3 seconds per step.

- [STEVE: A Step Verification Pipeline for Computer-use Agent Training](https://arxiv.org/abs/2503.12532)
    - Fanbin Lu, Zhisheng Zhong, Ziqin Wei, Shu Liu, Chi-Wing Fu, Jiaya Jia
    - 🏛️ Institutions: CUHK, SmartMore, HKUST
    - 📅 Date: March 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [model], [step verification], [binary stepwise labels], [KTO], [STEVE]
    - 📖 TLDR: STEVE trains desktop computer-use agents from suboptimal trajectories by verifying each step against before-and-after screenshots instead of relying on expensive gold trajectories. The resulting binary step labels support KTO training of a 7B agent that outperforms supervised fine-tuning on WinAgentArena.

- [Think Twice, Click Once: Enhancing GUI Grounding via Fast and Slow Systems](https://arxiv.org/abs/2503.06470)
    - Fei Tang, Yongliang Shen, Hang Zhang, Siqi Chen, Guiyang Hou, Wenqi Zhang, Wenqiao Zhang, Kaitao Song, Weiming Lu, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, Microsoft Research Asia
    - 📅 Date: March 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [dual-system cognition], [adaptive system switching], [progressive decomposition], [Focus]
    - 📖 TLDR: Focus is a GUI grounding model that switches between fast prediction and slower analysis depending on task complexity. It decomposes grounding into summarization, focused visual analysis, and coordinate prediction, and reaches strong ScreenSpot and ScreenSpot-Pro performance with a 2B model trained on 300K examples.

- [SpiritSight Agent: Advanced GUI Agent with One Look](https://arxiv.org/abs/2503.03196)
    - Zhiyuan Huang, Ziming Cheng, Junting Pan, Zhaohui Hou, Mingjie Zhan
    - 🏛️ Institutions: SenseTime Research, Beijing University of Posts and Telecommunications, MMLab, CUHK
    - 📅 Date: March 05, 2025
    - 📑 Publisher: CVPR 2025 (Poster)
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI-Lasagne], [Universal Block Parsing], [single-screenshot inference], [SpiritSight]
    - 📖 TLDR: SpiritSight is an end-to-end GUI agent designed to act from a single screenshot while retaining strong cross-platform grounding accuracy. The paper pairs the GUI-Lasagne dataset with Universal Block Parsing to reduce dynamic-resolution ambiguity and reports gains across web, mobile, and desktop benchmarks.

- [AppVLM: A Lightweight Vision Language Model for Online App Control](https://arxiv.org/abs/2502.06395)
    - Georgios Papoudakis, Thomas Coste, Zhihao Wu, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, University College London
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [lightweight VLM], [offline-to-online training], [AndroidControl], [AndroidWorld], [AppVLM]
    - 📖 TLDR: AppVLM is a lightweight vision-language model for mobile app control that is trained first on AndroidControl and then refined with trajectories collected in AndroidWorld. It achieves the best offline action prediction among the compared baselines and matches GPT-4o on online AndroidWorld success rate while running much faster.

- [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)
    - Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng, Xin Liu, Guang Shi
    - 🏛️ Institutions: ByteDance Seed, Tsinghua University
    - 📅 Date: January 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [GUI grounding], [unified action modeling], [system-2 reasoning], [reflective online traces], [UI-TARS]
    - 📖 TLDR: UI-TARS is an end-to-end GUI agent model that acts directly from screenshots instead of relying on wrapper-style prompting workflows around proprietary models. It combines enhanced perception, unified cross-platform action modeling, deliberate multi-step reasoning, and iterative training on reflective online traces, and reports strong performance across ten-plus GUI benchmarks.

- [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/)
    - Yuhao Yang, Yue Wang, Dongxu Li, Ziyang Luo, Bei Chen, Chao Huang, Junnan Li
    - 🏛️ Institutions: The University of Hong Kong, Salesforce AI Research, Alibaba Group, Australian National University, Independent Researcher
    - 📅 Date: December 20, 2024
    - 📑 Publisher: Findings of ACL 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI grounding], [pure vision], [instruction synthesis], [context-aware grounding], [Aria-UI]
    - 📖 TLDR: Aria-UI is a GUI-grounding model that deliberately avoids HTML or AXTree inputs and instead works from pure visual observations. It pairs a scalable instruction-synthesis pipeline with interleaved textual and text-image action histories for context-aware grounding, and reports state-of-the-art results across offline and online grounding benchmarks.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: Zhejiang University, National University of Singapore
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [information-sensitive cropping], [self-refining dual learning], [visual grounding], [Iris]
    - 📖 TLDR: Iris targets the visual-perception bottleneck of GUI agents in high-resolution, visually complex interfaces. It combines information-sensitive cropping with a self-refining dual-learning loop between referring and grounding, and the resulting gains transfer to both web and OS downstream tasks.

- [Falcon-UI: Understanding GUI Before Following User Instructions](https://arxiv.org/abs/2412.09362)
    - Huawen Shen, Chang Liu, Gengluo Li, Xinlong Wang, Yu Zhou, Can Ma, Xiangyang Ji
    - 🏛️ Institutions: Institute of Information Engineering, Chinese Academy of Sciences, Nankai University, Tsinghua University, Beijing Academy of Artificial Intelligence, University of Chinese Academy of Sciences
    - 📅 Date: December 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [Insight-UI Dataset], [GUI understanding], [instruction-free pretraining], [Falcon-UI]
    - 📖 TLDR: Falcon-UI studies whether GUI-context understanding should be learned before instruction following. It introduces the large instruction-free Insight-UI Dataset for GUI pretraining and shows that this staged training improves a 7B model enough to approach much larger baselines.

- [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html)
    - Yiheng Xu, Zekun Wang, Junli Wang, Dunjie Lu, Tianbao Xie, Amrita Saha, Doyen Sahoo, Tao Yu, Caiming Xiong
    - 🏛️ Institutions: University of Hong Kong, Salesforce Research
    - 📅 Date: December 05, 2024
    - 📑 Publisher: ICML 2025
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [pure vision], [inner monologue], [two-stage training], [Aguvis]
    - 📖 TLDR: Aguvis is a pure-vision GUI agent that removes textual interface representations and operates directly on screen images. It combines a large grounding-and-reasoning dataset with a two-stage training pipeline and inner-monologue reasoning, reporting strong offline and online performance without relying on closed-source models.

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [UI-guided visual token selection], [interleaved vision-language-action streaming], [screenshot grounding], [ShowUI]
    - 📖 TLDR: ShowUI is a lightweight vision-language-action model for GUI visual agents that targets efficient screenshot perception and action-history modeling. It introduces UI-guided visual token selection and interleaved vision-language-action streaming, reaching 75.1% zero-shot screenshot grounding while remaining competitive on web and mobile GUI tasks.

- [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218)
    - Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao
    - 🏛️ Institutions: Shanghai AI Laboratory, Shanghai Jiaotong University, The University of Hong Kong, MIT
    - 📅 Date: October 30, 2024
    - 📑 Publisher: ICLR 2025
    - 💻 Env: [Desktop], [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [GUI grounding], [cross-platform corpus], [OS-Atlas]
    - 📖 TLDR: OS-Atlas is a foundation action model for GUI agents built on a multi-platform grounding-data synthesis toolkit and a corpus with more than 13 million GUI elements. It improves GUI grounding and zero-shot out-of-distribution agent performance across desktop, mobile, and web benchmarks.

- [AutoGLM: Autonomous Foundation Agents for GUIs](https://arxiv.org/abs/2411.00820)
    - Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long Iong, Jiadai Sun, Jiaqi Wang, Junjie Gao, Junjun Shan, Kangning Liu, Shudan Zhang, Shuntian Yao, Siyi Cheng, Wentao Yao, Wenyi Zhao, Xinghan Liu, Xinyi Liu, Xinying Chen, Xinyue Yang, Yang Yang, Yifan Xu, Yu Yang, Yujia Wang, Yulin Xu, Zehan Qi, Yuxiao Dong, Jie Tang
    - 🏛️ Institutions: Zhipu AI, Tsinghua University
    - 📅 Date: October 28, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [model], [foundation agent], [intermediate interface], [progressive reinforcement learning], [AutoGLM]
    - 📖 TLDR: AutoGLM is a foundation-agent system for browser and phone control that emphasizes an intermediate interface separating planning from grounding. The paper pairs that design with progressive self-evolving reinforcement learning and reports strong performance on both web and Android evaluations.

- [MobileFlow: A Multimodal LLM For Mobile GUI Agent](https://arxiv.org/abs/2407.04346)
    - Songqin Nong, Jiali Zhu, Rui Wu, Jiongchao Jin, Shuo Shan, Xiutian Huang, Wenhao Xu
    - 🏛️ Institutions: Ant Group
    - 📅 Date: July 05, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [hybrid visual encoder], [multilingual GUI], [MobileFlow]
    - 📖 TLDR: This paper introduces *MobileFlow*, a multimodal large language model tailored for mobile GUI agents. With approximately 21 billion parameters and hybrid visual encoders, it supports variable image resolutions and multilingual GUIs, enhancing the model's ability to interpret image data and comprehend user instructions for GUI interaction tasks.

- [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://aclanthology.org/2024.findings-emnlp.68/)
    - Ziyang Meng, Yu Dai, Zezheng Gong, Shaoxiong Guo, Minglong Tang, Tongquan Wei
    - 🏛️ Institutions: East China Normal University
    - 📅 Date: June 20, 2024
    - 📑 Publisher: Findings of EMNLP 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [GUI VQA], [hallucination mitigation], [FAC], [referent method], [VGA]
    - 📖 TLDR: Introduces VGA, a GUI-understanding model trained to reduce hallucinations caused by over-reliance on textual priors instead of on-screen evidence. The paper builds a 63.8K GUI VQA dataset with a referent-based construction method and uses a two-stage FAC fine-tuning procedure to improve visually grounded answers.

- [Octopus v3: Technical Report for On-device Sub-billion Multimodal AI Agent](https://arxiv.org/abs/2404.11459)
    - Wei Chen, Zhiyuan Li
    - 🏛️ Institutions: Stanford University
    - 📅 Date: April 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [functional tokens], [on-device agent], [edge deployment], [Octopus v3]
    - 📖 TLDR: Presents Octopus v3, a sub-billion multimodal agent model aimed at on-device deployment on hardware as small as a Raspberry Pi. Its core idea is to introduce functional tokens that map multimodal inputs into action-oriented representations for agent tasks.

- [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://eccv.ecva.net/virtual/2024/poster/749)
    - Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeff Nichols, Yinfei Yang, Zhe Gan
    - 🏛️ Institutions: Apple
    - 📅 Date: April 08, 2024
    - 📑 Publisher: ECCV 2024 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [benchmark], [grounding], [reasoning], [mobile UI understanding], [ferret-UI]
    - 📖 TLDR: This paper presents **Ferret-UI**, a multimodal large language model (MLLM) designed to understand and interact with mobile user interfaces. The model incorporates advanced capabilities for referring, grounding, and reasoning about UI elements. By training on a variety of UI tasks, Ferret-UI achieves high performance in tasks such as icon recognition and text extraction. The authors introduce a unique architecture that allows for improved visual feature extraction from mobile screens, paving the way for applications in accessibility and user interaction.

- [Improving Language Understanding from Screenshots](https://arxiv.org/abs/2402.14073)
    - Tianyu Gao, Zirui Wang, Adithya Bhaskar, Danqi Chen
    - 🏛️ Institutions: Princeton Language and Intelligence (PLI), Princeton University
    - 📅 Date: February 21, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [screenshot language model], [PTP], [pretraining objective], [multimodal language understanding]
    - 📖 TLDR: Studies how to make screenshot language models better at text-heavy understanding by pretraining them with a patch-and-text prediction objective that reconstructs both image regions and embedded text. The resulting models close much of the gap to text-only baselines on GLUE-style tasks and also improve autoregressive screenshot language modeling.

- [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://arxiv.org/abs/2402.04615)
    - Gilles Baechler, Srinivas Sunkara, Maria Wang, Fedir Zubach, Hassan Mansoor, Vincent Etter, Victor Cărbune, Jason Lin, Jindong Chen, Abhanshu Sharma
    - 🏛️ Institutions: Google DeepMind
    - 📅 Date: February 07, 2024
    - 📑 Publisher: IJCAI 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [UI understanding], [infographics understanding], [ScreenAI], [screen annotation]
    - 📖 TLDR: Presents ScreenAI, a vision-language model specialized for screen understanding across both UI and infographic settings. It combines PaLI-style modeling with pix2struct-style patching and is trained on a mixture designed specifically for screen-centric perception tasks.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/)
    - Kanzhi Cheng, Qiushi Sun, Yougang Chu, Fangzhi Xu, Li YanTao, Jianbing Zhang, Zhiyong Wu
    - 🏛️ Institutions: Nanjing University, Shanghai AI Lab
    - 📅 Date: January 19, 2024
    - 📑 Publisher: ACL 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [GUI grounding], [ScreenSpot], [SeeClick]
    - 📖 TLDR: SeeClick is a screenshot-only visual GUI agent that targets the core GUI grounding problem without relying on structured accessibility trees or HTML-like inputs. The paper introduces GUI-grounding pretraining data generation and the ScreenSpot benchmark, and shows that better grounding directly improves downstream GUI agent performance.

- [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7ef7d8359036afd8c2378d82c21058a4-Abstract-Conference.html)
    - Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu, Izzeddin Gur
    - 🏛️ Institutions: The University of Tokyo, Google DeepMind
    - 📅 Date: January 01, 2024
    - 📑 Publisher: ICLR 2024 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [model], [offline training], [WebGUM], [demonstration learning], [MiniWoB], [WebShop], [Mind2Web]
    - 📖 TLDR: Trains an instruction-following multimodal web agent offline from a large demonstration corpus using both screenshots and HTML as input. WebGUM substantially improves grounded perception and multi-step reasoning, outperforming prior offline methods on MiniWoB, beating PaLM-540B on WebShop, and transferring positively to Mind2Web.

- [CogAgent: A Visual Language Model for GUI Agents](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_CogAgent_A_Visual_Language_Model_for_GUI_Agents_CVPR_2024_paper.html)
    - Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhao Chen, Yuxuan Wang, Yining Ye, Jiayi Zhang, Hao Dong, Wenhu Chen, Yizhou Wang, Kai-Wei Chang
    - 🏛️ Institutions: Tsinghua University, Zhipu AI
    - 📅 Date: December 15, 2023
    - 📑 Publisher: CVPR 2024
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [visual language model]
    - 📖 TLDR: This paper presents CogAgent, a visual language model designed for GUI agents. The authors introduce a new dataset, CogBench, featuring 1,430 GUI tasks across various applications. CogAgent employs a novel training approach combining supervised fine-tuning and decision-making fine-tuning. The model demonstrates superior performance on CogBench and generalizes well to unseen applications, outperforming existing models like GPT-4V in GUI task completion.

- [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716)
    - Zhizheng Zhang, Wenxuan Xie, Xiaoyi Zhang, Yan Lu
    - 🏛️ Institutions: Microsoft Research Asia
    - 📅 Date: October 07, 2023
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [model], [instruction grounding], [pixel-to-sequence], [reinforcement learning], [RUIG]
    - 📖 TLDR: Presents RUIG, a metadata-free grounding model that maps natural-language instructions to coordinates on UI screenshots using a pixel-to-sequence decoder. The main contribution is an RL-style training objective that strengthens spatial decoding quality, positioning RUIG as a generic UI-grounding API rather than a full agent stack.

- [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://proceedings.mlr.press/v202/lee23g.html)
    - Kenton Lee, Mandar Joshi, Iulia Raluca Turc, Hexiang Hu, Fangyu Liu, Julian Martin Eisenschlos, Urvashi Khandelwal, Peter Shaw, Ming-Wei Chang, Kristina Toutanova
    - 🏛️ Institutions: Google
    - 📅 Date: February 01, 2023
    - 📑 Publisher: ICML 2023
    - 💻 Env: [Web]
    - 🔑 Key: [model], [pretraining], [screenshot parsing], [image-to-text], [Pix2Struct]
    - 📖 TLDR: Presents Pix2Struct, an image-to-text model pretrained by reconstructing simplified HTML from masked webpage screenshots. The paper positions screenshot parsing as a unified pretraining task for visually situated language and shows strong transfer across document, illustration, and UI understanding tasks.

- [Spotlight: Mobile UI Understanding using Vision-Language Models with a Focus](https://proceedings.iclr.cc/paper_files/paper/2023/hash/0f4145fde6f5ae66745ef2a16bd1a7cd-Abstract-Conference.html)
    - Gang Li, Yang Li
    - 🏛️ Institutions: Google Research
    - 📅 Date: September 29, 2022
    - 📑 Publisher: ICLR 2023 (Poster)
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [region-based focus], [mobile UI understanding], [Spotlight]
    - 📖 TLDR: Presents Spotlight, a vision-language model for mobile UI understanding that uses screenshots plus a user-specified focus region instead of relying on view hierarchy metadata. The paper targets multiple UI tasks, including captioning, summarization, grounding, and tappability prediction, under a unified visual-only setup.

- [Screen2Words: Automatic Mobile UI Summarization with Multimodal Learning](https://dl.acm.org/doi/10.1145/3472749.3474765)
    - Bryan Wang, Gang Li, Xin Zhou, Zhourong Chen, Tovi Grossman, Yang Li
    - 🏛️ Institutions: University of Toronto
    - 📅 Date: August 06, 2021
    - 📑 Publisher: UIST 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [dataset], [mobile UI summarization], [multimodal learning], [Screen2Words]
    - 📖 TLDR: Introduces Screen2Words, a dataset and model for generating high-level natural-language summaries of mobile screens. The paper is important because it turns UI understanding into screen-level semantic summarization rather than only element-level labeling.

- [UIBert: Learning Generic Multimodal Representations for UI Understanding](https://www.ijcai.org/proceedings/2021/235)
    - Chongyang Bai, Xiaoxue Zang, Ying Xu, Srinivas Sunkara, Abhinav Rastogi, Jindong Chen, Blaise Agüera y Arcas
    - 🏛️ Institutions: Google Research
    - 📅 Date: July 29, 2021
    - 📑 Publisher: IJCAI 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [pretraining], [multimodal representation learning], [view hierarchy], [UIBert]
    - 📖 TLDR: Introduces UIBert, a transformer model for UI understanding that jointly models screenshots, text, and structural metadata such as the Android view hierarchy. The paper proposes five UI-specific pretraining tasks built around self-alignment between modalities and reports gains on nine downstream UI tasks.

- [Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements](https://aclanthology.org/2020.emnlp-main.443/)
    - Yang Li, Gang Li, Luheng He, Jingjie Zheng, Hong Li, Zhiwei Guan
    - 🏛️ Institutions: Google Research, Georgia Institute of Technology
    - 📅 Date: November 30, 2020
    - 📑 Publisher: EMNLP 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [model], [accessibility], [natural language generation], [WidgetCaption]
    - 📖 TLDR: Introduces widget captioning as the task of generating accessibility-oriented natural-language descriptions for mobile UI elements. The paper contributes a large captioned dataset and frames element description as a core building block for accessible mobile assistants.
