# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
            
        stack = [root]
        result = []
        
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            
            # Push left first so that right is popped and processed first
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        # Reverse the result to get Left -> Right -> Root order
        return result[::-1]