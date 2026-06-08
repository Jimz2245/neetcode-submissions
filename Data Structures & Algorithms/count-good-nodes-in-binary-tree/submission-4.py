# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = self.good(root, root.val)
        return count

    def good(self, root, large):
        if not root:
            return 0
        if root.val >= large:
            return 1 + self.good(root.left, root.val) + self.good(root.right, root.val)
        else:
            return self.good(root.left, large) + self.good(root.right, large)

        