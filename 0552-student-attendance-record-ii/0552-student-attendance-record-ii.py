class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initial states for n = 1:
        # P: ends in 'P' (length 1: "P") -> count = 1
        # L1: ends in one 'L' (length 1: "L") -> count = 1
        # L2: ends in two 'L's -> count = 0
        # A0: ends in 'A' with 0 previous 'A's (length 1: "A") -> count = 1
        # A1: ends in 'A' with 1 previous 'A' and one 'L' -> count = 0
        # A2: ends in 'A' with 2 consecutive 'L's -> count = 0
        
        P, L1, L2, A0, A1, A2 = 1, 1, 0, 1, 0, 0
        
        if n == 1:
            return (P + L1 + L2 + A0 + A1 + A2) % MOD
            
        for _ in range(2, n + 1):
            new_P = (P + L1 + L2) % MOD
            new_L1 = P
            new_L2 = L1
            new_A0 = (P + L1 + L2 + A0 + A1 + A2) % MOD
            new_A1 = A0
            new_A2 = A1
            
            P, L1, L2, A0, A1, A2 = new_P, new_L1, new_L2, new_A0, new_A1, new_A2
            
        return (P + L1 + L2 + A0 + A1 + A2) % MOD