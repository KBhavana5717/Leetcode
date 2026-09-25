from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        max_width = 0
        # Queue stores tuples of (node, index)
        queue = deque([(root, 0)])
        
        while queue:
            level_length = len(queue)
            # The index of the first node in the current level
            left_index = queue[0][1]
            
            for _ in range(level_length):
                node, index = queue.popleft()
                
                # Normalize index for the current level to prevent overflow
                current_index = index - left_index
                
                if node.left:
                    queue.append((node.left, 2 * current_index))
                if node.right:
                    queue.append((node.right, 2 * current_index + 1))
            
            # Width of the current level
            max_width = max(max_width, current_index + 1)
            
        return max_width