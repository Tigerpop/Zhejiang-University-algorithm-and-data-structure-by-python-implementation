# 多项式的表示

# 一：循序存储结构的直接表示。
# a[i]x**i
# 下标i ：0，1，2，3，4，5...
# a[i]:  1，0，-3，0，0，4...

# 二：顺序存储结构表示非零项。
# 用结构数组 (系数a[i],指数i) 表示 可以 简约空间。
# 下标i：    0，1，2...
# 系数a[i]:  9，15，3...
# 指数i ：   12，8，2...

# 三：链表结构存储非零项。
# 链表相较顺序存储列表，最大的好处就是很容易往序列中添加和删除元素，
# 单看插入和删除操作，最优可达到O(1)的复杂度。
# 另外，链表的好处还有不需要连续的存储空间，
# 且不需要预先知道数据集的大小。但是查找的操作不方便。[最下方有链表的介绍]

# (系数、指数、指针) 按指数下降排列。












# 链表的实现
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def __str__(self):
        return str(self.data)#方便后续观察数据。

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def isEmpty(self):
        return self.head == None
    def addFirst(self,item):
        temp = Node(item) #创建节点并作为传入对象。
        temp.next = self.head #新节点指向头节点
        self.head = temp #头节点重新指向新加入节点。
        self.size +=1
    def remove(self,item):
        currentNode = self.head
        found = False
        previous = None
        # 因为链表的最后节点指向的是None，不等于None说明还没遍历完。
        while currentNode != None and not found:  # while用and，一项不满足就停止循环。
            # print(' 还在循环中。')
            if currentNode.data == item:
                found = True
            else:   # 没找着，就向后移动，previous留着插入或删除用。
                previous = currentNode
                currentNode = currentNode.next
                # print('有向后移动')
        if not found: # 这里的found 是false，没找到。
            print('链表中没有你要找的内容。')
            raise ValueError('SingleLinkedList.remove(item): item not in SingleLinkedList')
        if previous == None: # 要删除的元素是第一个这种情况。
            self.head = currentNode.next
        else:       #删除只需要哦一步，插入需要先插后半截再接上前半截。
            previous.next = currentNode.next
        self.size -= 1

# if __name__== '__main__':
u = SingleLinkedList()
u.isEmpty()
print(u.head)
u.addFirst(4)
print(u.head)
u.addFirst('Doge')
print(u.head)
u.addFirst('ok')
print(u.head)
u.addFirst('ok1')
print(u.head)
u.addFirst('ok2')
print(u.head,'#########  #######')
u.remove('ok2')
print(u.head)
u.remove('ok1')
print(u.head)
u.remove('ok')
print(u.head)