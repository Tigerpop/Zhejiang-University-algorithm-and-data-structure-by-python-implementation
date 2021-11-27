'''
分离链接法 separate chaining
    将一个位置上有冲突的所有关键词都储存在同一个单链表中。

例子
    关键词序列 47，7，29，11，16，92，22，8，3，50，37，89，94，21；
    h(key) = key mod 11
    用分离链接法处理冲突。

    表中有9个结点只需要1次查找就能查找到，
    5个结点需要查找两次。
    查找成功的平均查找次数：
    ASLs = (9+5*2)/14 = 1.36

'''
class HashTable():
    class Node():          # 存放的东西都在这个内部类node中。
        def __init__(self,data,next=None):
            self.data = data
            self.next = next
    def __init__(self,tablesize):
        self.TableSize = tablesize
        self.TheList = [None for _ in range(self.TableSize)]
    def Hash(self,item):
        return item%self.TableSize
    def Find(self,item):         # 返回的是结点。
        Pos = self.Hash(item)
        node = self.TheList[Pos]
        while node != None and node.data != item:
            node = node.next
        return node
    def Insert(self,item):       # 插入链表的最后。
        node = self.Node(item)
        Pos = self.Hash(item)
        if self.TheList[Pos] == None:
            self.TheList[Pos] = self.Node(item)
        else:
            P = self.TheList[Pos]
            while P.next != None :     # 这里设定的能加入重复元素，链表尾插入。
                P = P.next
            P.next = node
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

if __name__ == '__main__':
    A = [47,7,29,11,16,92,22,8,3,50,37,89,94,21]
    h = HashTable(11)
    for i in A:
        h.Insert(i)
    h.Delete(11)
    h.Delete(3)
    h.Delete(92)
    h.Delete(89)
    for i in range(len(h.TheList)):
        if h.TheList[i] != None:
            p = h.TheList[i]
            list_ = []
            while p != None:
                list_.append(p.data)
                p = p.next
            print(i,list_)
        else:
            print(None)

    h.Delete(55)