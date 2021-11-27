'''
插入排序的判断
    题意：
        给出排序的中间产物，
        区分简单的插入排序和归并排序,
        然后将排序进行完。
        sample input
        10                               插入排序：前面有序，后面没插入的部分没变化。
        3，1，2，8，7，  5，9，4，6，0
        1，2，3，7，8，  5，9，4，6，0

        10                               归并排序：分段有序，比如这里就是两两有序。
        3，1，2，8，7，5，9，4，0，6                 归并中有序长度一定是 2、4、8 ...
        1，3，  2，8，  5，7，  4，9， 0,6

    思路：
    先判断可能是插入排序还是归并排序
    再往下排一个步骤。

"捏软柿子算法"
    我们可以很简单的发现，判断插入排序明显比判断归并排序简单很多，于是我们从"软柿子"———插入排序下手。
    1、 判断是否是插入排序：
        一、从左往右扫描，直到发现顺序不对（出现左大于右），跳出循环，并记录跳出点位置point。
        二、从跳出位置继续往右扫描，与原始序列对比，
            发现有不同就return False。
            往右扫描到结束均未发现不同，return (True point)。
        从point位置继续插入排序。
    2、 判断是否是归并排序：
        一、猜想有序长度是2，如果不对就4、8、16 ...类推。
            for i in range(1,log2(N),1):
                l = 2**i
                # 检验 l=2 是否正确，需要在每一个子列中比较看是否有序，如 01 之间 、23之间、45之间，跳跃一个l的长度。
                # 假如已经确定长度为2时已经有序，再试试看长度4时是否正确。
                # 由于长度为2的小段内部已经确定有序，
                # 此时仅仅需要比较两个长度为2的小段邻接位置是否有序，然后跳过2个小段再比较...以此类推。如 12之间、56之间，跳跃2l的长度。
                # 通俗案例
                #   l = 2 时，检验是否有序
                #     (l/2)-1=0, 从 0 开始和后一个比 ，隔 l = 2 个元素比，直到超范围。
                #   l = 4 时，检验是否有序
                #     (l/2)-1=1 从 1 开始和后一个比，隔 l = 4 个元素比，直到超范围。
                #   l = 8 时，检验是否有序
                #     (l/2)-1=3 从 3 开始和后一个元素比，隔 l = 8 隔元素比，直到超范围。
                if l 无序:
                    l = 2**(i-1)
                    break
            return (True,l)        # 返回上一个有序的长度。
        从有序子列长度为l， 继续归并排序。

边际测试
    最小N ，应该是4。因为 1、2、3个元素时，解都不是唯一的，也就是说既有可能是插入排序、也可能是归并排序的中间产物。
    最大N。

'''
import math
# "捏软柿子"算法
def main(A):
    original = A[0]
    process = A[1]
    Is_Insert = Judge_Insert_Sort(original, process)
    print(Is_Insert)
    if Is_Insert[0]:
        Continue_Insert_Sort(original, process, Is_Insert[1])
        return
    Is_Merge = Judge_Merge_Sort(original,process)
    if Is_Merge[0]:
        Continue_Merge_Sort(original,process,Is_Merge[1])

def Judge_Insert_Sort(original,process):
    i = 0
    N = len(process)
    while i < N - 1 and process[i] <= process[i+1]:    # 找跳出位置；若跳出位置i=N-1，则已经插入排序完毕。
        i += 1
    if i == N - 1:
        print('不确定是否为插入排序，因为排序已经排完。')
        return False,"Can't determine."
    point = i+1
    for j in range(point,N):
        if original[j] != process[j]:
            print('不是插入排序。')
            return False,point
    print('是插入排序,排到了%d号位置'%point)
    return True,point

def Continue_Insert_Sort(original,process,point):
    def Insert_Sort(A,point):
        for p in range(point,len(A)):  # 从5号位置抓牌
            temp = A[p]  # 这次抓到的牌
            preIndex = p - 1
            current = p
            while A[preIndex] > temp and preIndex >= 0:  # 找插入位置。python找插入位置用while写方便一些。
                A[current] = A[preIndex]
                current = preIndex
                preIndex = current - 1
            A[current] = temp
    Insert_Sort(process,point)
    print('排好序的结果是：\n',process)

def Judge_Merge_Sort(original,process):
    N = len(process)
    for i in range(1,int(math.log(N,2))+1, 1):
        l = 2**i
        for j in range((l//2)-1,N,l):
            if j+1 < N and process[j] > process[j+1]:
                l = 2**(i-1)
                if l == 1:                               # 有序子列长度连2都达不到，不能确定是归并排序。
                    print('不能确定是归并排序。')
                    return False,l
                print('是归并排序，归并到了有序子列长度为%d' % l)
                return True, l
# 虽然递归写法的归并排序更加简单，但是题意要求从中间项继续运行，所以被迫选择循环写法的归并排序。
def Continue_Merge_Sort(original,process,l):
    def Merge_pass(A, temp_A, N, length):
        if length < N / 2:
            for i in range(0, N - 2 * length, 2 * length):
                Merge1(A, temp_A, i, i + length, i + 2 * length - 1)
            i += 2 * length
            if i + length <= N - 1:  # 在满足一个length后，还足够形成一个子序列(这个子序列可能是1个元素也可能是满length个元素)，构成一对。
                Merge1(A, temp_A, i, i + length, N - 1)
            else:  # 只剩下一个子列。
                for j in range(i, N):  # 多出来的单独的有序子列，放到temp_A,下次归并再处理。
                    temp_A[j] = A[j]  # 原本有序的子序列 直接 贴到temp中不做处理。
            global tag
            tag = i
        else:
            i = tag  # 找到未处理尾巴的起始位置。
            Merge1(A, temp_A, 0, i, N - 1)
    def Merge1(A, TmpA, L, R, RightEnd):
        LeftEnd = R - 1
        Tmp = L
        NumElements = RightEnd - L + 1
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
    def Merge_Sort(A, l):
        N = len(A)
        length = l             # 从有序子列长度l情况下 继续归并排序。
        temp_A = A.copy()
        if temp_A != None:
            while length < N:  # 不断交替A temp_A位置,让归并继续下去，最后存在A 中。
                Merge_pass(A, temp_A, N, length)
                length *= 2
                Merge_pass(temp_A, A, N, length)
                length *= 2
        else:
            return "空间不足"
    Merge_Sort(process,l)
    print('从有序子列长度为 %d 情况继续归并排序，排序结果为\n'%l,process)


if __name__ == '__main__':
    # A = [[3,1,2,8,7, 5,9,4,6,0],[1,2,3,7,8, 5,9,4,6,0]]
    # A = [[3, 1, 2, 8, 7, 5, 9, 4, 6, 0], [0,1,2,3,4,5,6,7,8,9]]
    B = [[3,1,2,8,7,5,9,4,0,6],[1,3,2,8,5,7,4,9,0,6]]
    # B = [[3, 1, 2, 8, 7, 5, 9, 4, 0, 6], [0,1,2,5,4,3,6,7,8,9]]
    main(B)