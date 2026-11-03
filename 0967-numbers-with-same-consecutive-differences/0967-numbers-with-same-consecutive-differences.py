class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        current = {d for d in range(1, 10)}
        
        for _ in range(n - 1):
            next_current = set()
            for num in current:
                last_digit = num % 10
                if last_digit + k <= 9:
                    next_current.add(num * 10 + last_digit + k)
                if last_digit - k >= 0:
                    next_current.add(num * 10 + last_digit - k)
            current = next_current
            
        return list(current)