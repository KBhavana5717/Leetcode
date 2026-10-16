class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [0] * (n + 1)
        
        # Base case: when s1 is empty, we must delete all characters of s2
        for j in range(n - 1, -1, -1):
            dp[j] = dp[j + 1] + ord(s2[j])
            
        for i in range(m - 1, -1, -1):
            new_dp = [0] * (n + 1)
            # Base case: when s2 is empty, we must delete all remaining characters of s1
            new_dp[n] = dp[n] + ord(s1[i])
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    new_dp[j] = dp[j + 1]
                else:
                    new_dp[j] = min(
                        ord(s1[i]) + dp[j],
                        ord(s2[j]) + new_dp[j + 1]
                    )
            dp = new_dp
            
        return dp[0]