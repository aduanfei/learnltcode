class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxpath=root.val
        self.findmax(root)
        return self.maxpath

    def findmax(self,root):
        if not root:
            return 0
        lmax=self.findmax(root.left)
        rmax=self.findmax(root.right)
        self.maxpath=max(self.maxpath,lmax+rmax+root.val,lmax+root.val,rmax+root.val,root.val)
        return max(lmax+root.val,rmax+root.val,root.val)