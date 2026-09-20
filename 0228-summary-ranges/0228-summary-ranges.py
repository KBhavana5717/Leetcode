class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i = 0
        n = len(nums)
        
        while i < n:
            low = nums[i]
            # Advance while numbers are consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            high = nums[i]
            
            # Format and append the range
            if low == high:
                res.append(str(low))
            else:
                res.append(f"{low}->{high}")
                
            i += 1
            
        return res