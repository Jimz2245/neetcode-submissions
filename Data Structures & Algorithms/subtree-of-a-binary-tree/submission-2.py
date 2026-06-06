# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            

    def sameTree(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None or s.val != t.val:
            return False
        else:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
