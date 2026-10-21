class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Step 1: make the first column all 1s by flipping rows that start with 0
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        # Step 2: for each column, take whichever of 0s/1s is more common as 1s
        score = 0
        for j in range(n):
            ones = sum(grid[i][j] for i in range(m))
            best = max(ones, m - ones)
            score += best * (1 << (n - 1 - j))

        return score