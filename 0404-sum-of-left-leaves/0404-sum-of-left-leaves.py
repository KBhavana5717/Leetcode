class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sum_val = 0
        
        # Check if the left child exists and is a leaf node (no children)
        if root.left and not root.left.left and not root.left.right:
            sum_val += root.left.val
            
        # Recursively traverse left and right subtrees
        sum_val += self.sumOfLeftLeaves(root.left)
        sum_val += self.sumOfLeftLeaves(root.right)
        
        return sum_val