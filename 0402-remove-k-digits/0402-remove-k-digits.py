class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Pop from the stack if the current digit is smaller than the last one,
            # and we still have digits left to remove (k > 0)
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # If we still need to remove digits, pop from the end (since it's a monotonic stack)
        if k > 0:
            stack = stack[:-k]
            
        # Convert stack to string and remove any leading zeros
        result = "".join(stack).lstrip('0')
        
        # Return "0" if the result is empty
        return result if result else "0"