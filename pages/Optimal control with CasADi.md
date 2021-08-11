- https://web.casadi.org/docs/#document-ocp
- CasADi can be used to solve optimal control problems (OCP) using a variety of methods, including direct (a.k.a. discretize-then-optimize) and indirect (a.k.a. optimize-then-discretize) methods, all-at-once (e.g. collocation) methods and shooting-methods requiring embedded solvers of initial value problems in ODE or DAE.
- As a user, you are in general expected to write your own OCP solver and CasADi aims as making this as easy as possible by providing powerful high-level building blocks.
- Since you are writing the solver yourself (rather than calling an existing “black-box” solver), a basic understanding of how to solve OCPs is indispensable.
- Good, self-contained introductions to numerical optimal control can be found in the recent textbooks by  [Lorenz T. Biegler, Nonlinear Programming: Concepts, Algorithms, and Applications to Chemical Processes , SIAM 2010]
   or [John T. Betts, Practical Methods for Optimal Control Using Nonlinear Programming , SIAM 2001] 
  [2] or Moritz Diehl’s lecture notes on numerical optimal control. https://www.syscop.de/files/2015ws/numopt/numopt_0.pdf
## 8.1. A simple test problem
- To illustrate some of the methods, we will consider the following test problem, namely driving a Van der Pol oscillator to the origin, while trying to minimize a quadratic cost:
-
- with T=10.
- In CasADi’s examples collection [3], you find codes for solving optimal control problems using a variety of different methods.
- In the following, we will discuss three of the most important methods, namely direct single shooting, direct multiple shooting and direct collocation.
### 8.1.1. Direct single-shooting
- In the direct single shooting method, the control trajectory is parameterized using some piecewise smooth approximation, typically piecewise constant.
- Using an explicit expression for the controls, we can then eliminate the whole state trajectory from the optimization problem, ending up with an NLP in only the discretized controls.
- In CasADi’s examples collection, you will find the codes direct_single_shooting.py and direct_single_shooting.m for Python and MATLAB/Octave, respectively. These codes implement the direct single shooting method and solves it with IPOPT, relying on CasADi to calculate derivatives. To obtain the discrete time dynamics from the continuous time dynamics, a simple fixed-step Runge-Kutta 4 (RK4) integrator is implemented using CasADi symbolics. Simple integrator codes like these are often useful in the context of optimal control, but care must be taken so that they accurately solve the initial-value problem.
- The code also shows how the RK4 scheme can be replaced by a more advanced integrator, namely the CVODES integrator from the SUNDIALS suite, which implements a variable stepsize, variable order backward differentiation formula (BDF) scheme. An advanced integrator like this is useful for larger systems, systems with stiff dynamics, for DAEs and for checking a simpler scheme for consistency.
- 8.1.2. Direct multiple-shooting¶
  The direct_multiple_shooting.py and direct_multiple_shooting.m codes, also in CasADi’s examples collection, implement the direct multiple shooting method. This is very similar to the direct single shooting method, but includes the state at certain shooting nodes as decision variables in the NLP and includes equality constraints to ensure continuity of the trajectory.
- The direct multiple shooting method is often superior to the direct single shooting method, since “lifting” the problem to a higher dimension is known to often improve convergence. The user is also able to initialize with a known guess for the state trajectory.
- The drawback is that the NLP solved gets much larger, although this is often compensated by the fact that it is also much sparser.
- 8.1.3. Direct collocation¶
  Finally, the direct_collocation.py and direct_collocation.m codes implement the direct collocation method. In this case, a parameterization of the entire state trajectory, as piecewise low-order polynomials, are included as decision variables in the NLP. This removes the need for the formulation of the discrete time dynamics completely.
- The NLP in direct collocation is even larger than that in direct multiple shooting, but is also even sparser.