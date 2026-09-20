class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for r in range(m):
            for c in range(n):
                live_count = 0
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) in (1, 2):
                        live_count += 1
                
                # Apply Game of Life rules
                if board[r][c] == 1 and (live_count < 2 or live_count > 3):
                    board[r][c] = 2  # Live becomes dead
                elif board[r][c] == 0 and live_count == 3:
                    board[r][c] = 3  # Dead becomes live
                    
        # Update board to final state
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1