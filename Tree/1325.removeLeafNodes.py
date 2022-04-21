class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        virtualnode=TreeNode(0)
        virtualnode.left=root
        self.dfs(virtualnode,target)
        return virtualnode.left
    def dfs(self,root,target):
        if not root:
            return
        if self.dfs(root.left,target):
            root.left=None
        if self.dfs(root.right,target):
            root.right=None
        if not root.left and not root.right and root.val==target:
            return 1
        else:
            return 0