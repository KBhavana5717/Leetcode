class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] stores the max product for breaking integer i
        dp = [1] * (n + 1)
        
        for i in range(2, n + 1):
            for j in range(1, i):
                # Choose the maximum between not breaking further vs breaking further
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
                
        return dp[n]