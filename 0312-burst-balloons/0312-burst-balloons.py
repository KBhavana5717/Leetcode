class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # Add 1 to the boundaries to handle edge cases
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] represents the maximum coins from bursting balloons between i and j
        dp = [[0] * n for _ in range(n)]
        
        # Length of the interval
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                # Try every balloon 'k' as the last one to be burst in this range
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
                    
        return dp[0][n - 1]