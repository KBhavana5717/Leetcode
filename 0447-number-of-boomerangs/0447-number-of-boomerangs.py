from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        boomerangs = 0
        
        for p1 in points:
            distance_count = defaultdict(int)
            for p2 in points:
                if p1 == p2:
                    continue
                # Calculate squared Euclidean distance to avoid floating-point inaccuracies
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                dist = dx * dx + dy * dy
                
                distance_count[dist] += 1
                
            # For each unique distance, if we have 'count' points, 
            # we can choose any 2 distinct points for (j, k) in count * (count - 1) ways
            for dist, count in distance_count.items():
                boomerangs += count * (count - 1)
                
        return boomerangs