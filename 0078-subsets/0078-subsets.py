class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(index: int, path: list[int]):
            # Every state represents a valid subset
            res.append(path.copy())
            
            # Iterate through remaining elements to build subsets
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop() # Backtrack
                
        backtrack(0, [])
        return res