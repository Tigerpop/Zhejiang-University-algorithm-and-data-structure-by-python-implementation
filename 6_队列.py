# 队列的顺序结构存储实现
# 队列尾巴rear入，队列头front出，
# front默认在-1位置，也就是说front没有进入队列。
# 可以想象成一个可以打开底部的栈，
# 但是出队列一个元素，已有队列元素不会自动往下掉。（一个水平放置的管子）
'''
class Q():
    Data[MaxSize]
    rear
    front
'''
# 循环队列，
# 循环队列其实也是一管子，但是会智能填空。
# front和rear都指向同一个位置，像一个环。
# 两种方案判断满：null时头尾都在同一位置。
# 1、只装n-1个元素，（rear+1）% maxsize = front 时算满。注意front其实没有进入队列。
# 2、装n个元素，环空间塞满，用额外的size变量不断自加，size==maxsize为满。
# 以下为方法 1实现循环队列 的例子：

class Queue():
    def __init__(self,MaxSize):
        self.size = MaxSize
        self.rear = 0
        self.front = 0
        self.Data = [None] * self.size
    def add(self,item):
        if (self.rear+1)%self.size == self.front:
            print('队列已经满了,添加%s失败'%item)
            return
        self.rear += 1
        self.Data[self.rear] = item
    def out(self):
        if self.rear == self.front:
            print('队列为空')
        self.front = (self.front+1)%self.size
        out_item = self.Data[self.front]
        self.Data[self.front] = None
        return out_item

q = Queue(3)
q.add(9)
q.add(10)
q.add(11)
print(q.Data)
print(q.out())
print(q.Data)


# 链式存储实现队列
# 因为链表的尾部删除操作不方便（因为不知道前一个是什么），
# 所以链尾作rear（指向最后一个元素）。链头作front(指向第一个元素)。
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class Qlinckedlist():
    def __init__(self):
        self.rear = None
        self.front = None # 实际上front就是head。
    def out(self):
        if self.front == None:
            print('队列为空。')
        # 这里注意：rear指向最后一个元素，与此元素实体绑定，
        # 若链只有一个元素，此元素被删除，rear需要与元素脱离。重定向。
        if self.front == self.rear:
            self.rear = None  # 删除的只剩下一个元素，虽rear不指向元素，但front依然指向它，所以还是可以操作。
        temp = self.front
        self.front = temp.next
        return temp.data
    def add(self,item):
        node = Node(item)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node   # 不能省略，要指定next的指向。
            self.rear = self.rear.next
    def show(self):
        linckedlist = []
        temp = self.front
        while temp:
            (linckedlist.append(temp.data))
            temp = temp.next
        print(linckedlist)
queue = Qlinckedlist()
queue.add(12)
queue.add('x')
queue.add('y')
queue.add(88)
queue.add(99)
queue.show()
queue.out()
queue.out()
queue.show()

# 用链式存储结构的队列实现多项式加法运算。
# 两个多项式按指数下降排列。
# 算法思路：
'''
# p1\p2分别指向两个多项式的第一个节点，
若：p1.expon==p2.expon,系数相加，若结果！=0，作为结果多项式的系数，
p1、p2都向后移动一项。
若：p1.expon>p2.expon,p1结果放进结果多项式，p1后移一位。
若：p1.expon<p2.expon,p2结果放进结果多项式，p2后移一位。
某一边的多项式挪完了，将另一个多项式剩余节点依次放进结果多项式中。
'''
class PolyNode():
    def __init__(self,coef,expon):
        self.coef = coef
        self.expon = expon
        self.next = None

# a = [[1, 2], [3, 4], [5, 14], [8, 3],[9,11]]
# b = [[2,1],[3,4],[2,5],[4,8],[12,3]]
a = [[5,2],[10,3],[2,-2],[9,4]]
b = [[3,4],[5,7],[-10,2]]
class Creat_linkedlist():
    def __init__(self,multlist):
        self.front = None
        self.rear = None
        self.multlist = sorted(multlist,key=lambda x:x[1],reverse=True)
        self.multadd()
        self.show()
    def add(self,c,e):  # 添加节点。
        node = PolyNode(c,e)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node  # 不能省略，要指定next的指向。
            self.rear = self.rear.next
    def show(self):
        linckedlist = []
        temp = self.front
        while temp:
            (linckedlist.append([temp.coef,temp.expon]))
            temp = temp.next
        print(linckedlist)
    def multadd(self):
        for data in self.multlist:
            self.add(data[0],data[1])

def add_computing(a_linkedlist,b_linkedlist): # 一元多项式加法。
    c_linkedlist = Creat_linkedlist([[0, 0]])
    p1 = a_linkedlist.front
    p2 = b_linkedlist.front
    while(p1 and p2):
        if p1.expon == p2.expon:
            sum = p1.coef + p2.coef
            if sum: # 和非零。
                Attach(sum,p1.expon,c_linkedlist)
            p1 = p1.next
            p2 = p2.next
            continue
        elif p1.expon < p2.expon:
            Attach(p2.coef,p2.expon,c_linkedlist)
            p2 = p2.next
            continue
        else:
            Attach(p1.coef,p1.expon,c_linkedlist)
            p1 = p1.next
            continue
    while p1:   # 一条链处理完，把另一条加入新链。
        Attach(p1.coef,p1.expon,c_linkedlist)
        p1 = p1.next
    while p2:
        Attach(p2.coef, p2.expon, c_linkedlist)
        p2 = p2.next
    # 把第一个[0,0] 节点删除。
    c_linkedlist.front = c_linkedlist.front.next
    return c_linkedlist

def Attach(c,e,linkedlist): # 把一个node续到一个链表的尾部。
    p = PolyNode(c,e)
    linkedlist.rear.next = p
    linkedlist.rear = linkedlist.rear.next

a_linkedlist = Creat_linkedlist(a)
b_linkedlist = Creat_linkedlist(b)
c_linkedlist = add_computing(a_linkedlist,b_linkedlist)
c_linkedlist.show()

# 多项式求积
# 仅表示非零项，
# 用数组实现编程容易调试容易，但是要事先确定数组大小。
# 链表实现，动态小强，但是编程相对复杂，调试困难。
# 上面例子已经实现了两个一元多项式求和，在上面基础上添加求积方法。
'''
多项式求积算法思路：
逐项插入
p1的第一项乘p2的第一项，指数相加，系数相乘，，插入新链表，以此类推
关键在于如何降序插入。可以用左插入和右插入方法，
也可以用 一个移动的游标。利用游标逐个比较找到插入点。
重新回顾以下链表的基本遍历框架
while p:
    balaba...labala
    p = p.next
尤其需要注意，链表的递归嵌套易错点：
正确案例如下：
t1 = a_linkedlist.front
while t1:
    t2 = b_linkedlist.front    # 让t2 循环一次后 ，能复位到t2 头指针位置。
    while t2:
        print(t1.expon,t2.expon)
        t2 = t2.next
    t1 = t1.next
易错写成：
t1 = a_linkedlist.front
t2 = b_linkedlist.front      # 这样嵌套的循环一次结束后，无法复位到t2 的头指针位置。
while t1:
    while t2:
        print(t1.expon,t2.expon)
        t2 = t2.next
    t1 = t1.next
'''
def mult(alinkedlist,blinkedlist):
    t1 = alinkedlist.front
    new_linkedlist = Creat_linkedlist([[0, 0]])
    while t1:
        t2 = blinkedlist.front
        while t2:
            c = t1.coef*t2.coef
            e = t1.expon+t2.expon
            temp = new_linkedlist.front
            # 每次插入操作，都要从头利用游标temp遍历new_linkedlist链表，跳过不适合的插入点。
            # 注意： 要先判断temp的next是否为空，再比指数大小，为空可直接插入，
            # 不为空则在指数比插入值指数小的位置前插入。
            while temp.next and temp.next.expon > e:
                temp = temp.next         #（跳过不适合的插入点）
            # 插入前判断指数相等的特殊情况：
            if temp.next and temp.next.expon == e:
                if (temp.next.coef + c) == 0:
                    temp.next = temp.next.next    #系数和为0，直接删除。
                else:
                    temp.next.coef =  temp.next.coef + c  # 指数相同改系数即可，不用插入。
                    print(temp.next.coef,c)
            else: #理想位置temp已经出现，开始插入：
                p = PolyNode(c,e)
                p.next = temp.next
                temp.next = p
            t2 = t2.next
        t1 = t1.next
    new_linkedlist.front = new_linkedlist.front.next
    return new_linkedlist

d_linkedlist = mult(a_linkedlist,b_linkedlist)
d_linkedlist.show()



