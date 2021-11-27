# 打印0到n 的数字。

import time
# 循环
start_1  = time.time()
def print_n(n):
    for i in range(n):
        print(i+1)
print_n(9)
print('循环用时：%d 秒'%(time.time()-start_1))

# 递归  （容易超过最大深度。）
start_2 = time.time()
def print_N(n):
    if n:
        print_N(n-1)
        print('第%d层递归是%d'%(n,n))
print_N(9)
print('递归用时：%d 秒'%(time.time()-start_2))
