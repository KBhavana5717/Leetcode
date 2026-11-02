from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_sum += num
            if current_sum - goal in prefix_sums:
                total_subarrays += prefix_sums[current_sum - goal]
            prefix_sums[current_sum] += 1
            
        return total_subarrays