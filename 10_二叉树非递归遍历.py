'''
二叉树非递归遍历，栈实现。

'''
# **********************************************
class Creatstack():
    def __init__(self):
        self.stack = []
        self.top = -1
    def Isempty(self):
        return self.top == -1
    def push(self,data):
        self.stack.append(data)
        self.top += 1
    def pop(self):
        if self.Isempty():
            raise Exception('stack is empty')
        else:
            d = self.stack.pop()
            self.top -= 1
            return d
    def show_top(self):
        if self.top != -1:
            temp = self.stack[self.top]
            return temp
        else:
            return None
class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

# **********************************************

# 中序遍历。
# 遇到一个结点，入栈，遍历它的左子树。
# 左子树遍历结束后，从栈顶弹出结点并访问。
# 按右指针中序遍历它的右子树。也是入栈，左子树没有就出栈。
# 利用栈，非递归中序遍历
def inordertraversal(BT):
    list_ = []
    S = Creatstack()
    while(BT or S.Isempty()!=True): # 树和栈都清空才行。
        # 1、向左遍历入栈 2、左空出栈 3、转右重复之前操作。
        while(BT):
            S.push(BT)   #（第一次遇见）（直接存入结点，而不是存结点data）。
            BT = BT.left # 这个内部while一次入栈完毕时，BT是None。
        # 此时BT.left为空（左）。
        # 把栈中的BT结点出栈（中）。
        # 右边重复中序遍历（右）。
        if(S.Isempty() !=True ):
            BT = S.pop()#(第二次遇见) 重定义BT。若BT.right空，大循环再运行，跳过入栈在此再次出栈。
            list_.append(BT.data)
            BT = BT.right    # 此时BT可能是None。若为None则跳过上面的入栈循环。
    return list_

# 先序中序后序 总路径是一样的，只是输出顺序不同。
# 中序遍历就是（第二次遇见）输出。
# 先序遍历就是（第一次遇见）输出。
# 以下为非递归先序遍历。
def preordertraversal(BT):
    list_ = []
    S = Creatstack()
    while(BT or S.Isempty()!=True):
        while BT:
            S.push(BT)  # (第一次遇见)
            list_.append(BT.data)
            BT = BT.left
        if S.Isempty()!=True:
            BT = S.pop()
            BT = BT.right
    return list_

# 非递归的后序遍历，要求在left为空且right也为空的时候输出。
# 还是强调一遍，路径是一样的。
# 但是一个结点在left和right均为空，或(第二次在栈顶)，才会输出。

# 思路一：
# 从结点是否被经过一次的角度设计，可以利用动态添加标签属性完成。
def postordertraversal(BT):
    list_ = []
    S = Creatstack()
    while(BT or S.Isempty()!=True):
        while BT:
            S.push(BT)
            BT.first_ = True # 动态添加属性到对象中（用于确认是否第一次在栈顶）
            BT = BT.left
        if S.Isempty()!=None:
            BT = S.show_top()
            if (BT and BT.first_==True ):
                BT.first_ = False # 有一个向右找的动作时，其实就过了次"根"了。
                BT = BT.right
            else:
                list_.append(S.pop().data)
                BT = None
    return list_

# 非递归后序遍历。
# 思路二：
# 确认右边是不是被处理完毕了。
''' 补充说明。
a = Node('a')
b = a
b.data = 'b'
print(a.data)   输出 b    # 可见结点 可变。
'''
def postordertraversal_2(BT):
    list_ = []
    S = Creatstack()
    while (BT or S.Isempty()!=True):
        while BT:
            S.push(BT)
            BT = BT.left
        if S.Isempty()!= True:
            BT = S.show_top()
            # print(BT.right)
            if BT.right == None or BT.right.data == None:
                list_.append(S.pop().data)
                BT.data = None
                BT = None    # 注意链表中删除某个结点并不是  结点= None,所以树的结构没有变。
            else:
                BT = BT.right
    return list_

# 改进第二种后序遍历方法，不改变原树，也动态添加一个属性，有点像第一种打标签方法了。
def postordertraversal_2_1(BT):
    list_ = []
    S = Creatstack()
    while (BT or S.Isempty()!=True):
        while BT:
            S.push(BT)
            if BT.right:
                BT.right.over = False
            BT = BT.left
        if S.Isempty()!= True:
            BT = S.show_top()
            # print(BT.right)
            if (BT.right == None or BT.right.over == True):
                list_.append(S.pop().data)
                BT.over = True
                BT = None    # 注意链表中删除某个结点并不是  结点= None,所以树的结构没有变。
            else:
                BT = BT.right
    return list_

'''
简要总结：
不管是先序中序还是后序，路径其实是一样的，就是处理的时机不同。
1、非遍历的先序遍历是：
"第一次见面" 入栈的时候，就（处理）。
然后左入栈，入完开始出栈，出一个就指向右边一次，重复前面操作。
2、非遍历的中序遍历是：
"第二次见面"，出栈时（处理）。
左入栈操作，入完开始出栈，出栈便（处理），处理完一个，就指向右边一次，重复前面操作。
3、非遍历的后序遍历是：
思路一：（标签确定是此结点是不是已经被经过一次了）
左入栈完毕，回到根结点，识别标签，
（若无标签，不做处理，指向右边、打标签），  # 注意：指向右边、打标签。
（若有标签表示曾经来过栈顶，开始处理，继续弹出。）
思路二：（确认右边的结点都被处理过了）
'''


if __name__ == '__main__':
    tree = Node('a', Node('b', Node('d'), Node('f', Node('e'))), Node('c', Node('g', None, Node('h')), Node('i')))

    Inorder = inordertraversal(tree)
    print('中序遍历结果是：',Inorder)

    Preorder = preordertraversal(tree)
    print('先序遍历结果是：',Preorder)

    Postorder = postordertraversal(tree)
    print('后序遍历结果是：',Postorder)

    Postorder_2 = postordertraversal_2(tree)
    print('第二种思路后序遍历结果是：',Postorder_2)

    # 因为第二种解法改变了树的存储内容，再先序遍历，输出都为空了。
    Preorder = preordertraversal(tree)
    print('先序遍历结果是：',Preorder)

    tree = Node('a', Node('b', Node('d'), Node('f', Node('e'))), Node('c', Node('g', None, Node('h')), Node('i')))

    Postorder_2_1 = postordertraversal_2_1(tree)
    print('改进后的第二种思路后序遍历结果是：',Postorder_2_1)