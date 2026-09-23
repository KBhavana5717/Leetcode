class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Each land cell starts with 4 sides
                    perimeter += 4
                    
                    # If there is a land cell above, subtract 2 shared edges
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                        
                    # If there is a land cell to the left, subtract 2 shared edges
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
                        
        return perimeter