class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
            
        memo = {}
        
        def dp(mask, current_total):
            if mask in memo:
                return memo[mask]
            
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if not (mask & bit):
                    # If picking this number wins immediately, or forces the opponent to lose
                    if current_total + i >= desiredTotal or not dp(mask | bit, current_total + i):
                        memo[mask] = True
                        return True
                        
            memo[mask] = False
            return False
            
        return dp(0, 0)