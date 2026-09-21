class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If the current interval starts before the previous one ends, it's an overlap
            if intervals[i][0] < prev_end:
                removals += 1
            else:
                # No overlap, update the end time
                prev_end = intervals[i][1]
                
        return removals