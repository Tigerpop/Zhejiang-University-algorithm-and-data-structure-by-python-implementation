'''
       (v1)     2->     (v2)
   4->     1->      3<-       10->
(v3)   2<-     (v4)     2->     (v5)
    5->      8<-      4->       6<-
       (v6)     1<-     (v7)

'''
# 有向有权图的简单构建。
class Graph():
    def __init__(self,n_vertices):
        self._n_vertices = n_vertices
        self.G = [[] for _ in range(self._n_vertices)]
    def add_edge(self,pro_vertices,new_vertices,edge_weight):
        self.G[pro_vertices].append({new_vertices:edge_weight})
        # self.G[new_vertices].append({pro_vertices: edge_weight}) 若为无向图需要加上此步骤
    def show_Graph(self):
        for i in range(self._n_vertices):
            print(self.G[i])
graph = Graph(7)
graph.add_edge(0,1,2)
graph.add_edge(0,3,1)
graph.add_edge(1,3,3)
graph.add_edge(1,4,10)
graph.add_edge(2,0,4)
graph.add_edge(2,5,5)
graph.add_edge(3,2,2)
graph.add_edge(3,4,2)
graph.add_edge(3,5,8)
graph.add_edge(3,6,4)
graph.add_edge(4,6,6)
graph.add_edge(6,5,1)
graph.show_Graph()
'''
一个非常有趣的假设，假如线路上有负值，那会出现沿着一个闭环循环negative-cost-cycle，花销出现负无穷。
只要出现了这样的 negative_cost_cycle ,所有总花销最小化的的算法都挂掉。



" Dijkstra 算法 "
    S 为 { 源点s + 已经确定了最短路径的顶点vi} 集合
    对任意未收录的顶点v ，定义dist[v] 为s 到 v 最短路径的长度，但是该路径为仅经过集合S中的顶点，
    {s --> (vi属于S) --> v }的最小长度。
    
    若路径是按照递增（不会出现 假如线路上有负值） 顺序生成的：
   （S 按照 dist[vi] 大小从小到大 收录 这些点进 S 集合的）：
        1、真正的最短路径必须是只经过S集合中的顶点。（为什么？）这个可以反证，...假如经过了集合外的点w...。
        2、每次从未收录的顶点中选一个dist 最小的v收录。（贪心）
        3、增加一个v进入S集合，可能影响另外一个（S集合外）w 的dist值！
            一、如果 因为加入 v 而导致dist[w] 变小的话，那v 一定在 s 到 w 的路径上。
            二、如果 加入v 而导致 w的 dist[w] 变化的话，那v 与 w 一定有一条直接的边。
                二的证明（反证）：
                    假定 加入v 而导致 w的 dist[w] 变化，v 与 w 之间还有点 v·。
                    v 是新加入S集合 的，所以dist[v]是S中最大的，
                    若v -- w之间还有结点v·，
                    则 dist[v] > dist[v·]
                       s --> ... --> v --> v· --> w 路径长度一定大于或等于
                       dist[v] + v· 
                       s --> ...-->  v· --> w 的路径长度
                       dist[v·]
                    加 v 就并不能改变 dist[w],因为加 v 不影响 w 在S集合内的最短路径。
                    所以假定错误，v 与 w之间没有顶点，而是直接边连接。
            增加一个 v 进入S ，影响的只是 v 邻接的这一圈 结点 ，有可能让dist[w]变小。
            综合一和二：
                若加入 v 点，邻接点w（w是S集合外的顶点）而言，dist[w] 无影响，则还是dist[w],若有影响就是 dist[v] + <v,w>weight。
                dist[w] = min( dist[w] , dist[v] + <v,w>weight ) # w 为 v 的邻接点。
                    
    在 Dijkstra 算法 中，未被访问过的点的 dist[w] 不能被定义为-1，而要被定义为+∞，
    因为，dist[w] = min( dist[w] , dist[v] + <v,w>weight ) 
    这一步可能需要对未访问的点比大小，如果被定义为-1，那未被访问的 dist[w]始终要比dist[v] + <v,w>weight 小，因为它是负数。
    
Dijkstra 算法伪代码：
# 这里图的 边的权重都是非负数。如果有负边，以下不成立。
void Dijkstra(Vertex s):
    while 1:
        v = 未收录顶点中dist 最小者
        if 这样的v不存在：
            break
        collected[v] = True
        for v 的每个邻接点 w:
            if collected[w] == False:
                if dist[v] + <v,w>weight < dist[w]:
                    dist[w] = dist[v] + <v,w>weight
                    path[w] = v   # 添加路径。
                    
                    
    未收录顶点中dist 最小者
    方法1：直接扫描所有未收录的顶点 O(V),
        T = O(V**2 + E)   对稀疏图效果好，（边的条数|E|远小于|V|²）的图称为稀疏图
        # 每一个点被收录 要外循环v次，每个点还要扫描一遍路径又是O(V)的循环，把边加进去是E 。
    方法2：将dist存在 最小堆 中 O(logV)
        为了每次能够快速找到最短的dist，我们用最小堆存储数组。
        每次弹出根结点，然后调整最小堆。O(logV)
        更新dist[w]，插回最小堆去。   O(logV)
        T = O( VlogV + ElogV )   对稠密图效果好 E V**2 是同一个数量级 。条数|E|接近|V|²，称为稠密图（dense graph）
        T = O( ElogV ) 
'''
'''
data
下标   1  2  3  4  5  6  7
dist  +∞ +∞ +∞ +∞ +∞ +∞ +∞
path  -1 -1 -1 -1 -1 -1 -1
colle  F  F  F  F  F  F  F

data
下标   1 2 3 4 5 6 7
dist  0 2 3 1 3 6 5
path -1 1 4 1 4 7 4
colle T T T T T T T 
回溯一遍path的路径就可以找到 最暖路径。
'''
class data():
    def __init__(self,Vertex_num):
        self.dist = [float('inf') for _ in range(Vertex_num)]
        self.path = [-1 for _ in range(Vertex_num)]
        self.collected = [False for _ in range(Vertex_num)]
# 主要算法
def Dijkstra(s,data):  # s 是起始结点位置。
    while 1:
        v = Find_Smallest_Dist(s,data)
        if v == None:
            return '最短路径构建结束',data
        data.collected[v] = True  # 收录结点
        for w in near_Node(v):   # 影响未收录的相邻结点
            if data.collected[w] == False:
                # 找出v-->w 边对应权重。
                [weight_v_w] = [value for dic in graph.G[v] for key,value in dic.items() if key == w]
                if data.dist[w] > data.dist[v] + weight_v_w:
                    data.dist[w] = data.dist[v] + weight_v_w
                    data.path[w] = v
        print(data.dist,'改变成的dist')


def Find_Smallest_Dist(s,data):
    data.dist[s] = 0
    uncollected_list = [i for i in range(len(data.dist)) if data.collected[i] == False]
    print(uncollected_list,'没收集到!!!')
    # if uncollected_list == []:
    #     return None
    for i in uncollected_list:   # 运行到 uncollected_list == []时，会自动停止，无返回值。
        if data.dist[i] == min([data.dist[i] for i in uncollected_list]):
            print(i,'   没收集的最小dist对应位置')
            print(data.dist[i],'   没有收录的最小dist值')
            return i

def near_Node(v):
    near_Node = [key for dic in graph.G[v] for key in dic]
    return near_Node

def path_Smallest(v): # 查找任意点的路径需要一个栈完成逆序输出。
    list_in = []
    list_out = []
    while v != -1:
        list_in.append(v)
        v = data.path[v]
    for i in range(len(list_in)):
        list_out.append(list_in.pop())
    print(list_out)

if __name__ == '__main__':
    data = data(7)
    Dijkstra(0,data)
    print('\n\n','dist',data.dist)
    print('path',data.path)
    print('collected',data.collected)

    print('输出最短路径')
    path_Smallest(5)
