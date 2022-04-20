#单次遍历找到结果后不可直接返回，可能有多个路径满足
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

import collections
import copy
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res=[]
        self.outerSum(root,sum)
        return len(self.res)
    def outerSum(self,root,sum):
        if not root:
            return
        self.path=[root.val]
        self.innerSum(root,sum)
        self.outerSum(root.left,sum)
        self.outerSum(root.right,sum)
    def innerSum(self,root,sum):
        if not root:
            return
        if sum==root.val:
            self.res.append(copy.deepcopy(self.path))
        if root.left :
            self.path.append(root.left.val)
            self.innerSum(root.left,sum-root.val)
        if root.right :
            self.path.append(root.right.val)
            self.innerSum(root.right,sum-root.val)
        self.path.pop()

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

l=[1,-2,-3,1,3,-2,None,-1]
root=generate_tree(l)
s=Solution()
sum
print(s.pathSum(root,-1))