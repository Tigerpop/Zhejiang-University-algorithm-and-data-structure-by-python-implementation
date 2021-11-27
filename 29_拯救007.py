'''
图只是一个抽象概念，并非一定是邻接矩阵或者邻接表才行。
一个遍历过程也可能实现了 图的 逻辑。

建立模型
假设 007 离四个岸边均为10米距离
以007 所在的位置为原点建立直角坐标系，中心坐标（0，0）ax+by+c = 0 为直线方程
上边线为 y = 10    a=0 b=1 c= -10
下边线为 y = -10   a=0 b=1 c= 10
左边为 x = -10    a=1 b=0 c= -10
右边为 x = 10    a=1 b=0 c= 10

任意点（x0,y0）到边的最短距离为
min(  abs(a*x0+b*y0+c) /（a**2+b**2）**0.5  )

设 007 能保持安全的最大跳跃距离 d = 2 米

要保证 007 能够跳出去，要有一条路径通道岸边。用DFS更加适合。

'''
Fish_list = [
    [0,0,False],
    [2,0,False],
    [4,0,False],
    [6,0,False],
    [8,0,False],
    [1,1,False],
    [4,-5,False],
    [3,3,False],
    [-6,5,False],
    [5,-9,False]
]
def Find_Around(v):
    v_around_list = []
    for v_other in Fish_list:
        # 在可跳跃范围内 且 不是自己
        if 2 >= ((v[0]-v_other[0])**2+(v[1]-v_other[1])**2)**0.5 \
            and v!=v_other:
            v_around_list.append(v_other)
    return v_around_list

def Is_Safe(v):
    Boundary = [[0,1,-10],[0,1,10],[1,0,-10],[1,0,10]]
    answer = []
    for a,b,c in Boundary:
        answer.append(abs(a*v[0]+b*v[1]+c)/(a**2+b**2)**0.5) #点到岸边的距离。
    if min(answer) <= 2:
        return 'safe'
    return 'dangerous'

# 在原有的DFS基础上 加入成功上岸 退出条件。
# 还是重申一下，return 只是退出递归中的一层。减少函数中return 数量有助于理解。
def DFS(v):   # 其实只需要对过原点的 连通分量 深度优先遍历就行了。
    v[2] = True
    answer = 'no'
    if Is_Safe(v) == 'safe':
        answer = 'yes'
    else:
        for w in Find_Around(v):
            if w[2] == False:
                print(w)
                answer = DFS(w)
                print(answer)
                if answer == 'yes':
                    break
    return answer

if __name__ == '__main__':
    result = DFS(Fish_list[0])
    if result == 'yes':
        print('007 能 跳出去。')
    else:
        print('007 不能 跳出去。')








