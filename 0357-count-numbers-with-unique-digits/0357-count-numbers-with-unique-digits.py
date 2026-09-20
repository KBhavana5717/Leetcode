class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
            
        total = 10  # For n = 1 (numbers 0 to 9)
        unique_digits = 9
        available_digits = 9
        
        for i in range(2, n + 1):
            unique_digits *= available_digits
            total += unique_digits
            available_digits -= 1
            
        return total