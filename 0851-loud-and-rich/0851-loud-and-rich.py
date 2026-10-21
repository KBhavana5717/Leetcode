from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)

        # richer_than[b] = everyone who definitely has more money than b
        richer_than = defaultdict(list)
        for a, b in richer:
            richer_than[b].append(a)

        answer = [-1] * n

        def dfs(x):
            if answer[x] != -1:
                return answer[x]

            best = x                              # x is richer-or-equal to itself
            for y in richer_than[x]:
                candidate = dfs(y)                # quietest among everyone >= y
                if quiet[candidate] < quiet[best]:
                    best = candidate

            answer[x] = best
            return best

        for i in range(n):
            dfs(i)

        return answer