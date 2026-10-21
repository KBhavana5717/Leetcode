class Solution:
    def racecar(self, target: int) -> int:
        dp = [0, 1, 4]
        
        for t in range(3, target + 1):
            k = t.bit_length()
            if (1 << k) - 1 == t:
                dp.append(k)
                continue
                
            # Option 1: Go past t by k instructions, turn around, and come back
            ans = k + 1 + dp[(1 << k) - 1 - t]
            
            # Option 2: Go just before t by k - 1 instructions, turn around, go back j steps, turn around again
            for j in range(k - 1):
                ans = min(ans, (k - 1) + 1 + j + 1 + dp[t - ((1 << (k - 1)) - (1 << j))])
                
            dp.append(ans)
            
        return dp[target]