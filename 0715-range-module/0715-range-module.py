class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)
        
        # Add all intervals that end before the new range starts
        while i < n and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1
            
        # Merge all overlapping or adjacent intervals with the new range
        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1
            
        new_intervals.append([left, right])
        
        # Add the remaining intervals
        while i < n:
            new_intervals.append(self.intervals[i])
            i += 1
            
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        # Find the interval that could potentially cover [left, right]
        idx = bisect.bisect_right(self.intervals, [left, float('inf')]) - 1
        if idx >= 0 and self.intervals[idx][0] <= left and self.intervals[idx][1] >= right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        for interval in self.intervals:
            # If the current interval is completely to the left or right of the removed range, keep it as is
            if interval[1] <= left or interval[0] >= right:
                new_intervals.append(interval)
            else:
                # If there is an overlap, split or trim the interval
                if interval[0] < left:
                    new_intervals.append([interval[0], left])
                if interval[1] > right:
                    new_intervals.append([right, interval[1]])
                    
        self.intervals = new_intervals