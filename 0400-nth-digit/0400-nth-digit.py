class Solution:
    def findNthDigit(self, n: int) -> int:
        len_digits = 1
        count = 9
        start = 1
        
        # 1. Find the length of the number where the nth digit is located
        while n > len_digits * count:
            n -= len_digits * count
            len_digits += 1
            count *= 10
            start *= 10
            
        # 2. Find the exact number that contains the nth digit
        target_num = start + (n - 1) // len_digits
        
        # 3. Find the specific digit within the number
        return int(str(target_num)[(n - 1) % len_digits])