from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
            
        queue = deque([root])
        null_seen = False
        
        while queue:
            node = queue.popleft()
            if not node:
                null_seen = True
            else:
                if null_seen:
                    return False
                queue.append(node.left)
                queue.append(node.right)
                
        return True