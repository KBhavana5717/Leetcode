class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0
        
        for i in range(rows):
            for j in range(cols):
                temp = dp[j + 1]
                if matrix[i][j] == '1':
                    dp[j + 1] = min(dp[j], dp[j + 1], prev) + 1
                    max_side = max(max_side, dp[j + 1])
                else:
                    dp[j + 1] = 0
                prev = temp
                
        return max_side * max_side