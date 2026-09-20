class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix by shifting right until left == right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Shift back to the left by the number of shifts we performed
        return left << shift