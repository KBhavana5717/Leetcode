import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        # Sort courses by their last day (deadline)
        courses.sort(key=lambda x: x[1])
        
        time = 0
        max_heap = []
        
        for duration, lastDay in courses:
            time += duration
            heapq.heappush(max_heap, -duration)
            
            # If the total time exceeds the deadline of the current course,
            # drop the course that takes the longest time so far.
            if time > lastDay:
                time += heapq.heappop(max_heap) # Adds a negative number, effectively subtracting
                
        return len(max_heap)