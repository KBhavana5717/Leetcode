class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = {}

        def find(i):
            if parent.setdefault(i, i) != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for r in range(n):
            for c in range(n):
                # Each 1x1 cell is divided into 4 triangles: 0: top, 1: right, 2: bottom, 3: left
                root = 4 * (r * n + c)
                val = grid[r][c]
                
                if val != '\\':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                if val != '/':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)

                # Connect with neighboring cells
                # Right neighbor
                if c + 1 < n:
                    union(root + 1, 4 * (r * n + (c + 1)) + 3)
                # Bottom neighbor
                if r + 1 < n:
                    union(root + 2, 4 * ((r + 1) * n + c) + 0)

        unique_roots = set(find(x) for x in parent)
        return len(unique_roots)