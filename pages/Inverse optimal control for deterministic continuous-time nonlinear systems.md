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
	- Each method contains an inner loop which computes a predicted trajectory by minimizing a candidate cost function. In other words, each method solves a forward optimal control problem repeatedly in an inner loop. This can often lead to a computational bottleneck. The other goal of this paper is to develop an approach which does not solve a forward optimal control problem repeatedly in an inner loop. Our method, inspired by ideas from inverse optimization in [4], makes the assumption that observations may arise from a system which is only approximately optimal. We define how optimal a trajectory is based on how closely it satisfies necessary conditions for optimal control. This assumption allows us to define residual functions based on these necessary conditions which, when minimized over the unknown parameters, yields a solution which makes the observations most optimal. As we will show, this new approach reduces to solving a matrix Riccati differential equation followed by one least-squares minimization.
	- 尽管学习的方式有所不同，但这些方法具有共同的结构。 本文的一个目标是解释这种通用结构，并在一组示例问题上比较这些方法。 这些算法的一个共同组成部分尤为重要。 每个方法都包含一个内部循环，它通过最小化候选成本函数来计算预测轨迹。 换句话说，每种方法在内循环中重复解决前向最优控制问题。 这通常会导致计算瓶颈。 本文的另一个目标是开发一种不会在内环中重复解决前向最优控制问题的方法。 我们的方法受到 [4] 中逆优化思想的启发，假设观测值可能来自仅近似最优的系统。 我们根据轨迹满足最优控制的必要条件的程度来定义轨迹的最优程度。 这个假设允许我们根据这些必要条件定义残差函数，当在未知参数上最小化时，产生一个使观测值最佳的解决方案。 正如我们将展示的，这种新方法简化为求解矩阵 Riccati 微分方程，然后进行最小二乘最小化。