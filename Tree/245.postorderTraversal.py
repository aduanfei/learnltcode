# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        root.visited = 0
        stack = [root]
        node = root
        while (node.left):
            node.left.visited = 0
            stack.append(node.left)
            node = node.left
        while (stack):
            node = stack.pop()

            if (not node.right) or (node.visited):
                res.append(node.val)
            else:
                node.visited = 1
                stack.append(node)
                node.right.visited = 0
                stack.append(node.right)
                cur = node.right
                while (cur.left):
                    cur.left.visited = 0
                    stack.append(cur.left)
                    cur = cur.left

        return res


