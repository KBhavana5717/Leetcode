import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        lcm = math.lcm(a, b)
        
        left, right = 1, n * min(a, b)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            count = (mid // a) + (mid // b) - (mid // lcm)
            
            if count >= n:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans % MOD