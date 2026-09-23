class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = [0] * 26
        curr_len = 0
        
        for i in range(len(s)):
            # Check if current character continues the wraparound sequence from the previous one
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                curr_len += 1
            else:
                curr_len = 1
                
            idx = ord(s[i]) - ord('a')
            count[idx] = max(count[idx], curr_len)
            
        return sum(count)