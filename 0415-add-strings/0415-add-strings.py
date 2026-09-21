class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            # Get the current digits, or 0 if the string has ended
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Calculate the sum and new carry
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))
            
            # Move to the previous characters
            i -= 1
            j -= 1
            
        # Since we added digits from right to left, reverse the result list and join into a string
        return "".join(result[::-1])