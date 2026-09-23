from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
            
        sum_counts = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
                
            # Calculate subtree sum for the current node
            current_sum = node.val + dfs(node.left) + dfs(node.right)
            sum_counts[current_sum] += 1
            return current_sum
            
        dfs(root)
        
        # Find the maximum frequency among all sums
        max_freq = max(sum_counts.values())
        
        # Collect all sums that have the maximum frequency
        return [s for s, freq in sum_counts.items() if freq == max_freq]