from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        q = deque()
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append((r, c, 0))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc)

        # Find the first island and add all its cells to the queue via DFS
        found = False
        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        # Perform BFS to find the shortest bridge to the second island
        while q:
            r, c, dist = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    if grid[nr][nc] == 1:
                        return dist
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))
        
        return 0