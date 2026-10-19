class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        for i, x in enumerate(nums):
            if abs(x - i) > 1:
                return False
        return True