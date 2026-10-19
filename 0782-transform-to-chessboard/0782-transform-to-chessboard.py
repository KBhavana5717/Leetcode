class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)
        
        # Check if the board is valid chessboard
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1
                    
        sum_row = sum(board[0])
        sum_col = sum(board[i][0] for i in range(n))
        
        if not (n // 2 <= sum_row <= (n + 1) // 2):
            return -1
        if not (n // 2 <= sum_col <= (n + 1) // 2):
            return -1
            
        row_swaps = 0
        col_swaps = 0
        
        for i in range(n):
            row_swaps += board[i][0] == i % 2
            col_swaps += board[0][i] == i % 2
            
        if n % 2 == 1:
            if row_swaps % 2 == 1:
                row_swaps = n - row_swaps
            if col_swaps % 2 == 1:
                col_swaps = n - col_swaps
        else:
            row_swaps = min(row_swaps, n - row_swaps)
            col_swaps = min(col_swaps, n - col_swaps)
            
        return (row_swaps + col_swaps) // 2