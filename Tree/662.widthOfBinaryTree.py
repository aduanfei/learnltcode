import collections
#假设为完全二叉树标记节点位置

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = collections.deque([(root, 1)])
        ans = 0
        level = 0

        while (stack):
            stacklen = len(stack)
            leftpos = 0
            for _ in range(stacklen):

                node, pos = stack.popleft()
                if leftpos == 0:
                    leftpos = pos
                levelnodes = pos - leftpos + 1

                ans = max(ans, levelnodes)
                if node.left:
                    stack.append((node.left, 2 * pos))
                if node.right:
                    stack.append((node.right, 2 * pos + 1))
            level += 1
        return ans

