'''
求： 符合六度空间理论的人 占 总人数的百分比。

算法：
1】对每个结点，BFS
2】搜索过程中累计访问结点数
3】记录"层"数，仅计算6层内的结点数

如何记录 层数 有两种方法。
方法一：
    每个结点加一个属性 "层"，
    从初始结点定义层为1，每一次入队列操作，
    都来一个父结点层数+1，
    记录6层即可。

    方法一的空间浪费太多，没有必要额外开一个新的属性 "层"

方法二：
    用一个 level表示层数 ，指针 last 指向每层的最后一个元素，
    如何知道last 应该在哪一个位置呢？
    第一层的last 好确定，就是 遍历 v 的相邻结点 的最后一个。
    因为第一层元素只有v，v就是last。在第二层和第三层后，我们更好理解last的含义。
    我们需要出队列元素 轮到 last结点时，遍历完所有last结点相邻结点后，
    才层数+1，才last向外层走。（整体结构类似于一环套一环，一共套6层。）
    我们设定 tail 为游走指针，每次指向入队列元素，
    当出队列元素 == last时，说明这一圈走完了。
#     这里我说的不好，可以看陈姥姥的课，说的非常好。

方法二伪代码：
def BFS():
    visited[v] = true
    level = 0
    last = v
    count = 1
    add_queue(v,Q)
    while !IsEmpty(Q):
        v = out_queue(Q)
        for (v的每一个邻接点w):
            if !visited(w):
                visited[w] = true
                add_queue(w,Q)
                count++
                tail = w
        if v == last:  # 说明这一层的最后一个 结点都被遍历完了。
            level++    # 如第二层遍历完了，level = level +1 = 2
            last = tail
        if level == 6:
            break
    return count
'''
'''
建立模型

A  -----   B
-  -       -   - 
-    -     -      C 
-       -  -         -
E  -----   D            F

为了方便，我们不用六度空间，用二度空间来作实验，看看二度空间的正确率。
用邻接矩阵建立图就是 先初始化点，再给边赋权值。说白了就两步。
'''
import copy
def BuildGraph():
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

    Nv = input_list[0][0]  #点
    Ne = input_list[0][1]  #边
    G = [ [ [0,'N'] for i in range(Nv)] for j in range(Nv) ] # 列表推导完成初始化，列表推导类似于生成器会生成一组数据构成列表。N表示没访问过。
    for e in input_list:
        if len(e)>2:
            G[e[0]][e[1]] = [e[2],'N']  # 连线，给边赋值。
            G[e[1]][e[0]] = [e[2],'N']
    for i in range(Nv):
        print(G[i])
    return G
Graph = BuildGraph()

class Queue():
    def __init__(self):
        self.data = []
    def Add_queue(self,v):
        self.data.insert(0,v)
    def Out_queue(self):
        if self.IsEmpty() == False:
            return self.data.pop()
    def IsEmpty(self):
        return len(self.data) == 0

def Connected_Node_List(v,G):
    list_ = []
    for w in range(len(G[v])):
        if G[v][w][0] != 0:
            list_.append(w)
    return list_

def visited(v,G):
    for i in range(len(G[v])):
        if G[v][i][1] == 'N':
            G[v][i][1] = 'Y'
            result = False
        else:
            result = True
    return result

# 用方法二完成二度空间问题求解。(母亲点 是上一圈的最后一个点，说明儿子这圈已经被遍历完了。)
def BFS(v):  # 这里的v是结点，可以直接用1、2、3.. 表示。
    G = copy.deepcopy(Graph)  # 用深拷贝是为了循环时 三维数组能复原。
    visited(v,G)
    Q = Queue()
    level = 0
    last = v
    Q.Add_queue(v)
    count = 1
    while Q.IsEmpty() == False:
        v = Q.Out_queue()
        for w in Connected_Node_List(v,G):
            if visited(w,G)==False:
                Q.Add_queue(w)
                count += 1
                tail = w
        if last == v:
            level += 1
            last = tail
        if level == 2:
            break
    return count


def main():
    count = 0
    for i in range(len(Graph)):
        if BFS(i) == len(Graph):  # 覆盖到了全部人。
            count += 1
        print(BFS(i))
    print('''
A  -----   B  
-  -       -   - 
-    -     -      C 
-       -  -         -
E  -----   D            F
''')
    print('二度空间在 这个图中 合理的比例为 %d/%d '%(count,len(Graph)))


if __name__ == '__main__':
    main()

