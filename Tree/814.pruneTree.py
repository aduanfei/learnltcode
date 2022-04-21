#根节点可能被删除，添加虚拟节点

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        prunenode = TreeNode(0)
        prunenode.left = root
        self.dfs(prunenode)
        return prunenode.left

    def dfs(self, root):
        if not root:
            return 0
        lsum = self.dfs(root.left)
        if lsum == 0:
            root.left = None
        rsum = self.dfs(root.right)
        if rsum == 0:
            root.right = None
        nodesum = lsum + rsum + root.val
        return nodesum