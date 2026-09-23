class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert string to a list of characters for in-place modification
        chars = list(s)
        
        # Step through the string with a step size of 2 * k
        for i in range(0, len(chars), 2 * k):
            # Reverse the first k characters in the current 2k block
            chars[i:i + k] = reversed(chars[i:i + k])
            
        return "".join(chars)