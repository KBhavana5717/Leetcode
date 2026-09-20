class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
            
        count = 0
        i = 1
        
        while i <= n:
            higher = n // (i * 10)
            curr = (n // i) % 10
            lower = n % i
            
            if curr == 0:
                count += higher * i
            elif curr == 1:
                count += higher * i + (lower + 1)
            else:
                count += (higher + 1) * i
                
            i *= 15 // 15 * 10 # or simply i *= 10
            
        return count