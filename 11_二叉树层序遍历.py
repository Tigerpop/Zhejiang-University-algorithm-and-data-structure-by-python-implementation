'''
二叉树是二维结构，遍历后变成一维结构。
遍历方法不同，一维数组顺序不同。
之前用栈来保存根结点，实现来先、中、后序排列，
现在用队列来保存right结点，来实现层序遍历。

所谓层序，就是 一层一层访问。
层序遍历思想：
====
根 入 队列，
left right 入队列，
根出队列，
====
left -> left.left left.right 两个入队列，
right -> right.left right.right 两个入队列，
left right 两个出队列，
====
...以此类推。
'''
class Queue():
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.q_data = []
    def add(self,data):
        self.rear += 1
        self.q_data.append(data)
    def out(self):
        if self.front == self.rear:
            print('队列已经空了。')
            return
        out_item = self.q_data.pop(0)
        self.rear -= 1
        return out_item
    def out_all(self):
        list_ = []
        while self.front != self.rear:
            list_.append(self.out())
        return list_

class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def levelordertraversal(BT):
    list_ = []
    if BT == None:
        return '树是空的'
    q = Queue()
    q.add(BT)
    while q.front!=q.rear :
        out_item = q.out_all()
        for BT in out_item:
            list_.append(BT.data)  # 输出。
            if BT.left:
                q.add(BT.left)
            if BT.right:
                q.add(BT.right)
    return list_


def main():
    tree = Node('a', Node('b', Node('d'), Node('f', Node('e'))), Node('c', Node('g', None, Node('h')), Node('i')))
    levelorder = levelordertraversal(tree)
    print('层序遍历：',levelorder)

if __name__ == '__main__':
    main()