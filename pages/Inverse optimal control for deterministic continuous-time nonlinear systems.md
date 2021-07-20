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
	  predicted and observed trajectories. This method is
	  applied to develop a model of human goal-oriented
	  locomotion in the plane (i.e. paths taken during goaloriented walking tasks) using observations from motion
	  capture, and implement the model on a humanoid robot.