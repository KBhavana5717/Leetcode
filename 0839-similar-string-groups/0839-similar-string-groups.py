class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        strs = list(set(strs))
        n = len(strs)
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        def is_similar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2
            
        groups = n
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    if union(i, j):
                        groups -= 1
                        
        return groups