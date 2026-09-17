# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n == 0:
            return []
            
        memo = {}
        
        def helper(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
                
            all_trees = []
            for i in range(start, end + 1):
                # Generate all left and right subtrees
                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)
                
                # Connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
                        
            memo[(start, end)] = all_trees
            return all_trees
            
        return helper(1, n)