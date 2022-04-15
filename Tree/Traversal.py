class Node(object):
    def __init__(self,val=0,ln=None,rn=None):
        self.val=val
        self.lnode=ln
        self.rnode=rn

def preorderTraversal(root):
    if root==None:
        return
    stack=[root]
    while(stack):
        cur=stack.pop()
        print(cur.val)
        if cur.right:
            stack.append(cur.right)
        if(cur.left):
            stack.append(cur.left)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return
        self.stack=[]
        self.deepleft(root)
        ls=[]
        while(self.stack):
            cur=self.stack.pop()
            ls.append(cur.val)
            if(cur.right):
                self.deepleft(cur.right)
        return ls
    def deepleft(self,rnode):
        self.stack.append(rnode)
        while(rnode.left):
            self.stack.append(rnode.left)
            rnode=rnode.left
