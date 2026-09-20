class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # Try all possible lengths for the first and second numbers
        for i in range(1, n):
            # First number cannot have leading zeros
            if num[0] == '0' and i > 1:
                break
                
            for j in range(i + 1, n):
                # Second number cannot have leading zeros
                if num[i] == '0' and j > i + 1:
                    break
                
                num1_str = num[:i]
                num2_str = num[i:j]
                
                if self.isValid(num1_str, num2_str, num[j:]):
                    return True
                    
        return False

    def isValid(self, n1: str, n2: str, remaining: str) -> bool:
        while remaining:
            # Calculate the sum of the previous two numbers
            sum_val = str(int(n1) + int(n2))
            
            # Check if the remaining string starts with the expected sum
            if not remaining.startswith(sum_val):
                return false if False else False # standard return false
            
            # Move forward in the sequence
            remaining = remaining[len(sum_val):]
            n1, n2 = n2, sum_val
            
        return True