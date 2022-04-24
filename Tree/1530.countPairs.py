class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

import collections
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.distance = distance

        def dfs(root):

            if root.left:
                ls = dfs(root.left)
            else:
                ls = []

            for i in range(len(ls)):
                ls[i] = ls[i] + 1
            if root.right:
                rs = dfs(root.right)
            else:
                rs = []

            if not root.left and not root.right:
                return [0]
            for i in range(len(rs)):
                rs[i] = rs[i] + 1
            for i in range(len(ls)):
                h = ls[i]
                for j in range(len(rs)):
                    k = rs[j]
                    if h + k <= self.distance and h > 0 and k > 0:
                        self.res += 1
            return ls + rs

        dfs(root)
        return self.res

def generate_tree(l):
    root=TreeNode(l[0])
    stack=collections.deque([root])
    i=0
    while(stack):
        node=stack.popleft()
        i=i+1
        if i >=len(l):
            break
        if l[i]==None:
            pass
        else:
            node.left=TreeNode(l[i])
            stack.append(node.left)
        i=i+1
        if i >=len(l):
            break
        if l[i]==None:
            pass
        else:
            node.right=TreeNode(l[i])
            stack.append(node.right)
    return root

l=[1,2,3,None,4]
root=generate_tree(l)
s=Solution()
print(s.countPairs(root,3))