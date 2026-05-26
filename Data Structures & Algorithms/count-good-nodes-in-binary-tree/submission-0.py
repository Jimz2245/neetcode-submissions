# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        q = collections.deque()
        q.append(root)
        qm = collections.deque()
        qm.append(root.val)
        while q:
            node = q.popleft()
            val = qm.popleft()
            if node:
                current_max = max(val, node.val)
                if node.val >= val:
                    ret += 1
                if node.left:
                    q.append(node.left)
                    qm.append(current_max)
                if node.right:
                    q.append(node.right)
                    qm.append(current_max)
        return ret
