class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        violation_count = 0
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                violation_count += 1
                if violation_count > 1:
                    return False
                
                # Decide whether to modify nums[i] or nums[i + 1]
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    # If the element before i is greater than nums[i+1],
                    # we must raise nums[i+1] to equal nums[i]
                    nums[i + 1] = nums[i]
                else:
                    # Otherwise, lower nums[i] to equal nums[i+1]
                    nums[i] = nums[i + 1]
                    
        return True