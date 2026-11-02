class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)
        count = 0
        
        # Helper function to check if a number is a palindrome
        def is_palindrome(n: int) -> bool:
            s = str(n)
            return s == s[::-1]

        # Generate palindromes up to 10^9 (square root of 10^18)
        # We generate roots up to length 5 (e.g., 1 to 99999)
        # Odd and even length palindromes are generated using a mirror approach.
        
        # Single digit base cases or direct check for small roots
        for length in range(1, 10):
            # Generate palindromes for this length
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            
            for i in range(start, end):
                s = str(i)
                if length % 2 == 1:
                    # Odd length palindrome: e.g., 123 -> 12321
                    p_str = s + s[:-1][::-1]
                else:
                    # Even length palindrome: e.g., 123 -> 123321
                    p_str = s + s[::-1]
                
                root = int(p_str)
                # Max root can be 10^9, since (10^9)^2 = 10^18
                if root > 10**9:
                    break
                    
                sq = root * root
                if sq > R:
                    break
                    
                if sq >= L and is_palindrome(sq):
                    count += 1
                    
        return count