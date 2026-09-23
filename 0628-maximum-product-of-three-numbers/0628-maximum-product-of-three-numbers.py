class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Sort the array to easily access smallest and largest elements
        nums.sort()
        
        # The maximum product can either be:
        # 1. The product of the three largest numbers
        # 2. The product of the two smallest numbers (negatives) and the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])