'''
静态查找————没有插入删除。
动态查找————集合记录动态变化，有插入和删除。

"哨兵"原理：
腾出空间，在存储结构中存入某一与储存值不相干的特定值，
只要值等于这一值，（判断为满、或执行某一操作），
避免多设定一个size变量来判断是否为满，或执行某操作。
哨兵实现顺序查找，T(n) = O(n),运气好第一个找到，运气不好最后一个找到。
'''

test_list1 = [1,2,3,4,5,6,7,'K',9,10] # k 在第7 个位置。
test_list2 = [1,2,3,4,5,6,7,8,9]
# 用哨兵实现第一个k值位置的查找：
def search(list,k):
    #设置哨兵。
    list.append(k)
    for i in range(len(list)):
        if list[i] == k:
            if i == len(list)-1:
                return "存储结构中没哟'K'值"
            else:
                print(len(list),i)
                return 'K值的位置在%d'%i

print(search(test_list1,'K'))
print(search(test_list2,'K'))


print('\n\n~~~~~~~~~~`')
# 二分查找位置，降低时间复杂度。 n 变 logn ,之前的分治思想，是把n**2 降为nlogn。
# 二分查找的前提条件："元素有序"。
'''
但是这里必须提一下：
二分算法是分治算法的特殊情况！
区别在于：
二分算法是一次比较，直接扔掉不符合要求的另一半，
分治算法则只是作了划分，并没有缩减问题的规模。 
'''
# 循环实现二分法。
print('循环实现二分法.')
list_1 = [5,16,39,45,51,98,100,202,226,321,368,444,501]
list_2 = [0,1]
def Division_cycle( list,k):
    # 赋初始值,这里的left right mid 都是索引值。
    left = 0
    right = len(list)-1
    while left <= right:   # 二分法的终止条件是left > right。
        mid = (left + right) // 2
        if list[mid] == k:
            return '找到的位置在 %d'%mid
        elif list[mid] < k:
            left = mid + 1
        elif list[mid] > k:
            right = mid - 1
    return '你要找的值不在列表中。'

add = Division_cycle(list_2,0)
print(add)
add = Division_cycle(list_1,368)
print(add)

print('\n\n二分法递归实现 ')
# 递归实现二分法查找。
# 以下典型错误传参，1、默认参数必须是不可变类型；2、函数"（）"内形参中参数不能相互调用。
# def Division_recursion(list_,k,left=0,right=(len(list_)-1)):

def Division_recursion_test(list_,k):
    L = 0
    R = len(list_)-1
    return Division_recursion(list_, k, left=L, right=R)
def Division_recursion(list_,k,left=0,right=0):
    mid = (left + right) // 2
    while left <= right:
        if list_[mid] == k:
            return '找到的位置在 %d'%mid
        elif list_[mid] < k:
            return Division_recursion(list_,k,mid+1,right)
        else:
            return Division_recursion(list_,k,left,mid-1)
    return '你要找的值不在列表中。'

add = Division_recursion_test(list_1,501)
print(add)
