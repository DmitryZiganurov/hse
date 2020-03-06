import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

#Графики левой и правой части уравнения и производной разности этих функций
x = np.arange(0.6,0.7,0.001)
plt.grid()
plt.plot(x,np.cos(x))
plt.plot(x,np.sqrt(x))
#Корень уравнения приблизительно 0.642
#plt.plot(x,-np.sin(x)-1/(2*np.sqrt(x))) #Производная функции

result = namedtuple('result',['x', 'niter','error'])
def f(x):
    return np.cos(x)-np.sqrt(x)

def newton_iteration(f, x0, alpha, eps=1e-5, maxiter=10000):
    x_prev=x0
    x_curr=x_prev-alpha*f(x_prev)
    niter=0
    while(abs(x_prev-x_curr)>eps and niter<maxiter):
        x_prev=x_curr
        x_curr=x_prev-alpha*f(x_prev)
        niter+=1
    error=False
    if(niter==maxiter):
        error=True
    return result(x_curr,niter,error)

res=newton_iteration(f,0.9,-0.8)
print("Корень: ",res.x)
print("Количество итераций: ",res.niter)
print("Ошибка: ",res.error)


#Зависимость количества интераций от альфа:
#-1.0   7
#-0.9   5
#-0.8   3
#-0.7   6
#-0.6   8
#-0.5   11
#-0.4   14
#-0.3   20
#-0.2   32
#Минимум итераций достигается при альфа примерно равное -0.8. Из графика производной функции можно видеть,
#что она ограничена: ее значение принадлежить промежутку от -1.21 до -1.24 в окрестности корня. Вычисляя альфа-оптимальное,
#можно убедиться в том, что ее значение также примерно -0.8.