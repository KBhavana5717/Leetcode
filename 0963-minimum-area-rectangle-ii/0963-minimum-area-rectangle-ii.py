class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        point_set = set((x, y) for x, y in points)
        n = len(points)
        min_area = float('inf')
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x3, y3 = points[k]
                    
                    # Check if (p1, p2, p3) forms a right angle at p2
                    # Vector P2P1 = (x1 - x2, y1 - y2)
                    # Vector P2P3 = (x3 - x2, y3 - y2)
                    if (x1 - x2) * (x3 - x2) + (y1 - y2) * (y3 - y2) == 0:
                        # Find the fourth point p4 = p1 + p3 - p2
                        x4 = x1 + x3 - x2
                        y4 = y1 + y3 - y2
                        
                        if (x4, y4) in point_set:
                            # Calculate area
                            area = ((x1 - x2)**2 + (y1 - y2)**2)**0.5 * ((x3 - x2)**2 + (y3 - y2)**2)**0.5
                            min_area = min(min_area, area)
                            
        return min_area if min_area != float('inf') else 0.0