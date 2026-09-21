class Solution:
    def countSegments(self, s: str) -> int:
        # split() without arguments splits by whitespace and filters out empty strings
        return len(s.split())