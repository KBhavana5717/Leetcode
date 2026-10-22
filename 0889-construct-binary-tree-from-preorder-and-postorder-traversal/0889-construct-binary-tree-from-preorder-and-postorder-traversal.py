class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # The second element in preorder is the root of the left subtree
        left_root_val = preorder[1]
        
        # Find the index of the left root in postorder to determine left subtree size
        left_size = postorder.index(left_root_val) + 1
        
        root.left = self.constructFromPrePost(
            preorder[1 : 1 + left_size],
            postorder[:left_size]
        )
        root.right = self.constructFromPrePost(
            preorder[1 + left_size:],
            postorder[left_size:-1]
        )
        
        return root