class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start: int, path: list[int]):
            # If the combination is of size k, add it to results
            if len(path) == k:
                res.append(path.copy())
                return
            
            # Pruning: only loop up to the point where we still have enough numbers left
            needed = k - len(path)
            for i in range(start, n - needed + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return res