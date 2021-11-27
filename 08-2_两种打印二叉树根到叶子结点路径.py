
# 一、打印二叉树根到叶子结点路径

'''
           A
     B          C
  D     F    G     I
       E      H
'''
class Node():
    def __init__(self,data=None,L=None,R=None):
        self.data = data
        self.L = L
        self.R = R

# 打印二叉树根到叶子结点路径
def print_path(BT,path=[],re=[]):
    if BT:
        path.append(BT.data)
        if BT.L == None and BT.R == None: # 叶子结点。
            re.append(path.copy())
            # path.pop() 找到无子结点的就退出一个。上下为行文美观统一移到下方path.pop()。
        else:
            print_path(BT.L,path,re)
            print_path(BT.R,path,re)
            # path.pop() 遍历完两个子结点，退出一个。
        path.pop()  #为美观，统一到此处。
    return re

tree = Node('a', Node('b', Node('d'), Node('f', Node('e'))), Node('c', Node('g', None, Node('h')), Node('i')))
r = print_path(tree)
print(r)

# 二、打印二叉树左右边所标注的路径，左标0，右标1。
def print_0_1_path(BT,path=[],re=[],code_=None):
    if BT:
        path.append(code_)
        if BT.L == None and BT.R == None:
            re.append(path.copy())
        else:
            print_0_1_path(BT.L,path,re,code_='0')
            print_0_1_path(BT.R,path,re,code_='1')
        path.pop()
    return re

def result_0_1_path(BT):
    re = print_0_1_path(BT)
    result = []
    for r in re:
        r.pop(0)
        result.append(''.join(r))
    return result


r = result_0_1_path(tree)
print(r)
