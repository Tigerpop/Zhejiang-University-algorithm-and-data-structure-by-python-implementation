'''
用最小的代价连接图所有的点

图的最小生成树
Minimum Spanning Tree

树 ：
    无回路
    v个顶点v-1条边
生成树：
    包含了全部顶点
    v-1条边都在图里
最小生成树：
    边的权重和是最小的
    向生成树加任意一条边都会构成回路
'''
'''
此题 贪心算法
    "贪"： 每一步都要最"好"的。
    "好"： 权重最小的边。
    
    约束条件
    只能用图里有的边
    只能正好用掉v-1条边
    不能有回路
'''
'''
Prim贪心算法 ---- 让一颗小树长大
    类似Dijkstra算法，但是不是在原有基础上累加，而是只考虑一步长度。

# dist[w] 定义为w结点到整个树的距离,parent[s] = -1 ,初始结点的dist定义为 +∞。
def Prim():
    MST = {s}
    while 1:
        v = MST未收录的dist最小者
        if  这样的v不存在：
            break
        收录v点
        for v的所有邻接点w：
            if w未被收录：
                if E(v,w) < dist[w]:
                    dist[w] = E(v,w)
                    parent[s] = v
    if MST收录到的v的数量 < v个：
        return '存在孤立的点,生成树不存在。 '
# 时间复杂度 T = O(v**2)
# 所以适应稠密图(稠密 E > v）(稀疏 E ≈￿ v)
    
'''
'''
Kruskal 贪心算法 ---- 将森林合并成树
    默认为每个结点就是一棵树
    每次收进一条边，就等于两棵树并成了一棵树，
    最后把所有的结点并进来成为一棵树。

def Kruskal():
    MST = {} # 最小生成树存的是边。
    while （ MST 中不到v-1条边 and E 中还有边  ):
        从E中取出一条权重最小的边 E(v,w)  # *** 最小堆 ***
        将 E(v,w) 从 E 中删除
        if E(v,w) 不在MST 中构成回路：   # *** 并查集 *** 如果新加入的点w不在 v的集合内，那就不会形成闭合回路。
            将 E(v,w)加入 新的集合 
        else:
            无视E(v,w)。           
    if MST 中不到 v-1 条边：
        return '存在不联通点，生成树不存在。'

# 时间复杂度 T = O(Elog(E)) 
# 适用于稀疏图。
'''
'''
       (v1)    2    (v2)
     4     1      3      10
(v3)    2    (v4)    7    (v5)
     5      8      4       6
       (v6)    1     (v7)

'''
# ***********************************************************************************************
# Prim算法 稠密图 邻接矩阵 示例。
class Graph():
    def __init__(self,n_vertices):
        self._n_vertices = n_vertices
        self.G = [ [float('inf') for _ in range(n_vertices) ] for _ in range(n_vertices) ]
    def add_edge(self,v,w,weight):
        self.G[v][w] = weight
        self.G[w][v] = weight
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
graph.add_edge(3,4,7)
graph.add_edge(3,5,8)
graph.add_edge(3,6,4)
graph.add_edge(4,6,6)
graph.add_edge(6,5,1)
graph.show_Graph()
print('    \n')

class data():
    def __init__(self,Vertex_num):
        self.dist = [float('inf') for _ in range(Vertex_num)]    # 这里的dist 是v到这棵树的距离。
        self.parent = [-1 for _ in range(Vertex_num)]      # 用数组来储存树。

def Prim(s,data):  # s 是起始结点位置。
    while 1:
        v = Find_Smallest_Dist(s,data)
        if v == None:
            break
        data.dist[v] = 0  # 收录结点
        for w in near_Node(v):   # 影响未收录的相邻结点
            if data.dist[w] != 0:
                # 找出v-->w 边对应权重。
                weight_v_w = graph.G[v][w]
                if data.dist[w] > weight_v_w:  # 由于是点到树的距离，不是点到源点的距离，
                    data.dist[w] = weight_v_w   # 所以 一步距离和原有的dist距离比较即可。
                    data.parent[w] = v
    for collected in data.dist:
        if collected != 0:
            return '这样的最小生成树不存在，因为有孤立点。'
    return data

def Find_Smallest_Dist(s,data):
    if data.dist[s] != 0:
        data.dist[s] = -1
    uncollected_list = [i for i in range(len(data.dist)) if data.dist[i]!=0]
    print(uncollected_list,'没收集到!!!')
    if uncollected_list == []:
        return None
    for i in uncollected_list:
        if data.dist[i] == min([data.dist[i] for i in uncollected_list]):
            print(i,'   没收集的最小dist对应位置')
            print(data.dist[i],'   没有收录的最小dist值')
            return i

def near_Node(v):
    near_Node = [ w for w in range(len(graph.G[v])) if w != float('inf')]
    return near_Node

def CreatTree(H):# 得出的parent其实就是一棵树了，如果有强迫症也可以这样建立一个邻接表，树本身就是一种特殊的图。
    G = [[] for _ in range(7)]
    for i in range(len(H)):
        for j in range(len(H )):
            if H[j] == i:
                G[i].append({j:graph.G[i][j]})
    for i in range(len(G)):
        if G[i] != []:
            print(i,G[i])
    return G

data = data(7)
Prim(0,data)
print('\n\n**********\n Prim算法的结果如下：')
print('dist',data.dist)
print('parent',data.parent)
# 得出的parent其实就是一棵树了，如果有强迫症也可以这样建立一个邻接表，树本身就是一种特殊的图。
t = CreatTree(data.parent)
print('**********\n')
# ***********************************************************************************************

# ***********************************************************************************************
# Kruskal 算法，稀疏图,邻接表。
# 提前解释一下，为什么之前未连接的两个点在同一个集合内，一旦连接着两个点，就会出现闭合回路，就不是树了。
# 如果在同一个集合内，这两个点又没有连接，说明他们在一条线上，他们之间又若干的点。
# 此时连接两点，注定产生一个闭合回路，图就不是树了。
# Kruskal算法就是基于并查集的贪心算法。
#
# 这里分散的把关键点说一下：
# （下面的代码 变量命名有点不太规范）：
# 用new_MST 数组 存 集合信息，默认初始化每个点都是一个集合（树）。
# 用所有边构建一个最小堆，再用最小堆选出 权重最小的边。
# 合并集合（树）的过程中用到了 路径压缩，在new_MST内完成。
# 判断两点不在一个树上，合并成新的树的时候是要全覆盖的。
# 能够合并v、w 点，就添加边<v,w>进 新集合E,集合E 就是最后要输出的树。
# 统计最后树的数量 和前面 伪代码略有不同，是数new_MST中-1来完成的。
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
graph = Graph(7)
graph.add_edge(0,1,2) # v - w - weight
graph.add_edge(0,3,1)
graph.add_edge(1,3,3)
graph.add_edge(1,4,10)
graph.add_edge(2,0,4)
graph.add_edge(2,5,5)
graph.add_edge(3,2,2)
graph.add_edge(3,4,7)
graph.add_edge(3,5,8)
graph.add_edge(3,6,4)
graph.add_edge(4,6,6)
graph.add_edge(6,5,1)
graph.show_Graph()
Edge = [
    [0,1,2],
    [0,3,1],
    [1,3,3],
    [1,4,10],
    [2,0,4],
    [2,5,5],
    [3,2,2],
    [3,4,7],
    [3,5,8],
    [3,6,4],
    [4,6,6],
    [6,5,1]
]
print(Edge)
print('_________\n')

def Kruskal():
    E = []
    new_MST = [-1 for _ in range(len(graph.G))]  # 初始假设每个点都是独立的树（并查集）。
    MST = Edge # 最小生成树存的是边。
    H = creat_Heap(MST)
    while ( Edge_Num(new_MST)<len(graph.G)-1 and len(MST) ):
        theMin = pop_smallest_Edge(H,MST)#从E中取出一条权重最小的边 E(v,w) ,将 E(v,w) 从 E 中删除
        v = theMin[0]
        w = theMin[1]
        weight = theMin[2]
        print(new_MST)
        print(theMin)
        if NotInTheSomeSet(v,w,new_MST):  #E(v,w) 不在MST 中构成回路：   # *** 并查集 *** 如果新加入的点w不在 v的集合内，那就不会形成闭合回路。
            Unin(v,w,new_MST)
            E.append(theMin)  #
            print(v,w)
    count = 0
    for i in new_MST:
        if i == -1:
            count += 1
    if count > 1:
        return '存在不联通点，生成树不存在。%d个集合'%count
    return E

def Edge_Num(new_MST): # 统计边的数量。
    count = 0
    for i in new_MST:
        if i != -1:
            count += 1
    return count

def findRoot(x,new_MST):   # 找root并压缩路径。
    if new_MST[x] == -1:
        return x
    else:
        new_MST[x] = findRoot(new_MST[x],new_MST)
        return new_MST[x]

def NotInTheSomeSet(v,w,new_MST):
    if findRoot(v,new_MST) != findRoot(w,new_MST):
        return True

def Unin(v,w,new_MST):
    v_root = findRoot(v,new_MST)
    w_root = findRoot(w,new_MST)
    for i in range(len(new_MST)):
        if new_MST[i] == w_root:
            new_MST[i] = v_root
    new_MST[w_root] = v_root

def creat_Heap(MST):
    H = HeapStruct()
    H.MinHeapCreate(Capacity_Size=20)
    for e in MST:
        H.Insert(e)
    return H

def pop_smallest_Edge(heap,MST):
    theMin = heap.DeleteMin()
    for e in MST:
        if e == theMin:
            MST.remove(e)
    return theMin

# 最小堆。稍微对element存的值进行了更改,其实就是改了比较大小的位置，由element的元素改为元素的元素。
class HeapStruct():
    def __init__(self,elements=[None],addre=0,capacity=0):
        self.elements = elements
        self.addre = addre # addre 相当于指针，表明堆中最大的那个位置。
        self.capacity = capacity
    def MinHeapCreate(self,Capacity_Size):
        print(' 若插入数值，请确保插入数值在 0 以上 。结点容量为%d'%Capacity_Size)
        self.elements = [None] * (Capacity_Size+1) # 因为有"哨兵"。
        self.capacity = Capacity_Size
        self.elements[0] = self.MinData() # 定义哨兵，其值小于堆中最小值，便于以后更快操作。
        print('self capacity = %s'%self.capacity)
    def MinData(self):
        return [0,0,0]
    def Insert(self,item):
        if self.IsFull():
            print('最小堆已满')
            return
        i = self.addre + 1
        if self.elements[0][2] >= item[2]:
            print('插入数值大小小于下限')
            return
        while self.elements[i//2][2] > item[2]: # i/2 address是父结点的位置。加入值比父类结点小就往上走。这个循环是找到插入位置，并为插入点腾开位置。
            print(self.elements[i//2],item)
            self.elements[i] = self.elements[i//2] # 值得一提：树结构中移动，有的可变动值，而不动结点结构。
            i //= 2
        self.elements[i] = item
        self.addre += 1
    def IsFull(self):
        if self.addre == self.capacity:
            print( self.addre,self.capacity)
            return 1
        return 0
    def IsEmpty(self):
        if self.addre == 0:
            return 1
        return
    def DeleteMin(self):
        if self.IsEmpty():
            print('最小堆已空。')
            return
        minitem = self.elements[1]
        temp = self.elements[self.addre]
        self.elements[self.addre] = None
        self.addre -= 1 # 拿掉最后一个结点。
        parent = 1
        # 保证比最小的儿子还要小，就向上走。
        while parent*2 <= self.addre: # 保证有儿子（必有左儿子）（可能有右儿子）
            left_child = parent * 2
            if self.addre != left_child and self.elements[left_child+1][2] < self.elements[left_child][2]:
                child = left_child + 1
            else:
                child = left_child
            if self.elements[child][2] <= temp[2]: # 假定temp在根位置。
                self.elements[parent] = self.elements[child]
                parent = child  # 沿着最小儿子的路径往下走。
            elif self.elements[child][2] > temp[2]:
                self.elements[parent] = temp # 找到适合位置。
                return minitem
        self.elements[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。
        return minitem

E = Kruskal()
print('\n\n**********\n Kruskal算法的结果如下：')
print('最终的最小生成树为：')
for edge in E:
    print(edge)