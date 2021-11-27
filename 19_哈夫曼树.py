'''
先回顾一下，数据存储空间知识。
位bit：
二进制数，例如1001就是"四位"的二进制数，表示若干状态。
字节byte：
1 字节 == 8 位，是计算机处理的基本单位。通常1个字节可以存入一个ASCII码，2个字节可以存放一个汉字国标码。
字：
计算机进行数据处理时，一次存取、加工和传送的数据长度称为字（word）。一个字通常由一个或多个（一般是字节的整数位）字节构成。例如286微机的字由2个字节组成，它的字长为16；486微机的字由4个字节组成，它的字长为32位机。
ASCII码:
由美国国家标准局(ANSI)制定的ASCII码（American Standard Code for Information Interchange，美国标准信息交换码），它已被国际标准化组织（ISO）定为国际标准，称为ISO 646标准。适用于所有拉丁文字字母，ASCII码有7位码和8位码两种形式

'''
'''
哈夫曼树

如何根据结点的不同查找频率构造更有效的搜索树？

带权路径长度WPL:
二叉树n个叶子结点，每个叶子结点带有权值 W（k），从根结点到叶子结点的长度为L(k)
每个叶子结点的带权路径长度之和 WPL = SUM(W(k)*L(k))

最优二叉树/哈夫曼树： WPL 最小的二叉树。
哈夫曼树不是堆！！只不过哈夫曼树的建立过程用最小堆会快一些。

'''
# 哈夫曼树的构造：
# 在权值列表中，把最小的两权值建树，树根为权值和，
# 再在权值列表中用 此权值和 代替最小两个权值，形成新的列表。
# 在新的列表中找两个最小的权值，建树，树根为这两的权值和
# ...
# 直到 列表中只有两权值，建最后一颗树，树根为权值和。

# 值得一提：
# 在n个数中，选取两个最小的权值然后形成新的值，
# 用排序 不如用堆 的效率高，
'''
（我并不明白为什么这里用堆比排序效率高）
'''
# 哈夫曼树的特点：
# 1、没有度为1 的结点。n1 = 0
# 2、n个叶子结点的哈夫曼树 有2n-1个结点。 因为 n2 = n0 -1
# 3、哈夫曼树非叶结点的左右子树交换后仍是哈夫曼树。
# 4、同一组权值 ，可能存在不同构的两颗哈夫曼树。

# 科学建立哈夫曼树需要用到最小堆。 O(Nlog N)
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
        return Node(0)
    def Insert(self,item):   # 这里插入的都是结点。
        if self.IsFull():
            print('最小堆已满')
            return
        i = self.addre + 1
        if self.elements[0].weight >= item.weight:
            print('插入数值大小小于下限')
            return
        while self.elements[i//2].weight > item.weight: # i/2 address是父结点的位置。加入值比父类结点小就往上走。这个循环是找到插入位置，并为插入点腾开位置。
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
            if self.addre != left_child and self.elements[left_child+1].weight < self.elements[left_child].weight:
                child = left_child + 1
            else:
                child = left_child
            if self.elements[child].weight <= temp.weight: # 假定temp在根位置。
                self.elements[parent] = self.elements[child]
                parent = child  # 沿着最小儿子的路径往下走。
            elif self.elements[child].weight > temp.weight:
                self.elements[parent] = temp # 找到适合位置。
                return minitem
        self.elements[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。
        return minitem

'''
哈夫曼树的建立算法：
1、 将 权值序列 建立最小堆，element_list 中存放树的结点,而不是单纯的数字。
    
2、 从最小堆中(按结点值)取出两个最小的元素，再(按结点值)求和建立根结点，
    形成一个链表结构的树 T ，返回根结点。

3、 将求和形成的根结点插入最小堆，
    此时堆中走了两个元素，来了一个新的元素，只不过这个新元素是 T 的根结点。
    
4、 重复1、2、3 步骤。直到堆中元素只有一个元素(作n-1次合并)，完成世界线收束，哈夫曼树建立完毕。
    此时堆中只有一个元素，而这个元素是哈夫曼树的根结点。

整体复杂度为 O(Nlog N)
'''
class Node():
    def __init__(self,weight=0,left=None,right=None):
        self.weight = weight
        self.left = left
        self.right = right
class HFM_Tree():
    def __init__(self,H):
        h = HeapStruct_2()
        h.MinHeapCreate(10)
        for i in H:
            h.Insert(Node(i))   # 笨办法建堆。
        for i in range(h.addre-1): # 作n-1次合并
            T = Node()
            T.left = h.DeleteMin()
            T.right = h.DeleteMin()
            T.weight = T.left.weight + T.right.weight
            h.Insert(T)
        # 循环后最小堆中只有一个元素，它是哈夫曼树的根结点。
        T = h.DeleteMin()
        self.HFM_tree = T  # 哈夫曼树构建完毕。
        # print(self.HFM_tree.weight)
    def preorder(self,BT,list_=[]): # 利用可变对象特性遍历。
        if BT:
            list_.append(BT.weight)
            self.preorder(BT.left,list_)
            self.preorder(BT.right,list_)
        return list_

H = [1,2,3,4,5]
hfm = HFM_Tree(H)
list_ = hfm.preorder(hfm.HFM_tree)
print(list_)

