class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        from collections import defaultdict, deque
        
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
                
        visited_routes = [False] * len(routes)
        visited_stops = {source}
        queue = deque([(source, 0)])
        
        while queue:
            stop, buses = queue.popleft()
            
            if stop == target:
                return buses
                
            for r in stop_to_routes[stop]:
                if not visited_routes[r]:
                    visited_routes[r] = True
                    for next_stop in routes[r]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses + 1))
                            
        return -1