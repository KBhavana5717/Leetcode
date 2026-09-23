class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Calculate total absolute differences from the median
        return sum(abs(num - median) for num in nums)