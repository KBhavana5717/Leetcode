class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            # Compute the sum of the squares of the digits
            n = sum(int(digit) ** 2 for digit in str(n))
            
        return n == 1