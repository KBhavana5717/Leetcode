class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] represents the minimum money needed to guarantee a win for range [i, j]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Length of the range we are checking
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                # Try every number k in the range [i, j] as the first guess
                for k in range(i, j + 1):
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], cost)
                    
        return dp[1][n]