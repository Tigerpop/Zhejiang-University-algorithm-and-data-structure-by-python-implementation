# 多项式求和，   a下标n-1 x上标n-1
# 多项式在给定点x处的值。
import time
# 我自己搞一个装饰器，让函数循环执行这么多次。
def reuse_(num):
    def outer(func):
        def inner(*args):
            for i in range(num):
                result = func(*args)
            return result
        return inner
    return outer

list_x = range(999)

@reuse_(10**3)  # 装饰上方法1。
def f(a,n,x):
    p = 0
    for i in range(n+1):
        p += (a[i]*(x**i))
    return p
start_1 = time.time()
f_value = f(list_x,888,888)
print(f_value)
# 第一种方法 f内一次循环 用i次乘法，一共用n(1+n)/2次乘法。
print('第一种方法运行时间：%d'%(time.time()-start_1))

# 用嵌套的结合律重写上面问题解决。
@reuse_(10**3) # 装饰上方法2。
def ff(a,n,x):
    p = a[n]
    for i in range(n,0,-1):
        p = a[i-1] + x*p
    return p
start_2 = time.time()
ff_value = ff(list_x,888,888)
print(ff_value)
# 第二种方法，ff循环一次用了一次乘法，一共用了n次乘法。
print('第二种方法运行时间：%d'%(time.time()-start_2))


# 第一种方法f 时间复杂度为T(n) = C1 n**2 + C2 n
# 第二种方法ff时间复杂度为T(n) = C n

