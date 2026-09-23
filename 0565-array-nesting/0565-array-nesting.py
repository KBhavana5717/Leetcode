class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_len = 0
        visited = [False] * len(nums)
        
        for i in range(len(nums)):
            if not visited[i]:
                curr_len = 0
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = nums[curr]
                    curr_len += 1
                max_len = max(max_len, curr_len)
                
        return max_len