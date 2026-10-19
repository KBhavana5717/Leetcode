class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}
        
        for i in range(len(graph)):
            if i not in color:
                queue = [i]
                color[i] = 0
                
                while queue:
                    node = queue.pop(0)
                    for neighbor in graph[node]:
                        if neighbor in color:
                            if color[neighbor] == color[node]:
                                return False
                        else:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                            
        return True