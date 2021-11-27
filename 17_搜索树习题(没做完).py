'''
题目：
给定多组序列，判断是否为同一颗二叉搜索树.

给定 一个 序列，它对应的二叉搜索树是一定的，
但是 给定一个二叉搜索树，它的序列却是不一定一样的。

'''
'''
思路：
思路一、分别建立搜索树，判别树是否一样。
思路二、不建立树。以根数字为中心，比较数字大小，左数组与右数组再不断这样递归，看数组顺序是否一致。
思路三、建立一棵树，再判别与其它序列是否与该树一致。

'''
# 思路三：
# 1、搜索树表示
# 2、建搜索树T
# 3、判别一序列是否与搜索树T一致
class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.flag = 0

def insert(BT,item):   # 二叉搜索树 的插入。
    if BT == None:
        BT = Node(item)
        BT.left = None
        BT.right = None
    elif BT.data > item:
        BT.left = insert(BT.left,item)
    elif BT.data < item:
        BT.right = insert(BT.right,item)
    return BT

def preorder(BT,list_=[]):  # 先序遍历打印出来检查。
    if BT:
        list_.append(BT.data)
        preorder(BT.left)
        preorder(BT.right)
    return list_

list_ = [[3,1,2,4],[3,2,1,4],[3,4,1,2],[3,1,2,4]]

def main(list_=list_):
    N = len(list_[0])
    L = len(list_)
    while N:
        T = MakeTree(N)  # 建立搜索树。
        for i in range(L-1):
            if Judge(T,N,i): # 判别是否相等。
                print('yes')
            else:
                print('no')
            Reset(T) #  清除T中标记的flag
    return 0

def MakeTree(N):
    v = list_[0].copy()
    T = Node(v.pop(0))
    for i in range(N-1):
        insert(T,v.pop(0))
    return T

# 沿着list的顺序查找，查找某个数字如果超找的过程中遇到新的没遇见的结点（数字），
# 这个结点的出现位置一定和原树不一样。
# 可以判定两个树一定不一样。因为按照新列表的构建顺序，它构建不起来原来树的结构。
def check(BT,num):
    if BT.flag:     # 该结点过去被查找过。 flag = 1 ,搜索过程可以判断是否树相等。
        if num < BT.data:
            return check(BT.left,num)
        if num > BT.data:
            return check(BT.right,num)
    else:   # 没有被查过。
        if num == BT.data:
            BT.flaf = 1 # 标记已经找过了。
            return 1    # 找到了这个数。结束搜索。
        else:    # 遇到一个以前没遇见过的，且与要找的数不相等的 结点，可知两个树构造不一样。
            return 0

def Judge(BT,N,i):  # check 是看单个结点与原树的位置是否一致，Judge就要看每一个结点是否都匹配原树的结构。
    v = list_[i+1].copy()
    v_0 = v.pop(0)
    if BT.data!=v_0:
        return 0      # 根结点就不一样。
    else:
        BT.flag = 1
    for n in range(N-1):
        if check(BT,v.pop(0)) == 0:
            return 0
    return 1

def Reset(BT):
    if BT.left:
        Reset(BT.left)
    if BT.right:
        Reset(BT.right)
    BT.flag = 0


tree = MakeTree(len(list_[0]))
j = Judge(tree,len(list_[0]),2)
print(j)



