'''
AOE (Activity On Edge )网络
每一条边代表一个活动。
    边表示活动，顶点表示活动到此结束。
    边上表示 （1、活动持续时间；2、和机动时间。），
    顶点分三份（1、顶点编号；2、最早完成时间；3、最晚完成时间。），

    逻辑：
        一条边事件执行的前提条件，是以此边为出度的顶点，此顶点的入度边 全部执行完工。
    解释：
        最早完成时间：（考虑前面的顶点，他们再怎么懒，到这里也可以开工了。）
                    顶点的最早完成时间，Max（其入度的边的持续时间 + 前一顶点最早完成时间）
                    因为要保证到这个时间点，工程一定能够开工，就要保证之前的工程最慢的都做完了。
        最晚完成时间：（考虑后面的顶点，我再怎么懒拖工期，也要保证后面一定没问题。）
                    顶点的最晚完成时间，Min（后一顶点的最晚完成时间 - 其入度边的持续时间 ）
                    这个是从终点逆推 回源点 算出来的。
                    意思是，要保证后一个工程按时（终点的最早完成时间）结束，
                    此顶点必须要在 "最晚完成时刻完成"，否则在 "最早完成时间" 内完成不了工程。
        机动时间：   某组顶点v,w,边<v,w>，
                    （w的最晚完成时间 - v的最早完成时间 - <v,w>的活动持续时间），
                    如果存在这个时间差，
                    则 边<v,w>还存在"可以偷懒的机动时间"。
        关键路径：   绝对不能被延误的活动所组成的路径。
                    也就是没有 "机动时间" 的路径。


一般用于安排项目的工序。

由于陈老师说了 ，这题完成的做完"略烦"，所以我们只改 求最终工期，瞬间工程量小了好多，哈哈。
本题的图就不画了，好麻烦，看视频好了。
'''
class Graph():
    def __init__(self,n_vertices):
        self.n_vertices = n_vertices
        self.G = [[] for _ in range(n_vertices)]
    def add_edge(self,pro_vertices,new_vertices,edge_weight):
        self.G[pro_vertices].append({new_vertices:edge_weight})
    def show_Graph(self):
        for i in self.G:
            print(i)
graph = Graph(9)
graph.add_edge(0,1,6)
graph.add_edge(0,2,4)
graph.add_edge(0,3,5)
graph.add_edge(1,4,1)
graph.add_edge(2,4,1)
graph.add_edge(3,5,2)
graph.add_edge(4,6,9)
graph.add_edge(4,7,7)
graph.add_edge(5,7,4)
graph.add_edge(6,8,2)
graph.add_edge(7,8,4)
graph.add_edge(5,4,0)  # 老师讲解中改变的位置。
graph.show_Graph()

def Find_end_earliest_time(): # 像这样的方向单一的图，可以类似于树，用一个队列配合BFS遍历。
    Q = []
    early_end = [0 for _ in range(len(graph.G))]  # 用一个独立于图的数组存时间信息。
    Enqueue(0,Q) # 直接从0起始点开始。
    # print(Q)
    while IsEmpty(Q) == False:
        v = Dequeue(Q)
        # print(v,'!!')
        print(early_end)
        for w in near_Node(v):
            print(v,'near',w)
            if early_end[w] == 0:    # 没有赋值过，可以入队列了。
                Enqueue(w,Q)
            [weight] = [value for dic in graph.G[v] for key,value in dic.items() if key==w ]
            if early_end[w] < early_end[v] + weight:  # 选一条最长的。理解意思是不同于Dijkstra算法的更新dist。
                early_end[w] = early_end[v] + weight
    return early_end[v]

def Enqueue(v,Q):
    Q.append(v)
def Dequeue(Q):
    return Q.pop(0)
def IsEmpty(Q):
    return len(Q) == 0
def near_Node(v,list_=[]):
    if graph.G[v] != []:
        list_ = [key for dic in graph.G[v] for key in dic.keys()]
    return list_

end_earliest_time = Find_end_earliest_time()
print('\n总工程最早完成时间为：',end_earliest_time)

# 注意
# # for w in []:
# # 以上情况根本不会运行。