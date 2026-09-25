class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base choice: print s[i] separately, solve for the rest
            res = dp(i + 1, j) + 1
            
            # Try to combine s[i] with any matching s[k]
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, dp(i, k - 1) + dp(k + 1, j))
                    
            memo[(i, j)] = res
            return res
            
        return dp(0, len(s) - 1)