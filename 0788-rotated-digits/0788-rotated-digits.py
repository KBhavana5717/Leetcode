class Solution:
    def rotatedDigits(self, n: int, s: str = "") -> int:
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if all(c in '0125689' for c in s) and any(c in '2569' for c in s):
                count += 1
        return count