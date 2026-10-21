import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap = []          # fuel amounts of stations we've passed (negated for max-heap)
        fuel = startFuel       # how far we can currently reach
        stops = 0
        i = 0
        n = len(stations)

        while fuel < target:
            # Collect every station we can reach with current fuel
            while i < n and stations[i][0] <= fuel:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1

            # No station to refuel from, so we're stuck
            if not max_heap:
                return -1

            # Refuel at the best station we passed
            fuel += -heapq.heappop(max_heap)
            stops += 1

        return stops