import pandas
# 动态添加
class lab():
    def __init__(self,name ):
        self.name = name
l = lab('cys')
l.age = 10 # 给对象动态添加属性。
print(l.age)
lab.add = '中国' # 给类动态添加属性。(之前实例化的对象也会偷偷加上新属性)
print(l.add)


class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def change():
    n = Node(12,Node(11),Node(13))
    n.sex = True
    return n
print(change().sex==True)

a = Node('a')
b = a
b.data = None
print(a.data)    # 可见结点 是可变对象。

import copy
a = Node('a')
b = copy.copy(a)
b.data = 'b'
print('结点 浅复制',a.data)

yy = [1]
temp = 5>2 or 4>2 and 5<3
print(temp)
x = 10
temp = True or yy.pop()!=None   # or 一旦确认左侧True，右边不会处理。
print(temp,yy)
temp =  yy.pop()!=None or True
print(temp,yy)

yy = [1]
temp = False and yy.pop()
print(temp,yy)

temp = yy.pop() and False # and  一旦确认左侧False，右边不会处理
print(temp,yy)

print(max(1,2))
a = '-1'
b = 0
print(a!='-1')
if b :
    print('ok')
a = '123'
print('234'[0])
print(len([]))
for i in range(0):
    print('ok')

bt_list = []
bt_list.append(Node('B','4','3'))
bt_list.append(Node('A','-1','0'))
bt_list.append(Node(None,None,None))
bt_list.append(Node('D','-1','-1'))
bt_list.append(Node('C','-1','-1'))
def buildtree(BTlist):  # 找根。
    check = [None]*len(BTlist)
    for i in range(2):
        print(i)
        check[i] = 0
buildtree(bt_list)

print('~~~~~~`')
def test(x,list_=[]):
    if x == 2:
        list_.append(x)
        print(list_)
        return list_
    list_.append(x)
    return test(2)

print(test(4))

class WFT():
    pass

print(WFT() == WFT())
print(id(WFT()) == id(WFT()))

list_ = [1,2,3,4]
v = list_.copy()
print(v.pop(0))
print(v.pop(0))
print(v)
print(list_)

print(7//2)
print('     \n~~~~~~~=')
class aaa():
    def creat(self):
        print('aa')
        A = aaa()
        return A

a = aaa()
a.creat()
for i in range(1,11,3):
    print(i)
print(1//2)

class HeapStruct_2():
    def __init__(self,elements=[None],addre=0,capacity=0):
        self.elements = elements
        self.addre = addre # addre 相当于指针，表明堆中最大的那个位置。
        self.capacity = capacity
    def MinHeapCreate(self,Capacity_Size):
        print(' 若插入数值，请确保插入数值在 0 以上 。结点容量为%d'%Capacity_Size)
        self.elements = [None] * (Capacity_Size+1) # 因为有"哨兵"。
        self.capacity = Capacity_Size
        self.elements[0] = self.MinData() # 定义哨兵，其值小于堆中最小值，便于以后更快操作。
        print('self capacity = %s'%self.capacity)
    def MinData(self):
        return 0
    def Insert(self,item):
        if self.IsFull():
            print('最小堆已满')
            return
        i = self.addre + 1
        if self.elements[0] >= item:
            print('插入数值大小小于下限')
            return
        while self.elements[i//2] > item: # i/2 address是父结点的位置。加入值比父类结点小就往上走。这个循环是找到插入位置，并为插入点腾开位置。
            print(self.elements[i//2],item)
            self.elements[i] = self.elements[i//2] # 值得一提：树结构中移动，有的可变动值，而不动结点结构。
            i //= 2
        self.elements[i] = item
        self.addre += 1
    def IsFull(self):
        if self.addre == self.capacity:
            print( self.addre,self.capacity)
            return 1
        return 0
    def IsEmpty(self):
        if self.addre == 0:
            return 1
        return
    def DeleteMin(self):
        if self.IsEmpty():
            print('最小堆已空。')
            return
        minitem = self.elements[1]
        temp = self.elements[self.addre]
        self.elements[self.addre] = None
        self.addre -= 1 # 拿掉最后一个结点。
        parent = 1
        # 保证比最小的儿子还要小，就向上走。
        while parent*2 <= self.addre: # 保证有儿子（必有左儿子）（可能有右儿子）
            left_child = parent * 2
            if self.addre != left_child and self.elements[left_child+1] < self.elements[left_child]:
                child = left_child + 1
            else:
                child = left_child
            if self.elements[child] <= temp: # 假定temp在根位置。
                self.elements[parent] = self.elements[child]
                parent = child  # 沿着最小儿子的路径往下走。
            elif self.elements[child] > temp:
                self.elements[parent] = temp # 找到适合位置。
                return minitem
        self.elements[parent] = temp  # 在有儿子的情况到循环结束，没有temp的落脚点，此时叶子结点parent那个位置适合temp。
        return minitem

h = HeapStruct_2()
h.MinHeapCreate(12)
# h.Insert(101)
h.Insert(22)
h.Insert(12)
h.Insert(13)
h.Insert(44)
h.Insert(44)
h.Insert(44)
h.Insert(50)
print(h.elements,'\n',h.addre)
h.DeleteMin()
print(h.elements,'\n',h.addre)

class node():
    def __init__(self,data=0):
        self.data = data


list_ = []
list_.append(node(1))  # 列表里面装结点。
print(list_[0].data)

m = {'name':'chenyushao','age':28}
for i in range(len(m)):
    item = m.popitem()
    print(item[0],item[1])

# me = m.copy()
# t = me.popitem()
# print(t[0],t[1])
# t = me.popitem()
# print(t[0],t[1])
# print(me)
# print(m)

d = dict.fromkeys(['name','age'])
print(d)
# 可变对象。
def out(list_=[]):
    list_.append('a')
    def inner(list_):
        list_.append('b')
        return list_ ,'inner'
    inner(list_)
    print(list_)
    return list_ , 'out'

print(out())
b = ''.join(['1','2'])
print(b,type(b))

# 先序遍历创建二叉树
class Node():
    def __init__(self,data=None,L=None,R=None):
        self.data = data
        self.L = L
        self.R = R
def Creat_tree(H,p=Node()):
    for i in range(len(H)):
        if H[0] == '#':
            H.pop(0)
            p = None
            return p
        else:
            p.data = H.pop(0)
            p.L = Creat_tree(H,Node())
            p.R = Creat_tree(H,Node())
            return p


def inordertraversal(BT,list_=[]):
    if BT:
        inordertraversal(BT.L,list_)
        list_.append(BT.data)  # 或者直接print(BT.data)也可以。
        inordertraversal(BT.R,list_)
    return (list_)


H = ['A','B','C','#','E','D','#']
# H = list('abc##de#g##f###')
tree = Creat_tree(H)
result = inordertraversal(tree)
print(result)

# 打印二叉树根到叶子结点路径
def print_path(BT,path=[],re=[]):
    if BT:
        path.append(BT.data)
        if BT.L == None and BT.R == None: # 叶子结点。
            re.append(path.copy())
        else:
            print_path(BT.L,path,re)
            print_path(BT.R,path,re)
        path.pop()
    return re

tree = Node('a', Node('b', Node('d'), Node('f', Node('e'))), Node('c', Node('g', None, Node('h')), Node('i')))
r = print_path(tree)
print(r)

s = list(range(5))
print(s)
s = -1
print(abs(s))
print(s+s)
print(1//2)

p = [[2,4]]
[n,m] = p.pop(0)
print(n,m)

global a_
a_ = 0
def aa(b=[]):
    if a_ == 0:
        # a_ = 1 # 这里非常容易错，python默认用了全局变量，但是一旦后面有更改此全局变量，又会被认为是局部变量，造成未定义先调用。
        print('!!!!',a_)
aa()

a = []
def updata_a():
    # a = [1]
    a.append(1)
updata_a()
print(a,'____')

a = []
def updata_a():
    a = [1]
updata_a()
print(a)

class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, key, value):
        if key == 'size':
            self.width,self.height = value
        else:
            self.__dict__[key] = value

r = Rectangle()
print (r.__dict__)
print(Rectangle.__dict__)
print(dir(r))

a = 4
b = 3
x  = (a**2+b**2)**0.5

print(x)
print(abs(a*1+b*1-10))

x = 0
def x_test():
    global x
    if x != 1:
        x = 1
        print(x)
x_test()

for a,b,c in [[1,2,3],[4,5,6]]:
    print(a,b,c)

class some():
    def __init__(self):
        self.name = 'chenyushao'
    def add(self):
        self.g = 'chen'
        # self.gg[0] = 'yu'  # 这样的动态赋值是不行的。区分不了list和dict类型。
        self.ggg = [1,2,3]

s = some()
s.add()
print(s.g)
print(s.ggg)
print([[0]*2]*2) # list * num 永远是list里面的元素翻倍。
print([1,2,3]*0)

class some():
    def __init__(self,age=10):
        self.age = age
        self.name = self.age +1
s = some(11)
s.age = 10
print(s.name)
print([]*3)
input_list = [
    [5, 7],
    ['A', 'B', 1, 'a'],
    ['B', 'C', 1, 'b'],
    ['C', 'D', 0.5, 'c'],
    ['B', 'D', 0.5, 'b'],
    ['A', 'D', 1, 'a'],
    ['D', 'E', 1, 'd'],
    ['A', 'E', 1, 'a']
]
print(input_list)
print('~~~~~~~~~~~~\n ')


input_list = [
    [5, 7],
    ['A', 'B', 1],
    ['B', 'C', 1],
    ['C', 'D', 0.5],
    ['B', 'D', 0.5],
    ['A', 'D', 1],
    ['D', 'E', 1],
    ['A', 'E', 1]
]
for i in range(1,len(input_list)):
    for j in range(2):
        if input_list[i][j] == 'A':
            print(' !!!!!!')
            input_list[i][j] = 1
        if j == 'B':
            j = 2
        if j == 'C':
            j = 3
        if j == 'D':
            j = 4
        if j == 'E':
            j = 5
word_list = ['A', 'B', 'C', 'D', 'E']
print(input_list)
g = [[1,2,3],[4,5,6],[7,8,9]]
g[1][1] = 10
print(g)
gg = [[0]*3]*3
gg[1][1] = 10
print(gg)
a=list('1')
a.append('2')
print(a)
print([None for i in range(5)])


class Queue():
    def __init__(self, Maxsize):
        self.rear = -1
        self.front = -1
        self.data = [None for i in range(Maxsize)]

    def Add_queue(self, v):
        self.data.insert(0, v)
print(len([None]) )
print([i for i in range(6)])

class Node():
    def __init__(self,num,data=None):
        self.num = num
        self.data = data
        self.Edge = Edge(None,0)   # 指针就是边。

class Edge():
    def __init__(self,next,weight):
        self.next = next
        self.weight = weight

class Queue():
    def __init__(self,num):
        node = Node(num)
        self.front = node
        self.rear = node
    def add(self,num_item,weight):
        new_node = Node(num_item)
        self.rear.Edge = Edge(new_node,weight)
        self.rear = self.rear.Edge.next
    def show(self,list_=[]):
        temp = self.front
        while temp:
            list_.append(temp.num)
            list_.append('-->')
            list_.append(temp.Edge.weight)
            list_.append('-->')
            temp = temp.Edge.next
        print(list_)

q = Queue(1)
q.add(2,0.9)
q.add(3,0.8)
q.show()

a = [ [] for _ in range(2)]
print(a)
print(len([]))
a = {'a':11}
print(a.keys())
print(a['a'])
for key in a.keys():
    print(key)
for key in a:
    print(key)
a = {}
a[1] = 10
a[2] = 20
print(a)
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 设置默认值，该key在dict中不存在，新增key-value对
print(cars.setdefault('PORSCHE', 9.2)) # 9.2
print(cars)
# 设置默认值，该key在dict中存在，不会修改dict内容
print(cars.setdefault('BMW', 3.4)) # 8.5
print(cars)
key = 'abc'


# dic = {}
# dic.setdefault(key,[]).append(111)
# dic.setdefault(key,[]).append(111)
# print(dic)
# dic['abc'].append(333)
# print(dic)

dict_ = {}
dict_['abc'] = [111]
dict_['abc'].append(222)
dict_['def'] = [333]
print(dict_)
for key in dict_:
    print(key,'@@@')

dict_ = {0:[111]}

dict_[1] = copy.deepcopy(dict_[0]).append(222)
print(copy.deepcopy(dict_[0]))
d = copy.deepcopy(dict_)
d[1] = d[0].append(999)
d[2] = d[0].append(999)
d.setdefault(3,[]).append(888)
# d.setdefault(1,[]).append(888)
print(d)
print(dict_)
path = {1:[1]}
path.setdefault(2,path[1].copy()).append(2)
path.setdefault(3,path[2].copy()).append(3)
print(path,'end \n')

for dic in [{0:'a'},{1:'b'}]:  # 找出v-->w 边对应权重。
    print(dic,dic.items())
    for key, value in dic.items():
        if key == 0:
            print(value,'!!!')
lis = [{0:'a'},{1:'b'}]
[new] = [value for dic in lis for key,value in dic.items() if key==0]
print(new,'this is new ')
value = ((value) for dic in lis for key, value in dic.items() if key == 1)
print(value)
for i in value :
    print(i)

a = [{1:2},{3:4}]
for dic in a:
    for key in dic :
        print(key)
result = [key for dic in a for key in dic ]
print(result)
aa = [i for i in range(3) if i > 10]
print((aa))
#
# for i in range(2):
#     if i == 1:
#         break
# a = i + 1
# print(a)
# x = sorted('123459876')
# print(x)
# class child():
#     def __init__(self,name = 'chen',*son   ):
#         self.name = name
#         self.son = [son_name for son_name in son]
# c = child('chenyushao ','miaoyang','aiyinsitan')
# print(c.name)
# print(c.son)
# c.son = 'zhoujilun'
# print(c.son)
print('*******************\n')
for w in []:
    print(w,'this is []')
    if w==[]:
        print('print')
        print(w,'ok')
# print(w)
for i in range(3):
    pass
print(i)
print({1:(1,2,3)})
print('!!!!!!!!!!')
for p in range(len([1,2,3,4])-1,0,-1):
    print(p)
def Swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
a = 1
b = 2
a,b = Swap(a,b)
print(a,b)

A = [8,9]
a = A[0]
b = A[1]
print(id(a),id(b))
a,b = Swap(a,b)
print(id(a),id(b))
print(A)
Swap(A[0],A[1])
print(id(A[0]),id(A[1]))
print(A)

A = [8,9]
def Swap(A):   # 对可变对象本体操作才能 达到修改目的，若对元素操作则不行。
    temp = A[0]
    A[0] = A[1]
    A[1] = temp
Swap(A)
print(A)

D = 10
while D > 0:
    print(D)
    D = D // 2
import numpy as np
a = np.logspace(0,3,4,base=2)
print(a)
a = np.logspace(3,0,4,base=2)
print(a)
n = 3
a = np.logspace(0,n,n+1,base=2)
print(a)
a = np.logspace(0,-3,4,base=2)
print(a)
import math
print(math.log(100,10))

N = 9
D_list = N * np.logspace(-1,-math.log(N,2),int(math.log(N,2)),base=2)
D_list = N * np.logspace(-1,-math.log(N,2),int(math.log(N,2)),base=2)
print(D_list,'111')
for i in D_list:
    if int(i) == 0:
        i = 1
    print(int(i))

A = [1,2,3]
print(A[-1],'@@@@@@')
if A[-1] > 100:  
    print('!!!',i)
for i in range(0,-1,-1): 
    print(i,'SHIBUSHI')

for i in range(2,0,-1):
    print(i)
print(i)
print('a'<'b')
print('c'<'f')
print('d'<'b')

a = []+[1,2]
print(a,'!!!')
print(7%1,'\n~~~~~~~~~~~~~~')

with open('单词表.txt') as f :
    lines = f.readline()
    print(type(lines),lines=='\n')
    while lines=='\n':
        print('kong')
        lines = f.readline()
    while lines:
        print(lines, '!!!')
        lines = f.readline()
print(ord('a'))
print(100**(1/2)==10)


def NextPrime(N):
    Maxtablesize = 1000000
    p_fun = lambda N: N + 2 if N % 2 else N + 1  # 从大于N的下一个奇数开始
    p = p_fun(N)
    while p <= Maxtablesize:
        for i in range(int(p**(1 / 2)), 2, -1):  # 判断是否是质数，从开根号位置向下试，只要能整除就不是质数。
            if p % i == 0:
                break  # 有一个能整除就确定不是质数
        if i == 3:  # 前面已经排除了2和1，找完了还没整除，说明是质数。
            break
        else:
            p += 2  # 这个奇数不是质数，找下一个奇数试试。
    return p
r = NextPrime(100)
print(r)
aa = '123456789'
print(aa[-4:],aa)
hash_table_input = [33,  1,   13,   12,  34,   38,   27,   22,   32, None ,21]
h = sum(x != None for x in hash_table_input)
hh = sum(1 for x in hash_table_input if x != None )
print(hh)
node_input = [x for x in hash_table_input if x != None]
print(node_input)