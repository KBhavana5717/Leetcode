import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Combine capital and profits into a list of tuples and sort by capital required
        projects = sorted(zip(capital, profits))
        
        max_profit_heap = []
        i = 0
        n = len(projects)
        
        for _ in range(k):
            # Push all affordable projects into the max-heap based on their profits
            while i < n and projects[i][0] <= w:
                # We store negative profit because Python's heapq is a min-heap
                heapq.heappush(max_profit_heap, -projects[i][1])
                i += 1
                
            # If no affordable projects are available, break out of the loop
            if not max_profit_heap:
                break
                
            # Pick the project with the maximum profit
            w += -heapq.heappop(max_profit_heap)
            
        return w