#找到p值后判断在右子树还是前树

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        pre = None
        cur = root
        while (cur.val != p.val):
            if cur.val > p.val:
                pre = cur
                cur = cur.left

            elif cur.val < p.val:
                cur = cur.right
        if not cur.right:
            return pre
        cur = cur.right
        while (cur.left):
            cur = cur.left
        return cur