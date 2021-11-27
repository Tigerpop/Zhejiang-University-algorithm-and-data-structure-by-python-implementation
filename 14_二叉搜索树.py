'''
二叉搜索树
非空左子树的值<根结点的值。
非空右子树的值>根结点的值。
左右子树都是二叉搜索树。
'''
class Node():
    def __init__(self,data,left=None,right=None ):
        self.data = data
        self.left = left
        self.right = right

# 尾递归 实现二叉搜索树的查找。
def find_(x,BinTree):
    if BinTree == None:
        return None
    if x > BinTree.data:
        return find_(x,BinTree.right)
        # 这样的 return 同一方法的递归，叫"尾递归"，理论上"尾递归"都可以用循环实现。
    if x < BinTree.data:
        return find_(x,BinTree.left)
    elif x == BinTree.data:
        return BinTree

# 循环 实现二叉搜索树的查找。
def find(x,BinTree):  #使用查找指针
    while BinTree:
        if x > BinTree.data:
            BinTree = BinTree.right
        if x < BinTree.data:
            BinTree = BinTree.left
        else:
            return BinTree
    return '没找着'
'''
# 循环实现的二叉搜索树查找，效率与树的结构有关，
# 树如果都是只有左结点或者都是只有右结点，查找效率会很低。
# 因为：
# 查找次数就是树的高度，
# 如果只有左子树一边倒，就会变成一个链表，
# n个结点高度是n，查找效率不高，达不到lg(N)。
'''

# 尾递归实现找最小
def findmin(BT):
    if BT==None:
        return None
    if BT.left == None:                 # 基线条件
        return BT
    else:
        return findmin(BT.left)

# 循环实现找最大
def findmax(BT):
    if BT:
        while BT.right:
            BT = BT.right
    return BT

# 递归实现插入,和递归实现查找类似。查找return即可，而插入要改变树的结构。
# 等于是把相关的路径重新构建了一遍，等于相关的指针重新指了一遍，
# 没有定义的路径，则保留原样。
def insert(x,BT):
    if BT == None:  # 基线条件。
        BT = Node(x)
        BT.left = None
        BT.right = None
    else:
        if x < BT.data:
            BT.left = insert(x,BT.left)  # 可以回顾以下链表的插入，两个步骤。
        if x >= BT.data:
            BT.right = insert(x,BT.right)
        # else:
        #     raise importError
    return BT
# 这里提示以下，写这种递归方法的套路。
# 首先要明确insert(x,BT)方法返回的是就是BT，用BT左子树右子树指向BT的左子树右子树，保证树的结构，在出现空位置可以插入时，再完成插入。


def preorder(BT,list_=[]):
    if BT:
        list_.append(BT.data)
        print(list_)
        preorder(BT.left)
        preorder(BT.right)
    return list_

'''
二叉搜索树的删除。
我们可以分三种情况：
一、删除结点为叶子结点，直接删除。
二、删除结点只有一个子结点，将父结点直接指向其子结点  (其实二情况包含了一情况)。
三、删除结点有两个子结点，
（删除此结点后，要么从左边找一个最大的、要么从右边找一个最小的，补上这个结点的位置）
（这样有一个好处，左最大和右最小都一定是叶子结点或者单一子结点，相当于又转为了问题一和问题二。）
'''
def delete( x,BT ): # 删除类似插入，也相当于重新构建的树的结构。
    if BT == None:
        print('未找到相应元素')
    elif x < BT.data:
        BT.left = delete(x,BT.left)
    elif x > BT.data:
        BT.right = delete(x,BT.right)
    elif x == BT.data: # 找到删除结点位置，按照上面三种情况讨论。
        if BT.left and BT.right :
            temp = findmin(BT.right)      # 此处也可以换成 从左子树中找最大的,下面跟着变。
            BT.data = temp.data         # 替换data 而没有选择插入删除，因为这样更简单。
            BT.right = delete(temp.data,BT.right) # 删除右子树中最小的结点。这里直接转化为了叶子结点或者一个子结点情况。
        else:   # 删除结点为一个或0个子结点。(注意：此处的删除不需要在这个位置完成经典的链表删除，而是考虑到return BT ，会在前面的树的构建过程，完成跳过结点的删除操作。)
            if BT.left == None:   # 有右孩子或者无孩子。
                BT = BT.right    # 只需要改变return 的结果，回溯到上面树的构建，就完成了跳过结点的删除操作。
            elif BT.right == None:
                BT = BT.left
    return BT


if __name__ == '__main__':
    tree = Node(6,Node(3,Node(1),Node(4)),Node(10,None,Node(12)))

    fmin = findmin(tree)
    fmax = findmax(tree)
    fx = find(10,tree)
    fx_ = find_(3,tree)
    fsert = insert(5,tree)
    insert_x = preorder(fsert)
    print(fmin.data,fmax.data,fx.data,fx_.data)
    print(insert_x,'\n\n')

    tree = Node(30,Node(15),Node(41,Node(33,None,Node(35,Node(34),None)),Node(50)))



