from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
                
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                curr, current_prod = queue.popleft()
                
                if curr == end:
                    return current_prod
                    
                for neighbor, weight in graph[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_prod * weight))
                        
            return -1.0

        # Evaluate each query
        results = []
        for c, d in queries:
            results.append(bfs(c, d))
            
        return results