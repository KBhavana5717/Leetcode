import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap for the smaller half (stored as negative numbers)
        self.small = []
        # Min-heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap and balance with min-heap
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 2: Maintain size property (small can have at most 1 extra element)
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If sizes are equal, average the roots of both heaps
        return (-self.small[0] + self.large[0]) / 2.0