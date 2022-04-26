import collections
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right



class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque([root])
        while (queue):
            curlen = len(queue)
            leftvalue = None
            found = False
            for _ in range(curlen):
                tempnode = queue.popleft()
                if tempnode.left:
                    queue.append(tempnode.left)
                if tempnode.right:
                    queue.append(tempnode.right)
                if not found:
                    leftvalue = tempnode.val
                    found = True

        return leftvalue
