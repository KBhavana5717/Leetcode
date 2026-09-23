class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))
        
        height = get_height(root)
        m = height + 1
        n = (1 << (height + 1)) - 1
        
        res = [["" for _ in range(n)] for _ in range(m)]
        
        def fill(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            # Ensure the shift count is never negative
            shift = height - r - 1
            if shift < 0:
                return
            offset = 1 << shift
            
            if node.left:
                fill(node.left, r + 1, c - offset)
            if node.right:
                fill(node.right, r + 1, c + offset)
                
        fill(root, 0, (n - 1) // 2)
        return res