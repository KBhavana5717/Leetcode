from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        max_time = -1
        res = ""
        
        for p in permutations(arr):
            h = p[0] * 10 + p[1]
            m = p[2] * 10 + p[3]
            if h < 24 and m < 60:
                current_time = h * 60 + m
                if current_time > max_time:
                    max_time = current_time
                    res = f"{p[0]}{p[1]}:{p[2]}{p[3]}"
                    
        return res