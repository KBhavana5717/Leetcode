class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(list(path))
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Pass 'i' instead of 'i + 1' to allow reuse of the same element
                backtrack(i, path, target - candidates[i])
                path.pop()
                
        backtrack(0, [], target)
        return res