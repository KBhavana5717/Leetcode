class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort the array
        sorted_nums = sorted(nums)
        n = len(nums)
        
        # Split into lower and upper halves
        mid = (n + 1) // 2
        lower = sorted_nums[:mid]
        upper = sorted_nums[mid:]
        
        # Interleave the elements into nums in-place
        nums[::2] = lower[::-1]
        nums[1::2] = upper[::-1]