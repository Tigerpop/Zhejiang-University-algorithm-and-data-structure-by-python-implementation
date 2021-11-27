'''
Dijkstra 变形。
一题意：
    要求数 最短路径 有多少条。

    count[s] = 1
    (v的加入对w点而言)
    如果找到更短的路径： count[w] = count[v]
                       # 原有 count[w] 作废，被替代。
                       # 对dist[w]更新，此时v-w就在最短路径上，
                       # 最短路径数量就是之前v的最短路径数量。
    (对w点而言)
    如果找到等长的路径： count[w] += count[v]
                       # 这里是易错点，不是count[w] = count[v] + 1
                       # 因为w 和 v之间是只有一条路没错，但是count[v]可能是许多条路径，
                       # 所以 v 带给 w 的最短路径 数量的增加，是count[v] 条，而不是1 条。
                       # 所以 是在 count[w] 原有基础上 增加 count[v] 条最短路径。
二题意：
    要求边数最少的最短路径。

    严格说，这个问题，在之前已经被解决过了。
    我们在Dijkstra的dist变化方法不变的前提下，设置count来专门计数边的数量，而不像dist一样记录边的权重。

    count[s] = 0
    如果找到更短的路径： count[w] = count[v] + 1  # v-w 在最短路径上。
    如果找到等长路径：   count[w] = count[v] + 1  老师说错了，不需要改变。
                       count[w] 不做改变，就可以了。
'''

'''
       (v0)    2    (v1)
     1     1      1       9
(v2)    2    (v3)     10    (v4)  5  (v7)
     5      8      4      6
       (v5)    1     (v6)

'''
# ***********************************************************************************************

# Number of paths
# Number of edges

class Graph():
    def __init__(self,n_vertices):
        self.n_vertices = n_vertices
        self.G = [[float('inf') for _ in range(n_vertices)] for _ in range(n_vertices)]
    def add_edge(self,pro_vertices,new_vertices,edge_weight):
        self.G[pro_vertices][new_vertices] = edge_weight
        self.G[new_vertices][pro_vertices] = edge_weight
    def show_Graph(self):
        for i in self.G:
            print(i)
graph = Graph(8)
graph.add_edge(0,1,2)
graph.add_edge(0,3,1)
graph.add_edge(1,3,1)
graph.add_edge(1,4,9)
graph.add_edge(2,0,1)
graph.add_edge(2,5,5)
graph.add_edge(3,2,2)
graph.add_edge(3,4,10)
graph.add_edge(3,5,8)
graph.add_edge(3,6,4)
graph.add_edge(4,6,6)
graph.add_edge(6,5,1)
graph.add_edge(4,7,5)
graph.show_Graph()
print('    \n')

class data():
    def __init__(self,Vertex_num):
        self.dist = [float('inf') for _ in range(Vertex_num)]
        self.path = [-1 for _ in range(Vertex_num)]
        self.collected = [False for _ in range(Vertex_num)]
        self.Number_of_edges = [0 for _ in range(len(graph.G))]
        self.Number_of_pages = [1 for _ in range(len(graph.G))]
# Dijkstra
def Dijkstra(s,data):  # s 是起始结点位置。
    while 1:
        v = Find_Smallest_Dist(s,data)
        if v == None:
            return '最短路径构建结束',data
        data.collected[v] = True  # 收录结点
        for w in near_Node(v):   # 影响未收录的相邻结点
            if data.collected[w] == False:
                # 找出v-->w 边对应权重。
                dist_weight = graph.G[v][w]
                if data.dist[w] > data.dist[v] + dist_weight:
                    data.dist[w] = data.dist[v] + dist_weight
                    data.path[w] = v
                    data.Number_of_edges[w] = data.Number_of_edges[v] + 1
                    data.Number_of_pages[w] = data.Number_of_pages[v]
                elif data.dist[w] == data.dist[v] + dist_weight:
                    data.Number_of_pages[w] += data.Number_of_pages[v]
        print(data.dist,'改变成的dist')

def Find_Smallest_Dist(s,data):
    data.dist[s] = 0
    uncollected_list = [i for i in range(len(data.dist)) if data.collected[i] == False]
    print(uncollected_list,'没收集到!!!')
    for i in uncollected_list:      # 运行到 uncollected_list == []时，会自动停止，无返回值。
        if data.dist[i] == min([data.dist[i] for i in uncollected_list]):
            print(i,'   没收集的最小dist对应位置')
            print(data.dist[i],'   没有收录的最小dist值')
            return i

def near_Node(v):
    near_Node = [w for w in range(len(graph.G[v])) if graph.G[v][w] != float('inf') ]
    return near_Node

def path_Smallest(v,data): # 查找任意点的路径需要一个栈完成逆序输出。
    list_in = []
    list_out = []
    while v != -1:
        list_in.append(v)
        v = data.path[v]
    for i in range(len(list_in)):
        list_out.append(list_in.pop())
    print(list_out)
    return list_out

d = data(8)
Dijkstra(0,d)
print(d.dist)
p = path_Smallest(5,d)
print('0到5的最短路径为',p)
print('从0点到各个点的边数，做成列表是：',d.Number_of_edges)
print('从0点到各个边的路径数，做成列表是：',d.Number_of_pages)
