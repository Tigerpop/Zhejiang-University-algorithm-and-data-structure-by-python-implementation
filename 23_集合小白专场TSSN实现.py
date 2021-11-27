'''
5 #5个元素
c 3 2 no
i 3 2
c 3 2 yes
i 4 5
i 2 4
c 3 5 yes
i 1 3
c 1 5 yes
s  # 输出the network is connected

主框架
main（）
    while ：
        读入指令集
        处理指令
        return

'''
def main(L):
    S = L.pop(0)[0] * [-1]  #S 是集合。
    for o in L:
        print(o,o[0])
        if o[0] == 'i':
            Input_connection(o[1],o[2],S)
        if o[0] == 'c':
            Check_connection(o[1],o[2],S)
        if o[0] == 's':
            Check_network(S)
    # return S

def find(x,s):
    while s[x] >= 0:
        x = s[x]
    return x
def union(x,y,s=[]):  # 有潜在问题，下一课解决。
    s[y] = x

def Input_connection(node1,node2,S):
    root1 = find(node1-1,S)   # node1 - 1 是为了做映射 。
    root2 = find(node2-1,S)
    if root1 != root2:  # 如果是两个集合,就连接两个点。
        union(root1,root2,S)
def Check_connection(node1,node2,S):
    root1 = find(node1-1,S)
    root2 = find(node2-1,S)
    if root1 == root2:
        print('yes')
    else:
        print('no')
def Check_network(S):  # 集合数量。
    num = 0
    for i in range(len(S)):
        if S[i] < 0:
            num += 1
    if num == 1:
        print('the network is connected')
    else:
        print('there are %d components.'%num)

if __name__ == '__main__':
    L = [[5] ,
        ['c', 3, 2] ,
        ['i', 3, 2],
        ['c', 3, 2] ,
        ['i', 4, 5],
        ['i', 2, 4],
        ['c', 3, 5],
        ['i', 1, 3],
        ['c', 1, 5],
        ['s'] ]

    main(L)




