class Solution:

  def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
    rows, cols = len(dungeon), len(dungeon[0])

    # Initialize a 2D DP table with infinity
    dp = [[float("inf")] * (cols + 1) for _ in range(rows + 1)]

    # Base cases for the bottom-right destination cell
    dp[rows][cols - 1] = 1
    dp[rows - 1][cols] = 1

    # Fill the DP table from bottom-right to top-left
    for r in range(rows - 1, -1, -1):
      for c in range(cols - 1, -1, -1):
        min_health_on_exit = min(dp[r + 1][c], dp[r][c + 1])
        dp[r][c] = max(1, min_health_on_exit - dungeon[r][c])

    return dp[0][0]