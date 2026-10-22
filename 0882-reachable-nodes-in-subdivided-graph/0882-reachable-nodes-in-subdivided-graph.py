import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt
            
        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist.get(u, float('inf')):
                continue
                
            for v, cnt in graph[u].items():
                # Moves needed to reach node v through this edge
                move_cost = cnt + 1
                if dist.get(u, float('inf')) + move_cost < dist.get(v, float('inf')) and dist.get(u, float('inf')) + move_cost <= maxMoves:
                    dist[v] = dist[u] + move_cost
                    heapq.heappush(pq, (dist[v], v))
                    
        ans = 0
        for u in dist:
            if dist[u] <= maxMoves:
                ans += 1
                
        for u, v, cnt in edges:
            u_reach = max(0, maxMoves - dist.get(u, float('inf')))
            v_reach = max(0, maxMoves - dist.get(v, float('inf')))
            ans += min(cnt, u_reach + v_reach)
            
        return ans