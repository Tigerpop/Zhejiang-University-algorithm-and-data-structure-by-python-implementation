'''
按秩归并 是对union方法的改进。

路径压缩是对find方法改进。



'''
# 改进后的find 的目的还是从s中找出x的根结点。
#     注意else中包括三步：
#     1、找出父结点的根，
#     2、将此结点指向这个 （父结点的根），
#     3、返回此根。
# 作用：把树高给缩短了。儿子直接指向了爷爷，和父亲同辈了。
#       只需要一次find，就可以把树的结构改变，缩短成2层的树。方便日后操作。
def find(x,s):
    if s[x] < 0:
        return x
    else:
        s[x] = find(s[x], s) # 在递归从"基线条件反向出栈"时，重构了树的结构。
        return s[x]     # 这样的"尾递归"不会让系统内存爆掉。
                        # 因为"尾递归"容易转为循环。
                        # 编译器会把"尾递归"直接编译为循环来使用。
                        # 也就是说执行时，机器用的其实是循环。


# 在按秩归并的情况下，最坏的情况满二叉树，树高log n ，查询次数log n，
# 查n次就是nlog n，

'''
引理Targan 
令T(M,N)为交错执行 M>=N 次带路径压缩的查找，和 N-1 次按秩归并的最坏情况时间。
则 存在常数 k1 k2 使得：
k1 * M * a(M,N) <= T(M,N) <= k2 * M * a(M,N)

a(M,N) = min{i>=1, A(i,\M/N\)>log N } <= O(log* N) <= 4


'''
def find(x,s):
    if s[x] < 0:
        return x
    else:
        s[x] = find(s[x], s) # 在递归从"基线条件反向出栈"时，重构了树的结构。
        return s[x]

def union(x,y,s):
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