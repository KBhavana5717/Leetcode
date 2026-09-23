class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        result = str(root.val)
        
        # If there is a left child, or if there is no left child but there is a right child
        if root.left or root.right:
            result += "(" + self.tree2str(root.left) + ")"
            
        # If there is a right child, we must include it
        if root.right:
            result += "(" + self.tree2str(root.right) + ")"
            
        return result