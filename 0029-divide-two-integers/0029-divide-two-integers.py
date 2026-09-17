class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle boundary cases for 32-bit signed integer limits [-2^31, 2^31 - 1]
        MAX_INT = 2147483647  # 2^31 - 1
        MIN_INT = -2147483648 # -2^31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers using bit manipulation
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        while a >= b:
            temp_divisor, multiple = b, 1
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            a -= temp_divisor
            quotient += multiple
            
        return -quotient if negative else quotient