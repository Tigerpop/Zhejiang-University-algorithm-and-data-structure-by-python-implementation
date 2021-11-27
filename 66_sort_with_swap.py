'''
sort with swap
    题意：
    -------------------------------------------------------------------
            0   1   2   3   4   5   6   7   8   9
    A       3   5   7   2   6   4   9   0   8   1
    Table   7   9   3   0   5   1   4   2   8   6
    -------------------------------------------------------------------
    0 到 N-1 这 N 个数字的排列，如何仅仅依靠与 0 交换，达到排序目的，一共需要交换多少次？

    回顾：讲表排序时，说过一个理论 —— "N个数组的排列是由若干个独立的环组成。"
        具体的调整以包含A[0]的环为例子：
    A       0 1 2 3 4 5 6 7
    key     f d   a   b
    - - - - - - - - - - - -
    | table 3 5   1   0     |   # 已经通过指针得出的第一个环的正确顺序。
    temp = A[i]
    next_i = table[i]
    #  * 注意，以下为第2种写法，temp直接赋值到最后一个空缺位置，比较好理解，注意最后一个空缺位置调整后把指针调整正确。
    while table[table[i]] != table[i]:    # 看将要用来填充空缺的元素是否被调整过，如果调整过，说明形成闭环，可以用temp来填充了。
        next_i = table[i]
        A[i] = A[next_i]
        table[i] = i
        i = next_i
    A[next_i] = temp
    table[next_i] = next_i

    策略：
        本题中 0 扮演了 物理排序中"空缺"的角色。
        情况一：环内只有一个元素，不需要交换。
        情况二：第0个环内有n0个元素，包括0，需要n-1次交换。
        情况三：第i个环内有ni个元素，不包括0，需要先把0换到环内（1次交换），再进行 (ni+1)-1 次交换，一共ni+1次交换。
               这个把0查到换内的操作，相当于把0做成了一个闭环的引子而已。

        N个元素的序列，包含S 个单元环，K个多元环，则交换次数为：
            = n0-1 + sum(ni+1){i from 1 to K-1 }
            = K - 2 + sum(ni){i from 0 to K-1 }
            而 所有的非单一元素环的元素总个数 sum(ni){i from 0 to K-1 } = N - S
            = N - S + K - 2
        题目要求一共交换多少次，转变为求 S 和 K 的问题。
        在程序编写上，可以不用写一个 swap（）方法，然后用0代替空缺位置一个一个swap交换，数一共交换了多少次，
        因为我们有现成的 "物理排序" 代码可以直接用，只需要用 "物理排序" 记录出 S K 两个值，
        就能把题目中的总交换次数算出来。
解题：
    先根据A制作table
    再根据以上提到的策略算出总交换次数。
'''
A =  [3,5,7,2,6,4,9,0,8,1]
def Creat_table(A):
    Table = [None for _ in A]
    for i in range(len(A)):
        Table[A[i]] = i
    return Table

def Count_Multivariate_or_Single_ring(A,Table):# 就是"物理排序"用next_i填窟窿。
    Multivate_cum = 0
    Single_cum = 0
    Is_cum = [0 for _ in A]                     # 用一个数组来记录这个位置的元素是否被计数过。
    for i in range(len(A)):
        start_i = i
        temp = A[i]
        next_i = table[i]
        cum = 1                                 #   用来记录数量。
        while table[table[i]] != table[i]:      # 单一元素环会跳过循环。
            cum += 1
            Is_cum[i] += 1                      # 表示这个位置已经被计数过了。记录访问的次数。
            next_i = table[i]
            A[i] = A[next_i]
            table[i] = i                        # 表示已经调整好了
            i = next_i
        A[next_i] = temp
        table[next_i] = next_i                  # 表示环最后一个空位已经调整好了。
        Is_cum[i] += 1                          # 表示这个位置已经被计数过了。记录访问的次数
        if Is_cum[start_i]==1 and cum == 1:     # 只有在第一次访问，且环内1个元素。才记录
            print('!!!')
            Single_cum += 1
        if Is_cum[start_i]==1 and cum > 1:      # 只有在第一次访问，且环内多个元素，才记录。
            Multivate_cum += 1
    return Multivate_cum,Single_cum

table = Creat_table(A)
print(table)
K,S = Count_Multivariate_or_Single_ring(A,table)
print('排序好的结果是：',A)
print('多元环数为：%d，单元环数为：%d'%(K,S))
print('只和0交换的排序方法，计算得出总的交换次数为：\n N - S + K - 2 = %d 次。\
        \n\n 浙大的算法数据结构课程到此完结撒花，\n希望我们更进一步在计算机技术上精益求精，\
        \n保持学习热情，努力探索未知的世界！'%(len(A)-S+K-2))