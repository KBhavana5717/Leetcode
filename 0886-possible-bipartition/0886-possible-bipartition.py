class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        from collections import defaultdict, deque
        
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
            
        color = {}
        
        for i in range(1, n + 1):
            if i not in color:
                color[i] = 0
                queue = deque([i])
                
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if neighbor in color:
                            if color[neighbor] == color[node]:
                                return False
                        else:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                            
        return True