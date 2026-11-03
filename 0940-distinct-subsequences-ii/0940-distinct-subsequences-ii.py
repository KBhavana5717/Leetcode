class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = {}
        total = 0
        
        for char in s:
            added = (total + 1 - dp.get(char, 0)) % MOD
            dp[char] = (total + 1) % MOD
            total = (total + added) % MOD
            
        return total % MOD