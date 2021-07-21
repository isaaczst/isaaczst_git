- http://jandan.net/p/109301
- 在某些方面人工智能(AI)已被证明强于人类，但是当涉及到人类的自然能力——想象力——时，神经网络仍还不够看。
- 一旦人类知道什么是猫，我们就可以很容易地想象出一只不同颜色的猫，或一只摆出不同姿势的猫，或一只处于不同环境中的猫。对于人工智能网络来说，人类这一能力这简直逆天，毕竟它们现在还停留在能够识别出猫(经足够训练)。
- 为了释放人工智能的想象力，研究人员想出了一种新的方法，使人工智能系统能够计算出一个物体应该是什么样子，即使以前从未真正见过。
- 南加州大学(USC)的计算机科学家Yunhao Ge说："我们受到人类视觉概括能力的启发，试图在机器中模拟人类的想象力。人类可以将他们学到的知识按属性分类——例如形状、姿势、位置、颜色——然后重新组合来想象一个新对象。我们的论文试图用神经网络来模拟这个过程。"
- 关键是推断--大量训练数据(如汽车的图片)，然后超越所见，进入未见。这对人工智能来说是困难的任务。
- 团队在这里想出的方法被称为可控的分离表征学习，类似于那些用于创建深度伪造视频的方法——分离样本的不同部分(所以在深度伪造视频的情况下，分离面部运动和面部身份)。
- 这意味着，如果人工智能看到一辆红色汽车和一辆蓝色自行车，那么它将能够为自己 "想象" 出一辆红色自行车——即使它以前从未见过。研究人员把这些放在一个框架中，他们称之为群体监督学习。
- 科学家赋予了AI基本的想象力
- ![2021_07_21_image.png](https://cdn.logseq.com/%2Fc15b201a-227a-4f6b-aebf-92b9206a58c2640bb083-4bac-461f-82dd-fe48c0852a442021_07_21_image.png?Expires=4780475265&Signature=C0qTOlpzr01maPLEtHvlY1EjVXuee0WFNfPuxKkszgEegPyYoj5R8s7nhtfQQ5Yu9CsZCIqAE25D3ARClbgj37nNEcmSOfR0AP-L2Qff909uaCswa2l0hVYIhSM6aoxc7KVmKz6RFvFs-Zqugso0t3TWTft48uRWqAvwhsdnexhOuRoIm~MSeYj90aSMiISd0camWWYizZblIVX8BlO91alGOG~gdPaFwAqox9cAvZSBcz~5iVLhC7rLQKgytUAwa3AZfM8iqzC46xmhPU~kNqg8VDHUDky7o2vBRof-2mXPxNNPYiaRl4ACkk0y77WNt0lIL~WAk1lBUziLQdkSOQ__&Key-Pair-Id=APKAJE5CCD6X7MP6PTEA)
- 嗨，Siri plus 从训练数据中推断出新的数据。(Itti et al., 2021)
- 这项技术的主要创新之一是分组处理样本，并在此过程中建立起它们之间的语义联系。然后，人工智能能够识别它所看到的样本的相似性和差异性，利用这些知识来产生全新的东西。
- 南加州大学计算机科学家Laurent Itti说："这种新的拆分方法，第一次真正释放了人工智能系统的想象力，使它们更接近于人类对世界的理解。”
- 这些想法并非完全新颖，但在这里，研究人员已经进一步优化了概念，使方法更加灵活，并与其他类型的数据兼容。他们还将该框架开放了源代码，因此其他科学家可以更容易地利用他们的成果。
- 研究人员说，同样的方法也可以应用于医学和自动驾驶汽车领域，人工智能能够 "想象" 新的药物，或者将过去没有经过专门训练的新道路场景可视化。
- Itti说："深度学习已经在许多领域展示了无与伦比的性能和前景，但往往是通过浅层次的模仿来进行，而没有更深入地了解使每个物体独特的独立属性。"
- 该研究已发表在2021年国际学习表征会议上，可点此阅读→
	- https://openreview.net/forum?id=8wqCDnBmnrT
# Zero-shot Synthesis with Group-Supervised Learning
- Yunhao Ge, Sami Abu-El-Haija, Gan Xin, Laurent Itti
  28 Sept 2020 (modified: 16 Feb 2021)
  ICLR 2021 PosterReaders:  EveryoneShow BibtexShow Revisions
- Keywords: Disentangled representation learning, Group-supervised learning, Zero-shot synthesis, Knowledge factorization
  Abstract: Visual cognition of primates is superior to that of artificial neural networks in its ability to “envision” a visual object, even a newly-introduced one, in different attributes including pose, position, color, texture, etc.  To aid neural networks to envision objects with different attributes,  we propose a family of objective functions, expressed on groups of examples, as a novel learning framework that we term Group-Supervised Learning (GSL). GSL allows us to decompose inputs into a disentangled representation with swappable components, that can be recombined to synthesize new samples.  For instance, images of red boats & blue cars can be decomposed and recombined to synthesize novel images of red cars.   We propose an implementation based on auto-encoder, termed group-supervised zero-shot synthesis network (GZS-Net) trained with our learning framework, that can produce a high-quality red car even if no such example is witnessed during training. We test our model and learning framework on existing benchmarks, in addition to a new dataset that we open-source. We qualitatively and quantitatively demonstrate that GZS-Net trained with GSL outperforms state-of-the-art methods
  Code Of Ethics: I acknowledge that I and all co-authors of this work have read and commit to adhering to the ICLR Code of Ethics
  One-sentence Summary: To aid neural networks to envision objects with different attributes,  we propose GSL which allows us to decompose inputs into a disentangled representation with swappable components, that can be recombined to synthesize new samples. 
  Supplementary Material:   zip