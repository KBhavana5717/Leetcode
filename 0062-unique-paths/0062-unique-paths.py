class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D DP array with 1s for the first row
        dp = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
                
        return dp[-1]