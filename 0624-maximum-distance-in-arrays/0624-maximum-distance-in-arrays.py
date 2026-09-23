class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        res = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            # Calculate the distance with the current array's max and previous min, 
            # and current array's min and previous max
            res = max(res, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            
            # Update the global min and max with the current array's extremes
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
            
        return res