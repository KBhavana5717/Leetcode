class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        import math
        
        m = len(img)
        n = len(img[0])
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total_sum = 0
                count = 0
                
                # Check all 9 cells in the 3x3 neighborhood
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if 0 <= r < m and 0 <= c < n:
                            total_sum += img[r][c]
                            count += 1
                            
                res[i][j] = math.floor(total_sum / count)
                
        return res