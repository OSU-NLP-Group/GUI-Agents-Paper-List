# Wei Chen's Papers

- [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://ar5iv.org/abs/2410.15164)
    - Jingxuan Chen, Derek Yuen, Bin Xie, Yuhao Yang, Gongwei Chen, Zhihao Wu, Li Yixing, Xurui Zhou, Weiwen Liu, Shuai Wang, Rui Shao, Liqiang Nie, Yasheng Wang, Jianye Hao, Jun Wang, Kun Shao
    - 🏛️ Institutions: Huawei Noah’s Ark Lab, Harbin Institute of Technology, Shenzhen, UCL
    - 📅 Date: October 19, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [AI agent], [smartphone control], [framework]
    - 📖 TLDR: SPA-Bench is introduced as a benchmark designed to evaluate multimodal large language model (MLLM)-based smartphone agents, offering a task set that spans common smartphone functionalities across system and third-party applications. It includes a plug-and-play framework for real-time agent interactions on Android, integrating over ten agents with an adaptable evaluation pipeline measuring success across diverse metrics. Through this, the benchmark exposes challenges such as UI interpretation, action grounding, and memory retention in mobile environments, advancing research in smartphone-based agent applications.

- [MobileAgentBench: An Efficient and User-Friendly Benchmark for Mobile LLM Agents](https://mobileagentbench.github.io/)
    - Luyuan Wang, Yongyu Deng, Yiwei Zha, Guodong Mao, Qinmin Wang, Tianchen Min, Wei Chen, Shoufa Chen
    - 🏛️ Institutions: CMU, University of Michigan, Northeastern University, HKU
    - 📅 Date: June 12, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [benchmark], [MobileAgentBench]
    - 📖 TLDR: This paper introduces *MobileAgentBench*, a benchmark designed to evaluate the performance of large language model-based mobile agents. It defines 100 tasks across 10 open-source apps, categorized by difficulty levels, and assesses existing agents like AppAgent and MobileAgent to facilitate systematic comparisons.

- [Octopus v4: Graph of language models](https://arxiv.org/abs/2404.15371)
    - Wei Chen, Zhiyuan Li
    - 🏛️ Institutions: Unknown
    - 📅 Date: April 29, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [framework], [graph of language models], [multi-model integration], [functional tokens]
    - 📖 TLDR: Octopus v4 introduces a novel approach to integrating multiple open-source language models, each optimized for specific tasks, using a graph structure. The paper presents a method for coordinating these models using functional tokens, enabling more efficient and flexible task execution. This approach allows for the combination of specialized models to tackle complex tasks while maintaining the efficiency needed for on-device deployment. Octopus v4 demonstrates improved performance and versatility compared to single-model approaches, particularly in handling diverse and multi-step tasks.

- [Octopus v3: Technical Report for On-device Sub-billion Multimodal AI Agent](https://arxiv.org/abs/2404.11459)
    - Wei Chen, Zhiyuan Li
    - 🏛️ Institutions: Stanford University
    - 📅 Date: April 17, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [Mobile]
    - 🔑 Key: [model], [multimodal], [functional token], [on-device AI], [Octopus v3]
    - 📖 TLDR: This paper introduces Octopus v3, a compact multimodal AI agent with less than 1 billion parameters, designed for efficient on-device operation. It processes both English and Chinese inputs, integrating visual and textual data to perform tasks such as sending emails, messaging, and online shopping. The model employs a functional token approach to translate image-based data into actionable outcomes, demonstrating high accuracy and efficiency on edge devices, including Raspberry Pi.

- [Octopus: On-device language model for function calling of software APIs](https://arxiv.org/abs/2404.01549)
    - Wei Chen, Zhiyuan Li, Mingyuan Ma
    - 🏛️ Institutions: Unknown
    - 📅 Date: April 2, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [dataset], [benchmark], [API function calling], [conditional masking], [on-device LLMs]
    - 📖 TLDR: This paper introduces *Octopus*, an on-device language model fine-tuned to perform software API function calls with improved accuracy over cloud-based models like GPT-4. By compiling a dataset from 20,000 API documents and utilizing conditional masking techniques, the model enhances API interactions while maintaining quick inference speeds. Octopus also introduces a new benchmark for evaluating API call accuracy, addressing challenges in automated software development and API integration, particularly for edge devices.

- [Octopus v2: On-device language model for super agent](https://arxiv.org/abs/2404.01744)
    - Wei Chen, Zhiyuan Li
    - 🏛️ Institutions: Unknown
    - 📅 Date: April 2, 2024
    - 📑 Publisher: arXiv
    - 💻 Env: [GUI]
    - 🔑 Key: [model], [framework], [on-device language model], [function calling], [super agent]
    - 📖 TLDR: This paper introduces Octopus v2, an innovative on-device language model designed for efficient function calling in AI agents. The 2-billion parameter model outperforms GPT-4 in both accuracy and latency, while reducing context length by 95%. Octopus v2 uses a novel method of encoding functions into specialized tokens, significantly improving performance and enabling deployment across various edge devices. The model demonstrates a 35-fold latency improvement over Llama-7B with RAG-based function calling, making it suitable for real-world applications on resource-constrained devices.
