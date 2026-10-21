class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            if num % 2 == 0:
                return num == 2
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        if 8 <= n <= 11:
            return 11

        # Generate palindromes and check if they are prime
        length = len(str(n))
        while True:
            # Generate palindromes of current length
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            
            for i in range(start, end):
                s = str(i)
                # Construct palindrome
                if length % 2 == 0:
                    p = int(s + s[::-1])
                else:
                    p = int(s + s[-2::-1])
                
                if p >= n and is_prime(p):
                    return p
                    
            length += 1