from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        
        # Rule 1: If a mine 'M' is revealed, change it to 'X' and game over.
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
            
        rows, cols = len(board), len(board[0])
        
        def dfs(row: int, col: int):
            # Count adjacent mines
            mine_count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                        mine_count += 1
            
            # Rule 3: If an empty square 'E' has at least one adjacent mine, change it to a digit ('1' to '8').
            if mine_count > 0:
                board[row][col] = str(mine_count)
            else:
                # Rule 2: If an empty square 'E' with no adjacent mines is revealed, change it to 'B' 
                # and reveal all adjacent unrevealed squares recursively.
                board[row][col] = 'B'
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'E':
                            dfs(nr, nc)

        dfs(r, c)
        return board