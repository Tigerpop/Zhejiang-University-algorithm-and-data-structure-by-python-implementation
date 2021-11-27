class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

# 例子一：
# 输出叶子结点方法。left 、right均为None，就输出，这里用前序遍历实现。
def preorder(BT,list_=[]):
    if BT:
        if BT.left==None and BT.right==None:
            list_.append(BT.data)
        preorder(BT.left)
        preorder(BT.right)
    return list_


tree = Node('a', Node('b', Node('d'), Node('f', Node('e'))), Node('c', Node('g', None, Node('h')), Node('i')))
print(preorder(tree))

# 例子二：
# 求二叉树的高度。
# 用层序遍历求高度（深度）非常简单，但是这我们练习用递归解决。
def postorderheight(BT):
    if BT:
        HLeft = postorderheight(BT.left)
        HRight = postorderheight(BT.right)
        MaxH = max(HLeft , HRight)
        return MaxH +1
    else:
        return 0

print(postorderheight(tree))


# 例子三：
# 二元运算表达式树及其遍历。
# 叶子结点是运算数，非叶子结点存运算符。

# 注意：
# 中序遍历时，得到的表达式不一定正确，
# 因为中序输出结果严格匹配顺序，不会考虑到输出运算法优先级。
# 这个问题我们可以通过给中序表达式 加括号解决，输出左子树时加左括号，右子树加右括号。

tree2 = Node('+',Node('+',Node('a'),Node('*',Node('b'),Node('c'))),Node('*',Node('+',Node('*',Node('d'),Node('e')),Node('f')),Node('g')))

def preorder(BT,list_=[]): # 先序
    if BT:
        list_.append(BT.data)
        preorder(BT.left)
        preorder(BT.right)
    return ' '.join(list_)
def inorder(BT,list_=[]):  # 加括号的中序。
    if BT:
        list_.append('(')
        inorder(BT.left)
        list_.append(BT.data)
        inorder(BT.right)
        list_.append(')')
    return ' '.join(list_)
def postorder(BT,list_=[]): # 后序
    if BT:
        postorder(BT.left)
        postorder(BT.right)
        list_.append(BT.data)
    return ' '.join(list_)

pre = preorder(tree2)
print(pre)
ino = inorder(tree2)
print(ino)
post_ = postorder(tree2)
print(post_)

# 例子四：
# 已知两种遍历序列确定二叉树。
# 任意两种遍历种只要包括中序，就能确定二叉树。
# 如，一个前序遍历和一个中序遍历，
# 前序遍历可以确定中序根的位置，➡又通过中序根左边的部分，确认前序遍历的左子树。
'''
用递归的方法 类似先序遍历 去重建二叉树。
'''
class Rebuild():
    def reconstructbinarytree(self,pre,tin):
        # 这个方法的目的是用于解决，写方法时参数内参数调用参数的问题。
        # pre: 前序遍历  list类型或者者str类型
        #  tin: 中序遍历
        return self.rebuild_tree(pre,0,len(pre)-1,tin,0,len(tin)-1)

    def rebuild_tree(self,pre,pre_start,pre_end,tin,tin_start,tin_end):
        # 类似先序遍历 去重建二叉树。
        if pre_start > pre_end or tin_start > tin_end:  # 基线条件。
            return None

        head = Node(pre[pre_start])
        tin_mid = tin.index(pre[pre_start])
        left_length = tin_mid - tin_start

        head.left = self.rebuild_tree(pre,pre_start+1,pre_start+left_length,
                                      tin,tin_start,tin_mid-1)
        head.right = self.rebuild_tree(pre,pre_start+left_length+1,pre_end,
                                       tin,tin_mid+1,tin_end)
        return head  # 每一个递归返回一个根结点，最后返回的是总的根结点。

def postorderprint(BT,list_=[]):
    if BT:
        postorderprint(BT.left)
        postorderprint(BT.right)
        list_.append(BT.data)
    return list_

pre = ['a', 'b', 'd', 'f', 'e', 'c', 'g', 'h', 'i']
tin = ['d', 'b', 'e', 'f', 'a', 'g', 'h', 'c', 'i']
R = Rebuild()
head = R.reconstructbinarytree(pre,tin)
print(postorderprint(head))  # 已知前序 中序 求后序。

