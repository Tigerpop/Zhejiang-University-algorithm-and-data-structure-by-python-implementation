'''
归并算法排序
    归并排序是稳定排序
    "分而治之"，再递归处理。
    承接上一课中的 有序子列归并，使用 分而治之的思路，
    先把数组分为左边和右边部分，分别排好顺序，再用有序子列归并，归并左、右部分。

'''
# 时间复杂度的推导可以看《二分法、分而治之时间复杂度推导.pages》
# T = O(NlogN）
def M_Sort(A,temp_A,L,RightEnd ):  # 分而治之，先左边变有序再右变有序，最后归并一下让总的变有序。
    if L < RightEnd:               # 当此条件不满足的时候，我们就不做下面的事情，写代码时先完成递归部分，再回头补上此基线条件。
        Center = (L + RightEnd)//2 # 注意除法的取整
        M_Sort(A,temp_A,L,Center)
        M_Sort(A,temp_A,Center+1,RightEnd)
        Merge(A,temp_A,L,Center+1,RightEnd)
'''
注意！！！！
特意说明一个问题：
    为什么要在M_Sort参数里带着temp_A 这个临时数组走，
    而不是在M_Sort内部每次生成一个temp_A临时数组？
    这是因为：
        虽然他们的总的空间复杂度是一样的，但是每次在M_Sort内部生成一个临时数组又关掉，
        递归中用到M_Sort，就会频繁开辟内存空间又清理内存空间，不合算。
        最好的做法是一开始就生成一个temp_A临时数组，只把这个数组的指针传进整个工程中。
        视频中陈老师的图解分析的非常直观。
'''
# 统一函数接口
def Merge_Sort(A):
    N = len(A)
    temp_A = [None for _ in A]
    if temp_A!=None:       # 如果空间足够
        M_Sort(A,temp_A,0,N-1)
    else:
        return "空间不足"

def Merge(A,TmpA,L,R,RightEnd):
    LeftEnd = R - 1
    Tmp = L                        # 存放数组的起始位置。
    NumElements = RightEnd - L + 1 # 记录元素个数
    while L <= LeftEnd and R <= RightEnd:
        if A[L] < A[R]:            # 这里决定了次排序是稳定的排序。
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
    A = [1,5,6,2,4,3,8,9,7]
    Merge_Sort(A)
    print('上面的过程可以清晰的观察归并排序的过程\n',A)