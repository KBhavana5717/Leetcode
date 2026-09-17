class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Generate the n-bit Gray code sequence using the formula i ^ (i >> 1)
        return [i ^ (i >> 1) for i in range(1 << n)]