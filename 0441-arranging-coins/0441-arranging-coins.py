class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            # Total coins needed for 'mid' complete rows is given by k * (k + 1) / 2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed <= n:
                res = mid          # Mid is a valid number of complete rows
                left = mid + 1     # Try to find a larger number of rows
            else:
                right = mid - 1    # Too many coins needed, try fewer rows
                
        return res