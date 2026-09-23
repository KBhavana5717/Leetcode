class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        
        for i in range(length):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the left neighbor is empty or out of bounds (start of array)
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right neighbor is empty or out of bounds (end of array)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                # If both neighbors are empty, we can plant a flower here
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    
            # If we've already placed enough flowers, we can return True early
            if n <= 0:
                return True
                
        return n <= 0