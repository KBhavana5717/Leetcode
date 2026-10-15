class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        import math
        min_repeats = math.ceil(len(b) / len(a))
        
        if b in a * min_repeats:
            return min_repeats
        if b in a * (min_repeats + 1):
            return min_repeats + 1
            
        return -1