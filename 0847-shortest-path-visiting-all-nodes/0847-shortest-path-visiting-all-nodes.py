from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        full = (1 << n) - 1

        # Start from every node at once (multi-source BFS)
        queue = deque((i, 1 << i) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}

        steps = 0
        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()

                for nei in graph[node]:
                    new_mask = mask | (1 << nei)

                    if new_mask == full:
                        return steps + 1

                    if (nei, new_mask) not in seen:
                        seen.add((nei, new_mask))
                        queue.append((nei, new_mask))
            steps += 1

        return -1