class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos: int, visited: int) -> int:
            if pos > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                # Check if num is not visited and satisfies the divisibility condition
                if not (visited & (1 << num)) and (num % pos == 0 or pos % num == 0):
                    count += backtrack(pos + 1, visited | (1 << num))
                    
            return count

        return backtrack(1, 0)