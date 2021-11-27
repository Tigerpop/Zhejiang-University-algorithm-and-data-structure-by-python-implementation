'''
电话聊天狂人
    n
    13151548956 18514547845
    18615611548 13774574851
    13151548956 16854975848
    13151548956 13774574851

    统计哪一个号码的接电话和打电话的总次数是最多的？

解法1：
    排序
    1、读入号码，每个号码是11长度的字符串。
    2、排序。
    3、扫描有序数组，累计同号码出现的次数，并更新最大次数。
    优点；
    这种思路非常简单，适合在考试的时候解题用，但是在工程问题时不适用，
    缺点：
    不方便拓展。无法解决"动态插入"的问题。
    比如新加入n个数据，每加入一个数据，就问一个 "聊天狂人"，
    每次都排序就要NlogN，大约就是N^2logN 。

解法2：
    直接映射（桶排序）
    1、创建全单元数的整数数组，保证每个号码对应唯一的单元下标，数组初始化为0。
    2、对读入的每一个点好号码，找到对应单元，数值累计1次。
    3、顺序扫描数组，找出累计次数最多的单元。
    优点：
    编程简单快捷额，主要是思路简单。
    缺点：
    下标是 11 位长的电话号码，一般用的整数是10位的，
    就算用了longlong的整数，11位的数字（第一个位置总是1），一个数字2byte，也有2*10^10个byte。
    占内存空间太大，
    一行两个号码 ，需要 (2*10^10)*2 bytes = 37 G。
    假如问题中 n 是 10^5 ,最多也就 2*10^5个电话号码，
    但 总单元数 是固定的，都是2*10^10个单元，
    也就是说不同规模的问题，都需要扫描这样一个巨大数量。
    所以这个解法无论是时间复杂度还是空间复杂度，都不行。仅仅只是想的挺美好。

解法3：
    带智商的散列
    手机号
    123        4567      89 10 11
    网络识别号  地区编码   用户随机
    由于前面的一些位数重复率太高，会导致太多元素被映射到同一个区域，
    合理的方法：
        把最后5位 ，就是一个地区号加用户随机的号码组成5位，用于散列。
        假如有 N 行，最多就有 2N 个电话号码，
        取 p 略大于 2N 的质数，构建 p 个空位的数组。
        用分离链接法处理冲突。
        h(key) 我们直接简单的用除留余数法。
        在插入一个新的号码时，要先在 h(key)位置遍历搜索一次链表，
        如果已经存在这个号码，就在这个号码的链表结点的计数属性中+1，
        如果不存在这个号码，就在链表的头部插入这个包括这个号码的结点。

def main():
    创建散列表
    读入号码插入表中
    扫描表，找出输出狂人

'''

class HashTable():
    # 结点改动，增加计数功能的属性。
    class Node():
        def __init__(self, data, cum=1, next=None):
            self.data = data
            self.cum = cum
            self.next = next
    def __init__(self,tablesize):
        self.TableSize = tablesize
        self.TheList = [None for _ in range(self.TableSize)]
    # 改动，切片用最后的五位来求hash运算。
    def Hash(self,item):
        return int(item[-5:])%self.TableSize
    def Find(self,item):         # 返回的是结点。
        Pos = self.Hash(item)
        node = self.TheList[Pos]
        while node != None and node.data != item:
            node = node.next
        return node
    # 这里进行了一点改动。
    # 注意 node == P_node 不对的，应该用node中的data来比较，确定是否相等。
    def Insert(self,item):
        node = self.Node(item)
        Pos = self.Hash(item)
        P_node = self.TheList[Pos]
        if self.TheList[Pos] == None:               # 链表为空。
            self.TheList[Pos] = node
        elif P_node.data == node.data:                        # 链表第一个元素就是node，在结点属性上+1。
            P_node.cum += 1
        else:                                       # 有链表且不是链表第一个元素，在链表里面找。
            while P_node.next != None and P_node.next.data != node.data:
                P_node = P_node.next
            if P_node.next == None:                 # 链表里面也没有，插入到链表最后。
                P_node.next = node
            elif P_node.next.data == node.data:               # 找到已有元素位置，在结点属性上+1。
                P_node.next.cum += 1
    def Delete(self,item):       # 链表解决冲突的方法，可以真删除。
        node = self.Find(item)
        if node == None:
            print("要找的内容'%d'不在hash表中。"%item)
            return
        Pos = self.Hash(item)
        P_node = self.TheList[Pos]
        if P_node == node:            # 第一个元素正好是要删除的那一个。
            self.TheList[Pos] = node.next
            return
        while P_node.next != node:    # 要找的元素非第一个元素，这种情况，找到要删除的元素的前一个元素。
            P_node = P_node.next
        P_node.next = node.next

def main():
    A = [[10],
         ['13142514512','12345678987'],
         ['18443141262','18397431567'],
         ['18515678345','18397431567'],
         ['18397431567','18515678345'],
         ['18515678349','18515678349'],
         ['18515678349','18515678349'],
         ['18515678349','18515678349'],
         ['15233334444','15233334444'],
         ['15233334444','15233334444'],
         ['15233334444','15233334444']]
    N = len(A)
    A.pop(0)
    H = CreatTable(N*2)      # 创建散列表,最多2N 个不同电话号码。
    for i in range(N-1):       # 读入号码插入表中
        H.Insert(A[i][0])
        H.Insert(A[i][1])
    ScanAndOutput(H)         # 扫描表，找出输出狂人

def CreatTable(N):
    # 返回大于N 且小于 Maxtablesize 的最小质数，质数就是范围内只能被1和自己整除的数。
    def NextPrime(N):
        Maxtablesize = 1000000
        p_fun = lambda N: N + 2 if N % 2 else N + 1    # 从大于N的下一个奇数开始
        p = p_fun(N)
        while p <= Maxtablesize:
            for i in range(int(p ** (1 / 2)), 2, -1):  # 判断是否是质数，从开根号位置向下试，只要能整除就不是质数。
                if p % i == 0:
                    break                              # 有一个能整除就确定不是质数
            if i == 3:                                 # 前面已经排除了2和1，找完了还没整除，说明是质数。
                break
            else:
                p += 2                                 # 这个奇数不是质数，找下一个奇数试试。
        return p                                       # 总能找到一个最小的质数返回。
    nextprime = NextPrime(N)
    h = HashTable(nextprime)
    return h

def ScanAndOutput(H):        # 更新最大通话次数，更新最小号码，统计狂人人数。
    the_most = 0
    statistics = []
    for node_point in H.TheList:
        while node_point != None:
            statistics.append(node_point)
            node_point = node_point.next
    # 按照结点的计数大小排序
    def Insert_Sort(A):
        for p in range(1, len(A)):  # 抓牌
            temp_cum = A[p].cum  # 这次抓到的牌
            temp_node = A[p]
            preIndex = p - 1
            current = p
            while A[preIndex].cum > temp_cum and preIndex >= 0:  # 找插入位置。python找插入位置用while写方便一些。
                A[current] = A[preIndex]
                current = preIndex
                preIndex = current - 1
            A[current] = temp_node
    Insert_Sort(statistics)
    result_list = []
    print('电话狂人是：%s' % statistics[-1].data)
    for i in range(len(statistics)-1,-1,-1):
        result_sort = statistics[i].data,statistics[i].cum
        result_list.append(result_sort)
        if statistics[i].cum ==  statistics[-1].cum:
            print('电话狂人并列第一的是:%s'%statistics[i].data)
    print('电话狂人从大到小依次是：',result_list)

if __name__ == '__main__':
    main()



