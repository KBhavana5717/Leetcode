class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if image[r][c] == original_color:
                image[r][c] = color
                if r > 0:
                    dfs(r - 1, c)
                if r < rows - 1:
                    dfs(r + 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if c < cols - 1:
                    dfs(r, c + 1)
                    
        dfs(sr, sc)
        return image