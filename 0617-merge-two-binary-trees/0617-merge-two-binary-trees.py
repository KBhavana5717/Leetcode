class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If both nodes are null, return null
        if not root1 and not root2:
            return None
        
        # If root1 is null, the merged node is root2
        if not root1:
            return root2
        
        # If root2 is null, the merged node is root1
        if not root2:
            return root1
        
        # If both nodes exist, sum their values into a new node (or root1)
        root1.val += root2.val
        
        # Recursively merge the left and right children
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1