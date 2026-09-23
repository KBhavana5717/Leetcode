# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        # Dictionary to store the frequency of prefix sums encountered so far
        prefix_sums = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the current path sum from the root
            current_sum += node.val
            
            # Find the number of valid paths ending at the current node
            # current_sum - targetSum gives the required previous prefix sum
            path_count = prefix_sums.get(current_sum - targetSum, 0)
            
            # Add current sum to the prefix sum map before visiting children
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recurse for left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            
            # Backtrack: remove the current sum from the map when leaving the node
            prefix_sums[current_sum] -= 1
            
            return path_count

        return dfs(root, 0)