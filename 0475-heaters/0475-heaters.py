import bisect

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        min_radius = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the heater on the right (if it exists)
            dist_right = heaters[idx] - house if idx < len(heaters) else float('inf')
            
            # Distance to the heater on the left (if it exists)
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # Find the closest heater distance for the current house
            closest_dist = min(dist_left, dist_right)
            
            # The radius must cover the most restrictive house
            min_radius = max(min_radius, closest_dist)
            
        return min_radius