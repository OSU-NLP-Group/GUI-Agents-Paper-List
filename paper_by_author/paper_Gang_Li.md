# Gang Li's Papers

- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596)
    - Haojia Lin, Xiaoyu Tan, Yulei Qin, Zihan Xu, Yuchen Shi, Zongyi Li, Gang Li, Shaofei Cai, Siqi Cai, Chaoyou Fu, Ke Li, Xing Sun
    - 🏛️ Institutions: Tencent Youtu Lab, PKU, NJU
    - 📅 Date: October 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Env: [Desktop]
    - 🔑 Key: [benchmark], [dataset], [reward model], [computer-using agent], [CUARewardBench], [Unanimous Prompt Ensemble (UPE)]
    - 📖 TLDR: This paper introduces CUARewardBench, the first benchmark for evaluating reward models tailored to computer-using agents. It includes step-level and trajectory-level annotations from tasks across 10 software types and 7 agent architectures. The study identifies the limitations of current reward models and proposes UPE, a prompting-based method that significantly improves evaluation accuracy.

- [PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction For Continual Learning](https://arxiv.org/abs/2510.15863)
    - Simon Yu, Gang Li, Weiyan Shi, Peng Qi
    - 🏛️ Institutions: NEU, Uniphore
    - 📅 Date: October 17, 2025
    - 📑 Publisher: ICLR 2026
    - 💻 Env: [Web]
    - 🔑 Key: [framework], [skill learning], [compositional skills], [transfer generalization], [Polymorphism], [PolySkill], [continual learning]
    - 📖 TLDR: This paper introduces **PolySkill**, a framework that enables LLM-based web agents to acquire generalizable and composable skills by decoupling a skill's abstract goal from its concrete implementation, inspired by polymorphic abstraction in software engineering. Evaluated on the Mind2Web benchmark, PolySkill significantly enhances skill reuse, improves task success rates on both seen and unseen websites, and reduces the number of interaction steps, demonstrating effective continual learning and skill transfer capabilities.

- [WARC-Bench: Web Archive Based Benchmark for GUI Subtask Executions](https://arxiv.org/abs/2510.09872)
    - Sanjari Srivastava, Gang Li, Cheng Chang, Rishu Garg, Manpreet Kaur, Charlene Y. Lee, Yuezhang Li, Yining Mao, Ignacio Cases, Yanan Xie, Peng Qi
    - 🏛️ Institutions: Uniphore
    - 📅 Date: October 10, 2025
    - 📑 Publisher: ICLR 2026 (Poster)
    - 💻 Env: [Web]
    - 🔑 Key: [benchmark], [web agent], [GUI subtask execution], [reinforcement learning], [RLVR], [WARC-Bench]
    - 📖 TLDR: This paper introduces WARC-Bench, a web benchmark focused on short-horizon GUI subtasks such as date pickers, container scrolling, and other widget-level interactions that existing benchmarks under-emphasize. It packages dynamic realistic webpages as Web ARChive files for sandboxed evaluation and shows that even strong computer-use models struggle on these subtasks. The paper also studies supervised fine-tuning and RL with verifiable rewards, showing RLVR over SFT checkpoints improves open-source performance on the benchmark.

- [Spotlight: Mobile UI Understanding using Vision-Language Models with a Focus](https://arxiv.org/abs/2209.14927)
    - Gang Li, Yang Li
    - 🏛️ Institutions: Google Research
    - 📅 Date: September 29, 2022
    - 📑 Publisher: ICLR 2023
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [model], [dataset], [mobile UI tasks], [region-based focus]
    - 📖 TLDR: This paper introduces "Spotlight," a vision-language model for mobile UI understanding that operates solely on visual inputs (screenshots) and a specified focus region on the screen. By leveraging a large-scale dataset and training strategies tailored to mobile interfaces, Spotlight performs multiple UI-related tasks, including widget captioning, screen summarization, command grounding, and tappability prediction. It utilizes a vision-only approach, avoiding reliance on view hierarchies to achieve greater robustness and scalability across different mobile UI environments.

- [Screen2Words: Automatic Mobile UI Summarization with Multimodal Learning](https://arxiv.org/abs/2108.03353)
    - Bryan Wang, Gang Li, Xin Zhou, Zhourong Chen, Tovi Grossman, Yang Li
    - 🏛️ Institutions: University of Toronto
    - 📅 Date: August 6, 2021
    - 📑 Publisher: UIST 2021
    - 💻 Env: [Mobile]
    - 🔑 Key: [framework], [dataset], [mobile UI summarization], [multimodal learning], [Transformer model]
    - 📖 TLDR: The paper introduces *Screen2Words*, an approach that utilizes multimodal learning to generate descriptive language summaries for mobile UI screens, combining textual, visual, and structural data from screens. The study created a large-scale dataset with 112,085 annotated screen summaries for 22,417 unique UIs, aiming to support model training for mobile UI understanding. The dataset facilitates a Transformer-based model trained to summarize screens by highlighting main functionalities, and the approach is validated with benchmarks in the mobile environment.

- [Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements](https://arxiv.org/abs/2010.04295)
    - Yang Li, Gang Li, Luheng He, Jingjie Zheng, Hong Li, Zhiwei Guan
    - 🏛️ Institutions: Google Research
    - 📅 Date: November 2020
    - 📑 Publisher: EMNLP 2020
    - 💻 Env: [Mobile]
    - 🔑 Key: [dataset], [benchmark], [model], [accessibility], [natural language generation], [WidgetCaption]
    - 📖 TLDR: This paper introduces the task of *widget captioning*, which aims to automatically generate natural language descriptions for UI elements in mobile apps to enhance accessibility. Using both visual and structural data from UI components, the study presents a novel dataset of 162,859 captions across 61,285 UI elements. Multiple deep learning models were tested on this dataset, with findings suggesting the potential for improving screen reader usability for visually impaired users by generating descriptive captions of UI elements.
