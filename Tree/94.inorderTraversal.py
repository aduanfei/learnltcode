# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

import collections
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        self.res = []
        root.visited = 0
        stack = collections.deque([root])
        while (stack):
            node = stack.pop()
            if not node.visited:
                node.visited = 1
                if node.right:
                    node.right.visited = 0
                    stack.append(node.right)
                stack.append(node)
                while (node.left):
                    if not hasattr(node.left,"visited"):
                        node.left.visited = 0
                        stack.append(node.left)
                        node = node.left
                    else:
                        break
            else:
                self.res.append(node.val)

        return self.res
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        res = []
        stack=[root]
        node=root
        while(node.left):
            stack.append(node.left)
            node=node.left
        while(stack):
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                node=node.right
                while(node.left):
                    stack.append(node.left)
                    node=node.left
        return res



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

l=[2,3,None,1]
root=generate_tree(l)
s=Solution()
print(s.inorderTraversal(root))