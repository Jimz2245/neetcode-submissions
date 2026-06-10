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
            node = temp.right
            temp.right = temp.left
            temp.left = node
            self.invertTree(temp.right)
            self.invertTree(temp.left)
        return root
































        