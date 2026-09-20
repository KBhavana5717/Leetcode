class Solution:

  def numIslands(self, grid: list[list[str]]) -> int:
    if not grid:
      return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r: int, c: int) -> None:
      # Base case: check bounds and if current cell is water ('0')
      if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
        return

      # Mark the current cell as visited by changing it to '0'
      grid[r][c] = '0'

      # Recursively visit all 4 adjacent directions
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '1':
          island_count += 1
          dfs(r, c)  # Sink the entire island

    return island_count