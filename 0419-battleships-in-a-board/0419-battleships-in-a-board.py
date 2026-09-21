class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        rows, cols = len(board), len(board[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                # If the current cell is empty, skip it
                if board[r][c] == '.':
                    continue
                
                # If there is an 'X' to the left, this cell is part of a horizontal battleship already counted
                if r > 0 and board[r - 1][c] == 'X':
                    continue
                
                # If there is an 'X' above, this cell is part of a vertical battleship already counted
                if c > 0 and board[r][c - 1] == 'X':
                    continue
                
                # Otherwise, this is the top-left starting cell of a new battleship
                count += 1
                
        return count