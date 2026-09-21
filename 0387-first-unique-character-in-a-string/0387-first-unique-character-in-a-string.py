from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count frequencies of each character
        count = Counter(s)
        
        # Find the first character with a frequency of 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        return -1