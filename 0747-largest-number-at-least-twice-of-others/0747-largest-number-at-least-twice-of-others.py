class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        for i, num in enumerate(nums):
            if i != max_idx and max_val < 2 * num:
                return -1
                
        return max_idx