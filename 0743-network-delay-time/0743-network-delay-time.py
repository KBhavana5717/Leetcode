import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        min_heap = [(0, k)]
        distances = {}
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if node in distances:
                continue
            distances[node] = time
            
            for neighbor, weight in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        if len(distances) != n:
            return -1
        return max(distances.values())