class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        mark = len(s)
        
        for i in range(len(s) - 1, 0, -1):
            if s[i] < s[i - 1]:
                mark = i - 1
                s[i - 1] = str(int(s[i - 1]) - 1)
                
        for i in range(mark + 1, len(s)):
            s[i] = '9'
            
        return int("".join(s))