class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def helper(left: int, right: int) -> TreeNode | None:
            # Base case: if pointers cross, return None
            if left > right:
                return None
            
            # Find the middle element to keep the tree height-balanced
            mid = (left + right) // 2
            
            # Create the root node with the middle element value
            root = TreeNode(nums[mid])
            
            # Recursively construct the left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)