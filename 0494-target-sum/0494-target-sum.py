class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        
        def dp(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Try adding '+' or '-' to the current number
            add = dp(index + 1, current_sum + nums[index])
            subtract = dp(index + 1, current_sum - nums[index])
            
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]
            
        return dp(0, 0)