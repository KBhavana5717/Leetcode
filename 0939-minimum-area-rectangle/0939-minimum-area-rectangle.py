class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        point_set = set(tuple(p) for p in points)
        min_area = float('inf')
        
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # Check if they form a diagonal of a non-zero area rectangle
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(min_area, area)
                        
        return min_area if min_area != float('inf') else 0