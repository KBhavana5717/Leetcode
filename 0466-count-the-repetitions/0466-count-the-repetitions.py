class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        n = len(s2)
        d = {}
        
        # Precompute transitions for each starting index in s2
        for i in range(n):
            cnt = 0
            j = i
            for c in s1:
                if c == s2[j]:
                    j += 1
                    if j == n:
                        cnt += 1
                        j = 0
            d[i] = (cnt, j)
            
        ans = 0
        j = 0
        # Iterate n1 times using the precomputed state transitions
        for _ in range(n1):
            cnt, j = d[j]
            ans += cnt
            
        return ans // n2