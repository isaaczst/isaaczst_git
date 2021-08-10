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
		- ```integrate.solve_ivp(f,(t_0,t_1),y_0,method='RK45',dense_output=False)```
		- f即上式左侧的函数，(t_0, t_1)为参数t的范围，y0为初值条件。method='RK45'为选择的方法，默认为5（4）阶龙格库塔法。dense_output选择的是是否稠密输出，这个主要是画图的时候需要，默认为否。
		- 以解下列方程为例：
		- ![公式](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cmathrm+dy%7D%7B%5Cmathrm+dt%7D%3Dy%5Csin+t%5C%5C)
		- 其解析解为：
		- ![](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cmathrm+dy%7D%7B%5Cmathrm+dt%7D%3Dy%5Csin+t%5CRightarrow%5Cfrac%7B%5Cmathrm+dy%7D%7By%7D%3D%5Csin+t%5Cmathrm+dt%5CRightarrow%5Cln+y%3DC-%5Ccos+t%5C%5C%5CRightarrow+y%3De%5E%7BC-%5Ccos+t%7D%5CRightarrow+y%3DCe%5E%7B-%5Ccos+t%7D%5C%5C)
		- integrate.solve_ivp中的method的可选参数还有很多，包括：
		- 参数	方法
		  'RK23'	显式2(3)阶龙格库塔法
		  'DOP853'	显式8阶龙格库塔法
		  'Radau'	隐式5阶龙格库塔法
		  'BDF'	向后微分公式法
		-
	- 2.给出边界条件的情况
		- SciPy中的函数integrate.solve_bvp用来求解下列形式的常微分方程（组）：
		- [公式]
	- 其中bc表示boundary condition，即边界条件。
	- 上式中，x是一个一维自变量，y(x)是一个n维向量值函数，p是一个k维未知向量，为了上述方程能被解决，需要n+k个边界条件，也就是函数bc必须是n+k维的。
	- 函数的具体形式和参数为：
	- integrate.solve_bvp(f,bc,x,y,p=None,S=None)
	  在本文中，我们不介绍方程左侧的 [公式] 项，这个主要是用来解决方程的奇异点问题。
	- 下面举例说明该函数的用法，为求解波动方程：
	- [公式]
	- 该方程的解析解为： [公式]