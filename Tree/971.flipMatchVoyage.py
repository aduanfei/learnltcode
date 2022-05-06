import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if not root:
            return
        self.res = []
        self.index = 0
        if not root.val == voyage[0]:
            return [-1]
        self.voyage = voyage
        print(self.res)
        if self.dfs(root, 0):
            return self.res
        else:
            return [-1]


    def dfs(self, root,index):
        if not root:
            return 1
        r1 = self.dfs(root.left, index + 1)
        r2 = self.dfs(root.right, index + 1)
        if (not r1) and r2:
            self.res.append(root)
        if not root.val == self.voyage:
            return 0
        else:
            return r1 or r2

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

l=[1,2,3]
voyage=[1,3,2]
root=generate_tree(l)
s=Solution()
print(s.flipMatchVoyage(root,voyage))