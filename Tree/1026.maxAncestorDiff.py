class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxgap = 0

        def dfs(root, mi, ma):
            if not root:
                return
            mi = abs(min(mi, root.val))
            ma = abs(max(ma, root.val))
            self.maxgap = max(abs(mi - ma), self.maxgap)
            dfs(root.left, mi, ma)
            dfs(root.right, mi, ma)

        dfs(root, root.val, root.val)
        return self.maxgap
