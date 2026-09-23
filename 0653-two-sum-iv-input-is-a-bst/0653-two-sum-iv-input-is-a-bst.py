class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def dfs(node):
            if not node:
                return False
            
            # Check if the complement needed to reach target k exists
            complement = k - node.val
            if complement in seen:
                return True
            
            seen.add(node.val)
            
            # Recursively search left and right subtrees
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)