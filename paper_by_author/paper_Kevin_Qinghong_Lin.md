# Kevin Qinghong Lin's Papers

- [GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents](https://arxiv.org/abs/2604.07429)
    - Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
    - 🏛️ Institutions: NUS, Oxford
    - 📅 Date: April 08, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [game agent], [computer-use control], [semantic control], [GameWorld]
    - 📖 TLDR: GameWorld is a standardized browser-based benchmark for multimodal game agents with 34 games and 170 tasks. Two game agent interfaces are studied: (i) computer-use agents that directly emit keyboard and mouse controls, and (ii) generalist multimodal agents that act in a semantic action space.

- [GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks](https://arxiv.org/abs/2603.25864)
    - Saelyne Yang, Jaesang Yu, Yi-Hao Peng, Kevin Qinghong Lin, Jae Won Cho, Yale Song, Juho Kim
    - 🏛️ Institutions: KAIST, CMU, Oxford, Konkuk University, Google, SkillBench
    - 📅 Date: March 26, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [General GUI]
    - 🔑 Key: [benchmark], [collaborative assistance], [behavior state detection], [intent prediction], [help prediction], [think-aloud data], [GUIDE]
    - 📖 TLDR: GUIDE studies collaborative GUI assistance rather than pure task automation, using 67.5 hours of think-aloud recordings from 120 novice users across 10 software applications. It benchmarks behavior-state detection, intent prediction, and help prediction, and shows that current multimodal models still struggle to infer what users are doing and when intervention would be useful.

- [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440)
    - Xiangru Jian, Shravan Nayak, Kevin Qinghong Lin, Aarash Feizi, Kaixin Li, Patrice Bechard, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: ServiceNow, University of Waterloo, Mila, Université de Montréal, McGill University, Oxford, NUS
    - 📅 Date: March 25, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [video demonstrations], [desktop workflows], [grounding dataset], [VideoCUA], [GroundCUA], [UI-Vision], [CUA-Suite]
    - 📖 TLDR: CUA-Suite is a large-scale desktop-agent data ecosystem centered on continuous expert video rather than sparse screenshots. It combines VideoCUA, UI-Vision, and GroundCUA to provide 55 hours of demonstrations, dense grounding annotations, and evaluation data across 87 professional desktop applications where current foundation action models still fail frequently.

- [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856)
    - Yuhao Zheng, Li'an Zhong, Yi Wang, Rui Dai, Kaikui Liu, Xiangxiang Chu, Linyuan Lv, Philip Torr, Kevin Qinghong Lin
    - 🏛️ Institutions: USTC, AMAP, Alibaba Group, Sun Yat-sen University, Oxford
    - 📅 Date: February 10, 2026
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [world model], [renderable code generation], [AndroidCode], [render-aware reinforcement learning], [next-state prediction], [Code2World]
    - 📖 TLDR: Code2World models GUI dynamics by generating renderable code for the next interface state rather than directly predicting pixels. Trained on AndroidCode with render-aware RL, it improves next-state prediction and downstream Android navigation.

- [ShowUI-π: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965)
    - Siyuan Hu, Kevin Qinghong Lin, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS
    - 📅 Date: December 31, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [benchmark], [model], [drag interaction], [flow-based model], [continuous action], [ScreenDrag], [ShowUI-π]
    - 📖 TLDR: ShowUI-π treats GUI dragging as a continuous dexterous-control problem rather than only discrete point prediction, while still supporting ordinary click actions in the same model. It also introduces ScreenDrag with 20K trajectories across five domains, and the 450M-parameter model outperforms much larger proprietary GUI agents on this benchmark.

- [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661)
    - Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Juan A. Rodriguez, Montek Kalsi, Rabiul Awal, Nicolas Chapados, M. Tamer Özsu, Aishwarya Agrawal, David Vazquez, Christopher Pal, Perouz Taslakian, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, Université de Montréal, ServiceNow, University of Waterloo, NUS, École de Technologie Supérieure, Polytechnique Montréal
    - 📅 Date: March 19, 2025
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [UI-Vision], [element grounding], [layout grounding], [action prediction], [drag-and-drop], [spatial reasoning]
    - 📖 TLDR: UI-Vision is a desktop GUI benchmark with dense human-demonstration annotations over 83 applications, covering element grounding, layout grounding, and action prediction. It exposes persistent weaknesses of current agents on professional software, spatial reasoning, and actions such as drag-and-drop, while providing an open benchmark for desktop-centric GUI evaluation.

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025 (Poster)
    - 💻 Env: [Mobile], [Web]
    - 🔑 Key: [model], [dataset], [UI-guided visual token selection], [interleaved vision-language-action streaming], [screenshot grounding], [ShowUI]
    - 📖 TLDR: ShowUI is a lightweight vision-language-action model for GUI visual agents that targets efficient screenshot perception and action-history modeling. It introduces UI-guided visual token selection and interleaved vision-language-action streaming, reaching 75.1% zero-shot screenshot grounding while remaining competitive on web and mobile GUI tasks.

- [GUI Action Narrator: Where and When Did That Action Take Place?](https://arxiv.org/abs/2406.13719)
    - Qinchen Wu, Difei Gao, Kevin Qinghong Lin, Zhuoyu Wu, Xiangwu Guo, Peiran Li, Weichen Zhang, Hengxu Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS, CAS, Shenzhen
    - 📅 Date: June 19, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop], [Web]
    - 🔑 Key: [benchmark], [dataset], [Act2Cap], [GUI video captioning], [GUI Narrator]
    - 📖 TLDR: GUI Action Narrator introduces Act2Cap, a benchmark and dataset of 4,189 GUI action video-captioning samples covering actions such as clicks, drags, and typing across desktop software and web tools. It also proposes GUI Narrator, which uses the cursor as a visual prompt plus temporal and spatial sampling to caption those actions more accurately than off-the-shelf multimodal models.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen Wu, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, NUS, Microsoft
    - 📅 Date: June 14, 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [instructional videos], [visual-centric tasks], [hierarchical evaluation], [VideoGUI]
    - 📖 TLDR: VideoGUI is a desktop GUI benchmark built from high-quality instructional videos covering visual-centric software such as Photoshop, video editing tools, and Stable Diffusion WebUI. It evaluates assistants at high-level planning, middle-level action narration, and atomic execution, and finds that even GPT-4o performs poorly on these visually specified tasks.
