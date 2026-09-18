class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # Map each value to its index in the inorder array for O(1) lookups
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # Pointer for the current root in the postorder array (starting from the end)
        self.post_idx = len(postorder) - 1
        
        def helper(left: int, right: int) -> TreeNode | None:
            # Base case: if there are no elements to construct the subtree
            if left > right:
                return None
            
            # Select the current root value from postorder and decrement the index
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            # Find the index of this root in the inorder array
            idx = inorder_map[root_val]
            
            # Build right subtree first because we are moving backwards from postorder
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)