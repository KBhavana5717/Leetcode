class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        
        for i in range(len(nums)):
            # If the window exceeds size k, remove the oldest element
            if i > k:
                window.remove(nums[i - k - 1])
                
            # If the current number is already in the window, we found a duplicate
            if nums[i] in window:
                return True
                
            window.add(nums[i])
            
        return False