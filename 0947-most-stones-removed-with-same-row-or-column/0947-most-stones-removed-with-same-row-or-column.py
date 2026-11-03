class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        parent = {}

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for x, y in stones:
            # To avoid collision between row x and col y, we offset col indices (e.g., y + 10001)
            r = x
            c = y + 10001
            if r not in parent:
                parent[r] = r
            if c not in parent:
                parent[c] = c
            union(r, c)

        unique_roots = set(find(x) for x in parent)
        return len(stones) - len(unique_roots)