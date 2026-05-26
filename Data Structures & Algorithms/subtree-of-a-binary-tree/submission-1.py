# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root is None and subRoot is None
        if root.val == subRoot.val:
            if self.compare(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def compare(self, root, subRoot) -> bool:
        if root is None or subRoot is None:
            return root is None and subRoot is None
        if root.val == subRoot.val:
            return True and self.compare(root.left, subRoot.left) and self.compare(root.right, subRoot.right)
        else:
            return False
        
        