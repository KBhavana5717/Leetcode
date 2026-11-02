from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        
        def get_coordinates(s: int) -> tuple[int, int]:
            quot = (s - 1) // n
            rem = (s - 1) % n
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        queue = deque([(1, 0)])
        visited = {1}
        
        while queue:
            curr, moves = queue.popleft()
            
            if curr == n * n:
                return moves
                
            for next_sq in range(curr + 1, min(curr + 6, n * n) + 1):
                r, c = get_coordinates(next_sq)
                destination = board[r][c] if board[r][c] != -1 else next_sq
                
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))
                    
        return -1