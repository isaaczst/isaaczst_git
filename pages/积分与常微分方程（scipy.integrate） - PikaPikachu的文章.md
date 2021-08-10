- 2 积分与常微分方程（scipy.integrate） - PikaPikachu的文章 - 知乎
  https://zhuanlan.zhihu.com/p/367067235
-
- 2 常微分方程
	- 1.给出初始条件的情况
	- SciPy提供了有力的常微分方程求解工具，即函数integrate.solve_ivp
	- 该函数用于解决形如下式的ODE：
	- ![](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cmathrm+d%5Cbold+y%7D%7B%5Cmathrm+dt%7D%3Df%28t%2C%5Cbold+y%29%2C%5C+%5Cbold+y%28t_0%29%3D%5Cbold+y_0%5C%5C)
	- 这里的y可以为标量也可以为矢量。
	- 函数的具体形式为：