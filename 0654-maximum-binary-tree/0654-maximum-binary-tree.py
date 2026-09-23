class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Find the maximum value and its index in the current array
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        # Create the root node with the maximum value
        root = TreeNode(max_val)
        
        # Recursively build the left and right subtrees
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        
        return root