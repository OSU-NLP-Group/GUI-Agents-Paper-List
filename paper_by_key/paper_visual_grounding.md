# Papers with Keyword: visual grounding

- [CocoaBench: Evaluating Unified Digital Agents in the Wild](https://arxiv.org/abs/2604.11201)
    - Shibo Hao, Zhining Zhang, Zhiqi Liang, Tianyang Liu, Yuheng Zha, Qiyue Gao, Jixuan Chen, Zilong Wang, Zhoujun Cheng, Haoxiang Zhang, Junli Wang, Hexi Jin, Boyuan Zheng, Kun Zhou, Yu Wang, Feng Yao, Licheng Liu, Yijiang Li, Zhifei Li, Zhengtao Han, Pracha Promthaw, Tommaso Cerruti, Xiaohan Fu, Ziqiao Ma, Jingbo Shang, Lianhui Qin, Julian McAuley, Eric P. Xing, Zhengzhong Liu, Rupesh Kumar Srivastava, Zhiting Hu
    - 🏛️ Institutions: UC San Diego, OSU, CMU, MBZUAI
    - 📅 Date: April 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [unified digital agents], [long-horizon tasks], [visual grounding], [CocoaBench], [CocoaAgent]
    - 📖 TLDR: CocoaBench evaluates unified digital agents on long-horizon tasks requiring flexible composition of vision, search, and coding. Tasks are specified by an instruction and an automatic evaluation function, enabling reliable scalable evaluation across agent infrastructures. The best-evaluated system reaches only 45.1%, exposing gaps in reasoning, tool use, and visual grounding.

- [Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection](https://arxiv.org/abs/2604.07831)
    - Wenkui Yang, Chao Jin, Haisu Zhu, Weilin Luo, Derek Yuen, Kun Shao, Huaibo Huang, Junxian Duan, Jie Cao, Ran He
    - 🏛️ Institutions: UCAS, CASIA, Huawei, ShanghaiTech
    - 📅 Date: April 09, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [safety], [red teaming], [visual grounding], [UI injection]
    - 📖 TLDR: This paper proposes Semantic-level UI Element Injection, a red-teaming method that overlays safety-aligned UI elements onto screenshots to misdirect GUI agents' visual grounding. Using a modular Editor-Overlapper-Victim pipeline with iterative search, optimized attacks improve attack success rate by up to 4.4x over random injection and transfer across models.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548)
    - Xiaoce Wang, Guibin Zhang, Junzhe Li, Jinzhe Tu, Chun Li, Ming Li
    - 🏛️ Institutions: Tsinghua, NUS, PKU, Shenzhen MSU-BIT University, Guangming Laboratory
    - 📅 Date: January 30, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [tool use], [tokenization], [curriculum learning], [visual grounding], [data efficiency], [ToolTok]
    - 📖 TLDR: ToolTok treats GUI operations as paths over learnable tool tokens with semantic anchoring and curriculum learning. This makes GUI agents more efficient and generalizable, reaching competitive performance with far less training data than other post-training methods.

- [How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors](https://arxiv.org/abs/2601.21961)
    - Kuai Yu, Naicheng Yu, Han Wang, Rui Yang, Huan Zhang
    - 🏛️ Institutions: Columbia, UC San Diego, UIUC
    - 📅 Date: January 29, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [evaluation pipeline], [visual attribute factors], [VAF], [visual grounding], [robustness]
    - 📖 TLDR: This paper introduces VAF, a controlled evaluation pipeline for measuring how benign UI visual attributes affect web-agent choices while preserving page semantics. Across 48 variants, 5 real websites, and 4 agents, it shows that contrast, size, position, and card clarity strongly influence agent behavior, while several text-style factors matter much less.

- [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009)
    - Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu, Vineeth N Balasubramanian
    - 🏛️ Institutions: Indian Institute of Technology, Bombay, Indian Institute of Technology, Hyderabad
    - 📅 Date: December 26, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [General GUI]
    - 🔑 Key: [slow-fast reasoning], [visual grounding], [latent thinking], [adaptive perception], [iSHIFT]
    - 📖 TLDR: iSHIFT is a 2.5B GUI agent that combines latent thinking with perception-control tokens so it can switch between a fast global mode and a slower grounding-heavy mode. The paper positions this as a way to allocate reasoning depth and visual focus adaptively while still matching state-of-the-art results on multiple GUI benchmarks.

- [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
    - Zhiqi Ge, Juncheng Li, Xinglei Pang, Minghe Gao, Kaihang Pan, Wang Lin, Hao Fei, Wenqiao Zhang, Siliang Tang, Yueting Zhuang
    - 🏛️ Institutions: ZJU, NUS
    - 📅 Date: December 13, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [model], [GUI grounding], [information-sensitive cropping], [self-refining dual learning], [visual grounding], [Iris]
    - 📖 TLDR: Iris targets the visual-perception bottleneck of GUI agents in high-resolution, visually complex interfaces. It combines information-sensitive cropping with a self-refining dual-learning loop between referring and grounding, and the resulting gains transfer to both web and OS downstream tasks.

- [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9/)
    - Yijun Qian, Yujie Lu, Alexander Hauptmann, Oriana Riva
    - 🏛️ Institutions: CMU, UC Santa Barbara, Google Research
    - 📅 Date: June 16, 2024
    - 📑 Publisher: NAACL 2024 Industry Track
    - 💻 Env: [General GUI]
    - 🔑 Key: [GUI grounding], [visual grounding], [UI element localization], [layout-guided contrastive learning], [multi-context learning], [LVG]
    - 📖 TLDR: This paper defines visual UI grounding, where a model must localize the UI element referenced by a natural-language command directly from a screenshot without relying on UI metadata. It proposes LVG, which combines layout-guided contrastive learning with synthetic-to-real multi-context learning and improves top-1 accuracy by more than 4.9 points over strong baselines.

- [Dual-View Visual Contextualization for Web Navigation](https://doi.org/10.1109/CVPR52733.2024.01369)
    - Jihyung Kil, Chan Hee Song, Boyuan Zheng, Xiang Deng, Yu Su, Wei-Lun Chao
    - 🏛️ Institutions: OSU
    - 📅 Date: February 06, 2024
    - 📑 Publisher: CVPR 2024 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [GUI grounding], [dual-view contextualization], [visual grounding], [web element neighborhood], [Mind2Web]
    - 📖 TLDR: This paper contextualizes each HTML element with its corresponding screenshot region and nearby elements, combining textual and visual features to represent webpage elements more informatively. It evaluates the approach on Mind2Web and reports consistent gains in cross-task, cross-website, and cross-domain settings.
