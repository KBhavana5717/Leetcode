from functools import lru_cache

class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> list[int]:
        res = []
        
        for i in range(len(expression)):
            char = expression[i]
            if char in "+-*":
                # Divide: split into left and right sub-expressions
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Conquer: combine results based on the operator
                for l in left_results:
                    for r in right_results:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        elif char == '*':
                            res.append(l * r)
                            
        # Base case: if the string is just a number, return it
        if not res:
            res.append(int(expression))
            
        return res