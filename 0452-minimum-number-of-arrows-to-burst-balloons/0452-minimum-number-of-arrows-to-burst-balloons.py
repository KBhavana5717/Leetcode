class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        
        # Sort the balloons based on their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        # Shoot the first arrow at the end of the first balloon
        arrow_pos = points[0][1]
        
        for i in range(1, len(points)):
            # If the current balloon starts after the current arrow position, 
            # we need a new arrow
            if points[i][0] > arrow_pos:
                arrows += 1
                arrow_pos = points[i][1]
                
        return arrows