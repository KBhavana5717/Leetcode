class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root or root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)