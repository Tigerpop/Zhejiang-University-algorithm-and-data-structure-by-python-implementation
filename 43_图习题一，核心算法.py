'''
题意：
在距离权重最短的前提条件下，选择收费权重最小的路径。
计算0 到 3 的最优路径。

          (0)
    1\20      2\20
(1)      4\10      (2)
    2\30      1\20
          (3)

Sample Input  (v,w,distance_weight,charge_weight)
4 5 0 3
0 1 1 20
1 3 2 30
0 3 4 10
0 2 2 20
2 3 1 20


此题为 单源最短路径的变形：
    Dijkstra
    等距离时，按收费更新。


伪代码
在Dijkstra算法的基础上，将更新时的内容调整。

if dist[v] + E<v,w> < dist[w]:
    dist[w] = dist[v] + E<v,w>
    path[w] = v
    cost[w] = cost[v] + C<v,w>
elif (dist[v] + E<v,w> = dist[w]) and cost[v] + C<v,w> <cost[w] :
    cost[w] = cost[v] + C<v,w>
    path[w] = v
    # 此时dist没有变，所以不用改。
'''
class Graph():  # 稀疏矩阵 邻接表表示。
    def __init__(self,n_vertices):
        self.n_vertices = n_vertices
        self.G = [[] for _ in range(n_vertices)]
    def add_edge(self,pro_vertices,new_vertices,dist_weight,cost_weight):
        self.G[pro_vertices].append({new_vertices:(dist_weight,cost_weight)})
    def show_Graph(self):
        for i in self.G:
            print(i)
graph = Graph(4)
graph.add_edge(0,1,1,20)   # (v,w,distance_weight,charge_weight)
graph.add_edge(0,2,2,20)
graph.add_edge(0,3,4,10)
graph.add_edge(1,3,2,30)
graph.add_edge(2,3,1,20)
graph.show_Graph()

class data():
    def __init__(self,Vertex_num):
        self.dist = [float('inf') for _ in range(Vertex_num)]
        self.cost = [0 for _ in range(Vertex_num)]
        self.path = [-1 for _ in range(Vertex_num)]
        self.collected = [False for _ in range(Vertex_num)]
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
                [(dist_weight,cost_weight)] = [value for dic in graph.G[v] for key,value in dic.items() if key == w]
                if data.dist[w] > data.dist[v] + dist_weight:
                    data.dist[w] = data.dist[v] + dist_weight
                    data.cost[w] = data.cost[v] + cost_weight
                    data.path[w] = v
                elif (data.dist[w] == data.dist[v] + dist_weight \
                    and data.cost[w] > data.cost[v] + cost_weight):
                    data.cost[w] = data.cost[v] + cost_weight
                    data.path[w] = v
        print(data.dist,'改变成的dist')

def Find_Smallest_Dist(s,data):
    data.dist[s] = 0
    uncollected_list = [i for i in range(len(data.dist)) if data.collected[i] == False]
    print(uncollected_list,'没收集到!!!')
    for i in uncollected_list:  # 运行到 uncollected_list == []时，会自动停止，无返回值。
        if data.dist[i] == min([data.dist[i] for i in uncollected_list]):
            print(i,'   没收集的最小dist对应位置')
            print(data.dist[i],'   没有收录的最小dist值')
            return i

def near_Node(v):
    near_Node = [key for dic in graph.G[v] for key in dic]
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

if __name__ == '__main__':
    d = data(4)
    Dijkstra(0,d)
    print(d.path)
    print('\n从0 到3 的最优路径为：')
    path_Smallest(3,d)
    print('总的dist为：%d'%d.dist[3])
    print('总的cost为：%d'%d.cost[3])