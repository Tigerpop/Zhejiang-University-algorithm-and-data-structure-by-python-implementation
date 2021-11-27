'''
希尔排序（插入排序发展而来）：

定义增量序列 Dm > Dm-1 > ... > D1 = 1。
* 对每个Dk 进行 Dk间隔 的排序。
（注意："Dk间隔" 有序的序列，在执行 Dk-1间隔 排序后，仍然是 Dk间隔 有序的。）
* 详解：
    Dk间隔 排序，指的是隔Dk个元素，跳着比大小然后交换，
    然后每隔Dk个元素回头再比大小交换，
    相当于完成一个隔着Dk个元素 完成一次插入 的 插入排序。

'''
import numpy as np
import math
# 原始 希尔排序
def Shell_Sort(A):
    N = len(A)
    # python制作等比数列 不用numpy的话似乎有点麻烦。for(D = N/2,D>0,D/2)就能搞定，python要麻烦一些。
    # D = N/2
    # while D > 0:
    #     * 隔Dk插入排序。
    #     D = D/2
    # 以下相当于左边把N提出来，右边一个降序的等比数列,项数为log(2,N)。
    D_list = N * np.logspace(-1,-math.log(N,2),int(math.log(N,2)),base=2)
    for D in D_list:
        if int(D) == 0:               # log函数计算特性，不用太纠结。该=1时，会=0.9999999999
            D = 1
        D = int(D)
        print(D)
        # 下面就是一个插入排序的变形。
        # for p in range(D,N,D):        # 跳着抓牌
        #     temp = A[p]
        #     for i in range(p,-1,-D):  # 跳着比大小找插入位置
        #         if A[i-D] > temp:
        #             A[i] = A[i-D]
        #         else:
        #             break
        #     A[i] = temp               # 跳着插入
        # 下面就是一个插入排序的变形。
        for p in range(D,N,D):
            temp = A[p]
            current = p
            preindex = p-D
            while preindex >=0 and A[preindex] > temp:
                A[current] = A[preindex]
                current = preindex
                preindex -= D
            A[current] = temp

# A = [1,5,6,2,4,3,8,9,7]
A = [3,1,9,8,28,36,44,35,0,100]
Shell_Sort(A)
print(A)
# 因为两个等值的元素可能由于跳着排大小，导致前后顺序发生变化，因此，希尔排序不是稳定的。
# 问题是 最坏、好情况：T = Θ(N**2)，
# Dk 作为增量元素，可能增量元素相互之间不互质，小增量根本不起作用。
# 更多的增量序列：
# Hibbrad 增量序列，Dk = 2**k -1。
# Sedgewick 增量序列，有点复杂不列举了。
# 数据流非常大的排序问题，可以考虑希尔排序 配合Sedgewick 增量序列。
