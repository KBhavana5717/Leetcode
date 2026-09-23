class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        
        # Step 1: Find the first decreasing digit from the right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        # If no such digit exists, the digits are in descending order (e.g., 21)
        if i < 0:
            return -1
            
        # Step 2: Find the smallest digit to the right of 'i' that is greater than digits[i]
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        # Step 3: Swap digits[i] and digits[j]
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the sublist from i + 1 to the end to get the smallest combination
        digits[i + 1:] = reversed(digits[i + 1:])
        
        # Convert back to an integer
        result = int("".join(digits))
        
        # Check if the result fits in a 32-bit signed integer range
        if result > 2**31 - 1:
            return -1
            
        return result