# 一、栈的顺序存储实现。
# stack栈先进后出。栈的时间复杂度是O(N)
# push/pop 入栈/出栈
import re
class Stack():
    def __init__(self,size):
        self.size = size
        self.stack = []
        self.top = -1
    def push(self,x):
        if self.is_full():
            raise Exception('stack is full')
        else:
            self.stack.append(x)
            self.top = self.top + 1
    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        else:
            self.stack.pop()
            self.top = self.top - 1
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        # if self.top == self.size-1:
        #     return True
            return self.top == self.size -1
    def show_stack(self):
        print(self.stack)
S = Stack(5)
for i in range(5):
    S.push(i)
S.show_stack()
for i in range(3):
    S.pop()
S.push(9)
S.show_stack()

# 题目要求：用一个数组实现两个栈，最大利用数组空间。
# 思路：两头往中间增长，两个栈的指针相遇，就算满了。左侧为左栈的底部，右侧为右栈的底部。
# 左侧栈的空条件（左栈指针为-1），右栈的空条件（右栈指针为Maxsize）。
class D_stack():
    def __init__(self,Maxsize):
        self.Maxsize = Maxsize
        self.Data = [None] * Maxsize
        self.Top1 = -1
        self.Top2 = Maxsize
        print('入栈、出栈操作时，输入1、2 确定左右栈。')
    def show_null_num(self):
        if self.Top2 - self.Top1 == 1: # 满栈
            print('栈已经满了')
        return '空着的数量有 %d 个'%(self.Top2 - self.Top1 - 1),self.Data
    def is_empty(self):
        return self.Top1 == -1 and self.Top2 == self.Maxsize
    def push(self,item,Tag):
        if self.Top2 - self.Top1 == 1: # 满栈
            # print('栈已经满了')
            raise Exception('栈已经满了')
        if Tag == 1:
            self.Data[self.Top1+1] = item
            self.Top1 += 1
        else:
            self.Data[self.Top2-1] = item
            self.Top2 -= 1
    def pop(self,Tag):
        if Tag == 1:
            if self.Top1 == -1:
                print('左栈为空')
            else:
                pop_value = self.Data[self.Top1]
                self.Data[self.Top1] = None
                self.Top1 -= 1
                return pop_value
        else:
            if self.Top2 == self.Maxsize:
                print('右栈为空')
            else:
                pop_value = self.Data[self.Top2]
                self.Data[self.Top2] = None
                self.Top2 += 1
                return pop_value

d_stack = D_stack(10)
print(d_stack.is_empty())
d_stack.push(2,1)
d_stack.push(2,2)
d_stack.push(3,2)
d_stack.push('x',2)
d_stack.push('y',1)
d_stack.push(9,1)
d_stack.push(1,1)
d_stack.push(2,1)
d_stack.push(2,1)
d_stack.push(2,1)
# d_stack.push('x',2)
print(d_stack.show_null_num())
d_stack.pop(1)
d_stack.pop(2)
print(d_stack.show_null_num())

# 二、栈的链式存储实现。
# top指针的位置一定在head上(也就是说入栈出栈都在链头部位置)，
# 因为 若在链表尾部，虽然能插入，但不方便删除。
class Node():
    def __init__(self,data):
        self.Data = data
        self.next = None
class CreateStack():
    def __init__(self):
        self.head = None
        self.size = 0
    def is_empty(self):
        print('链表栈是空的：',self.head == None,'栈里还有%d个元素。'%self.size)
        return self.head == None
    def push_first(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.size += 1
    def pop_first(self):
        temp = self.head
        self.head = temp.next
        self.size -= 1
    def print_linckedlist(self):  # 看链表的情况。
        temp = self.head
        while temp:
            print(temp.Data)
            temp = temp.next

s = CreateStack()
s.is_empty()
s.push_first(1)
s.push_first(2)
s.push_first(3)
s.pop_first()
s.is_empty()
s.push_first('x')
s.push_first('y')
s.print_linckedlist()


# 表达式的求值
# 中缀表达式 转 为后缀表达式，T(N)=O(n)每循环一次以下方法，输出一个运算符或运算数。
# 1.碰到运算数：就输出，碰到运算符就存起来，
# 看后一个运算符优先级决定是否输出。
# 2.左括号：入栈
# 3.右括号：将栈顶运算符弹出并输出，直到遇到左括号（括号都是出栈但不输出）。
# 4.运算符 :若优先级 > 栈顶运算符，则把它压栈。
#          若优先级 =< 栈顶运算符，将栈顶运算符弹出并输出。
#          再比较新的栈顶运算符，直到该运算符 > 栈顶运算符优先级为止。
# 5.处理完毕，把堆栈中留存的运算符一并输出。
print('\n\n#############')


# 例题：中缀表达式 转 为后缀表达式,并计算后缀表达式。
class Stack():    # 这里用顺序存储实现一个栈,用来存储运算符。
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def top(self):
        return self.stack[-1]
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return []==self.stack
    def size(self):
        return len(self.stack)

def Pretreatment(list):   #用正则 预处理后处理解决**问题。
    new_list= re.sub(r'\*\*','^',list)
    return new_list
def Posttreatment(list):
    new_list = re.sub(r'\^','**',list)
    return new_list

def Middle_to_later(trans_string,op_rank): #字典存放优先级。
    later_list = [] # 用于放新的表达式
    S = Stack()
    trans_string = Pretreatment(trans_string)
    for checking_char in trans_string:
        if checking_char in '0123456789':
            later_list.append(checking_char)
        elif checking_char in ['^','*','/','+','-']:
            while not S.is_empty() and op_rank[S.top()]>=op_rank[checking_char]:
                later_list.append(S.pop())  # 非空且压不住，出栈。
            S.push(checking_char) # 空或者压的住，符号入栈。
        elif checking_char == '(':
            S.push(checking_char)
        elif checking_char == ')':
            top_char = S.pop()
            while top_char !='(':
                later_list.append(top_char)
                top_char = S.pop()
    while not S.is_empty():  # 遍历完 list，栈里还有符号。
        later_list.append(S.pop())
    return Posttreatment(''.join(later_list))

#每当在输入上看到运算符时，计算两个最近的操作数。用栈存数字完成。
def computer_laster(laster_str):
    stack = Stack()
    laster_str = Pretreatment(laster_str)
    for computing_char in laster_str:
        if computing_char in '0123456789':
            stack.push(computing_char)
        else:  # 遇到运算符
            value2 = int(stack.pop()) #操作要按顺序进行。
            value1 = int(stack.pop())
            if computing_char == '+':
                value = value1 + value2
            if computing_char == '-':
                value = value1 - value2
            if computing_char == '*':
                value = value1 * value2
            if computing_char == '/':
                value = value1 / value2
            elif computing_char == '^':
                value = value1 ** value2
            stack.push(value) #算出的结果重新入栈
    return stack.pop()

def main():
    op_rank = {'^':3,'*':2,'/':2,'+':1,'-':1,'(':0} #'('谁都能压得住。
    string_list = ['1+2*3-(4/2)','4+7*2**2']
    for trans_string in string_list:
        laster_str= Middle_to_later(trans_string, op_rank)
        print('%s-------> %s'%(trans_string,laster_str))
        print('后缀表达式运行结果是：%d'%computer_laster(laster_str))

if __name__ == '__main__':
    main()

# 栈 还能用于
'''
函数调用及递归的实现
           
深度优先搜索

回溯算法
'''







