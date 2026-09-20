class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1  # Start with 1 slot available for the root
        
        for node in preorder.split(','):
            # If slots are exhausted before processing all nodes, it's invalid
            if slots <= 0:
                return False
            
            if node == '#':
                slots -= 1
            else:
                slots += 1  # Consumes 1 slot (-1) and adds 2 new slots (+2), net +1
                
        return slots == 0