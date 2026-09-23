# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        
        # Step 1: Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Step 2: Node found, handle deletion cases
            
            # Case 1: Node has no left child (returns right child, whether it's None or a node)
            if not root.left:
                return root.right
            
            # Case 2: Node has no right child
            elif not root.right:
                return root.left
            
            # Case 3: Node has both children
            # Find the inorder successor (smallest in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
                
            # Replace current node's value with the successor's value
            root.val = curr.val
            
            # Delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, curr.val)
            
        return root