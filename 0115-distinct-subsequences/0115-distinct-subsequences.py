class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] represents the number of distinct subsequences of s that form t[0..j-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # An empty string t can always be formed 1 time by any prefix of s
        
        for i in range(1, m + 1):
            # Traverse backwards to use values from the previous row correctly
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]