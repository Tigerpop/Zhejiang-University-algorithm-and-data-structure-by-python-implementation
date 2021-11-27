'''
Huffman 编码不唯一，而且最优编码也不一定就是Hufffman 编码。

1、最优编码 --- 总长度WPL 最小。

2、无歧义解码 --- 数据仅存在于叶子结点上。

3、没有度为 1 的结点，（可以反证），有1、2、必有3。


因为主要的代码之前 20哈夫曼编码 那期我已经写完了，只需要稍加改动就行，下面就不再全部重写了，
以下为伪代码。
'''
minHeap = Min_Heap().Min_Heap_Creat(H)
huffmanTree = Huffman(minHeap)

codeLen = WPL( huffmanTree, 0) # 这个参数0是深度。用递归思想看，总的WPL就是左子树的WPL加右子树的WPL。

# 1、检查是不是最优编码，WPL最小。
def WPL(T,Depth): #类似前序遍历。
    if T.left == None and T.right == None :
        return Depth * T.weight
    else:  # 因为Huffman树一定 只有叶子结点 或者两个子结点。不是叶子结点就注定两个结点。
        return WPL(T.left,Depth+1) + WPL(T.right,Depth+1)

# 2、检查编码是否无歧义。（是否满足前缀码要求）
    # 比如 code编码是1011 ，下一行读到 code101 它就不在叶子结点位置上而在 路径结点上。
    # 或者说一行一行读code，1001，100 ，101 之前已经有了一个100，1001就是一个树不存在的位置。
def IsUnambiguous(student_Test_Code): # 根据所读code建立一棵树，在树叶子结点存code，下一个读取的code看看能不能正确插到叶子结点上。
    new_Tree = Node()
    for code ,weight in student_Test_Code:
        for i in code:
            if i == 0:
                if new_Tree.left == None:
                    new_Tree.left = Node(None)
                    new_Tree = new_Tree.left
                else:
                    new_Tree = new_Tree.left
            if i == 1:
                if new_Tree.right == None:
                    new_Tree.right = Node(None)
                    new_Tree = new_Tree.right
                else:
                    new_Tree = new_Tree.right
        new_Tree.data = code

    def preordertraversal(BT,list_=[]):
        if BT:
            list_.append(BT.data)
            if BT.data != None :
                if BT.left != None or BT.right != None: #非叶子结点有存code。
                    list_.append( 'ambigurous')
            preordertraversal(BT.left,list_)
            preordertraversal(BT.right,list_)
        return list_

    result = preordertraversal(new_Tree)
    if result == ['ambigurous']:
        return 'Ambigurous'
    else:
        return 'Unambigurous'


# 3、检查长度是否正确。
    #把学生提交的每个code长度和出现的频率相乘，再全部求和
    #将这个求和的结果和 我们前面算出来的标准codeLen 相比，看看对不对。
def check_Len(student_Test_Code):
    codetest = 0
    for i in len(H):
        for j in student_Test_Code.weight:
            codetest += (student_Test_Code[i] * j)
    return codetest == codeLen
