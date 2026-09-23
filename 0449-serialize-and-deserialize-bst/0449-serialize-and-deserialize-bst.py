# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals = []
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
            
        vals = deque(map(int, data.split(",")))
        
        def build(lower: int, upper: int) -> Optional[TreeNode]:
            if not vals or not (lower < vals[0] < upper):
                return None
                
            val = vals.popleft()
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            
            return node  # Fixed: return the constructed node instead of calling build again
            
        return build(float('-inf'), float('inf'))