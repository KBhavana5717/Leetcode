class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        if not rectangles:
            return False
            
        # Track the large bounding box coordinates
        min_x = min(r[0] for r in rectangles)
        min_y = min(r[1] for r in rectangles)
        max_x = max(r[2] for r in rectangles)
        max_y = max(r[3] for r in rectangles)
        
        total_area = 0
        corners = set()
        
        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)
            
            # The 4 corners of each small rectangle
            p1, p2, p3, p4 = (x1, y1), (x1, y2), (x2, y1), (x2, y2)
            
            # Toggle points in the set (add if not present, remove if already present)
            for p in (p1, p2, p3, p4):
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
                    
        # Exactly 4 corners must remain, and they must match the bounding box corners
        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }
        
        if corners != expected_corners:
            return False
            
        # Total area must match the bounding box area
        return total_area == (max_x - min_x) * (max_y - min_y)