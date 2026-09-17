class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int, i: int) -> bool:
            # If all characters are matched
            if i == len(word):
                return True
            
            # Check bounds, character match, and whether it's already visited
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[i]):
                return False
            
            # Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 adjacent directions (down, up, right, left)
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))
            
            # Backtrack: restore the original cell value
            board[r][c] = temp
            return found

        # Iterate through every cell to find a starting point
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False