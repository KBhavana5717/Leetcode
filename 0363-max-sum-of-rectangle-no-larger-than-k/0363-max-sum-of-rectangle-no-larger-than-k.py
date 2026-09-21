from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        # Iterate over all possible left columns
        for left in range(cols):
            # Initialize row sums for the current left-to-right column range
            row_sums = [0] * rows
            
            for right in range(left, cols):
                # Update row sums by adding elements of the current column
                for r in range(rows):
                    row_sums[r] += matrix[r][right]
                
                # Find the max subarray sum no larger than k using prefix sums and binary search
                current_sum = 0
                prefix_sums = [0]
                
                for val in row_sums:
                    current_sum += val
                    # We need current_sum - prev_sum <= k => prev_sum >= current_sum - k
                    target = current_sum - k
                    idx = bisect_left(prefix_sums, target)
                    
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, current_sum - prefix_sums[idx])
                    
                    insort(prefix_sums, current_sum)
                    
                    # Optimization: if we already found k, we can return early
                    if max_sum == k:
                        return k
                        
        return max_sum