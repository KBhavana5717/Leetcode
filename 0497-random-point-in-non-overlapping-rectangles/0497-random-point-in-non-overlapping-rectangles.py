import random
import bisect

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.prefix_sums = []
        total_points = 0
        
        for a, b, x, y in rects:
            # Number of integer points in a rectangle is (width + 1) * (height + 1)
            points = (x - a + 1) * (y - b + 1)
            total_points += points
            self.prefix_sums.append(total_points)
            
        self.total_points = total_points

    def pick(self) -> list[int]:
        # Choose a random point index from 0 to total_points - 1
        target = random.randint(0, self.total_points - 1)
        
        # Use binary search to find which rectangle this point belongs to
        rect_index = bisect.bisect_right(self.prefix_sums, target)
        
        # Adjust target relative to the chosen rectangle's starting offset
        if rect_index > 0:
            target -= self.prefix_sums[rect_index - 1]
            
        a, b, x, y = self.rects[rect_index]
        width = x - a + 1
        
        # Calculate the 2D coordinates from the 1D target index
        dx = target % width
        dy = target // width
        
        return [a + dx, b + dy]