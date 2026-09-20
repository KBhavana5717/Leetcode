class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        sign = '+'
        n = len(s)
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
                
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if sign == '+':
                    stack.append(current_number)
                elif sign == '-':
                    stack.append(-current_number)
                elif sign == '*':
                    stack.append(stack.pop() * current_number)
                elif sign == '/':
                    # Python's // rounds down towards negative infinity, 
                    # but problem requires truncating toward zero.
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-((-prev) // current_number))
                    else:
                        stack.append(prev // current_number)
                        
                sign = char
                current_number = 0
                
        return sum(stack)