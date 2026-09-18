class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        
        def dfs(node: TreeNode | None, current_sum: int, path: list[int]):
            if not node:
                return
            
            # Add current node to path and update the remaining sum
            path.append(node.val)
            
            # Check if it's a leaf node and matches the target sum
            if not node.left and not node.right and current_sum == node.val:
                result.append(list(path)) # Append a copy of the valid path
            else:
                # Recurse down left and right subtrees
                dfs(node.left, current_sum - node.val, path)
                dfs(node.right, current_sum - node.val, path)
            
            # Backtrack: remove the current node before returning to the parent
            path.pop()
            
        dfs(root, targetSum, [])
        return result