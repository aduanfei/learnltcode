#不太懂

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
        self.voyage = voyage
        self.res = []
        self.index = -1
        if self.dfs(root):
            return self.res
        return [-1]

    def dfs(self, root):
        if not root:
            return 1
        self.index += 1
        ind = self.index
        if not root.val == self.voyage[ind]:
            return 0
        l1 = self.dfs(root.left)
        r1 = self.dfs(root.right)
        if not (l1 and r1):
            self.index = ind
            l2 = self.dfs(root.right)
            r2 = self.dfs(root.left)
            if not (l2 and r2):
                return 0
            else:

                self.res.append(root.val)
        return 1


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
root=generate_tree(l)
voyage=[1,3,2]
s=Solution()
print(s.flipMatchVoyage(root,voyage))