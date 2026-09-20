from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()  # stores indices
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # Remove elements from the back that are smaller than the current element
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            # Add current element index
            q.append(i)
            
            # Record the maximum for the window once we reach size k
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res