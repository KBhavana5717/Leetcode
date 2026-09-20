# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the leftmost node of the current node
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # Current must be None at this point, so pop from stack
            curr = stack.pop()
            
            # Decrement k, and if k becomes 0, we found our kth smallest element
            k -= 1
            if k == 0:
                curr_val = curr.val
                return curr_val
                
            # We have visited the node and its left subtree. Now, right subtree.
            curr = curr.right
        