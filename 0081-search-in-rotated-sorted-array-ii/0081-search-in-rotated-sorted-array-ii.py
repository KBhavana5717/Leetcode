class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle duplicates where we cannot determine the sorted half
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Check if the left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False