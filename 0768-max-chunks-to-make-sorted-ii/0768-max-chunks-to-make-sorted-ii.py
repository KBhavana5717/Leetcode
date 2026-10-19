class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        max_of_left = [0] * n
        min_of_right = [0] * n
        
        curr_max = -inf
        for i in range(n):
            curr_max = max(curr_max, arr[i])
            max_of_left[i] = curr_max
            
        curr_min = inf
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, arr[i])
            min_of_right[i] = curr_min
            
        chunks = 0
        for i in range(n - 1):
            if max_of_left[i] <= min_of_right[i + 1]:
                chunks += 1
                
        return chunks + 1