class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Try deleting either the left or the right character
                sub1 = s[left + 1:right + 1]
                sub2 = s[left:right]
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]
        return True