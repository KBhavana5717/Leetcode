class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    
        backtrack([])
        return res