'''
表排序
    不移动元素，而只移动元素指针的排序方法 ，叫"间接排序"。
    这样的排序 可以避免挪动元素，比如每个元素都是一个很大的结构一本书。
    表排序：
        定义一个指针数组作为"表"table，
        运用各种排序方法，依据key对table排序。

排序前：
A       0 1 2 3 4 5 6 7
key     f d c a g b h e
 - - - - - - - - - - - -
| table 0 1 2 3 4 5 6 7 |
 - - - - - - - - - - - -

排序后：
A       0 1 2 3 4 5 6 7
key     f d c a g b h e
 - - - - - - - - - - - -
| table 3 5 2 1 7 0 4 6 |       # table 存放的元素是key在A 中对应的坐标。
 - - - - - - - - - - - -

如果仅仅要求按照顺序输出，输出
    A[table[0]],A[table[1]],A[table[2]]... 即可。

物理排序：
如果要求在table排序的基础上，把这些"书"物理"key意义上排好序。
    定理：N个数字的排列，一定是由若干个独立的环组成。
    调整的时候，按照一个环一个环的错位交换，来物理排序。

    具体的调整以包含A[0]的环为例子：
    A       0 1 2 3 4 5 6 7
    key     f d   a   b
    - - - - - - - - - - - -
    | table 3 5   1   0     |   # 已经通过指针得出的第一个环的正确顺序。
    - - - - - - - - - - - -
    # 先空出第一个位置，再把真正应该放这个位置的元素放到这个位置，
    # 每当正确的位置放好以后，把table修正为正确指针，可以此判断是否环结束。
        i = 0
        temp = A[i]
        while table[i] != i:                # 循环会在i回到环的起点结束。
            A[i] = A[table[i]]              # 此位置放正确的key
            now_i = i                       # 此时的指针
            temp_table = table[i]           # 临时存储下一个位置
            table[i] = i                    # 此位置指针调正确
            i = temp_table                  # 跳转下一个位置
        A[new_i] = temp                         # 起始位置赋值，完成环的收尾。
    #  * 注意，以上写法temp 本应该正确赋值的位置先被错误赋值了一次，跳出循环后，被正确的temp赋值所覆盖。也可以选第二种写法。

复杂度分析：
    最好情况：初始有序。
    最坏情况：每次swap 要交换3次，
             此时正好又N/2个环，每个环包含2个元素，
             需要3N/2次移动
             T = O(mN)
'''
# 根据上文的理论：实践一个包含A[0]的环的物理排序
# A = ['f','d',None,'a',None,'b']
# table = [3,5,None,1,None,0]
# i = 0
# temp = A[i]
# while table[i] != i:        # 循环会在i回到环的起点结束。
#     A[i] = A[table[i]]      # 此位置放正确的key
#     next_i = table[i]       # 零时存储下一个位置
#     now_i = i               # 记录此时的i
#     table[i] = i            # 此位置指针调正确
#     i = next_i              # 跳转下一个位置
# A[now_i] = temp
# print(A)
# print(table,'\n')

# 表排序（利用插入排序）
# 假定'f','d','c','a','g','b','h','e'各自都是很大的存储结构。
# 实际比较是依照table表的顺序插入排序，只不过比较时，顺着指针找key关键字比大小而已。
def table_sort(A):
    table = [i for i in range(len(A))]
    def Insert_sort(A,table):                 # 要让table的变化影响到比大小的顺序。
        for p in range(1,len(A)):             # 实际比较是依照table表的顺序插入排序，只不过比较时，顺着指针找key关键字比大小而已。
            temp_table = table[p]
            current = p
            preIndex = p-1
            while A[table[preIndex]]>A[temp_table] and preIndex >=0: # 这一步是关键，table的比大小实际靠指针指向的key来完成,另外注意是和temp比，这里我都写错过好几次了。
                table[current] = table[preIndex]
                current = preIndex
                preIndex = current - 1
                # print(table)
            table[current] = temp_table
        return table
    table = Insert_sort(A,table)
    print(table,'result')
    return table

# A = ['f','d','c','a','g','b','h','e']
# table = [3, 5, 2, 1, 7, 0, 4, 6 ]
# 物理排序
def Physical_sort(A,table):
    for i in range(len(A)):
        if table[i] != i    :
            temp = A[i]
            next_i = table[i]
            #  * 注意，以下第1种写法，temp 本应该正确赋值的位置先被错误赋值了一次，跳出循环后，在new_i位置被正确的temp赋值所覆盖。
            # while table[i] != i:    # 循环会在i回到环的起点结束。
            #     A[i] = A[table[i]]  # 此位置放正确的key
            #     next_i = table[i]   # 零时存储下一个位置
            #     now_i = i           # 记录此时的i
            #     table[i] = i        # 此位置指针调正确
            #     i = next_i          # 跳转下一个位置
            # A[now_i] = temp
            #  * 注意，以下为第2种写法，temp直接赋值到最后一个空缺位置，比较好理解，注意最后一个空缺位置调整后把指针调整正确。
            while table[table[i]] != table[i]:    # 看将要用来填充空缺的元素是否被调整过，如果调整过，说明形成闭环，可以用temp来填充了。
                next_i = table[i]
                A[i] = A[next_i]
                table[i] = i
                i = next_i
            A[next_i] = temp
            table[next_i] = next_i
# Physical_sort(A,table)
# print(A)
# print(table)

if __name__ == '__main__':
    A = ['f', 'd', 'c', 'a', 'g', 'b', 'h', 'e']
    Table = table_sort(A)
    Physical_sort(A,Table)
    print(A)
