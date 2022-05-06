import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.result=[]
        self.targetSum=targetSum
        self.dfs(root,[])
        return self.result
    def dfs(self,root,path):
        if root.left:
            panext=copy.deepcopy(path)
            self.dfs(root.left,copy.deepcopy(path.append(root)))
        if root.right:
            panext=copy.deepcopy(path)
            self.dfs(root.right,copy.deepcopy(path.append(root)))
        if not root.left and not root.right:
            path.append(root)
            if sum(path)==self.targetSum:
                self.result.append(path)