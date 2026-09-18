# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
            
        stack = [root]
        result = []
        
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            
            # Push right first so that left is processed first
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
        return result