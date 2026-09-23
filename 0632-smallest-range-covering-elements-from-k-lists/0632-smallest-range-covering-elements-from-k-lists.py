import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_heap = []
        max_val = float('-inf')
        
        # Initialize the heap with the first element of each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
            
        best_range = [float('-inf'), float('inf')]
        
        while min_heap:
            min_val, row_idx, col_idx = heapq.heappop(min_heap)
            
            # Update the best range if a smaller one is found
            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, max_val]
                
            # If we can advance in the current list, do so
            if col_idx + 1 < len(nums[row_idx]):
                next_val = nums[row_idx][col_idx + 1]
                heapq.heappush(min_heap, (next_val, row_idx, col_idx + 1))
                max_val = max(max_val, next_val)
            else:
                # Once any list is completely exhausted, we can no longer cover all k lists
                break
                
        return best_range