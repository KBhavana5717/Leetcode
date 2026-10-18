class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        memo = {}

        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 == n or c1 == n or r2 == n or c2 == n or \
               grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')
            
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            
            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]
            
            cherries = grid[r1][c1]
            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]
                
            cherries += max(
                dp(r1 + 1, c1, r2 + 1),  # Down, Down
                dp(r1 + 1, c1, r2),      # Down, Right
                dp(r1, c1 + 1, r2 + 1),  # Right, Down
                dp(r1, c1 + 1, r2)       # Right, Right
            )
            
            memo[(r1, c1, r2)] = cherries
            return cherries

        return max(0, dp(0, 0, 0))