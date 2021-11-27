# 先序遍历创建二叉树
class Node():
    def __init__(self,data=None,L=None,R=None):
        self.data = data
        self.L = L
        self.R = R
def Creat_tree(H,p=Node()):  # H 为list，利用list可变对象的特性。
    for i in range(len(H)):
        if H[0] == '#':
            H.pop(0)
            return None
        else:
            p.data = H.pop(0)
            p.L = Creat_tree(H,Node())
            p.R = Creat_tree(H,Node())
            return p

def inordertraversal(BT,list_=[]):
    if BT:
        inordertraversal(BT.L,list_)
        list_.append(BT.data)  # 或者直接print(BT.data)也可以。
        inordertraversal(BT.R,list_)
    return (list_)


H = ['A','B','C','#','E','D','#']
H = list('abc##de#g##f###')
tree = Creat_tree(H)
result = inordertraversal(tree)
print(result)
