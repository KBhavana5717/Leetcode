class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to get 32-bit integer range
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # Calculate sum without carry, and carry value, masked to 32 bits
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
            
        # If a is negative (exceeds MAX_INT in 32-bit space), convert it to Python's signed negative integer
        return a if a <= MAX_INT else ~(a ^ MASK)