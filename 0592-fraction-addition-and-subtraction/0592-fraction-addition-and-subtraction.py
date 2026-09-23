import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Find all fractions with their respective signs (e.g., "-1/2", "+1/2")
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        
        numerator = 0
        denominator = 1
        
        # Process pairs of (numerator, denominator)
        for i in range(0, len(nums), 2):
            num = nums[i]
            den = nums[i+1]
            
            numerator = numerator * den + num * denominator
            denominator *= den
            
            # Simplify fraction to prevent integer overflow
            common_divisor = abs(gcd(numerator, denominator))
            numerator //= common_divisor
            denominator //= common_divisor
            
        return f"{numerator}/{denominator}"