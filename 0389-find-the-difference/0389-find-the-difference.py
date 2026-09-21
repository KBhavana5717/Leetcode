class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        
        # XOR all characters from string s
        for char in s:
            ans ^= ord(char)
            
        # XOR all characters from string t
        for char in t:
            ans ^= ord(char)
            
        # Convert the resulting ASCII code back to a character
        return chr(ans)