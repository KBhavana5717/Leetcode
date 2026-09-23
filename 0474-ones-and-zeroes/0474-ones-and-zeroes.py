class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # DP table where dp[i][j] stores the max subset size with i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            
            # Update DP table in reverse to simulate 0/1 knapsack
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                    
        return dp[m][n]