'''
快速排序
    和归并排序一样，快速排序的策略 ，也是"分而治之"。

伪代码
def  Quicksort(A):
    if len(A) < 2:
        return
    pivot = 从A[]中选一个主元
    将 S = { A[]除去pivot之外的元素 } 分成2个独立的子集
        A1 = {a属于S,a<pivot}
        A2 = {a属于S,a>pivot}
    A[] = Quicksort(A1) ∪ pivot ∪ Quicksort(A2)
    return A

以上的伪代码存在问题
一、pivot = 从A[]中选一个主元，这一步怎么选？才能快？

二、将 S = { A[]除去pivot之外的元素 } 分成2个独立的子集，
    怎么分才能快？

最好的时间复杂度，就是之前老推导的，中分分而治之，O(NlogN) 。
'''
 
'''
选主元
    令pivot = A[0] 
    T(N) = O(N) + T(N-1)          # 选了左边，再扫描了全体，再对后面N-1个元素递归。
         = O(N) + O(N-1) + T(N-2)
         ...
         = O(N) + O(N-1) + ...+O(1)
         = O(N**2)
    这样选左边作主元的方法不可取。

    令pivot = 随即取。
    令pivot = 最大与最小，取中位数。

伪代码
def Median3(A,L,R):
    Center = (L + R)/2
    if A[L] > A[Center]:
        Swap(A,L,Center)
    if A[L] > A[R]:
        Swap(A,L,R)
    if A[Center] > A[R]:
        Swap(A,Center,R)
    # 经过这三次变换，确认了小中大的顺序。
    # 同时，我们可以加入一种巧妙的方法缩小下一次的搜索范围。
    # 将中位数藏到右侧倒数第二个位置，
    # 因为交换后一定有A[L]<A[R],不用考虑最左和最右，
    # 下一次划分子集只需要考虑 L+1～R-1的范围。
    Swap(A,Center,R-1)
    return A[R-1]
'''
'''
子集划分
    此时不考虑L和R，在L+1～R-1的范围看，
    主元在R-1位置，
    设置指针i从L-1从左往右，指针j从R-2从右往左，
    A[i] 如果比A[R-1]大，就停住，否则继续走，
    A[j] 如果比A[R-1]小，就停住，否则继续走，
    Swap（A[i]停， A[j]停 ）
    以上的步骤终止条件是i>j。
    
    问题：
        如果正好有元素=pivot怎么办？
        方法一：停下来交换。每次交换，主元会大概放在中间的位置，
               这样递归之前经常推导，大概O(NlogN)
        方法二：不理他，继续移动指针。主元不会动留在端点，
               这样的递归上面推导了，大概O(N**2)。

快速排序的优点： 
    这里就可以看出来，快速排序为什么会快，
    因为，每一次选好主元并子集划分后，主元会一次性被放到正确的位置。

快速排序的缺点：
    用递归会频繁的入栈出栈，开辟空间等等，说人话就是慢。
    对小规模的数据N<100，简单排序快，如插入排序、冒泡排序。
    解决：
        规模小的时候，停止递归，直接简单排序。

'''
import numpy as np
import math

def Quicksort(A,L,R,Cutoff=2):
    if Cutoff <= R-L:             # 递归到当前待排序的部分(R-L)只有Cutoff个值的时候，又会使用到简单排序。
        print('快速排序：')
        Pivot = Median3(A,L,R)    # 除了返回一个值，主元已经放在正确位置。
        i = L
        j = R-1
        if j<0:
            return A
        print(Pivot)
        while 1:
            while A[i+1] < Pivot: # 相当于前面说的“停顿”。
                i += 1
            while A[j-1] > Pivot: # 相当于前面说的“停顿”。
                j -= 1
            print(i,j)
            i += 1
            j -= 1
            if i < j:
                Swap(A,i,j )
                print(i,j,A)
            else:
                break           # 循环终止条件。
            # 停住时，i的正确位置已经出现。和R-1位置交换。
        Swap(A,i,R-1)
        print(A)
        Quicksort(A,L,i-1)
        Quicksort(A,i+1,R)
    else:
        print('简单排序：')
        Insert_Sort(A)           # 数据少时用简单排序。

def Quick_Sort(A):
    N = len(A)
    Quicksort(A,0,N-1)

def Median3(A,L,R):
    Center = (L + R)//2
    if A[L] > A[Center]:
        Swap(A,L,Center)
    if A[L] > A[R]:
        Swap(A,L,R)
    if A[Center] > A[R]:
        Swap(A,Center,R)
    Swap(A,Center,R-1)         # 技巧点。
    return A[R-1]

def Swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# 插入排序
def Insert_Sort(A):
    for p in range(1, len(A)):     # 抓牌
        temp = A[p]                # 这次抓到的牌
        preIndex = p-1
        current = p
        while A[preIndex] > temp and preIndex >= 0 :  # 找插入位置。python找插入位置用while写方便一些。
            A[current] = A[preIndex]
            current = preIndex
            preIndex = current - 1
            # print(A)
        A[current] = temp

if __name__ == '__main__':
    A = [3,1,9,8,28,36,44,35,0,100]
    Quick_Sort(A)
    print(A)