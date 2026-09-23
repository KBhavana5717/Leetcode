class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = set()
        
        def backtrack(index, path):
            if len(path) >= 2:
                res.add(tuple(path))
            
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
                    
        backtrack(0, [])
        return list(res)