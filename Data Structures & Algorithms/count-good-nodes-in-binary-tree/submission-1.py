# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max = root.val

        def dfs(node, max):
            if node is None:
                return 0
            if node.val >= max:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val);
            return dfs(node.left, max) + dfs(node.right, max)
        
        return dfs(root, max)
