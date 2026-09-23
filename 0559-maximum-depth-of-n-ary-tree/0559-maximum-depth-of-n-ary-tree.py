"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case: if the tree is empty, depth is 0
        if not root:
            return 0
        
        # If the node has no children (or children list is empty), its depth is 1
        if not root.children:
            return 1
        
        # Recursively find the maximum depth among all child subtrees and add 1 for the current node
        max_child_depth = max(self.maxDepth(child) for child in root.children)
        
        return max_child_depth + 1