'''
《21集合》中find 方法，首先要扫描，找出这个data == x 的结点位置i。

最坏情况，list中有n个元素，要找的元素在最后，要找n遍。
如果find 方法反复执行n次之后，
时间复杂度为 O(N**2)

我们之前就说过，看见复杂度为 n**2 想到分治降低到nlog n，看见n想到二分降低到logn，
但是这里我们换一个角度，直接改变数据的存储属性结构，省略掉找位置这一步。

这题中 data 只存int 数。
所以 node 中 data属性 可以省略，只需要 与list脚标对上就行。

list中只有parent的值，相当于list里只存parent不用data，node中也不需要额外标注parent属性了。
结点node 都没有存在的必要了。
就直接免了"首先要扫描，找出这个data == x 的结点位置i"这个步骤。一个列表解决所有。

几个 -1 就有几个集合（树）。

简化后的node和find 方法。

'''

def find(x,s=[]):
    while s[x] >= 0:  # 找总根结点（集合）
        x = s[x]
    print(x)
    return x

s = [-1,-1,0,1,2,3]
find(3,s)
find(0,s)
find(2,s)

