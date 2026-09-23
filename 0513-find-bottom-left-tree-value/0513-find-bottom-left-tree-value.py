from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        queue = deque([root])
        bottom_left_val = 0
        
        while queue:
            node = queue.popleft()
            
            # Update bottom_left_val at the start of each level
            # We assign from right to left so the very first popped element 
            # of the last level ends up being the leftmost element.
            bottom_left_val = node.val
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
                
        return bottom_left_val