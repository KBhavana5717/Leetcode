from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            
            # Optimization: merge consecutive boxes of the same color on the left
            while i < j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1
                
            # Option 1: remove the current block of k + 1 boxes
            res = (k + 1) * (k + 1) + dp(i + 1, j, 0)
            
            # Option 2: find a matching box later in the array to combine with our current block
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
                    
            return res

        return dp(0, len(boxes) - 1, 0)