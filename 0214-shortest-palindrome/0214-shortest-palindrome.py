class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
            
        rev_s = s[::-1]
        # Combine s, a special separator, and its reverse
        new_string = s + "#" + rev_s
        
        # Build the KMP table (LPS array) for new_string
        lps = [0] * len(new_string)
        j = 0
        for i in range(1, len(new_string)):
            while j > 0 and new_string[i] != new_string[j]:
                j = lps[j - 1]
            if new_string[i] == new_string[j]:
                j += 1
                lps[i] = j
                
        # The last value of lps gives the length of the longest palindromic prefix of s
        palindrome_len = lps[-1]
        
        # Take the remaining characters from the reverse that are not in the palindromic prefix
        add_to_front = rev_s[:len(s) - palindrome_len]
        
        return add_to_front + s     