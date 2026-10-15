class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = {}
        cand1, cand2 = None, None
        
        for u, v in edges:
            if v in parent:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break
            parent[v] = u
            
        def find(i, uf):
            if uf[i] == i:
                return i
            uf[i] = find(uf[i], uf)
            return uf[i]
            
        uf = list(range(n + 1))
        
        for u, v in edges:
            if [u, v] == cand2:
                continue
            root_u = find(u, uf)
            root_v = find(v, uf)
            if root_u == root_v:
                if cand1:
                    return cand1
                return [u, v]
            uf[root_v] = root_u
            
        return cand2