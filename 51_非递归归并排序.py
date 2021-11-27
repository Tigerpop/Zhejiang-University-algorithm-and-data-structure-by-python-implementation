'''
非递归的归并排序算法
Merge1 决定了次排序是稳定的排序。
归并排序算法 需要一个等大小的空间，
而且需要来来回回倒来倒去，
所以，实际应用中，不被用于内排序，而被用于外排序！！！！

    每两个相邻的元素归并，形成新元素组，
    每两个相邻的新元素组 归并，形成新新元素组，
    ...
    重复直到归并成一个完整的元素组。
    用下面的图表示过程：         # 这一共的深度为logN
        - - - - - - - -       # - 代表 当前有序子序列。一行到下一行的过程就是merge_pass。
         --  --  -- --
           ----  ----
            --------

递归的方向是从"整到分"，
非递归的方向是从"分到整"。
'''
# 每行的归并不论奇数项还是偶数项，先把前面能组队的都组队处理，最后两项、或者一项再单独处理。
# 就是以下场景：
# 注意项数的定义，项数指的是有序子列个数。
# -- -- -- -|- -     # ｜是i被允许的最后位置，项数是奇数。
# -- -- -- -- |--    #  项数是偶数。注意项数的意思，项数中满了length就会被当一个子列，两个子列当一组，最后多出了一部分也会被当一个子列。
def Merge_pass(A,temp_A,N,length):             # length 是当前有序子序列的长度。A位置是修改前，temp_A位置是修改后。
    if length < N/2:
        for i in range(0,N-2*length,2*length):     # 注意 循环结尾取到了N-2*length位置。
            print('i=',i)
            Merge1(A,temp_A,i,i+length,i+2*length-1)
        print('到包括i的倒数第二个位置已经处理完毕 i=',i)
        i += 2*length
        print('i进入最后的子序列对，或者单独子序列。i=',i)
        if i + length <= N-1:            # 在满足一个length后，还足够形成一个子序列(这个子序列可能是1个元素也可能是满length个元素)，构成一对。
            print('偶')
            Merge1(A,temp_A,i,i+length,N-1)
        else:                            # 只剩下一个子列。
            print('奇')
            for j in range(i,N):         # 多出来的单独的有序子列，放到temp_A,下次归并再处理。
                temp_A[j] = A[j]         # 原本有序的子序列 直接 贴到temp中不做处理。
        global tag
        tag = i
    else:
        i = tag                          # 找到未处理尾巴的起始位置。
        Merge1(A,temp_A,0,i,N-1)

def Merge_Sort(A):
    N = len(A)
    length = 1
    temp_A = A.copy()
    if temp_A != None:
        while length < N:              # 不断交替A temp_A位置,让归并继续下去，最后存在A 中。
            print('1')
            Merge_pass(A,temp_A,N,length)
            length *= 2
            print('2')
            Merge_pass(temp_A,A,N,length)
            length *= 2
    else:
        return "空间不足"

# 这里的Merge1和之前的略有不同，在最后没有从temp_A赋值到A,等于说把A归并完的结果存入了temp_A。
def Merge1(A,TmpA,L,R,RightEnd):
    LeftEnd = R - 1
    Tmp = L  # 存放数组的起始位置。
    NumElements = RightEnd - L + 1  # 记录元素个数
    while L <= LeftEnd and R <= RightEnd:
        if A[L] < A[R]:  # 这里决定了次排序是稳定的排序。
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
    # # 因为L 已经变了，只能从后往前推。
    # print(TmpA,'temp')
    # for i in range(RightEnd, RightEnd - NumElements, -1):
    #     A[i] = TmpA[i]

if __name__ == '__main__':
    A = [3,1,9,8,28,36,44,35,0,100]
    temp_A = A.copy()
    N = len(A)
    length = 1
    print('length=',length)
    Merge_pass(A, temp_A, N, length)
    print(temp_A)
    length = 2
    print('length=', length)
    Merge_pass( temp_A,A, N, length)
    print(A)
    length = 4
    print('length=', length)
    Merge_pass(A,temp_A, N, length)
    print(temp_A)
    length = 8
    print('length=', length)
    Merge_pass(temp_A,A, N, length)
    print(A)
    length = 16
    print('length=', length)
    Merge_pass(A,temp_A, N, length)
    print(temp_A,'最终结果。')

    Merge_Sort(A)
    print(A,'最终结果。')
