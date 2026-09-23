from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Ensure mid is even so we can check pairs (mid, mid + 1)
            if mid % 2 == 1:
                mid -= 1
                
            # If the pair matches, the single element is in the right half
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                # Otherwise, the single element is in the left half (including mid)
                right = mid
                
        return nums[left]