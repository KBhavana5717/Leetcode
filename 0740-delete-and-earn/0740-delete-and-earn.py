from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        counts = Counter(nums)
        max_val = max(nums)
        
        # This is essentially the House Robber problem
        dp = [0] * (max_val + 1)
        dp[1] = counts[1] * 1
        
        for i in range(2, max_val + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + counts[i] * i)
            
        return dp[max_val]