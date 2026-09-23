class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        
        def dfs(r, c, moves):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            if moves == 0:
                return 0
                
            if (r, c, moves) in memo:
                return memo[(r, c, moves)]
                
            ans = 0
            ans = (ans + dfs(r + 1, c, moves - 1)) % MOD
            ans = (ans + dfs(r - 1, c, moves - 1)) % MOD
            ans = (ans + dfs(r, c + 1, moves - 1)) % MOD
            ans = (ans + dfs(r, c - 1, moves - 1)) % MOD
            
            memo[(r, c, moves)] = ans
            return ans
            
        return dfs(startRow, startColumn, maxMove)