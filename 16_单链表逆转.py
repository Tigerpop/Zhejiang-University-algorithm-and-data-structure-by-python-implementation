'''
给了单链表的头结点，
给了一个int K 。
要求把每 K 个结点逆转一下，
要求返回的是逆转以后头结点的指针。
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.front = None
        self.rear = None
    def add(self,item):
        node = Node(item)
        if self.front==None and self.rear== None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    def show(self):
        list_ = []
        temp = self.front
        while temp:
            list_.append(temp.data)
            temp = temp.next
        print(list_)
        return list_

ll = linkedlist()
ll.add('seat')
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.show()

'''
给了单链表的头结点，
给了一个int K 。
要求把每 K 个结点逆转一下，
要求返回的是逆转以后头结点的指针。
'''
'''
需要三个指针，new指向逆转好的，old指向还没有逆转好的，temp指向old后面的结点以防丢失后面的数据。
三个指针连续的后移。
'''

def reverse(head,k):
    new = head.next
    old = new.next
    for i in range(k-1):
        temp = old.next
        old.next = new # 实现逆序操作。
        new = old
        old = temp
    head.next.next = old       # 保证链表的完整性。
                          # head的 next，这里可以体现出头部设置空结点的好处。
                          # 这里的空结点用seat在链表里设定了。就没有写进reverse方法里面了。
    head.next = new  #
    return new

result = reverse(ll.front,6)
print(result.data)
ll.show()

'''
注意：
这里重点介绍一下设置头结点，在链表操作中的好处
1、使头部的操作和中部尾部的操作一致；
2、使非空链表与空链表的操作统一；
3、在改变链表的顺序时，可以避免链表数据丢失。
'''
'''
就比如上面这题，如果有一个头结点，可以说相当于有一个锚。
方便和后面的几个新加入的new、old等指针配合使用。

纠正一个我之前的错误认知，插入结点时，并不是说一定要保证链表的连贯不断，
而是要保证 断开的结点还能 在书写上能够找回来，
插入结点时之所以是"先插再断"，是因为这样可以在书写上实现找到后序结点。
本题中，逆序的过程中，出现过断链的情况，但是借助new 、old 指针，
可以找回结点，所以也没关系。
'''


