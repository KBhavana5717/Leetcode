from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        
        for row in wall:
            current_pos = 0
            # We don't include the last brick's end edge because drawing a line 
            # along the very right edge of the wall crosses 0 bricks, but doesn't cross any gaps.
            for brick in row[:-1]:
                current_pos += brick
                edge_counts[current_pos] += 1
                
        # The minimum number of crossed bricks is total rows minus the maximum frequency of shared edges.
        max_edges = max(edge_counts.values(), default=0)
        return len(wall) - max_edges