'''
堆排序算法
    堆排序算法是在选择排序的基础上发展而来的。

'''
# ****************************************************************************************************
# 利用最小堆，原始版本堆排序。
class HeapStruct_2():
    def __init__(self,elements=[None],addre=0,capacity=0):
        self.elements = elements
        self.addre = addre # addre 相当于指针，表明堆中最大的那个位置。
        self.capacity = capacity
    def MinHeapCreate(self,Capacity_Size):
        print(' 若插入数值，请确保插入数值在 0 以上 。结点容量为%d'%Capacity_Size)
        self.elements = [None] * (Capacity_Size+1) # 因为有"哨兵"。
        self.capacity = Capacity_Size
        self.elements[0] = self.MinData() # 定义哨兵，其值小于堆中最小值，便于以后更快操作。
        print('self capacity = %s'%self.capacity)
    def MinData(self):
        return 0
    def Insert(self,item):
        if self.IsFull():
            print('最小堆已满')
            return
        i = self.addre + 1
        if self.elements[0] >= item:
            print('插入数值大小小于下限')
            return
        while self.elements[i//2] > item: # i/2 address是父结点的位置。加入值比父类结点小就往上走。这个循环是找到插入位置，并为插入点腾开位置。
            print(self.elements[i//2],item)
            self.elements[i] = self.elements[i//2] # 值得一提：树结构中移动，有的可变动值，而不动结点结构。
            i //= 2
        self.elements[i] = item
        self.addre += 1
    def IsFull(self):
        if self.addre == self.capacity:
            print( self.addre,self.capacity)
            return 1
        return 0
    def IsEmpty(self):
        if self.addre == 0:
            return 1
        return
    def DeleteMin(self):
        if self.IsEmpty():
            print('最小堆已空。')
            return
        minitem = self.elements[1]
        temp = self.elements[self.addre]
        self.elements[self.addre] = None
        self.addre -= 1 # 拿掉最后一个结点。
        parent = 1
        # 保证比最小的儿子还要小，就向上走。
        while parent*2 <= self.addre: # 保证有儿子（必有左儿子）（可能有右儿子）
            left_child = parent * 2
            if self.addre != left_child and self.elements[left_child+1] < self.elements[left_child]:
                child = left_child + 1
            else:
                child = left_child
            if self.elements[child] <= temp: # 假定temp在根位置。
                self.elements[parent] = self.elements[child]
                parent = child  # 沿着最小儿子的路径往下走。
            elif self.elements[child] > temp:
                self.elements[parent] = temp # 找到适合位置。
                return minitem
        self.elements[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。
        return minitem

'''
原始的堆排序算法。
'''
# 原始的堆排序算法（多浪费O(N)的空间）总的时间复杂度 T = O(Nlog(N))。
def Heap_Sort(A):   # 目的是改A , 但是堆中实际上是又开辟了一个A一样大小的空间，（多浪费O(N)的空间）。
    N = len(A)
    h = HeapStruct_2()
    h.MinHeapCreate(12)
    BuildHeap(A,h)                   #  O(NlogN) 因为我是用最傻的硬插的方法造新堆。
    for i in range(N):               #  O(N)
        A[i] = h.DeleteMin()         #  O(log（N))

def BuildHeap(A,h):
    for a in A:
        h.Insert(a)
# def DeleteMin(A):

A_ = [1,5,6,2,4,3,8,9,7]
Heap_Sort(A_)
print('原始的堆排序 时间复杂度O(NlogN）、空间复杂度 2N,结构如下：\n',A_,'\n')

# ****************************************************************************************************

# 不利用最小堆而利用最大堆，改进版本堆排序。

# 步骤一：把数组（i ～ N）部分调整为最大堆。
# 步骤二：把最大堆根元素和最后一个元素换一个位置，固定最大值到数组末尾N-1位置。
# 步骤一：把数组（i ～ N-1）部分调整为最大堆。
# 步骤二：把最大堆根元素和倒数第二个元素换一个位置，固定最大值到数组N-2位置。
# ...
# 注释：所谓的结点下沉 shiftdown，
# 就是前面学过的
# 假定temp在根位置，从根往下找位置并调整树结构的过程。

# 正式发行版 堆排序。
def Heap_Sort_new(A):                # 默认有"哨兵"在0位置，所以后序都在1位置往后变动。
    N = len(A)
    for i in range(int(N/2),0,-1):   # BuildHeap，在有"哨兵"时，其倒数第一个子结点为叶子结点的位置就在N/2处。
        PercDown(A,i,N-1)            # i 对应的是每次shiftdown的根位置，N-1对应最后一个元素的位置。
    for i in range(N-1,0,-1):        # DeleteMax
        Swap(A,1,i)
        PercDown(A,1,i-1)            # 每次下沉，都会有一个最大的数补充到root位置，还是最大堆。

# PercDown就是 shiftdown，时间复杂度为 O(logN)。
# 在有"哨兵"时，其倒数第一个子结点为叶子结点的位置就在N/2处。
def PercDown(A,i,num):
    parent = i
    temp = A[i]
    while parent * 2 <= num:         # 保证有儿子（必有左儿子）（可能有右儿子）
        left_child = parent * 2
        if num != left_child and A[left_child + 1] > A[left_child]:
            child = left_child + 1
        else:
            child = left_child
        if A[child] >= temp:         # 假定temp在根位置。
            A[parent] = A[child]
            parent = child           # 沿着最大儿子的路径往下走。
        elif A[child] < temp:
            A[parent] = temp         # 找到适合位置。
            return
    A[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。

def Swap(A,a,b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp
    # print(A[a],A[b],'!!!')

A = [1,5,6,2,4,3,8,9,7]
A.insert(0,-1)  # 加个"哨兵"
Heap_Sort_new(A)
A.pop(0)       # 不看"哨兵"
print('用heapify堆化的堆排序 平均时间复杂度O( 2NlogN - O(NloglogN) ）、空间复杂度 N,结构如下：\n',A,'\n')