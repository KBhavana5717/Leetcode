class Solution:
    def flipMatchVoyage(self, root: TreeNode | None, voyage: list[int]) -> list[int]:
        res = []
        i = 0

        def dfs(node):
            nonlocal i
            if not node:
                return True
            if node.val != voyage[i]:
                return False
            
            i += 1
            if node.left and node.left.val != voyage[i]:
                res.append(node.val)
                return dfs(node.right) and dfs(node.left)
            
            return dfs(node.left) and dfs(node.right)

        if dfs(root):
            return res
        return [-1]