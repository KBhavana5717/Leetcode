# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:
        
        def dfs(node):
            # Base case: if node is None, return (0, 0) -> (rob, not_rob)
            if not node:
                return (0, 0)
                
            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)
            
            # If we rob this node, we cannot rob its children
            rob_current = node.val + left_not_rob + right_not_rob
            
            # If we don't rob this node, we can choose to either rob or not rob its children
            not_rob_current = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
            
            return (rob_current, not_rob_current)
            
        return max(dfs(root))