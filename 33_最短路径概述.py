'''

单源 最短路径问题：
    从固定点出发，求其到其它所有点的距离。
    1、有向 无权图
    2、有向 有权图

多源 最短路径问题：
    求任意两点之间的最短距离。 # 注意最后输出不是两个点之间的最短距离，而是图中所有的两个点之间的最短路径，是很多个输出。

    笨办法 是把 "单源最短路径"问题重复结点次，来实现"多源最短路径"问题求解。

'''
'''
无权图 的单源 有向最短路径算法 ，

dist[w] = s 到 w 的最短距离 
dist[s] = 0
dist[] = 负数   #当visited 用。

path[w] = s 到 w 的路上经过的点。

void Unweighted(Vertex s):
    Enqueue(s,q)
    while !IsEmpty(q):
        v = Dequeue(q)
        for v 的邻接点 w:
            if dist[w] == -1:   # 等于起到了 visited的作用。
                dist[w] = dist[v] +1
                path[w] = v
                Enqueue(w,q)

'''
'''
以下还是用了全部双向的图，如果要改有向图，仅仅需要将add_edge()方法减少一个加边的赋值操作即可。
A(0)----- B(1)
-  -       -   -
-    -     -    C(2)
-       -  -       -
E(4)----- D(3)       F(5)
'''
# 上一节课用很繁琐的方法表示了邻接表，现在用简单的办法表示。
# 表示起来和上节课有一点不一样，上节课的 表内的每一条链表，链表第一个元素都是本结点。
# 这次我们用网上更多人用的方式，邻接表直接不包含 本结点。
class Graph():
    def __init__(self,n_vertices):
        self._n_vertices = n_vertices
        self.G = [[] for _ in range(self._n_vertices)]
    def add_edge(self,pro_vertices,new_vertices,edge_weight):
        self.G[pro_vertices].append({new_vertices:edge_weight})
        self.G[new_vertices].append({pro_vertices: edge_weight})
    def show_Graph(self):
        for i in range(self._n_vertices):
            print(self.G[i])

graph = Graph(6)
graph.add_edge(0,1,0.1)
graph.add_edge(1,2,0.2)
graph.add_edge(1,3,0.5)
graph.add_edge(0,3,0.1)
graph.add_edge(3,4,0.8)
graph.add_edge(0,4,0.6)
graph.add_edge(2,5,0.2)
graph.show_Graph()
print('_________\n')
'''
[{1: 0.1}, {3: 0.1}, {4: 0.6}]
[{0: 0.1}, {2: 0.2}, {3: 0.5}]
[{1: 0.2}, {5: 0.2}]
[{1: 0.5}, {0: 0.1}, {4: 0.8}]
[{3: 0.8}, {0: 0.6}]
[{2: 0.2}]
'''
# 修改字典（dicta.pop(key)或dicta.append(value)）进行迭代，这会导致结果 KeyError: 1
# 字典value为list，deepcopy 后，循环添加新的  键值对，会出现None的情况，
# python正确写法，需要用dic.setdefault(key,[]).append(value)写法。
dist = [-1 for _ in range(6)]
def Unweight_Shortest_Path(v):
    path = {v:[]}
    dist[v] = 0
    Q = Queue()
    Q.Enqueue(v)
    while Q.IsEmpty() == False:
        v = Q.Dequeue()
        for w in near_Node(v):
            if dist[w] == -1 :
                Q.Enqueue(w)
                dist[w] = dist[v] + 1   # 每往外围走一步，路程在上个结点基础上+1。
                path.setdefault(w,path[v].copy()).append(v) # 每一次都是在母结点路径基础上，再添加母结点。python写法中dict添加新的键值对这样写最好。避免踩坑。
    return dist,path

def near_Node(v): # 邻接表中的临近点，就是一条链上的点。
    list_ = []
    for i in graph.G[v]:
        for w in i.keys():
            list_.append(w)
    return list_

class Queue():
    def __init__(self):
        self.data = []
    def Enqueue(self,v ):
        self.data.insert(0,v)
    def Dequeue(self):
        return self.data.pop()
    def IsEmpty(self):
        return len(self.data ) == 0
'''
A(0)----- B(1)
-  -       -   -
-    -     -    C(2)
-       -  -       -
E(4)----- D(3)       F(5)
'''
if __name__ == '__main__':
    print('以C为源点，到各个点的path为：')
    source_Vertex = 4
    (d,p) = Unweight_Shortest_Path(source_Vertex)
    print('源点%d 到各个vertex的距离按结点号排序为：\n%s'%(source_Vertex,d))
    print('源点%d 到各个点最短路径依次为：\n%s'%(source_Vertex,p))
