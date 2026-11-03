class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
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

        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    union(x, d)
                    union(x, x // d)
                d += 1

        from collections import Counter
        count = Counter(find(x) for x in nums)
        return max(count.values())