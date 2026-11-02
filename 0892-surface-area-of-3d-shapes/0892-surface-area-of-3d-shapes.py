class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total_area = 0
        
        for r in range(n):
            for c in range(n):
                v = grid[r][c]
                if v > 0:
                    # Add top and bottom faces + all 4 sides per cube
                    total_area += 2 + (4 * v)
                    
                    # Subtract overlapping faces with neighbors
                    if r > 0:
                        total_area -= min(v, grid[r - 1][c])  # Top neighbor
                    if r < n - 1:
                        total_area -= min(v, grid[r + 1][c])  # Bottom neighbor
                    if c > 0:
                        total_area -= min(v, grid[r][c - 1])  # Left neighbor
                    if c < n - 1:
                        total_area -= min(v, grid[r][c + 1])  # Right neighbor
                        
        return total_area