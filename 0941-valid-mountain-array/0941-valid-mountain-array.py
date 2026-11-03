class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        # Walk up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
            
        # Peak can't be the first or the last element
        if i == 0 or i == n - 1:
            return False
            
        # Walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
            
        return i == n - 1