class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
            
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push children to stack in reverse order so that the leftmost child is processed first
            if node.children:
                for child in reversed(node.children):
                    stack.append(child)
                    
        return result