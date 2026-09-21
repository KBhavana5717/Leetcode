import bisect

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        # Store start times with their original indices and sort them
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        start_keys = [start[0] for start in starts]
        
        result = []
        for interval in intervals:
            end_val = interval[1]
            # Use binary search to find the smallest start >= end_val
            idx = bisect.bisect_left(start_keys, end_val)
            
            if idx < n:
                result.append(starts[idx][1])
            else:
                result.append(-1)
                
        return result