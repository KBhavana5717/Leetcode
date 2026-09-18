import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
            
        max_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            curr_max = 0
            
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                # Handle duplicate points
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue
                    
                dx = x2 - x1
                dy = y2 - y1
                
                # Reduce the fraction using GCD
                gcd = math.gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                
                # Standardize signs to ensure unique representation for slopes
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy) # Handle vertical lines
                elif dy == 0:
                    dx = abs(dx) # Handle horizontal lines
                    
                slopes[(dx, dy)] += 1
                curr_max = max(curr_max, slopes[(dx, dy)])
                
            # Total points on the line = points with same slope + the anchor point + duplicates
            max_points = max(max_points, curr_max + duplicates + 1)
            
        return max_points