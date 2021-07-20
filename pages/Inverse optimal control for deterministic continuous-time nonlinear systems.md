# Abstract:
	- Inverse optimal control is the problem of computing a cost function with respect to which observed state and input trajectories are optimal.
	- We present a new method of inverse optimal control based on minimizing the extent to which observed trajectories violate first-order necessary conditions for optimality.
	- We consider continuous-time deterministic optimal control systems with ^^a cost function that is a linear combination of known basis functions^^.
	- We compare our approach with three prior methods of inverse optimal control.
	- We demonstrate the performance of these methods by performing simulation experiments using a collection of nominal system models.
	- We compare the robustness of these methods by analysing how they perform under perturbations to the system.
	- To this purpose, we consider two scenarios: one in which we exactly know the set of basis functions in the cost function, and another in which the true cost function contains an unknown perturbation.
	- Results from simulation experiments show that our new method is more computationally efficient than prior methods, performs similarly to prior approaches under large perturbations to the system, and better learns the true cost function under small perturbations.
# I. INTRODUCTION
	- In the problem of optimal control we are asked to find input and state trajectories that minimize a given cost function.
	- In the problem of inverse optimal control we are asked to find a cost function with respect to which observed input and state trajectories are optimal.
	- Methods of inverse optimal control are beginning to find widespread application in robotics.
	- In this paper, we consider this problem under deterministic continuous-time nonlinear systems and cost functions modeled by a linear combination of known basis functions.
	- Three existing methods which solve this problem are the following:
- The max-margin inverse reinforcement learning method of Abbeel and Ng [1].
	- This method is motivated by the problem of efficiently automating vehicle navigation tasks which currently require human expert operation.
	- This method works by trying to learn a cost function that, when minimized, yields a trajectory with similar features as the expert.
	- This method recently contributed to a framework which enables autonomous helicopter aerobatic flight based on observations of human expert pilots.
- The maximum-margin planning method of Ratliff, et al.[2].
	- This method shares the motivation of Abbeel and Ng, and works by minimizing a regularized risk function using an incremental subgradient method.
	- This method contributed to a framework which mimics human driving of an autonomous mobile robot in complex off-road terrain
- The method of Mombaur, et al. which we will call bilevel inverse optimal control [3].
	- This work is motivated by the problem of generating humanoid robot behavior which is similar to natural human motion.
	- This method works by minimizing the sum squared error between
	  predicted and observed trajectories.
	- This method is applied to develop a model of human goal-oriented
	  locomotion in the plane (i.e. paths taken during goaloriented walking tasks) using observations from motion capture, and implement the model on a humanoid robot.
- Despite differences in how learning is performed, these methods share common structure.
	- One goal of this paper is to explain this common structure and compare these methods on a set of example problems.
	- One common component to these algorithms is particularly important.
	- Each method contains an inner loop which computes a predicted trajectory by minimizing a candidate cost function.
	- In other words, each method solves a forward optimal control problem repeatedly in an inner loop.
	- This can often lead to a computational bottleneck.
	- The other goal of this paper is to develop an approach which does not solve a forward optimal control problem repeatedly in an inner loop.
	- ^^Our method, inspired by ideas from inverse optimization in [4], makes the assumption that observations may arise from a system which is only approximately optimal.^^
	- We define how optimal a trajectory is based on how closely it satisfies necessary conditions for optimal control.
	- This assumption allows us to define residual functions based on these necessary conditions which, when minimized over the unknown parameters, yields a solution which makes the observations most optimal.
	- As we will show, this new approach reduces to solving a matrix Riccati differential equation followed by one least-squares minimization.
	- CN
	  - 尽管学习的方式有所不同，但这些方法具有共同的结构。 
	  - 本文的一个目标是解释这种通用结构，并在一组示例问题上比较这些方法。 这些算法的一个共同组成部分尤为重要。 每个方法都包含一个内部循环，它通过最小化候选成本函数来计算预测轨迹。 换句话说，每种方法在内循环中重复解决前向最优控制问题。 这通常会导致计算瓶颈。 本文的另一个目标是开发一种不会在内环中重复解决前向最优控制问题的方法。 我们的方法受到 [4] 中逆优化思想的启发，假设观测值可能来自仅近似最优的系统。 我们根据轨迹满足最优控制的必要条件的程度来定义轨迹的最优程度。 这个假设允许我们根据这些必要条件定义残差函数，当在未知参数上最小化时，产生一个使观测值最佳的解决方案。 正如我们将展示的，这种新方法简化为求解矩阵 Riccati 微分方程，然后进行最小二乘最小化。
- It is unclear at this point how all of these methods compare in terms of prediction accuracy, computational complexity and robustness to system perturbations.
	- In this paper, we explore the performance of these methods using three example systems:
	- (1) linear quadratic regulation,
	- (2) quadratic regulation of a kinematic unicycle, and
	- (3) calibration of an elastic rod.
	- We compare the robustness of these methods by analysing how they perform under perturbations to the system.
	- To this purpose, we consider two scenarios: one in which we exactly know the set of basis functions in the cost function, and another in which the true cost function contains an unknown perturbation.
	- Results from simulation experiments show that our new method is more computationally efficient than prior methods, performs similarly to prior approaches under large perturbations to the system, and better learns the true cost function under small perturbations
	- CN
	  - 目前尚不清楚所有这些方法在预测精度、计算复杂性和对系统扰动的鲁棒性方面的比较。 在本文中，我们使用三个示例系统探索这些方法的性能：（1）线性二次调节，（2）运动学独轮车的二次调节，以及（3）弹性杆的校准。 我们通过分析它们在系统扰动下的表现来比较这些方法的稳健性。 为此，我们考虑两种情况：一种是我们确切知道成本函数中的基函数集，另一种是真实成本函数包含未知扰动。 仿真实验结果表明，我们的新方法比现有方法计算效率更高，在对系统的大扰动下与现有方法相似，并且在小扰动下更好地学习真实成本函数
- The rest of the paper proceeds as follows.
	- In Section II we discuss related work and note the variety of problems to which inverse optimal control and related methods are applied.
	- In Section III we describe the class of systems we consider, and the associated inverse optimal control problem.
	- In Section IV we describe the existing methods of inverse optimal control with which we compare our new method [1]–[3].
	- In Section V we develop our new method based on necessary conditions for optimal control.
	- In Section VI we describe simulation experiments,and Section VII presents results and discussion.
	- e
	  - 本文的其余部分如下。 在第二节中，我们讨论了相关工作，并注意到逆优化控制和相关方法所应用的各种问题。 在第三节中，我们描述了我们考虑的系统类别，以及相关的逆最优控制问题。
	     在第四节中，我们描述了逆向最优控制的现有方法，并与我们的新方法 [1]-[3] 进行了比较。 在第五节中，我们根据最优控制的必要条件开发了我们的新方法。 在第六节中，我们描述了模拟 e
-
# II. RELATED WORK
- Inverse optimal control is often used as a solution approach to the broad problem of learning from demonstration, which is often referred to as imitation learning or apprenticeship learning.
	- The problem of learning from demonstration is to derive a control policy (a mapping from states to actions) from examples, or demonstrations, provided by a teacher.
	- Demonstrations are typically considered to be sequences of state-action pairs recorded during the teacher’s demonstration
	- CN
	  - 逆最优控制通常被用作解决从示范中学习的广泛问题的方法，这通常被称为模仿学习或学徒学习。 从演示中学习的问题是从教师提供的示例或演示中导出控制策略（从状态到动作的映射）。
	    演示通常被认为是教师演示期间记录的状态-动作对序列
- There are generally two methods of approach within learning from demonstration.
	- One approach is to learn a map from states to actions using classification or regression.
	- Argall, et al. provide a survey of the work in this area [5].
	- The second general approach is to learn a cost function with respect to which observed input and state trajectories are (approximately) optimal, i.e. inverse optimal control [1]–[4], [6]–[21].
	- These methods have primarily focused on finite-dimensional optimization and stochastic optimal control problems
	- CN 
	  - 从示范中学习通常有两种方法。 一种方法是使用分类或回归来学习从状态到动作的映射。
	    阿加尔等人。 提供对该领域工作的调查[5]。
	    第二种通用​​方法是学习一个代价函数，关于观察到的输入和状态轨迹是（近似）最优的，即逆最优控制 [1]-[4]，[6]-[21]。 这些方法主要集中在有限维优化和随机最优控制问题上
- In the context of finite parameter optimization, Keshavarz, et al. [4] develop an inverse optimization method which learns the value function of a discrete-time stochastic control system given observations.
	- These ideas were extended to learn a cost function for a deterministic discrete-time system in Puydupin-Jamin, et al. [6], and a hybrid dynamical system in [22].
	- Similarly, Terekhov, et al. [7], [8] and Park, et al.
	  [9] develop an inverse optimization method for deterministic finite-dimensional optimization problems with additive cost functions and linear constraints.
	- Other recent work formulates an optimization problem which simultaneously learns a cost function and optimal trajectories [23], [24].
	- cn
	  - 在有限参数优化的背景下，Keshavarz 等人。  [4] 开发了一种逆优化方法，该方法可以学习给定观测值的离散时间随机控制系统的值函数。 这些想法在 Puydupin-Jamin 等人中被扩展到学习确定性离散时间系统的成本函数。  [6] 和 [22] 中的混合动力系统。 同样，捷列霍夫等人。  [7]、[8] 和 Park 等人。
	     [9] 开发了一种用于具有附加成本函数和线性约束的确定性有限维优化问题的逆优化方法。 最近的其他工作制定了一个优化问题，该问题同时学习成本函数和最佳轨迹 [23]、[24]。
- A variety of methods have been developed in the context of stochastic optimal control problems and, in particular, Markov decision processes [1], [11], [13], [15]–[17], [19], [20].
	- Ng and Russell [11] developed a method for stationary Markov decision processes based on linear programming.
	- Abbeel and Ng [1] extends that work by finding a cost function with respect to which the expert’s cost is less than that of predicted trajectories by a margin.
	- A further extension simultaneously learns the system dynamics along specific trajectories of interest [13].
	- Ramachandran, et al. [16] takes a Bayesian approach and assumes that actions are distributed proportional to the future expected reward.
	- The method developed in Ziebart, et al. [17] works by computing a probability distribution over all possible paths which matches features along the observed trajectory.
	- Dvjijotham and Todorov [19] develop a method of inverse optimal control for linearlysolvable stochastic optimal control problems.
	- Their method takes advantage of the fact that, for the class of system model they consider, the Hamilton-Jacobi-Bellman equation gives an explicit formula for the cost function once the value function is known.
	- Aghasadeghi and Bretl [20] develop a method of inverse optimal control that uses path integrals to create a probability distribution over all possible paths.
	- The problem is then one of maximizing the likelihood of observations.
	- cn
	  - 已经在随机最优控制问题的背景下开发了多种方法，特别是马尔可夫决策过程 [1]、[11]、[13]、[15]-[17]、[19]、[20]  .  Ng 和 Russell [11] 开发了一种基于线性规划的平稳马尔可夫决策过程的方法。
	     Abbeel 和 Ng [1] 通过找到一个成本函数来扩展这项工作，在该函数中，专家的成本比预测轨迹的成本低一点。 进一步的扩展同时学习沿特定感兴趣轨迹的系统动力学 [13]。 拉马钱德兰等人。  [16] 采用贝叶斯方法，并假设行动的分布与未来的预期回报成正比。  Ziebart 等人开发的方法。  [17] 的工作原理是计算所有可能路径上的概率分布，这些路径与沿观察轨迹的特征匹配。  Dvjijotham 和 Todorov [19] 开发了一种用于线性可解随机最优控制问题的逆最优控制方法。 他们的方法利用了这样一个事实：对于他们考虑的系统模型类别，一旦价值函数已知，Hamilton-Jacobi-Bellman 方程就会给出成本函数的明确公式。  Aghasadeghi 和 Bretl [20] 开发了一种逆优化控制方法，该方法使用路径积分来创建所有可能路径的概率分布。
	     那么问题之一是最大化观察的可能性。
-
-
-
-
-