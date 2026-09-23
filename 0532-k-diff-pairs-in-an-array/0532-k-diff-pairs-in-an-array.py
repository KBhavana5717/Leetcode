from collections import Counter
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
            
        count = Counter(nums)
        pairs = 0
        
        for num in count:
            if k == 0:
                # If k is 0, we need at least 2 occurrences of the same number
                if count[num] > 1:
                    pairs += 1
            else:
                # If k > 0, check if num + k exists in the counter
                if num + k in count:
                    pairs += 1
                    
        return pairs