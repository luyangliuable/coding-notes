class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return root

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
