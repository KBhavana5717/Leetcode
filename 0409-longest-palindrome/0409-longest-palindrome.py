from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count the frequency of each character
        count = Counter(s)
        length = 0
        has_odd = False
        
        for freq in count.values():
            # Add the largest even part of each character's frequency
            length += (freq // 2) * 2
            # If the frequency is odd, we can use one odd character in the center
            if freq % 2 == 1:
                has_odd = True
                
        # If there is at least one character with an odd frequency, 
        # we can place one in the exact middle of the palindrome
        if has_odd:
            length += 1
            
        return length