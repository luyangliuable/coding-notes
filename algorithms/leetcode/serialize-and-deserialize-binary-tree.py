# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node) -> None:
            if not node:
                res.append('N')
                return

            res.append(str( node.val ))
            res.append(dfs(node.left))
            res.append(dfs(node.right))

        dfs(root)

        return ",".join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        a = data.split(",")
        self.i = 0

        def dfs():
            if a[self.i] == 'N':
                return None

            node = TreeNode(a[self.i])

            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()



        

# Your Codec object will be instantiated and called as such:
ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

t = TreeNode('a', TreeNode('b', TreeNode('d', TreeNode('e'), TreeNode('f'))), TreeNode('c'))
print( ser.serialize(t) );
