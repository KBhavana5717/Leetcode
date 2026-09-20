import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # Collect all events: (x, -height, right) for start, (x, height, 0) for end
        # To handle overlapping correctly:
        # 1. At the same x, start events (negative height) should come before end events.
        # 2. If multiple start events share x, taller buildings (more negative) come first.
        # 3. If multiple end events share x, smaller x2 comes first (handled naturally or via sorting).
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, height, 0))
            
        events.sort(key=lambda x: (x[0], x[1]))
        
        result = []
        # Max-heap to store active heights, initialized with ground level (height 0) and a dummy right coordinate infinity
        # We store tuples of (negative_height, right_coordinate)
        live_buildings = [(0, float('inf'))]
        
        for x, neg_h, right in events:
            # Remove buildings that have already ended before or at current x
            while x >= live_buildings[0][1]:
                heapq.heappop(live_buildings)
                
            if neg_h < 0:
                # It's a start event, add to heap
                heapq.heappush(live_buildings, (neg_h, right))
                
            # Current maximum height in the skyline
            current_max = -live_buildings[0][0]
            
            # If the result is empty or the max height changed, record the key point
            if not result or result[-1][1] != current_max:
                result.append([x, current_max])
                
        return result