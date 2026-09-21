class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        result = 1
        
        # Ensure a is within modulo bounds initially
        a %= MOD
        
        for digit in b:
            # Each time we move to the next digit, the previous result is raised to the 10th power,
            # and multiplied by a raised to the current digit.
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD
            
        return result