class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2
        
        def dfs(r, c, id):
            stack = [(r, c)]
            grid[r][c] = id
            size = 0
            while stack:
                curr_r, curr_c = stack.pop()
                size += 1
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = id
                        stack.append((nr, nc))
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1
                    
        max_size = max(island_sizes.values(), default=0)
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    current_size = 1 + sum(island_sizes[id] for id in seen)
                    max_size = max(max_size, current_size)
                    
        return max_size if max_size != 0 else 1