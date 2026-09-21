from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequencies of characters in both strings
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        # Check if magazine has enough of each character
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
                
        return True