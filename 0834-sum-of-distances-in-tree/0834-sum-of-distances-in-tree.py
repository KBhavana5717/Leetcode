class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        count = [1] * n
        ans = [0] * n
        
        def dfs(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    count[node] += count[neighbor]
                    ans[0] += ans[neighbor] + count[neighbor]
                    
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    ans[neighbor] = ans[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor, node)
                    
        dfs(0, -1)
        dfs2(0, -1)
        return ans