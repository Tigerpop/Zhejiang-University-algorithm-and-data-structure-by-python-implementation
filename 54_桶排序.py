'''
桶排序
    之前说的排序算法都是基于比较大小来排序的。
    这样基于比较大小的排序，有一个最坏的时间复杂度下界 NlogN。

    例如：把成绩按分数排成桶，把学生学习往桶里放。
    N个学生，M种成绩。
    我们可以把成绩排好序，每一种成绩下，作一个链表，有这个分数的学生就加入链表。
    def Bucket_Sort(A,M):
        N = len(A)
        while 读入一个学生的成绩：
            将该生成绩插入count[grade]链表
        for i in range(0,M):
            if count[i]:
                输出整个count[i]链表

    T(N,M) = O(M+N)
    每个学生加入桶的时间复杂度是O(N)
    每种分数都输出一遍的时间复杂度是O(M)
M>>N 该怎么办？
'''
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

def Bucket_Sort(A,M):
    count = [Qlinckedlist() for _ in M]   # 数组中每一个元素都是一个链表。
    studentNum = 0
    while A:
        studentGrade = A.pop(0)
        count[studentGrade].add(studentNum)
        studentNum += 1
    result = []
    for q in count:
        if q.front!=None:
            result += q.show()
    return result

if __name__ == '__main__':
    A = [5,4,3,7,6,7,8,2,9,10]
    M = [0,1,2,3,4,5,6,7,8,9,10]
    result = Bucket_Sort(A,M)
    print('学生编号按分数由小到大排序为：\n',result)

