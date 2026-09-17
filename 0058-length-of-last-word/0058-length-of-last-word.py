class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string into words and return the length of the last one
        return len(s.split()[-1])