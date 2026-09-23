class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # stores indices
        
        # Traverse twice to simulate the circular array
        for i in range(2 * n - 1, -1, -1):
            curr_idx = i % n
            
            # Pop elements from stack that are less than or equal to current element
            while stack and nums[stack[-1]] <= nums[curr_idx]:
                stack.pop()
                
            # If stack is not found empty, the top element is the next greater number
            if stack:
                res[curr_idx] = nums[stack[-1]]
                
            # Push current index onto the stack
            stack.append(curr_idx)
            
        return res