from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        count = Counter(arr)
        
        # Sort by absolute value to handle smaller values/zeros first
        for x in sorted(arr, key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] < count[x]:
                return False
            count[2 * x] -= count[x]
            count[x] = 0
            
        return True