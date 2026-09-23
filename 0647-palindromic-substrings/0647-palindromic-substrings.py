class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        for i in range(n):
            # Check for odd-length palindromes (single character center)
            count += self.expandAroundCenter(s, i, i)
            # Check for even-length palindromes (two character center)
            count += self.expandAroundCenter(s, i, i + 1)
            
        return count
        
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        sub_count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            sub_count += 1
            left -= 1
            right += 1
        return sub_count