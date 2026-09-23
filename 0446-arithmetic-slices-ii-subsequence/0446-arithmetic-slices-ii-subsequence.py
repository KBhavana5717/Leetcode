from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        total_count = 0
        
        # Array of dictionaries: dp[i] maps difference -> count of subsequences ending at i
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # Count of subsequences of length >= 2 ending at j with this difference
                count = dp[j][diff]
                
                # Add to total valid arithmetic slices (only those of length >= 3 contribute)
                total_count += count
                
                # Extend the subsequences from j to i, and account for the 2-length pair (j, i)
                dp[i][diff] += count + 1
                
        return total_count