class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root=self.buildTree(preorder)
        return root

    def buildTree(self,preorder):
        if not preorder:
            return
        root=TreeNode(preorder[0])
        ind=0
        while ind<len(preorder)  and preorder[ind]<=root.val:
            ind+=1
        root.left=self.buildTree(preorder[1:ind])
        if ind<len(preorder):
            root.right=self.buildTree(preorder[ind:])
        return root