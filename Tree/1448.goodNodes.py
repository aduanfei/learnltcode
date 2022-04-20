
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.goodnum=1
        self.ismax(root.left,root.val)
        self.ismax(root.right,root.val)
        return self.goodnum

    def ismax(self,root,max):
        if not root:
            return
        if root.val>=max:
            self.goodnum+=1
            max=root.val
        self.ismax(root.left,max)
        self.ismax(root.right,max)