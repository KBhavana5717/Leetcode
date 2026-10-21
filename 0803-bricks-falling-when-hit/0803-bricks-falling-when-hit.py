class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        
        # Mark whether there's initially a brick at hit locations, and remove them
        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 2  # 2 means it was removed by a hit
            else:
                grid[r][c] = 3  # 3 means it was an empty space when hit
                
        parent = list(range(m * n + 1))
        size = [1] * (m * n + 1)
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, root):
            root_i, root_root = find(i), find(root)
            if root_i != root_root:
                parent[root_i] = root_root
                size[root_root] += size[root_i]
                
        def get_index(r, c):
            return r * n + c
            
        # Initialize DSU with all stable bricks remaining after all hits
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    idx = get_index(r, c)
                    if r == 0:
                        union(idx, m * n)
                    if r > 0 and grid[r - 1][c] == 1:
                        union(idx, get_index(r - 1, c))
                    if c > 0 and grid[r][c - 1] == 1:
                        union(idx, get_index(r, c - 1))
                        
        res = [0] * len(hits)
        
        # Process hits in reverse order
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 3:
                continue
            
            grid[r][c] = 1
            idx = get_index(r, c)
            prev_roof_size = size[find(m * n)]
            
            if r == 0:
                union(idx, m * n)
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    union(idx, get_index(nr, nc))
                    
            new_roof_size = size[find(m * n)]
            dropped = max(0, new_roof_size - prev_roof_size - 1)
            res[i] = dropped
            
        return res