class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, it cannot be partitioned into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = set([0])
        
        for num in nums:
            # Create a new set of possible sums by adding the current number
            next_dp = set(dp)
            for t in dp:
                if t + num == target:
                    return True
                next_dp.add(t + num)
            dp = next_dp
            
        return target in dp