class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        banned = {tuple(m) for m in mines}
        dp = [[0] * n for _ in range(n)]
        ans = 0
        
        for r in range(n):
            # Left
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count
            # Right
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
                
        for c in range(n):
            # Up
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
            # Down
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
                ans = max(ans, dp[r][c])
                
        return ans