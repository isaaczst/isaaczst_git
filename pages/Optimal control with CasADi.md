- https://web.casadi.org/docs/#document-ocp
- CasADi can be used to solve optimal control problems (OCP) using a variety of methods, including direct (a.k.a. discretize-then-optimize) and indirect (a.k.a. optimize-then-discretize) methods, all-at-once (e.g. collocation) methods and shooting-methods requiring embedded solvers of initial value problems in ODE or DAE.
- As a user, you are in general expected to write your own OCP solver and CasADi aims as making this as easy as possible by providing powerful high-level building blocks.
- Since you are writing the solver yourself (rather than calling an existing “black-box” solver), a basic understanding of how to solve OCPs is indispensable. Good, self-contained introductions to numerical optimal control can be found in the recent textbooks by Biegler
  [1] or Betts
  [2] or Moritz Diehl’s lecture notes on numerical optimal control.