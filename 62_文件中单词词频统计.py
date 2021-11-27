'''
词频统计
首先明确这属于动态查找，适合使用散列表。
    先设计方法把单词"切"出来：
        除了大小写字母、数字、下划线，包括空格的其它字符均视为分隔符。
    对新读入的单词在单词表中查找，如果已经存在，将单词词频+1，
    如果不存在，则插入该单词并记录词频为1。

    注意：
        词频记录什么时候 +1 要看
        只有在已经占领位置的key和待插入元素一样时，
        才会词频 +1 。
        而不是只要有一个冲突就 +1 ！
        有冲突且冲突位置元素和待插入元素一样，词频才+1。
        (词频存放在散列表中,这样只需要加一个data属性，方便一些。)

    目的：
        显示词频前4% 的所有单词。
'''
import re
# 散列表开放地址法、平方探测的实现。
class HashTable():
    class Data():                           # 用一个内部类增加可读性,其调用和类内调用方法属性一样用self即可。
        def __init__(self,element=None,inf=None,WordNum=0):
            self.element = element
            self.WordNum = WordNum          # 在散列表一个属性中存 词频。
            self.inf = inf
    def __init__(self,tablesize,thecells=[]):
        MinTableSize = 10
        if tablesize < MinTableSize:
            print('散列表太小，直接用数组即可。')
            return None
        self.tablesize = tablesize
        self.TableSize = self.NextProme(tablesize)
        self.TheCells = [self.Data(None,None,0) for _ in range(self.TableSize)]
    def NextProme(self,tablesize):    # 比如原本要建立一个12个空间的散列表，但是12不是质数，取余有很多重复值，所以我们取13为大小建立散列表，方便取余。
        return 101
    def Hash(self,word):               # 字符串 哈希位移法，并用秦九韶算法 减少级数求和中乘法的使用次数
        h = 0
        i = 0
        while i < len(word):  # 没到字符串结尾。
            h = (h << 5) + ord(word[i])
            i += 1
        return h % self.tablesize
    def Insert(self,item):              # 这里的item就是find里的key。
        Pos = self.Find(item)
        self.TheCells[Pos].inf = '占用'
        self.TheCells[Pos].element = item
        if self.TheCells[Pos].element == item:
            self.TheCells[Pos].WordNum += 1
        else:
            self.TheCells[Pos].WordNum = 1
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
        return NewPos
    def Delete(self,positon):
        self.TheCells[positon].inf = None
        print('已经删除了散列表%d位置的元素'%positon)

# 词频统计。
class Count_Words_Number():
    def __init__(self,document):
        self.TableSize = 100
        self.Wordcount = 0
        self.Document = document
        self.H = HashTable(self.TableSize)
        list_ = self.Make_Words_list()
        for word in list_:                   # 从单词总列表挑适合的插入开放地址的哈希表。
            if len(word) >= 3:
                self.Wordcount += 1
                self.H.Insert(word)
    # 制作一个单词总列表。
    def Make_Words_list(self):
        list_ = []
        with open(self.Document) as f:
            lines = f.readline()
            while lines=='\n':                 # 读到第一行非空行,注意如果一行为空，readline返回的是换行符。
                lines = f.readline()
            pat = '[a-zA-Z\_0-9]+'             # 除了大小写字母、数字、下划线，包括空格的其它字符均视为分隔符。
            while lines:
                list_ += (re.findall(pat, lines))
                lines = f.readline()
        return list_
    def show(self):
        list_ = []
        for data in self.H.TheCells:
            if data.inf:
                d = data.inf,data.element,data.WordNum
                list_.append(d)
        print(list_)
        list_ = sorted(list_,key=lambda x:x[2])       # 按照词频 升序排序。
        print(list_)
        return list_

if __name__ == '__main__':
    cwn = Count_Words_Number('单词表.txt')
    wordstalbe = cwn.Make_Words_list()
    print(wordstalbe)
    result = cwn.show()
    result_list = []
    for i in range(4):
        result_list.append(result.pop())
    print('\n词频前4，单词分别如下：\n',result_list)

# python正则表达式尝试。
# import re
# result = re.match('p$','p.com')
# print(result)-
# text = 'Hm... Errapple -- Err are *you_sure*you know*? 9-he said,souding insecure.'
# pat = '[a-zA-Z\_0-9]+'
# result = re.findall(pat,text)
# print(result)
# result = re.search('Err([a-z]*) ',text)
# print(result)
# print(result.group(0))
# print(result.group(1))
# emphasis_pattern1 = r'\*([^\*]+)\*'
# emphasis_pattern2 = r'\*(.+)\*'
# emphasis_pattern3 = r'\*(.+?)\*'
# new_text = re.sub(emphasis_pattern1,r'<em>\1<em>',text)
# print(text)
# print(new_text)