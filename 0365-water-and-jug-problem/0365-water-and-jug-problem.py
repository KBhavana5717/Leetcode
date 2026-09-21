import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # If the target is greater than the combined capacity, it's impossible
        if x + y < target:
            return False
        
        # If either jug capacity is 0, target must equal the other jug or 0
        if x == 0 or y == 0:
            return target == 0 or target == x or target == y
            
        # Bézout's identity check: target must be a multiple of gcd(x, y)
        return target % math.gcd(x, y) == 0