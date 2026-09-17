class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(list(path))
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                # Move to the next index (i + 1) since each element is used once
                backtrack(i + 1, path, target - candidates[i])
                path.pop()
                
        backtrack(0, [], target)
        return res