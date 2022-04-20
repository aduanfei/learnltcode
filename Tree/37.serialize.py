class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
import collections
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        ans = ""
        queue = collections.deque([root])
        while (queue):
            quelen = len(queue)
            for _ in range(quelen):
                node = queue.popleft()
                if node:
                    ans += str(node.val) + ","
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    ans += "null,"

        return ans[:-1]

    def deserialize(self, data):

        if data == "null":
            return None
        nodes = data.split(",")
        p = 0
        p1 = 1
        p2 = 2
        root = TreeNode(nodes[0])
        nodelist = [root]

        while (p2 < len(nodes)):
            node = nodelist[p]
            if node:
                if p1 < len(nodes):
                    if nodes[p1] == "null":
                        nodelist.append(None)
                    else:
                        node.left = TreeNode(nodes[p1])
                        nodelist.append(node.left)
                if p2 < len(nodes):
                    if nodes[p2] == "null":
                        nodelist.append(None)
                    else:
                        node.right = TreeNode(nodes[p2])
                        nodelist.append(node.right)
                p1 += 2
                p2 += 2
            p += 1

        return root

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

l= [1,2,3,None,None,4,5]
root=generate_tree(l)
s=Codec()
rs=s.serialize(root)
print(rs)