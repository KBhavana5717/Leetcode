class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces, reverse each individual word, and join them back with spaces
        return " ".join(word[::-1] for word in s.split())