'''
有序子列归并
    其实在前面何老师已经讲过了，在多项式加减法计算那集。
'''
# L \ R LiftEnd \RightEnd 都是充当指针作用。
# T = O(N) 时间复杂度。
def Merge(A,TmpA,L,R,RightEnd):
    LeftEnd = R - 1
    Tmp = L                        # 存放数组的起始位置。
    NumElements = RightEnd - L + 1 # 记录元素个数
    while L <= LeftEnd and R <= RightEnd:
        if A[L] < A[R]:
            TmpA[Tmp] = A[L]
            L += 1
        else:
            TmpA[Tmp] = A[R]
            R += 1
        Tmp += 1
    while L <= LeftEnd:
        TmpA[Tmp] = A[L]
        Tmp += 1
        L += 1
    while R <= RightEnd:
        TmpA[Tmp] = A[R]
        Tmp += 1
        R += 1
    # 因为L 已经变了，只能从后往前推。
    print(TmpA)
    for i in range(RightEnd,RightEnd-NumElements,-1):
        A[i] = TmpA[i]

if __name__ == '__main__':
    A_list = [1,3,5,7,9,0,2,4,6,8]    # 两个有序子列组成的数组。
    A_temp = [None for _ in A_list]
    Merge(A_list,A_temp,0,5,9)
    print(A_list)
