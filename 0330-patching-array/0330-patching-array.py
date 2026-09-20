class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        miss = 1
        i = 0
        length = len(nums)
        
        while miss <= n:
            if i < length and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # Patch with 'miss', which extends our coverage up to 2 * miss - 1
                miss += miss
                patches += 1
                
        return patches