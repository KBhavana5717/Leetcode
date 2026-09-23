class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
            
        upper = 10**n - 1
        lower = 10**(n - 1)
        max_val = upper * upper
        
        # Construct the first half from the maximum possible value downwards
        for left in range(upper, lower - 1, -1):
            # Create a palindrome by mirroring the left half
            palindrome = int(str(left) + str(left)[::-1])
            
            if palindrome > max_val:
                continue
                
            # Check if this palindrome can be expressed as the product of two n-digit numbers
            i = upper
            while i * i >= palindrome:
                if palindrome % i == 0:
                    return palindrome % 1337
                i -= 1
                
        return 0