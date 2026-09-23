class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR gives 1 where bits are different and 0 where they are the same
        xor_result = x ^ y
        
        # Count the number of set bits (1s)
        return bin(xor_result).count('1')