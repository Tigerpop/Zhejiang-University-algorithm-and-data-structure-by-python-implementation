'''
方法一：
    直接把单源最短路径 调用 v 遍。  # 注意最后输出不是两个点之间的最短距离，而是图中所有的两个点之间的最短路径，是很多个输出。
    T = O（V(V**2 + E)) = O(V**3 + EV) 对稀疏图效果好，（边的条数|E|远小于|V|²）的图称为稀疏图。
方法二：
    Floyd 算法
    逐步成型
    T = O(V**3)  对于稠密图Floyd算法更好。

    既然目标是 稠密图，那我们就优先使用邻接矩阵来表示图。

'''
'''
Floyd 算法
    Dk[i][j] = 路径{i-->{l <= k } --> j }的最小长度。
    D0,D1,D2...Dv-1[i][j] 即给出了i到j 的真正最短距离。
    最初的D(-1)是什么？
        邻接矩阵
    若i、j之间没有边，把D[i][j]定义为+∞，利于之后发现更小的路径后被替代。
    
    递推原理：
        当Dk-1已经完成，递推到Dk时：
            情况1：新收录的顶点 k ，根本就不在最短路径{i-->{l <= k }-->j}内，则 Dk = Dk-1。
            情况2、k 在{i-->{l <= k }-->j}最短路径上，
                该路径必由两段最短路径组成：
                Dk[i][j] = Dk-1[i][k] + Dk-1[k][j] 
                （由于D[][] 是 已经收录点之间的最短路径，将Dk[i][j]拆为两段路径后,
                可见[i][k]、[k][j] 均不包含k 结点，也就是说，D[i][k]、D[k][j]仅仅
                包含已经收录的非k结点即可构成，所以在k-1步也就是k值加入之前，就可以计算出来。）
                综合情况1和情况2。
                结论：
                    Dk[i][j] = min( Dk-1[i][j],(Dk-1[i][k]+Dk-1[k][j]) )
    
    简单说步骤就是：
    1、构造一个初始矩阵，此初始矩阵直接为邻接矩阵。并初始化一个位置的path为-1。
    2、按0～N 顺序加入 结点，对初始矩阵每一条边， 试探一下会不会改变其最短路径。
       若D[i][j] > D[i][k] + D[k][j]
       则 会改变其最短路径。 D[i][j] = D[i][k] + D[k][j] ，
       i 到 j 的最短路径 = i 到 k 的最短路径 + k 到 j 的最短路径。
       k一定在ij路径之间，path[i][j] = k.            
    3、事后递归打印从i到k的路径，再打印path[i][j],再递归打印从k到j的路径。
'''
'''
这里我们用邻接矩阵表示稀疏图，来练习。 
       (v1)     2->     (v2)
   4->     1->      3<-       10->
(v3)   2<-     (v4)     2->     (v5)
    5->      8<-      4->       6<-
       (v6)     1<-     (v7)

'''
class Graph():
    def __init__(self,n_vertices):
        self._n_vertices = n_vertices
        self.G = [ [float('inf') for _ in range(n_vertices) ] for _ in range(n_vertices) ]
    def add_edge(self,v,w,weight):
        self.G[v][w] = weight
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
print('    \n')

def Floyd(n_vertices):
    D = [[float('inf') for _ in range(n_vertices)] for _ in range(n_vertices)]
    path = [[-1 for _ in range(n_vertices)] for _ in range(n_vertices)]
    for i in range(n_vertices):
        for j in range(n_vertices):
            D[i][j] = graph.G[i][j]  # 初始化最短路径矩阵。
            if i == j:      # 这里排除自己到自己的路径，其实也可以加，不影响。
                D[i][j] = 0
    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                if D[i][j] > D[i][k] + D[k][j]: # 对每一个新加入的结点试一试能不能影响每一路径的最短路径。
                    D[i][j] = D[i][k] + D[k][j]
                    path[i][j] = k        # 加入的k点缩短了最短路径，k在这条路径上。
    return D,path
    # 注意大三个for循环嵌套，T = O(v**3)

# 对于路径的打印需要使用递归。递归的基线条件是path[i][j] == -1,说明两点之间没有中间点了。
# 总是分三份，一份i 到k ，一份k，一份k到 j。
# 比如想要打印 0到6之间的路径
def print_Path(i , j,list_=[]):
    list_ = [i]
    def inner_print_Path(i,j,list_):
        # if Path[i][j] == -1:         # 同下写法一致。
        #     return list_
        # k = Path[i][j]
        # inner_print_Path(i, k,list_)
        # list_.append(k)
        # inner_print_Path(k,j,list_)
        # return list_
        while Path[i][j] != -1:         # 同上写法一致。
            k = Path[i][j]
            inner_print_Path(i, k,list_)
            list_.append(k)
            inner_print_Path(k,j,list_)
            return list_
        return list_

    result_list = inner_print_Path(i, j, list_)
    result_list.append(j)
    return result_list


if __name__ == '__main__':
    Dist , Path = Floyd(7)
    for dic in Dist:
        print(dic)
    print('\n')
    for i in range(7):
        print(Path[i])

    p05 = print_Path(0,5)
    print(p05)
    for i in range(7):
        for j in range(7):
            shortest_Path = print_Path(i,j)
            print('%s 和 %s 的最短路径为： '%(i,j),shortest_Path)


