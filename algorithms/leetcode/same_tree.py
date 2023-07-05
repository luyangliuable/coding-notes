

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Beats 98.71%
        # The order we check the base conditions matter
        # Reducing number of checks and operations increasing performance

        def dfs(a, b):
            if a == None and b == None:
                return True

            if b and a and a.val == b.val:
                return dfs(a.right, b.right) and dfs(a.left, b.left)
            else:
                return False


        return dfs(p, q)

