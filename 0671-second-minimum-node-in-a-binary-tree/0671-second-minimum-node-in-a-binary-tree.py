class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        min_val = root.val
        ans = float('inf')
        
        def dfs(node):
            nonlocal ans
            if not node:
                return
            if min_val < node.val < ans:
                ans = node.val
            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return ans if ans != float('inf') else -1