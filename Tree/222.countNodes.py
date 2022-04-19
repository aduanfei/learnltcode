#完全二叉树，位运算 左树为0右树为1
#二分法，注意中间数取值
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftnode = root
        h = 0
        while (leftnode):
            h += 1
            leftnode = leftnode.left
        j = 1 << h-1
        k = (1 << (h )) - 1
        return self.halfcount(root, j, k)

    def halfcount(self, root, j, k):
        if j==k:
            return j
        cur = root
        if k - j == 1:
            curmid = mid = k
        else:
            curmid = mid = ((j + k) >> 1)
        steps = []
        while (not curmid == 1):
            step = curmid - (curmid >> 1) * 2
            curmid = curmid >> 1
            steps.append(step)
        steplen = len(steps)
        for i in range(steplen):
            step = steps[steplen - i - 1]
            if step == 0:
                if cur.left:
                    cur = cur.left
                else:
                    if k - j == 1:
                        return j
                    return self.halfcount(root, j, mid)
            else:
                if cur.right:
                    cur = cur.right
                else:
                    if k - j == 1:
                        return j
                    return self.halfcount(root, j, mid)
        return self.halfcount(root, mid, k)

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

l=[1]
root=generate_tree(l)
s=Solution()
s.countNodes(root)