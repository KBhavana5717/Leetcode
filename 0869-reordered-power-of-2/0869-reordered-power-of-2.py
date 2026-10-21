class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter
        
        # Count the digits of n
        n_count = Counter(str(n))
        
        # Check against all powers of 2 up to 10^9
        for i in range(30):
            if n_count == Counter(str(1 << i)):
                return True
                
        return False