'''
有10台电脑，1-2、2-4、3-5、4-7、5-8、6-9、6-10、连接

问：2-7、5-9之间是否联通？

解决思路：1、把10台电脑视为10个集合，
         2、在一条线上，视为集合作了 并 运算。
         3、两个点是否在一条线上，转化为了两个点是否在一个集合内。

这样 两步骤算法 "并" "查"。
可以用树来表示集合，树的结点代表集合的元素。
用树根root来代表某一个集合。

"双亲"表示法 ---- 每个孩子指向双亲。
可以不用链表 用数组就能存储，(静态链表)表示。
(静态链表) 可参考《13二叉树同构》

但是双亲表示法的指向不一样，一个结点只有一个指针，都是只指向父结点，

2 {4  6  8}
1 {3 5 7 9}

'''
class Node():
    def __init__(self,data=None,parent=None):
        self.data = data
        self.parent = parent # parent 是 list 中的位置，而不是字面意义上的parent的值。
class Tree():
    def __init__(self,maxsize=10):
        print('最大10个元素。')
        self.s = [None] * maxsize
        self.maxsize = maxsize
        self.address = 0
    def add(self,item,item_parent):
        self.s[self.address] = (Node(item,item_parent))
        self.address += 1

    # 查找元素所在的集合，（根结点表示的模型中，就是找根结点。）
    def find(self,x):
        i = 0
        while i < self.address and self.s[i].data != x: # 找x位置。
            i += 1
        if i >= self.address:
            return -1,'没找到' # 没找到。
        while self.s[i].parent >= 0:  # i 就是x的位置，现在开始找这个位置总的根结点。
            i = self.s[i].parent
        return i   # 总的根结点位置。(集合的确定)

tree = Tree() # tree 里面其实包括了两个集合（两棵树）
tree.add(4,1)
tree.add(10,-1)
# print(tree.s[0].data,tree.s[0].parent)
tree.add(6,1)
tree.add(8,1)

tree.add(9,-1)
tree.add(3,4)
tree.add(5,4)
tree.add(7,4)
# print(tree.s[4].data,tree.s[4].parent)
t3 = tree.find(3)
print(t3) # 3 属于 4号位置这个集合。
t5 = tree.find(5)
print(t5)  # 也是属于4号集合。
t6 = tree.find(6)
print(t6)
t21 = tree.find(21)
print(t21)