class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = w
            
        ROWS, COLS = len(board), len(board[0])
        res = []
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # Avoid duplicates
                
            board[r][c] = '#'  # Mark as visited
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
                    
            board[r][c] = char  # Restore cell state
            
            # Optimization: prune the Trie branch if it becomes empty
            if not next_node.children:
                del node.children[char]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return res