'''
这里的非递归中序遍历 我们在 《10二叉树非递归遍历》 已经写过代码了，
现在我们来再回顾一下：

我用用一个堆栈来实现非递归的中序遍历，
    push 的顺序依然为先序遍历
    pop 的顺序为中序遍历

题目
根据一个先序遍历 一个中序遍历，可以先建立一个树，再根据这个树搞 后序遍历。
这种思路的代码 我们在 《12二叉树应用例子 的第四个例子》已经完成代码了。
但是这样的做法有点麻烦。

我们下面用  不建立树  的办法，根据先序遍历中序遍历，写出一个后序遍历。
有点类似分而治之的理念。
利用pre确定post的根结点；
再利用in确定左子树、右子树的位置。
递归左子树、右子树。
'''
preList = [1,2,3,4,5,6]
inList = [3,2,4,1,6,5]
postList = [None for _ in range(len(preList)) ]

# 这里我们不像原来一样完整的指定一个区间确定左子树和右子树。
# 而是只利用 起始位置的索引，配合一个固定长度，完成左右区域的划分。
def solve(n,preL=0,inL=0,postL=0):  # preL相当于前序list中的指针，中序后序以此类推,只在方法形参对应位置迭代变化。
    print(preL,inL,postL)
    print(postList)
    if n == 0:   # 右边一段出现长度为0时，直接退出。
        return
    if n == 1:
        postList[postL] = preList[preL]
    root = preList[preL]
    postList[postL+n-1] = root
    for i in range(n):  # 找中序中root的位置。注意此时i为长度，inL+i才是位置。
        if inList[inL+i] == root:
            break
    L_Len = i   # 左边一段的长度。
    R_Len = n-L_Len-1  # 右...
    solve(L_Len,preL=preL+1,inL=inL,postL=postL)  # 左
    solve(R_Len,preL=preL+L_Len+1,inL=inL+L_Len+1,postL=postL+L_Len) # 右

solve(len(preList))
print('后序遍历是',postList)

