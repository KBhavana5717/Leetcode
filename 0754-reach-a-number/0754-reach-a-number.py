class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        s = 0
        while s < target or (s - target) % 2 != 0:
            k += 1
            s += k
        return k