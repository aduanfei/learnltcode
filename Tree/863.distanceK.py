import collections
#dfs转为图（邻接表）后bfs


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        mp=collections.defaultdict(list)
        visited=[target]
        def dfs(root):
            if root.left:
                mp[root.left].append(root)
                mp[root].append(root.left)
                dfs(root.left)
            if root.right:
                mp[root.right].append(root)
                mp[root].append(root.right)
                dfs(root.right)
        stack=collections.deque([target])
        dfs(root)
        level=[]
        if k==0:
            return [target.val]
        while(stack):
            k-=1
            level=[]
            nodelen=len(stack)
            for _ in range(nodelen):
                node=stack.popleft()
                for n in mp[node]:
                    if not n in visited:
                        visited.append(n)
                        level.append(n.val)
                        stack.append(n)

            if k==0:
                break
        return level