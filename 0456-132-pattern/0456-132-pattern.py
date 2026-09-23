class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        third = -float('inf')  # Represents nums[k]
        
        # Traverse the array backwards from right to left
        for i in range(len(nums) - 1, -1, -1):
            # If current element is less than 'third', we found our 132 pattern
            if nums[i] < third:
                return True
            
            # Pop elements from the stack that are smaller than nums[i] 
            # and update 'third' to be the largest valid nums[k]
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
                
            # Push the current element onto the stack as a potential nums[j]
            stack.append(nums[i])
            
        return False