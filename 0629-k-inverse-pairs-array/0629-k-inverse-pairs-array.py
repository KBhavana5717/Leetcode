class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[j] will store the number of arrays of the current length with j inverse pairs
        dp = [0] * (k + 1)
        dp[0] = 1  # Base case: 1 array of length 1 with 0 inverse pairs
        
        for i in range(2, n + 1):
            temp = [0] * (k + 1)
            total = 0
            for j in range(k + 1):
                # Add the value from dp[j]
                total = (total + dp[j]) % MOD
                
                # If the window size exceeds i, subtract the element that falls out of the window
                if j >= i:
                    total = (total - dp[j - i] + MOD) % MOD
                
                temp[j] = total
            dp = temp
            
        return dp[k]