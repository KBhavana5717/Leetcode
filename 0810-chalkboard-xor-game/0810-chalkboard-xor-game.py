class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        from functools import reduce
        from operator import xor
        
        if reduce(xor, nums) == 0:
            return True
        return len(nums) % 2 == 0