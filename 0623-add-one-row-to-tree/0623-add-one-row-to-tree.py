class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # If depth is 1, a new root node is created with the original tree as its left subtree
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        
        if not root:
            return None
            
        # If we are at depth - 1, insert the new nodes
        if depth == 2:
            left_node = TreeNode(val)
            right_node = TreeNode(val)
            
            left_node.left = root.left
            right_node.right = root.right
            
            root.left = left_node
            root.right = right_node
        else:
            # Otherwise, traverse deeper down the tree
            self.addOneRow(root.left, val, depth - 1)
            self.addOneRow(root.right, val, depth - 1)
            
        return root