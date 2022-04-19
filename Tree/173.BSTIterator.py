
#搜索二叉树中序遍历为有序序列
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.list=[]
        self.index=-1
        self.dfs(root)
    def dfs(self,root):
        if not root:
            return
        self.dfs(root.left)
        self.list.append(root.val)
        self.dfs(root.right)

    def next(self):
        """
        :rtype: int
        """
        self.index+=1
        return self.list[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        if  self.index<len(self.list)-1:
            return True
        else:
            return False