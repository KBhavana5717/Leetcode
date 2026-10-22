class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7
        
        # DP table initialized with zeros
        # dp[i][j] represents the number of schemes with i members and at least j profit.
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for g, p in zip(group, profit):
            for i in range(n, g - 1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % MOD
                    
        return sum(dp[i][minProfit] for i in range(n + 1)) % MOD