# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root
        if temp:
            place = temp.left
            temp.left = temp.right
            temp.right = place
            self.invertTree(temp.left)
            self.invertTree(temp.right)
        return root
        