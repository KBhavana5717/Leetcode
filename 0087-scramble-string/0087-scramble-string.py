import functools

class Solution:
    @functools.cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
            
        # Quick pruning: if they don't have the exact same characters, return False
        if sorted(s1) != sorted(s2):
            return False
            
        n = len(s1)
        for i in range(1, n):
            # Case 1: Without swap (s1 left matches s2 left, s1 right matches s2 right)
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                return True
                
            # Case 2: With swap (s1 left matches s2 right, s1 right matches s2 left)
            if (self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])):
                return True
                
        return False