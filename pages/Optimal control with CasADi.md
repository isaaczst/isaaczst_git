- https://web.casadi.org/docs/#document-ocp
- CasADi can be used to solve optimal control problems (OCP) using a variety of methods, including direct (a.k.a. discretize-then-optimize) and indirect (a.k.a. optimize-then-discretize) methods, all-at-once (e.g. collocation) methods and shooting-methods requiring embedded solvers of initial value problems in ODE or DAE.
- As a user, you are in general expected to write your own OCP solver and CasADi aims as making this as easy as possible by providing powerful high-level building blocks.
- Since you are writing the solver yourself (rather than calling an existing “black-box” solver), a basic understanding of how to solve OCPs is indispensable.
- Good, self-contained introductions to numerical optimal control can be found in the recent textbooks by  [Lorenz T. Biegler, Nonlinear Programming: Concepts, Algorithms, and Applications to Chemical Processes , SIAM 2010]
   or [John T. Betts, Practical Methods for Optimal Control Using Nonlinear Programming , SIAM 2001] 
  [2] or Moritz Diehl’s lecture notes on numerical optimal control. https://www.syscop.de/files/2015ws/numopt/numopt_0.pdf
## 8.1. A simple test problem
- To illustrate some of the methods, we will consider the following test problem, namely driving a Van der Pol oscillator to the origin, while trying to minimize a quadratic cost: