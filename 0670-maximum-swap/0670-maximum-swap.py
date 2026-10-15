class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        last = {int(c): i for i, c in enumerate(s)}
        
        for i, c in enumerate(s):
            digit = int(c)
            for d in range(9, digit, -1):
                if d in last and last[d] > i:
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return int("".join(s))
                    
        return num