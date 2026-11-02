class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            # If left is even, move right
            if nums[left] % 2 == 0:
                left += 1
            # If right is odd, move left
            elif nums[right] % 2 != 0:
                right -= 1
            # If left is odd and right is even, swap them
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return nums   