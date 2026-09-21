class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        curr = 1
        
        for _ in range(n):
            res.append(curr)
            
            # Try to go deeper into the decimal tree (e.g., 1 -> 10)
            if curr * 10 <= n:
                curr *= 10
            else:
                # If we can't go deeper or we've reached the upper bound, backtrack/increment
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1
                
        return res