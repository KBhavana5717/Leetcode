class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Valid moves for each key on the dialer pad
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        # Initialize counts for each digit for length 1
        dp = [1] * 10
        
        for _ in range(n - 1):
            next_dp = [0] * 10
            for i in range(10):
                for nxt in moves[i]:
                    next_dp[nxt] = (next_dp[nxt] + dp[i]) % MOD
            dp = next_dp
            
        return sum(dp) % MOD