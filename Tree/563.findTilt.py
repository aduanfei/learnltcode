class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.nodesum=collections.defaultdict(int)
        self.tilt=[]
        self.getsum(root)
        return sum(self.tilt)

    def getsum(self,root):
        if not root:
            return  0
        lsum=self.getsum(root.left)
        rsum=self.getsum(root.right)
        self.tilt.append(abs(lsum-rsum))
        nodesum=root.val+lsum+rsum
        return nodesum