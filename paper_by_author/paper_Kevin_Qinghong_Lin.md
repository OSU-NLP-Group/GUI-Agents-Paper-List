# Kevin Qinghong Lin's Papers

- [GUIDE: A Benchmark for Understanding and Assisting Users in Open-Ended GUI Tasks](https://arxiv.org/abs/2603.25864)
    - Saelyne Yang, Jaesang Yu, Yi-Hao Peng, Kevin Qinghong Lin, Jae Won Cho
    - 🏛️ Institutions: KAIST, Carnegie Mellon University, University of Oxford, Konkuk University, Google
    - 📅 Date: March 26, 2026
    - 📑 Publisher: CVPR 2026
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [GUI agent], [user intent detection], [behavior understanding], [multimodal models], [desktop]
    - 📖 TLDR: GUIDE is a benchmark evaluating AI models on perceiving user behavior, inferring intent, and providing assistance during open-ended GUI tasks, comprising 67.5 hours of screen recordings from 120 novice users across 10 software applications, revealing that current multimodal models struggle but benefit significantly from structured user context.

- [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440)
    - Xiangru Jian, Shravan Nayak, Kevin Qinghong Lin, Aarash Feizi, Kaixin Li...
    - 🏛️ Institutions: Unknown
    - 📅 Date: 2026-03-25
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [computer-use agent], [video demonstration], [training data], [desktop automation]
    - 📖 TLDR: CUA-Suite is a large-scale ecosystem of ~10,000 human-demonstrated expert video tasks (30 fps) across 87 diverse desktop applications with dense annotations, addressing the data scarcity bottleneck that limits CUA development by providing continuous video rather than sparse screenshots.

- [Computer-Use Agents as Judges for Generative User Interface](https://arxiv.org/abs/2511.15567)
    - Kevin Qinghong Lin, Siyuan Hu, Linjie Li, Zhengyuan Yang, Lijuan Wang, Philip Torr, Mike Zheng Shou
    - 🏛️ Institutions: University of Oxford, Show Lab, National University of Singapore, Microsoft
    - 📅 Date: November 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [benchmark], [agent-native GUI], [automatic GUI design], [AUI-gym], [coder-CUA collaboration]
    - 📖 TLDR: This paper studies how computer-use agents can actively improve interfaces rather than only operate them. It introduces AUI-Gym, a benchmark for automatic GUI development across 52 applications and 1,560 synthesized tasks, together with a Coder-CUA collaboration framework in which a coding model iteratively redesigns interfaces while a computer-use agent judges task solvability through interaction. The work shifts GUI design toward agent-centric efficiency and reliability, showing that agent feedback can materially improve downstream execution success.

- [Grounding Computer Use Agents on Human Demonstrations](https://arxiv.org/abs/2511.07332)
    - Aarash Feizi, Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Kaixin Li, Rabiul Awal, Xing Han Lu, Johan Obando-Ceron, Juan A. Rodriguez, Nicolas Chapados, David Vazquez, Adriana Romero-Soriano, Reihaneh Rabbany, Perouz Taslakian, Christopher Pal, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, McGill University, Universite de Montreal, ServiceNow Research, University of Waterloo, University of Oxford, National University of Singapore, Polytechnique Montreal, Ecole de Technologie Superieure, CIFAR
    - 📅 Date: November 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [model], [GUI grounding], [desktop grounding], [reinforcement learning], [GroundCUA], [GroundNext]
    - 📖 TLDR: This paper introduces GroundCUA, a large-scale desktop grounding dataset built from expert human demonstrations, covering 87 applications, 56K screenshots, and more than 3.56M human-verified UI annotations. Using this data, the authors train the GroundNext family of grounding models, which achieve state-of-the-art results across five benchmarks with far less training data than prior work, and improve further with reinforcement learning post-training. The paper shows that high-quality human demonstration data is a key driver for robust grounding in general-purpose computer-use agents.

- [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661)
    - Shravan Nayak, Xiangru Jian, Kevin Qinghong Lin, Juan A. Rodriguez, Montek Kalsi, Rabiul Awal, Nicolas Chapados, M. Tamer Özsu, Aishwarya Agrawal, David Vazquez, Christopher Pal, Perouz Taslakian, Spandana Gella, Sai Rajeswar
    - 🏛️ Institutions: Mila, Universite de Montreal, ServiceNow, University of Waterloo, National University of Singapore, Ecole de Technologie Superieure, CIFAR AI Chair, Polytechnique Montreal
    - 📅 Date: March 19, 2025
    - 📑 Publisher: ICML 2025 (Poster)
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [framework], [UI-vision], [UI-TARS-72B], [spatial reasoning], [drag-and-drop], [element grounding], [layout grounding], [action prediction]
    - 📖 TLDR: This paper introduces *UI-Vision*, a comprehensive, license-permissive benchmark designed for evaluating autonomous agents in real-world desktop GUI environments. It encompasses 83 software applications with dense annotations of human demonstrations, including bounding boxes, UI labels, and action trajectories. The benchmark defines three tasks—Element Grounding, Layout Grounding, and Action Prediction—to assess agents' performance. Evaluations reveal limitations in state-of-the-art models like UI-TARS-72B, particularly in understanding professional software, spatial reasoning, and complex actions such as drag-and-drop. By releasing UI-Vision as open-source, the authors aim to advance the development of more capable agents for desktop tasks.

- [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore, Microsoft
    - 📅 Date: November 26, 2024
    - 📑 Publisher: CVPR 2025
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [dataset], [UI-guided visual token selection], [interleaved vision-language-action streaming], [ShowUI]
    - 📖 TLDR: This paper introduces *ShowUI*, a vision-language-action model designed to enhance GUI automation by addressing challenges in UI visual perception and action modeling. It features innovations like UI-Guided Visual Token Selection to reduce computational costs and Interleaved Vision-Language-Action Streaming for effective management of visual-action history. Trained on a curated dataset, ShowUI achieves 75.1% accuracy in zero-shot screenshot grounding and demonstrates competitive performance across web, mobile, and online environments.

- [GUI Action Narrator: Where and When Did That Action Take Place?](https://arxiv.org/abs/2406.13719)
    - Qinchen Wu, Difei Gao, Kevin Qinghong Lin, Zhuoyu Wu, Xiangwu Guo, Peiran Li, Weichen Zhang, Hengxu Wang, Mike Zheng Shou
    - 🏛️ Institutions: Show Lab, National University of Singapore, Chinese Academy of Sciences, Shenzhen
    - 📅 Date: June 19, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [dataset], [framework], [Act2Cap], [GUI narrator]
    - 📖 TLDR: The authors present **Act2Cap**, a GUI action dataset containing 4,189 video-caption pairs depicting various GUI actions such as clicks, drags, and typing across multiple software environments. They also propose **GUI Narrator**, a framework that leverages cursor detection as a visual prompt to enhance the interpretation of high-resolution screenshots for GUI video captioning. Evaluations reveal that even advanced multimodal models face challenges in this domain, highlighting the need for specialized approaches to improve performance.

- [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html)
    - Kevin Qinghong Lin, Linjie Li, Difei Gao, Qinchen Wu, Mingyi Yan, Zhengyuan Yang, Lijuan Wang, Mike Zheng Shou
    - 🏛️ Institutions: National University of Singapore, Microsoft GenAI
    - 📅 Date: June 2024
    - 📑 Publisher: NeurIPS 2024 Datasets and Benchmarks Track
    - 💻 Env: [GUI]
    - 🔑 Key: [benchmark], [instructional videos], [visual planning], [hierarchical task decomposition], [complex software interaction]
    - 📖 TLDR: VideoGUI presents a benchmark for evaluating GUI automation on tasks derived from instructional videos, focusing on visually intensive applications like Adobe Photoshop and video editing software. The benchmark includes 178 tasks, with a hierarchical evaluation method distinguishing high-level planning, mid-level procedural steps, and precise action execution. VideoGUI reveals current model limitations in complex visual tasks, marking a significant step toward improved visual planning in GUI automation.
