# T worst(n)
# T avg(n)
# T avg(n) < T worst(n)
# 我们关心的是最坏情况复杂度
'''
时间复杂度的渐进表示法：
T(n) = O(f(n)) 表示时间复杂度有一个上界。T(n) <= Cf(n)

T(n) = Ω(g(n)) 表示时间复杂度有一个上界。T(n) >= Ωg(n)

T(n) = Θ(g(n)) 表示同时有一个上界和下界。

'''
# 求连续子列和的最大值。{A1,A2,A3...AN}
aa = [1,2,-1,8,-1]
# 方法一：暴利遍历。T(n) = O(N**3)
def MaxsubseqSum(a,N):
    MaxSum = 0
    for i in range(0,N):  # i 是左端 j 是右端。
        for j in range(i,N):
            ThisSum = 0
            for k in range(i,j+1):
                ThisSum += a[k]
            if (ThisSum>MaxSum):
                MaxSum = ThisSum
    return MaxSum

a_maxsubseqsum = MaxsubseqSum(aa,len(aa))
print(a_maxsubseqsum)
print('    !!!!!!! ')

# 方法一的改进：
# 改进暴利遍历方法，已知i和j，无需k这层循环可求和。
# 因为j从i点向右移动的过程中即可完成求和计算，
# 无需固定j后再重新重复一遍i到j的过程。
# 新方法时间复杂度降低为：O(N**2)。
aa = [1,2,3,4,-11,2]
def MaxsubseqSum(a,N):
    MaxSum = 0
    for i in range(0,N):  # i 是左端 j 是右端。
        ThisSum = 0
        for j in range(i,N):
            ThisSum += a[j]
            if (ThisSum>MaxSum):
                MaxSum = ThisSum
    return MaxSum

a_maxsubseqsum = MaxsubseqSum(aa,len(aa))
print(a_maxsubseqsum)

# 方法二："分而治之"
# 程序员看见n**2的时间复杂度，应该本能的将其改为nlogn的时间复杂度。
# 这样的思想中典型的是"分而治之"
# 一般只要用到二分，都会出现O(logn)这样的复杂度上限，二分和分而治之是不同的思路，二分会抛弃一部分内容不做处理。
'''
但是这里必须提一下：
二分算法是分治算法的特殊情况！
区别在于：
二分算法是一次比较，直接扔掉不符合要求的另一半，
分治算法则只是作了划分，并没有缩减问题的规模。 

二分法和分而治之法的 时间复杂度推导在py文件不方便看，转《二分法、分而治之时间复杂度推导.pages》。
'''

# 方法三："在线处理"。
# 在线就是输入任意数据就进行即时处理，在任意地方终止输入都可以
# 给出当前的解。这个"在线处理"的复杂度为O(N)
# 此例子的原理：
# 用一个 子list 平行于 案例list，从左往右一个一个加进去，
# 当加入一个新值，这个 子list 的和如果变大，说明可加入。
# 如果加入的这个新值使 子list 的和变小了，说明此值待定。
# 如果加入的这个新值使 子list 的和变小了，而且直接使
# 子list的和 变成了负数，则直接舍弃掉原有 子list 的和。
# 从 子list的和 变负数的位置重新建 新的 子list，继续从左往右。
aa = [1,2,3,4,-11,2]
def MaxSubseqSumnew(a,N):
    ThisSum = 0
    MaxSum = 0
    for i in range(N):
        ThisSum += a[i]    # 向右累加。
        if ThisSum > MaxSum:
            MaxSum = ThisSum   #（新加入的有正向效果）就更新当前结果。
        if ThisSum < 0: #（新加入的负向效果让之前积累都变成负了），直接整段抛弃。
            ThisSum = 0
    return MaxSum
fastest = MaxSubseqSumnew(aa,len(aa))
print(fastest)
