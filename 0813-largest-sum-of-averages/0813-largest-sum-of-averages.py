class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
        # dp[i] represents the max score for prefix of length i using at most current partitions
        dp = [0.0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = prefix_sum[i] / i
            
        for p in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            for i in range(p, n + 1):
                for j in range(p - 1, i):
                    new_dp[i] = max(new_dp[i], dp[j] + (prefix_sum[i] - prefix_sum[j]) / (i - j))
            dp = new_dp
            
        return dp[n]