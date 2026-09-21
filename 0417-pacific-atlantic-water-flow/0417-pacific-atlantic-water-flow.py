class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable):
            reachable.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable:
                    # Water flows from a cell to a neighbor if the neighbor's height 
                    # is greater than or equal to the current cell's height (reverse flow)
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable)
                        
        # Traverse from the ocean borders inward
        for r in range(rows):
            dfs(r, 0, pacific_reachable)         # Left border (Pacific)
            dfs(r, cols - 1, atlantic_reachable) # Right border (Atlantic)
            
        for c in range(cols):
            dfs(0, c, pacific_reachable)         # Top border (Pacific)
            dfs(rows - 1, c, atlantic_reachable) # Bottom border (Atlantic)
            
        # Find cells that can reach both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
                    
        return result