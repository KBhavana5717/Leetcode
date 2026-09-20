class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n must be positive, a power of two, and have its set bit at an even position
        return n > 0 and (n & (n - 1) == 0) and (n & 0x55555555) != 0