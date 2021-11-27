'''
二叉树和度为2的树区别是 ： 二叉树有左右之分。

特殊二叉树：
1、斜二叉树。
2、完美二叉树（满二叉树）full binary tree。
3、完全二叉树 complete binary tree。
   完全二叉树 最下层的结点，可以右缺。
   也就是只要有结点，其编号就和完美二叉树一致。


二叉树的重要性质：
1、第i层最大结点数为：2^(i-1)。
2、深度为k的二叉树，最大结点总数为：2^(k) -1。   # 深度为3的二叉"树"有3层，但是最深的"结点"深度为0 1 2 为2。
3、n2 表示有两个子结点的结点个数，n1 为... 1个，n0 为... 0个。
则，n0 = n2 +1 。
因为：n0+n1+n2 - 1 = 边数 = 0*n0 +1*n1 +2*n2。


二叉树的遍历：
先序遍历--根、左、右。pre
中序遍历--左、根、右。in
后序遍历--左、右、根。post
层次遍历-- 从上到下，从左到右。level

虽然树 因为结构复杂不方便用顺序存储结构表示，
但是二叉树相对简单，特别是完全二叉树时，
若按照根开始编号哦，存储是可以连续的。
所以，完全二叉树我们也可以用连续存储结构表示。
1、除了根结点之外的所有父结点，结点编号都是"n/2"，其子结点编号为n。
2、结点编号n，它的左儿子编号是2n，右儿子编号是2n+1。

如果不是完全二叉树，是一般的二叉树，可一通过补充空位的方法，
然后按照完全二叉树一样的方法算。（浪费空间）
'''
# abdfecghi, 以下先用递归来实现。
# 先序遍历
class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def preordertraversal(BT,list_=[]):
    if BT:
        list_.append(BT.data) # 或者直接print(BT.data)也可以。
        preordertraversal(BT.left,list_)
        preordertraversal(BT.right,list_)
    return (list_)

def inordertraversal(BT,list_=[]):
    if BT:
        inordertraversal(BT.left,list_)
        list_.append(BT.data)
        inordertraversal(BT.right,list_)
    return list_

def postordertraersal(BT,list_=[]):
    if BT:
        postordertraersal(BT.left,list_)
        postordertraersal(BT.right,list_)
        list_.append(BT.data)
    return list_

# 使用堆栈，非递归遍历：

def main():
    # 直接通过链式结点建立树。tree其实可以视为一个node。
    tree = Node('a', Node('b', Node('d'), Node('f', Node('e'))), Node('c', Node('g', None, Node('h')), Node('i')))

    t_pre = preordertraversal(tree)
    print('先序遍历是： ',t_pre)
    t_in = inordertraversal(tree)
    print('中序遍历是：',t_in)
    t_post = postordertraersal(tree)
    print('后序遍历是：',t_post)

if __name__ == '__main__':
    main()


