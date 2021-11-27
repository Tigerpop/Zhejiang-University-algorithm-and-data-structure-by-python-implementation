'''
一下为伪代码，分几个步骤来建立图。

向函数里面传递一个值，传指针比较适合，而不是传一个结点。（但是下面我用python实现，还是传入了结点）
用MGraph定义 指向 顶点结构体的指针。
MGraph 就代表图。

用c里面 用结构体 来 框基本单元：
struct GNode
————————————————————
Nv  顶点数
Ne  边数
G[][]   邻接矩阵
data[]  存在顶点的数据
————————————————————

定义 一个指针 指向 结点struct GNode，
typedef struct GNode *PtrToGNode

把这个指针 命名为 邻接矩阵的图
typedef PtrToGNode MGraph

'''
# ************************************************
'''
MGraph 初始化
def CreatGraph(vertexNum):
    MGraph Graph
    Graph -> Nv = vertexNum
    Graph -> Ne = 0
    for v in Nv :
        for w in Nv :
            Graph -> G[v][w] = 0
    return Graph 
        
'''
# ************************************************
'''
向MGraph 插入边

类似第一步的 用MGraph定义 指向 顶点结点的指针,
用Edge 定义 指向 边结构体的指针。

typedef struct ENode *PtrToENode
struct ENode:
    Vertex v1 v2     有向边 <v1,v2>
    WeighType Weight  权重
typedef PtrToENode Edge

# 其实插入边的操作就是 把 邻接矩阵的元素 赋值为 权重
void InsertEdge(MGraph Graph,Edge E):
    # 对有向图，仅仅需要下面第一步就行，无向图还需要做一次下面一样的反方向赋权重值。
    Graph -> G[E->v1][E->v2] = E -> Weight
    Graph -> G[E->v2][E->v1] = E -> Weight
'''
# ************************************************
'''
完整地建立一个MGraph 

输入格式
Nv Ne
v1 v2 Weight
...

MGraph BuildGraph():
    MGraph Graph
    Edge E
    scanf(Nv)
    Graph = CreatGraph(Nv)
    scanf(Ne)
    if Graph -> Ne != 0:
        for e in Graph->Ne :
            scanf(v1,v2,Weight)
            InsertEdge( Graph,E )    
    # 如果顶点有数据的话，读入数据。
    for v in Graph->Nv : 
        data[] = ...
    return Graph

'''
# ************************************************
# 以上几个步骤，在考试中简写如下：
# def BuildGraph():
#     scanf(Nv)
#     for i in range(Nv):
#         for j in range(Nv):
#             G[i][j] = 0     # 初始化图
#     scanf(Ne)
#     for i in range(Ne):
#         G[v1][v2] = w       # 连接边。
#         G[v2][v1] = w


# 用python实现时，本人粗略的认为 类GNode 和 类ENode 是Graph类的两个属性,其实可以简写直接写成属性不用类也行。
# 输入格式
# Nv Ne
# v1 v2 Weight data  #其中data可有可无。
# ...
# 说实话，这个代码写的太啰嗦了，可以简写，但是我们故意模块化搞一搞。
# 说实话，下面的代码我都不想看第二遍，太狗屎了，其实完全可以很简单的写出来。
class GNode():     #  每个结点都携带了完整的图的信息。这样是不是太浪费了？
    def __init__(self,Nv=1,Ne=0):
        self.Nv = Nv
        self.Ne = Ne
        self.data = [None] * Nv
        # self.G = [ [0] * Nv ] * Nv # 这样创建二维数组会留大坑！！参考 https://zhuanlan.zhihu.com/p/88197389 原因是浅拷贝，我们以这种方式创建的列表，list_two 里面的三个列表的内存是指向同一块，不管我们修改哪个列表，其他两个列表也会跟着改变。
        self.G = [[0 for i in range(Nv)] for j in range(Nv)] # 列表推导科学实现二维数组。其实用numpy和pandas更方便。
class ENode():
    def __init__(self,v1=0,v2=0,weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
class MGraph():
    def __init__(self,vertexNum,edgeNum):
        self.GNode = GNode(vertexNum,edgeNum) # 初始化顶点，这里没有用老师的Creat方法，而是将其集成到里GNode构造函数里了。
        self.ENode = ENode()
    def InsertEdge(self,E):  # E从输入读入。更新 ENode类。
        for i in range(5):    #打印一下和下面作对比。
            print(self.GNode.G[i])
        self.GNode.G[E.v1][E.v2] = E.weight  # 给点加上边，图就算基本构建完毕。
        self.GNode.G[E.v2][E.v1] = E.weight
        print('-->')
        for i in range(5):     # 打印一下和上面没插入前对比。
            print(self.GNode.G[i])
    def InsertData(self,data):
        for v in range(self.GNode.Nv):
            self.GNode.data[v] = data[v]
'''
A  -----   B
-  -       -   - 
-    -     -      C 
-       -  -         -
E  -----   D            F
'''
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
    word_list = ['A','B','C','D','E','F']

    MG = MGraph(input_list[0][0],input_list[0][1])
    for e in range(1,len(input_list)):
        E = ENode(input_list[e][0], input_list[e][1], input_list[e][2])
        print(E.v1,E.v2,E.weight)
        MG.InsertEdge(E)
    MG.InsertData(word_list)

if __name__ == '__main__':
    main()

