class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter=0
        def dfs(root):
            if not root:
                return -1
            ld=dfs(root.left)+1
            rd=dfs(root.right)+1
            self.diameter=max(ld+rd,self.diameter)
            return max(ld,rd)
        dfs(root)
        return self.diameter