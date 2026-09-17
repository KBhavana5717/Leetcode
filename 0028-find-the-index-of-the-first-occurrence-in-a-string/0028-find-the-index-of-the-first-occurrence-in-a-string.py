class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Python's built-in find() method uses optimized substring search algorithms (like Boyer-Moore-Horspool)
        return haystack.find(needle)