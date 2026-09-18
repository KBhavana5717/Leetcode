# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, current_sum: int) -> int:
            if not node:
                return 0
            
            # Update the current number along the path
            current_sum = current_sum * 10 + node.val
            
            # If it's a leaf node, return the path sum
            if not node.left and not node.right:
                return current_sum
            
            # Recurse for left and right children
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
            
        return dfs(root, 0)