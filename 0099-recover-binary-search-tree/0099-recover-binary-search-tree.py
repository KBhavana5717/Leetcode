# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        curr = root
        
        # Morris In-Order Traversal
        while curr:
            if curr.left:
                # Find the predecessor (rightmost node in the left subtree)
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                    
                if not pred.right:
                    pred.right = curr  # Establish temporary link
                    curr = curr.left
                else:
                    pred.right = None  # Remove temporary link
                    # Check for BST violation
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right
            else:
                # Check for BST violation
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
                
        # Swap the values of the two corrupted nodes to recover the BST
        if first and second:
            first.val, second.val = second.val, first.val