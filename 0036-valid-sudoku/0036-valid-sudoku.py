class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnmap = defaultdict(set)
        rowmap = defaultdict(set)
        squaremap = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowmap[row]
                or board[row][col] in columnmap[col]
                or board[row][col] in squaremap[(row//3, col//3)]):
                    return False
                rowmap[row].add(board[row][col])
                columnmap[col].add(board[row][col])
                squaremap[(row//3, col//3)].add(board[row][col])
        return True