'''
hash问题的逆问题
    题目：
    已知 h(x) = x % N 以及用线性探测解决冲突。
    先给出散列映射的结果，
    反求输入的顺序。

    关键：当处理的元素之间有非常明确的 前后顺序关系时，要联想到"拓扑排序"。

    分析：
        x 被映射到了h(x)位置，发现这个位置已经有了y，则 y 一定是在 x 之前被输入的。
        比如如下散列表的存储情况：
        h(key) = key mod 11
        --------------------------------------------------------
        下标    0   1   2   3   4    5    6    7    8    9    10
        h(key) 33  1   13   12  34   38   27   22   32   _    21
        --------------------------------------------------------
        我们可以看出33 有可能是第一个输入的，1 有可能是第一个输入的，13可能是第一个输入的，
        38、21 也可能是第一个输入，

        但是 12 原本应该放进1号位置，而实际上被放进了3号位置，说明12一定是在1 后面输入的。
        用线性探测的方式处理位置冲突，找下一个位置，
        此时 12 原本应该放进2号位置，但是2号位置已经放了13，说明12一定在13之后输入。
        (1->3,2->3)

        34原本应该放在1号位置，同以上推理，34 一定在1、13、12之后输入。
        (1->4,2->4,3->4)

        27 一定在38之后输入(5->6)

        22 一定在33、1、13、12、34、38、27、之后输入 (0,1,2,3,4,5,6 -> 7)

        32 一定在其它所有元素 之后输入 (去掉None以后看，0,1,2,3,4,5,6,7,9 ->8)

        以上关系可以用结点的链表形式表现出来。

        但是有一点需要注意：
        如果按从小到大的输入，第一个是1 第二个是13， 第三个不是在深度为0的结点找，
        在确定1 和 13 为前两位输入之后， 应该从"入度"为0 角度考虑，接下来的一位是从33 12 38 21 这四个之中找。
        考虑的是结点的入度而不是深度。

        回顾之前学习过的知识，
        在构建完结点的链表关系以后，按照结点的指针关系排好输入的顺序，以上的排序过程，就是《拓扑排序》，可以回顾《41拓扑排序》。

程序框架
def main():
    根据已有的哈希表构建图
    根据图拓扑排序
'''
class Graph():  # 邻接表表示的图，用一个数组存储入度信息。
    def __init__(self,n_vertices,data):
        self._n_vertices = n_vertices
        self.G = [[] for _ in range(self._n_vertices)]
        self.data = data(n_vertices)
    def add_edge(self,pro_vertices,new_vertices,edge_weight):
        self.G[pro_vertices].append({new_vertices:edge_weight})
        self.data.indegree[new_vertices] += 1
    def show_Graph(self):
        for i in range(self._n_vertices):
            print(self.G[i])
        print('入度的list为：\n',self.data.indegree)
class data():
    def __init__(self,n_vertices):
        self.indegree = [0 for _ in range(n_vertices)]

def hash(key):
    return key%11

def CreatGraph(hash_table):
    node_input = [x for x in hash_table if x != None]    # 去除空位置，方便图结点与输入的元素一一对应。
    # 为了方便后面入度都为0时按照值的大小从小到大输出，这里提前把输入顺序按值从小到大排好。
    node_input = sorted(node_input)
    graph = Graph(len(node_input),data)                        # 非空的就做成结点。
    for key_i in range(len(node_input)):
        key = node_input[key_i]
        shoud_i = hash(key)
        di = 1                                                 # 线性探测 的di 从1到tablesize。
        while hash_table[shoud_i] != key:                     # 找适合的位置，并完善图的构建。
            # hash_table[shoud_i] 映射在node_input 中的编号,有可能有多个一样的数。
            shoud_i_change = [i for i in range(len(node_input)) if node_input[i]==hash_table[shoud_i]]
            graph.add_edge(shoud_i_change.pop(),key_i,1)
            shoud_i = (di+shoud_i)%len(hash_table)
            di = +1
    graph.show_Graph()
    return graph,node_input

def TopSort(graph,node_input):
    def near_Node(v,list_key=[]):
        if graph.G[v] != []:
            list_key = [key for dic in graph.G[v] for key in dic.keys()]
        return list_key
    Q = []
    out = []
    count = 0
    for v in range(len(graph.G)):
        if graph.data.indegree[v] == 0:
            Enqueue(v,Q)
    print(Q)
    while IsEmpty(Q) == False:
        v = Dequeue(Q)
        out.append(v)
        print(v,'结点正在处理')
        count += 1
        for w in near_Node(v):
            graph.data.indegree[w] -= 1
            if graph.data.indegree[w] == 0:
                Enqueue(w,Q)
    if count != len(graph.G):
        return '图中有回路，无法拓扑序。'
    print(out)
    out_list = []
    for i in out:
        out_list.append(node_input[i])
    print('反推出来的输入顺序是：\n',out_list)

def Enqueue(v,Q):
    Q.append(v)
def Dequeue(Q):
    return Q.pop(0)
def IsEmpty(Q):
    return len(Q) == 0

def main():
    hash_table = [33, 1, 13, 12, 34, 38, 27, 22, 32, None, 21]
    g,n = CreatGraph(hash_table)
    TopSort(g,n)

if __name__ == '__main__':
    main()