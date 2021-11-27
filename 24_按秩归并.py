'''
上一课中 找root 然后 union 会让树越长越高。
union(root1,root2,S)
def union(x,y,s=[]):  # 有潜在问题，下一课解决。
    s[y] = x

时间复杂度 n**2

正确的做法是把 矮的树 贴到高的树 的根结点上。减少时间复杂度。

方法一：

树的高度，可以存在root的parent内，非常简洁，让-1拥有更多的意义。

s[root] = - 树高

if root1高度 < root2高度：
    s[root1] = root2
if 等高：
    root1高度 ++
    s[root1] = root2

方法二：

比规模

把小树贴到大树上。

s[root] = - 元素个数

if root1规模 < root2规模：
    s[root1] = root2
    s[root2] += s[root1]    # 规模总会变，不像树高可能不变。
if 等：
    s[root2] += s[root1]
    s[root1] = root2

思考：
不论是按高度还是按规模
最坏情况下，n结点的树高为  O（log N）
此时
每次union 都是两颗等高等规模的树，不可避免的增加树高。
不断的2倍，满二叉树。
因此树高log N, 找的次数等于树高  O（log N）。
'''
# 这里用方法二重写 union方法：
def union(x,y,s=[]):
    if abs(s[x]) < abs(s[y]):
        s[y] += s[x]    # 一定要注意 集合规模扩张要写在前面！！！
        s[x] = y        # 小集合 融入 大集合
        print('1 !', s[x], s[y])
    elif abs(s[x]) > abs(s[y]):
        s[x] += s[y]
        s[y] = x
    elif abs(s[x]) == abs(s[y]):
        s[y] += s[x]
        s[x] = y

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

def find(x,s=[]):
    while s[x] >= 0:
        x = s[x]
    return x
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