class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low, high = 0, len(s)
        res = []
        for char in s:
            if char == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append(low)
        return res