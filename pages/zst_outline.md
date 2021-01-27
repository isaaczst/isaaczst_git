---
title: zst_outline
---

## [[thread]]
## Memo: The Outline of Thesis 

The following is the table of content with comments
# 0 Introduction

## 0.1 Backgound
### - Optimal control is the core of modern production
### - CS techniques forged versatile data acquiring capability
### - No more obstacles for optimal control on complexe system
### - But obsacles on 'software'level remain large
## 0.2 Research Motivation
### - Investigate the current paradigms of optimal control paradigms
### - Review the development history and potentional solution of nonlinear optimal control
### - propose an imporved methdology
## 0.3 Research Objective
### - Introduce new concepts for prposed methdology
### - Explore potential of machine learnig techniques for optimal control
- Develop practical control solution
- Provide  mathmetical analysis includes convergence and computation burden, etc.
## 0.4 Research Contribution
### - A new paradigm of optimal control
- A dual frame of optimization of dynamic system
## 0.5 Dissertation Organization



#  1 iterature review

## 1.1 Introduction
### - The classical setting of optimal control
- The history of canonical approach
## 1.2 Optimal control-PDE approaches
### - The variation method background
- The model based approach
- The methods relates to Lapunov and Riccati equation
- The approximation solution, such as LMI, etc
- The variant of predictive control (MPC)
## 1.3 Dynamic Programming - Reinforcement Learning approaches
### - The data based approach
- The methods based on discrete variable space
- The dynamic programming on linear system: LQR
- Reinforcement learning and Adaptive dyamic programming
## 1.4 Motivation from 'Curse of Dimension'
### - Current approaches to balance 'dynamic uncertainty'and 'variable discreteness'
- Motivated from machine learning theory development
#  2 theory background

## 2.1 classical optimal control thoery
### - Optimization and optimal control
- Theoritical solution on Lagrange form
- Co-state and Hamiltonian apporach
## 2.2 data driven adaptive dynamic programming
### - Dynamic programming
- Reinforcement learning
- 'off-policy'and 'on-policy'searching
- Q-learning
## 2.3 solutions for high dimension system
### - Discretization and local linerlization
- 'upwind'and 'gowind'format
## 2.4 challenging to current paradigm
### - Markov Process
- EM algorithm and aynchronism optimization
- theory of Support Vector Machine
# 3 EM algorithm of QR task

## 3.1 Introduction of Criterion Function
### - Introduce '(optimal) trajectory state'
- Introduce 'generlized dynamic programming'
- Introduce criterion function
## 3.2 Optimal control via criterion function
### - Optimal action algorithm in LQR
- Optimal action algorithm in Q-learning
- Relation of optimal action and 'trajectory state'
- Criterion function is the implicit form of policy function
## 3.3 EM algorithm of searching optimal policy
### - Algorithm 
- Pseudocode
## 3.4 Convergence of proposed algorithm
### - Duality of criterion function model and optimal trajectory measurement
- Asynchronism vs. Gradient Descent Methods
- Proof on the base of contraction mapping
# 4 Simulation and test
## 4.1 Low dimension case: MegLev
### - step task
- Discretion
- more ...
## 4.2 Low dimension case: Piecewise Linear system
### - two-piece setting
- data and accuracy
- convergence checking
- computation burden analysing
## 4.3 High dimension case: 2 link inverted pendulum
### -
## 4.4 High dimension case: UAV (to be determined)
### -
# 5 Discussion

## 5.1 Discover the topology feature of optimal policy
### - Introduce the criterion function enables the usuage of 'first priciple'knowledge
- Duality of optimal criterion and optimal action enables the modelling of topology feature 
- Introduce of SVM enables feature apporixmation in low-dimension space
## 5.2 Advantage on state space feature approximation
### - The paradigm combines the adjustment of sampling domain (for criterion function model learning) and the modeling iteration
- Learning computation burden is limited
## 5.3 'Grey box'nature of EM paradigm
### - 'First principle'knowldege is introduced via Riccation equation
- The network of the agent is 'shallow'vs. deep neuron network paradigm
- Verification of safty and reliability is available since SVM kernels maps to variation method.
## 5.4 Trade-off of the algorithm generalization and cost of learning
### - Trade-off of generalization matches the potential applications in the future
- Interface is operator-friendly in both acadmy and industry communities
## 5.5 Development potentional
### - The realtion to inverted reinforcement learning problem
- etc.
## 5.6 Future work
### - Industrial practice and verification
- Computation efficiency, etc.


---
# 脉络







​
