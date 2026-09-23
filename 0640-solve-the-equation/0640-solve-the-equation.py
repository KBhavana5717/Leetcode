class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluate(expr):
            # Helper to parse and evaluate one side of the equation
            # Returns [coefficient of x, constant value]
            import re
            tokens = re.findall(r'[+-]?[^-+]+', expr)
            x_coeff = 0
            const = 0
            
            for token in tokens:
                if 'x' in token:
                    if token == 'x' or token == '+x':
                        x_coeff += 1
                    elif token == '-x':
                        x_coeff -= 1
                    else:
                        x_coeff += int(token[:-1])
                else:
                    const += int(token)
            return x_coeff, const

        left_side, right_side = equation.split('=')
        left_x, left_c = evaluate(left_side)
        right_x, right_c = evaluate(right_side)
        
        # Bring all x terms to the left and constants to the right
        # left_x * x + left_c = right_x * x + right_c
        # (left_x - right_x) * x = right_c - left_c
        
        total_x = left_x - right_x
        total_c = right_c - left_c
        
        if total_x == 0:
            if total_c == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        ans = total_c // total_x
        return f"x={ans}"