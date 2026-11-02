class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        s_n = str(n)
        k = len(s_n)
        d_len = len(digits)
        
        # Count all numbers with fewer digits than n
        count = sum(d_len ** i for i in range(1, k))
        
        # Count numbers with the same number of digits as n
        for i, ch in enumerate(s_n):
            prefix_matched = False
            for d in digits:
                if d < ch:
                    count += d_len ** (k - 1 - i)
                elif d == ch:
                    prefix_matched = True
                    break
                else:
                    break
            if not prefix_matched:
                return count
                
        # If n itself can be formed completely
        return count + 1