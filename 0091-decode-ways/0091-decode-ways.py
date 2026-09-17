class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # Base case: 1 way to decode an empty string at the end
        next_to_next = 0
        next_val = 1
        curr = 0
        
        for i in range(n - 1, -1, -1):
            # If the current character is '0', it cannot be decoded on its own
            if s[i] == '0':
                curr = 0
            else:
                curr = next_val
                # Check if the two-digit combination is valid (between "10" and "26")
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    curr += next_to_next
            
            # Shift pointers for the next iteration
            next_to_next = next_val
            next_val = curr
            
        return next_val