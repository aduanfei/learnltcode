
#返回深度和节点

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        def dfs(depth, root):
            if not root:
                return (depth, root)

            ln = dfs(depth + 1, root.left)

            rn = dfs(depth + 1, root.right)
            if ln[0] > rn[0]:
                return ln
            elif ln[0] == rn[0]:
                return (ln[0], root)
            return rn

        return dfs(0, root)[1]