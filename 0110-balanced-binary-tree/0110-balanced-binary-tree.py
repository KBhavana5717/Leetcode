class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def get_height(node: TreeNode | None) -> int:
            # Base case: an empty tree has a height of 0
            if not node:
                return 0
            
            # Get height of left subtree; return -1 if unbalanced
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            
            # Get height of right subtree; return -1 if unbalanced
            right_height = get_height(node.right)
            if right_height == -1:
                return -1
            
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return the actual height of the current node
            return max(left_height, right_height) + 1
        
        return get_height(root) != -1