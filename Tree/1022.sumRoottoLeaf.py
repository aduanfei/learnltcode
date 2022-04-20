class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
import collections


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.bits = []
        self.sum = 0
        self.dfs(root)
        return self.sum

    def dfs(self, root):
        self.bits.append(root.val)
        if not root.left and not root.right:
            self.sumbits()
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)

        self.bits.pop()

    def sumbits(self):
        bitnum = self.bits[0]
        for i in range(1, len(self.bits)):
            bitnum = bitnum * 2 + self.bits[i]
        self.sum += bitnum

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

l=[1,0,1,0,1,0,1]
root=generate_tree(l)
s=Solution()
print(s.sumRootToLeaf(root))