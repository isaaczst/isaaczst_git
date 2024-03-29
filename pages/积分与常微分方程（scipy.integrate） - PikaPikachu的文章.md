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
		- [](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cmathrm+d%5Cbold+y%7D%7B%5Cmathrm+dx%7D%3Df%28x%2C%5Cbold+y%2Cp%29%2BS%5Cfrac%7By%7D%7Bx-a%7D%2C%5Cquad+a%5Cle+x%5Cle+b%5C%5C+%5Ctext%7Bbc%7D%28%5Cbold+y%28a%29%2C%5Cbold+y%28b%29%2Cp%29%3D0%5C%5C)
		- 其中bc表示boundary condition，即边界条件。
		- 上式中，x是一个一维自变量，y(x)是一个n维向量值函数，p是一个k维未知向量，为了上述方程能被解决，需要n+k个边界条件，也就是函数bc必须是n+k维的。
		- 函数的具体形式和参数为：
		- `integrate.solve_bvp(f,bc,x,y,p=None,S=None)`
		  在本文中，我们不介绍方程左侧的 ![公式](https://www.zhihu.com/equation?tex=S%5Cfrac%7By%7D%7Bx-a%7D) 项，这个主要是用来解决方程的奇异点问题。
		- 下面举例说明该函数的用法，为求解波动方程：
		- [](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cmathrm+d%5E2y%7D%7B%5Cmathrm+dx%5E2%7D%2Bk%5E2y%3D0%5C%5C+y%280%29%3Dy%281%29%3D0%5C%5C+y%27%280%29%3Dk%5C%5C)
		- 该方程的解析解为： [](https://www.zhihu.com/equation?tex=y%3D%5Csin+kx%2C%5Cquad+k%3Dn%5Cpi%2C%5Cquad+n%5Cin%5Cmathbb%7BZ%7D)
		-
		-
		- def f(x,y,p):
		    k=p[0]
		    return np.vstack((y[1],-k**2*y[0]))
		- def bc(y_a,y_b,p):
		    k=p[0]
		    return np.array([y_a[0],y_b[0],y_a[1]-k])
		- x=np.linspace(0,1,5)
		  y=np.zeros((2,x.size))
		  y[0,1]=1
		  y[0,3]=-1
		  result=integrate.solve_bvp(f,bc,x,y,p=[6])
		  x_plot=np.linspace(0,1,1000)
		  y_plot=result.sol(x_plot)[0]
		  plt.plot(x_plot,y_plot)
		  plt.grid()
		  plt.xlabel('x')
		  plt.ylabel('y')
		  plt.show()