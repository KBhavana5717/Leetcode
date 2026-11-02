class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        ones_count = 0
        
        for char in s:
            if char == '1':
                ones_count += 1
            else:
                flips = min(flips + 1, ones_count)
                
        return flips