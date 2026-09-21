class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
            
        # Count frequencies of each character
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
            
        # Find the first character whose frequency is less than k
        for char, count in char_counts.items():
            if count < k:
                # Split the string at this character and recursively check parts
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
                
        # If all characters meet the frequency requirement, return the length of s
        return len(s)