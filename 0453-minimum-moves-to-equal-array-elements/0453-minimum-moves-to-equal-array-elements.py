class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # Sum of all elements minus (minimum element * number of elements)
        return sum(nums) - len(nums) * min(nums)