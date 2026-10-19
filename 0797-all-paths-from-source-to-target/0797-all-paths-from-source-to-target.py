class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        res = []
        
        def dfs(curr, path):
            if curr == target:
                res.append(list(path))
                return
            
            for neighbor in graph[curr]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
                
        dfs(0, [0])
        return res