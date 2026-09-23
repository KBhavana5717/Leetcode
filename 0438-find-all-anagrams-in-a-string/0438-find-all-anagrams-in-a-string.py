class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26
        
        # Initialize frequency arrays for pattern p and the first window in s
        for i in range(m):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
            
        result = []
        if p_count == s_count:
            result.append(0)
            
        # Slide the window over string s
        for i in range(m, n):
            # Add the new character entering the window on the right
            s_count[ord(s[i]) - ord('a')] += 1
            # Remove the old character leaving the window on the left
            s_count[ord(s[i - m]) - ord('a')] -= 1
            
            # If the frequency counts match, record the starting index
            if p_count == s_count:
                result.append(i - m + 1)
                
        return result