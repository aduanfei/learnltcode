#扩大参数

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root,-99999,99999)
    def dfs(self,root,lower,upper):
        if not root:
            return upper-lower
        lv=self.dfs(root.left,lower,root.val)
        rv=self.dfs(root.right,root.val,upper)
        return min(lv,rv)