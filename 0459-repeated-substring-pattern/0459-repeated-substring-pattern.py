class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Trick: Double the string, remove the first and last characters, 
        # and check if 's' is still present in the middle.
        return s in (s + s)[1:-1]