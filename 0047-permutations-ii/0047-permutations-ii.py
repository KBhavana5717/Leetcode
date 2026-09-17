class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        visited = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                # If the element is already used, skip it
                if visited[i]:
                    continue
                
                # If duplicate and the previous identical element was not used, skip it
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visited[i] = False
                
        backtrack([])
        return res