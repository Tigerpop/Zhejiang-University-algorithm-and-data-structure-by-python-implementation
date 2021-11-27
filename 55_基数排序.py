'''
基数排序
    十进制基数就是1，要安排10个桶。

策略"次位优先"：Least Significant Digit
    从个位先开始比较，再10位，再100位...

基数排序步骤：
    先建立一个桶Bucket，以10为基数，0，1，2...9，
    按个位入桶 pass1
    按十位入桶 pass2
    ...
    pass P
    按照最后一次入桶P的顺序从小到大输出。

    每一次pass？ 都是一次桶排序，假如基数是M,M个桶 , 则：
    每一次的 T = O(N+M)，全部入一次桶，再出一次桶，线性。
    一共 T = O(P*(N+M)) 。

    以 M = 10 为基数的话，P = lgM。
'''
'''
多关键字排序：
    每一个关键字，相当于基数排序的 个位、十位...pass的过程。
    例如：
        按主：花色排序
        按次：数字排序
        次位优先LSD 比 主位优先MSD快。    
'''
# 以下代码实践多关键字排序，来给随机的不完整的牌排序。
import random
class Poker():
    def __init__(self,color,num):
        self.color = color
        self.num = num

def CreatpokerList(pokernum=53):
    A = []
    for i in range(pokernum):
        colorList = ['梅花','方块','红桃','黑桃']
        p = Poker(random.choice(colorList),random.randint(1,13))
        A.append(p)
    return A

def Showpoker(A):
    for poker in A:
        print(poker.color,poker.num)

# 桶排序用到的链表。
class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Qlinckedlist():
    def __init__(self):
        self.rear = None
        self.front = None
    def out(self):                       # 头部删除
        if self.front == None:
            print('队列为空。')
        if self.front == self.rear:      # 删除的只剩下一个元素。
            self.rear = None
        temp = self.front
        self.front = temp.next
        return temp.data
    def add(self,item):                  # 尾部添加
        node = Node(item)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    def show(self):
        linckedlist = []
        temp = self.front
        while temp:
            (linckedlist.append(temp.data))
            temp = temp.next
        print(linckedlist)
        return linckedlist

# 桶排序 M是桶列表,这里把次位排序和主位排序都包在内了 。
# 这里注意，链表中并不是poker类，而是单纯的node结点，node内也仅有位置信息，最后输出的也是位置信息，笼统说就算指针吧。
def Bucket_Sort(A,attribute,order,M):                # 这里留了一个属性和顺序的参数，方便对第一次输出结果再加工，不用再写一个方法了。
    count = [Qlinckedlist() for _ in M]              # 数组中每一个元素都是一个链表。
    i = 0
    studentNum = order[i]
    A_copy = A.copy()
    while i<len(order):                              # 入桶
        if attribute == 0:                           # 主位优先选0
            studentGrade = A_copy[order[i]].color
            for n in range(len(count)):
                if M[n] == studentGrade:
                    count[n].add(studentNum)
        elif attribute == 1:                          # 次位优先选1
            # studentGrade = A_copy.pop(0).num
            studentGrade = A_copy[order[i]].num
            count[studentGrade - 1].add(studentNum)   # 由于0-12和1-13差1。
        i += 1
        if i<len(order):
            studentNum = order[i]
    result = []
    for q in count:                                   # 出桶
        if q.front!=None:
            result += q.show()
    return result                                     # 返回的result 是指针，用list表示应该在的位置。


if __name__ == '__main__':
    # 这样的次位优先排序，需要多次桶排序，先根据次位的数字大小桶排序，再主位花色桶排序。
    # 构建牌list。
    A = CreatpokerList()
    Showpoker(A)
    print(len(A))

    # 次位优先桶排序
    M = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    order_ = [i for i in range(len(A))]
    print(order_)
    result_1 = Bucket_Sort(A,1,order_,M)
    print(result_1,'\n',len(result_1))       # 输出的排好的顺序。把A按这个顺序输出。
    M = ['梅花','方块','红桃','黑桃']

    # 在上一次的次位桶排序基础上继续主位桶排序。
    result_0 = Bucket_Sort(A,0,result_1,M)
    result_list = []
    for i in result_0:
        temp = (A[i].color,A[i].num)
        result_list.append(temp)
    print('\n最终的排序结果是：\n',result_list)

