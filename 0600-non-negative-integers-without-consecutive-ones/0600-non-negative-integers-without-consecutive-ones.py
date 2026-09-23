class Solution:
    def findIntegers(self, n: int) -> int:
        # Convert n to its binary representation string (e.g., "101")
        s = bin(n)[2:]
        length = len(s)
        
        # f[i] will store the count of valid binary strings of length i without consecutive ones.
        # This follows Fibonacci-like growth (Fib(2) = 2, Fib(3) = 3, Fib(4) = 5, etc.)
        f = [0] * (length + 1)
        f[0] = 1
        if length > 1:
            f[1] = 2
        for i in range(2, length + 1):
            f[i] = f[i - 1] + f[i - 2]
            
        ans = 0
        prev_bit = '0'
        
        # Iterate through the binary representation of n from left to right
        for i in range(length):
            bit = s[i]
            if bit == '1':
                # If the current bit is '1', we can safely place '0' at this position 
                # and all valid combinations for the remaining bits can be added.
                ans += f[length - 1 - i]
                
                # If we encounter consecutive ones, any further bits won't form valid numbers,
                # so we break out of the loop.
                if prev_bit == '1':
                    return ans
                prev_bit = '1'
            else:
                prev_bit = '0'
                
        # Include `n` itself if its binary representation is valid
        return ans + 1