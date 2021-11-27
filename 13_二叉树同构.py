'''
给定两颗树，t1、t2，如果t1可以通过若干次左右孩子交换变成t2， 两颗树就是"同构"的。

这里是二叉树的新的表示方式，不一定从根结点开始，
只表示左右孩子的结点编号，
而结点编号不一定是按照根结点开始层序遍历排的。

'''
'''
之前我们都是用链表表示二叉树，这里我们用顺序结构list 表示二叉树。
结构数组表示二叉树：(静态链表)。-1表示为None
       A| B | C | D
left  -1| 2 | -1| -1
right  1| 3 | -1| -1
编号： 0   1   2   3
等价于：
       B| A |   | D | C
left   4| -1|   | -1| -1
right  3| 0 |   | -1| -1
编号： 0   1   2   3  4

" left 和 right 中没有出现的编号，就是根结点的编号 。 "

（静态链表）有链表的灵活性，又存放在顺序存储结构的数组中。并非指针指向下一个结点。
'''
'''
思路：
1、二叉树的表示。
2、建立二叉树。(静态链表构建二叉树就是找出根结点。)
3、同构判别。
     
程序框架搭建：
main:
    r1 = buildtree(t1)
    r2 = buildtree(t2)
    if isomorphic(r1,r2):
        print('true')
'''

class Node():
    def __init__(self,element,left=None,right=None):
        self.element = element
        self.left = left
        self.right = right

def buildtree(BTlist):  # 找根。
    check = [None] * len(BTlist)
    for i in range(len(BTlist)):
        check[i] = 0
    for i in range(len(BTlist)):
        if BTlist[i] == None:
            check[i] = 1
            print('这里是： 空',i)
            continue
        element = BTlist[i].element
        left = BTlist[i].left
        print(left,'第多少次',i)
        right = BTlist[i].right
        if left[0]!='-':
            BTlist[i].left = int(left)
            check[BTlist[i].left] = 1     # 有被当成左孩子，就给这个位置打标记1。
        else:
            BTlist[i].left = None
        if right[0]!='-':
            BTlist[i].right = int(right)
            check[BTlist[i].right] = 1    #有被当成右孩子，就给这个位置打标记1。
        else:
            BTlist[i].right = None
    for i in range(len(BTlist)): # 根结点不会被当作孩子，所以标记还是0。
        if check[i] == 0:
            root = i
    return root

def isomorphic(t1,t2,r1,r2):
    if r1==None and r2 == None:  #both empty
        return 1
    if ((r1==None and r2!=None) or (r1!=None and r2 ==None)):
        return 0    # one of them is empty
    if t1[r1].element!=t2[r2].element:
        return 0    # root are different
    if t1[r1].left == None and t2[r2].left == None: # both have no left subtree
        return isomorphic(t1,t2,t1[r1].right,t2[r2].right)

    #  no need to swap the left and the right
    if (t1[r1].left!=None and t2[r2].left!=None) and (t1[t1[r1].left].element == t2[t2[r2].left].element):
        return (isomorphic(t1,t2,t1[r1].left,t2[r2].left) and isomorphic(t1,t2,t1[r1].right,t2[r2].right))
    #  need to swap the left and zhe right
    else:
        return isomorphic(t1,t2,t1[r1].left,t2[r2].right) and isomorphic(t1,t2,t1[r1].right,t2[r2].left)


bt_list = []
bt_list.append(Node('B','4','3'))
bt_list.append(Node('A','-1','0'))
bt_list.append(None)
bt_list.append(Node('D','-1','-1'))
bt_list.append(Node('C','-1','-1'))
bt_list_2 = []
bt_list_2.append(Node('B','4','3'))
bt_list_2.append(Node('A','-1','0'))
bt_list_2.append(None)
bt_list_2.append(Node('D','-1','-1'))
bt_list_2.append(Node('C','-1','-1'))

r1 = buildtree(bt_list)
r2 = buildtree(bt_list_2)
if isomorphic(bt_list,bt_list_2,r1, r2):
    print('两颗树为同构。')