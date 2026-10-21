from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        
        all_keys = 0
        start_r, start_c = -1, -1
        
        for r in range(R):
            for c in range(C):
                cell = grid[r][c]
                if cell == '@':
                    start_r, start_c = r, c
                elif 'a' <= cell <= 'f':
                    all_keys |= (1 << (ord(cell) - ord('a')))
                    
        # State: (r, c, current_keys)
        queue.append((start_r, start_c, 0, 0))
        visited.add((start_r, start_c, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, keys, dist = queue.popleft()
            
            if keys == all_keys:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C:
                    cell = grid[nr][nc]
                    
                    if cell == '#':
                        continue
                        
                    # Check if it's a lock and we don't have the key
                    if 'A' <= cell <= 'F':
                        if not (keys & (1 << (ord(cell) - ord('A')))):
                            continue
                            
                    new_keys = keys
                    if 'a' <= cell <= 'f':
                        new_keys |= (1 << (ord(cell) - ord('a')))
                        
                    if (nr, nc, new_keys) not in visited:
                        visited.add((nr, nc, new_keys))
                        queue.append((nr, nc, new_keys, dist + 1))
                        
        return -1