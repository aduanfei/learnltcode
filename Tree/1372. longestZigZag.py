import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution_dp(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        f,g=collections.defaultdict(int),collections.defaultdict(int)
        nodes=collections.deque([root])
        while(nodes):
            node=nodes.popleft()
            if node.left:
                nodes.append(node.left)
                f[node.left]=g[node]+1
            if node.right:
                nodes.append(node.right)
                g[node.right]=f[node]+1
        r1=0
        r2=0
        if(f.values()):
            r1=max(f.values())
        if(g.values()):
            r2=max(g.values())
        return max(r1,r2)


li=[1,1,1,None,1,None,None,1,1,None,1]

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


class Solution_dfs(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dist = 0
        if not root:
            return
        nodes = [root]
        self.dfs(root.left, 0, -1)
        self.dfs(root.right, 0, 1)

        return self.dist

    def dfs(self, root, dist, dir):
        if not root:
            return
        dist += 1
        self.dist = max(self.dist, dist)

        if dir == -1:
            self.dfs(root.right, dist, dir * -1)
            self.dfs(root.left, 0, dir)
        else:
            self.dfs(root.left, dist, dir * -1)
            self.dfs(root.right, 0, dir)
root=generate_tree(li)

r=s1.longestZigZag(root)



