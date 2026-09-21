"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add all children of the current node to the queue
                if node.children:
                    for child in node.children:
                        queue.append(child)
                        
            result.append(current_level)
            
        return result