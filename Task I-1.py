from collections import namedtuple
result = namedtuple('result',['x', 'niter','error'])

#Возвращает значение функции
def f(x):
    return x**2-4

#Возвращает значение производной функции
def fder(x):
    return 2*x

def newton_iteration(f, fder, x0, eps=1e-5, maxiter=1000):
    #x_(n-1)
    x_prev=x0
    #x_n
    x_curr=x_prev-f(x_prev)/fder(x_prev)
    niter=0
    while(abs(x_prev-x_curr)>eps and niter<maxiter):
        x_prev=x_curr
        #x_n=x_(n-1)-f(x_(n-1))/fder(x_(n-1))
        x_curr=x_prev-f(x_prev)/fder(x_prev)
        niter+=1
    error=False
    if(niter==maxiter):
        error=True
    return result(x_curr,niter,error)

res=newton_iteration(f,fder,100000)
print("Корень: ",res.x)
print("Количество итераций: ",res.niter)
print("Ошибка: ",res.error)
