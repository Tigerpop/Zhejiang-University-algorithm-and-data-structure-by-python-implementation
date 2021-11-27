'''
哈利波特要带一个 动物，保证这个动物变成其它的动物都相对容易，
也就是要求带上的这个动物，变成别的动物最难的那条路径 最短。

思路
使用Floyd 算法 在 邻接矩阵中算出 任意两点之间的最短距离。
遍历所有结点，每一个结点算出到其它结点距离的最大值，
比较每一结点对应的这个距离最大值，选其中距离最大值最小的结点。

'''
'''
程序框架搭建

def main():
    读入图
    分析图
    return 0   

def main():
    G = BuildGraph()
    FindAnimal(G)
    return 0
    
def BuildGraph():  # 题目其实是求多源最短路径，用到Floyd算法，因此 用邻接矩阵。
    CreatGraph
    InsertEdge 
    
def FindAnimal(G):
    Floyd
    FindMaxDist --> FindMin
    return FindMin
    
'''
def main():
    G = BuildGraph()
    FindAnimal(G)

def BuildGraph(n_vertices,H):
    def CreatGraph(n_vertices):
        G = [[float('inf') for _ in range(n_vertices) ]for _ in range(n_vertices)]
        return G
    def InsertEdge(v,w,weight):
        G[v][w] = weight
        G[w][v] = weight
    G = CreatGraph(n_vertices)
    for i in range(H.pop(0)[1]):
        item = H.pop(0)
        InsertEdge(item[0]-1,item[1]-1,item[2])  # 下标和 案例差一位，错位对齐。
    return G

def FindAnimal(G):
    def Floyd(G):
        D = G
        n_vertices = len(G)
        for k in range(n_vertices):
            for i in range(n_vertices):
                for j in range(n_vertices):
                    if i == j:
                        D[i][j] = 0
                    elif i==j and D[i][j] < 0:
                        return '出现负值圈，无法处理'
                    elif D[i][j] > D[i][k] + D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]
        return D
    def FindMin(D):
        The_Min = float('inf')
        for (single_Max,i) in Find_single_Max(D):
            if single_Max == float('inf'):    # 特殊情况，图有不联通点，带啥动物都完不成任务。
                return '图不联通，有孤立点，带哪只动物都完成不了任务。'
            if The_Min > single_Max:
                The_Min = single_Max
                Animal = i + 1        # 下标和案例错位，变回去。
        return Animal
    def Find_single_Max(D):
        single_Max_list = []
        for i in range(len(D)):
            single_Max = max(D[i])
            single_Max_list.append((single_Max,i))
        return single_Max_list
    D = Floyd(G)
    print(D)
    return FindMin(D)

if __name__ == '__main__':
    H = [[6,11],[3,4,70],[1,2,1],[5,4,50],[2,6,50],[5,6,60],[1,3,70],[4,6,60],[3,6,80],[5,1,100],[2,4,60],[5,2,80]]
    n_vertices = H[0][0]
    Graph = BuildGraph(n_vertices,H)
    print(Graph)
    Animal = FindAnimal(Graph)
    print('带走 %d号 动物，可以较为简单的变成其它任意一种动物。'%Animal)
