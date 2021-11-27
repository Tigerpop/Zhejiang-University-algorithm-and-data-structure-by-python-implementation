'''
冲突的处理方法
    一、换个位置：开放地址法
    二、同一位置的冲突对象组织在一起：链地址法

开放地址法 Open Addressing：
    一旦冲突，按照某种规则取寻找另一空地址。
    若发生第i次冲突，试探的下一个地址将增加di，
    hi(key) = (h(key) + di) mod TableSize      i 属于 [1,TableSize]
    di 决定来不同的解决冲突方案：
        线性探测：di = i
        平方探测：di = + - i^2
        双散列：  di = i*h2(key)            # 引入另一个散列函数
                 经验证明 以下形式比较好：
                 h2(key) = p - (key mod p)  p为质数
'''
'''
线性探测法：
    关键词序列{47,7,29,11,9,84,54,20,30}    
    散列表表长度tablesize13，装填因子9/13，
    散列函数 h(key) = key mod 11     # 注意取11是小于13的，之后的线性探测是%13取余！
    用线性探测法处理冲突，列出一次插入后的散列表，估算查找性能。
    答：
    h(47) = 3 ,   h(7) = 7,   h(29) = 7 遇到冲突，
    试一试 d1 = 1，h1(29) = (7+1) mod 11 = 8 可以存放。
    h(11) = 0,   h(9) = 9,  
    h(84) = 7 遇到冲突，
    试一试 d1 = 1, h1(84) = 8,8位置已经有存放了，还是冲突，
    试一试 d2 = 2，h2(84) = 9, 9位置已经有存放了，还是冲突，
    试一试 d3 = 3, h3(84) = 10，可以存放。
    dn 可以很大，在散列表中循环到前面的位置。
    ...
    从老师的图中可以看出，当散列出现集中冲突的时候，
    存放会在一个区域形成聚集。

散列查找性能分析
    一、成功"平均"查找长度ASLs
    二、不成功"平均"查找长度ASLu
    ----------------------------------------------------
    H       0，1，2，3，4，5，6，7，8，9，10，11，12
    key     11,30，  47,        7,29,9, 84, 54, 20
    冲突次数 0，6，   0          0，1，0，3， 1， 3
    ----------------------------------------------------
    
    如何确定元素在散列表中？
    冲突0次，找一次就找到了，冲突1次，要找2次才能找到。
    成功平均查找次数 = （1+7+1+1+2+1+4+2+4）/9 = 23/9 = 2.56
    
    如何确定元素不在散列表中？
    以 h = 0 为例，如果h =0处没有该元素也不能断定散列表中一定没有该元素，
    因为可能由于线性探测的位移移动到了前面或者后面的位置，
    一直要循环移动，直到遇到空位置，才能断定该元素一定不在散列表中。
    h = 0 不在散列表中，h =1 时该元素也不在散列表中，h = 2 发现是空位，
    所以，要3次 才能断定 h = 0 的元素确实不在散列表中。
    不成功平均查找长度 = (3+2+1+2+1+1+1+9+8+7+6）/11 = 41/11 = 3.73
    注意：
        h(key) = key mod 11 计划就是存放11个数，之不过散列表有13个空间。
        不成功的查找只会考虑0～10的位置。就是按计划找那几个位置。
        
例子
    将acos\define\float\exp\char\atan\ceil\floor
    8个元素顺次存入一张大小为26的散列表中。
    h(key) = key[0] - 'a'  采用线性探测 di = i，
    ---------------------------------------------------------
    0,      1,      2,      3,      4,      5,      6,      7,      8,  ...
    acos            char    define  exp     float
    ---------------------------------------------------------
    atan 遇到第一个冲突
    ---------------------------------------------------------
    0,      1,      2,      3,      4,      5,      6,      7,      8,  ...
    acos    atan    char    define  exp     float
    ---------------------------------------------------------
    最终
    ---------------------------------------------------------
    0,      1,      2,      3,      4,      5,      6,      7,      8,  ...
    acos    atan    char    define  exp     float   ceil    floor
    ---------------------------------------------------------
    成功平均查找比较次数
    ASLs = (1*5 + 2 + 5 + 3)/8 = 15/8 = 1.87
    不成功平均查找次数
    h(key)计划分为26种情况计划存放26个数。
    ASLu = (9+8+7+6+5+4+3+2+ 1*18)/26 = 62/26 = 2.38
'''
'''
平方探测法：
    以增量序列 1^2、-1^2、2^2 -2^2 ... q^2 -q^2。
    注意：第1次冲突 1^2， 第2次冲突 -1^2，第3次冲突 2^2 ...
    还是以上上个案例看：
    ----------------------------------------------------
    H       0，1， 2，3，4，5，6，7，8，9，10，11，12
    key     11,30,20,47,      84,7,29,9, 54
    冲突次数    3   3          2     1     
    ----------------------------------------------------
    ASLs = (1*5 + 2 + 3 + 4 + 4)/9 = 2
    
    线性探测 时，只要元素在散列表中，一个一个位移找总能找着正确的位置，
    而 平方探测（二次探测）可能一直跳来跳去，找不到真正的位置。
    跳着找不到位置的案例：
    h(key) = key mod 5
    -----------------
    H     0，1，2，3，4
    key   5  6  7      
    -----------------
    一直循环。
    
    
    二次探测（平方探测）也有聚集现象，但是没有线性探测的聚集严重。
    有结论：
        散列表 TableSize 是 4k+3 形式的质数时，平方探测法可以查到整个散列空间。
    
'''
# 开放地址法、平方探测的实现。
class HashTable():
    class Data():                           # 用一个内部类增加可读性,其调用和类内调用方法属性一样用self即可。
        def __init__(self,element=None,inf=None):
            self.element = element
            self.inf = inf
    def __init__(self,tablesize,thecells=[]):
        MinTableSize = 10
        if tablesize < MinTableSize:
            print('散列表太小，直接用数组即可。')
            return None
        self.tablesize = tablesize
        self.TableSize = self.NextProme(tablesize)
        self.TheCells = [self.Data(None,None) for _ in range(self.TableSize)]
    def NextProme(self,tablesize):    # 比如原本要建立一个12个空间的散列表，但是12不是质数，取余有很多重复值，所以我们取13为大小建立散列表，方便取余。
        return 13
    def Hash(self,key):               # 除留取余
        return key%self.tablesize
    # 注意："删除后的空位置" 和 "原本就空的位置" 是不一样的。
    #       "懒惰删除"即 只需要增加一个"删除标记"，而不需要真正的删除，来保证查找时不"断链"。
    #       以免影响其它元素的查找和添加。这里就用inf 来完成目标。
    #       inf 表示是否存放元素，删除操作就是把inf变成None即可，element不动。
    def Insert(self,item):
        Pos = self.Find(item)
        if self.TheCells[Pos].inf == None:
            self.TheCells[Pos].inf = '占用'
            self.TheCells[Pos].element = item
    def Find(self,key):   # 平方探测法,来修正hash返回的位置。每一个key都注定有一个对应的位置。
        cNum = 0          # 记录冲突次数
        CurrentPos = self.Hash(key)
        NewPos = CurrentPos
        while self.TheCells[NewPos].inf != None and \
            self.TheCells[NewPos].element != key:       # 这个位置有存放 而且 存放值不是要找的值。
            if cNum%2:       # 奇数情况，注意奇数对h（）的修正是变大。
                NewPos = CurrentPos + (cNum//2 + 1)**2
                while NewPos >= self.TableSize:    # 变大的方向循环找位置，相当于取余，换一种写法而已
                    NewPos -= self.TableSize
            else:            # 偶数情况，偶数的修正是变小。
                NewPos = CurrentPos - (cNum//2)**2
                while NewPos < 0:                  # 变小的方向找位置。
                    NewPos += self.TableSize
            cNum += 1
        # print(NewPos)
        return NewPos
    def Delete(self,positon):
        self.TheCells[positon].inf = None
        print('已经删除了散列表%d位置的元素'%positon)

if __name__ == '__main__':
    h = HashTable(10)
    h.Insert(5)
    h.Insert(4)
    h.Insert(14)
    h.Insert(26)
    h.Insert(34)
    h.Insert(9)
    h.Insert(19)
    h.Insert(29)
    h.Insert(39)
    h.Delete(10)
    for i in h.TheCells:
        print(i.inf,i.element)
    print('用49 填补 已经被删除的原本19所在的位置。\n')
    h.Insert(49)      # 用49 填补 已经被删除的原本19所在的位置。
    for i in h.TheCells:
        print(i.inf,i.element)
'''
再散列 Rehashing
    当散列表中元素太多时，装填因子a太大，查找效率会下降，
    理想a 属于（0.5～0.85）
    解决办法是rehash，把散列表变大。
    
    比如 原来11个空的hash表，装了9个元素后，a值太大了，我们rehash扩大散列表，
    用一个23个空的hash表来存数据，不能把之前的元素原位置copy过来，
    而应该9个元素全部重算一遍，根据新的位置放入hash表。
    
'''





