import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
            
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # Add all boundary cells to the min-heap and mark them as visited
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
                    
        water_trapped = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while min_heap:
            height, r, c = heapq.heappop(min_heap)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # If the neighbor's height is less than the current boundary height, it traps water
                    water_trapped += max(0, height - heightMap[nr][nc])
                    # Push the new boundary height into the heap (taking the max to form the limiting wall)
                    heapq.heappush(min_heap, (max(height, heightMap[nr][nc]), nr, nc))
                    
        return water_trapped