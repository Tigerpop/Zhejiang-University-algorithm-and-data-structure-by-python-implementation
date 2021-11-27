'''
struct GNode
————————————————————
Nv  顶点数
Ne  边数
AdjList  G   邻接表
data[]  存在顶点的数据
————————————————————

输入格式
Nv Ne
v1 v2 Weight
...

A  -----   B
-  -       -   -
-    -     -      C
-       -  -         -
E  -----   D            F

'''

# 我这里没有完全按照老师的思路来写。
# 我把边视为点的一个附带属性。边这个属性也是一个类，内置类指针。
# 邻接表是个列表，元素为一个个链表实现的队列。
# 以后可以用更简单的方式来写，这里是故意写成类和链表的形式了。
class Node():
    def __init__(self,num,data=None):
        self.num = num
        self.data = data
        self.Edge = Edge(None,0)   # 指针就是边。

class Edge():
    def __init__(self,next,weight):
        self.next = next
        self.weight = weight

class Queue():
    def __init__(self,num):
        node = Node(num)
        self.front = node
        self.rear = node
    def add(self,num_item,weight): # 尾部加入。
        new_node = Node(num_item)
        self.rear.Edge = Edge(new_node,weight)
        self.rear = self.rear.Edge.next
    def show(self):
        list_ = []
        temp = self.front
        while temp:
            list_.append(temp.num)
            list_.append(' %0.2f'%temp.Edge.weight)
            list_.append('--> ')
            temp = temp.Edge.next
        print(list_)

class CreatGraph():
    def __init__(self,Nv=1,Ne=0,MaxVertexNum=6):
        self.Nv = Nv
        self.Ne = Ne
        self.G = [Queue(i) for i in range(MaxVertexNum)]
    # 初始化离散的点。之后每个离散的点连成链表的过程就是图构建的过程。
    def Insert(self,num,item,weight):
        self.G[num].add(item,weight)
    def show_Graph(self):
        for i in range(self.Nv):
            self.G[i].show()

def main():
    input_list = [
        [6,7],
        ['A','B',0.1],
        ['B','C',0.2],
        ['B','D',0.5],
        ['A','D',0.1],
        ['D','E',0.8],
        ['A','E',0.6],
        ['C','F',0.2]
    ]
    for i in range(1,len(input_list)):
        for j in range(2):
            if input_list[i][j] == 'A':
                input_list[i][j] = 0
            if input_list[i][j] == 'B':
                input_list[i][j] = 1
            if input_list[i][j] == 'C':
                input_list[i][j] = 2
            if input_list[i][j] == 'D':
                input_list[i][j] = 3
            if input_list[i][j] == 'E':
                input_list[i][j] = 4
            if input_list[i][j] == 'F':
                input_list[i][j] = 5
    introduce = input_list.pop(0)
    graph = CreatGraph(introduce[0],introduce[1])
    for e in input_list:
        graph.Insert(e[0],e[1],e[2])   # 无向图，插入两次。
        graph.Insert(e[1], e[0], e[2])
        print(e[0],e[1],e[2])
    graph.show_Graph()

if __name__ == '__main__':
    main()