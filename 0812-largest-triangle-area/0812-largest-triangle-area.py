class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        import itertools
        
        max_area = 0.0
        for p1, p2, p3 in itertools.combinations(points, 3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            if area > max_area:
                max_area = area
                
        return max_area