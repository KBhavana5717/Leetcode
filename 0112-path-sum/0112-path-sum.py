class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # Base case: if the tree is empty, there are no paths
        if not root:
            return False
        
        # Check if we are at a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check left and right subtrees with the reduced target sum
        remaining_sum = targetSum - root.val
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum)