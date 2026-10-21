from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        n = len(s1)
        queue = deque([(s1, 0)])
        seen = {s1}

        while queue:
            cur, steps = queue.popleft()

            # first position where cur differs from s2
            i = 0
            while cur[i] == s2[i]:
                i += 1

            # swap in a letter that belongs at position i
            for j in range(i + 1, n):
                # cur[j] must be the letter we need, and must not already be correct at j
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    nxt = list(cur)
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    nxt = "".join(nxt)

                    if nxt == s2:
                        return steps + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, steps + 1))

        return -1