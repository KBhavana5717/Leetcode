class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 3^19 is the largest power of 3 that fits within a 32-bit signed integer
        max_power_of_three = 3**19
        return n > 0 and max_power_of_three % n == 0