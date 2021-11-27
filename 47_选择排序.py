'''
选择排序算法
    过于简单，以至于直接看代码吧。
'''
def Selection_Sort(A):
    N = len(A)
    for i in range(N):
        MinPosition = ScanForMin(A,i) # 从i到N-1位置找最小元素。
        Swap(A,i,MinPosition)         # 将未排序的最小元换到已排序的最后位置。

def ScanForMin(A,i):   # 最傻的方法。
    N = len(A)
    for j in range(i,N):
        count = 0
        for k in range(i,N):
            if A[j] <= A[k]:
                count += 1
                if count == N-i: # 比所有的元素都小或相等了。
                    print(A[j])
                    return j

def Swap(A,i,m):
    temp = A[i]
    A[i] = A[m]
    A[m] = temp

# 制约时间复杂度的 关键是 ScanForMin 方法。
# 如果仅仅是普通遍历一遍，T = Θ(N**2)
# 如果用最小堆，则会优化很多。

A = [1,5,6,2,4,3,8,9,7]
Selection_Sort(A)
print(A)