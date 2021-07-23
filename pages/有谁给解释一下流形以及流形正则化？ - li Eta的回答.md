- 作者：li Eta
  链接：https://www.zhihu.com/question/40794637/answer/88455767
  来源：知乎
- 看你标签有『机器学习』，那看来是问机器学习中的流形。机器学习中的流形借用了数学中流形的概念，机器学习并不真的去研究拓扑。更多的时候，机器学习中的流形是指数据分布在高维空间中的一个低维度的流形上面，意思就是数据本质上不是高维度的（所以处理起来不会像真正的高维数据一样困难）。
- 如图：
- <img src="https://pic2.zhimg.com/50/47f213d67585a7fe64f02e6720ca4f27_720w.jpg?source=1940ef5c" data-rawwidth="190" data-rawheight="197" class="content_image" width="190"/>
- 数据看似分布在一个三维空间中，而实际上则是分布在一个卷曲的二维平面上，也就是数据的真实分布其实只有二维。
- 直接在原始数据的高维空间中采用机器学习中的分类/回归方法，往往会面对高维度带来的模型高复杂度问题，导致模型的泛化能力下降，所以如果能够讲数据合理得展开在低维空间中，那么能够大大简化模型复杂度。
- 很多真实数据都具备类似的性质，比如：同一张正面人脸在不同光照环境下的图像集。
- 流形的概念很早就被引入到机器学习中，大量的降维方法都尝试从高维空间中复原出低维数据（也就是把上面这种三维卷曲摊开，放在二维平面上），包括PCA(Principal Components Analysis)、LLE(Locally Linear Embedding)、MDS(Multidimensional Scaling)、Isomap、KPCA等。回到问题中来，『流形正则化』其实就是在机器学习问题中的正则化项中加入和流形相关的项，利用数据中的几何结构，起到半监督的作用，比如：两个样本在流形中距离相近，那么他们的label也应该一样或相似。
- 参考paper: Manifold Regularization: A Geometric Framework for Learning from Labeled and Unlabeled Examples一个一般的机器学习有监督优化问题可以形式化成这样（式子都来自于上面的参考）：
- <img src="https://pic1.zhimg.com/50/f1f4e1fce466893efb35756bb121cca2_720w.jpg?source=1940ef5c" data-rawwidth="329" data-rawheight="71" class="content_image" width="329"/>
- 其中第一项是经验误差，第二项是正则化项（RKHS表示），而加入了流形正则化的优化问题可以形式化成：
- <img src="https://pic1.zhimg.com/50/77fe796dc7775832fd040ff66b97f88d_720w.jpg?source=1940ef5c" data-rawwidth="425" data-rawheight="70" class="origin_image zh-lightbox-thumb" width="425" data-original="https://pic1.zhimg.com/77fe796dc7775832fd040ff66b97f88d_r.jpg?source=1940ef5c"/>
- 其实就是多了最后一项，作用是约束 f 的输出使得输出的y符合样本x的分布所代表的几何结构。约束 f 输出的项可以是各种各样的，比如常见的graph regularization：
- <img src="https://pica.zhimg.com/50/61ee3ea7880ffaaa5bfe07ff1ff4a2a8_720w.jpg?source=1940ef5c" data-rawwidth="186" data-rawheight="61" class="content_image" width="186"/>
- 其中 W_ij 表示i和j两个样本之间在流形上的近似度。更加详细的细节（推导、解释以及这种优化目标对应的representor theorem的扩展）都在参考paper中。应用中这么几个作用：1. 利用样本的空间分布信息2. 给有监督模型加流形正则化，可以尽可能多得利用无监督的数据，使得模型转化为半监督模型编辑于 2016-02-29