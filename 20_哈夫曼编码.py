
'''
给定一段字符，如何对字符编码，占存储空间最少。

7个字符组成的文本，58个字符串。

ASCII码 ：58 * 8 = 464 位

等长3位编码 ：58 * 3 = 174 位

不等长编码 ：
    避免二意性  ———— 前缀码prefix code ，任何字符的编码都不是另一字符编码的前缀。
    （可以无二意的解码）
        用二叉树进行编码，左右分支0、1，字符在叶结点上。
        要避免有字符结点在非叶结点，因为这样会出现前缀带来的二意性。

例如：
a 出现4次， b 出现1次， c 出现2次，d 出现1次。
把字符放在满二叉树的叶子结点上，
查找a 要在树中经过 00 两条边， b 经过 01 两条边 ...
cost（aaacbacd）= 0000001001001011 是 8 * 2 = 16位。
问题转化为 哈夫曼树的问题，
因为哈夫曼树的 带权路径长度WPL 最小。
cost（aaacbacd）< 16

'''

'''
例题：
a 10次
e 15次
i 12
s 3
t 4
sp 13
nl 1
用最小的存储空间表示以上文本。

答案：以字符出现频率为权值，建立哈夫曼树，追求带权路径长度WPL 最小。
     a 111
     e 10
     i 00
     s 11011
     t 1100
     sp 01
     nl 11010
     代码如下：
'''
# 最小堆。
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
        # 假定temp在根位置,保证temp比最小的儿子还要小，最小的儿子就向上走，parent指针沿着最小儿子的路径往下走。
        while parent*2 <= self.addre: # 保证有儿子（必有左儿子）（可能有右儿子）
            left_child = parent * 2
            if self.addre != left_child and self.elements[left_child+1].weight < self.elements[left_child].weight:
                child = left_child + 1
            else:
                child = left_child
            if self.elements[child].weight <= temp.weight: # 假定temp在根位置。
                self.elements[parent] = self.elements[child]
                parent = child  # 沿着最小儿子的路径往下走，若一直循环也没找到temp落脚点，parent落到叶子结点位置。
            elif self.elements[child].weight > temp.weight:
                self.elements[parent] = temp # 找到适合位置。
                return minitem
        self.elements[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。
        return minitem


class Node():
    def __init__(self,weight=0,name=None,left=None,right=None):
        self.weight = weight
        self.name = name  # 多加一个结点属性，方便后序找出对应关系。
        self.left = left
        self.right = right

class HFM_Tree():   # 可以把平面构思 提升为空间立体构思。
    def __init__(self,H):
        h = HeapStruct_2()
        h.MinHeapCreate(10)
        for i in range(len(H)):
            item = H.popitem()
            h.Insert(Node(item[1],item[0]))   # 笨办法建堆。
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

    # 打印0——1左右路径，可参考我之前的《8.2两种打印...》的代码。
    def label_preorder(self,BT,list_=[],re={},code_=None):
        if BT:
            list_.append(code_)
            if BT.left == None and BT.right == None:  # 叶子结点
                re[(BT.weight, BT.name)] = list_.copy()
            else:
                self.label_preorder(BT.left,list_,re,code_='0')
                self.label_preorder(BT.right,list_,re,code_='1')
            list_.pop()
        return re
    def result_0_1_path(self,BT):
        re = self.label_preorder(BT)
        result = {}
        for key,value in re.items():
            value.pop(0)
            result[key] = (''.join(value))
        return result

if __name__ == '__main__':
    H = {'a':10,'e':15,'i':12,'s':3,'t':4,'sp':13,'nl':1}
    hfm = HFM_Tree(H)
    dict_ = hfm.label_preorder(hfm.HFM_tree)
    print(dict_.keys())
    print(dict_)
    result = hfm.result_0_1_path(hfm.HFM_tree)
    print(result)