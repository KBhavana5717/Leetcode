class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Area of rectangle A
        area_a = (ax2 - ax1) * (ay2 - ay1)
        # Area of rectangle B
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Calculate overlap width and height
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        
        # Area of overlap
        overlap_area = overlap_width * overlap_height
        
        # Total area = Area A + Area B - Overlap Area
        return area_a + area_b - overlap_area