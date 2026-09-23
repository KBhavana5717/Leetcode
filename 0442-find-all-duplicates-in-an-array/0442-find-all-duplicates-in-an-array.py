class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        
        for num in nums:
            # Find the index corresponding to the current number (1-indexed to 0-indexed)
            idx = abs(num) - 1
            
            # If the value at this index is negative, it means we've seen this number before
            if nums[idx] < 0:
                result.append(abs(num))
            else:
                # Otherwise, negate the value to mark it as visited
                nums[idx] = -nums[idx]
                
        return result