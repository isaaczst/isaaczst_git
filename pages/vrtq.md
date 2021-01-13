---
title: vrtq
---

## [知乎年度最长科普文]—上帝公式 e^(iπ)=-1 与群论有什么关系？ - zdr0的文章 - 知乎 https://zhuanlan.zhihu.com/p/303377401

# [知乎年度最长科普文]—上帝公式 e^(iπ)=-1 与群论有什么关系？



[zdr0](https://www.zhihu.com/people/sai-27-16)

数学话题下的优秀答主



编辑推荐

等 3 项收录



1,896 人赞同了该文章

大家好！事情的起因是半个多月之前的一个晚上，我无意间在油管上看到了 3b1b 大佬的一个视频[[1\]](https://zhuanlan.zhihu.com/p/303377401#ref_1)。看完之后我突然“灵光一现”，打算就此写一个“观后感”。我大意了啊，没有停笔，很快这个“灵光”的光强就“烧掉了”我不少头发。

现在大家看到的这篇科普文是原文的“花絮”，无论是在长度上还是在难度上相较于原文都有所削减。因为原文是长达 **37 页**的 pdf，是本人写科普文以来写过的最长的一篇文章，也是我修改次数最多的一篇文章。并且在原文中对很多细节都做了比较详细的讨论，我把原文的下载链接放在了最后[[2\]](https://zhuanlan.zhihu.com/p/303377401#ref_2)，大家有兴趣的话可以去读一读。

如果各位读了原文，并发现了其中的 ***错误\*** 的话请一定 ***评论\*** 告知我(**请不要私信，除非有特殊情况，否则我一般不看私信**)。感谢！

最后的一个小通知：由于这学期我非常忙，所以《十分钟数学课》系列暂时停更，等下个假期再重新开更。并且专栏文章的更新速度会变得很慢。大家见谅。

------

> 在阅读本文之前，请 ***忘记\*** 你所熟知的 Euler 公式：
> ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ctheta%7D%3D%5Ccos%28%5Ctheta%29%2Bi%5Ccdot+%5Csin%28%5Ctheta%29.%5C%5C)
> 因为当你将 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta%3D%5Cpi) 代入时它会直接告诉你：
> ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Cpi%7D%3D-1%5C%5C)
> 但如果这样这篇文章就没有存在的意义了。

***总注：\***

> ![[公式]](https://www.zhihu.com/equation?tex=%28%5Crm+i%29.) 不要被文章后面那些“复杂的”符号“吓到了”。如果大家能够将前面基本符号的运作方式搞清楚，则后面那些“复杂”符号的运作方式大家也就能清楚了。并且我对每个符号都举了例子，相信大家通过这些例子一定可以清楚那些符号的运作方式。
> ![[公式]](https://www.zhihu.com/equation?tex=%28%5Crm+ii%29.) 文中的下划线没有特殊含义。
> ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7B%28iii%29.%7D) 群论部分我会尽量用最简单的语言讲清楚。这也是为了告诉大家 ***不要跳过\*** 文章中的任何一部分，因为每一部分都至关重要并且环环相扣。跳过其中一部分会对后面的阅读造成障碍。
> ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7B%28iv%29.%7D) 这次文中没有任何证明，可安心阅读。
> ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7B%28v%29.%7D) ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B1%5Csim+4%7D) 节的目录结构与内容与原文的目录结构与内容一致。

![[公式]](https://www.zhihu.com/equation?tex=%5CLARGE+%5Cbm%7B%5Crm%7BContents%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B1.%7D) 引言
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B2.%7D) 群
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B3.%7D) 群同态
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B4.%7D) 置换与置换群
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.%7D) 站在群的角度上来理解代数运算
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B6.%7D) 再看群同态与上帝公式和群论的关系

------

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B1%7D.%7D%7D) 引言

所谓上帝公式(即我们常说的 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7BEuler%7D) ***恒等式\*** )：

![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Cpi%7D%2B1%3D0.%5Ctag%7B1.1%7D)

这个公式充斥着无尽的美感，所以它也是我最喜欢的公式，没有之一。这个公式将自然底数 ![[公式]](https://www.zhihu.com/equation?tex=e) ，单位虚数 ![[公式]](https://www.zhihu.com/equation?tex=i) ，圆周率 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi) ，最小的自然数(这里认为![[公式]](https://www.zhihu.com/equation?tex=0)不是自然数) ![[公式]](https://www.zhihu.com/equation?tex=1) 与数字 ![[公式]](https://www.zhihu.com/equation?tex=0) 巧妙的组合在了一起。这个公式的起源有很多文章已经介绍过了，所以这篇文章我们就换一个视角来重新探索上帝公式背后隐藏的数学知识，而它背后的数学知识也告诉了我们上帝公式绝不仅仅只有表面上的这种数字关系。

为了探索这种探索上帝公式背后的数学知识，我们首先要来学一些群论的知识。

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B2%7D.%7D%7D) 群

我们先不看群的定义。现在让我们穿越回上小学的时候。上小学的时候，我们最先接触到的数字之间的运算就是两个数字之间的加法，更准确地说应该是两个自然数之间的加法。因为当时我们还不知道什么是整数，什么是小数等等。现在让我们脱离两个自然数之间的加法，来看一个更为高级运算，即 ***两个整数之间的加法\***。

为了与后面的群中的运算做对比，这里我们将整数集上的加法记作 ![[公式]](https://www.zhihu.com/equation?tex=+%2B_%7B%5Cmathbb%7BZ%7D%7D) (这与我们熟知的加法是一样的，只不过为其加上了下标 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 。其中 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 表示整数集。为一种运算添加这样的下标可以时刻提醒我们该运算是定义在哪个集合上的。这并非多此一举的做法，因为当运算种类增加的时候，如果没有这样的下标就可能会出现理解混乱)。

对于整数集上的加法我们知道它是满足结合律的，也就是说比如：

![[公式]](https://www.zhihu.com/equation?tex=%282%2B_%7B%5Cmathbb%7BZ%7D%7D3%29%2B_%7B%5Cmathbb%7BZ%7D%7D4%3D5%2B_%7B%5Cmathbb%7BZ%7D%7D4%3D2%2B_%7B%5Cmathbb%7BZ%7D%7D%283%2B_%7B%5Cmathbb%7BZ%7D%7D4%29%3D2%2B_%7B%5Cmathbb%7BZ%7D%7D7%3D9.%5Ctag%7B2.1%7D)

再比如：

![[公式]](https://www.zhihu.com/equation?tex=%28-5%2B_%7B%5Cmathbb%7BZ%7D%7D2%29%2B_%7B%5Cmathbb%7BZ%7D%7D7%3D-3%2B_%7B%5Cmathbb%7BZ%7D%7D7%3D4%3D-5%2B_%7B%5Cmathbb%7BZ%7D%7D%282%2B_%7B%5Cmathbb%7BZ%7D%7D7%29%3D-5%2B_%7B%5Cmathbb%7BZ%7D%7D9%3D4.%5Ctag%7B2.2%7D)

那么一般的，对于整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的任意三个整数 ![[公式]](https://www.zhihu.com/equation?tex=z_1%2C%5C%2Cz_2%2C%5C%2Cz_3%5Cin%5Cmathbb%7BZ%7D) ，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cz_1%2C%5C%2Cz_2%2C%5C%2Cz_3%5Cin%5Cmathbb%7BZ%7D%5C%2C%3A%5C%2C%28z_1%2B_%7B%5Cmathbb%7BZ%7D%7Dz_2%29%2B_%7B%5Cmathbb%7BZ%7D%7Dz_3%3Dz_1%2B_%7B%5Cmathbb%7BZ%7D%7D%28z_2%2B_%7B%5Cmathbb%7BZ%7D%7Dz_3%29.%5Ctag%7B2.3%7D)

除此以外我们还知道任何整数与整数 ![[公式]](https://www.zhihu.com/equation?tex=0) 的和都是该整数本身。比如：

![[公式]](https://www.zhihu.com/equation?tex=4%2B_%7B%5Cmathbb%7BZ%7D%7D0%3D0%2B_%7B%5Cmathbb%7BZ%7D%7D4%3D4%2C%5Cquad+-3%2B_%7B%5Cmathbb%7BZ%7D%7D0%3D0%2B_%7B%5Cmathbb%7BZ%7D%7D%28-3%29%3D-3.%5Ctag%7B2.4%7D)

即对于任意一个整数 ![[公式]](https://www.zhihu.com/equation?tex=z%5Cin%5Cmathbb%7BZ%7D) 而言，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cz%5Cin%5Cmathbb%7BZ%7D%5C%2C%3A%5C%2Cz%2B_%7B%5Cmathbb%7BZ%7D%7D0%3D0%2B_%7B%5Cmathbb%7BZ%7D%7Dz%3Dz.%5Ctag%7B2.5%7D)

因为整数 ![[公式]](https://www.zhihu.com/equation?tex=0) 的这种性质，我们将整数 ![[公式]](https://www.zhihu.com/equation?tex=0) 称为整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的 ***对加法\*** ***![[公式]](https://www.zhihu.com/equation?tex=%2B_%7B%5Cmathbb%7BZ%7D%7D)\*** ***的单位元素\*** 。同样是为了与将来群中的单位元素做对比，我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 的单位元素 ![[公式]](https://www.zhihu.com/equation?tex=0) 记作 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) 。

此外，对整数集中的每一个整数都存在一个“与之相反的”整数，使得两者的和为 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) 。比如：

![[公式]](https://www.zhihu.com/equation?tex=-5%2B_%7B%5Cmathbb%7BZ%7D%7D5%3D5%2B_%7B%5Cmathbb%7BZ%7D%7D%28-5%29%3D0_%7B%5Cmathbb%7BZ%7D%7D.%5Ctag%7B2.6%7D)

所以一般的，对于任意一个整数 ![[公式]](https://www.zhihu.com/equation?tex=z%5Cin%5Cmathbb%7BZ%7D) ，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cz%5Cin%5Cmathbb%7BZ%7D%2C%5Cquad+z%2B_%5Cmathbb%7BZ%7D%28-z%29%3D%28-z%29%2B_%5Cmathbb%7BZ%7Dz%3D0_%5Cmathbb%7BZ%7D.%5Ctag%7B2.7%7D)

这样的一个整数 ![[公式]](https://www.zhihu.com/equation?tex=-z) 我们称为整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的***整数\*** ***![[公式]](https://www.zhihu.com/equation?tex=z)\*** ***的对加法\*** ***![[公式]](https://www.zhihu.com/equation?tex=+%2B_%7B%5Cmathbb%7BZ%7D%7D)\*** ***的逆元\***。同样是为了与将来群中的逆元做对比，这里我们将整数 ![[公式]](https://www.zhihu.com/equation?tex=z) 的逆元记作 ![[公式]](https://www.zhihu.com/equation?tex=-z_%7B%5Cmathbb%7BZ%7D%7D) 。

最后我们要说的是两个整数的和一定还是一个整数，我们将此性质称为***整数集对其上的加法\*** ***![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D)\*** ***是封闭的\*** 。

另外，我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) 看做是一种作用，这个作用的效果是将输入的两个整数通过相加的方式变成第三个整数。这就意味着我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) 看做是一个映射：

![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D%3A%5Cmathbb%7BZ%7D%5Ctimes%5Cmathbb%7BZ%7D%5Cto%5Cmathbb%7BZ%7D%2C%5Cquad+%28z_1%2Cz_2%29%5Cmapsto+z_1%2B_%7B%5Cmathbb%7BZ%7D%7Dz_2.%5Ctag%7B2.8%7D)

这样一个映射也可以说明整数集对其上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) 是封闭的。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 显然，整数集上的单位元素是唯一的，即为 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) ，且对每个整数 ![[公式]](https://www.zhihu.com/equation?tex=z%5Cin%5Cmathbb%7BZ%7D) ，其逆元也是唯一的，即为 ![[公式]](https://www.zhihu.com/equation?tex=-z%5Cin%5Cmathbb%7BZ%7D) 。(注意，这里 ***不要\*** 说成整数集中的逆元是唯一的)

大家如果能完全理解上述有关整数的加法的例子话那么就成功了 ![[公式]](https://www.zhihu.com/equation?tex=99.%5Coverline%7B9%7D%5C%25) 啦～因为通过类比，我们可以非常轻松又快速地理解群的定义。下面我们就给出群的定义：

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bblue%7D%7B%5Clarge%7B%5Cbm%7B%5Crm%7BDefinition%5Cquad+2.1%3A%7D%7D%7D%7D)

设 ![[公式]](https://www.zhihu.com/equation?tex=M) 是一个集合，且设 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M) 为 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的一个运算：

![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M%3AM%5Ctimes+M%5Cto+M%2C%5Cquad+%28m_1%2Cm_2%29%5Cmapsto+m_1%5Ccirc_M+m_2.%5Ctag%7B2.9%7D)

则称结构 ![[公式]](https://www.zhihu.com/equation?tex=%28M%2C%5Ccirc_M%29) 是一个 ***群\*** ，当它满足以下条件时：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M) 是可结合的；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) (至少)存在一个 ![[公式]](https://www.zhihu.com/equation?tex=e_M%5Cin+M) ，使得对于所有的 ![[公式]](https://www.zhihu.com/equation?tex=m%5Cin+M) 有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2C+m%5Cin+M%5C%2C%3A%5C%2Ce_M%5Ccirc_M+m%3Dm%5Ccirc_M+e_M%3Dm.%5Ctag%7B2.10%7D)

这样的一个 ![[公式]](https://www.zhihu.com/equation?tex=e_M%5Cin+M) 称为 ![[公式]](https://www.zhihu.com/equation?tex=M) 中的 ***单位元素\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 对于每个 ![[公式]](https://www.zhihu.com/equation?tex=m%5Cin+M) ，存在(至少)一个 ![[公式]](https://www.zhihu.com/equation?tex=n_%7BM%7D%5Cin+M) ，使得：

![[公式]](https://www.zhihu.com/equation?tex=m%5Ccirc_M+n_%7BM%7D%3Dn_%7BM%7D%5Ccirc_M+m%3De_M.%5Ctag%7B2.11%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bblue%7D%7B%5Cblacksquare%7D)

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 显然，当我们将定义 ![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbm%7B%5Crm%7BDefinition%5Cquad+2.1%7D%7D%7D) 中的集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 换成集合 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) ，将运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M) 换成整数集上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) ，将集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 中的单位元素 ![[公式]](https://www.zhihu.com/equation?tex=e_M) 换成整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的单位元素 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) ，将 ![[公式]](https://www.zhihu.com/equation?tex=m%2Cm_1%2Cm_2%5Cin+M) 换成 ![[公式]](https://www.zhihu.com/equation?tex=z%2Cz_1%2Cz_2%5Cin%5Cmathbb%7BZ%7D) ，将 ![[公式]](https://www.zhihu.com/equation?tex=n_M%5Cin%5Cmathbb%7BM%7D) 换成 ![[公式]](https://www.zhihu.com/equation?tex=-z_%7B%5Cmathbb%7BZ%7D%7D%5Cin%5Cmathbb%7BZ%7D) 时我们就可以理解群的定义了。

根据群的定义我们可以知道 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BZ%7D%2C%2B_%5Cmathbb%7BZ%7D%29) 是一个群，我们将这个群称为 ***整数加法群\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+2.1%3A%7D%7D%7D%7D)

请可各位读者朋友独立验证 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%7B%5Cmathbb%7BR%7D%7D%29) 与 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BC%7D%2C%2B_%7B%5Cmathbb%7BC%7D%7D%29) 也是两个群。且前者称为 ***实数加法群\*** ，后者称为 ***复数加法群\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D)

认识了什么是群之后我们就已经结束了三分之一的工作啦～打起精神，一鼓作气，把剩下的群的知识学完！下面将要介绍的一个重要的概念是 ***群同态 。\***

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B3%7D.%7D%7D) 群同态

这个名词听起来挺高端的是吧？其实我们通过一个我们高中就学过的函数便可以“可视化”群同态这个概念，进而让这个概念变得很好理解。下面我们就从这个函数讲起。

这个函数就是自然底数 ![[公式]](https://www.zhihu.com/equation?tex=e) 的指数函数。我们知道同底数的(这里为 ![[公式]](https://www.zhihu.com/equation?tex=e) )指数运算律为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28x_1%2Bx_2%29%3D%5Cexp%28x_1%29%5Ccdot%5Cexp%28x_2%29%2C%5Cquad+x_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B3.1%7D)

我们知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28x%29) 的定义域是实数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D) ，值域是正实数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%3E0%7D) 。所以，不严谨地可以说：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cx_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D%5C%2C%3A%5C%2C%5Cexp%28x_1%29%5Ccdot%5Cexp%28x_2%29%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D.%5Ctag%7B3.2%7D)

此时我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot) 写为正实数集上的乘法，即 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D) 。这是因为这里正实数集对 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D) 是封闭的，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%3A%5Cmathbb%7BR%7D_%7B%3E0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Cquad+%28%5Cexp%28x_1%29%2C%5Cexp%28x_2%29%29%5Cmapsto+%5Cexp%28x_1%29%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%5Cexp%28x_2%29%5Ctag%7B3.3%7D.)

又因为 ![[公式]](https://www.zhihu.com/equation?tex=x_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D) ，所以我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%2B) 写为实数域上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%7B%5Cmathbb%7BR%7D%7D) 。如之前所述， ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%7B%5Cmathbb%7BR%7D%7D%29) 是一个群。并且容易验证 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29) 是一个乘法群(作为练习，请各位自行验证。注意， ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D) 的封闭性已经说过了，只需验证剩下三条即可)。于是现在我们得到了两个群，我们将两者分别定义为：

![[公式]](https://www.zhihu.com/equation?tex=G%3A%3D%28%5Cmathbb%7BR%7D%2C%2B_%5Cmathbb%7BR%7D%29%2C%5Cquad+H%3A%3D%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29.%5Ctag%7B3.4%7D)

则在这两个群之间的映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%3AG%5Cto+H) 满足：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cx_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D%5C%2C%3A%5C%2C%5Cexp%5Cleft%28x_1%2B_%7B%5Cmathbb%7BR%7D%7Dx_2%5Cright%29%3D%5Cexp%28x_1%29%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%5Cexp%28x_2%29.%5Ctag%7B3.5%7D+)

如果现在我们将群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%5Cmathbb%7BR%7D%29) 与群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29) 换成为两个一般的群 ![[公式]](https://www.zhihu.com/equation?tex=%28G%2C%5Ccirc_G%29) 和 ![[公式]](https://www.zhihu.com/equation?tex=%28H%2C%5Ccirc_H%29) ，群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%5Cmathbb%7BR%7D%29) 与群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29) 之间的映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp) 换成任意一个映射 ![[公式]](https://www.zhihu.com/equation?tex=f) ，但是使 ![[公式]](https://www.zhihu.com/equation?tex=f) 仍保持性质：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cg_1%2C%5C%2Cg_2%5Cin+G%5C%2C%3A%5C%2Cf%28g_1%5Ccirc_G+g_2%29%3Df%28g_1%29%5Ccirc_H+f%28g_2%29.%5Ctag%7B3.6%7D)

则 ![[公式]](https://www.zhihu.com/equation?tex=f) 就称为群 ![[公式]](https://www.zhihu.com/equation?tex=G) 与群 ![[公式]](https://www.zhihu.com/equation?tex=H) 之间的一个群同态。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 可以将式 ![[公式]](https://www.zhihu.com/equation?tex=%283.6%29) 与式 ![[公式]](https://www.zhihu.com/equation?tex=%283.5%29) 做一个类比：
> ![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+%26x_i%3Dg_i%2C%5Cquad+i%3D1%2C2%2C%5C%5C+%26G%3D%5Cmathbb%7BR%7D%2C%5C%5C+%26H%3D%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5C%5C+%26f%3D%5Cexp%2C%5C%5C+%26%5Ccirc_G%3D%2B_%5Cmathbb%7BR%7D%2C%5C%5C+%26%5Ccirc_H%3D%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D.+%5Cend%7Barray%7D%5C%5C)
>
> 这样群同态就好理解了。

下面我就要给出群同态的定义了。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bblue%7D%7B%5Clarge%7B%5Cbm%7B%5Crm%7BDefinition%5Cquad+3.1%3A%7D%7D%7D%7D)

设 ![[公式]](https://www.zhihu.com/equation?tex=%28G%2C%5Ccirc_G%29) 与 ![[公式]](https://www.zhihu.com/equation?tex=%28H%2C%5Ccirc_H%29) 是两个群。一个从群 ![[公式]](https://www.zhihu.com/equation?tex=G) 到群 ![[公式]](https://www.zhihu.com/equation?tex=H) 的群同态是一个映射 ![[公式]](https://www.zhihu.com/equation?tex=f%3AG%5Cto+H) ，对该映射有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cg_1%2C%5C%2Cg_2%5Cin+G%5C%2C%3A%5C%2Cf%28g_1%5Ccirc_G+g_2%29%3Df%28g_1%29%5Ccirc_H+f%28g_2%29.%5Ctag%7B3.7%7D)

我们将所有从群 ![[公式]](https://www.zhihu.com/equation?tex=G) 到群 ![[公式]](https://www.zhihu.com/equation?tex=H) 的同态 ![[公式]](https://www.zhihu.com/equation?tex=f) 的集合记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BHom%7D%28G%2CH%29) 。而且最为正规的记法为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BHom%7D_%7B%5Cmathrm%7BGroup%7D%7D%28%28G%2C%5Ccirc_G%29%2C%28H%2C%5Ccirc_H%29%29.%5Ctag%7B3.8%7D+)

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bblue%7D%7B%5Cblacksquare%7D)

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B4%7D.%7D%7D) 置换与置换群

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B4.1%7D%7D) **置换**

新的知识又出现啦！我们还是先讲一个直观的例子。

<img src="https://pic4.zhimg.com/80/v2-06ac1fb9664101089a9a6a4184a1b013_1440w.jpg" alt="img" style="zoom:67%;" />



图片1

如图片 1 所示，我们将一个正方形的顶点自左上开始，按照顺时针方向从 ① 到 ④ 进行了编号。这样做的目的是为了让大家能够最直观的看到这个正方形所做的所有旋转和镜像变换。

现在我们来总结一下上面正方形的八种变换，它们分别是：什么也不做 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BId%7D) 围绕中心做逆时针 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D%2C%5C%2C180%5E%7B%5Ccirc%7D%2C%5C%2C270%5E%7B%5Ccirc%7D) 的旋转，关于两条平行于边的对称轴的镜像，以及关于两个对角线的镜像。

这样用文字描述变换实在是很不方便，所以我们现在来做一件有意思的事情，就是使用数字来表示这些变换。首先我们按照从 ①![[公式]](https://www.zhihu.com/equation?tex=%28%3D1%29) 到 ④![[公式]](https://www.zhihu.com/equation?tex=%28%3D4%29) 的顺序将处于初始状态的正方形的顶点写在一个括号中，比如像这样：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.1%7D)

这里需要注意：处于初始状态与不对这个正方形做任何变换不是一回事！现在我们让这个写有初始状态顶点所对应的数字的括号变得大一些：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+%5Cstar+%26+%5Cstar+%26+%5Cstar+%26%5Cstar+%5Cend%7Bpmatrix%7D%5Ctag%7B4.1.2%7D)

即我们在原先的括号下面又增加了一行，那么这一行要写什么呢？在回答这个问题之前我们要明确的是，除了不对正方形做变换这种情况以外，其他七种情况下，只要对正方形做了变换，那么变换之后正方形的每个顶点数字相对于初始状态的顶点数字都发生了变化。于是这一行要写的就是：正方形做了某一次变换后，相对于初始状态的顶点对应数字的变化。举两个具体的例子好了，首先就是最特殊的，我们不对正方形做任何变换，那么此时正方形的状态与处于初始状态时是一致的，即顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) 依然对应顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) ，顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) 依然对应顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) ...等等，所以此时第二行应该写的是：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+1+%26+2+%26+3+%26+4+%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.3%7D)

再比如正方形做了一个 ![[公式]](https://www.zhihu.com/equation?tex=270%5E%7B%5Ccirc%7D) 的旋转，那么对于旋转之后的顶点我们有：顶点 ![[公式]](https://www.zhihu.com/equation?tex=4) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) ；顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) ；顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=3) ；顶点 ![[公式]](https://www.zhihu.com/equation?tex=3) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=4) 。于是此时，我们的第二行应该写：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+4+%26+1+%26+2+%26+3+%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.4%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+4.1.1%3A%7D%7D%7D%7D)

请大家尝试将剩余的 ![[公式]](https://www.zhihu.com/equation?tex=6) 的情况写出来。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D)

这样我们就实现了通过数字取描述正方形的这八种变换了。因为我们可以将处于初始状态的被数字 ![[公式]](https://www.zhihu.com/equation?tex=1%5Csim+4) 标记的正方形的四个顶点看成是 ![[公式]](https://www.zhihu.com/equation?tex=1) 号到 ![[公式]](https://www.zhihu.com/equation?tex=4) 号这四个位置，然后正方形每做一次变换这四个位置上的某几个数字就会出现更替，我们将更替之后的数字与 ![[公式]](https://www.zhihu.com/equation?tex=1) 号到 ![[公式]](https://www.zhihu.com/equation?tex=4) 号这四个位置一一对应起来就可以描述这种变换了。

很显然，数字的更替意味着数字相对于初始状态时的位置发生了变换，因此，我们将这些变换都称为 ***置换\*** 。

通过上述例子，相信大家对置换的概念已经有了一个基本的认识了，现在我们来深化一下置换的概念。我们还是继续上面的例子。

现在让我们 ***脱离正方形这个实体\*** ，而仅考虑 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字。我们还是先将 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 按照顺序写在一个括号中的第一行：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+%5Cstar+%26+%5Cstar+%26+%5Cstar+%26+%5Cstar++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.5%7D)

这里的第二行我们写 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字在做某种重新排列之后的结果，比如 ![[公式]](https://www.zhihu.com/equation?tex=2%2C1%2C4%2C3) ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.6%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+4.1.2%3A%7D%7D%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5C%5C)

对应了之前正方形的八种变换中的哪一种？

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D)

显然，第一行的数字经过这“某种重新排列”之后被重新排序，重新排序的结果是第二行的元素。现在我将所有的对应关系写出来，以方便大家理解：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+2+%5C%5C+%26+2%5Cto+1+%5C%5C+%26+3%5Cto+4+%5C%5C+%26+4%5Cto+3.+%5Cend%7Balign%2A%7D%5Ctag%7B4.1.7%7D)

通过所列出的所有对应关系我们可以发现：这种所谓的“重新排列”的变换实际上是一种映射关系，即 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每一个数字都通过这种映射变成 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B1%2C2%2C3%2C4%7D) ***这四个数字中的\*** 另一个。我们现在将该映射记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) ，然后我们可以将上面列出的四种关系写为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+%5Csigma%281%29%3D2+%5C%5C+%26+2%5Cto+%5Csigma%282%29%3D1+%5C%5C+%26+3%5Cto+%5Csigma%283%29%3D4+%5C%5C+%26+4%5Cto+%5Csigma%284%29%3D3.+%5Cend%7Balign%2A%7D.%5Ctag%7B4.1.8%7D)

现在我们可以说： ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这种排列顺序经过映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 的作用变成了 ![[公式]](https://www.zhihu.com/equation?tex=2%2C1%2C4%2C3) 这种排列顺序。现在我们将这种对应关系在之前的括号中可得：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+%5Csigma%281%29+%26+%5Csigma%282%29+%26+%5Csigma%283%29+%26+%5Csigma%284%29++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.9%7D)

当然，对于不同的重新排列我们的映射也是不同的，比如现在有如下的对应关系：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+4+%5C%5C+%26+2%5Cto+1+%5C%5C+%26+3%5Cto+2+%5C%5C+%26+4%5Cto+3.+%5Cend%7Balign%2A%7D.%5Ctag%7B4.1.10%7D)

显然，我们刚才的映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 并不能实现这种从 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 到 ![[公式]](https://www.zhihu.com/equation?tex=4%2C1%2C2%2C3) 的这种排列，因为比如 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%281%29%3D2%5Cne+4) 。但是我们可以找到另外一个映射，使得这个映射可以实现这种重新排列呀。比如我们可以将这个映射记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) ，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+%5Ctau%281%29%3D4+%5C%5C+%26+2%5Cto+%5Ctau%282%29%3D1+%5C%5C+%26+3%5Cto+%5Ctau%283%29%3D2+%5C%5C+%26+4%5Cto+%5Ctau%284%29%3D3.+%5Cend%7Balign%2A%7D%5Ctag%7B4.1.11%7D)

现在我们在置换的概念上又更近一步了，但是还缺乏严谨性。比如映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )具有什么性质呢？对于任意一个可数的有限集合我们如何定义这个一个映射呢？这种映射之间可以复合吗？复合所产生的效果又是什么呢？下面我们就一一来回答这些问题。

从我们刚刚所说的例子中我们发现：无论是映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 还是映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) 它们都具有以下性质：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 当映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )作用于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每个数字时，其结果也必然是这四个数字中的某一个，而不会出现别的数字。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 当映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )作用于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每个数字时，每个结果都是不同的，比如：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%281%29%3D2%2C%5Cquad+%5Csigma%282%29%3D1%2C%5Cquad%5Csigma%283%29%3D4%2C%5Cquad+%5Csigma%284%29%3D3.%5Ctag%7B4.1.12%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 当映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )作用于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每个数字时，每个数字在映射的作用下都会得到一个结果。

综合以上三条，我们现在可以说映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )是一个从集合 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) 到自身上的一个双射。拿映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 举例，我们可以将它定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3A%5C%7B1%2C2%2C3%2C4%5C%7D%5Cto%5C%7B1%2C2%2C3%2C4%5C%7D%2C%5Cquad+%5Csigma%28i%29%3Dj%2C%5C%2C%5C%2Ci%2Cj%3D1%2C2%2C3%2C4.%5Ctag%7B4.1.13%7D)

其实定义了这样一个映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 之后我们就得到了关于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 的全部置换了。也就是说将来我们就不再区分 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 和 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) 了。

现在我们来回答第二个问题：对于任意一个可数的有限集合我们如何定义这个一个映射呢？从上一个问题的答案中我们知道，这样的一个映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 是一个集合到自身的双射，而这里的集合必须是 ***有限可数集合\*** 。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 这里的有限可数集合可以 ***非常不严谨地\*** 理解为：可以清点这样一个集合中的全部元素。

现在我们就来考察一个最简单的有限可数集合—由 ![[公式]](https://www.zhihu.com/equation?tex=1) 到 ![[公式]](https://www.zhihu.com/equation?tex=n) 这 ![[公式]](https://www.zhihu.com/equation?tex=n) 个自然数构成的集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D) 。则对于这样的一个集合我们可以定义置换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) ：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3A%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D%5Cto%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D%2C%5Cquad+%5Csigma%28i%29%3Dj%2C%5C%2C%5C%2Ci%2Cj%3D1%2C2%2C%5Cldots%2Cn.%5Ctag%7B4.1.14%7D)

我们也可以将其写为括号的形式，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+%5Cldots+%26+n+%5C%5C+%5Csigma%281%29+%26+%5Csigma%282%29+%26+%5Cldots+%26+%5Csigma%28n%29++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.15%7D)

更为一般地，我们可以对任意一个与集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D) ***等势的\*** 集合 ![[公式]](https://www.zhihu.com/equation?tex=X%3D%5C%7Bx_1%2Cx_2%2C%5Cldots%2Cx_n%5C%7D) 定义置换：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3AX%5Cto+X%2C%5Cquad+%5Csigma%28x_i%29%3Dx_j%2C%5C%2C%5C%2Ci%2Cj%3D1%2C2%2C%5Cldots%2Cn.%5Ctag%7B4.1.16%7D)

或将其写为括号的形式：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3D%5Cbegin%7Bpmatrix%7D+x_1+%26+x_2+%26+%5Cldots+%26+x_n+%5C%5C+%5Csigma%28x_1%29+%26+%5Csigma%28x_2%29+%26+%5Cldots+%26+%5Csigma%28x_n%29++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.17%7D)

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 这里的等势可以 ***非常不严谨地\*** 理解为：集合 ![[公式]](https://www.zhihu.com/equation?tex=X%3D%5C%7Bx_1%2Cx_2%2C%5Cldots%2Cx_n%5C%7D) 与集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D) 具有“相同的”元素个数。

现在我们来到了一个关键性的问题面前：两个置换之间是否可以进行复合？为了回答这个问题，我们再次回到之前所说的正方形的例子。首先非常显然的是我们现在处于初始状态的正方形逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后在此基础上再逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=180%5E%7B%5Ccirc%7D) 就相当于直接从初始状态逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=270%5E%7B%5Ccirc%7D) 。
另外一个不是十分明显的例子是：

![img](https://pic2.zhimg.com/80/v2-90a620118733af9a2f9bcef9aaa9d551_1440w.jpg)图

片2

即我们先将处于初始状态的正方形逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后在此基础上再将其关于连结左上和右下顶点的对角线进行镜像，所得到的结果与直接对处于初始状态的正方形关于竖直对称轴镜像的结果是一致的。图片2中的中的复合 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 表示的是变换的复合，也就是说“将处于初始状态的正方形逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后在此基础上再将其关于连结左上和右下顶点的对角线进行镜像”是一个***复合变换\*** ，其效果与单次变换“将处于初始状态的正方形关于竖直对称轴镜像”的结果是一致的。
同样我们发现，使用文字来描述这个复合变换是在是非常的繁琐。既然我们之前已经使用数字去表示置换了，那我们现在就使用这些数字去表示复合变换，即表示置换的复合。对于置换的复合，我们仍然使用符号 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 。
由之前所述我们知道，“将处于初始状态的正方形逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ”这个变换的数字表述为：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3D+%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+3+%26+4+%26+1++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.18%7D)

而“将处于初始状态的正方形关于连结左上和右下顶点的对角线进行镜像”这个变换的数字表述为：

![[公式]](https://www.zhihu.com/equation?tex=%5Ctau%3D+%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+1+%26+4+%26+3+%26+2++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.19%7D)

最后，“将处于初始状态的正方形关于竖直对称轴镜像”这个变换的数字表述为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.20%7D)

于是，根据刚刚对复合变换的文字描述，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5Ccirc%5Ctau%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+3+%26+4+%26+1++%5Cend%7Bpmatrix%7D%5Ccirc%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+1+%26+4+%26+3+%26+2++%5Cend%7Bpmatrix%7D%3D+%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.21%7D)

对于这一点我们可以来验证一下。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26%28%5Csigma%5Ccirc%5Ctau%29%281%29%3D%5Csigma%28%5Ctau%281%29%29%3D%5Csigma%281%29%3D2%2C%5C%5C+%26%28%5Csigma%5Ccirc%5Ctau%29%282%29%3D%5Csigma%28%5Ctau%282%29%29%3D%5Csigma%284%29%3D1%2C%5C%5C+%26%28%5Csigma%5Ccirc%5Ctau%29%283%29%3D%5Csigma%28%5Ctau%283%29%29%3D%5Csigma%283%29%3D4%2C%5C%5C+%26%28%5Csigma%5Ccirc%5Ctau%29%284%29%3D%5Csigma%28%5Ctau%284%29%29%3D%5Csigma%282%29%3D3.+%5Cend%7Balign%2A%7D%5Ctag%7B4.1.22%7D)

显然，我们是对的！
通过这个直观的例子我们可以明白一个十分重要的问题：***置换之间是可以进行复合的，且复合之后的可以得到一个“新的”置换。并且从初始状态通过复合置换得到的结果与从初始状态直接通过这个“新的”置换得到的结果必然是一致的\*** 。而且如果你愿意的话，你甚至可以将多个置换进行复合。


![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B4.2%7D%7D) **置换群**
现在我们已经认识了群、群同态以及置换的概念了。下面我们来介绍 ***置换群\*** 。置换群中的元素是一个非空集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的置换。一个具体的例子就是我们刚才所举的集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C3%2C4%5C%7D) 上的置换 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C3%2C4%5C%7D) 。那么现在就产生了几个基本的问题：
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 置换群中的运算是什么？
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 置换群中的单位元素是什么？
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 置换群中各个元素的逆元是什么？
这些基本的问题都是关于群的定义的问题。下面我们还是来一一解答一下。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 首先是置换群中的运算。置换群中的运算就是我们之前所提到的两个置换之间的复合运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 。容易验证该运算是满足结合律的，且非空集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的置换所构成的集合对该运算是封闭的。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 置换群中的单位元素我们记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7B%7BId%7D%7D) 。之前正方形置换的例子中，“什么也不做”这一变换就是正方形置换的置换群中的单位元素。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 置换群中的元素 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 的逆元我们记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E%7B-1%7D) ，因为：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5Ccirc%5Csigma%5E%7B-1%7D%3D%5Csigma%5E%7B-1%7D%5Ccirc%5Csigma%3D%5Cmathrm%7BId%7D.%5Ctag%7B4.2.1%7D)

一个直观的例子是：设变换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 为将正方形逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，则 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E%7B-1%7D) 表示的就是将正方形顺时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，那两个变换的复合变换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5Ccirc%5Csigma%5E%7B-1%7D) 就是将正方形先绕中心逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后再将正方形绕中心顺时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，那么最后的结果与“什么也不做”(即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BId%7D) )这一变换是一样的。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D) 置换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 的逆是存在的，因为我们之前说过，置换是一个双射。
一个以集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的全部置换为元素的群我们称为 ![[公式]](https://www.zhihu.com/equation?tex=M) 的 ***对称群\*** ，并记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BSym%7D%28M%29) 。但集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 具有 ![[公式]](https://www.zhihu.com/equation?tex=n) 则元素时， ![[公式]](https://www.zhihu.com/equation?tex=M) 的对称群可以记作 ![[公式]](https://www.zhihu.com/equation?tex=S_n) ，称为 ![[公式]](https://www.zhihu.com/equation?tex=n) 次对称群。现在我们在这篇文章中所需要的知识已经全部学完了。群论是一个非常庞大的知识体系，我这里也仅仅是为了写这篇科普文章才简单的介绍了一下群的一些基本概念。其他更深的知识就请对群论感兴趣的朋友自行探索吧。

##  ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge%5Cbm%7B%5Crm%7B5.%7D%7D) **站在群的角度上来理解代数运算**

在本节中，我们将要“忘记”我们熟知的基本的代数运算加法和乘法。我们会将数字理解为一些作用，通过这些作用可以将原来的数字变成新的数字。在定义后面的这些作用的时候我们会 ***仿照定义置换时所使用的那种括号的形式\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B%5Crm%7B5.1%7D%7D%7D) **整数的滑动与实数的滑动**
首先我们来定义滑动的概念。为了进一步的讨论和方便大家的理解，我们就将滑动的概念定义在整数集上。我们这里将要仿照置换的定义对滑动进行定义。首先我们还是来看直观的例子。

![img](https://pic2.zhimg.com/80/v2-0a09412a43e8bc2da23017e443270bfd_1440w.jpg)

图片3

如图片 3 所示，为了保证直观性，我们定义了所谓的“整数轴”，整数轴只在具体的整数处为点，其余各处均为虚线。现在我们对整数轴做一个向右滑动的动作，这个动作使整个整数轴向右滑动了一个单位。特别的，如果我们只观察数字 ![[公式]](https://www.zhihu.com/equation?tex=0) 的话，我们发现它通过这种滑动滑到了原来数字 ![[公式]](https://www.zhihu.com/equation?tex=1) 的位置上。这样一个滑动作用使我们有了以下的对应关系：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D++%5Cldots%5C%5C++-4%5Cto+-3%5C%5C++-3%5Cto+-2%5C%5C++-2%5Cto+-1%5C%5C++-1%5Cto+0%5C%5C++0%5Cto+1%5C%5C++1%5Cto+2%5C%5C++2%5Cto+3%5C%5C++%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.1.1%7D)

显然，上述的对应关系蕴含了一种映射关系，我们将这个映射记为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bv%7D) ，则：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D++%5Cldots%5C%5C++-4%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-4%29%3D-3%5C%5C++-3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-3%29%3D-2%5C%5C++-2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-2%29%3D-1%5C%5C++-1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-1%29%3D0%5C%5C++0%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%280%29%3D1%5C%5C++1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%281%29%3D2%5C%5C++2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%282%29%3D3%5C%5C++%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.1.2%7D)

虽然整数集是一个可数无穷集，但是我们依然可以 ***借助\*** 置换那里的记号，将上述映射关系写在一个括号中，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%3A%3D%5Cbegin%7Bpmatrix%7D+%5Cldots+%26+-4+%26+-3+%26+-2+%26+-1+%26+0+%26+1+%26+2+%26+3+%26%5Cldots+%5C%5C+%5Cldots+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-4%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-3%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-2%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-1%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%280%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%283%29+%26+%5Cldots++%5Cend%7Bpmatrix%7D.%5Ctag%7B5.1.3%7D)

这样我们就可以定义 ***整数集上的一个向右的滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%3A%5Cmathbb%7BZ%7D%5Cto%5Cmathbb%7BZ%7D%2C%5Cquad+i%5Cmapsto+i%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamond%7D+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BZ%7D.%5Ctag%7B5.1.4%7D)

***整数集上的一个向左的滑动为\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bv%7D%3A%5Cmathbb%7BZ%7D%5Cto%5Cmathbb%7BZ%7D%2C%5Cquad+i%5Cmapsto+i%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BZ%7D.%5Ctag%7B5.1.5%7D)

下面通过几个例子说明几个问题。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 比如先将整数 ![[公式]](https://www.zhihu.com/equation?tex=1) 向右滑动 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamond%7D+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=4) 然后再将 ![[公式]](https://www.zhihu.com/equation?tex=4) 向左滑动 ![[公式]](https://www.zhihu.com/equation?tex=5) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=4%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+5) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=-1) ，这与直接将 ![[公式]](https://www.zhihu.com/equation?tex=1) 向左滑动两个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+2) 得到的结果是一样的。这说明了 ***整数的滑动是可以复合的\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 将任意一个整数滑动任意一个固定的整数单位 ![[公式]](https://www.zhihu.com/equation?tex=j) 所得到的结果都是唯一的，这说明了整数的滑动是可逆的(即双射的)。并且具体的，将整数 ![[公式]](https://www.zhihu.com/equation?tex=1) 向右滑动 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamond%7D+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=4) 然后再将 ![[公式]](https://www.zhihu.com/equation?tex=4) 向左滑动 ![[公式]](https://www.zhihu.com/equation?tex=3) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=4%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+3) ，结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=1) 。这说明了对 ***任意一个固定的整数单位\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7Bj%7D) ***，左滑动与右滑动互为逆元\*** 。且对任意一个固定整数单位 ![[公式]](https://www.zhihu.com/equation?tex=j) 的左滑动与右滑动的复合为 ***单位元\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B%5Cmathrm%7BId%7D_V%7D) ，表示“不做滑动”。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 显然，整数的任意两个滑动的复合还是一个整数的滑动。***即定义在整数集上的滑动对复合运算\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) ***是封闭的\***。
有了整数的滑动以后我们就可以仿照它来定义实数的滑动了。***实数的一个向右的滑动\*** 定义为：

![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%3A%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.1.6%7D)

***实数的一个向左的滑动为\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%3A%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.1.7%7D)

同理，我们可以说明实数的滑动也是：
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 可以复合的。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 双射的，且具有逆元和单位元。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%7D%29.) 对复合是封闭的。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+5.1.1%3A%7D%7D%7D%7D)
请大家自行验证以上三条，对内容的理解会有一定帮助。
![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D+)


![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B%5Crm%7B5.2%7D%7D%7D) **非零有理数与非零实数的伸缩**
![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbm%7B5.2.1%7D%7D) **正有理数与负有理数的伸缩**
作为引入，首先我们先来考察正有理数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BQ%7D_%7B%3E0%7D) 。我们先来定义正有理数集上的伸缩。

![img](https://pic1.zhimg.com/80/v2-5eb5f45a0b9a869800a324c500fbf12c_1440w.jpg)图片4

如图片 4 所示，我们这里又定义了一个“正有理数轴”(正有理数轴的虚线比整数轴稍微密了一点，这只是为了做一下区分)。现在我们对这个正有理数轴做一个拉长的动作，这个动作将整个正有理数轴拉长为原来的两倍(这就意味着做正有理数轴上的每一个点都被“拉长为”原来的两倍)。如果我们只观察正有理数 ![[公式]](https://www.zhihu.com/equation?tex=1) 的话，我们会发现它通过这种拉长的作用变为的原来的正有理数 ![[公式]](https://www.zhihu.com/equation?tex=2) 。因此对于这样一个拉长的作用我们有以下对应关系：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+1%5Cto+2%5C%5C+2%5Cto+4%5C%5C+3%5Cto+6%5C%5C+4%5Cto+8%5C%5C+5%5Cto+10%5C%5C+6%5Cto+12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.1%7D)

显然，上述的对应关系也蕴含了一种映射关系，我们将这个映射记为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D) ，则：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%281%29%3D2%5C%5C+2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%282%29%3D4%5C%5C+3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%283%29%3D6%5C%5C+4%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%284%29%3D8%5C%5C+5%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%285%29%3D10%5C%5C+6%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%286%29%3D12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.2%7D)

我们依然仿照置换中的记号，将上面的对应的关系写为括号的形式：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D%5Ctag%7B5.2.1.3%7D)

这样我们就可以定义 ***正有理数集上的一个拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.1.4%7D)

同理可定义 ***正有理数集上的一个收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D%5Ctag%7B5.2.1.3%7D)

下面我们依然通过几个例子说明几个问题。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 比如先将 ![[公式]](https://www.zhihu.com/equation?tex=1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=3) ，然后再将 ![[公式]](https://www.zhihu.com/equation?tex=3) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=6) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=3%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+6) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7B2%7D) ，这与直接将 ![[公式]](https://www.zhihu.com/equation?tex=1) 收缩两个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+2) 得到的结果是一样的。这说明了 ***正有理数的伸缩是可以复合的\*** 。

![img](https://pic4.zhimg.com/80/v2-067ca05ed4aa066b3b87708dc76f5bdb_1440w.jpg)

图片5：正有理数的伸缩复合示例。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 将任意一个正有理数拉长 (或收缩) 任意一个固定的 ***正有理数单位\*** ![[公式]](https://www.zhihu.com/equation?tex=j) 所得到的结果都是唯一的，这说明了正有理数拉长 (或收缩)是可逆的(即双射的)。并且具体的，先将 ![[公式]](https://www.zhihu.com/equation?tex=1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=3) ，然后再将 ![[公式]](https://www.zhihu.com/equation?tex=3) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=3) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=3%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3) ，结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=1) 。这说明了对 ***任意一个固定的正有理数单位\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7Bj%7D) ***，拉长与收缩互为逆元\*** 。且对任意一个固定整数单位 ![[公式]](https://www.zhihu.com/equation?tex=j) 的拉长与收缩的复合为 ***单位元\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B%5Cmathrm%7BId%7D_S%7D) ，表示“不做伸缩”。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 显然，正有理数的任意两个伸缩的复合还是一个正有理数的伸缩。***即定义在正有理数集上的伸缩对复合运算\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) ***是封闭的\***。
有了正有理数的伸缩作为引入之后，我们再来看看负有理数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BQ%7D_%7B%3C0%7D) 上的伸缩。
为了方便说明，我们再来定义一个“负有理数轴”。这里我们同样将负有理数轴拉长到原来的两倍(这就意味着做负有理数轴上的每一个点都被“拉长为”原来的两倍)。如果我们只观察负有理数 ![[公式]](https://www.zhihu.com/equation?tex=1) 的话，我们会发现它通过这种拉长的作用变为的原来的负有理数 ![[公式]](https://www.zhihu.com/equation?tex=-2) 。因此对于这样一个拉长的作用我们有以下对应关系：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+-1%5Cto+-2%5C%5C+-2%5Cto+-4%5C%5C+-3%5Cto+-6%5C%5C+-4%5Cto+-8%5C%5C+-5%5Cto+-10%5C%5C+-6%5Cto+-12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.6%7D)

显然，上述的对应关系也蕴含了一种映射关系，我们将这个映射记为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D) ，则：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+-1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%281%29%3D-2%5C%5C+-2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%282%29%3D-4%5C%5C+-3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%283%29%3D-6%5C%5C+-4%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%284%29%3D-8%5C%5C+-5%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%285%29%3D-10%5C%5C+-6%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%286%29%3D-12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.7%7D)

我们依然仿照置换中的记号，将上面的对应的关系写为括号的形式：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.2.1.8%7D)

这样我们就可以定义 ***负有理数集上的一个拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.2.1.8%7D)

同理可定义 ***负有理数集上的一个收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bs%5E%7B-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.1.10%7D)

并且，负有理数的伸缩与正有理数的伸缩的性质 ![[公式]](https://www.zhihu.com/equation?tex=%5Crm+i%29%5Csim%5Crm%7Biii%29%7D) 是类似的。留做练习，请大家自行说明。


![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbm%7B5.2.2%7D%7D) **非零有理数的纯镜像以及其负有理数倍伸缩**

刚才我们定义的伸缩中都有。 ![[公式]](https://www.zhihu.com/equation?tex=j%3E0) 那么现在问题来了，如果我非要定义一个***负有理数倍的伸缩\*** (即 ![[公式]](https://www.zhihu.com/equation?tex=j%3C0) ) 那怎么办呢？这里我们可以不直接对这个负有理数倍的伸缩做定义，我们先来定义一个叫 ***非零有理数的纯镜像\*** 的概念。



![img](https://pic4.zhimg.com/80/v2-eb6d68e07d1000dc45b0891724f0b53b_1440w.jpg)图片6

为了定义这个纯镜像的概念，如图片 6 所示，我们首先在正有理数轴上固定一个点 ![[公式]](https://www.zhihu.com/equation?tex=i) ，然后我们在有理数 ![[公式]](https://www.zhihu.com/equation?tex=0) 处放上一面镜子(平面镜)，则会在负有理数轴上出现一个点 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%7D%5C%2Ci) ，这个点与有理数 ![[公式]](https://www.zhihu.com/equation?tex=0) 之间的距离也为 ![[公式]](https://www.zhihu.com/equation?tex=i) ，我们就把 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Ci) 称为正有理数 ![[公式]](https://www.zhihu.com/equation?tex=i) 的 ***负镜像点\*** 。同理，对于每个负有理数 ![[公式]](https://www.zhihu.com/equation?tex=j) ，我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj) 称为负有理数 ![[公式]](https://www.zhihu.com/equation?tex=j) 的 ***正镜像点\*** 。

> 举两个例子：
> ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C5%3D-5%2C%5Cquad+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-2%29%3D2.%5Ctag%7B5.2.2.1%7D)

现在我们可以定义非零有理数的镜像的概念了。我们定义 ***正有理数的纯负镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Ci.%5Ctag%7B5.2.2.2%7D)

定义 ***负有理数的纯正镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Ci.%5Ctag%7B5.2.2.3%7D)
![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B%2B%7D%7D%5Ccirc%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B-%7D%7D%5Cright%29%3D+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B-%7D%7D%5Ccirc%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B%2B%7D%7D%5Cright%29%3D%5Cmathrm%7BId%7D_M.%5Ctag%7B5.2.2.4%7D)

有了非零有理数的纯镜像的概念之后我们就可以定义所谓的负数倍的伸缩了。定义 ***正有理数的负有理数倍拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.5%7D)

定义 ***正有理数的负有理数倍收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.6%7D)

定义 ***负有理数的负有理数倍拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.7%7D)

定义 ***负有理数的负有理数倍收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.8%7D)

> 举两个例子，比如将 ![[公式]](https://www.zhihu.com/equation?tex=2) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=-3) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D6%3D-6%5Ctag%7B5.2.2.9%7D)
> 将 ![[公式]](https://www.zhihu.com/equation?tex=-4) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=-2) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-2%29%3D2.%5Ctag%7B5.2.2.10%7D)

现在为了统一符号，我们将要舍弃我们之前的正有理数的正有理数倍伸缩与负有理数的正有理数倍伸缩的定义，并通过一个新的概念—— ***纯虚镜像\*** ，给出两者的等价定义。首先我们来定义纯虚镜像。
定义 ***正有理数的纯正虚镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Ci%3Di.%5Ctag%7B5.2.2.11%7D)

定义 ***负有理数的纯负虚镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Ci%3Di.%5Ctag%7B5.2.2.12%7D)

> 举两个例子：
> ![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C5%3D5%2C%5Cquad+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-2%29%3D-2%5Ctag%7B5.2.2.13%7D)

有了纯虚镜像的定义之后，我们就可以将非零有理数的正有理数倍伸缩进行等价地定义了。我们将 ***正有理数的正有理数倍拉长\*** 等价地定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.14%7D)

将 ***正有理数的正有理数倍收缩\*** 等价地定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.15%7D)

将 ***负有理数的正有理数倍拉长\*** 等价地定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.16%7D)

将 ***负有理数的正有理数倍收缩\*** 等价地定义为:

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.17%7D)

> 举两个例子，比如将 ![[公式]](https://www.zhihu.com/equation?tex=2) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=3) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C3%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D6%3D6.%5Ctag%7B5.2.2.18%7D)
> 将 ![[公式]](https://www.zhihu.com/equation?tex=-4) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-2%29%3D-2.%5Ctag%7B5.2.2.19%7D)

显然，通过上面所举的例子我们发现，以上八种变换都是可逆的(即双射的)。
最终我们可以将以上八种情况合并为种：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D%3A%5Cmathbb%7BQ%7D_%7B%5Cne+0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%5Cne+0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbigtriangleup%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Clozenge%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%5Cne0%7D.%5Ctag%7B5.2.2.20%7D)

下面我们要来谈一谈 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的复合问题。我们通过一个例子来说明![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的复合问题。我们先将 ![[公式]](https://www.zhihu.com/equation?tex=-1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍(负有理数的正有理数倍拉长)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29.%5Ctag%7B5.2.2.21%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28-2%5Cright%29%3D-2.)

得到结果 ![[公式]](https://www.zhihu.com/equation?tex=-2) ，然后我们再将 ![[公式]](https://www.zhihu.com/equation?tex=-2) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=-3) 倍(负有理数的负有理数倍拉长)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C3%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-6%29%3D6.%5Ctag%7B5.2.2.22%7D)

这就说明了负有理数的负有理数倍拉长是可以复合负有理数的正有理数倍拉长的，更一般的，负有理数的负有理数倍伸缩可以复合负有理数的正有理数倍伸缩。
但是比如第一次做的伸缩是负有理数的正有理数倍伸缩，那么根据定义，此时的结果是负有理数，所以就 ***不能对此结果再做\*** 正有理数的伸缩操作了。这就说明了：***正有理数的伸缩不能与负有理数的正有理数倍伸缩复合\***。但是正有理数的伸缩可以与负有理数的负有理数倍伸缩复合，这是因为负有理数的负有理数倍伸缩的结果是正有理数。
经过以上的分析我们发现：![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的复合可分为 ***有效复合\*** 与 ***无效复合\*** 两种情况。所谓有效复合，指的就是例如负有理数的负有理数倍伸缩与负有理数的正有理数倍伸缩的复合，且：

![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%5Ccirc%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%5Cright%29%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D.%5Ctag%7B5.2.2.23%7D)

而所谓无效复合，指的就是例如正有理数的正有理数倍伸缩不能与负有理数的正有理数倍伸缩复合，并且对于无效复合，我们定义复合的结果为第一次伸缩变换的结果，即例如：

![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%5Ccirc%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%5Cright%29%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.24%7D)

定义有效复合与无效复合的原因是为了保证八种 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的两两复合对复合运算都是封闭的。因为从有效复合与无效复合的定义来看，两者的结果都仍是八种 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 中的某一种。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D)
> 由于八种 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 都是双射的，所以他们的到达域等于值域，于是我们便可以将第一次伸缩变换的到达域下一次伸缩变换的定义域做一下比较，当两者相同时复合便是有效的，否则是无效的。


并且我们有：
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 有效复合的有效复合是有效的；
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 有效复合的无效复合是无效的；
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 无效复合的有效复合是有效的；
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D) 无效复合的无效复合是无效的。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D)
> 在原文中我对 ![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的两两复合做了 ***非常详细\*** 的讨论，***推荐大家去看一下原文或者视频\*** 。

有关逆元，我们也通过一个例子来说明。
我们先将 ![[公式]](https://www.zhihu.com/equation?tex=-1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍(负有理数的正有理数倍拉长)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29.%5Ctag%7B5.2.2.25%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28-2%5Cright%29%3D-2.)

得到结果 ![[公式]](https://www.zhihu.com/equation?tex=-2) ，然后我们再将 ![[公式]](https://www.zhihu.com/equation?tex=-2) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍(负有理数的正有理数倍收缩)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-1%29%3D-1.%5Ctag%7B5.2.2.26%7D)

结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=-1) ，这就说明了对于同一伸缩倍数 ![[公式]](https://www.zhihu.com/equation?tex=2) 而言，负有理数的正有理数倍拉长与负有理数的正有理数倍拉长互为逆元，两者复合的结果是单元元 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BId%7D_%7BB%7D) ，表示“不进行伸缩”。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D)
> 实际上，对于八种 ![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D++) ： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.27%7D)
> 它们的逆元都是唯一的，并且(从左到右)分别为： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.28%7D)

对于非零实数而言，我们也可以定义它的伸缩为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D%3A%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cto%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacktriangle%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacklozenge%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D_%7B%5Cne0%7D.%5Ctag%7B5.2.2.29%7D)

其中 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacklozenge%7D) 表示非零实数的伸缩运算， ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacktriangle%7D) 表示非零实数的镜像(包括纯镜像和纯虚镜像)运算。与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 一样，其也有八种情况：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.30%7D)

并且上述的八种映射都是双射的，也就是说它都是具有逆的，它们的逆分别是(从左到右)：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.31%7D)

并且这八种情况的复合也分有效复合与无效复合两种。且任意两个 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 对一般的复合运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 也是封闭的，且无效复合的无效复合还是无效的，无效复合的有效复合是有效的，有效复合的无效复合是无效的，有效复合的有效复合是有效的。***总之，\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) ***与\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) ***的运作方式以及基本性质都是十分相似的\***。


![[公式]](https://www.zhihu.com/equation?tex=%5Clarge+%5Cbm%7B5.3%7D) **复数的滑动**

![img](https://pic4.zhimg.com/80/v2-bd006cd19364e9fa0cedac4a5354feff_1440w.jpg)

图片7

如图 7 中的滑动是将原始的复平面沿复数 ![[公式]](https://www.zhihu.com/equation?tex=5%2B3%5Ccdot+i) 进行的滑动。它可以被视为在实轴上的 ![[公式]](https://www.zhihu.com/equation?tex=5) 个单位的向右滑动(对应了实数的滑动)和虚轴上的 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位的向上滑动的复合，如图 8 所示。

![img](https://pic1.zhimg.com/80/v2-e4ac67daf616d8603873e2dd7eafc5b8_1440w.jpg)

图片8

图片 8 中的 ![[公式]](https://www.zhihu.com/equation?tex=%5Cheartsuit) 为一种运算，后面我们会看到它的定义。
这样的分解可以让我们分别得到实轴与虚轴上的两个对应关系。首先是实轴上的对应关系：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Cto+2%5C%5C+-2%5Cto+3%5C%5C+-1%5Cto+4%5C%5C+0%5Cto+5%5C%5C+1%5Cto+6%5C%5C+2%5Cto+7%5C%5C+3%5Cto+8%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.1%7D)

利用之前定义的实数的向右滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bu%7D) 我们可以得到：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-3%29%3D2%5C%5C+-2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-2%29%3D3%5C%5C+-1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-1%29%3D4%5C%5C+0%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%280%29%3D5%5C%5C+1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%281%29%3D6%5C%5C+2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%282%29%3D7%5C%5C+3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%283%29%3D8%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.2%7D)

然后我们就可以将实轴上的这种对应关系写为括号的形式了：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%3D+%5Cbegin%7Bpmatrix%7D+%5Cldots+%26+-3+%26+-2+%26+-1+%26+0+%26+1+%26+2+%26+3+%26+%5Cldots+%5C%5C+%5Cldots+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-3%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-2%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-1%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%280%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%283%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.3.3%7D)

下面我们再来看虚轴上的对应关系：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Ccdot+i%5Cto+0%5C%5C+-2%5Ccdot+i%5Cto+1%5Ccdot+i%5C%5C+-1%5Ccdot+i%5Cto+2%5Ccdot+i%5C%5C+0%5Cto+3%5Ccdot+i%5C%5C+1%5Ccdot+i%5Cto+4%5Ccdot+i%5C%5C+2%5Ccdot+i%5Cto+5%5Ccdot+i%5C%5C+3%5Ccdot+i%5Cto+6%5Ccdot+i%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.4%7D)

我们发现，如果我们只考察虚部的话，那么这种对应关系也可以被视为是实轴上的滑动。我们将这种 ***只看虚部的向上滑动\*** 定义为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cuparrow) 。于是我们有：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Cto+%5Cmu%5Cuparrow%28-3%29%3D0%5C%5C+-2%5Cto+%5Cmu%5Cuparrow%28-2%29%3D1%5C%5C+-1%5Cto+%5Cmu%5Cuparrow%28-1%29%3D2%5C%5C+0%5Cto+%5Cmu%5Cuparrow%280%29%3D3%5C%5C+1%5Cto+%5Cmu%5Cuparrow%281%29%3D4%5C%5C+2%5Cto+%5Cmu%5Cuparrow%282%29%3D5%5C%5C+3%5Cto+%5Cmu%5Cuparrow%283%29%3D6%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.5%7D)

写为括号的形式为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cuparrow%3D+%5Cbegin%7Bpmatrix%7D+%5Cldots+%26+-3+%26+-2+%26+-1+%26+0+%26+1+%26+2+%26+3+%26+%5Cldots+%5C%5C+%5Cldots+%26+%5Cmu%5Cuparrow%28-3%29+%26+%5Cmu%5Cuparrow%28-2%29+%26+%5Cmu%5Cuparrow%28-1%29+%26+%5Cmu%5Cuparrow%280%29+%26+%5Cmu%5Cuparrow%281%29+%26+%5Cmu%5Cuparrow%282%29+%26+%5Cmu%5Cuparrow%283%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.3.6%7D)

这样我们就可以定义复数集上的一个 ***右上滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29.%5Ctag%7B5.3.7%7D)

其中运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Cheartsuit) ***表示先沿实轴做滑动\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7Bu%7D) ***，然后在沿虚轴做滑动\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cupdownarrow) 。
我们刚刚定义了复平面的右上滑动，同理我们可以借助 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7Bu%7D) 和 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cupdownarrow) 具体的定义 ![[公式]](https://www.zhihu.com/equation?tex=8) 个基本方向上的滑动。但是在此之前，我们还需要先对 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cupdownarrow) 做一个明确的定义。定义 ***只考虑虚部的下滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cuparrow%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+k%5Cmapsto+k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C+l%2C%5C%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.8%7D)

定义 ***只考虑虚部的上滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cdownarrow%3A%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+k%5Cmapsto+k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2C+l%2C%5C%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.9%7D)

接下来我们就可以具体地定义复平面的 ![[公式]](https://www.zhihu.com/equation?tex=8) 个基本方向上的滑动了。定义 ***复数集上的右上滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2Cl%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.10%7D)

定义 ***复数集上的右下滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Csearrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cdownarrow%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cdownarrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2Cl%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.11%7D)

定义 ***复数集上的左上滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnwarrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C+l%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.12%7D)

定义 ***复数集上的左下滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cswarrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%2C%5Cmu%5Cdownarrow%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cdownarrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2Cj%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2Cl%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.13%7D)

定义 ***复数集上的竖直上滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cuparrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cmathrm%7BId%7D_U%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto%5Cleft%28%5Cmathrm%7BId%7D_U%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3Dk%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2Cl%2C%5Cquad+l%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.14%7D)

定义 ***复数集上的竖直下滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cdownarrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cmathrm%7BId%7D_U%2C%5Cmu%5Cdownarrow%5Cright%29%5Cmapsto%5Cleft%28%5Cmathrm%7BId%7D_U%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cdownarrow%5Cright%29%3Dk%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2Cl%2C%5Cquad+l%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.15%7D)

定义 ***复数集上的水平左滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bw%7D%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%2C%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%3Di%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5Cquad+j%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.16%7D)

定义 ***复数集上的水平右滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bw%7D%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%3Di%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5Cquad+j%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.17%7D)

下面我们通过例子来说明几个问题。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 我们对复数 ![[公式]](https://www.zhihu.com/equation?tex=0%2B0%5Ccdot+i) 先做右上滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+1+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C2%5Cright%29) 得到结果 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，再做右上滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+2+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C1%5Cright%29) 得到结果 ![[公式]](https://www.zhihu.com/equation?tex=3%2B3%5Ccdot+i) ，那么最终的效果与直接做右上滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+3+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C3%5Cright%29) 滑动的效果是一样的。这就说明了 ***复数的滑动是可以复合的\*** 。

![img](https://pic2.zhimg.com/80/v2-fd886c9a6886f74148e8589151b9d29d_1440w.jpg)图片9：复数滑动的复合。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 我们对复数 ![[公式]](https://www.zhihu.com/equation?tex=0%2B0%5Ccdot+i) 先做右上滑动![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+1+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C2%5Cright%29) 得到结果 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，再做左下滑动![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+1+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2C2%5Cright%29) ，结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=0%2B0%5Ccdot+i) 。这就说明了***复数的滑动是可逆的\*** 。具体而言，之前定义的复平面在八个基本方向上的滑动：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%2C%5C%2Cw%5Csearrow%2C%5C%2Cw%5Cnwarrow%2C%5C%2Cw%5Cswarrow%2C%5C%2Cw%5Cuparrow%2C%5C%2Cw%5Cdownarrow%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7Bw%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7Bw%7D%5Ctag%7B5.3.18%7D)

的逆分别是(从左至右)分别是：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cswarrow%2C%5C%2Cw%5Cnwarrow%2C%5C%2Cw%5Csearrow%2C%5C%2Cw%5Cnearrow%2C%5C%2Cw%5Cdownarrow%2C%5C%2Cw%5Cuparrow%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7Bw%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7Bw%7D.%5Ctag%7B5.3.19%7D)
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 复数集上的任意两个滑动的复合还是还是一个复数集上的滑动。即定义在***复数集上的滑动对复合运算\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) ***是封闭的\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge+%5Cbm%7B5.4%7D) **非零复数的旋转伸缩**

现在终于来到了我们的最后一个部分了。非零复数的伸缩分为两种，一种是非零复数的非零实数倍的伸缩，这种伸缩我们也称为 ***纯伸缩\*** 。另外一种是非零复数的非零复数倍的伸缩，这种伸缩我们称为 ***带旋转的伸缩\*** 。对于带旋转的伸缩，我们还需定义的是 ***纯旋转\*** 的概念。首先我们先来看非零复数的纯伸缩。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.1%7D) **非零复数的纯伸缩**

> **这是原文中最为复杂的一部分，所以这里我打算换一种简单的定义方式。**

![img](https://pic1.zhimg.com/80/v2-f0769f2715e7f555f1cce5dfa70e10cc_1440w.jpg)图片10

如图片 10 所示，我们将复平面拉长为原来的两倍，这相当于我们同时将实轴与虚轴拉长到原来的两倍。而非零实数的正实数倍拉长我们之前已经定义过了，并且，对虚轴如果我们只考虑它的虚部的话，那么这里虚轴的拉长我们也可以视为非零实数的正实数倍拉长。这或许为我们定义非零复数的纯伸缩提供了一种思路。所以我们不妨顺着这个思路继续深入。我们首先要做的就是仿照非零实数的正实数倍拉长，定义一个对应的 ***只考虑虚轴的拉长 。\***

![[公式]](https://www.zhihu.com/equation?tex=r%5Cupdownarrow%3A%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cto%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%2C%5Cquad+i%5Cmapsto+%7B%5Cblacktriangle%7D%5Cupdownarrow%5Cleft%28i%5C%2C%7B%5Cblacklozenge%7D%5Cupdownarrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%7D%5Cuparrow%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D_%7B%5Cne0%7D%5Ctag%7B5.4.1.1%7D.)

这里将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 中的左右箭头 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleftrightarrow) 换成了上下箭头 ![[公式]](https://www.zhihu.com/equation?tex=%5Cupdownarrow) ，表示的是 ***竖直方向上的伸缩\*** 。显然， ![[公式]](https://www.zhihu.com/equation?tex=r) 也具有 ![[公式]](https://www.zhihu.com/equation?tex=8) 种子情况。

其中 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 必须与 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cupdownarrow) ***必须同为拉长或者同为收缩，并且同为拉长时，拉长的倍数必须相等；同为收缩时，收缩的倍数必须相等\*** 。

并且我们知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 的定义域与值域也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%5Cne+0%7D) 与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%5Cne+0%7D) 。这样我们就可以先来定义实部和虚部都不等于零的复数的伸缩了：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%2A%5Cupdownarrow%7D%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cupdownarrow.%5Ctag%7B5.4.1.2%7D)

其中运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Cclubsuit) 表示 ***实轴与虚轴同时做相同倍数的拉长或者相同倍数的收缩\*** 。另外我们知道，非零复数还包括在实轴上的复数和在虚轴上的复数。那么我们进一步定义在实轴上的复数的伸缩为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%5C%2C%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D.%5Ctag%7B5.4.1.3%7D)

而在虚轴上的复数的伸缩我们定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D%5C%2C%3A%3D+r%5Cupdownarrow.%5Ctag%7B5.4.1.4%7D)

式 ![[公式]](https://www.zhihu.com/equation?tex=%285.4.1.3%29%2C%5C%2C%285.4.1.4%29) 并不意味着当其中一个轴做伸缩时另外一个轴就不做相同的伸缩了，所以这里我们可以理解为当实轴做伸缩 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleftrightarrow) 时，虚轴在 ***被动地做与实轴一样的伸缩\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D) ；当虚轴做伸缩 ![[公式]](https://www.zhihu.com/equation?tex=%5Cupdownarrow) 时，实轴在 ***被动地做与虚轴一样的伸缩\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D) 。

现在我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%2A%5Cupdownarrow%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D) 合并到一起，并统一定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cupdownarrow.%5Ctag%7B5.4.1.5%7D+%5Cend%7Barray%7D)

我们根据非零复数所处的位置便可知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%2A%5Cupdownarrow%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D) 中的哪一个。具体的我们可以定义 ***非零复数的纯拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Crightarrow%7D%7B%5Cdelta%5Cuparrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cuparrow.%5Ctag%7B5.4.1.6%7D+%5Cend%7Barray%7D)

定义***非零复数的纯收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdelta%5Cdownarrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cdownarrow.%5Ctag%7B5.4.1.7%7D+%5Cend%7Barray%7D)

最后我们来谈一谈 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 复合的问题。对于 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D) 或者 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D) 的复合情况这里就不再说明了，因为这两种情况下的复合与非零实数伸缩的复合原理是一样的。不过可以从这两种特殊情况中看到的是： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 复合也会涉及到有效复合与无效复合这两种不同的情况。但是， ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 的复合是否有效也完全取决于 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) (或 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cupdownarrow) )之间的复合是否有效。

> 举一个实际的例子。比如我想将复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) 做 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%29) 倍的拉长，这就意味着我们要同时对实轴和虚轴做![[公式]](https://www.zhihu.com/equation?tex=%28-2%29)倍的拉长： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+2%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D2%3D-2.%5Ctag%7B5.4.1.8%7D) ![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B%2B%5Cto-%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cdownarrow4%3D-4.%5Ctag%7B5.4.1.9%7D)
> 这样得到的结果是 ![[公式]](https://www.zhihu.com/equation?tex=-2-4%5Ccdot+i) 。因为此时 ![[公式]](https://www.zhihu.com/equation?tex=i%2C%5C%2Cj) 都是负实数(即 ![[公式]](https://www.zhihu.com/equation?tex=%28i%2Cj%29) 为一负有序实数对)，所以我们就不能进一步对 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%2C-4%29) 做正实数的伸缩的了(即正有序实数对的负伸缩不能复合其自身，即这种复合就是无效的)。但是我们可以对负有序实数对 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%2C-4%29) 做负有序实数对的伸缩，比如再对它做一个 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%29) 倍的拉长： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cleft%28-2%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E-%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cleft%28-2%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E-%7D%5C%2C+2%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%28-4%29%3D4.%5Ctag%7B5.4.1.10%7D) ![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B-%5Cto%2B%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5Cleft%28-4%5C%2C%7B%5Cblacklozenge%5E-%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5Cleft%28-4%5C%2C%7B%5Cblacklozenge%5E-%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%5Cblacktriangle%5E%7B-%7D%5Cuparrow%28-8%29%3D8.%5Ctag%7B5.4.1.11%7D)
> 这样最终的结果是 ![[公式]](https://www.zhihu.com/equation?tex=4%2B8%5Ccdot+i) 。

对于无效的复合，我们依然将其结果定义为复合之前的变换。这样就保证了 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 对复合的封闭性。并且我们断言： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 的所有情况都是可逆的。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.2%7D) **非零复数的纯旋转**

非零复数的纯旋转的定义可以说是非常直观的。首先是 ***非零复数的纯逆时针旋转\*** ：

![[公式]](https://www.zhihu.com/equation?tex=p_%7B%5Ccirclearrowleft%7D%3A%5Cmathbb%7BR%7D_%7B%3E0%7D%5Ctimes%5B0%2C2%5Cpi%29%5Cto%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%28r%2C%5Cphi%29%5Cmapsto+%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta%2C%5Cquad%5Ctheta%5Cin%5B0%2C2%5Cpi%29.%5Ctag%7B5.4.2.1%7D)

然后是 ***非零复数的纯顺时针旋转\*** ：

![[公式]](https://www.zhihu.com/equation?tex=p_%7B%5Ccirclearrowright%7D%3A%5Cmathbb%7BR%7D_%7B%3E0%7D%5Ctimes%5B0%2C2%5Cpi%29%5Cto%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%28r%2C%5Cphi%29%5Cmapsto+%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowright%5Ctheta%2C%5Cquad%5Ctheta%5Cin%5B0%2C2%5Cpi%29.%5Ctag%7B5.4.2.2%7D)

> 举个实际的例子：
> ![[公式]](https://www.zhihu.com/equation?tex=%282%2C60%5E%7B%5Ccirc%7D%29%5Cmapsto+%5Cleft%282%5Cangle60%5E%7B%5Ccirc%7D%5Cright%29%5Ccirclearrowleft15%5E%7B%5Ccirc%7D%5Ctag%7B5.4.2.3%7D%3D2%5Cangle75%5E%7B%5Ccirc%7D.)
> 表示的就是将长度为 ![[公式]](https://www.zhihu.com/equation?tex=2) 的，辐角为 ![[公式]](https://www.zhihu.com/equation?tex=60%5E%7B%5Ccirc%7D) 的复数逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=15%5E%7B%5Ccirc%7D) 。

并且我们容易验证以下几点：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 定义在复数集上的纯旋转是可以复合的。比如先将复平面逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=45%5E%7B%5Ccirc%7D) (即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft+45%5E%7B%5Ccirc%7D) )，然后再逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=45%5E%7B%5Ccirc%7D) (即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft+45%5E%7B%5Ccirc%7D) )，则最后的效果与直接逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) (即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft+90%5E%7B%5Ccirc%7D) )的效果是一致的，如图11所示：

![img](https://pic4.zhimg.com/80/v2-7666bccb59210c0d69eab85dbad8eb1b_1440w.jpg)图片11

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 定义在复数集上的纯旋转是双射的(即可逆的)。因为我们可以将任意一个非零的复数 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cangle%5Cphi) 通过逆时针(或顺时针)旋转角度 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta) 都可对应于复平面上的一个复数。而且反过来，将复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta) (或 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta) ) 顺时针(或逆时针)旋转之后都可以唯一对应到一个非零的复数 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cangle%5Cphi) 。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 定义在复数集上的任意两个纯旋转的复合还是一个复数集上的纯旋转。即定义在复数集上的纯旋转对复合运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 是封闭的。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.3%7D) **非零复数的带旋转的伸缩**

在定义非零复数的带旋转的伸缩之前我们首先要来思考一个问题：我们是否真的仅仅将非零复数的纯伸缩与纯旋转进行复合就可以了？答案是否定的。但这是为什么呢？如果不将两者直接复合那应该如何定义非零复数的的带旋转的伸缩呢？这里我们不妨先回忆我们非零复数的纯伸缩的定义。在我们讨论非零复数的纯伸缩的时候我们发现，对于非零复数的正实数伸缩，伸缩的结果总是没有镜像效果的(我们可以将这种伸缩称为非零复数的 ***保向伸缩\*** )，即非零复数的正实数伸缩总是将一个复数直接进行伸缩而不用考虑镜像(这一点的根源是非零实数的正实数伸缩)。而非零复数的负实数伸缩总是会产生镜像作用的(即复数在被拉长的同时会通过复平面的原点中心对称，这一点的根源是非零实数的负实数伸缩)，而这种镜像作用恰好对应了非零复数的纯 ![[公式]](https://www.zhihu.com/equation?tex=180%5E%7B%5Ccirc%7D) 旋转。所以我们如果直接将非零复数的纯伸缩与非零复数的纯旋转复合的话会很混乱。所以取而代之的是，我们将 ***非零复数的正实数伸缩与非零复数的纯旋转进行复合\*** ，进而来定义非零复数的带旋转的伸缩。

这里我们首先要给出具体的非零复数的正实数伸缩的定义。我们将要分八种情况进行说明。我们将“挖掉原点的”复平面拆解一下，拆解为一下八个部分：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) ***实轴正半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) ***实轴负半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) ***虚轴正半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D) ***虚轴负半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D) ***实部与虚部均大于零的部分\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvi%29.%7D) ***实部小于零，但是虚部大于零的部分\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvii%29.%7D) ***实部与虚部均小于零的部分\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bviii%29.%7D) ***实部大于零，但是虚部小于零的部分\*** 。

之后我将 ***使用相应的编号来代表这八个部分\*** 。首先要明确的是 ***任意一个非零复数一定处于这八个部分中的一个，且同时只能属于唯一的一个\*** 。所以我们定义非零复数的正实数伸缩可以通过对这八种情况分别进行定义。下面我们就来逐一的定义一下：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28%2B%2C0%29%5Cto%28%2B%2C0%29%7D%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%5C%2C%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D.%5Ctag%7B5.4.3.1%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28-%2C0%29%5Cto%28-%2C0%29%7D%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%5C%2C%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.4.3.2%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5E%7B%280%2C%2B%29%5Cto%280%2C%2B%29%7D%5Cupdownarrow%7D%5C%2C%3A%3D+r%5E%7B%2B%5Cto%2B%7D%5Cupdownarrow.%5Ctag%7B5.4.3.3%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5E%7B%280%2C-%29%5Cto%280%2C-%29%7D%5Cupdownarrow%7D%5C%2C%3A%3D+r%5E%7B-%5Cto-%7D%5Cupdownarrow.%5Ctag%7B5.4.3.4%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28%2B%2C%2B%29%5Cto%28%2B%2C%2B%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B%2B%5Cto%2B%7D%5Cupdownarrow.%5Ctag%7B5.4.3.5%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvi%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28-%2C%2B%29%5Cto%28-%2C%2B%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B%2B%5Cto%2B%7D%5Cupdownarrow.%5Ctag%7B5.4.3.6%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28-%2C-%29%5Cto%28-%2C-%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B-%5Cto-%7D%5Cupdownarrow.%5Ctag%7B5.4.3.7%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bviii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28%2B%2C-%29%5Cto%28%2B%2C-%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B%2B%5Cto-%7D%5Cupdownarrow.%5Ctag%7B5.4.3.8%7D)

我们将以上八种情况合并为映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D) 。根据复数所处的位置我们可以明确 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D) 应为以上八种情况中的哪一种。

现在非零复数的正实数倍拉长 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D) 已经定义好了，下面我们就可以来定义非零复数带旋转的伸缩了。如之前所述，非零复数带旋转的伸缩可由为零复数的正实数倍拉长与非零复数的纯旋转复合得到(我们下面 ***只讨论逆时针旋转\*** ，顺时针旋转同理)：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi%3A%5Cmathbb%7BR%7D_%7B%5Cne0%7D%5Ctimes%5B0%2C2%5Cpi%29%5Cto%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%28r%2C%5Cphi%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D%5C%2C%5Ccirc+%5Cleft%28%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta%5Cright%29%5Cright%29.%5Ctag%7B5.4.3.9%7D)

> 举一个具体的例子： 先将 ![[公式]](https://www.zhihu.com/equation?tex=%5Csqrt%7B3%7D%2Bi) 逆时针 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta%3D30%5E%7B%5Ccirc%7D) 的旋转得到： ![[公式]](https://www.zhihu.com/equation?tex=%282%2C30%5E%7B%5Ccirc%7D%29%5Cmapsto%5Cleft%282%5Cangle30%5E%7B%5Ccirc%7D%5Cright%29%5Ccirclearrowleft30%5E%7B%5Ccirc%7D%3D2%5Cangle60%5E%7B%5Ccirc%7D.%5Ctag%7B5.4.3.10%7D)
> 变成复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B%5Csqrt%7B3%7D%5Ccdot+i) 之后再拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%7D%5C%2C+2%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D2%3D2.%5Ctag%7B5.4.3.11%7D) ![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B%2B%5Cto%2B%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow%5Cleft%28%5Csqrt%7B3%7D%5C%2C%7B%5Cblacklozenge%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow%5C%2C2%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow%5Cleft%28%5Csqrt%7B3%7D%5C%2C%7B%5Cblacklozenge%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow2%5Csqrt+3%3D2%5Csqrt+3.%5Ctag%7B5.4.3.12%7D)
> 最后得到结果 ![[公式]](https://www.zhihu.com/equation?tex=2%2B2%5Ccdot%5Csqrt%7B3%7D%5Ccdot+i) 。

在之前的讨论中，我们知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D%5Cright%29) 与 ![[公式]](https://www.zhihu.com/equation?tex=p_%7B%5Ccirclearrowleft%7D) 都是双射的，则他们的复合 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 也是双射的。于是，当两个 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 之间可以复合时，复合的结果自然也是双射的。所以我们需要重点讨论的是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 的可复合性。现在设：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_%7Ba%7D%3A%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Ca%7D%5Cright%29%2C%5Cquad+%5Cpsi_%7Bb%7D%3A%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D%5Cright%29.%5Ctag%7B5.4.3.13%7D)

我们可以将复合 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_a%5Ccirc%5Cpsi_b) 写为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_a%5Ccirc%5Cpsi_b%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc%5C%2C+p_%7B%5Ccirclearrowleft%2Ca%7D%5Cright%29%5Ccirc%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D%5Cright%29.%5Ctag%7B5.4.3.14%7D)

复合的有效性取决于 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D) 与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D) 复合的合法性。为了保证两个非零复数的正实数倍拉长复合的合法性，我们***必须要留意的是做完\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D) ***之后非零复数所处的位置\***，***然后再根据位置从前述的八种情况中选出对应的一种\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D) ***进行复合\*** 。在 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D) 无效时我们定义：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_a%5Ccirc%5Cpsi_b%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc%5C%2C+p_%7B%5Ccirclearrowleft%2Ca%7D%5Cright%29%5Ccirc%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D%5Cright%29%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D.%5Ctag%7B5.4.3.15%7D)

即保持复合之前的旋转伸缩，这一定义与非零实数的非零实数倍拉长的无效复合的定义是类似的。并且由合法复合与非合法复合的定义我们保证了 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 对复合运算是封闭的。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.4%7D) **站在群的角度上来理解代数运算**

在这之前我们已经做足了铺垫，现在我们可以站在群的角度上来理解代数运算了。整数和有理数我们就不再讨论了。我们只讨论实数与复数。首先我们先给出结论：

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7B%5Ccolor%7Bred%7D%7BTheorem%5Cquad+5.4.1%3A%7D%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D+) 实数的滑动对应于实数的加法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D+) 非零实数的非零实数倍伸缩对应于非零实数的乘法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D+) 复数的滑动对应于复数的加法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D+) 非零复数的纯伸缩对应于非零复数与非零实数的乘法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D+) 非零复数的旋转伸缩对应于非零复数与非零复数的乘法。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bred%7D%7B%5Clarge%5Cblacksquare%7D)

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B%5Crm%7BRemark%3A%7D%7D%7D) 这里我们没有为复数的纯旋转找到对应关系。这一关系我们将在下一节中补上。

下面我就仅对 ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%7D%29%5Csim%5Crm%7Bv%7D%29) 各举一个例子。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7B%5Ccolor%7BGreen%7D%7BExample%5Cquad+5.4.1%3A%7D%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 对于复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，给它加上另一个复数 ![[公式]](https://www.zhihu.com/equation?tex=3%2B4%5Ccdot+i) 得到 ![[公式]](https://www.zhihu.com/equation?tex=4%2B6%5Ccdot+i) 。这相当于对复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) 做了一个右上滑动，即：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%3A%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+3+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%282%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C4%5Cright%29.%5Ctag%7B5.4.4.1%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%7D%29.) 对于复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，给它乘上另一个负实数 ![[公式]](https://www.zhihu.com/equation?tex=-3) 得到 ![[公式]](https://www.zhihu.com/equation?tex=-3-6%5Ccdot+i) 。这相当于对复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) 做了一个纯负实数倍的拉长，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%2B%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E-%7D%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%2B%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+3%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%2B%7D3%3D-3.%5Ctag%7B5.4.4.2%7D)

![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B%2B%5Cto-%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%2B%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E-%7D%5Cuparrow%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+3%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cdownarrow6%3D-6.%5Ctag%7B5.4.4.3%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D) 对于复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Csqrt%7B3%7D%2Bi) ，给它乘上另一个复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B%5Csqrt%7B3%7D%5Ccdot+i) 得到 ![[公式]](https://www.zhihu.com/equation?tex=4%5Ccdot+i) 。这相对于先对复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Csqrt%7B3%7D%2Bi) 做了一个 ![[公式]](https://www.zhihu.com/equation?tex=60%5E%5Ccirc) 的纯旋转：

![[公式]](https://www.zhihu.com/equation?tex=%282%2C30%5E%7B%5Ccirc%7D%29%5Cmapsto%5Cleft%282%5Cangle30%5E%7B%5Ccirc%7D%5Cright%29%5Ccirclearrowleft60%5E%7B%5Ccirc%7D%3D2%5Cangle90%5E%7B%5Ccirc%7D.%5Ctag%7B5.4.4.4%7D)

变成复数 ![[公式]](https://www.zhihu.com/equation?tex=2%5Ccdot+i) 之后再拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Crightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cuparrow%7D%3D%5Cunderset%7B%5Crightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5E%7B%280%2C%2B%29%5Cto%280%2C%2B%29%7D%5Cuparrow%7D%5C%5C+%7Br%5E%7B%2B%5Cto-%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow%5Cleft%282+%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow%5C%2C2%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow4%3D4.%5Ctag%7B5.4.4.5%7D+%5Cend%7Barray%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bgreen%7D%7B%5Clarge%5Cblacksquare%7D)

最后总结一下，如果在群的角度上理解代数运算的话我们实际上是将数字看成了一种作用，通过这种作用可以将原来的数字变成新的数字，所以说代数运算只不过是群作用的一种实际体现。

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge%5Cbm%7B6.%7D) 再看群同态与上帝公式和群论的关系

在之前我们看到，以 ![[公式]](https://www.zhihu.com/equation?tex=e) 为底的指数函数的运算律是群同态的一种体现。其实不止以 ![[公式]](https://www.zhihu.com/equation?tex=e) 为底的指数函数，以其他大于零的实数 ![[公式]](https://www.zhihu.com/equation?tex=x) 作为底数的指数函数也是群同态的一种体现。因为我们也有：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Ba%2Bb%7D%3Dx%5Ea%5Ccdot+x%5Eb.%5Ctag%7B6.1%7D)

现在我们假设 ![[公式]](https://www.zhihu.com/equation?tex=a%2C%5C%2Cb%5Cin%5Cmathbb%7BR%7D) ，由于之前我们将实数的加法解释为了实数的滑动，将非零实数的乘法解释为了非零实数的伸缩，并且底数大于零的实指数函数的值域是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%3E0%7D) 。于是现在我们可以这样去理解 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Ba%2Bb%7D%3Dx%5Ea%5Ccdot+x%5Eb) ：***我们将实数的滑动\*** ![[公式]](https://www.zhihu.com/equation?tex=%7Ba%2Bb%7D) ***作为输入，得到的是正实数的伸缩\*** 。这为我们提供了指数函数运算律的另一种理解方式。

那么基于这种理解方式，我们自然能想到是的：***以其他大于零的实数\*** ![[公式]](https://www.zhihu.com/equation?tex=x) ***作为底数的指数函数，当输入为复数的滑动时，输出的应是非零复数的旋转伸缩\*** 。那么这个结论是否正确呢？下面我们就来简单讨论一下。

不妨设：

![[公式]](https://www.zhihu.com/equation?tex=a%3A%3D%5Calpha%2B%5Cbeta%5Ccdot+i%2C%5C%2C%5C%2Cb%3A%3D%5Cgamma%2B%5Cdelta%5Ccdot+i%2C%5Cquad+%5Calpha%2C%5C%2C%5Cbeta%2C%5C%2C%5Cgamma%2C%5C%2C%5Cdelta%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B6.2%7D)

则：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Ba%2Bb%7D%3Dx%5E%7B%28%5Calpha%2B%5Cbeta%5Ccdot+i%29%2B%28%5Cgamma%2B%5Cdelta%5Ccdot+i%29%7D%3Dx%5E%7B%28%5Calpha%2B%5Cgamma%29%2Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3Dx%5E%7B%28%5Calpha%2B%5Cgamma%29%7D%5Ccdot+x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D.%5Ctag%7B6.3%7D)

由于 ![[公式]](https://www.zhihu.com/equation?tex=x%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5C%2C%5Calpha%2C%5C%2C%5Cgamma%5Cin%5Cmathbb%7BR%7D) ，所以 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7B%28%5Calpha%2B%5Cgamma%29%7D%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D) ，进而 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7B%28%5Calpha%2B%5Cgamma%29%7D) 起到的是纯伸缩的作用。那么现在的问题是为什么 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D) 起到的是纯旋转的作用呢？一种比较简单的解释方式是：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3D%5Cexp%5Cleft%28%5Cln%5Cleft%28x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cright%29%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cright%29.%5Ctag%7B6.4%7D)

由于 ![[公式]](https://www.zhihu.com/equation?tex=x%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5C%2C%5Cbeta%2C%5C%2C%5Cdelta%5Cin%5Cmathbb%7BR%7D) ，所以 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D) ，进而 ![[公式]](https://www.zhihu.com/equation?tex=+%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cin%5Cmathbb%7BR%7D) 。现在我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29) 定义为 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta) ，则：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cright%29%3D%5Cexp%5Cleft%28i%5Ccdot%5Ctheta%5Cright%29.%5Ctag%7B6.5%7D)

这就说明了 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D) 总是一个长度为 ![[公式]](https://www.zhihu.com/equation?tex=1) 的复数。所以它起到是复平面上的纯旋转作用。并且我们看到，以***任意一个大于零的实数\*** ![[公式]](https://www.zhihu.com/equation?tex=x) ***为底的指数函数将虚轴映射为复平面上的单位圆\*** 。也就是说给定一个非零复数，给它乘以一个 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28i%5Ccdot%5Ctheta%29) 相当于使该复数纯旋转了角度 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta) 。于是我们的又一个结论是(补 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B%5Crm%7BTheorem%5Cquad+5.4.1%7D%7D) 中的复数的纯旋转找到对应关系)：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvi%29.%7D) 非零复数的纯旋转对应于非零复数与复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28i%5Ccdot%5Ctheta%29) 的乘法。

现在让我们再看到 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D) ，现在我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbeta%2B%5Cdelta) 定义为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi%5Cin%5Cmathbb%7BR%7D) 。则：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3Dx%5E%7Bi%5Ccdot%5Cxi%7D%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28x%5E%7B%5Cxi%7D%5Cright%29%5Cright%29.%5Ctag%7B6.6%7D)

就是说我们对以任意一个大于零的实数 ![[公式]](https://www.zhihu.com/equation?tex=x) 为底的指数函数的指数上放置一个纯虚数 ![[公式]](https://www.zhihu.com/equation?tex=i%5Ccdot%5Cxi) ，相当于在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动了角度 ![[公式]](https://www.zhihu.com/equation?tex=%5Cln%5Cleft%28x%5E%7B%5Cxi%7D%5Cright%29) ，其在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的弧长也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cln%5Cleft%28x%5E%7B%5Cxi%7D%5Cright%29) 。则当 ![[公式]](https://www.zhihu.com/equation?tex=x%3De) 时有：

![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ccdot%5Cxi%7D%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28e%5E%7B%5Cxi%7D%5Cright%29%5Cright%29%3D%5Cexp%28i%5Ccdot+%5Cxi%29.%5Ctag%7B6.7%7D)

也就是说以 ![[公式]](https://www.zhihu.com/equation?tex=e) 为底的指数函数的特殊之处在于，当其指数为 ![[公式]](https://www.zhihu.com/equation?tex=i%5Ccdot%5Cxi) 时，其在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的角度恰好也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi) ，并且在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的弧长也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi) 。更为特殊的，当 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi%3D%5Cpi) 时， ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ccdot%5Cpi%7D) 表示的是：在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的角度为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi%5Coverset%7B%5Ctriangle%7D%7B%3D%7D180%5E%7B%5Ccirc%7D) ，并且在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的弧长也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi) ，而在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动弧长 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi) 后到达的点是 ![[公式]](https://www.zhihu.com/equation?tex=%28-1%2C0%5Ccdot+i%29) 。因此，在这种意义上我们有：

![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ccdot%5Cpi%7D%3D-1.%5Ctag%7B6.8%7D)

------



## 参考

1. [^](https://zhuanlan.zhihu.com/p/303377401#ref_1_0)Euler's formula with introductory group theory https://www.youtube.com/watch?v=mvmuCPvRoWQ

1. [^](https://zhuanlan.zhihu.com/p/303377401#ref_2_0)奶牛快传链接 https://cowtransfer.com/s/2d0ff5dfa6d743

编辑于 2020-11-28

精选评论（1）

- [![饭饭](https://pic1.zhimg.com/3e575891324fab002732cb9e614172b5_s.jpg?source=06d4cd63)](https://www.zhihu.com/people/fanrongboy)[饭饭](https://www.zhihu.com/people/fanrongboy)2020-12-13

  本来都截图并标注，把原文里的一些笔误给画出来了，无奈知乎无法发图，只好用公式序号标记上下来定位了，公式太多，检查的不是很仔细，应该有不少遗漏，暂提交这些：

  1、（3.6）后面的Remark，xi=gi是不是写反了，应为gi=xi，和下面符号对应上

  2、（4.1.13）上面：综合以上三条，我们现在可以说映射 [公式] (或者映射 [公式] )是一个从集合 [公式] 到自身上的一个双射。//集合的名字怎么和映射一样？

  3、（4.1.13）下面：其实定义了这样一个映射 [公式] 之后我们就得到了关于 [公式] 的全部置换了。也就是说将来我们就不再区分 [公式] 和 [公式] 了。//为什么不区分？这不是两种不同的置换或者说映射吗？怎么能用同一个字母表示？

  4、（5.2.1.4）下面：同理可定义 正有理数集上的一个收缩 为：//下面的配图错误，用的还是拉伸的公式图片，看图片序号为5.2.1.3和前面重复了

  5、（5.2.1.6）上面：如果我们只观察负有理数 1 的话，//这里应该是-1

  6、（5.2.1.7）此处公式里括号中应该是-1，-2，-3才对

  7、（5.2.1.8）下面：这样我们就可以定义 负有理数集上的一个拉长 为：//下部的配图的有误，应该是5.2.1.9的图，却用了5.2.1.8的图。同时5.2.1.8这个公式图也有错误，括号里面不应该是-1、-2、-3的吗？

  8、（5.2.2.1）然后我们在有理数 [公式] 处放上一面镜子(平面镜)，则会在负有理数轴上出现一个点 [公式] //这个点的公式右上角少了一个+号

  9、（5.2.2.13）公式第一个三角符号下面漏了打一个右箭头

  10、（5.2.2.20）上面：最终我们可以将以上八种情况合并为 种：// 漏打了“一”字

  11、（5.2.2.24）上面：正有理数的正有理数倍伸缩不能与负有理数的正有理数倍伸缩复合 //此处配图有疑惑，公式符号和文字描述不对应，应为：++ 。-+ ；还有符合运算到底是从左到右开始还是从右到左计算，看公式似乎默认都是从右到左的？

  12、（5.2.2.24）Remark部分：于是我们便可以将第一次伸缩变换的到达域下一次伸缩变换的定义域做一下比较 //漏打了“与”字

  13、（5.2.2.26）下面：负有理数的正有理数倍拉长与负有理数的正有理数倍拉长互为逆元 //后一个“拉长”应为“收缩”



[zdr0](https://www.zhihu.com/people/97148f897df6540033355be3b742052b) (作者) 回复[饭饭](https://www.zhihu.com/people/3cd021639c1465f84ad127e130d74e38)2020-12-13

首先感谢你认真的读了我的文章并指出了不少问题～下面我对非笔误的问题进行一下回答。

3两种不同的映射可以使用同一字母表示，f=x^3和f=x^5，这两个都是R到R上的映射当然你也可以用不同的
10是没错的
11(5.2.2.24)是也无效复合的一个例子，前面那句话里有“例如”二字，但这个例子与前面那句话无关
# [知乎年度最长科普文]—上帝公式 e^(iπ)=-1 与群论有什么关系？



[zdr0](https://www.zhihu.com/people/sai-27-16)

数学话题下的优秀答主



编辑推荐

等 3 项收录



1,896 人赞同了该文章

大家好！事情的起因是半个多月之前的一个晚上，我无意间在油管上看到了 3b1b 大佬的一个视频[[1\]](https://zhuanlan.zhihu.com/p/303377401#ref_1)。看完之后我突然“灵光一现”，打算就此写一个“观后感”。我大意了啊，没有停笔，很快这个“灵光”的光强就“烧掉了”我不少头发。

现在大家看到的这篇科普文是原文的“花絮”，无论是在长度上还是在难度上相较于原文都有所削减。因为原文是长达 **37 页**的 pdf，是本人写科普文以来写过的最长的一篇文章，也是我修改次数最多的一篇文章。并且在原文中对很多细节都做了比较详细的讨论，我把原文的下载链接放在了最后[[2\]](https://zhuanlan.zhihu.com/p/303377401#ref_2)，大家有兴趣的话可以去读一读。

如果各位读了原文，并发现了其中的 ***错误\*** 的话请一定 ***评论\*** 告知我(**请不要私信，除非有特殊情况，否则我一般不看私信**)。感谢！

最后的一个小通知：由于这学期我非常忙，所以《十分钟数学课》系列暂时停更，等下个假期再重新开更。并且专栏文章的更新速度会变得很慢。大家见谅。

------

> 在阅读本文之前，请 ***忘记\*** 你所熟知的 Euler 公式：
> ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ctheta%7D%3D%5Ccos%28%5Ctheta%29%2Bi%5Ccdot+%5Csin%28%5Ctheta%29.%5C%5C)
> 因为当你将 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta%3D%5Cpi) 代入时它会直接告诉你：
> ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Cpi%7D%3D-1%5C%5C)
> 但如果这样这篇文章就没有存在的意义了。

***总注：\***

> ![[公式]](https://www.zhihu.com/equation?tex=%28%5Crm+i%29.) 不要被文章后面那些“复杂的”符号“吓到了”。如果大家能够将前面基本符号的运作方式搞清楚，则后面那些“复杂”符号的运作方式大家也就能清楚了。并且我对每个符号都举了例子，相信大家通过这些例子一定可以清楚那些符号的运作方式。
> ![[公式]](https://www.zhihu.com/equation?tex=%28%5Crm+ii%29.) 文中的下划线没有特殊含义。
> ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7B%28iii%29.%7D) 群论部分我会尽量用最简单的语言讲清楚。这也是为了告诉大家 ***不要跳过\*** 文章中的任何一部分，因为每一部分都至关重要并且环环相扣。跳过其中一部分会对后面的阅读造成障碍。
> ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7B%28iv%29.%7D) 这次文中没有任何证明，可安心阅读。
> ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7B%28v%29.%7D) ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B1%5Csim+4%7D) 节的目录结构与内容与原文的目录结构与内容一致。

![[公式]](https://www.zhihu.com/equation?tex=%5CLARGE+%5Cbm%7B%5Crm%7BContents%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B1.%7D) 引言
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B2.%7D) 群
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B3.%7D) 群同态
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B4.%7D) 置换与置换群
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.%7D) 站在群的角度上来理解代数运算
![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B6.%7D) 再看群同态与上帝公式和群论的关系

------

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B1%7D.%7D%7D) 引言

所谓上帝公式(即我们常说的 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7BEuler%7D) ***恒等式\*** )：

![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Cpi%7D%2B1%3D0.%5Ctag%7B1.1%7D)

这个公式充斥着无尽的美感，所以它也是我最喜欢的公式，没有之一。这个公式将自然底数 ![[公式]](https://www.zhihu.com/equation?tex=e) ，单位虚数 ![[公式]](https://www.zhihu.com/equation?tex=i) ，圆周率 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi) ，最小的自然数(这里认为![[公式]](https://www.zhihu.com/equation?tex=0)不是自然数) ![[公式]](https://www.zhihu.com/equation?tex=1) 与数字 ![[公式]](https://www.zhihu.com/equation?tex=0) 巧妙的组合在了一起。这个公式的起源有很多文章已经介绍过了，所以这篇文章我们就换一个视角来重新探索上帝公式背后隐藏的数学知识，而它背后的数学知识也告诉了我们上帝公式绝不仅仅只有表面上的这种数字关系。

为了探索这种探索上帝公式背后的数学知识，我们首先要来学一些群论的知识。

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B2%7D.%7D%7D) 群

我们先不看群的定义。现在让我们穿越回上小学的时候。上小学的时候，我们最先接触到的数字之间的运算就是两个数字之间的加法，更准确地说应该是两个自然数之间的加法。因为当时我们还不知道什么是整数，什么是小数等等。现在让我们脱离两个自然数之间的加法，来看一个更为高级运算，即 ***两个整数之间的加法\***。

为了与后面的群中的运算做对比，这里我们将整数集上的加法记作 ![[公式]](https://www.zhihu.com/equation?tex=+%2B_%7B%5Cmathbb%7BZ%7D%7D) (这与我们熟知的加法是一样的，只不过为其加上了下标 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 。其中 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 表示整数集。为一种运算添加这样的下标可以时刻提醒我们该运算是定义在哪个集合上的。这并非多此一举的做法，因为当运算种类增加的时候，如果没有这样的下标就可能会出现理解混乱)。

对于整数集上的加法我们知道它是满足结合律的，也就是说比如：

![[公式]](https://www.zhihu.com/equation?tex=%282%2B_%7B%5Cmathbb%7BZ%7D%7D3%29%2B_%7B%5Cmathbb%7BZ%7D%7D4%3D5%2B_%7B%5Cmathbb%7BZ%7D%7D4%3D2%2B_%7B%5Cmathbb%7BZ%7D%7D%283%2B_%7B%5Cmathbb%7BZ%7D%7D4%29%3D2%2B_%7B%5Cmathbb%7BZ%7D%7D7%3D9.%5Ctag%7B2.1%7D)

再比如：

![[公式]](https://www.zhihu.com/equation?tex=%28-5%2B_%7B%5Cmathbb%7BZ%7D%7D2%29%2B_%7B%5Cmathbb%7BZ%7D%7D7%3D-3%2B_%7B%5Cmathbb%7BZ%7D%7D7%3D4%3D-5%2B_%7B%5Cmathbb%7BZ%7D%7D%282%2B_%7B%5Cmathbb%7BZ%7D%7D7%29%3D-5%2B_%7B%5Cmathbb%7BZ%7D%7D9%3D4.%5Ctag%7B2.2%7D)

那么一般的，对于整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的任意三个整数 ![[公式]](https://www.zhihu.com/equation?tex=z_1%2C%5C%2Cz_2%2C%5C%2Cz_3%5Cin%5Cmathbb%7BZ%7D) ，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cz_1%2C%5C%2Cz_2%2C%5C%2Cz_3%5Cin%5Cmathbb%7BZ%7D%5C%2C%3A%5C%2C%28z_1%2B_%7B%5Cmathbb%7BZ%7D%7Dz_2%29%2B_%7B%5Cmathbb%7BZ%7D%7Dz_3%3Dz_1%2B_%7B%5Cmathbb%7BZ%7D%7D%28z_2%2B_%7B%5Cmathbb%7BZ%7D%7Dz_3%29.%5Ctag%7B2.3%7D)

除此以外我们还知道任何整数与整数 ![[公式]](https://www.zhihu.com/equation?tex=0) 的和都是该整数本身。比如：

![[公式]](https://www.zhihu.com/equation?tex=4%2B_%7B%5Cmathbb%7BZ%7D%7D0%3D0%2B_%7B%5Cmathbb%7BZ%7D%7D4%3D4%2C%5Cquad+-3%2B_%7B%5Cmathbb%7BZ%7D%7D0%3D0%2B_%7B%5Cmathbb%7BZ%7D%7D%28-3%29%3D-3.%5Ctag%7B2.4%7D)

即对于任意一个整数 ![[公式]](https://www.zhihu.com/equation?tex=z%5Cin%5Cmathbb%7BZ%7D) 而言，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cz%5Cin%5Cmathbb%7BZ%7D%5C%2C%3A%5C%2Cz%2B_%7B%5Cmathbb%7BZ%7D%7D0%3D0%2B_%7B%5Cmathbb%7BZ%7D%7Dz%3Dz.%5Ctag%7B2.5%7D)

因为整数 ![[公式]](https://www.zhihu.com/equation?tex=0) 的这种性质，我们将整数 ![[公式]](https://www.zhihu.com/equation?tex=0) 称为整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的 ***对加法\*** ***![[公式]](https://www.zhihu.com/equation?tex=%2B_%7B%5Cmathbb%7BZ%7D%7D)\*** ***的单位元素\*** 。同样是为了与将来群中的单位元素做对比，我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 的单位元素 ![[公式]](https://www.zhihu.com/equation?tex=0) 记作 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) 。

此外，对整数集中的每一个整数都存在一个“与之相反的”整数，使得两者的和为 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) 。比如：

![[公式]](https://www.zhihu.com/equation?tex=-5%2B_%7B%5Cmathbb%7BZ%7D%7D5%3D5%2B_%7B%5Cmathbb%7BZ%7D%7D%28-5%29%3D0_%7B%5Cmathbb%7BZ%7D%7D.%5Ctag%7B2.6%7D)

所以一般的，对于任意一个整数 ![[公式]](https://www.zhihu.com/equation?tex=z%5Cin%5Cmathbb%7BZ%7D) ，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cz%5Cin%5Cmathbb%7BZ%7D%2C%5Cquad+z%2B_%5Cmathbb%7BZ%7D%28-z%29%3D%28-z%29%2B_%5Cmathbb%7BZ%7Dz%3D0_%5Cmathbb%7BZ%7D.%5Ctag%7B2.7%7D)

这样的一个整数 ![[公式]](https://www.zhihu.com/equation?tex=-z) 我们称为整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的***整数\*** ***![[公式]](https://www.zhihu.com/equation?tex=z)\*** ***的对加法\*** ***![[公式]](https://www.zhihu.com/equation?tex=+%2B_%7B%5Cmathbb%7BZ%7D%7D)\*** ***的逆元\***。同样是为了与将来群中的逆元做对比，这里我们将整数 ![[公式]](https://www.zhihu.com/equation?tex=z) 的逆元记作 ![[公式]](https://www.zhihu.com/equation?tex=-z_%7B%5Cmathbb%7BZ%7D%7D) 。

最后我们要说的是两个整数的和一定还是一个整数，我们将此性质称为***整数集对其上的加法\*** ***![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D)\*** ***是封闭的\*** 。

另外，我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) 看做是一种作用，这个作用的效果是将输入的两个整数通过相加的方式变成第三个整数。这就意味着我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) 看做是一个映射：

![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D%3A%5Cmathbb%7BZ%7D%5Ctimes%5Cmathbb%7BZ%7D%5Cto%5Cmathbb%7BZ%7D%2C%5Cquad+%28z_1%2Cz_2%29%5Cmapsto+z_1%2B_%7B%5Cmathbb%7BZ%7D%7Dz_2.%5Ctag%7B2.8%7D)

这样一个映射也可以说明整数集对其上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) 是封闭的。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 显然，整数集上的单位元素是唯一的，即为 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) ，且对每个整数 ![[公式]](https://www.zhihu.com/equation?tex=z%5Cin%5Cmathbb%7BZ%7D) ，其逆元也是唯一的，即为 ![[公式]](https://www.zhihu.com/equation?tex=-z%5Cin%5Cmathbb%7BZ%7D) 。(注意，这里 ***不要\*** 说成整数集中的逆元是唯一的)

大家如果能完全理解上述有关整数的加法的例子话那么就成功了 ![[公式]](https://www.zhihu.com/equation?tex=99.%5Coverline%7B9%7D%5C%25) 啦～因为通过类比，我们可以非常轻松又快速地理解群的定义。下面我们就给出群的定义：

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bblue%7D%7B%5Clarge%7B%5Cbm%7B%5Crm%7BDefinition%5Cquad+2.1%3A%7D%7D%7D%7D)

设 ![[公式]](https://www.zhihu.com/equation?tex=M) 是一个集合，且设 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M) 为 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的一个运算：

![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M%3AM%5Ctimes+M%5Cto+M%2C%5Cquad+%28m_1%2Cm_2%29%5Cmapsto+m_1%5Ccirc_M+m_2.%5Ctag%7B2.9%7D)

则称结构 ![[公式]](https://www.zhihu.com/equation?tex=%28M%2C%5Ccirc_M%29) 是一个 ***群\*** ，当它满足以下条件时：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M) 是可结合的；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) (至少)存在一个 ![[公式]](https://www.zhihu.com/equation?tex=e_M%5Cin+M) ，使得对于所有的 ![[公式]](https://www.zhihu.com/equation?tex=m%5Cin+M) 有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2C+m%5Cin+M%5C%2C%3A%5C%2Ce_M%5Ccirc_M+m%3Dm%5Ccirc_M+e_M%3Dm.%5Ctag%7B2.10%7D)

这样的一个 ![[公式]](https://www.zhihu.com/equation?tex=e_M%5Cin+M) 称为 ![[公式]](https://www.zhihu.com/equation?tex=M) 中的 ***单位元素\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 对于每个 ![[公式]](https://www.zhihu.com/equation?tex=m%5Cin+M) ，存在(至少)一个 ![[公式]](https://www.zhihu.com/equation?tex=n_%7BM%7D%5Cin+M) ，使得：

![[公式]](https://www.zhihu.com/equation?tex=m%5Ccirc_M+n_%7BM%7D%3Dn_%7BM%7D%5Ccirc_M+m%3De_M.%5Ctag%7B2.11%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bblue%7D%7B%5Cblacksquare%7D)

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 显然，当我们将定义 ![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbm%7B%5Crm%7BDefinition%5Cquad+2.1%7D%7D%7D) 中的集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 换成集合 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) ，将运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc_M) 换成整数集上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%5Cmathbb%7BZ%7D) ，将集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 中的单位元素 ![[公式]](https://www.zhihu.com/equation?tex=e_M) 换成整数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BZ%7D) 中的单位元素 ![[公式]](https://www.zhihu.com/equation?tex=0_%5Cmathbb%7BZ%7D) ，将 ![[公式]](https://www.zhihu.com/equation?tex=m%2Cm_1%2Cm_2%5Cin+M) 换成 ![[公式]](https://www.zhihu.com/equation?tex=z%2Cz_1%2Cz_2%5Cin%5Cmathbb%7BZ%7D) ，将 ![[公式]](https://www.zhihu.com/equation?tex=n_M%5Cin%5Cmathbb%7BM%7D) 换成 ![[公式]](https://www.zhihu.com/equation?tex=-z_%7B%5Cmathbb%7BZ%7D%7D%5Cin%5Cmathbb%7BZ%7D) 时我们就可以理解群的定义了。

根据群的定义我们可以知道 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BZ%7D%2C%2B_%5Cmathbb%7BZ%7D%29) 是一个群，我们将这个群称为 ***整数加法群\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+2.1%3A%7D%7D%7D%7D)

请可各位读者朋友独立验证 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%7B%5Cmathbb%7BR%7D%7D%29) 与 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BC%7D%2C%2B_%7B%5Cmathbb%7BC%7D%7D%29) 也是两个群。且前者称为 ***实数加法群\*** ，后者称为 ***复数加法群\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D)

认识了什么是群之后我们就已经结束了三分之一的工作啦～打起精神，一鼓作气，把剩下的群的知识学完！下面将要介绍的一个重要的概念是 ***群同态 。\***

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B3%7D.%7D%7D) 群同态

这个名词听起来挺高端的是吧？其实我们通过一个我们高中就学过的函数便可以“可视化”群同态这个概念，进而让这个概念变得很好理解。下面我们就从这个函数讲起。

这个函数就是自然底数 ![[公式]](https://www.zhihu.com/equation?tex=e) 的指数函数。我们知道同底数的(这里为 ![[公式]](https://www.zhihu.com/equation?tex=e) )指数运算律为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28x_1%2Bx_2%29%3D%5Cexp%28x_1%29%5Ccdot%5Cexp%28x_2%29%2C%5Cquad+x_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B3.1%7D)

我们知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28x%29) 的定义域是实数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D) ，值域是正实数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%3E0%7D) 。所以，不严谨地可以说：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cx_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D%5C%2C%3A%5C%2C%5Cexp%28x_1%29%5Ccdot%5Cexp%28x_2%29%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D.%5Ctag%7B3.2%7D)

此时我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot) 写为正实数集上的乘法，即 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D) 。这是因为这里正实数集对 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D) 是封闭的，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%3A%5Cmathbb%7BR%7D_%7B%3E0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Cquad+%28%5Cexp%28x_1%29%2C%5Cexp%28x_2%29%29%5Cmapsto+%5Cexp%28x_1%29%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%5Cexp%28x_2%29%5Ctag%7B3.3%7D.)

又因为 ![[公式]](https://www.zhihu.com/equation?tex=x_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D) ，所以我们可以将 ![[公式]](https://www.zhihu.com/equation?tex=%2B) 写为实数域上的加法 ![[公式]](https://www.zhihu.com/equation?tex=%2B_%7B%5Cmathbb%7BR%7D%7D) 。如之前所述， ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%7B%5Cmathbb%7BR%7D%7D%29) 是一个群。并且容易验证 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29) 是一个乘法群(作为练习，请各位自行验证。注意， ![[公式]](https://www.zhihu.com/equation?tex=%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D) 的封闭性已经说过了，只需验证剩下三条即可)。于是现在我们得到了两个群，我们将两者分别定义为：

![[公式]](https://www.zhihu.com/equation?tex=G%3A%3D%28%5Cmathbb%7BR%7D%2C%2B_%5Cmathbb%7BR%7D%29%2C%5Cquad+H%3A%3D%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29.%5Ctag%7B3.4%7D)

则在这两个群之间的映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%3AG%5Cto+H) 满足：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cx_1%2C%5C%2Cx_2%5Cin%5Cmathbb%7BR%7D%5C%2C%3A%5C%2C%5Cexp%5Cleft%28x_1%2B_%7B%5Cmathbb%7BR%7D%7Dx_2%5Cright%29%3D%5Cexp%28x_1%29%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%5Cexp%28x_2%29.%5Ctag%7B3.5%7D+)

如果现在我们将群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%5Cmathbb%7BR%7D%29) 与群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29) 换成为两个一般的群 ![[公式]](https://www.zhihu.com/equation?tex=%28G%2C%5Ccirc_G%29) 和 ![[公式]](https://www.zhihu.com/equation?tex=%28H%2C%5Ccirc_H%29) ，群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D%2C%2B_%5Cmathbb%7BR%7D%29) 与群 ![[公式]](https://www.zhihu.com/equation?tex=%28%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D%29) 之间的映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp) 换成任意一个映射 ![[公式]](https://www.zhihu.com/equation?tex=f) ，但是使 ![[公式]](https://www.zhihu.com/equation?tex=f) 仍保持性质：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cg_1%2C%5C%2Cg_2%5Cin+G%5C%2C%3A%5C%2Cf%28g_1%5Ccirc_G+g_2%29%3Df%28g_1%29%5Ccirc_H+f%28g_2%29.%5Ctag%7B3.6%7D)

则 ![[公式]](https://www.zhihu.com/equation?tex=f) 就称为群 ![[公式]](https://www.zhihu.com/equation?tex=G) 与群 ![[公式]](https://www.zhihu.com/equation?tex=H) 之间的一个群同态。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 可以将式 ![[公式]](https://www.zhihu.com/equation?tex=%283.6%29) 与式 ![[公式]](https://www.zhihu.com/equation?tex=%283.5%29) 做一个类比：
> ![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+%26x_i%3Dg_i%2C%5Cquad+i%3D1%2C2%2C%5C%5C+%26G%3D%5Cmathbb%7BR%7D%2C%5C%5C+%26H%3D%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5C%5C+%26f%3D%5Cexp%2C%5C%5C+%26%5Ccirc_G%3D%2B_%5Cmathbb%7BR%7D%2C%5C%5C+%26%5Ccirc_H%3D%5Ccdot_%7B%5Cmathbb%7BR%7D_%7B%3E0%7D%7D.+%5Cend%7Barray%7D%5C%5C)
>
> 这样群同态就好理解了。

下面我就要给出群同态的定义了。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bblue%7D%7B%5Clarge%7B%5Cbm%7B%5Crm%7BDefinition%5Cquad+3.1%3A%7D%7D%7D%7D)

设 ![[公式]](https://www.zhihu.com/equation?tex=%28G%2C%5Ccirc_G%29) 与 ![[公式]](https://www.zhihu.com/equation?tex=%28H%2C%5Ccirc_H%29) 是两个群。一个从群 ![[公式]](https://www.zhihu.com/equation?tex=G) 到群 ![[公式]](https://www.zhihu.com/equation?tex=H) 的群同态是一个映射 ![[公式]](https://www.zhihu.com/equation?tex=f%3AG%5Cto+H) ，对该映射有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cforall%5C%2Cg_1%2C%5C%2Cg_2%5Cin+G%5C%2C%3A%5C%2Cf%28g_1%5Ccirc_G+g_2%29%3Df%28g_1%29%5Ccirc_H+f%28g_2%29.%5Ctag%7B3.7%7D)

我们将所有从群 ![[公式]](https://www.zhihu.com/equation?tex=G) 到群 ![[公式]](https://www.zhihu.com/equation?tex=H) 的同态 ![[公式]](https://www.zhihu.com/equation?tex=f) 的集合记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BHom%7D%28G%2CH%29) 。而且最为正规的记法为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BHom%7D_%7B%5Cmathrm%7BGroup%7D%7D%28%28G%2C%5Ccirc_G%29%2C%28H%2C%5Ccirc_H%29%29.%5Ctag%7B3.8%7D+)

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bblue%7D%7B%5Cblacksquare%7D)

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge+%7B%5Cbm%7B%5Crm%7B4%7D.%7D%7D) 置换与置换群

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B4.1%7D%7D) **置换**

新的知识又出现啦！我们还是先讲一个直观的例子。

<img src="https://pic4.zhimg.com/80/v2-06ac1fb9664101089a9a6a4184a1b013_1440w.jpg" alt="img" style="zoom:67%;" />



图片1

如图片 1 所示，我们将一个正方形的顶点自左上开始，按照顺时针方向从 ① 到 ④ 进行了编号。这样做的目的是为了让大家能够最直观的看到这个正方形所做的所有旋转和镜像变换。

现在我们来总结一下上面正方形的八种变换，它们分别是：什么也不做 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BId%7D) 围绕中心做逆时针 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D%2C%5C%2C180%5E%7B%5Ccirc%7D%2C%5C%2C270%5E%7B%5Ccirc%7D) 的旋转，关于两条平行于边的对称轴的镜像，以及关于两个对角线的镜像。

这样用文字描述变换实在是很不方便，所以我们现在来做一件有意思的事情，就是使用数字来表示这些变换。首先我们按照从 ①![[公式]](https://www.zhihu.com/equation?tex=%28%3D1%29) 到 ④![[公式]](https://www.zhihu.com/equation?tex=%28%3D4%29) 的顺序将处于初始状态的正方形的顶点写在一个括号中，比如像这样：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.1%7D)

这里需要注意：处于初始状态与不对这个正方形做任何变换不是一回事！现在我们让这个写有初始状态顶点所对应的数字的括号变得大一些：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+%5Cstar+%26+%5Cstar+%26+%5Cstar+%26%5Cstar+%5Cend%7Bpmatrix%7D%5Ctag%7B4.1.2%7D)

即我们在原先的括号下面又增加了一行，那么这一行要写什么呢？在回答这个问题之前我们要明确的是，除了不对正方形做变换这种情况以外，其他七种情况下，只要对正方形做了变换，那么变换之后正方形的每个顶点数字相对于初始状态的顶点数字都发生了变化。于是这一行要写的就是：正方形做了某一次变换后，相对于初始状态的顶点对应数字的变化。举两个具体的例子好了，首先就是最特殊的，我们不对正方形做任何变换，那么此时正方形的状态与处于初始状态时是一致的，即顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) 依然对应顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) ，顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) 依然对应顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) ...等等，所以此时第二行应该写的是：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+1+%26+2+%26+3+%26+4+%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.3%7D)

再比如正方形做了一个 ![[公式]](https://www.zhihu.com/equation?tex=270%5E%7B%5Ccirc%7D) 的旋转，那么对于旋转之后的顶点我们有：顶点 ![[公式]](https://www.zhihu.com/equation?tex=4) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) ；顶点 ![[公式]](https://www.zhihu.com/equation?tex=1) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) ；顶点 ![[公式]](https://www.zhihu.com/equation?tex=2) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=3) ；顶点 ![[公式]](https://www.zhihu.com/equation?tex=3) 对应了初始状态的顶点 ![[公式]](https://www.zhihu.com/equation?tex=4) 。于是此时，我们的第二行应该写：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+4+%26+1+%26+2+%26+3+%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.4%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+4.1.1%3A%7D%7D%7D%7D)

请大家尝试将剩余的 ![[公式]](https://www.zhihu.com/equation?tex=6) 的情况写出来。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D)

这样我们就实现了通过数字取描述正方形的这八种变换了。因为我们可以将处于初始状态的被数字 ![[公式]](https://www.zhihu.com/equation?tex=1%5Csim+4) 标记的正方形的四个顶点看成是 ![[公式]](https://www.zhihu.com/equation?tex=1) 号到 ![[公式]](https://www.zhihu.com/equation?tex=4) 号这四个位置，然后正方形每做一次变换这四个位置上的某几个数字就会出现更替，我们将更替之后的数字与 ![[公式]](https://www.zhihu.com/equation?tex=1) 号到 ![[公式]](https://www.zhihu.com/equation?tex=4) 号这四个位置一一对应起来就可以描述这种变换了。

很显然，数字的更替意味着数字相对于初始状态时的位置发生了变换，因此，我们将这些变换都称为 ***置换\*** 。

通过上述例子，相信大家对置换的概念已经有了一个基本的认识了，现在我们来深化一下置换的概念。我们还是继续上面的例子。

现在让我们 ***脱离正方形这个实体\*** ，而仅考虑 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字。我们还是先将 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 按照顺序写在一个括号中的第一行：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+%5Cstar+%26+%5Cstar+%26+%5Cstar+%26+%5Cstar++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.5%7D)

这里的第二行我们写 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字在做某种重新排列之后的结果，比如 ![[公式]](https://www.zhihu.com/equation?tex=2%2C1%2C4%2C3) ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.6%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+4.1.2%3A%7D%7D%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5C%5C)

对应了之前正方形的八种变换中的哪一种？

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D)

显然，第一行的数字经过这“某种重新排列”之后被重新排序，重新排序的结果是第二行的元素。现在我将所有的对应关系写出来，以方便大家理解：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+2+%5C%5C+%26+2%5Cto+1+%5C%5C+%26+3%5Cto+4+%5C%5C+%26+4%5Cto+3.+%5Cend%7Balign%2A%7D%5Ctag%7B4.1.7%7D)

通过所列出的所有对应关系我们可以发现：这种所谓的“重新排列”的变换实际上是一种映射关系，即 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每一个数字都通过这种映射变成 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B1%2C2%2C3%2C4%7D) ***这四个数字中的\*** 另一个。我们现在将该映射记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) ，然后我们可以将上面列出的四种关系写为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+%5Csigma%281%29%3D2+%5C%5C+%26+2%5Cto+%5Csigma%282%29%3D1+%5C%5C+%26+3%5Cto+%5Csigma%283%29%3D4+%5C%5C+%26+4%5Cto+%5Csigma%284%29%3D3.+%5Cend%7Balign%2A%7D.%5Ctag%7B4.1.8%7D)

现在我们可以说： ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这种排列顺序经过映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 的作用变成了 ![[公式]](https://www.zhihu.com/equation?tex=2%2C1%2C4%2C3) 这种排列顺序。现在我们将这种对应关系在之前的括号中可得：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+%5Csigma%281%29+%26+%5Csigma%282%29+%26+%5Csigma%283%29+%26+%5Csigma%284%29++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.9%7D)

当然，对于不同的重新排列我们的映射也是不同的，比如现在有如下的对应关系：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+4+%5C%5C+%26+2%5Cto+1+%5C%5C+%26+3%5Cto+2+%5C%5C+%26+4%5Cto+3.+%5Cend%7Balign%2A%7D.%5Ctag%7B4.1.10%7D)

显然，我们刚才的映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 并不能实现这种从 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 到 ![[公式]](https://www.zhihu.com/equation?tex=4%2C1%2C2%2C3) 的这种排列，因为比如 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%281%29%3D2%5Cne+4) 。但是我们可以找到另外一个映射，使得这个映射可以实现这种重新排列呀。比如我们可以将这个映射记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) ，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26+1%5Cto+%5Ctau%281%29%3D4+%5C%5C+%26+2%5Cto+%5Ctau%282%29%3D1+%5C%5C+%26+3%5Cto+%5Ctau%283%29%3D2+%5C%5C+%26+4%5Cto+%5Ctau%284%29%3D3.+%5Cend%7Balign%2A%7D%5Ctag%7B4.1.11%7D)

现在我们在置换的概念上又更近一步了，但是还缺乏严谨性。比如映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )具有什么性质呢？对于任意一个可数的有限集合我们如何定义这个一个映射呢？这种映射之间可以复合吗？复合所产生的效果又是什么呢？下面我们就一一来回答这些问题。

从我们刚刚所说的例子中我们发现：无论是映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 还是映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) 它们都具有以下性质：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 当映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )作用于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每个数字时，其结果也必然是这四个数字中的某一个，而不会出现别的数字。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 当映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )作用于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每个数字时，每个结果都是不同的，比如：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%281%29%3D2%2C%5Cquad+%5Csigma%282%29%3D1%2C%5Cquad%5Csigma%283%29%3D4%2C%5Cquad+%5Csigma%284%29%3D3.%5Ctag%7B4.1.12%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 当映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )作用于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 这四个数字中的每个数字时，每个数字在映射的作用下都会得到一个结果。

综合以上三条，我们现在可以说映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) (或者映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) )是一个从集合 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) 到自身上的一个双射。拿映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 举例，我们可以将它定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3A%5C%7B1%2C2%2C3%2C4%5C%7D%5Cto%5C%7B1%2C2%2C3%2C4%5C%7D%2C%5Cquad+%5Csigma%28i%29%3Dj%2C%5C%2C%5C%2Ci%2Cj%3D1%2C2%2C3%2C4.%5Ctag%7B4.1.13%7D)

其实定义了这样一个映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 之后我们就得到了关于 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C3%2C4) 的全部置换了。也就是说将来我们就不再区分 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 和 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctau) 了。

现在我们来回答第二个问题：对于任意一个可数的有限集合我们如何定义这个一个映射呢？从上一个问题的答案中我们知道，这样的一个映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 是一个集合到自身的双射，而这里的集合必须是 ***有限可数集合\*** 。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 这里的有限可数集合可以 ***非常不严谨地\*** 理解为：可以清点这样一个集合中的全部元素。

现在我们就来考察一个最简单的有限可数集合—由 ![[公式]](https://www.zhihu.com/equation?tex=1) 到 ![[公式]](https://www.zhihu.com/equation?tex=n) 这 ![[公式]](https://www.zhihu.com/equation?tex=n) 个自然数构成的集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D) 。则对于这样的一个集合我们可以定义置换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) ：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3A%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D%5Cto%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D%2C%5Cquad+%5Csigma%28i%29%3Dj%2C%5C%2C%5C%2Ci%2Cj%3D1%2C2%2C%5Cldots%2Cn.%5Ctag%7B4.1.14%7D)

我们也可以将其写为括号的形式，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+%5Cldots+%26+n+%5C%5C+%5Csigma%281%29+%26+%5Csigma%282%29+%26+%5Cldots+%26+%5Csigma%28n%29++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.15%7D)

更为一般地，我们可以对任意一个与集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D) ***等势的\*** 集合 ![[公式]](https://www.zhihu.com/equation?tex=X%3D%5C%7Bx_1%2Cx_2%2C%5Cldots%2Cx_n%5C%7D) 定义置换：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3AX%5Cto+X%2C%5Cquad+%5Csigma%28x_i%29%3Dx_j%2C%5C%2C%5C%2Ci%2Cj%3D1%2C2%2C%5Cldots%2Cn.%5Ctag%7B4.1.16%7D)

或将其写为括号的形式：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3D%5Cbegin%7Bpmatrix%7D+x_1+%26+x_2+%26+%5Cldots+%26+x_n+%5C%5C+%5Csigma%28x_1%29+%26+%5Csigma%28x_2%29+%26+%5Cldots+%26+%5Csigma%28x_n%29++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.17%7D)

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7BRemark%3A%7D%7D)
> 这里的等势可以 ***非常不严谨地\*** 理解为：集合 ![[公式]](https://www.zhihu.com/equation?tex=X%3D%5C%7Bx_1%2Cx_2%2C%5Cldots%2Cx_n%5C%7D) 与集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C%5Cldots%2Cn%5C%7D) 具有“相同的”元素个数。

现在我们来到了一个关键性的问题面前：两个置换之间是否可以进行复合？为了回答这个问题，我们再次回到之前所说的正方形的例子。首先非常显然的是我们现在处于初始状态的正方形逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后在此基础上再逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=180%5E%7B%5Ccirc%7D) 就相当于直接从初始状态逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=270%5E%7B%5Ccirc%7D) 。
另外一个不是十分明显的例子是：

![img](https://pic2.zhimg.com/80/v2-90a620118733af9a2f9bcef9aaa9d551_1440w.jpg)图

片2

即我们先将处于初始状态的正方形逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后在此基础上再将其关于连结左上和右下顶点的对角线进行镜像，所得到的结果与直接对处于初始状态的正方形关于竖直对称轴镜像的结果是一致的。图片2中的中的复合 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 表示的是变换的复合，也就是说“将处于初始状态的正方形逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后在此基础上再将其关于连结左上和右下顶点的对角线进行镜像”是一个***复合变换\*** ，其效果与单次变换“将处于初始状态的正方形关于竖直对称轴镜像”的结果是一致的。
同样我们发现，使用文字来描述这个复合变换是在是非常的繁琐。既然我们之前已经使用数字去表示置换了，那我们现在就使用这些数字去表示复合变换，即表示置换的复合。对于置换的复合，我们仍然使用符号 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 。
由之前所述我们知道，“将处于初始状态的正方形逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ”这个变换的数字表述为：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%3D+%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+3+%26+4+%26+1++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.18%7D)

而“将处于初始状态的正方形关于连结左上和右下顶点的对角线进行镜像”这个变换的数字表述为：

![[公式]](https://www.zhihu.com/equation?tex=%5Ctau%3D+%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+1+%26+4+%26+3+%26+2++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.19%7D)

最后，“将处于初始状态的正方形关于竖直对称轴镜像”这个变换的数字表述为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.20%7D)

于是，根据刚刚对复合变换的文字描述，我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5Ccirc%5Ctau%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+3+%26+4+%26+1++%5Cend%7Bpmatrix%7D%5Ccirc%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+1+%26+4+%26+3+%26+2++%5Cend%7Bpmatrix%7D%3D+%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%5C%5C+2+%26+1+%26+4+%26+3++%5Cend%7Bpmatrix%7D.%5Ctag%7B4.1.21%7D)

对于这一点我们可以来验证一下。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%26%28%5Csigma%5Ccirc%5Ctau%29%281%29%3D%5Csigma%28%5Ctau%281%29%29%3D%5Csigma%281%29%3D2%2C%5C%5C+%26%28%5Csigma%5Ccirc%5Ctau%29%282%29%3D%5Csigma%28%5Ctau%282%29%29%3D%5Csigma%284%29%3D1%2C%5C%5C+%26%28%5Csigma%5Ccirc%5Ctau%29%283%29%3D%5Csigma%28%5Ctau%283%29%29%3D%5Csigma%283%29%3D4%2C%5C%5C+%26%28%5Csigma%5Ccirc%5Ctau%29%284%29%3D%5Csigma%28%5Ctau%284%29%29%3D%5Csigma%282%29%3D3.+%5Cend%7Balign%2A%7D%5Ctag%7B4.1.22%7D)

显然，我们是对的！
通过这个直观的例子我们可以明白一个十分重要的问题：***置换之间是可以进行复合的，且复合之后的可以得到一个“新的”置换。并且从初始状态通过复合置换得到的结果与从初始状态直接通过这个“新的”置换得到的结果必然是一致的\*** 。而且如果你愿意的话，你甚至可以将多个置换进行复合。


![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B4.2%7D%7D) **置换群**
现在我们已经认识了群、群同态以及置换的概念了。下面我们来介绍 ***置换群\*** 。置换群中的元素是一个非空集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的置换。一个具体的例子就是我们刚才所举的集合 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C3%2C4%5C%7D) 上的置换 ![[公式]](https://www.zhihu.com/equation?tex=%5C%7B1%2C2%2C3%2C4%5C%7D) 。那么现在就产生了几个基本的问题：
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 置换群中的运算是什么？
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 置换群中的单位元素是什么？
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 置换群中各个元素的逆元是什么？
这些基本的问题都是关于群的定义的问题。下面我们还是来一一解答一下。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 首先是置换群中的运算。置换群中的运算就是我们之前所提到的两个置换之间的复合运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 。容易验证该运算是满足结合律的，且非空集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的置换所构成的集合对该运算是封闭的。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 置换群中的单位元素我们记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7B%7BId%7D%7D) 。之前正方形置换的例子中，“什么也不做”这一变换就是正方形置换的置换群中的单位元素。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 置换群中的元素 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 的逆元我们记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E%7B-1%7D) ，因为：

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5Ccirc%5Csigma%5E%7B-1%7D%3D%5Csigma%5E%7B-1%7D%5Ccirc%5Csigma%3D%5Cmathrm%7BId%7D.%5Ctag%7B4.2.1%7D)

一个直观的例子是：设变换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 为将正方形逆时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，则 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E%7B-1%7D) 表示的就是将正方形顺时针绕中心旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，那两个变换的复合变换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5Ccirc%5Csigma%5E%7B-1%7D) 就是将正方形先绕中心逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，然后再将正方形绕中心顺时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) ，那么最后的结果与“什么也不做”(即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BId%7D) )这一变换是一样的。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D) 置换 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma) 的逆是存在的，因为我们之前说过，置换是一个双射。
一个以集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 上的全部置换为元素的群我们称为 ![[公式]](https://www.zhihu.com/equation?tex=M) 的 ***对称群\*** ，并记作 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BSym%7D%28M%29) 。但集合 ![[公式]](https://www.zhihu.com/equation?tex=M) 具有 ![[公式]](https://www.zhihu.com/equation?tex=n) 则元素时， ![[公式]](https://www.zhihu.com/equation?tex=M) 的对称群可以记作 ![[公式]](https://www.zhihu.com/equation?tex=S_n) ，称为 ![[公式]](https://www.zhihu.com/equation?tex=n) 次对称群。现在我们在这篇文章中所需要的知识已经全部学完了。群论是一个非常庞大的知识体系，我这里也仅仅是为了写这篇科普文章才简单的介绍了一下群的一些基本概念。其他更深的知识就请对群论感兴趣的朋友自行探索吧。

##  ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge%5Cbm%7B%5Crm%7B5.%7D%7D) **站在群的角度上来理解代数运算**

在本节中，我们将要“忘记”我们熟知的基本的代数运算加法和乘法。我们会将数字理解为一些作用，通过这些作用可以将原来的数字变成新的数字。在定义后面的这些作用的时候我们会 ***仿照定义置换时所使用的那种括号的形式\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B%5Crm%7B5.1%7D%7D%7D) **整数的滑动与实数的滑动**
首先我们来定义滑动的概念。为了进一步的讨论和方便大家的理解，我们就将滑动的概念定义在整数集上。我们这里将要仿照置换的定义对滑动进行定义。首先我们还是来看直观的例子。

![img](https://pic2.zhimg.com/80/v2-0a09412a43e8bc2da23017e443270bfd_1440w.jpg)

图片3

如图片 3 所示，为了保证直观性，我们定义了所谓的“整数轴”，整数轴只在具体的整数处为点，其余各处均为虚线。现在我们对整数轴做一个向右滑动的动作，这个动作使整个整数轴向右滑动了一个单位。特别的，如果我们只观察数字 ![[公式]](https://www.zhihu.com/equation?tex=0) 的话，我们发现它通过这种滑动滑到了原来数字 ![[公式]](https://www.zhihu.com/equation?tex=1) 的位置上。这样一个滑动作用使我们有了以下的对应关系：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D++%5Cldots%5C%5C++-4%5Cto+-3%5C%5C++-3%5Cto+-2%5C%5C++-2%5Cto+-1%5C%5C++-1%5Cto+0%5C%5C++0%5Cto+1%5C%5C++1%5Cto+2%5C%5C++2%5Cto+3%5C%5C++%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.1.1%7D)

显然，上述的对应关系蕴含了一种映射关系，我们将这个映射记为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bv%7D) ，则：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D++%5Cldots%5C%5C++-4%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-4%29%3D-3%5C%5C++-3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-3%29%3D-2%5C%5C++-2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-2%29%3D-1%5C%5C++-1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-1%29%3D0%5C%5C++0%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%280%29%3D1%5C%5C++1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%281%29%3D2%5C%5C++2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%282%29%3D3%5C%5C++%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.1.2%7D)

虽然整数集是一个可数无穷集，但是我们依然可以 ***借助\*** 置换那里的记号，将上述映射关系写在一个括号中，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%3A%3D%5Cbegin%7Bpmatrix%7D+%5Cldots+%26+-4+%26+-3+%26+-2+%26+-1+%26+0+%26+1+%26+2+%26+3+%26%5Cldots+%5C%5C+%5Cldots+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-4%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-3%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-2%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%28-1%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%280%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%283%29+%26+%5Cldots++%5Cend%7Bpmatrix%7D.%5Ctag%7B5.1.3%7D)

这样我们就可以定义 ***整数集上的一个向右的滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bv%7D%3A%5Cmathbb%7BZ%7D%5Cto%5Cmathbb%7BZ%7D%2C%5Cquad+i%5Cmapsto+i%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamond%7D+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BZ%7D.%5Ctag%7B5.1.4%7D)

***整数集上的一个向左的滑动为\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bv%7D%3A%5Cmathbb%7BZ%7D%5Cto%5Cmathbb%7BZ%7D%2C%5Cquad+i%5Cmapsto+i%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BZ%7D.%5Ctag%7B5.1.5%7D)

下面通过几个例子说明几个问题。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 比如先将整数 ![[公式]](https://www.zhihu.com/equation?tex=1) 向右滑动 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamond%7D+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=4) 然后再将 ![[公式]](https://www.zhihu.com/equation?tex=4) 向左滑动 ![[公式]](https://www.zhihu.com/equation?tex=5) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=4%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+5) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=-1) ，这与直接将 ![[公式]](https://www.zhihu.com/equation?tex=1) 向左滑动两个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+2) 得到的结果是一样的。这说明了 ***整数的滑动是可以复合的\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 将任意一个整数滑动任意一个固定的整数单位 ![[公式]](https://www.zhihu.com/equation?tex=j) 所得到的结果都是唯一的，这说明了整数的滑动是可逆的(即双射的)。并且具体的，将整数 ![[公式]](https://www.zhihu.com/equation?tex=1) 向右滑动 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamond%7D+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=4) 然后再将 ![[公式]](https://www.zhihu.com/equation?tex=4) 向左滑动 ![[公式]](https://www.zhihu.com/equation?tex=3) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=4%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamond%7D+3) ，结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=1) 。这说明了对 ***任意一个固定的整数单位\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7Bj%7D) ***，左滑动与右滑动互为逆元\*** 。且对任意一个固定整数单位 ![[公式]](https://www.zhihu.com/equation?tex=j) 的左滑动与右滑动的复合为 ***单位元\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B%5Cmathrm%7BId%7D_V%7D) ，表示“不做滑动”。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 显然，整数的任意两个滑动的复合还是一个整数的滑动。***即定义在整数集上的滑动对复合运算\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) ***是封闭的\***。
有了整数的滑动以后我们就可以仿照它来定义实数的滑动了。***实数的一个向右的滑动\*** 定义为：

![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%3A%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.1.6%7D)

***实数的一个向左的滑动为\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%3A%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.1.7%7D)

同理，我们可以说明实数的滑动也是：
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 可以复合的。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 双射的，且具有逆元和单位元。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%7D%29.) 对复合是封闭的。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bdarkorange%7D%7B%5Clarge%7B%5Cbm%7B%5Crm+%7BExercise%5Cquad+5.1.1%3A%7D%7D%7D%7D)
请大家自行验证以上三条，对内容的理解会有一定帮助。
![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Ccolor%7Bdarkorange%7D%7B%5Cblacksquare%7D+)


![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B%5Crm%7B5.2%7D%7D%7D) **非零有理数与非零实数的伸缩**
![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbm%7B5.2.1%7D%7D) **正有理数与负有理数的伸缩**
作为引入，首先我们先来考察正有理数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BQ%7D_%7B%3E0%7D) 。我们先来定义正有理数集上的伸缩。

![img](https://pic1.zhimg.com/80/v2-5eb5f45a0b9a869800a324c500fbf12c_1440w.jpg)图片4

如图片 4 所示，我们这里又定义了一个“正有理数轴”(正有理数轴的虚线比整数轴稍微密了一点，这只是为了做一下区分)。现在我们对这个正有理数轴做一个拉长的动作，这个动作将整个正有理数轴拉长为原来的两倍(这就意味着做正有理数轴上的每一个点都被“拉长为”原来的两倍)。如果我们只观察正有理数 ![[公式]](https://www.zhihu.com/equation?tex=1) 的话，我们会发现它通过这种拉长的作用变为的原来的正有理数 ![[公式]](https://www.zhihu.com/equation?tex=2) 。因此对于这样一个拉长的作用我们有以下对应关系：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+1%5Cto+2%5C%5C+2%5Cto+4%5C%5C+3%5Cto+6%5C%5C+4%5Cto+8%5C%5C+5%5Cto+10%5C%5C+6%5Cto+12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.1%7D)

显然，上述的对应关系也蕴含了一种映射关系，我们将这个映射记为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D) ，则：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%281%29%3D2%5C%5C+2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%282%29%3D4%5C%5C+3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%283%29%3D6%5C%5C+4%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%284%29%3D8%5C%5C+5%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%285%29%3D10%5C%5C+6%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%286%29%3D12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.2%7D)

我们依然仿照置换中的记号，将上面的对应的关系写为括号的形式：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D%5Ctag%7B5.2.1.3%7D)

这样我们就可以定义 ***正有理数集上的一个拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.1.4%7D)

同理可定义 ***正有理数集上的一个收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B%2B%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D%5Ctag%7B5.2.1.3%7D)

下面我们依然通过几个例子说明几个问题。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 比如先将 ![[公式]](https://www.zhihu.com/equation?tex=1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=3) ，然后再将 ![[公式]](https://www.zhihu.com/equation?tex=3) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=6) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=3%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+6) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7B2%7D) ，这与直接将 ![[公式]](https://www.zhihu.com/equation?tex=1) 收缩两个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+2) 得到的结果是一样的。这说明了 ***正有理数的伸缩是可以复合的\*** 。

![img](https://pic4.zhimg.com/80/v2-067ca05ed4aa066b3b87708dc76f5bdb_1440w.jpg)

图片5：正有理数的伸缩复合示例。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 将任意一个正有理数拉长 (或收缩) 任意一个固定的 ***正有理数单位\*** ![[公式]](https://www.zhihu.com/equation?tex=j) 所得到的结果都是唯一的，这说明了正有理数拉长 (或收缩)是可逆的(即双射的)。并且具体的，先将 ![[公式]](https://www.zhihu.com/equation?tex=1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位，即 ![[公式]](https://www.zhihu.com/equation?tex=1%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3) ，得到结果 ![[公式]](https://www.zhihu.com/equation?tex=3) ，然后再将 ![[公式]](https://www.zhihu.com/equation?tex=3) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=3) 个为单位，即 ![[公式]](https://www.zhihu.com/equation?tex=3%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3) ，结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=1) 。这说明了对 ***任意一个固定的正有理数单位\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7Bj%7D) ***，拉长与收缩互为逆元\*** 。且对任意一个固定整数单位 ![[公式]](https://www.zhihu.com/equation?tex=j) 的拉长与收缩的复合为 ***单位元\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B%5Cmathrm%7BId%7D_S%7D) ，表示“不做伸缩”。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 显然，正有理数的任意两个伸缩的复合还是一个正有理数的伸缩。***即定义在正有理数集上的伸缩对复合运算\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) ***是封闭的\***。
有了正有理数的伸缩作为引入之后，我们再来看看负有理数集 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BQ%7D_%7B%3C0%7D) 上的伸缩。
为了方便说明，我们再来定义一个“负有理数轴”。这里我们同样将负有理数轴拉长到原来的两倍(这就意味着做负有理数轴上的每一个点都被“拉长为”原来的两倍)。如果我们只观察负有理数 ![[公式]](https://www.zhihu.com/equation?tex=1) 的话，我们会发现它通过这种拉长的作用变为的原来的负有理数 ![[公式]](https://www.zhihu.com/equation?tex=-2) 。因此对于这样一个拉长的作用我们有以下对应关系：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+-1%5Cto+-2%5C%5C+-2%5Cto+-4%5C%5C+-3%5Cto+-6%5C%5C+-4%5Cto+-8%5C%5C+-5%5Cto+-10%5C%5C+-6%5Cto+-12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.6%7D)

显然，上述的对应关系也蕴含了一种映射关系，我们将这个映射记为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D) ，则：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D+-1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%281%29%3D-2%5C%5C+-2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%282%29%3D-4%5C%5C+-3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%283%29%3D-6%5C%5C+-4%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%284%29%3D-8%5C%5C+-5%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%285%29%3D-10%5C%5C+-6%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%286%29%3D-12%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.2.1.7%7D)

我们依然仿照置换中的记号，将上面的对应的关系写为括号的形式：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.2.1.8%7D)

这样我们就可以定义 ***负有理数集上的一个拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%3D%5Cbegin%7Bpmatrix%7D+1+%26+2+%26+3+%26+4+%26+5+%26+6+%26%5Cldots+%5C%5C+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%283%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%284%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%285%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bs%5E%7B-%7D%7D%286%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.2.1.8%7D)

同理可定义 ***负有理数集上的一个收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bs%5E%7B-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C+j%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.1.10%7D)

并且，负有理数的伸缩与正有理数的伸缩的性质 ![[公式]](https://www.zhihu.com/equation?tex=%5Crm+i%29%5Csim%5Crm%7Biii%29%7D) 是类似的。留做练习，请大家自行说明。


![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbm%7B5.2.2%7D%7D) **非零有理数的纯镜像以及其负有理数倍伸缩**

刚才我们定义的伸缩中都有。 ![[公式]](https://www.zhihu.com/equation?tex=j%3E0) 那么现在问题来了，如果我非要定义一个***负有理数倍的伸缩\*** (即 ![[公式]](https://www.zhihu.com/equation?tex=j%3C0) ) 那怎么办呢？这里我们可以不直接对这个负有理数倍的伸缩做定义，我们先来定义一个叫 ***非零有理数的纯镜像\*** 的概念。



![img](https://pic4.zhimg.com/80/v2-eb6d68e07d1000dc45b0891724f0b53b_1440w.jpg)图片6

为了定义这个纯镜像的概念，如图片 6 所示，我们首先在正有理数轴上固定一个点 ![[公式]](https://www.zhihu.com/equation?tex=i) ，然后我们在有理数 ![[公式]](https://www.zhihu.com/equation?tex=0) 处放上一面镜子(平面镜)，则会在负有理数轴上出现一个点 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%7D%5C%2Ci) ，这个点与有理数 ![[公式]](https://www.zhihu.com/equation?tex=0) 之间的距离也为 ![[公式]](https://www.zhihu.com/equation?tex=i) ，我们就把 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Ci) 称为正有理数 ![[公式]](https://www.zhihu.com/equation?tex=i) 的 ***负镜像点\*** 。同理，对于每个负有理数 ![[公式]](https://www.zhihu.com/equation?tex=j) ，我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj) 称为负有理数 ![[公式]](https://www.zhihu.com/equation?tex=j) 的 ***正镜像点\*** 。

> 举两个例子：
> ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C5%3D-5%2C%5Cquad+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-2%29%3D2.%5Ctag%7B5.2.2.1%7D)

现在我们可以定义非零有理数的镜像的概念了。我们定义 ***正有理数的纯负镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Ci.%5Ctag%7B5.2.2.2%7D)

定义 ***负有理数的纯正镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Ci.%5Ctag%7B5.2.2.3%7D)
![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B%2B%7D%7D%5Ccirc%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B-%7D%7D%5Cright%29%3D+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B-%7D%7D%5Ccirc%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B%2B%7D%7D%5Cright%29%3D%5Cmathrm%7BId%7D_M.%5Ctag%7B5.2.2.4%7D)

有了非零有理数的纯镜像的概念之后我们就可以定义所谓的负数倍的伸缩了。定义 ***正有理数的负有理数倍拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.5%7D)

定义 ***正有理数的负有理数倍收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.6%7D)

定义 ***负有理数的负有理数倍拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.7%7D)

定义 ***负有理数的负有理数倍收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3C0%7D.%5Ctag%7B5.2.2.8%7D)

> 举两个例子，比如将 ![[公式]](https://www.zhihu.com/equation?tex=2) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=-3) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D6%3D-6%5Ctag%7B5.2.2.9%7D)
> 将 ![[公式]](https://www.zhihu.com/equation?tex=-4) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=-2) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-2%29%3D2.%5Ctag%7B5.2.2.10%7D)

现在为了统一符号，我们将要舍弃我们之前的正有理数的正有理数倍伸缩与负有理数的正有理数倍伸缩的定义，并通过一个新的概念—— ***纯虚镜像\*** ，给出两者的等价定义。首先我们来定义纯虚镜像。
定义 ***正有理数的纯正虚镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bm%5E%7B%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Ci%3Di.%5Ctag%7B5.2.2.11%7D)

定义 ***负有理数的纯负虚镜像\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bm%5E%7B-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2Ci%3Di.%5Ctag%7B5.2.2.12%7D)

> 举两个例子：
> ![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C5%3D5%2C%5Cquad+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-2%29%3D-2%5Ctag%7B5.2.2.13%7D)

有了纯虚镜像的定义之后，我们就可以将非零有理数的正有理数倍伸缩进行等价地定义了。我们将 ***正有理数的正有理数倍拉长\*** 等价地定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.14%7D)

将 ***正有理数的正有理数倍收缩\*** 等价地定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3E0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3E0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.15%7D)

将 ***负有理数的正有理数倍拉长\*** 等价地定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.16%7D)

将 ***负有理数的正有理数倍收缩\*** 等价地定义为:

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%3A%5Cmathbb%7BQ%7D_%7B%3C0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%3C0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%3E0%7D.%5Ctag%7B5.2.2.17%7D)

> 举两个例子，比如将 ![[公式]](https://www.zhihu.com/equation?tex=2) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=3) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C3%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5Cleft%282%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B%2B%7D%7D%5C%2C+3%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D6%3D6.%5Ctag%7B5.2.2.18%7D)
> 将 ![[公式]](https://www.zhihu.com/equation?tex=-4) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍，即： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-4%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-2%29%3D-2.%5Ctag%7B5.2.2.19%7D)

显然，通过上面所举的例子我们发现，以上八种变换都是可逆的(即双射的)。
最终我们可以将以上八种情况合并为种：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D%3A%5Cmathbb%7BQ%7D_%7B%5Cne+0%7D%5Cto%5Cmathbb%7BQ%7D_%7B%5Cne+0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbigtriangleup%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Clozenge%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BQ%7D_%7B%5Cne0%7D.%5Ctag%7B5.2.2.20%7D)

下面我们要来谈一谈 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的复合问题。我们通过一个例子来说明![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的复合问题。我们先将 ![[公式]](https://www.zhihu.com/equation?tex=-1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍(负有理数的正有理数倍拉长)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29.%5Ctag%7B5.2.2.21%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28-2%5Cright%29%3D-2.)

得到结果 ![[公式]](https://www.zhihu.com/equation?tex=-2) ，然后我们再将 ![[公式]](https://www.zhihu.com/equation?tex=-2) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=-3) 倍(负有理数的负有理数倍拉长)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C3%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-6%29%3D6.%5Ctag%7B5.2.2.22%7D)

这就说明了负有理数的负有理数倍拉长是可以复合负有理数的正有理数倍拉长的，更一般的，负有理数的负有理数倍伸缩可以复合负有理数的正有理数倍伸缩。
但是比如第一次做的伸缩是负有理数的正有理数倍伸缩，那么根据定义，此时的结果是负有理数，所以就 ***不能对此结果再做\*** 正有理数的伸缩操作了。这就说明了：***正有理数的伸缩不能与负有理数的正有理数倍伸缩复合\***。但是正有理数的伸缩可以与负有理数的负有理数倍伸缩复合，这是因为负有理数的负有理数倍伸缩的结果是正有理数。
经过以上的分析我们发现：![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的复合可分为 ***有效复合\*** 与 ***无效复合\*** 两种情况。所谓有效复合，指的就是例如负有理数的负有理数倍伸缩与负有理数的正有理数倍伸缩的复合，且：

![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%5Ccirc%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%5Cright%29%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D.%5Ctag%7B5.2.2.23%7D)

而所谓无效复合，指的就是例如正有理数的正有理数倍伸缩不能与负有理数的正有理数倍伸缩复合，并且对于无效复合，我们定义复合的结果为第一次伸缩变换的结果，即例如：

![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%5Ccirc%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%5Cright%29%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.24%7D)

定义有效复合与无效复合的原因是为了保证八种 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的两两复合对复合运算都是封闭的。因为从有效复合与无效复合的定义来看，两者的结果都仍是八种 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 中的某一种。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D)
> 由于八种 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 都是双射的，所以他们的到达域等于值域，于是我们便可以将第一次伸缩变换的到达域下一次伸缩变换的定义域做一下比较，当两者相同时复合便是有效的，否则是无效的。


并且我们有：
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 有效复合的有效复合是有效的；
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 有效复合的无效复合是无效的；
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 无效复合的有效复合是有效的；
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D) 无效复合的无效复合是无效的。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D)
> 在原文中我对 ![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 的两两复合做了 ***非常详细\*** 的讨论，***推荐大家去看一下原文或者视频\*** 。

有关逆元，我们也通过一个例子来说明。
我们先将 ![[公式]](https://www.zhihu.com/equation?tex=-1) 拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍(负有理数的正有理数倍拉长)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-1%29%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29.%5Ctag%7B5.2.2.25%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28-2%5Cright%29%3D-2.)

得到结果 ![[公式]](https://www.zhihu.com/equation?tex=-2) ，然后我们再将 ![[公式]](https://www.zhihu.com/equation?tex=-2) 收缩 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍(负有理数的正有理数倍收缩)，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cbigtriangleup%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%5Cleft%28%28-2%29%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Clozenge%5E%7B-%7D%7D%5C%2C2%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbigtriangleup%5E%7B-%7D%7D%28-1%29%3D-1.%5Ctag%7B5.2.2.26%7D)

结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=-1) ，这就说明了对于同一伸缩倍数 ![[公式]](https://www.zhihu.com/equation?tex=2) 而言，负有理数的正有理数倍拉长与负有理数的正有理数倍拉长互为逆元，两者复合的结果是单元元 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathrm%7BId%7D_%7BB%7D) ，表示“不进行伸缩”。

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Cmathrm%7BRemark%3A%7D%7D)
> 实际上，对于八种 ![[公式]](https://www.zhihu.com/equation?tex=+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D++) ： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.27%7D)
> 它们的逆元都是唯一的，并且(从左到右)分别为： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cbeta%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.28%7D)

对于非零实数而言，我们也可以定义它的伸缩为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D%3A%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cto%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%2C%5Cquad+i%5Cmapsto+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacktriangle%7D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacklozenge%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%7D%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D_%7B%5Cne0%7D.%5Ctag%7B5.2.2.29%7D)

其中 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacklozenge%7D) 表示非零实数的伸缩运算， ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cblacktriangle%7D) 表示非零实数的镜像(包括纯镜像和纯虚镜像)运算。与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) 一样，其也有八种情况：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.30%7D)

并且上述的八种映射都是双射的，也就是说它都是具有逆的，它们的逆分别是(从左到右)：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.2.2.31%7D)

并且这八种情况的复合也分有效复合与无效复合两种。且任意两个 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 对一般的复合运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 也是封闭的，且无效复合的无效复合还是无效的，无效复合的有效复合是有效的，有效复合的无效复合是无效的，有效复合的有效复合是有效的。***总之，\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) ***与\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cbeta%7D) ***的运作方式以及基本性质都是十分相似的\***。


![[公式]](https://www.zhihu.com/equation?tex=%5Clarge+%5Cbm%7B5.3%7D) **复数的滑动**

![img](https://pic4.zhimg.com/80/v2-bd006cd19364e9fa0cedac4a5354feff_1440w.jpg)

图片7

如图 7 中的滑动是将原始的复平面沿复数 ![[公式]](https://www.zhihu.com/equation?tex=5%2B3%5Ccdot+i) 进行的滑动。它可以被视为在实轴上的 ![[公式]](https://www.zhihu.com/equation?tex=5) 个单位的向右滑动(对应了实数的滑动)和虚轴上的 ![[公式]](https://www.zhihu.com/equation?tex=3) 个单位的向上滑动的复合，如图 8 所示。

![img](https://pic1.zhimg.com/80/v2-e4ac67daf616d8603873e2dd7eafc5b8_1440w.jpg)

图片8

图片 8 中的 ![[公式]](https://www.zhihu.com/equation?tex=%5Cheartsuit) 为一种运算，后面我们会看到它的定义。
这样的分解可以让我们分别得到实轴与虚轴上的两个对应关系。首先是实轴上的对应关系：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Cto+2%5C%5C+-2%5Cto+3%5C%5C+-1%5Cto+4%5C%5C+0%5Cto+5%5C%5C+1%5Cto+6%5C%5C+2%5Cto+7%5C%5C+3%5Cto+8%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.1%7D)

利用之前定义的实数的向右滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bu%7D) 我们可以得到：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-3%29%3D2%5C%5C+-2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-2%29%3D3%5C%5C+-1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-1%29%3D4%5C%5C+0%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%280%29%3D5%5C%5C+1%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%281%29%3D6%5C%5C+2%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%282%29%3D7%5C%5C+3%5Cto+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%283%29%3D8%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.2%7D)

然后我们就可以将实轴上的这种对应关系写为括号的形式了：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%3D+%5Cbegin%7Bpmatrix%7D+%5Cldots+%26+-3+%26+-2+%26+-1+%26+0+%26+1+%26+2+%26+3+%26+%5Cldots+%5C%5C+%5Cldots+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-3%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-2%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%28-1%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%280%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%281%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%282%29+%26+%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%283%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.3.3%7D)

下面我们再来看虚轴上的对应关系：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Ccdot+i%5Cto+0%5C%5C+-2%5Ccdot+i%5Cto+1%5Ccdot+i%5C%5C+-1%5Ccdot+i%5Cto+2%5Ccdot+i%5C%5C+0%5Cto+3%5Ccdot+i%5C%5C+1%5Ccdot+i%5Cto+4%5Ccdot+i%5C%5C+2%5Ccdot+i%5Cto+5%5Ccdot+i%5C%5C+3%5Ccdot+i%5Cto+6%5Ccdot+i%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.4%7D)

我们发现，如果我们只考察虚部的话，那么这种对应关系也可以被视为是实轴上的滑动。我们将这种 ***只看虚部的向上滑动\*** 定义为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cuparrow) 。于是我们有：
![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Br%7D+%5Cldots%5C%5C+-3%5Cto+%5Cmu%5Cuparrow%28-3%29%3D0%5C%5C+-2%5Cto+%5Cmu%5Cuparrow%28-2%29%3D1%5C%5C+-1%5Cto+%5Cmu%5Cuparrow%28-1%29%3D2%5C%5C+0%5Cto+%5Cmu%5Cuparrow%280%29%3D3%5C%5C+1%5Cto+%5Cmu%5Cuparrow%281%29%3D4%5C%5C+2%5Cto+%5Cmu%5Cuparrow%282%29%3D5%5C%5C+3%5Cto+%5Cmu%5Cuparrow%283%29%3D6%5C%5C+%5Cldots+%5Cend%7Barray%7D.%5Ctag%7B5.3.5%7D)

写为括号的形式为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cuparrow%3D+%5Cbegin%7Bpmatrix%7D+%5Cldots+%26+-3+%26+-2+%26+-1+%26+0+%26+1+%26+2+%26+3+%26+%5Cldots+%5C%5C+%5Cldots+%26+%5Cmu%5Cuparrow%28-3%29+%26+%5Cmu%5Cuparrow%28-2%29+%26+%5Cmu%5Cuparrow%28-1%29+%26+%5Cmu%5Cuparrow%280%29+%26+%5Cmu%5Cuparrow%281%29+%26+%5Cmu%5Cuparrow%282%29+%26+%5Cmu%5Cuparrow%283%29+%26+%5Cldots+%5C%5C+%5Cend%7Bpmatrix%7D.%5Ctag%7B5.3.6%7D)

这样我们就可以定义复数集上的一个 ***右上滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29.%5Ctag%7B5.3.7%7D)

其中运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Cheartsuit) ***表示先沿实轴做滑动\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7Bu%7D) ***，然后在沿虚轴做滑动\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cupdownarrow) 。
我们刚刚定义了复平面的右上滑动，同理我们可以借助 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7Bu%7D) 和 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cupdownarrow) 具体的定义 ![[公式]](https://www.zhihu.com/equation?tex=8) 个基本方向上的滑动。但是在此之前，我们还需要先对 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cupdownarrow) 做一个明确的定义。定义 ***只考虑虚部的下滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cuparrow%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+k%5Cmapsto+k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C+l%2C%5C%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.8%7D)

定义 ***只考虑虚部的上滑动\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%5Cdownarrow%3A%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BR%7D%2C%5Cquad+k%5Cmapsto+k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2C+l%2C%5C%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.9%7D)

接下来我们就可以具体地定义复平面的 ![[公式]](https://www.zhihu.com/equation?tex=8) 个基本方向上的滑动了。定义 ***复数集上的右上滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2Cl%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.10%7D)

定义 ***复数集上的右下滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Csearrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cdownarrow%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cdownarrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2Cl%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.11%7D)

定义 ***复数集上的左上滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnwarrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C+l%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.12%7D)

定义 ***复数集上的左下滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cswarrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%2C%5Cmu%5Cdownarrow%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cdownarrow%5Cright%29%3D%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2Cj%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2Cl%5Cright%29%2C%5Cquad+j%2C%5C%2Cl%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.13%7D)

定义 ***复数集上的竖直上滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cuparrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cmathrm%7BId%7D_U%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto%5Cleft%28%5Cmathrm%7BId%7D_U%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3Dk%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2Cl%2C%5Cquad+l%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.14%7D)

定义 ***复数集上的竖直下滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cdownarrow%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cmathrm%7BId%7D_U%2C%5Cmu%5Cdownarrow%5Cright%29%5Cmapsto%5Cleft%28%5Cmathrm%7BId%7D_U%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cdownarrow%5Cright%29%3Dk%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2Cl%2C%5Cquad+l%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.15%7D)

定义 ***复数集上的水平左滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftarrow%7D%7Bw%7D%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%2C%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%3Di%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5Cquad+j%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.16%7D)

定义 ***复数集上的水平右滑动\*** ：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7Bw%7D%3A%5Cmathbb%7BR%7D%5Ctimes%5Cmathbb%7BR%7D%5Cto%5Cmathbb%7BC%7D%2C%5Cquad+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmathrm%7BId%7D_%7BMU%7D%5Cright%29%3Di%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+j%2C%5Cquad+j%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B5.3.17%7D)

下面我们通过例子来说明几个问题。
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 我们对复数 ![[公式]](https://www.zhihu.com/equation?tex=0%2B0%5Ccdot+i) 先做右上滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+1+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C2%5Cright%29) 得到结果 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，再做右上滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+2+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C1%5Cright%29) 得到结果 ![[公式]](https://www.zhihu.com/equation?tex=3%2B3%5Ccdot+i) ，那么最终的效果与直接做右上滑动 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+3+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C3%5Cright%29) 滑动的效果是一样的。这就说明了 ***复数的滑动是可以复合的\*** 。

![img](https://pic2.zhimg.com/80/v2-fd886c9a6886f74148e8589151b9d29d_1440w.jpg)图片9：复数滑动的复合。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 我们对复数 ![[公式]](https://www.zhihu.com/equation?tex=0%2B0%5Ccdot+i) 先做右上滑动![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+1+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C2%5Cright%29) 得到结果 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，再做左下滑动![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28i%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+1+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28k%5C%2C%7B%5Cdiamondsuit%7D%5Cdownarrow%5C%2C2%5Cright%29) ，结果又回到了 ![[公式]](https://www.zhihu.com/equation?tex=0%2B0%5Ccdot+i) 。这就说明了***复数的滑动是可逆的\*** 。具体而言，之前定义的复平面在八个基本方向上的滑动：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%2C%5C%2Cw%5Csearrow%2C%5C%2Cw%5Cnwarrow%2C%5C%2Cw%5Cswarrow%2C%5C%2Cw%5Cuparrow%2C%5C%2Cw%5Cdownarrow%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7Bw%7D%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7Bw%7D%5Ctag%7B5.3.18%7D)

的逆分别是(从左至右)分别是：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cswarrow%2C%5C%2Cw%5Cnwarrow%2C%5C%2Cw%5Csearrow%2C%5C%2Cw%5Cnearrow%2C%5C%2Cw%5Cdownarrow%2C%5C%2Cw%5Cuparrow%2C%5C%2C%5Cunderset%7B%5Crightarrow%7D%7Bw%7D%2C%5C%2C%5Cunderset%7B%5Cleftarrow%7D%7Bw%7D.%5Ctag%7B5.3.19%7D)
![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 复数集上的任意两个滑动的复合还是还是一个复数集上的滑动。即定义在***复数集上的滑动对复合运算\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) ***是封闭的\*** 。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge+%5Cbm%7B5.4%7D) **非零复数的旋转伸缩**

现在终于来到了我们的最后一个部分了。非零复数的伸缩分为两种，一种是非零复数的非零实数倍的伸缩，这种伸缩我们也称为 ***纯伸缩\*** 。另外一种是非零复数的非零复数倍的伸缩，这种伸缩我们称为 ***带旋转的伸缩\*** 。对于带旋转的伸缩，我们还需定义的是 ***纯旋转\*** 的概念。首先我们先来看非零复数的纯伸缩。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.1%7D) **非零复数的纯伸缩**

> **这是原文中最为复杂的一部分，所以这里我打算换一种简单的定义方式。**

![img](https://pic1.zhimg.com/80/v2-f0769f2715e7f555f1cce5dfa70e10cc_1440w.jpg)图片10

如图片 10 所示，我们将复平面拉长为原来的两倍，这相当于我们同时将实轴与虚轴拉长到原来的两倍。而非零实数的正实数倍拉长我们之前已经定义过了，并且，对虚轴如果我们只考虑它的虚部的话，那么这里虚轴的拉长我们也可以视为非零实数的正实数倍拉长。这或许为我们定义非零复数的纯伸缩提供了一种思路。所以我们不妨顺着这个思路继续深入。我们首先要做的就是仿照非零实数的正实数倍拉长，定义一个对应的 ***只考虑虚轴的拉长 。\***

![[公式]](https://www.zhihu.com/equation?tex=r%5Cupdownarrow%3A%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cto%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%2C%5Cquad+i%5Cmapsto+%7B%5Cblacktriangle%7D%5Cupdownarrow%5Cleft%28i%5C%2C%7B%5Cblacklozenge%7D%5Cupdownarrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%7D%5Cuparrow%5C%2Cj%5Cright%29%5Cright%29%2C%5C%2C%5C%2Cj%5Cin%5Cmathbb%7BR%7D_%7B%5Cne0%7D%5Ctag%7B5.4.1.1%7D.)

这里将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 中的左右箭头 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleftrightarrow) 换成了上下箭头 ![[公式]](https://www.zhihu.com/equation?tex=%5Cupdownarrow) ，表示的是 ***竖直方向上的伸缩\*** 。显然， ![[公式]](https://www.zhihu.com/equation?tex=r) 也具有 ![[公式]](https://www.zhihu.com/equation?tex=8) 种子情况。

其中 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 必须与 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cupdownarrow) ***必须同为拉长或者同为收缩，并且同为拉长时，拉长的倍数必须相等；同为收缩时，收缩的倍数必须相等\*** 。

并且我们知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) 的定义域与值域也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%5Cne+0%7D) 与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%5Cne+0%7D) 。这样我们就可以先来定义实部和虚部都不等于零的复数的伸缩了：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%2A%5Cupdownarrow%7D%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cupdownarrow.%5Ctag%7B5.4.1.2%7D)

其中运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Cclubsuit) 表示 ***实轴与虚轴同时做相同倍数的拉长或者相同倍数的收缩\*** 。另外我们知道，非零复数还包括在实轴上的复数和在虚轴上的复数。那么我们进一步定义在实轴上的复数的伸缩为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%5C%2C%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D.%5Ctag%7B5.4.1.3%7D)

而在虚轴上的复数的伸缩我们定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D%5C%2C%3A%3D+r%5Cupdownarrow.%5Ctag%7B5.4.1.4%7D)

式 ![[公式]](https://www.zhihu.com/equation?tex=%285.4.1.3%29%2C%5C%2C%285.4.1.4%29) 并不意味着当其中一个轴做伸缩时另外一个轴就不做相同的伸缩了，所以这里我们可以理解为当实轴做伸缩 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleftrightarrow) 时，虚轴在 ***被动地做与实轴一样的伸缩\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D) ；当虚轴做伸缩 ![[公式]](https://www.zhihu.com/equation?tex=%5Cupdownarrow) 时，实轴在 ***被动地做与虚轴一样的伸缩\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D) 。

现在我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%2A%5Cupdownarrow%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D) 合并到一起，并统一定义为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cupdownarrow.%5Ctag%7B5.4.1.5%7D+%5Cend%7Barray%7D)

我们根据非零复数所处的位置便可知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%2A%5Cupdownarrow%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%2C%5C%2C%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D) 中的哪一个。具体的我们可以定义 ***非零复数的纯拉长\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Crightarrow%7D%7B%5Cdelta%5Cuparrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cuparrow.%5Ctag%7B5.4.1.6%7D+%5Cend%7Barray%7D)

定义***非零复数的纯收缩\*** 为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cdelta%5Cdownarrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%5Cunderset%7B%5Cleftarrow%7D%7B%5Cgamma%7D%5C%2C%5Cclubsuit%5C%2Cr%5Cdownarrow.%5Ctag%7B5.4.1.7%7D+%5Cend%7Barray%7D)

最后我们来谈一谈 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 复合的问题。对于 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D) 或者 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5Cupdownarrow%7D) 的复合情况这里就不再说明了，因为这两种情况下的复合与非零实数伸缩的复合原理是一样的。不过可以从这两种特殊情况中看到的是： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 复合也会涉及到有效复合与无效复合这两种不同的情况。但是， ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 的复合是否有效也完全取决于 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%7D) (或 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cupdownarrow) )之间的复合是否有效。

> 举一个实际的例子。比如我想将复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) 做 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%29) 倍的拉长，这就意味着我们要同时对实轴和虚轴做![[公式]](https://www.zhihu.com/equation?tex=%28-2%29)倍的拉长： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+2%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D2%3D-2.%5Ctag%7B5.4.1.8%7D) ![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B%2B%5Cto-%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cdownarrow4%3D-4.%5Ctag%7B5.4.1.9%7D)
> 这样得到的结果是 ![[公式]](https://www.zhihu.com/equation?tex=-2-4%5Ccdot+i) 。因为此时 ![[公式]](https://www.zhihu.com/equation?tex=i%2C%5C%2Cj) 都是负实数(即 ![[公式]](https://www.zhihu.com/equation?tex=%28i%2Cj%29) 为一负有序实数对)，所以我们就不能进一步对 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%2C-4%29) 做正实数的伸缩的了(即正有序实数对的负伸缩不能复合其自身，即这种复合就是无效的)。但是我们可以对负有序实数对 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%2C-4%29) 做负有序实数对的伸缩，比如再对它做一个 ![[公式]](https://www.zhihu.com/equation?tex=%28-2%29) 倍的拉长： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B-%5Cto%2B%7D%7D%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cleft%28-2%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E-%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cleft%28-2%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E-%7D%5C%2C+2%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B-%7D%7D%28-4%29%3D4.%5Ctag%7B5.4.1.10%7D) ![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B-%5Cto%2B%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5Cleft%28-4%5C%2C%7B%5Cblacklozenge%5E-%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5C%2C%28-2%29%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%7B-%7D%7D%5Cuparrow%5Cleft%28-4%5C%2C%7B%5Cblacklozenge%5E-%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%5Cblacktriangle%5E%7B-%7D%5Cuparrow%28-8%29%3D8.%5Ctag%7B5.4.1.11%7D)
> 这样最终的结果是 ![[公式]](https://www.zhihu.com/equation?tex=4%2B8%5Ccdot+i) 。

对于无效的复合，我们依然将其结果定义为复合之前的变换。这样就保证了 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 对复合的封闭性。并且我们断言： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) 的所有情况都是可逆的。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.2%7D) **非零复数的纯旋转**

非零复数的纯旋转的定义可以说是非常直观的。首先是 ***非零复数的纯逆时针旋转\*** ：

![[公式]](https://www.zhihu.com/equation?tex=p_%7B%5Ccirclearrowleft%7D%3A%5Cmathbb%7BR%7D_%7B%3E0%7D%5Ctimes%5B0%2C2%5Cpi%29%5Cto%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%28r%2C%5Cphi%29%5Cmapsto+%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta%2C%5Cquad%5Ctheta%5Cin%5B0%2C2%5Cpi%29.%5Ctag%7B5.4.2.1%7D)

然后是 ***非零复数的纯顺时针旋转\*** ：

![[公式]](https://www.zhihu.com/equation?tex=p_%7B%5Ccirclearrowright%7D%3A%5Cmathbb%7BR%7D_%7B%3E0%7D%5Ctimes%5B0%2C2%5Cpi%29%5Cto%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%28r%2C%5Cphi%29%5Cmapsto+%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowright%5Ctheta%2C%5Cquad%5Ctheta%5Cin%5B0%2C2%5Cpi%29.%5Ctag%7B5.4.2.2%7D)

> 举个实际的例子：
> ![[公式]](https://www.zhihu.com/equation?tex=%282%2C60%5E%7B%5Ccirc%7D%29%5Cmapsto+%5Cleft%282%5Cangle60%5E%7B%5Ccirc%7D%5Cright%29%5Ccirclearrowleft15%5E%7B%5Ccirc%7D%5Ctag%7B5.4.2.3%7D%3D2%5Cangle75%5E%7B%5Ccirc%7D.)
> 表示的就是将长度为 ![[公式]](https://www.zhihu.com/equation?tex=2) 的，辐角为 ![[公式]](https://www.zhihu.com/equation?tex=60%5E%7B%5Ccirc%7D) 的复数逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=15%5E%7B%5Ccirc%7D) 。

并且我们容易验证以下几点：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) 定义在复数集上的纯旋转是可以复合的。比如先将复平面逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=45%5E%7B%5Ccirc%7D) (即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft+45%5E%7B%5Ccirc%7D) )，然后再逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=45%5E%7B%5Ccirc%7D) (即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft+45%5E%7B%5Ccirc%7D) )，则最后的效果与直接逆时针旋转 ![[公式]](https://www.zhihu.com/equation?tex=90%5E%7B%5Ccirc%7D) (即 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft+90%5E%7B%5Ccirc%7D) )的效果是一致的，如图11所示：

![img](https://pic4.zhimg.com/80/v2-7666bccb59210c0d69eab85dbad8eb1b_1440w.jpg)图片11

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) 定义在复数集上的纯旋转是双射的(即可逆的)。因为我们可以将任意一个非零的复数 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cangle%5Cphi) 通过逆时针(或顺时针)旋转角度 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta) 都可对应于复平面上的一个复数。而且反过来，将复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta) (或 ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta) ) 顺时针(或逆时针)旋转之后都可以唯一对应到一个非零的复数 ![[公式]](https://www.zhihu.com/equation?tex=r%5Cangle%5Cphi) 。

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 定义在复数集上的任意两个纯旋转的复合还是一个复数集上的纯旋转。即定义在复数集上的纯旋转对复合运算 ![[公式]](https://www.zhihu.com/equation?tex=%5Ccirc) 是封闭的。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.3%7D) **非零复数的带旋转的伸缩**

在定义非零复数的带旋转的伸缩之前我们首先要来思考一个问题：我们是否真的仅仅将非零复数的纯伸缩与纯旋转进行复合就可以了？答案是否定的。但这是为什么呢？如果不将两者直接复合那应该如何定义非零复数的的带旋转的伸缩呢？这里我们不妨先回忆我们非零复数的纯伸缩的定义。在我们讨论非零复数的纯伸缩的时候我们发现，对于非零复数的正实数伸缩，伸缩的结果总是没有镜像效果的(我们可以将这种伸缩称为非零复数的 ***保向伸缩\*** )，即非零复数的正实数伸缩总是将一个复数直接进行伸缩而不用考虑镜像(这一点的根源是非零实数的正实数伸缩)。而非零复数的负实数伸缩总是会产生镜像作用的(即复数在被拉长的同时会通过复平面的原点中心对称，这一点的根源是非零实数的负实数伸缩)，而这种镜像作用恰好对应了非零复数的纯 ![[公式]](https://www.zhihu.com/equation?tex=180%5E%7B%5Ccirc%7D) 旋转。所以我们如果直接将非零复数的纯伸缩与非零复数的纯旋转复合的话会很混乱。所以取而代之的是，我们将 ***非零复数的正实数伸缩与非零复数的纯旋转进行复合\*** ，进而来定义非零复数的带旋转的伸缩。

这里我们首先要给出具体的非零复数的正实数伸缩的定义。我们将要分八种情况进行说明。我们将“挖掉原点的”复平面拆解一下，拆解为一下八个部分：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D) ***实轴正半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D) ***实轴负半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) ***虚轴正半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D) ***虚轴负半轴\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D) ***实部与虚部均大于零的部分\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvi%29.%7D) ***实部小于零，但是虚部大于零的部分\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvii%29.%7D) ***实部与虚部均小于零的部分\*** ；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bviii%29.%7D) ***实部大于零，但是虚部小于零的部分\*** 。

之后我将 ***使用相应的编号来代表这八个部分\*** 。首先要明确的是 ***任意一个非零复数一定处于这八个部分中的一个，且同时只能属于唯一的一个\*** 。所以我们定义非零复数的正实数伸缩可以通过对这八种情况分别进行定义。下面我们就来逐一的定义一下：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28%2B%2C0%29%5Cto%28%2B%2C0%29%7D%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%5C%2C%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D.%5Ctag%7B5.4.3.1%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28-%2C0%29%5Cto%28-%2C0%29%7D%5Cupdownarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%5C%2C%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D.%5Ctag%7B5.4.3.2%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5E%7B%280%2C%2B%29%5Cto%280%2C%2B%29%7D%5Cupdownarrow%7D%5C%2C%3A%3D+r%5E%7B%2B%5Cto%2B%7D%5Cupdownarrow.%5Ctag%7B5.4.3.3%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5E%7B%280%2C-%29%5Cto%280%2C-%29%7D%5Cupdownarrow%7D%5C%2C%3A%3D+r%5E%7B-%5Cto-%7D%5Cupdownarrow.%5Ctag%7B5.4.3.4%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28%2B%2C%2B%29%5Cto%28%2B%2C%2B%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B%2B%5Cto%2B%7D%5Cupdownarrow.%5Ctag%7B5.4.3.5%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvi%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28-%2C%2B%29%5Cto%28-%2C%2B%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B%2B%5Cto%2B%7D%5Cupdownarrow.%5Ctag%7B5.4.3.6%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28-%2C-%29%5Cto%28-%2C-%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B-%5Cto-%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B-%5Cto-%7D%5Cupdownarrow.%5Ctag%7B5.4.3.7%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bviii%29.%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5E%7B%28%2B%2C-%29%5Cto%28%2B%2C-%29%7D%5Cupdownarrow%7D%3A%3D+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%5C%2C%5Cclubsuit%5C%2Cr%5E%7B%2B%5Cto-%7D%5Cupdownarrow.%5Ctag%7B5.4.3.8%7D)

我们将以上八种情况合并为映射 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D%5C%2C%3A%5Cleft%28%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Ctimes%5C%7B0%5C%7D%5Cright%29%5C%2C%5Ccup%5C%2C%5Cleft%28%5C%7B0%5C%7D%5Ctimes%5Cmathbb%7BR%7D_%7B%5Cne+0%7D%5Cright%29%5Cright%29%5Cto+%5Cmathbb%7BC%7D_%7B%5Cne+0%7D) 。根据复数所处的位置我们可以明确 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D) 应为以上八种情况中的哪一种。

现在非零复数的正实数倍拉长 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D) 已经定义好了，下面我们就可以来定义非零复数带旋转的伸缩了。如之前所述，非零复数带旋转的伸缩可由为零复数的正实数倍拉长与非零复数的纯旋转复合得到(我们下面 ***只讨论逆时针旋转\*** ，顺时针旋转同理)：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi%3A%5Cmathbb%7BR%7D_%7B%5Cne0%7D%5Ctimes%5B0%2C2%5Cpi%29%5Cto%5Cmathbb%7BC%7D_%7B%5Cne+0%7D%2C%5Cquad+%28r%2C%5Cphi%29%5Cmapsto%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D%5C%2C%5Ccirc+%5Cleft%28%5Cleft%28r%5Cangle%5Cphi%5Cright%29%5Ccirclearrowleft%5Ctheta%5Cright%29%5Cright%29.%5Ctag%7B5.4.3.9%7D)

> 举一个具体的例子： 先将 ![[公式]](https://www.zhihu.com/equation?tex=%5Csqrt%7B3%7D%2Bi) 逆时针 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta%3D30%5E%7B%5Ccirc%7D) 的旋转得到： ![[公式]](https://www.zhihu.com/equation?tex=%282%2C30%5E%7B%5Ccirc%7D%29%5Cmapsto%5Cleft%282%5Cangle30%5E%7B%5Ccirc%7D%5Cright%29%5Ccirclearrowleft30%5E%7B%5Ccirc%7D%3D2%5Cangle60%5E%7B%5Ccirc%7D.%5Ctag%7B5.4.3.10%7D)
> 变成复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B%5Csqrt%7B3%7D%5Ccdot+i) 之后再拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍： ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto%2B%7D%7D%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5C%2C2%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%7D%5C%2C+2%5Cright%29%3D%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E%7B%2B%7D%7D2%3D2.%5Ctag%7B5.4.3.11%7D) ![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B%2B%5Cto%2B%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow%5Cleft%28%5Csqrt%7B3%7D%5C%2C%7B%5Cblacklozenge%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow%5C%2C2%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow%5Cleft%28%5Csqrt%7B3%7D%5C%2C%7B%5Cblacklozenge%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%7B%5Cblacktriangle%5E%7B%2B%7D%7D%5Cuparrow2%5Csqrt+3%3D2%5Csqrt+3.%5Ctag%7B5.4.3.12%7D)
> 最后得到结果 ![[公式]](https://www.zhihu.com/equation?tex=2%2B2%5Ccdot%5Csqrt%7B3%7D%5Ccdot+i) 。

在之前的讨论中，我们知道 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta%5Cupdownarrow%7D) ![[公式]](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cupdownarrow%7D%5Cright%29) 与 ![[公式]](https://www.zhihu.com/equation?tex=p_%7B%5Ccirclearrowleft%7D) 都是双射的，则他们的复合 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 也是双射的。于是，当两个 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 之间可以复合时，复合的结果自然也是双射的。所以我们需要重点讨论的是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 的可复合性。现在设：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_%7Ba%7D%3A%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Ca%7D%5Cright%29%2C%5Cquad+%5Cpsi_%7Bb%7D%3A%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D%5Cright%29.%5Ctag%7B5.4.3.13%7D)

我们可以将复合 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_a%5Ccirc%5Cpsi_b) 写为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_a%5Ccirc%5Cpsi_b%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc%5C%2C+p_%7B%5Ccirclearrowleft%2Ca%7D%5Cright%29%5Ccirc%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D%5Cright%29.%5Ctag%7B5.4.3.14%7D)

复合的有效性取决于 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D) 与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D) 复合的合法性。为了保证两个非零复数的正实数倍拉长复合的合法性，我们***必须要留意的是做完\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D) ***之后非零复数所处的位置\***，***然后再根据位置从前述的八种情况中选出对应的一种\*** ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D) ***进行复合\*** 。在 ![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc+%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D) 无效时我们定义：

![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi_a%5Ccirc%5Cpsi_b%3D%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Ca%7D%5Cupdownarrow%7D%5Ccirc%5C%2C+p_%7B%5Ccirclearrowleft%2Ca%7D%5Cright%29%5Ccirc%5Cleft%28%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D%5Cright%29%3A%3D%5Cunderset%7B%5Cleftrightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%2Cb%7D%5Cupdownarrow%7D%5Ccirc+%5C%2Cp_%7B%5Ccirclearrowleft%2Cb%7D.%5Ctag%7B5.4.3.15%7D)

即保持复合之前的旋转伸缩，这一定义与非零实数的非零实数倍拉长的无效复合的定义是类似的。并且由合法复合与非合法复合的定义我们保证了 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpsi) 对复合运算是封闭的。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B5.4.4%7D) **站在群的角度上来理解代数运算**

在这之前我们已经做足了铺垫，现在我们可以站在群的角度上来理解代数运算了。整数和有理数我们就不再讨论了。我们只讨论实数与复数。首先我们先给出结论：

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7B%5Ccolor%7Bred%7D%7BTheorem%5Cquad+5.4.1%3A%7D%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bi%29.%7D+) 实数的滑动对应于实数的加法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bii%29.%7D+) 非零实数的非零实数倍伸缩对应于非零实数的乘法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D+) 复数的滑动对应于复数的加法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%29.%7D+) 非零复数的纯伸缩对应于非零复数与非零实数的乘法；

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D+) 非零复数的旋转伸缩对应于非零复数与非零复数的乘法。

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bred%7D%7B%5Clarge%5Cblacksquare%7D)

> ![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%7B%5Cbm%7B%5Crm%7BRemark%3A%7D%7D%7D) 这里我们没有为复数的纯旋转找到对应关系。这一关系我们将在下一节中补上。

下面我就仅对 ![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%7D%29%5Csim%5Crm%7Bv%7D%29) 各举一个例子。

![[公式]](https://www.zhihu.com/equation?tex=%5Clarge%5Cbm%7B%5Crm%7B%5Ccolor%7BGreen%7D%7BExample%5Cquad+5.4.1%3A%7D%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biii%29.%7D) 对于复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，给它加上另一个复数 ![[公式]](https://www.zhihu.com/equation?tex=3%2B4%5Ccdot+i) 得到 ![[公式]](https://www.zhihu.com/equation?tex=4%2B6%5Ccdot+i) 。这相当于对复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) 做了一个右上滑动，即：

![[公式]](https://www.zhihu.com/equation?tex=w%5Cnearrow%3A%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%2C%5Cmu%5Cuparrow%5Cright%29%5Cmapsto+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7Bu%7D%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%28%5Cmu%5Cuparrow%5Cright%29%3D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cdiamondsuit%7D%5C%2C+3+%5Cright%29%5C%2C%5Cheartsuit%5C%2C%5Cleft%282%5C%2C%7B%5Cdiamondsuit%7D%5Cuparrow%5C%2C4%5Cright%29.%5Ctag%7B5.4.4.1%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Biv%7D%29.) 对于复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) ，给它乘上另一个负实数 ![[公式]](https://www.zhihu.com/equation?tex=-3) 得到 ![[公式]](https://www.zhihu.com/equation?tex=-3-6%5Ccdot+i) 。这相当于对复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B2%5Ccdot+i) 做了一个纯负实数倍的拉长，即：

![[公式]](https://www.zhihu.com/equation?tex=%5Cunderset%7B%5Crightarrow%7D%7B%5Cgamma%5E%7B%2B%5Cto-%7D%7D%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%2B%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+%5Cleft%28%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacktriangle%5E-%7D%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%2B%7D%5Cleft%281%5C%2C%5Cunderset%7B%5Crightarrow%7D%7B%5Cblacklozenge%5E%2B%7D%5C%2C+3%5Cright%29%3D%5Cunderset%7B%5Cleftarrow%7D%7B%5Cblacktriangle%5E%2B%7D3%3D-3.%5Ctag%7B5.4.4.2%7D)

![[公式]](https://www.zhihu.com/equation?tex=%7Br%5E%7B%2B%5Cto-%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%2B%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E-%7D%5Cuparrow%5C%2C%28-3%29%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cdownarrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+3%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cdownarrow6%3D-6.%5Ctag%7B5.4.4.3%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bv%29.%7D) 对于复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Csqrt%7B3%7D%2Bi) ，给它乘上另一个复数 ![[公式]](https://www.zhihu.com/equation?tex=1%2B%5Csqrt%7B3%7D%5Ccdot+i) 得到 ![[公式]](https://www.zhihu.com/equation?tex=4%5Ccdot+i) 。这相对于先对复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Csqrt%7B3%7D%2Bi) 做了一个 ![[公式]](https://www.zhihu.com/equation?tex=60%5E%5Ccirc) 的纯旋转：

![[公式]](https://www.zhihu.com/equation?tex=%282%2C30%5E%7B%5Ccirc%7D%29%5Cmapsto%5Cleft%282%5Cangle30%5E%7B%5Ccirc%7D%5Cright%29%5Ccirclearrowleft60%5E%7B%5Ccirc%7D%3D2%5Cangle90%5E%7B%5Ccirc%7D.%5Ctag%7B5.4.4.4%7D)

变成复数 ![[公式]](https://www.zhihu.com/equation?tex=2%5Ccdot+i) 之后再拉长 ![[公式]](https://www.zhihu.com/equation?tex=2) 倍：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7D+%5Cunderset%7B%5Crightarrow%7D%7B%5Cdelta_%7B%5Cmathrm%7BP.D.%7D%7D%5Cuparrow%7D%3D%5Cunderset%7B%5Crightarrow_%7B%5Cmathrm%7Bpas.%7D%7D%7D%7B%5Cdelta%5E%7B%280%2C%2B%29%5Cto%280%2C%2B%29%7D%5Cuparrow%7D%5C%5C+%7Br%5E%7B%2B%5Cto-%7D%7D%5Cuparrow%3D%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow%5Cleft%282+%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+%5Cleft%28%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow%5C%2C2%5Cright%29%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow%5Cleft%282%5C%2C%7B%5Cblacklozenge%5E%2B%7D%5Cuparrow%5C%2C+2%5Cright%29%3D%7B%5Cblacktriangle%5E%2B%7D%5Cuparrow4%3D4.%5Ctag%7B5.4.4.5%7D+%5Cend%7Barray%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Ccolor%7Bgreen%7D%7B%5Clarge%5Cblacksquare%7D)

最后总结一下，如果在群的角度上理解代数运算的话我们实际上是将数字看成了一种作用，通过这种作用可以将原来的数字变成新的数字，所以说代数运算只不过是群作用的一种实际体现。

## ![[公式]](https://www.zhihu.com/equation?tex=%5CLarge%5Cbm%7B6.%7D) 再看群同态与上帝公式和群论的关系

在之前我们看到，以 ![[公式]](https://www.zhihu.com/equation?tex=e) 为底的指数函数的运算律是群同态的一种体现。其实不止以 ![[公式]](https://www.zhihu.com/equation?tex=e) 为底的指数函数，以其他大于零的实数 ![[公式]](https://www.zhihu.com/equation?tex=x) 作为底数的指数函数也是群同态的一种体现。因为我们也有：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Ba%2Bb%7D%3Dx%5Ea%5Ccdot+x%5Eb.%5Ctag%7B6.1%7D)

现在我们假设 ![[公式]](https://www.zhihu.com/equation?tex=a%2C%5C%2Cb%5Cin%5Cmathbb%7BR%7D) ，由于之前我们将实数的加法解释为了实数的滑动，将非零实数的乘法解释为了非零实数的伸缩，并且底数大于零的实指数函数的值域是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D_%7B%3E0%7D) 。于是现在我们可以这样去理解 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Ba%2Bb%7D%3Dx%5Ea%5Ccdot+x%5Eb) ：***我们将实数的滑动\*** ![[公式]](https://www.zhihu.com/equation?tex=%7Ba%2Bb%7D) ***作为输入，得到的是正实数的伸缩\*** 。这为我们提供了指数函数运算律的另一种理解方式。

那么基于这种理解方式，我们自然能想到是的：***以其他大于零的实数\*** ![[公式]](https://www.zhihu.com/equation?tex=x) ***作为底数的指数函数，当输入为复数的滑动时，输出的应是非零复数的旋转伸缩\*** 。那么这个结论是否正确呢？下面我们就来简单讨论一下。

不妨设：

![[公式]](https://www.zhihu.com/equation?tex=a%3A%3D%5Calpha%2B%5Cbeta%5Ccdot+i%2C%5C%2C%5C%2Cb%3A%3D%5Cgamma%2B%5Cdelta%5Ccdot+i%2C%5Cquad+%5Calpha%2C%5C%2C%5Cbeta%2C%5C%2C%5Cgamma%2C%5C%2C%5Cdelta%5Cin%5Cmathbb%7BR%7D.%5Ctag%7B6.2%7D)

则：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Ba%2Bb%7D%3Dx%5E%7B%28%5Calpha%2B%5Cbeta%5Ccdot+i%29%2B%28%5Cgamma%2B%5Cdelta%5Ccdot+i%29%7D%3Dx%5E%7B%28%5Calpha%2B%5Cgamma%29%2Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3Dx%5E%7B%28%5Calpha%2B%5Cgamma%29%7D%5Ccdot+x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D.%5Ctag%7B6.3%7D)

由于 ![[公式]](https://www.zhihu.com/equation?tex=x%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5C%2C%5Calpha%2C%5C%2C%5Cgamma%5Cin%5Cmathbb%7BR%7D) ，所以 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7B%28%5Calpha%2B%5Cgamma%29%7D%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D) ，进而 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7B%28%5Calpha%2B%5Cgamma%29%7D) 起到的是纯伸缩的作用。那么现在的问题是为什么 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D) 起到的是纯旋转的作用呢？一种比较简单的解释方式是：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3D%5Cexp%5Cleft%28%5Cln%5Cleft%28x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cright%29%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cright%29.%5Ctag%7B6.4%7D)

由于 ![[公式]](https://www.zhihu.com/equation?tex=x%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D%2C%5C%2C%5Cbeta%2C%5C%2C%5Cdelta%5Cin%5Cmathbb%7BR%7D) ，所以 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cin%5Cmathbb%7BR%7D_%7B%3E0%7D) ，进而 ![[公式]](https://www.zhihu.com/equation?tex=+%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cin%5Cmathbb%7BR%7D) 。现在我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29) 定义为 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta) ，则：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28x%5E%7B%28%5Cbeta%2B%5Cdelta%29%7D%5Cright%29%5Cright%29%3D%5Cexp%5Cleft%28i%5Ccdot%5Ctheta%5Cright%29.%5Ctag%7B6.5%7D)

这就说明了 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D) 总是一个长度为 ![[公式]](https://www.zhihu.com/equation?tex=1) 的复数。所以它起到是复平面上的纯旋转作用。并且我们看到，以***任意一个大于零的实数\*** ![[公式]](https://www.zhihu.com/equation?tex=x) ***为底的指数函数将虚轴映射为复平面上的单位圆\*** 。也就是说给定一个非零复数，给它乘以一个 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28i%5Ccdot%5Ctheta%29) 相当于使该复数纯旋转了角度 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctheta) 。于是我们的又一个结论是(补 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbm%7B%5Crm%7BTheorem%5Cquad+5.4.1%7D%7D) 中的复数的纯旋转找到对应关系)：

![[公式]](https://www.zhihu.com/equation?tex=%5Crm%7Bvi%29.%7D) 非零复数的纯旋转对应于非零复数与复数 ![[公式]](https://www.zhihu.com/equation?tex=%5Cexp%28i%5Ccdot%5Ctheta%29) 的乘法。

现在让我们再看到 ![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D) ，现在我们将 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbeta%2B%5Cdelta) 定义为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi%5Cin%5Cmathbb%7BR%7D) 。则：

![[公式]](https://www.zhihu.com/equation?tex=x%5E%7Bi%5Ccdot%28%5Cbeta%2B%5Cdelta%29%7D%3Dx%5E%7Bi%5Ccdot%5Cxi%7D%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28x%5E%7B%5Cxi%7D%5Cright%29%5Cright%29.%5Ctag%7B6.6%7D)

就是说我们对以任意一个大于零的实数 ![[公式]](https://www.zhihu.com/equation?tex=x) 为底的指数函数的指数上放置一个纯虚数 ![[公式]](https://www.zhihu.com/equation?tex=i%5Ccdot%5Cxi) ，相当于在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动了角度 ![[公式]](https://www.zhihu.com/equation?tex=%5Cln%5Cleft%28x%5E%7B%5Cxi%7D%5Cright%29) ，其在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的弧长也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cln%5Cleft%28x%5E%7B%5Cxi%7D%5Cright%29) 。则当 ![[公式]](https://www.zhihu.com/equation?tex=x%3De) 时有：

![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ccdot%5Cxi%7D%3D%5Cexp%5Cleft%28i%5Ccdot%5Cln%5Cleft%28e%5E%7B%5Cxi%7D%5Cright%29%5Cright%29%3D%5Cexp%28i%5Ccdot+%5Cxi%29.%5Ctag%7B6.7%7D)

也就是说以 ![[公式]](https://www.zhihu.com/equation?tex=e) 为底的指数函数的特殊之处在于，当其指数为 ![[公式]](https://www.zhihu.com/equation?tex=i%5Ccdot%5Cxi) 时，其在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的角度恰好也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi) ，并且在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的弧长也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi) 。更为特殊的，当 ![[公式]](https://www.zhihu.com/equation?tex=%5Cxi%3D%5Cpi) 时， ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ccdot%5Cpi%7D) 表示的是：在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的角度为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi%5Coverset%7B%5Ctriangle%7D%7B%3D%7D180%5E%7B%5Ccirc%7D) ，并且在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动的弧长也是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi) ，而在单位圆上从 ![[公式]](https://www.zhihu.com/equation?tex=0%5E%7B%5Ccirc%7D) 开始转动弧长 ![[公式]](https://www.zhihu.com/equation?tex=%5Cpi) 后到达的点是 ![[公式]](https://www.zhihu.com/equation?tex=%28-1%2C0%5Ccdot+i%29) 。因此，在这种意义上我们有：

![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bi%5Ccdot%5Cpi%7D%3D-1.%5Ctag%7B6.8%7D)

------



## 参考

1. [^](https://zhuanlan.zhihu.com/p/303377401#ref_1_0)Euler's formula with introductory group theory https://www.youtube.com/watch?v=mvmuCPvRoWQ

1. [^](https://zhuanlan.zhihu.com/p/303377401#ref_2_0)奶牛快传链接 https://cowtransfer.com/s/2d0ff5dfa6d743

编辑于 2020-11-28

精选评论（1）

- [![饭饭](https://pic1.zhimg.com/3e575891324fab002732cb9e614172b5_s.jpg?source=06d4cd63)](https://www.zhihu.com/people/fanrongboy)[饭饭](https://www.zhihu.com/people/fanrongboy)2020-12-13

  本来都截图并标注，把原文里的一些笔误给画出来了，无奈知乎无法发图，只好用公式序号标记上下来定位了，公式太多，检查的不是很仔细，应该有不少遗漏，暂提交这些：

  1、（3.6）后面的Remark，xi=gi是不是写反了，应为gi=xi，和下面符号对应上

  2、（4.1.13）上面：综合以上三条，我们现在可以说映射 [公式] (或者映射 [公式] )是一个从集合 [公式] 到自身上的一个双射。//集合的名字怎么和映射一样？

  3、（4.1.13）下面：其实定义了这样一个映射 [公式] 之后我们就得到了关于 [公式] 的全部置换了。也就是说将来我们就不再区分 [公式] 和 [公式] 了。//为什么不区分？这不是两种不同的置换或者说映射吗？怎么能用同一个字母表示？

  4、（5.2.1.4）下面：同理可定义 正有理数集上的一个收缩 为：//下面的配图错误，用的还是拉伸的公式图片，看图片序号为5.2.1.3和前面重复了

  5、（5.2.1.6）上面：如果我们只观察负有理数 1 的话，//这里应该是-1

  6、（5.2.1.7）此处公式里括号中应该是-1，-2，-3才对

  7、（5.2.1.8）下面：这样我们就可以定义 负有理数集上的一个拉长 为：//下部的配图的有误，应该是5.2.1.9的图，却用了5.2.1.8的图。同时5.2.1.8这个公式图也有错误，括号里面不应该是-1、-2、-3的吗？

  8、（5.2.2.1）然后我们在有理数 [公式] 处放上一面镜子(平面镜)，则会在负有理数轴上出现一个点 [公式] //这个点的公式右上角少了一个+号

  9、（5.2.2.13）公式第一个三角符号下面漏了打一个右箭头

  10、（5.2.2.20）上面：最终我们可以将以上八种情况合并为 种：// 漏打了“一”字

  11、（5.2.2.24）上面：正有理数的正有理数倍伸缩不能与负有理数的正有理数倍伸缩复合 //此处配图有疑惑，公式符号和文字描述不对应，应为：++ 。-+ ；还有符合运算到底是从左到右开始还是从右到左计算，看公式似乎默认都是从右到左的？

  12、（5.2.2.24）Remark部分：于是我们便可以将第一次伸缩变换的到达域下一次伸缩变换的定义域做一下比较 //漏打了“与”字

  13、（5.2.2.26）下面：负有理数的正有理数倍拉长与负有理数的正有理数倍拉长互为逆元 //后一个“拉长”应为“收缩”



[zdr0](https://www.zhihu.com/people/97148f897df6540033355be3b742052b) (作者) 回复[饭饭](https://www.zhihu.com/people/3cd021639c1465f84ad127e130d74e38)2020-12-13

首先感谢你认真的读了我的文章并指出了不少问题～下面我对非笔误的问题进行一下回答。

3两种不同的映射可以使用同一字母表示，f=x^3和f=x^5，这两个都是R到R上的映射当然你也可以用不同的
10是没错的
11(5.2.2.24)是也无效复合的一个例子，前面那句话里有“例如”二字，但这个例子与前面那句话无关
