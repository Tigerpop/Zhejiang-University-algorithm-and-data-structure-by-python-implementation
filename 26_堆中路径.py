'''
可以先温习一下树的路径8.2

输入：
5 3
46 23 26 24 10
5 4 3
输出：
24 23 10
46 23 10
26 10

'''
# def main():
#     读取n m 结点个数，查找目标个数
#     根据输入建立堆(最小堆吧)
#     打印到根的路径


addr = [0]    #利用可变对象的特性。
def Insert(heap,item):
    if heap[0] >= item:
        print('小于哨兵！')
        return
    if addr[0] == 0:
        heap[1] = item # 插入
        addr[0] += 1
        return
    i = addr[0] + 1
    while heap[i//2] >= item: # 找插入位置i。
        heap[i] = heap[i//2]
        i //= 2
    heap[i] = item  # 插入
    addr[0] += 1

def main(H,MinValue=0,list_=[]):
    [n,m] = H[0]
    heap = [None] * (n+1)
    heap[0] = MinValue  # 哨兵
    for i in H[1]:
        Insert(heap,i) # 建堆
    for i in H[2]:     # 打印路径
        while i >= 1:
            list_.append(heap[i])
            i //= 2
        list_.append(' --- ')
    print(list_)
    return list_
if __name__ == '__main__':
    h = [[5, 3],
        [46 ,23 ,26 ,24 ,10],
        [5, 4, 3]]
    main(h)




#  额外提示，用案例提示作用域的易错点。
global a_
a_ = 0  # python int类型的global 用起来并不方便。
def aa(b=[]):
    if a_ == 0:
        # 这里非常容易错，python默认用了全局变量，
        # 但是一旦后面有"赋值"语句，
        # 又会被认为是新建局部变量，造成未定义先调用。
        # 如list的append（）方法，没有用到赋值，就可以避免此类情况。
        # a_ += 1
        print('\n\n!!!!',a_)
aa()





