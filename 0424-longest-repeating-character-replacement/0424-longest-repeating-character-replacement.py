class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # Add current character count
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Track the frequency of the most frequent character in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # Check if the current window is valid
            # (Window Length - Frequency of most frequent character) represents 
            # the number of characters we need to replace.
            if (right - left + 1) - max_freq > k:
                # Shrink the window from the left if replacements exceed k
                count[s[left]] -= 1
                left += 1
                
            # Update the maximum valid window length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length