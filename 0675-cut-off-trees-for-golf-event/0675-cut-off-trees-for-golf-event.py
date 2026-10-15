from collections import deque

class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = []
        
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
                    
        trees.sort()
        
        def bfs(start_r, start_c, target_r, target_c):
            if start_r == target_r and start_c == target_c:
                return 0
            
            queue = deque([(start_r, start_c, 0)])
            visited = {(start_r, start_c)}
            
            while queue:
                r, c, steps = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] != 0 and (nr, nc) not in visited:
                        if nr == target_r and nc == target_c:
                            return steps + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
            return -1

        curr_r, curr_c = 0, 0
        total_steps = 0
        
        for _, tr, tc in trees:
            steps = bfs(curr_r, curr_c, tr, tc)
            if steps == -1:
                return -1
            total_steps += steps
            curr_r, curr_c = tr, tc
            
        return total_steps