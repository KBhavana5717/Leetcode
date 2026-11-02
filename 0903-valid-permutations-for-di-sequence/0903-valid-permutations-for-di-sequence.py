class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1] * (n + 1)
        
        for char in s:
            new_dp = [0] * (len(dp) - 1)
            if char == 'I':
                curr_sum = 0
                for j in range(len(new_dp)):
                    curr_sum = (curr_sum + dp[j]) % MOD
                    new_dp[j] = curr_sum
            else:
                curr_sum = 0
                for j in range(len(new_dp) - 1, -1, -1):
                    curr_sum = (curr_sum + dp[j + 1]) % MOD
                    new_dp[j] = curr_sum
            dp = new_dp
            
        return dp[0]