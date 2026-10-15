class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
                
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            left_path = 0
            right_path = 0
            
            if node.left and node.left.val == node.val:
                left_path = left_len + 1
            if node.right and node.right.val == node.val:
                right_path = right_len + 1
                
            self.ans = max(self.ans, left_path + right_path)
            return max(left_path, right_path)
            
        dfs(root)
        return self.ans