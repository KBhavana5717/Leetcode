import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # sort by wage/quality ratio, lowest first
        workers = sorted(zip(quality, wage), key=lambda w: w[1] / w[0])

        heap = []            # max-heap of qualities (stored negated)
        total_quality = 0
        best = float('inf')

        for q, w in workers:
            ratio = w / q                    # highest ratio so far, so everyone is paid at this rate
            heapq.heappush(heap, -q)
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)   # removes the largest quality (negated)

            if len(heap) == k:
                best = min(best, total_quality * ratio)

        return best