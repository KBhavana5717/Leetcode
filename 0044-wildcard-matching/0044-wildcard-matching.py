class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        star_idx = -1
        match_idx = 0
        
        while i < len(s):
            # Case 1: Direct match or '?' wildcard
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            # Case 2: '*' wildcard encountered, store position
            elif j < len(p) and p[j] == '*':
                star_idx = j
                match_idx = i
                j += 1
            # Case 3: Mismatch, but we can fallback to the last '*'
            elif star_idx != -1:
                j = star_idx + 1
                match_idx += 1
                i = match_idx
            # Case 4: Mismatch and no '*' to fallback on
            else:
                return False
                
        # Check remaining characters in pattern are all '*'
        while j < len(p) and p[j] == '*':
            j += 1
            
        return j == len(p)