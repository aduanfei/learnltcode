class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution(object):
    count = 0

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not inorder:
            return
        root = TreeNode(preorder[0])
        inrd = inorder.index(root.val)

        # prerd=preorder.index(inorder[inrd-1])
        root.left = self.buildTree(preorder[1:inrd + 1], inorder[0:inrd])
        root.right = self.buildTree(preorder[inrd + 1:], inorder[inrd + 1:])

        return root


class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return
        rootval = postorder[len(postorder) - 1]
        i = inorder.index(rootval)

        root = TreeNode(rootval)

        # prerd=preorder.index(inorder[inrd-1])
        root.left = self.buildTree(inorder[0:i], postorder[0:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:len(postorder) - 1])

        return root