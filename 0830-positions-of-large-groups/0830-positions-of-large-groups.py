class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                res.append([i, j - 1])
            i = j
        return res