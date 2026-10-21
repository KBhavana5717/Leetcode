class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        state = [0] * n  # 0: unvisited, 1: visiting, 2: safe
        
        def dfs(node: int) -> bool:
            if state[node] > 0:
                return state[node] == 2
            
            state[node] = 1
            for neighbor in graph[node]:
                if state[neighbor] == 1 or not dfs(neighbor):
                    return False
            
            state[node] = 2
            return True
            
        return [i for i in range(n) if dfs(i)]