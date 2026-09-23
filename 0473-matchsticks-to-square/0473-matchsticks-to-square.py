class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_len = sum(matchsticks)
        
        # A square must have 4 equal sides
        if total_len % 4 != 0 or len(matchsticks) < 4:
            return False
            
        target = total_len // 4
        
        # Sort in descending order to optimize pruning
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > target:
            return False
            
        sides = [0] * 4
        
        def dfs(index):
            if index == len(matchsticks):
                # All matchsticks placed successfully
                return sides[0] == sides[1] == sides[2] == target
                
            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                    
                # Pruning: if this side is empty, trying other empty sides will be redundant
                if sides[i] == 0:
                    break
                    
            return False
            
        return dfs(0)