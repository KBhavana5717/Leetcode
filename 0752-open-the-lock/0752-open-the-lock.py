from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
            
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            curr, turns = queue.popleft()
            
            if curr == target:
                return turns
                
            for i in range(4):
                digit = int(curr[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    next_state = curr[:i] + str(new_digit) + curr[i+1:]
                    
                    if next_state not in dead and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
                        
        return -1