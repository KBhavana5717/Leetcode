import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-indexed
        res = []
        
        factorial = math.factorial(n - 1)
        
        for i in range(n, 0, -1):
            index = k // factorial
            res.append(numbers.pop(index))
            
            if i > 1:
                k %= factorial
                factorial //= (i - 1)
                
        return "".join(res)