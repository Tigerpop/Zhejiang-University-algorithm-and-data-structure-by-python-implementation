'''
优先队列：
取出元素的顺序是依照优先级（关键字）大小，而不是元素加入队列的先后顺序。

若数组或链表实现优先队列

数组
插入 --- 元素总是插入尾部，O(1)
删除 --- 查找最大（小）关键字 O(n）
         从数组中删除，需要移动元素 O(n）
链表
插入 --- 元素总是插入链表的头部 O(1)
删除 --- 查找最大（小）关键字 O(n）
         删去结点      O(1)
有序数组
插入 --- 找到适合的位置    O(n）或O(log n）
        移动元素并插入  O(n）
删除 --- 删去最后一个元素 O(1)
有序链表
插入 --- 找到适合的位置 O(n）
         插入元素 O(1)
删除 --- 删除首元素或者最后的元素 O(1)

'''
'''
若使用二叉搜索树
在平衡条件下，删除都是 O(log2 n)
但是多删除几个以后，树就歪了，不平衡了，效率开始下降向 O(N)变化。

'''
# 堆的两个特性：
# 1结构性、用数组表示的 完全二叉树 。
# 2有序性、任意结点的关键字是其子树所有结点的最大值（或最小值）
#     最大堆MaxHeap （大顶堆）
#                  （小顶堆）

# class Node():
#     def __init__(self,data,left=None,right=None):
#         self.data = data
#         self.left = left
#         self.right = right

# 堆其实就是一个完全二叉树，大小按层序遍历 依次变大或者变小，
# 不过address的角标还是 1 2 3 4 ... 所以直接存放在数组里面也是很方便的。

# 最大堆的创建
class HeapStruct():
    def __init__(self,elements=[None],addre=0,capacity=0):
        self.elements = elements
        self.addre = addre # addre 相当于指针，表明堆中最大的那个位置。
        self.capacity = capacity
    def MaxHeapCreate(self,MaxSize):
        print(' 若插入数值，请确保插入数值在 100 以内 。结点容量为%d'%MaxSize)
        self.elements = [None] * (MaxSize+1) # 因为有"哨兵"。
        self.capacity = MaxSize
        self.elements[0] = self.MaxData() # 定义哨兵，其值大于堆中最大值，便于以后更快操作。
        print('self capacity = %s'%self.capacity)
    def MaxData(self):
        return 100
# 将新增结点插入到其父结点到根结点的有序序列中。
    def Insert(self,item):
        if self.IsFull():
            print('最大堆已满')
            return
        i = self.addre + 1
        if self.elements[0] <= item:
            print('插入数值大小超限')
            return
        while self.elements[i//2] < item: # i/2 address是父结点的位置。加入值比父类结点大就往上走。这个循环是找到插入位置，并为插入点腾开位置。
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
        return 0

# 算法：将堆中最大值删除。
#   步骤：1、拿走根结点。
#        2、将addre结点搬家，从根到下，沿着最大儿子线路（线路上结点重排），找适合落脚点。
    def DeleteMax(self):
        if self.IsEmpty():
            print('最大堆已空。')
            return
        maxitem = self.elements[1]
        temp = self.elements[self.addre]
        self.elements[self.addre] = None
        self.addre -= 1 # 拿掉最后一个结点。
        # 找temp 放的位置 ，用parent从根来找这个位置。
        # 把temp假象在根结点，从上往下过滤下层结点。temp不需要放在根位置，比较temp值即可达到效果。
        # 用temp和左右儿子最大的那个比，大儿子比temp大，就上来，temp下去；比temp小，就直接放temp。
        parent = 1
        while parent*2 <= self.addre: # 保证有儿子（必有左儿子）（可能有右儿子）
            left_child = parent * 2
            # 找最大的那个儿子。
            # （左不等，则一定有右儿子） 且 （右大于左时） 右儿子定义为大儿子。
            if self.addre != left_child and self.elements[left_child+1] > self.elements[left_child]:
                child = left_child + 1
            else:
                child = left_child
            # 这里有个逻辑问题需要解释一下，只需要把最大的儿子那一路变动就行，
            # 因为大的那个儿子，已经作过了和小儿子的比较，它登顶小儿子没意见，
            # 大儿子只需要和temp比，temp路径确定，就是不断沿着最大儿子换上下位置。
            if self.elements[child] >= temp: # 假定temp在根位置。
                self.elements[parent] = self.elements[child]
                parent = child  # 沿着最大儿子的路径往下走。
            elif self.elements[child] < temp:
                self.elements[parent] = temp # 找到适合位置。
                return maxitem
        self.elements[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。
        return maxitem


h = HeapStruct()
h.MaxHeapCreate(50)
# h.Insert(101)
h.Insert(22)
h.Insert(12)
h.Insert(13)
h.Insert(44)
h.Insert(44)
h.Insert(44)
h.Insert(50)
print(h.elements,'\n',h.addre)
h.DeleteMax()
print(h.elements,'\n',h.addre)

'''
最大堆的建立：
方法一：
像上面不断插入来建立最大堆。
时间复杂度 O(Nlog N） 因为一次擦乳的时间复杂度是二分法类似的 log N ，循环n次。
方法二：
在线性时间复杂度下，建立最大堆。
找到最后一个节点的父节点，从它开始进行节点shiftdown下沉操作，直到结束。该方法不难。
多次shiftdown 会完成一个堆化 heapify 形成一个堆，但是只有从倒数第一个非叶结点，逐次往上shiftdown才会形成堆，不是随便一个shiftdown都能形成堆的。
O(N)
步骤一：将n个元素按输入顺序存入，先满足完全二叉树的结构特性。
步骤二：调整结点位置，满足最大堆的有序特性。
      先从倒数第一个有儿子的结点调起，把它和最大的儿子比大小，
      类似于删除中的部分操作，将它和儿子调整成堆。
      再从倒数第二个有儿子的... 
      重复步骤二 ... 直到根结点。  
      
T = O(n） 我不知道推导。   
'''
# 方法二 heapify堆化 建立最大堆。 可以跳到后面《48堆排序》巩固一下。
# 可以插入前面的 heap 类中，作一个方法。
def BuildHeap_new_mathed(A,N):   # 这里都是默认有个"哨兵"在0位置 。
    def shiftdown(A,i,N):
        parent = i
        temp = A[i]
        while parent * 2 <= N:  # 保证有儿子（必有左儿子）（可能有右儿子）
            left_child = parent * 2
            if N != left_child and A[left_child + 1] > A[left_child]:
                child = left_child + 1
            else:
                child = left_child
            if A[child] >= temp:  # 假定temp在根位置。
                A[parent] = A[child]
                parent = child  # 沿着最大儿子的路径往下走。
            elif A[child] < temp:
                A[parent] = temp  # 找到适合位置。
                return
        A[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。
    for j in range(int(N/2),0,-1):
        shiftdown(A,j,N)

A =[0,1,5,6,2,4,3,8,9,7,10,13,12,11]
BuildHeap_new_mathed(A,len(A)-1)
print('用heapify堆化，O(N),shiftdown不断下沉的方法构建堆为：\n',A,'\n')




# 最小堆建立。
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

h = HeapStruct_2()
h.MinHeapCreate(12)
# h.Insert(101)
h.Insert(22)
h.Insert(12)
h.Insert(13)
h.Insert(44)
h.Insert(44)
h.Insert(44)
h.Insert(50)
print(h.elements,'\n',h.addre)
h.DeleteMin()
print(h.elements,'\n',h.addre)
