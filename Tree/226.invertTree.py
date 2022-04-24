class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        def dfs(root):
            if not root:
                return
            r=root.right
            l=root.left
            root.left=dfs(r)
            root.right=dfs(l)
            return root
        return dfs(root)
