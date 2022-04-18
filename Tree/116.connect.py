"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        stack = collections.deque([root])
        while (stack):
            size = len(stack)
            pre = None
            for _ in range(size):
                node = stack.popleft()
                if not pre:
                    pre = node
                else:
                    pre.next = node
                    pre = node
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return root
