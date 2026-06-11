# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
                continue
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return " ".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(" ")
        if values[0] == "N":
            return None
        root = TreeNode(int(values[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()

            if values[i] == "N":
                node.left = None
            else:
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            if values[i+1] == "N":
                node.right = None
            else:
                node.right = TreeNode(int(values[i+1]))
                queue.append(node.right)
            i += 2
        return root

        
